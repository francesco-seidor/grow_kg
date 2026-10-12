---
id: 12-production-and-manufacturing/mds-bld-573
title: 创建生产版本 - MDS (BLD) (BLD_S4CLD2608_Master_Data_ZH_XX)
description: Chinese machine-translated master data script (BLD) for creating and editing production versions via F6400 or F2568 in SAP S/4HANA Cloud Public Edition.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-versions]
aliases: [BLD_S4CLD2608_Master_Data_ZH_XX]
keywords: [Production Versions, production version proposals, bill of materials, routings, master recipes, mass editing, business roles, BLD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-573
topic: 12-production-and-manufacturing/production-versions
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建生产版本 - MDS (BLD) (BLD_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Production Versions** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建生产版本 - MDS (BLD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897881)

[2 前提条件 3](#_Toc233897882)

[2.1 系统访问 3](#_Toc233897883)

[2.2 角色 3](#_Toc233897884)

[2.3 所需组织单位 3](#_Toc233897885)

[2.4 必填和可选主数据 4](#_Toc233897886)

[3 概览表 5](#_Toc233897887)

[4 测试过程 6](#_Toc233897888)

[4.1 创建生产版本 6](#_Toc233897889)

[4.2 编辑生产版本（可选） 9](#_Toc233897890)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

创建生产版本

在本文档中，您将找到有关如何为 创建生产版本的描述 SAP S/4HANA Cloud Public 版本 系统。描述 包括那些数据段与 SAP S/4HANA Cloud Public 版本 设备。与 无关的字段 范围 SAP S/4HANA Cloud Public 版本 未在本文档中描述。

按此处所述创建的生产版本可用于处理。 生产流程。

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
| 生产工程师 - 离散制造 | SAP_BR_PRODN_ENG_DISC | 生产工程 - 离散制造 | SAP_BR_PRODN_ENG_DISC |  |
| 生产工程师 - 流程制造 | SAP_BR_PRODN_ENG_PROC | 生产工程 - 流程制造 | SAP_BR_PRODN_ENG_PROC |  |

### 所需组织单位

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有数据 | 工厂 |  | 生产版本的所有数据取决于工厂。 | 工厂：__________ |

### 必填和可选主数据

生产版本数据记录可能 参考其他主数据 。因此， 下表提供了可选和必填主数据对象的概览， 在生产版本中使用。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 材料 | 为每个物料和工厂创建生产版本。 | 必填 | 在 生产版本：批量处理 屏幕, 材料 将输入 。对于物料创建，您可以遵循主数据脚本中的步骤： 创建“原材料”类型的产品主数据 - MDS - BNR ， 创建“半成品”类型的产品主数据 - MDS - BNS ，或 创建“成品”类型的产品主数据 - MDS - BNT 。 |
| 物料清单 | 在生产中分配物料的 BOM 主数据 版本 | 必填 | 在 生产版本：批量处理 屏幕， 备选物料清单 和 物料清单用途 将被输入。对于物料清单创建，您可以遵循主数据脚本中的步骤： 创建生产和销售物料清单 - MDS - BNK 。 |
| 任务清单 | 在生产版本中分配物料的获取清单。 | 必填 | 在 生产版本：批量处理 屏幕， 任务清单类型 ， 分组 ，以及 组计数器 将被输入。对于任务清单创建，您可以遵循主数据脚本中的步骤： 创建工艺路线 - MDS - BNL 或者 创建主配方 - MDS - 3X9 。 |

## 概览表

此范围项目由下列流程步骤组成： 表：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建生产版本](#unique_8) [第 ] 页 6 | 生产工程师 - 离散制造 或者 生产工程师 - 流程制造 | 处理生产版本 (F6400) 或者 管理生产版本 (F2568) |  |
| [编辑生产版本（可选）](#unique_9) [第 ] 页 9 | 生产工程师 - 离散制造 或者 生产工程师 - 流程制造 | 处理生产版本 (F6400) |  |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建生产版本

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

可以使用不同的 SAP Fiori 应用执行此步骤。您可以利用 3 个选项。您可以选择其中之一。

选项 1

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 或者 生产工程师 - 流程制造 。 | 因此， 启动 视图。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 处理生产版本 (F6400) 。 | 应用随即打开。 |  |
| 3 | 输入选择字段 | 输入以下内容并选择 执行 ：材料 ： <输入物料编号>工厂 ： <输入工厂> |  |  |
| 4 | 检查生产版本建议 | 在 生产版本建议 标签中，您可以找到创建新生产版本的建议，如果 相应的物料清单/任务列表组合尚不存在。您可以通过选择建议浏览建议详细信息并进行可能的更改。 | 备注 已引入配置步骤（标识：105965）以配置生产版本建议的规则。 |  |
| 5 | 接受建议 | 选择生产版本建议，然后选择 接受建议 。 |  |  |
| 6 | 确认 | 在 中 确认 对话框中，选择 确定 。 | 根据建议的参数创建新的生产版本。您可以在以下位置找到它： 现有生产 版本 标签。 |  |

选项 2

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 或者 生产工程师 - 流程制造 。 | 因此， 启动 视图。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 处理生产版本 (F6400) 。 | 应用随即打开。 |  |
| 3 | 输入选择字段 | 输入以下内容并选择 执行 ：材料 ： <输入物料编号>工厂 ： <输入工厂> |  |  |
| 4 | 选择标签 | 选择 现有生产版本 标签。 |  |  |
| 5 | 创建 | 选择 创建 . 在 中 创建生产版本 对话框中，输入以下内容并 选择 创建 ：材料 ： <输入物料编号>工厂 ： <输入工厂>生产版本 ： <A 4 位数>生产版本描述 ： <描述> |  |  |
| 6 | 输入参数 | 输入必要的参数并选择 创建 ：有效期开始日期 ： <当天>有效期结束日期 ： <9999 年 12 月 31 日>最小批量 ： <1>最大批量 ： <999999999>任务清单 部分：任务清单类型 ： <选择物料的任务清单类型>任务清单组 ： <选择物料组>任务清单计数器 ： <选择物料的组计数器>物料清单 部分：备选物料清单 ： <选择物料的备选物料清单>物料清单用途 ： <选择物料清单主数据的物料清单用途， 材料> | 生产版本已创建。 |  |

选项 3

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 或者 生产工程师 - 流程制造 。 | 因此， 启动 视图。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理生产版本 (F2568) 。 | 因此， 生产版本：批量处理 视图。 |  |
| 3 | 输入工厂代码 | 输入 工厂代码 。 |  |  |
| 4 | 输入物料 | 输入 材料 。按下 输入 。 |  |  |
| 5 | 生产版本 | 输入生产版本行项目，然后按 输入 。材料 ： <输入物料 编号>生产版本 ： <A 4 数字号码>有效自 ： <当天>有效期至 ： <9999 年 12 月 31 日>起始批量 ： <1>到批量 ： <999999999>备选物料清单 ：按下 F4 选择 备选物料清单 对于物料物料清单用途 ：按下 F4 选择 物料清单 用法 物料的 BOM 主数据分组 ： <输入此项的 组 材料>组计数器 ： <输入 的组计数器 材料>类型 ： <选择 的任务清单类型 材料> |  |  |
| 6 | 保存数据 | 选择 保存 。 | 生产版本已创建。 |  |

### 编辑生产版本（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 或者 生产工程师 - 流程制造 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 处理生产版本 (F6400) 。 | 应用随即打开。 |  |
| 3 | 输入选择字段 | 输入以下内容并选择 执行 ：材料 ： <输入物料编号>工厂 ： <输入工厂> |  |  |
| 4 | 导航到现有生产版本标签 | 转到 现有生产版本 标签。 |  |  |
| 5 | 编辑生产版本 | 选择要更改的生产版本，然后选择 编辑 基于 生产 版本 屏幕。根据需要对字段进行必要的更改。备注 如果要对多个生产版本进行类似更改，可以在 上进行多选。 现有生产版本 标签，然后选择 批量编辑 。在 中 批量编辑 对话框中，您可以对列出的字段进行所需更改。 |  |  |
| 6 | 保存 | 选择 保存 。 | 生产版本已成功更新。 |  |

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
- related-to :: [[12-production-and-manufacturing/fertigungsversion-anlegen-sds-bld-568]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-version-mds-bld-569]]
- related-to :: [[12-production-and-manufacturing/mds-bld-571]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-versao-de-producao-mds-bld-572]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 8,012 chars in the whole document
