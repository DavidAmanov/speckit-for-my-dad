---
name: create-new-task
description: Form a new task and add it to tasks.md for the current spec-kit feature, matching spec-kit's task structure and intent. Use when the user runs /create-new-task or wants to add a single task without regenerating the whole task list.
---

Add exactly one new task to the current feature's `tasks.md`, matching spec-kit's existing structure.

## Steps

1. **Ask the user questions, one at a time** — what the task is, which files/areas it touches, whether it depends on or blocks other tasks, and whether it can run in parallel with existing tasks.
2. **Check the existing artifacts** — read `spec.md`, `plan.md`, and `tasks.md` in the current spec branch's folder to make sure the new task fits requirements it relates to and doesn't duplicate an existing task.
3. **Format the task** in the same structure as the other tasks in `tasks.md`:
   - Next available task ID (e.g. `T0NN`)
   - Clear description
   - File paths involved
   - `[P]` marker if it can run in parallel
   - User story reference `[US#]` if applicable
   - Dependencies on other tasks, if any
4. **Add it to `tasks.md`** — insert the task into the correct phase/section, respecting dependency order.
5. **Recommend next step** — after adding, tell the user in chat to run `speckit-analyze` / `/speckit.analyze` before running `speckit-implement` / `/speckit.implement`, so the new task is checked for consistency with the spec and plan first.

## Notes

- Ask questions one at a time so the user isn't overwhelmed.
- If the user's answers imply a change to the spec or plan (not just a new task), flag this to the user rather than silently adding it.
- Never mark the new task as completed `[X]` — always add it as `[ ]`.
