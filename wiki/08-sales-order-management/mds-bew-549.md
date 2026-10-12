---
id: 08-sales-order-management/mds-bew-549
title: 创建赠品条件 - MDS (BEW) (BEW_S4CLD2608_Master_Data_ZH_XX)
description: Chinese (machine-translated) master data script BEW for creating free goods conditions in sales via Manage Free Goods - Sales (VBN2) in S/4HANA Cloud 2608.
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/free-goods]
aliases: [BEW_S4CLD2608_Master_Data_ZH_XX]
keywords: [Free Goods and Free-of-Charge Delivery, free goods conditions, master data script, pricing conditions, sales orders, business roles, condition key combinations, BEW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-549
topic: 08-sales-order-management/free-goods
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建赠品条件 - MDS (BEW) (BEW_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Free Goods and Free-of-Charge Delivery** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建赠品条件 - MDS (BEW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897871)

[2 前提条件 3](#_Toc233897872)

[2.1 系统访问 3](#_Toc233897873)

[2.2 角色 3](#_Toc233897874)

[2.3 必填和可选主数据 3](#_Toc233897875)

[3 概览表 5](#_Toc233897876)

[4 测试过程 6](#_Toc233897877)

[4.1 创建赠品条件 6](#_Toc233897878)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

业务上下文

一些客户可能会在购买特定金额时免费收货。A 赠品条件允许为特定客户维护此协议 和物料。用于销售订单事务中。

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
| 定价专家 | SAP_BR_PRICING_SPECIALIST | 价格管理 | SAP_BR_PRICING_SPECIALIST |  |

### 必填和可选主数据

下表提供了要使用的可选和强制主数据对象的概览。 创建定价条件时。

如果已安装 SAP Best Practices baseline package，则可以使用基线包 样本数据或添加自己的主数据（根据需要）：

| 主数据对象 | 在数据段中使用 | 必填/可选 | 示例值 | 备注 |
| --- | --- | --- | --- | --- |
| 销售组织 | 初始屏幕 | 必填 | <销售组织编号> |  |
| 分销渠道 | 初始屏幕 | 必填 | <分销渠道编号> |  |
| 客户 | 初始屏幕 | 必填 | <客户编号> |  |
| 材料 | 初始屏幕 | 可选 | 例如 TG11 |  |

|  |
| --- |
| 记住 主数据值的示例值为国家/地区特定， baseline package 示例数据为支持的提供本地化值 国家/地区。 |

## 概览表

创建赠品条件 - MDS 包含下列流程步骤： 表：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | SAP Fiori 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建赠品条件](#unique_7) [第 ] 页 6 | 定价专家 | 管理赠品 - 销售 (VBN2) | 创建赠品条件记录。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建赠品条件

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程描述了创建定价条件。

|  |
| --- |
| 记住 主数据值的示例值是国家/地区特定的。 替换 提供的国家/地区特定值 SAP S/4HANA Cloud Public 版本 系统或使用为此创建的主数据值， 目的。 |

过程

| 测试步骤 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 随即显示 SAP Fiori 快速启动板。 | 随即显示 SAP Fiori 快速启动板。 |
| 2 | 访问 SAP Fiori 应用 | 打开 管理赠品 - 销售 (VBN2) 。 | 新视图打开，显示 更改免费货物 确定 。 |  |
| 3 | 定价条件类型 | 在 中 更改免费货物确定 视图，输入以下信息：折扣类型 ：例如， YA00按下 输入 。 | 因此， 更改免费货物 SD (YA00)：选择 视图随即打开。 |  |
| 4 | 组合键 | 客户/物料然后选择 选择 。 |  |  |
| 5 | 选择 | 在 中 更改赠品 SD (YA00)： 选择 视图中，输入以下内容 信息：销售组织 ： <公司 代码>分销渠道 ：例如， 10客户 ： <客户 编号>生效日期 ： <日期>选择 执行 。 | 更改免费货物 SD (YA00) 视图。 |  |
| 6 | 更改价格条件 | 在 中 更改免费货物 SD (YA00) 屏幕上，输入数据 如下：材料 ：例如， TG11最小数量 ：例如， 1,000对于 ：例如， 500单位 ：例如， PC附加数量 ：例如， 10附加数量单位 ：例如， PC计算类型 ：例如， 1免费货物 ：例如， 1 | 已维护赠品条件。 |  |
| 7 | 保存 | 选择 保存 。 | 保存赠品条件。 |  |

关键字组合：销售组织/分销渠道/价格组/物料

| 测试步骤 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 随即显示 SAP Fiori 快速启动板。 | 随即显示 SAP Fiori 快速启动板。 |
| 2 | 访问 SAP Fiori 应用 | 打开 管理赠品 - 销售 (VBN2) 。 | 新视图打开，显示 更改免费货物确定 。 |  |
| 3 | 定价条件类型 | 在 中 更改免费货物确定 视图中，输入以下信息：折扣类型 ：例如， YA00按下 输入 。 | 因此， 更改免费货物 SD (YA00)：选择 视图随即打开。 |  |
| 4 | 组合键 | 销售组织/分销渠道/价格组/物料然后选择 选择 |  |  |
| 5 | 选择 | 在 中 更改免费货物 SD (YA00)：选择 视图中，输入以下信息：销售组织 ： <公司代码>分销渠道 ：例如， 10价格组 ： <价格组>生效日期 ： <日期>选择 执行 。 | 更改免费货物 SD (YA00) 视图。 |  |
| 6 | 更改价格条件 | 在 中 更改免费货物 SD (YA00) 屏幕上，输入以下数据：材料 ：例如， TG11最小数量 ：例如， 1,000对于 ：例如， 500单位 ：例如， PC附加数量 ：例如， 10附加数量单位 ：例如， PC计算类型 ：例如， 1免费货物 ：例如， 1 | 已维护赠品条件。 |  |
| 7 | 保存 | 选择 保存 。 | 保存赠品条件。 |  |

关键字组合：销售组织/分销渠道/物料

| 测试步骤 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 随即显示 SAP Fiori 快速启动板。 | 随即显示 SAP Fiori 快速启动板。 |
| 2 | 访问 SAP Fiori 应用 | 打开 管理赠品 - 销售 (VBN2) 。 | 新视图打开，显示 更改免费货物确定 。 |  |
| 3 | 定价条件类型 | 在 中 更改免费货物确定 视图中，输入以下信息：折扣类型 ：例如， YA00按下 输入 。 | 因此， 更改免费货物 SD (YA00)：选择 视图随即打开。 |  |
| 4 | 组合键 | 销售组织/分销渠道/物料然后选择 选择 。 |  |  |
| 5 | 选择 | 在 中 更改免费货物 SD (YA00)：选择 视图中，输入以下信息：销售组织 ： <公司代码>分销渠道 ：例如， 10生效日期 ： <日期>选择 执行 。 | 更改免费货物 SD (YA00) 视图。 |  |
| 6 | 更改价格条件 | 在 中 更改免费货物 SD (YA00) 屏幕上，输入以下数据：材料 ：例如， TG11最小数量 ：例如， 1,000对于 ：例如， 500单位 ：例如， PC附加数量 ：例如， 10附加数量单位 ：例如， PC计算类型 ：例如， 1免费货物 ：例如， 1 | 已维护赠品条件。 |  |
| 7 | 保存 | 选择 保存 。 | 保存赠品条件。 |  |

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
- related-to :: [[08-sales-order-management/criar-condicao-de-bonificacao-em-mercadoria-mds-bew-548]]
- related-to :: [[08-sales-order-management/master-data-script-create-free-goods-condition-mds-bew-545]]
- related-to :: [[08-sales-order-management/mds-bew-547]]
- related-to :: [[08-sales-order-management/naturalrabattkondition-anlegen-sds-bew-544]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BEW_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 7,040 chars in the whole document
