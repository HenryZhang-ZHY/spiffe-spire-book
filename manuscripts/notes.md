# 注释与参考资料

## SPIFFE 的历史与动机

1. *Building Microservices*，O'Reilly Media, Inc.，2015 年。
2. *Turtles All the Way Down: Storing Secrets in the Cloud and the Data Center*，Daniel Somerfield，AppSecUSA 2015，https://appsecusa2015.sched.com/event/621130a7c1090d129134ab6fb1c3cba4

## 优势

3. X.509 原是 X.500 电信标准的一部分，该标准提出建立一个全球目录，用户可按名称查询人类和服务器的数据并获取其证书。除 X.509 之外，X.500 标准的其余部分均未得到广泛采用。
4. 更多信息参见 https://www.rfc-editor.org/rfc/pdfrfc/rfc5280.txt.pdf。
5. 一项较新的扩展名为 X.509 Name Constraints（名称约束，参见 https://tools.ietf.org/html/rfc5280%23page-40），允许对证书颁发机构（CA）施加限制，使其无法为外部组织签发证书，但该扩展并未得到广泛采用。
6. 服务如何与证书颁发机构进行安全通信？由于证书颁发机构自身的证书是广为人知的，任何人都可以与其建立安全连接。
7. 关于证书吊销列表（CRL）及其潜在问题的介绍，参见 Ronald Rivest 的文章《Can we eliminate certificate revocation lists?》（参见 https://people.csail.mit.edu/rivest/pubs/Riv98b.pdf）。
8. 身份本身并不授予授权；相反，是将与该身份相关的特定属性关联起来（存储在独立存储中），从而使决策点或执行点能够判断该实体是否获得访问授权。

## SPIFFE 与 SPIRE 概念介绍

9. 该 API 不要求身份认证是一个重要区别，因为这正是我们得以解决底层乌龟问题的一个关键方面。SPIFFE 实现仍然有责任准确识别 API 的调用方，但必须以禁止工作负载传递带内凭据的方式来完成。
10. 随身份一同提供的信息可能包括中间 CA 证书、用于证明身份的私钥，以及用于校验 SVID 的公钥。
11. 身份本身同时包含信任域和名称两部分。名称部分有时可能被称为“身份”，但如果没有信任域来确保其唯一性，则被视为不完整。

## 开始之前

12. 一篇关于技术采纳群体的优秀读物：*Technology Adoption Curve: Traits of Adopters at Each Stage of the Lifecycle*（参见 https://academy.whatfix.com/technology-adoption-curve）。

## 设计 SPIRE 部署

13. 集群由多个配置完全相同的服务器构成。
