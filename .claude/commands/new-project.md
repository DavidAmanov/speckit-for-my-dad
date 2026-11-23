---
name: new-project
description: Create a new spec-kit or OpenSpec project in its own folder and install this repo's skills, guide, and rules into it — or update them in a project created earlier. Run only from the speckit-for-my-dad folder. Use when the user runs /new-project, wants to start a new project, or wants to update the skills or guide in an existing project.
---

Create the user's project in its **own folder** (never inside this repo) and copy everything they need into it, so from then on they work only in that folder: skills, `guide-for-dad.md`, and the rules block of `AGENTS.md`.

The project uses one of two toolkits: **spec-kit** (`specify init`, creates `.specify/`) or **OpenSpec** (`openspec init`, creates `openspec/`).

The same skill updates an existing project: if the target folder already has `.specify/` or `openspec/`, skip init and just (re)install our files.

Speak in the language set in `AGENTS.md` → Language. Show each command before running it, and stop on the first error — explain it, don't skip it.

## 1. Check where you are

- This skill must run from the speckit-for-my-dad folder: it needs `.agents/skills/new-project/SKILL.md` and `guide-for-dad.md` next to it. If they aren't there, tell the user to open the agent in the speckit-for-my-dad folder and run `/new-project` again, then stop.
- Remember this folder's absolute path — it's the **source**.

## 2. Pick the target folder

- If the user gave a path, use it. Otherwise ask for a project name, and suggest `~/projects/<name>` (Windows: `%USERPROFILE%\projects\<name>`) as the location.
- Resolve it to an absolute path — the **target**.
- The target must **not** be inside the source folder. If it is, say why (a project inside this repo mixes two git histories) and ask for another location.
- Decide the mode:
  - target has `.specify/` or `openspec/` → **update** mode, go to step 4
  - target doesn't exist, or exists and is empty → **create** mode, go to step 2b
  - target exists, isn't empty, and has neither → ask the user what's in there before touching it. Only continue with create mode (init right in that folder) if they confirm. An existing app is a normal case for OpenSpec.

## 2b. Pick the toolkit (create mode only)

If `/start-guide` or the user already said which toolkit, use it. Otherwise ask them to choose **spec-kit** or **OpenSpec**, showing under each option the short "Best for" and "Downside" from Step 4 of `guide-for-dad.md`, in the user's language. Don't choose for them.

## 3. Create the project (create mode only)

Work out which agent you are running as (Claude Code, Codex CLI, opencode, or other). If unclear, ask. Then follow **3a** for spec-kit or **3b** for OpenSpec.

### 3a. spec-kit

1. Check that `specify` is installed (`specify --version`). If not, tell the user to finish the install steps of `guide-for-dad.md` first (`/start-guide` does them), and stop.
2. Run `specify init --help` and read the current flag names. spec-kit changes its flags between versions — don't guess them. You need the flag that selects the coding agent and the flag for the script type.
3. Run init from the **parent** folder of the target, passing the agent and script type as flags. The interactive pickers don't work when you run the command yourself. Script type: `sh` on macOS/Linux, `ps` on Windows. Example shape (check the real flag names from `--help`). For an existing non-empty folder the user confirmed, run it inside the target with `--here` instead:

   ```bash
   mkdir -p ~/projects && cd ~/projects && specify init <name> --ai claude --script sh
   ```

4. Check that the target now has `.specify/`. If not, show the output and stop.

### 3b. OpenSpec

1. Check that `openspec` is installed (`openspec --version`). If not, tell the user to finish the install steps of `guide-for-dad.md` first (`/start-guide` does them), and stop.
2. Run `openspec init --help` and read the current flags and tool IDs — don't guess them. You need the flag that selects tools non-interactively (currently `--tools <ids>`) and, if present, the artifact-language flag (currently `--language`).
3. Create the target folder if it doesn't exist. If it has no `.git/`, run `git init` in it (OpenSpec doesn't do this itself).
4. Run init **inside** the target, passing your agent's tool ID and, if the flag exists, the language from `AGENTS.md` → Language (as a language name, e.g. `Russian`). Example shape:

   ```bash
   mkdir -p ~/projects/<name> && cd ~/projects/<name> && git init && openspec init --tools claude --language English
   ```

