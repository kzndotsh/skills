# Repo map: dair-ai/Prompt-Engineering-Guide

Purpose: open-source prompt-engineering guide (promptingguide.ai), MIT licence, by DAIR.AI / Elvis Saravia. A Next.js 13 + Nextra 2 docs site; all content is MDX. English = `*.en.mdx`; other languages use `*.<lang>.mdx` siblings.

## Contents
1. Top-level layout
2. Content sections (where to find what)
3. i18n conventions
4. Site/build structure (Next, Nextra, components, API routes)
5. Contributing/running locally
6. Audit notes

## 1. Top-level layout
| Path | What |
|---|---|
| `pages/` | all site content (MDX) + `_app.tsx`, `_meta.<lang>.json` nav files, `api/` routes, `style.css` |
| `pages/index.en.mdx` | landing page + CourseCard components (no technique content) |
| `notebooks/` | 12 Jupyter notebooks (see `notebooks-and-code-recipes.md`) |
| `lecture/` | `Prompt-Engineering-Lecture-Elvis.pdf` (50 slides; see `lecture-summary.md`) |
| `guides/` | 8 older markdown guides (prompts-intro, basic-usage, advanced-usage, applications, chatgpt, adversarial, reliability, miscellaneous) + README; predate the `pages/` site (legacy, GPT-3 era) |
| `img/` | images used by MDX via `import X from '../../img/...png'` (code-generation, synthetic_rag, synthetic_diversity, agents, claude, claude-code, context-engineering-guide, 4o-image-generation, technique figures) |
| `public/` | favicons only (`144-favicon.svg`, dark variant) |
| `components/` | React helpers (see section 4) |
| `ar-pages/` | Arabic pages kept outside `pages/` (not routed; `pages/index.ar.mdx` exists; others staged here) |
| `middleware.js` | `export { locales as middleware } from 'nextra/locales'` (locale routing) |
| `next.config.js` | Nextra config: theme `nextra-theme-docs`, `themeConfig: ./theme.config.tsx`, `latex: true`; i18n locales and SVGR for `components/icons/*.svg` |
| `theme.config.tsx` | logo, i18n dropdown, head/meta/OG, GitHub + Discord links, `docsRepositoryBase`, footer (Copyright 2026 DAIR.AI), SerpAPI sponsor in git timestamp, `pre` override, CopyPageDropdown on English non-root pages, purple Services button in navbar |
| `package.json` | Next ^13.5.6, nextra and nextra-theme-docs ^2.13.2, React 18, katex, FontAwesome, `@vercel/analytics`, `@napi-rs/simple-git`; scripts dev/build/start; name still `nextra-docs-template` |
| `CITATION.cff`, `README.md`, `LICENSE.md` | citation (Saravia 2022), project intro/guide index, MIT |
| `CLAUDE.md` | tells agents: Next.js/Nextra project, read `Prompt-Engineering-Guide-notes/learnings/` (directory not present in the clone), notes go in that Obsidian vault, do not push unless asked |
| `infographic-review.html`, `pnpm-lock.yaml`, `package-lock.json` | misc/build artefacts (both lockfiles present) |

## 2. Content sections (`pages/<section>/`, nav order from `pages/_meta.en.json`)
Nav keys: index, introduction, techniques, agents, guides, applications, prompts, models, risks, research, papers, tools, notebooks, datasets, readings, courses (menu), about.
| Section | English page count | Notes |
|---|---|---|
| `introduction/` | 5 (+index `introduction.en.mdx`): settings, basics, elements, tips, examples | |
| `techniques/` | 18 (+index): zeroshot, fewshot, cot, meta-prompting, consistency, knowledge, prompt_chaining, tot, rag, art, ape, activeprompt, dsp, pal, react, reflexion, multimodalcot, graph | |
| `agents/` | 7: introduction, components, ai-workflows-vs-ai-agents, function-calling, context-engineering, context-engineering-deep-dive, deep-agents | newer content |
| `guides/` | 5: 4o-image-generation, context-engineering-guide, deep-research, optimizing-prompts, reasoning-llms | |
| `applications/` | 9 | this slice; see `applications.md` |
| `prompts/` | 12 prompt-hub pages: classification, coding, creativity, evaluation, information-extraction, image-generation, mathematics, question-answering, reasoning, text-summarization, truthfulness, adversarial-prompting | |
| `models/` | 21: chatgpt, claude-3, code-llama, collection, flan, gemini (+advanced, pro), gemma, gpt-4, grok-1, kimi-k2.5, llama, llama-3, mistral-7b, mistral-large, mixtral, mixtral-8x22b, olmo, phi-2, sora | |
| `risks/` | 3: adversarial, factuality, biases | |
| `research/` | 13: groq, guided-cot, infini-attention, llm-agents, llm-reasoning, llm-recall, llm-tokenization, rag, rag-faithfulness, rag_hallucinations, synthetic_data, thoughtsculpt, trustworthiness-in-llms | |
| top-level pages | `papers.en.mdx` (451 lines), `tools`, `notebooks`, `datasets`, `readings`, `courses`, `services`, `about`, `index` | `course.<lang>.mdx` exist for other languages; English is `courses.en.mdx` (naming mismatch) |
Each section dir has `_meta.en.json` mapping slug to nav title (ordering = key order). `applications.en.mdx`-style index pages just render `<ContentFileNames section="..." lang="en"/>`.

