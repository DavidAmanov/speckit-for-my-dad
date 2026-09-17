---
name: where-am-i
description: Analyze the current project state and remind the user where they left off, then offer options for what to do next. Use when the user runs /where-am-i or says they're lost, confused, or don't remember what they were doing.
---

Figure out where the user left off and tell them, in plain language, then offer next steps.

## What to check

1. Review the current chat history for what was being worked on.
2. Check the most recent git commit: message and changed files (`git log -1` and `git show --stat HEAD`).
3. Check for a `.specify/` or `specs/*/` directory. If a feature branch/folder exists, read whichever of `spec.md`, `plan.md`, `tasks.md`, or `issues-table.md` was modified most recently, and note how many tasks in `tasks.md` are checked off (`[X]`) versus open (`[ ]`).
4. Check for any recent error output in the conversation that was never resolved.
5. Check which folder you're in:
   - `.agents/skills/new-project/SKILL.md` exists → this is the speckit-for-my-dad folder, not a project. Projects live in their own folders. Tell the user that, and offer `/new-project` for a new one, or ask them to open the agent in their project folder to continue one.
   - `.agents/speckit-for-my-dad.version` exists → this is a project. Read its `commit=` and `source=`. If the source folder still exists, compare with `git -C <source> rev-parse --short HEAD`; if they differ, mention in one line that newer skills and guide are available (`/new-project <this folder>` in the speckit-for-my-dad folder).

## Report to the user

Summarize in plain language: what feature/step they're on, what artifact exists, and what state it's in (e.g. "you have a plan and 8 tasks, 3 done, 5 open, and you haven't run implement yet").

Then present these options:

1. **Continue** — if there is remaining work (unfinished tasks, the next step in the spec-kit loop per `guide-for-dad.md`), offer to continue it. Name the specific next command (e.g. `speckit-implement` or `/speckit.implement`).
2. **Review the code** — run a code review of the recent changes.
3. **I don't understand, explain again** — ask the user what specifically was unclear, give a focused explanation of just that point, then present these same three options again.

## Notes

- If no plan or log file exists yet, base the summary only on chat history and the last commit.
- If there is no remaining work, omit the "Continue" option and instead confirm the feature loop is complete and ask if they want to start a new feature (pointing to `/grill-me` → `speckit-specify`).
- Option 3 can repeat as many times as needed until the user picks something else.
