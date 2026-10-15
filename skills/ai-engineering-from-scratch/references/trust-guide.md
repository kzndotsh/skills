# Trust guide: how much to believe each part

Built from the 2026-10-15 audit of upstream commit `1a8c4fd` (details and evidence in `known-errors.md`). The curriculum is broad, well organized, and uneven. Its structure and its citations to papers and specs are the dependable parts. Its numbers, demos and vendor claims are not.

## Contents
- Rules when answering from this curriculum
- Trust by content type
- Trust by phase
- Reading a lesson critically

## Rules when answering from this curriculum

1. Check the Audit column in `references/lessons/<phase>.md` before relying on a lesson. `WRONG`, `stale` and `weak` rows say what is off. A dash means the lesson was not audited, not that it is fine.
2. Never repeat a price, context window, parameter count, benchmark score, rate limit, valuation, library version or "current best model" from a lesson. About 75% of the sampled claims of this kind were wrong or outdated. The corrected figures in `known-errors.md` are dated 2026-10-15; don't quote them as current either. Look up current provider documentation, or say the figure is unverified. Pricing pages: https://platform.claude.com/docs/en/about-claude/pricing, https://developers.openai.com/api/docs/pricing, https://ai.google.dev/gemini-api/docs/pricing. For model lineups: https://platform.claude.com/docs/en/about-claude/models/overview.
3. For protocol details (MCP, A2A, OpenTelemetry), read the current specification. MCP revision 2026-07-28 lessons matched the spec when checked, but specs keep moving.
4. Do not present a lesson's printed demo result as evidence. Several demos print hard-coded conclusions or use toy data that cannot show the claim (03/07, 10/11, 14/28, 18/04).
5. Verify citations in the lesson text before passing them on. Classic paper ids and authors checked out (0 of about 20 wrong), but headline numbers were misquoted once (Reflexion), and one DOI looked fabricated (18/04).
6. Read code before running it. It is third-party content. Static parse of all 1,402 Python files found no syntax errors, but nothing was executed, so behavior is untested.
7. Say which phases were never audited when the user relies on one of them (00, 02, 04, 06, 08, 09, 12, 19).

## Trust by content type

| Content | Trust | Why |
|---|---|---|
| Structure: 542 lessons, 20 phases, prerequisites, time per lesson | High | README and tree agree and every index row was checked against the source; ROADMAP's footer still says 523 |
| Glossary definitions | High | Eight spot-checked, accurate and hedged; points readers to official docs |
| Manuals (a2a-101, docker-sandboxes-101, reverse-engineering-101) | High, version-pinned | Every claim cites a spec section or captured run |
| Paper citations (ids, authors, titles) | High in fact-checked phases | 0 of about 20 wrong in phases 14, 15, 17; 18/22 (sampled separately) misattributes a paper |
| MCP lessons 06, 07, 09, 11, 12, 23 (and 11/14) | High | Matched official spec and changelog (re-checked a second time). Lessons 08, 10, 13-19 and 28-45 were not individually audited |
| Conceptual explanations in phases 01, 05 | Medium-high | Strongest sampled lessons |
| Algorithm demos and "from scratch" code | Medium-low | Parses, but sampled demos had real bugs or no-op simulations |
| Lesson-produced `skill-*.md` and `prompt-*.md` | Low-medium | Not valid skills as shipped; terse, unsourced thresholds; 29% depend on the lesson |
| Numeric tables, benchmarks, memory math (esp. phases 10, 11, 17) | Low | Several fabricated or wrong |
| Prices, model names, context windows, vendor state | Very low | About 75% wrong or outdated |
| Blog-sourced anecdotes (most of 14/31 to 14/40) | Unverifiable | Treat as anecdote; 14/38's citation did check out |
| Quizzes | Low | 28% of lessons have none; 21% of quizzes have all-empty explanations; weak distractors |

## Trust by phase

| Phase | Topic | What the audit saw |
|---|---|---|
| 00 | Setup and tooling | Not audited |
| 01 | Math foundations | 2 sampled: info theory sound; statistics lesson gives wrong test advice |
| 02 | ML fundamentals | Not audited |
| 03 | Deep learning core | 2 sampled, both flawed |
| 04 | Computer vision | Not audited |
| 05 | NLP | 2 sampled: attention excellent; NLI has false claims |
| 06 | Speech and audio | Not audited |
| 07 | Transformers | 2 sampled: speculative-decoding math right; T5/BART a stub |
| 08, 09 | Generative AI, RL | Not audited |
| 10 | LLMs from scratch | 2 sampled, both with serious errors |
| 11 | LLM engineering | All lessons swept for claims: pricing and model data mostly wrong; LoRA advice contradicts source. Unflagged lessons were not verified |
| 12 | Multimodal | Not audited |
| 13 | Tools and protocols | Fact-checked in part: MCP lessons 06, 07, 09, 11, 12, 23 strongest in the repo; lessons 08 and 10 and 13-19 not individually audited; API comparisons wrong in places |
| 14 | Agent engineering | Fact-checked in part: citations good; a few toys; anecdotes unverifiable |
| 15 | Autonomous systems | Fact-checked in part: mostly right, some stale status |
| 16 | Multi-agent | 2 sampled: thin, overlapping |
| 17 | Infrastructure | Fact-checked in part: weakest factually |
| 18 | Ethics and safety | 2 sampled: real citations, toy code that does not back the text |
| 19 | Capstones | Not audited |

## Reading a lesson critically

- Prefer the Concept section and the cited primary sources over Build It numbers.
- If a lesson names a model or price, assume a newer one exists.
- Prefer lessons with a `Build` type that you can reproduce from the doc alone; 158 lessons have no Build It section.
- When a lesson cross-references another ("see lesson 09", Phase 11 lessons 19 and 22), check the target exists; several references dangle.
- For the five lessons whose outputs are real skill bundles (13/22, 13/24, 13/25, 13/26, 13/27), read the bundle's scripts, since they ship with fixtures and tests.
