---
id: 12-production-and-manufacturing/mds-5cp-441
title: 创建生产资源/工具 - MDS (5CP) (5CP_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script 5CP for SAP S/4HANA Cloud Public Edition 2608: creating production resources/tools (PRTs) and assigning them to routings and production orders."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-resources-tools]
aliases: [5CP_S4CLD2608_Master_Data_ZH_XX]
keywords: [Production Resources/Tools (PRTs), production resources tools, material prt, document prt, equipment prt, miscellaneous prt, prt status and control key, routing prt assignment, production order prt assignment, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-441
topic: 12-production-and-manufacturing/production-resources-tools
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建生产资源/工具 - MDS (5CP) (5CP_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Production Resources/Tools (PRTs)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建生产资源/工具 - MDS (5CP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897725)

[2 前提条件 4](#_Toc233897726)

[2.1 系统访问 4](#_Toc233897727)

[2.2 角色 4](#_Toc233897728)

[2.3 所需组织单位 5](#_Toc233897729)

[2.4 必填和可选主数据 5](#_Toc233897730)

[2.5 数据创建的主要参数 5](#_Toc233897731)

[2.5.1 PRT 状态 5](#_Toc233897732)

[2.5.2 PRT 控制码 6](#_Toc233897733)

[3 概览表 7](#_Toc233897734)

[4 过程 8](#_Toc233897735)

[4.1 创建生产资源/工具 8](#_Toc233897736)

[4.1.1 创建物料 PRT 8](#_Toc233897737)

[4.1.2 创建杂项 PRT 9](#_Toc233897738)

[4.1.3 创建文档 PRT 11](#_Toc233897739)

[4.1.4 创建设备 PRT 12](#_Toc233897740)

[4.2 在工艺路线中分配生产资源/工具（可选） 13](#_Toc233897741)

[4.3 在生产订单中分配 PRT（可选） 15](#_Toc233897742)

[5 附录 18](#_Toc233897743)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何为 创建生产资源/工具主数据记录的描述 SAP S/4HANA Cloud Private Edition system。不同于机器和 固定资产、PRT（生产资源/工具）是执行 活动，可以重复使用。

有多种类别的生产资源/工具可用。类别确定特征和业务 PRT 可以具有的功能。

您可以在此主数据脚本的指令下创建自己的 PRT。

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
| 生产工程师 - 离散制造 | SAP_BR_PRODN_ENG_DISC | 生产工程 - 离散制造 | SAP_BR_PRODN_ENG_DISC |  |
| 生产主管 - 离散制造 | SAP_BR_PRODN_SUPERVISOR_DISC | 生产管理 - 离散制造 | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST | 主数据 - 产品 / 产品治理 | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| 设计工程师 | SAP_BR_DESIGN_ENGINEER | 文档管理 | SAP_BR_DESIGN_ENGINEER |  |
| 维护计划员 | SAP_BR_MAINTENANCE_PLANNER | 维护计划 | SAP_BR_MAINTENANCE_PLANNER |  |

### 所需组织单位

物料主数据的某些段取决于 公司，常规（中央）数据不依赖于组织单位或公司 代码。下表提供了这些不同数据段及其 相关组织单位：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 所有数据 | 工厂 |  | 所有数据均取决于工厂。 | 工厂：____________ |

### 必填和可选主数据

参考工艺路线数据记录可能参考其他主数据。下表提供了 参考中使用的可选和强制主数据对象的概览。 工艺路线。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 工艺路线 | 在工艺路线中分配生产资源/工具 | 可选 | 我们假设您具有工艺路线，并且想要为其分配生产资源/工具。 |

### 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录，并且始终需要创建 PRT 主数据记录：

#### PRT 状态

PRT 状态控制生产资源/工具的使用。根据其状态， 可以在 PRT 维护中为各种任务发布生产资源/工具。

| PRT 状态 | 描述 |
| --- | --- |
| 01 | 创建于 |
| 02 | 已针对 PRT 使用计划发布 |
| 03 | 已下达至生产 |

#### PRT 控制码

PRT 控制代码确定是将 PRT 分配到任务清单还是订单 包含在以下业务功能中：

| PRT 控制参数文件 | 描述 |
| --- | --- |
| 1 | 所有功能 |
| 2 | 打印 |

## 概览表

此范围项目由下列流程步骤组成： 表：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [创建物料 PRT](#unique_11) [第 ] 页 8 | 主数据专家 - 产品数据 | 创建物料 (MM01) |  |
| [创建杂项 PRT](#unique_12) [第 ] 页 9 | 生产工程师 - 离散制造 | 管理生产资源和工具 (F7653) |  |
| [创建文档 PRT](#unique_13) [第 ] 页 11 | 设计工程师 | 管理文档 (F2733) |  |
| [创建设备 PRT](#unique_14) [第 ] 页 12 | 维护计划员 | 创建技术对象 (W0029) |  |
| [在工艺路线中分配生产资源/工具（可选）](#unique_15) [第 ] 页 13 | 生产工程师 - 离散制造 | 更改工艺路线 (CA02) |  |
| [在生产订单中分配 PRT（可选）](#unique_16) [第 ] 页 15 | 生产主管 - 离散制造 | 更改生产订单 (CO02) |  |

## 过程

本节介绍属于此主数据的每个段或流程步骤的过程。 记录。

### 创建生产资源/工具

#### 创建物料 PRT

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

本章介绍如何创建物料 PRT。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 因此， 启动 页面。 |  |
| 2 | 打开 SAP Fiori 应用 | 打开 创建物料 (MM01) 。 | 随即打开一个新窗口，显示 创建物料（初始） 屏幕） 。 |  |
| 3 | 输入物料基本数据 | 在 创建物料（初始屏幕） ，请进行以下操作 条目：材料 ： <物料编号> ，针对 示例， PRT_01物料类型 ： 生产 资源/工具选择 选择视图 。 | 因此， 选择视图 视图。 |  |
| 4 | 选择视图 | 在 选择视图 屏幕上，选择 视图：基本视图生产资源/工具其他必要视图选择 继续 。 |  |  |
| 5 | 输入组织级别数据 | 在 组织级别 视图，位于 组织级别部分，输入以下内容：工厂 ： <工厂代码> ，例如 1010按下 输入 。 |  |  |
| 6 | 输入基本视图数据 | 在 基本数据 1 标签上，输入 以下数据：描述 ： <已完成 装配 PRT>基本计量单位 ： <EA>选择 生产资源/工具 tab。 | 基本数据已保存。 |  |
| 7 | 输入生产资源/工具数据 | 在 生产资源/工具 标签上，输入以下内容 数据：PRT 使用 ： <009>PRT 控制参数文件 ： <1>选择 保存 。 | 屏幕返回到初始屏幕。已创建物料 PRT_01。 |  |

#### 创建杂项 PRT

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

本章介绍如何创建杂项 PRT。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理生产资源和工具 (F7653) 。 | 应用随即打开。 |  |
| 3 | 选择创建 | 选择 创建 。 | 随即打开一个新窗口，显示 创建 PRT 屏幕。 |  |
| 4 | 输入名称 | 输入以下内容：生产资源/工具 ： <名称> ，例如， PRT_02选择 基本数据 。 | 因此， 创建生产资源/工具：基本数据 屏幕。 |  |
| 5 | 输入基本数据 | 为创建的 PRT 提供描述：查找 生产资源/工具描述 工具提示并输入： <杂项 PRT 02>在 中 基本数据 部分中，输入以下内容：状态 ： <03>PRT 使用 ： <009>基本计量单位 ： <EA>选择 保存 。 | 屏幕将返回到初始屏幕。已创建生产资源/工具。 |  |

#### 创建文档 PRT

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

本章介绍如何创建文档 PRT。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 设计工程师 。 | 因此， 启动 页面。 |  |
| 2 | 打开 SAP Fiori 应用 | 打开 管理文档 (F2733) 。 | 随即打开一个新窗口，显示 管理 文档 。 |  |
| 3 | 创建文档 | 选择 创建 。在 文档 屏幕上，进行以下操作： 条目：凭证类型 ： <SPP>凭证描述 ： <PRT_03>选择 创建 。 | 已创建凭证。记录凭证编号。 |  |
| 4 | 编辑文档 | 选择 编辑 （位于右上角）。在 中 凭证数据 部分，将 文档 状态 调入 工作中 。在 中 原件 部分，选择 上载 ， 然后从您的 PC 附加 PRT 文档。选择 保存 。 | 文档已保存。 |  |
| 5 | 审批凭证 | 选择 编辑 （位于右上角）。在 中 凭证数据 部分，将 文档 状态 整数 已发布 。选择 保存 。 | 文档已保存。 |  |

#### 创建设备 PRT

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

本章介绍如何创建设备 PRT。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 维护计划员 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建技术对象 (W0029) 。 | 应用随即打开。 |  |
| 3 | 创建设备 | 在 创建技术对象 屏幕上，选择 技术对象类型：设备 。在下一屏幕中，输入以下内容：技术对象类型 ： 设备技术对象 ： 留空有效自 ： 当天日期技术对象类别 ： P（生产资源/工具）选择 继续 。 |  |  |
| 4 | 维护常规数据 | 在 创建技术对象：<设备标识> 屏幕的 常规数据 部分， 输入以下内容：描述 ： <例如，PRT 设备>或者，维护更多常规数据，然后导航到 生产资源/工具 数据 部分。 | 因此， 创建技术对象：一般数据 屏幕。 |  |
| 5 | 维护 PRT 数据 | 在 中 PRT 数据 部分，输入以下内容：任务清单用途 ： 009（所有任务清单类型）控制代码 ： 1（所有功能）或者，维护更多详细信息。例如，您可以创建测量点 与一些 Characteristics 一起指派，然后附加 字段中的测量点 测量点 ， 并选中字段的复选框 加载 记录 。 | 因此， 创建技术对象：位置数据 屏幕。 |  |
| 6 | 保存设备 | 或者，您可以维护其他部分的附加信息。选择 保存 。 | 已创建设备。记录设备编号。 |  |

### 在工艺路线中分配生产资源/工具（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

本章介绍如何分配工艺路线中的物料 PRT、杂项 PRT、文档 PRT 或设备 PRT。您可以分配不同的类型 需要生产资源和工具到任务清单和生产订单。分配到任务清单的 PRT 将自动复制到生产订单。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产工程师 - 离散制造 。 | 因此， 启动 页面。 |  |
| 2 | 打开 SAP Fiori 应用 | 打开 更改工艺路线 (CA02) 。 | 随即打开一个新窗口，显示 更改工艺路线：初始 屏幕 。 |  |
| 3 | 输入物料 | 输入以下内容并选择 。 继续 ：材料 ： <物料 编号>工厂 ： <工厂代码> ，例如 1010 | 因此， 更改工艺路线：工序概览 屏幕。 |  |
| 4 | 选择工序 | 选择项目并选择 操作 。选择要分配 PRT 的工序。然后选择 PRT 。 | 因此， 更改工艺路线：PRT 概览 屏幕。 |  |
| 5 | 分配物料 PRT | 如果工序中不存在 PRT，请进行以下操作 对话框中的条目： 更改工艺路线：新建 PRT 。如果已存在，请选择 材料 ，输入以下内容并 按绿色复选标记：PRT 项目编号 ： <0010>材料 ： <物料 编号> ，例如 PRT_01工厂 ： <工厂 代码> ，例如 1010 | 物料 PRT 已分配到工序 。 |  |
| 6 | 分配杂项 PRT | 选择 其他 ，输入以下内容并 按绿色复选标记：PRT 项目编号 ： <0020>生产资源/工具 ： <名称> ，例如 PRT_02 | 杂项 PRT 已分配到工序 。 |  |
| 7 | 分配文档 PRT | 选择 文档 ，进行以下输入 并按绿色复选标记：PRT 项目编号 ： <0030>文档 ： <凭证编号 已在先前步骤中创建>凭证类型 ： <SPP>凭证部分 ： <000>文档版本 ： <00>数量 ： <1 EA>控制参数 ： <1> | 文档 PRT 已分配到工序 。 |  |
| 8 | 分配设备 PRT | 选择 设备 ，输入以下内容并选择绿色 复选标记：设备 ： <上一步骤中创建的设备编号> |  |  |
| 9 | 保存更改 | 选择 保存 。 | 已保存工艺路线。 |  |

### 在生产订单中分配 PRT（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

本章介绍如何为生产订单中的工序分配物料 PRT、杂项 PRT、文档 PRT 或设备 PRT。制造 确保已预先创建生产订单。在订单创建期间，还可以在工序概览标签中分配 PRT。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 生产主管 - 离散制造 。 | 因此， 启动 页面。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 更改生产订单 (CO02) 。 | 随即打开一个新窗口，显示 生产订单更改： 初始屏幕 。 |  |
| 3 | 输入订单信息 | 输入以下内容并选择 。 继续 ：订单 ： <订单编号> | 因此， 生产订单创建：更改 屏幕。 |  |
| 4 | 选择操作 | 选择 操作 。在 中 工序概览 表，选中一个复选框 操作，例如， 工序 0010 ， 并选择 生产资源/工具 。 | 新对话框 生产订单更改：PRT 新 条目 如果 中不存在 PRT，则会显示 操作。如果已存在任何，则 生产资源/工具概览 表将显示。 |  |
| 5 | 分配物料 PRT | 如果工序中不存在 PRT，请在对话框中输入以下内容 生产订单更改：PRT 新 条目 ：如果已存在，则选择 + 时间 底部 生产资源/工具 概览 并输入以下内容：项目编号 ：例如， 0010材料 ：例如， PRT_01工厂 ：例如， 1010选择绿色复选标记。 | 物料 PRT 已分配到工序 。 |  |
| 6 | 分配杂项 PRT | 选择 + 位于底部 生产 资源/工具概览 然后选择 其他 。然后进行以下操作 条目：项目编号 ：例如， 0020生产资源/工具 ：例如， PRT_02选择绿色复选标记。 | 杂项 PRT 已分配到工序 。 |  |
| 7 | 分配文档 PRT | 选择 + 位于底部 生产 资源/工具概览 然后选择 文档 。然后进行以下操作 条目：项目编号 ： <0030>文档 ： <先前创建的凭证编号 步骤>凭证类型 ： <SPP>凭证部分 ： <000>文档版本 ： <00>数量 ： <1 EA>控制代码 ： <1>选择绿色复选标记。 | 文档 PRT 已分配到工序 。 |  |
| 8 | 分配设备 PRT | 选择 + 位于底部 生产资源/工具概览 以及 选择 设备 。然后输入以下内容：设备 ： <上一步骤中创建的设备编号>控制参数文件 ： 1（所有功能）选择绿色复选标记。 |  |  |

## 附录

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
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-resources-tools-mds-5cp-437]]
- related-to :: [[12-production-and-manufacturing/master-data-script-mds-5cp-japanese-439]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-medios-auxiliares-de-fabricacion]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 11,886 chars in the whole document
