# Research notes (from dair-ai Prompt-Engineering-Guide: pages/research/*, pages/research.en.mdx, pages/papers.en.mdx)

Most pages are short summaries (2024) of one paper or survey. Where the repo gives no recipe, "Takeaway" is the practical lesson; additions from general knowledge are marked (not in repo). Dates are as stated in the repo; model names in findings are of the time.

## Table of contents
1. RAG (rag.en.mdx, 44 KB survey) - paradigms, components, techniques, evaluation, paper table
2. RAG-related short pages: rag-faithfulness, rag_hallucinations, llm-recall
3. LLM agents (llm-agents.en.mdx)
4. Reasoning: llm-reasoning, guided-cot, thoughtsculpt
5. Other: llm-tokenization, trustworthiness-in-llms, synthetic_data, infini-attention, groq
6. papers.en.mdx index grouped by topic
7. Audit notes

---------------------------------------------------------------------------

## 1. Retrieval Augmented Generation - pages/research/rag.en.mdx
Source: Gao et al. 2023, "Retrieval-Augmented Generation for LLMs: A Survey" (arXiv 2312.10997). Page is a digest + a table of ~50 papers.

### Basic pipeline (use when: knowledge-intensive or fast-changing facts, domain data; prefer over retraining)
1. Indexing: chunk documents -> embed chunks -> store in vector index.
2. Retrieval: embed query, fetch top-k similar chunks.
3. Generation: concatenate retrieved chunks with the original prompt; LLM answers.
RAG vs fine-tuning (survey): RAG injects NEW/updated knowledge; fine-tuning improves internal knowledge, output format/tone/style and complex instruction following; they are complementary; prompt engineering also helps. No retraining needed for RAG.

### Paradigms
- Naive RAG: index -> retrieve -> generate. Failure modes: low precision (misaligned chunks), low recall (missing chunks), stale info, redundancy/repetition when augmenting, style reconciliation across passages, model over-relying and just parroting the retrieved text.
- Advanced RAG: optimize pre-retrieval (data granularity, index structure, metadata, alignment, mixed retrieval), retrieval (fine-tuned or dynamic embeddings) and post-retrieval (re-ranking, moving relevant context to prompt edges, recomputing similarity, prompt/context compression).
- Modular RAG: swappable modules (search, memory, fusion, routing, predict, task adapter); Naive and Advanced are special cases. Techniques: hybrid search (keyword + semantic), recursive retrieval (small chunks first then larger parents), StepBack prompting (abstract to principles before answering; arXiv 2310.06117), sub-queries / sub-question engines (LlamaIndex), HyDE (embed an LLM-written hypothetical answer instead of the query; arXiv 2212.10496).

### Retrieval component
- Chunking: depends on content/app; sentence-transformers do better on single sentences, text-embedding-ada-002 better with 256-512 token blocks; experiment (DATED embedding model names).
- Fine-tune embedding models for specialized domains (example: BGE-large-EN from BAAI).
- Query-document alignment: query rewriting (Query2Doc, ITER-RETGEN, HyDE), embedding transformation.
- Retriever-LLM alignment: fine-tune retrievers with LLM feedback (AAR, REPLUG, UPRISE); adapters (PRCA, RECOMP, PKG).

### Generation/augmentation
- Frozen LLM: post-retrieval compression and reranking. Or fine-tune the generator to use retrieved context.
- When to augment: pre-training (RETRO), fine-tuning, inference.
- Sources: unstructured, structured, LLM-generated.
- Process: iterative retrieval (multiple rounds; RETRO, GAR-meets-RAG), recursive retrieval (IRCoT, Tree of Clarifications), adaptive retrieval (decide when/what to retrieve: FLARE, Self-RAG).

### Evaluation
- Downstream task metrics (EM, F1); retrieval metrics (NDCG, Hit Rate).
- Three quality scores: context relevance, answer faithfulness, answer relevance. Four abilities: noise robustness, negative rejection, information integration, counterfactual robustness.
- Benchmarks: RGB, RECALL. Tools: RAGAS, ARES, TruLens, RaLLe. Several use an LLM as judge.

