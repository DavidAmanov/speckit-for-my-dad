# Welcome to Spec-Kit: Simplified Guide

## Glossary

Before you start, here are a few terms you'll see throughout this guide:

- **SDD (Specification-Driven Development)** — a way of building software where you write down precisely *what* you want and *why* before any code is written, then review each intermediate document before the next one is generated.
- **Toolkit** — the SDD tool that drives the work. This guide supports two, and you pick one per project in Step 4:
  - **Spec-Kit** — GitHub's toolkit. Turns a feature description into a specification, a plan, a task list, and a working implementation through a strict, many-step loop with a check at every stage.
  - **OpenSpec** — a lighter toolkit. Each feature is a "change" folder with a proposal, the spec changes, a design, and tasks, made in one go; when it's built, the change is merged into the project's permanent specs.
- **Harness / agent** — the AI coding tool you're chatting with (Claude Code, Codex CLI, opencode, or another) that can read your files, run commands on your computer, and run skills on your behalf.
- **Terminal** — the command-line window on your computer where you type and run commands (also called console or command prompt).
- **`.agents/skills/`** — where this project's own skills live, in a format shared by Claude Code, Codex CLI, opencode, and other modern agents. Each skill is a command (like `/start-guide` or `speckit-specify`) that performs one step of the workflow.
- **`AGENTS.md`** — this project's configuration file for the agent itself (current language, behavior rules). Claude Code reads it through `CLAUDE.md`.
- **Two folders** — the **speckit-for-my-dad folder** (this guide's home, used only for setup and for creating new projects) and your **project folder** (where your app lives). Step 6 creates the project folder and copies this guide and all the skills into it, so after that you only ever work in the project folder.
- **Spec-Kit files:** `spec.md` / `plan.md` / `tasks.md` — what to build, how to build it, and the ordered list of steps to build it, one set per feature in `specs/<feature>/`.
- **OpenSpec files:** `openspec/changes/<change>/` — one folder per feature in progress (`proposal.md`, spec changes, `design.md`, `tasks.md`); `openspec/specs/` — the permanent description of how the whole app behaves right now.

## Project Purpose

This guide helps you build your own application or website using an SDD toolkit — **spec-kit** or **OpenSpec** — run through an AI coding agent. The toolkit doesn't remove the work of building software — it moves the work from *writing code* to *writing precise requirements and checking each step*. You will not type much code yourself, but you will read documents and make decisions constantly. That's the deal, and it's a good one: mistakes get caught on paper, not after the app is half-built.

This guide and the skills next to it work with **Claude Code, Codex CLI, opencode**, and any other agent that supports the "Agent Skills" format — pick whichever you already have or prefer.

## How to Use This Guide

You have **two options**:

### Option 1: Manual Execution
Follow each step below yourself, running the commands in your terminal and the toolkit commands in your agent chat.

### Option 2: Automatic Guide (Recommended)
Type the following in your agent chat:
```
/start-guide
```
The skill walks through each step for you **one at a time**, stopping after every step so you can look at what it produced before continuing. It will not run ahead of you.

Run it in the speckit-for-my-dad folder for setup. After Step 6 it asks you to open your agent in your new project folder and type `/start-guide` again — it continues from there.

---

## Part 1 — One-Time Setup

You do Steps 1–3 once per computer, Steps 4–5 once per computer *per toolkit*, and Steps 6–7 once per project.

> **Reading this in your project folder?** Steps 1–6 are already done — this copy of the guide was put here by Step 6. Continue from Step 7, or from wherever you left off (`/where-am-i` tells you).

### Step 1: Choose Language

**Description:** Select the language for your communication with the agent and for all generated documentation.

- **Why it matters:** the entire guide and every document the toolkit generates will be in this language.
- **Recommendation:** your native language, or English if you're comfortable with it.
- **How to proceed:** type `/choose-language`, pick a language. `AGENTS.md` is updated automatically, and Step 6 copies this choice into your new project. You can change it inside a project later with the same command.

---

### Step 2: Which Agent and Model to Use

**Description:** Pick your AI coding agent, and know which model tier to reach for at each step so you don't waste limits.

- **Agent:** any agent that supports Agent Skills works — Claude Code, Codex CLI, and opencode are all tested with this guide's skills. If you already use one, stick with it.
- **Model for thinking steps** — spec-kit: `speckit-constitution`, `speckit-specify`, `speckit-clarify`, `speckit-plan`; OpenSpec: `explore`, `propose`, `update`. Use your agent's top-tier ("Opus"-class or equivalent) model. These steps involve judgment calls that affect everything downstream.
- **Model for building** — spec-kit: `speckit-implement`; OpenSpec: `apply`. A mid-tier ("Sonnet"-class or equivalent) model handles well-described tasks fine, and is faster and cheaper.
- **Why it matters:** don't spend your limits on a top-tier model for routine, well-specified work like wiring up a button. Save the strong model for the thinking-heavy steps.

---

### Step 3: Install Git

**Description:** Git saves the history of your project, so any step can be undone. Spec-kit also uses it to keep a branch per feature. You need it installed even if you never type a git command yourself.

- **How to install:** [git-scm.com/downloads](https://git-scm.com/downloads), then verify with `git --version` in your terminal.

---

### Step 4: Choose Your Toolkit — Spec-Kit or OpenSpec

**Description:** Pick which SDD toolkit drives your project. Both do the same basic job — you describe a feature in words, the agent writes documents, you check them, the agent builds it — but at a different pace. Pick one; this step then installs what that toolkit needs.

#### Option A: Spec-Kit

A strict, step-by-step process: constitution → specify → clarify → checklist → plan → tasks → analyze → implement → converge. Each step makes or checks one document, and you review it before the next.

- **Best for:**
  - a brand-new app you're starting from scratch;
  - learning SDD properly — every stage is a separate, visible step;
  - bigger features, where catching a mistake on paper saves hours;
  - when you want as many automatic checks as possible (`clarify`, `checklist`, `analyze`, `converge`).
- **Downside:** more steps and more reading per feature; slower for small changes.
- **Needs:** uv and Python 3.11+.

#### Option B: OpenSpec

A light process: propose → apply → archive. One command writes the whole package for a feature at once (proposal, spec changes, design, tasks), you review and adjust it, the agent builds it, then the change is merged into the project's permanent specs.

- **Best for:**
  - adding features to or changing an app that already exists (including one you didn't build with this guide);
  - lots of small and medium changes, quickly;
  - when you want one up-to-date description of how the whole app behaves (`openspec/specs/`), kept current automatically;
  - when you already know fairly well what you want.
- **Downside:** fewer built-in checks — reviewing the documents carefully is more on you.
- **Needs:** Node.js 20.19 or newer.

**Not sure?** For a first, new project, pick **Spec-Kit** — its extra steps teach you what good requirements look like. Pick **OpenSpec** if you're changing an existing app, or once the spec-kit loop feels slow for your small changes. The choice is per project: a later project can use the other one.

#### Install what your toolkit needs

**If you chose Spec-Kit — uv and Python:**

- **Install uv:**
  - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
  - Full instructions if these don't work: [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/)
  - Verify: `uv --version`
- **Python:** uv can install Python for you (`uv python install 3.12`), or get it from [python.org](https://www.python.org/downloads/) — **3.11 or higher is required**, spec-kit will not run on older versions. Verify: `python3 --version`

**If you chose OpenSpec — Node.js:**

- **Install Node.js** (the LTS version) from [nodejs.org](https://nodejs.org/en/download) — **20.19.0 or higher is required**.
- Verify: `node --version` and `npm --version`

**If using `/start-guide`:** the agent asks you which toolkit you want, shows these two options, then checks for what that toolkit needs and installs what's missing.

---

### Step 5: Install the Toolkit

**Description:** Install the toolkit you chose in Step 4, globally, so every project can use it.

**Spec-Kit:**

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

- **Verification:** `specify --version`
- **Keeping it updated later:** `specify self upgrade`

**OpenSpec:**

```bash
npm install -g @fission-ai/openspec@latest
```

- **Verification:** `openspec --version`
- **Keeping it updated later:** run the same install command again, then `openspec update` inside each project.

---

### Step 6: Create Your Project

**Description:** Create a separate folder for your project, set it up for your toolkit and your agent, and copy this guide and all the skills into it.

In the agent chat, **in the speckit-for-my-dad folder**, type:

```
/new-project
```

It asks for a project name, where to put it (for example `~/projects/my-app`), and which toolkit (if you didn't already pick one in `/start-guide`), then:
1. sets the toolkit up for your agent:
   - Spec-Kit: runs `specify init` — this decides whether spec-kit's commands are `speckit-specify` (skills) or `/speckit.specify` (slash commands);
   - OpenSpec: runs `openspec init` — it prints how its commands look in your agent (`/opsx:propose` in Claude Code, `/opsx-propose` in opencode, `$openspec-propose` in Codex);
2. copies the skills, this guide (`guide-for-dad.md`), and the rules from `AGENTS.md` into the new folder;
3. offers to save it all in git.

**Your project never goes inside the speckit-for-my-dad folder** — that would mix your app with this guide.

**What you get in the project folder:**
- `guide-for-dad.md` — a copy of this guide
- `AGENTS.md` and `CLAUDE.md` — the rules and language for the agent
- `.agents/skills/` and `.claude/skills/` — the skills (`/start-guide`, `/where-am-i`, ...) next to the toolkit's own
- Spec-Kit: `.specify/` — spec-kit's configuration, templates, and (soon) your project's constitution; `specs/` appears with your first `speckit-specify`, one folder per feature
- OpenSpec: `openspec/` — `config.yaml` (project context and rules), `specs/` (how the app behaves, filled in as features are finished), `changes/` (features in progress)

There is no "project type" prompt — neither toolkit asks what kind of app you're building at this stage; that comes from what you tell it when you describe your first feature.

- **Then switch folders:** close the agent, open it in your project folder (`/new-project` shows the exact command), and type `/start-guide`. Everything from Step 7 on happens there.
- **Doing it by hand instead:** Spec-Kit — `cd ~/projects && specify init my-app`; OpenSpec — `mkdir -p ~/projects/my-app && cd ~/projects/my-app && git init && openspec init`. Then in the speckit-for-my-dad folder run `/new-project ~/projects/my-app` — it sees the toolkit is already set up and only copies the guide and skills.
- **Already have an app?** (OpenSpec's strong side.) Run `/new-project` with the path to your existing app's folder. It asks before touching anything and runs `openspec init` right there — your code stays as it is.

---

### Step 7: Project Rules

**Description:** Write down, once per project, the principles every later step is checked against. Do this once per project, not once per feature.

- Keep them short and concrete. Good starter principles for a solo, non-professional project: *"use the simplest stack that works," "no new dependency without a stated reason," "every feature ships with a one-paragraph 'how to check this by hand' note."*

**Spec-Kit — constitution:** run `speckit-constitution` (or `/speckit.constitution`). It writes non-negotiable MUST/SHOULD rules.

- **This project defaults to the "living spec" model**: `spec.md` for a feature is always edited to reflect its current true state, not appended to like a changelog. Your agent should mention this to you once here — if it doesn't, you can say it yourself.
- **What to check:** open `.specify/memory/constitution.md` afterward. Does it actually match how you want to work? These rules will block or reshape later steps, so fix anything wrong now.

**OpenSpec — project context:** there is no separate command. Tell the agent what the project is and your principles; it writes them into `openspec/config.yaml`: `context:` (what the app is, for whom, the tech stack if you already know it, your principles) and, if needed, `rules:` (extra requirements for a specific document, e.g. "every proposal lists how to check it by hand").

- **Living spec is built in:** `openspec/specs/` always describes how the app works *now*. Each finished feature updates it (Step 13 of Part 3), so you don't need to agree on this separately.
- **What to check:** open `openspec/config.yaml`. Does the context describe your project correctly? It's included in every document OpenSpec writes. Note: these are guidelines for the agent, not strict checks — OpenSpec won't block a step that breaks them, so you're the one who watches for that.

---

**Now the per-feature loop starts.** Spec-Kit → go to Part 2. OpenSpec → skip Part 2 and go to Part 3.

---

## Part 2 — The Per-Feature Loop (Spec-Kit)

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

## Part 3 — The Per-Feature Loop (OpenSpec)

**Only if you chose OpenSpec in Step 4.** This replaces Part 2. One pass through Steps 8–13 below builds one feature (OpenSpec calls it a "change"). When you want the next feature, start again at Step 8.

**Command names depend on your agent.** Below they're written the Claude Code way (`/opsx:propose`). In opencode it's `/opsx-propose`, in Codex `$openspec-propose` — `openspec init` printed the right form for you, and `/start-guide` uses it automatically.

**Rule of thumb: one feature = one user-visible action** — the same as in Part 2. One change folder per action; if your idea is several things a user could do separately, make several changes.

### Step 8: Grill Me (optional but recommended for your first few features)

**Description:** `/grill-me` interviews you about the feature idea, one question at a time, until it's precise enough to propose. Exactly as in Part 2.

- Keep answers about *what* the feature does. How it's built goes into `design.md`, which OpenSpec writes in Step 10.

---

### Step 9 (optional): Explore

**Description:** `/opsx:explore` is a thinking partner: it reads your code, compares options, and answers questions — without writing any code or files.

- **Use it when:** you're changing an existing app and don't know how the relevant part works now, or you're torn between two ways of doing something.
- Skip it when the idea is already clear after Step 8.

---

### Step 10: Propose

**Description:** `/opsx:propose <your feature in one or two sentences>` creates the folder `openspec/changes/<change-name>/` with everything needed before building:

- `proposal.md` — why this change and what it changes;
- `specs/` — the spec changes: which requirements are added, changed, or removed, each with concrete scenarios ("given… when… then…");
- `design.md` — how it will be built (the tech part);
- `tasks.md` — the checklist of work.

- **What to check:**
  - `proposal.md`: is this what you asked for — nothing invented, nothing missing? Is it one user-visible action?
  - `specs/`: can you read each scenario and say "yes, that's exactly how it should behave"? Nothing vague like "works fast"?
  - `design.md`: is it reasonably simple for something this small? Does it agree with your project context (Step 7)?
  - `tasks.md`: does the number of tasks feel proportional to the feature?

---

### Step 11: Adjust Until It's Right

**Description:** Fix what you didn't like in Step 10 before anything gets built. This step usually takes a couple of rounds — that's normal.

- Tell the agent in plain words what to change ("the photo size limit should be 10 MB, not 5"). It edits the right file; `/opsx:update` then brings the other documents of the change in line with the edit.
- Before moving on, the agent runs `openspec validate <change-name>` — a **read-only** check that the documents are structured correctly. It doesn't judge whether they're *what you want* — that's your job.
- Need to add one task without rewriting the list? Use `/create-new-task`.

---

### Step 12: Apply

**Description:** `/opsx:apply` works through `tasks.md` one task at a time, writes the code, and ticks each task off.

- **What to check:** this is the step where you actually try the feature. Run the app, do the thing the feature describes, and confirm it behaves the way the scenarios in `specs/` said it should.
- **Found a problem?** Say what's wrong. If it's a bug, the agent fixes it. If the *plan itself* was wrong, go back to Step 11 (update the documents), then `/opsx:apply` again — the documents must stay true.

---

### Step 13: Archive

**Description:** `/opsx:archive` finishes the feature: it merges the spec changes into the permanent `openspec/specs/` and moves the change folder to `openspec/changes/archive/<date>-<change-name>/`.

- **Only archive when** every task in `tasks.md` is ticked and you've tried the feature yourself. Archive warns you if something is unfinished — don't archive past the warning.
- **What to check:** open `openspec/specs/` — the new behavior should now be described there. This folder is the up-to-date description of your whole app.

---

## What Happens Next

You've finished one feature. To build another, **go back to Step 8** of your part (Part 2 for spec-kit, Part 3 for OpenSpec) with the next idea. The project rules (Step 7) and the setup (Steps 1–6) don't repeat for this project — everything else does, once per feature, for the life of the project.

If you ever lose track of where you are, run `/where-am-i` instead of guessing.

---

## Frequently Asked Questions

**Q: Do I need to know how to code?**
A: You won't type much code yourself — but you will read and judge every generated document (`spec.md`, `plan.md`, `tasks.md`, or OpenSpec's `proposal.md`, `specs/`, `design.md`, `tasks.md`) and decide whether it's right before the next step builds on it. SDD moves the work from *writing code* to *writing precise requirements and reviewing results*; it doesn't remove the work. Skipping the review steps is how you end up with something that "works" but isn't what you wanted.

**Q: Spec-Kit or OpenSpec — which one should I pick?**
A: See Step 4. Short version: spec-kit for a new app and for learning, with more checks and more steps; OpenSpec for changing an existing app and for many small changes, faster but with fewer checks.

**Q: Can I switch toolkits in the middle of a project?**
A: Not easily — they keep their documents in different formats and folders, so one project uses one toolkit. Your next project can use the other: run `/new-project` and pick it (install it first with Steps 4–5).

**Q: Can I customize the generated code?**
A: Yes — both toolkits produce a real codebase you can edit like any other.

**Q: What if I get stuck?**
A: Run `/where-am-i` to get your bearings, or `/explain-me` to have the agent explain the part of this specific project you're confused about, grounded in your actual files.

**Q: How long does a first small feature take?**
A: Expect roughly 1–3 hours for a genuinely small, single-action feature with spec-kit, somewhat less with OpenSpec — most of it reading and deciding, not waiting. A whole first app is many features, so budget accordingly — don't expect "app in an afternoon."

**Q: How do I start a second project?**
A: Go back to the speckit-for-my-dad folder and run `/new-project` again (Step 6). Steps 1–3 don't repeat; Steps 4–5 only if you want the toolkit you haven't installed yet.

**Q: How do I get a newer version of the guide and skills into my project?**
A: In the speckit-for-my-dad folder, run `git pull`, then `/new-project ~/projects/my-app` (your project's path). It updates only the guide, the skills, and the rules block in `AGENTS.md` — your code, specs, and language setting stay as they are. If you edited your copy of the guide, it asks before replacing it.

**Q: Do I have to use Claude Code?**
A: No — this guide and its skills work with Claude Code, Codex CLI, and opencode, and should work with any agent that supports the shared "Agent Skills" format. Command names look slightly different per agent (`speckit-specify` vs. `/speckit.specify`; `/opsx:propose` vs. `/opsx-propose` vs. `$openspec-propose`).

---

## Notes

- Keep the "Language" line in `AGENTS.md` current if you switch languages — each project has its own.
- Don't edit the skills or this guide inside a project folder: updates overwrite them. Change them in the speckit-for-my-dad folder, then update the project.
- Review every generated document and the code itself — don't rubber-stamp any step.
- Use version control (git) — spec-kit already makes a branch per feature; with OpenSpec, commit after each finished feature. Commit your own edits too.
- Update your toolkit occasionally: spec-kit — `specify self upgrade`; OpenSpec — `npm install -g @fission-ai/openspec@latest`, then `openspec update` in each project.

---

**Ready to get started?** Type `/start-guide` in your agent chat now!
