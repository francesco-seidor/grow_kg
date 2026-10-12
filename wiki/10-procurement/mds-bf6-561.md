---
id: 10-procurement/mds-bf6-561
title: "主数据脚本: 创建计划协议 - MDS (BF6) (BF6_S4CLD2608_Master_Data_ZH_XX)"
description: "Chinese (machine-translated) master data script BF6 for creating scheduling agreements (standard, consignment, subcontracting) via app F2179 in SAP S/4HANA Cloud Public."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements]
aliases: [BF6_S4CLD2608_Master_Data_ZH_XX]
keywords: [Purchase Scheduling Agreements, scheduling agreements, consignment procurement, subcontracting procurement, standard procurement, number ranges, master data scripts, business roles, BF6]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-561
topic: 10-procurement/scheduling-agreements
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 主数据脚本: 创建计划协议 - MDS (BF6) (BF6_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建计划协议 - MDS (BF6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897827)

[2 前提条件 3](#_Toc233897828)

[2.1 系统访问 3](#_Toc233897829)

[2.2 角色 3](#_Toc233897830)

[2.3 所需组织单位 3](#_Toc233897831)

[2.4 必填和可选主数据 4](#_Toc233897832)

[2.5 数据创建的主要参数 4](#_Toc233897833)

[2.5.1 编号范围 4](#_Toc233897834)

[3 概览表 5](#_Toc233897835)

[4 测试过程 6](#_Toc233897836)

[4.1 创建标准采购的计划协议 6](#_Toc233897837)

[4.1.1 创建含审批凭证的计划协议 - 标准 6](#_Toc233897838)

[4.1.2 创建不具有审批凭证的计划协议 - 标准 8](#_Toc233897839)

[4.2 创建寄售采购的计划协议 10](#_Toc233897840)

[4.3 创建转包采购的计划协议 12](#_Toc233897841)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

本文档提供了为 创建计划协议的描述。 SAP S/4HANA Cloud Public 版本 系统。因此， 描述包括那些数据段与 SAP S/4HANA Cloud Public 版本 设备，例如 采购数据、物料数据和供应商数据。与 范围无关的字段 SAP S/4HANA Cloud Public 版本 交付日期 SAP Best Practices 在此中未描述 文档。

计划协议是与供应商达成的长期协议，涵盖根据预定条件供应物料。 这些条件对预定义期间和预定义总数量有效。

计划协议的主要优势包括：

- 计划协议可以替换大量采购订单或合同发布。
- 这是一个长期协议，允许您与供应商协商更好的价格。

存在以下项目类别：

- 标准采购
- 寄售采购
- 转包采购

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
| 采购员 | SAP_BR_PURCHASER | 采购 / 供应商开发及合同管理 | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### 所需组织单位

贵公司的组织结构和主数据在 ERP 中创建 系统。组织结构反映以下内容的结构： 您的公司。下表提供了这些不同数据段的概览，以及 其相关组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 采购数据 | 采购组织 | 采购组、物料组、收货处理时间等 on。 | 采购数据可存在于以下项目的每个采购组织： 采购流程中使用该物料。 | 采购组织：__________ |

### 必填和可选主数据

计划协议可能参考其他主数据。下表提供了 要在计划中使用的可选和强制主数据对象的概览。 协议。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 材料 |  | 必填 | 要输入物料，首先要创建物料主数据。 |
| 供应商 |  | 必填 | 要输入供应商，首先要创建供应商主数据。 |

### 数据创建的主要参数

在此部分中，为影响行为的基本参数提供描述 计划协议的，并且始终需要创建计划 协议。

#### 编号范围

为计划协议定义了以下编号范围：

| 编号范围 | 范围/业务伙伴标识 | 备注 |
| --- | --- | --- |
| 内部编号 | 用于标准用途的内部数字编号范围：5500000000 – 5599999999 | 系统自动分配 数字编号到计划协议。 |
| 外部数字 | 外部数字编号范围：5600000000 – 5699999999 | 此编号范围为外部数字编号保留 assignment。 |

## 概览表

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
|  |  |  |  |
| [创建含审批凭证的计划协议 - 标准](#unique_10) [第 ] 页 6 | 采购员 | 管理采购计划协议 (F2179) | 含审批凭证的计划协议 - 标准 |
| [创建不具有审批凭证的计划协议 - 标准](#unique_11) [第 ] 页 8 | 采购员 | 管理采购计划协议 (F2179) | 不含审批凭证的计划协议 - 标准 |
| [创建寄售采购的计划协议](#unique_12) [第 ] 页 10 | 采购员 | 管理采购计划协议 (F2179) | 寄售采购的计划协议为 已创建 |
| [创建转包采购的计划协议](#unique_13) [第 ] 页 12 | 采购员 | 管理采购计划协议 (F2179) | 创建转包采购的计划协议 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建标准采购的计划协议

#### 创建含审批凭证的计划协议 - 标准

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

为标准采购创建计划协议。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理采购计划协议 (F2179) 。 | 应用随即打开。 |  |
| 3 | 创建计划协议 | 选择 创建 创建新的计划协议。 | 因此， 新建采购计划协议 屏幕。 |  |
| 4 | 输入抬头数据 | 使用以下数据创建新的计划协议：供应商 ： <供应商>协议类型 ： LPA（含审批的 SA） doc.)有效期开始 ： <MM/DD/YYYY>有效期至 ： <MM/DD/YYYY>公司代码 ： <公司 代码>采购组织 ： <采购 组织>采购组 ： <采购组>目标价值 ： <目标 值> |  |  |
| 5 | 输入抬头注释 | 转到 备注 部分并输入以下部分标题 注释：抬头文本抬头注释定价类型截止日期交货条件装运说明付款条件质保合同违约金担保合同附加条款（条款）资产其他合同约定入库交货供应商备忘录（常规）供应商备忘录（采购组织） |  |  |
| 6 | 将项目添加到计划协议 | 来自 新建采购计划协议 屏幕上，选择 个项目 构面并选择 创建 。 | 因此， 采购计划协议项目 屏幕。 |  |
| 7 | 输入项目数据 | 在 个项目 facters 屏幕上，进行以下输入：工厂 ： <工厂>材料 ： <物料>目标数量 ： <目标 数量>订单净价 ： <订单净价>税码 ： <XX（信息中的缺省值） 记录）>税收日期 ： <使用 缺省日期为今天的日期 值>在 中 输出控制 部分， 进行以下输入：创建参数文件 ： <创建 参数文件>选择 应用 屏幕底部。 |  |  |
| 8 | 创建 | 返回到 新建采购计划协议 屏幕，然后选择 创建 屏幕底部。记录计划协议编号。 | 已创建计划协议。 |  |

#### 创建不具有审批凭证的计划协议 - 标准

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

为标准采购创建计划协议。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理采购计划协议 (F2179) 。 | 因此， 管理采购计划协议 (F2179) 显示列表页面 |  |
| 3 | 创建计划协议 | 选择 创建 创建新的计划协议 | 因此， 新建采购计划协议 抬头视图随即显示。 |  |
| 4 | 输入抬头数据 | 使用以下数据创建新的计划协议：供应商 ： <供应商>协议类型 ： LP（计划 协议）有效期开始 ： <MM/DD/YYYY>有效期至 ： <MM/DD/YYYY>公司代码 ： <公司 代码>采购组织 ： <采购 组织>采购组 ： <采购组>目标价值 ： <目标 值> |  |  |
| 5 | 输入抬头注释 | 导航到 备注 部分并输入 部分以下抬头注释：抬头文本抬头注释定价类型截止日期交货条件装运说明付款条件质保合同违约金担保合同附加条款（条款）资产其他合同约定入库交货供应商备忘录（常规）供应商备忘录（采购组织） |  |  |
| 6 | 将项目添加到计划协议 | 来自 新建采购计划协议 视图，请选择 个项目 构面并选择 创建 . | 因此， 采购计划协议项目 视图。 |  |
| 7 | 输入项目数据 | 在 个项目 facters 屏幕上，进行以下输入：工厂 ： <工厂>材料 ： <物料>目标数量 ： <目标数量>订单净价 ： <订单净值 价格>税码 ： <XX（ 信息记录中的缺省值）>税收日期 ： <使用 缺省日期为今天的日期 值>选择 应用 屏幕底部。 |  |  |
| 8 | 创建 | 返回到 新建采购计划协议 抬头视图和 选择 创建 位于视图底部。记录计划协议编号。 | 已创建计划协议。 |  |

### 创建寄售采购的计划协议

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

为寄售采购创建计划协议。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理采购计划协议 (F2179) 。 | 因此， 管理计划协议 清单页面随即显示。 |  |
| 3 | 创建计划协议 | 选择 创建 创建新的计划协议。 | 因此， 新计划协议 抬头视图随即显示。 |  |
| 4 | 输入抬头数据 | 使用以下数据创建新的计划协议：协议类型 ： LP 计划协议供应商 ： <供应商>有效期开始 ： 缺省 今天有效期结束日期 ： MM/DD/YYYY，例如今天 + 720 天采购组 ： <采购组>采购组织 ： <采购组织>公司代码 ： <公司代码>目标价值 ： 例如 XXXXX 欧元 |  |  |
| 5 | 将项目添加到计划协议 | 来自 新建采购计划协议 视图，请选择 个项目 构面并选择 创建 。 | 因此， 新建计划协议项目 视图。 |  |
| 6 | 输入项目数据 | 在 个项目 facet 视图中，进行以下输入：项目类别 ： K （寄售）工厂 ： <工厂>材料 ： <物料>目标数量 ： <目标数量>税码 ： XX（缺省值） 信息记录中的值）税收日期 ： 缺省 今天备注 如果激活 RITA 并为公司代码 维护税收登记国家/地区 财务配置步骤 103464（激活 RITA 和 维护税收注册国家），然后维护税收国家 可以采用，或者您也可以选择不同的税收国家/地区 列表中的值。备注 根据您的配置环境，可以在 下访问配置步骤 配置您的解决方案 在 SAP Fiori 快速启动板或 业务流程配置 应用在 SAP Central Business Configuration 的项目体验中。选择 应用 位于视图底部。 |  |  |
| 7 | 创建 | 返回到 新建采购计划协议 视图，然后选择 创建 位于视图底部。记录计划协议编号。 | 已创建计划协议。 |  |

### 创建转包采购的计划协议

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

为转包采购创建计划协议。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 采购员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理采购计划协议 (F2179) 。 | 因此， 管理计划协议 显示列表页面 |  |
| 3 | 创建计划协议 | 选择 创建 创建新计划 同意 | 因此， 新计划协议 抬头视图 显示 。 |  |
| 4 | 输入抬头数据 | 使用以下数据创建新的计划协议：协议类型 ： LP 计划协议供应商 ： <供应商>有效期开始 ： 缺省 今天有效期结束日期 ： MM/DD/YYYY，例如今天 + 720 天采购组 ： <采购组>采购 组织 ： <采购 组织>公司代码 ： <公司代码>目标价值 ： 例如 XXXXX 欧元 |  |  |
| 5 | 将项目添加到计划协议 | 来自 新建采购计划协议 视图，请选择 个项目 构面并选择 创建 。 | 因此， 新建计划协议项目 视图。 |  |
| 6 | 输入项目数据 | 在 个项目 facet 视图中，进行以下输入：项目类别 ： L （转包）工厂 ： <工厂>存储地点 ： <存储地点>材料 ： <物料>订单净价 ： 信息中的缺省值 记录目标数量 ： <目标数量>税码 ： XX（缺省值） 信息记录中的值）税收日期 ： 缺省 今天备注 如果激活 RITA 并为公司代码 维护税收登记国家/地区 财务配置步骤 103464（激活 RITA 和 维护税收注册国家），然后维护税收国家 可以采用，或者您也可以选择不同的税收国家/地区 列表中的值。备注 根据您的配置环境，可以在 下访问配置步骤 配置您的解决方案 在 SAP Fiori 快速启动板或 业务流程配置 应用在 SAP Central Business Configuration 的项目体验中。选择 应用 位于底部 视图。 |  |  |
| 7 | 创建 | 返回到 新建采购计划 协议 视图，然后选择 创建 位于视图底部。记录计划协议编号。 | 已创建计划协议。 |  |

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
- related-to :: [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557]]
- related-to :: [[10-procurement/mds-bf6-559]]
- related-to :: [[10-procurement/script-de-dados-mestre-criar-programa-de-remessas-mds-bf6-560]]
- related-to :: [[10-procurement/script-de-datos-maestros-creacion-de-plan-de-entregas-mds-bf6-558]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 10,241 chars in the whole document
