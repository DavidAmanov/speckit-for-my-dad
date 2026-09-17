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

## Language

Read the "Language" section of `AGENTS.md` and speak to the user in that language for the rest of the walkthrough, including this skill's own messages.

## Where are you? Pick the part

The guide runs in two folders. Work out which one you're in:

- **speckit-for-my-dad folder** — `.agents/skills/new-project/SKILL.md` exists. Run **Part A**.
- **User's project folder** — `.agents/speckit-for-my-dad.version` exists. Run **Part B**.
- Neither — say you can't tell where you are, and ask the user to open the agent in the speckit-for-my-dad folder (for a new project) or in their project folder (to continue one).

Step numbers below match `guide-for-dad.md`.

## Part A — setup, in the speckit-for-my-dad folder

1. **Choose language** — `/choose-language`, only if the user wants to change the current value. Mention that the language is copied into the new project at Step 6.
2. **Agent and model** — confirm which AI agent and model tiers the user is using (informational, no install).
3. **Git** — check `git --version`; if missing, point the user to https://git-scm.com/downloads and wait.
4. **uv and Python** — check `uv --version`; if missing, run the official installer for the user's OS. Check Python 3.11+; if missing, offer `uv python install 3.12`, or point to https://www.python.org/downloads/.
5. **spec-kit** — `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`, then verify with `specify --version`. If it's already installed, skip.
6. **Create the project** — run `/new-project`. It creates the project in its own folder and copies the skills and this guide into it.

Then stop. Tell the user plainly that the rest happens in the new folder: close this agent, open it in the project folder (`new-project` printed the exact command), and type `/start-guide` again. Do not continue with Part B from here.

If the user already has a project and only wants to continue it, skip straight to telling them to open the agent in that folder.

## Part B — in the user's project folder

First check where the project is:

- No `.specify/memory/constitution.md`, or it's still the unfilled template → start at Step 7.
- Constitution filled in → it's already done. Run the checks from `where-am-i` and continue from the step the user is actually on (usually Step 8 with a new feature idea). Say which step you're starting from and why.

Then, after reading the files `specify init` installed (`.claude/skills/speckit-*`, `.agents/skills/speckit-*`, or `.opencode/commands/speckit.*`), work out whether spec-kit commands are invoked as `speckit-specify` (skills-mode) or `/speckit.specify` (command-mode) for this user's agent, and use that exact form for the rest of the session.

7. **Constitution** — `speckit-constitution` / `/speckit.constitution`, including telling the user, once, that this project defaults to the "living spec" model (spec.md is always edited to reflect current truth, not appended to). Before Step 8, explain that the per-feature loop is about to start and repeats for every new feature from here on.
8. **Grill me** — `/grill-me` on the user's feature idea, until it is one clear user-visible action
9. **Specify** — `speckit-specify` / `/speckit.specify`
10. **Clarify** — `speckit-clarify` / `/speckit.clarify`
11. **Checklist** — `speckit-checklist` / `/speckit.checklist`
12. **Plan** — `speckit-plan` / `/speckit.plan`
13. **Tasks** — `speckit-tasks` / `/speckit.tasks`
14. **Analyze** — `speckit-analyze` / `/speckit.analyze`. If it reports CRITICAL/HIGH findings, run `/fix-issues-after-analyze`, then re-run analyze before continuing; only move on once it's clean or the user explicitly accepts remaining LOW findings
15. **Implement** — `speckit-implement` / `/speckit.implement`
16. **Converge** — `speckit-converge` / `/speckit.converge`. If it appends any tasks, go back to Step 15; repeat until it appends nothing
17. Tell the user this feature is done, and that Steps 8–16 are the loop they repeat for every future feature. `taskstoissues` is optional and only useful if they're tracking work on GitHub with other people

## Notes

- Never run `/speckit.implement` or `/speckit.converge`'s follow-up implement pass without the user having seen the current `tasks.md`.
- If the user seems lost mid-walkthrough, suggest `/where-am-i` instead of guessing.
