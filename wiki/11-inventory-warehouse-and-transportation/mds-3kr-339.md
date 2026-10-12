---
id: 11-inventory-warehouse-and-transportation/mds-3kr-339
title: 维护仓位和固定仓位分配 - MDS (3KR) (3KR_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script 3KR: create, change, display, mass-change storage bins and assign fixed bins in EWM, S/4HANA Cloud Public Edition 2608."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-storage-bins]
aliases: [3KR_S4CLD2608_Master_Data_ZH_XX]
keywords: [EWM Storage Bins and Fixed Bin Assignments, storage bins, fixed bin assignment, bin mass change, warehouse master data, business roles, business partners, machine translation, 3KR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-339
topic: 11-inventory-warehouse-and-transportation/ewm-storage-bins
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 维护仓位和固定仓位分配 - MDS (3KR) (3KR_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **EWM Storage Bins and Fixed Bin Assignments** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 维护仓位和固定仓位分配 - MDS (3KR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897545)

[2 前提条件 3](#_Toc233897546)

[2.1 系统访问 3](#_Toc233897547)

[2.2 角色 3](#_Toc233897548)

[2.3 所需组织单位 3](#_Toc233897549)

[2.4 必填和可选主数据 4](#_Toc233897550)

[3 概览表 5](#_Toc233897551)

[4 测试过程 6](#_Toc233897552)

[4.1 创建仓位 6](#_Toc233897553)

[4.2 更改仓位 7](#_Toc233897554)

[4.3 显示仓位 8](#_Toc233897555)

[4.4 对仓位执行批量更改 9](#_Toc233897556)

[4.5 分配固定仓位 10](#_Toc233897557)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将了解如何执行以下活动来创建仓库 仓位和固定仓位分配：

- [创建仓位](#unique_2) [第 ] 页 6
- [更改仓位](#unique_3) [第 ] 页 7
- [显示仓位](#unique_4) [第 ] 页 8
- [对仓位执行批量更改](#unique_5) [第 ] 页 9
- [分配固定仓位](#unique_6) [第 ] 页 10

该描述包括与主数据相关的数据段，以便在常规系统环境中工作。你主要了解 通常需要使用输入值填充哪些数据段和字段。与 SAP S/4HANA 范围无关的字段 SAP Best Practices 提供的内容不会在本文档中描述，即使它们可能显示在屏幕上。

您可以将此主数据用于所有仓库管理业务流程。

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

主数据的某些段取决于公司的组织单位。 常规（中央）数据不取决于组织单位或公司代码。因此， 下表提供了这些不同数据段及其相关 组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有 | 仓库编号 |  |  |  |

### 必填和可选主数据

主数据记录可能 参考其他主数据 。下表提供了要在 <类型> 主数据记录中使用的可选和强制主数据对象的概览。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 业务伙伴 | 分配固定仓位 | 必填 | 业务伙伴，作为仓库的授权处置方 |

## 概览表

此主记录由下表中提供的多个段组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建仓位](#unique_2) [第 ] 页 6 | 仓库职员 (EWM) | 创建仓位 (/SCWM/LS01) | 已创建仓位。 |
| [更改仓位](#unique_3) [第 ] 页 7 | 仓库职员 (EWM) | 编辑仓位 (/SCWM/LS02) | 仓位已更改。 |
| [显示仓位](#unique_4) [第 ] 页 8 | 仓库职员 (EWM) | 显示仓位 (/SCWM/LS03) | 显示仓位。 |
| [对仓位执行批量更改](#unique_5) [第 ] 页 9 | 仓库职员 (EWM) | 批量编辑仓位 (/SCWM/LS11) | 对仓位进行批量更改。 |
| [分配固定仓位](#unique_6) [第 ] 页 10 | 仓库职员 (EWM) | 分配固定仓位 (/SCWM/BINMAT) | 已创建固定仓位分配。 |

## 测试过程

本部分介绍作为此主记录一部分的每个段或流程步骤的过程。

### 创建仓位

目的

在本部分中，您将找到有关如何使用 SAP Fiori 快速启动板在 SAP S/4HANA 中创建仓位的描述。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板作为 仓库职员 (EWM) 。 |  |  |
| 2 | 访问应用 | 打开 创建仓位 (/SCWM/LS01) 。 |  |  |
| 3 | 输入仓位标识 | 在 创建仓位 (/SCWM/LS01) 屏幕上，输入以下数据：仓库编号 ： <您的仓库编号>仓位 ： <仓位标识>选择 输入 。 |  |  |
| 4 | 输入仓位属性 | 在 仓位 标签上，输入以下数据：存储类型 ： <存储类型>备注 仅 存储类型 字段必填。以下所有其他字段均为可选字段：最大重量最大体积仓位过道X 坐标堆栈Y 坐标仓位级别Z 坐标仓位角度 |  |  |
| 5 | 保存数据 | 选择 保存 。 | 系统会显示一条消息，提示您已保存仓位。 |  |

### 更改仓位

目的

在此部分中，使用 SAP Fiori 快速启动板更改 SAP S/4HANA 中的仓位。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板作为 仓库职员 (EWM) 。 |  |  |
| 2 | 访问应用 | 打开 编辑仓位 (/SCWM/LS02) 。 |  |  |
| 3 | 输入仓位标识 | 在 编辑仓位 (/SCWM/LS02) 屏幕上，输入以下数据：仓库编号 ： <您的仓库编号>仓位 ： <仓位标识>选择 输入 。 |  |  |
| 4 | 更改仓位属性 | 在 仓位 标签上，根据需要更改以下值。备注 只能更改以下字段：最大重量最大体积仓位过道X 坐标堆栈Y 坐标仓位级别Z 坐标仓位角度 |  |  |
| 5 | 保存数据 | 选择 保存 。 | 系统会显示一条消息，提示您已保存仓位。 |  |

### 显示仓位

目的

在此部分中，使用 SAP Fiori 快速启动板显示 SAP S/4HANA 中的仓位。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板 作为 仓库职员 (EWM) 。 |  |  |
| 2 | 访问应用 | 打开 显示仓位 (/SCWM/LS03) 。 |  |  |
| 3 | 输入仓位标识 | 在 显示仓位 (/SCWM/LS03) 屏幕上，输入以下数据：仓库编号 ： <您的仓库编号>仓位 ： <仓位标识>选择 输入 。 | 显示仓位属性。 |  |

### 对仓位执行批量更改

目的

在此部分中，使用 SAP Fiori 快速启动板对 SAP S/4HANA 中的仓位进行批量更改。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板作为 仓库职员 (EWM) 。 |  |  |
| 2 | 访问应用 | 打开 批量编辑仓位 (/SCWM/LS11) 。 |  |  |
| 3 | 输入过滤条件 | 在 仓库编号 XXXX 中仓位的批量更改 屏幕上，输入以下数据：仓库编号 ： <您的仓库编号>可输入以下值作为选择/过滤条件：仓位 ： <仓位标识> 收件人 <仓位标识>存储类型 ： <存储类型标识> 收件人 <存储类型标识>已冻结状态备注 如果选择 动态选择 复选框，可以为仓位选择选择多个过滤器。选择 执行 。 | 显示符合选择条件的仓位清单。 |  |
| 4 | 批量更改仓位 | 通过选中相应复选框来选择所选条目。选择 删除 可一次删除多个仓位。或者选择 编辑 可同时更改多个仓位。您将能够更改仓位的以下属性。最大重量最大体积仓位过道堆栈仓位级别仓位角度 |  |  |
| 5 | 保存数据 | 选择 保存 。 | 系统会显示一条消息，告知您已保存仓位的更改。 |  |

### 分配固定仓位

目的

在此部分中，使用 SAP Fiori 快速启动板在 SAP S/4HANA 中进行固定仓位分配。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板作为 仓库职员 (EWM) 。 |  |  |
| 2 | 访问应用 | 打开 分配固定仓位 (/SCWM/BINMAT) 。 |  |  |
| 3 | 输入过滤条件 | 在 维护固定仓位 屏幕上，输入以下数据：仓库编号 ： <您的仓库编号>产品 ： <产品标识> 收件人 <产品标识>授权处置方 ： <业务伙伴标识> 收件人 <业务伙伴标识>备注 授权处置方是为仓库编号维护的业务伙伴。仓位 ： <仓位标识> 收件人 <仓位标识>存储类型 ： <存储类型标识> 收件人 <存储类型标识>选择 执行 。 | 显示符合选择条件的已分配固定仓位的清单。 |  |
| 4 | 创建固定仓位分配 | 在 仓库编号 XXXX：显示固定仓位 屏幕上，选择 编辑 。在 仓库编号 XXXX：维护固定仓位 屏幕上，选择 创建 。在新创建的行中，输入以下值：处置 ： <授权处置方的业务伙伴标识>仓位 ： <固定仓位标识>类型 ： <固定仓位存储类型标识>产品 ： <产品标识>最大数量 ： <数量>显示计量单位 ： <最大数量的计量单位> 例如，PC最小数量 ： <数量>显示计量单位 ： <最小数量的计量单位> 例如，PC如果已在仓库产品主数据中维护以下字段的值：最大仓位数最大数量最小数量显示计量单位 针对最大值/最小数量因此， 最大数量 以及 最小数量 将根据 的值计算固定仓位分配中的值 最大数量 ， 最小数量 以及 最大仓位数 在仓库产品主数据中。因此， 显示计量单位 也通过仓库产品主数据填充。 |  |  |
| 5 | 保存数据 | 选择 保存 。 | 系统会显示一条消息，提示您已保存仓位。 |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-storage-bins-and-fixed-bin-assignments-mds-3kr-335]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-337]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-posicoes-no-deposito-e-atribuicoes-de]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-actualizar-ubicaciones-y-asignaciones-de-ubic]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 7,988 chars in the whole document
