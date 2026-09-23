#!/usr/bin/env python3
"""Install or update speckit-for-my-dad files in a project folder.

This is the deterministic half of the `new-project` skill: it copies the skills,
the guide, the rules block of AGENTS.md, the license, and writes the version
file. It never runs `specify init` or `openspec init`, never touches app code,
`specs/`, `.specify/`, or `openspec/`, and never decides anything a human should
decide.

Usage:
    install.py --target <path>                 # read-only: print the plan
    install.py --target <path> --apply         # do it
    install.py --target <path> --apply --guides backup|overwrite|keep

`--apply` stops with exit code 2 if a guide file in the target was edited after
it was installed, and `--guides` says what to do with those edits. Everything
else is unambiguous and needs no flag.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

MARK_START = "<!-- speckit-for-my-dad:start -->"
MARK_END = "<!-- speckit-for-my-dad:end -->"
LANGUAGE_PREFIX = "Current communication language:"
VERSION_REL = Path(".agents/speckit-for-my-dad.version")
LICENSE_REL = Path(".agents/LICENSE-speckit-for-my-dad")
SKILL_DIRS = (Path(".agents/skills"), Path(".claude/skills"))
# Only makes sense in the source repo, so it is never installed into a project.
SOURCE_ONLY_SKILLS = {"new-project"}

SOURCE = Path(__file__).resolve().parent


class Fail(Exception):
    """A condition the script refuses to guess its way past."""


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    out = subprocess.run(
        ["git", "-C", str(SOURCE), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return out.stdout.strip() if out.returncode == 0 else ""


def source_version() -> str:
    commit = git("rev-parse", "--short", "HEAD")
    if not commit:
        return "unknown"
    return f"{commit}-dirty" if git("status", "--porcelain") else commit


def read_version_file(target: Path) -> dict[str, str]:
    path = target / VERSION_REL
    if not path.is_file():
        return {}
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        key, sep, value = line.partition("=")
        if sep:
            values[key.strip()] = value.strip()
    return values


def stored_guide_hashes(version: dict[str, str]) -> dict[str, str]:
    raw = version.get("guide_hashes", "")
    hashes: dict[str, str] = {}
    for entry in raw.split(","):
        name, sep, digest = entry.partition(":")
        if sep and name.strip():
            hashes[name.strip()] = digest.strip()
    return hashes


def stored_skills(version: dict[str, str]) -> list[str]:
    return [s.strip() for s in version.get("skills", "").split(",") if s.strip()]


def source_skills() -> list[str]:
    root = SOURCE / ".agents" / "skills"
    if not root.is_dir():
        raise Fail(
            f"no skills found at {root} — run this script from a "
            "speckit-for-my-dad checkout"
        )
    names = sorted(
        p.name
        for p in root.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name not in SOURCE_ONLY_SKILLS
    )
    if not names:
        raise Fail(f"{root} has no skills to install")
    return names


def source_guides() -> list[Path]:
    main = SOURCE / "guide-for-dad.md"
    if not main.is_file():
        raise Fail(f"{main} is missing — is this a speckit-for-my-dad checkout?")
    translations = sorted(SOURCE.glob("guide-for-dad-*.md"))
    return [main, *translations]


def source_block() -> str:
    text = (SOURCE / "AGENTS.md").read_text(encoding="utf-8")
    start = text.find(MARK_START)
    end = text.find(MARK_END)
    if start == -1 or end == -1 or end < start:
        raise Fail("the source AGENTS.md has no speckit-for-my-dad:start/:end block")
    return text[start : end + len(MARK_END)]


def language_line(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith(LANGUAGE_PREFIX):
            return line
    return None


def with_language_of(block: str, old_text: str) -> str:
    """Carry the project's own language line into the new block."""
    old = language_line(old_text)
    new = language_line(block)
    if old and new and old != new:
        return block.replace(new, old, 1)
    return block


