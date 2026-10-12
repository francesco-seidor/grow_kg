---
id: 03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-bni-615
title: 主数据脚本 SAP S/4HANA Cloud Public Edition - 创建资产 - MDS (BNI) (BNI_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) master data script for fixed asset master records in S/4HANA Cloud Public Edition 2608: prerequisites, asset classes, and test steps via F3425A."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/fixed-asset-master-data]
aliases: [BNI_S4CLD2608_Master_Data_ZH_XX]
keywords: [Fixed Asset Master Records, asset master data, asset classes, number ranges, asset creation, legacy data transfer date, sub-assets, balance carryforward, asset blocking and deletion, depreciation keys]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-615
topic: 03-financial-accounting-and-close/fixed-asset-master-data
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 主数据脚本 SAP S/4HANA Cloud Public Edition - 创建资产 - MDS (BNI) (BNI_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Fixed Asset Master Records** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建资产 - MDS (BNI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897916)

[2 前提条件 4](#_Toc233897917)

[2.1 系统访问 4](#_Toc233897918)

[2.2 角色 4](#_Toc233897919)

[2.3 所需组织单位 4](#_Toc233897920)

[2.4 必填和可选主数据 5](#_Toc233897921)

[2.5 数据创建的主要参数 5](#_Toc233897922)

[2.5.1 资产类和编号范围 5](#_Toc233897923)

[2.6 预备步骤 7](#_Toc233897924)

[2.6.1 验证资产会计系统就绪状况 7](#_Toc233897925)

[2.6.1.1 确认接管日期信息 7](#_Toc233897926)

[2.6.1.2 确认当前会计年度的余额结转运行 9](#_Toc233897927)

[3 概览表 12](#_Toc233897928)

[4 测试过程 14](#_Toc233897929)

[4.1 创建资产 14](#_Toc233897930)

[4.2 更改资产 16](#_Toc233897931)

[4.3 显示资产 17](#_Toc233897932)

[4.4 冻结资产 18](#_Toc233897933)

[4.5 删除资产 19](#_Toc233897934)

[4.6 创建资产子资产 20](#_Toc233897935)

[4.7 更改资产主记录的凭证 22](#_Toc233897936)

[4.8 折旧码：显示详细信息 23](#_Toc233897937)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

固定资产是企业拥有的对象、权利或其他项目，旨在长期使用并且可以单独使用 在资产负债表中识别。维护固定资产包括创建、更改和显示资产主记录。

不同的信息项目根据系统中的使用范围和功能进行结构化，以方便用户 创建、维护和评估主数据。

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
| 资产会计 | SAP_BR_AA_ACCOUNTANT | 固定资产 | SAP_BR_AA_ACCOUNTANT |  |
| 总账会计 | SAP_BR_GL_ACCOUNTANT | 总账 | SAP_BR_GL_ACCOUNTANT |  |

### 所需组织单位

固定资产主数据取决于公司的组织单位。

下表提供了此组织单位的概览：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 公司代码数据 | 公司代码 | 标识、描述、成本中心、 等等 | 对于使用固定资产主记录的企业结构的每个公司代码标识，都可以存在公司代码数据。 | <您的公司代码> |

### 必填和可选主数据

固定资产主数据记录 可能参考其他主数据 。因此， 下表提供了可选和必填主数据对象的概览， 用于固定资产主数据记录中。

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 成本中心 | 在资产主数据中，可以在 中找到成本中心 的条目。 时间相关 标签。 | 必填 | 要输入固定资产的成本中心，您必须拥有 之前已创建成本中心。在固定资产主记录中， 然后可以输入实际成本中心。 |

### 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录且 始终需要 创建固定资产主数据 记录：

#### 资产类和编号范围

资产类别确定固定资产主记录编号的编号范围。之后您无法更改分配或标识，只能将其传输到为其他资产类别创建的其他固定资产主记录。如果将资产类分配到内部编号范围，则无法手动输入资产主记录标识。在这种情况下，请将该字段留空，因为系统会自动从分配的数字编号范围中选择一个编号。

在公司代码 1010 中为固定资产定义了以下资产类和相应编号范围：

| 资产类 | 编号范围/资产主记录标识 | 备注 |
| --- | --- | --- |
| 1000 | 内部数字编号范围：10000000 – 19999999 | 不动产和类似权利 |
| 1100 | 内部数字编号范围：10000000 – 19999999 | 建筑物 |
| 1200与所有国家/地区无关 | 内部数字编号范围：10000000 – 19999999 | 土地改良 |
| 1500与所有国家/地区无关 | 内部数字编号范围：10000000 – 19999999 | 租赁物改良 |
| 2000 | 内部数字编号范围：20000000 – 29999999 | 机器和设备 |
| 3000 | 内部数字编号范围：30000000 – 39999999 | 固定设备和装置 |
| 3100 | 内部数字编号范围：50000000 – 59999999 | 车辆 |
| 3200 | 内部数字编号范围：60000000 – 69999999 | 计算机硬件 |
| 3210 | 内部数字编号范围：60000000 – 69999999 | 计算机软件 |
| 3300 | 内部数字编号范围：30000000 – 39999999 | 办公设备 |
| 4000 | 内部数字编号范围：40000000 – 49999999 | 在建工程（有形） |
| 4010 | 内部数字编号范围：40000000 – 49999999 | 在建工程（无形资产） |
| 4001 | 内部数字编号范围：40000000 – 49999999 | 作为投资度量的在建工程（有形） |
| 4011 | 内部数字编号范围：40000000 – 49999999 | 作为投资度量的在建工程（无形） |
| 5000 | 内部数字编号范围：80000000 – 89999999 | 低值资产 |
| 8200 | 内部数字编号范围：90000000 – 99999999 | 商誉 |
| 8300 | 内部数字编号范围：80000000 - 89999999 | 其他无形资产 |
| 9000 | 内部数字编号范围：90000000 - 99999999 | 仅限于税收的资产 |

### 预备步骤

#### 验证资产会计系统就绪状况

##### 确认接管日期信息

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，确认用于输入历史资产的数据接管日期、状态和凭证类型的值。

|  |
| --- |
| 备注 初始内容激活完成后，必须定义接管日期。定义当前会计年度和过去 在资产会计中关闭的会计年度。接管日期对于系统处理至关重要，因为它标识了 加载旧资产值。对于 SAP S/4HANA Cloud Public 版本 系统，这通常是上一年结束日期。例如，如果系统为 FY-2020 且 公司位于标准日历会计年度中，接管日期为 2020 年 12 月 31 日。 |

|  |
| --- |
| 注意 这意味着自 2020 年末起加载旧历史资产。 |

过程

| 流程步骤# | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 Fiori 应用 | 打开 进行公司代码设置 - 资产会计特定 (F7312) 。 | 因此， 显示资产会计中公司代码的设置 屏幕。要在更改和显示模式之间切换，请选择 更改/显示 。 |  |
| 3 | 选择公司代码 | 在屏幕左侧选择公司代码，然后选择 选择公司代码 。 |  |  |
| 4 | 常规设置 | 选择 常规设置 标签。 |  |  |
| 5 | 检查常规设置 | 检查公司的状态。 | 因此， 基本信息 标签显示您的公司代码设置。因此， 公司代码状态 应该是 用于测试 。 |  |
| 6 | 维护历史数据传输的参数 | 在 中 历史数据传输 部分，检查或 更改以下条目：备注 如果需要，首先通过选择创建新的历史传输细分 创建历史传输细分 。传输日期 ： 用于测试目的集 此日期到上一年度结束的最后一天。历史数据传输状态 ： 出于测试目的，将此状态设置为“上线”（允许其他过账）凭证类型 ： 用于测试目的集 这个到 AA备注 对于 传输日期 值，通常是上一年的年末日期。如果指示您使用年中日期，则为月末日期。日期应始终向前移动（不要将其向后更改）。备注 对于 历史数据传输状态 价值，您 有四个选项：准备中：系统允许不完整定制 历史数据传输的设置（无凭证过账 此阶段中允许。）进行中：仅允许历史数据传输过账（针对 例如，其他类型的过账、购置、报废 不允许。）进行中（允许其他过账）：两种历史数据传输 允许过账和其他过账。此状态使 当您在 中执行更多历史数据传输时， 已生产的公司代码。已完成：历史数据传输已完成。历史数据 不允许传输过账，并且不允许 创建历史资产。 |  |  |
| 7 | 保存更改 | 选择 菜单 > 常规 > 保存 。 |  |  |

##### 确认当前会计年度的余额结转运行

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，您确认已运行当前会计年度的余额结转。

|  |
| --- |
| 备注 如果您的实施不使用特定分类账，则忽略该分类账。 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 总账会计 。 |  |  |
| 2 | 访问 SAP Fiori 应用 | 打开 计划总账作业 (F1927) 。 |  |  |
| 3 | 创建 | 选择 创建 。 |  |  |
| 4 | 输入详细信息 | 输入以下内容并选择 步骤 2 ：作业模板 ： 余额结转作业名称 ： 余额结转 |  |  |
| 5 | 输入详细信息 | 输入以下内容并选择 步骤 3 ：立即开始 ： 已选择 |  |  |
| 6 | 输入详细信息 | 输入以下内容并选择 计划 ：分类账 ： <分类账> ，例如， 0L公司代码 ： <公司代码>结转至会计年度 ： <会计年度>测试运行 ： 已选择 | 已将作业运行计划为测试运行。 |  |
| 7 | 检查结果 | 要检查测试运行的结果，请在 作业 窗格并选择其行右侧的箭头按钮。 |  |  |
| 8 | 运行详细信息 | 选择 运行详细信息 标签。检查日志状态。 |  |  |
| 9 | 生产运行 | 要执行生产运行，请重复此流程，但取消选择 测试运行 。 | 已将作业运行计划为生产运行。 |  |

## 概览表

此范围项目由下表中列出的流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务/应用 | 预期结果 |
| --- | --- | --- | --- |
| [创建资产](#unique_12) [第 ] 页 14 | 资产会计 | 打开 管理固定资产 (F3425A) | 固定资产主数据在公司代码（折旧表）级别创建。 |
| [更改资产](#unique_13) [第 ] 页 16 | 资产会计 | 打开 管理固定资产 (F3425A) | 固定资产主数据已更新。 |
| [显示资产](#unique_14) [第 ] 页 17 | 资产会计 | 打开 管理固定资产 (F3425A) | 显示固定资产主数据。 |
| [冻结资产](#unique_15) [第 ] 页 18 | 资产会计 | 打开 管理固定资产 (F3425A) | 固定资产 已冻结。 |
| [删除资产](#unique_16) [第 ] 页 19 | 资产会计 | 打开 管理固定资产 (F3425A) | 固定资产主数据已删除。 |
| [创建资产子资产](#unique_17) [第 ] 页 20 | 资产会计 | 打开 管理固定资产 (F3425A) | 已创建子资产。 |
| [更改资产主记录的凭证](#unique_18) [第 ] 页 22 | 资产会计 | 打开 管理固定资产 (F3425A) | 显示现有资产主数据记录（主资产或子资产）的所有过去更改。 |
| [折旧码：显示详细信息](#unique_19) [第 ] 页 23 | 资产会计 | 折旧码：显示详细信息 (FAA_DEPRKEY_SHOW)备注 如果已为新设计激活功能切换，则应用 折旧码：显示详细信息 (FAA_DEPRKEY_SHOW) 将不适用。 | 通过此应用，提供有关标准内容提供的折旧码背后的设置的信息。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建资产

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，您可以创建新的资产主数据记录作为日常业务的一部分。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理固定资产 (F3425A) 。 | 因此， 管理固定资产 屏幕。 |  |
| 3 | 输入资产主数据详细信息 | 选择 创建 > 创建主资产 。输入以下内容：公司代码 ： <您的公司代码>资产类 ： <要为其创建新资产的资产类>后续资本化 ： <仅在您要使用此主记录过账后资本化时需要>可以使用参考资产主数据。如果需要，应将要用作参考的资产输入到 资产主编号 字段（ 参考 部分。选择 确定 。 | 因此， 创建主资产 屏幕。 |  |
| 4 | 输入资产描述和基本计量单位 | 输入以下内容：描述 ： <您的资产描述>基本计量单位 ： <输入所需计量单位> |  |  |
| 5 | 选择时间相关数据标签 | 选择 时间相关数据 标签。 | 因此， 时间相关数据 标签。 |  |
| 6 | 输入成本中心 | 输入以下内容：成本中心 ： <您的成本中心>WBS_Element ： <您的 WBS_Element>备注 成本中心 和/或 WBS_Element 允许作为折旧的成本收集器输入。 |  |  |
| 7 | 输入资本化日期 | 您只需输入 资本化日期 创建资产时， 后续资本化 标识。资本化日期 ： <您的资本化日期> |  |  |
| 8 | 检查其他标签 | 转到其他标签并进行任何必要的输入或更改。 |  |  |
| 9 | 输入、检查或调整折旧参数 | 为所有可用折旧范围输入以下内容：DKey ： <您的折旧码>备注 如果已为新设计激活功能切换，请使用 折旧参数文件而非折旧码。使用年限 ： <使用年限（年）>期间 ： <使用年限（期间）> | 所有必需的折旧参数均已正确维护。 |  |
| 10 | 保存新资产主数据 | 选择 创建 保存您的输入。 | 创建资产主记录。系统会显示一条消息，确认创建并显示新资产编号。 |  |

### 更改资产

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，您可以更改现有资产主数据记录（主编号或子编号）作为日常业务的一部分。

|  |
| --- |
| 备注 只有通过公司内转移到在新资产类中创建的新资产主记录，才能更改资产类。 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理固定资产 (F3425A) 。 | 因此， 管理固定资产 屏幕。 |  |
| 3 | 输入资产信息 | 输入以下内容：公司代码 ： <您的公司代码>资产 ： <您的资产编号>选择 执行 。使用资产编号链接从表中选择资产编号。在下一屏幕中，选择 编辑 。 | 因此， 管理固定资产 屏幕。备注 通过选择资产、选择要在对话框中显示的操作，然后再次选择该操作，可以使用显示、更改和删除功能。 |  |
| 4 | 更改资产主数据 | 对资产主数据进行所需更改。 | 进行所需更改。 |  |
| 5 | 保存已更改的资产主数据 | 选择 创建 保存您的输入。备注 系统显示 成功 通知。您需要验证更改。 | 资产主数据更改已保存。执行的更改显示在 变更文档 标签。 |  |

### 显示资产

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，可以将现有资产数据记录（主编号或子编号）显示为日常业务的一部分。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理固定资产 (F3425A) 。 | 因此， 管理固定资产 屏幕。 |  |
| 3 | 输入资产信息 | 输入以下内容：公司代码 ： <您的公司代码>资产 ： <您的资产编号>子编号 ： <案例中的资产子编号>选择 执行 。选择您的 资产编号 ，通过使用含资产编号的链接从表中获取。通过选择每个科目检查资产主记录 标签 页面。 |  |  |

### 冻结资产

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，锁定现有资产主数据记录（主或子编号）以供进一步购置。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理固定资产 (F3425A) 。 | 因此， 管理固定资产 屏幕。 |  |
| 3 | 输入资产信息 | 输入以下内容并选择 执行 ：公司代码 ： <您的公司代码>资产 ： <您的资产编号> | 因此， 管理固定资产 屏幕。 |  |
| 4 | 设置锁定标识 | 选择您的 资产编号 从表中删除。在新屏幕上，选择 冻结 。备注 因此， 资产 <资产编号> 已冻结 显示 个通知。 | 设置锁定标识。资产已锁定，无法进一步购置。执行的更改显示在 变更文档 标签。 |  |

### 删除资产

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，您可以删除现有资产主数据记录（主编号或子编号）。

|  |
| --- |
| 备注 只能直接删除无资本化日期和无值的资产。 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理固定资产 (F3425A) 。 | 因此， 管理固定资产 屏幕。 |  |
| 3 | 输入资产信息 | 输入以下内容并选择 执行 ：公司代码 ： <您的公司代码>资产 ： <您的资产编号> |  |  |
| 4 | 设置删除标识 | 选择您的 资产编号 ，然后在新屏幕上选择 删除 。 | 已设置该标识。 |  |
| 5 | 确认 | A 是否删除对象 ？ 消息将显示在屏幕上。选择 删除 进行确认。 |  |  |

### 创建资产子资产

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，您可以创建新的资产子资产数据记录作为日常业务的一部分。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理固定资产 (F3425A) 。 | 因此， 管理固定资产 屏幕。 |  |
| 3 | 输入主要资产参考 | 在 管理固定资产 屏幕上，选择 创建资产 > 创建资产子资产 。输入以下条目，然后按 输入 ：公司代码 ： <您的公司代码>资产 ： <要为其创建子资产的资产主编号>后续资本化 ： <仅在您要使用此主记录过账后资本化时需要> | 因此， 创建子资产 屏幕。因此， 常规 标签。 |  |
| 4 | 输入基本信息 | 在 常规 标签上，输入以下内容：资产描述 ： <您的资产描述>计量单位 ： <计量单位>资本化日期 ： <您的日期> |  |  |
| 5 | 时间相关数据 | 选择 时间相关数据 标签。 |  |  |
| 6 | 成本中心或 WBS_Element | 创建、检查或调整以下条目：成本中心 ： <您的成本中心>或者 WBS_Element ： <您的 WBS_Element> |  |  |
| 7 | 检查其他标签 | 转到其他标签并进行任何必要的输入或更改。 | 填写所有必填资产主数据字段。 |  |
| 8 | 输入、检查或调整折旧参数 | 针对所有可用折旧范围，根据需要输入或调整以下条目：DKey ： <您的折旧码>备注 如果已为新设计激活功能切换，请使用 折旧参数文件而非折旧码。使用年限 ： <您的使用年限（年）>期间 ： <使用年限（期间）> | 所有必需的折旧参数均已正确维护。 |  |
| 9 | 保存新资产子资产 | 保存输入内容。 | 创建资产主子资产。子资产以 1 开头，例如 xxxxx-1 。 |  |

### 更改资产主记录的凭证

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，可以显示现有资产主数据记录的所有过去更改（主编号或子编号）。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理固定资产 (F3425A) 。 | 因此， 管理固定资产 屏幕。 |  |
| 3 | 输入资产信息 | 输入以下内容并选择 执行 ：公司代码 ： <您的公司代码>资产编号 ： <您的资产编号>资产子编号 ： <您的资产子编号> | 因此， 资产主记录变更 屏幕。 |  |

### 折旧码：显示详细信息

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此活动中，可以显示现有资产主数据记录的所有过去更改 （主资产或子资产）。

|  |
| --- |
| 备注 如果已为新设计激活功能切换，则应用 折旧码：显示详细信息 (FAA_DEPRKEY_SHOW) 将不适用。 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 通过/失败/注释 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 资产会计 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 折旧码：显示详细信息 (FAA_DEPRKEY_SHOW) 。 | 应用随即打开。 |  |
| 3 | 输入资产信息 | 输入以下内容并选择 执行 ：折旧表 ： <折旧表>折旧码 ： <折旧码> | 因此， 折旧表中的折旧码 <XXXX> <XXXX> 屏幕。随即显示所选折旧码后面的设置。 |  |

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
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-asset-bni-sap-s-4hana-cloud-public-edition-6]]
- related-to :: [[03-financial-accounting-and-close/mds-bni-613]]
- related-to :: [[03-financial-accounting-and-close/script-de-dados-mestre-criar-imobilizado-mds-bni-614]]
- related-to :: [[03-financial-accounting-and-close/script-de-datos-maestros-crear-activo-fijo-mds-bni-612]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 15,391 chars in the whole document
