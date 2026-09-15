---
name: start-guide
description: Walk the user through the entire spec-kit-for-my-dad setup and first-feature loop, one step at a time, pausing for the user's go-ahead after every step. Use when the user runs /start-guide or asks to begin, set up, or get started with this project.
---

Read `guide-for-dad.md` in full before doing anything else. Then execute its steps **one at a time, in order**, exactly as written below. Do not skip ahead, do not batch multiple steps into one turn, and do not treat this as a checklist to blast through — the entire point of spec-kit is that a human looks at each artifact before the next step builds on it.

## Rules for every step

1. Announce which step you're starting and why it matters, in one or two sentences.
2. Do the step (run the command, invoke the `speckit-*`/`/speckit.*` command, ask the question — whichever the step calls for).
3. If the step produced a file (`spec.md`, `plan.md`, `tasks.md`, ...), tell the user in plain language what to open and what to check, using the "What to check" list for that step in `guide-for-dad.md`. Do not just say "done, moving on."
4. Stop and wait for the user to say to continue. Never chain two `speckit-*` steps in the same turn without the user confirming in between.
5. If a step fails (missing tool, error), fix or explain it before moving on — do not silently skip a failed step.

## Language and agent detection

- Read the "Language" section of `AGENTS.md` and speak to the user in that language for the rest of the walkthrough, including this skill's own messages.
- Before Step 4 (`specify init`), figure out which coding agent the user is actually running you as (Claude Code, Codex CLI, opencode, or another). If unclear, ask. Pass the matching `--integration` value to `specify init` (or let the interactive picker in `specify init` handle it — either is fine, just don't guess silently).
- After `specify init` finishes, check what it printed or what got installed (`.claude/skills/speckit-*`, `.agents/skills/speckit-*`, or `.opencode/commands/speckit.*`) to learn whether spec-kit commands are invoked as `speckit-specify` (skills-mode) or `/speckit.specify` (command-mode) for this user's agent, and use that exact form for the rest of the session.

## Steps to execute

Follow `guide-for-dad.md` section by section:

1. Choose language (`/choose-language`, only if the user wants to change from the current value)
2. Confirm which AI agent + model tiers the user is using (informational, no install)
3. Check for `git`; if missing, point the user to https://git-scm.com/downloads and wait
4. Check for `uv`; if missing, run the official installer for the user's OS
5. Check for Python 3.11+; if missing, point to https://www.python.org/downloads/
6. Install spec-kit: `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`, then verify with `specify --version`
7. `specify init` — new project, with agent detection as above
8. `speckit-constitution` / `/speckit.constitution` — including telling the user, once, that this project defaults to the "living spec" model (spec.md is always edited to reflect current truth, not appended to)
9. Explain the per-feature loop is about to start, and that it repeats for every new feature from here on
10. `/grill-me` on the user's first feature idea, until it is one clear user-visible action
11. `speckit-specify` / `/speckit.specify`
12. `speckit-clarify` / `/speckit.clarify`
13. `speckit-checklist` / `/speckit.checklist`
14. `speckit-plan` / `/speckit.plan`
15. `speckit-tasks` / `/speckit.tasks`
16. `speckit-analyze` / `/speckit.analyze` — if it reports CRITICAL/HIGH findings, run `/fix-issues-after-analyze`, then re-run analyze before continuing; only move on once it's clean or the user explicitly accepts remaining LOW findings
17. `speckit-implement` / `/speckit.implement`
18. `speckit-converge` / `/speckit.converge` — if it appends any tasks, go back to step 17; repeat until it appends nothing
19. Tell the user their first feature is done, and that steps 10–18 are the loop they repeat for every future feature — `taskstoissues` is optional and only useful if they're tracking work on GitHub with other people

## Notes

- Never run `/speckit.implement` or `/speckit.converge`'s follow-up implement pass without the user having seen the current `tasks.md`.
- If the user seems lost mid-walkthrough, suggest `/where-am-i` instead of guessing.
