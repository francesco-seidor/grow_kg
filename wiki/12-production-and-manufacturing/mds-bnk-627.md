---
id: 12-production-and-manufacturing/mds-bnk-627
title: 创建生产和销售物料清单 - MDS (BNK) (BNK_S4CLD2608_Master_Data_ZH_XX)
description: Chinese (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script for creating production (usage 1) and sales (usage 5) BOMs with change number.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/material-boms]
aliases: [BNK_S4CLD2608_Master_Data_ZH_XX]
keywords: [Material BOMs for Production and Sales, bill of materials, production bom, sales bom, change numbers, bom usage, bom item categories, business roles, master data scripts, routings]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-627
topic: 12-production-and-manufacturing/material-boms
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建生产和销售物料清单 - MDS (BNK) (BNK_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Material BOMs for Production and Sales** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建生产和销售物料清单 - MDS (BNK) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897946)

[2 前提条件 3](#_Toc233897947)

[2.1 系统访问 3](#_Toc233897948)

[2.2 角色 3](#_Toc233897949)

[2.3 所需组织单位 3](#_Toc233897950)

[2.4 必填和可选主数据 4](#_Toc233897951)

[2.5 数据创建的主要参数 4](#_Toc233897952)

[2.5.1 物料清单用途 4](#_Toc233897953)

[3 概览表 5](#_Toc233897954)

[4 测试过程 6](#_Toc233897955)

[4.1 创建更改编号 6](#_Toc233897956)

[4.2 创建生产物料清单 7](#_Toc233897957)

[4.3 创建销售物料清单 10](#_Toc233897958)

[5 附录 12](#_Toc233897959)

[5.1 后续流程：创建工艺路线 12](#_Toc233897960)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

生产物料清单是生产的组件的正式结构化清单。 产品或装配（产品的一部分）。清单包含对象号 以及数量和计量单位。组件可能是 原材料或表示装配的半成品物料。

它在 MRP 运行中用于计算物料需求和事务，例如 生产订单。信息特定于生产站点（称为工厂）。

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
| 物料清单工程师 | SAP_BR_BOM_ENGINEER | 物料清单 | SAP_BR_BOM_ENGINEER |  |

### 所需组织单位

贵公司的组织结构和主数据已在您的 系统。组织结构反映您的 公司。主数据代表物料、客户和供应商，例如， 具体取决于公司的运营重点。

使用您自己的主数据或以下示例数据进行测试。 过程。

### 必填和可选主数据

物料清单数据记录可能参考其他主数据。下表概述了 要在 BOM 中使用的可选和强制主数据对象

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 材料 | 在 中 创建物料 BOM：初始屏幕 以及 创建 物料 BOM：一般项目视图， 输入 物料编号 中的 材料 和组件 。 | 必填 | 在开始流程之前，请完成以下主数据脚本作为前提条件 步骤：创建“原材料”类型的产品主数据 - MDS (BNR)创建“半成品”类型的产品主数据 - MDS （BNS）创建“成品”类型的产品主数据 - MDS （BNT）创建“贸易货物”类型的产品主数据 - MDS (BNF) |

### 数据创建的主要参数

在本部分中，我们将介绍一些影响主记录行为的基本参数，并且始终需要这些参数来创建物料清单：

#### 物料清单用途

物料清单 (BOM) 用途定义了物料的范围（如销售或生产） 可以使用物料清单。

| 物料清单用途 | 描述 |
| --- | --- |
| 1 | 生产 |
| 5 | 销售和分销 |

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建更改编号](#unique_10) [第 ] 页 6 | 物料清单工程师 | 创建变更主数据 (CC01) |  |
| [创建生产物料清单](#unique_11) [第 ] 页 7 | 生产工程师 - 离散制造 | 维护物料清单（版本 2） - 创建、更改和显示物料清单 (F1813A) |  |
| [创建销售物料清单](#unique_12) [第 ] 页 10 | 生产工程师 - 离散制造 | 维护物料清单 - 创建、更改和显示物料清单 (F1813) |  |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建更改编号

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

创建变更主数据，用于在生产和物料清单的后续步骤中创建物料清单。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 物料清单工程师 。 |  |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建变更主数据 (CC01) 。 |  |  |
| 3 | 输入更改编号 | 在 创建更改主数据：初始屏幕 屏幕上，输入以下数据并按 输入 。更改编号 ： <输入更改编号，例如：CN001>保留其他字段中的缺省值。 |  |  |
| 4 | 输入更改主数据 | 在 创建更改主数据：更改抬头 屏幕上，输入以下示例提供的数据并按 输入 ：旁边的字段 更改编号 ： 更改制造物料清单的主数据有效自 ： 今天更改编号状态 ： 01 已激活 |  |  |
| 5 | 选中物料清单复选框 | 在 创建变更主数据：对象类型 屏幕， 对象类型 表， 物料清单 行中，选中以下复选框：激活对象管理记录 |  |  |
| 6 | 选择保存 | 选择 保存 。 | 创建变更主数据。 |  |

### 创建生产物料清单

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
| 2 | 访问 SAP Fiori 应用 | 打开 维护物料清单（版本 2） - 创建、更改和显示物料清单 (F1813A) 。 |  |  |
| 3 | 创建物料清单 | 选择 创建物料清单 . 在 上 创建物料清单 屏幕上，输入以下内容 数据并选择 确定 。材料 ： <成品/半成品物料 编号>更改编号 ： <您的更改 在上一步骤中创建的编号>工厂 ： <您的 工厂>物料清单用途 ： 1（用于生产 仅） |  |  |
| 4 | 添加组件数据 | 在 中 部件 部分，选择 添加 图标以添加一个或多个 components。项目类别项目类别 ： <L 表示 库存项目>组件 ： <物料编号， 原始/半成品>数量 ： <数量>组件计量单位 ： PC | 已添加组件数据。 |  |
| 5 | 输入物料清单项目类别非库存 (‘N’) | 在 中 部件 部分，选择 添加 图标以添加一个或多个组件。项目类别项目类别 ： <N 表示非库存 项目>组件 ： <物料编号，原材料/半成品 产品>组件数量 ： <数量>组件计量单位 ： PC按下 输入 启用 组件 以及 组件 数量 字段。备注 此项目类别用于未存储在库存中的组件，非库存项目 可以在物料清单中输入（含或不含主数据） record。 | 添加非库存项目的组件数据。 |  |
| 6 | 输入物料清单项目类别可变大小 (‘R’) | 在 中 部件 部分，选择 添加 图标以添加一个或多个组件。项目类别项目类别 ： < R 表示可变大小 项目>组件 ： <物料编号，原材料/半成品 产品>选择箭头打开 明细 页面。在 可变大小项目数据 进行所需输入。大小 1 ： <输入可变大小的维度 项目>大小 2 ： <输入可变大小的维度 项目>大小 3 ： <输入可变大小的维度 项目>尺寸单位 ： <输入您的计量单位， 可变尺寸项目数量>公式代码 ： <输入要计算的公式 可变大小项目>可变大小项目数 ： <数量>可变尺寸项目数量 ： <计算的数量 用于可变大小项目>选择 应用 。备注 利用此项目类别，您可以指定不同大小的组件部分， 一种物料，例如所需的钢板尺寸 修复一些种植园。 | 已添加/计算可变项目的组件数据。 |  |
| 7 | 输入物料清单项目类别文本项目 (‘T’) | 对于新 物料清单项目编号 行，进行类似于以下内容的输入 以下示例：个项目 类别 ： 文本 项目在 中 物料清单项目 编号 第 行，选择箭头打开 明细 页面。在 上 维护物料清单 - 基本 详细信息 屏幕，组件 数量 ： 1组件计量单位 ： PC选择 状态/长文本 标签以显示 项目文本 。个项目 文本 ： 文档 | 已添加文本项目的文本文档数据。 |  |
| 8 | 检查抬头 | 在 中 抬头属性 部分，您可以 检查数据并根据需要进行更改。 |  |  |
| 9 | 保存数据 | 保存输入内容。 | 消息 已保存物料 BOM 随即显示。 |  |

### 创建销售物料清单

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
| 2 | 访问 SAP Fiori 应用 | 选择 维护物料清单 - 创建、更改和显示物料清单 (F1813) 。 |  |  |
| 3 | 创建物料清单 | 选择 创建物料清单 . 在 创建物料清单 屏幕上，输入以下数据并选择 确定 。材料 ： <物料清单抬头物料编号> ，例如， SDBOMERLAHD 或 SDBOMLUMFHD工厂 ： <输入您的工厂>更改编号 ： <您在上一步中创建的更改编号>物料清单用途 ： 5 |  |  |
| 4 | 添加组件数据 | 在 中 部件 部分，选择 添加 图标以添加一个或多个组件。项目类别项目类别 ： <L 代表库存项目>组件 ： <物料编号，贸易货物>数量 ： <数量> | 已添加组件数据。 |  |
| 5 | 检查抬头 | 在 中 抬头属性 部分，您可以检查数据并根据需要进行更改。 |  |  |
| 6 | 保存数据 | 保存输入内容。 | 随即显示已保存物料清单消息。 |  |

## 附录

### 后续流程：创建工艺路线

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 工艺路线 |  |  | 要执行此活动，请完成 创建工艺路线 - MDS （BNL） 测试 script。 |

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
- related-to :: [[12-production-and-manufacturing/bom-mds-bnk-625]]
- related-to :: [[12-production-and-manufacturing/crear-lista-de-materiales-para-material-para-produccion-y-ventas-mds-b]]
- related-to :: [[12-production-and-manufacturing/create-material-bom-for-production-and-sales-mds-bnk-623]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-lista-tecnica-de-materiais-para-producao]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 8,535 chars in the whole document
