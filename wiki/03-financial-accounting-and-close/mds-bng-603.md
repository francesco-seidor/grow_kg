---
id: 03-financial-accounting-and-close/mds-bng-603
title: 创建总账科目和成本要素 - MDS (BNG) (BNG_S4CLD2608_Master_Data_ZH_XX)
description: Chinese (machine-translated) SAP S/4HANA Cloud Public Edition master data script (BNG) for creating G/L accounts and cost elements by copying via F1241.
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/chart-of-accounts-and-gl-accounts]
aliases: [BNG_S4CLD2608_Master_Data_ZH_XX]
keywords: [Chart of Accounts YCOA and G/L Account Creation, gl accounts, cost elements, chart of accounts, account types, account groups, business configuration, business roles, master data scripts, BNG]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-603
topic: 03-financial-accounting-and-close/chart-of-accounts-and-gl-accounts
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建总账科目和成本要素 - MDS (BNG) (BNG_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Chart of Accounts YCOA and G/L Account Creation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建总账科目和成本要素 - MDS (BNG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897944)

[2 前提条件 3](#_Toc233897945)

[2.1 系统访问 3](#_Toc233897946)

[2.2 角色 3](#_Toc233897947)

[2.3 所需组织单位 3](#_Toc233897948)

[2.4 必填和可选主数据 4](#_Toc233897949)

[2.5 数据创建的主要参数 6](#_Toc233897950)

[3 概览表 7](#_Toc233897951)

[4 测试过程 8](#_Toc233897952)

[4.1 创建总账科目 8](#_Toc233897953)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

总账科目主记录包含有关科目的信息， 控制如何向其过账业务交易以及如何对其进行管理。

SAP 中的总账提供全面且最新的视图， 资产、应付账款和应收账款科目，并与其他 SAP 完全集成 模块。

由于所有 SAP 模块均已集成，因此某些 GL 过账由 自动生成 系统在后台，例如收货/收发票科目过账（货物 已接收/已收到发票）和库存移动总账过账。

某些科目是“未清项目管理”科目。它们用作清算科目，因此单个 例如，当收款和付款及物料满足以下条件时，可以清算项目 已处理。

其他科目（例如，客户和供应商对账科目） 直接过账到 ，因为它们只是 中业务伙伴的反映 明细分类账。

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
| 配置专家 - 业务流程配置 | SAP_BR_BPC_EXPERT | 业务流程配置 / 业务流程配置 - 财务 / 业务流程配置 - 采购 / 管理您的解决方案 / 业务流程配置 - 工作流 / 业务配置 - 功能管理 / 业务流程配置 - 可扩展性浏览器 / 业务配置 - 运输 | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### 所需组织单位

客户主数据的某些细分取决于公司的组织单位，常规（中央）数据不取决于组织单位或公司代码。下表提供了这些不同数据段及其相关组织单位的概览：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 总账科目 | 公司代码会计科目表成本控制范围 | 请参阅 [必填和可选主数据](#unique_6) [第 ] 页 4 | 对于使用总账科目和成本要素主记录的企业结构的每个公司代码标识，都可以存在公司代码数据。 | 公司代码：____________会计科目表____________成本控制范围____________ |

### 必填和可选主数据

客户主数据记录可能参考其他主数据。下表提供了要在客户主数据记录中使用的可选和必填主数据对象的概览。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 会计科目表 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 控制 部分。 | 必填 |  |
| 总账科目 | 在总账科目 UI 上，您可以在以下位置找到条目： 复制 帐户 屏幕。 | 必填 |  |
| 描述 | 在总账科目 UI 上，您可以在以下位置找到条目： 复制 帐户 屏幕。 | 必填 |  |
| 账户类型 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 控制 部分。 | 必填 |  |
| 科目组 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 控制 部分。 | 必填 |  |
| 职能范围 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 控制 部分。 | 可选 | 用于损益科目。 |
| 总账科目长文本 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 描述 部分。 | 可选 |  |
| 公司代码复选框 | 在总账科目 UI 上，您可以在 上找到条目 常规 选项卡（ 定义 在公司代码中 部分。 | 必填 | 分配到一个或多个公司代码。 |
| 已冻结，无法创建 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 管理 部分。 | 可选 |  |
| 已冻结过账 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 管理 部分。 | 可选 |  |
| 冻结计划 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 管理 部分。 | 可选 |  |
| 已加删除标记 | 在总账科目 UI 上，您可以在 上找到条目 常规 标签，位于 管理 部分。 | 可选 |  |
| 科目货币 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 科目控制 节。 |  |  |
| 仅以本币计的余额 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 科目控制 节。 | 可选 |  |
| 税收类别 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 科目控制 节。 | 可选 |  |
| 允许不含税过账 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 科目控制 节。 | 可选 |  |
| 备选科目编号 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 科目控制 节。 | 可选 |  |
| 排序码 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 科目 管理 部分。 | 可选 |  |
| 成本控制范围 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 上的会计设置 成本控制范围 部分。 | 必填 | 对于账户类型可选 资产负债表 帐户 |
| 成本要素类别 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 上的会计设置 成本控制范围 部分。 | 必填 | 对于账户类型可选 资产负债表 帐户 |
| 记录数量 | 新建总账科目后，您可以找到公司的详细信息 代码在 控制数据 > 上的会计设置 成本控制范围 部分。 | 可选 |  |
| 字段状态组 | 新建总账科目后，您可以找到公司的详细信息 代码在 创建/银行/利息 > 凭证控制 创建 部分。 | 可选 |  |
| 仅自动过账 | 新建总账科目后，您可以找到公司的详细信息 代码在 创建/银行/利息 > 凭证控制 创建 部分。 | 可选 |  |
| 自动过账补充 | 新建总账科目后，您可以找到公司的详细信息 代码在 创建/银行/利息 > 凭证控制 创建 部分。 | 可选 |  |
| 计划级别 | 新建总账科目后，您可以找到公司的详细信息 代码在 创建/银行/利息 > 银行/财务 详细信息 部分。 | 可选 |  |
| 与现金流相关 | 新建总账科目后，您可以找到公司的详细信息 代码在 创建/银行/利息 > 银行/财务 详细信息 部分。 | 可选 |  |
| 已冻结过账 | 新建总账科目后，您可以找到公司的详细信息 代码在 管理 。 | 可选 |  |
| 已加删除标记 | 新建总账科目后，您可以找到公司的详细信息 代码在 管理 。 | 可选 |  |
| 翻译文本 | 在总账科目 UI 上，您可以在 中找到该条目 翻译 标签， 语言 密钥 部分。 | 可选 | 将描述翻译成所需语言。 |

### 数据创建的主要参数

在本部分中，我们将介绍一些影响主记录行为的基本参数，并且始终需要这些参数来创建客户主数据记录：

账户类型

- 资产负债表科目
- 非运营费用或收入
- 初级成本或收入
- 次级成本

科目组

- 统驭科目准备输入
- 固定资产科目
- 损益表科目
- 流动资金科目
- 物料管理科目
- 总账科目（常规）

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [创建总账科目](#unique_9) [第 ] 页 8 | 配置专家 - 业务流程配置 | 管理您的解决方案 (F1241) |  |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建总账科目

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

创建新总账科目时，建议使用现有编号范围作为新总账科目的参考。

过程

取决于 的配置环境 SAP S/4HANA Cloud Public 版本 ，选择以下选项之一：

配置您的解决方案 ：

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 配置专家 - 业务流程配置 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理您的解决方案 (F1241) 。 |  |  |
| 3 | 访问配置 | 打开 配置您的解决方案 。 | 因此， 配置您的解决方案：实现阶段 屏幕。 |  |
| 4 | 访问配置 | 输入以下内容：应用范围 ： 财务子应用程序范围 ： 总账 |  |  |
| 5 | 打开 | 选择列右侧的箭头，其中包含 会计科目表 项目。 |  |  |
| 6 | 选择配置步骤 | 对于 管理总账科目主数据 步骤，选择 配置 。 |  |  |
| 7 | 搜索您的账户 | 输入以下内容并选择 执行 ：查看 ： 科目表视图会计科目表 ： YCOA | 系统显示匹配的总账科目清单。 |  |
| 8 | 选择总账科目 | 选择 总账科目 来自搜索结果。备注 单击蓝色账号链接。 | 因此， 总账科目主数据 屏幕。 |  |
| 9 | 复制科目 | 选择 复制 。 | 因此， <总账科目编号> 的副本 屏幕。 |  |
| 10 | 创建帐户 | 输入以下内容并选择 确定 ：账号 ： <账号>维护语言描述 (EN) ： <描述>集团科目编号 ： <账号>备注 此字段仅在以下情况下可见： 合并 在范围内。 | 屏幕上输入的数据 总账科目主数据 随即显示。 |  |
| 11 | 添加描述 | 在 中 基本信息 部分中，输入以下内容：会计科目表 ： YCOA总账科目长文本 ： <描述> |  |  |
| 12 | 分配公司代码 | 在 中 公司代码分配 部分，选择 公司代码 将其分配给客户。 |  |  |
| 13 | 添加翻译 | 在 中 翻译 部分，输入所有所需语言的短文本和长文本。 |  |  |
| 14 | 保存数据 | 选择 保存 。 | 系统确认科目 已成功保存。 |  |

SAP Central Business Configuration：

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 登录 SAP Central Business Configuration 中的项目体验。 | 打开已激活灵活工作流 |  |
| 2 | 访问 SAP Fiori 应用 | 转到 业务流程配置 应用，并搜索以下活动： 管理总账科目主数据 。选择搜索结果中的行项目以查看有关此配置活动的更多详细信息。选择 转到活动 按钮以直接导航到 SAP S/4HANA Cloud Public 版本 系统。以 身份登录 SAP Fiori 快速启动板 配置专家 - 业务流程配置 。 |  |  |
| 3 | 搜索您的账户 | 输入以下内容并选择 执行 ：查看 ： 科目表视图会计科目表 ： YCOA | 系统显示匹配的总账科目清单。 |  |
| 4 | 选择总账科目 | 选择 总账科目 来自搜索结果。备注 单击蓝色账号链接。 | 因此， 总账科目主数据 屏幕。 |  |
| 5 | 复制科目 | 选择 复制 。 | 因此， <总账科目编号> 的副本 屏幕。 |  |
| 6 | 创建帐户 | 输入以下内容并选择 确定 ：账号 ： <账号>维护语言描述 (EN) ： <描述>集团科目编号 ： <账号>备注 此字段仅在以下情况下可见： 合并 在范围内。 | 屏幕上输入的数据 总账科目主数据 随即显示。 |  |
| 7 | 添加描述 | 在 中 基本信息 部分中，输入以下内容：会计科目表 ： YCOA总账科目长文本 ： <描述> |  |  |
| 8 | 分配公司代码 | 在 中 公司代码分配 部分，选择 公司代码 将其分配给客户。 |  |  |
| 9 | 添加翻译 | 在 中 翻译 部分，输入所有所需语言的短文本和长文本。 |  |  |
| 10 | 保存数据 | 选择 保存 。 | 系统确认科目 已成功保存。 |  |

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
- related-to :: [[03-financial-accounting-and-close/criar-conta-do-razao-e-classe-de-custo-mds-bng-602]]
- related-to :: [[03-financial-accounting-and-close/g-l-mds-bng-601]]
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-g-l-account-and-cost-element-mds-bng-599]]
- related-to :: [[03-financial-accounting-and-close/sachkonto-und-kostenart-anlegen-sds-bng-598]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 9,325 chars in the whole document
