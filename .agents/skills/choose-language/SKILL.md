---
name: choose-language
description: Change the language used for talking to the user and for generated spec-kit documentation. Use when the user runs /choose-language or asks to switch languages.
---

Change the project's language setting and switch to it immediately.

## Steps

1. Show the supported languages with their native names:

   | Code | Language | Native name |
   |------|----------|-------------|
   | eng  | English  | English |
   | rus  | Russian  | Русский |
   | spa  | Spanish  | Español |
   | fra  | French   | Français |
   | deu  | German   | Deutsch |
   | ita  | Italian  | Italiano |
   | jpn  | Japanese | 日本語 |
   | zho  | Chinese (Simplified) | 中文 |

2. Ask the user to pick one (they can also just name a language not on the list — support it if you reasonably can).
3. Open `AGENTS.md` and edit the line `Current communication language: **...**` in the "Language" section to the new choice, keeping the same format.
4. From this point on in the conversation, speak to the user in the new language, and write any spec-kit artifacts you generate (`spec.md`, `plan.md`, `tasks.md`, etc.) in it too.
5. If `guide-for-dad.md` exists in a translated form for this language already (e.g. the user asks for it), use that file; otherwise offer to translate `guide-for-dad.md` into a new `guide-for-dad-{code}.md` and keep the English original untouched as the source of truth.
6. Confirm the change to the user in the new language.

## Notes

- `AGENTS.md` is the single source of truth for the language setting — every other skill in this project reads it from there. Do not create a separate language file.
- Existing files already written in the old language are not retroactively translated.
- Code comments stay in English unless the user asks otherwise.
