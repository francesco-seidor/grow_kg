---
id: 06-management-accounting/mds-2us-291
title: 主数据脚本 - 创建通用分配主数据 - MDS (2US) (2US_S4CLD2608_Master_Data_ZH_XX)
description: Chinese master data script (MDS 2US) for testing universal allocation cycles (plan/actual overhead and profit center allocations) in SAP S/4HANA Cloud Public Edition.
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/universal-allocation]
aliases: [2US_S4CLD2608_Master_Data_ZH_XX]
keywords: [Universal Allocation Cycles, universal allocation, overhead allocation cycles, actual allocation, planned allocation, profit center allocation, manage allocations app, business roles, cost centers, allocation template upload]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-291
topic: 06-management-accounting/universal-allocation
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 主数据脚本 - 创建通用分配主数据 - MDS (2US) (2US_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Universal Allocation Cycles** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建通用分配主数据 - MDS (2US) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897462)

[2 前提条件 4](#_Toc233897463)

[2.1 系统访问 4](#_Toc233897464)

[2.2 角色 4](#_Toc233897465)

[2.3 所需组织单位 4](#_Toc233897466)

[2.4 必填和可选主数据 5](#_Toc233897467)

[3 概览表 6](#_Toc233897468)

[4 测试过程 7](#_Toc233897469)

[4.1 计划分配 7](#_Toc233897470)

[4.1.1 管理计划间接费用分摊周期 7](#_Toc233897471)

[4.1.2 编辑计划间接费用分摊周期 9](#_Toc233897472)

[4.2 实际分配 11](#_Toc233897473)

[4.2.1 管理实际间接费用分摊周期 11](#_Toc233897474)

[4.2.2 编辑实际间接费用分摊周期 14](#_Toc233897475)

[4.3 计划利润中心分配 16](#_Toc233897476)

[4.3.1 管理计划利润中心分配周期 16](#_Toc233897477)

[4.4 实际利润中心分配 18](#_Toc233897478)

[4.4.1 管理实际利润中心分配周期 18](#_Toc233897479)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

通用分配涵盖成本中心的计划和实际分摊/分配 在间接费用成本控制中使用各种发送方/接收方金额组合， 百分比和部分。此主数据支持年度计划，通过 通过预定义的分配和分配周期重新分配成本 特定公司代码。通过将成本要素分配到间接费用中的成本中心， 成本控制，您可以控制成本，并比较计划和实际成本。位于 利润中心的附加、计划和实际分摊/分配也是 支持。

此脚本提供使用通用创建主数据的一些常规示例。 分配，但可以通过以下方式根据您的特定业务需求进行调整 金额、百分比和部分的各种发送方/接收方组合。

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
| 部门会计 | SAP_BR_DIVISION_ACCOUNTANT |  |  |  |

### 所需组织单位

贵公司的组织结构和主数据在 ERP 中创建 系统。组织结构反映以下内容的结构： 您的公司。主数据表示成本中心和成本中心组，具体取决于 公司的运营重点。

| 数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 成本控制范围 | 常规数据 | 必填 |  |
| 公司代码 | 组织单位 | 必填 |  |

### 必填和可选主数据

成本中心和成本中心组主数据记录可能参考其他主数据。下表提供了可选 和 的概览 分配中使用的必填主数据对象。

| 主数据对象 | 必填/可选 | 备注 |
| --- | --- | --- |
| 成本中心 | 必填 |  |
| 成本要素 | 必填 |  |
| 统计关键指标 | 可选 |  |
| 利润中心 | 必填 |  |

## 概览表

此范围项目由下列流程步骤组成： 表：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

计划分配

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [管理计划间接费用分摊周期](#unique_8) [第 ] 页 7 | 成本会计 - 间接费用 | 管理分配 (F3338A) | 将成本分配到成本中心组、成本中心或 ranges。 |
| [编辑计划间接费用分摊周期](#unique_9) [第 ] 页 9 | 成本会计 - 间接费用 | 管理分配 (F3338A) | 编辑计划间接费用分配周期。 |

实际分配

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [管理实际间接费用分摊周期](#unique_10) [第 ] 页 11 | 成本会计 - 间接费用 | 管理分配 (F3338A) | 将成本分配到成本中心组、成本中心或 ranges。 |
| [编辑实际间接费用分摊周期](#unique_11) [第 ] 页 14 | 成本会计 - 间接费用 | 管理分配 (F3338A) | 编辑实际间接费用分配周期。 |

计划利润中心分配

| 流程步骤 | 业务角色 | 事务/应用 | 预期 RPS 结果 |
| --- | --- | --- | --- |
| [管理计划利润中心分配周期](#unique_12) [第 ] 页 16 | 部门会计 | 管理分配 (F3338A) | 创建计划利润中心分配。 |

实际利润中心分配

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [管理实际利润中心分配周期](#unique_13) [第 ] 页 18 | 部门会计 | 管理分配 (F3338A) | 创建利润中心分配。 |

## 测试过程

### 计划分配

#### 管理计划间接费用分摊周期

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

在此示例中，计划间接费用分摊循环使用 次级成本要素，用于从一个成本中心或一组成本中心分配成本 按同一范围内的固定百分比向另一个成本中心或成本中心组。 公司代码。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理分配 (F3338A) 。 | 因此， 管理分配 视图。 |  |
| 3 | 创建周期抬头 | 选择 创建 按钮并选择 新建 周期 。 | 因此， 新建周期 对话框。备注 批量上载 分配周期可用于新建 分配和/或新的段，通过 管理 分配 应用使用 上载/下载模板 按钮。您 可以下载空白模板或选择现有模板 作为模板下载的分配周期。 |  |
| 4 | 输入值 | 输入以下内容并选择 。 创建 按钮：分配周期 ： <输入以...开头的周期标识 Z>分配上下文 ： <成本 中心>分配类型 ： 间接费用 分配分类账 ： 0L有效期至 ： 12/31/2030周期描述 ： <输入周期 描述>公司代码 ： 1010实际/计划： 计划计划类别 ： PLN | 因此， <新周期> 视图。 |  |
| 5 | 输入段数据 | 在 的下半部分 新分配周期 视图（在 细分 节，选择 创建 按钮和 在 新建 段 窗口并选择 创建 按钮：细分名称 ： <输入 以 Z 开头的段>段描述： <输入 描述> | 因此， <新段> 视图。 |  |
| 6 | 输入规则 | 选择新段并选择右侧的箭头。在 中 规则 标签上，输入以下内容：间接费用分配科目 ： 94201000发送方规则 ： 已过账 金额接收方规则 ： 固定 百分比份额百分比： 100货币 ： <输入本地 货币> |  |  |
| 7 | 输入发送方详细信息 | 在 中 发送方 标签上，输入以下内容：账号 ：更改 中的值 价值 类型 列 分组在 中 分组 列，使用 要选择的下拉列表 10_CE 位于以下 选择：账号 视图成本中心 ： 10101101 |  |  |
| 8 | 输入接收方详细信息 | 在 中 接收方 标签上，选择 添加 . 在 中 添加接收方 视图，选择 成本中心 然后选择 添加 。输入以下内容：成本中心更改 中的值 价值 类型 列 分组在 中 分组 列，使用 要选择的下拉列表 1010300 位于以下 选择：成本中心 视图 |  |  |
| 9 | 接收方基础 | 在 中 接收方基础 标签，选择 …（附加 选项） 按钮，然后选择 平均分配 。 | 您可以看到金额平均分配。 |  |
| 10 | 保存 | 选择 保存 按钮。 | 您的数据已保存。 |  |

#### 编辑计划间接费用分摊周期

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

此活动演示如何使用分配 使用模板处理大量数据。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理分配 (F3338A) 。 | 因此， 管理分配 视图。 |  |
| 3 | 输入值 | 输入以下内容并选择 。 执行 按钮：分配上下文 ： <成本中心>公司代码： 1010分类账： 0L分配周期 ： <在 刚刚创建的周期> | 因此， 分配周期 视图。 |  |
| 4 | 分配周期详细信息 | 选择分配周期，然后选择右侧的箭头转到详细信息。 选择 编辑 按钮。 | 因此， 管理分配 视图。 |  |
| 5 | 段部分 | 向下滚动至 细分 部分并选择您的细分，然后选择 > ( 明细 ），位于 right。 |  |  |
| 6 | 接收方基础 | 在 中 接收方基础 标签上，选择 上载/下载 值 。 | 因此， 上载接收方值 视图。 |  |
| 7 | 上载接收方值 | 选择 下载包含值的模板 . 下载并保存 file。 |  |  |
| 8 | 更新百分比 | 在文件中，使用如下所示的值更新百分比列：成本中心百分比001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | 百分比已更新。 |  |
| 9 | 接收方基础 | 返回到 接收方基础 标签并执行以下操作：选择 上载/下载值 。位于 上载接收方值 视图、 选择 浏览 。选择您保存的 file。屏幕指示值是否可以上载，或者 如果需要更正。选择 确认 。选择 保存 保存分配 循环。 | 您可以看到数据已经根据 csv 文件上载进行更新。 |  |

### 实际分配

#### 管理实际间接费用分摊周期

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

在此示例中，间接费用分摊周期使用次级成本 要素，用于将成本从一个成本中心或一组成本中心分配到另一个成本中心 相同公司代码内按固定百分比划分的成本中心或成本中心组。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理分配 (F3338A) 。 | 因此， 管理分配 视图。 |  |
| 3 | 创建周期抬头 | 选择 创建 按钮并选择 新建 周期 。 | 因此， 新建周期 对话框。 |  |
| 4 | 输入值 | 输入以下内容并选择 。 创建 按钮：分配周期 ： <输入以...开头的周期标识 Z>分配上下文 ： <成本中心>公司 代码 ： 1010分配类型 ： 间接费用 分配分类账 ： 0L有效期至 ： 12/31/2030周期描述 ： <输入周期 描述>公司代码 ： 1010实际/计划： 实际 | 因此， 分配：创建计划间接费用分配周期：抬头数据 视图。 |  |
| 5 | 输入段数据 | 在 的下半部分 新建分配周期 视图（在 细分 部分，选择 添加 按钮并在 新建 段 窗口：细分名称 ： <输入以 Z 开头的段>段描述： <输入描述> | 因此， 新建周期 视图。 |  |
| 6 | 输入规则 | 选择新段并选择右侧的箭头。在 中 规则 标签上，输入以下内容：间接费用分配科目 ： 94201000发送方规则 ： 已过账金额接收方规则 ： 固定百分比 |  |  |
| 7 | 输入发送方详细信息 | 在 中 发送方 标签上，输入以下内容：账号 ：更改 中的值 值类型 列 分组在 中 分组 列中，使用下拉列表搜索并选择 10_CE 位于以下 选择：账号 视图成本中心 ： 10101101备注 此外 至标准成本中心和总账科目，您可以 现在使用特定的日记帐分录属性，例如 货币、功能区、利润中心和 段以启用更精细的分配选择 发送方规则内。为此，请选择 添加 按钮，然后选择 所需选项。 |  |  |
| 8 | 输入接收方详细信息 | 在 中 接收方 标签，选择 +（添加） 按钮。选择 成本中心 ，然后选择 添加 按钮。输入以下内容：成本中心更改 中的值 值类型 列 分组在 中 分组 列中，使用下拉列表搜索并选择 1010300 位于以下 选择：成本中心 视图 |  |  |
| 9 | 接收方基础 | 在 中 接收方基础 标签，选择 …（附加 选项） 按钮，然后选择 平均分配 。 | 您可以看到金额平均分配。 |  |
| 10 | 保存 | 选择 保存 按钮。 | 您的数据已保存。 |  |

#### 编辑实际间接费用分摊周期

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

此活动演示如何使用分配 使用模板处理大量数据。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 成本会计 - 间接费用 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理分配 (F3338A) 。 | 因此， 管理分配 视图。 |  |
| 3 | 输入值 | 输入以下内容并选择 。 执行 按钮：分配上下文 ： <成本中心>公司代码： 1010分类账： 0L分配周期 ： <在 刚刚创建的周期> | 因此， 分配周期 视图。 |  |
| 4 | 分配周期详细信息 | 选择分配周期，然后选择右侧的箭头转到详细信息。 | 因此， 管理分配 视图。 |  |
| 5 | 段部分 | 向下滚动至 细分 部分并选择您的细分，然后选择 > ( 明细 ），位于 right。 |  |  |
| 6 | 接收方基础 | 在 中 接收方基础 标签，选择 上载/下载 值 。 | 因此， 上载接收方值 视图。 |  |
| 7 | 上载接收方值 | 选择 下载包含值的模板 . 下载并保存 file。 |  |  |
| 8 | 更新百分比 | 在文件中，使用如下所示的值更新百分比列：成本中心百分比001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | 百分比已更新。 |  |
| 9 | 接收方基础 | 返回到 接收方基础 标签并执行以下操作：选择 上载/下载值 。位于 上载接收方值 视图、 选择 浏览 。选择您保存的 file。屏幕指示值是否可以上载，或者 如果需要更正。选择 确认 。选择 保存 保存分配 循环。 | 您可以看到数据已经根据 csv 文件上载进行更新。 |  |

### 计划利润中心分配

#### 管理计划利润中心分配周期

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

此示例显示资产负债表科目余额到 和 的计划分配 来自多个利润中心。

前提条件

分配清算的总账科目必须可用。 使用总账 29500100 作为参考创建总账 29500000 CO 分配清算。有关详细信息 有关如何创建总账的信息，请参阅 创建总账科目和成本要素 - MDS (BNG)。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 部门会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理分配 (F3338A) 。 | 因此， 管理分配 视图。 |  |
| 3 | 创建周期抬头 | 选择 创建 按钮并选择 新建周期 。 | 因此， 新建周期 对话框。 |  |
| 4 | 输入值 | 输入以下内容并选择 。 创建 按钮：分配周期 ： <输入以...开头的周期标识 Z>分配上下文 ： <利润中心>公司 代码 ： 1010分配与分摊 类型 ： 分布分类账 ： 0L有效期至 ： 12/31/2030周期描述 ： <输入周期 描述>公司代码 ： 1010实际/计划： 计划计划类别 ： PLN | 因此， 管理分配 视图。 |  |
| 5 | 输入段数据 | 在 的下半部分 管理 分配 视图（在 段 部分，选择 创建 按钮并在 创建 新建段 窗口：细分名称 ： <输入其他 以 ZD 开头的段>细分描述 ： <输入 a 描述>选择 确定 。 |  |  |
| 6 | 输入规则 | 在 中 规则 标签上，执行以下操作 条目：货币： <输入本地 货币>发送方规则： 固定金额份额 (%) ： 100接收方规则： 固定 百分比选择 发送方 标签。 |  |  |
| 7 | 输入发送方详细信息 | 在 中 发送方 标签上，执行以下操作 条目：账户 编号 ： 29500000利润中心 ： YB600选择 发送方基础 标签。 |  |  |
| 8 | 发送方基础 | 输入以下内容：金额 ： 100000选择 接收方 标签。 |  |  |
| 9 | 输入接收方详细信息 | 在 中 接收方 标签上，选择 + 添加） . 在 中 添加 接收方 视图，选择 利润 居中 。选择 添加 按钮并输入以下内容：值类型 ： 间隔单一条目/自 ： YB700截止值 ：YB800选择 接收方基础 标签。 |  |  |
| 10 | 接收方基础 | 在 中 接收方基础 标签上，选择 …（附加选项） 按钮，然后选择 平均分配 。 | 您可以看到金额平均分配。 |  |
| 11 | 保存 | 选择 保存 按钮。 | 创建计划利润中心分配。 |  |

### 实际利润中心分配

#### 管理实际利润中心分配周期

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

上下文

此示例显示资产负债表科目余额的实际分配。 各种利润中心。

前提条件

分配清算的总账科目必须可用。创建总账 29500000 CO 使用总账 29500100 作为参考进行分配清算。有关如何创建 的详细信息 G/L，请参阅 创建总账科目和成本要素 - MDS (BNG)。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 部门会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理分配 (F3338A) 。 | 因此， 管理分配 视图。 |  |
| 3 | 创建周期抬头 | 选择 创建 按钮并选择 新建周期 。 | 因此， 新建周期 对话框。 |  |
| 4 | 输入值 | 输入以下内容并选择 。 创建 按钮：分配周期 ： <输入以...开头的周期标识 Z>分配上下文 ： <利润中心>公司 代码 ： 1010分配与分摊 类型 ： 分布分类账 ： 0L有效期至 ： 12/31/2030周期描述 ： <输入周期 描述>公司代码 ： 1010实际/计划： 实际 | 因此， 分配：创建计划分配周期：抬头 数据 视图。 |  |
| 5 | 输入段数据 | 在 的下半部分 管理 分配 视图（在 段 部分，选择 添加 按钮并在 中输入以下内容： 创建新细分 窗口：细分名称 ： <输入其他 以 ZD 开头的段>细分描述 ： <输入 a 描述> | 因此， 分配：创建计划分配周期：抬头 数据 视图。 |  |
| 6 | 输入规则 | 选择新建的细分并选择 > 符号 right。在 中 规则 标签上，设置 以下条目：货币： <输入本地 货币>发送方规则： 固定 金额份额 (%) ： 100接收方规则： 固定 百分比选择 发送方 标签。 |  |  |
| 7 | 输入发送方详细信息 | 在 中 发送方 标签上，执行以下操作 条目：账户 编号 ： 29500000利润中心 ： YB600选择 发送方基础 标签。 |  |  |
| 8 | 发送方基础 | 输入以下内容：金额 ： 100000选择 接收方 标签。 |  |  |
| 9 | 输入接收方详细信息 | 在 中 接收方 标签上，选择 + 添加） . 在 中 添加 接收方 视图，选择 利润 居中 。选择 添加 按钮并输入以下内容：值类型 ： 间隔单一条目/自 ： YB700截止值 ：YB800选择 接收方基础 标签。 |  |  |
| 10 | 接收方基础 | 在 中 接收方基础 标签上，选择 …（附加选项） 按钮，然后选择 平均分配 。 | 您可以看到金额平均分配。 |  |
| 11 | 保存 | 选择 保存 按钮。 | 创建利润中心分配。 |  |

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
- related-to :: [[06-management-accounting/create-universal-allocation-master-data-mds-2us-287]]
- related-to :: [[06-management-accounting/mds-2us-289]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-dados-mestre-de-alocacao-universal-mds-2u]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-datos-maestros-de-asignacion-universal]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 13,909 chars in the whole document
