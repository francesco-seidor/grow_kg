---
id: 11-inventory-warehouse-and-transportation/mds-bnz-699
title: 创建新的未清物料管理过账期间 - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script BNZ: close the MM period and open a new posting period with the Close Periods app (MMPV)."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/mm-posting-periods]
aliases: [BNZ_S4CLD2608_Master_Data_ZH_XX]
keywords: [MM Posting Periods, posting periods, period closing, master data scripts, materials management, inventory valuation, control record, product master data, business role templates, fiori launchpad access]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-699
topic: 11-inventory-warehouse-and-transportation/mm-posting-periods
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建新的未清物料管理过账期间 - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **MM Posting Periods** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建新的未清物料管理过账期间 - MDS (BNZ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233898042)

[2 前提条件 3](#_Toc233898043)

[2.1 系统访问 3](#_Toc233898044)

[2.2 角色 3](#_Toc233898045)

[3 概览表 4](#_Toc233898046)

[4 测试过程 5](#_Toc233898047)

[4.1 关闭 MM 期间并打开新过账期间 5](#_Toc233898048)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

有关物料库存和特定评估数据的信息，例如总库存值、总库存、评估元素类、价格 控制标识和价格单位由财务过账期间持有。必须在每个新过账开始时设置期间。 确保价值和货物移动过账到正确期间的期间。通常，只有当前过账期间对于 过账。所有其他过账期间均关闭。

仅当在控制记录中设置相应标志时，才能重新过账到上一期间。此标志自动 在初始化时和每次期间更改后设置。但是，在某些情况下，可能需要手动设置该标识。

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
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST | 主数据 - 产品 / 产品治理 | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [关闭 MM 期间并打开新过账期间](#unique_6) [第 ] 页 5 | 主数据专家 - 产品数据 | 关闭期间 (MMPV) | 过账期间为最新。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 关闭 MM 期间并打开新过账期间

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 关闭期间 (MMPV) 。备注 如果找不到 关闭期间 磁贴中，从 Fiori 快速启动板右上方的下拉列表中， 选择 磁贴目录 。根据 主数据 - 管理 组、 导航到 关闭期间 磁贴并将其添加到 我的主页 group。 | 应用随即打开。 |  |
| 3 | 输入选择数据 | 在 关闭物料主数据期间 记录 屏幕上，输入以下内容：从公司代码 ： <您的公司代码>到公司代码 ： <您的公司代码>期间 ： <打开期间>会计年度 ： <当前会计年度>检查并关闭期间 ： 已选择备注 在 中 期间 字段中，为月份输入两位数字。例如，一月等于 01 ，10 月等于 10 ，以此类推。如果要打开当前期间，请输入后续期间的当前月份。 |  |  |
| 4 | 选择执行 | 在 关闭物料主记录的期间 屏幕上，选择 执行 。 |  |  |
| 5 | 检查结果 | 如果日志显示 控制记录的当前期间（月/年）为 <您输入的期间/年度> ，您 可以在此处停止。备注 如果过账期间仍在过去，则按期间重复上述步骤，直到达到正确（当前）的步骤。对于 例如，显示的期间为 04 2014 ，但您想打开 12 2015 无法直接执行此操作。相反，您需要打开 05 2014 下一个期间，然后 06 2014 等，直到达到当前 period。如果要关闭过去一年的库存期间，可能会在以下位置显示系统消息： 步骤 3，指示您正在打开/关闭过去一年的某个期间。您需要确认此系统 message。 | 过账期间为最新。 |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/crear-nuevo-periodo-contable-mm-abierto-mds-bnz-696]]
- related-to :: [[11-inventory-warehouse-and-transportation/create-new-open-mm-posting-period-mds-bnz-695]]
- related-to :: [[11-inventory-warehouse-and-transportation/criar-periodo-contabil-mm-aberto-mds-bnz-698]]
- related-to :: [[11-inventory-warehouse-and-transportation/mm-mds-bnz-697]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 5,398 chars in the whole document
