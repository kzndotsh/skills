# Resources catalog: tools, services, datasets, courses, readings

Sources: pages/tools.en.mdx, services.en.mdx, datasets.en.mdx, courses.en.mdx, readings.en.mdx, about.en.mdx, index.en.mdx, README.md, CITATION.cff. The repo lists are alphabetical dumps with no descriptions, mostly frozen in early-mid 2023. Categories and one-line descriptions below are my own grouping (not in repo) unless noted; many projects have since been renamed, archived or acquired. Treat every URL as unverified.

## Contents
1. Tools and libraries (grouped)
2. Datasets
3. Readings (grouped)
4. Courses, services, community, citation
5. Audit notes

## 1. Tools and libraries (pages/tools.en.mdx; 61 entries, "Sorted by Name")
**Prompt development / playgrounds / IDEs:** AI Test Kitchen (aitestkitchen.withgoogle.com), Google AI Studio (ai.google.dev), OpenAI Playground (beta.openai.com/playground, legacy URL), OpenPlayground (nat.dev), EveryPrompt, Dyno (trydyno.com), Prompter (prompter.engineer), Prompt Engine (microsoft/prompt-engine), Promptmetheus, PromptPerfect (promptperfect.jina.ai), Scale SpellBook, Visual Prompt Builder (tools.saxifrage.xyz/prompt), Metaprompt (metaprompt.vercel.app), ChatGPT Prompt Generator (huggingface merve), OptimusPrompt, Knit (promptknit.com), Prompts.ai (sevazhidkov), Agenta (Agenta-AI/agenta), Promptly (trypromptly.com), LangBear, Wordware, Playground (playgroundai.com; image), loom (socketteer/loom; multiverse text exploration).
**Frameworks / orchestration / LLM apps:** LangChain (hwchase17/langchain, now langchain-ai/langchain), LangSmith (smith.langchain.com docs: tracing/eval), GPT Index (jerryjliu/gpt_index, now LlamaIndex), Guidance (microsoft/guidance), Outlines (normal-computing/outlines; constrained/structured generation, now dottxt-ai), Guardrails (ShreyaR/guardrails; output validation, now guardrails-ai), Chainlit, Dify, DUST (dust.tt), PromptAppGPT (mleoking), Portkey AI (gateway), AnythingLLM (Mintplex-Labs), fastRAG (IntelLabs; RAG pipelines), Interactive Composition Explorer (oughtinc/ice), ActionSchema, AnySolve.
**Evaluation / benchmarking / testing:** PromptBench (microsoft/promptbench), PromptTools (hegelai/prompttools), YiVal (YiVal/YiVal; prompt/config tuning), OpenICL (Shark-NLP; in-context learning framework), GPTTools comparison tool, PromptSource (bigscience-workshop; prompt templates for datasets), ThoughtSource (OpenBioLink; CoT data/tools), ClickPrompt (prompt-engineering/click-prompt).
**Security / adversarial:** PromptInject (agencyenterprise/PromptInject), hwchase17/adversarial-prompts, Guardrails.
**Local model runners:** ollama (jmorganca/ollama, now ollama/ollama), LM Studio (lmstudio.ai), LMFlow (OptimalScale; fine-tuning toolbox).
**Training/prompt-learning:** OpenPrompt (thunlp/OpenPrompt), betterprompt (stjordanis/betterprompt; test prompt quality with transformers).
**Prompt marketplaces/communities:** FlowGPT, Prompt Base (promptbase.com), Prompt Apps (chatgpt-prompt-apps.com), prompted.link, sharegpt (sharegpt.com), EmergentMind, SmartGPT (getsmartgpt.com).
**Image generation prompt tools:** DreamStudio (beta.dreamstudio.ai), Lexica (lexica.art), Prodia, Playground.
Not in the list but standard in 2026 (not in repo): LlamaIndex, DSPy, promptfoo, Langfuse, Pydantic AI, Instructor, vLLM, provider consoles/workbenches (Anthropic Console, OpenAI Playground/evals), MCP.

## 2. Datasets (pages/datasets.en.mdx; 9 entries)
- Anthropic's Red Team dataset (github.com/anthropics/hh-rlhf/tree/master/red-team-attempts; paper arXiv 2209.07858)
- Awesome ChatGPT Prompts (huggingface.co/datasets/fka/awesome-chatgpt-prompts)
- DiffusionDB (poloclub/diffusiondb): image-gen prompts
- Midjourney Prompts (huggingface succinctly/midjourney-prompts)
- P3 - Public Pool of Prompts (huggingface bigscience/P3): prompted NLP datasets (T0)
- PartiPrompts (parti.research.google): text-to-image eval prompts
- Real Toxicity Prompts (allenai.org/data/real-toxicity-prompts): toxicity eval
- Stable Diffusion Dataset (huggingface Gustavosta/Stable-Diffusion-Prompts)
- WritingPrompts (reddit r/WritingPrompts)
Also referenced elsewhere in repo: JSONL emotion-classification fine-tuning data at github.com/dair-ai/datasets/tree/main/openai; ML-Papers-of-the-Week (github.com/dair-ai/ML-Papers-of-the-Week) used by RAG and caching examples.

