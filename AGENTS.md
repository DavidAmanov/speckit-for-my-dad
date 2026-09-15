# AGENTS.md

## What this repository is

This repo is a beginner-friendly wrapper around GitHub's [spec-kit](https://github.com/github/spec-kit) — a Specification-Driven Development (SDD) toolkit. It is not application code. It is `guide-for-dad.md` (a human-facing, step-by-step walkthrough) plus a small set of project skills (below) that make spec-kit safe and legible for someone with little or no coding background.

This file (`AGENTS.md`) is read natively by Codex CLI and opencode, and by Claude Code via the `CLAUDE.md` symlink at the repo root. Whichever agent you are, follow it.

## Language

Current communication language: **English (eng)**

Talk to the user in this language, and write all generated spec-kit documentation (`spec.md`, `plan.md`, `tasks.md`, etc.) in it, until the `choose-language` skill changes this line. Supported: `eng`, `rus`, `spa`, `fra`, `deu`, `ita`, `jpn`, `zho` — or any language the user names.

## Skills in this project

Canonical skill files live once in `.agents/skills/<name>/SKILL.md` — this is the location Codex CLI and opencode read natively. `.claude/skills/<name>` are symlinks to the same files, so Claude Code sees them too. **Edit only the files under `.agents/skills/`** — never edit through the `.claude/skills/` symlink path.

| Skill | Use it to... |
|---|---|
| `start-guide` | Walk `guide-for-dad.md` step by step, pausing for confirmation after each step |
| `choose-language` | Change the language setting above |
| `grill-me` | Interview the user until a feature idea is precise enough for `speckit-specify` |
| `teach-me` | Explain how *this* project currently works, not spec-kit in general |
| `where-am-i` | Recover context: where the user left off and what to do next |
| `create-new-task` | Add a single new task to the current `tasks.md` without regenerating it |
| `fix-issues-after-analyze` | Apply fixes for findings from `speckit-analyze`, logging them to `issues-table.md` |

Depending on your harness, invoke these as `/start-guide` (Claude Code, opencode) or by name (Codex CLI and other Agent-Skills-only harnesses auto-select skills by relevance — you can still say "run the start-guide skill").

## How to run the spec-kit loop

- **Pace it.** Never run more than one `speckit-*` step without the user looking at the artifact it produced first. Stop, summarize what changed, and wait for an explicit go-ahead.
- **Command naming varies by agent.** spec-kit's own commands are invoked as `speckit-specify`, `speckit-plan`, ... in skills-mode agents (Claude Code, Codex CLI), or as `/speckit.specify`, `/speckit.plan`, ... in command-mode agents (opencode and others). Check what `specify init` actually installed for this user before assuming which form applies.
- **Specs describe *what*, never *how*.** If a tech stack, library, framework, or architecture detail shows up while drafting `spec.md`, redirect it to `speckit-plan` and say so out loud.
- **Default persistence model: living spec.** For a single-person, non-professional project, `spec.md` is always edited to reflect the feature's current true state, not appended to as a changelog. State this once, during `speckit-constitution`.
- **One feature = one user-visible action.** If a request bundles more than one, say so and suggest splitting it into separate `speckit-specify` runs.
- **`speckit-analyze` is read-only.** Its normal, healthy result is "go fix the spec/plan" — reaching it is not the end of the workflow. If it reports CRITICAL/HIGH findings, run `fix-issues-after-analyze`, then re-run analyze.
- **`speckit-converge` only appends tasks; it never writes code.** Always follow it with another `speckit-implement` pass, and repeat until converge appends nothing new.
