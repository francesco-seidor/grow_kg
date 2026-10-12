---
id: 06-management-accounting/mds-bnn-645
title: 创建活动类型和活动类型层次结构 - MDS (BNN) (BNN_S4CLD2608_Master_Data_ZH_XX)
description: "SAP S/4HANA Cloud 2608 master data script (ZH, machine-translated) for creating activity types and hierarchies, change log and where-used list in Controlling."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/activity-types]
aliases: [BNN_S4CLD2608_Master_Data_ZH_XX]
keywords: [Activity Types and Activity Type Hierarchies, activity types, activity type hierarchy, master data script, cost centers, secondary cost elements, change log, where-used list, controlling area, BNN]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-645
topic: 06-management-accounting/activity-types
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建活动类型和活动类型层次结构 - MDS (BNN) (BNN_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Activity Types and Activity Type Hierarchies** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建活动类型和活动类型层次结构 - MDS (BNN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897969)

[2 前提条件 3](#_Toc233897970)

[2.1 系统访问 3](#_Toc233897971)

[2.2 角色 3](#_Toc233897972)

[2.3 所需组织单位 3](#_Toc233897973)

[2.4 必填和可选主数据 4](#_Toc233897974)

[2.5 数据创建的主要参数 4](#_Toc233897975)

[2.6 预备步骤 4](#_Toc233897976)

[2.6.1 用户设置 - 设置成本控制范围 4](#_Toc233897977)

[3 概览表 6](#_Toc233897978)

[4 测试过程 7](#_Toc233897979)

[4.1 创建活动类型主数据 7](#_Toc233897980)

[4.2 创建活动类型层次结构主数据 8](#_Toc233897981)

[4.3 分析 10](#_Toc233897982)

[4.3.1 活动类型变更日志 10](#_Toc233897983)

[4.3.2 使用位置清单 - 活动类型 11](#_Toc233897984)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

活动类型表示成本中心在成本控制范围内产生的活动。活动类型用于计划和 分配以活动单位记录和测量的活动。活动数量使用活动价格进行评估，即 在成本中心维护。

活动类型的使用方式如下：

确定成本中心的基于数量的输出。生产和服务成本中心的计划活动数量必须： 与物流中的主生产计划保持一致。这确定了所需的计划作业数量，以及 产能。

控制成本中心的活动数量。这样便可测量运营率或容量比率。 成本中心利用率。

除手动计划活动数量外，还可以使用间接作业分配来计划作业数量 自动完成。

活动类型层次结构在计划中也很有用。由于没有可用于活动类型的多个选择工具， 可在活动类型层次结构中收集 活动，以便一次计划多个活动类型。

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
| 成本会计 - 间接费用 | SAP_BR_OVERHEAD_ACCOUNTANT | 间接费用会计 | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### 所需组织单位

在实施期间，已在 ERP 系统中创建公司的组织结构和主数据。组织 结构反映公司的结构。主数据表示活动类型和活动类型层次结构，具体取决于 公司的运营重点。

| 数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 成本控制范围 | 常规数据 | 必填 |  |

### 必填和可选主数据

缺省值

贵公司的组织结构和主数据在 ERP 中创建 系统。组织结构反映以下内容的结构： 您的公司。主数据取决于您的 运营重点 公司。

使用此组织特定的主数据（示例）启用业务流程 将在下一部分中提供。

活动类型和活动类型层次结构记录可能参考其他主数据。下表提供了可选 以及活动类型数据记录中使用的强制主数据对象。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 成本要素 | 常规数据 | 必填 | 次级成本要素（成本要素类型 ‘43’） |
| 总账科目 |  | 必填 | 对于次级成本要素（成本要素类型 ‘43’） |

### 数据创建的主要参数

此范围项目没有业务条件。

### 预备步骤

#### 用户设置 - 设置成本控制范围

| 步骤编号 | 步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 SAP Fiori 快速启动板 | 登录到 SAP Fiori 快速启动板 作为 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 选择设置 | 在用户上下文菜单下，选择 设置 。 | 因此， 用户设置 窗口。 |  |
| 3 | 选择缺省值 | 选择 缺省值 窗口。 | 因此， 缺省值 窗口。 |  |
| 4 | 输入数据 | 在 中 成本控制范围 字段中，输入 <成本控制范围值> ，然后选择 保存 。 | 成本控制范围，例如， A000 ，已为您的用户设置。 |  |

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建活动类型主数据](#unique_10) [第 ] 页 7 | 成本会计 - 间接费用 | 管理活动类型 (F1605A) | 可以根据新的业务需求创建活动类型。 |
| [创建活动类型层次结构主数据](#unique_11) [第 ] 页 8 | 成本会计 - 间接费用 | 管理全局层次结构 (F2918) | 可以根据新的业务需求创建活动类型层次结构。 |
| [活动类型变更日志](#unique_12) [第 ] 页 10 | 成本会计 - 间接费用 | 更改日志 - 活动类型 (F3866) |  |
| [使用位置清单 - 活动类型](#unique_13) [第 ] 页 11 | 成本会计 - 间接费用 | 管理活动类型（版本 2） (F1605A) |  |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的过程。您还可以将这些过程用于测试 主数据创建。

### 创建活动类型主数据

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理活动类型 (F1605A) 。 | 应用随即打开。 |  |
| 3 | 选择创建 | 选择 创建 。 |  |  |
| 4 | 输入活动类型数据 | 在 新活动类型：新 屏幕上的 常规数据 标签上，设置 以下条目：输入活动类型 ： 描述文本活动单位 ： <活动单位>名称 ： <名称>活动类型描述 ： <输入描述>有效自 ： <当前日期>有效期至 ： <年末日期>成本中心类别 ： <成本中心类别>活动类型类别 ： <活动类型类别>分配成本要素 ：例如， 94304000 。价格标识 ： <价格标识> | 因此， 常规数据 部分和各种标签显示。备注 您可以找到以下各项的 SAP 建议值： SAP S/4HANA Cloud Public 版本 （因为不支持其他可见项）：活动类型类别 ：仅限 1 （手动输入和手动分配）是 支持。价格标识 ：仅限 3 （手动设置价格）。实际作业类型类别 ：应为空。实际价格标识 ：默认情况下应为空。仅当已激活范围项目 时 33Q - 实际成本核算 ，你应该 使用 5 或者 7 （有关这两个值的详细信息，可以参阅 测试脚本中的 部分 33Q ）。 |  |
| 5 | 保存数据 | 选择 创建 。 | 创建并保存活动类型。 |  |

### 创建活动类型层次结构主数据

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

前提条件

您已按照中所述填写并保存物料的基本数据。[创建活动类型主数据](#unique_10) [第 ] 页 7。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理全局层次结构 (F2918) 。 | 应用随即打开。 |  |
| 3 | 选择创建 | 在 中 层次结构清单 部分，选择 创建 。 | 因此， 新建层次结构 屏幕。 |  |
| 4 | 输入新活动类型层次结构 | 在 新建层次结构 屏幕上，进行以下操作： 条目并选择 创建 ：类型 ： 活动类型层次结构层次结构标识 ： <最多 10 个字符的任意标识>注意 层次结构标识和节点标识的总长度不能超过 14 个字符。成本控制范围 ： A000层次结构描述 ： <任意描述> |  |  |
| 5 | 编辑新活动类型层次结构 | 在 层次结构清单 屏幕上，选择详细信息图标 > 并选择 编辑 针对新创建的活动类型层次结构。选择新创建的活动类型层次结构，然后选择 更多 屏幕右侧，以及 然后选择 快速输入 。在 快速输入 屏幕上，选择 活动类型 并执行以下操作 条目：标识 ： <使用搜索选择要添加的活动类型 函数>选择 确定 当你完成并选择 保存 。返回到 活动类型层次结构 屏幕并选择 激活 。 | 新创建的活动类型层次结构现已激活。 |  |

### 分析

#### 活动类型变更日志

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，运行活动类型的更改日志。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 更改日志 - 活动类型 (F3866) 。 | 因此， 变更日志 - 活动类型 对话框 显示 。 |  |
| 3 | 选择条件 | 输入以下内容：活动类型 ： <任何活动 类型> |  |  |
| 4 | 选择 | 选择 执行 。 | 随即显示显示更改详细信息历史记录的报表。 |  |

#### 使用位置清单 - 活动类型

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

通过此活动，您可以查看活动类型在其他主数据中的使用位置 例如利润中心和实际成本分配。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理活动类型（版本 2） (F1605A) 。 | 应用随即打开。 |  |
| 3 | 选择条件 | 输入以下内容：活动类型 ： <任何活动 类型> |  |  |
| 4 | 使用位置 | 选择所需成本中心，然后选择 使用位置 - 活动 类型 。 | 显示当前使用活动类型的报表。就详细情况而言， 可以选择主数据对象类型并进一步钻取。 |  |

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
- related-to :: [[06-management-accounting/criar-tipo-de-atividade-e-hierarquia-de-tipo-de-atividade-mds-bnn-644]]
- related-to :: [[06-management-accounting/leistungsart-und-leistungsartenhierarchie-anlegen-sds-bnn-640]]
- related-to :: [[06-management-accounting/master-data-script-create-activity-type-and-activity-type-hierarchy-bn]]
- related-to :: [[06-management-accounting/mds-bnn-643]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 8,850 chars in the whole document
