# Audit Summary: dair-ai/Prompt-Engineering-Guide (commit 5767372, 2026-03-11)

Scope audited: all ~134 English pages, `guides/*.md` legacy files, 12 notebooks, lecture PDF (text only; image-only slides on PAL, ReAct and injection not captured), README, CITATION, site config. 100k words. Other-language translations were not audited.

## Contents
1. Overall verdict
2. Stale content
3. Errors in examples and code
4. Contradictions
5. Gaps
6. Stub pages
7. Repo hygiene
8. How to use the guide safely

## 1. Overall verdict
Concepts (zero/few-shot, CoT, self-consistency, chaining, RAG, ReAct, injection taxonomy) remain valid. Concrete model advice, benchmark numbers, prices, API code, and example outputs are mostly 2022 to early 2024. Only Kimi K2.5 (models) and the context-engineering/agents pages are from 2025-2026.

## 2. Stale content
- Models section: vendor-reported benchmarks for GPT-4, Gemini, Claude 3, Mistral, Llama, Mixtral. Not usable for model choice.
- Code uses removed APIs: `openai.ChatCompletion`/`Completion.create`, text-davinci-003, gpt-4-1106-preview, `google.generativeai` with gemini-pro/1.5, `mistralai` v0 `MistralClient`, old Fireworks clients, old LangChain agents/imports, retired Code Llama endpoints.
- deep-research and 4o-image guides: o1-mini vs GPT-4o advice, April 2025 usage quotas, DALL-E 3 workarounds.
- applications: 2023 prices, GPT-4o fine-tuning promo valid until Sep 2024, no training-data format.
- Risks pages: text-davinci-003 era; DAN/simulator examples are screenshots and unreproducible.
- papers.en.mdx ends June 2024. README, readings, tools, courses frozen near 2023.

## 3. Errors in examples and code
- PAL date exemplar 4 returns `today.strftime` instead of `later.strftime` (pages and legacy guides; the PAL notebook has a similar wrong-variable exemplar).
- Self-consistency bagels exemplar missing its "The answer is" line; legacy guide has a truncated Olivia exemplar and a wrong "3/1/2002" line (fixed in pages/).
- Generated-knowledge demo: the "bad" knowledge is actually correct.
- Mixtral page: "32 tokens" context (should be 32K), "Llama 2 80B", safe_mode example calls the non-safe function.
- GPT-4 page contradicts itself on vision support and knowledge cutoff.
- Function-calling notebook double-encodes tool arguments.
- Context-caching notebook: wait loop assigns an unused variable; TTL comment says 5 min, code uses 15.
- Mixtral notebook: `safe_mode` defined but unused. Code Llama "infilling" isn't infilling.
- PAL notebook runs `exec()` on model output with no sandbox.
- Lecture slides: odd-number few-shot slide answers True (correct is False); zero-shot CoT apples slide self-contradicts.
- Legacy wine-review NER example: invalid JSON, unreliable offsets.
- Agents guide: Search Planner prompt says 2 subtasks while the deep-dive says 3 and the case study says 3-5; sample JSON has `priority: 1.2` against a declared int.
- papers.en.mdx: one arXiv ID shared by two papers, wrong or conflicting dates, malformed links.
- RAG notebook needs `ml-potw-10232023.csv` and caching notebook needs `weekly-ai-papers.txt`; neither is in the repo.
- Intro says examples ran at temperature=1 while advice is low temperature for factual tasks.

## 4. Contradictions
- reasoning-llms: avoid manual CoT on reasoning models. optimizing-prompts: recommends CoT/ReAct generally.
- deep-agents page dismisses the "don't build multi-agents" argument without evidence, conflicting with its own advice to hand sub-agents only the query.
- courses.en.mdx says "both courses"; nav lists six. notebooks page lists 5 of 12 notebooks.
- Mistral 7B page shows injections succeeding despite its guardrail prompt; Code Llama refuses harmless requests under a safety system prompt.

## 5. Gaps
Indirect prompt injection via tool output, agent/tool privilege, MCP, compaction and token budgeting, structured outputs, evals, least-to-most, self-refine, chain-of-verification, RAG chunking/reranking, social-bias coverage. The promised hybrid workflow+agent example and "Advanced context engineering [WIP]" section are missing. Optimizing-prompts has no examples; the "Top Reasoning Models" section is only a spreadsheet link.

## 6. Stub or thin pages
dsp ("coming soon"), graph, activeprompt, multimodalcot, art, meta-prompting (image only), coding application (empty sections), many research pages (paper blurbs, screenshots carry the substance).

## 7. Repo hygiene
CLAUDE.md references a `Prompt-Engineering-Guide-notes/` directory absent from the clone. package.json is still the Nextra template. Course-promo callouts appear on agents and research pages.

## 8. How to use the guide safely
- Take techniques and templates; re-verify against current provider docs for any model, price, limit, or API call.
- Re-run examples before citing outputs. Don't quote benchmarks for model selection.
- Sandbox any model-generated code.
- Cross-check the repo's own advice against the contradictions above before applying it.
