---
id: 04-tax-and-statutory-reporting/mds-2sw-279
title: 创建税收条件 - MDS (2SW) (2SW_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script 2SW: create tax condition records (MEK2) and create/change purchasing price conditions (MEK1, MEK2)."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/purchasing-tax-condition-records]
aliases: [2SW_S4CLD2608_Master_Data_ZH_XX]
keywords: [Tax Condition Records and Purchasing Price Conditions, tax condition records, purchasing price conditions, master data scripts, condition types, business roles, test procedures, tax codes, 2SW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-279
topic: 04-tax-and-statutory-reporting/purchasing-tax-condition-records
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建税收条件 - MDS (2SW) (2SW_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Tax Condition Records and Purchasing Price Conditions** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建税收条件 - MDS (2SW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897468)

[2 前提条件 3](#_Toc233897469)

[2.1 系统访问 3](#_Toc233897470)

[2.2 角色 3](#_Toc233897471)

[2.3 必填和可选主数据 3](#_Toc233897472)

[3 概览表 5](#_Toc233897473)

[4 测试过程 6](#_Toc233897474)

[4.1 创建税收条件记录 6](#_Toc233897475)

[4.2 创建价格条件 8](#_Toc233897476)

[4.3 更改价格条件 9](#_Toc233897477)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

税收条件记录包含特定于一个国家/地区的信息， 物料/税收标识的不同税收标识组合的税码 工厂/税收标识。

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
| 税务专家 | SAP_BR_TAX_SPECIALIST | 税率 | SAP_BR_TAX_SPECIALIST |  |
| 采购员 | SAP_BR_PURCHASER | 采购 / 供应商开发及合同管理 | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### 必填和可选主数据

物料主数据记录可能参考其他主数据。下表提供了 要在物料中使用的可选和强制主数据对象的概览。 主数据记录。

在本节中，我们将介绍一些影响主数据行为的基本参数 记录，并且始终需要创建定价条件：

目的地国家/地区：例如， 德国

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 目的地国家/地区 | 初始屏幕 | 必填 |  |

## 概览表

此范围项目由下表中提供的多个流程步骤组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | SAP Fiori 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建税收条件记录](#unique_7) [第 ] 页 6 | 税务专家 | 设置税率 - 采购 (MEK2) | 已设置税收条件。 |
| [创建价格条件](#unique_8) [第 ] 页 8 | 采购员 | 创建价格条件 - 采购 (MEK1) | 已创建价格条件。 |
| [更改价格条件](#unique_9) [第 ] 页 9 | 采购员 | 更改价格条件 - 采购 (MEK2) | 价格条件已更改。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建税收条件记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 税务专家 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 设置税率 - 采购 (MEK2) 。 | 应用随即打开。 |  |
| 3 | 定价条件类型 | 在 更改条件记录 屏幕上，输入以下内容并按 输入 ：条件类型 ：例如， TTX1 | 因此， 组合键 屏幕。 |  |
| 4 | 组合键 | 在 组合键 屏幕上，选择 税收：物料、工厂和来源 复选框并选择 选择 。 | 因此， 更改不可抵扣 T(TTX1)：选择 屏幕。 |  |
| 5 | 目的地国家/地区 | 在 更改不可抵扣 T(TTX1)：选择 屏幕上，输入以下内容并选择 。 执行 ：目的地国家/地区 ： <国家/地区代码> | 因此， 更改不可抵扣税收条件 (TTX1)：概览 屏幕。 |  |
| 6 | 更改税收条件 | 在 更改不可抵扣税收条件 (TTX1)：概览 屏幕上，输入以下内容：物料的税收标识 ： <物料的税收标识>工厂税标识 ： <税收标识：工厂>导入 ： <导入>有效自 ： <有效期自>有效期至 ： <有效期至>税码 ： <税码> | 已维护税收条件记录。 |  |
| 7 | 保存 | 选择 保存 。 | 税收条件记录已保存。 |  |
| 8 | 选择返回 | 选择 返回 两次。 |  |  |
| 9 | 定价条件类型 | 在 更改条件记录 屏幕上，输入以下内容并按 输入 ：条件类型 ：例如， TTX1 | 因此， 组合键 对话框。 |  |
| 10 | 组合键 | 在 中 组合键 对话框中，选择 税收：工厂和科目分配来源和地区 复选框并选择 选择 。 | 因此， 更改不可抵扣 T(TTX1)：选择 屏幕。 |  |
| 11 | 目的地国家/地区 | 在 更改不可抵扣 T(TTX1)：选择 屏幕上，输入以下内容并选择 。 执行 ：目的地国家/地区 ： <国家/地区代码> | 因此， 更改不可抵扣税收条件 (TTX1)：概览 屏幕。 |  |
| 12 | 更改税收条件 | 在 更改不可抵扣税收条件 (TTX1)：概览 屏幕上，输入以下内容：工厂税标识 ： <税收标识：工厂>税收标识科目分配 ： <税收标识科目分配>导入 ： <导入>税收标识地区 ： <地区>有效自 ： <有效期自>有效期至 ： <有效期至>税码 ： <税码> | 已维护税收条件记录。 |  |
| 13 | 保存 | 选择 保存 。 | 税收条件记录已保存。 |  |

### 创建价格条件

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建价格条件 - 采购 (MEK1) 。 | 应用随即打开。 |  |
| 3 | 定价条件类型 | 输入以下条目，然后按 输入 ：条件类型 ：例如， PPR0 | 因此， 组合键 对话框。 |  |
| 4 | 组合键 | 在 组合键 屏幕上，选择 物料信息记录 (工厂特定) 复选框并选择 选择 。 | 因此， 创建缺省总价条件 (PPR0)：快速 输入 屏幕。 |  |
| 5 | 创建缺省总条件 | 在 创建缺省总价条件 (PPR0)：快速输入 屏幕上，输入以下内容：供应商 ： <供应商>材料 ： <物料>采购组织 ： <采购组织>工厂 ： <工厂>信息类型 ：例如， 0 标准金额 ： <金额>单位 ： <定价单位>Per ： <按数量>计量单位 ： <单位>有效自 ： <有效期自>有效期至 ： <有效期至> | 维护缺省总条件记录。 |  |
| 6 | 保存 | 选择 保存 。 | 条件记录已保存。 |  |

### 更改价格条件

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 更改价格条件 - 采购 (MEK2) 。 | 应用随即打开。 |  |
| 3 | 定价条件类型 | 输入以下条目，然后按 输入 ：条件类型 ：例如， PPR0 | 因此， 组合键 屏幕。 |  |
| 4 | 组合键 | 在 组合键 屏幕上，选择 物料信息记录（工厂特定） 复选框并选择 选择 。 | 因此， 创建缺省总价条件 (PPR0)：快速输入 屏幕。 |  |
| 5 | 更改缺省总条件 | 在 更改缺省总价条件 (PPR0)：快速输入 屏幕上，输入以下内容：供应商 ： <供应商>材料 ： <物料>采购组织 ： <采购组织>工厂 ： <工厂>信息类型 ：例如， 0 标准选择 执行 。输入以下内容：金额 ： <金额> | 缺省总条件记录已更改。 |  |
| 6 | 保存 | 选择 保存 。 | 条件记录已保存。 |  |

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
- related-to :: [[04-tax-and-statutory-reporting/crear-condicion-para-determinacion-de-impuestos-mds-2sw-276]]
- related-to :: [[04-tax-and-statutory-reporting/master-data-script-create-tax-condition-2sw-275]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-277]]
- related-to :: [[04-tax-and-statutory-reporting/objetivo-script-de-dados-mestre-criar-condicao-de-imposto-mds-2sw-port]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 7,534 chars in the whole document
