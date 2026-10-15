# Phase 00: Setup and Tooling

Upstream commit `1a8c4fd`. 13 lessons. Path pattern: `phases/00-setup-and-tooling/<lesson>/docs/en.md`.
Audit coverage: All 13 lessons read in full (second pass, 2026-10-15): 1 stale, 3 unverified, 1 ok, 8 clean. Flagged WRONG and stale items were independently re-verified; weak, ok and clean come from a single reader (weak was spot-checked at about 94% precision).

Columns: Type = Build or Learn; Lang = code file types; Quiz = has quiz.json; Out = reusable artifacts in outputs/; Audit = audit status (a dash means not audited). Fetch a lesson per `repo-guide.md`.

| # | Folder | Title | Type | Time | Lang | Quiz | Out | Motto | Prerequisites | Audit |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | `01-dev-environment` | Dev Environment | Build | ~45 minutes | py, rs, ts | y | 1 | Your tools shape your thinking. Set them up once, set them up right. | None | clean: read in full; no error found (single pass) |
| 02 | `02-git-and-collaboration` | Git & Collaboration | Learn | ~30 minutes | - | y | - | Version control is not optional. Every experiment, every model, every lesson you build here gets tracked. | Phase 0, Lesson 01 | clean: read in full; no error found (single pass) |
| 03 | `03-gpu-setup-and-cloud` | GPU Setup & Cloud | Build | ~45 minutes | py | y | - | Training on CPU is fine for learning. Training for real needs a GPU. | Phase 0, Lesson 01 | clean: read in full; no error found (single pass) |
| 04 | `04-apis-and-keys` | APIs & Keys | Build | ~30 minutes | py, ts | y | 1 | Every AI API works the same way: send a request, get a response. The details change, the pattern doesn't. | Phase 0, Lesson 01 | unverified: Default model id claude-sonnet-5 and the $5 signup credit could not be confirmed on official Anthropic pages; sources I found conflict. |
| 05 | `05-jupyter-notebooks` | Jupyter Notebooks | Build | ~30 minutes | py | y | 1 | Notebooks are the lab bench of AI engineering. You prototype here, then move what works into production. | Phase 0, Lesson 01 | clean: read in full; no error found (single pass) |
| 06 | `06-python-environments` | Python Environments | Build | ~30 minutes | - | y | - | Dependency hell is real. Virtual environments are the cure. | Phase 0, Lesson 01 | unverified: Claim that CUDA 11.8 builds fail on CUDA 12.x drivers is likely overstated; I could not fetch an exact NVIDIA sentence to quote. |
| 07 | `07-docker-for-ai` | Docker for AI | Build | ~60 minutes | - | y | - | Containers make "works on my machine" a thing of the past. | Phase 0, Lessons 01 and 03 | clean: read in full; no error found (single pass) |
| 08 | `08-editor-setup` | Editor Setup | Build | ~20 minutes | - | y | - | Your editor is your co-pilot. Configure it once so it stays out of your way and starts pulling its weight. | Phase 0, Lesson 01 | clean: read in full; no error found (single pass) |
| 09 | `09-data-management` | Data Management | Build | ~45 minutes | py | y | 1 | Data is the fuel. How you manage it determines how fast you go. | Phase 0, Lesson 01 | stale: Says GitHub gives 1 GB free for Git LFS; GitHub's current Free plan lists 10 GiB storage and 10 GiB bandwidth. |
| 10 | `10-terminal-and-shell` | Terminal & Shell | Learn | ~35 minutes | - | y | - | The terminal is where AI engineers live. Get comfortable here. | Phase 0, Lesson 01 | clean: read in full; no error found (single pass) |
| 11 | `11-linux-for-ai` | Linux for AI | Learn | ~30 minutes | - | y | - | Most AI runs on Linux. You need to know enough to not be stuck. | Phase 0, Lesson 01 | clean: read in full; no error found (single pass) |
| 12 | `12-debugging-and-profiling` | Debugging and Profiling | Build | ~60 minutes | py | y | 1 | The worst AI bugs don't crash. They train silently on garbage and report a beautiful loss curve. | Lesson 1 (Dev Environment), basic PyTorch familiarity | unverified: Asserts 80% of AI bugs live at levels 1 and 2 with no source or data behind the figure. |
| 13 | `13-python-for-ai-engineering` | Python for AI Engineering | Build | ~120 minutes | py | y | 1 | Most code in this course uses the same small set of Python idioms. Learn that set here, before the math and model lessons depend… | Dev Environment, Python Environments | ok: Verified batched and sumprod both added in Python 3.12 as the lesson states; hand-checked printed outputs in doc and code. [single-pass] |