## 3. i18n conventions
- Locales configured: en (default), zh, jp, pt, tr, es, it, fr, kr, ca, fi, ru, de, ar (14). Language switcher text in `theme.config.tsx`; `i18n` list repeated in `next.config.js`.
- File naming: `<slug>.<locale>.mdx`, `_meta.<locale>.json`. Most sections only partially translated (e.g. `consistency` has 13 locales, newer pages English-only). Cross-links inside translated pages still use `promptingguide.ai/...` URLs.
- For this skill: ignore non-`en` files.

## 4. Site/build structure
- **MDX conventions:** page starts with `# Title`; imports like `import {Callout, Cards, Card, FileTree} from 'nextra-theme-docs'`, `import {Screenshot} from 'components/screenshot'`, images via `import IMG from '../../img/...'`; prompt/output convention is `*Prompt:*` / `*Output:*` followed by fenced code blocks; `<Callout type="info" emoji="...">` for notes and the repeated promo.
- **Components (`components/`):** `ContentFileNames.tsx` (cards from `/api/contentFiles`), `PromptFiles.jsx` (prompt-hub grouped cards from `/api/promptsFiles`), `CourseCard.tsx` (CoursePromo, CoursesSection, CourseCard on index), `AnnouncementBar.tsx` (global purple top bar, links to courses), `CopyPageDropdown.tsx` (copy page as Markdown / view; fetches raw `.en.mdx` through `/api/getPageContent`), `pre.tsx`/`CodeBlock.tsx`/`copy*.tsx`/`word-wrap.tsx`/`button.tsx`/`check.tsx` (code-block copy + wrap UI), `TabsComponent.tsx` (Nextra Tabs; takes `tabsData` of model/max_tokens/messages to show prompts across models), `counters.tsx` + css (demo counter), `icons/` (SVG icons via SVGR: arrow-right, box, brush, cards, chevron-right, cloud, code, diagram, dropper, files ...), `screenshot/` (Screenshot image wrapper).
- **API routes (`pages/api/`):** `contentFiles.js` (reads `pages/<section>/_meta.<lang>.json` and returns `{fileNames:[{slug,title}]}`), `promptsFiles.js` (scans prompts dir for `*.<lang>.mdx`, titles from meta), `getPageContent.ts` (accepts `pagePath` ending `.en.mdx`, fetches `https://raw.githubusercontent.com/dair-ai/Prompt-Engineering-Guide/main/pages/<pagePath>`, strips imports/exports/frontmatter, returns JSON; `.en.mdx` only). These need a Node server (no static export).
- **Analytics/other:** `_app.tsx` loads Google Tag Manager (gtag id in source), Vercel Analytics, AnnouncementBar; `theme.config.tsx` sets title suffix " | Prompt Engineering Guide".
- **Reading page text programmatically:** raw GitHub URLs per page, or the `/api/getPageContent?pagePath=techniques/cot.en.mdx` route.

## 5. Running / contributing
README: Node >= 18, install pnpm, `pnpm i next react react-dom nextra nextra-theme-docs`, `pnpm dev`, open http://localhost:3000. (package.json also supports `npm run dev`.) Contributions via "Edit" buttons/PRs and issues; MIT licence; sponsors via hello@dair.ai.

## 6. Audit notes
- README "Guides" index is stale/partial: omits agents, guides/, research/, prompts index detail, and many models (Claude 3, Gemma, Llama 3, Grok, Kimi, Mistral Large, Mixtral 8x22b, Sora, Gemini Pro/Advanced); links to "Takling" typo; mentions 13 languages while config has 14; announcements stop at Jan 2024 facts.
- `CLAUDE.md` references `Prompt-Engineering-Guide-notes/learnings/` which is absent: instructions that cannot be followed.
- `package.json` metadata is the Nextra template's (name `nextra-docs-template`, author Shu Ding, homepage of template); two lockfiles (npm and pnpm) can drift.
- `next.config.js` repeats locale list that is also in `theme.config.tsx` (duplicate source of truth). `pages/course.<lang>.mdx` vs `courses.en.mdx` naming mismatch. `pages/papers.en.mdx` is outside any section dir; `papers` listed in nav.
- `ar-pages/` duplicates a tree outside `pages/`; Arabic is only partially wired.
- `PromptFiles.jsx` uses `class=` instead of `className` (JSX warning); `ContentFileNames` fetches client-side so the content index renders empty without JS and is invisible to crawlers.
- `getPageContent.ts` fetches from GitHub main rather than local files (copy-page breaks for unpushed/new pages); regexes for stripping `export` are naive.
- Footer says "Copyright 2026 DAIR.AI" while CITATION says 2022 (just release date).
- Content mixes evergreen techniques with marketing (course callouts, promo code, services); extract only technical content.
