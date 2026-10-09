---
name: connect-playwright
description: Connect Playwright MCP to this project. Reads mcp.example, finds the npx path on this machine, writes the real (git-ignored) MCP config for the current agent environment, and verifies Playwright is installed. Use when the user runs /connect-playwright, wants to use Playwright in the agent, or asks why browser tools are missing.
---

Connect Playwright MCP to this project so the agent can open, click, and screenshot real web pages.

Speak in the language set in `AGENTS.md` → Language.

## 1. Detect the agent environment

Work out which agent you are running as:

| Agent | MCP config file | Config key |
|---|---|---|
| Claude Code | `.mcp.json` in the project root | `mcpServers` |
| Codex CLI | `codex.json` in the project root | `mcpServers` |
| opencode | `.opencode.json` in the project root | `mcpServers` |
| Other / unknown | `.mcp.json` in the project root | `mcpServers` (best guess) |

If you cannot determine the agent, tell the user which one you think this is and ask them to confirm.

## 2. Check for mcp.example

Look for `mcp.example` in the project root (same folder as `AGENTS.md`). If it is missing, stop and tell the user: the file should have come with the repo — run `git pull` in the speckit-for-my-dad folder and then `/new-project` to reinstall.

## 3. Find npx

Run: `which npx`

- If it returns a path → use that path as the `command` value.
- If it fails (not found in PATH) → try these common locations in order and use the first that exists:
  - `/usr/local/bin/npx`
  - `/usr/bin/npx`
  - `~/.nvm/versions/node/*/bin/npx` (expand glob, pick highest version)
  - `~/.volta/bin/npx`
  - `C:\Program Files\nodejs\npx.cmd` (Windows)
- If none found → tell the user: Node.js is not installed or not in PATH. Point them to https://nodejs.org and ask them to install it, then re-run `/connect-playwright`.

Show the user which path you found.

## 4. Check Playwright MCP is installable

Run: `npx @playwright/mcp@latest --version` (use the full npx path from step 3).

- If it prints a version → good, continue.
- If it fails with a network error → warn the user but continue anyway (the package will download on first use).
- If it fails for another reason → show the error and stop. The most common cause is an outdated Node.js version; tell the user to upgrade to Node 18+.

## 5. Write the config file

Determine the target config file from step 1. If it already exists:
- Read it.
- If it already has a `playwright` entry under `mcpServers`, ask the user: "Playwright is already configured here — overwrite it?" Stop if they say no.
- Merge the playwright entry in: keep every other key in the file, just add/replace `mcpServers.playwright`.

If it does not exist, create it from `mcp.example`:
- Copy the JSON from `mcp.example`.
- Replace the `"command"` value with the full npx path from step 3.
- Remove the `"_note"` key — it is only for humans reading the example.

Write the result. Show the user the final JSON you wrote.

## 6. Ensure config is git-ignored

Check `.gitignore` in the project root. If the config filename (e.g. `.mcp.json`) is not already listed there, append it. Show the user the line you added.

## 7. Reload / restart the MCP server

Tell the user what to do next depending on the agent:

- **Claude Code**: type `/mcp` to see the new server, or restart the session (close and reopen the terminal / IDE tab). The server starts automatically on next launch.
- **Codex CLI**: restart Codex with `codex` — it reads `codex.json` on startup.
- **opencode**: run `/mcp reload` or restart opencode.
- **Other**: restart the agent.

## 8. Verify (optional but recommended)

After the user restarts, ask them to run a quick smoke test: tell them to say "take a screenshot of https://example.com" and see if the agent opens a browser. If it errors, show the raw error and diagnose:

- `spawn npx ENOENT` → the npx path in the config is wrong; go back to step 3.
- `Error: browserType.launch: Executable doesn't exist` → Playwright browsers aren't installed. Run: `npx playwright install --with-deps chromium` (use the full npx path). Then ask the user to retry.
- Any other error → show it and ask the user to paste it here.
