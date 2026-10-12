---
id: 08-sales-order-management/mds-4vo-423
title: 创建产品替代 - MDS (4VO) (4VO_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script for creating product substitutions and exclusions, with optional reason, group and control setup."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [4VO_S4CLD2608_Master_Data_ZH_XX]
keywords: ["Product, Plant and Storage Location Substitution", product substitution, product exclusion, substitution reasons, substitution groups, substitution control, product master data, master data scripts, business roles, 4VO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-423
topic: 08-sales-order-management/product-and-location-substitution
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建产品替代 - MDS (4VO) (4VO_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建产品替代 - MDS (4VO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897696)

[2 前提条件 3](#_Toc233897697)

[2.1 系统访问 3](#_Toc233897698)

[2.2 角色 3](#_Toc233897699)

[2.3 所需组织单位 3](#_Toc233897700)

[2.4 必需主数据 4](#_Toc233897701)

[2.5 预备步骤 4](#_Toc233897702)

[2.5.1 创建产品替代原因（可选） 4](#_Toc233897703)

[2.5.2 创建替代组（可选） 5](#_Toc233897704)

[2.5.3 创建替代控制（可选） 7](#_Toc233897705)

[3 概览表 9](#_Toc233897706)

[4 测试过程 10](#_Toc233897707)

[4.1 创建产品替代 10](#_Toc233897708)

[4.2 创建产品排除 11](#_Toc233897709)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到如何为以下内容创建产品替代和排除主数据： SAP S/4HANA Cloud Public 版本 系统。

产品替代是一种用于将一个产品替换为另一个产品的技术。出于各种原因，可以创建产品替代。例如：

- 产品不再有库存
- 产品超出质保
- 替代产品库存充足

产品排除使客户能够排除产品作为替代。例如，可以为已终止产品创建排除。

## 前提条件

本部分汇总了执行系统、用户、主数据、组织数据、其他测试数据和业务条件方面测试的所有前提条件。

### 系统访问

| 系统 | 明细 |
| --- | --- |
| 系统 | 可通过 SAP Fiori 快速启动板访问。系统管理员为您提供用于访问分配给您的角色的各种应用的 URL。 |

### 角色

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） | 登录 |
| --- | --- | --- | --- | --- |
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST | 主数据 - 产品 / 产品治理 | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### 所需组织单位

组织结构反映贵公司的结构。产品替代品可以是 取决于公司的组织单位（工厂）。它也可以是独立的 组织单位。下表提供了相关 组织单位。

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 产品替代和产品排除 | 工厂 |  | 在产品替代/排除中，工厂不是必需的。产品 可能发生无工厂限制的变电站/排除。 | 工厂：____________ |

### 必需主数据

产品替代数据指的是产品主数据。测试的必填主数据 脚本表示物料/产品。通过以下操作创建自己的主数据： 示例主数据。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 材料 | 创建产品替代创建产品排除 | 必填 | 要创建产品替代或产品排除，应存在 您的系统中至少有 2 个物料/产品主数据 |

有关创建主数据对象的详细信息，请参阅 [主数据脚本 (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) 。

表 1：主数据脚本参考

| MDS | 描述 |
| --- | --- |
| BNF | 创建“贸易货物”类型的产品主数据 - MDS |

### 预备步骤

#### 创建产品替代原因（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供有关如何创建产品替代/排除原因的说明。可用的应用相关 取决于分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代原因 - 产品 (F4789) 。 | 因此， 管理替代原因 - 产品 屏幕。 |  |
| 3 | 选择创建 | 在 管理替代原因 - 产品 屏幕上，选择 创建 。 | 因此， 原因 屏幕。 |  |
| 4 | 输入原因 | 在 中 抬头 部分中，输入以下内容：原因 ： <输入新的替代原因代码，例如， 升级> |  |  |
| 5 | 保存数据 | 选择 创建 。 | 系统消息显示 对象已保存 。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 原因描述 屏幕。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分，将 以下条目：语言代码 ： <输入适用于原因的语言代码，例如，EN 表示 英语>原因描述 ： <输入描述原因的文本，例如， 适用于正在升级的产品> |  |  |
| 8 | 保存数据 | 选择 创建 。 | 系统消息显示 已创建描述 。 |  |

#### 创建替代组（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建“产品组”的说明 替代/排除。可用的应用取决于您分配的 role。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代组 - 产品 (F4788) 。 | 因此， 管理替代组 - 产品 显示屏幕。 |  |
| 3 | 选择创建 | 在 管理替代组 - 产品 屏幕上，选择 创建 。 | 因此， 管理替代组 - 产品 创建 屏幕。 |  |
| 4 | 输入组 | 在 中 抬头 部分，进行以下操作 条目：分组 ： <输入新组 用于替代，例如， STANDARD_DISPLAY> |  |  |
| 5 | 保存数据 | 选择 创建 。 | 系统消息显示 对象已保存 。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 组描述创建 屏幕是 显示。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分，将 以下条目：语言代码 ： <输入 适用于组的语言，例如，EN 英语>组描述 ： <输入 用于描述组的文本，例如，所有标准 计算机显示> |  |  |
| 8 | 保存数据 | 选择 创建 。 | 系统消息显示 对象已保存 。 |  |
| 9 | 选择返回 | 在 中 标题 部分，选择 <（后退） | 因此， 管理替代组 - 产品 屏幕。 |  |
| 10 | 激活组数据 | 选择 生效 。 | 系统消息显示 对象是 活动 。 |  |

#### 创建替代控制（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建产品控制的说明。 替代/排除组。可用的应用取决于您的 指派的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代控制 - 产品 (F4787) 。 | 因此， 管理替代控制 - 产品 屏幕。 |  |
| 3 | 选择创建 | 在 管理替代控制 - 产品 屏幕上，选择 创建 。 | 因此， 管理替代控制 - 产品 创建 屏幕。 |  |
| 4 | 输入控制 | 在 中 抬头 部分，进行以下操作 entry。控制 ： <输入新的 替代控制，例如， 销售> |  |  |
| 5 | 保存数据 | 选择 创建 。 | 系统消息显示 对象已保存 。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 控制描述创建 屏幕是 显示。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分，将 以下条目：语言代码 ： <输入 适用于控制的语言，例如，EN 英语>控制描述 ： <输入 描述控制的文本，例如，对于 销售> |  |  |
| 8 | 保存数据 | 选择 创建 。 | 系统消息显示 对象已保存 。 |  |
| 9 | 选择返回 | 在 中 标题 部分，选择 <（后退） 。 | 因此， 管理替代控制 - 产品 显示屏幕。 |  |
| 10 | 分配组 | 在 中 已分配组 部分，选择 指定 。 | 因此， 将组分配到控制 对话框。 |  |
| 11 | 选择组 | 在 中 将组分配到控制 对话框，搜索并选择 分组 。例如，选择 分组 <STANDARD_DISPLAY>选择 指定 。 | 系统消息显示 对象是 已分配 。 |  |

## 概览表

此范围项目由下表中提供的流程细分组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建产品替代](#unique_11) [第 ] 页 10 | 主数据专家 - 产品数据 | 管理替代 - 产品 (F4785) | 已创建产品替代记录。 |
| [创建产品排除](#unique_12) [第 ] 页 11 | 主数据专家 - 产品数据 | 管理排除 - 产品 (F4786) | 已创建产品排除记录。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建产品替代

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建产品替代的说明。应用 是否可用取决于分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代 - 产品 (F4785) 。 | 因此， 管理替代 - 产品 屏幕。 |  |
| 3 | 选择创建 | 在 中 管理替代 - 产品 视图，选择 创建 。 | 因此， 管理替代 - 产品 显示创建屏幕的灵活列布局。 |  |
| 4 | 输入抬头数据 | 在 中 抬头 部分，进行以下操作 条目：产品 ： <输入 需要 替代>替代产品 ： <输入 替代>工厂 ： <工厂 编号>必须提供“产品”和“替代产品”数据才能创建 替代。 |  |  |
| 5 | 输入基本信息数据 | 在 中 基本信息 部分，制造 以下条目：原因 ： <输入 创建替代的原因。例如，升级>有效自 ： <输入有效期的开始日期和时间>有效期至 ： <输入有效期的结束日期和时间>时区 ： <输入有效期适用的时区>以上条目是可选的。 |  |  |
| 6 | 保存数据 | 选择 创建 。 | 系统消息显示 对象已保存 。 |  |
| 7 | 激活产品替代数据 | 选择 生效 。 | 系统消息显示 对象处于活动状态 。 |  |

### 创建产品排除

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下程序提供创建产品排除的说明。应用 是否可用取决于分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理排除 - 产品 (F4786) 。 | 因此， 管理排除 - 产品 屏幕。 |  |
| 3 | 选择创建 | 在 中 管理排除 - 产品 视图、 选择 创建 。 | 因此， 管理排除 - 产品创建 屏幕。 |  |
| 4 | 输入抬头数据 | 在 中 抬头 部分，进行以下操作 条目：产品 ： <输入 需要从 中排除的产品 替代>工厂 ： <工厂 编号>产品是创建排除的必填项。 |  |  |
| 5 | 输入基本信息数据 | 在 中 基本信息 部分，制造 以下条目：原因 ： <输入 排除产品的原因>有效自 ： <输入有效期的开始日期和时间>有效期至 ： <输入有效期的结束日期和时间>时区 ： <输入有效期适用的时区>以上条目是可选的。 |  |  |
| 6 | 保存数据 | 选择 创建 。 | 系统消息显示 对象已保存 。 |  |
| 7 | 激活产品排除数据 | 选择 生效 。 | 系统消息显示 对象处于活动状态 。 |  |

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
- related-to :: [[08-sales-order-management/creacion-de-sustitucion-de-producto-mds-4vo-420]]
- related-to :: [[08-sales-order-management/create-product-substitution-mds-4vo-419]]
- related-to :: [[08-sales-order-management/mds-4vo-421]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-de-produto-mds-4vo-422]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 9,479 chars in the whole document
