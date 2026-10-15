# Prompting Techniques Reference

Source: dair-ai/Prompt-Engineering-Guide `pages/techniques/*.en.mdx` (+ `_meta.en.json`, `techniques.en.mdx`).
"(not in repo)" marks additions from general knowledge. Several repo pages are stubs; noted below.

## Contents
- Decision table: problem -> technique
- 1 Zero-shot  2 Few-shot  3 Chain-of-Thought (+zero-shot CoT, Auto-CoT)  4 Meta prompting
- 5 Self-consistency  6 Generated knowledge  7 Prompt chaining  8 Tree of Thoughts
- 9 RAG  10 ART  11 APE  12 Active-Prompt  13 Directional stimulus  14 PAL  15 ReAct
- 16 Reflexion  17 Multimodal CoT  18 GraphPrompts
- Audit notes

Repo ordering (`_meta.en.json`): zeroshot, fewshot, cot, meta-prompting, consistency, knowledge, prompt_chaining, tot, rag, art, ape, activeprompt, dsp, pal, react, reflexion, multimodalcot, graph.

---

## Decision table: problem -> technique

| Problem | Try first | Escalate to |
|---|---|---|
| Simple, well-known task (sentiment, summary, translate) | Zero-shot with clear instruction + output format | Few-shot |
| Wrong/unstable output format or label set | Few-shot (format and label space matter more than label correctness) | Output indicator, delimiters |
| Arithmetic / multi-step / commonsense reasoning wrong | CoT (few-shot with rationales, or "Let's think step by step") | Self-consistency; PAL for math/dates |
| Reasoning still unreliable, answer varies across runs | Self-consistency (sample N CoT paths, majority vote) | ToT |
| Need exact computation (dates, arithmetic, counting) | PAL (generate code, run it) | ReAct with calculator tool |
| Commonsense/fact question model gets wrong | Generated knowledge | RAG |
| Needs up-to-date or private facts; hallucination | RAG | ReAct with search |
| Task too complex for one prompt; need transparency/debuggability | Prompt chaining | ToT / agents |
| Search/lookahead/strategy problem (puzzles, planning, Game of 24) | ToT | - |
| Agent must act on environment/tools and reason about results | ReAct | Reflexion |
| Agent repeats mistakes across trials; has feedback signal (tests, reward) | Reflexion | - |
| Few-shot CoT exemplars are hand-picked and weak | Active-Prompt (annotate most uncertain questions) | Auto-CoT |
| Don't want to hand-write CoT demos | Auto-CoT, ART | - |
| Don't know the best instruction wording | APE / OPRO (LLM-generated and scored prompts) | Prompt tuning (training) |
| Want to steer a frozen black-box LLM toward desired content (e.g. summaries with keywords) | Directional stimulus prompting (hints from small policy LM) | - |
| Same structure applies to many problems; token budget tight | Meta prompting (structure-only template) | Few-shot |
| Image + text question answering | Multimodal CoT | - |
| Graph tasks | GraphPrompt | - |
| Simple + few-shot + CoT all fail | Consider fine-tuning (repo's own advice) | - |

Escalation order the guide implies: zero-shot -> few-shot -> CoT -> (self-consistency / decomposition / tools / retrieval) -> fine-tune.

---

## 1. Zero-Shot Prompting
Source: `zeroshot.en.mdx`; Wei et al. 2022 (instruction tuning, FLAN), RLHF (Christiano 2017).
- **What**: prompt contains only the instruction, no demonstrations. Works because models are instruction-tuned (finetuned on instruction datasets) and RLHF-aligned.
- **Use**: first attempt for any task the model plausibly knows.
- **Don't**: task needs a specific format/label space the model won't guess, or complex reasoning.
- **Template**:
```
Classify the text into neutral, negative or positive.

Text: I think the vacation is okay.
Sentiment:
```
-> `Neutral`.
- **Failure/fix**: when zero-shot fails, add demonstrations (few-shot).

## 2. Few-Shot Prompting
Source: `fewshot.en.mdx`; Brown et al. 2020; Min et al. 2022; Touvron 2023; Kaplan 2020.
- **What**: put k demonstrations (1-shot, 3-shot, 5-shot, 10-shot...) in the prompt; the model does in-context learning. Few-shot ability emerges with model scale.
- **Use**: need output format, label space, or style control; moderately hard tasks.
- **Template**:
```
<input> // <label>
<input> // <label>
<input> // <label>
<new input> //
```
Brown et al. example (1-shot new-word usage):
```
A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that uses the word whatpu is:
We were traveling in Africa and we saw these very cute whatpus.

To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses the word farduddle is:
```
- **Findings (Min et al. 2022)**: label space and input-text distribution of the demos matter; format matters; even random labels beat no labels; sampling random labels from the true label distribution (not uniform) helps further. Guide demo: randomized labels still gave the correct result, and even inconsistent formats worked on newer GPT models (anecdotal, "needs more analysis").
- **Limits**: fails on multi-step reasoning. Guide's odd-numbers sum task: 4 label-only exemplars still gave wrong "True". Fix: CoT.
- **Tips (mostly not in repo)**: choose diverse, representative exemplars; keep consistent format; order can matter; balance classes.
- When zero/few-shot insufficient the model may lack the capability: fine-tune or use advanced techniques.

## 3. Chain-of-Thought (CoT)
Source: `cot.en.mdx`; Wei et al. 2022; Kojima et al. 2022; Zhang et al. 2022 (Auto-CoT).

### 3a. Few-shot CoT
- **What**: exemplars include intermediate reasoning, not just answers. Emergent in sufficiently large models (authors' claim).
- **Use**: arithmetic, commonsense, symbolic reasoning.
- **Template** (verbatim from repo, one exemplar is enough):
```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
A:
```
-> `Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.`

### 3b. Zero-shot CoT
- **What**: append "Let's think step by step." to the question. No examples needed.
```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?

Let's think step by step.
```
Without the trigger the model answered `11 apples` (wrong); with it, correct `10`.
- Related (APE page): "Let's work this out in a step by step way to be sure we have the right answer." scored better on MultiArith/GSM8K.

### 3c. Auto-CoT
- **What**: automate exemplar construction. (1) cluster dataset questions; (2) pick a representative from each cluster and generate its chain with zero-shot CoT, filtered by simple heuristics (question <= ~60 tokens, rationale <= ~5 steps). Diversity mitigates wrong auto-generated chains.
- Code: github.com/amazon-science/auto-cot.
- **Caveats**: generated chains can be wrong; hand-crafting demos is costly (motivation).
- (not in repo) With current reasoning models (o-series, Claude extended thinking, etc.), explicit "think step by step" is often unnecessary or counterproductive; the model reasons internally. Still useful for non-reasoning models.

## 4. Meta Prompting
Source: `meta-prompting.en.mdx`; Zhang et al. 2024 (arXiv 2311.11482, "Meta Prompting for AI Systems").
- **What**: structure-oriented, syntax-focused prompting; give abstract templates of problem and solution form rather than concrete examples. Draws on type theory (categorical). The model is assumed to already know the domain.
- **Characteristics**: structure over content; syntax as template; abstract examples; domain-agnostic; categorical arrangement of prompt components.
- **vs few-shot**: fewer tokens, less bias from specific examples, fairer model comparisons, acts like zero-shot with structure. Paper's illustration compares a structured MATH-benchmark prompt to few-shot (image not reproducible here).
- **Use**: complex reasoning, math, coding, theoretical queries where you know the solution skeleton.
- **Caveat**: performance drops on unique/novel tasks (like zero-shot).
- **Template (not in repo; illustrative)**:
```
Problem: {{problem}}
Solution structure:
Step 1: Restate the quantities and unknowns.
Step 2: Choose the relevant formula or rule and state it.
Step 3: Substitute and compute, showing each operation.
Step 4: Check the result against the problem constraints.
Final answer: \boxed{...}
```
- (not in repo) The term also commonly means "using an LLM to write/refine prompts"; that sense is closer to APE (section 11).

## 5. Self-Consistency
Source: `consistency.en.mdx`; Wang et al. 2022 (arXiv 2203.11171).
- **What**: replace greedy decoding in CoT: sample multiple diverse reasoning paths (few-shot CoT, temperature > 0), then take the most frequent final answer (majority vote).
- **Use**: arithmetic and commonsense reasoning where a single CoT run is brittle.
- **Cost**: N times tokens/latency.
- **Procedure**: (1) few-shot CoT prompt; (2) sample N completions; (3) extract final answers; (4) majority vote. (The paper has weighted variants; repo says see paper.)
- **Worked example**: `When I was 6 my sister was half my age. Now I'm 70 how old is my sister?` Plain prompt -> `35` (wrong). With Wang et al. Table 17 CoT exemplars (the 8 grove/cars/chocolates/lollipops/toys/computers/golf-balls/bagels exemplars), three samples: 67, 67, 35 -> majority 67 (correct).
- **Caveats**: needs final-answer extraction; free-form outputs need normalization; no gain if all samples share the same bias; reasoning models make this partly redundant (not in repo).

## 6. Generated Knowledge Prompting
Source: `knowledge.en.mdx`; Liu et al. 2022 (arXiv 2110.08387).
- **What**: two calls. (1) Ask the LLM to generate relevant facts ("knowledge") for the input using few-shot Input/Knowledge exemplars. (2) Put each knowledge into a QA prompt and ask for an answer; pick the answer with highest confidence across knowledges (paper has details).
- **Use**: commonsense reasoning where the model errs from missing/mis-weighted facts, and no retrieval source available.
- **Step 1 template** (verbatim structure; 5 exemplars in repo, 1 shown):
```
Input: Greece is larger than mexico.
Knowledge: Greece is approximately 131,957 sq km, while Mexico is approximately 1,964,375 sq km, making Mexico 1,389% larger than Greece.

Input: Part of golf is trying to get a higher point total than others.
Knowledge:
```
- **Step 2 template**:
```
Question: Part of golf is trying to get a higher point total than others. Yes or No?

Knowledge: <generated knowledge>

Explain and Answer:
```
- **Worked example**: baseline `Yes.` (wrong). Knowledge 1 (golf = fewest strokes) -> "No..." (very confident). Knowledge 2 (also correct facts but phrased to read ambiguously) -> "Yes..." (lower confidence). So choose by confidence across several knowledges.
- **Caveats**: generated knowledge can be wrong; the repo's second answer shows the model can misread correct knowledge; needs multiple samples; the repo's own "Greece/Mexico 1,389% larger" exemplar is numerically odd.

## 7. Prompt Chaining
Source: `prompt_chaining.en.mdx`; inspired by Anthropic's prompt-chaining docs.
- **What**: split a task into subtasks; each prompt's output feeds the next. Intermediate outputs can be transformed or cleaned between steps.
- **Benefits**: better performance on complex tasks, transparency, controllability, reliability, easier debugging per stage; useful for conversational assistants and personalization.
- **Use**: document QA, multi-stage transformations, anything where one giant prompt gets confused.
- **Document QA pattern** (verbatim from repo):

Prompt 1 (extract; question goes in `user` message, `{{document}}` is the doc):
```
You are a helpful assistant. Your task is to help answer a question given in a document. The first step is to extract quotes relevant to the question from the document, delimited by ####. Please output the list of quotes using <quotes></quotes>. Respond with "No relevant quotes found!" if no relevant quotes were found.


####
{{document}}
####
```
Prompt 2 (answer from quotes):
```
Given a set of relevant quotes (delimited by <quotes></quotes>) extracted from a document and the original document (delimited by ####), please compose an answer to the question. Ensure that the answer is accurate, has a friendly tone, and sounds helpful.

####
{{document}}
####

<quotes>
{{quotes from prompt 1}}
</quotes>
```
- **Extension ideas** (repo exercise): add a step stripping citation markers like `[27]`.
- **Caveats**: error propagation between stages; add validation or fallback ("No relevant quotes found!") branches; more latency/cost. Repo example used `gpt-4-1106-preview` for long context.

## 8. Tree of Thoughts (ToT)
Source: `tot.en.mdx`; Yao et al. 2023 (2305.10601), Long 2023 (2305.08291), Hulbert 2023, Sun 2023 (PanelGPT).
- **What**: generalizes CoT. Maintain a tree of "thoughts" (coherent intermediate steps); LM generates candidates and self-evaluates them; search (BFS/DFS/beam) provides lookahead and backtracking.
- **Use**: tasks needing exploration or strategic lookahead (Game of 24, puzzles, planning).
- **Mechanics** (Game of 24): 3 steps, each an intermediate equation; keep best b=5 candidates per step; LM rates each candidate "sure/maybe/impossible" re reaching 24, sampled 3 times per thought. ToT substantially beat other prompting methods in the paper.
- **Variants**: Long 2023 uses an RL-trained "ToT Controller" to decide backtracking instead of fixed DFS/BFS (can keep learning with frozen LLM). Both are multi-round conversation tree search.
- **Single-prompt version (Hulbert 2023)**:
```
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
The question is...
```
PanelGPT (Sun 2023) benchmarks panel-discussion style prompting.
- **Caveats**: full ToT = many LLM calls and custom orchestration code (github.com/princeton-nlp/tree-of-thought-llm, jieyilong/tree-of-thought-puzzle-solver); single-prompt version is a role-play approximation without real search.

## 9. Retrieval Augmented Generation (RAG)
Source: `rag.en.mdx`; Lewis et al. 2020/2021 (2005.11401); survey Gao et al. Dec 2023 (2312.10997).
- **What**: retrieve relevant documents from an external source, concatenate as context with the input, then generate. Parametric knowledge (model weights) plus non-parametric memory (index). Knowledge updatable without retraining.
- **Use**: knowledge-intensive tasks, facts that change, private data, reducing hallucination, citing sources.
- **Original recipe**: pre-trained seq2seq generator + dense vector index of Wikipedia + neural retriever; fine-tuned end to end. Strong on Natural Questions, WebQuestions, CuratedTrec; more factual/specific/diverse on MS-MARCO and Jeopardy; better FEVER.
- **Prompt-level pattern (not in repo; standard)**:
```
Answer using only the context below. If the answer is not in the context, say "I don't know".

Context:
{{retrieved passages with ids}}

Question: {{question}}
Answer (cite passage ids):
```
- Notebook: `notebooks/pe-rag.ipynb` (ML paper title generation with open-source LLMs).
- **Caveats**: retrieval quality bounds answer quality; chunking, embeddings, reranking not covered by the repo page (see survey). Repo page is thin on practical details.

## 10. Automatic Reasoning and Tool-use (ART)
Source: `art.en.mdx`; Paranjape et al. 2023 (2303.09014).
- **What**: frozen LLM generates multi-step reasoning as a program; for a new task it selects demonstrations of multi-step reasoning and tool use from a task library; at test time generation pauses when a tool is called, tool output is integrated, then generation resumes. Zero-shot generalization to unseen tasks.
- **Extensible**: humans fix reasoning steps or add tools by editing the task/tool libraries.
- **Results**: beats few-shot and Auto-CoT on unseen BigBench and MMLU tasks; beats hand-crafted CoT when human feedback is included.
- **Use**: when you want automatic CoT + tool use without hand-scripting per task. Practically, this is the pattern of tool-calling agents (not in repo).
- **Caveat**: repo gives no prompt template; needs a task library and tool-orchestration code.

## 11. Automatic Prompt Engineer (APE)
Source: `ape.en.mdx`; Zhou et al. 2022 (2211.01910).
- **What**: instruction generation + selection as black-box optimization. An LLM (inference model) sees input/output demonstrations and proposes candidate instructions; a target model executes each; pick the instruction with the best evaluation score.
- **Result**: found zero-shot CoT trigger better than "Let's think step by step":
```
Let's work this out in a step by step way to be sure we have the right answer.
```
(improves MultiArith and GSM8K).
- **Use**: you have a labeled dev set and metric, and want a better instruction than hand-written ones.
- **Related automatic prompt optimization** (repo list): Prompt-OIRL (offline inverse RL, query-dependent prompts), OPRO (LLM optimizer; "Take a deep breath" helped on math), AutoPrompt (gradient-guided search), Prefix Tuning, Prompt Tuning (soft prompts via backprop).
- **Loop (not in repo)**: generate N instruction candidates -> score on dev set -> keep top -> optionally resample variants around the best.

## 12. Active-Prompt
Source: `activeprompt.en.mdx`; Diao et al. 2023 (2302.12246).
- **What**: choose which questions to hand-annotate with CoT. Steps: (1) query LLM (with or without few CoT examples) k times per training question; (2) compute uncertainty (disagreement among k answers); (3) humans annotate the most uncertain questions with CoT rationales; (4) use those new exemplars at inference.
- **Use**: you can afford a small annotation budget and fixed CoT exemplars underperform.
- **Caveat**: needs a pool of unlabeled questions and a human in the loop; page has no prompt template.

## 13. Directional Stimulus Prompting (DSP)
Source: `dsp.en.mdx`; Li et al. 2023 (2302.11520).
- **What**: a small tunable policy LM (trained, with RL) generates a stimulus/hint (e.g. keywords) for each input; the hint is added to the prompt of a frozen black-box LLM to guide output (e.g. summaries).
- **Use**: steer a black-box LLM without touching its weights; needs training data and a reward.
- **Repo status**: stub ("Full example coming soon!"). No template.
- **Template sketch (not in repo)**:
```
Article: {{article}}
Keywords (hint): {{hint from policy LM}}
Write a summary of the article that includes the keywords above.
```

## 14. PAL (Program-Aided Language Models)
Source: `pal.en.mdx`; Gao et al. 2022 (2211.10435).
- **What**: LLM reads a natural-language problem and writes a program as the reasoning; a runtime (Python interpreter) executes it. Offloads computation from the LLM, unlike CoT's free-text solution.
- **Use**: date arithmetic, math, counting, anything computable.
- **Prompt pattern**: few-shot `# Q:` / comment-reasoning / code lines ending with a formatted answer expression, then `# Q: {question}`.
Exemplar form (verbatim from the paper's date prompt):
```python
# Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
# If 2015 is coming in 36 hours, then today is 36 hours before.
today = datetime(2015, 1, 1) - relativedelta(hours=36)
# One week from today,
one_week_from_today = today + relativedelta(weeks=1)
# The answer formatted with %m/%d/%Y is
one_week_from_today.strftime('%m/%d/%Y')
```
Run: `llm_out = llm(PROMPT.format(question=question)); exec(llm_out); print(born)`. Question `Today is 27 February 2023. I was born exactly 25 years ago...` -> code -> `02/27/1998`.
- **Setup used**: LangChain `OpenAI(model_name='text-davinci-003', temperature=0)`, deterministic.
- **Caveats**: `exec` of model-generated code is dangerous; sandbox it (not in repo). Repo's exemplar 4 has a bug: ends with `today.strftime` instead of `later.strftime`. Model-specific imports are deprecated (see audit).

## 15. ReAct
Source: `react.en.mdx`; Yao et al. 2022 (2210.03629).
- **What**: interleave reasoning traces (Thought) and task actions (Action) with environment feedback (Observation). Reasoning plans/updates actions; actions fetch info for reasoning. Interpretable.
- **Use**: QA/fact-check needing search, decision-making agents (ALFWorld, WebShop), tool use.
- **Exemplar format** (verbatim shape from paper, HotpotQA):
```
Question What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1 I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1 Search[Colorado orogeny]
Observation 1 The Colorado orogeny was an episode of mountain building ...
Thought 2 It does not mention the eastern sector. So I need to look up eastern sector.
Action 2 Lookup[eastern sector]
Observation 2 ...
...
Action 5 Finish[1,800 to 7,000 ft]
```
Actions in the paper: `Search[entity]`, `Lookup[keyword]`, `Finish[answer]`.
- **Design**: reasoning-heavy tasks (HotpotQA) use dense thought-action-observation; many-step action tasks use thoughts sparsely.
- **Results (PaLM-540B)**: ReAct > Act on HotPotQA/Fever; ReAct beats CoT on Fever, lags CoT on HotpotQA; best = combining and switching between ReAct and CoT+Self-Consistency. On ALFWorld/WebShop ReAct > Act, still far from human experts.
- **Failure modes**: CoT hallucinates facts; ReAct's rigid structure limits reasoning flexibility; non-informative search results derail reasoning and make recovery hard.
- **LangChain usage** (zero-shot, no exemplars needed): agent `zero-shot-react-description` with tools `google-serper` and `llm-math`; trace format `Thought / Action / Action Input / Observation / Final Answer`. Example answer used Harry Styles' age (29) -> `29^0.23` = 2.169...
- Notebook: `notebooks/react.ipynb`.

## 16. Reflexion
Source: `reflexion.en.mdx`; Shinn et al. 2023 (2303.11366).
- **What**: "verbal reinforcement": environment feedback (scalar or text) is turned into a natural-language self-reflection stored in memory and given as context for the next trial; no weight updates.
- **Components**: Actor (CoT or ReAct generating actions/trajectory, with memory), Evaluator (scores trajectory; LLM or rule heuristics), Self-Reflection model (LLM that writes verbal cues from reward + trajectory + memory; stored in long-term memory; trajectory is short-term memory).
- **Loop**: define task -> generate trajectory -> evaluate -> reflect -> next trajectory.
- **Results**: AlfWorld ReAct+Reflexion completed 130/134 tasks; HotPotQA Reflexion+CoT beats CoT (with/without episodic memory); better on HumanEval, MBPP, Leetcode Hard (Python and Rust).
- **Use when**: trial-and-error learning, RL too expensive, nuanced feedback, need interpretable memory.
- **Limitations**: depends on self-evaluation quality; sliding-window memory (vector DB/SQL suggested for harder tasks); test-driven code checks struggle with non-deterministic or hardware-dependent functions.
- **Reflection prompt sketch (not in repo)**:
```
You attempted the task and failed. Trajectory: {{trajectory}}
Result/feedback: {{test output or reward}}
In 2-3 sentences, diagnose why it failed and state a concrete plan for the next attempt.
```
Prepend stored reflections to the next attempt's prompt.

## 17. Multimodal CoT
Source: `multimodalcot.en.mdx`; Zhang et al. 2023 (2302.00923).
- **What**: two-stage framework fusing text and vision: stage 1 generates a rationale from multimodal input; stage 2 infers the answer using that rationale.
- **Result**: a 1B multimodal CoT model beat GPT-3.5 on ScienceQA (2023 comparison).
- **Use**: visual question answering needing reasoning (diagrams, science questions).
- Further reading: "Language Is Not All You Need" (Kosmos-1, Feb 2023).
- **Repo status**: short summary, no prompt template. (not in repo) With modern VLMs you can approximate by asking: "Describe the relevant parts of the image, then reason step by step, then answer."

## 18. GraphPrompts
Source: `graph.en.mdx`; Liu et al. 2023 (2302.08043).
- **What**: prompting framework for graph neural networks to improve downstream graph tasks (a pre-training/prompt method for graphs, not text LLM prompting).
- **Repo status**: stub ("More coming soon!"). Nothing actionable; not relevant to ordinary LLM prompting.

---

## Audit notes
- **Stub pages**: `dsp.en.mdx` ("Full example coming soon!"), `graph.en.mdx` ("More coming soon!"), `activeprompt.en.mdx`, `multimodalcot.en.mdx`, `art.en.mdx` have no usable prompt templates; templates above marked "(not in repo)" are my sketches. `meta-prompting.en.mdx` has no prompt text (relies on an image).
- **Stale models/APIs**: PAL and ReAct code uses `text-davinci-003` (retired) and `from langchain.llms import OpenAI` / `initialize_agent` / `load_tools` (deprecated LangChain APIs); ReAct example facts (Olivia Wilde / Harry Styles, age 29) are time-bound. CoT/few-shot results come from GPT-3.5-era models; "Claude 3" appears in zero-shot page as an example of instruction-tuned models. Multimodal CoT "1B beats GPT-3.5" is a 2023 claim now irrelevant against current VLMs.
- **Likely outdated advice**: CoT and "think step by step" are redundant or harmful for reasoning-native models (not in repo). Self-consistency/ToT cost trade-offs differ with reasoning models. Many 2022-23 gains (APE, OPRO "take a deep breath") are model-specific and may not transfer.
- **Errors/oddities in examples**:
  - PAL exemplar 4 returns `today.strftime(...)` where it should be `later.strftime(...)`.
  - Self-consistency exemplar for Olivia/bagels lacks the "The answer is 8." ending (inconsistent with the other exemplars); its third sampled output (`70/2 = 35`) is wrong by design.
  - Generated-knowledge Greece/Mexico claim ("1,389% larger") is arithmetically unusual; the "Knowledge 2" which yields a wrong answer is actually correct knowledge, so the demo mostly shows misreading, not bad knowledge.
  - ToT page spells "Yao et el."; RAG page "Lewis et el.".
  - ReAct page says "Obs" and "Act" in prose but shows `Observation`/`Action` in the exemplar.
- **Contradiction/inconsistency**: few-shot page claims random/inconsistent formats still work ("newer GPT models more robust") while also saying format is key; both are anecdotal. Intro says `temperature=1` for examples while settings advice is low temperature for facts.
- **Gaps**: no coverage of least-to-most, self-refine, maieutic, complexity-based prompting (all only named in the prompt-chaining output), skeleton-of-thought, chain-of-verification, structured output/JSON modes, tool/function calling (modern form of ART/ReAct), prompt caching, evals, context-window management. RAG page lacks chunking/embedding/reranking/eval guidance and modern variants. Meta-prompting page lacks a worked prompt.
- **Page hygiene**: every page ends with CoursePromo/CourseCard marketing components (promo code), irrelevant to content. Images (diagrams, result tables) are not reproduced; numeric results quoted only where in text.
