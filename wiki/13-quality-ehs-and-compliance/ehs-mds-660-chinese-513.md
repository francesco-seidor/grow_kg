---
id: 13-quality-ehs-and-compliance/ehs-mds-660-chinese-513
title: 创建 EHS 产品 - MDS (660) (Chinese) (660_S4CLD2608_Master_Data_ZH_XX)
description: Chinese machine-translated master data script for creating an EHS product master record in SAP S/4HANA Cloud Public Edition via app F1602.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [660_S4CLD2608_Master_Data_ZH_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, master data scripts, ehs products, ehs waste management, business roles, 660]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-513
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建 EHS 产品 - MDS (660) (Chinese) (660_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建 EHS 产品 - MDS (660) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897829)

[2 前提条件 3](#_Toc233897830)

[2.1 系统访问 3](#_Toc233897831)

[2.2 角色 3](#_Toc233897832)

[3 概览表 4](#_Toc233897833)

[4 过程 5](#_Toc233897834)

[4.1 创建 EHS 产品主数据 - 常规数据 5](#_Toc233897835)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何为 S/4 HANA 系统创建 EHS 产品主数据记录的描述。该描述包括与主数据相关的数据段，以便在“常规”系统环境中工作。读取器主要学习哪些数据段和字段通常需要使用输入值填充。本文档不描述与 SAP Best Practices 的 S/4 HANA 内容交付范围无关的字段，尽管这些字段可能显示在 UI 上。

按此处描述创建的 EHS 产品主记录稍后可用于废弃物管理流程。

本文档提供了在解决方案激活后测试此范围项目的详细过程，反映了解决方案的预定义范围。每个流程步骤、报告或项目都包含在其自己的部分中，在表视图中提供系统交互（测试步骤）。不在流程范围内但测试所需的步骤会相应标记。必须添加项目特定的步骤。

|  |
| --- |
| 备注 此测试脚本中的值（十进制记数法、日期格式等）以美国标准表示法显示。如果将测试系统设置为使用其他表示法，则根据需要输入值。 |

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

| 名称 | 标识 |
| --- | --- |
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST |

## 概览表

此主记录由下表中提供的多个段组成。

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建 EHS 产品主数据 - 常规数据](#unique_6) [第 ] 页 5 | 主数据专家 - 产品数据 | 管理产品主数据 （ F1602 ) | 已创建 EHS 产品。 |

## 过程

本部分介绍作为此主记录一部分的每个段或流程步骤的过程。

### 创建 EHS 产品主数据 - 常规数据

目的

以下过程提供了创建 EHS 产品的说明，稍后可将其用于 EHS 废弃物管理流程。

过程（使用 Fiori 快速启动板）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 使用您的用户凭据登录到 SAP Fiori 快速启动板。 | 因此， 启动 页面。 |  |
| 2 | 导航到产品主数据 | 打开 管理产品主数据应用 （ F1602 ) | 因此， 管理产品主数据 应用，并显示清单报表。 |  |
| 3 | 创建产品 | 在 中 创建 对话框中，选择 产品 。 | 因此， 创建主数据记录 显示产品的 。 |  |
| 4 | 选择产品的主数据记录 | 在同一屏幕上：输入 <产品编号> （在 产品编号字段 。选择 <产品类型> （在 产品 类型 字段。选择 <产品组> （在 产品 分组 字段。输入 <描述> （在 描述 字段。选择 <基本单位> （通过 基本单位 字段。选择 确定 。 | 因此， 产品 包含主数据记录信息。 |  |
| 5 | 保存信息 | 选择 保存 。 | 因此， 产品 已创建。 |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-un-producto-ehs-mds-660-510]]
- related-to :: [[13-quality-ehs-and-compliance/criar-um-produto-ehs-mds-660-512]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-511]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-produkt-anlegen-sds-660-508]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 4,799 chars in the whole document