5. Check that the target now has `openspec/`. If not, show the output and stop. Note the command form `openspec init` printed for this agent (e.g. `/opsx:propose`) — tell it to the user in step 5.

## 4. Install or update our files

Take the source commit first: `git -C <source> rev-parse --short HEAD`. If `git -C <source> status --porcelain` isn't empty, add `-dirty` to it.

If `<target>/.agents/speckit-for-my-dad.version` exists, read it first — you need `skills=` and `guide_hashes=` from it below.

### 4a. Skills

- Our skills are every folder in `<source>/.agents/skills/` **except `new-project`**, which only makes sense in the source folder.
- Copy each of them, as real files (not symlinks), to **both** `<target>/.agents/skills/<name>/` and `<target>/.claude/skills/<name>/`. Before copying, delete the old copy of that one skill folder. Nothing else in those folders — spec-kit keeps its own `speckit-*` skills there, OpenSpec its `openspec-*` — may be deleted.
- Update mode: if a skill is listed in the old version file's `skills=` but no longer exists in the source, delete it from both target folders and tell the user.

### 4b. Guide

- Copy `<source>/guide-for-dad.md` and every `<source>/guide-for-dad-*.md` translation into the target root.
- Update mode: before you overwrite a guide file, compute its SHA-256 (`shasum -a 256`, or `Get-FileHash` on Windows) and compare it with the hash stored in the old version file. If they differ — or the file has no stored hash, e.g. a translation `choose-language` made inside the project — the user's copy may have changes: ask them, and if they agree, save their copy as `guide-for-dad.old.md` (or `guide-for-dad-<code>.old.md`) before overwriting.
- Guide files that exist only in the target (no source counterpart) are left alone.

### 4c. AGENTS.md

The source `AGENTS.md` holds a block between `<!-- speckit-for-my-dad:start -->` and `<!-- speckit-for-my-dad:end -->` (markers included) — that is what gets copied. Nothing outside the markers is copied.

- `<target>/AGENTS.md` doesn't exist → create it with only the block.
- It exists but has no markers → insert the block at the very top and keep the rest. spec-kit or OpenSpec may have written its own content there — keep it.
- It already has markers → replace everything between them (markers included) with the new block. **Keep the project's language:** copy the `Current communication language: **...**` line from the old block into the new one.

### 4d. CLAUDE.md

- `<target>/CLAUDE.md` doesn't exist → create it with a single line: `@AGENTS.md`
- It's a symlink to `AGENTS.md`, or already contains the line `@AGENTS.md` → leave it alone.
- Otherwise → add `@AGENTS.md` as the first line and keep the rest.

Never make `CLAUDE.md` a symlink: on Windows git turns symlinks into plain text files.

### 4e. License and version file

- Copy `<source>/LICENSE` to `<target>/.agents/LICENSE-speckit-for-my-dad`.
- Write `<target>/.agents/speckit-for-my-dad.version`:

  ```
  commit=<source commit>
  source=<absolute source path>
  installed=<today, YYYY-MM-DD>
  skills=<comma-separated skill names you copied>
  guide_hashes=<file>:<sha256>,<file>:<sha256>
  ```

## 5. Finish

1. Show `git -C <target> status --short` and briefly explain what was added. Offer to commit it in the target with a message like `Add speckit-for-my-dad skills and guide`. Commit only if the user agrees.
2. Tell the user in plain words:
   - the project lives in `<target>`, and all work on it happens there from now on;
   - which toolkit the project uses, and (OpenSpec) how its commands look in their agent;
   - close this agent, open it in `<target>` (show the exact `cd <target>` command and how to start their agent), and type `/start-guide` — it picks up from the project rules (Step 7);
   - to update the skills and guide later: in the speckit-for-my-dad folder, run `git pull`, then `/new-project <target>`.

## Notes

- Never run `specify init` or `openspec init` inside the source folder or with `--here` in it.
- Don't edit the user's app code, `specs/`, `.specify/`, or `openspec/` — this skill only touches the files listed in step 4.
- Copies of our skills in a project are overwritten on update. If the user wants to change a skill, it's done in the speckit-for-my-dad folder, then installed with `/new-project <target>`.
