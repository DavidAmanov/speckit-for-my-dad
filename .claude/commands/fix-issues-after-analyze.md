---
name: fix-issues-after-analyze
description: Fix the inconsistencies that speckit-analyze / /speckit.analyze found between the specification, plan, and tasks, and log every fix to issues-table.md. Use when the user runs /fix-issues-after-analyze, right after an analyze pass reports findings.
---

Fix the inconsistencies that the spec-kit analyze step found between the specification, plan, and tasks.

## When to use

spec-kit projects only (`.specify/` exists). OpenSpec has no analyze step — in an OpenSpec project, say so and suggest correcting the change's documents, `/opsx:update`, and `openspec validate <change>` instead.


Run this right after `speckit-analyze` / `/speckit.analyze` reports findings (duplications, ambiguities, underspecification, constitution conflicts, coverage gaps, or inconsistencies).

## Steps

1. **Read the analysis output** — use the findings from the most recent analyze run.
2. **Triage each finding** — group by severity (CRITICAL, HIGH, MEDIUM, LOW) and by which artifact it touches (spec, plan, tasks, or code).
3. **Fix each finding** — apply the smallest correct edit to resolve it:
   - Duplications: merge or remove the redundant requirement/task
   - Ambiguities: rewrite the vague wording to be specific and testable
   - Underspecification: fill in the missing detail directly in the relevant artifact
   - Constitution conflicts: adjust the conflicting artifact to comply, or flag it for the user if the constitution itself needs to change
   - Coverage gaps: add the missing task(s) so every requirement maps to a task
   - Terminology inconsistencies: align wording across spec, plan, and tasks
4. **Report what changed** — summarize each fix applied, and list any findings that could not be resolved automatically (e.g. ones that require a user decision).
5. **Update `issues-table.md`** — in the current spec branch's folder (`specs/[feature]/issues-table.md`), create the file if it doesn't exist yet, then record each fix in a table with exactly these columns and nothing else:

   | Problem | Why it appeared | Times fixed | How it was fixed |
   |---------|------------------|-------------|-------------------|

   - If a problem is new, add a row with "Times fixed" set to 1.
   - If a problem already has a row (same or effectively the same problem), increment "Times fixed" and update "How it was fixed" with the latest fix.
6. **Flag repeat problems** — after updating the table, check it for any problem with "Times fixed" greater than 1 and report those to the user in chat, noting that a recurring fix may indicate a cyclical error worth investigating.

## Notes

- Only fix findings actually reported by the analyze step — do not go looking for new issues.
- Fix CRITICAL and HIGH findings first.
- If a finding requires a judgment call the user should make, surface it instead of guessing.
- After fixing, recommend re-running `speckit-analyze` / `/speckit.analyze` to confirm the issues are resolved.
- `issues-table.md` contains only the table — no other content.
