# AGENTS.md

## What this repository is

This repo is a beginner-friendly wrapper around GitHub's [spec-kit](https://github.com/github/spec-kit) — a Specification-Driven Development (SDD) toolkit — and, as an alternative the user picks per project, around [OpenSpec](https://github.com/Fission-AI/OpenSpec). It is not application code. It is `guide-for-dad.md` (a human-facing, step-by-step walkthrough) plus a small set of project skills (below) that make spec-kit and OpenSpec safe and legible for someone with little or no coding background.

**The user's own project never lives in this repo.** `new-project` creates it in a separate folder and copies the skills, the guide, and the block between the `speckit-for-my-dad` markers below into it. All work on the project happens in that folder.

This file (`AGENTS.md`) is read natively by Codex CLI and opencode, and by Claude Code via the `CLAUDE.md` symlink at the repo root. Whichever agent you are, follow it.

## Editing this repo

- Canonical skill files live once in `.agents/skills/<name>/SKILL.md` — the location Codex CLI and opencode read natively. `.claude/skills/<name>` are symlinks to the same files, so Claude Code sees them too. **Edit only the files under `.agents/skills/`** — never through the `.claude/skills/` symlink path.
- Everything between the `speckit-for-my-dad:start` / `:end` markers is copied into user projects verbatim (except the language line, which each project keeps). Keep it free of anything that only makes sense in this repo.
- Wrapper-only skill, not copied into projects:

| Skill | Use it to... |
|---|---|
| `new-project` | Create the user's project (spec-kit or OpenSpec) in its own folder and install the skills, guide, and rules into it — or update them in an existing project |
| `connect-playwright` | Connect Playwright MCP to the current project: finds npx, writes the git-ignored MCP config for the current agent, and verifies the setup works |

<!-- speckit-for-my-dad:start -->
## Language

Current communication language: **English (eng)**

Talk to the user in this language, and write all generated spec-kit / OpenSpec documentation (`spec.md`, `plan.md`, `tasks.md`, `proposal.md`, `design.md`, etc.) in it, until the `choose-language` skill changes this line. Supported: `eng`, `rus`, `spa`, `fra`, `deu`, `ita`, `jpn`, `zho` — or any language the user names.

## speckit-for-my-dad skills

These skills and `guide-for-dad.md` come from the speckit-for-my-dad repo. In a user project they are copies under `.agents/skills/<name>/` and `.claude/skills/<name>/`, installed by that repo's `new-project` skill — `.agents/speckit-for-my-dad.version` records which version. Updating overwrites them, so change them in the speckit-for-my-dad repo, not here.

| Skill | Use it to... |
|---|---|
| `start-guide` | Walk `guide-for-dad.md` step by step, pausing for confirmation after each step |
| `choose-language` | Change the language setting above |
| `grill-me` | Interview the user until a feature idea is precise enough for `speckit-specify` |
| `explain-me` | Explain how the speckit-for-my-dad workflow and skills work in this folder, not spec-kit in general |
| `helper` | Answer questions about the user's own project code (structure, modules, database, concepts) — plain, brief, read-only |
| `deployer` | Deploy the project to a server (SSH, Docker, git), diagnose hosting, harden SSH, write one-command deploy config — never app code |
| `where-am-i` | Recover context: where the user left off and what to do next |
| `create-new-task` | Add a single new task to the current `tasks.md` (spec-kit feature or OpenSpec change) without regenerating it |
| `fix-issues-after-analyze` | Apply fixes for findings from `speckit-analyze`, logging them to `issues-table.md` (spec-kit only) |
| `connect-playwright` | Connect Playwright MCP to this project — finds npx, writes the git-ignored MCP config for Claude Code / Codex CLI / opencode, verifies browser tools are available |

Depending on your harness, invoke these as `/start-guide` (Claude Code, opencode) or by name (Codex CLI and other Agent-Skills-only harnesses auto-select skills by relevance — you can still say "run the start-guide skill").

## Which toolkit this project uses

Each project uses exactly one toolkit, chosen when it was created. Tell which from the folder: `.specify/` → **spec-kit**, `openspec/` → **OpenSpec**. Follow only that toolkit's section below, and never mix their commands or documents in one project.

## How to run the spec-kit loop

- **Pace it.** Never run more than one `speckit-*` step without the user looking at the artifact it produced first. Stop, summarize what changed, and wait for an explicit go-ahead.
- **Command naming varies by agent.** spec-kit's own commands are invoked as `speckit-specify`, `speckit-plan`, ... in skills-mode agents (Claude Code, Codex CLI), or as `/speckit.specify`, `/speckit.plan`, ... in command-mode agents (opencode and others). Check what `specify init` actually installed for this user before assuming which form applies.
- **Specs describe *what*, never *how*.** If a tech stack, library, framework, or architecture detail shows up while drafting `spec.md`, redirect it to `speckit-plan` and say so out loud.
- **Default persistence model: living spec.** For a single-person, non-professional project, `spec.md` is always edited to reflect the feature's current true state, not appended to as a changelog. State this once, during `speckit-constitution`.
- **One feature = one user-visible action.** If a request bundles more than one, say so and suggest splitting it into separate `speckit-specify` runs.
- **`speckit-analyze` is read-only.** Its normal, healthy result is "go fix the spec/plan" — reaching it is not the end of the workflow. If it reports CRITICAL/HIGH findings, run `fix-issues-after-analyze`, then re-run analyze.
- **`speckit-converge` only appends tasks; it never writes code.** Always follow it with another `speckit-implement` pass, and repeat until converge appends nothing new.

## How to run the OpenSpec loop

- **Pace it.** Never run more than one `opsx` step without the user looking at what it produced first. Stop, summarize what changed, and wait for an explicit go-ahead.
- **Command naming varies by agent.** `/opsx:propose` in Claude Code, `/opsx-propose` in opencode and Cursor-style agents, `$openspec-propose` in Codex CLI. Check what `openspec init` installed for this user before assuming which form applies.
- **Loop:** `grill-me` → (`/opsx:explore`, optional) → `/opsx:propose` → review, correct, `/opsx:update`, `openspec validate <change>` → `/opsx:apply` → `/opsx:archive`.
- **Project rules live in `openspec/config.yaml`** (`context:` and `rules:`). They guide generation but are not enforced — check new documents against them yourself and point out conflicts.
- **Living spec is built in.** `openspec/specs/` is the current truth about the app; archive merges each change's spec deltas into it. Never edit `openspec/specs/` directly for a feature in progress — change the delta specs in the change folder.
- **Keep documents true.** If trying the feature shows the proposal, spec deltas, or design were wrong, fix those documents (then `/opsx:update`) before applying again — don't just patch the code.
- **One feature = one user-visible action = one change folder.** If a request bundles more than one, say so and suggest separate `/opsx:propose` runs.
- **Archive only finished work.** Only run `/opsx:archive` when every task in the change's `tasks.md` is ticked and the user has confirmed the feature works.
<!-- speckit-for-my-dad:end -->
