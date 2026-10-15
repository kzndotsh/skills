# Applications (pages/applications/*.en.mdx + applications.en.mdx)

Source: dair-ai/Prompt-Engineering-Guide, section "LLM Applications & Guides" (`pages/applications.en.mdx` is only a card index rendered by `<ContentFileNames section="applications">` from `pages/applications/_meta.en.json`).

## Contents
1. Function calling (OpenAI tools API)
2. Generating data (few-shot synthetic exemplars)
3. Synthetic data for RAG / retrievers (Promptgator, Dai et al. 2022)
4. Dataset diversity: random-seed prompts, hierarchical generation, "textbook" data (Eldan 2023, Gunasekar 2023)
5. Code generation (comments to code, completion, SQL, explain)
6. Graduate job classification case study (Clavie et al. 2023)
7. Prompt functions (pf)
8. Context caching with Gemini 1.5 Flash
9. Fine-tuning GPT-4o / mini
10. Audit notes

Order in nav (`_meta.en.json`): finetuning-gpt4o, function_calling, context-caching, generating, synthetic_rag, generating_textbooks, coding, workplace_casestudy, pf.

---

## 1. Function calling (`function_calling.en.mdx`)
**What:** The model is fine-tuned to decide when an external function is needed and emits JSON arguments for it. It does NOT execute anything; your code runs the function and feeds the result back. Multiple tools can be declared per request.
**Use for:** tool-using chatbots/agents (weather, search, DB), structured extraction/tagging (NER, sentiment, keywords), natural language to API call or DB query, knowledge-base retrieval engines, math via custom functions.
**Not for:** when you only need a one-shot formatted answer (plain JSON prompting or structured outputs is simpler); open-source function calling is "coming soon" in the repo (no guidance).

Tool schema (OpenAI Chat Completions `tools` format, verbatim from repo):
```python
tools = [{
  "type": "function",
  "function": {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
      "type": "object",
      "properties": {
        "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
      },
      "required": ["location"],
    },
  },
}]
```
Call helper and flow:
```python
def get_completion(messages, model="gpt-3.5-turbo-1106", temperature=0, max_tokens=300, tools=None):
    response = openai.chat.completions.create(model=model, messages=messages,
        temperature=temperature, max_tokens=max_tokens, tools=tools)
    return response.choices[0].message
messages = [{"role": "user", "content": "What is the weather like in London?"}]
response = get_completion(messages, tools=tools)
# response.tool_calls[0].function.arguments == '{"location":"London","unit":"celsius"}'
```
Loop: (1) send messages+tools; (2) parse `tool_calls[i].function.arguments` with `json.loads`; (3) run your function; (4) append the assistant message, then a `{"role":"tool","tool_call_id":..., "name":..., "content": <result string>}` message per call; (5) call the model again to get the final natural-language answer. Full runnable version in `notebooks-and-code-recipes.md`.
**Key points:** descriptions are passed straight to the model and drive when/how it calls (notebook note); `tool_choice` = `"auto"` (default), `"none"`, or `{"type":"function","function":{"name":...}}` to force; parallel calls come back as several entries in `tool_calls`.
**Caveats:** model may not call a tool for greetings (correct behaviour); with `tool_choice="none"` it narrates intent but does nothing; validate args before executing (not in repo).
Source refs listed by repo: Fireworks function-calling model, LangChain tool-use benchmark, Gemini function calling docs, OpenAI function calling docs/cookbook, minimaxir structured data post, svpino math function-calling notebook.

## 2. Generating data (`generating.en.mdx`)
**What:** Use an LLM to produce exemplars/test data. **Template (verbatim):**
```
Produce 10 exemplars for sentiment analysis. Examples are categorized as either positive or negative. Produce 2 negative examples and 8 positive examples. Use this format for the examples:
Q: <sentence>
A: <sentiment>
```
Output was 8 positive + 2 negative one-line Q/A pairs. **Use:** quick eval sets, few-shot exemplar creation for other sections. **Caveat:** samples are generic and low-diversity; see sections 3-4 for diversity.

