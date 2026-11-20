#!/usr/bin/env python3
"""Build the Chinese translation's EPUB from manuscripts/*.md via Pandoc.

Usage:
    python book/build_epub.py
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPTS = ROOT / "manuscripts"
BOOK_DIR = ROOT / "book"
BUILD_DIR = BOOK_DIR / "build"

CHAPTER_ORDER = [
    "00-front-matter.md",
    "ch01.md", "ch02.md", "ch03.md", "ch04.md", "ch05.md",
    "ch06.md", "ch07.md", "ch08.md", "ch09.md", "ch10.md",
    "glossary.md", "notes.md", "epilogue.md",
]


def main() -> int:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    out_epub = BUILD_DIR / "SPIFFE-SPIRE-Book-ZH.epub"

    inputs = [str(MANUSCRIPTS / name) for name in CHAPTER_ORDER if (MANUSCRIPTS / name).exists()]

    cmd = [
        "pandoc",
        *inputs,
        "-f", "markdown",
        "-t", "epub3",
        "-o", str(out_epub),
        "--metadata", "title=Solving the Bottom Turtle（中文版）：SPIFFE/SPIRE 身份框架详解",
        "--metadata", "lang=zh-CN",
        "--metadata", "creator=SPIFFE/SPIRE Book Sprint 作者团队（原著，CC BY 4.0）；中文社区翻译",
        "--css", str(BOOK_DIR / "epub.css"),
        "--toc", "--toc-depth=2",
        "--resource-path", str(MANUSCRIPTS),
    ]
    subprocess.run(cmd, check=True)
    print(f"Built {out_epub}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
