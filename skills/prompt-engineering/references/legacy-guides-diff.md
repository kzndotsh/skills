# Legacy guides/*.md vs pages/ (what the legacy copies hold that pages/ lacks, or conflict)

Scope: repo-root `README.md`, `guides/README.md`, and `guides/prompts-{intro,basic-usage,advanced-usage,applications,chatgpt,adversarial,reliability,miscellaneous}.md`. The legacy guides are the pre-website (Dec 2022 - Mar 2023) version: all examples use `text-davinci-003` (Playground defaults `temperature=0.7`, `top-p=1`) unless noted. The pages/ site supersedes them. Verdict: legacy content is almost entirely a subset of pages/; only a few items are unique, and legacy has several errors the site fixed.

## Contents
1. Per-file summary and where each is superseded
2. Content present in legacy but missing or different in pages/
3. Conflicts and errors in legacy
4. Content only in pages/ (for contrast)
5. Recommendation for the skill
6. Audit notes

---

## 1. Per-file map

| Legacy file | Topics | pages/ counterpart | Status |
|---|---|---|---|
| README.md (root) | project blurb, announcements (3M learners Jan 2024, 13 languages, courses/services), full TOC of site, lecture links (video, notebook, slides), local run steps, citation (Saravia 2022), MIT license | pages/index.en.mdx, about | Marketing/TOC only; no prompt content. Local-run steps say `pnpm i next react react-dom nextra nextra-theme-docs` / `pnpm dev`. |
| guides/README.md | links to the 8 legacy guides | n/a | Index only |
| prompts-intro.md | basic prompt, LLM settings (temperature, top_p), standard/few-shot formats, prompt elements, design tips | pages/introduction/{basics,settings,elements,tips,examples}.en.mdx | Superseded (site is expanded; see section 2) |
| prompts-basic-usage.md | summarization, extraction, QA, classification, conversation, code generation, reasoning, notebooks | pages/introduction/examples.en.mdx + pages/prompts/** | Superseded; see 2.4 |
| prompts-advanced-usage.md | zero-shot, few-shot, CoT, zero-shot CoT, self-consistency, generated knowledge, APE | pages/techniques/*.en.mdx | Superseded |
| prompts-applications.md | generating data, PAL | pages/applications/generating.en.mdx, pages/techniques/pal.en.mdx | Mostly superseded; wine/NER labeling example is missing in pages/ (2.1) |
| prompts-chatgpt.md | ChatGPT intro, multi-turn, single-turn, instructing chat models, notebooks, ~40 ChatGPT-era references | pages/models/chatgpt.en.mdx | Superseded; reference list expanded in pages |
| prompts-adversarial.md | injection, leaking, jailbreaking, defenses | pages/risks/adversarial.en.mdx | Superseded; site adds DAN/Waluigi/simulators |
| prompts-reliability.md | factuality, biases, reference list | pages/risks/{factuality,biases}.en.mdx | Superseded; reference list not carried over |
| prompts-miscellaneous.md | Active-Prompt, DSP, ReAct, Multimodal CoT, GraphPrompts | pages/techniques/{activeprompt,dsp,react,multimodalcot,graph}.en.mdx | Superseded; stubs ("Full example coming soon") |

## 2. In legacy, missing or different in pages/

### 2.1 Data labeling / NER augmentation example (prompts-applications.md) - MISSING in pages/
Prompt:
```
produce 3 wine reviews and label taste, flavor, aroma related token; present the result as a json file, in addition add the coordinate of each term for NER task
```
Output: JSON list of reviews with `tokens` objects `{text, label, start, end}`; labels flavor/texture/aroma/taste. Caveats: the offsets in the shown output are inaccurate (not verified against the review strings); labels are inconsistent ("rich" labeled flavor in one review, aroma in another; "texture" label not in the requested set taste/flavor/aroma); the third review's array has a trailing comma and the whole output is missing the closing `]`, so it is invalid JSON; the model produced only the first tokens for review 3. Lesson: LLM-generated spans need programmatic offset verification (recomputing `text.find`). pages/applications/generating.en.mdx has the 10-exemplar sentiment generation prompt but not this one (grep for "wine" in pages/ finds nothing).
The sentiment data-generation prompt (present in both):
```
Produce 10 exemplars for sentiment analysis. Examples are categorized as either positive or negative. Produce 2 negative examples and 8 positive examples. Use this format for the examples:
Q: <sentence>
A: <sentiment>
```
Legacy remark: this output is reused as the exemplar set for the bias test (so the 8-positive/2-negative skew is by design).

### 2.2 Explicit explanation that few-shot demos with random labels still work (prompts-advanced-usage.md)
The hub page `classification/sentiment-fewshot` has the flipped-label prompt but no explanation. Legacy and pages/techniques/fewshot both explain via Min et al. (2022): label space and input distribution matter, format matters, random labels drawn from the true label distribution help. Legacy also shows a no-consistency-format variant (`Positive This is awesome! / This is bad! Negative / Wow that movie was rad! / Positive / What a horrible show! --` -> `Negative`) and claims newer GPT models are robust to random formats; flagged as unverified ("have to conduct a more thorough analysis"). In pages/ this appears in techniques/fewshot.

### 2.3 Legacy-only incidental details
- Intro: LLM settings text is shorter (only temperature and top_p; "alter one, not both"). pages/introduction/settings adds max length, stop sequences, frequency and presence penalties (not in legacy).
- Intro: "Others recommend that instructions are placed at the beginning... use a clear separator like ###" (present in pages/introduction/tips as well).
- Intro tips: "movie recommendation" agent example with DO NOT ASK FOR INTERESTS (present in pages/introduction/tips.en.mdx).
- Intro: "Specificity" example with Place extraction (`Desired format: Place: <comma_separated_list_of_places>`) is in pages/introduction/tips.
- Basic usage: simple summarization flow `Explain antibiotics\n\nA:` then "Explain the above in one sentence:". The "A:" cue explanation ("explicit prompt format used in QA") is legacy wording; pages/introduction/examples has a version.
- Basic usage: conversation/role prompting with two personas ("technical and scientific" vs "easy to understand even by primary school students"); both in pages/introduction/examples.
- Basic usage: "Python Notebooks" tables linking to notebooks/pe-lecture.ipynb, pe-pal.ipynb, pe-chatgpt-intro.ipynb, pe-chatgpt-langchain.ipynb, pe-chatgpt-adversarial.ipynb. Pages/ lists notebooks on pages/notebooks.en.mdx.
- ChatGPT guide: claims "significant cost reduction (90%)" for the gpt-3.5-turbo API vs text-davinci-003 and customers Snap Inc. and Instacart; both are also in pages/models/chatgpt.en.mdx. Legacy mentions "ChatML". The recommendation "for gpt-3.5-turbo-0301 add instructions in the user message rather than the system message" is in both; it is a model-snapshot-specific note that is obsolete (later chat models weight the system message properly).
- ChatGPT guide reference list: ~40 Feb-Mar 2023 papers (e.g. "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT" arXiv 2302.11382; "Dr ChatGPT, tell me what I want to hear"; "ChatGPT: Jack of all trades, master of none"; "Is ChatGPT a Good NLG Evaluator?"; "Check Your Facts and Try Again" 2302.12813; OpenAI Cookbook "How to format inputs to ChatGPT models"; Awesome ChatGPT Prompts repo). pages/models/chatgpt.en.mdx carries a much longer (about 140 arXiv links) reference list, so nothing is lost.
- Reliability guide reference list (not in pages/risks): Constitutional AI (2212.08073), "Rethinking the Role of Demonstrations" (2202.12837), "Prompting GPT-3 To Be Reliable" (2210.09150), "On the Advance of Making Language Models Better Reasoners" (2206.02336), "Unsolved Problems in ML Safety" (2109.13916), "Red Teaming Language Models to Reduce Harms" (2209.07858), StereoSet (ACL 2021), "Calibrate Before Use" (2102.09690), OpenAI Cookbook "Techniques to improve reliability". Some may be in pages/papers.en.mdx.
- Reliability guide "other upcoming topics": perturbations, spurious correlation, domain shift, toxicity, hate speech, stereotypical bias, gender bias, red teaming. Never written in pages/risks either (gap).
- Miscellaneous guide: Active-Prompt text (Diao et al., 2023), DSP (Li et al., 2023), ReAct (Yao et al., 2022), Multimodal CoT (Zhang et al., 2023; "1B model outperforms GPT-3.5 on ScienceQA"), GraphPrompts (Liu et al., 2023) are short stubs, all expanded or equivalent in pages/techniques.
- APE section lists AutoPrompt, Prefix Tuning, Prompt Tuning as related (also in pages/techniques/ape). The legacy APE text includes the discovered prompt "Let's work this out in a step by step way to be sure we have the right answer." (also in pages/techniques/ape).
- Adversarial: legacy states jailbreak example only for the hotwire poem; no DAN/Waluigi/simulators; shorter prompt-leaking definition.

### 2.4 Outputs and numbers that differ
- Basic usage reasoning: bare prompt `The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.\n\nA:` -> `No, the odd numbers in this group add up to an odd number: 119.` (also in pages/introduction/examples). Check: 15+5+13+7+1 = 41; 119 is wrong; the final answer "odd" is correct but the sum is wrong. The advanced guide's retry gives `Yes ... 107 ... even` (wrong). Step-by-step prompt result: `Odd numbers: 15, 5, 13, 7, 1 / Sum: 41 / 41 is an odd number.`; legacy admits the prompt "sometimes fails".
- Zero-shot classification in legacy README/basic usage is `Classify the text into neutral, negative or positive.` (no comma before "or"); the hub page uses `neutral, negative, or positive` and no trailing period. Trivial.
- Science QA prompt: legacy "Keep the answer short." vs hub "Keep the answer short and concise." (pages/introduction/examples also may differ). Not meaningful.

## 3. Conflicts and errors in legacy (fixed or different in pages/)

1. prompts-applications.md PAL date prompt, exemplar 5: `# If Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later ... then today is 3/1/2002.` - wrong; pages/techniques/pal.en.mdx says `3/12/2002`. Exemplar 4 (4/19/1969) in BOTH versions ends with `today.strftime(...)` instead of `later.strftime(...)`; a bug that remains in pages/ (answer would be 04/19/1969 not 04/20/1969). Do not copy it.
2. prompts-applications.md PAL imports `from langchain.llms import OpenAI` and `text-davinci-003`: both obsolete (LangChain moved to `langchain_openai`; model retired Jan 2024). pages/ still shows text-davinci-003 (line 43 of pal.en.mdx).
3. prompts-reliability.md factuality example has a formatting bug: `A: ? Q: ` run together before "How many moons does Mars have?" (a stray `Q:` on the previous line and missing newline). Fixed in pages/risks/factuality.en.mdx.
4. prompts-reliability.md: "mitigates" typo; "biasness"; "more balanced number" wording tweaked in pages. Content same.
5. prompts-adversarial.md: "analyze ... in order to hack" wording differs trivially from pages ("analyse"); the guard prompt otherwise equal. Legacy says "I couldn't reproduce" in first person vs pages "we".
6. prompts-adversarial.md says jailbreaking "contextualized cleverly" and has no discussion of model providers updating; pages adds the warning about patched attacks.
7. prompts-self-consistency (advanced): the exemplar block ends the Olivia exemplar mid-sentence: `A: She bought 5 bagels for $3 each. This means she spent 5`; pages/techniques/consistency.en.mdx completes it: `This means she spent $15. She has $8 left.` Legacy version is truncated and would mislead few-shot copy-paste.
8. advanced guide, generated knowledge: knowledge item says Mexico is "1,389% larger than Greece"; same text in pages/techniques/knowledge (arithmetic: 1,964,375 / 131,957 = 14.9x, i.e. ~1,389% larger; consistent).
9. README.md announcements are dated (3 million learners Jan 2024); README links point to promptingguide.ai web pages, and a legacy "Running the guide locally" step with `pnpm i ...` may differ from package.json scripts (not verified).
10. guides/README.md links use absolute `/guides/...` paths that only work on GitHub.
11. chatgpt guide ("gpt-3.5-turbo-0301 prefer user message") conflicts with current best practice of using the system message for instructions (not in repo). Also pages/models/chatgpt.en.mdx keeps the same statement, so it is stale there too.
12. Basic usage claims "current LLMs struggle to perform reasoning tasks" and "9,000 * 9,000 = 81,000,000" as a simple reasoning example; stale (2023). Few-shot guidance "from here start thinking about fine-tuning" predates strong instruction/reasoning models.

## 4. Content only in pages/ (not in legacy)

- Techniques: Meta Prompting, Reflexion, ToT, ART, RAG, Prompt Chaining (pages/techniques) - check other audit slices.
- Applications: function calling, synthetic data for RAG, generating textbooks, coding, workplace case study, context caching, fine-tuning GPT-4o (pages/applications).
- Models: GPT-4, Gemini, Mixtral, Mistral 7B, Llama, Phi-2, OLMo, Code Llama, Flan, etc. (pages/models).
- Prompt Hub (pages/prompts/**), Agents, guides on reasoning LLMs, context engineering, deep research, 4o image generation, optimizing prompts (pages/guides).
- Risks: DAN, Waluigi, GPT-4 simulator, game simulator, NIST reference.
- Pages are translated into 12+ languages; legacy guides are English-only.

## 5. Recommendation for the skill

- Treat legacy guides as redundant. Retain only: (a) the wine-review NER-labeling prompt as an example of structured JSON generation with an explicit warning about unreliable offsets, (b) the Reliability reference list as optional reading, and (c) the legacy "reasoning" progression (bare -> wrong, step-by-step -> right) as a teaching sequence.
- Prefer pages/ versions of every shared prompt; fix the PAL exemplar 4 `today.strftime` bug if you copy the PAL prompt (should be `later.strftime`).

## 6. Audit notes

- No legacy file was found to contain a technique or model absent from pages/, other than the wine example.
- Legacy "A:" cue text and the 3-sentence student-friendly examples match pages/introduction text almost verbatim (suggests pages/ was copy-edited from legacy; most differences are "I" -> "you/we", typo fixes, formatting).
- All legacy outputs are non-reproducible on current models; they are illustrations, not tests.
- README.md has sponsor/course promotion (SerpApi sponsor logo, DAIR.AI Academy discount code) that should not be treated as guidance; also an "Appearances" section of press links.
- Files read in full: README.md, guides/README.md, and all 8 prompts-*.md (chatgpt reference list read in full; long list of 2023 papers summarized, not reproduced).
