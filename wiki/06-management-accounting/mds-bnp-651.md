---
id: 06-management-accounting/mds-bnp-651
title: 创建成本要素组 - MDS (BNP) (BNP_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script BNP: create a cost element group with Manage Cost Element Groups app F5373 as overhead cost accountant."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-element-groups]
aliases: [BNP_S4CLD2608_Master_Data_ZH_XX]
keywords: [Cost Element Groups, master data scripts, cost accounting, controlling area, chart of accounts, business role templates, report structures, fiori launchpad access, BNP]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-651
topic: 06-management-accounting/cost-element-groups
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建成本要素组 - MDS (BNP) (BNP_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Cost Element Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建成本要素组 - MDS (BNP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897959)

[2 前提条件 3](#_Toc233897960)

[2.1 系统访问 3](#_Toc233897961)

[2.2 角色 3](#_Toc233897962)

[2.3 所需组织单位 3](#_Toc233897963)

[2.4 必填和可选主数据 4](#_Toc233897964)

[2.5 数据创建的主要参数 4](#_Toc233897965)

[3 概览表 5](#_Toc233897966)

[4 测试过程 6](#_Toc233897967)

[4.1 创建成本要素组主数据 6](#_Toc233897968)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

业务上下文

成本要素组通常用于收集相似的成本要素。 特征。成本要素组可用于 信息系统。可将成本要素组结构用于 定义报表的行结构。在报表中计算以下项的总计： 每个节点。

无论何时要处理多个成本，都可以使用成本要素组 一个事务中的 个元素。例如，在成本中心计划、分配或 评估。

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
| 成本会计 - 间接费用 | SAP_BR_OVERHEAD_ACCOUNTANT | 间接费用会计 | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### 所需组织单位

在实施期间，已在 ERP 系统中创建公司的组织结构和主数据。组织结构反映贵公司的结构。根据公司的运营重点，主数据代表成本要素组。

| 数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 成本控制范围 | 常规数据 | 必填 |  |

### 必填和可选主数据

成本要素组主数据记录可能参考其他主数据。下表提供了要在成本要素组数据记录中使用的可选和必填主数据对象的概览。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 科目表 | 组织单位 | 可选 |  |

### 数据创建的主要参数

此范围项目没有业务条件。

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [创建成本要素组主数据](#unique_9) [第 ] 页 6 | 成本会计 - 间接费用 | 管理成本要素组 (F5373) | 可根据新的业务需求创建成本要素组。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建成本要素组主数据

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

前提条件

您已输入并保存物料的基本数据。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本要素组 (F5373) 。 | 应用随即打开。 |  |
| 3 | 输入新成本要素组 | 在 管理成本要素组 屏幕上，选择 创建 . 在 创建成本要素 组：初始屏幕 中，输入以下内容：成本要素组 ： <成本 元素组>按下 输入 。或者，您可以从现有成本中心中选择参考 组。 | 因此， 创建成本要素组：结构 屏幕 随即显示。 |  |
| 4 | 输入成本要素和/或成本要素组 | 新主数据显示在 成本要素组： 结构 屏幕中，输入以下内容：描述 ： <描述>此外，通过将光标置于选择上并使用以下导航按钮，您可以输入以下内容：较低级别 ： <插入成本 较低级别的元素组>成本要素 ： <（插入选项） - 添加成本要素或要素范围>相同级别 ： <插入其他 相同较低级别的成本要素组> | 新主数据显示在 成本要素组： 结构 屏幕。 |  |
| 5 | 保存数据 | 选择 保存 。 | 创建并保存成本要素组。 |  |

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
- related-to :: [[06-management-accounting/create-cost-element-group-mds-bnp-647]]
- related-to :: [[06-management-accounting/criar-grupo-de-classes-de-custo-mds-bnp-650]]
- related-to :: [[06-management-accounting/kostenartengruppe-anlegen-sds-bnp-646]]
- related-to :: [[06-management-accounting/mds-bnp-649]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 5,512 chars in the whole document
