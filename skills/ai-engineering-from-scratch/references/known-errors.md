# Known errors and stale claims

Verified 2026-10-15 against primary sources (vendor docs, arXiv, official specs) for upstream commit `1a8c4fd`. Paths are `phases/<PP-...>/<NN-...>`; shorthand `PP/NN` matches the Audit column in `references/lessons/`. Anything not listed here was not audited, which is not the same as being correct.

## Contents
- Audit coverage and error rate
- Outright errors (with correction)
- Outdated
- Weak or misleading demos
- Unverifiable
- Reliable material

## Audit coverage and error rate

- Fact-check: 76 lessons swept with claim-extraction searches (versions, dates, arXiv ids, prices, percentages, model names), then dense passages read. 66 claims tabulated, 52 checked against a primary source. About 39% were wrong or outdated. For price, model and vendor-state claims about 75%; for arXiv ids, authors and titles 0 of about 20 wrong.
- Lesson depth sample: 18 lessons read in full (docs, code, quiz, outputs) across phases 01, 03, 05, 07, 10, 11, 14, 16, 18. Every one had at least one checkable error; 8 had a serious conceptual or code error; about 6 had fabricated or unsourced numeric tables. Python files parse; nothing was executed.
- Not audited: phases 00, 02, 04, 06, 08, 09, 12, 19 and most of 05, 07, 16, 18. A second pass re-checked the audit itself: scripted checks matched all 542 index rows to the source, and independent agents confirmed the flags against the lesson text and the corrections against primary sources (details in the audit notes, not shipped).

## Outright errors (with correction)

Corrections for prices, model sizes and context windows were true on 2026-10-15 and will drift. Use them to see that a lesson is wrong, then check current provider documentation before quoting any number.

