# 关于本书

本书是 *Solving the Bottom Turtle — A SPIFFE Way to Establish Trust in Your
Infrastructure via Universal Identity* 的中文翻译版。原书由 Daniel Feldman、Emily
Fox、Evan Gilman、Ian Haken、Frederick Kautz、Umair Khan、Max Lambrecht、Brandon
Lum、Agustín Martínez Fayó、Eli Nesterov、Andres Vega、Michael Wardrop 合著，首版
于 2020 年发布，由 SPIFFE/SPIRE 社区与 Hewlett Packard Enterprise（HPE）以 Book
Sprint 协作方式在两周内完成。

原书采用 [知识共享署名 4.0 国际许可协议（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/)
发布。本中文翻译版同样遵循该许可协议发布：你可以自由地分享、修改和再创作本书内容（包括商业用途），
前提是注明出处。

- 原书地址：<https://spiffe.io/book/>（PDF：<https://spiffe.io/pdf/Solving-the-bottom-turtle-SPIFFE-SPIRE-Book.pdf>）
- 原书版权：© 2020 原书作者（见上）
- 本翻译版由开源社区贡献者翻译整理，翻译过程中对原文的页眉页脚、分页等排版产物做了清理，
  并将原书中的图表转换为 Markdown 格式，但不会增删任何实质性内容。

## 本书简介

本书介绍了用于服务身份认证的 SPIFFE 标准，以及作为 SPIFFE 参考实现的 SPIRE 项目。这两个项目
为现代异构基础设施提供了统一的身份控制面，均为开源项目，隶属于云原生计算基金会（CNCF）。

随着应用架构不断演进以充分利用新型基础设施技术，安全模型也必须随之演进：软件已经从运行在一台
机器上的单体应用，发展为分布在公有云或私有数据中心成千上万台虚拟机上、彼此紧密关联的数十上百个
微服务。在这样的新型基础设施世界里，SPIFFE 与 SPIRE 能够帮助系统保持安全。

本书力图汇集 SPIFFE/SPIRE 领域顶尖专家的经验，帮助读者深入理解身份问题及其解决之道。借助这些
项目，开发者和运维人员可以使用新型基础设施技术构建软件，同时让安全团队摆脱昂贵且耗时的人工安全
流程。

访问控制、密钥管理与身份三者相互依赖：大规模管理密钥需要有效的访问控制；实施访问控制需要身份；
证明身份又需要持有某种密钥。保护一个密钥，往往需要另一种方式去保护另一个密钥，如此循环往复。

这不禁让人想起一个著名的轶事：一位女士打断了哲学家的演讲，告诉他世界是驮在一只乌龟的背上的。
当哲学家追问这只乌龟又站在什么上面时，她答道："下面全都是乌龟！"而找到最底层的那只乌龟——也就
是支撑其余一切安全机制的那个坚实基础——正是 SPIFFE 和 SPIRE 项目的目标。

本书封面上的角色"Zero 龟"，象征的正是那只最底层的乌龟：Zero 代表了数据中心与云环境中安全的基石，
值得信赖，并乐于支撑起其他所有的"乌龟"。SPIFFE 与 SPIRE 可以帮助你的组织找到属于自己的那只
"最底层的乌龟"。希望借助本书介绍的工具，你也能为自己的 Zero 龟找到归宿。
