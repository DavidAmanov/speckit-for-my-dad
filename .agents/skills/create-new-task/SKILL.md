---
name: create-new-task
description: Form a new task and add it to tasks.md for the current spec-kit feature or OpenSpec change, matching that toolkit's task structure and intent. Use when the user runs /create-new-task or wants to add a single task without regenerating the whole task list.
---

Add exactly one new task to the current feature's `tasks.md`, matching its existing structure.

Which `tasks.md`: spec-kit (`.specify/` exists) → `specs/<feature>/tasks.md` of the current feature branch. OpenSpec (`openspec/` exists) → `openspec/changes/<change>/tasks.md` of the change in progress (not in `archive/`); if there are several, ask which one.

## Steps

1. **Ask the user questions, one at a time** — what the task is, which files/areas it touches, whether it depends on or blocks other tasks, and whether it can run in parallel with existing tasks.
2. **Check the existing artifacts** — read `spec.md`, `plan.md`, and `tasks.md` (spec-kit) or `proposal.md`, `specs/`, `design.md`, and `tasks.md` (OpenSpec) of the current feature to make sure the new task fits requirements it relates to and doesn't duplicate an existing task.
3. **Format the task** in the same structure as the other tasks in `tasks.md`. OpenSpec tasks are simpler — usually `- [ ] <group>.<n> <description>` under numbered group headings; copy that numbering and skip the fields below that the file doesn't use. For spec-kit:
   - Next available task ID (e.g. `T0NN`)
   - Clear description
   - File paths involved
   - `[P]` marker if it can run in parallel
   - User story reference `[US#]` if applicable
   - Dependencies on other tasks, if any
4. **Add it to `tasks.md`** — insert the task into the correct phase/section, respecting dependency order.
5. **Recommend next step** — after adding, tell the user in chat to run `speckit-analyze` / `/speckit.analyze` before running `speckit-implement` / `/speckit.implement` (spec-kit), or `openspec validate <change>` before `/opsx:apply` (OpenSpec), so the new task is checked first.

## Notes

- Ask questions one at a time so the user isn't overwhelmed.
- If the user's answers imply a change to the spec or plan (not just a new task), flag this to the user rather than silently adding it.
- Never mark the new task as completed (`[X]` / `[x]`) — always add it as `[ ]`.