## 3. Readings (pages/readings.en.mdx; about 125 entries, "Sorted by Name"; mostly Jan-Apr 2023)
Highest-value for a practitioner (my pick; verify freshness):
- Prompt Engineering by Lilian Weng (lilianweng.github.io/posts/2023-03-15-prompt-engineering/): strong survey of CoT/ICL/etc.
- OpenAI Cookbook (github.com/openai/openai-cookbook); Best practices for prompt engineering with OpenAI API (help.openai.com article 6654000); OpenAI Prompt Examples (platform.openai.com/examples)
- Long Context Prompting for Claude 2.1 (anthropic.com/news/claude-2-1-prompting): long-context retrieval prompting tip; for current Claude guidance use docs.anthropic.com (not in repo)
- Prompt Engineering by Microsoft (microsoft.github.io/prompt-engineering); by co:here (docs.cohere.ai/docs/prompt-engineering); Generative AI with Cohere Part 1
- Pretrain, Prompt, Predict (pretrain.nlpedia.ai) and Language Models and Prompt Engineering: Systematic Survey of Prompting Methods in NLP (video)
- Methods of prompt programming (generative.ink); Prompts as Programming by Gwern; Simulators; The Waluigi Effect; Mysteries of mode collapse (LessWrong) - conceptual models of LLM behaviour
- Learn Prompting (learnprompting.org); Prompt Engineering 101/201 (Amatriain); Prompt Engineering 101 (Humanloop)
- Eight Things to Know about Large Language Models (arXiv 2304.00612); Language Model Behavior: A Comprehensive Survey (2303.11504); On pitfalls of sophisticated LLMs (2303.17511); LINGO (2304.06184); Retrieving Multimodal Information for Augmented Generation survey (2303.10868); FVQA 2.0 (2303.10699)
- Courses/lectures: CS324 Large Language Models (stanford-cs324.github.io/winter2022 and winter2023), CS224N Lecture 11: Prompting, Instruction Tuning, RLHF (slides), CMU Advanced NLP 2022: Prompting, Prompting for Few-shot Learning (Princeton COS597G lec05), Introduction to ChatGPT (edX), AI Safety, RLHF and Self-Supervision (Jared Kaplan, MLSys #79), Common Sense as Dark Matter (Yejin Choi, MLSys #78)
- Security: Exploring Prompt Injection Attacks (NCC Group), Prompt injection attacks against GPT-3 (Simon Willison, Sep 2022), Exploiting GPT-3 Prompts (Goodside), Indirect Prompt Injection on Bing Chat (greshake.github.io), Can AI really be protected from text-based attacks? (TechCrunch), JailBreaking ChatGPT, Using GPT-Eliezer against ChatGPT Jailbreaking, Reverse Prompt Engineering for Fun and (no) Profit, Prompt injection to read out the secret OpenAI API key
- Image generation: DALL-E 2 Prompt Engineering Guide, DALLE Prompt Book, Best 100+ Stable Diffusion Prompts, Diffusion Models: A Practical Guide (Scale), How to Draw Anything, How to get images that don't suck, NLP for Text-to-Image Generators: Prompt Analysis, Bing Image Creator post, DALL-E 2 Preview Risks and Limitations
- Prompt collections: Awesome ChatGPT Prompts (github f/awesome-chatgpt-prompts), ChatGPT3 Prompt Engineering list (mattnigh), Curtis64 prompt gists, The ChatGPT Prompt Book (slides), Prompt Engineering Template (spreadsheet), ChatGPT list of lists (Medium), ChatGPT Plugins Collection (unofficial), Awesome Textual Instruction Learning Papers (RenzeLou), Notes for Prompt Engineering by sw-yx (ai-notes), GitHub topic prompt-engineering
- Explainers/essays: What Is ChatGPT Doing ... and Why Does It Work? (Wolfram), In defense of prompt engineering (Willison), How to write good prompts (Andy Matuschak), Why is ChatGPT so good? (Scale), Introduction to RLHF (Surge), Extrapolating to Unnatural Language Processing with GPT-3's In-context Learning (Stanford AI blog), Interactive guide to GPT-3 prompt parameters, 2023 AI Index Report (Stanford), Generative AI: Perspectives from Stanford HAI, Prompting: Better Ways of Using Language Models for NLP Tasks (The Gradient), Prompting in NLP: zero-shot (Medium), Prompting Methods with LMs and Weak Supervision (Snorkel), How to make LLMs say true things, Building GPT-3 applications beyond the prompt (Microsoft), GPT-4 Tutorial chat with multiple PDFs, Giving GPT-3 a Turing Test
- Careers/news (low value now): Axios, Futurism, Washington Post, Atlantic ("Most Important Job Skill of This Century"), VentureBeat, People Matters, "Prompt Engineering: The Career of Future", Simon Willison on Bing; Bing/TechCrunch hands-on pieces; Sydney.edu prompt-writing article; SEO's guide to ChatGPT prompts; Make PowerPoint presentations with ChatGPT; Fed Honeypot book; Japanese summary article (dev.classmethod.jp)
- Other: Prompt Engineering in GPT-3 (Analytics Vidhya), Prompt engineering davinci-003 on our own docs (Patterns), Talking to machines (Artifact Research), 3 Principles for prompt engineering with GPT-3, A Generic Framework for ChatGPT Prompt Engineering, Anyone can Design! (YashSharma), AI Content Generation (Jon Stokes), GPT-3 & Beyond / GPT3 and Prompts primer (buildspace), Giving GPT-3 a Turing Test, Prompt Engineering: From Words to Art, The Mirror of Language, Meet Claude (Scale), A beginner-friendly guide to generative language models - LaMDA guide.

## 4. Courses, services, community, citation
- **DAIR.AI Academy** (academy.dair.ai); promo code `PROMPTING20` (extra 20% off) appears in README, courses page, many mdx callouts. Instructor: Elvis Saravia (ex-Meta AI, Elastic). Courses linked in nav (`pages/_meta.en.json`): Intro to Prompt Engineering (/introduction-prompt-engineering; index page says 2 hours, Beginner), Advanced Prompt Engineering, Intro to AI Agents (/introduction-ai-agents), Building Effective AI Agents with n8n (/building-effective-ai-agents; index page says Intermediate, 5 hours), Build RAG Systems (/introduction-to-rag), Building Advanced AI Agents (/advanced-ai-agents). `courses.en.mdx` says "both courses" (stale; nav lists six). Learner orgs named: Microsoft, Google, Apple, Airbnb, LinkedIn, Amazon, JPMorgan Chase, Asana, Intuit, Fidelity, Coinbase, Guru. Questions: training@dair.ai.
- **Services page** (services.en.mdx): cohort-based trainings (prompt engineering, context engineering, RAG, AI agents; private training via training@dair.ai), consulting (hello@dair.ai or Calendly with Elvis Saravia), custom AI solutions (hello@dair.ai). Commercial; no technical content.
- **About** (about.en.mdx): project by DAIR.AI (mission: democratize AI research/education); scope "prompt engineering, context engineering, RAG, and AI Agents"; sponsorship via hello@dair.ai; contributions via Edit buttons; inspirations: OpenAI Cookbook, Pretrain/Prompt/Predict, Learn Prompting. Sponsor: SerpAPI (README, footer).
- **Index** (index.en.mdx): defines prompt engineering as developing/optimizing prompts to use LMs efficiently; used by researchers (QA, arithmetic reasoning) and developers (robust prompting interfacing with LLMs and tools); also for safety and for augmenting LLMs with domain knowledge/tools.
- **Community:** Discord (discord.gg/YbMT8k6GfX), Twitter @dair_ai, YouTube channel, newsletter nlpnews.substack.com, 1h video lecture (youtu.be/dOxUroR57xs), slides in `lecture/`. README claims: #1 on Hacker News 21 Feb 2023, 3M learners by Jan 2024, 13 languages (config actually lists 14 locales incl. English: en zh jp pt tr es it fr kr ca fi ru de ar).
- **Citation (README + CITATION.cff):** Saravia, Elvis. "Prompt Engineering Guide". 12/2022. https://github.com/dair-ai/Prompt-Engineering-Guide. BibTeX key `Saravia_Prompt_Engineering_Guide_2022`, @article, journal = the GitHub URL. CFF: cff-version 1.2.0, date-released 2022-12-16, preferred-citation type article. Licence: MIT.
- **Press mentioned:** WSJ, Forbes, MarkTechPost (2023).

## 5. Audit notes
- tools.en.mdx: "Sorted by Name" is not strictly true (hwchase17/adversarial-prompts sits among "I"/"L" entries; GPT Index before GPTTools). Several URLs are moved or dead (OpenAI beta playground URL, hwchase17/langchain, gpt_index, jmorganca/ollama, guardrails by ShreyaR, AI Test Kitchen). No descriptions and no maintenance dates. Duplicate-ish: "Playground" (playgroundai.com image tool) vs "OpenAI Playground"/"OpenPlayground".
- readings.en.mdx: almost entirely Dec 2022-Jun 2023; contains career-hype articles and Twitter/Reddit/Medium links likely dead or paywalled; "Sorted by Name" mostly but not strictly. One entry in Japanese. The Claude link is Claude 2.1 only. Nothing on reasoning models, agents, MCP, structured outputs, context engineering.
- datasets.en.mdx: only 9 entries, no safety/eval datasets beyond Red Team and RealToxicity; no coding/eval prompt datasets.
- courses.en.mdx says "both courses" while nav lists six; index CourseCard text and nav titles differ ("Building Effective AI Agents" vs "...with n8n").
- Marketing content (promo codes, services, "Join now" callouts) is mixed into technical pages: ignore for technical answers.
- notebooks.en.mdx is covered in `notebooks-and-code-recipes.md`.