## 3. Synthetic dataset for RAG (`synthetic_rag.en.mdx`)
**Problem:** retrievers underperform in new languages/domains (example: Czech law, Indian tax assistant) and labeled data is scarce.
**Method (Promptagator, Dai et al. 2022, arXiv 2209.11755):** with a target corpus and about 8 manually labeled (document, query) pairs, prompt a strong LLM to generate a query for each unlabeled document; keep only the last document and generated query as a training pair; train/fine-tune a local retriever (distilling the LLM into a standard encoder).
Template (task = counter-argument retrieval, ArguAna-style; verbatim structure):
```
Task: Identify a counter-argument for the given argument.

Argument #1: {insert passage X1 here}

A concise counter-argument query related to the argument #1: {insert manually prepared query Y1 here}

Argument #2: {insert passage X2 here}
A concise counter-argument query related to the argument #2: {insert manually prepared query Y2 here}

<- paste your examples here ->

Argument N: {new document d}

A concise counter-argument query related to the argument #N:
```
General form: (e_prompt, e_doc(d1), e_query(q1), ..., e_doc(dk), e_query(qk), e_doc(d)).
**Guidance in repo:**
- Different retrieval tasks define "relevance" differently (supporting vs counter-arguments); encode the search intent in the instruction and examples.
- Write about 20 examples, randomly sample 2-8 per prompt for diversity. Examples must be representative, correctly formatted, and show target query length/tone; bad shots hurt the trained retriever.
- A cheaper chat model suffices (works in other languages). Cost estimate: prompt with 4-5 examples about 700 tokens (passages up to 128 tokens), output about 25 tokens; 50,000 docs about 55 USD at GPT-3.5 Turbo 2023 prices (0.0015/0.002 per 1k in/out). Can generate 2-4 queries per doc.
- 50,000 is from the paper: roughly the number of hand-labeled pairs needed to match synthetic-trained quality.
- The paper's per-dataset prompt templates (BeIR) are only shown as an image (not text) in repo.
**Related:** RAG technique page (`pages/techniques/rag.en.mdx`, not in this slice).

## 4. Dataset diversity (`generating_textbooks.en.mdx`)
**Problem:** even at high temperature, LLM-generated datasets are repetitive. Use case: you cannot send data to an external API, so train a local model on synthetic data.
**Technique A, random-seed slots (Eldan & Li 2023, TinyStories, arXiv 2305.07759):** build lists (about 1500 child-level words split into nouns/verbs/adjectives, plus story features such as dialogue, plot twist, bad ending, moral, foreshadowing), randomly sample entities per generation and fill a template. Template (verbatim):
```
Write a short story (3-5 paragraphs) which only uses very simple words that a 3 year old child would likely understand. The story should use the verb "{random.choice(verbs_list)}", the noun "{random.choice(nouns_list)}" and the adjective "{random.choice(adjectives_list)}". The story should have the following features: {random.choice(features_list)}, {random.choice(features_list)}. Remember to only use simple words!
```
Recipe: (1) list parameters that vary across samples; (2) compile value lists; (3) sample randomly, set temperature above default but below max; (4) train the local model on outputs. A class label can be one of the seeded entities (e.g. "positive"/"negative") to get labeled data for a classifier for free.
**Technique B, hierarchical/iterative generation:** first have the LLM generate intermediates (summary, a must-include sentence), then feed them into the final prompt:
```
Summary: {LLM-generated summary}
Features: {copied from initial prompt}
Sentence: {LLM-generated sentence that must appear}
Words: {copied from initial prompt}
Story:
```
Labels are known from the seed prompt (e.g. "contains dialogue / plot twist"), so classifiers can be trained on the output.
**Technique C, "textbook" data (Gunasekar et al. 2023, "Textbooks Are All You Need", Phi-1, arXiv 2306.11644):** high-quality, clear, textbook-like synthetic data; diversity via constraints on topic and target audience (high-schooler vs CS undergrad vs PhD phrase things differently). Phi-1: 1.5B params, about 1B synthetic tokens generated with GPT-3.5, evaluated on HumanEval (Chen et al. 2021). The authors did not publish their prompt; the repo's reconstruction:
```
Write an extract from a Computer Science textbook for a 1st-year bachelor. The coding language is Python 3.6.

This is an extract from the middle of the following topic: Singular matrices.

The extract starts with a high-level overview of the topic. Then, it presents an example and describes the solution in natural language. After that, it provides 1-2 code snippets, following the example. Each snippet has no more than 10 rows. There should be no text after code snippets.

Keep in mind that the extract should be concise and explain only one concept at a time. The code should represent a Python function & its call. All the common ML/DS libraries are available.

Don't be too verbose. The expected length of the extract is 2 paragraphs at most.
```
Notes: fine-tuning on synthetic data pays off more for niche domains and non-English; combine with CoT to transfer reasoning; Alpaca and Vicuna cited as examples of fine-tuning on synthetic data. Cost estimate in repo: 1B tokens at 0.002 USD/1k = 2,000 USD for output plus about the same for prompts (2023 prices).

