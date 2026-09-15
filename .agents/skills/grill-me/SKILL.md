---
name: grill-me
description: Interview the user relentlessly about a plan, design, or feature idea until reaching shared understanding, resolving each branch of the decision tree. Use when the user wants to stress-test a plan, get grilled on their design, mentions "grill me", or is about to run /speckit.specify with an idea that is still vague.
---

<!-- Adapted from Rob Mitterando's grill-me-skill: https://github.com/RobMitt/grill-me-skill
     See LICENSE in this repo's root for attribution details. -->

Interview the user relentlessly about every aspect of their plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

## How to ask questions

Use the **AskUserQuestion tool** for every question you ask. Never pose questions as plain text in your response — always use the multiple-choice popup so the user can quickly select an answer or type a custom one.

Ask **one question at a time**. Wait for the user's answer before moving to the next question. This keeps the conversation focused and prevents overwhelm.

For each question, provide 2–4 concrete multiple-choice options representing the most likely answers or directions. Think about what the user would realistically choose — generic options like "Yes" / "No" aren't helpful unless the question is genuinely binary. The user always has the "Other" field available to write something custom.

## Flow

1. After receiving an answer, briefly acknowledge the decision (1–2 sentences max), then immediately ask the next question via AskUserQuestion.
2. If a question can be answered by exploring the codebase or files, explore them yourself instead of asking the user.
3. Continue until all branches of the design tree are resolved.
4. When finished, provide a concise summary of all decisions made.

## When used before `/speckit.specify`

- Keep every question about *what* the user wants and *why*, never about implementation (languages, frameworks, databases) — that belongs to `/speckit.plan`, not here. If the user volunteers a tech-stack answer, note it aside for the planning step and steer the question back to behavior.
- Explicitly resolve scope: does this idea describe **one** user-visible action, or several? If several, say so and ask the user to pick the first one — the rest become separate features, each with their own `/speckit.specify` run later.
- End by handing the user a one-paragraph restatement of the feature and asking them to confirm before you (or they) run `/speckit.specify` with it.
