---
id: 13-quality-ehs-and-compliance/mds-bny-693
title: 创建物料/产品主数据的质量管理属性 - MDS (BNY) (BNY_S4CLD2608_Master_Data_ZH_XX)
description: "Master data script (Chinese, machine-translated) for maintaining Quality Management views of material master data via MM01, incl. inspection type setup."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/qm-material-master-attributes]
aliases: [BNY_S4CLD2608_Master_Data_ZH_XX]
keywords: [Quality Management View of the Material Master, quality management data, inspection types, material master data, automatic usage decision, quality info records, master data scripts, BNY]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-693
topic: 13-quality-ehs-and-compliance/qm-material-master-attributes
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建物料/产品主数据的质量管理属性 - MDS (BNY) (BNY_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Quality Management View of the Material Master** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建物料/产品主数据的质量管理属性 - MDS (BNY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233898078)

[2 前提条件 3](#_Toc233898079)

[2.1 系统访问 3](#_Toc233898080)

[2.2 角色 3](#_Toc233898081)

[2.3 所需组织单位 3](#_Toc233898082)

[3 概览表 4](#_Toc233898083)

[4 测试过程 5](#_Toc233898084)

[4.1 物料的质量管理属性 5](#_Toc233898085)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

如果物料质量需要检验，前提条件是质量 维护相应工厂的物料主数据管理视图。

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

### 所需组织单位

在本部分中，您将描述并解释与创建相关的所有组织单位 主数据记录。

客户主数据的一些段取决于 公司，常规（中央）数据不依赖于组织单位或公司 代码。下表提供了这些不同数据段及其 相关组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 质量管理 | 工厂 |  | 对于企业的每个工厂标识，都可以存在工厂数据 使用物料主记录的结构。 | 工厂： |

## 概览表

此范围项目由下列流程步骤组成： 表：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [物料的质量管理属性](#unique_7) [第 ] 页 5 | 主数据专家 - 产品数据 | 创建物料 (MM01) | 创建物料主数据 - 质量管理数据。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 物料的质量管理属性

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
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建物料 (MM01) 。 | 应用随即打开。 |  |
| 3 | 输入物料数据 | 在 创建物料（初始屏幕） 屏幕上，输入以下内容：材料 ： <物料 编号>物料类型 ： 贸易 货物按下 输入 。 | 因此， 选择视图 屏幕。 |  |
| 4 | 选择质量管理视图 | 在 选择视图 屏幕上，选择 质量 管理 视图并选择 组织 级别 。 | 随即显示用于组织数据输入的新屏幕。 |  |
| 5 | 输入组织级别数据 | 在 组织级别 屏幕的 组织级别 部分中，输入以下内容并选择 继续 ：工厂 ： <工厂 代码> | 因此， 创建物料…（贸易货物） 屏幕。 |  |
| 6 | 输入质量管理数据 | 在 创建物料 <XXX>（贸易货物） 屏幕上的 质量管理 标签上，输入物料描述：描述 ： <输入描述>在 中 常规数据 部分，位于 质量管理 标签上，输入以下内容：基本计量单位 ： <计量单位>选择 检验设置 。在显示的对话框中，选择 创建检验类型 并输入以下内容：检验类型 ：例如， 01 。首选检验类型 ： X激活 ： X选择 检验类型确定 查看详细信息。确保以下字段被标记为 X ：过账到检验库存使用任务清单检验自动分配检验特征选择 继续 。 |  |  |
| 7 | 启用/禁用自动使用决策（可选） | 选择或取消选择 自动使用决策 启用或禁用此物料和检验类型组合的自动使用决策。备注 可以为具有正检验结果的检验批次制定结果记录后的自动使用决策。要启用此功能 处理，您的系统必须在 管理您的解决方案 (F1241) 请查阅[SAP 帮助](https://help.sap.com/viewer/DRAFT/84dbf30eedb4450983dc3d1c81b71996/1811.500/en-US/746b66d98e504e238eca043bae05ecb8.html) 获取更多技术信息和前提条件。 |  |  |
| 8 | 输入采购数据（可选） | 如果要选择性地为物料使用质量信息记录，请在 质量管理 选项卡（ 采购数据 部分，进行以下操作 条目：QM 采购激活 ： X质量管理控制代码 ：例如， 0001 。 |  |  |
| 9 | 保存数据 | 选择 保存 。 | 您的数据已保存。 |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-quality-management-attributes-for-material-product-master-mds-b]]
- related-to :: [[13-quality-ehs-and-compliance/criar-atributos-de-administracao-de-qualidade-para-mestre-de-materiais]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-691]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-datos-maestros-crear-atributos-de-gestion-de-calidad-para-ma]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 5,808 chars in the whole document
