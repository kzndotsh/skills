# Modern Guides: Reasoning LLMs, Prompt Optimization, Deep Research, 4o Image Generation

Sources: pages/guides/reasoning-llms.en.mdx, optimizing-prompts.en.mdx, deep-research.en.mdx, 4o-image-generation.en.mdx (dair-ai/Prompt-Engineering-Guide). Written around May-June 2025; product facts (limits, model names) are stale. "(not in repo)" marks my additions.

## Contents
1. Reasoning LLMs: what, when, prompting rules, hybrid workflow, limitations
2. Optimizing prompts (generic design checklist)
3. OpenAI Deep Research: what it is, prompting tips, limits, alternatives
4. 4o / gpt-image-1 image generation: capabilities, prompting, limits, tips
5. Audit notes

---

## 1. Reasoning LLMs
(pages/guides/reasoning-llms.en.mdx)

Definition: large reasoning models (LRMs) are trained to do native thinking/chain-of-thought before answering. Repo examples: Gemini 2.5 Pro, Claude 3.7 Sonnet, o3 (also mentions Claude 4, DeepSeek-R1, Qwen, Llama-Nemotron, Phi-4-Mini-Reasoning).
Repo's smoke-test prompt (tools + reasoning):
```
What is the sum of the first 50 prime numbers? Generate and run Python code for the calculation, and make sure you get all 50. Provide the final sum clearly.
```

### 1.1 When to use reasoning models (patterns)
- Planning step in agentic systems (e.g. deep research: break query into searches, then an orchestrator dispatches workers).
- Agentic RAG: retrieval agent with reasoning chain that routes complex queries via tool calls over complex knowledge bases.
- LLM-as-a-Judge: reasoning model assesses predictions and writes feedback; an evaluator-optimizer loop feeds feedback plus current prompt to a meta-prompt that rewrites the system prompt.
- Visual reasoning (o3 "thinking with images": crop/zoom/rotate in chain of thought).
- Others: large complex document sets in technical domains, codebase review/debug, algorithm and scientific coding, math/science, literature synthesis, meta-prompting/routine generation, data validation, multi-step planning, extraction for QA, knowledge-intensive/ambiguous tasks.
- When NOT: simple or latency/cost-sensitive modules. Repo says use reasoning models only for reasoning-heavy components and modularize the app so they are isolated.

### 1.2 Prompting rules (repo)
1. Strategic use: only for reasoning-heavy modules.
2. Test-time compute: more thinking time generally means better results.
3. Effort setting: low = cheap/fast, medium = balance, high = more thinking tokens, slower.
4. Be explicit about the goal, constraints, desired output; remove assumptions.
5. AVOID manual CoT ("think step by step") in instructions; keep instructions simple and direct; add response constraints.
6. Structure inputs with delimiters. Structured output: repo recommends XML as default for generated content unless JSON is a hard requirement. Note: Claude 4's output format follows the prompt format (Markdown prompt -> heavy Markdown output).
7. Few-shot only when the model struggles to hit the desired output; align examples with the instructions; useful for showing behavior to avoid.
8. Use descriptive modifiers for higher-quality output (from Claude 4 docs): "Add thoughtful details like hover states, transitions, and micro-interactions" for front-end code.

Template (synthesized, not verbatim):
```
Goal: <one sentence>
Constraints: <length, sources, forbidden things>
Input: <data in delimiters/XML>
Output: <exact format; XML tags or JSON schema>
(no "think step by step")
```

### 1.3 Hybrid reasoning models (thinking can be toggled)
Escalation ladder:
1. Start with thinking off; evaluate (optionally with manual CoT here).
2. If shallow/mistaken and task benefits from analysis: enable thinking at low effort.
3. Not enough -> medium. Not enough -> high.
4. Few-shot to fix style/format.
Optimize accuracy first, then latency and cost.

### 1.4 Limitations (repo)
- Output quality: mixed languages, repetition, inconsistent formatting; mitigate by following model-specific prompting guides and removing ambiguous/unnecessary instructions.
- Reasoning hurts instruction following: explicit CoT can reduce instruction adherence (arXiv 2505.11423, "The Pitfalls of Reasoning for Instruction Following in LLMs", 2025). Mitigations from that paper: few-shot with carefully chosen examples, self-reflection, self-selective reasoning (model decides when to reason), classifier-selective reasoning.
- Over/underthinking: be specific about task, process, output format; or route only complex subtasks to a reasoning tool.
- Cost: much higher than chat models; track tokens, evaluate quality, watch cost from inconsistent outputs.
- Latency: slow, can emit irrelevant content; use concise prompts, stream tokens for perceived latency, smaller reasoning models or e.g. Claude 3.7 Sonnet are faster.
- Weak tool calling: parallel tool calls still problematic; DeepSeek-R1/Qwen poor at tool calling unless trained for it; decision making and robust dynamic tool use are the gap.
Related references (repo): Reasoning Models Don't Always Say What They Think (arXiv 2505.05410), The Illusion of Thinking (Apple), CoT Encyclopedia (2505.10185), Understanding Reasoning LLMs (Raschka).