## 5. Code generation (`coding.en.mdx`, marked "under development")
Setup in repo: OpenAI Playground chat mode, `gpt-3.5-turbo`, system message:
```
You are a helpful code assistant that can teach a junior developer how to code. Your language of choice is Python. Don't explain the code, just generate the code block itself.
```
Patterns (each with the exact prompt in the repo):
- **Basic:** `Write code that asks the user for their name and say "Hello"`.
- **Comments to code:** wrap numbered steps in a docstring block:
```
"""
1. Create a list of movies
2. Create a list of ratings for these movies
3. Combine them to make a json object of 10 movies with their ratings.
"""
```
  Output lacked `import json`: always run generated code and check imports.
- **Function completion / next line:** give a comment + partial signature (`# function to multiply two numbers and add 75 to it` / `def multiply(`); model completes.
- **Text-to-SQL:** put schema in the prompt:
```
"""
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science department
"""
```
  Then validate: ask the model for `CREATE TABLE` DDL ("Create a valid database schema with the above tables and columns"), then dummy rows ("Given the database schema above, generate valid insert statements include 4 rows for each table."), run in sqliteonline.com or similar; expected result 2 rows (Jane Doe, John Doe).
- **Explain code:** paste code + "Explain the above SQL statement." Gotcha: with the Python-only system message the model first says it cannot generate SQL but then explains; system messages can cause refusals/off-task behaviour, so keep the system message consistent with tasks.
- Editing, debugging, best practices: "Example coming soon" (empty). See `notebooks-and-code-recipes.md` for the Code Llama notebook which does cover debugging, unit tests, infilling.

## 6. Graduate job classification case study (`workplace_casestudy.en.mdx`)
Source: Clavie et al. 2023, arXiv 2303.07142; model `gpt-3.5-turbo`; task: is a job posting a true entry-level role for a recent graduate. Production-scale text classification.
Findings: LLM beat all other models including strong DeBERTa-V3; gpt-3.5-turbo beat older GPT-3 variants but sticks to output template worse (needs parsing); for tasks needing no expert knowledge few-shot CoT was WORSE than zero-shot in all experiments; prompt choice moved F1 from 65.6 to 91.7; forcing a strict template lowered performance (said to vanish in early GPT-4 tests, posterior to the paper); instruction placement + repeating key points was the biggest driver; naming the model with a human name gave +0.6 F1.
Modifications tested: Baseline (post + "is it fit for a graduate"), CoT (few examples), Zero-CoT (reason step-by-step first), rawinst (role/task instructions in user msg), sysinst (in system msg), bothinst (role in system, task in user), mock (mock a dialogue where it acknowledges instructions), reit (repeat key elements), strict (follow template strictly), loose (only final answer follows template), right (ask to reach the right conclusion), info (extra info for common reasoning failures), name (give it a name), pos (positive feedback before the query).
Cumulative results (P / R / F1 / template stickiness): Baseline 61.2/70.6/65.6/79%; CoT 72.6/85.1/78.4/87%; Zero-CoT 75.5/88.3/81.4/65%; +rawinst 85.8 F1; +sysinst 83.8; +bothinst 87.5; +mock 88.8; +reit 89.3; +strict 86.3 F1 but 98% stickiness; +loose 87.1 F1 / 95%; +right 89.6; +info 90.3; +name 90.9; +pos 91.7 (P 86.9, R 97, stickiness 81%).
**Takeaways:** split role (system) and task (user); repeat key constraints; iterate on prompt text empirically; trade-off between format adherence and accuracy. Caveat: GPT-3.5-era results; "positive feedback"/name tricks are weak, unreplicated effects (0.6 pt).

