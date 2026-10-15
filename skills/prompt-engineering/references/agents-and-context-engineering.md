# Agents, Workflows, Function Calling, Deep Agents, Context Engineering

Source: dair-ai/Prompt-Engineering-Guide, pages/agents/*.en.mdx, pages/agents.en.mdx, pages/guides/context-engineering-guide.en.mdx. Most of it is practitioner opinion from the DAIR.AI "Building Effective AI Agents with n8n" course (Elvis Saravia), not peer-reviewed. Items marked "(not in repo)" are my additions.

## Contents
1. Agent definition and components
2. Workflows vs agents (decision table, 3 workflow patterns, hybrid)
3. Function / tool calling (flow, tool definitions, agent loop, debugging, best practices)
4. Deep agents (planning, orchestrator + sub-agents, external memory, verification)
5. Context engineering: definition, what it covers
6. Context engineering guide: Search Planner worked example (full prompt, structured output)
7. Context engineering for agents: case study (issues, fixes, principles, pitfalls, metrics)
8. Deep dive: deep research agent (architecture split, full system prompt, iteration)
9. Checklists / quick-reference templates
10. Audit notes

---

## 1. Agent definition and components
(pages/agents/introduction.en.mdx, components.en.mdx)

- Agent = LLM-powered system that takes actions and solves complex tasks autonomously. Beyond plain text generation it has three pillars: planning (+reflection), tool access, memory.
- Planning: task decomposition (via CoT), self-reflection on past actions, adaptive learning, critical analysis of progress. Repo admits LLM planning is imperfect but essential.
- Tools: code interpreter, web search/scraping, calculator, image generation, DBs, APIs. The LLM must know when and how to pick a tool.
- Memory: short-term/working (context buffer, in-context learning, enough for most tasks) and long-term (external vector store, fast retrieval of history; "less commonly implemented").
- Why agents: single LLM calls handle narrow tasks (translation, email). Multi-step tasks (marketing strategy: research competitors, trends, internal data) need real-world/internal info + planning + reasoning.
- Use cases listed: recommendation, customer support, research (legal/finance/health), e-commerce, booking, reporting, financial analysis.
- Use when: task needs multiple steps, external info, or adaptive planning. Do NOT use when: a single prompt or a fixed pipeline suffices (see section 2).

## 2. AI workflows vs AI agents
(pages/agents/ai-workflows-vs-ai-agents.en.mdx; credits Anthropic "Building Effective Agents", 2024)

Definitions:
- Workflow: LLMs and tools orchestrated through predefined code paths. Predictable, explicit control flow.
- Agent: LLM dynamically directs its own process and tool usage.

| Aspect | Workflow | Agent |
|---|---|---|
| Control flow | Predefined, explicit | Dynamic, autonomous |
| Decisions | Hard-coded logic | LLM reasoning |
| Tool use | Orchestrated by code | Self-selected |
| Adaptability | Fixed paths | Flexible |
| Complexity | Lower, predictable | Higher, more capable |
| Fit | Well-defined tasks | Open-ended problems |

Choose workflow when: requirements clear and stable, predictability/consistency needed, easy debugging and monitoring, cost control matters, production reliability.
Choose agent when: open-ended/exploratory, number of steps hard to define upfront, flexibility > predictability, adaptive reasoning needed.
Hybrid (common in production): workflows for structure, agents for adaptive subtasks, e.g. a workflow routes requests to specialized agents. The repo promises a hybrid example "in an upcoming article"; it is not there.

### Workflow pattern 1: prompt chaining
Break task into sequential LLM calls; each output feeds the next; optional gate between steps.
Example in repo (n8n): chat message -> small model drafts outline -> check against criteria -> grade -> if pass, expand sections with stronger model then polish; if fail, manual edit step.
Use for: content generation pipelines, multi-stage document processing, sequential validation. Add validation gates between critical steps.

### Workflow pattern 2: routing
Classify the request, then dispatch to a specialized chain/agent/model.
Example: query classifier (small model + structured output parser) -> switch -> General / Refund / Support LLM chain.
Use for: customer support, multi-domain QA, delegation, cost optimization (cheap model for easy classes). Benefit: specialization + cost.

### Workflow pattern 3: parallelization
Run independent LLM operations simultaneously (example: content-safety pipeline). Use for moderation, multi-criteria evaluation, independent verification. Benefit: latency, throughput.

### Agent example
Task planner agent: chat -> agent with Chat Model (reasoning LLM), Memory, Tools (add_update_tasks to a Google Sheet, search_task). Request "Add a meeting with John tomorrow at 2 PM": the agent decides which tools, in what order. Key insight: order and selection come from request context, not predefined rules.
Core agent components (repo list): tool access, memory, reasoning engine, autonomy.
Agent use cases: deep research, agentic RAG, coding agents, data analysis, content editing, support, chatbots.

### Best practices (repo)
- Workflows: document each stage, fallback paths for failures, validation gates, per-step latency/success monitoring.
- Agents: clear well-documented tools with explicit purposes, memory/context retention strategy, guardrails on behavior and tool usage, log reasoning and decisions, iterative testing on diverse scenarios.

Missing from repo (not in repo): Anthropic's other patterns (orchestrator-workers, evaluator-optimizer) are only touched elsewhere (see guides-modern.md reasoning section for evaluator-optimizer and orchestrator-worker figures). Rule of thumb from Anthropic's post: start with the simplest solution (single prompt, then workflow) and add agent autonomy only if needed.

## 3. Function (tool) calling
(pages/agents/function-calling.en.mdx)

What: the LLM emits a structured request to call an external function; your code runs it; result goes back to the model. This is what turns a text generator into an agent. Also the route to MCP servers and knowledge bases.

Flow:
1. User query.
2. Context assembly: system message + tool definitions + user message.
3. Tool decision: model outputs structured call (tool name + arguments) or answers directly.
4. Tool execution: YOUR code executes the function.
5. Observation: tool result.
6. Response generation: observation appended to all prior messages, model produces the final answer (or another tool call).
The model always sees the full accumulated context; each call adds to it.

Tool definition = name + description (what it does AND when to use it) + parameters (types, descriptions, enums, required). Definitions are the only way the model knows tools exist. They are re-sent on every LLM call, so they cost tokens, cost and latency: be concise but descriptive.

Verbatim example (OpenAI-style schema):
```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location. Use this when the user asks about weather conditions in a specific city or region.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "The temperature unit to use"}
            },
            "required": ["location"]
        }
    }
}]
```

Agent loop: action (call tool) -> environment response -> observation -> decision (another action or answer). Trace example:
```
User: "Latest news from OpenAI"
Agent thinks: need current info -> use web_search
Action: web_search(query="OpenAI latest news announcements")
Observation: [search results]
Agent thinks: have enough -> summarize
Response: "Here are the latest updates..."
```

Debugging: expose intermediate steps (n8n: "Return Intermediate Steps"): which tools, exact arguments, observations, token use. Common failure modes: wrong tool chosen, bad/incomplete arguments, missing guidance in the definition, model misreads the observation. Platform abstraction may hide the real prompt; get as close to the raw API call as possible.

Best practices (repo):
- Specific descriptions. Instead of "Search the web": "Search the web for current information. Use this when the user asks about recent events, news, or data that may have changed since training."
- Repeat tool-usage guidance in the system prompt (looks redundant, improves selection with many tools):
```
You have access to the following tools:
- web_search: Use this for any questions about current events or recent information
- calculator: Use this for mathematical calculations
- knowledge_base: Use this to search internal documentation

Always prefer the knowledge_base for company-specific questions before using web_search.
```
- Constrain parameters: enums, examples in descriptions (e.g. "Use 'celsius' for most countries, 'fahrenheit' for US").
- Tools return informative errors that let the agent recover, e.g. "No results found for this query. Try broadening your search terms or using alternative keywords."

## 4. Deep agents
(pages/agents/deep-agents.en.mdx; opinion piece by Elvis Saravia, cites LangChain deep agents, Claude Code/Agent SDK, Philipp Schmid "Agents 2.0")

Claim: shallow agents (single loop in one context window) break on long multi-step problems (deep research, agentic coding). Deep agents add:
1. Planning: structured, updatable task plan (living to-do list) the agent can retry/recover from, instead of ad-hoc reasoning. Try plan mode in Claude Code/Codex. Human-in-the-loop expertise matters.
2. Orchestrator + sub-agents: orchestrator delegates to specialists (search, coder, KB retriever, analyst, verifier, writer), each with clean context and narrow focus; orchestrator integrates outputs. Main benefit: context management via separation of concerns. Author is "skeptical" of the Cognition "Don't Build Multi-Agents" argument; see audit notes.
3. Context retrieval / agentic search + external memory: store intermediate work in files, notes, vectors, DBs; reference rather than stuff the window. Hybrid memory (agentic search + semantic search) and let the agent choose. Papers cited: ReasoningBank (arXiv 2509.25140), Agentic Context Engineering (arXiv 2510.04618).
4. Context engineering: explicit instructions on when to plan, when to use a sub-agent, how to name files, how to collaborate with humans. Includes structured outputs, system-prompt optimization, compacting context, evaluating context effectiveness, optimizing tool definitions (Anthropic "Writing tools for agents").
5. Verification: verify outputs by LLM-as-judge or human; LLMs still hallucinate, are sycophantic, are prompt-injectable. Build verifiers from systematic eval pipelines.
Example system: DAIR.AI Academy customer-support agentic RAG (n8n).

## 5. Context engineering: definition
(pages/guides/context-engineering-guide.en.mdx)

- Repo's definition: "the process of designing and optimizing instructions and relevant context for the LLMs and advanced AI models to perform their tasks effectively" (text and multimodal). Framed as the rebrand/broadening of prompt engineering. Distinguishes "blind prompting" (a short question) from prompt engineering (thinking about context and structure).
- Scope list: prompt chains; system prompts/instructions; dynamic prompt elements (user input, date/time); RAG; query augmentation; tool definitions and instructions; few-shot demonstrations; input/output structuring (delimiters, JSON schema); short-term memory (state/history) and long-term memory (vector store); filtering noisy information.
- It is iterative and needs formal measurement (eval pipelines). "Creative and novel context engineering is the moat."
- Agent-specific scope (pages/agents/context-engineering.en.mdx): system prompts, task constraints, tool descriptions, memory management, error handling.

## 6. Context engineering guide: Search Planner worked example

Scenario: sub-agent "Search Planner" in an n8n multi-agent deep research app. Components of effective context, each illustrated:

### 6.1 System prompt (verbatim, lightly trimmed)
```
You are an expert research planner. Your task is to break down a complex research query (delimited by <user_query></user_query>) into specific search subtasks, each focusing on a different aspect or source type.

The current date and time is: {{ $now.toISO() }}

For each subtask, provide:
1. A unique string ID for the subtask (e.g., 'subtask_1', 'news_update')
2. A specific search query that focuses on one aspect of the main query
3. The source type to search (web, news, academic, specialized)
4. Time period relevance (today, last week, recent, past_year, all_time)
5. Domain focus if applicable (technology, science, health, etc.)
6. Priority level (1-highest to 5-lowest)

All fields (id, query, source_type, time_period, domain_focus, priority) are required for each subtask, except time_period and domain_focus which can be null if not applicable.

Create 2 subtasks that together will provide comprehensive coverage of the topic. Focus on different aspects, perspectives, or sources of information.

Each substask will include the following information:

id: str
query: str
source_type: str  # e.g., "web", "news", "academic", "specialized"
time_period: Optional[str] = None  # e.g., "today", "last week", "recent", "past_year", "all_time"
domain_focus: Optional[str] = None  # e.g., "technology", "science", "health"
priority: int  # 1 (highest) to 5 (lowest)

After obtaining the above subtasks information, you will add two extra fields. Those correspond to start_date and end_date. Infer this information given the current date and the time_period selected. start_date and end_date should use the format as in the example below:

"start_date": "2024-06-03T06:00:00.000Z",
"end_date": "2024-06-11T05:59:59.999Z",
```

### 6.2 Why each part is there
- Instructions: the role + task line alone is where "many beginners stop"; the rest is the context.
- User input in delimiters: `<user_query> What's the latest dev news from OpenAI? </user_query>`. Delimiters separate input from instructions/outputs.
- Enumerated fields + hints: without "1 (highest) to 5 (lowest)" the model may pick a 1-10 scale. Specify scales, enums, allowed null.
- Structured output: give a type spec in the prompt AND (in n8n) a JSON-example output parser that auto-generates a schema. Example output shape:
```json
{"subtasks":[{"id":"openai_latest_news","query":"latest OpenAI announcements and news","source_type":"news","time_period":"recent","domain_focus":"technology","priority":1,"start_date":"2025-06-03T06:00:00.000Z","end_date":"2025-06-11T05:59:59.999Z"}]}
```
  Many providers offer native structured outputs: prefer those over hand-rolling (not in repo for specific APIs).
- Tools / dynamic context: inject current date/time; otherwise the model guesses dates and produces bad searches. Better: expose date as a tool called only when needed. Date also enables inferring start_date/end_date from time_period.
- RAG & memory: cache previously generated subqueries in a vector store and retrieve similar plans, saving LLM calls (latency + cost).
- State & history: for revision loops, give the agent subtask state, revisions, past results from each agent. What to pass depends on what you optimize for; requires evals.
- Advanced (WIP in repo): context compression, management, safety, effectiveness evaluation; context dilutes with stale/irrelevant info and needs eval workflows to catch it.

## 7. Context engineering for agents: case study
(pages/agents/context-engineering.en.mdx)

Minimal deep research agent (orchestrator + web search + task sheet).

Issue 1: orchestrator creates 3 search tasks, runs 2, skips one silently. Root cause: no explicit completion constraint. Two fixes: flexible (allow skipping with justification) or strict (require all). Flexible prompt fragment:
```text
You are a deep research agent responsible for executing comprehensive research tasks.

TASK EXECUTION RULES:
- For each search task you create, you MUST either:
  1. Execute a web search and document findings, OR
  2. Explicitly state why the search is unnecessary and mark it as completed with justification

- Do NOT skip tasks silently or make assumptions about task redundancy
- If you determine tasks overlap, consolidate them BEFORE execution
- Update task status in the spreadsheet after each action
```
Issue 2: no debugging visibility. Fix: external task tracker (sheet/text file) with Task ID, search query, status (todo / in_progress / completed), results summary, timestamp.

Principles:
1. Eliminate ambiguity. Bad: "Perform research on the given topic." Good:
```text
Perform research on the given topic by:
1. Breaking down the query into 3-5 specific search subtasks
2. Executing a web search for EACH subtask using the search_tool
3. Documenting findings for each search in the task tracker
4. Synthesizing all findings into a comprehensive report
```
2. Make expectations explicit: required vs optional actions, quality standards, output formats, decision criteria.
3. Observability: log decisions, track state externally, record tool calls and outcomes, capture errors. Watch every run; odd behavior = prompt improvement signal.
4. Iterate: deploy -> observe -> identify deviations -> refine -> test -> repeat.
5. Balance strict (predictable) vs flexible (adaptive).

Advanced: layered context (System / Task / Tool / Memory layers); dynamic context adjustment by task complexity, resources, execution history, error patterns; validate context for completeness, clarity, consistency, testability.

Pitfalls:
- Over-constraint. Bad: "NEVER skip a search task. ALWAYS perform exactly 3 searches. NEVER combine similar queries." Better: "Aim to perform searches for all planned tasks. If you determine that tasks are redundant, consolidate them before execution and document your reasoning."
- Under-specification. Bad: "Do some research and create a report." Better: numbered procedure with report sections (executive summary, key findings per search task, conclusions and insights).
- Ignoring error cases:
```text
ERROR HANDLING:
- If a search fails, retry once with a rephrased query
- If retry fails, document the failure and continue with remaining tasks
- If more than 50% of searches fail, alert the user and request guidance
- Never stop execution completely without user notification
```
Metrics: task completion rate, behavioral consistency across similar inputs, error rate, user satisfaction, debugging time.

## 8. Deep dive: deep research agent
(pages/agents/context-engineering-deep-dive.en.mdx)

Architecture lesson: v1 had one agent doing task management, memory writes, web search and report generation. Result: context too long, forgot searches, missed status updates, unreliable. Fix: split into Deep Research Agent (plans, orchestrates; reasoning model, repo example Gemini 2.5 Pro, or GPT-5) and Search Worker Agent (only runs searches; fast/cheap model, Gemini 2.5 Flash or GPT-5-mini). Separation of concerns + cost-appropriate model per subtask. Sub-agent input should be minimal: just the query text, word for word. Sub-agent returns findings, error states, execution metadata.

Full system prompt (verbatim):
```md
You are a deep research agent who will help with planning and executing search tasks to generate a deep research report.

## GENERAL INSTRUCTIONS

The user will provide a query, and you will convert that query into a search plan with multiple search tasks (3 web searches). You will execute each search task and maintain the status of those searches in a spreadsheet.

You will then generate a final deep research report for the user.

For context, today's date is: {{ $now.format('yyyy-MM-dd') }}

## TOOL DESCRIPTIONS

Below are some useful instructions for how to use the available tools. 

Deleting tasks: Use the delete_task tool to clear up all the tasks before starting the search plan. 

Planning tasks: You will create a plan with the search tasks (3 web searches) and add them to the Google Sheet using the append_update_task tool. Make sure to keep the status of each task updated after completing each search. Each task begins with a todo status and will be updated to a "done" status once the search worker returns information regarding the search task.

Executing tasks: Use the Search Worker Agent tool to execute the search plan. The input to the agent are the actual search queries, word for word. 

Use the tools in the order that makes the most sense to you but be efficient. 
```
Lessons embedded in it:
- Current date matters (model cutoff is far behind today; "latest news" queries otherwise search stale info).
- Biggest gains often come from explaining tool usage in the SYSTEM PROMPT, not only parameter schemas (tool info lives in two places: prompt narrative and tool spec).
- Define allowed status values ("todo" -> "done"); otherwise runs drift between pending/to-do and completed/done/finished.
- "Use the tools in the order that makes the most sense" is deliberate flexibility; the agent may then run 2 of 3 searches or merge. If you need completeness:
```md
You MUST execute a web search for each and every search task you create.
Do NOT skip any tasks, even if they seem redundant.
```
  Flexible while developing (observe decisions); rigid in production.
- Still missing in that prompt (repo's list): per-task metadata (search type web/news/academic/PDF, time filters, domain, priority), richer planning guidance with good/bad decomposition examples, start/end date logic.
- Context-length management: isolate in separate agents, memory-management tools, summarize long outputs before appending, clear task lists between queries.
- Error handling snippet: retry once with rephrased query; mark "failed" with reason; notify user on critical errors; never proceed silently.

## 9. Quick-reference checklists

Agent system prompt skeleton (synthesized from the repo, not verbatim):
```
ROLE: one sentence.
GENERAL INSTRUCTIONS: input -> plan -> execute -> output; number of tasks; where state is kept.
CONTEXT: today's date, user/domain facts.
TOOL DESCRIPTIONS: per tool, when to use / not use, argument rules, ordering preferences.
ALLOWED STATUS VALUES / OUTPUT SCHEMA: enumerate.
EXECUTION RULES: must-do vs may-skip (with justification).
ERROR HANDLING: retry, fail, escalate.
```
Debug loop when an agent misbehaves: read intermediate steps -> classify (wrong tool / bad args / thin definition / misread observation / forgotten step / context bloat) -> fix in prompt/tool def, or split the agent -> retest on diverse inputs.

## 10. Audit notes

- Marketing and promo content is pervasive (PROMPTING20 codes, course callouts); ignore. Content is derived from one course; little independent evidence.
- Model names date it: GPT-4.1-mini/GPT-4o (workflows page), Gemini 2.5 Pro/Flash, GPT-5/GPT-5-mini (deep dive), "GPT-5 rumors" in a function-calling log sample. Treat as illustrative; substitute current models.
- Inconsistency: the guide's Search Planner prompt says "Create 2 subtasks"; the deep-dive agent says 3 searches; the case study says 3-5 subtasks. Numbers are arbitrary examples.
- The Search Planner prompt code block in the guide ends without closing its example properly, and the sample JSON output shows `"priority": 1.2` although the prompt declares `priority: int`. Shows that schema-in-prompt alone does not enforce types; use real structured output/validation.
- The guide's example start_date values (2024-06...) are inconsistent with the output example dates (2025-06...); format-only.
- Contradiction on flexibility: case study ("Flexible Approach (current)") and deep dive ("rigid in production") disagree on defaults; the Over-Constraint pitfall warns against rigid rules. Resolve by: mandate outcomes ("every task executed or justified"), not exact counts.
- Deep-agents page tells readers to dismiss the Cognition "don't build multi-agents" view without a counter-argument or data. Anthropic and Cognition both discuss shared-context failure modes of multi-agent systems (not in repo): sub-agents with minimal input lose context. The repo's own advice to give sub-agents only the query text can conflict with that; apply per task.
- "Long-term memory ... less commonly implemented" (components page) is outdated by late 2025; memory features are common (the deep-agents page itself leans on external memory).
- Gaps: no guidance on prompt injection via tool outputs, tool-permission/guardrail design beyond one line, token budgeting, parallel tool calls, MCP detail (only mentioned), evaluating agents beyond a metrics list, compaction techniques (named but not taught), cache-friendly context layout.
- Promised-but-missing: hybrid workflow+agent example, "more extensively in future articles" best practices, Advanced context engineering [WIP].
- agents/context-engineering.en.mdx and the guide both link to each other as "Context Engineering Deep Dive" (the deep-dive link in deep-agents.en.mdx points to the guide URL rather than to the deep-dive page); cosmetic.
- The `agents.en.mdx` index page only holds an intro and a ContentFileNames component.
