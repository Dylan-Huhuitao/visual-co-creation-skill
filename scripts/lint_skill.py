#!/usr/bin/env python3
"""Static repository integrity check, NOT an image-quality or tool-call behavior test.

Usage: python3 scripts/lint_skill.py .
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = (
    "SKILL.md", "README.md", "CHANGELOG.md",
    "references/visual-analysis.md", "references/creative-discovery.md",
    "references/prompt-engineering.md", "references/iteration-and-evaluation.md",
    "examples/two-entry-routes.md",
    "evaluations/evaluation-cases.md", "evaluations/run-log-template.md",
)
VERSION = "0.3.0"


def main(root: Path) -> int:
    errors: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing: {name}")

    if errors:
        print("\n".join("ERROR: " + e for e in errors))
        return 1

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    evaluation = (root / "evaluations/evaluation-cases.md").read_text(encoding="utf-8")

    if not skill.startswith("---\n"):
        errors.append("SKILL.md must begin with YAML frontmatter")
    else:
        closing = skill.find("\n---\n", 4)
        if closing < 0:
            errors.append("SKILL.md frontmatter is not closed")
        else:
            front = skill[4:closing]
            for field in (
                r"(?m)^name:\s*visual-co-creation-skill\s*$",
                r"(?m)^description:\s*.+$",
                r"(?m)^\s*version:\s*[\"']?0\.3\.0[\"']?\s*$",
                r"(?m)^\s*status:\s*[\"']?experimental[\"']?\s*$",
            ):
                if not re.search(field, front):
                    errors.append(f"Missing/mismatched frontmatter field: {field}")

    if f"v{VERSION}" not in readme.lower():
        errors.append("README does not identify v0.3.0")
    if f"[{VERSION}]" not in changelog:
        errors.append("CHANGELOG lacks 0.3.0 entry")

    ids = [int(x) for x in re.findall(r"(?m)^### E(\d{2})\s+[—-]", evaluation)]
    if ids != list(range(1, 26)):
        errors.append(f"Expected unique ordered E01–E25, got {ids}")

    # Inspect relative Markdown links in every maintained Markdown file.
    for file in root.rglob("*.md"):
        if ".git" in file.parts:
            continue
        content = file.read_text(encoding="utf-8")
        for link in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)", content):
            destination = link.split("#", 1)[0].strip().strip("<>")
            if not destination or re.match(r"^[a-z][a-z0-9+.-]*:", destination, re.I):
                continue
            if not (file.parent / destination).exists():
                errors.append(f"Broken local link: {file.relative_to(root)} -> {destination}")

    # Personal authorization phrases are session configuration, not public policy.
    if "Wisteria Black Hole" in skill:
        errors.append("Public SKILL.md hardcodes a private-user trigger")

    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS: required files, frontmatter/version, local links, and E01–E25 IDs")
    print("NOTE: no runtime authorization, image rendering, or artistic improvement was tested.")
    return 0


if __name__ == "__main__":
    base = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    raise SystemExit(main(base))
