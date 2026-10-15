# Learning paths

Source: `learning-paths/*.json` at commit `1a8c4fd`. Each path is an ordered lesson route with time estimates. Paths whose JSON lists `invocation` also exist as in-repo tutor skills. Hour estimates in the upstream README for the two longest routes are wrong; use the minutes below. The bracket after each lesson is its audit status (see trust-guide.md; labels: ok, clean, WRONG, stale, weak, unverified, not audited); optional lessons come last.

## Contents

- Agent Skills Engineering (`agent-skills`)
- Agent Systems Engineering (`agentic-ai-engineer`)
- AI Data Systems (`ai-data-engineer`)
- Developer Experience and Education (`ai-developer-relations-engineer`)
- AI Evaluation and Reliability (`ai-evaluation-reliability-engineer`)
- LLM Product Engineering (`applied-ai-engineer`)
- Building and Deploying AI Applications (`building-and-deploying-ai-applications`)
- Customer AI Deployment (`forward-deployed-ai-engineer`)
- Model Context Protocol (MCP) (`model-context-protocol`)
- Reverse Engineering (`reverse-engineering`)
- Product Judgment and Delivery (`shaping-the-build`)
- Software Engineering Fundamentals (`software-engineering-fundamentals`)
- Agent-Assisted Engineering (`using-coding-agents`)

## Agent Skills Engineering (`agent-skills`)

Build, route, secure, evaluate, package, and verify Agent Skills in real hosts.

Estimated 570 min (about 10 h), 5 required lessons, 1 optional.

1. `phases/13-tools-and-protocols/22-skills-and-agent-sdks` Agent Skills: Portable Contract and Runtime Boundary (90 min) [not audited]
2. `phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure` Skill Discovery and Progressive Disclosure (105 min) [ok: Skill catalog entry of about 100 tokens matches the Agent Skills spec]
3. `phases/13-tools-and-protocols/25-skill-invocation-and-routing` Skill Invocation and Routing (105 min) [not audited]
4. `phases/13-tools-and-protocols/26-skill-permissions-sandboxes-and-trust` Skill Permissions, Sandboxes, and Trust (120 min) [not audited]
5. `phases/13-tools-and-protocols/27-skill-evals-packaging-and-portability` Skill Evals, Packaging, and Portability (150 min) [ok: GitSkills dataset figures verified]
- (optional) `phases/13-tools-and-protocols/23-capstone-tool-ecosystem` Capstone: Stateless Tool Ecosystem (120 min, optional) [ok: Tasks-extension changes matched spec (tasks/cancel unchecked)]

## Agent Systems Engineering (`agentic-ai-engineer`)

Engineer tool-using agent loops with explicit context, memory, orchestration, safety, evaluation, and production control.

Estimated 865 min (about 14 h), 14 required lessons.

1. `phases/13-tools-and-protocols/01-the-tool-interface` The Tool Interface — Why Agents Need Structured I/O (45 min) [WRONG: Says parallel tool use is opt-in on Anthropic; it is the default]
2. `phases/13-tools-and-protocols/05-tool-schema-design` Tool Schema Design — Naming, Descriptions, Parameter Constraints (45 min) [not audited]
3. `phases/13-tools-and-protocols/06-mcp-fundamentals` MCP Fundamentals: Stateless Requests and JSON-RPC (55 min) [ok: MCP stateless details matched official spec and changelog]
4. `phases/14-agent-engineering/01-the-agent-loop` The Agent Loop: Observe, Think, Act (60 min) [stale: ReAct citation correct; lists AutoGen v0.4 as a current harness]
5. `phases/14-agent-engineering/06-tool-use-and-function-calling` Tool Use and Function Calling (60 min) [ok: Toolformer and BFCL V4 weights verified]
6. `phases/11-llm-engineering/05-context-engineering` Context Engineering: Windows, Budgets, Memory, and Retrieval (90 min) [stale: Context windows wrong or outdated for the Anthropic and Gemini models named]
7. `phases/14-agent-engineering/07-memory-virtual-context-memgpt` Agent Memory — Virtual Context and Memory Paging (75 min) [ok: MemGPT citation verified]
8. `phases/14-agent-engineering/13-langgraph-stateful-graphs` Stateful Graph Orchestration — Durable Execution and Checkpoints (75 min) [not audited]
9. `phases/14-agent-engineering/28-orchestration-patterns` Orchestration Patterns: Supervisor, Swarm, Hierarchical (60 min) [weak: Every 'pattern' reuses one keyword classifier; printed conclusions are hard-coded]
10. `phases/14-agent-engineering/26-failure-modes-agentic` Failure Modes: Why Agents Break (60 min) [not audited]
11. `phases/14-agent-engineering/27-prompt-injection-defense` Prompt Injection and the PVE Defense (75 min) [not audited]
12. `phases/14-agent-engineering/30-eval-driven-agent-development` Eval-Driven Agent Development (60 min) [not audited]
13. `phases/14-agent-engineering/29-production-runtimes` Production Runtimes: Queue, Event, Cron (60 min) [not audited]
14. `phases/14-agent-engineering/24-agent-observability-platforms` Agent Observability: Langfuse, Phoenix, Opik (45 min) [not audited]

