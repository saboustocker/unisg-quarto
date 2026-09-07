"""Copy _extensions/ from the repository root into every starter project."""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_extensions"
TARGETS = {
    "project-template": ["unisg", "unisg-book"],
    "book-template": ["unisg", "unisg-book"],
    "slides-template": ["unisg"],
}

for name, extensions in TARGETS.items():
    dest = ROOT / name / "_extensions"
    shutil.rmtree(dest, ignore_errors=True)
    for ext in extensions:
        shutil.copytree(SOURCE / ext, dest / ext)
    print(f"{name}: {', '.join(extensions)}")
