---
id: 11-inventory-warehouse-and-transportation/mds-3ks-345
title: 维护生产供应区 - MDS (3KS) (3KS_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script 3KS for optionally assigning bins to production supply areas (PSA) in warehouse management, with prerequisite sc"
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [3KS_S4CLD2608_Master_Data_ZH_XX]
keywords: [EWM Production Supply and Receipt, production supply areas, bin assignment, master data script, production integration, kanban supply, business roles, extended warehouse management, 3KS]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-345
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 维护生产供应区 - MDS (3KS) (3KS_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 维护生产供应区 - MDS (3KS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897541)

[2 前提条件 3](#_Toc233897542)

[2.1 系统访问 3](#_Toc233897543)

[2.2 角色 3](#_Toc233897544)

[2.3 所需组织单位 3](#_Toc233897545)

[2.4 必填和可选主数据 4](#_Toc233897546)

[2.5 业务条件 4](#_Toc233897547)

[3 概览表 6](#_Toc233897548)

[4 测试过程 7](#_Toc233897549)

[4.1 （可选）将仓位分配到 PSA - 仓库 7](#_Toc233897550)

[4.2 （可选）将仓位分配到 PSA 8](#_Toc233897551)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将了解如何执行以下活动来创建仓库 生产供应的主数据：

- [（可选）将仓位分配到 PSA - 仓库](#unique_2) [第 ] 页 7
- [（可选）将仓位分配到 PSA](#unique_3) [第 ] 页 8

生产供应区的创建和复制，以及到 PSA 的仓位分配应该通过执行 主数据脚本中的相关步骤或 中提及的测试脚本文档 业务条件 章节。此主数据 脚本仅用于客户检查相关设置，并在未满足业务条件时手动创建设置。

该描述包括与主数据相关的数据段，以便在常规系统环境中工作。你主要了解 通常需要使用输入值填充哪些数据段和字段。与 SAP S/4HANA 范围无关的字段 SAP Best Practices 提供的内容不会在本文档中描述，即使它们可能出现在 UI 上。

将此主数据用于仓库管理中的生产集成业务流程。

## 前提条件

### 系统访问

| 系统 | 明细 |
| --- | --- |
| 系统 | 可通过 SAP Fiori 快速启动板访问。系统管理员为您提供 用于访问分配给您的角色的各种应用的 URL。 |

### 角色

使用 SAP 提供的以下业务角色模板创建业务角色，并将其分配给各个测试用户。

或者，如果可用，您可以使用 SAP 提供的以下空间。创建包含预定义基本应用的页面的空间，并将其分配到业务角色。然后将此业务角色分配给单个用户。

有关详细信息，请参阅 如何从模板创建业务角色 （在[产品帮助](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) 对于 SAP S/4HANA Cloud Public 版本 。

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） |
| --- | --- | --- | --- |
| 仓库职员 (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | 仓库办公室 | SAP_BR_WAREHOUSE_CLERK_EWM |

### 所需组织单位

主数据的某些段取决于公司的组织单位。常规（中央）数据不取决于 组织单位或公司代码。下表提供了这些不同数据段及其相关段的概览。 组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有 | 仓库编号 |  |  |  |

### 必填和可选主数据

主数据记录可能 参考其他主数据 。下表提供了可选和必需主数据的概览。 创建到 PSA 主数据记录的仓位分配时要使用的数据对象。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 业务伙伴 | 将仓位分配到 PSA - 仓库 | 必填 | 业务伙伴作为仓库的授权处置方。 |
| 生产供应区 | 将仓位分配到 PSA - 仓库 | 必填 | 在 SAP S/4HANA 中创建的生产供应区。请参阅业务条件章节。 |
| 产品 | 将仓位分配到 PSA - 仓库 | 必填 |  |
| 仓位 | 将仓位分配到 PSA - 仓库 | 必填 |  |

### 业务条件

在测试此范围项目之前，必须满足以下业务条件。

| 范围项目标识 | 业务条件 |
| --- | --- |
| 40D - 创建生产供应区 - MDS | 此主数据脚本是此文档的前提条件。创建生产供应区 (PSA) 时，使用云 WM 存储地点，例如 105W 。执行此主数据脚本后，已创建以下设置：在 SAP S/4HANA 中创建生产供应区。相关生产供应区自动从 SAP S/4HANA 复制到云 仓库。 |
| 3DV - 仓库生产集成 | 本文档的前提条件是 3DV 测试的“预备步骤”章节中的“创建控制周期”步骤 script。执行创建控制周期步骤后，已创建以下设置：相关生产供应区会自动从 SAP S/4HANA 复制到云仓库。仓位已分配到 PSA。 |
| 3VT - 到生产的仓库看板供应 | 本文档的前提条件是 3VT 测试的“预备步骤”章节中的“看板的控制周期：库存转储”步骤 script。执行看板的控制周期：库存转储步骤后，已创建以下内容 设置：相关生产供应区会自动从 SAP S/4HANA 复制到云仓库。仓位已分配到 PSA。 |

## 概览表

此主记录由下表中提供的多个段组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [（可选）将仓位分配到 PSA - 仓库](#unique_2) [第 ] 页 7 | 仓库职员 (EWM) | 将仓位分配到 PSA - 仓库 (/SCWM/PSASTAGE) | 创建仓位到 PSA 的分配。 |
| [（可选）将仓位分配到 PSA](#unique_3) [第 ] 页 8 | 仓库职员 (EWM) | 将仓位分配到 PSA (/SCWM/PSASTAGE2) | 创建仓位到 PSA 的分配。 |

## 测试过程

本部分介绍作为此主记录一部分的每个段或流程步骤的过程。

### （可选）将仓位分配到 PSA - 仓库

目的

在此部分中，您可以使用 SAP Fiori 快速启动板管理 SAP S/4HANA 中仓库编号的所有生产供应区的仓位分配。

此步骤是可选的，如果已按预期将仓位分配到 PSA，则可以跳过此步骤。仅当在控制周期创建步骤期间尚未完成 PSA 的仓位分配时才需要。请参阅“业务条件”章节中的“创建控制周期”步骤。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板作为 仓库职员 (EWM) 。 |  |  |
| 2 | 访问应用 | 打开 将仓位分配到 PSA - 仓库 (/SCWM/PSASTAGE) 。 |  |  |
| 3 | 创建新条目 | 在 更改视图“将仓位分配到 PSA”：概览 屏幕上，选择 新条目 。 |  |  |
| 4 | 输入分配值 | 在 新条目：已添加条目的详细信息 屏幕上，输入以下数据：处置 ： <授权处置方的业务伙伴标识>供应区域 ： <生产供应区>产品 ： <产品标识>仓位 ： <仓位标识> |  |  |
| 5 | 保存数据 | 选择 保存 。 | 系统会显示一条消息，告知您已保存仓位到 PSA 的分配。 |  |

### （可选）将仓位分配到 PSA

目的

在此部分中，您可以使用 SAP Fiori 快速启动板管理 SAP S/4HANA 中特定生产供应区内的所有仓位分配。

此步骤是可选的，如果已按预期将仓位分配到 PSA，则可以跳过此步骤。仅当在控制周期创建步骤期间尚未完成 PSA 的仓位分配时才需要。请参阅“业务条件”章节中的“创建控制周期”步骤。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板作为 仓库职员 (EWM) 。 |  |  |
| 2 | 访问应用 | 打开 将仓位分配到 PSA (/SCWM/PSASTAGE2) 。 |  |  |
| 3 | 确定工作区 | 在 确定工作范围条目 屏幕上，输入以下数据：授权处置方 ： <授权处置方的业务伙伴标识>供应区域 ： <生产供应区>选择 继续 。 |  |  |
| 4 | 创建新条目 | 在 更改视图“将仓位分配到 PSA”：概览 屏幕上，选择 新条目 。 |  |  |
| 5 | 输入分配值 | 在 新条目：已添加条目的详细信息 屏幕上，输入以下数据：产品 ： <产品标识>仓位 ： <仓位标识> |  |  |
| 6 | 保存数据 | 选择 保存 。 | 系统会显示一条消息，告知您已保存仓位到 PSA 的分配。 |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/produktionsversorgungsbereich-pflegen-sds-3ks-340]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 6,922 chars in the whole document