## 7. Prompt functions (`pf.en.mdx`)
**What:** treat the chat as a shell: define named "functions" (name, input, rule) with a meta prompt, then call `name(args)` and chain them. Tested on GPT-3.5, "better on GPT-4" (2023 claim).
Meta prompt (verbatim, condensed in framing only):
```
Hello, ChatGPT! I hope you are doing well. I am reaching out to you for assistance with a specific function. I understand that you have the capability to process information and perform various tasks based on the instructions provided. In order to help you understand my request more easily, I will be using a template to describe the function, input, and instructions on what to do with the input. Please find the details below:

function_name: [Function Name]
input: [Input]
rule: [Instructions on how to process the input]

I kindly request you to provide the output for this function, based on the details I have provided. Your assistance is greatly appreciated. Thank you!
I will replace the text inside the brackets with the relevant information for the function I want you to perform. This detailed introduction should help you understand my request more efficiently and provide the desired output. The format is function_name(input) If you understand, just answer one word with ok.
```
Definitions:
```
function_name: [trans_word]
input: ["text"]
rule: [I want you to act as an English translator, spelling corrector and improver. I will provide you with input forms including "text" in any language and you will detect the language, translate it and answer in the corrected of my text, in English.]
```
Others: `expand_word` (keep meaning, more literary, output in original language), `fix_english` (improve vocabulary/sentences, natural, keep meaning), `pg` (password generator with params length, capitalized, lowercase, numbers, special; "Do not include any explanations"). Calls: `trans_word('...')`, `fix_english(expand_word(trans_word('...')))`, `pg(length = 10, capitalized = 1, lowercase = 5, numbers = 2, special = 1)` or positional `pg(10,1,5,2,1)`. Tip: append `DO NOT SAY THINGS ELSE OK, UNLESS YOU DONT UNDERSTAND THE FUNCTION` to suppress chatter. Page suggests storing the functions as few-shot/preset in chat UIs (ChatGPT-Next-Web, chatbox, PromptAppGPT, ChatGPT-Desktop) and mentions Copilot, LangChain, marvin.
**Modern take (not in repo):** the same idea is now done with system prompts/skills/custom GPTs or real tool definitions; a password generator via LLM is insecure (LLMs are not random sources). Chaining by nesting depends on the model keeping state in a chat; with APIs just chain calls in code.

## 8. Context caching with Gemini 1.5 Flash (`context-caching.en.mdx`)
Use case: query a year of ML-Papers-of-the-Week summaries (one text file) repeatedly without resending it. Steps: convert README to .txt; upload via `google.generativeai`; `caching.CachedContent.create(model, display_name, system_instruction, contents, ttl)`; build model with `GenerativeModel.from_cached_content`; query. Example queries: "Can you please tell me the latest AI papers of the week?", "Can you list the papers that mention Mamba? List the title of the paper and summary.", "What are some of the innovations around long-context LLMs? List the title of the paper and summary." Page text says TTL 15 min; notebook comment says "5 minute TTL" but code uses 15 (inconsistent). Code in `notebooks-and-code-recipes.md`. Page promotes AI-courses callout.
**Stale:** `google-generativeai` / `genai.configure` / `caching.CachedContent` and model `gemini-1.5-flash-001` are the legacy SDK/model; Google moved to the `google-genai` SDK and retired Gemini 1.5 models (not in repo). Concept (cache a large static prefix, pay less per query, TTL-bound) still valid and also exists as Anthropic/OpenAI prompt caching (not in repo).

