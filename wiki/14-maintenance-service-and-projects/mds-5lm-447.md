---
id: 14-maintenance-service-and-projects/mds-5lm-447
title: "主数据脚本: 创建功能位置 - MDS (5LM) (5LM_S4CLD2608_Master_Data_ZH_XX)"
description: "Chinese (machine-translated) master data script 5LM for creating a functional location structure (one top-level, two sub-locations) in SAP S/4HANA Cloud Public Edition 2608."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/functional-locations]
aliases: [5LM_S4CLD2608_Master_Data_ZH_XX]
keywords: [Functional Locations, technical objects, master data scripts, structure indicator, maintenance planning, maintenance work centers, cost centers, business roles, 5LM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-447
topic: 14-maintenance-service-and-projects/functional-locations
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 主数据脚本: 创建功能位置 - MDS (5LM) (5LM_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Functional Locations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建功能位置 - MDS (5LM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897698)

[2 前提条件 3](#_Toc233897699)

[2.1 系统访问 3](#_Toc233897700)

[2.2 角色 3](#_Toc233897701)

[2.3 所需组织单位 3](#_Toc233897702)

[2.4 必填和可选主数据 4](#_Toc233897703)

[2.5 数据创建的主要参数 4](#_Toc233897704)

[2.5.1 结构标识 4](#_Toc233897705)

[2.5.2 技术对象类别 5](#_Toc233897706)

[3 概览表 6](#_Toc233897707)

[4 过程 7](#_Toc233897708)

[4.1 创建功能位置 7](#_Toc233897709)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您可以找到有关如何创建功能位置主数据的详细过程 SAP S/4HANA 系统的数据记录。它包括与以下内容相关的数据段： 主数据在常规系统环境中工作。本文档还提供 有关哪些数据段和字段需要输入值的信息。

与 SAP S/4HANA 内容交付范围无关的字段 尽管最佳实践可能出现在用户上，但本文档中未对其进行描述 接口 (UI)。按此处描述创建的功能位置可用于： 维护流程。

## 前提条件

本部分汇总了创建功能所需的所有前提条件。 位置。

### 系统访问

应使用以下系统执行测试：

表 1：

| 系统 | 明细 |
| --- | --- |
| 系统 | 可通过 SAP Fiori 快速启动板访问。您的系统管理员 为您提供访问分配给您的 role。 |

### 角色

使用 SAP 提供的以下业务角色模板创建业务角色，并将其分配给各个测试用户。

或者，如果可用，您可以使用 SAP 提供的以下空间。创建包含预定义基本应用的页面的空间，并将其分配到业务角色。然后将此业务角色分配给单个用户。

有关详细信息，请参阅 如何从模板创建业务角色 （在[产品帮助](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) 对于 SAP S/4HANA Cloud Public 版本 。

| 名称（角色模板） | ID（角色模板） | 名称（空格） | 标识（空格） |
| --- | --- | --- | --- |
| 维护计划员 | SAP_BR_MD_SPECIALIST_EAM | 维护计划员 | SAP_EAM_SPT_MD_SPECIALIST_PC |

### 所需组织单位

主数据的某些段取决于公司的组织单位。常规 （中央）数据不取决于组织单位或公司代码。因此， 下表概述了不同的数据段及其相关的 组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有数据 | 工厂 |  | 功能位置的所有数据取决于工厂。 | 工厂：__________ |

### 必填和可选主数据

功能位置数据记录可能参考其他主数据。下表提供了 要在功能中使用的可选和强制主数据对象的概览。 位置。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 维护工作中心 | 在功能位置用户界面 (UI) 中， 组织数据 tab，找到维护工作中心的条目 责任部分。 | 可选 | 系统使用维护工作中心作为参数来确定某些值，例如 如安装、机器或人工。 |
| 成本中心 | 在功能位置用户界面 (UI) 中， 组织 数据 标签上，您可以在以下位置找到成本中心的条目： 责任部分。 | 可选 | 系统使用成本中心作为成本核算的参数。 |

### 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录，并且始终需要用于创建功能位置：

#### 结构标识

功能位置的结构标识确定 功能位置标签。它建立了以下因素：

- 技术系统的层次结构级别数
- 级别的键值长度
- 分隔符（连字符）

表 2：

| 结构标识 | 描述 |
| --- | --- |
| YBPM | 最佳实践的结构标识 |

#### 技术对象类别

这是显示功能位置类别的代码。

表 3：

| 技术对象类别 | 描述 |
| --- | --- |
| M | 技术系统 - 标准 |

## 概览表

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建功能位置](#unique_11) [第 ] 页 7 | SAP_BR_MD_SPECIALIST_EAM | 创建技术对象 (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2) | 已创建功能位置。 |

## 过程

### 创建功能位置

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此测试步骤中，维护一个由以下内容组成的功能位置结构： 最高级别的功能位置和两个下级功能位置。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板 作为 主数据专家 SAP_BR_MD_SPECIALIST_EAM 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建技术对象 (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2) 。 | 随即打开一个新窗口，显示创建技术对象：初始 屏幕。 |  |
| 3 | 创建功能位置 | 在 创建技术对象 屏幕， 选择技术对象类型：功能位置。在下一屏幕中，输入以下内容：技术对象类型 ： 功能位置结构标识 ： YBPM（最佳流程的结构标识） 练习）技术对象 ： <例如 1711 >技术对象类别 ： M（技术 系统标准）选择 继续 。 |  |  |
| 4 | 维护常规数据 | 在 创建技术对象：1711 屏幕，在 常规数据 部分， 输入以下内容：描述 ： <例如，空气压缩机 1 工厂 >（可选）维护更多常规数据，然后导航到 位置数据 部分。 | 随即显示创建技术对象：常规数据屏幕。 |  |
| 5 | 维护位置数据 | 在 中 位置数据 部分，输入 以下：维护工厂 ： <例如，1710 代表 US>备注 属于相同结构的技术对象必须全部。 分配了相同的工厂。或者，您可以 将所有技术的工厂信息留空 objects。（可选）维护更多详细信息，例如地址 信息。 | 随即显示创建技术对象：位置数据屏幕。 |  |
| 6 | 维护组织数据 | 在 中 组织数据 部分，输入 以下内容：计划工厂 ： <例如，1710 代表 US>维护工作中心 ： <例如 RES-0100 美国>成本中心 ： <例如，<例如， 17101701 表示 US>或者，您可以维护附加信息，例如合作伙伴 信息，依此类推 组织 数据 部分。 | 创建技术对象：组织数据屏幕 出现。 |  |
| 7 | 保存功能位置 | 或者，您可以维护其他 节。单击 检查条目 按钮。选择 保存 。然后导航回主页屏幕。 | 已创建功能位置。 |  |
| 8 | 创建次级功能 地点 | 要维护功能位置结构，请按描述进行操作 在上述步骤中，并维护以下功能 位置：技术对象 ： 1711-001描述 ： <针对 示例，压缩机 # 1 >在 中 位置数据 部分，输入 以下：位置 ： <例如， YB_1701>厂区 ： YOH在 中 组织数据 部分， 维护以下条目：计划员组 ： <例如，920 代表 US>计划工厂 ： <例如，1710 代表 US>维护工作中心 ： <例如 RES-0100 美国>工作中心工厂 ： <例如，1710 代表 US>目录参数文件 ： <例如，YB-PM0003 代表美国 >或者，您可以在其他位置维护附加信息 节。选择 检查条目 按钮。选择 保存 。输入以下内容：技术对象 ： 1711-002描述 ： <针对 示例，压缩机 # 2 >在 中 位置数据 部分，输入 以下：位置 ： < 针对 示例，YB_1702>厂区： <YOH>在 中 组织数据 部分， 维护以下条目：计划员组 ： <针对 示例，920 代表 US>计划工厂 ： <针对 例如，1710 代表 US>维护工作 居中： <例如， 美国 RES-0100>工作中心工厂 ： <例如，1710 代表 US>目录参数文件 ： <例如，YB-PM0003 代表美国 >或者，您可以维护其他 节。单击 检查条目 按钮。选择 保存 。 | 创建下级功能位置。 |  |
| 9 | 检查资产中的技术对象 查看器 | 在主页页面，选择 显示技术 对象 磁贴。在 显示技术对象 屏幕， 维护相关技术对象，例如 1711，然后 选择 继续 。检查功能位置结构和详细信息，根据 技术对象，选择 您还可以： 显示 资产查看器中的技术对象 。 |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-ubicacion-tecnica-mds-5lm-es-444]]
- related-to :: [[14-maintenance-service-and-projects/create-functional-location-mds-5lm-443]]
- related-to :: [[14-maintenance-service-and-projects/mds-5lm-445]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-local-de-instalacao-mds-5lm-446]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 7,180 chars in the whole document
