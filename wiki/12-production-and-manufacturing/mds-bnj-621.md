---
id: 12-production-and-manufacturing/mds-bnj-621
title: 创建生产工作中心 - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese machine-translated master data script (BNJ) for creating production work centers, work center groups and assignments in SAP S/4HANA Cloud Public Edition."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-work-centers]
aliases: [BNJ_S4CLD2608_Master_Data_ZH_XX]
keywords: [Production Work Centers and Work Center Groups, work centers, work center categories, work center groups, capacity planning, costing data, standard value key, routings, business roles, BNJ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-621
topic: 12-production-and-manufacturing/production-work-centers
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建生产工作中心 - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Production Work Centers and Work Center Groups** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建生产工作中心 - MDS (BNJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897967)

[2 前提条件 4](#_Toc233897968)

[2.1 系统访问 4](#_Toc233897969)

[2.2 角色 4](#_Toc233897970)

[2.3 所需组织单位 4](#_Toc233897971)

[2.4 必填和可选主数据 5](#_Toc233897972)

[2.5 数据创建的主要参数 5](#_Toc233897973)

[2.5.1 工作中心类别 5](#_Toc233897974)

[3 概览表 6](#_Toc233897975)

[4 测试过程 7](#_Toc233897976)

[4.1 创建工作中心 7](#_Toc233897977)

[4.2 管理工作中心组（可选） 9](#_Toc233897978)

[4.2.1 创建工作中心组（可选） 10](#_Toc233897979)

[4.2.2 分配工作中心（可选） 11](#_Toc233897980)

[5 附录 12](#_Toc233897981)

[5.1 创建工艺路线 12](#_Toc233897982)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

工作中心是执行生产工序的位置。例如，工作中心 可以代表生产线、机器、机器组、员工或组 员工。

工作中心保存用于产能计划的信息（例如，可用产能）， 计划（例如，处理时间的公式）和成本核算（例如成本中心）。此项 信息用于任务清单和生产工作订单等事务中。 信息特定于生产站点（称为工厂）。

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

### 所需组织单位

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有数据 | 工厂 |  | 工作中心的所有数据取决于工厂。 | 工厂：__________ |

### 必填和可选主数据

工作中心数据记录可能 参考其他主数据 。以下 表中提供了要在 中使用的可选和必需主数据对象的概览。 工作中心。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 标准值码 | 在工作中心 UI 的基本数据标签中，您可以找到 的条目 标准值码 中的 标准 值维护 部分。 | 必填 | 系统使用标准值作为来源参数 标准 值 计算执行时间、产能 要求和成本。使用标准值码，将参数标识分配到标准 values。此参数标识用于标识以下项中的标准值： formula。可使用参数标识确定 标准值，如安装、机器或人工。 |

### 数据创建的主要参数

在本部分中，我们将介绍一些影响主记录行为的基本参数，并且始终需要创建工作中心：

#### 工作中心类别

工作中心类别确定可在工作中心的主记录中维护哪些数据。工作中心可按其类别（例如，生产工作中心、维护工作中心和服务工作中心等）进行区分。

| 工作中心类别 | 描述 |
| --- | --- |
| 0001 | 机器 |
| 0007 | 生产线 |

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建工作中心](#unique_10) [第 ] 页 7 | 生产工程师 - 离散制造 | 管理工作中心 (F6175) |  |
| [创建工作中心组（可选）](#unique_11) [第 ] 页 10 | 生产工程师 - 离散制造 | 管理工作中心组 (F4044) |  |
| [分配工作中心（可选）](#unique_12) [第 ] 页 11 | 生产工程师 - 离散制造 | 管理工作中心组 (F4044) |  |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建工作中心

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 打开 SAP Fiori 应用 | 选择 管理工作中心 (F6175) 。 |  |  |
| 3 | 选择创建 | 选择 创建 。 | 随即显示新屏幕，显示 创建工作中心：初始 屏幕 。 |  |
| 4 | 输入工厂代码 | 输入 工厂代码 。 | 因此， 创建组织 屏幕。 |  |
| 5 | 输入工作中心标识 | 输入 工作中心标识 。备注 工作中心标识的字段长度小于 8。 |  |  |
| 6 | 工作中心类别 | 选择工作中心类别：<0001> 机器<0007> 生产线 |  |  |
| 7 | 选择基本数据 | 选择 基本数据 按钮。 | 因此， 创建工作中心：基本数据 屏幕 随即显示。 |  |
| 8 | 输入数据 | 在 基本数据 标签上，输入以下数据：描述 ： <输入描述>负责人 ： <工厂的负责人或负责人>用法 ： <009>标准值码 ： <SAP1> |  |  |
| 9 | 设置容量和处理公式 | 在 产能 标签上，输入以下数据：产能类别 ： <001（机器/002（人员）>设置公式 ： <SAP005>处理公式 ： <SAP006>按下 输入 。 | 因此， 创建工作中心 容量：抬头 屏幕。 |  |
| 10 | 设置工作中心产能 | 在 中 工作中心产能：抬头 部分，输入以下数据：产能类别描述 ： <添加描述>产能负责人 ：按下 F4 搜索工厂的负责人。工厂日历标识 ： <您所在国家的日历>活动版本 ： <1>容量基本单位 ：例如， D起始时间 ： <开始时间>结束时间 ： <结束时间>间休长度 ： <间休长度>操作时间 ： <操作时间>产能利用率 ： <100>单项产能数 ： <10>与有限计划相关 ： <X>长期计划 ： <X>可由多个工序使用 ： <X>按下 输入 。 | 屏幕返回到产能概览。 |  |
| 11 | 输入计划数据 | 在 计划 标签上，输入以下数据：产能类别 ： <001（机器/002（人员）>设置持续时间 ： <SAP001>处理持续时间 ： <SAP002> |  |  |
| 12 | 输入成本核算数据 | 在 成本核算 标签页上，输入以下数据：成本中心 ： <公司代码的成本中心>活动类型（用于设置） ： <3>公式（用于设置） ： <SAP005>活动类型（机器） ： <1>公式（机器） ： <SAP006>活动类型（人工） ： <11>公式（人工） ： <SAP007>作业单位 ： 选择所需计量单位，例如，最小值 |  |  |
| 13 | 保存数据 | 保存输入内容。 |  |  |

### 管理工作中心组（可选）

目的

本章介绍如何根据需要对工作中心进行分组。

#### 创建工作中心组（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

此流程步骤向您显示如何创建工作中心组。

您可以检查通过流程步骤创建的示例工作中心组。 创建并分配工作中心组 在范围项目 中 31L 。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问应用 | 打开 管理工作中心组 (F4044) 。 | 应用随即打开。 |  |
| 3 | 创建群组 | 选择 创建 位于表上方。在 创建群组 屏幕上，设置 以下条目：分组 ： <输入组名称>工厂 ： 1010组类型 ： <ALTERNATIV> 或 <SAME LINE> 或 <RSPONSBLTY>描述 ： <输入描述>选择 创建 。 | 已创建工作中心组。 |  |

#### 分配工作中心（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

此流程步骤向您显示如何将工作中心分配到工作中心组。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问应用 | 打开 管理工作中心组 (F4044) 。 | 应用随即打开。 |  |
| 3 | 选择组 | 查找在先前步骤中创建的组，然后选择行末尾的 > 图标。 | 详细信息列表显示在右侧面板上。 |  |
| 4 | 分配工作中心 | 在 中 组组件 部分，选择 分配工作中心 。从对话框中选择一个或多个工作中心，然后选择 好的 。备注 如果工作中心已分配到其他组，将出现错误消息： 工作中心 "XXX" 已分配给此 组类型 。 | 显示分配到组的工作中心。已成功分配工作中心。 |  |

## 附录

### 创建工艺路线

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 工艺路线 |  |  | 要执行此活动，请运行 创建工艺路线 - MDS （BNL） 测试 script。 |

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
- related-to :: [[12-production-and-manufacturing/create-production-work-center-mds-bnj-617]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-619]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-centro-de-trabalho-da-producao-mds-bnj-62]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-crear-puesto-de-trabajo-de-produccion-mds-bnj]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 8,190 chars in the whole document
