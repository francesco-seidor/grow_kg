---
id: 14-maintenance-service-and-projects/mds-5mh-465
title: 创建维护工作中心 - MDS (5MH) (5MH_S4CLD2608_Master_Data_ZH_XX)
description: 主数据脚本（中文机器翻译）：在 SAP S/4HANA Cloud Public Edition 中通过 CR01 创建工厂维护工作中心的测试步骤。
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/maintenance-work-centers]
aliases: [5MH_S4CLD2608_Master_Data_ZH_XX]
keywords: [Maintenance Work Centers, maintenance work center, work center category, master data scripts, standard value key, capacity planning, costing data, business roles, 5MH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-465
topic: 14-maintenance-service-and-projects/maintenance-work-centers
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建维护工作中心 - MDS (5MH) (5MH_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Maintenance Work Centers** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建维护工作中心 - MDS (5MH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897719)

[2 前提条件 3](#_Toc233897720)

[2.1 系统访问 3](#_Toc233897721)

[2.2 角色 3](#_Toc233897722)

[2.3 所需组织单位 3](#_Toc233897723)

[2.4 必填和可选主数据 4](#_Toc233897724)

[2.5 数据创建的主要参数 4](#_Toc233897725)

[2.5.1 工作中心类别 4](#_Toc233897726)

[3 概览表 5](#_Toc233897727)

[4 过程 6](#_Toc233897728)

[4.1 创建维护工作中心 6](#_Toc233897729)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何创建维护工作中心主数据的描述 SAP S/4HANA 系统的数据记录。该描述包括的数据段 与主数据相关，以便在“常规”系统环境中工作。阅读器 主要了解哪些数据段和字段通常需要使用输入填充。 值。与 S/4HANA 内容交付范围无关的字段 本文档中未介绍 SAP Best Practices，尽管它们可能出现在 用户界面 (UI)。

按照此处所述创建的维护工作中心主记录可用于： 维护流程。

## 前提条件

本部分汇总创建工作中心的所有前提。

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
| 生产工程师 - 离散制造 | SAP_BR_PRODN_ENG_DISC | 生产工程 - 离散制造 | SAP_BR_PRODN_ENG_DISC |

### 所需组织单位

主数据的一些段取决于公司的组织单位， 常规 （中央）数据不取决于组织单位或公司代码。因此， 下表提供了这些不同数据段及其相关 组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有数据 | 工厂 |  | 工作中心的所有数据取决于工厂。 | 工厂：––––-- |

### 必填和可选主数据

工作中心数据记录可能参考其他主数据。下表提供了概览 在 工作中心中使用的可选和强制主数据对象。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 标准值码 | 在工作中心屏幕中， 基本数据 选项卡， 在标准值维护中查找标准值键值的条目 节。 | 必填 | 系统使用标准值作为参数（来源标准） 公式中的值用于计算执行时间，能力需求 和成本。使用标准值代码分配参数标识。 至标准值。此参数标识用于标识标准值 在公式中。您可以使用参数标识来确定关键字。 用于标准值，例如安装、机器或人工。 |

### 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录，并且始终需要创建维护工作中心：

#### 工作中心类别

工作中心类别确定哪些数据可以在 工作中心。工作中心可按其类别进行区分（例如， 生产工作中心、维护工作中心、服务工作中心等。）

表 2：

| 工作中心类别 | 描述 |
| --- | --- |
| 0005 | 工厂维护 |

## 概览表

此范围项目由表中列出的多个流程步骤组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建维护工作中心](#unique_10) [第 ] 页 6 | SAP_BR_PRODN_ENG_DISC | 创建工作中心 (CR01) | 已创建工作中心。 |

## 过程

本部分介绍属于此范围项目的每个流程步骤的过程。 您还可以使用这些过程测试主数据创建。

### 创建维护工作中心

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
| 1 | 登录 | 登录到 SAP Fiori 快速启动板 SAP_BR_PRODN_ENG_DISC 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建工作中心 (CR01) 。 | 随即打开一个新窗口，显示 创建工作中心：初始屏幕 。 |  |
| 3 | 输入工厂代码 | 输入 工厂代码 ： <1010> | 因此， 创建组织 屏幕是 显示。 |  |
| 4 | 输入工作中心标识 | 输入工作中心标识： <RES-0100>备注 工作中心标识的字段长度小于 8。 |  |  |
| 5 | 工作中心类别 | 选择工作中心类别： <0005> 工厂 维护 |  |  |
| 6 | 选择基本数据 | 选择 基本数据 左上方的 按钮 屏幕角。 | 随即显示创建工作中心：基本数据屏幕。 |  |
| 7 | 输入工作中心描述、选择负责人、用途和标准 值键值 | 在 基本数据 标签上，输入以下内容 数据：描述 ：例如， RES-0100负责人 ：例如， <YMM> 工厂维护技工 主管用法 ：例如， <004> 仅维护任务 列表标准值码 ：例如， <SAP0> 无标准 值 |  |  |
| 8 | 输入控制代码 | 选择 缺省值 标签上，输入 以下数据：控制代码 ：例如， <YBM1> 工厂 维护 - 内部 。 |  |  |
| 9 | 设置容量公式和其他公式 | 在 产能 标签上，输入以下内容 数据：产能类别 ：例如， <002> 人员其他公式 ：例如， <YBPM01> 项目:RqmtsNetwkMai | 选择回车。创建工作中心产能：抬头屏幕 出现。 |  |
| 10 | 设置工作中心产能 | 在工作中心产能：抬头部分，输入以下数据：产能类别描述 ：例如， 机械 容量产能负责人 ：例如， <A> 计划员 组 A工厂日历 ：您所在国家/地区的 ID 日历，例如 <01> 德国 标准容量基本单位 ：例如， <H> 小时起始时间 ：例如， <06:00:00>结束时间 ：例如， <14:30:00>间休长度 ：例如， <00:30:00>产能利用率 ：例如， <100>单项产能数 ：例如， <10>长期计划 ： <X> | 选择回车。屏幕返回到产能概览。 |  |
| 11 | 输入计划数据 | 在 计划 标签上，输入以下内容 数据：产能类别 ：例如， <002> 人员 |  |  |
| 12 | 输入成本核算数据 | 在 成本核算 标签页，输入 以下数据：起始日期 ：例如， <2015 年 1 月 1 日>成本中心 ：例如， < 10101701> 工厂和维护 DE作业类型内部处理 ： 用于 示例， <11> 人员 小时成本核算的公式代码 ： 用于 示例， <YBPM01> 项目：需求网络维护 |  |  |
| 13 | 保存数据 | 保存您的输入 | 条目已保存。 |  |

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
- related-to :: [[14-maintenance-service-and-projects/create-maintenance-work-center-mds-5mh-461]]
- related-to :: [[14-maintenance-service-and-projects/criar-centro-de-trabalho-de-manutencao-mds-5mh-464]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-463]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-crear-puesto-de-trabajo-de-mantenimiento-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 6,637 chars in the whole document
