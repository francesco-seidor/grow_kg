---
id: 03-financial-accounting-and-close/sepa-mds-bnv-687
title: 创建 SEPA 授权 - MDS (BNV) (BNV_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script to create, display, list and manage SEPA mandates (FSEPA_M1/M3/M4, F5158)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/direct-debit-and-sepa-mandates]
aliases: [BNV_S4CLD2608_Master_Data_ZH_XX]
keywords: [Direct Debit and SEPA Mandates, sepa mandates, sepa direct debit, display sepa mandates, sepa mandate list, manage sepa mandates, accounts receivable, business roles, master data scripts, BNV]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-687
topic: 03-financial-accounting-and-close/direct-debit-and-sepa-mandates
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建 SEPA 授权 - MDS (BNV) (BNV_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Direct Debit and SEPA Mandates** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建 SEPA 授权 - MDS (BNV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233898015)

[2 前提条件 3](#_Toc233898016)

[2.1 系统访问 3](#_Toc233898017)

[2.2 角色 3](#_Toc233898018)

[2.3 所需组织单位 3](#_Toc233898019)

[2.4 必填和可选主数据 4](#_Toc233898020)

[2.5 数据创建的主要参数 4](#_Toc233898021)

[3 概览表 5](#_Toc233898022)

[4 测试过程 6](#_Toc233898023)

[4.1 创建 SEPA 授权 6](#_Toc233898024)

[4.2 显示 SEPA 授权 7](#_Toc233898025)

[4.3 显示 SEPA 授权清单 8](#_Toc233898026)

[4.4 管理 SEPA 授权 9](#_Toc233898027)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何为您的 创建单一欧元支付区 (SEPA) 授权的描述 SAP S/4HANA Cloud Public 版本 系统。该描述包括与 SAP S/4HANA Cloud Public 版本 设备。与 范围无关的字段 SAP S/4HANA Cloud Public 版本 交付日期 SAP Best Practices 在此中未描述 文档。

SEPA 授权由债务人（客户采购货物或服务）完成，用于授权债权人（零售商或服务） 提供者）通过 SEPA 直接借记收款。同时，SEPA 授权包括债务人银行的权限 支付这些收款。

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
| 应收账款会计 | SAP_BR_AR_ACCOUNTANT | 应收账款 | SAP_BR_AR_ACCOUNTANT |  |

### 所需组织单位

客户主数据的一些段取决于 公司，常规（中央）数据不依赖于组织单位或公司 代码。下表提供了这些不同数据段及其 相关组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 授权 | 业务伙伴 | 客户编号、IBAN 和 SWIFT/BIC | 仅对使用 SEPA 直接付款的欧洲客户有效 Debit。 | 客户编号： <您的编号 |
| 授权 | 公司代码 | 公司代码 | 对于您的每个公司代码标识，都可以存在公司代码数据 使用 SEPA 授权的企业结构。 | 公司代码：您的代码 |

### 必填和可选主数据

下表提供了以下可选和必填主数据对象的概览： 用于利润中心主数据记录中。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 客户编号 | 初始屏幕 | 必填 |  |
| 公司代码 | 初始屏幕 | 必填 |  |

### 数据创建的主要参数

本部分介绍一些基本参数，这些参数会影响主记录的行为，并且始终需要创建 SEPA 授权：

公司代码：

例如， XX10 。

业务伙伴 - 客户：

例如，客户编号 XX100003 。

## 概览表

此范围项目由下列流程步骤组成： 表：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | SAP Fiori 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建 SEPA 授权](#unique_9) [第 ] 页 6 | 应收账款会计 | 创建 SEPA 授权 (FSEPA_M1) | 已创建 SEPA 授权。 |
| [显示 SEPA 授权](#unique_10) [第 ] 页 7 | 应收账款会计 | 显示 SEPA 授权 (FSEPA_M3) | 显示 SEPA 授权。 |
| [显示 SEPA 授权清单](#unique_11) [第 ] 页 8 | 应收账款会计 | 显示 SEPA 授权清单 (FSEPA_M4) | 显示 SEPA 授权清单。 |
| [管理 SEPA 授权](#unique_12) [第 ] 页 9 | 应收账款会计 | 管理 SEPA 授权 (F5158) | 显示 SEPA 授权。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建 SEPA 授权

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
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 应收账款会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建 SEPA 授权 (FSEPA_M1) 。 | 应用随即打开。 |  |
| 3 | 切换应用程序 | 在 创建托管：初始屏幕 屏幕上，选择 切换应用程序。选择财务 会计 （在 选择应用程序 对话框并选择 继续 。 |  |  |
| 4 | 付款方编号 | 在 中 客户 字段中，输入 XX100003 。 |  |  |
| 5 | 收款方标识 | 在 中 付款公司代码 字段中，输入 XX10 并按 输入 继续。备注 如果显示具有已激活状态的授权屏幕，则表示已创建这些授权。选择授权，然后选择 继续 检查和更改授权书。 | 因此， 创建授权：详细信息屏幕 屏幕。 |  |
| 6 | 补充数据 | 选择 补充数据 。 | 字段将自动填充。 |  |
| 7 | 基本数据 | 在 基本数据 标签上，输入以下内容：状态 ： 已输入B2B 授权复选框 ： 选择签名的位置 ： <位置>签名日期 ： <日期> |  |  |
| 8 | 付款方 | 在 付款方 选项卡（ 付款方的银行数据 部分，验证 IBAN 和 SWIFT/BIC 字段已填充。备注 此数据是客户主数据的一部分，并且 应该已经创建并可用。 |  |  |
| 9 | 收款方 | 在 收款方 标签上，输入以下内容：债权人标识 ： <债权人标识> |  |  |
| 10 | 保存数据 | 保存输入内容。 | 系统消息 已创建授权 0000000000## 随即显示。 |  |

### 显示 SEPA 授权

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

前提条件

授权已存在。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 应收账款会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 显示 SEPA 授权 (FSEPA_M3) 。 | 应用随即打开。 |  |
| 3 | 付款方编号 | 在 中 客户 字段中，输入 XX100003 。 |  |  |
| 4 | 收款方标识 | 在 中 付款公司代码 字段中，输入 XX10 并按 输入 继续。 | 因此， 显示授权：明细屏幕 屏幕。 |  |
| 5 | 导航 | 选择不同的标签：基本数据 ， 付款方 ， 和/或 收款方 。 | 随即显示信息。 |  |
| 6 | 返回 | 选择 退出 。 |  |  |

### 显示 SEPA 授权清单

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

前提条件

授权已存在。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 应收账款会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 显示 SEPA 授权清单 (FSEPA_M4) 。 | 应用随即打开。 |  |
| 3 | 选择执行 | 如果显示对话框，请选择 财务 会计 （在 选择 应用程序 对话框，然后选择 继续 。如果未显示对话框，请检查 技术 选择 标签，并验证 应用程序 字段设置为 财务会计 。选择 执行 。 | 因此， 授权 屏幕，显示现有授权清单。 |  |
| 4 | 选择授权 | 选择 授权参考编号 。 | 因此， 更改授权 屏幕上，列出所选授权的详细信息。 |  |
| 5 | 审核 | 虽然可以在需要时更改授权数据，但不要更改任何数据，只需检查授权数据。 |  |  |
| 6 | 退出 | 选择 继续 两次，或选择 取消 退出。 |  |  |

### 管理 SEPA 授权

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

前提条件

授权已存在。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 应收账款会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理 SEPA 授权 (F5158) 。 | 应用随即打开。 |  |
| 3 | 选择授权 | 在 中 应用程序 字段中），选择 财务 会计 。 |  |  |
| 4 | 选择授权 | 在 中 付款公司代码 字段中，输入 XX10 。选择 执行 。选择要编辑的行，然后选择 编辑 。 | 因此， 更改授权：详细信息 屏幕。 |  |
| 5 | 审核并编辑 | 检查并编辑以下选项卡中的任何可用字段：基本数据付款方收款方 |  |  |
| 6 | 保存您的输入 | 选择 保存 保存您的输入。 |  |  |

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
- related-to :: [[03-financial-accounting-and-close/crear-mandato-sepa-mds-bnv-684]]
- related-to :: [[03-financial-accounting-and-close/create-sepa-mandate-mds-bnv-683]]
- related-to :: [[03-financial-accounting-and-close/criar-mandato-sepa-mds-bnv-686]]
- related-to :: [[03-financial-accounting-and-close/sepa-mandat-anlegen-sds-bnv-682]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 8,349 chars in the whole document