## 9. Fine-tuning GPT-4o (`finetuning-gpt4o.en.mdx`)
Announcement summary (Aug 2024): checkpoint `gpt-4o-2024-08-06`, via the fine-tuning dashboard; customizes structure, tone, domain-instruction adherence. Prices stated: 25 USD per 1M training tokens; 3.75 USD per 1M input and 15 USD per 1M output tokens at inference; paid tiers only; free training tokens until Sep 23 (1M/day for GPT-4o, 2M/day for 4o mini). Demo: emotion classification fine-tuning of GPT-4o mini on JSONL dataset (github.com/dair-ai/datasets/tree/main/openai), evaluate in playground then via API. No JSONL format shown on the page (chat-format `{"messages":[...]}` per line is standard, not in repo).
**Stale:** prices, promo dates, and model snapshot are Aug 2024 facts; verify current docs.

## 10. Audit notes
- Heavily GPT-3.5/GPT-4-2023 era: coding.en.mdx (gpt-3.5-turbo playground), workplace_casestudy (GPT-3.5 only; "few-shot CoT worse than zero-shot" is task/model-specific and not a general rule), pf (ChatGPT-era chat hack), synthetic_rag/generating_textbooks (2023 prices, GPT-3.5 Turbo 0.0015/0.002 per 1k, ChatGPT 0.002/1k).
- Function calling page: header text says "GPT-4 and GPT-3.5"; code uses `gpt-3.5-turbo-1106` (old); `function_call=None` field shown in ChatCompletionMessage output is the deprecated functions API remnant; no tool-result round trip in the page itself (only the notebook, which has bugs; see notebooks file). "Functional calling" typo; "it doesn't actually executes" typo. "Open-source LLMs: coming soon" is empty.
- coding.en.mdx: "Editing Code", "Debugging Code", "Best practices" are empty stubs; page is flagged "under development". Section "Explain Code" demonstrates a system-message conflict but no fix.
- generating_textbooks: image-only content for Phi-1 metrics; prompt in the Phi-1 reconstruction pastes code without fence (page formatting issue). Text says Phi-1 "rival models ten times its size"; claim from paper, unverified here. "Takling" typo in README link title.
- synthetic_rag.en.mdx: imports `remark-math`/`rehype-katex` inside MDX (unused boilerplate); LaTeX formula relies on `latex: true` in next.config.js. The cost line `50,000 * (700 * 0.001 * $0.0015 + 25 * 0.001 * $0.002) = 55` should be about 55 USD (700*0.001*0.0015=0.00105, 25*0.001*0.002=0.00005; sum 0.0011 x 50,000 = 55): arithmetic is OK.
- workplace_casestudy table: italicised rows are the ones the paper marks as individual tests; "Template Stickiness" drops sharply for Zero-CoT (65%) vs CoT (87%): accuracy/format trade-off.
- context-caching page and notebook disagree on TTL (15 min text and code vs "5 minute" comment). Notebook has dead loop variable `video_file` (never assigned to `file`, so the wait loop would never terminate if state stayed PROCESSING).
- finetuning page: cost/promo facts expire; no training-data format.
- Many pages end with a marketing Callout ("Join now", promo code PROMPTING20); ignore.
- Gaps: no agent/MCP tool use, structured-output/JSON-mode, prompt caching for other vendors, evals, or prompt-injection handling for function calling in this section (see risks section of repo).