### Open challenges (survey)
Context length vs RAG, robustness to counterfactual/adversarial docs, RAG+fine-tune hybrids, scaling laws, production concerns (security, privacy, efficiency), multimodal RAG, evaluation.

### Notable table entries (insights by paper, repo's 'RAG Research Insights')
- Corrective RAG (CRAG, Jan 2024): retrieval evaluator grades retrieved docs; fall back to web search; self-correction.
- RAPTOR (Jan 2024): recursively cluster+summarize chunks into a tree; retrieve at multiple abstraction levels for long docs.
- Chain-of-Note (Nov 2023): write reading notes per retrieved doc before answering; robust to noise/unknowns.
- Token elimination for readers (Oct 2023): up to 62.2% runtime cut, 2% perf drop.
- Self-RAG (Oct 2023): reflection tokens; adaptive retrieval + self-critique.
- RECOMP (Oct 2023): compress retrieved docs into summaries before in-context use.
- "Retrieval meets Long Context LLMs" (Oct 2023): 4K-context LLM with retrieval matches 16K-context (positional-interpolated) fine-tuned LLM on long-context tasks.
- RA-DIT (Oct 2023): two-step instruction tuning (LM to use context; retriever to match LM preferences).
- Making RAG robust to irrelevant context (Oct 2023): train with mixed relevant/irrelevant contexts.
- Lost in the Middle (Jul 2023): accuracy drops when relevant info sits mid-context -> order/rerank so key passages are at the start/end.
- FLARE (May 2023): predict next sentence, if low-confidence tokens, use it as a query and regenerate.
- Rewrite-Retrieve-Read (May 2023): train small rewriter via RL from black-box LLM feedback.
- IRCoT (Dec 2022): interleave retrieval with CoT steps for multi-step QA.
- GenRead (generate-then-read), Recitation-augmented LMs: let the LLM write its own context.
- Long-tail knowledge (Nov 2022): retrieval compensates for facts rare in pretraining.
- Classics: RAG (Lewis et al., May 2020), DPR (Apr 2020), Atlas, RETRO (Dec 2021), HyDE (Dec 2022), DSP (Dec 2022).
- RAG tools named: LangChain, LlamaIndex, DSPy, Flowise, Haystack, Meltano, Cohere Coral, Weaviate Verba, Amazon Kendra (DATED list).

Practical takeaways (prompting/RAG):
- Retrieval quality dominates; start with chunking + hybrid search + reranking before touching the generator.
- Put the most relevant chunks first/last; compress or filter noisy chunks; label sources.
- Add an abstain path ("answer only from context, else say unsure"; see models.md ChatGPT QA template) and evaluate negative rejection and counterfactual robustness.
- Measure retrieval and generation separately (context relevance / faithfulness / answer relevance).
- Use multi-step/iterative retrieval for multi-hop questions; single-shot retrieval is not enough.

Caveats: the page contains two promotional callouts for dair.ai courses (with a discount code) - ignore. Many images carry the actual taxonomy/metrics tables (not text). Several tool names/models are dated (ada-002).

---------------------------------------------------------------------------

## 2. Short RAG/recall pages

### How faithful are RAG models? (rag-faithfulness; Wu et al. 2024, arXiv 2404.10198)
- Finding: quantifies tug-of-war between retrieved context and the model's internal prior (GPT-4 and others on QA). Correct retrieved context fixes most errors (94% accuracy). When documents contain more wrong values and the model's prior is weak, the model repeats the wrong info; with a strong prior it resists. The more the retrieved value deviates from the prior, the less likely the model is to adopt it.
- Takeaway: RAG is only as reliable as retrieved content; wrong docs can override correct knowledge on weak-prior topics. Validate/score retrieved docs, prefer authoritative sources, test with contradicting/incorrect context.

