---
id: 13-quality-ehs-and-compliance/ehs-mds-3sr-363
title: 创建 EHS 位置 - MDS (3SR) (3SR_S4CLD2608_Master_Data_ZH_XX)
description: "Master data script (Chinese, machine-translated) for creating EHS locations and assigning them to the location structure via Manage Locations (EHFND_UI_LOC_ENTR"
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-locations]
aliases: [3SR_S4CLD2608_Master_Data_ZH_XX]
keywords: [EHS Locations, location structure, business roles, master data scripts, 3SR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-363
topic: 13-quality-ehs-and-compliance/ehs-locations
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建 EHS 位置 - MDS (3SR) (3SR_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **EHS Locations** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建 EHS 位置 - MDS (3SR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897560)

[2 前提条件 3](#_Toc233897561)

[2.1 系统访问 3](#_Toc233897562)

[2.2 角色 3](#_Toc233897563)

[3 概览表 4](#_Toc233897564)

[4 过程 5](#_Toc233897565)

[4.1 创建 EHS 位置主数据 - 常规数据 5](#_Toc233897566)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

本文档可帮助您在位置结构中创建 EHS 位置。EHS 位置是 中使用的中央主数据对象 环境、健康、 与安全 。创建组织到位置中的 EHS 位置 结构是解决方案初始设置的一部分，位置在 作为解决方案一部分的流程。

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
| 工业卫生师 （事件 经理） | SAP_BR_INDUSTRIAL_HYGIENIST | 工作场所安全 | SAP_BR_INDUSTRIAL_HYGIENIST |  |
| 环境经理 | SAP_BR_EHS_ENV_MGMT | 环境管理 | SAP_BR_EHS_ENV_MGMT |  |
| 变更管理协调员 | SAP_BR_CHG_MGMT_COORDINATOR | 变更管理 | SAP_BR_CHG_MGMT_COORDINATOR |  |

## 概览表

此主记录由下表中提供的多个段组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 细分 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [创建 EHS 位置主数据 - 常规数据](#unique_6) [第 ] 页 5 | 工业卫生师环境经理变更管理协调员 | 管理位置 (EHFND_UI_LOC_ENTRY) | 创建 EHS 位置并将其分配到 EHS 位置结构。 |

## 过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建 EHS 位置主数据 - 常规数据

目的

以下过程提供了创建 EHS 位置和分配 EHS 位置结构。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 使用以下角色之一登录 SAP Fiori 快速启动板：工业卫生师环境经理变更管理协调员 | 显示 SAP Fiori 快速启动板，其中包含相应部分和磁贴 role。 |  |
| 2 | 导航到位置结构 | 打开 管理位置 (EHFND_UI_LOC_ENTRY) 。 | 因此， 位置 屏幕。位置结构最初具有 所有位置 设置为 顶层。 |  |
| 3 | 创建位置 | 选择 编辑位置结构 。在 位置结构 屏幕：选择 所有位置 行。选择 新建 。在 创建位置 屏幕：输入 <位置名称> 位置 字段。选择 <位置类型> 通过 的值帮助 位置类型 字段。输入日期 01.01.2000 （在 修订开始 日期 字段。选择 保存 。选择 返回到位置结构 。在 位置结构 屏幕：保存输入内容。 | 名称为 的位置 <位置名称> 已创建并保存在位置结构中。 |  |
| 4 | 编辑位置 | 在 位置结构 屏幕：在 中 名称 列中，选择 <位置 名称> 链接。 | 因此， 编辑位置 应用。 |  |
| 5 | 添加基本信息 | 在 位置 ： <位置名称> 屏幕，位于 基本信息 标签：添加 <位置描述> 中的文本 描述 字段。选择 翻译 旁边 位置 field。添加不同语言的翻译文本。选择 翻译 描述 字段。添加已翻译 不同语言的文本。选择 上载图像 为位置添加图片。保存输入内容。 | 位置的数据已保存。 |  |
| 6 | 添加地址 | 在 位置 ： <位置名称> 屏幕，位于 地址 标签：输入 <名称行 1> （在 名称行 1 字段。输入 <名称行 2> （在 名称行 2 字段。输入 <街道名称> （在 街道 field。输入 <邮政编码> （在 邮政 代码 字段。输入 <城市名称> （在 城市 field。选择 <国家/地区> 国家/地区 字段，通过 值帮助。选择 <地区> （在 地区 字段 通过值帮助。保留缺省值 UTC 中的值 时间 区域 字段。在以下位置输入附加数据： 电话号码 ， 传真 编号 ， 纬度 ， 经度 ，以及 仰角 字段。保存输入内容。 | 位置的数据已保存。 |  |
| 7 | 添加负责人 | 此步骤仅与以下角色相关：SAP_BR_INDUSTRIAL_HYGIENIST （ 工业卫生师 )SAP_BR_EHS_ENV_MGMT （ 环境经理 )在 位置 ： <位置名称> 屏幕，位于 负责人 tab：在 中 负责人（按角色） 表，请选择您的 <用户名> 名称 列（通过值 ） help。在 中 角色 列，选择 事故 经理 或者 环境 经理 从下拉列表中。保存输入内容。 | 位置的数据已保存。 |  |
| 8 | 添加文档 | 在 位置 ： <位置名称> 屏幕，位于 文档 标签：在 中 文档和链接 表中，选择 添加 文件 为位置添加文档。保存输入内容。 | 所选文档将添加到表中。位置的数据已保存。 |  |
|  | 激活位置 | 在 位置 ： <位置名称> 屏幕：选择 设置状态 在页眉中。选择 激活 选项。 | 位置已激活。因此， 状态 字段设置为 激活 在页眉中。位置的数据已保存。 |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-ehs-location-mds-3sr-359]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-361]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-local-ehs-mds-3sr-362]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 5,899 chars in the whole document
