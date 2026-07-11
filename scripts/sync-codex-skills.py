#!/usr/bin/env python3
"""Generate Codex skill packages from canonical workflow Markdown files."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGET = ROOT / "codex-skills"


def description(name, body):
    title = body.splitlines()[0].lstrip("# ").strip()
    return f"Use for {title.lower()} of Indian listed equities with point-in-time, source-backed evidence. Trigger when the user asks to run {name} or requests the corresponding India public-equity workflow."


def main():
    TARGET.mkdir(exist_ok=True)
    for source in sorted(SOURCE.glob("*.md")):
        name = source.stem
        if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
            raise SystemExit(f"invalid skill name: {name}")
        body = source.read_text(encoding="utf-8")
        package = TARGET / name
        agents = package / "agents"
        agents.mkdir(parents=True, exist_ok=True)
        skill = f"---\nname: {name}\ndescription: {description(name, body)}\n---\n\n{body}\n"
        (package / "SKILL.md").write_text(skill, encoding="utf-8")
        title = body.splitlines()[0].lstrip("# ").strip()
        openai_yaml = (
            "interface:\n"
            f"  display_name: \"{title}\"\n"
            f"  short_description: \"India-focused, source-backed {title.lower()}\"\n"
            f"  default_prompt: \"Use {name} for an Indian listed company or universe, with an explicit as-of date.\"\n"
        )
        (agents / "openai.yaml").write_text(openai_yaml, encoding="utf-8")
        print(f"generated {name}")


if __name__ == "__main__":
    main()