## 2. Optimizing prompts
(pages/guides/optimizing-prompts.en.mdx; short, generic summary of a video)

Checklist:
- Specificity and clarity: state the desired outcome; ambiguity gives irrelevant output.
- Structured inputs/outputs: JSON/XML for inputs; state output format (list, paragraph, code).
- Delimiters to separate elements.
- Task decomposition: split monolithic prompts into subtasks (prompt chain).
- Few-shot: provide input-output pairs (see pages/techniques/fewshot.en.mdx).
- CoT: "think step by step" (see techniques/cot.en.mdx). CAVEAT: contradicts section 1.2 rule 5 for reasoning models.
- ReAct: reasoning + acting with tools (techniques/react.en.mdx).
No templates or examples in the file itself. Best used as a pointer list.

## 3. OpenAI Deep Research
(pages/guides/deep-research.en.mdx; product circa Feb-May 2025)

What: OpenAI agent for multi-step web research; tools = browsing + Python; reports with citations; accepts uploaded files; built with RL on browsing/reasoning, can backtrack and adapt; powered by a proprietary o3 variant (lightweight version on o4-mini). Process: search -> analyze -> synthesize -> report / insights / action plan, over hundreds of sources, minutes instead of hours.
Use it when: task needs multi-faceted, domain-specific queries over real-time info plus careful reasoning (market/competitor analysis, literature review, product comparison, policy/legal research, technical reports, study plans, GitHub repo analysis). Repo advice for everything else (then-current): plain o1-mini for tasks needing reasoning, GPT-4o for simple one-offs.
Custom alternative: Flowise, LlamaIndex, crewAI, n8n, LangGraph with o1/o3-mini; cheaper, flexible, but lacks OpenAI's specialised model. See agents-and-context-engineering.md section 8 for a hand-built version.

### Prompting tips (repo)
- Clear, specific instructions; give it a plan; get the prompt right first time (runs are costly/slow).
- Answer its clarifying questions thoroughly rather than skipping.
- Give many precise keywords (brand, technical term, product name): it searches by keywords.
- Use clear verbs: compare, suggest, recommend, report.
- Specify output format: report type, sections, tables, columns, headers.
- Upload PDFs/files as context for technical or unfamiliar topics.
- Always verify sources yourself.
Template (synthesized, not in repo):
```
Task: <compare|report on|recommend> <topic with precise keywords>.
Scope: time range <dates>, regions <...>, source types <...>.
Output: report with sections <...>; a table with columns <...>; cite sources inline.
Attached: <files>.
```
Idea list in repo: market research, product reviews/price comparison, legal case research, fact-checking, trend tracking, study plans, tool-feature updates, health literature, blog drafting, bios/resumes, slide suggestions.

### Limitations (repo)
Hallucinations, trouble separating authoritative sources from rumor, weak synthesis of technical/domain info, citation and formatting errors, cannot reliably force N sources or restrict to given sources, domain bias, poor with date/time queries (be explicit), no paywalled sources, charts/embedding not working at the time, hard to export, read-only (no actions like Operator), limited personalization.
Usage limits cited (April 2025): Plus/Team/Enterprise/Edu 25 per month, Pro 250, Free 5 lightweight; fallback to lightweight when original quota is exhausted. Stale.

## 4. 4o Image Generation (gpt-image-1)
(pages/guides/4o-image-generation.en.mdx; circa spring 2025)

What: OpenAI autoregressive image model sharing GPT-4o's architecture; strong text-in-image, editing, image inputs. Access: ChatGPT ("Generate an image of...", or Tools -> "Create an image"), Sora, API as `gpt-image-1`; callable from gpt-4o, 4o-mini, 4.1, 4.1-mini, 4.1-nano, o3.
Specs: 1:1 1024x1024 (default), 3:2 1536x1024, 2:3 1024x1536. Reference image types: PNG, JPEG, WEBP, non-animated GIF.
Capabilities: inpainting (only for images generated in that chat), text-prompt edits, style transfer from a reference image, transparent PNG (must say "transparent PNG"/"transparent background"), text in images, same subject in different styles, combining images.

