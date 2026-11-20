#!/usr/bin/env python3
"""Build the Chinese translation's full-book PDF from manuscripts/*.md via Pandoc + Typst.

Usage:
    python book/build_pdf.py

Requires `pandoc` and `typst` on PATH (both are pinned in this repo's mise.toml).
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPTS = ROOT / "manuscripts"
BOOK_DIR = ROOT / "book"
BUILD_DIR = BOOK_DIR / "build"

# Reading order for the compiled book.
CHAPTER_ORDER = [
    "00-front-matter.md",
    "ch01.md", "ch02.md", "ch03.md", "ch04.md", "ch05.md",
    "ch06.md", "ch07.md", "ch08.md", "ch09.md", "ch10.md",
    "glossary.md", "notes.md", "epilogue.md",
]

TITLE_PAGE = """
#align(center)[
  #v(4cm)
  #text(size: 28pt, weight: "bold")[Solving the Bottom Turtle]

  #v(0.4cm)
  #text(size: 16pt)[SPIFFE/SPIRE：构建异构基础设施的统一身份信任（中文版）]

  #v(2cm)
  #text(size: 12pt)[原著：SPIFFE/SPIRE Book Sprint 作者团队（CC BY 4.0）]

  #text(size: 12pt)[中文翻译：开源社区贡献者]
]
#pagebreak()
"""


def md_to_typst(md_path: Path) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "typst", str(md_path)],
        capture_output=True, text=True, encoding="utf-8", check=True,
    )
    return result.stdout


def main() -> int:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    preamble = (BOOK_DIR / "preamble.typ").read_text(encoding="utf-8")

    parts = [preamble, TITLE_PAGE]
    for name in CHAPTER_ORDER:
        md_path = MANUSCRIPTS / name
        if not md_path.exists():
            print(f"warning: missing {md_path}, skipping", file=sys.stderr)
            continue
        parts.append(md_to_typst(md_path))

    combined_typ = BOOK_DIR / "book.typ"
    combined_typ.write_text("\n\n".join(parts), encoding="utf-8")

    out_pdf = BUILD_DIR / "SPIFFE-SPIRE-Book-ZH.pdf"
    subprocess.run(
        ["typst", "compile", "--root", str(ROOT), str(combined_typ), str(out_pdf)],
        check=True,
    )
    print(f"Built {out_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
