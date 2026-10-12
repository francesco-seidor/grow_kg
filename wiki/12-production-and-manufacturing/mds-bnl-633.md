---
id: 12-production-and-manufacturing/mds-bnl-633
title: 创建工艺路线 - MDS (BNL) (BNL_S4CLD2608_Master_Data_ZH_XX)
description: 主数据脚本（中文机器翻译）：通过管理工艺路线 (F5425) 为成品/半成品创建生产工艺路线，含工序、组件分配。
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BNL_S4CLD2608_Master_Data_ZH_XX]
keywords: [Routings and Reference Operation Sets, production routing, routing operations, work center usage, control keys, external processing, component assignment, master data prerequisites, business roles, BNL]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-633
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建工艺路线 - MDS (BNL) (BNL_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建工艺路线 - MDS (BNL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897939)

[2 前提条件 3](#_Toc233897940)

[2.1 系统访问 3](#_Toc233897941)

[2.2 角色 3](#_Toc233897942)

[2.3 所需组织单位 3](#_Toc233897943)

[2.4 必填和可选主数据 4](#_Toc233897944)

[2.5 数据创建的主要参数 4](#_Toc233897945)

[2.5.1 用法 4](#_Toc233897946)

[3 概览表 6](#_Toc233897947)

[4 测试过程 7](#_Toc233897948)

[4.1 创建工艺路线 7](#_Toc233897949)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

生产工艺路线定义物料的生产流程。它包含 生产期间要执行的工序或工作步骤。它定义了 物料和工作中心。它构成了生产订单的模板，并且是基础 用于产品成本核算。

工艺路线是针对成品或半成品定义的，并且特定于 生产站点（称为工厂）。它适用于给定批量，包括 每个工序都分配到工作中心的工序数量。

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
| 生产工程师 - 离散制造 | SAP_BR_PRODN_ENG_DISC | 生产工程 - 离散制造 | SAP_BR_PRODN_ENG_DISC |  |

### 所需组织单位

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有数据 | 工厂 |  | 工艺路线的所有数据取决于工厂。 | 工厂：__________ |

### 必填和可选主数据

工艺路线数据记录可能参考其他主数据。下表提供了 要在工艺路线中使用的可选和强制主数据对象的概览。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 材料 |  | 必填 | 在执行之前，完成以下测试脚本作为前提条件 流程步骤：创建“原材料”类型的产品主数据 - MDS (BNR)创建“半成品”类型的产品主数据 - MDS （BNS）创建“成品”类型的产品主数据 - MDS （BNT） |
| 工作中心 | 位于 创建工艺路线：工序概览 屏幕， 选择内部工序的工作中心 | 必填（可选） | 对于外部工序，工作中心不是强制输入 field。如果需要，请执行 创建工艺路线 - MDS (BNL) 测试脚本。 |
| 物料清单 |  | 可选 | 执行 创建生产和销售物料清单 - MDS (BNK) 测试脚本。 |
| 采购信息记录 |  | （必需） | 对于外部工序，您可以使用采购信息记录 捕获所有供应相关数据 |
| 物料组 |  |  |  |
| 成本要素 |  |  |  |

### 数据创建的主要参数

在本部分中，我们将介绍一些影响主记录行为的基本参数，并且始终需要这些参数来创建工艺路线：

#### 用法

| 工作中心类别 | 描述 |
| --- | --- |
| 1 | 生产 |
| 2 | 工程/设计 |
| 3 | 通用 |

## 概览表

此范围项目由下表中列出的流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建工艺路线](#unique_10) [第 ] 页 7 | 生产工程师 - 离散制造 | 管理工艺路线 (F5425) |  |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建工艺路线

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理工艺路线 (F5425) 。 | 应用随即打开。 |  |
| 3 | 选择创建 | 选择 创建 。 | 随即打开一个新窗口，显示 创建工艺路线 屏幕。 |  |
| 4 | 设置创建工艺路线屏幕 | 输入以下数据： 创建工艺路线 屏幕：材料 ： <成品/半成品物料 编号>工厂 ： <您的工厂编号>选择 继续 。 | 因此， 创建工艺路线：抬头详细信息 屏幕。 |  |
| 5 | 设置创建工艺路线：抬头详细信息屏幕 | 输入以下数据： 创建工艺路线：抬头详细信息 屏幕：用法 ： <1 用于生产>状态 ： <4 已发布 - 常规>从批量到批量 ： <输入批量间隔和计量单位> |  |  |
| 6 | 设置创建工艺路线：工序概览屏幕 | 选择 操作 以及 创建工艺路线：工序概览屏幕 随即显示。输入以下数据： 创建工艺路线：工序概览屏幕 ：工作中心 ： 内部工序需要（空白）用于外部工序控制代码 ： <YBP1/YBP2/YBP3/YBP5>无自动收货的内部操作的 YBP1YBP2 用于外部工序（PP 转包）YBP3 用于含自动收货的内部操作YBP4 用于流程制造里程碑描述 ： <输入 操作描述>然后双击您输入的工序。 |  |  |
| 7 | 外部处理部分的外部工序设置 | 输入以下数据： 创建工艺路线：工序详细信息 屏幕：采购信息记录 ： 必需 用于内部操作，（空白）用于外部 运营物料组 ： L002/L003成本要素 ： <您所在国家/地区的相关成本要素>采购组织 ： <采购组织> 。 |  |  |
| 8 | 标准值部分的内部工序设置 | 输入以下数据： 创建工艺路线工序详细信息 屏幕：设置 ： <设置时间>机器 ： <机器操作时间>人工 ： <工时> |  |  |
| 9 | 添加更多操作 | 对每个操作重复上述步骤。 |  |  |
| 10 | 选择组件 | 选择 组件分配 然后选择组件。 | 因此， 物料组件概览 视图。 |  |
| 11 | 创建新分配 | 选择 新分配 。 | A 新建分配 对话框。 |  |
| 12 | 分配到工序/活动清单 | 选择 工序/活动清单 。 |  |  |
| 13 | 选择工序 | 选择工序并按 输入 。 |  |  |
| 14 | 分配其他组件 | 对其他组件重复上述步骤。 |  |  |
| 15 | 保存数据 | 保存输入内容。 | 已创建工艺路线。 |  |

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
> Flagged while digesting this document, not verified: 控制代码说明中 YBP5 在列表中出现而说明列出 YBP4，疑似内部不一致

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/arbeitsplan-anlegen-sds-bnl-628]]
- related-to :: [[12-production-and-manufacturing/creacion-de-hoja-de-ruta-mds-bnl-630]]
- related-to :: [[12-production-and-manufacturing/criar-roteiro-mds-bnl-632]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-routing-mds-bnl-629]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 6,535 chars in the whole document
