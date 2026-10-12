---
id: 10-procurement/mds-bhd-567
title: 创建采购信息记录 - MDS (BHD) (BHD_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) SAP S/4HANA Cloud Public 2608 master data script BHD: creating purchasing info records (standard, consignment, subcontracting, pipeline) and mass changes."
cluster: 10-procurement
tags: [kb/procurement, topic/purchasing-info-records]
aliases: [BHD_S4CLD2608_Master_Data_ZH_XX]
keywords: [Purchasing Info Records, consignment info record, subcontracting info record, pipeline info record, mass change info records, mass price change, number ranges, business roles, master data prerequisites, tax code configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-567
topic: 10-procurement/purchasing-info-records
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建采购信息记录 - MDS (BHD) (BHD_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Purchasing Info Records** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建采购信息记录 - MDS (BHD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897893)

[2 前提条件 4](#_Toc233897894)

[2.1 系统访问 4](#_Toc233897895)

[2.2 角色 4](#_Toc233897896)

[2.3 所需组织单位 4](#_Toc233897897)

[2.4 必填和可选主数据 5](#_Toc233897898)

[2.5 数据创建的主要参数 5](#_Toc233897899)

[2.5.1 编号范围 5](#_Toc233897900)

[3 概览表 6](#_Toc233897901)

[4 测试过程 7](#_Toc233897902)

[4.1 创建采购信息记录 7](#_Toc233897903)

[4.2 创建寄售的采购信息记录 9](#_Toc233897904)

[4.3 创建转包的采购信息记录 12](#_Toc233897905)

[4.4 创建管道的采购信息记录 14](#_Toc233897906)

[4.5 批量更改采购信息记录 17](#_Toc233897907)

[4.6 采购信息记录的批量价格更改 19](#_Toc233897908)

[5 附录 21](#_Toc233897909)

[5.1 相关功能 21](#_Toc233897910)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

采购信息记录包含特定于物料和提供物料的供应商的信息。

其中包含供应商收取的价格、其标准订单数量和过量交货容差等信息，以及 在递送下。它用于采购订单事务中。

信息特定于特定采购单位（称为采购组织）和特定站点（称为工厂） 在您的组织内。

## 前提条件

本部分汇总了执行系统、用户、主数据、组织数据、其他测试数据和业务条件方面测试的所有前提条件。

### 系统访问

| 系统 | 明细 |
| --- | --- |
| 系统 | 可通过 SAP Fiori 快速启动板访问。系统管理员为您提供用于访问分配给您的角色的各种应用的 URL。 |

### 角色

使用 SAP 提供的以下业务角色模板创建业务角色，并将其分配给各个测试用户。

或者，如果可用，您可以使用 SAP 提供的以下空间。创建包含预定义基本应用的页面的空间，并将其分配到业务角色。然后将此业务角色分配给单个用户。

有关详细信息，请参阅 如何从模板创建业务角色 （在[产品帮助](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) 对于 SAP S/4HANA Cloud Public 版本 。

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） | 登录 |
| --- | --- | --- | --- | --- |
| 采购员 | SAP_BR_PURCHASER | 采购 / 供应商开发及合同管理 | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### 所需组织单位

贵公司的组织结构和主数据在 ERP 系统中创建 项目实施期间。组织结构反映您的 公司。下表提供了这些不同数据段的概览，以及 其相关组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 采购数据 | 采购组织 | 采购组、物料组、收货处理时间等。 | 对于物料所属的每个采购组织，都可以存在采购数据 用于采购流程。 | 采购组织：__________ |

### 必填和可选主数据

采购信息记录可能参考其他主数据。下表提供了 要在采购信息中使用的可选和强制主数据对象的概览。 记录。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 材料 |  | 必填 | 要输入物料，首先要创建物料主数据。 |
| 供应商 |  | 必填 | 要输入供应商，首先要创建供应商主数据。 |

### 数据创建的主要参数

在此部分中，为影响 行为的基本参数提供描述。 采购信息记录，并且始终需要这些信息来创建采购信息记录。

#### 编号范围

为采购信息记录定义了以下编号范围：

| 编号范围 | 范围/业务伙伴标识 | 备注 |
| --- | --- | --- |
| 内部编号 | 用于标准用途的内部数字编号范围：5300000000 – 5399999999 | 系统自动将数字编号分配给以下各项时使用此编号范围： material。 |
| 外部数字 | 外部数字编号范围（高）：5400000000 – 5499999999 | 此编号范围保留用于外部数字编号分配。 |

## 概览表

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建采购信息记录](#unique_10) [第 ] 页 7 | 采购员 | 管理采购信息记录 (F1982) | 已创建采购信息记录。 |
| [创建寄售的采购信息记录](#unique_11) [第 ] 页 9 | 采购员 | 管理采购信息记录 (F1982) | 已创建寄售的采购信息记录。 |
| [创建转包的采购信息记录](#unique_12) [第 ] 页 12 | 采购员 | 管理采购信息记录 (F1982) | 转包的采购信息记录已创建。 |
| [创建管道的采购信息记录](#unique_13) [第 ] 页 14 | 采购员 | 管理采购信息记录 (F1982) | 已创建管道的采购信息记录。 |
| [批量更改采购信息记录](#unique_14) [第 ] 页 17 | 采购员 | 批量更改采购信息记录 (F2667) | 已应用对采购信息记录的批量更改。 |
| [采购信息记录的批量价格更改](#unique_15) [第 ] 页 19 | 采购员 | 价格更改：信息记录 | 已应用采购信息记录的批量价格更改。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建采购信息记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理采购信息记录 (F1982) 。 | 因此， 管理采购信息记录 (F1982) 屏幕。 |  |
| 3 | 打开新采购信息 记录 | 选择 创建 。 | 因此， 采购信息记录屏幕 随即显示。 |  |
| 4 | 输入抬头数据 | 输入以下内容：采购信息记录类别 ： <标准>采购组织 ： <采购 组织>供应商 ： <供应商>材料 ： <物料>工厂 ： <工厂>采购组 ： <采购 组> | 已添加抬头数据。 |  |
| 5 | 输入基本信息 | 输入以下内容：可用自 ： MM/DD/YYYY可用至 ： MM/DD/YYYY | 基本信息 已添加。 |  |
| 6 | 输入采购数据 | 输入以下内容：国际贸易条款 ： <国际贸易条款>国际贸易条款位置 1 ： <国际贸易条款位置 1> | 采购数据 已添加。 |  |
| 7 | 输入交货和数量 数据 | 输入以下内容：交货时间（天） ： <XX 天>交货不足容差百分比 ： <XX>过量交货容差 (%) ： <XX>税码 ： <税收 代码>备注 当通过以下方式激活 TDT（时间相关税收）时 配置步骤 101016（定义税码 销售和采购） 提供税码，税率有效期自字段为 必填。您可以输入当前日期， 已调整为税码的有效开始日期 根据配置步骤中的设置。当 RITA（间接征税登记）时 国外），税务登记国家是 在配置步骤中为公司代码维护 103464（激活 RITA 并维护税收登记） 国家/地区）和税码，税收国家/地区 字段必填，其中 给定公司代码作为缺省值，但您可以 更改为在 中维护的有效国家/地区标识 相应配置步骤。备注 根据您的配置环境，可以在 下访问配置步骤 配置您的解决方案 在 SAP Fiori 快速启动板或 业务流程配置 应用在 SAP Central Business Configuration 的项目体验中。订单单位 ： <订单单位>标准订单数量 ： <标准订单 数量>根据需要选择以下条目：无限制交货基于收货的发票 验证无评估收货 结算订单确认需求确认控制 | 交货和数量数据 已添加。 |  |
| 8 | 输入条件数据 | 在 中 条件 部分，选择 创建 图标。 输入以下数据：有效自 ： <有效期起始日期>金额 ： <金额>定价单位 ： <定价单位>有效期至 ： <有效期截止日期>货币 ： <货币>选择 应用 。 | 条件数据已添加。 |  |
| 9 | 输入参考数据（可选） | 或者，您可以输入参考数据。 | 已添加参考数据。 |  |
| 10 | 保存数据 | 选择 创建 。 | 已保存采购信息记录。 |  |

### 创建寄售的采购信息记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理采购信息记录 (F1982) | 随即显示管理采购信息记录屏幕。 |  |
| 3 | 打开新的采购信息记录 | 选择 创建 。 | 随即显示采购信息记录屏幕。 |  |
| 4 | 输入抬头数据 | 输入以下内容：采购信息记录 类别 ： < 寄售>采购组织 ： <采购 组织>供应商 ： <供应商>材料 ： <物料>工厂 ： <工厂>采购组 ： <采购组> | 已添加抬头数据。 |  |
| 5 | 输入基本信息 | 输入以下内容：可用自 ： MM/DD/YYYY可用至 ： MM/DD/YYYY | 已添加常规信息。 |  |
| 6 | 输入采购数据 | 输入以下内容：国际贸易条款 ： <国际贸易条款>国际贸易条款位置 1 ： <国际贸易条款位置 1> | 已添加采购数据。 |  |
| 7 | 输入交货和数量数据 | 输入以下内容：交货时间（天） ： <XX 天>交货不足容差百分比 ： <XX>过量交货容差 (%) ： <XX>税码 ： <税码>备注 当通过以下方式激活 TDT（时间相关税收）时 配置步骤 101016（定义税码 销售和采购） 提供税码，税率有效期自字段为 必填。您可以输入当前日期， 已调整为税码的有效开始日期 根据配置步骤中的设置。当 RITA（间接征税登记）时 国外），税务登记国家是 在配置步骤中为公司代码维护 103464（激活 RITA 并维护税收登记） 国家/地区）和税码，税收国家/地区 字段必填，其中 给定公司代码作为缺省值，但您可以 更改为在 中维护的有效国家/地区标识 相应配置步骤。备注 根据您的配置环境，可以在 下访问配置步骤 配置您的解决方案 在 SAP Fiori 快速启动板或 业务流程配置 应用在 SAP Central Business Configuration 的项目体验中。订单单位 ： <订单 单位>标准订单数量 ： <标准订单 数量> | 已添加交货和数量数据。 |  |
| 8 | 输入条件数据 | 在条件部分，选择 创建 图标。输入 以下数据：有效自 ： <有效期自 日期>金额 ： <金额>定价单位 ： <定价 单位>有效期至 ： <有效期至 日期>货币 ： <货币>选择 应用 。 | 条件数据已添加 |  |
| 9 | 输入参考数据（可选） | 或者，您可以输入参考数据。 | 已添加参考数据。 |  |
| 10 | 保存数据 | 选择 创建 。 | 已保存采购信息记录。 |  |

### 创建转包的采购信息记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理采购信息记录 (F1982) 。 | 管理采购信息记录 (F1982) 屏幕 显示 。 |  |
| 3 | 打开新的采购信息记录 | 选择 创建 。 | 随即显示采购信息记录屏幕。 |  |
| 4 | 输入抬头数据 | 输入以下内容：采购信息记录 类别 ： <转包>采购组织 ： <采购 组织>供应商 ： <供应商>材料 ： <物料>工厂 ： <工厂>采购组 ： <采购组> | 已添加抬头数据。 |  |
| 5 | 输入基本信息 | 输入以下内容：可用自 ： MM/DD/YYYY可用至 ： MM/DD/YYYY | 已添加常规信息。 |  |
| 6 | 输入交货和数量数据 | 输入以下内容：交货时间（天） ： <XX 天>交货不足容差百分比 ： <XX>过量交货容差 (%) ： <XX>税码 ： <税码>备注 当通过以下方式激活 TDT（时间相关税收）时 配置步骤 101016（定义税码 销售和采购） 提供税码，税率有效期自字段为 必填。您可以输入当前日期， 已调整为税码的有效开始日期 根据配置步骤中的设置。当 RITA（间接征税登记）时 国外），税务登记国家是 在配置步骤中为公司代码维护 103464（激活 RITA 并维护税收登记） 国家/地区）和税码，税收国家/地区 字段必填，其中 给定公司代码作为缺省值，但您可以 更改为在 中维护的有效国家/地区标识 相应配置步骤。备注 根据您的配置环境，可以在 下访问配置步骤 配置您的解决方案 在 SAP Fiori 快速启动板或 业务流程配置 应用在 SAP Central Business Configuration 的项目体验中。订单单位 ： <订单单位>标准订单数量 ： <标准订单 数量> | 已添加交货和数量数据。 |  |
| 7 | 输入条件数据 | 在条件部分，选择 创建 图标。输入 以下数据：有效自 ： <有效期自 日期>金额 ： <金额>定价单位 ： <定价单位>有效期至 ： <有效期至 日期>货币 ： <货币>选择 应用 。 | 条件数据已添加。 |  |
| 8 | 输入参考数据（可选） | 或者，您可以输入参考数据。 | 已添加参考数据。 |  |
| 9 | 保存数据 | 选择 创建 。 | 已保存采购信息记录。 |  |

### 创建管道的采购信息记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理采购信息记录 (F1982) 。 | 应用随即打开。 |  |
| 3 | 打开新的采购信息记录 | 选择 创建 。 | 因此， 采购信息记录屏幕 显示 。 |  |
| 4 | 输入抬头数据 | 输入以下内容：采购信息记录类别 ： <管道>采购组织 ： <采购组织>供应商 ： <供应商>材料 ： <管道物料>工厂 ： <工厂>采购组 ： <采购组>物料组 ： <物料组> | 已添加抬头数据。 |  |
| 5 | 输入基本信息 | 输入以下内容：可用自 ： MM/DD/YYYY可用至 ： MM/DD/YYYY | 已添加常规信息。 |  |
| 6 | 输入采购数据 | 输入以下内容：国际贸易条款 ： <国际贸易条款>国际贸易条款位置 1 ： <国际贸易条款位置 1> | 已添加采购数据。 |  |
| 7 | 输入交货和数量数据 | 输入以下内容：交货时间（天） ： <XX 天>交货不足容差百分比 ： <XX>过量交货容差 (%) ： <XX>税码 ： <税码>备注 通过配置步骤 101016（定义）激活 TDT（时间相关税收）时 销售和采购税码） 提供公司代码和税码，税率 “有效期自”字段为必填字段。您可以输入当前 日期，该日期将调整为有效期开始日期 税码（根据 中的设置） 配置步骤。激活 RITA（国外间接征税登记）时，在 中为公司代码 维护税收登记国家/地区 配置步骤 103464（激活 RITA 并维护税收登记国家/地区）和税码为 给定，税收国家/地区字段为必填字段，其中公司代码的国家/地区标识是缺省的 值，但您可以更改在配置步骤中维护的有效国家/地区标识 相应地。备注 根据您的配置环境，可以在 下访问配置步骤 配置您的解决方案 在 SAP Fiori 快速启动板或 业务流程配置 应用在 SAP Central Business Configuration 的项目体验中。订单单位 ： <订单单位>标准订单数量 ： <标准订单数量>根据需要选择以下条目：无限制交货基于收货的发票 验证无评估收货 结算订单确认 要求确认控制 | 已添加交货和数量数据。 |  |
| 8 | 输入条件数据 | 在 中 条件 部分，选择 创建 。输入以下数据：有效自 ： <有效期起始日期>金额 ： <金额>定价单位 ： <定价单位>有效期至 ： <有效期截止日期>货币 ： <货币>选择 应用 。 | 条件数据已添加。 |  |
| 9 | 输入参考数据（可选） | 或者，您可以输入参考数据。 | 已添加参考数据。 |  |
| 10 | 保存数据 | 选择 创建 。 | 已保存采购信息记录。 |  |

### 批量更改采购信息记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此过程中，将更改应用到多个所选 采购信息 记录 批量。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 批量更改采购信息记录 (F2667) 。 | 应用随即打开。 |  |
| 3 | 搜索采购信息 记录 | 要搜索采购信息记录，请在过滤器中输入以下值：供应商 ： <供应商标识>采购组 ：例如， 001工厂 ： <工厂标识>选择 执行 。 | 搜索结果显示相应过滤条件的详细信息。缺省情况下，为批量更改操作选择所有采购信息记录。 |  |
| 4 | 选择采购信息记录 | 选择 采购信息记录 采购信息记录和采购 组织 标签。选择 批量编辑 。 |  |  |
| 5 | 设置新值 | 在以下条目中输入新值：在 中 常规数据 部分：供应商物料编号供应商物料组在 中 采购组织数据 部分：采购组最小订单数量选择 应用批量更改 。随即显示一个对话框，用于确认批量更改。在 应用批量更改 屏幕上，选择 应用 。随即出现一个对话框，其中显示 作业标识 。选择 查看作业清单 。 | 新值应用于所选采购信息记录。 |  |
| 6 | 检查应用程序作业 | 输入搜索条件并选择执行。因此， 应用程序作业 屏幕，其中包含所有采购信息的作业标识列表 条记录。选择 日志 验证所选采购信息记录是否成功。 |  |  |

### 采购信息记录的批量价格更改

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此过程中， 价格更改：信息记录 （MEKP） 应用用于批量更新信息记录的价格。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 价格更改：信息记录 （MEKP） 。 | 应用随即打开。 |  |
| 3 | 输入初始数据 | 输入以下内容并选择 执行 ：采购组织 ： <采购组织标识>供应商 ： <供应商标识>材料 ： <物料标识>不含物料的信息记录 ： <空白>测试运行 ： <空白>转到 更改条件类型或总价 部分并输入以下内容：条件类型 ： <条件类型标识> ，例如 PPR0绝对金额 ： <绝对金额> ，例如 10符号 ： <符号> ，例如， +总价 ： <空白>等级行 ： <X>转到 条件有效 部分并输入以下内容：打开 ： <当前日期>或者 发件人 <空白> 收件人 <空白> | 为采购信息记录维护新值。 |  |
| 4 | 检查采购信息记录更改 | 在 供应商 <XXXX> 的信息记录的价格更改 屏幕，检查 旧的 和 新建 记录并确认更改。 | 采购信息记录价格更改已保存。 |  |
| 5 | 退出 | 选择 退出 。 |  |  |

## 附录

### 相关功能

下面列出了与采购信息记录相关的一些重要应用程序功能， 上述测试过程中未涵盖的内容。

| 职能范围 | 功能 | 详细的信息 | 备注 |
| --- | --- | --- | --- |
| 采购信息记录 | 信息记录相关应用 | WebGUI：删除采购信息记录 (ME15)WebGUI：按供应商显示采购信息记录 (ME1L)WebGUI：维护对采购信息记录的更改 (ME14)WebGUI：维护采购条件 (MEKA)WebGUI：维护舍入参数文件 (OWD1) |  |

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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/create-purchasing-info-record-mds-bhd-master-data-script-563]]
- related-to :: [[10-procurement/criar-registro-info-para-compras-mds-bhd-566]]
- related-to :: [[10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562]]
- related-to :: [[10-procurement/mds-bhd-565]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 13,362 chars in the whole document
