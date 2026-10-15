---
name: prompt-engineering
description: Prompt engineering knowledge base distilled and audited from the DAIR.AI Prompt Engineering Guide (promptingguide.ai). Use when writing, debugging, or improving prompts for LLMs; choosing a prompting technique (few-shot, chain-of-thought, self-consistency, ReAct, RAG, prompt chaining, PAL, ToT, Reflexion, meta-prompting); designing agents, tool/function calling, or context engineering; prompting reasoning models; defending against prompt injection, leaking, and jailbreaks; or looking up example prompts, LLM settings (temperature, top-p), and model notes.
license: MIT. Derived from DAIR.AI material, see NOTICE.md
---

# Prompt Engineering

Source: dair-ai/Prompt-Engineering-Guide at commit 5767372 (2026-03-11), English pages, notebooks, and lecture slides. Everything below was read in full and audited. Reference files carry templates, examples, caveats, and per-file "Audit notes".

**Read first:** the guide is mostly a 2022 to early-2024 snapshot (GPT-3.5, text-davinci-003, GPT-4, Mixtral era). Technique concepts hold up. Model-specific claims, prices, benchmarks, and code samples do not. See `references/audit-summary.md` before trusting any date-bound claim.

## Workflow for writing or fixing a prompt

1. Define the task, the output format, and how you will judge success. Without a check, you can't tell if a rewrite helped.
2. Start with the simplest prompt that could work: clear instruction, specific context, delimiters, explicit output format. Say what to do rather than what to avoid. Specificity beats length.
3. If output is wrong, escalate one step at a time: add few-shot examples (format and label space matter more than label correctness) -> reasoning (CoT, or a reasoning model) -> decomposition (prompt chaining) -> tools or retrieval (PAL, ReAct, RAG) -> fine-tuning.
4. Set parameters deliberately: low temperature/top-p for factual or extraction tasks, higher for creative tasks. Change one of temperature or top-p, not both.
5. Test against adversarial and edge inputs, including prompt injection if the prompt handles untrusted text.
6. Iterate on a fixed test set. A single lucky run proves nothing. The repo's own bias and exemplar-order examples are single-run, so don't copy that.

## Where to look

| Need | File |
|---|---|
| Prompt elements, settings, tips, basic examples | `references/fundamentals.md` |
| Pick or apply a technique (decision table + templates for 18 techniques) | `references/techniques.md` |
| Ready-made prompts by task (classification, QA, coding, extraction, summarization, math, reasoning, creativity, image gen) | `references/prompt-library.md` |
| Agents, workflows vs agents, function calling, deep agents, context engineering | `references/agents-and-context-engineering.md` |
| Reasoning-model prompting, prompt optimization, deep research, 4o image gen | `references/guides-modern.md` |
| Prompt injection, leaking, jailbreaks, defenses, biases, factuality | `references/risks-and-safety.md` |
| Real-world applications and case studies (code gen, synthetic data, fine-tuning, caching, job classification) | `references/applications.md` |
| Per-model notes (Llama, Mistral, Gemini, GPT-4, Claude 3, Gemma, ...) and chat templates | `references/models.md` |
| Research digests (RAG surveys, faithfulness, reasoning, tokenization, long context) and paper index | `references/research-notes.md` |
| Runnable patterns (function calling, PAL, RAG, ReAct, LangChain, caching) with staleness notes | `references/notebooks-and-code-recipes.md` |
| Lecture slide summary | `references/lecture-summary.md` |
| Tools, services, datasets, courses, readings | `references/resources-catalog.md` |
| Repo layout and what's in legacy `guides/` | `references/repo-map.md`, `references/legacy-guides-diff.md` |
| Cross-cutting audit findings (errors, stale items, gaps) | `references/audit-summary.md` |

Load only the file the task needs. Each starts with a table of contents.

## Quick technique picker

- Simple known task -> zero-shot with an explicit format.
- Format or labels wrong -> few-shot.
- Multi-step reasoning on a non-reasoning model -> CoT ("Let's think step by step" or worked exemplars); unstable answers -> self-consistency (sample N, majority vote).
- Exact arithmetic or dates -> PAL (generate code, execute in a sandbox).
- Fresh, private, or hallucination-prone facts -> RAG, or ReAct with search.
- Too complex for one prompt -> prompt chaining.
- Search or planning puzzles -> Tree of Thoughts.
- Agent repeats mistakes with a feedback signal -> Reflexion.
- Reasoning models (o-series style): give a clear goal and constraints and skip manual CoT. The repo says so, though other pages recommend CoT generally. Treat CoT as for non-reasoning models.

## Cautions

- Treat repo example outputs as illustrations, not benchmarks. Many came from retired models at temperature 1.
- Known bugs in repo examples: the PAL date exemplar returns `today.strftime` instead of `later.strftime`; the self-consistency bagels exemplar lacks its "The answer is" line; the function-calling notebook double-encodes tool arguments. The reference files carry corrected notes.
- Never `exec()` model output outside a sandbox (the PAL notebook does).
- Several technique pages (DSP, GraphPrompts, Active-Prompt, ART, multimodal CoT, meta-prompting) are stubs. The reference sketches for them are tagged "(not in repo)".
- Gaps in the guide: indirect prompt injection via tool output, MCP, structured outputs, evals, least-to-most, self-refine, chain-of-verification, chunking and reranking for RAG. Use current provider documentation for these.
- Agent and context-engineering pages are one course's opinion and carry promo callouts. Their prompt examples contradict each other (subtask counts, schema types).
