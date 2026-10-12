---
id: 14-maintenance-service-and-projects/mds-5mi-471
title: 创建测量点 - MDS (5MI) (5MI_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script for creating measuring points and counters (EAMS_WDA_MP_OIF), incl. category M configuration."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/measuring-points-and-counters]
aliases: [5MI_S4CLD2608_Master_Data_ZH_XX]
keywords: [Measuring Points and Counters, measuring points, measuring counters, measuring point category, condition-based maintenance, business configuration, technical objects, business roles, master data scripts, 5MI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-471
topic: 14-maintenance-service-and-projects/measuring-points-and-counters
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建测量点 - MDS (5MI) (5MI_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Measuring Points and Counters** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建测量点 - MDS (5MI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897704)

[2 前提条件 3](#_Toc233897705)

[2.1 系统访问 3](#_Toc233897706)

[2.2 角色 3](#_Toc233897707)

[2.3 所需组织单位 3](#_Toc233897708)

[2.4 必填和可选主数据 4](#_Toc233897709)

[2.5 数据创建的主要参数 4](#_Toc233897710)

[2.5.1 测量点类别 4](#_Toc233897711)

[3 概览表 7](#_Toc233897712)

[4 过程 8](#_Toc233897713)

[4.1 创建测量点 8](#_Toc233897714)

[4.2 创建测量计数器 10](#_Toc233897715)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您可以找到有关如何创建测量点主数据的描述 S/4HANA 系统的 记录。该描述包括以下数据段： 与主数据相关以在“常规”系统环境中工作。阅读器主要包括 了解通常需要使用输入值填充的数据段和字段。 与 SAP Best 提供的 S/4HANA 内容范围无关的字段 本文档中未描述实践，尽管它们可能出现在用户上 接口 (UI)。

## 前提条件

本部分汇总创建测量点的所有前提条件。

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
| 主数据专家 - 维护管理 | SAP_BR_MD_SPECIALIST_EAM | 主数据 - 维护管理 | SAP_EAM_SPT_MD_SPECIALIST_PC |

### 所需组织单位

主数据的某些段取决于公司的组织单位。 常规（中央）数据不取决于组织单位或公司代码。 下表提供了不同数据段及其相关 的概览。 组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### 必填和可选主数据

测量点数据记录可能参考其他主数据。下表提供了 要在测量中使用的可选和强制主数据对象的概览。 积分。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 技术对象 |  | 必填 | 设备或功能位置。 |
| 特征 |  | 必填 | 特征描述对象的属性。的值 characteristic 指定属性。 |

### 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录，并且始终需要用于创建测量点。

#### 测量点类别

测量点类别确定哪些数据可以在 的主记录中维护 测量点。在系统中通过测量点 区分测量点 类别。每个测量点类别都由代码标识，这是第一件事 在系统中创建测量点时将其分配到测量点。

表 2：

| 测量点类别 | 描述 |
| --- | --- |
| M | 计量点 (一般) |

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

此活动的目的是配置测量点类别。

过程

根据 SAP S/4HANA Cloud Public Edition 的配置环境， 选择以下选项之一：

配置您的解决方案 ：

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板 作为 配置专家 - 业务流程配置 。 | 因此， SAP Fiori 快速启动板 显示 。 |  |
| 2 | 访问应用 | 打开 管理您的解决方案 （ F1241 ）。 | 管理您的解决方案 屏幕是 显示。 |  |
| 3 | 打开配置您的解决方案 | 选择 配置您的解决方案 。备注 要为预期本地版本创建国家/地区相关设置，请选择 设置本地版本 。选择应用程序范围作为 资产管理选择子应用程序范围作为 维护管理选择项目名称为 主数据 | 配置您的解决方案屏幕。 |  |
| 4 | 打开“定义测量点类别” | 低于 配置步骤 ，选择步骤名称“ 定义测量点类别 ”并单击 配置 | 测量点类别 屏幕将显示 |  |
| 5 | 启用 CBM 的条件（可选） | 选择测量点类别“M”输入 计量范围 消息为“W”勾选复选框 创建通知单击 保存 | 已建立 CBM 的条件 |  |

SAP Central Business Configuration

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录到 SAP Fiori 快速启动板 配置专家 - 业务流程 配置 。 | 因此， SAP Fiori 快速启动板 显示 。 |  |
| 2 | 访问应用 | 打开 实施活动 | 因此， 管理您的解决方案 屏幕是 显示。 |  |
| 3 | 访问配置 | 要在树视图中查找活动，请单击搜索图标并 选择扩展的 搜索 选项输入节点文本/活动描述： " 定义 测量点类别 ”，然后单击 继续 | 随即显示树视图中的活动。 |  |
| 4 | 打开“定义测量点类别” | 低于 配置步骤 ，选择步骤 名称 " 定义测量点类别 " 并单击 配置 | 测量点类别 屏幕将 显示 |  |
| 5 | 启用 CBM 的条件（可选） | 选择测量点类别“M”输入 计量范围 消息为“W”勾选复选框 创建 通知单击 保存 | 已建立 CBM 的条件 |  |

## 概览表

此范围项目由表中列出的多个流程步骤组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建测量点](#unique_10) [第 ] 页 8 | SAP_BR_MD_SPECIALIST_EAM | 创建测量点 (EAMS_WDA_MP_OIF) 应用 | 已创建测量点。 |

## 过程

本部分介绍属于此范围项目的每个流程步骤的过程。您 还可以使用这些过程测试主数据创建。

### 创建测量点

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
| 1 | 登录 | 登录到 SAP Fiori 快速启动板 作为主数据专家 SAP_BR_MD_SPECIALIST_EAM 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建测量点 (EAMS_WDA_MP_OIF) 应用。 | 随即打开一个新窗口，显示 创建测量点 屏幕。 |  |
| 3 | 输入详细信息 | 输入以下内容：测量点/计数器 ： <测量点>参考对象类型 ： <技术对象> | 随即出现一个新屏幕，其中显示参考对象。 |  |
| 4 | 输入参考对象详细信息 | 输入以下内容：技术对象 ： <设备/功能位置编号>按回车键或选择 继续 。 | 创建测量点 |  |
| 5 | 常规数据 | 在 常规数据 部分，输入以下内容：描述 ： <测量点描述>特征 ： 例如，OPERATING_HOUR/PRESSURE测量点类别 ： M（计量点常规） |  |  |
| 6 | 输入目标限制和计数器数据 | 在 目标限制 以及 计数器数据 部分，输入以下内容：目标价值 ： 例如 10 PA范围上限 ： 例如 15 PA范围下限 ： 例如 5 PA |  |  |
| 7 | 输入测量容差（可选） | 在 测量容差部分 ，输入以下内容：测量容差上限 ：例如 12 PA测量容差下限 ：例如，7 PA |  |  |
| 8 | 维护条件（仅针对基于条件的维护） | 在维护条件部分，单击启用条件的复选框，选择任意条件：例如，对于条件：MEASUREMENT READING > UPPER LIMIT输入以下详细信息对象类型 （通知类型）：例如，被动工作优先级 ：选择创建通知所需的优先级，例如 1 非常高激活 ：单击复选框以激活此条件长文本 ：输入要创建的通知的长文本描述 ：输入要创建的通知的描述 |  |  |
| 9 | 检查条目 | 选择 检查条目 。 | 检查条目。 |  |
| 10 | 保存数据 | 保存输入内容。 | 已创建测量点。 |  |

### 创建测量计数器

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
| 1 | 登录 | 登录到 SAP Fiori 快速启动板 作为主数据 专家 SAP_BR_MD_SPECIALIST_EAM 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建测量点 （ EAMS_WDA_MP_OIF ）应用。 | 随即打开一个新窗口，显示 创建测量点 屏幕。 |  |
| 3 | 输入详细信息 | 输入以下内容：测量点/计数器 ： <计数器>参考对象类型 ： <技术对象> | 随即出现一个新屏幕，其中显示参考对象。 |  |
| 4 | 输入参考对象 | 输入以下内容：技术对象 ： <设备/功能位置编号>按下 输入 或选择 继续 。 | 创建测量点（计数器） 屏幕打开。 |  |
| 5 | 输入基本信息 | 在 常规数据 部分，输入以下内容：描述 ： <计量计数器描述>测量点类别 ： M（计量点常规）特征 ：例如， OPERATING_HOUR/PRESSURE | 常规数据已维护 |  |
| 6 | 输入目标限制和计数器数据 | 在 目标限制和计数器数据 部分，输入以下内容：溢出读数 ： <计数器溢出读数>年度估算 ： <技术对象的年度估算>测量范围单位 | 已维护目标限制 |  |
| 7 | 检查条目 | 选择 检查条目 。 | 检查条目。 |  |
| 8 | 保存数据 | 保存输入内容。 | 已创建测量点。 |  |

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
- related-to :: [[14-maintenance-service-and-projects/5mi-469]]
- related-to :: [[14-maintenance-service-and-projects/crear-punto-de-medicion-mds-5mi-468]]
- related-to :: [[14-maintenance-service-and-projects/create-measuring-point-mds-5mi-467]]
- related-to :: [[14-maintenance-service-and-projects/criar-ponto-de-medicao-mds-5mi-470]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 8,301 chars in the whole document
