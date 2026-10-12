---
id: 09-subscription-billing-and-contract-accounting/mds-5bd-429
title: 创建订阅产品销售开票 - MDS (5BD) (5BD_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script 5BD for SAP S/4HANA Cloud 2608: creating subscription billing products, rate elements, pricing lookup tables and S/4HANA product enrichment."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5BD_S4CLD2608_Master_Data_ZH_XX]
keywords: [Subscription Products and Rate Plans, subscription products, rate elements, billing plan templates, pricing lookup tables, price calculation service, product master enrichment, sbpd and sbre product types, distribution chain, country versions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-429
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建订阅产品销售开票 - MDS (5BD) (5BD_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建订阅产品销售开票 - MDS (5BD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897672)

[2 前提条件 4](#_Toc233897673)

[2.1 系统访问 4](#_Toc233897674)

[2.2 角色 4](#_Toc233897675)

[2.3 所需组织单位 (SAP S/4HANA) 4](#_Toc233897676)

[3 概览表 6](#_Toc233897677)

[4 过程 7](#_Toc233897678)

[4.1 创建订阅产品 (SAP Subscription Billing) 7](#_Toc233897679)

[4.1.1 创建计费项 7](#_Toc233897680)

[4.1.2 创建计费方案模板 9](#_Toc233897681)

[4.1.3 创建产品 11](#_Toc233897682)

[4.1.4 使用定价方案创建产品 12](#_Toc233897683)

[4.1.5 上载价格确定的查找表 15](#_Toc233897684)

[4.2 丰富订阅产品 (SAP S/4HANA) 21](#_Toc233897685)

[4.2.1 增强 SBPD 类型的订阅开票产品 21](#_Toc233897686)

[4.2.2 增强 SBRE 类型的订阅开票产品 23](#_Toc233897687)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何创建订阅产品主数据的描述 数据。该描述包括与主数据相关的数据段。 在“普通”系统环境中工作。读者主要了解哪些数据段 通常需要使用输入值填充 和 字段。与 无关的字段 尽管范围可能出现在 UI 上，但本文档中未描述范围。

按此处所述创建的订阅主记录可用于： 订阅计费。

| 订阅产品标识 | 描述 | 用法 |
| --- | --- | --- |
| P-CLOUD_STORAGE | 订阅产品 | 表示订阅开票产品 |
| P-CLD_STORAGE_PCS | 价格计算服务产品 | 表示价格计算产品 |

## 前提条件

### 系统访问

| 系统 | 明细 |
| --- | --- |
| SAP S/4HANA 系统 | 可通过 SAP Fiori 快速启动板访问。您的系统管理员 为您提供访问分配给以下用户的各种应用的 URL 您的角色。 |
| SAP Subscription Billing | 可通过 URL 访问。系统管理员为您提供 用于访问应用程序的 URL。 |
| 价格计算服务 | 可通过 SAP Fiori 快速启动板访问。您的系统管理员 为您提供访问分配给以下用户的各种应用的 URL 您的角色。 |

### 角色

使用 SAP 提供的以下业务角色模板创建业务角色并分配 提供给你的测试用户。

SAP S/4HANA

| 名称 | 标识 |
| --- | --- |
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST |

SAP Subscription Billing

请联系您的系统管理员进行权限设置。

### 所需组织单位 (SAP S/4HANA)

主数据的一些段取决于公司的组织单位， 常规 （中央）数据不取决于组织单位或公司代码。因此， 下表提供了这些不同数据段及其相关 组织单位：

| 数据段 | 取决于 | 要使用的组织单位 | 要使用的组织单位 |
| --- | --- | --- | --- |
| 创建主数据记录 | 销售组织 | 1710（国内销售组织 - US） | 对于德国，使用 1010（国内销售组织 - DE） |
| 创建主数据记录 | 分销渠道 | 10（直销） | 10（直销） |

## 概览表

此主记录由下表中提供的多个段组成。

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| 创建订阅产品 (SAP Subscription Billing) | 不适用 | 不适用 | 已创建订阅产品。 |
| 创建订阅产品 (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | 管理产品主数据 | 已创建订阅产品。 |

## 过程

本节介绍属于此主数据的每个段或流程步骤的过程。 记录。

### 创建订阅产品 (SAP Subscription Billing)

#### 创建计费项

目的

在此活动中，您可以在 SAP Subscription Billing 中创建计费项。费率标识必须与 SBRE 类型的相关 S/4HANA 产品相对应：

| 费率标识 | 费率类型 | 描述 |
| --- | --- | --- |
| R-ONETIME | 一次性 | 一次性激活费用 |
| R-SEATS | 周期性 | 基于座席的每月费用 |
| R-TRAFFIC | 基于使用量 | 基于流量的用量费用 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Subscription Billing 快速启动板。 | 因此， 主页 页面。 |  |
| 2 | 导航到计费项 | 低于 主数据和配置 ，选择 管理业务配置 > 计费项 。 | 因此， 计费项 视图。 |  |
| 3 | 创建计费项：R-ONETIME | 选择 创建 > 一次性 然后维护以下数据：标识： R-ONETIME单位 ： 每个 (EA)标签 ： 一次性激活费用数据源 ： 没有一次性类型 ： 初始 费用开票类型 ： 费用描述 ：维护描述，例如 ，一次性激活费激活 ： 已选择选择 保存 。 | 创建 R-ONETIME 计费项。 |  |
| 4 | 创建计费项：R-SEATS | 选择 创建 ，然后维护以下数据：类型： 周期性标识： R-SEATS单位 ： 每个 (EA)标签 ： 基于座席的每月费用数据源 ： 订阅开票类型 ： 费用描述 ：维护描述，例如 ，基于座席的每月费用激活 ： 已选择选择 保存 。 | 创建 R-SEATS 计费项。 |  |
| 5 | 创建计费项：R-TRAFFIC | 选择 创建 ，然后维护以下数据：类型： 基于使用量标识： R-TRAFFIC单位 ： 每个 EA标签 ： 基于流量的用量费用数据源 ： 用法开票类型 ： 费用使用计费子项 ： 已选择 （仅针对 PCS 产品）用量计费变式 ： 已汇总技术资源标识类型： 云存储空间标识描述 ：维护描述，针对 示例 ，上载/下载流量激活 ： 已选择选择 保存 。 | 创建 R-TRAFFIC 计费项。 |  |

|  |
| --- |
| 备注 技术资源识别 中的订户和订阅的服务 技术系统。当您根据 为客户开票时，需要这些内容 您的服务使用情况。例如，测量电力消耗，此处为 技术资源标识类型： 可定义为 “电表标识”，这是唯一标识（例如 EM392734-A） 针对其发布用途。在里程管理场景中， 测量， 技术资源标识类型： 可能是 定义为“汽车牌照号”。这是用户输入字段，根据服务/场景进行定义。 |

#### 创建计费方案模板

目的

在此活动中，您可以在 SAP Subscription Billing 中创建计费方案模板。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到计费方案模板 | 低于 定价 ，选择 管理计费方案 模板 应用。 | 随即显示可用的计费方案模板。 |  |
| 3 | 创建计费方案模板： | 选择 创建 > 不含定价方案 并在 中维护以下数据： 常规信息 ：描述： 基于座席的计划模板开票周期 ： 每月的 每月的第一天货币： 值 - 美元 （适用于美国国家版本） | 因此， 计费方案模板 屏幕。 |  |
| 4 | 维护计费项的费用/贷项 | 在费用/贷项部分中，选择 费用/贷项， 选择 添加 然后选择 一次性 。然后维护 以下数据：计费项 ： R-ONETIME价格 值 ： 100 美元对于 费用/贷项 ，选择 创建 然后选择 周期性 然后选择 百分比定价费用 。然后 维护以下数据：费率 元素 ： R-SEATS应用 下一周期变更 ： 已选择提前开票 ： 已选择首期按比例分摊 ： 已选择单价 ： 10 美元比率 ： 100对于 费用/ 信用 ，选择 添加 以及 然后选择 用法 冻结 定价 。然后维护以下内容 数据：计费项 ： R-TRAFFIC费率 子元素 ：维护 费率 子元素如果 使用率 子元素 选项在 中启用[创建计费项](#unique_7) [第 ] 页 7 步骤。备注 计费子项 是必填字段，如果 在 使用计费子项 选项为 已启用。变更下期生效 ：不是 已选择已含数量 ： 值 - 1冻结 大小 ： 值 – 1单位区块价格 ： 值 – 1 美元（针对国家/地区版本） US）选择 创建 。然后选择 发布 。 | 已创建费用/贷项。 |  |

#### 创建产品

目的

在此活动中，您可以在 SAP Subscription Billing 中创建产品 P-CLOUD_STORAGE。的标识 SAP Subscription Billing 中的产品必须与相关产品标识相对应 在 SAP S/4HANA 中。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到产品 | 低于 主数据和配置 ，打开 管理 产品 应用。 | 显示可用产品。 |  |
| 3 | 维护基本产品信息 | 选择 创建 并维护以下数据： 常规信息 范围：产品名称： 云存储产品标识： P-CLOUD_STORAGE订阅类型 ： 商业将订阅创建为待定： 已取消选择订阅设置 ： S/4 集成 | 已维护常规信息。 |  |
| 4 | 维护产品的计费方案 | 低于 计费方案 ，选择 创建 > 不含定价方案 并维护以下数据：备注 如果您使用的产品需要定价方案，则必须选择 含定价 方案 。有关使用和不使用定价方案的定价的概览，请参阅[定价](https://help.sap.com/docs/subscription-billing/feature-overview/pricing) （在 SAP Subscription Billing 文档中）。市场 ： 美国东部 （适用于美国国家版本）计费方案模板 ： 基于座席的计划模板描述 ： 经常性计费方案（基于季节）开票周期 ：每月第一天 月选择 创建 。 | 已为产品维护计费方案。 |  |
| 5 | 维护订阅期限 | 低于 订阅期限 ，维护以下内容：预计期限 ：例如 12最短期限 ： 12续约期限 ： 12撤销期间 ： 14 | 已维护订阅期限。 |  |
| 6 | 创建产品 | 对于整个产品，选择 创建 。然后选择 发布 。 | P-CLOUD_STORAGE 产品已创建。 |  |

#### 使用定价方案创建产品

在浏览示例用例时，您可以使用示例值从 创建数据 或者，您可以使用随每个新 租户。必须先在价格计算服务中执行以下步骤： 使用定价方案创建产品。

您可以在 中找到有关如何使用定价方案设置定价（使用示例）的详细描述[使用定价方案的定价配置指南](https://help.sap.com/docs/subscription-billing/pricing-configuration/pricing-with-pricing-schemes-configuration-guide)。

过程

1. 管理字段目录

如果使用示例数据，则在 中使用预定义的字段目录。 管理字段目录 应用。因此，你无需做任何 此处有附加设置。因此， 管理字段目录 应用 允许您创建稍后用于定义查找表的字段 和价格项说明的输入属性。

2. 创建查找表

在 中 管理查找表 应用，您可以创建查找 通过将输入字段集映射到输出字段集进行表。这些查找 然后在后续步骤中使用表创建价格项说明。因此， 此步骤的目标是创建以下一次性查找表， 经常性费用和使用费：

- 一次性价格
- RecurringPrice
- UsagePrice
- 折扣 1

这些表是预定义内容的一部分。因此，您无需进行任何额外的 此步骤中的设置。

3. 价格元素细则

在 中 管理价格项说明 应用，定义您的 通过创建价格项说明进行定价配置。其中包括 设置定价逻辑和可覆盖字段：

- 一次性价格
- RecurringPrice
- UsagePrice
- 折扣 1

|  |
| --- |
| 备注 如果上述元素的价格项说明不是 维护，你必须维护它们 管理价格 元素规格 应用，方法是选择单个 元素 可覆盖字段 > 添加/创建 > 价格/折扣 > 保存 。 |

4. 定价方案

在 中 管理定价方案 应用，您可以创建和维护定价 模式。定价方案是一个程序，用于定义用途和关系 给定可定价凭证的价格项说明。另外， 确定执行这些规范以生成 已定价凭证中的总金额。

定价方案“初始”是预定义内容的一部分。因此，您需要 在此步骤中不要进行任何附加设置。

5. 创建计费方案模板

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到 计费方案 模板 应用 | 转到 定价 > 管理计费方案模板 | 随即显示计费方案模板。 |  |
| 3 | 选择 创建 | 选择 创建 > 含定价 方案 并维护以下数据 英寸 常规信息 ：描述 ： RPT 用于 价格计算标签 ： PCS （可选）定价方案 ： 初始开票周期 ：每月第一天 月日期账单设置 ： 初始设置货币 ： 美元 | 已维护常规信息。 |  |
| 4 | 维护 费用/贷项 针对费率 元素 | 对于一次性，选择 费用/贷项 > 创建 > 一次性 并输入 费率 元素 = R-ONETIME 。选择 可覆盖字段详细信息 > 创建 > 折扣 1 并输入 一次性 价格 = 选择 。 选择 应用 。对于经常性，选择 费用/贷项 > 创建 > 周期性 并输入 费率 元素 = R-SEATS 。选择 可覆盖字段详细信息 > 创建 > 折扣 1 并输入 周期性 价格 = 选择 。 选择 应用 。对于用途，请选择 费用/贷项 > 创建 > 使用区块定价 并输入 费率 元素 = R-TRAFFIC 以及 费率 子元素 。备注 计费子项 是一个 必填字段（如果 使用率 子元素 选项在 中启用 [创建计费项](#unique_7) [第 ] 页 7 step。选择 可覆盖字段详细信息 > 创建 > 折扣 1 并输入 基于使用量 价格 = 选择 。 选择 应用 。选择 创建 然后 发布 。 |  |  |

6. 创建产品

创建产品 P-CLOUD_STORAGE_PC 在 SAP Subscription Billing 中。SAP Subscription Billing 中产品的标识 必须与 SAP S/4HANA 中的相关产品标识相对应。您可以使用 以下过程：

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Subscription Billing。 | 因此， 主页 页面。 |  |
| 2 | 导航到 产品 | 低于 主数据和配置 ，打开 管理 产品 应用。 | 显示可用产品。 |  |
| 3 | 维护常规产品信息 | 选择 创建 并维护 以下数据 常规 信息 范围：产品名称 ： Cloud 存储价格计算产品标识 ： P-CLOUD_STORAGE_PC订阅类型 ： 商业将订阅创建为待定 ： 已取消选择 | 已维护常规信息。 |  |
| 4 | 维护产品的计费方案 | 在 计费方案 标签上，选择 创建 - > 含定价方案 导航到 创建模板 并维护以下数据：市场 ： 美国 东部 （适用于美国国家版本）计费方案模板 ： RPT 用于价格计算描述 ： RPT 用于 价格计算开票周期 ：每月 当月的第一天选择 创建 。 | 已为产品维护计费方案。 |  |
| 5 | 维护 订阅期限 | 低于 订阅参数 ，维护以下数据： 在 订阅期限 范围：预计期限 ：例如 12最短期限 ： 12续约期限 ： 12撤销期间 ： 14 | 已维护订阅期限。 |  |
| 6 | 创建产品 | 在 产品 视图，选择 创建 。选择 发布 。 | P-CLOUD_STORAGE_PC 产品已创建。 |  |

7.上载价格确定的查找表

有关上载查找表的详细信息，请参阅[上载价格确定的查找表](#unique_11) [第 ] 页 15。

#### 上载价格确定的查找表

您可以上载一次性、周期性和基于用量的费用的查找表，并为 上载查找表 折扣，使用以下过程。结果表中的数据用于查找 价格确定期间作为定价流程一部分的相关价格。

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
| 3 | 选择 UsagePrice | 选择查找表 UsagePrice 。下载空表并将其本地存储为 CSV 文件。提示 如果下载文件的格式不是 列 分隔，您必须更改电子表格的格式 转换为美国格式。 |  |  |
| 4 | 更新下载的文件 | 输入以下值并保存文件：产品代码 ： P-CLOUD_STORAGE_PCmarketId ： A1费率元素 ： R-TRAFFIC价格 ： 体积价格（价格类型） ： 线性以下特定值可用于 的每个分层 高费率子元素：rateSubElement ：高价格（范围） ：500价格（范围单位） ：EA价格（值） ：30价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于每个分层：rateSubElement ：高价格（范围） ：1000价格（范围单位） ：EA价格（值） ：25价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于每个分层：rateSubElement ：高价格（范围） ：价格（范围单位） ：EA价格（值） ：20价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于 的每个分层 低费率子项：rateSubElement ：低价格（范围） ：500价格（范围单位） ：EA价格（值） ：15价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于 的每个分层 低费率子项：rateSubElement ：低价格（范围） ：1000价格（范围单位） ：EA价格（值） ：10价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA以下特定值可用于 的每个分层 低费率子项：rateSubElement ：低价格（范围） ：价格（范围单位） ：EA价格（值） ：5价格（价值货币） ： 美元价格（数量值） ：1价格（数量单位） ：EA |  |  |
| 5 | 上载 CSV 文件 | 选择查找表 UsagePrice 然后继续 到 导入 > 浏览 从上一步上载保存的文件。备注 有两种类型的导入。选择 合并 保持现有的 数据完好无损。单击 导入 。 | 查找表 UsagePrice 已更新。 |  |

表 4：上载折扣表

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Price Calculation | 因此， 主页 页面。 |  |
| 2 | 导航到 计费方案模板 | 低于 主数据管理 ，打开 管理查找表数据 应用。 | 随即显示查找表。 |  |
| 3 | 选择 折扣 1 | 选择查找表 折扣 1 。下载空表并将其本地存储为 CSV 文件。提示 如果下载文件的格式不是 列 分隔，您必须更改电子表格的格式 转换为美国格式。 |  |  |
| 4 | 更新下载的文件 | 输入以下值并保存文件：marketId ： A1折扣 ： 单个折扣（价格类型） ： 百分比折扣（值） ： 0.1 |  |  |
| 5 | 上载 CSV 文件 | 选择查找表 折扣 1 然后继续 到 导入 > 浏览 从上一步上载保存的文件。备注 有两种类型的导入。选择 合并 保持现有的 数据完好无损。单击 导入 。 | 查找表 折扣 1 已更新。 |  |

### 丰富订阅产品 (SAP S/4HANA)

#### 增强 SBPD 类型的订阅开票产品

目的

在此活动中，增强 SAP S/4HANA 中的订阅开票产品 P-CLOUD_STORAGE。 此产品在订阅开票中创建，复制到 SAP S/4HANA，并且 将产品复制设置为范围项目 57Z 的一部分后可用。 有关产品复制的详细信息，请参阅[配置产品和费率复制的 IFlow 包 元素](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/93e79ab9ec8e4dc49bc1710e396608ed.html)。

|  |
| --- |
| 备注 巴西特定字段需要正确的税款计算。有关详细信息 关于此内容，请参阅 物料主数据 > 为主数据定义业务规则特定字段 > 创建巴西主数据 (JD0_BR) 。 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用。 |  |
| 3 | 查找产品 | 在顶部的搜索区域中，输入 产品 ： P-CLOUD_ 存储 和 P-CLOUD_ STORAGE_PC 。选择 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链：常规 信息 | 从报表清单中选择产品，产品编号： P-CLOUD_STORAGE基本单位： EA产品类型： SBPD（后续开票产品）描述： 云存储然后选择 确定 。备注 位于 描述 请提供 语言 和 产品 特定地区的详细信息， 例如， 语言 ： 英语 和 产品 ： 订阅 计费产品 。 | 应打开产品并维护基本信息。 |  |
| 5 | 维护分销链：一般信息 | 在 产品 视图，位于 分布 链 区域，请选择 创建 并维护以下 数据：销售组织 ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）备注 不需要分销链 SBPD 产品 如果您使用 MDI，则键入 。仅在以下情况下才需要它们： 正在使用云集成。 |  | 对于德国国家版本，改为维护以下值 1710：销售组织 ： 1010（国内 德国销售组织）这两个国家的其他条目相同 |
| 6 | 维护分销链：分组条件 | 导航到 分组条件 区域并维护以下数据：项目类别组 ： SBPD（后续开票产品）科目分配组 ： X9（定期服务）税收分类 ： 1（全额税）然后选择 应用 > 创建 。备注 不需要项目类别组。 SBPD 产品 如果您使用 MDI，则键入 。仅在以下情况下才需要执行此操作： 正在使用云集成。 | 维护分组条件并保存产品。 | 对于德国国家版本，改为维护以下值 1（全额税）：税收分类 ： 6（全额税） 服务业）这两个国家的其他条目相同。 |
| 7 | 维护工厂 | 导航到 工厂 > 创建 并维护以下数据：工厂 ： 1710（美国工厂）选择 应用 > 保存 。 | 已维护工厂数据。 |  |

#### 增强 SBRE 类型的订阅开票产品

目的

在此活动中，增强 SAP S/4HANA 中的以下订阅产品： 对应于 SAP Subscription Billing 中的计费项：产品在 订阅开票并复制到 SAP S/4HANA。计费项将可用 按 57Z 范围项目设置指南中所述设置产品复制后 或参阅[产品和计费项复制](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/9dbec8b5ce1841a6a39f0af5571ed63b.html?version=latest)。

|  |
| --- |
| 备注 巴西特定字段需要正确的税款计算。有关详细信息 相关内容，请参阅 物料主数据 > 为主数据定义业务规则特定字段 > 检查创建巴西主数据 (JD0_BR) 。 |

| 产品标识 | 产品类型 | 描述 |
| --- | --- | --- |
| R-ONETIME | SBRE | 一次性激活费用 |
| R-SEATS | SBRE | 基于座位的每月费用 |
| R-TRAFFIC | SBRE | 基于流量的用量费用 |

过程

产品：R-ONETIME

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用。 |  |
| 3 | 查找产品 | 在顶部的搜索区域中，输入 产品 ： R-ONETIME 。选择 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链：常规 信息 | 在 产品 视图，位于 分销链 区域，选择 创建 并维护以下数据：销售组织 ： 1710（国内销售组织 - US）分销渠道 ： 10（直接 销售）备注 位于 描述 提供 语言 以及 产品 特定地区的详细信息，用于 例如， 语言 ： 英语 以及 产品 ： 订阅开票 产品 。 | 应打开产品并维护基本信息。 | 对于德国国家版本，维护以下值而不是 1710：销售组织 ： 1010（德国国内销售组织）这两个国家的其他条目相同。 |
| 5 | 维护分销链：分组条件 | 导航到 分组条件 区域并维护以下数据：科目分配组 ： X9（定期服务）税收分类 ： 1（全额税）然后选择 应用 然后 创建 。备注 产品类型不需要项目类别组。 SBRE 如果正在使用 MDI。 | 维护分组条件并保存产品。 | 对于德国国家版本，维护以下值而不是 1 （全额税）：税收分类 ： 6（全额税（服务））两个版本的其他条目相同。 |
| 6 | 维护工厂 | 导航到 工厂 区域，选择 创建 并维护以下数据：工厂 ：1710（美国工厂）选择 应用 以及 保存 。 | 已维护工厂数据。 | 对于德国国家版本，维护以下值：工厂 ： 工厂 10101（工厂 DE） |

产品：R-SEATS

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用。 |  |
| 3 | 查找产品 | 在顶部的搜索区域中，输入 产品 ： R-SEATS按下按钮 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链：常规 信息 | 在 产品 视图，位于 分销链 区域，选择 创建 并维护以下数据：销售组织 ： 1710（国内销售 组织 (US)分销渠道 ： 10（直接 销售）备注 位于 描述 提供 语言 以及 产品 特定地区的详细信息，用于 例如， 语言 ： 英语 以及 产品 ： 订阅开票 产品 。 | 应打开产品并维护基本信息。 | 对于德国国家版本，维护以下值而不是 1710：销售组织 ：1010（国内销售组织 DE）这两个国家的其他条目相同 |
| 5 | 维护分销链：分组条件 | 导航到 分组条件 区域并维护以下数据：科目分配组 ： X9（定期服务）税收分类 ： 1（全额税）然后选择 应用 。 | 维护分组条件并保存产品。 | 对于德国国家版本，维护以下值而不是 1 （全额税）：税收分类 ： 6（全额税（服务））两个版本的其他条目相同。 |
| 6 | 维护工厂 | 导航到 工厂 区域，选择 创建 并维护以下数据：工厂 ：1710（美国工厂）选择 应用 以及 保存 。 | 已维护工厂数据。 | 对于德国国家版本，维护以下值：工厂 ： 工厂 1010（工厂） DE） |

产品: R-TRAFFIC

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 主页 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 管理产品主数据 磁贴。 | 因此， 管理产品主数据 应用。 |  |
| 3 | 查找产品 | 在顶部的搜索区域中，输入 产品 ： R - 交通按下按钮 执行 。 | 您的产品将显示在报表清单中。 |  |
| 4 | 打开产品并维护分销链：常规 信息 | 在 产品 视图，位于 分销链 区域，选择 创建 并维护以下数据：销售组织 ： 1710（国内销售 组织 (US)分销渠道 ： 10（直接 销售）备注 位于 描述 提供 语言 以及 产品 特定地区的详细信息，用于 例如， 语言 ： 英语 以及 产品 ： 订阅开票 产品 。 | 应打开产品并维护基本信息。 | 对于德国国家版本，维护以下值而不是 1710：销售组织 ：1010（国内销售组织 DE）这两个国家的其他条目相同 |
| 5 | 维护分销链：分组条件 | 导航到 分组条件 区域并维护以下数据：项目类别组 ： SBRE（替代开票费率要素）科目分配组 ： X9（定期服务）税收分类 ： 1（全额税）选择 应用 然后 保存 。备注 产品 不需要项目类别组 SBRE （如果您正在使用 MDI）。 | 产品已保存。 | 对于德国本地版本，维护以下值而不是 1 （全额税）：税收分类 ： 6（全额税（服务））两个版本的其他条目相同。 |
| 6 | 维护工厂 | 导航到 工厂 区域，选择 创建 并维护以下数据：工厂 ：1710（美国工厂）选择 应用 然后 保存 。 | 已维护工厂数据。 | 对于德国国家版本，维护以下内容 值： 工厂 ：工厂 10101（工厂 DE） |

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
> Flagged while digesting this document, not verified: Plant for Germany R-SEATS given as 1010 while R-ONETIME and R-TRAFFIC give 10101 (internal inconsistency)

> [!warning] Conflict
> Flagged while digesting this document, not verified: Product ID P-CLD_STORAGE_PCS in overview table differs from P-CLOUD_STORAGE_PC created in procedure

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-facturacion-de-ventas-de-productos-de-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 17,543 chars in the whole document
