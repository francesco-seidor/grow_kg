---
id: 14-maintenance-service-and-projects/mds-5to-489
title: 为项目创建服务产品 - MDS (5TO) (5TO_S4CLD2608_Master_Data_ZH_XX)
description: "Master data script (Chinese, machine-translated) for creating a service product master record 'Project' via MM01, usable in solution orders, SAP S/4HANA Cloud 2"
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [5TO_S4CLD2608_Master_Data_ZH_XX]
keywords: [Solution Orders and SAP CPQ Quotations, service products, product master data, sales organization data, profit center, solution orders, master data scripts, 5TO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-489
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 为项目创建服务产品 - MDS (5TO) (5TO_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 为项目创建服务产品 - MDS (5TO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897727)

[2 前提条件 3](#_Toc233897728)

[2.1 系统访问 3](#_Toc233897729)

[2.2 角色 3](#_Toc233897730)

[2.3 所需组织单位 3](#_Toc233897731)

[2.4 必需和运营主数据 4](#_Toc233897732)

[3 概览表 5](#_Toc233897733)

[4 测试过程 6](#_Toc233897734)

[4.1 创建服务产品 - 项目 6](#_Toc233897735)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您可以找到有关如何创建包含价格的服务产品主数据记录的描述。该描述包括与主数据相关的数据段，以便在“常规”系统环境中工作。读取器主要学习哪些数据段和字段通常需要使用输入值填充。此文档不描述与范围无关的字段，尽管这些字段可能显示在 UI 上。

按此处描述创建的服务产品主记录可用于解决方案订单。

| 服务产品标识 | 描述 | 用法 |
| --- | --- | --- |
| 项目 | 项目 | 表示项目 |

## 前提条件

### 系统访问

| 系统 | 明细 |
| --- | --- |
| 系统 | 可通过 SAP Fiori 快速启动板访问。系统管理员为您提供用于访问分配给您的角色的各种应用的 URL。 |

### 角色

使用 SAP 提供的以下业务角色模板创建业务角色，并将其分配给各个测试用户。

或者，如果可用，您可以使用 SAP 提供的以下空间。创建包含预定义基本应用的页面的空间，并将其分配到业务角色。然后将此业务角色分配给单个用户。

有关详细信息，请参阅 如何从模板创建业务角色 （在[产品帮助](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) 对于 SAP S/4HANA Cloud Public 版本 。

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） |
| --- | --- | --- | --- |
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST | 主数据 - 产品 | SAP_CMD_SP_PR_MAINT |

### 所需组织单位

主数据的某些段取决于公司的组织单位，常规（中央）数据不取决于组织单位或公司代码。下表提供了这些不同数据段及其相关组织单位的概览：

| 数据段 | 取决于 | 用于美国的组织单位 | 要用于 DE 的组织单位 |
| --- | --- | --- | --- |
| 创建物料 | 销售组织 | 1710（国内销售组织 - US） | 1010（德国国内销售组织） |
| 创建物料 | 分销渠道 | 10（直销） | 10（直销） |

### 必需和运营主数据

物料主数据记录可能参考其他主数据。下表提供了要在物料主数据记录中使用的可选和必填主数据对象的概览。

|  |
| --- |
| 备注 需要巴西特定字段才能获得正确的税收计算。支票 巴西发票 - JD0 中的 定义 BR 特定字段 主数据 章节（针对物料主数据）。 |

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 利润中心 |  | 必填 | 需要将利润中心分配到物料（产品）主数据 用于正确的评估流程。 |

## 概览表

此主记录由下表中提供的多个段组成。

如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。

您可以使用搜索栏找到主页上不包含的所有其他应用。

如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 设置 > 应用查找器 。

| ID（角色模板） | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| 创建服务产品 | SAP_BR_PRODMASTER_SPECIALIST | 创建物料 (MM01) | 已创建服务产品。 |

## 测试过程

本部分介绍作为此主记录一部分的每个段或流程步骤的过程。

### 创建服务产品 - 项目

目的

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品 数据 (MDG) 。 |  |  |
| 2 | 访问 SAP Fiori 应用 | 选择 创建物料 (MM01) 磁贴。 | 因此， 创建物料（初始屏幕） 是 显示。 |  |
| 3 | 维护物料基本数据（针对服务产品） ) | 在 创建物料（初始屏幕） 输入以下内容：物料： 项目物料类型： 服务 产品然后选择 继续（回车） 。 | 您已维护新服务产品的基本信息。因此， 选择视图 对话 窗口。 |  |
| 4 | 选择视图 | 在 选择视图基本数据 1 视图，然后 选择 继续（回车） 。 | 因此， 创建物料项目 视图为 显示。 |  |
| 5 | 维护基本数据 | 在 基本数据 1 视图中，维护以下 值：描述： 项目 个项目基本单位 度量： AU（活动） UNIT）材料 组： P001 （服务）GenItemGroup： SPRJ （项目）然后选择 保存 。 | 维护基本数据并保存服务产品。之后 保存， 创建物料（初始屏幕） 视图为 显示。对于贵公司使用的每种不同语言， 产品的相应描述必须按语言维护。 代码！ |  |
| 6 | 扩展产品详细信息 | 在 创建物料（初始屏幕） 视图、 输入物料 项目 ，然后选择 继续（回车） 。 | 因此， 选择视图 对话窗口是 显示。 |  |
| 7 | 选择视图 | 在 选择视图 对话窗口中，选择 以下视图：销售：销售组织数据 1销售：销售组织数据 2然后选择 继续 （输入） 。 | 因此， 组织级别 对话窗口是 显示。 |  |
| 8 | 选择组织级别 | 在 组织级别 窗口中，维护 以下值：销售组织： 1710 （国内销售组织 (US)分销 渠道： 10（直销）然后 选择 继续（回车） 。 | 已选择组织数据。因此， 创建 物料 项目 视图。 |  |
| 9 | 维护销售组织数据 (1) | 在 销售：销售组织 1 视图，维护 以下值：常规 数据现金 折扣： X <已选择>税务数据税收 分类： 1（全额税）然后 选择 输入 。 | 已维护销售组织数据。因此， 销售：销售 组织 2 标签页。 |  |
| 10 | 维护销售组织数据 (2) | 在 销售：销售组织 2 视图，维护 以下条目：项目类别 group： SPRJ（项目）然后选择 输入 。然后选择 保存 。 | 已维护销售组织数据。因此， 销售： 常规/工厂 标签页。 |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 5,912 chars in the whole document
