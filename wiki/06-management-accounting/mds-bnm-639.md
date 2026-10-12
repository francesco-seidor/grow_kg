---
id: 06-management-accounting/mds-bnm-639
title: 创建成本中心和成本中心组 - MDS (BNM) (BNM_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) SAP master data script BNM for creating cost centers and cost center groups, with test steps and where-used analysis."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-centers-and-groups]
aliases: [BNM_S4CLD2608_Master_Data_ZH_XX]
keywords: [Cost Centers and Cost Center Groups, cost centers, cost center groups, standard hierarchy, global hierarchies, where-used analysis, master data scripts, master data integration, BNM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-639
topic: 06-management-accounting/cost-centers-and-groups
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建成本中心和成本中心组 - MDS (BNM) (BNM_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Cost Centers and Cost Center Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建成本中心和成本中心组 - MDS (BNM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897990)

[2 前提条件 3](#_Toc233897991)

[2.1 系统访问 3](#_Toc233897992)

[2.2 角色 3](#_Toc233897993)

[2.3 所需组织单位 3](#_Toc233897994)

[2.4 必填和可选主数据 4](#_Toc233897995)

[2.5 数据创建的主要参数 4](#_Toc233897996)

[3 概览表 5](#_Toc233897997)

[4 测试过程 6](#_Toc233897998)

[4.1 创建成本中心主数据 6](#_Toc233897999)

[4.2 创建成本中心组主数据 8](#_Toc233898000)

[4.3 分析 11](#_Toc233898001)

[4.3.1 使用位置清单 - 成本中心实际 11](#_Toc233898002)

[5 附录 13](#_Toc233898003)

[5.1 成本中心复制自SAP S/4HANA Cloud Public 版本 到 SAP Master Data Integration（可选） 13](#_Toc233898004)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

成本中心代表组织单位责任范围，其财务 可以分配成本。通过将组织划分为多个成本中心，您可以遵循 几个目标。

通过向成本中心分配成本，您可以确定成本在何处产生 组织。

如果在成本中心级别计划成本，则可以在以下位置检查成本效率： 成本。

如果要将间接费用成本准确分配到各个产品、服务或 市场细分，您需要直接将成本进一步分配到这些成本中心 涉及产品或服务的创建。通过这些成本中心，您可以 然后使用不同的方法将活动和成本分配给相关产品， 服务和市场细分市场。

这样，您就可以在产品成本中评估半成品和成品 成本控制 (CO-PC)，并在获利能力分析中计算边际收益 (CO-PA)

成本中心组表示成本中心的层次结构，称为 标准层次结构。创建的每个成本中心必须分配到 标准层次结构。这样可以确保标准层次结构包含所有成本， 在成本控制组中居中。在分析标准层次结构时，SAP 系统 自动包含所有成本中心。

请注意，成本中心可以分配到任意数量的备选组。但是， 维护标准层次结构时无法创建备选组。

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
| 成本会计 - 间接费用 | SAP_BR_OVERHEAD_ACCOUNTANT | 间接费用会计 | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### 所需组织单位

贵公司的组织结构和主数据在 ERP 中创建 系统。组织结构反映以下内容的结构： 您的公司。主数据表示成本中心和成本中心组，具体取决于 公司的运营重点。

| 数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 成本控制范围 | 常规数据 | 必填 |  |
| 公司代码 | 组织单位 | 必填 |  |

### 必填和可选主数据

成本中心和成本中心组主数据记录可能参考其他主数据。因此， 下表提供了可选和必填主数据对象的概览， 在成本中心数据记录中使用。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 层次结构范围 | 组织单位 | 必填 |  |
| 业务范围 | 组织单位 | 可选 |  |
| 职能范围 | 组织单位 | 可选 |  |
| 利润中心 | 组织单位 | 必填 |  |

### 数据创建的主要参数

此范围项目没有业务条件。

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [创建成本中心主数据](#unique_9) [第 ] 页 6 | 成本会计 - 间接费用 | 管理成本中心 - 旧版本 (F1443A) | 可以根据新的业务需求创建成本中心。 |
| [创建成本中心组主数据](#unique_10) [第 ] 页 8 | 成本会计 - 间接费用 | 管理全局层次结构 (F2918) 或者 管理成本中心组 (F1024) | 可根据新的业务需求创建成本中心组。 |
| [使用位置清单 - 成本中心实际](#unique_11) [第 ] 页 11 | 成本会计 - 间接费用 | 管理成本中心 - 旧版本 (F1443A) |  |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的过程。 您还可以使用这些过程测试主数据创建。

### 创建成本中心主数据

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

|  |
| --- |
| 备注 标准层次结构节点 1~自 2502 版本起，对于新客户安装，将使用值为 1~ 的全局层次结构功能提供标准层次结构。先前客户可以继续使用基于集的标准层次结构值 0001。在生产系统中创建第一个成本中心时，必须选择值 1~ ，位于以下位置的搜索下拉列表中： 标准层次结构节点 字段。这将建立标准层次结构中的顶级节点 1~。在系统中创建第一个成本中心后，还会自动创建标准层次结构节点 1~ 。自 2502 版本起， SAP S/4HANA Cloud Public 版本 公共版本缺省内容始终随标准层次结构 1~ 一起提供，必须用作顶级。 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本中心 - 旧版本 (F1443A) 。 | 应用随即打开。 |  |
| 3 | 新建成本中心 | 选择 创建 以创建新的成本中心。 |  |  |
| 4 | 输入新成本中心 | 在 基本信息 标签上，输入以下内容：成本中心 ： <文本>名称 ： <文本>描述 ： <文本>负责人 ： <负责人>有效自 ： <2017 年 1 月 1 日>有效期至 ： <9999 年 12 月 31 日>成本中心类别 ： <成本中心类别>或者，您可以更改有效日期的缺省值，并从现有成本中心主数据中选择参考。 | 随即打开一个新部分，显示常规信息。 |  |
| 5 | 输入成本中心组织数据 | 在 中 组织单位 部分，位于 成本中心 屏幕上，输入以下内容：标准层次结构节点 ： <1~>公司代码 ： <公司代码>职能范围 ： <功能范围>利润中心 ： <利润中心>仅针对 PSM：备注 如果您有 公共部门管理 (PSM) 则这些字段将在选择 PSM 公司代码后可用于输入。资金 ： <资金>资金固定分配 ： <是/否>拨款 ： <拨款>拨款固定分配 ： <是/否>功能范围固定分配 ： <是/否>备注 因此， 固定分配 仅在输入相应主数据后显示 功能范围 、 资金 和 拨款 复选框。具有预算的成本中心 ： <成本中心>预算可用性控制参数文件 ： <参数文件>预算可用性控制已激活 ： <是/否> | 选择滚动显示组织数据。 |  |
| 6 | 创建 | 选择 创建 。 | 已创建成本中心。 |  |

### 创建成本中心组主数据

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

前提条件

对于本章节，必须已按照章节[创建成本中心主数据](#unique_9) [第 ] 页 6。在上一章中保存主数据条目后，开始此过程。

|  |
| --- |
| 备注 或者 管理全局层次结构 (F2918) 或者 管理成本中心组 (F1024) 可以在创建备选层次结构时使用，但只能选择一个方法（全局层次结构组或基于集合的组）。这两个方法均在以下步骤中描述。允许现有客户继续使用 基于集合的组 相关应用 管理成本中心组 (F1024) 直到完全迁移并将迁移状态标记为 完成 通过以下路径使用 BPC 专家角色： 业务流程配置 > 会计 > 常规设置：将基于集合的组迁移到全局层次结构 (F6228) 。SAP 提供的成本中心组演示主数据也使用基于集合的组创建，也可以进行转换。您可以通过以下方式找到有关成本中心组到全局层次结构转换的详细信息：[https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?状态=草稿](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT)。 |

过程：选项 1 - 全局层次结构组

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理全局层次结构 (F2918) 。 | 应用随即打开。 |  |
| 3 | 选择创建 | 在 中 层次结构清单 部分，选择 创建 。 | 因此， 新建层次结构 屏幕。 |  |
| 4 | 输入新的成本中心层次结构 | 在 新建层次结构 屏幕上，输入以下内容并选择 创建 ：类型 ： 成本中心层次结构层次结构标识 ： <最多 10 个字符的任意标识>注意 层次结构标识和节点标识的总长度不能超过 14 个字符。成本控制范围 ： A000层次结构描述 ： <任意描述>有效自 ： <当前日期> |  |  |
| 5 | 编辑新成本层次结构 | 在 层次结构清单 屏幕上，选择详细信息图标 > 并选择 编辑 新建的成本中心层次结构。选择新创建的成本中心层次结构，然后选择 更多 ，然后选择 快速输入 。在 快速输入 屏幕上，选择 成本中心 并输入以下内容：标识 ： <使用搜索功能选择要添加的成本中心>选择 确定 当你完成并选择 保存 。返回到 成本中心层次结构 屏幕并选择 激活 。 | 新创建的成本中心层次结构现已激活。 |  |

过程：选项 2 - 基于集合的组

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本中心组 (F1024) 。 | 应用随即打开。 |  |
| 3 | 新建成本中心组 | 在 中 结果清单：成本中心组 部分，选择 新建 。 |  |  |
| 4 | 输入新成本中心组 | 在 成本中心组：新 屏幕上，输入以下内容：成本控制范围 ： <A000>成本中心组 ： <成本中心组>选择 继续 并输入以下内容：名称 ： <名称>选择 保存 。或者，您可以从现有成本中心组中选择参考。 | 因此， 成本中心组：新 屏幕。 |  |
| 5 | 输入成本中心组织数据 | 在 成本中心组：新 屏幕上，输入以下内容：在顶层，您可以通过选择 新建 ：新建子组 ： <成本中心组>在较低级别，可以通过选择 新建 ：新建子组 ： <成本中心组>新建同级组 ： <成本中心组>在顶层，您可以通过选择 添加 ：添加子组 ： <成本中心组添加成本中心 ： <成本中心>添加成本中心范围 ： <成本中心>在较低级别，可以通过选择 新建 ：新建子组 ： <成本中心组>新建同级组 ： <成本中心组>添加成本中心 ： <成本中心>添加成本中心范围 ： <成本中心> | 新主数据显示在 成本中心组：新 屏幕。 |  |
| 6 | 保存数据 | 选择 保存 。 | 创建并保存成本中心组。 |  |

### 分析

#### 使用位置清单 - 成本中心实际

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

通过此作业，您可以查看成本中心在其他主数据中的使用位置 例如活动类型、利润中心和实际成本分配。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 |  |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本中心 - 新版本 (F1443B) 。 | 因此， 管理成本中心 屏幕。 |  |
| 3 | 选择条件 | 输入以下内容并选择 执行 ：成本中心 ： <您的成本中心> |  |  |
| 4 | 使用位置 | 选择所需成本中心，然后选择 使用位置 。从下拉列表中选择一个选项。例如， 在所有对象中 。 | 随即显示一个报表，其中显示成本中心的当前使用位置。有关详细信息，您可以选择主数据对象 类型并进一步钻取。 |  |

|  |
| --- |
| 备注 因此， 调用清单 - 成本中心 (F3549) 应用还可用于确定 个成本中心当前已使用。 |

## 附录

### 成本中心复制自SAP S/4HANA Cloud Public 版本 到 SAP Master Data Integration（可选）

此链接描述 SAP S/4HANA Cloud Public 版本 通过 SAP Master Data Integration 将成本中心主数据集成到其他云应用程序，例如 SAP SuccessFactors ：[https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html](https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html)。

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
- related-to :: [[06-management-accounting/create-cost-center-and-cost-center-group-mds-bnm-635]]
- related-to :: [[06-management-accounting/mds-bnm-637]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-custo-e-grupo-de-centros-de-cus]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-centro-de-coste-y-grupo-de-centros-de-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 10,207 chars in the whole document
