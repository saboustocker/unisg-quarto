"""Copy _extensions/ from the repository root into every starter project."""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_extensions"
TARGETS = {
    "project-template": ["unisg", "unisg-book", "unisg-slides"],
    "book-template": ["unisg-book", "unisg-slides"],
    "slides-template": ["unisg-slides"],
}

for name, extensions in TARGETS.items():
    dest = ROOT / name / "_extensions"
    shutil.rmtree(dest, ignore_errors=True)
    for ext in extensions:
        shutil.copytree(SOURCE / ext, dest / ext)
    print(f"{name}: {', '.join(extensions)}")
