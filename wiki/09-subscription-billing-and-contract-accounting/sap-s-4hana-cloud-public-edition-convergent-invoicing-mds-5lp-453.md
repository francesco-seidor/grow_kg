---
id: 09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453
title: 主数据脚本 SAP S/4HANA Cloud Public Edition - 创建订阅产品 Convergent Invoicing - MDS (5LP) (5LP_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script 5LP: create business partners, contract accounts and subscription products in SAP Subscription Billing and enrich them in S/4HANA."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5LP_S4CLD2608_Master_Data_ZH_XX]
keywords: [Subscription Products and Rate Plans, subscription products, business partner creation, customer master data, contract accounts, rate elements, billing plan templates, price calculation service, pricing lookup tables, product master enrichment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-453
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 主数据脚本 SAP S/4HANA Cloud Public Edition - 创建订阅产品 Convergent Invoicing - MDS (5LP) (5LP_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建订阅产品 Convergent Invoicing - MDS (5LP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897678)

[2 前提条件 4](#_Toc233897679)

[2.1 系统访问 4](#_Toc233897680)

[2.2 角色 4](#_Toc233897681)

[2.3 所需组织单位 (SAP S/4HANA) 5](#_Toc233897682)

[3 概览表 6](#_Toc233897683)

[4 过程 7](#_Toc233897684)

[4.1 创建业务伙伴 7](#_Toc233897685)

[4.1.1 创建客户主数据 8](#_Toc233897686)

[4.1.2 创建合同科目 11](#_Toc233897687)

[4.2 创建订阅产品 (SAP Subscription Billing) 12](#_Toc233897688)

[4.2.1 创建计费项 12](#_Toc233897689)

[4.2.2 创建计费方案模板 14](#_Toc233897690)

[4.2.3 创建产品 (SAP Subscription Billing) 15](#_Toc233897691)

[4.2.4 为价格计算服务创建产品 18](#_Toc233897692)

[4.2.5 上载价格确定的查找表 20](#_Toc233897693)

[4.3 增强订阅开票产品 26](#_Toc233897694)

[4.3.1 增强 SBPD 类型的订阅产品 26](#_Toc233897695)

[4.3.2 增强 SBRE 类型的订阅产品 29](#_Toc233897696)

[5 附录 33](#_Toc233897697)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何创建订阅产品主数据的描述 数据。该描述包括与主数据相关的数据段。 在“普通”系统环境中工作。在这里，读者主要了解 需要使用输入值填充的段和字段。字段不是 此文档中不描述与范围相关，尽管它们可能出现在 UI。

根据此凭证创建的订阅主记录可用于： 订阅计费。

| 订阅产品标识 | 描述 | 用法 |
| --- | --- | --- |
| P-CLOUD_COMM | 订阅产品 | 表示订阅产品 |
| P-CLOUD_SUPPORT | 订阅产品 | 表示订阅产品 |

## 前提条件

### 系统访问

下表讨论系统访问要求。

| 系统 | 明细 |
| --- | --- |
| SAP S/4HANA 系统 | 可通过 SAP Fiori 快速启动板访问。系统管理员为您提供访问 分配给您的角色的各种应用。 |
| SAP Subscription Billing | 可通过 URL 访问。系统管理员为您提供访问 应用程序。 |

### 角色

您可以使用提供的以下业务角色模板创建业务角色。 由 SAP 提供，并将其分配给您的个人测试用户。

SAP S/4HANA

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） | 登录 |
| --- | --- | --- | --- | --- |
| 主数据 专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST | 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST |  |
| 应付账款和应收账款会计 (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | 应付账款和应收账款会计 (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA |  |

SAP Subscription Billing

您必须联系系统管理员设置所需的 authorizations。

### 所需组织单位 (SAP S/4HANA)

虽然主数据的某些段取决于 公司，常规（中央）数据不依赖于组织单位或 公司代码。下表提供了这些不同数据段的概览。 及其相关组织单位：

| 数据段 | 取决于 | 要使用的组织单位 | 备注 |
| --- | --- | --- | --- |
| 创建主数据记录 | 销售组织 | 1710（国内销售组织 - US） | 对于德国，使用 1010（国内销售组织 - DE） |
| 创建主数据记录 | 分销渠道 | 10（直销） |  |

## 概览表

此主记录由下表中提供的多个段组成。

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| 创建订阅产品（SAP 订阅） 计费） | 不适用 | 不适用 | 已创建订阅产品。 |
| 丰富订阅产品 (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | 管理产品主数据 | 已创建订阅产品。 |

## 过程

本部分介绍属于此流程的每个段或流程步骤的过程。 主记录。

### 创建业务伙伴

上下文

在此活动中，为 S/4HANA Cloud 中的新 FI-CA 客户创建业务伙伴。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以应付账款和应收账款会计 (FI-CA) 身份登录 SAP Fiori 快速启动板。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 维护业务伙伴 (BP) 。 | 因此， 维护业务伙伴 视图。 |  |
| 3 | 创建业务伙伴 | 选择 人员 或选择 更多 > 业务伙伴 > 创建 > 人员 。 | 因此， 创建人员 视图。 |  |
| 4 | 选择业务伙伴角色 | 输入以下内容：在业务伙伴角色中创建 ： 合同合作伙伴 | 因此， 更改为其他业务伙伴角色 视图在创建中显示 mode。 |  |
| 5 | 创建 | 选择 创建 | 选择 合同伙伴角色 基于 创建 人员 对话框。合同合作伙伴（新） 已为 选择 在业务伙伴角色中创建 。 |  |
| 6 | 输入基本数据 | 输入以下内容：业务伙伴 ： <输入特定标识> ，例如 BP_US_97分组 ： 外部字母数字编号 |  |  |
| 7 | 输入地址数据 | 输入以下条目： 地址 标签：名/姓 ： John/Miller街道/门牌号 ： Hillview Ave/3410邮政编码/城市 ： 94304/PALO ALTO国家/地区 ： 美国地区 ： CA税收管辖权 ： CA00000000提示 如果 税收管辖权 不是 可见，单击 + 展开 options。 |  |  |
| 8 | 维护付款数据 | 使用 添加银行详细信息 管理业务伙伴 应用，以及 注册付款卡使用 管理 业务伙伴主数据 应用。在以下条目中输入： 付款 事务 标签：位于 银行详细信息 部分输入：标识 ： 01国家 ： 美国银行代码 ： 011000390银行账户 ： <银行 账户>Swift 代码 (SWIFT/BIC) ： CITIUS33XXX选择 提交 。 | 因此， 检查对账码 视图弹出。 |  |
| 9 | 保存 | 选择 保存 。 | 新业务伙伴已创建。 |  |

#### 创建客户主数据

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

在此活动中，使用业务伙伴角色扩展 FI-CA 业务伙伴 FLCU01 以及 MKK 销售范围主数据。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 使用您的用户凭据登录到 SAP Fiori 快速启动板，用户凭据为 SAP_BR_APR_ACCOUNTANT_FICA | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 维护业务伙伴 （业务伙伴） 。 | 因此， 维护业务伙伴 屏幕。 |  |
| 3 | 选择业务伙伴 | 输入 业务伙伴 编号 |  |  |
| 4 | 打开业务伙伴 | 选择 输入 |  |  |
| 5 | 切换到更改模式 | 选择 在显示和更改之间切换 |  |  |
| 6 | 在业务伙伴角色中更改 | 在 中 在业务伙伴角色中更改 字段中，选择 以下值： 客户此业务伙伴角色的技术代码 是 FLCU01 。 |  |  |
| 7 | 输入地址信息 | 信函语言： <EN> |  |  |
| 8 | 打开销售范围 | 选择 销售和分销 （位于视图顶部）。 | 因此， 销售范围 视图。 |  |
| 9 | 输入销售范围数据 | 输入以下数据：销售组织 ： 1710分销渠道 ： 10产品组 ： 00选择 输入 然后 保存 。备注 以上三个条目构成了销售范围。在许多情况下，销售 设置销售处理目的，例如，在 销售订单或定价。 | 已为业务伙伴保存更改。 |  |
| 10 | 输入装运数据 | 在 装运 标签 相关 装运 部分，输入以下内容 数据：交货工厂 ： 1710 |  |  |
| 11 | 输入税务信息 | 在 开票 选项卡，位于 输出 税收 部分，输入以下数据：税收分类 ： <1>例如，值 <1> 表示此客户完全应税。 |  |  |
| 12 | 保存数据 | 保存输入内容。 |  |  |
| 13 | 在业务伙伴角色中更改 | 在 中 在业务伙伴角色中更改 字段中，选择 以下值： 合同合作伙伴此业务伙伴角色的技术代码 是 MKK 。 |  |  |
| 14 | 输入地址信息 | 信函语言： <EN> |  |  |
| 15 | 输入装运数据 | 在 装运 标签页中的 装运 部分，输入以下数据：交货工厂 ： 1710 |  |  |
| 16 | 输入税务信息 | 在 开票 标签页中的 输出 税收 部分，输入以下数据：税收分类 ： <1>例如，值 <1> 表示此客户完全应税。 |  |  |
| 17 | 保存数据 | 保存输入内容。 |  |  |

#### 创建合同科目

上下文

在此活动中，为 中的 FI-CA 客户创建合同科目主数据 SAP S/4HANA Cloud Public 版本 。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 使用用户凭据，使用应付账款和应收账款会计 (FI-CA) 业务角色登录到 SAP Fiori 快速启动板。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 维护合同科目 (CAA3) 。 | 因此， 合同帐户显示：初始屏幕 显示 。 |  |
| 3 | 创建合同科目 | 选择 创建 或选择 更多 > 合同科目 > 创建 。 | 因此， 合同帐户创建：初始屏幕 显示 。 |  |
| 4 | 输入基本数据 | 输入以下内容：合同账户 ： <输入特定标识> ，例如， CA_US_97业务伙伴 ： <选择在创建业务伙伴步骤中创建的业务伙伴编号>合同科目类别 ： Y1有效自 ： <当天日期> |  |  |
| 5 | 维护合同账户详细信息 | 选择 继续 。 | 因此， 合同帐户创建：一般数据 屏幕。 |  |
| 6 | 输入基本信息 | 在以下条目中输入： 常规 标签：合同科目名称 ： <合同账户名称>科目关系 ： 账户持有人容差组 ： Y001 不允许容差计划组 ： 国内客户付款条件 ： YN01科目确定标识 ： Y1 |  |  |
| 7 | 输入付款/税收数据 | 在以下条目中输入： 付款/税收 标签：公司代码组 ： 1710标准公司代码 ： 1710 |  |  |
| 8 | 输入催款/信函 | 输入以下条目： 催款/信函 标签：信函变式 ： <仅打印输出，立即> |  |  |
| 9 | 保存 | 选择 保存 。 | 随即创建新的合同科目。 |  |

### 创建订阅产品 (SAP Subscription Billing)

#### 创建计费项

目的

在此活动中，您可以在 SAP Subscription Billing 中创建计费项。费率标识 必须与 类型的相关 S/4HANA 产品相对应 SBRE ：

| 费率标识 | 费率类型 | 描述 |
| --- | --- | --- |
| R-ONETIME | 一次性 | 一次性激活费用 |
| R-SEATS | 周期性 | 基于座席的每月费用 |
| R-票据 | 基于使用量 | 基于票据的使用费用 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到计费项 | 低于 主数据和配置 ， 选择 业务配置 > 计费项 。 | 因此， 计费项 视图。 |  |
| 3 | 创建计费项：一次性 | 选择 创建 ，然后维护以下内容 数据：类型： 一次性标识： R-ONETIME单位 ： 每个 EA标签 ： 一次性激活 费用数据源 ： 没有一次性类型 ： 初始 费用开票类型 ： 费用描述 ：维护描述，针对 示例 ，一次性激活费激活 ： 已选择选择 保存 。 | 创建 R 一次性计费项。 |  |
| 4 | 创建计费项：R-SEATS | 选择 创建 ，然后维护以下内容 数据：类型： 周期性标识： R-SEATS单位 ： 每个 EA标签 ： 基于座席的每月 费用数据源 ： 订阅开票类型 ： 费用描述 ：维护描述，针对 示例 ，基于座席的每月费用激活 ： 已选择选择 保存 。 | 创建 R-SEATS 计费项。 |  |
| 5 | 创建计费项：R-TICKETS | 选择 创建 ，然后维护以下内容 数据：类型： 基于使用量标识： R-票据单位 ： 千兆字节（GB）/件（EA）标签 ： 基于消息的使用 费用数据源 ： 用法开票类型 ： 费用用量计费变式 ： 已汇总技术资源标识类型： 云存储空间标识描述 ：维护描述，针对 示例 ， 中的上载/下载流量 GB激活 ： 已选择选择 保存 。 | 创建 R-TICKETS 计费项。 |  |

#### 创建计费方案模板

目的

在此活动中，您可以在 SAP Subscription Billing 中创建计费方案模板。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到计费方案模板 | 低于 定价 ，打开 计费方案模板 应用。 | 随即显示可用的计费方案模板。 |  |
| 3 | 创建计费方案模板：SEATS | 选择 创建 > 不含定价方案 ，并在 中维护以下数据： 常规信息 ：描述： 基于座席的计划模板开票周期 ： 值 - 每月 在每月的第一天货币： 值 - 美元 （适用于美国国家版本）选择 添加 | 已定义模板的基本数据。 |  |
| 4 | 维护 SEATS 的费用/贷项 | 在 中创建一次性费用 费用/贷项 分段依据 选择 添加 > 一次性 。维护以下数据：计费项 ： R-ONETIME价格 ： 值 - 9.99 美元 （适用于美国国家版本）在 中创建固定资费 费用/贷项 分段依据 选择 添加 > 周期性 > 百分比定价 。维护以下数据：计费项 ： R-SEATS变更下期生效 ： 已选择提前开票 ：已选择首期按比例分摊 ： 已选择单价 ： 1 美元比率 ： 100在 中创建基于用量的费用 费用/贷项 分段依据 选择 添加 > 基于使用量 > 区块定价 。维护以下数据：费率 元素 ： R-票据变更下期生效 ： 未选择已含数量 ： 值 - 1区块大小 ： 价值 - 1单位区块价格 ： 值 - 1 美元 （针对国家/地区 版本 US）选择 保存 以及 发布 。 | 已创建费用/贷项。 |  |

#### 创建产品 (SAP Subscription Billing)

目的

在此活动中，您可以在 SAP 中创建产品 P-CLOUD_COMM 和 P-CLOUD_SUPPORT Subscription Billing。SAP Subscription Billing 中产品的标识必须 对应于 SAP S/4HANA 中的相关产品标识

过程

产品：P-CLOUD_COMM

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到产品 | 在 下 主数据和 配置 目录，选择 业务配置 > 产品 。 | 显示可用产品。 |  |
| 3 | 维护基本产品信息 | 选择 创建 ，然后维护 以下数据 常规信息 area：产品名称： 云通信产品标识： P-CLOUD_COMM订阅类型 ： 商业将订阅创建为待定： 已取消选择电子销售： 已选择 | 已维护常规信息。 |  |
| 4 | 维护产品的计费方案 | 在 中 计费方案 范围 ， 选择 从 创建计费方案 模板。在 创建计费方案 视图，维护 以下数据：市场 ： 美国东部 （适用于美国国家版本）计费方案模板 ： 基于座席的计划模板描述 ： 周期性 费率计划（基于季节） | 已维护产品的计费方案。 |  |
| 5 | 维护订阅期限 | 维护以下订阅参数详细信息：预计期限 ： 用于 示例，12最短期限 ： 12续约期限 ： 12撤销期间 ： 14 | 已维护订阅期限。 |  |
| 6 | 创建产品 | 在 创建计费方案 视图，请选择 创建 。在 产品 视图，请选择 保存 。然后选择 发布 。 | P-CLOUD_COMM 产品已创建。 |  |

产品：P-CLOUD_SUPPORT

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到产品 | 在左侧导航区域中，选择 产品 。 | 显示可用产品。 |  |
| 3 | 维护基本产品信息 | 选择 创建 ，然后维护 以下数据 常规信息 area：产品名称： 云支持产品标识： P-CLOUD_SUPPORT订阅类型 ： 商业将订阅创建为待定： 已取消选择电子销售： 已选择 | 已维护常规信息。 |  |
| 4 | 维护产品的计费方案 | 在 中 计费方案 范围 ， 选择 从 创建计费方案 模板。在 创建计费方案 视图，维护 以下数据：市场 ： 美国东部 （适用于美国国家版本）计费方案模板 ： 基于座席的计划模板描述 ： 周期性 费率计划（基于季节） | 已维护产品的计费方案。 |  |
| 5 | 维护订阅期限 | 维护订阅参数详细信息：预计期限 ： 用于 示例，12最短期限 ： 12续约期限 ： 12撤销期间 ： 14 | 已维护订阅期限。 |  |
| 6 | 创建产品 | 在 创建计费方案 视图，请选择 创建 。在 产品 视图，请选择 保存 。然后选择 发布 。 | P-CLOUD_SUPPORT 产品已创建。 |  |

#### 为价格计算服务创建产品

在浏览示例用例时，您可以使用示例值来创建数据 也可以使用预定义配置，该配置随每个 新租户。必须先执行价格计算中的以下步骤，然后才能创建 PCS 的产品。

过程

1. 管理字段目录

如果使用示例数据，则在 中使用预定义的字段目录。 管理字段目录 应用。因此，你无需做任何 此处有附加设置。因此， 管理字段目录 应用 允许您创建稍后用于定义查找表的字段 和价格项说明的输入属性。

2. 创建查找表

在 中 管理查找表 应用，您可以创建查找 通过将输入字段集映射到输出字段集进行表。这些查找 然后在后续步骤中使用表创建价格项说明。因此， 此步骤的目标是创建以下一次性查找表， 经常性费用和使用费：

- 一次性价格
- RecurringPrice
- UsagePrice
- 折扣 1

这些表是预定义内容的一部分。因此，你无需做任何 此步骤的附加设置。

3. 价格元素细则

在 中 管理价格项说明 应用，定义您的 通过创建价格项说明进行定价配置。其中包括 设置定价逻辑和可覆盖字段：

- 一次性价格
- RecurringPrice
- UsagePrice
- 折扣 1

这些价格项说明是预定义内容的一部分。因此，您 无需在此步骤中进行任何附加设置。

4. 定价方案

在 中 管理定价方案 应用，您可以创建并维护 定价方案。定价方案是一个程序，用于定义用途和 给定可定价凭证的价格项说明关系。 它还确定执行这些规范的顺序，以生成 已定价凭证中的总金额。

定价方案“初始”是预定义内容的一部分。因此，您需要 在此步骤中不要进行任何附加设置。

5. 创建计费方案模板

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到 计费方案 模板 应用 | 转到 定价 > 计费方案模板 | 随即显示计费方案模板。 |  |
| 3 | 选择 创建 | 选择 创建 - 含定价 方案 并维护以下数据 英寸 常规信息 ：描述 ： RPT 用于 价格计算标签 ： PCS （可选）定价方案 ： 初始开票周期 ：每月第一天 月日期货币 ： 美元 | 已维护常规信息。 |  |
| 4 | 维护 费用/贷项 针对费率 元素 | 对于一次性，选择 费用/贷项 > 添加 > 一次性 并输入 费率 元素 = R-ONETIME 。对于经常性，选择 费用/贷项 > 添加 > 周期性 并输入 费率 元素 = R-SEATS 。对于用途，请选择 费用/贷项 > 添加 > 使用区块定价 并输入 费率 元素 = R-TRAFFIC 。选择 保存 然后 发布 。 |  |  |

6. 创建产品

创建产品 P-CLOUD_STORAGE_PC 在 SAP Subscription Billing 中。SAP Subscription Billing 中产品的标识 必须与 SAP S/4HANA 中的相关产品标识相对应。您可以使用 以下过程：

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到 产品 | 低于 主数据和 配置 ，打开 产品 应用。 | 显示可用产品。 |  |
| 3 | 维护常规产品信息 | 选择 创建 并维护 以下数据 常规 信息 范围：产品名称 ： Cloud 存储价格计算产品标识 ： P-CLOUD_STORAGE_PC订阅类型 ： 商业将订阅创建为待定 ： 已取消选择 | 已维护常规信息。 |  |
| 4 | 维护产品的计费方案 | 在 计费方案 标签上，选择 创建 - 含定价 方案 。备注 有关价格计算产品的详细信息，请参阅[SAP Subscription Billing 与 定价方案](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)导航到 从 创建计费方案 模板 > 创建含定价的计费方案 方案 并维护以下数据：市场 ： 美国 东部 （适用于美国国家版本）计费方案模板 ： RPT 用于价格计算描述 ： RPT 用于 价格计算开票周期 ：每月 当月的第一天选择 创建 。 | 已为产品维护计费方案。 |  |
| 5 | 维护 订阅期限 | 在 中维护以下数据： 订阅期限 范围：预计期限 ：例如 12最短期限 ： 12续约期限 ： 12撤销期间 ： 14 | 已维护订阅期限。 |  |
| 6 | 创建产品 | 在 创建计费方案 视图、 选择 创建 。在 产品 视图，请选择 保存 。选择 发布 。 | P-CLOUD_STORAGE_PC 产品已创建。 |  |

7.上载价格确定的查找表

有关上载查找表的详细信息，请参阅 正在上载 价格确定的查找表。

有关价格计算产品的详细信息，请参阅[使用定价方案的 SAP Subscription Billing](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)

#### 上载价格确定的查找表

您可以上载一次性、周期性和基于用量的费用的查找表，并为 上载查找表 折扣，使用以下步骤。下表中的数据用于 在价格确定期间查找相关价格作为定价流程的一部分。

表 1：上载一次性表

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Price Calculation | 因此， 主页 页面。 |  |
| 2 | 导航到 计费方案模板 | 低于 主数据管理 ，打开 管理查找表数据 应用。 | 随即显示查找表。 |  |
| 3 | 选择 一次性价格 | 选择查找表 一次性价格 。下载空表并将其本地存储为 CSV 文件。提示 如果下载文件的格式不是 列 分隔，您必须更改电子表格的格式 转换为美国格式。 |  |  |
| 4 | 更新下载的文件 | 输入以下值并保存文件：产品代码 ： P-CLOUD_STORAGE_PCmarketId ： A1费率元素 ： R-ONETIME价格 ： 单个价格（价格类型） ： 固定价格（值） ： 5000价格（价值货币） ： 美元 |  |  |
| 5 | 上载 CSV 文件 | 选择查找表 一次性价格 以及 转到 导入 > 浏览 从上一步上载保存的文件。备注 有两种类型的导入。选择 合并 保持现有的 数据完好无损。单击 导入 。 | 查找表 一次性价格 已更新。 |  |

表 2：上载循环表

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Price Calculation | 因此， 主页 页面。 |  |
| 2 | 导航到 计费方案模板 | 低于 主数据管理 ，打开 管理查找表数据 应用。 | 随即显示查找表。 |  |
| 3 | 选择 RecurringPrice | 选择查找表 RecurringPrice 。下载空表并将其本地存储为 CSV 文件。提示 如果下载文件的格式不是 列 分隔，您必须更改电子表格的格式 转换为美国格式。 |  |  |
| 4 | 更新下载的文件 | 输入以下值并保存文件：产品代码 ： P-CLOUD_STORAGE_PCmarketId ： A1费率元素 ： R-SEATS价格 ： 单个价格（价格类型） ： 线性价格（值） ： 50价格（价值货币） ： 美元价格（数量值） ： 1价格（数量单位） ： EA |  |  |
| 5 | 上载 CSV 文件 | 选择查找表 RecurringPrice 以及 转到 导入 > 浏览 从上一步上载保存的文件。备注 有两种类型的导入。选择 合并 保持现有的 数据完好无损。单击 导入 。 | 查找表 RecurringPrice 已更新。 |  |

表 3：上载使用表

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Price Calculation | 因此， 主页 页面。 |  |
| 2 | 导航到 计费方案模板 | 低于 主数据管理 ，打开 管理查找表数据 应用。 | 随即显示查找表。 |  |
| 3 | 选择 UsagePrice | 选择查找表 一次性价格 。下载空表并将其本地存储为 CSV 文件。提示 如果下载文件的格式不是 列 分隔，您必须更改电子表格的格式 转换为美国格式。 |  |  |
| 4 | 更新下载的文件 | 输入以下值并保存文件：产品代码 ： P-CLOUD_STORAGE_PCmarketId ： A1费率元素 ： R-TRAFFIC价格 ： 体积价格（价格类型） ： 线性以下特定值可用于 的每个分层 高费率子元素：rateSubElement ：高价格（范围） ：500价格（范围单位） ：EA价格（值） ：30价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于每个分层：rateSubElement ：高价格（范围） ：1000价格（范围单位） ：EA价格（值） ：25价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于每个分层：rateSubElement ：高价格（范围） ：价格（范围单位） ：EA价格（值） ：20价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于 的每个分层 低费率子项：rateSubElement ：低价格（范围） ：500价格（范围单位） ：EA价格（值） ：15价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于 的每个分层 低费率子项：rateSubElement ：低价格（范围） ：1000价格（范围单位） ：EA价格（值） ：10价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于 的每个分层 低费率子项：rateSubElement ：低价格（范围） ：价格（范围单位） ：EA价格（值） ：5价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA |  |  |
| 5 | 上载 CSV 文件 | 选择查找表 一次性价格 并转到 导入 > 浏览 从上一步上载保存的文件。备注 有两种类型的导入。选择 合并 保持现有的 数据完好无损。单击 导入 。。 | 查找表 一次性价格 已更新。 |  |

表 4：上载折扣表

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Price Calculation | 因此， 主页 页面。 |  |
| 2 | 导航到 计费方案模板 | 低于 主数据管理 ，打开 管理查找表数据 应用。 | 随即显示查找表。 |  |
| 3 | 选择 折扣 1 | 选择查找表 折扣 1 。下载空表并将其本地存储为 CSV 文件。提示 如果下载文件的格式不是 列 分隔，您必须更改电子表格的格式 转换为美国格式。 |  |  |
| 4 | 更新下载的文件 | 输入以下值并保存文件：marketId ： A1折扣 ： 单个折扣（价格类型） ： 百分比折扣（值） ： 0.1 |  |  |
| 5 | 上载 CSV 文件 | 选择查找表 折扣 1 并转到 导入 > 浏览 从上一步上载保存的文件。备注 有两种类型的导入。选择 合并 保持现有的 数据完好无损。单击 导入 。。 | 查找表 折扣 1 已更新。 |  |

### 增强订阅开票产品

#### 增强 SBPD 类型的订阅产品

目的

在此活动中，增强订阅产品 P-CLOUD_COMM 和 P-CLOUD_SUPPORT。这些产品在 SAP Subscription 中创建 计费并复制到 SAP S/4HANA。

过程

产品：P-CLOUD_COMM

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用 出现。 |  |
| 3 | 查找产品 P-CLOUD_COMM | 在顶部的搜索区域中，输入 产品： P-CLOUD_COMM 。按下按钮 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链： 常规信息 | 从报表清单中选择产品，产品编号： P-CLOUD_COMM基本单位： EA产品类型： SBPD（后续开票产品）然后选择 确定 。备注 位于 描述 请提供 语言 和 产品 特定的详细信息 地区，例如， 语言 ： 英语 和 产品 ： 订阅 计费产品 。 | 产品应该已打开，并且一般信息是 维护。 |  |
| 5 | 维护分销链：一般 信息 | 在 产品 视图，位于 分销链范围，c 选择 创建 并维护以下 数据：销售组织 ： 1710 国内销售组织 US分销渠道 ： 10 直接销售备注 SBPD 产品不需要分销链 如果您使用 MDI，则键入 。仅在以下情况下需要： 正在使用云集成。 | 维护分组条件并保存产品。 | 对于德国国家版本，维护以下值 代替 1（全额税）：税收分类：6（全额税（服务））这两个国家的其他条目相同。 |
| 6 | 维护分销链：分组 条款 | 导航到 分组条件 范围 并维护以下数据：项目类别组 ： SBPD （订阅开票产品）科目分配组 ： X9（定期服务）税收分类 ： 1 （全额税）然后选择 应用然后创建 。备注 仅当使用 时才需要项目类别组 云集成而非主数据集成 用于复制 |  |  |
| 7 | 维护工厂 | 导航到 工厂范围 ，选择 创建和维护以下数据：工厂 ：1710（美国工厂）然后选择 应用 然后 保存 | 已维护工厂数据。 |  |

产品：P-CLOUD_SUPPORT

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用 出现。 |  |
| 3 | 查找产品 P-CLOUD_SUPPORT | 在顶部的搜索区域中，输入 产品： P-CLOUD_SUPPORT按下按钮 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链： 常规信息 | 从报表清单中选择产品，产品编号： P-CLOUD_COMM基本单位： EA产品类型： SBPD（后续开票产品）然后选择 确定 。备注 位于 描述 请提供 语言 和 产品 特定的详细信息 地区，例如， 语言 ： 英语 和 产品 ： 订阅 计费产品 。 | 产品应该已打开，并且一般信息是 维护。 |  |
| 5 | 维护分销链：一般 信息 | 在 产品 视图，位于 分销链范围，c 选择 创建 并维护以下 数据：销售组织 ： 1710 国内销售组织 US分销渠道 ： 10 直接销售备注 SBPD 产品不需要分销链 如果正在使用主数据集成，则键入 。仅限 如果您正在使用 Cloud Integration，则为必需。 | 维护分组条件并保存产品。 | 对于德国国家版本，维护以下值 代替 1（全额税）：税收分类：6（全额税（服务））这两个国家的其他条目相同。 |
| 6 | 维护分销链：分组 条款 | 导航到 分组条件 范围 并维护以下数据：项目类别组 ： SBPD （订阅开票产品）科目分配组 ： X9（定期服务）税收分类 ： 1 （全额税）然后选择 应用然后创建 。备注 SBPD 产品不需要分销链 如果使用主数据集成，则键入 ，并且 仅在使用 Cloud 时需要 集成。 |  |  |
| 7 | 维护工厂 | 导航到 工厂范围 ，选择 创建和维护以下数据：工厂 ：1710（美国工厂）然后选择 应用 然后 保存 | 已维护工厂数据。 |  |

#### 增强 SBRE 类型的订阅产品

目的

在此活动中，增强 SAP S/4HANA 中的以下订阅产品。 这些产品在 SAP Subscription Billing 中创建并复制到 SAP S/4HANA。

| 产品标识 | 产品类型 | 描述 |
| --- | --- | --- |
| R-ONETIME | SBRE | 一次性激活费用 |
| R-SEATS | SBRE | 基于座位的每月费用 |
| R-票据 | SBRE | 基于票据的使用费用 |

过程

产品：R_ONETIME

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用 出现。 |  |
| 3 | 查找产品 R_ONETIME | 在搜索区域中，输入 产品： R-ONETIME单击 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链： 常规信息 | 在 产品 视图，位于 分销链范围，c 选择 创建 并维护以下 数据：销售组织 ： 1710 国内销售组织 US分销渠道 ： 10 直接销售现金折扣 ： 是备注 位于 描述 请提供 语言 和 产品 特定的详细信息 地区，例如， 语言 ： 英语 和 产品 ： 订阅开票 产品 。 | 产品应该已打开，并且一般信息是 维护。 | 对于德国国家版本，维护以下值 代替 1710：销售组织 ： 1010 国内销售组织 DE这两个国家的其他条目相同。 |
| 5 | 维护分销链：分组 条款 | 导航到 分组条件 范围 并维护以下数据：科目分配组 ： X9（定期服务）税收分类 ： 1 （全额税）然后选择 应用 。 | 维护分组条件并保存产品。 | 对于德国国家版本，维护以下值 代替 1（全额税）：税收分类 ： 6 （全额税（服务））这两个国家的其他条目相同。 |
| 6 | 维护工厂 | 导航到 工厂 区域，请选择 创建 并维护以下 数据：工厂： 1710（美国工厂）然后选择 应用 然后 创建 。 | 已维护工厂数据。 |  |

产品：R_SEATS

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用 出现。 |  |
| 3 | 查找产品 R_SEATS | 在搜索区域中，输入 产品： R-SEATS单击 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链： 常规信息 | 从报表清单中选择产品。在 产品 视图，点击 开 编辑 。在 中 分销链 区域， 选择 创建 并维护 以下数据：销售组织 ： 1710 国内销售组织 US分销渠道 ： 10 直接销售备注 位于 描述 请提供 语言 和 产品 特定的详细信息 地区，例如， 语言 ： 英语 和 产品 ： 订阅开票 产品 。 | 产品应该已打开，并且一般信息是 维护。 | 对于德国国家版本，维护以下值 代替 1710：销售组织 ： 1010 国内销售组织 DE这两个国家的其他条目相同。 |
| 5 | 维护分销链：分组 条款 | 导航到 分组条件 范围 并维护以下数据：项目类别组 ： SBRE Sub.计费计费项）科目分配组 ： X9（定期服务）税收分类 ： 1 （全额税）然后选择 应用。 | 维护分组条件并保存产品。 | 对于德国国家版本，维护以下值 代替 1（全额税）：税收分类 ： 6 （全额税（服务））这两个国家的其他条目相同。 |
| 6 | 维护工厂 | 导航到 工厂 区域，请选择 创建 并维护以下 数据：工厂： 1710（美国工厂）然后选择 应用 以及 保存 。 | 已维护工厂数据。 |  |

产品：R_TICKETS

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用 出现。 |  |
| 3 | 查找产品 R_TICKETS | 在搜索区域中，输入 产品： R-票据单击 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链： 常规信息 | 从报表清单中选择产品。在 产品 视图，点击 开 编辑 。在 中 分销链 区域， 选择 创建 并维护 以下数据：销售组织 ： 1710 国内销售组织 US分销渠道 ： 10 直接销售备注 位于 描述 请提供 语言 和 产品 特定的详细信息 地区，例如， 语言 ： 英语 和 产品 ： 订阅开票 产品 。 | 产品应该已打开，并且一般信息是 维护。 | 对于德国国家版本，维护以下值 代替 1710：销售组织 ： 1010 国内销售组织 DE这两个国家的其他条目相同。 |
| 5 | 维护分销链：分组 条款 | 导航到 分组条件 范围 并维护以下数据：科目分配组 ： X9（定期服务）税收分类 ： 1 （全额税）然后选择 应用。 | 维护分组条件并保存产品。 | 对于德国国家版本，维护以下值 代替 1（全额税）：税收分类 ： 6 （全额税（服务））这两个国家的其他条目相同。 |
| 6 | 维护工厂 | 导航到 工厂 区域，请选择 创建 并维护以下 数据：工厂： 1710（美国工厂）然后选择 应用 以及 保存 。 | 已维护工厂数据。 |  |

## 附录

表 5：排版惯例

| 字体样式 | 描述 |
| --- | --- |
| 示例 | 屏幕中引用的单词或字符。其中包括字段名称、屏幕标题、按钮标签、菜单 名称、菜单路径和菜单选项。对其他文档的文本交叉引用。 |
| 示例 | 强调的词语或表达。 |
| 示例 | 系统对象的技术名称。其中包括报告名称、程序名称、事务代码、表 编程语言的名称和关键概念 由正文括起来，例如 SELECT 和 INCLUDE。 |
| 示例 | 屏幕上的输出。这包括文件和目录名称及其路径、消息、 变量和参数的名称、源文本和名称关闭 安装、升级和数据库工具。 |
| 示例 | 确切的用户输入。这些是在系统中输入的单词或字符，与 它们出现在文档中。 |
| <示例> | 可变用户输入。尖括号表示替换这些单词和字符。 使用适当的条目在系统中进行输入。 |
| 示例 | 键盘上的键，例如， F2 或 输入 。 |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen. These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross-references to other documents. |
| Example | Emphasized words or expressions. |
| EXAMPLE | Technical names of system objects. These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen. This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names of installation, upgrade and database tools. |
| Example | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry. Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| EXAMPLE | Keys on the keyboard, for example, F2 or ENTER. |

|  |
| --- |
|  |
| www.sap.com/contactsap |
| © 2026 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company. The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors. National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies. See [www.sap.com/copyright](http://www.sap.com/copyright) for additional trademark information and notices. |

<!-- image omitted: SAP Logo -->

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Usage rate element named R-TICKETS in rate element section but R-TRAFFIC in the price calculation template and usage lookup table steps

> [!warning] Conflict
> Flagged while digesting this document, not verified: P-CLOUD_SUPPORT enrichment step opens product number P-CLOUD_COMM

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 21,758 chars in the whole document
