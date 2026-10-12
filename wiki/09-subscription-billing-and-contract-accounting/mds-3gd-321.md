---
id: 09-subscription-billing-and-contract-accounting/mds-3gd-321
title: 创建基于服务类型的定价条件 - MDS (3GD) (3GD_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script 3GD for creating service-type-based pricing conditions PST0, PST1, PST2 via Manage Material Prices - Sales (VK12"
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/consumption-items-and-rating]
aliases: [3GD_S4CLD2608_Master_Data_ZH_XX]
keywords: [Consumption Items and Service-Type-Based Rating, pricing conditions, service-based pricing, master data script, convergent invoicing, condition types, business roles, 3GD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-321
topic: 09-subscription-billing-and-contract-accounting/consumption-items-and-rating
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建基于服务类型的定价条件 - MDS (3GD) (3GD_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Consumption Items and Service-Type-Based Rating** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建基于服务类型的定价条件 - MDS (3GD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897523)

[2 前提条件 3](#_Toc233897524)

[2.1 系统访问 3](#_Toc233897525)

[2.2 角色 3](#_Toc233897526)

[2.3 必填和可选主数据 3](#_Toc233897527)

[3 概览表 5](#_Toc233897528)

[4 测试过程 6](#_Toc233897529)

[4.1 创建 PST0 的定价条件 6](#_Toc233897530)

[4.2 创建 PST1 的定价条件 7](#_Toc233897531)

[4.3 创建 PST2 的定价条件 8](#_Toc233897532)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

基于服务的定价条件用于存储在 Convergent 定价中执行自动定价所需的信息 开发票。其中包括基于不同变式的价格和附加费。它们可能特定于特定客户，或者 物料或参数组合。基于服务的定价条件保存信息，例如以特定货币计的价格 用于物料。此信息用于并存储在可开票项目、开票计划项目、开票凭证和开发票中 文档。

信息通常特定于组织内的特定销售单位。

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

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） |
| --- | --- | --- | --- |
| 定价专家 | SAP_BR_PRICING_SPECIALIST | 价格管理 | SAP_BR_PRICING_SPECIALIST |

### 必填和可选主数据

主数据记录可能 参考其他主数据 。下表 提供要在主数据中使用的可选和强制主数据对象的概览。 数据记录。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 销售组织 | 初始屏幕 | 必填 | <销售组织编号> |
| 分销渠道 | 初始屏幕 | 必填 | <分销渠道编号> |

## 概览表

此主记录由下表中提供的多个段组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建 PST0 的定价条件](#unique_7) [第 ] 页 6 | 定价专家 | 设置物料价格 - 销售 (VK12) | 已维护物料定价条件。 |
| [创建 PST1 的定价条件](#unique_8) [第 ] 页 7 | 定价专家 | 设置物料价格 - 销售 (VK12) | 已维护物料定价条件。 |
| [创建 PST2 的定价条件](#unique_9) [第 ] 页 8 | 定价专家 | 设置物料价格 - 销售 (VK12) | 已维护物料定价条件。 |

## 测试过程

本部分介绍属于此流程的每个段或流程步骤的过程。 主记录。

### 创建 PST0 的定价条件

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

此过程描述创建销售定价条件：PST0

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 将出现“开始”页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 设置物料价格 - 销售 (VK12) 。 | 因此， 更改条件记录 屏幕。 |  |
| 3 | 定价条件类型 | 在 中 更改条件记录 视图中，输入以下内容并选择 输入 。条件类型 ： PST0 |  |  |
| 4 | 选择 | 在 中 更改基于服务类型的定价条件 (PST0)：选择 视图中，输入以下内容并选择 执行 。销售组织 ： <销售组织>分销渠道 ： <分销渠道> |  |  |
| 5 | 更改价格条件 | 在 中 更改基于服务类型的定价条件 (PST0)：概览 视图中，输入以下内容并选择 保存 。材料 ： CBPTS002金额 ： <金额>计量单位 ： <PC>有效自 ： <当前日期>有效期至 ：例如， <当前日期 + 一年> | 已维护物料定价条件。 |  |

### 创建 PST1 的定价条件

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

此过程描述创建销售定价条件：PST1

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 将出现“开始”页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 设置物料价格 - 销售 (VK12) 。 | 因此， 更改条件记录 屏幕。 |  |
| 3 | 定价条件类型 | 在 中 更改条件记录 视图中，输入以下内容并选择 输入 。条件类型 ： PST1 |  |  |
| 4 | 选择 | 在 中 更改基于服务类型的变式 (PST1)：选择 视图中，输入以下内容并选择 执行 。销售组织 ： 销售组织分销渠道 ： 分销渠道 |  |  |
| 5 | 更改价格条件 | 在 中 更改基于服务类型的变式 (PST1)：概览 视图中，输入以下内容并选择 保存 。材料 ： CBPTS001变式 ： HIGH_END金额 ： <金额>计量单位 ： PC有效自 ： <当前日期>有效期至 ：例如， <当前日期 + 一年> | 已维护物料定价条件。 |  |

### 创建 PST2 的定价条件

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

此过程描述创建销售定价条件：PST2

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 将出现“开始”页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 设置物料价格 - 销售 (VK12) 。 | 因此， 更改条件记录 屏幕。 |  |
| 3 | 定价条件类型 | 在 中 更改条件记录 视图中，输入以下内容并选择 输入 。条件类型 ： PST2 |  |  |
| 4 | 选择 | 在 中 基于服务类型的可变 % (PST2)：选择 视图中，输入以下内容并选择 执行 。销售组织 ： 销售组织分销渠道 ： 分销渠道 |  |  |
| 5 | 更改价格条件 | 在 中 更改基于服务类型的可变 % (PST2)：概览 视图中，输入以下内容并选择 保存 。材料 ： CBPTS001变式 ： HIGH_END金额 ： <金额>有效自 ： <当前日期>有效期至 ：例如， <当前日期 + 一年> | 已维护物料定价条件。 |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/criar-condicao-de-determinacao-de-precos-baseada-em-tipo-de-servico-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-service-type-based-pricing-condition-mds-3gd]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-319]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-condicion-de-determinacion-de-precios-b]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 6,880 chars in the whole document