| Lesson | Claim in lesson | Correct |
|---|---|---|
| 14/03 | Reflexion gives a "130% improvement" on AlfWorld | Paper reports +22% absolute; 130 is tasks solved out of 134 |
| 14/09 | Mem0 paper reports LoCoMo 91.6, LongMemEval 93.4, BEAM 64.1 | Not from the 2025 paper (it reports about 26% relative gain and 91% lower p95 latency); they came from Mem0's own evaluation docs, which now list different values. The arXiv id itself is correct |
| 17/03 | "DeepSeek-V3 67B" | 671B total, 37B active |
| 17/07 | H100+vLLM $0.09/M vs GB200+Dynamo $0.012/M is "7x" | Misreads SemiAnalysis InferenceX: the $0.012 figure belonged to a GB200 vs MI325X comparison, and the cost ratio depends on one operating point (tokens/s per user). Re-check the live benchmark pages before quoting any ratio |
| 11/11 | Opus 4.7 $15/$75; GPT-5 $5/$15; Gemini 3 Pro $1.25/$5 | Opus 4.7 $5/$25; GPT-5 $1.25/$10 (both confirmed 2026-10-15; the model lineup has since moved on). Gemini 3 Pro's price was also wrong and the model has been retired, with 3.1 Pro listed at about $2/$12 |
| 11/05 | Opus 4.7 has a 200K window; Gemini 3 Pro 2M | 1M standard on current lineup; Gemini 3 Pro 1M |
| 11/04 | Gemini Embedding 2 $0.15/M | $0.20/M text |
| 13/01 | Parallel tool use is opt-in on Anthropic | Default (and contradicts 13/02) |
| 13/20 | OTel GenAI semantic conventions are stable (v1.37+) | Still status Development |
| 01/15 | Wilcoxon test for 5 CV folds | Minimum two-sided p is 0.0625; cannot reach 0.05 |
| 05/21 | RAGAS and RAG evals use NLI | They use LLM judges |
| 10/02 | Llama uses SentencePiece; "space maps to G"; several other tokenizer facts | Llama 3 uses tiktoken-style BPE; the byte is U+0120; non-ASCII text is silently dropped if the `regex` package is missing |
| 10/11 | Benchmark table; "70B INT4 on a 24 GB GPU" (in the lesson's `outputs/skill-quantization.md`; the doc only says "single consumer GPU"); 70B/32K KV cache is 40 GB (doc line 118) | Table unsourced and implausible; 70B INT4 is about 35 GB; GQA KV cache is about 10.7 GB |
| 11/08 | q+v LoRA targets are the sweet spot; "NF4" quantizer; full fine-tune of 8B needs "56GB" | QLoRA paper found all linear layers needed; the lesson's "NF4" is uniform int4; its own parts (16+16+32 GB) sum to 64 GB before activations; quiz parameter count (about 80M at r=16) is wrong |
| 18/22 | Cites "Kowalczyk et al." arXiv 2503.06808 | That is "Privacy Auditing of Large Language Models" by Panda, Tang, Nasr, Choquette-Choo, Mittal |

## Outdated

| Lesson | Claim | Now |
|---|---|---|
| 13/02 | Anthropic has no strict-mode flag | `strict: true` on tools exists (grammar-constrained) |
| 11/15 | Anthropic minimum cacheable 1,024 / 2,048 tokens; OpenAI caching = 50% off | Minimums vary by model (512 to 4,096); GPT-5 cached input is 90% off |
| 14/01, 11/17 | AutoGen v0.4 as a current harness | Maintenance mode; Microsoft Agent Framework is the successor; ConversableAgent is the v0.2 API |
| 15/01 | METR doubling time near seven months; Opus 4.6 as the horizon | TH1.1 reports about 4 months; two model generations newer exist |
| 15/08 | DeepMind Frontier Safety Framework v3 | v3.1 published April 2026 |
| 17/01 | Claude 3.7 Sonnet, Gemini 2.5, GPT-5 as current | Several generations newer |
| 17/02 | Fireworks valued at $4B | Reported about $17.5B (July 2026) |
| 17/04 | vLLM v0.18.0 feature matrix | PyPI is at 0.29 or newer |
| 11/09, 11/10, 15/06 | Opus 4.6 and GPT-5 as frontier or judge models | Replaced by newer releases |

## Weak or misleading demos

- 03/07: doc's backward pass omits the dropout mask; the demo data cannot overfit; the "conclusion" print is hard-coded.
- 03/12: JIT benchmark times eager code without `block_until_ready`, so the speedup is bogus.
- 07/08: Build It is a stub, with no cross-attention code and no quiz.
- 10/11: simulated AWQ is a mathematical no-op; simulated GPTQ is not GPTQ; the sensitivity experiment adds Gaussian noise rather than quantizing.
- 14/17: no real Claude Agent SDK code; the "parallel" subagents run sequentially.
- 14/28: every "pattern" reuses one keyword `classify()`, and the printed conclusions are hard-coded.
- 16/04: the lesson says the three orchestrators differ, but its code makes all three produce the same message pool; no quiz.
- 18/04: the doc says alpha 0.3-0.5 restores near-base-model sycophancy, but the code's own takeaway says no alpha does without cost; one Science DOI looks fabricated.
- 05/10 cites lesson 09 numbers (89% at length 5 to chance at 80) that do not exist.

## Unverifiable

Blog- or anecdote-sourced statistics in 14/31 to 14/40 (position bias about 40%, verbosity about 15%, "88 AGENTS.md", "52% to 21%"), the AMBIG-SWE numbers in 14/32 (no citation in the lesson), and Cloudflare code-review figures in 14/39 (the lesson cites Cloudflare's blog but we could not retrieve it). Treat as anecdote. Exception: 14/38's arXiv citation checked out.

## Reliable material

- MCP revision 2026-07-28 content in 13/06, 13/07, 13/09, 13/11, 13/12, 13/23 and 11/14 matched the official spec and changelog on every detail checked (stateless requests, `server/discover`, error codes -32020/-32021/-32022, `ttlMs` and `cacheScope`, MRTR, deprecations, tasks extension; `tasks/cancel` not checked).
- Paper citations in 14/01 to 14/10, 15/03 to 15/05, 17/06, 17/09, 17/10 (ReAct, ReWOO, Reflexion, ToT, LATS, Self-Refine, CRITIC, Toolformer, MemGPT, Voyager, AlphaEvolve, DGM, AI Scientist-v2, SGLang, AWQ, GPTQ): ids, authors and headline figures were re-checked a second time against arXiv and matched, apart from the Reflexion and Mem0 misreads above. 18/22 (sampled separately) misattributes a paper, so cite-check anywhere else.
- 05/10 (attention) was the strongest lesson sampled: worked example verified by hand.
