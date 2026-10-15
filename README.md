# skills

[![skills.sh](https://skills.sh/b/kzndotsh/skills)](https://skills.sh/kzndotsh/skills)

Agent skills for Claude Code and other agents that read `SKILL.md`. Each folder under `skills/` is one skill: a `SKILL.md` entry point plus optional `references/` that the agent loads on demand.

## Skills

| Skill | What it does |
|---|---|
| [prompt-engineering](skills/prompt-engineering/) | Audited knowledge base for writing and debugging LLM prompts: technique picker (few-shot, CoT, self-consistency, ReAct, RAG, chaining, PAL, ToT, Reflexion), agents and context engineering, reasoning-model prompting, prompt-injection defenses, model notes, and a prompt library. |
| [ai-engineering-from-scratch](skills/ai-engineering-from-scratch/) | Navigator and trust guide for the AI Engineering from Scratch curriculum (542 lessons, 20 phases): a per-phase lesson index, learning routes, a glossary index, and an audit that flags which lessons are correct, stale, or flawed. |
| [arctic-shift](skills/arctic-shift/) | Query archived Reddit posts, comments, threads, subreddits, and users through the free Arctic Shift API when reddit.com blocks automated access: endpoint picker, scoping rules, pagination, and failure modes. |

## Install

With the [skills CLI](https://github.com/vercel-labs/skills) (hosted at `kzndotsh/skills`):

```bash
npx skills add kzndotsh/skills --list          # see what's in the repo
npx skills add kzndotsh/skills -s prompt-engineering
npx skills add kzndotsh/skills -g --all        # every skill, user level
```

Or by hand, from a clone:

```bash
ln -s "$PWD/skills/prompt-engineering" ~/.claude/skills/prompt-engineering
```

## Use with Ruler

[Ruler](https://github.com/intellectronica/ruler) keeps one set of agent instructions and skills in a project's `.ruler/` folder and copies them into each agent's native location (`.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, and others). These skills use the plain `<name>/SKILL.md` layout it expects.

```bash
mkdir -p .ruler/skills
cp -r path/to/skills/skills/prompt-engineering .ruler/skills/
npx @intellectronica/ruler apply
```

Skills support in Ruler is experimental and on by default. Preview with `--dry-run`. Commit `.ruler/` and treat the generated agent directories as build output.

## Other agents

Skills in this layout also work in Cursor, which reads `.agents/skills/`, `.cursor/skills/`, and the Claude and Codex compatibility paths (`.claude/skills/`, `.codex/skills/`), at project or user level. Its docs require `name` to match the folder name, which holds here. Cursor cannot import a single skill from a repo. To share with a Cursor team, package skills as a plugin with `.cursor-plugin/marketplace.json`; that isn't set up here.

## Adding a skill

Copy [`template/`](template/) to `skills/<name>/` and edit.

## Lint

```bash
python3 scripts/lint.py
```

Checks every skill under `skills/` against the Agent Skills spec and Claude's authoring limits (name and description rules, reserved words, valid frontmatter YAML, body under 500 lines, contents lists, broken or unlinked references) and the llms.txt files (structure, links into this repo, freshness of the root file). CI runs it on every push. No dependencies.

## llms.txt

[llmstxt.org](https://llmstxt.org/)-style indexes for agents that can fetch a URL but can't install skills:

- [`llms.txt`](llms.txt): the master index. Lists each skill and links to that skill's own index.
- `skills/<skill>/llms.txt`: one per skill, inside the skill folder. It links the skill's `SKILL.md`, every reference file and any scripts by raw URL. For `ai-engineering-from-scratch` it is one large file (about 140 KB, roughly 35k tokens) with a section per phase linking all 542 upstream lessons at a pinned commit, each with our audit status.

The master and the generic per-skill files come from `python3 scripts/gen_llms.py`, and lint fails if they are stale. The curriculum file comes from that skill's `scripts/build_index.py --llms`. A loaded agent has no use for these files, since `SKILL.md` already indexes the skill; installing a skill copies them along.

## Layout

```
skills/
  <skill-name>/
    SKILL.md        frontmatter (name, description) + instructions
    references/     detail files, loaded only when needed
```

The folder name matches the `name` in `SKILL.md`. Only `name` and `description` are required in the frontmatter. Skills that aren't ready can set `metadata.internal: true` to stay out of normal discovery.

## Sources and credit

`prompt-engineering` is distilled from the [DAIR.AI Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) (MIT license, commit `5767372`, 2026-03-11). The reference files paraphrase the guide, include some short verbatim prompt templates, and add audit notes on stale content, errors, and gaps. Content tagged "(not in repo)" comes from outside the guide. All credit for the underlying material goes to DAIR.AI and the cited paper authors.

## License

[MIT](LICENSE). `skills/prompt-engineering` also carries the upstream DAIR.AI MIT notice in its [NOTICE.md](skills/prompt-engineering/NOTICE.md).
