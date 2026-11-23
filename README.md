# Spec-Kit for My Dad

A beginner-friendly guide and skill layer for using [GitHub's spec-kit](https://github.com/github/spec-kit) or [OpenSpec](https://github.com/Fission-AI/OpenSpec) (Specification-Driven Development) with an AI coding agent — **works with Claude Code, Codex CLI, opencode, and any other agent that supports the shared "Agent Skills" format.**

## What is This?

This project simplifies spec-kit and OpenSpec for someone with little or no coding background:

- **Choice of toolkit** — spec-kit (strict, many checks, best for new apps and learning) or OpenSpec (light, best for changing existing apps and quick iterations), picked per project with a short "best for" under each
- **Step-by-step guide** ([guide-for-dad.md](./guide-for-dad.md)), split into a one-time setup and a repeatable per-feature loop for each toolkit, with a "what to check" list at every step
- **Automated, paced walkthrough** (`/start-guide`) that runs one step at a time and waits for you to look at the result before continuing
- **Multi-language support** (`/choose-language`)
- **Extra skills** that spec-kit itself doesn't provide: getting interviewed about a vague idea before specifying it, recovering context, explaining the project in its own terms, and tracking recurring problems found by analysis

## Quick Start

### Option 1: Automatic Setup (Recommended)

In your agent chat:
```
/start-guide
```
This walks through installing git, choosing spec-kit or OpenSpec, installing what it needs (uv + Python, or Node.js) and the toolkit itself, then creates your project in its own folder (`/new-project`) with this guide and all the skills copied in. You then open your agent in the project folder and run `/start-guide` again for the project rules and your first feature — pausing after each step for you to confirm.

This folder is only for setup and for creating or updating projects. Your app never lives here.

### Option 2: Manual Setup

1. Read [guide-for-dad.md](./guide-for-dad.md)
2. Follow each step yourself in your terminal and agent chat

## Project Structure

```
speckit-for-my-dad/
├── README.md                 # This file
├── guide-for-dad.md          # Step-by-step guide (setup + per-feature loop)
├── AGENTS.md                 # Agent config: language setting, skill list, workflow rules
├── CLAUDE.md                 # Symlink → AGENTS.md, so Claude Code reads the same file
└── .agents/skills/           # Canonical skill files (read natively by Codex CLI, opencode)
    ├── new-project/SKILL.md  # wrapper-only, not copied into projects
    ├── start-guide/SKILL.md
    ├── choose-language/SKILL.md
    ├── grill-me/SKILL.md
    ├── explain-me/SKILL.md
    ├── helper/SKILL.md
    ├── deployer/SKILL.md
    ├── where-am-i/SKILL.md
    ├── app-map/SKILL.md
    ├── create-new-task/SKILL.md
    └── fix-issues-after-analyze/SKILL.md
```

`.claude/skills/<name>` are symlinks into `.agents/skills/<name>` — Claude Code reads skills only from `.claude/skills/`, so the symlinks make the same files visible there without duplicating content. **Edit skills under `.agents/skills/` only.**

### What a user project gets

`/new-project` creates the project in its own folder with `specify init` or `openspec init`, then copies in:

```
my-app/
├── guide-for-dad.md                   # copy of the guide (plus any guide-for-dad-*.md translations)
├── AGENTS.md                          # the block between the speckit-for-my-dad markers
├── CLAUDE.md                          # one line: @AGENTS.md
├── .agents/skills/<skill>/            # real copies, not symlinks (Windows-safe)
├── .claude/skills/<skill>/            # same copies, for Claude Code
├── .agents/LICENSE-speckit-for-my-dad
└── .agents/speckit-for-my-dad.version # source commit, skill list, guide hashes
```

To update a project: `git pull` here, then `/new-project <path-to-project>`. It replaces only the files above, keeps the project's language, and asks before overwriting a guide the user edited.

## Supported Languages

- English (eng) — Default
- Russian (rus)
- Spanish (spa)
- French (fra)
- German (deu)
- Italian (ita)
- Japanese (jpn)
- Chinese (zho)

Change anytime with `/choose-language`. The current setting lives in [AGENTS.md](./AGENTS.md), not in a separate rules file. New projects start with the language set here, and each project can then change its own.

## Standard Spec-Kit Commands

Once `specify init` has run, spec-kit exposes these commands. Depending on which agent you picked during init, they're invoked either as `speckit-name` (skills-mode: Claude Code, Codex CLI) or `/speckit.name` (command-mode: opencode and others) — check what `specify init` actually installed for you.

| Command | Purpose |
|---|---|
| `constitution` | Define project governance and non-negotiable rules (once per project) |
| `specify` | Create a feature specification from natural language |
| `clarify` | Resolve ambiguities in the specification |
| `checklist` | Generate quality checklists that validate the requirements themselves |
| `plan` | Create a technical architecture and implementation plan |
| `tasks` | Generate an ordered task list from the plan |
| `analyze` | Read-only cross-artifact consistency and coverage check |
| `implement` | Execute the tasks and build the feature |
| `converge` | Compare codebase against spec/plan/tasks and append any remaining work as tasks |
| `taskstoissues` | Convert tasks into GitHub issues (optional, team use) |

## Standard OpenSpec Commands

Once `openspec init` has run, OpenSpec exposes these commands. Their form depends on the agent: `/opsx:propose` (Claude Code), `/opsx-propose` (opencode), `$openspec-propose` (Codex CLI) — `openspec init` prints the right one.

| Command | Purpose |
|---|---|
| `explore` | Think through an idea against the existing code, without writing anything |
| `propose` | Create a change folder: proposal, spec deltas, design, tasks |
| `update` | Bring a change's documents back in line after you edit one of them |
| `apply` | Work through the change's tasks and write the code |
| `sync` | Merge a change's spec deltas into `openspec/specs/` (optional — archive does it) |
| `archive` | Finish the change: merge spec deltas and move it to `openspec/changes/archive/` |

## Project Skills (this repo, not spec-kit or OpenSpec itself)

| Skill | What it does |
|---|---|
| `/new-project` | Creates a project in its own folder and copies the guide and skills into it, or updates an existing one (run in this folder only) |
| `/start-guide` | Runs the full guide, one paced step at a time |
| `/choose-language` | Switches the project's language |
| `/grill-me` | Interviews you about a feature idea before you specify it |
| `/explain-me` | Explains this project, grounded in its actual current files |
| `/helper` | Answers questions about your project's code, structure, and database in plain language — never edits anything |
| `/deployer` | Helps put your project on a server (SSH, Docker, git), keeps the server secure, sets up one-command deploys |
| `/where-am-i` | Recovers where you left off and suggests next steps |
| `/app-map` | Keeps `app-map.md` — block diagrams of how your app is built — up to date with your fresh code |
| `/create-new-task` | Adds one task to the current `tasks.md` without regenerating it |
| `/fix-issues-after-analyze` | Fixes findings from `analyze` and logs them to `issues-table.md`, flagging repeat problems (spec-kit only) |

## What Can You Build?

Websites, mobile apps, desktop apps, APIs, CLI tools, data pipelines, AI/ML applications — neither toolkit is tied to a stack. Build one feature at a time; see [guide-for-dad.md](./guide-for-dad.md) for why that matters.

## Prerequisites

- git — [git-scm.com](https://git-scm.com/downloads)
- For spec-kit: [uv](https://docs.astral.sh/uv/) and Python **3.11+**
- For OpenSpec: [Node.js](https://nodejs.org/) **20.19+**
- One of: Claude Code, Codex CLI, opencode, or another Agent-Skills-compatible AI coding agent

## Contributing

Have suggestions to improve this guide? Add new skills, improve documentation, add languages, or share what you built.

## Support

- Check the FAQ in [guide-for-dad.md](./guide-for-dad.md)
- Run `/where-am-i` or `/explain-me` in the agent chat
- Read the skill files directly under [.agents/skills/](./.agents/skills/)

## Credits

The `/grill-me` skill is adapted from Rob Mitterando's [grill-me-skill](https://github.com/RobMitt/grill-me-skill) — see [LICENSE](./LICENSE) for attribution details.

## License

MIT — see [LICENSE](./LICENSE). This project is a guide layer on top of spec-kit and OpenSpec; they are installed separately (`uv tool install specify-cli`, `npm install -g @fission-ai/openspec`) and are not vendored here.

---

**Ready to get started?** Type `/start-guide` in your agent chat!