def rm(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def copy_tree(src: Path, dst: Path) -> None:
    rm(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    # symlinks=False: the source may use symlinks, a project gets real files.
    shutil.copytree(src, dst, symlinks=False)


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


# --------------------------------------------------------------------------- #
# the plan
# --------------------------------------------------------------------------- #


class Plan:
    def __init__(self) -> None:
        self.steps: list[tuple[str, object]] = []
        self.notes: list[str] = []
        self.modified_guides: list[str] = []

    def step(self, description: str, action) -> None:
        self.steps.append((description, action))

    def note(self, text: str) -> None:
        self.notes.append(text)


def check_target(target: Path) -> str:
    if not target.exists():
        raise Fail(
            f"{target} does not exist — create the project with `specify init` or "
            "`openspec init` first"
        )
    if not target.is_dir():
        raise Fail(f"{target} is not a folder")
    if target == SOURCE or SOURCE in target.parents:
        raise Fail(
            f"{target} is inside the speckit-for-my-dad folder ({SOURCE}). A project "
            "there would mix two git histories — pick a location outside it."
        )
    initialized = (target / ".specify").is_dir() or (target / "openspec").is_dir()
    return "update" if initialized else "create"


def plan_skills(target: Path, plan: Plan, version: dict[str, str]) -> list[str]:
    names = source_skills()
    for name in names:
        src = SOURCE / ".agents" / "skills" / name
        for skills_dir in SKILL_DIRS:
            dst = target / skills_dir / name
            verb = "replace" if dst.exists() or dst.is_symlink() else "install"
            plan.step(
                f"{verb} skill {name} at {dst.relative_to(target)}",
                lambda s=src, d=dst: copy_tree(s, d),
            )

    gone = [n for n in stored_skills(version) if n not in names]
    for name in gone:
        for skills_dir in SKILL_DIRS:
            dst = target / skills_dir / name
            if dst.exists() or dst.is_symlink():
                plan.step(
                    f"remove skill {name} (dropped upstream) "
                    f"from {dst.relative_to(target)}",
                    lambda d=dst: rm(d),
                )
        plan.note(f"skill `{name}` no longer exists upstream and is being removed")
    return names


def plan_guides(target: Path, plan: Plan, version: dict[str, str], guides: str | None):
    hashes = stored_guide_hashes(version)
    installed: dict[str, str] = {}

    for src in source_guides():
        name = src.name
        dst = target / name
        digest = sha256(src)
        installed[name] = digest

        if not dst.is_file():
            plan.step(f"copy {name}", lambda s=src, d=dst: copy_file(s, d))
            continue

        current = sha256(dst)
        if current == digest:
            plan.note(f"{name} is already up to date")
            continue

        untouched = name in hashes and hashes[name] == current
        if untouched:
            plan.step(f"update {name}", lambda s=src, d=dst: copy_file(s, d))
            continue

        # The user (or choose-language) changed this copy after it was installed.
        plan.modified_guides.append(name)
        if guides == "keep":
            plan.note(f"{name} was edited here — keeping your copy, not updating it")
            # Record no hash for it: the next update must ask again rather than
            # mistake these edits for a pristine install and overwrite them.
            installed.pop(name, None)
        elif guides == "overwrite":
            plan.step(
                f"overwrite {name}, discarding the edits made here",
                lambda s=src, d=dst: copy_file(s, d),
            )
        elif guides == "backup":
            backup = dst.with_suffix(".old.md")
            plan.step(
                f"save your edited {name} as {backup.name}, then update {name}",
                lambda s=src, d=dst, b=backup: (
                    shutil.copyfile(d, b),
                    copy_file(s, d),
                ),
            )
        else:
            plan.step(f"update {name} — needs --guides", lambda: None)

    return installed


def plan_agents_md(target: Path, plan: Plan) -> None:
    block = source_block()
    path = target / "AGENTS.md"

    if not path.is_file():
        plan.step(
            "create AGENTS.md with the speckit-for-my-dad rules block",
            lambda: path.write_text(block + "\n", encoding="utf-8"),
        )
        return

    text = path.read_text(encoding="utf-8")
    start = text.find(MARK_START)
    end = text.find(MARK_END)

    if start == -1 or end == -1 or end < start:
        # spec-kit or OpenSpec may have written its own content here — keep all of it.
        def prepend() -> None:
            path.write_text(f"{block}\n\n{text}", encoding="utf-8")

        plan.step(
            "insert the rules block at the top of AGENTS.md, keeping what is there",
            prepend,
        )
        return

    old_block = text[start : end + len(MARK_END)]
    new_block = with_language_of(block, old_block)
    if old_block == new_block:
        plan.note("the rules block in AGENTS.md is already up to date")
        return

    def replace() -> None:
        path.write_text(
            text[:start] + new_block + text[end + len(MARK_END) :], encoding="utf-8"
        )

    kept = language_line(old_block)
    plan.step("replace the rules block in AGENTS.md", replace)
    if kept:
        plan.note(f"keeping this project's language line: {kept}")


def plan_claude_md(target: Path, plan: Plan) -> None:
    path = target / "CLAUDE.md"
    pointer = "@AGENTS.md"

    if not path.exists() and not path.is_symlink():
        # Never a symlink: on Windows git turns symlinks into plain text files.
        plan.step(
            "create CLAUDE.md pointing at AGENTS.md",
            lambda: path.write_text(pointer + "\n", encoding="utf-8"),
        )
        return

    if path.is_symlink():
        plan.note("CLAUDE.md is a symlink to AGENTS.md — leaving it alone")
        return

    text = path.read_text(encoding="utf-8")
    if pointer in text.splitlines():
        plan.note("CLAUDE.md already points at AGENTS.md")
        return

    plan.step(
        "add the @AGENTS.md line at the top of CLAUDE.md, keeping the rest",
        lambda: path.write_text(f"{pointer}\n\n{text}", encoding="utf-8"),
    )


def plan_license_and_version(
    target: Path, plan: Plan, skills: list[str], guide_hashes: dict[str, str]
) -> None:
    license_src = SOURCE / "LICENSE"
    if license_src.is_file():
        plan.step(
            f"copy the license to {LICENSE_REL}",
            lambda: copy_file(license_src, target / LICENSE_REL),
        )

    commit = source_version()
    body = "\n".join(
        [
            f"commit={commit}",
            f"source={SOURCE}",
            f"installed={dt.date.today().isoformat()}",
            f"skills={','.join(skills)}",
            "guide_hashes="
            + ",".join(f"{n}:{h}" for n, h in sorted(guide_hashes.items())),
        ]
    )

    def write_version() -> None:
        path = target / VERSION_REL
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body + "\n", encoding="utf-8")

    plan.step(f"record version {commit} in {VERSION_REL}", write_version)


def build_plan(target: Path, guides: str | None) -> tuple[Plan, str]:
    mode = check_target(target)
    version = read_version_file(target)
    plan = Plan()
    skills = plan_skills(target, plan, version)
    guide_hashes = plan_guides(target, plan, version, guides)
    plan_agents_md(target, plan)
    plan_claude_md(target, plan)
    plan_license_and_version(target, plan, skills, guide_hashes)
    return plan, mode


# --------------------------------------------------------------------------- #
# entry point
# --------------------------------------------------------------------------- #


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Install or update speckit-for-my-dad files in a project folder."
    )
    parser.add_argument("--target", required=True, help="the project folder")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="carry out the plan (without this the script only prints it)",
    )
    parser.add_argument(
        "--guides",
        choices=("backup", "overwrite", "keep"),
        help="what to do with guide files that were edited in the target",
    )
    args = parser.parse_args(argv)

    target = Path(args.target).expanduser().resolve()

    try:
        plan, mode = build_plan(target, args.guides)
    except Fail as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"source: {SOURCE}  ({source_version()})")
    print(f"target: {target}  ({mode} mode)")
    print()

    if plan.modified_guides and not args.guides:
        print("These guide files were edited after they were installed here:")
        for name in plan.modified_guides:
            print(f"  - {name}")
        print()
        print("Ask the user, then re-run with one of:")
        print("  --guides backup     save their copy as *.old.md, then update")
        print("  --guides overwrite  discard their edits")
        print("  --guides keep       leave their copy as it is")
        return 2

    label = "Doing" if args.apply else "Would do"
    if plan.steps:
        print(f"{label}:")
        for description, _ in plan.steps:
            print(f"  - {description}")
    else:
        print("Nothing to do.")

    if plan.notes:
        print()
        print("Notes:")
        for note in plan.notes:
            print(f"  - {note}")

    if not args.apply:
        print()
        print("Read-only. Re-run with --apply to make these changes.")
        return 0

    print()
    for description, action in plan.steps:
        try:
            action()
        except OSError as exc:
            print(f"error: failed while it tried to {description}: {exc}", file=sys.stderr)
            return 1
    print(f"Done. {len(plan.steps)} change(s) applied in {target}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
