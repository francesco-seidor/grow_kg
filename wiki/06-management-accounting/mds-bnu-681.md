---
id: 06-management-accounting/mds-bnu-681
title: 创建成本核算运行 - MDS (BNU) (BNU_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script BNU: create and execute a product costing run in app F1865 as Inventory Accountant."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [BNU_S4CLD2608_Master_Data_ZH_XX]
keywords: [Product Costing Runs and Standard Cost Updates, costing run, product cost estimate, master data scripts, costing variant, business roles, organizational units, test procedures, price update, BNU]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-681
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建成本核算运行 - MDS (BNU) (BNU_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建成本核算运行 - MDS (BNU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233898024)

[2 前提条件 3](#_Toc233898025)

[2.1 系统访问 3](#_Toc233898026)

[2.2 角色 3](#_Toc233898027)

[2.3 所需组织单位 3](#_Toc233898028)

[2.4 必填和可选主数据 4](#_Toc233898029)

[2.5 数据创建的主要参数 4](#_Toc233898030)

[2.5.1 成本核算变式 4](#_Toc233898031)

[3 概览表 6](#_Toc233898032)

[4 测试过程 7](#_Toc233898033)

[4.1 创建成本核算运行 7](#_Toc233898034)

[4.2 执行成本核算运行 8](#_Toc233898035)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

本文档包含作为前提条件必须完成的流程步骤，您才能 开始完成所选物流场景的标准测试脚本。

在本文档中，您将找到有关如何创建和执行产品成本核算的描述 运行用于公司/工厂的物料。目的是计划成本 不参考订单的物料，并为物料和其他成本设置价格 会计对象。

您可以使用“产品成本计划”来分析公司产品的成本， 作为：

- 制造物料
- 服务
- 其他无形商品

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
| 成本会计 - 库存 | SAP_BR_INVENTORY_ACCOUNTANT | 库存会计 | SAP_BR_INVENTORY_ACCOUNTANT |  |

### 所需组织单位

要创建成本核算运行，您需要指定 成本控制范围 和 公司代码 。

|  |
| --- |
| 备注 在 中 要使用的组织单位 列中，输入数据段的值 这与您的系统环境相关。例如，对于公司代码：10 = 德国，17 = 美国 |

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 成本核算数据 | 成本控制范围 |  |  | 成本控制范围：____________ |
|  | 公司代码 |  |  | 公司代码：__________ |
| 选择 | 工厂 |  |  | 工厂：__________ |

### 必填和可选主数据

物料清单数据记录可能参考其他主数据。下表概述了 要在物料清单中使用的可选和必填主数据对象。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 材料 | 创建成本估算 > 流步骤 > 选择 | 必填 | 通常，指定物料类型以指示 物料成本核算运行应创建产品成本核算。 |
| 生产主数据（物料清单、工艺路线、工作中心等）。 | 在 中 创建成本估算 流步骤 结构 展开 | 可选（或）必填 | 如果制造的产品用于成本核算运行（用于 例如，物料类型为 "FERT"（成品）或 "HALB" 的产品 （半成品），这些产品具有一种物料清单， 在成本核算运行中展开。同时，工艺路线是 从工作中心、分配的成本中心和 使用的活动类型，以及成本率针对 计算最终成本核算数据。 |

### 数据创建的主要参数

在本部分中，我们将介绍一些影响主记录行为的基本参数，并且始终需要这些参数来创建物料清单：

#### 成本核算变式

成本核算变式 定义应用程序和定制之间的链接，因为所有成本 参考成本核算变式执行和保存估算。

| 成本核算变式 | 描述 | 备注 |
| --- | --- | --- |
| PYC1 | 成本估算标准 | 此成本核算变式用于为所选 创建标准产品成本估算 materials。根据结果，物料评估数据将 已更新。 |

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用名称 | 预期结果 |
| --- | --- | --- | --- |
| [创建成本核算运行](#unique_10) [第 ] 页 7 | 成本会计 - 库存 | 管理成本核算运行 - 估算成本 (F1865) | 显示含成本核算数据的抬头数据标签。 |
| [执行成本核算运行](#unique_11) [第 ] 页 8 | 成本会计 - 库存 | 管理成本核算运行 - 估算成本 (F1865) |  |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建成本核算运行

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，创建成本核算运行。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 库存 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本核算运行 - 估算成本 (F1865) 。 | 因此， 管理成本核算运行估算成本 视图。 |  |
| 3 | 创建成本核算运行 | 选择 创建 。 | 因此， 创建新成本核算运行 视图。 |  |
| 4 | 输入成本核算运行的参数 | 输入以下条目，然后按 输入 。成本核算运行 ： 测试 1成本核算运行日期 ： <输入当前日期>描述 ： 成本核算运行测试 1成本核算变式 ： PYC1成本核算版本 ： 1成本控制范围 ： A000公司代码 ： 1010成本核算起始日期 ： <当前日期>成本核算截止日期 ： 采用缺省值数量结构日期 ： <当前日期>评估日期 ： <当前日期> |  |  |
| 5 | 保存成本核算运行 | 选择 保存 。 |  |  |

### 执行成本核算运行

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，执行成本核算运行。不包括已配置物料。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 库存 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本核算运行 - 估算成本 (F1865) 。 | 因此， 管理成本核算运行估算成本 视图。 |  |
| 3 | 选择成本核算运行 | 搜索在上一步中创建的成本核算运行，然后单击 条目并选择 编辑 访问 成本核算运行。 |  |  |
| 4 | 打开成本核算运行 | 输入以下内容：成本核算运行 ： 输入在上一步中创建的成本核算运行 并选择 输入 。展开 处理 部分。 |  |  |
| 5 | 创建成本估算 | 在 中 处理 表，每行都有 更改参数 按钮，位于 参数 列中）。选择 选择行，然后输入以下内容：物料类型 ： HALB、ROH、FERT工厂 ： 1010取消选择 后台处理 并选择选项 EXPLO 。保存您的输入并选择 返回 。选择 执行 ，显示在 执行 列中，选择行的状态指示灯变为绿色。 | 执行选择。 |  |
| 6 | 创建成本估算 | 对于 成本核算 行，选择 更改参数 按钮。在 成本核算运行：成本估算 - 更改参数 ，取消选择 后台处理 标识，然后选择 保存 。选择 返回选择 执行 ，显示在 执行 列和 成本核算 行的状态指示灯变为绿色。 | 执行成本核算运行。 |  |
| 7 | 创建成本估算 | 从菜单中，选择 编辑 > 成本核算结果 。如果此行的状态指示灯为红色，则查看成本核算级别报表。更正报表中的错误。要重新运行成本核算（如有必要），请重复结构展开和成本核算行。 | 执行成本核算运行。 |  |
| 8 | 创建成本估算 | 在 分析 行，选择 更改参数 按钮。选择 SAP&11 对于参数设置。在 成本核算运行：分析 - 更改参数 ，取消选择 后台处理 标识，然后选择 保存 。选择 返回 。选择 执行 ，显示在 执行 列中）。 | 执行成本核算运行。 |  |
| 9 | 创建成本估算 | 在 标记 行，选择 锁定 按钮。在 价格更新：组织 度量 屏幕上，选择 公司 代码 ： 1010 。在出现的对话框中，输入成本核算变式 PYC1 和成本核算版本 1 ，然后选择 输入 。行的状态指示灯变为 绿色。选择 返回 。选择 更改 参数 并取消选择 背景 处理 。选择 保存 。选择 返回 ， 并选择 执行 。 | 执行成本核算运行。 |  |
| 10 | 创建成本估算 | 在 发布行 ，选择 更改参数 并取消选择 测试运行 以及 后台处理 。选择 保存 。选择 返回 ，然后选择 执行 。 | 当前价格将在物料主数据中更新。 |  |

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
- related-to :: [[06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678]]
- related-to :: [[06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680]]
- related-to :: [[06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676]]
- related-to :: [[06-management-accounting/master-data-script-create-costing-run-mds-bnu-677]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 7,649 chars in the whole document
