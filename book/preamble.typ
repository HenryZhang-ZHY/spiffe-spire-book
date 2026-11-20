// 中文版排版模板（Typst）
// 字体优先级：优先使用思源宋体/黑体（CI 环境安装），本地 Windows 回退到系统自带的微软雅黑/宋体。

#set document(title: "Solving the Bottom Turtle 中文版：SPIFFE/SPIRE 身份框架详解", author: "SPIFFE/SPIRE 项目作者（原著）；社区翻译")

#set text(
  font: ("Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", "SimSun", "Microsoft YaHei"),
  size: 11pt,
  lang: "zh",
)

#set page(
  paper: "a4",
  margin: (x: 2.4cm, y: 2.6cm),
  numbering: "1",
)

#set heading(numbering: none)

#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  v(1.2cm)
  text(size: 22pt, weight: "bold")[#it.body]
  v(0.8cm)
}

#show heading.where(level: 2): it => {
  v(0.6cm)
  text(size: 15pt, weight: "bold")[#it.body]
  v(0.3cm)
}

#show heading.where(level: 3): it => {
  v(0.4cm)
  text(size: 12.5pt, weight: "bold")[#it.body]
  v(0.2cm)
}

#show raw: set text(font: ("Cascadia Code", "Consolas", "Courier New"))

#show figure: it => {
  align(center)[#it.body]
  v(0.2cm)
  align(center)[#text(size: 9.5pt, style: "italic")[#it.caption]]
  v(0.4cm)
}

#show link: underline
