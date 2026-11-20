# Solving the Bottom Turtle（中文版）

*SPIFFE/SPIRE：构建异构基础设施的统一身份信任*

本仓库是 SPIFFE 官方书籍 [*Solving the Bottom Turtle — A SPIFFE Way to Establish
Trust in Your Infrastructure via Universal Identity*](https://spiffe.io/book/)
（[原书 PDF](https://spiffe.io/pdf/Solving-the-bottom-turtle-SPIFFE-SPIRE-Book.pdf)）
的中文社区翻译版，提供 PDF、EPUB 与在线阅读网站三种形式。

原书版权归 Daniel Feldman、Emily Fox、Evan Gilman、Ian Haken、Frederick Kautz、
Umair Khan、Max Lambrecht、Brandon Lum、Agustín Martínez Fayó、Eli Nesterov、
Andres Vega、Michael Wardrop 所有，采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
许可发布；本中文翻译版同样以 CC BY 4.0 发布。详见 [`manuscripts/00-front-matter.md`](manuscripts/00-front-matter.md)。

## 下载与阅读

> 💡 [在线阅读](https://henryzhang-zhy.github.io/spiffe-spire-book/) ·
> [下载 PDF](https://github.com/HenryZhang-ZHY/spiffe-spire-book/releases/latest/download/SPIFFE-SPIRE-Book-ZH.pdf) ·
> [下载 EPUB](https://github.com/HenryZhang-ZHY/spiffe-spire-book/releases/latest/download/SPIFFE-SPIRE-Book-ZH.epub) ·
> [英文原书官网](https://spiffe.io/book/) ·
> [英文原书 PDF](https://spiffe.io/pdf/Solving-the-bottom-turtle-SPIFFE-SPIRE-Book.pdf)

PDF / EPUB 由每次推送到 `main` 分支后的 GitHub Actions 自动构建并发布到
[Releases](https://github.com/HenryZhang-ZHY/spiffe-spire-book/releases/latest)，
上面的下载链接始终指向最新构建。

## 仓库结构

| 目录 | 内容 |
| --- | --- |
| `manuscripts/` | 中文译文（唯一正文来源，Markdown），PDF/EPUB/网站均由此构建 |
| `assets/figures/` | 从原书裁剪出的架构图/示意图（PNG） |
| `book/` | PDF（Pandoc + Typst）与 EPUB（Pandoc）构建脚本与排版模板 |
| `site/` | 在线阅读网站（mdBook），`site/src` 由 `scripts/build_site.py` 自动生成，不要手改 |
| `scripts/` | 构建脚本与翻译风格/术语对照指南 |
| `.github/workflows/` | CI：构建网站、PDF、EPUB，并发布 Release 与部署 GitHub Pages |

## 本地构建

本仓库使用 [mise](https://mise.jdx.dev/) 管理工具链（Python、Pandoc、Typst、mdBook），见 `mise.toml`。

```bash
mise install

# 生成网站源并本地预览
python scripts/build_site.py
mdbook serve site    # http://localhost:3000

# 构建 PDF（Pandoc + Typst）
python book/build_pdf.py

# 构建 EPUB（Pandoc）
python book/build_epub.py
```

## 参与翻译 / 校对

正文的唯一来源是 `manuscripts/` 下的 Markdown 文件，修改译文请直接改这里；修改后重新运行
`scripts/build_site.py`、`book/build_pdf.py`、`book/build_epub.py` 即可验证效果。翻译术语与风格
请遵循 [`scripts/translation-style-guide.md`](scripts/translation-style-guide.md)。

## 许可

- 本仓库的构建脚本、排版模板等工具代码采用 [MIT License](LICENSE)。
- 原书正文、配图及本书的中文翻译文本采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
