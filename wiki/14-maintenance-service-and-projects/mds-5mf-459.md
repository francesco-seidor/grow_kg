---
id: 14-maintenance-service-and-projects/mds-5mf-459
title: 创建设备 - MDS (5MF) (5MF_S4CLD2608_Master_Data_ZH_XX)
description: 主数据脚本（中文机器翻译）：在 SAP S/4HANA Cloud Public Edition 中创建设备主数据并安装到功能位置。
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/equipment]
aliases: [5MF_S4CLD2608_Master_Data_ZH_XX]
keywords: [Equipment Master Records, equipment master data, technical object category, master data scripts, functional location, maintenance work center, cost center, business roles, 5MF]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-459
topic: 14-maintenance-service-and-projects/equipment
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建设备 - MDS (5MF) (5MF_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Equipment Master Records** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建设备 - MDS (5MF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897749)

[2 前提条件 3](#_Toc233897750)

[2.1 系统访问 3](#_Toc233897751)

[2.2 角色 3](#_Toc233897752)

[2.3 所需组织单位 3](#_Toc233897753)

[2.4 必填和可选主数据 4](#_Toc233897754)

[3 概览表 5](#_Toc233897755)

[4 数据创建的主要参数 6](#_Toc233897756)

[4.1 技术对象类别 6](#_Toc233897757)

[5 过程 7](#_Toc233897758)

[5.1 创建设备 7](#_Toc233897759)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您可以找到有关如何创建设备主数据的详细过程 S/4HANA 系统的 条记录。它包括与 在常规系统环境中工作的主数据。本文档还提供相关信息 关于哪些数据段和字段需要输入值。

与 SAP Best 提供的 S/4HANA 内容范围无关的字段 本文档中未描述实践，尽管它们可能出现在用户上 接口 (UI)。

## 前提条件

本部分汇总了创建设备的所有前提条件。

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

主数据的某些段取决于公司的组织单位。 常规（中央）数据不取决于组织单位或公司代码。 下表提供了不同数据段及其相关 的概览。 组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有数据 | 工厂 |  | 设备的所有数据取决于工厂。 | 工厂：__________ |

### 必填和可选主数据

设备数据记录可能参考其他主数据。下表概述了 要在设备中使用的可选和必填主数据对象。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 维护工作中心 | 在设备主用户界面 (UI) 的组织数据标签中， 在职责中找到维护工作中心的条目 节。 | 可选 | 系统使用维护工作中心作为参数来确定 某些值，例如安装、机器或人工。 |
| 成本中心 | 在设备主用户界面 (UI) 的组织数据标签中， 您可以在职责部分找到成本中心的条目。 | 可选 | 系统使用成本中心作为成本核算的参数。 |

## 概览表

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建设备](#unique_8) [第 ] 页 7 | SAP_BR_MD_SPECIALIST_EAM | 创建技术对象 (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2) | 已创建设备。 |

## 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录，并且始终需要用于创建设备。

### 技术对象类别

可能的用途包括：

- 机械
- 设备
- 生产资源/工具
- 客户设备

表 2：

| 技术对象类别 | 描述 |
| --- | --- |
| M | 机器 |

## 过程

### 创建设备

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此测试步骤中，维护安装在 功能位置。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板 作为 SAP_BR_MD_SPECIALIST_EAM 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建技术对象 (EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2) 。 | 随即打开一个新窗口，显示 创建技术 对象：初始 屏幕。 |  |
| 3 | 创建设备 | 在 创建技术对象 屏幕， 选择技术对象类型：设备。在下一屏幕中，输入以下内容：技术对象类型 ： 设备技术对象 ： 留空有效自 ： 今天 日期技术对象类别 ： M（技术 系统标准）选择 继续 。 |  |  |
| 4 | 维护常规数据 | 在 创建技术对象：<设备标识> 屏幕上的 常规数据 部分，输入 以下：描述 ： 对于 示例，手动隔离阀>对象类型 ： 对于 示例，9400>启动日期 ： 对于 示例，当天日期>制造国家/地区 ： 例如，US>建造月份/年份 ： 例如，04/2011>制造商零件编号 ： 例如，HZZ-TD B4>制造商序列号 ： 例如，HZZ-TD B4/66>购置价值/货币 ： 例如 10,000.00/ USD >购置日期 ： 对于 示例，04/10/2011 >（可选）维护更多常规数据，然后导航到 位置数据 部分。 | 随即显示创建技术对象：常规数据屏幕。 |  |
| 5 | 维护位置数据 | 在 中 位置数据 部分，输入 以下：维护工厂 ： 对于 例如，1710 代表 US>位置 ： 例如， YB_1701 用于 US>厂区 ： 对于 示例，美国为 YOH>备注 属于相同结构的技术对象必须全部。 分配了相同的工厂。或者，您可以 将所有技术的工厂信息留空 objects。（可选）维护更多详细信息，例如地址 信息。 | 随即显示创建技术对象：位置数据屏幕。 |  |
| 6 | 维护组织数据 | 在 中 组织数据 部分，输入 以下内容：计划员组 ： 对于 示例，920 代表 US>计划工厂 ： 例如，1710 代表 US>维护工作中心 ： 例如，RES-0100 表示 US>工作中心工厂 ： 例如，1710 代表 US>成本中心 ： 对于 例如，17101701 用于 US>或者，您可以维护附加信息，例如合作伙伴 组织数据部分中的信息等。 | 创建技术对象：组织数据屏幕 出现。 |  |
| 7 | 保存设备 | 或者，您可以维护其他部分的附加信息。选择 检查条目 按钮。选择 保存 。 | 已创建设备。 |  |
| 8 | 在功能位置安装设备 | 在 更改技术对象：<设备标识> 屏幕上， 导航到 结构 部分。选择 更改结构：安装 。在 更改安装位置 屏幕上，输入以下内容：上级技术对象 ： 例如 < 1710>位置 ： <离开 空>安装日期/时间 ： <保留系统建议>选择 确定 。选择 保存 。 |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/crear-equipo-mds-5mf-456]]
- related-to :: [[14-maintenance-service-and-projects/create-equipment-mds-5mf-455]]
- related-to :: [[14-maintenance-service-and-projects/criar-equipamento-mds-5mf-458]]
- related-to :: [[14-maintenance-service-and-projects/equipment-anlegen-sds-5mf-454]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 6,541 chars in the whole document
