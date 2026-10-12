---
id: 13-quality-ehs-and-compliance/ehs-mds-65z-chinese-507
title: 创建 EHS 化学品合规性信息材料 - MDS (65Z) (Chinese) (65Z_S4CLD2608_Master_Data_ZH_XX)
description: Chinese machine-translated master data script for creating an EHS Chemical Compliance Information (CCI) material in SAP S/4HANA Cloud Public Edition via app F4864.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [65Z_S4CLD2608_Master_Data_ZH_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, master data scripts, ehs cci items, ehs waste management, business roles, 65Z]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-507
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建 EHS 化学品合规性信息材料 - MDS (65Z) (Chinese) (65Z_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建 EHS 化学品合规性信息材料 - MDS (65Z) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897748)

[2 前提条件 3](#_Toc233897749)

[2.1 系统访问 3](#_Toc233897750)

[2.2 角色 3](#_Toc233897751)

[3 概览表 4](#_Toc233897752)

[4 过程 5](#_Toc233897753)

[4.1 创建 EHS 化学品合规性信息物料主数据 - 常规数据 5](#_Toc233897754)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何为 S/4 HANA 系统创建 EHS 化学品合规性信息物料主数据记录的描述。该描述包括与主数据相关的数据段，以便在“常规”系统环境中工作。读取器主要学习哪些数据段和字段通常需要使用输入值填充。本文档不描述与 SAP Best Practices 的 S/4 HANA 内容交付范围无关的字段，尽管这些字段可能显示在 UI 上。

按此处描述创建的 EHS 化学品合规性信息物料主记录稍后可用于废弃物管理流程。

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

| 名称（角色模板） | ID（角色模板） |
| --- | --- |
| 环境经理 | SAP_BR_EHS_ENV_MGMT |

## 概览表

此主记录由下表中提供的多个段组成。

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建 EHS 化学品合规性信息物料主数据 - 常规数据](#unique_6) [第 ] 页 5 | 环境经理 | 管理物料数据 （ F4864 ) | 已创建 EHS 化学品合规性信息 (CCI) 物料。 |

## 过程

本部分介绍作为此主记录一部分的每个段或流程步骤的过程。

### 创建 EHS 化学品合规性信息物料主数据 - 常规数据

目的

以下过程提供了创建 EHS 化学品合规性信息物料的说明，稍后可将其用于 EHS 废弃物管理流程。

过程（使用 Fiori 快速启动板）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 使用您的用户凭据登录到 SAP Fiori 快速启动板。 | 因此， 启动 页面。 |  |
| 2 | 打开管理客户主数据 | 打开 管理物料数据 应用（ F4864 ）。 | 因此， 管理物料数据 应用，并显示清单报表。 |  |
| 3 | 创建新物料 | 选择 创建 。在屏幕上：输入 <名称> （在 内部名称 字段。选择 <物流角色> （来自 物流角色 下拉列表。选择 保存 。 | 因此， 新物料 标签，并创建新物料。 |  |
| 4 | 添加产品 | 选择 编辑 。在 中 产品 部分，选择 添加 选择一个产品。选择 保存 。注释：只能将一个产品分配到物料。 | 产品将添加到物料并保存信息。 |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-un-material-de-informacion-de-conformidad-de-producto-quimico-eh]]
- related-to :: [[13-quality-ehs-and-compliance/create-an-ehs-chemical-compliance-information-material-mds-65z-503]]
- related-to :: [[13-quality-ehs-and-compliance/criar-um-material-de-informacoes-de-conformidade-quimica-ehs-mds-65z-5]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-japanese-505]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 4,586 chars in the whole document