### Reducing hallucination in structured outputs via RAG (rag_hallucinations; ServiceNow, arXiv 2404.08189)
- Finding: small LM + very small retriever RAG for natural-language-to-workflow (JSON) generation reduces hallucination (invalid steps/tables) and enables low-resource deployment.
- Takeaway: retrieve valid schema elements/examples for structured output (JSON); small models suffice; page suggests speculative decoding and YAML instead of JSON as further optimizations (YAML cheaper in tokens; ties to the tokenization note).

### LLM in-context recall is prompt dependent (llm-recall; Machlab & Battle 2024, arXiv 2404.08865)
- Finding: needle-in-a-haystack across several LLMs shows recall varies with context length and needle depth, and small prompt changes move recall significantly; training-data/prompt interplay can degrade responses. Recall improves with larger size, better attention, training strategy and fine-tuning.
- Takeaway: do not assume long-context recall is uniform; evaluate your own prompt/needle/position; keep a continuous eval protocol; do not trust vendor "near-perfect NIAH".

---------------------------------------------------------------------------

## 3. LLM Agents - pages/research/llm-agents.en.mdx
Digest of Wang et al. 2023 survey (arXiv 2308.11432) and others.

### Architecture (when you need an agent vs LLM vs RAG)
Escalation example: simple fact -> LLM alone; missing knowledge -> RAG; multi-part analytic question needing search, databases, code interpreter, charting -> agent (planning + tools + memory).
Core components:
- Agent/brain: general LLM activated by a prompt template describing operation + tools; optional profile/persona (handcrafted, LLM-generated, or data-driven).
- Planning without feedback: task decomposition via CoT (single path) or Tree of Thoughts (multi path).
- Planning with feedback: iteratively reflect/refine from observations: ReAct (loop Thought -> Action -> Observation, N times) and Reflexion; feedback may be environment, human or model.
- Memory: short-term (in-context, bounded by window), long-term (external vector store with fast retrieval), hybrid; formats: natural language, embeddings, databases, structured lists (GITM uses key=text, value=embedding).
- Tools: Wikipedia/search APIs, code interpreter, math engines, DBs, other models. Approaches: MRKL (LLM + expert modules), Toolformer (fine-tune to call APIs), function calling (tool API definitions in request), HuggingGPT (LLM as planner over HF models).

### Notable agents/frameworks listed (DATED, 2023)
ChemCrow, Generative Agents, AgentSims, ChatDev/MetaGPT/ToolLLM, D-Bot, OS-Copilot, Boiko et al., Blind Judgement, EduChat, CodeHelp, IELLM; frameworks LangChain, AutoGPT, AutoGen, Langroid, OpenAgents, LlamaIndex, GPT Engineer, DemoGPT, GPT Researcher, AgentVerse, crewAI, Phidata, BMTools.

### Evaluation
Human annotation, Turing test, metrics (success, human-similarity, efficiency), protocols (simulation, social, multi-task, software testing), benchmarks: ALFWorld, AgentBench, WebShop, WebArena, ToolBench, Mobile-Env, ClemBench, SocKET, GentBench, E2E, etc.

