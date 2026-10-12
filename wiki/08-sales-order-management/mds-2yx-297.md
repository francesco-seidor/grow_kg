---
id: 08-sales-order-management/mds-2yx-297
title: 创建客户物料信息记录 - MDS (2YX) (2YX_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script 2YX: create a customer-material information record with Manage Customer Materials app F2499."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-material-info-records]
aliases: [2YX_S4CLD2608_Master_Data_ZH_XX]
keywords: [Customer-Material Info Records, customer material info records, master data scripts, unit conversion, sales organization, distribution channel, internal sales, business role templates, fiori launchpad access, 2YX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-297
topic: 08-sales-order-management/customer-material-info-records
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建客户物料信息记录 - MDS (2YX) (2YX_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Customer-Material Info Records** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建客户物料信息记录 - MDS (2YX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897487)

[2 前提条件 3](#_Toc233897488)

[2.1 系统访问 3](#_Toc233897489)

[2.2 角色 3](#_Toc233897490)

[2.3 必填和可选主数据 3](#_Toc233897491)

[2.4 必填和可选主数据 4](#_Toc233897492)

[3 概览表 5](#_Toc233897493)

[4 测试过程 6](#_Toc233897494)

[4.1 创建客户物料信息 6](#_Toc233897495)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何为您的 创建客户物料信息 的描述 SAP S/4HANA Cloud Public 版本 系统。因此， 描述包括那些数据段与 SAP S/4HANA Cloud Public 版本 设备。不相关的字段 用于范围 SAP S/4HANA Cloud Public 版本 内容未在本文档中描述。

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
| 内部销售代表 | SAP_BR_INTERNAL_SALES_REP | 内部销售 / 客户退货 / 开票 | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### 必填和可选主数据

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 客户 | 初始屏幕 | 必填 |  |
| 销售组织 | 初始屏幕 | 必填 |  |
| 分销渠道 | 初始屏幕 | 必填 |  |
| 材料 | 初始屏幕 | 可选 |  |

### 必填和可选主数据

在本部分中，您可以找到一些影响主记录行为的基本参数，并且始终需要创建定价 condition：

销售组织 ： <销售组织>

分销渠道 ： <分销渠道>

客户 ： <客户>

材料 ： <物料编号>

## 概览表

此范围项目由下列流程步骤组成： 表：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | SAP Fiori 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建客户物料信息](#unique_8) [第 ] 页 6 | 内部销售代表 | 管理客户物料 (F2499) | 已创建客户物料信息记录。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建客户物料信息

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
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 内部销售代表 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理客户物料 (F2499) 。 | 应用随即打开。 |  |
| 3 | 访问客户物料的创建 | 选择 创建 。 | 因此， 客户物料 屏幕。 |  |
| 4 | 输入基本客户物料信息 | 输入以下内容：客户 ： <客户>产品 ： <物料编号>销售组织 ： <销售组织>分销渠道 ： <分销渠道>客户物料描述 ：提供客户和物料的描述。 | 维护基本客户物料信息。 |  |
| 5 | 输入销售单位 | 在 中 单位转换 部分中，输入以下内容：1 PAL（客户单位） ： 2 件（基本） 单位） | 维护客户-物料组合的销售单位。备注要在此屏幕上维护销售单位和转换，需要计量单位的物料主数据和 应维护转换。您可以参考其他主数据脚本，例如， 创建“贸易货物”类型的产品主数据 - MDS - BNF （针对贸易货物）。在此屏幕上维护销售单位后，其将显示在销售凭证中。 |  |
| 6 | 选择创建 | 选择 创建 。 | 客户物料已成功创建。 |  |

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
- related-to :: [[08-sales-order-management/crear-registro-info-para-cliente-y-material-mds-2yx-294]]
- related-to :: [[08-sales-order-management/create-customer-material-info-record-mds-2yx-293]]
- related-to :: [[08-sales-order-management/criar-registro-info-de-material-do-cliente-mds-2yx-296]]
- related-to :: [[08-sales-order-management/kundenmaterial-infosatz-anlegen-sds-2yx-292]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 5,489 chars in the whole document
