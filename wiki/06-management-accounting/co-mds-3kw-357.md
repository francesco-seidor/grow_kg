---
id: 06-management-accounting/co-mds-3kw-357
title: 主数据脚本 - 创建 CO 成本率 - MDS (3KW) (3KW_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script 3KW: maintain CO cost rates (service, plan, actual) and ICO account prerequisites."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-rates]
aliases: [3KW_S4CLD2608_Master_Data_ZH_XX]
keywords: ["CO Cost Rates (Service, Plan and Actual)", cost rates, service cost rates, plan cost rates, actual cost rates, intercompany accounts, automatic account determination, activity allocation, display cost rates, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-357
topic: 06-management-accounting/cost-rates
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 主数据脚本 - 创建 CO 成本率 - MDS (3KW) (3KW_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **CO Cost Rates (Service, Plan and Actual)** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建 CO 成本率 - MDS (3KW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897567)

[2 前提条件 3](#_Toc233897568)

[2.1 系统访问 3](#_Toc233897569)

[2.2 角色 3](#_Toc233897570)

[2.3 预备步骤 3](#_Toc233897571)

[2.3.1 可选：维护公司间清算科目（仅用于公司间过账） 3](#_Toc233897572)

[2.3.2 可选：维护边际收益科目（仅适用于使用公司间费率的公司间过账） 5](#_Toc233897573)

[3 概览表 7](#_Toc233897574)

[4 测试过程 8](#_Toc233897575)

[4.1 管理成本率 - 服务 8](#_Toc233897576)

[4.2 管理成本率 - 计划 12](#_Toc233897577)

[4.3 管理成本率 - 实际 13](#_Toc233897578)

[5 分析 15](#_Toc233897579)

[5.1 显示成本率 15](#_Toc233897580)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

以下应用可用于维护成本率（活动价格）。每个应用 具有不同的用途，具体取决于如何定义费率以及哪些对象可以 接收活动分配。

| 应用 | 受影响的范围项目 | 备注 |
| --- | --- | --- |
| 管理成本率 - 服务 (F3161) | 时间记录 (1Q4)间接费用成本会计 (J54)时间记录 - 基于项目的服务 (J12)服务订单管理和监控 (3D2) | 时间记录 |
| 管理成本率 - 计划 (F3162) | 标准成本计算 (BEG)期末关账 - 工厂 (BEI)期末关账 - 维护订单 (BF7) | 制造确认、订单计划和实际确认 |
| 管理成本率 - 实际 (F3422) | 实际成本核算 (33Q) | 用于输入成本中心活动的实际成本率。仅当客户要使用实际成本核算时才需要实际成本率。 |

本文档提供了在解决方案激活后测试此范围项目的详细过程，反映了解决方案的预定义范围。每个流程步骤、报告或项目都包含在其自己的部分中，在表视图中提供系统交互（测试步骤）。不在流程范围内但测试所需的步骤会相应标记。必须添加项目特定的步骤。

|  |
| --- |
| 备注 此测试脚本中的值（十进制记数法、日期格式等）以美国标准表示法显示。如果将测试系统设置为使用其他表示法，则根据需要输入值。 |

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

### 预备步骤

#### 可选：维护公司间清算科目（仅用于公司间过账）

使用

此活动允许您创建和更新公司间 (ICO) 过账的清算科目。ICO 清算科目派生自活动的总账科目。

过程

取决于 的配置环境 SAP S/4HANA Cloud Public 版本 ，选择以下选项之一：

配置您的解决方案 ：

1. 以 身份登录 SAP Fiori 快速启动板 配置专家 - 业务流程配置 。
2. 打开 管理您的解决方案 (F1241) 。
3. 如有必要，选择 设置本地版本 更改国家/地区。
4. 选择 配置您的解决方案 。
5. 在 中 配置步骤 部分，位于 名称 列，用于 自动科目确定 (100297) 行中，选择 配置 。
6. 继续执行下表中的过程。

SAP Central Business Configuration：

1. 登录 SAP Central Business Configuration 中的项目体验。
2. 转到 业务流程配置 应用。要在树视图中查找活动，请搜索 自动科目确定 活动。
3. 选择 打开文档 找到的行项目以查看有关此配置活动的更多详细信息。
4. 选择链接以直接导航到 SAP S/4HANA Cloud Public 版本 系统。以 身份登录 SAP Fiori 快速启动板 配置专家 - 业务流程配置 。
5. 继续执行下表中的过程。

| 步骤编号 | 步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 选择范围 | 对于显示的行，输入以下内容并选择 步骤 2 ：范围： 成本控制子范围： 成本中心会计流程： 分配实际过账的公司间清算科目 |  |  |
| 2 | 选择参数 | 输入以下内容并选择 步骤 3 ：会计科目表 ： YCOA |  |  |
| 3 | 维护科目确定 | 添加与 ICO 清账相关的科目。备注 缺省内容通过清账总账科目 68888800 - ICO 清账科目 - 差旅和 99999900 - ICO 清账科目 - 咨询提供。如果需要，您可以使用此参考创建自己的科目（使用总账科目类型 N - 非运营费用或收入）。 |  |  |

#### 可选：维护边际收益科目（仅适用于使用公司间费率的公司间过账）

使用

此活动允许您创建和更新公司间 (ICO) 过账的利润科目。如果使用 ICO 费率维护和过账，则需要执行此步骤。利润率总账清算科目根据活动分配总账科目派生。

过程

取决于 的配置环境 SAP S/4HANA Cloud Public 版本 ，选择以下选项之一：

配置您的解决方案 ：

1. 以 身份登录 SAP Fiori 快速启动板 配置专家 - 业务流程配置 。
2. 打开 管理您的解决方案 (F1241) 。
3. 如有必要，选择 设置本地版本 更改国家/地区。
4. 选择 配置您的解决方案 。
5. 在 中 配置步骤 部分，位于 名称 列，用于 自动科目确定 (100297) 行中，选择 配置 。
6. 继续执行下表中的过程。

SAP Central Business Configuration：

1. 登录 SAP Central Business Configuration 中的项目体验。
2. 要在树视图中查找活动，请搜索 自动科目确定 活动。
3. 选择 打开文档 找到的行项目以查看有关此配置活动的更多详细信息。
4. 选择链接以直接导航到 SAP S/4HANA Cloud Public 版本 系统。以 身份登录 SAP Fiori 快速启动板 配置专家 - 业务流程配置 。
5. 继续执行下表中的过程。

| 步骤编号 | 步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 选择范围 | 对于显示的行，输入以下内容并选择 步骤 2 ：范围： 成本控制子范围： 成本中心会计流程： 分配公司间保证金科目 |  |  |
| 2 | 选择参数 | 输入以下内容并选择 步骤 3 ：会计科目表 ： YCOA |  |  |
| 3 | 维护科目确定 | 添加与活动分配总账的 ICO 利润率相关的科目。备注 缺省内容通过利润科目 97777700 - ICO 利润率提供。如果需要，您可以使用此选项作为参考来创建自己的边际收益科目（使用总账科目 P 初级成本和收入）。 |  |  |

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [管理成本率 - 服务](#unique_8) [第 ] 页 8 | 成本会计 - 间接费用 | 管理成本率 - 服务 (F3161) | 为服务维护成本单价。 |
| [管理成本率 - 计划](#unique_9) [第 ] 页 12 | 成本会计 - 间接费用 | 管理成本率 - 计划 (F3162) | 已为计划维护成本率。 |
| [管理成本率 - 实际](#unique_10) [第 ] 页 13 | 成本会计 - 间接费用 | 管理成本率 - 实际 (F3422) | 为实际值维护成本率。 |

## 测试过程

### 管理成本率 - 服务

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

使用此应用根据各种条件输入成本率。成本率是 通过时间记录用于以下接收方对象的活动分配或 直接活动分配：

- 成本中心
- 项目 WBS 要素
- 服务订单

通过此应用，您可以为服务成本级别和特定 员工，因此对专业服务提供商很有用。但是，它还可以 如果需要服务成本率，则制造公司使用 成本级别和员工。

以下字段可用于价格维护：

- 公司代码（提供）始终填充，因此与访问无关 序列
- 待开票公司（收货）
- ICO 价格（标记）
- 成本中心（提供）
- 活动类型（提供）
- 服务成本级别（提供）
- 员工号（提供）
- 工作项目（新）（接收）
- WBS 要素（接收）

列表的顺序在 的末尾显示具有最高优先级的键值 清单（WBS 要素）。

更新价格表时检查以下规则。

- 发送公司代码为必填
- 必须填充以下一个或多个字段： 作业 类型 ， 服务成本级别 或者 人事 编号 （仅支持成本中心）
- 因此， 员工号 以及 成本中心 字段排除 彼此作为一个价格的关键字段。此人有特定的 成本率或 平均 成本中心费率有效。
- 因此， 员工号 以及 服务成本级别 个字段 互相排除作为一个价格的关键字段。该人员具有 特定成本率或 平均 服务成本级别之一 有效。
- 成本中心和服务成本级别是允许的键值组合。
- 在活动类型中定义的成本中心类别控制允许的 成本中心和活动类型的组合。
- 如果输入公司内成本率，应保留接收公司 空白
- WBS 特定的成本率可用于跨公司和公司内部活动 分配。如果输入接收公司和 WBS 要素，则 系统检查 WBS 要素是否分配到接收公司 系统不会自动从 WBS 派生接收公司 元素，因为这可能导致迁移成本率出现问题）。
- 检查并设置 ICO 标志
    - 如果接收公司代码为空，请使用用户 的 ICO 标志 输入
    - 如果 接收公司代码 不等于 发送公司 代码，将 ICO 标志设置为 true
    - 否则，将 ICO 标志设置为 false

| 成本中心 | 活动类型 | 服务成本级别 | 员工号（员工） | 工作项目（接收） | WBS+要素（接收） | 要开票的公司代码（接收） | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 发送方 | 接收方 |  |  |  |  |  |  |
|  | X |  |  |  |  |  | 至少一个字段（活动类型、服务成本级别、 必须填充员工号） |
|  |  | X |  |  |  |  |  |
| 从不 |  | 从不 | X |  |  |  |  |
| 从不 | X | 从不 | X |  |  |  | 无成本中心的人员编号，无服务成本级别 |
| X | X |  |  |  |  |  | 成本中心 + 作业类型 |
| X |  | X |  |  |  |  | 成本中心 + 服务成本级别 |
| X | X | X |  |  |  |  | 成本中心 + 作业类型 + 服务成本级别 |
|  | X | X |  |  |  |  | 活动类型 + 服务成本级别 |
|  | X |  |  | (X) | (X) |  | 可以填充 WBS 或工作项目 |
|  |  | X |  | (X) | (X) |  |  |
| 从不 |  | 从不 | X | (X) | (X) |  |  |
| 从不 | X | 从不 | X | (X) | (X) |  |  |
| X | X |  |  | (X) | (X) |  |  |
| X |  | X |  | (X) | (X) |  |  |
| X | X | X |  | (X) | (X) |  |  |
|  | X | X |  | (X) | (X) |  |  |
|  | X |  |  | (X) | (X) | X | 公司间费率 |
|  |  | X |  | (X) | (X) | X |  |
| 从不 |  | 从不 | X | (X) | (X) | X |  |
| 从不 | X | 从不 | X | (X) | (X) | X |  |
| X | X |  |  | (X) | (X) | X |  |
| X |  | X |  | (X) | (X) | X |  |
| X | X | X |  | (X) | (X) | X |  |
|  | X | X |  | (X) | (X) | X |  |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 |  |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本率 - 服务 (F3161) 。 | 因此， 管理成本率 - 服务 屏幕。 |  |
| 3 | 公司代码 | 输入以下内容并选择 添加 ：公司代码： <公司代码> |  |  |
| 4 | 维护服务成本单价 | 输入以下内容并选择 。 保存 ：接收公司 ：<留空>备注 此字段应该 仅在公司间成本率的情况下使用，否则 留空。成本中心 ： <成本中心>活动类型 ： <活动类型>工作分解结构要素 ： <这是可选的 字段>起始会计年度 ： <当前年度>起始期间 ： <当前期间>费率 ： 100备注 此比率用于过账到所有分类账。货币 ： <货币>Per ： 1活动单位 ： H | 已创建成本率。 |  |

### 管理成本率 - 计划

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

此作业用于计划制造中成本中心活动的成本率。 environment。这些汇率用于：

- 到生产订单和维护订单的活动分配
- 物料成本核算

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 |  |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本率 - 计划 (F3162) 。 | 因此， 管理成本率 - 计划 屏幕。 |  |
| 3 | 添加 | 选择 添加 。 |  |  |
| 4 | 维护计划成本率 | 输入以下内容并选择 。 保存 ：成本 居中 ： <成本 中心>作业 类型 ： <活动 类型>起始会计 年 ： <当前年度>起始期间 ： <当前 周期>货币 ： <货币>固定费率 ： <金额>变量 费率 ： <金额>备注 此比率用于过账到所有分类账。 | 已为计划维护成本率。 |  |

### 管理成本率 - 实际

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

此作业用于输入成本中心的实际成本率。 实际成本核算中使用的作业。实际成本率可以按分类账维护。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 |  |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理成本率 - 实际 (F3422) 。 | 因此， 管理成本率 - 实际 屏幕。 |  |
| 3 | 添加 | 选择 添加 。 |  |  |
| 4 | 维护实际成本率 | 输入以下内容并选择 。 保存 ：成本 居中 ： <成本 中心>作业 类型 ： <活动 类型>分类账 ： <例如，0L 或线索 分类帐>备注如果使用实际成本率计算，系统 计算每个分类账的实际成本率。如果你想 查看或更正自动计算的成本 费率，必须输入分类账。实际成本率 分类账字段为空用于全部过账 分类帐。如果存在分类账特定的实际成本率， 系统使用分类账特定比率。要查看分类账列，请调整 成本率列表并选择分类账。起始会计年度 ： <当前 年>起始期间 ： <当前 周期>货币 ： <货币>固定 费率 ： <金额>变量 费率 ： <金额>备注 此比率用于过账到所有分类账。 | 为实际值维护成本率。 |  |

## 分析

### 显示成本率

目的

此报表使您可以选择和查看各种成本单价类型。

前提条件

成本单价必须已存在。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 |  |  |
| 2 | 访问 SAP Fiori 应用 | 打开 显示成本率 (F5150) 。 | 因此， 显示成本率 屏幕。 |  |
| 3 | 选择条件 | 输入以下内容并选择 。 执行 ：分类账 ： <将此字段留空>备注 如果将选择字段留空，将显示相同且适用于 的比率 所有分类账（示例计划率）。在 中指定分类账 选择限制成本率显示到比率 仅为选定的特定分类帐维护 仅适用于实际费率。成本中心 ： <针对 示例，10101101>作业 类型 ： <例如， 11>起始会计年度 期间 ： <当前 周期>截止会计年度 期间 ： <当前 周期> |  |  |

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
- related-to :: [[06-management-accounting/co-mds-3kw-355]]
- related-to :: [[06-management-accounting/crear-tasas-de-coste-co-mds-3kw-354]]
- related-to :: [[06-management-accounting/master-data-script-create-co-cost-rates-mds-3kw-353]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-taxas-de-custo-co-mds-3kw-356]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 11,520 chars in the whole document
