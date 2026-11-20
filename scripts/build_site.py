#!/usr/bin/env python3
"""Generate the mdBook website source (site/src) from manuscripts/*.md.

manuscripts/ is the single source of truth. This script copies each chapter
into site/src, rewrites image paths to the site's asset layout, and
generates site/src/SUMMARY.md.

Usage:
    python scripts/build_site.py
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPTS = ROOT / "manuscripts"
ASSETS = ROOT / "assets"
SITE = ROOT / "site"
SRC = SITE / "src"

# (manuscript filename, display title for SUMMARY.md)
CHAPTERS = [
    ("00-front-matter.md", "关于本书"),
    ("ch01.md", "第 1 章 历史与行业背景"),
    ("ch02.md", "第 2 章 收益"),
    ("ch03.md", "第 3 章 基础概念"),
    ("ch04.md", "第 4 章 SPIFFE 与 SPIRE 简介"),
    ("ch05.md", "第 5 章 启动之前的准备"),
    ("ch06.md", "第 6 章 设计 SPIRE 部署方案"),
    ("ch07.md", "第 7 章 与 SPIFFE 和 SPIRE 集成"),
    ("ch08.md", "第 8 章 使用 SPIFFE 和 SPIRE"),
    ("ch09.md", "第 9 章 SPIFFE 与其他方案的比较"),
    ("ch10.md", "第 10 章 从业者视角"),
    ("glossary.md", "术语表"),
    ("notes.md", "注释与参考资料"),
    ("epilogue.md", "后记"),
]

IMG_PATH_RE = re.compile(r"\]\(\.\./assets/")


def main() -> None:
    if SRC.exists():
        shutil.rmtree(SRC)
    SRC.mkdir(parents=True)

    # Copy figures so they resolve relative to site/src/assets/.
    shutil.copytree(ASSETS, SRC / "assets")

    summary_lines = ["# Summary", ""]
    for filename, title in CHAPTERS:
        src_path = MANUSCRIPTS / filename
        if not src_path.exists():
            print(f"warning: missing {src_path}, skipping")
            continue
        text = src_path.read_text(encoding="utf-8")
        text = IMG_PATH_RE.sub("](assets/", text)
        (SRC / filename).write_text(text, encoding="utf-8")
        summary_lines.append(f"- [{title}]({filename})")

    (SRC / "SUMMARY.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print(f"Generated site/src with {len(summary_lines) - 2} chapters")


if __name__ == "__main__":
    main()