### Challenges (practical failure modes)
Role-playing fidelity; long-horizon planning errors that agents cannot recover from + finite context; value alignment; prompt robustness (a multi-prompt framework amplifies small prompt-change sensitivity; hallucination across module interfaces); knowledge boundary (model's internal knowledge biases simulations); efficiency/cost (many LLM calls).

Practical takeaways: keep prompts per module minimal and test sensitivity; give the agent explicit tool descriptions; use feedback loops (ReAct/Reflexion) for tasks needing trial-and-error; manage memory explicitly; budget calls/latency. See Kimi K2.5 notes in models.md for the parallel-orchestrator pattern (isolated subagent contexts, return only relevant outputs).
Caveats: page has dair.ai course promo callout; "Math Agents" and "Boiko et al." links are empty; "Wang et al. 2023" referenced without link in one place; the framework list is 2023 (many tools superseded; missing current agent SDKs/MCP).

---------------------------------------------------------------------------

## 4. Reasoning

### LLM Reasoning overview - llm-reasoning.en.mdx
- Surveys: Sun et al. 2023 (reasoning with foundation models, multimodal & agents; arXiv 2312.11562); Qiao et al. 2023 (reasoning with LM prompting; strategies = prompt engineering, process optimization, external engines; single-stage prompting e.g. CoT, Active-Prompt; arXiv 2212.09597); Huang & Chang 2023 (towards reasoning in LLMs; arXiv 2212.10403: fine-tuning on explanations, CoT, decomposition, in-context learning).
- Debate: Kambhampati 2024 (arXiv 2403.04121) - position that LLMs do "universal approximate retrieval", not reasoning/planning as normally understood; web-scale training can be mistaken for reasoning.
- Takeaway: do not assume reasoning transfers to novel planning tasks; add verification/external solvers/tools (not in repo: especially for planning/search problems).
- Caveats: the Huang et al. link is empty in the text; also the figure source for the first image cites 2212.09597 (Qiao) not Sun et al. (the figure and cited paper do not match); "Huang et al. (2023)" is actually Huang & Chang. Dated 2023-early 2024; no coverage of reasoning-trained models (o1-style, thinking modes).

### LM-guided chain-of-thought - guided-cot.en.mdx (Lee et al. 2024, arXiv 2404.03414)
- Finding: a small LM distilled from a large LM's rationales (then RL-tuned with rationale- and task-oriented rewards) generates rationales; a frozen large LM then predicts the answer. Better than standard prompting and CoT on multi-hop extractive QA; self-consistency adds more.
- Takeaway: split rationale generation (small, tunable model) from answering (large frozen model); ask which sub-skill you really need the large model for.

### ThoughtSculpt - thoughtsculpt.en.mdx (Chi et al. 2024, arXiv 2404.05966)
- Finding: graph-style reasoning with iterative self-revision plus Monte Carlo Tree Search; components: thought evaluator (feedback on partial outputs), thought generator (new candidates), decision simulator (rolls out lines of thought to estimate path value). Suited for open-ended generation, multi-step reasoning, creative ideation (tasks decomposable into components).
- Takeaway: generate -> evaluate -> revise loops with search beat single-pass for decomposable creative tasks (cf. Tree of Thoughts, Graph of Thoughts in techniques files).

---------------------------------------------------------------------------

## 5. Other research pages

### LLM Tokenization - llm-tokenization.en.mdx (Karpathy lecture)
Behaviors traced to tokenization (BPE): spelling failures, string reversal, poor non-English (e.g. Japanese), bad arithmetic, GPT-2 weak at Python (whitespace), halting on `<|endoftext|>`, "trailing whitespace" warnings, SolidGoldMagikarp glitch tokens, and "prefer YAML over JSON" (fewer tokens). Takeaway: when a prompt underperforms, check how the key terms/acronyms/numbers tokenize (Tiktokenizer); structure/format affects token count and reliability; do not ask LLMs for character-level manipulation without tools (not in repo: use code execution).

### Trustworthiness in LLMs - trustworthiness-in-llms.en.mdx (Sun et al. 2024, TrustLLM, arXiv 2401.05561)
- 8 dimensions proposed (benchmark across 6: truthfulness, safety, fairness, robustness, privacy, machine ethics); 16 LLMs, 30+ datasets.
- Findings: proprietary models generally more trustworthy than open-source (gap closing); GPT-4 and Llama 2 reject stereotypes and resist adversarial attacks; some models (Llama 2) over-calibrated toward safety, refusing benign prompts. Truthfulness hurt by noisy/outdated data, improved with external knowledge (RAG); fairness: GPT-4 ~65% on stereotype recognition; robustness varies widely in open-ended/OOD; privacy: leakage on Enron emails; ethics: basic moral grasp, weak on complex cases.
- Takeaway: in high-stakes uses, ground with retrieval, test refusals vs over-refusals, run an eval kit (github.com/HowieHwong/TrustLLM) and check the leaderboard. Dated (16 models, early 2024).

### Synthetic data - synthetic_data.en.mdx (Google DeepMind et al., arXiv 2404.07503)
Overview of synthetic data for LMs: applications, challenges, future directions. Takeaway: creating synthetic data is easy; ensuring quality, factuality, fidelity, unbiasedness, trustworthiness and privacy is the hard part; validate before training.

### Infini-attention - infini-attention.en.mdx (Google, arXiv 2404.07143)
Compressive memory added to vanilla attention (local masked attention + long-term linear attention in one block); bounded memory/compute for unbounded inputs; 114x memory compression; 1B model scaling to 1M sequence, 8B new SOTA on 500K-token book summarization. Takeaway: architecture-level, no prompt guidance; signals long-context memory direction.

### Groq - groq.en.mdx
Inference speed vendor note: Groq LPU inference engine, claimed 18x faster than other cloud providers on Anyscale LLMPerf (Llama 2 70B, Mixtral 8x7B at the time); metrics: output tokens/s, time-to-first-token (TTFT) matter for streaming UX. Takeaway: latency metrics to track. Pure vendor claim from early 2024; charts are images; pricing/speed numbers stale.

---------------------------------------------------------------------------

## 6. papers.en.mdx - index grouped by topic (curated; ~420 entries in source, long tail omitted)
Source file is a flat list of arXiv links with month/year, in four sections: Overviews, Approaches, Applications, Collections. Latest entry is June 2024 (The Prompt Report). Below, only the load-bearing papers, regrouped by topic. (Titles abbreviated.)

### Surveys / overviews
The Prompt Report (Jun 2024, 2406.06608); Prompt Design and Engineering: Intro & Advanced (Jan 2024); Hallucination in LLMs survey (Nov 2023); A Survey of LLMs (Apr 2023, 2303.18223); Survey for In-context Learning (Dec 2022); Towards Reasoning in LLMs (Dec 2022); Reasoning with LM Prompting (Dec 2022); Augmented Language Models survey (Feb 2023); Tool Learning with Foundation Models (Apr 2023); Emergent Abilities of LLMs (Jun 2022); Pre-train, Prompt, and Predict (Jul 2021); Harnessing LLMs in Practice (Apr 2023); Jailbreaking ChatGPT via Prompt Engineering (May 2023); Few-shot Fine-tuning vs In-context Learning (May 2023).

### Core prompting techniques (zero/few-shot, CoT, decomposition)
GPT-3 / Language Models are Few-Shot Learners (May 2020); Rethinking the Role of Demonstrations (Feb 2022); Calibrate Before Use (Feb 2021); Fantastically Ordered Prompts (Apr 2021); Prompt Programming for LLMs (Feb 2021); Chain of Thought Prompting (Jan 2022); Zero-shot CoT "Let's think step by step" (May 2022); Self-Consistency (Mar 2022); Automatic CoT (Oct 2022); Active Prompting with CoT (Feb 2023); Synthetic Prompting (Feb 2023); Multimodal CoT (Feb 2023); Plan-and-Solve (May 2023); Least-to-most-style: Decomposed Prompting (Oct 2022), Successive Prompting (Dec 2022); Maieutic Prompting (May 2022); Generated Knowledge Prompting (Oct 2021); Directional Stimulus Prompting (Feb 2023); Re-Reading Improves Reasoning (Sep 2023); Analogical Prompting (Oct 2023); EchoPrompt (Sep 2023); Chain of Density summarization (Sep 2023); "According to ..." prompting (May 2023); Prompting with Pseudo-Code Instructions (May 2023); Principled Instructions Are All You Need (26 prompting principles, Dec 2023); Tab-CoT (May 2023); Chain-of-Symbol (May 2023).

### Search / structured reasoning
Tree of Thoughts (May 2023); LLM-Guided ToT (May 2023); Graph of Thoughts (Aug 2023); Skeleton-of-Thought (Jul 2023); Reasoning with LM is Planning with World Model (May 2023); Chain-of-Verification (Sep 2023); Self-Refine (Mar 2023); Reflexion (Mar 2023); Let's Verify Step by Step (May 2023); Self-Verification (Dec 2022); CRITIC (May 2023); Multiagent Debate (May 2023); Boosted Prompt Ensembles (Apr 2023); Adaptive-Consistency (May 2023); Thought Propagation (Oct 2023); Contrastive Decoding Improves Reasoning (Sep 2023).

### Program / tool-aided reasoning and agents
PAL (Nov 2022); MathPrompter (Mar 2023); Logic-LM (May 2023); Satisfiability-Aided LMs (May 2023); ReAct (Oct 2022); MRKL (May 2022); Toolformer (Feb 2023); ART (Mar 2023); ChatCoT (May 2023); MultiTool-CoT (May 2023); LLMs as Tool Makers (May 2023); Gorilla (May 2023); TaskMatrix.AI (Mar 2023); HuggingGPT (Mar 2023, in ChatGPT refs); CAMEL (Mar 2023); SwiftSage (May 2023); Tool-Interactive CRITIC (May 2023); Role-Play with LLMs (May 2023); PEARL (May 2023); Walking Down the Memory Maze (Oct 2023).

### Retrieval / knowledge augmentation
RAG (2020, in RAG page); Active RAG/FLARE (May 2023); Query Rewriting for RAG (May 2023); DSP (Dec 2022); Recitation-Augmented LMs (Oct 2022); Atlas (listed Nov 2022 but arXiv Aug 2022); Promptagator (Sep 2022); DocPrompting (Jul 2022); Check Your Facts and Try Again / LLM-Augmenter (Feb 2023); Context-faithful Prompting (Mar 2023); Augmented LLMs with Parametric Knowledge Guiding (May 2023); WikiChat (May 2023); LLMs Can Be Easily Distracted by Irrelevant Context (Feb 2023); UPRISE (Mar 2023).

### Prompt optimization / automation
Large Language Models Are Human-Level Prompt Engineers (APE, Nov 2022); AutoPrompt (Oct 2020); Hard Prompts Made Easy (Feb 2023); Evolutionary prompt optimizers (Sep 2023); Query-dependent prompt optimization with offline inverse RL (Sep 2023); Revisiting Automated Prompting (Apr 2023); LLMLingua prompt compression (Oct 2023); Batch Prompting (Jan 2023); FrugalGPT (May 2023); Self-Taught Optimizer STOP (Oct 2023); A Prompt Pattern Catalog (Feb 2023); TELeR taxonomy (May 2023); Reframing Instructional Prompts (Sep 2021).

### Soft/continuous prompts and tuning
Prefix-Tuning (Jan 2021); The Power of Scale for Parameter-Efficient Prompt Tuning (Apr 2021); PPT; Making PLMs Better Few-shot Learners / LM-BFF (Dec 2020/Aug 2021, listed twice); Multitask Prompt Tuning (Mar 2023); Progressive Prompts (Jan 2023); Universality and Limitations of Prompt Tuning (May 2023); many niche variants (visual, graph, speech, domain-specific) omitted.

### In-context learning theory / analysis
Larger LMs do ICL differently (Mar 2023); What ICL "learns" (May 2023); ICL as kernel regression (May 2023); Understanding ICL from repetitions (Sep 2023); Why think step-by-step? locality of experience (Apr 2023); Language Models Don't Always Say What They Think: unfaithful CoT (May 2023); Chain-of-Thought is a policy improvement operator (Sep 2023); Large LMs are Greedy Reasoners (Oct 2022); Show Your Work: Scratchpads (Nov 2021); Scaling Laws for Neural LMs (Jan 2020).

### Safety, alignment, robustness, injection
Constitutional AI (Dec 2022); InstructGPT (Mar 2022); Ignore Previous Prompt (Nov 2022); Prompt Injection threats to application-integrated LLMs (Feb 2023); Certifying LLM Safety against Adversarial Prompting (Sep 2023); Red-Teaming with Chain of Utterances (Aug 2023); Capacity for Moral Self-Correction (Feb 2023); On Second Thought, Let's Not Think Step by Step (CoT bias/toxicity, Dec 2022); Model-Written Evaluations (Dec 2022); NOTABLE backdoors (May 2023); GPT detectors biased against non-native writers (Apr 2023); Marked Personas (May 2023); Prompting GPT-3 to be Reliable (Oct 2022); Zero-resource hallucination: SelfCheckGPT (Mar 2023); hallucination survey (Nov 2023).

### Long context / efficiency
Efficient Streaming LMs with Attention Sinks (Sep 2023); Pause tokens (Oct 2023); Skeleton-of-Thought (Jul 2023); (see also Infini-attention, Lost in the Middle in RAG table).

### Multimodal / other domains (examples only)
The Dawn of LMMs: GPT-4V (Sep 2023); Visual CoT (May 2023); text-to-image prompt taxonomies (Apr 2022, Sep 2021); Midjourney/diffusion prompt engineering (Nov 2022, Feb 2023); code generation (Piloting Copilot and Codex Oct 2022; Dynamic Temperature Sampling Sep 2023; Think Outside the Code May 2023); text-to-SQL prompt studies (May 2023, several); medical/legal/finance (Med-PaLM Towards Expert-Level Medical QA May 2023; BloombergGPT Mar 2023; Legal Prompt Engineering Dec 2022).

### Collections (links)
Chain-of-Thought Papers (Timothyxxx/Chain-of-ThoughtsPapers); Papers with Code prompt-engineering task; thunlp/PromptPapers.

---------------------------------------------------------------------------

## 7. Audit notes (research + papers)
- research.en.mdx is only an intro plus an auto-generated listing; no content.
- Most research pages are 1-2 paragraph summaries with embedded YouTube iframes, so substance is thin; the full papers should be consulted for any recipe. Only RAG and llm-agents are substantive; both carry promotional course callouts to ignore.
- Staleness: nearly everything is Jan-Apr 2024 or older; no coverage of reasoning models, agentic coding tools, MCP, prompt caching, structured outputs, long-context 1M+ in production, computer use. Groq numbers and tool lists are dated.
- Possible errors/oddities: llm-reasoning has an empty link for "Huang et al. (2023)" and mismatched figure attributions; "Math Agents" and Boiko et al. links empty in llm-agents; rag_hallucinations suggests YAML-over-JSON without evidence; trustworthiness page says "The author proposed" (it is a survey with many authors) and mentions 8 dimensions but benchmarks 6.
- papers.en.mdx data issues: duplicates (Graph of Thoughts x2, From Sparse to Dense x3, Interactive NLP x2, Fact-Checking Complex Claims x2, Measuring Inductive Biases x2, Small LMs Improve Giants x2, The Capacity for Moral Self-Correction x2, Making PLMs Better Few-shot Learners x2); arXiv 2309.02772 used for both "Certifying LLM Safety" and "Improving Code Generation by Dynamic Temperature Sampling" (one is wrong); arXiv 2302.09236 is used for both "Scalable Prompt Generation for Semi-supervised Learning" and "Language Model Crossover"; "Enhancing Zero-Shot CoT through Logic" (2309.13339) dated Feb 2024 in Approaches but Sep 2023 in Applications; Atlas dated Nov 2022 between Sep 2022 entries; malformed link "Zero- and Few-Shot Event Detection via Prompt-Based Meta Learning]https://..."; typo "Mqy 2022" (PPT); "Assessing Language Model Deployment with Risk Cards" has no URL; the page claims daily/weekly updates but ends at Jun 2024; list is not strictly sorted by date; Approaches vs Applications classification is loose.
- Gaps: no summaries of what each paper contributes (technique files in the repo cover CoT, ToT, ReAct, etc.); for 2025-2026 methods you must look outside the repo (not in repo).