## AI Data Systems (`ai-data-engineer`)

Build reliable data, feature, embedding, retrieval, evaluation, and observability pipelines for AI systems.

Estimated 915 min (about 15 h), 11 required lessons.

1. `phases/00-setup-and-tooling/09-data-management` Data Management (45 min) [stale: Says GitHub gives 1 GB free for Git LFS; GitHub's current Free plan lists 10 GiB storage…]
2. `phases/02-ml-fundamentals/08-feature-engineering` Feature Engineering & Selection (90 min) [WRONG: Citation title is wrong: the Micci-Barreca 2001 paper is 'A preprocessing scheme for high…]
3. `phases/02-ml-fundamentals/13-ml-pipelines` ML Pipelines (120 min) [stale: Presents MLflow registry stages (Staging/Production/Archived) as current; MLflow deprecat…]
4. `phases/10-llms-from-scratch/03-data-pipelines` Data Pipelines for Pre-Training (90 min) [not audited]
5. `phases/11-llm-engineering/04-embeddings` Embeddings & Vector Representations (75 min) [stale: Gemini Embedding 2 price wrong]
6. `phases/11-llm-engineering/05-context-engineering` Context Engineering: Windows, Budgets, Memory, and Retrieval (90 min) [stale: Context windows wrong or outdated for the Anthropic and Gemini models named]
7. `phases/11-llm-engineering/06-rag` RAG (Retrieval-Augmented Generation) (90 min) [not audited]
8. `phases/11-llm-engineering/07-advanced-rag` Advanced RAG (Chunking, Reranking, Hybrid Search) (90 min) [not audited]
9. `phases/11-llm-engineering/10-evaluation` Evaluation & Testing LLM Applications (45 min) [stale: Treats Opus 4.7 as the frontier model]
10. `phases/11-llm-engineering/13-production-app` Building a Production LLM Application (120 min) [not audited]
11. `phases/17-infrastructure-and-production/13-llm-observability` LLM Observability Stack Selection (60 min) [not audited]

## Developer Experience and Education (`ai-developer-relations-engineer`)

Build credible integrations, examples, and reusable agent packages, then turn developer friction into clearer tools and teaching.

Estimated 905 min (about 15 h), 11 required lessons.

1. `phases/00-setup-and-tooling/04-apis-and-keys` APIs & Keys (30 min) [unverified: Default model id claude-sonnet-5 and the $5 signup credit could not be confirmed on offic…]
2. `phases/13-tools-and-protocols/01-the-tool-interface` The Tool Interface — Why Agents Need Structured I/O (45 min) [WRONG: Says parallel tool use is opt-in on Anthropic; it is the default]
3. `phases/13-tools-and-protocols/05-tool-schema-design` Tool Schema Design — Naming, Descriptions, Parameter Constraints (45 min) [not audited]
4. `phases/13-tools-and-protocols/06-mcp-fundamentals` MCP Fundamentals: Stateless Requests and JSON-RPC (55 min) [ok: MCP stateless details matched official spec and changelog]
5. `phases/13-tools-and-protocols/07-building-an-mcp-server` Building an MCP Server: Stateless Python and TypeScript (85 min) [ok: server/discover, ttlMs, cacheScope matched spec]
6. `phases/13-tools-and-protocols/22-skills-and-agent-sdks` Agent Skills: Portable Contract and Runtime Boundary (90 min) [not audited]
7. `phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure` Skill Discovery and Progressive Disclosure (105 min) [ok: Skill catalog entry of about 100 tokens matches the Agent Skills spec]
8. `phases/13-tools-and-protocols/25-skill-invocation-and-routing` Skill Invocation and Routing (105 min) [not audited]
9. `phases/13-tools-and-protocols/27-skill-evals-packaging-and-portability` Skill Evals, Packaging, and Portability (150 min) [ok: GitSkills dataset figures verified]
10. `phases/13-tools-and-protocols/23-capstone-tool-ecosystem` Capstone: Stateless Tool Ecosystem (120 min) [ok: Tasks-extension changes matched spec (tasks/cancel unchecked)]
11. `phases/14-agent-engineering/54-build-the-feedback-ratchet` Build a Feedback Ratchet with Ownership and Retirement (75 min) [not audited]

## AI Evaluation and Reliability (`ai-evaluation-reliability-engineer`)

Measure model and agent behavior, expose failure modes, instrument the runtime, and build release and incident controls around evidence.

Estimated 750 min (about 12 h), 12 required lessons.

1. `phases/02-ml-fundamentals/09-model-evaluation` Model Evaluation (90 min) [clean: read in full; no error found (single pass)]
2. `phases/11-llm-engineering/10-evaluation` Evaluation & Testing LLM Applications (45 min) [stale: Treats Opus 4.7 as the frontier model]
3. `phases/14-agent-engineering/30-eval-driven-agent-development` Eval-Driven Agent Development (60 min) [not audited]
4. `phases/14-agent-engineering/26-failure-modes-agentic` Failure Modes: Why Agents Break (60 min) [not audited]
5. `phases/14-agent-engineering/23-otel-genai-conventions` OpenTelemetry GenAI Semantic Conventions (60 min) [not audited]
6. `phases/17-infrastructure-and-production/08-inference-metrics-goodput` Inference Metrics — TTFT, TPOT, ITL, Goodput, P99 (60 min) [not audited]
7. `phases/17-infrastructure-and-production/13-llm-observability` LLM Observability Stack Selection (60 min) [not audited]
8. `phases/17-infrastructure-and-production/21-ab-testing-llm-features` A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem (60 min) [not audited]
9. `phases/17-infrastructure-and-production/22-load-testing-llm-apis` Load Testing LLM APIs — Why k6 and Locust Lie (75 min) [not audited]
10. `phases/17-infrastructure-and-production/20-shadow-canary-progressive` Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs (60 min) [not audited]
11. `phases/17-infrastructure-and-production/24-chaos-engineering-llm` Chaos Engineering for LLM Production (60 min) [not audited]
12. `phases/17-infrastructure-and-production/23-sre-for-ai` SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection (60 min) [not audited]

## LLM Product Engineering (`applied-ai-engineer`)

Turn language-model capability into evaluated, safe, cost-aware product behavior that can survive production traffic.

Estimated 885 min (about 15 h), 12 required lessons.

1. `phases/11-llm-engineering/01-prompt-engineering` Prompt Engineering: Techniques & Patterns (90 min) [not audited]
2. `phases/11-llm-engineering/03-structured-outputs` Structured Outputs: JSON, Schema Validation, Constrained Decoding (90 min) [not audited]
3. `phases/11-llm-engineering/04-embeddings` Embeddings & Vector Representations (75 min) [stale: Gemini Embedding 2 price wrong]
4. `phases/11-llm-engineering/05-context-engineering` Context Engineering: Windows, Budgets, Memory, and Retrieval (90 min) [stale: Context windows wrong or outdated for the Anthropic and Gemini models named]
5. `phases/11-llm-engineering/06-rag` RAG (Retrieval-Augmented Generation) (90 min) [not audited]
6. `phases/11-llm-engineering/09-function-calling` Function Calling & Tool Use (75 min) [stale: Treats Opus 4.7 and GPT-5 as the frontier and judge models]
7. `phases/11-llm-engineering/10-evaluation` Evaluation & Testing LLM Applications (45 min) [stale: Treats Opus 4.7 as the frontier model]
8. `phases/11-llm-engineering/11-caching-cost` Caching, Rate Limiting & Cost Optimization (45 min) [WRONG: Pricing for all three vendors' flagship models is wrong (see known-errors.md)]
9. `phases/11-llm-engineering/12-guardrails` Guardrails, Safety & Content Filtering (45 min) [not audited]
10. `phases/11-llm-engineering/13-production-app` Building a Production LLM Application (120 min) [not audited]
11. `phases/17-infrastructure-and-production/19-ai-gateways` AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost (60 min) [not audited]
12. `phases/17-infrastructure-and-production/20-shadow-canary-progressive` Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs (60 min) [not audited]

## Building and Deploying AI Applications (`building-and-deploying-ai-applications`)

Build an AI feature from prompt and structured output through retrieval, evaluation, production serving, observability, and release.

Estimated 780 min (about 13 h), 12 required lessons.

1. `phases/11-llm-engineering/01-prompt-engineering` Prompt Engineering: Techniques & Patterns (60 min) [not audited]
2. `phases/11-llm-engineering/03-structured-outputs` Structured Outputs: JSON, Schema Validation, Constrained Decoding (60 min) [not audited]
3. `phases/11-llm-engineering/04-embeddings` Embeddings & Vector Representations (60 min) [stale: Gemini Embedding 2 price wrong]
4. `phases/11-llm-engineering/05-context-engineering` Context Engineering: Windows, Budgets, Memory, and Retrieval (60 min) [stale: Context windows wrong or outdated for the Anthropic and Gemini models named]
5. `phases/11-llm-engineering/06-rag` RAG (Retrieval-Augmented Generation) (75 min) [not audited]
6. `phases/11-llm-engineering/10-evaluation` Evaluation & Testing LLM Applications (75 min) [stale: Treats Opus 4.7 as the frontier model]
7. `phases/11-llm-engineering/11-caching-cost` Caching, Rate Limiting & Cost Optimization (60 min) [WRONG: Pricing for all three vendors' flagship models is wrong (see known-errors.md)]
8. `phases/11-llm-engineering/12-guardrails` Guardrails, Safety & Content Filtering (60 min) [not audited]
9. `phases/11-llm-engineering/13-production-app` Building a Production LLM Application (90 min) [not audited]
10. `phases/17-infrastructure-and-production/13-llm-observability` LLM Observability Stack Selection (60 min) [not audited]
11. `phases/17-infrastructure-and-production/20-shadow-canary-progressive` Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs (60 min) [not audited]
12. `phases/17-infrastructure-and-production/23-sre-for-ai` SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection (60 min) [not audited]

## Customer AI Deployment (`forward-deployed-ai-engineer`)

Discover a customer workflow, reduce its riskiest assumptions, and carry a useful AI system through measurement and rollout.

Estimated 865 min (about 14 h), 12 required lessons.

1. `phases/14-agent-engineering/47-outcomes-before-output` Define the Outcome Before You Choose the Output (60 min) [not audited]
2. `phases/14-agent-engineering/48-discover-the-real-workflow` Discover the Workflow People Actually Perform (70 min) [not audited]
3. `phases/14-agent-engineering/49-map-assumptions-and-risk` Map Assumptions and Resolve the Riskiest One First (65 min) [not audited]
4. `phases/14-agent-engineering/50-choose-the-smallest-testable-slice` Choose the Smallest Slice That Can Change the Decision (65 min) [not audited]
5. `phases/14-agent-engineering/51-write-specifications-that-preserve-judgment` Write Specifications That Preserve Judgment (75 min) [not audited]
6. `phases/11-llm-engineering/06-rag` RAG (Retrieval-Augmented Generation) (90 min) [not audited]
7. `phases/11-llm-engineering/10-evaluation` Evaluation & Testing LLM Applications (45 min) [stale: Treats Opus 4.7 as the frontier model]
8. `phases/11-llm-engineering/13-production-app` Building a Production LLM Application (120 min) [not audited]
9. `phases/14-agent-engineering/52-design-success-metrics` Design Success Metrics Before the Result Exists (70 min) [not audited]
10. `phases/14-agent-engineering/53-prototype-pilot-or-production` Choose Prototype, Pilot, or Production Deliberately (70 min) [not audited]
11. `phases/17-infrastructure-and-production/20-shadow-canary-progressive` Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs (60 min) [not audited]
12. `phases/14-agent-engineering/54-build-the-feedback-ratchet` Build a Feedback Ratchet with Ownership and Retirement (75 min) [not audited]

## Model Context Protocol (MCP) (`model-context-protocol`)

Build, secure, verify, and operate stateless MCP systems from JSON-RPC envelopes through conformance release gates.

Estimated 1395 min (about 23 h), 17 required lessons, 1 optional.

1. `phases/13-tools-and-protocols/06-mcp-fundamentals` MCP Fundamentals: Stateless Requests and JSON-RPC (55 min) [ok: MCP stateless details matched official spec and changelog]
2. `phases/13-tools-and-protocols/07-building-an-mcp-server` Building an MCP Server: Stateless Python and TypeScript (85 min) [ok: server/discover, ttlMs, cacheScope matched spec]
3. `phases/13-tools-and-protocols/08-building-an-mcp-client` Building an MCP Client: Discovery, Routing, and Dual-Era Fallback (85 min) [not audited]
4. `phases/13-tools-and-protocols/09-mcp-transports` MCP Transports: stdio and Stateless Streamable HTTP (65 min) [ok: Error codes and per-request _meta matched spec]
5. `phases/13-tools-and-protocols/10-mcp-resources-and-prompts` MCP Resources and Prompts: Addressable Context for Stateless Servers (60 min) [not audited]
6. `phases/13-tools-and-protocols/11-mcp-sampling` MCP Model Input: Sampling Migration and Stateless MRTR (75 min) [ok: Deprecations and MRTR matched spec]
7. `phases/13-tools-and-protocols/12-mcp-roots-and-elicitation` Explicit Scope and Stateless Elicitation (60 min) [ok: MRTR input_required matched spec]
8. `phases/13-tools-and-protocols/13-mcp-async-tasks` MCP Tasks Extension: Durable Work on a Stateless Core (90 min) [not audited]
9. `phases/13-tools-and-protocols/14-mcp-apps` MCP Apps on the Stateless Protocol (75 min) [not audited]
10. `phases/13-tools-and-protocols/15-mcp-security-tool-poisoning` MCP Security: Poisoned Metadata, Routing, and MRTR State (60 min) [not audited]
11. `phases/13-tools-and-protocols/16-mcp-security-oauth-2-1` MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up (90 min) [not audited]
12. `phases/13-tools-and-protocols/18-mcp-auth-production` MCP Auth in Production: Issuer-Bound Enrollment and Tokens (90 min) [not audited]
13. `phases/13-tools-and-protocols/17-mcp-gateways-and-registries` Stateless MCP Gateways and Registry Admission (75 min) [not audited]
14. `phases/13-tools-and-protocols/28-mcp-tool-contracts-and-content` MCP Tool Contracts and Content (120 min) [not audited]
15. `phases/13-tools-and-protocols/29-mcp-reliability-cancellation-and-flow-control` MCP Reliability, Cancellation, and Flow Control (120 min) [not audited]
16. `phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift` MCP Registry Supply Chain: Admission, Drift, and Rollback (90 min) [not audited]
17. `phases/13-tools-and-protocols/31-mcp-conformance-versioning-and-operations` MCP Conformance Engineering: Versioning, Evidence, and Operations (100 min) [not audited]
- (optional) `phases/13-tools-and-protocols/23-capstone-tool-ecosystem` Capstone: Stateless Tool Ecosystem (120 min, optional) [ok: Tasks-extension changes matched spec (tasks/cancel unchecked)]

## Reverse Engineering (`reverse-engineering`)

Read a compiled program you built yourself: parse the file, decode the instructions, lift them to pseudocode, record evidence, and prove a rebuild equal, then learn the field around that pipeline with its main tools.

Estimated 1945 min (about 32 h), 14 required lessons.

1. `phases/13-tools-and-protocols/32-program-anatomy-elf-from-scratch` Program Anatomy: An ELF Reader From Scratch (120 min) [not audited]
2. `phases/13-tools-and-protocols/33-disassembly-and-control-flow` Disassembly and Control Flow: From Bytes to a Graph You Can Check (150 min) [not audited]
3. `phases/13-tools-and-protocols/34-lifting-to-pseudocode` Lifting to Pseudocode: IR, SSA, and Structuring From Scratch (150 min) [not audited]
4. `phases/13-tools-and-protocols/35-evidence-confidence-and-unknowns` Evidence, Confidence, and Unknowns in Binary Analysis (105 min) [not audited]
5. `phases/13-tools-and-protocols/36-rebuild-and-prove-equal` Rebuild and Prove Equal: Differential Tests, Byte Comparison, and the Evidence… (110 min) [not audited]
6. `phases/13-tools-and-protocols/37-the-reverse-engineering-landscape` The Reverse Engineering Landscape: History, Tool Families, and How a Decompiler… (150 min) [not audited]
7. `phases/13-tools-and-protocols/38-calling-conventions-and-stack-frames` Calling Conventions and Stack Frames: System V, Windows x64, and AArch64 (140 min) [not audited]
8. `phases/13-tools-and-protocols/39-compiler-idioms-and-optimization` Compiler Idioms: What Optimization Does to Your Code and How to Read It Back (150 min) [not audited]
9. `phases/13-tools-and-protocols/40-linking-loading-and-stripped-binaries` Linking, Loading, and Stripped Binaries: PLT, GOT, Imports, Fixups, and Functio… (160 min) [not audited]
10. `phases/13-tools-and-protocols/41-recovering-data-and-types` Recovering Data and Types: Structs, Arrays, C++ Objects, and DWARF (140 min) [not audited]
11. `phases/13-tools-and-protocols/42-dynamic-analysis-of-your-own-program` Dynamic Analysis of Your Own Program: Debuggers, Traces, and Confirming Static… (130 min) [not audited]
12. `phases/13-tools-and-protocols/43-bytecode-and-managed-formats` Beyond Native Code: Python, JVM, .NET, and WebAssembly Bytecode (150 min) [not audited]
13. `phases/13-tools-and-protocols/44-binary-diffing-and-symbolic-execution` Binary Diffing and Symbolic Execution: Matching Functions and Solving for Inputs (150 min) [not audited]
14. `phases/13-tools-and-protocols/45-ai-assisted-reverse-engineering` AI-Assisted Reverse Engineering: LLM Decompilers, Analysis Agents, and Ground T… (140 min) [not audited]

## Product Judgment and Delivery (`shaping-the-build`)

Turn evidence into outcomes, assumptions, testable slices, executable specifications, measurement plans, and owned feedback loops.

Estimated 550 min (about 9 h), 8 required lessons.

1. `phases/14-agent-engineering/47-outcomes-before-output` Define the Outcome Before You Choose the Output (60 min) [not audited]
2. `phases/14-agent-engineering/48-discover-the-real-workflow` Discover the Workflow People Actually Perform (70 min) [not audited]
3. `phases/14-agent-engineering/49-map-assumptions-and-risk` Map Assumptions and Resolve the Riskiest One First (65 min) [not audited]
4. `phases/14-agent-engineering/50-choose-the-smallest-testable-slice` Choose the Smallest Slice That Can Change the Decision (65 min) [not audited]
5. `phases/14-agent-engineering/51-write-specifications-that-preserve-judgment` Write Specifications That Preserve Judgment (75 min) [not audited]
6. `phases/14-agent-engineering/52-design-success-metrics` Design Success Metrics Before the Result Exists (70 min) [not audited]
7. `phases/14-agent-engineering/53-prototype-pilot-or-production` Choose Prototype, Pilot, or Production Deliberately (70 min) [not audited]
8. `phases/14-agent-engineering/54-build-the-feedback-ratchet` Build a Feedback Ratchet with Ownership and Retirement (75 min) [not audited]

## Software Engineering Fundamentals (`software-engineering-fundamentals`)

Build the repository, debugging, testing, interface, security, release, and operational foundations AI systems depend on.

Estimated 730 min (about 12 h), 13 required lessons.

1. `phases/00-setup-and-tooling/01-dev-environment` Dev Environment (45 min) [clean: read in full; no error found (single pass)]
2. `phases/00-setup-and-tooling/02-git-and-collaboration` Git & Collaboration (60 min) [clean: read in full; no error found (single pass)]
3. `phases/00-setup-and-tooling/06-python-environments` Python Environments (45 min) [unverified: Claim that CUDA 11.8 builds fail on CUDA 12.x drivers is likely overstated; I could not f…]
4. `phases/00-setup-and-tooling/07-docker-for-ai` Docker for AI (60 min) [clean: read in full; no error found (single pass)]
5. `phases/00-setup-and-tooling/09-data-management` Data Management (60 min) [stale: Says GitHub gives 1 GB free for Git LFS; GitHub's current Free plan lists 10 GiB storage…]
6. `phases/00-setup-and-tooling/10-terminal-and-shell` Terminal & Shell (45 min) [clean: read in full; no error found (single pass)]
7. `phases/00-setup-and-tooling/12-debugging-and-profiling` Debugging and Profiling (60 min) [unverified: Asserts 80% of AI bugs live at levels 1 and 2 with no source or data behind the figure.]
8. `phases/13-tools-and-protocols/01-the-tool-interface` The Tool Interface — Why Agents Need Structured I/O (60 min) [WRONG: Says parallel tool use is opt-in on Anthropic; it is the default]
9. `phases/13-tools-and-protocols/05-tool-schema-design` Tool Schema Design — Naming, Descriptions, Parameter Constraints (60 min) [not audited]
10. `phases/14-agent-engineering/38-verification-gates` Verification Gates (55 min) [ok: arXiv 2604.01483 is real but a narrow finance-compliance fit]
11. `phases/17-infrastructure-and-production/20-shadow-canary-progressive` Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs (60 min) [not audited]
12. `phases/17-infrastructure-and-production/25-security-secrets-audit` Security — Secrets, API Key Rotation, Audit Logs, Guardrails (60 min) [not audited]
13. `phases/17-infrastructure-and-production/23-sre-for-ai` SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection (60 min) [not audited]

## Agent-Assisted Engineering (`using-coding-agents`)

Frame, plan, execute, delegate, verify, review, and improve coding-agent work inside real repositories.

Estimated 900 min (about 15 h), 16 required lessons.

1. `phases/14-agent-engineering/31-agent-workbench-why-models-fail` Agent Workbench Engineering: Why Capable Models Still Fail (45 min) [not audited]
2. `phases/14-agent-engineering/32-minimal-agent-workbench` The Minimal Agent Workbench (45 min) [unverified: ICLR 2026 AMBIG-SWE numbers not found in the paper]
3. `phases/14-agent-engineering/33-instructions-as-executable-constraints` Agent Instructions as Executable Constraints (50 min) [not audited]
4. `phases/14-agent-engineering/34-repo-memory-and-state` Repo Memory and Durable State (60 min) [not audited]
5. `phases/14-agent-engineering/35-initialization-scripts` Initialization Scripts for Agents (45 min) [not audited]
6. `phases/14-agent-engineering/36-scope-contracts` Scope Contracts and Task Boundaries (50 min) [unverified: Blog-sourced statistics]
7. `phases/14-agent-engineering/43-frame-the-task-before-code` Frame the Task Before the Agent Writes Code (60 min) [not audited]
8. `phases/14-agent-engineering/44-plan-from-evidence` Build an Evidence-Backed Execution Plan (65 min) [not audited]
9. `phases/14-agent-engineering/37-runtime-feedback-loops` Runtime Feedback Loops (50 min) [not audited]
10. `phases/14-agent-engineering/38-verification-gates` Verification Gates (55 min) [ok: arXiv 2604.01483 is real but a narrow finance-compliance fit]
11. `phases/14-agent-engineering/39-reviewer-agent` Reviewer Agent: Separate Builder from Marker (55 min) [unverified: Cloudflare figures not independently verified; other statistics anecdotal]
12. `phases/14-agent-engineering/45-delegate-with-isolation` Delegate Agent Work with Isolation and Merge Contracts (70 min) [not audited]
13. `phases/14-agent-engineering/40-multi-session-handoff` Multi-Session Handoff (50 min) [not audited]
14. `phases/14-agent-engineering/41-workbench-for-real-repos` The Workbench on a Real Repo (60 min) [not audited]
15. `phases/14-agent-engineering/46-turn-feedback-into-system` Turn Every Agent Correction into a System Improvement (65 min) [not audited]
16. `phases/14-agent-engineering/42-agent-workbench-capstone` Capstone: Ship a Reusable Agent Workbench Pack (75 min) [not audited]
