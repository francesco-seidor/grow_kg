---
id: 13-quality-ehs-and-compliance/mds-bf5-555
title: 创建质量信息记录 - MDS (BF5) (BF5_S4CLD2608_Master_Data_ZH_XX)
description: "SAP S/4HANA Cloud 2608 master data script (ZH, machine-translated) for creating quality info records, QM control keys and PPAP setup as quality planner."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-info-records]
aliases: [BF5_S4CLD2608_Master_Data_ZH_XX]
keywords: [Quality Info Records in Procurement, quality info records, ppap, qm control keys, master data script, first article inspection, supplier approval, goods receipt inspection, quality planner role, BF5]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-555
topic: 13-quality-ehs-and-compliance/quality-info-records
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建质量信息记录 - MDS (BF5) (BF5_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Quality Info Records in Procurement** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建质量信息记录 - MDS (BF5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897859)

[2 前提条件 3](#_Toc233897860)

[2.1 系统访问 3](#_Toc233897861)

[2.2 角色 3](#_Toc233897862)

[2.3 所需组织单位 3](#_Toc233897863)

[2.4 必填和可选主数据 4](#_Toc233897864)

[3 概览表 5](#_Toc233897865)

[4 测试过程 6](#_Toc233897866)

[4.1 在采购中创建质量信息记录 6](#_Toc233897867)

[4.2 为没有质量信息记录的物料创建质量信息记录（可选） 7](#_Toc233897868)

[4.3 分配采购的质量管理控制代码 8](#_Toc233897869)

[4.4 创建 PPAP 的设置 9](#_Toc233897870)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

如果物料需要质量保证协议或供应商审批，则质量计划员必须创建质量信息 record（质量信息记录）。质量信息记录确定如何进一步处理物料。

创建采购订单时，系统会检查是否需要质量信息记录，以及是否可用于以下组合： 物料和供应商。

系统还会检查供应商和物料-供应商组合是否已针对报价、采购订单冻结或审批 和/或收货。此检查的执行取决于物料中采购控制代码的 QM 设置 master。

此外，您可以分配质量管理系统并相应地触发可能的检验。还可以确定收货 触发检验和/或源检验。还可以指示需要生产部件审批流程 (PPAP) 您可以在质量信息记录中为其计划首件检验 (FAI)。可在此处通过更新 PPAP 管理 PPAP 状态和评估代码（基于制定的使用决策）。此外，您可以一次将多个采购订单/项目 PPAP 分配到 执行首件检验 (FAI)。

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
| 质量计划员 | SAP_BR_QUALITY_PLANNER | 质量计划 | SAP_BR_QUALITY_PLANNER |  |

有关业务角色的详细信息，请参阅实施 的管理指南中的将业务角色分配给用户 SAP S/4HANA Cloud Public 版本 。

### 所需组织单位

客户主数据的一些段取决于 公司，常规（中央）数据不依赖于组织单位或公司 代码。下表提供了这些不同数据段及其 相关组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 质量信息记录 | 工厂 |  | 对于企业的每个工厂标识，都可以存在工厂数据 使用物料主记录的结构。 | 工厂： |

### 必填和可选主数据

质量管理数据记录可能参考其他主数据。下表提供了 要在质量信息中使用的可选和强制主数据对象的概览。 记录。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 物料主数据 |  | 必填 | 通过质量管理视图。有关详细信息，请参阅主数据 script, 创建物料/产品主数据的质量管理属性 - MDS (BNY)。 |
| 供应商主数据 |  | 必填 |  |

|  |
| --- |
| 备注 如果质量管理采购代码需要 供应商审批。在这种情况下，对于每个供应商-物料组合，质量 需要创建信息记录。 |

## 概览表

此范围项目由下列流程步骤组成： 表：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [在采购中创建质量信息记录](#unique_8) [第 ] 页 6 | 质量计划员 | 创建质量信息记录 - 采购 (QI01) | 已创建质量信息记录。 |
| [为没有质量信息记录的物料创建质量信息记录（可选）](#unique_9) [第 ] 页 7 | 质量计划员 | 管理质量信息记录 (F2256A) | 已创建质量信息记录。 |
| [分配采购的质量管理控制代码](#unique_10) [第 ] 页 8 | 质量计划员 | 分配采购的质量管理控制代码 - 手动处理 (QI05) | 已创建质量信息记录。 |
| [创建 PPAP 的设置](#unique_11) [第 ] 页 9 | 质量计划员 | 管理质量信息记录 (F2256A) | 已创建质量信息记录。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 在采购中创建质量信息记录

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 质量计划员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建质量信息记录 - 采购 (QI01) 。 | 因此， 创建质量信息记录 视图。 |  |
| 3 | 输入基本信息 | 输入以下内容：材料 ： <物料编号>供应商 ： <供应商代码>工厂 ： <工厂代码>选择 继续 。 |  |  |
| 4 | 输入审批数据 | 在 中 发布 部分，输入以下数据：下达至 ： 日期 未来，例如，在一年内可选：下达数量已激活 ：已标记下达数量 ：例如， 15 |  |  |
| 5 | 保存数据 | 选择 保存 。 | 您的数据已保存。 |  |

|  |
| --- |
| 备注 在质量信息记录中，您还可以决定是取消激活收货检验还是执行货物 收货检验和/或源检验。为此，请选择 检验控制 标签，并输入 以下数据：如果除收货检验外还想执行源检验，请输入 源检验和提前期（以天为单位）。如果不想执行收货检验，即使物料主数据中的设置指定了 检验，设置 无检验 标识。如果要执行源检验而不是收货检验，请设置相关标识。如果设置此标识，则在进行源检验时，系统不会为收货创建检验批次 已执行。如果未执行源检验，则为收货生成检验批次。在 下 检验控制 标签中，还可以输入以下内容：供应商的质量管理系统如果供应商具有质量管理系统，则可以在此处存储此特定物料的质量管理系统的描述。生产部件审批您可以指定需要生产部件审批流程。必须对此进行进一步设置，在 管理质量信息记录 (F2256A) 应用（请参阅章节[分配采购的质量管理控制代码](#unique_10) [第 ] 页 8）。 |

### 为没有质量信息记录的物料创建质量信息记录（可选）

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 质量计划员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理质量信息记录 (F2256A) 。 |  |  |
| 3 | 创建质量信息记录（可选） | 选择 创建 在结果表的右上角， 维护 抬头 级别：材料 ： 材料 号码供应商 ： 供应商 代码工厂 ： 工厂 代码对于 发布 部分，请参阅上一章，步骤 4。 |  |  |
| 4 | 保存数据 | 选择 创建 。 | 您的数据已保存，并创建了新的质量信息记录。 |  |

### 分配采购的质量管理控制代码

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 质量计划员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 分配采购的质量管理控制代码 - 手动处理 (QI05)。 |  |  |
| 3 | 分配质量管理控制代码 | 您可以在工厂和/或物料级别运行此选择。选择 要分配的 QM 控制代码。材料 ： 材料 号码工厂 ： 工厂 代码质量管理控制代码 ： 质量管理 控制密钥实施数据库更改 ： 已激活（如果未设置此标识， 仅执行测试运行）备注 仅那些物料，其中 激活采购中的 QM 标识在物料主数据中设置， 已选择。 |  |  |

### 创建 PPAP 的设置

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

前提条件

通过使用专用检验计划用途收货模型实现首件检验。 检验，分配到 中质量管理的以下控制代码 采购：

- 0001 供应商审批
- 9001 供应商审批（含错误消息）

具体来说，必须满足以下条件才能进行首件检验： 已执行：

- 首先存在使用收货模型检验 (51) 的检验计划 商品检验。
- 上面列出的质量管理控制代码之一已分配到物料。
- 对于此物料，存在具有以下设置的质量信息记录 下 生产部件审批 ：
    - 已启用生产部件审批以及 PPAP 级别和 PPAP 设置状态。
    - 至少输入一个采购订单和采购订单项目。

在采购订单项目收货时，为首件商品创建检验批次 检验。对于此检验批，质量管理控制代码的首件检验计划用途为 为检验类型维护的使用情况。

过程

在 中启用 PPAP 管理质量信息记录 (F2256A) 应用。在此，您可以 指定应在货物上进行首件检验的物料 一个或多个采购订单项目的收据。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 质量计划员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理质量信息记录 (F2256A) 。 |  |  |
| 3 | 创建质量信息记录 | 选择 创建 在结果表的右上角， 维护 抬头 级别：材料 ： 物料编号供应商 ： 供应商代码工厂 ： 工厂代码对于 发布 部分，请参阅之前的步骤 4 chapter。或者，选择要启用 PPAP 的现有质量信息记录。 |  |  |
| 4 | 输入生产部件审批数据 | 转到 生产部件审批 部分。选择 启用 。将相应的 PPAP 级别分配到 PPAP 级别 字段。 |  |  |
| 5 | 保存数据 | 选择 创建 。 | 您的数据已保存，并创建了新的质量信息记录。 |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-registro-info-de-calidad-mds-bf5-552]]
- related-to :: [[13-quality-ehs-and-compliance/create-quality-info-record-mds-bf5-551]]
- related-to :: [[13-quality-ehs-and-compliance/criar-registro-info-de-qualidade-mds-bf5-554]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-553]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 8,698 chars in the whole document