Prompting tips:
- Be detailed when you have a specific goal; if vague, ChatGPT fills in details. Trick: ask o3 to write 3 varied image-optimized prompts from your description, then merge the best parts.
- Specify lighting, composition, style (and camera/lens if you want a photo look); also subject, medium, environment, color, mood.
- Model choice: 4o fastest for one-off edits; reasoning model (o3) for multi-step creative iteration because it keeps style/font/colors consistent.
- State aspect ratio explicitly even with reference images; default is 1:1.
- Same-chat consistency: good for small edits, bad for creative resets. Start a new chat for independent tasks. If early iterations are far off, ask the model to output the prompt it used, spot the misplaced emphasis, start a new chat with a revised prompt.
- Multiple images from one prompt needs a reasoning model and explicit instruction; unreliable. Repo test prompt:
```
Generate an image of [decide this yourself], in the style of an oil painting by Van Gogh. Use a 3:2 aspect ratio. Before you generate the image, recite the rules of this image generation task. Then send the prompt to the 4o Image Generation model. Do not use DALL-E 3. If the 4o Image Generation model is timed out, tell me how much time is left until you can queue the next prompt to the model.

Rules:
- Use only the aspect ratio mentioned earlier.
- Output the prompt you sent to the image generation model exactly as you sent it, do this every time in between image generations
- Create three variations with a different subject, but the same rules. After an image is generated, immediately start creating the next one, without ending your turn or asking me for confirmation for moving forward.
```
- Use verbs "draw" / "edit".
- To avoid fallback to DALL-E 3, add to ChatGPT personalization: "Never use the DALL-E tool. Always generate images with the new image gen tool. If the image tool is timed out, tell me instead of generating with DALL-E."
- Strict prompt adherence is hard: ChatGPT may rewrite your prompt before sending it to the image model, more likely with long prompts or multi-turn.
- Example photoreal prompt from repo (Art Deco rocket): subject + era style + setting + time of day + material + mood + lighting ("A high-resolution photograph of a majestic Art Deco-style rocket ... standing on a realistic launch pad during golden hour... mirror-polished metallic surface reflecting a vivid sunset sky... cinematic warm light with strong shadows...").
Use cases: logos (multi-turn, reasoning model), marketing assets from existing visuals, coloring pages (2:3), stickers (transparent bg), material transfer from reference, interior design from a room photo.
Limitations: prompt rewriting, unclear/dynamic quotas, queueing on free tier, yellow tint, too dark with dark elements, refusals under usage policy, no upscaling, cropping errors, hallucinations, trouble with many concepts, imprecise data/graph visuals, poor non-Latin text, weak fix-a-typo edits, inconsistent naming (Imagegen / gpt-image-1 / 4o Image Generation / image_gen.text2im), occasional wrong aspect ratio.

## 5. Audit notes

- Reasoning-models guide: models named are 2025-era (o3, Claude 3.7, Gemini 2.5, DeepSeek-R1). The "no manual CoT" rule holds in principle, but newer hybrid models (e.g. Claude with extended/adaptive thinking, GPT-5 reasoning effort) change details: check current vendor docs (not in repo). The effort levels low/medium/high are OpenAI-style; Anthropic uses a thinking token budget (not in repo).
- Contradiction: optimizing-prompts recommends CoT and ReAct generally; reasoning-llms says avoid CoT with reasoning models. Reconcile: CoT for non-reasoning models only.
- "Recommend XML over JSON as default" is an unsupported opinion with a Claude-specific flavor; JSON/structured outputs are better where parsers are involved.
- Claims "poor tool calling" for reasoning models is already outdated (o3 and later, Claude with thinking do tool use well); treat as historical.
- reasoning-llms "Top Reasoning Models" is only a link to a Google Sheet; no content in repo. Leaderboard links may be dead. The "Code demo" and "most up-to-date guide" links are external Google Drive/Docs.
- deep-research.en.mdx: heavily stale (o1-mini/GPT-4o advice, usage limits, "not entirely clear whether OpenAI will launch the model via API", "Operator" may merge). Contains an editorial leftover "Hypothesis testing?" and typos ("Enginering", "critize"). Its "o1-mini vs GPT-4o" selection advice should be dropped. Claude artifact/ChatGPT share links are unretrievable examples.
- 4o-image-generation: product-specific, quota and model list stale; the image alt for the "transparent PNG" example reuses the inpainting image file (likely copy-paste error). Tips on ChatGPT personalization to avoid DALL-E 3 are obsolete if DALL-E is retired (not in repo, verify). The generic lessons (detail, aspect ratio, new chat to reset, ask for the prompt) transfer to other image models.
- optimizing-prompts: thin, no examples, referencing "this blog post" (video transcript). Low value; point to pages/techniques/* instead.
- Course promo callouts (PROMPTING20, "limited to first 500 students") appear in all four; ignore.
