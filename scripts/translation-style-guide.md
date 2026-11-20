# 翻译风格与术语对照指南

本指南用于统一全书翻译的术语与行文风格，所有章节翻译必须遵循。

## 总体要求

- 目标读者：中文技术读者（安全/基础设施工程师），语体为正式but平实的技术书籍中文，避免生硬直译和机翻腔。
- 完整、准确地翻译原文内容，不得省略实质性信息，也不得添加原文没有的内容。
- 原文中的脚注/引用链接、代码、命令行示例、URL、文件路径保持原样不翻译。
- 专有名词、缩写首次出现可在括号中给出英文全称或简短说明，之后直接使用英文缩写。
- 表格统一转换为标准 Markdown 表格语法。
- 行文中出现的 `[[FIGURE:fig-x-y]]` 占位符，请替换为对应的 Markdown 图片引用：
  `![<对该图的简短中文说明>](../assets/figures/fig-x-y.png)`，图片下方另起一行给出斜体图注（翻译原书的
  Fig. x.y 图注文字）。
- 标题层级：章标题用 `#`，章内一级小节用 `##`，小节内部的小标题用 `###`，与原书的视觉层级保持一致（原书用大号
  字体 + 色块表示一级小节，中号加粗表示二级小节）。
- 不要保留原书的页码、页眉页脚文字。

## 术语对照表（必须统一使用）

| English | 中文译法 | 说明 |
| --- | --- | --- |
| SPIFFE | SPIFFE | 全称 Secure Production Identity Framework For Everyone，保留英文缩写 |
| SPIRE | SPIRE | 全称 SPIFFE Runtime Environment，保留英文缩写 |
| SVID | SVID | SPIFFE Verifiable Identity Document，保留英文缩写，首次出现可注明中文含义"SPIFFE 可验证身份文档" |
| trust domain | 信任域 | |
| workload | 工作负载 | |
| workload identity | 工作负载身份 | |
| attestation | 验证 | node attestation 译为"节点验证"，workload attestation 译为"工作负载验证" |
| attestor / attestation plugin | 验证器 / 验证插件 | |
| registration entry | 注册条目 | |
| trust bundle | 信任包 | |
| federation / federated | 联邦 / 联邦化 | |
| root of trust | 信任根 | |
| Workload API | Workload API | 保留英文，不翻译 |
| mTLS | mTLS（双向 TLS） | |
| secret zero | 第零号密钥问题（secret zero） | 首次出现保留英文术语并加括号说明 |
| zero trust | 零信任 | |
| perimeter security | 边界安全 | |
| identity document | 身份文档 | |
| certificate authority (CA) | 证书颁发机构（CA） | 之后用 CA |
| upstream CA | 上游 CA | |
| node | 节点 | |
| SPIRE Agent | SPIRE Agent | 组件专有名，不翻译 |
| SPIRE Server | SPIRE Server | 组件专有名，不翻译 |
| rotation | 轮换 | |
| bootstrap / bootstrapping | 引导 | |
| selector | 选择器 | |
| plugin | 插件 | |
| data store | 数据存储 | |
| high availability (HA) | 高可用（HA） | |
| service mesh | 服务网格 | |
| Envoy | Envoy | 保留英文 |
| OIDC | OIDC | 保留英文缩写 |
| JWT | JWT | 保留英文缩写 |
| PKI | PKI（公钥基础设施） | |
| X.509 | X.509 | |

如遇到本表未覆盖的术语，请选择业界通行的中文技术译法，并在该章内保持前后一致。
