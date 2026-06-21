# -*- coding: utf-8 -*-
import zipfile
from pathlib import Path

SKILL = Path(r"C:\클로드실습(김영은)\skills\overseas-steel-analysis")
OUT = Path(r"C:\클로드실습(김영은)\skills") / (SKILL.name + ".skill")

EXCLUDE_PARTS = {"__pycache__", ".git", ".DS_Store", "node_modules"}
EXCLUDE_SUFFIX = {".pyc", ".pyo"}

def should_exclude(p: Path) -> bool:
    if any(part in EXCLUDE_PARTS for part in p.parts):
        return True
    if p.suffix in EXCLUDE_SUFFIX:
        return True
    return False

count = 0
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for f in SKILL.rglob("*"):
        if not f.is_file():
            continue
        arc = f.relative_to(SKILL.parent)
        if should_exclude(arc):
            print("  skip:", arc)
            continue
        z.write(f, str(arc))
        print("  add :", arc)
        count += 1
print(f"\nPackaged {count} files -> {OUT}")
print("size:", OUT.stat().st_size, "bytes")
