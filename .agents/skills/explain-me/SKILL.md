---
name: explain-me
description: Explain how this specific project works, grounded in its actual current skills, rules, and files, not a generic description of spec-kit or OpenSpec. Use when the user runs /explain-me or asks how something in this project works.
---

Explain this project to the user, grounded in what is actually here — never a generic description of spec-kit, OpenSpec, or AI coding agents in general.

## Before answering

1. Read every `SKILL.md` under `.agents/skills/` to know what skills actually exist and what they actually do.
2. Read `AGENTS.md` for the current language setting, the list of skills, and the behavioral rules this project runs under.
3. Read `guide-for-dad.md` for the full step-by-step workflow and glossary.
4. In the speckit-for-my-dad folder (`.agents/skills/new-project/` exists), read `README.md` for the overview. In a user project, `README.md` belongs to the user's app — read `.agents/speckit-for-my-dad.version` instead to know which version of the skills and guide is installed.
5. If the project has a `.specify/` or `specs/` directory (spec-kit) or an `openspec/` directory (OpenSpec) already, skim what's in there too, and explain only the toolkit this project uses — the user may be asking about their actual current spec/plan/tasks, not the abstract workflow.

## Then

6. Ask the user, in one open-ended question, in the project's configured language (`AGENTS.md` → Language), what they want to understand.
7. If the question is vague, ask one short follow-up to narrow it down before explaining.
8. Explain — grounded specifically in what was read in steps 1–5: real skill names, real file paths, real current state (e.g. "your `spec.md` currently has 3 user stories" rather than "a spec.md typically has user stories").
9. If something the user asks about doesn't exist yet in the project, say so directly instead of describing it as if it exists.
10. After explaining, offer to go deeper on any part of the answer or move to a different topic.
