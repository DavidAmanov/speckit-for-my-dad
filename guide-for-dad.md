# Welcome to Spec-Kit: Simplified Guide

## Glossary

Before you start, here are a few terms you'll see throughout this guide:

- **Spec-Kit** — a Specification-Driven Development (SDD) tool that turns a natural-language feature description into a specification, a plan, a task list, and a working implementation, through a repeatable loop.
- **SDD (Specification-Driven Development)** — a way of building software where you write down precisely *what* you want and *why* before any code is written, then review each intermediate document (spec, plan, tasks) before the next one is generated.
- **Harness / agent** — the AI coding tool you're chatting with (Claude Code, Codex CLI, opencode, or another) that can read your files, run commands on your computer, and run skills on your behalf.
- **Terminal** — the command-line window on your computer where you type and run commands (also called console or command prompt).
- **`.agents/skills/`** — where this project's own skills live, in a format shared by Claude Code, Codex CLI, opencode, and other modern agents. Each skill is a command (like `/start-guide` or `speckit-specify`) that performs one step of the workflow.
- **`AGENTS.md`** — this project's configuration file for the agent itself (current language, behavior rules). Claude Code reads it through `CLAUDE.md`.
- **Two folders** — the **speckit-for-my-dad folder** (this guide's home, used only for setup and for creating new projects) and your **project folder** (where your app lives). Step 6 creates the project folder and copies this guide and all the skills into it, so after that you only ever work in the project folder.
- **`spec.md` / `plan.md` / `tasks.md`** — the three core artifacts spec-kit produces for each feature: what to build, how to build it, and the ordered list of steps to build it.

## Project Purpose

This guide helps you build your own application or website using **spec-kit**, run through an AI coding agent. Spec-kit doesn't remove the work of building software — it moves the work from *writing code* to *writing precise requirements and checking each step*. You will not type much code yourself, but you will read documents and make decisions constantly. That's the deal, and it's a good one: mistakes get caught on paper (in `spec.md`), not after the app is half-built.

This guide and the skills next to it work with **Claude Code, Codex CLI, opencode**, and any other agent that supports the "Agent Skills" format — pick whichever you already have or prefer.

## How to Use This Guide

You have **two options**:

### Option 1: Manual Execution
Follow each step below yourself, running the commands in your terminal and the spec-kit commands in your agent chat.

### Option 2: Automatic Guide (Recommended)
Type the following in your agent chat:
```
/start-guide
```
The skill walks through each step for you **one at a time**, stopping after every step so you can look at what it produced before continuing. It will not run ahead of you.

Run it in the speckit-for-my-dad folder for setup. After Step 6 it asks you to open your agent in your new project folder and type `/start-guide` again — it continues from there.

---

## Part 1 — One-Time Setup

You do this once per computer (Steps 1–5) and once per project (Steps 6–7).

> **Reading this in your project folder?** Steps 1–6 are already done — this copy of the guide was put here by Step 6. Continue from Step 7, or from wherever you left off (`/where-am-i` tells you).

### Step 1: Choose Language

**Description:** Select the language for your communication with the agent and for all generated documentation.

- **Why it matters:** the entire guide and everything spec-kit generates (`spec.md`, `plan.md`, etc.) will be in this language.
- **Recommendation:** your native language, or English if you're comfortable with it.
- **How to proceed:** type `/choose-language`, pick a language. `AGENTS.md` is updated automatically, and Step 6 copies this choice into your new project. You can change it inside a project later with the same command.

---

### Step 2: Which Agent and Model to Use

**Description:** Pick your AI coding agent, and know which model tier to reach for at each step so you don't waste limits.

- **Agent:** any agent that supports Agent Skills works — Claude Code, Codex CLI, and opencode are all tested with this guide's skills. If you already use one, stick with it.
- **Model for planning/specification/constitution/design** (`speckit-constitution`, `speckit-specify`, `speckit-clarify`, `speckit-plan`): use your agent's top-tier ("Opus"-class or equivalent) model. These steps involve judgment calls that affect everything downstream.
- **Model for implementation** (`speckit-implement`): a mid-tier ("Sonnet"-class or equivalent) model handles well-described tasks fine, and is faster and cheaper.
- **Why it matters:** don't spend your limits on a top-tier model for routine, well-specified work like wiring up a button. Save the strong model for the thinking-heavy steps.

---

### Step 3: Install Git

**Description:** spec-kit uses git to track a branch and folder per feature. You need it installed even if you never type a git command yourself.

- **How to install:** [git-scm.com/downloads](https://git-scm.com/downloads), then verify with `git --version` in your terminal.

---

### Step 4: Install uv and Python

**Description:** spec-kit's installer (`uv`) and spec-kit itself need Python 3.11 or newer.

- **Install uv:**
  - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
  - Full instructions if these don't work: [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/)
  - Verify: `uv --version`
- **Python:** uv can install Python for you (`uv python install 3.12`), or get it from [python.org](https://www.python.org/downloads/) — **3.11 or higher is required**, spec-kit will not run on older versions. Verify: `python3 --version`

**If using `/start-guide`:** the agent checks for both and installs what's missing.

---

### Step 5: Install Spec-Kit

**Description:** Install the spec-kit CLI globally with uv.

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

- **Verification:** `specify --version`
- **Keeping it updated later:** `specify self upgrade`

---

### Step 6: Create Your Project

**Description:** Create a separate folder for your project, set it up for spec-kit and your agent, and copy this guide and all the skills into it.

In the agent chat, **in the speckit-for-my-dad folder**, type:

```
/new-project
```

It asks for a project name and where to put it (for example `~/projects/my-app`), then:
1. runs `specify init` for your agent — this decides whether spec-kit's commands are `speckit-specify` (skills) or `/speckit.specify` (slash commands);
2. copies the skills, this guide (`guide-for-dad.md`), and the rules from `AGENTS.md` into the new folder;
3. offers to save it all in git.

**Your project never goes inside the speckit-for-my-dad folder** — that would mix your app with this guide.

**What you get in the project folder:**
- `guide-for-dad.md` — a copy of this guide
- `AGENTS.md` and `CLAUDE.md` — the rules and language for the agent
- `.agents/skills/` and `.claude/skills/` — the skills (`/start-guide`, `/where-am-i`, ...) next to spec-kit's own
- `.specify/` — spec-kit's configuration, templates, and (soon) your project's constitution
- `specs/` — created once you run your first `speckit-specify`, one folder per feature

There is no "project type" prompt — spec-kit doesn't ask what kind of app you're building at this stage; that comes from what you tell it in `speckit-specify`.

- **Then switch folders:** close the agent, open it in your project folder (`/new-project` shows the exact command), and type `/start-guide`. Everything from Step 7 on happens there.
- **Doing it by hand instead:** `cd ~/projects && specify init my-app`, then in the speckit-for-my-dad folder run `/new-project ~/projects/my-app` — it sees spec-kit is already set up and only copies the guide and skills.

---

### Step 7: Constitution

**Description:** In your project folder, `speckit-constitution` (or `/speckit.constitution`) defines non-negotiable project principles (MUST/SHOULD rules) that every later step is checked against. Do this once per project, not once per feature.

- Keep it short and concrete. Good starter principles for a solo, non-professional project: *"use the simplest stack that works," "no new dependency without a stated reason," "every feature ships with a one-paragraph 'how to check this by hand' note."*
- **This project defaults to the "living spec" model**: `spec.md` for a feature is always edited to reflect its current true state, not appended to like a changelog. Your agent should mention this to you once here — if it doesn't, you can say it yourself.
- **What to check:** open `.specify/memory/constitution.md` afterward. Does it actually match how you want to work? These rules will block or reshape later steps, so fix anything wrong now.

---

## Part 2 — The Per-Feature Loop

**This is the part you repeat for every feature, forever.** One pass through Steps 8–16 builds one feature. When you want the next feature, start again at Step 8.

**Rule of thumb: one feature = one user-visible action.** "Let users upload a photo" is one feature. "A photo album app" is ten features wearing a trenchcoat — if your idea sounds like several things a user could do separately, split it and run this loop once per piece.

### Step 8: Grill Me (optional but recommended for your first few features)

**Description:** `/grill-me` interviews you about the feature idea, one question at a time, until it's precise enough to specify.

- **Why it matters:** a vague idea in → a vague, wrong spec out. This step catches that before spec-kit writes anything.
- Keep answers about *what* the feature does, not *how* it's built — if you catch yourself naming a database or a framework, that's for Step 12 (plan), not here.

---

### Step 9: Specify

**Description:** `speckit-specify` transforms your feature idea into a structured specification: functional requirements, success criteria, user stories.

- **Rule: no tech stack in the spec.** Describe *what* the user sees and does, never *how* it's built. If the generated `spec.md` mentions a specific library, framework, or database, that's a sign it wandered into planning territory — push it back to Step 12.
- **What to check** in the generated `spec.md`:
  - Does it describe what the user sees/does, not how it's implemented?
  - Can you point at each requirement and say "done" or "not done" — nothing vague like "the app should be fast"?
  - Does it only contain what you actually asked for — nothing invented?

---

### Step 10: Clarify

**Description:** `speckit-clarify` finds unclear areas in the spec and resolves them by asking you targeted questions.

- **What to check:** after this step, re-skim `spec.md` — every "TBD" or ambiguity you remember should now be resolved.

---

### Step 11: Checklist

**Description:** `speckit-checklist` generates domain-specific quality checklists (UX, API, security, performance) that check the *requirements*, not the implementation — think of it as "unit tests for the spec."

- **What to check:** read the generated checklist and answer honestly — if an item fails, that's a gap in `spec.md`, go fix it there before moving on.

---

### Step 12: Plan

**Description:** `speckit-plan` is where the tech stack finally enters — a technical architecture and implementation plan based on your spec.

- **What to check** in `plan.md`: does the stack sound reasonable for something this small? Simpler is almost always better for a first feature. If it looks over-engineered, say so — your constitution (Step 7) should be pushing back on this too.

---

### Step 13: Tasks

**Description:** `speckit-tasks` converts spec + plan into an ordered, dependency-aware task list.

- **What to check:** skim `tasks.md` — does the number of tasks feel proportional to the feature? Dozens of tasks for a small feature is a sign the feature should have been split back in Step 8.
- Need to add one task later without regenerating the whole list? Use `/create-new-task`.

---

### Step 14: Analyze

**Description:** `speckit-analyze` is a **read-only** cross-check of spec, plan, tasks, and your constitution, for duplication, ambiguity, gaps, and conflicts.

- **This step routinely sends you backward — that's normal, not a failure.** If it reports CRITICAL or HIGH findings, run `/fix-issues-after-analyze`, then run `speckit-analyze` again. Only move on to Step 15 once it's clean or you've explicitly accepted the remaining low-severity notes.
- `/fix-issues-after-analyze` keeps a running log in `issues-table.md` — if the same problem keeps reappearing (its "times fixed" count climbs), that's worth stopping and investigating rather than patching again.

---

### Step 15: Implement

**Description:** `speckit-implement` processes the task list and writes the actual implementation.

- **What to check:** this is the step where you actually try the feature. Run the app, do the thing the feature describes, and confirm it works the way `spec.md` said it should.

---

### Step 16: Converge

**Description:** `speckit-converge` compares the codebase against spec/plan/tasks and **appends** any remaining unbuilt work as new tasks — it never writes code itself.

- **If it appends anything, go back to Step 15** (`speckit-implement`) to build those new tasks, then run converge again. Repeat until a converge pass appends nothing — that's when the feature is actually done, not when Step 15 first finishes.

---

### Step 17 (optional): Tasks to Issues

**Description:** `speckit-taskstoissues` converts the task list into GitHub issues, for tracking work with other people.

- Only useful if you're on GitHub and collaborating with others. Skip it if you're working solo — there's nothing to track issues *for*.

---

## What Happens Next

You've finished one feature. To build another, **go back to Step 8** with the next idea. The constitution (Step 7) and the setup (Steps 1–6) don't repeat for this project — everything else does, once per feature, for the life of the project.

If you ever lose track of where you are, run `/where-am-i` instead of guessing.

---

## Frequently Asked Questions

**Q: Do I need to know how to code?**
A: You won't type much code yourself — but you will read and judge every generated document (`spec.md`, `plan.md`, `tasks.md`) and decide whether it's right before the next step builds on it. SDD moves the work from *writing code* to *writing precise requirements and reviewing results*; it doesn't remove the work. Skipping the review steps is how you end up with something that "works" but isn't what you wanted.

**Q: Can I customize the generated code?**
A: Yes — spec-kit generates a real codebase you can edit like any other.

**Q: What if I get stuck?**
A: Run `/where-am-i` to get your bearings, or `/explain-me` to have the agent explain the part of this specific project you're confused about, grounded in your actual files.

**Q: How long does a first small feature take?**
A: Expect roughly 1–3 hours for a genuinely small, single-action feature, most of it reading and deciding, not waiting. A whole first app is many features, so budget accordingly — don't expect "app in an afternoon."

**Q: How do I start a second project?**
A: Go back to the speckit-for-my-dad folder and run `/new-project` again (Step 6). Steps 1–5 don't repeat — the tools are already installed.

**Q: How do I get a newer version of the guide and skills into my project?**
A: In the speckit-for-my-dad folder, run `git pull`, then `/new-project ~/projects/my-app` (your project's path). It updates only the guide, the skills, and the rules block in `AGENTS.md` — your code, specs, and language setting stay as they are. If you edited your copy of the guide, it asks before replacing it.

**Q: Do I have to use Claude Code?**
A: No — this guide and its skills work with Claude Code, Codex CLI, and opencode, and should work with any agent that supports the shared "Agent Skills" format. Command names may look slightly different (`speckit-specify` vs. `/speckit.specify`) depending on which one you picked in `specify init`.

---

## Notes

- Keep the "Language" line in `AGENTS.md` current if you switch languages — each project has its own.
- Don't edit the skills or this guide inside a project folder: updates overwrite them. Change them in the speckit-for-my-dad folder, then update the project.
- Review every generated artifact (`spec.md`, `plan.md`, `tasks.md`, and the code itself) — don't rubber-stamp any step.
- Use version control (git) — spec-kit already does, one branch per feature; commit your own edits too.
- Update spec-kit occasionally: `specify self upgrade`.

---

**Ready to get started?** Type `/start-guide` in your agent chat now!
