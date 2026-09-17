#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"

errors = []
skill_files = sorted(SKILLS.glob("*/SKILL.md"))
if not skill_files:
    errors.append("no SKILL.md files found")

for path in skill_files:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter")
        continue
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{path}: malformed YAML frontmatter")
        continue
    front = match.group(1)
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    expected = path.parent.name
    if not name:
        errors.append(f"{path}: missing lowercase name")
    elif name.group(1) != expected:
        errors.append(f"{path}: name {name.group(1)!r} != directory {expected!r}")
    if not desc or len(desc.group(1).strip()) < 40:
        errors.append(f"{path}: description is missing or too short")
    if "TODO" in text:
        errors.append(f"{path}: TODO placeholder remains")

if errors:
    print("SKILL VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"SKILL VALIDATION PASS: {len(skill_files)} skills")
