---
id: 02-business-partner-and-product-master-data/mds-2ni-273
title: 创建应用程序组和特征显示 - MDS (2NI) (2NI_S4CLD2608_Master_Data_ZH_XX)
description: 主数据脚本（中文机器翻译）：用 CU_CHAR_DISPLAY 创建应用程序组和特征显示并分配特征。
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2NI_S4CLD2608_Master_Data_ZH_XX]
keywords: [Configurable Materials and Characteristic Display, characteristic display, application group, master data scripts, characteristics, variant configuration, 2NI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-273
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建应用程序组和特征显示 - MDS (2NI) (2NI_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建应用程序组和特征显示 - MDS (2NI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897432)

[2 前提条件 3](#_Toc233897433)

[2.1 系统访问 3](#_Toc233897434)

[2.2 角色 3](#_Toc233897435)

[2.3 必需和运营主数据 3](#_Toc233897436)

[2.4 数据创建的主要参数 4](#_Toc233897437)

[2.4.1 事务 4](#_Toc233897438)

[3 概览表 5](#_Toc233897439)

[4 测试过程 6](#_Toc233897440)

[4.1 创建应用程序组 6](#_Toc233897441)

[4.2 创建特征显示 7](#_Toc233897442)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将获得如何为以下内容创建特征显示记录的描述： SAP S/4HANA Cloud Public 版本 系统。描述包括与以下内容相关的数据： SAP S/4HANA Cloud Public 版本 设备，例如应用程序 组、特征显示和特征分配。与 范围无关的字段 SAP S/4HANA Cloud Public 版本 未在本文档中描述。

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
| 产品配置建模器 | SAP_BR_PRODUCT_CONFIG_MODELER | 变式配置 | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### 必需和运营主数据

特征显示记录可能参考其他主数据。下表提供了 要在物料中使用的可选和强制主数据对象的概览。 主数据记录。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 特征 |  | 必填 | 特征将分配到特征显示 记录 |

### 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录，并且始终需要创建特征显示。

#### 事务

借助事务 ，系统确定在哪个事务中 特征显示应可用。

对于 1711 版本，仅支持销售和分销凭证。

| 事务 | 备注 |
| --- | --- |
| 销售和分销凭证 | 对于 1711 版本，只有销售和分销凭证是 支持特性显示。 |
| 生产订单 |  |
| 贸易合同 |  |
| 采购订单 |  |
| 收货 |  |
| 订单确认 |  |

## 概览表

在此部分中，用户在创建主数据记录时执行的步骤清单为 已提供。主数据对象的每个逻辑、有意义的段都应导致 单独步骤（例如：组织单位相关的数据段等）。

范围项目 创建应用程序组和特征显示 - MDS 包含多个流程步骤 在下表中提供：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤、报表或项目 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [创建应用程序组](#unique_9) [第 ] 页 6 | 产品配置建模器 | 维护特征显示配置 (CU_CHAR_DISPLAY) | 已创建应用程序组 |
| [创建特征显示](#unique_10) [第 ] 页 7 | 产品配置建模器 | 维护特征显示配置 (CU_CHAR_DISPLAY) | 已创建应用程序组 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的过程。 您还可以使用这些过程测试主数据创建。

### 创建应用程序组

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 维护特征显示配置 (CU_CHAR_DISPLAY) 。 | 因此， 更改视图“应用程序组”：概览 视图。 |  |
| 3 | 输入应用程序组 | 在 更改视图“应用程序组”：概览 屏幕上，选择 新条目 。并进行以下操作 条目：事务 ： <从下拉列表中选择>应用程序组 ： <任意代码> | 因此， 新条目：已添加条目的概览 屏幕。 |  |
| 4 | 保存数据 | 选择 保存 。 |  |  |

### 创建特征显示

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 选择 维护特征显示配置 (CU_CHAR_DISPLAY) 。 | 因此， 更改视图“应用程序组”：概览 视图。 |  |
| 3 | 输入应用程序组 | 在 更改视图“应用程序组”：概览 屏幕上，选择 特征显示 。选择 新条目 。输入以下内容并按 。 输入 ：特性显示 ： <任意代码> 。描述 ： <输入特征描述 显示> 。应用程序组 ： <选择 F4 获取帮助> 。 | 因此， 更改视图“特征显示”：概览 屏幕。 |  |
| 4 | 分配特征 | 选择在上一步中创建的特征显示，然后选择 特征 分配 。输入以下内容：序列 ： <输入序号以确定特征的顺序> 。特征名称 ： <搜索特征，按 选择 F4 搜索帮助> 。颜色 ： <输入适当的列宽以显示特征描述和值> 。 | 因此， 更改视图“特征分配”：概览 屏幕 显示 。 |  |
| 5 | 保存数据 | 选择 保存 。 |  |  |

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
> Flagged while digesting this document, not verified: 事务表称仅销售和分销凭证支持（1711 版本），但同表列出多种事务，可能与 2608 版现状不符

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]
- related-to :: [[02-business-partner-and-product-master-data/crear-grupo-de-aplicaciones-y-visualizacion-de-caracteristicas-mds-2ni]]
- related-to :: [[02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-271]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 6,352 chars in the whole document
