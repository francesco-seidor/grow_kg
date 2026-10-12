---
id: 06-management-accounting/mds-bnh-609
title: 创建利润中心 - MDS (BNH) (BNH_S4CLD2608_Master_Data_ZH_XX)
description: Chinese (machine-translated) master data script (MDS BNH) for creating a profit center via Manage Profit Centers - Old Version (F3516) in SAP S/4HANA Cloud 2608.
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/profit-centers]
aliases: [BNH_S4CLD2608_Master_Data_ZH_XX]
keywords: [Profit Centers and Profit Center Reorganization, profit center, master data script, controlling area, profit center group, segment reporting, validity periods, business roles, BNH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-609
topic: 06-management-accounting/profit-centers
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建利润中心 - MDS (BNH) (BNH_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Profit Centers and Profit Center Reorganization** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建利润中心 - MDS (BNH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897925)

[2 前提条件 3](#_Toc233897926)

[2.1 系统访问和角色 3](#_Toc233897927)

[2.2 所需组织单位 3](#_Toc233897928)

[2.3 必填和可选主数据 4](#_Toc233897929)

[2.4 数据创建的主要参数 5](#_Toc233897930)

[3 概览表 6](#_Toc233897931)

[4 测试过程 7](#_Toc233897932)

[4.1 创建利润中心主数据 7](#_Toc233897933)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

利润中心是会计中的组织单位，反映 组织以管理为导向的结构，以实现内部控制。 通过将公司划分为利润中心，可以确定内部利润 职责范围，以及将职责委派给分散的单位。

利润中心的主数据包括利润中心的名称， 其分配到的成本控制范围，以及利润中心的有效期 作为利润中心、利润中心的负责人的信息 分配到标准层次结构的节点，以及通信所需的数据 （地址、电话号码等）。

## 前提条件

本部分汇总了执行系统、用户、主数据、组织数据、其他测试数据和业务条件方面测试的所有前提条件。

### 系统访问和角色

在以下系统中执行测试：

| 系统 | 明细 |
| --- | --- |
| SAP S/4HANA Cloud Public 版本 | 系统标识： ###客户端： ### |

使用 SAP 提供的以下业务角色模板创建业务角色，并将其分配给各个测试用户。

或者，如果可用，您可以使用 SAP 提供的以下空间。创建包含预定义基本应用的页面的空间，并将其分配到业务角色。然后将此业务角色分配给单个用户。

有关详细信息，请参阅 如何从模板创建业务角色 （在[产品帮助](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) 对于 SAP S/4HANA Cloud Public 版本 。

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） | 登录 |
| --- | --- | --- | --- | --- |
| 部门会计 | SAP_BR_DIVISION_ACCOUNTANT | 分部会计 | SAP_BR_DIVISION_ACCOUNTANT |  |

### 所需组织单位

客户主数据的某些细分取决于公司的组织单位，常规（中央）数据不取决于组织单位或公司代码。下表提供了这些不同数据段及其相关组织单位的概览：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 利润中心基本数据 | 成本控制范围利润中心组细分 | 名称、长文本、有效期、负责用户、负责人 | 利润中心组允许控制员通过提供组名称（而不是单个利润中心名称，例如，在定制或报表中）按组寻址利润中心。在报表中，这允许分析聚合级别的成本控制关键指标。段通常不显式过账。数据从科目分配对象（如利润中心）派生。反过来，利润中心通常不会明确过账。数据从初级科目分配对象（如成本中心、内部订单等）派生。 | 成本控制范围：____________利润中心组：____________细分：____________ |
| 利润中心公司代码分配 | 公司代码 | 公司代码 | 对于使用利润中心主记录的企业结构的每个公司代码标识，都可以存在公司代码数据。 | 公司代码：____________ |

### 必填和可选主数据

下表提供了要在利润中心主数据记录中使用的可选和必填主数据对象的概览。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 成本控制范围 | 利润中心基本数据 | 必填 | 参考成本控制范围可用于创建新利润。 center。 |
| 利润中心 | 利润中心基本数据 | 必填 | 参考利润中心可用于创建新利润。 center。 |
| 有效自 | 利润中心基本数据 | 必填 |  |
| 有效期至 | 利润中心基本数据 | 必填 |  |
| 名称 | 利润中心基本数据 | 必填 |  |
| 长文本 | 利润中心基本数据 | 可选 |  |
| 负责用户 | 利润中心基本数据 | 可选 |  |
| 负责人 | 利润中心基本数据 | 必填 |  |
| 利润中心组 | 利润中心基本数据 | 必填 |  |
| 部门 | 利润中心基本数据 | 可选 |  |
| 细分 | 利润中心基本数据 | 可选 | 如果利润中心对美国公司有效，我们建议填充 段字段；通过这种方式，可以执行段报告。 |
| 计划模板 | 利润中心基本数据 | 可选 |  |
| 地址和通讯字段 | 利润中心地址和通讯数据 | 全部为可选 |  |

### 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录且 始终需要 创建利润中心主数据 数据记录：

成本控制范围：A000

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [创建利润中心主数据](#unique_8) [第 ] 页 7 | 部门会计 | 管理利润中心 - 旧版本 (F3516) | 随即打开一个新窗口，显示 利润中心的主数据 屏幕。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建利润中心主数据

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 部门会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理利润中心 - 旧版本 (F3516) 。 | 因此， 利润中心的主数据 屏幕。 |  |
| 3 | 搜索利润中心 | 搜索利润中心。选择 执行 。 | 屏幕上将显示利润中心清单。 |  |
| 4 | 添加利润中心 | 选择 创建 。 | 因此， 利润中心：新 屏幕。 |  |
| 5 | 输入新利润中心数据 | 在 中 新利润中心 部分，输入 以下数据：利润中心 ： <名称> ，例如， YBXXX备注 最大长度为 10 个字符。请勿使用特殊 个字符，如 %、！、$、&、@ 等。他们将导致 应用崩溃，无法删除。有效自 ： <有效期自 日期>有效期至 ： <有效期至 日期>名称 ： <任意 描述>负责人 ： <名称 负责人> |  |  |
| 6 | 输入基本数据 | 在 组织单位 标签上，输入 以下数据：标准层次结构节点 ： <利润中心组>细分 ： <段> |  |  |
| 7 | 公司代码分配 | 选中或取消选中复选框以将公司代码分配到新利润中心。 |  |  |
| 8 | 保存数据 | 保存输入内容。 |  |  |
| 9 | 设置新的有效期（可选） | 选择 编辑 。在您创建的利润中心中，选择 有效期 > 新有效期 。为 有效自 以及 有效期至 字段，并选择源数据 期间。选择 创建 。备注 如果新有效期与现有有效期重叠， 重叠时间将从当前期间排除。如果新有效期与其他期间之间存在间隙， 系统将阻止此操作。 |  |  |
| 10 | 更改时间相关字段（可选） | 您可以更改新创建的 中的以下时间相关字段 有效期。部门PC 负责人负责用户标题名称名称 2名称 3名称 4锁定标识选择 保存 。备注 如果修改与时间无关的字段，更改将 适用于所有有效期。如果新期间与先前期间之间没有差异，或者 则新期间将与现有 一个。 | 随即创建新的有效期。变更记录显示在 更改日志 部分。 |  |

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
- related-to :: [[06-management-accounting/create-profit-center-mds-bnh-605]]
- related-to :: [[06-management-accounting/mds-bnh-607]]
- related-to :: [[06-management-accounting/profitcenter-anlegen-sds-bnh-604]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-lucro-mds-bnh-608]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 6,679 chars in the whole document
