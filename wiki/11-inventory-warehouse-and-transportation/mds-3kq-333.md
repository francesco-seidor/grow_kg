---
id: 11-inventory-warehouse-and-transportation/mds-3kq-333
title: 维护仓库产品属性 - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_ZH_XX)
description: Chinese (machine-translated) master data script 3KQ for maintaining warehouse product attributes via Warehouse Monitor (/SCWM/MON) or Manage Product Master Data
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-product-attributes]
aliases: [3KQ_S4CLD2608_Master_Data_ZH_XX]
keywords: [EWM Warehouse Product Attributes, warehouse product attributes, warehouse monitor, master data script, product master data, replenishment, business roles, extended warehouse management, 3KQ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-333
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-product-attributes
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 维护仓库产品属性 - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Product Attributes** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 维护仓库产品属性 - MDS (3KQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897534)

[2 前提条件 3](#_Toc233897535)

[2.1 系统访问 3](#_Toc233897536)

[2.2 角色 3](#_Toc233897537)

[2.3 所需组织单位 3](#_Toc233897538)

[2.4 必填和可选主数据 4](#_Toc233897539)

[3 概览表 5](#_Toc233897540)

[4 测试过程 6](#_Toc233897541)

[4.1 维护仓库产品属性 - 使用仓库监控器 6](#_Toc233897542)

[4.2 维护仓库产品属性 7](#_Toc233897543)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将了解如何为物料/产品主数据创建仓库相关属性。有两个选项可用于维护仓库属性：

- 您可以通过以下路径维护仓库产品属性： 仓库监控器 (/SCWM/MON) 应用。此应用可用于单个更改和批量更改。
- 您可以通过以下路径维护仓库产品属性： 管理产品主数据 (F1602) 应用。此应用可用于单个更改。

本文档包括与主数据相关的数据段，以便在常规系统环境中工作。读取器主要学习哪些数据段和字段通常需要使用输入值填充。本文档不描述与 SAP Best Practices 的 SAP S/4HANA 内容交付范围无关的字段，即使这些字段可能显示在 UI 上。

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
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST | 主数据 - 产品 / 产品治理 | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### 所需组织单位

主数据的某些段取决于公司的组织单位。 常规（中央）数据不取决于组织单位或公司代码。因此， 下表提供了这些不同数据段及其相关 组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有 | 仓库编号 |  |  |  |

### 必填和可选主数据

主数据记录可能 参考其他主数据 。下表提供了要在 <类型> 主数据记录中使用的可选和强制主数据对象的概览。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 业务伙伴 | 维护仓库产品属性 | 必填 | 业务伙伴，作为仓库的授权处置方 |

## 概览表

此主记录由下表中提供的多个段组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [维护仓库产品属性 - 使用仓库监控器](#unique_7) [第 ] 页 6 | 仓库职员 (EWM) | 仓库监控器 (/SCWM/MON) | 执行仓库产品的批量更改。 |
| [维护仓库产品属性](#unique_8) [第 ] 页 7 | 主数据专家 - 产品数据 | 管理产品主数据 (F1602) | 已创建物料主数据的仓库属性。 |

## 测试过程

本部分介绍作为此主记录一部分的每个段或流程步骤的过程。

### 维护仓库产品属性 - 使用仓库监控器

目的

在本部分中，使用 仓库监控器 (/SCWM/MON) 应用。此应用可用于单个更改和批量更改。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板作为 仓库职员 (EWM) 。 |  |  |
| 2 | 访问应用 | 打开 仓库监控器 (/SCWM/MON) 。 | 因此， 仓库管理监控器 SAP - 仓库编号 XX50 屏幕。 |  |
| 3 | 选择菜单 | 在屏幕左侧区域的层次结构中，选择 产品主数据 > 仓库属性 。 |  |  |
| 4 | 输入产品编号 | 在 中 /SCWM/SAPLPROD_OVERVIEW 对话框中，输入以下数据：基本属性 部分：产品编号 ： <产品编号> 收件人 <产品编号>附加选项 部分：仅无仓库数据的产品 ： X选择 执行 。 | 在屏幕右侧区域中，系统显示尚未使用仓库数据维护的产品。 |  |
| 5 | 选择产品 | 在 中 仓库属性 区域，选择产品，然后选择 更多方法 > 批量更改/创建 。 |  |  |
| 6 | 选择产品 | 在 中 /SCWM/SAPLPROD_OVERVIEW 对话框中，输入以下数据（如果适用）。在 中 仓库数据 部分：入库控制标识出库控制标识散装存储标识周期盘点标识处理类型确定标识选择 执行 。备注 在云仓库管理中，通常使用相同的值维护入库控制标识和出库控制标识。但是，在仓库中使用的补货流程中，必须以不同方式维护这两个字段以启用该流程。 |  |  |
| 7 | 保存数据 | 在对话框中，确认更改。 | 系统会显示一条消息，提示您已成功保存产品。 |  |

### 维护仓库产品属性

目的

在本部分中，您将找到有关如何维护仓库产品属性的描述 通过 管理产品主数据 (F1602) 应用。可使用此应用 用于单个更改。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板作为 主数据专家 - 产品数据 。 |  |  |
| 2 | 访问应用 | 打开 管理产品主数据 (F1602) 。 |  |  |
| 3 | 输入物料编号 | 在 管理产品主数据 (F1602) 屏幕上，输入以下数据：产品 ： <物料编号>选择 执行 。 | 物料主数据显示在 产品 部分。 |  |
| 4 | 选择物料 | 选择物料主数据所在的行。 |  |  |
| 5 | 选择仓库管理 | 在 产品 屏幕上，选择 仓库 管理 选项卡并转到 仓库管理 > 仓库 。 |  |  |
| 6 | 编辑物料主数据 | 在 产品 屏幕上，选择 编辑 。 |  |  |
| 7 | 添加仓库数据 | 在 中 仓库 部分，选择仓库 仓库编号。如果仓库编号不存在，则选择 创建 。 |  |  |
| 8 | 输入值 | 在 仓库 屏幕上，输入以下内容 数据：在 中 基本信息 部分：仓库 ： <EWM 仓库 编号>授权处置方 ： <业务 授权处理方的合作伙伴标识>流程类型确定标识周期盘点标识备注 仅限 仓库 以及 授权方 处置 是输入的必填项。以下值 是可选的。在 中 入库 部分：入库控制标识在 中 下架 部分：下架控制标识备注 在云仓库管理中，入库控制标识和 使用相同的值维护库存出库控制标识。 但是，在仓库中使用的补货流程中， 字段的维护方式必须不同，以启用该流程。 |  |  |
|  | 创建补货的存储类型数据 | 在 中 存储类型 部分，选择 创建 。在 新记录 - 存储类型 屏幕上，输入 以下数据：在 中 基本信息 部分：存储类型 ： <存储 类型>最大仓位数 ： <数量 仓位>在 中 补货 部分：最小补货数量/显示计量单位 ： <数量>/<计量单位>最小数量/显示计量单位 ： <数量>/<计量单位>最大数量/显示计量单位 ： <数量>/<计量单位> |  |  |
| 9 | 保存数据 | 选择 应用 。 | 仓库数据已保存。 |  |
| 10 | 返回到产品屏幕 | 返回到 产品 屏幕。 |  |  |
| 11 | 选择仓库管理 | 在 产品 屏幕上，选择 工厂 标签。 |  |  |
| 12 | 添加工厂数据 | 在 中 工厂 部分中，选择工厂。如果您的工厂不存在，请选择 创建 。 |  |  |
| 13 | 输入值 | 在 工厂 屏幕上，在常规信息部分输入以下数据：序列号参数文件：<序列号参数文件> |  |  |
| 14 | 保存数据 | 选择 应用 。 | 保存工厂数据。 |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/actualizar-atributos-de-productos-de-almacen-mds-3kq-es-330]]
- related-to :: [[11-inventory-warehouse-and-transportation/attribute-fur-lagerprodukte-pflegen-sds-3kq-328]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-maintain-warehouse-products-attributes-3kq-329]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-331]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 7,085 chars in the whole document
