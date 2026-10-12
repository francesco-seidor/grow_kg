---
id: 09-subscription-billing-and-contract-accounting/mds-3ja-327
title: 为基于消耗的开票创建产品主数据 - MDS (3JA) (3JA_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese machine-translated SAP S/4HANA Cloud 2608 master data script (3JA): create configurable product master with characteristics, class, variant pricing for consumption-based billing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/variant-configured-products-in-provider-contracts]
aliases: [3JA_S4CLD2608_Master_Data_ZH_XX]
keywords: [Variant-Configured Products in Provider Contracts, product master data, consumption-based billing, configurable material, characteristics, classes, configuration profile, variant pricing, sales data, material classification]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-327
topic: 09-subscription-billing-and-contract-accounting/variant-configured-products-in-provider-contracts
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 为基于消耗的开票创建产品主数据 - MDS (3JA) (3JA_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Variant-Configured Products in Provider Contracts** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 为基于消耗的开票创建产品主数据 - MDS (3JA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897518)

[2 前提条件 4](#_Toc233897519)

[2.1 系统访问 4](#_Toc233897520)

[2.2 角色 4](#_Toc233897521)

[2.3 所需组织单位 4](#_Toc233897522)

[2.4 必填和可选主数据 5](#_Toc233897523)

[2.5 数据创建的主要参数 5](#_Toc233897524)

[2.5.1 分组和编号范围 5](#_Toc233897525)

[2.5.2 行业部门 6](#_Toc233897526)

[3 概览表 7](#_Toc233897527)

[4 测试过程 8](#_Toc233897528)

[4.1 创建可配置物料主数据 - 基本数据 8](#_Toc233897529)

[4.2 创建特征 10](#_Toc233897530)

[4.3 创建类 12](#_Toc233897531)

[4.4 创建配置参数文件 14](#_Toc233897532)

[4.5 创建物料主数据 - 分类 15](#_Toc233897533)

[4.6 创建变式定价 16](#_Toc233897534)

[4.7 创建产品主数据 - 销售数据/销售税数据 17](#_Toc233897535)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到有关如何为 创建物料主数据记录的描述 SAP S/4HANA Cloud Public 版本 系统。该描述包括与主数据相关的数据段，以便在“常规”系统环境中工作。读取器主要学习哪些数据段和字段通常需要使用输入值填充。与 范围无关的字段 SAP S/4HANA Cloud Public 版本 文档中未描述 内容，尽管它们可能出现在 UI 上。

具有按此处所述创建的变式定价的产品主记录，可用于基于消耗的开票。

## 前提条件

本部分汇总了执行系统、用户、主数据、组织数据、其他测试数据和业务条件方面测试的所有前提条件。

### 系统访问

| 系统 | 明细 |
| --- | --- |
| 系统 | 可通过 SAP Fiori 快速启动板访问。系统管理员为您提供 URL 以获取 访问分配给您的角色的各种应用。 |

### 角色

使用 SAP 提供的以下业务角色模板创建业务角色，并将其分配给各个测试用户。

或者，如果可用，您可以使用 SAP 提供的以下空间。创建包含预定义基本应用的页面的空间，并将其分配到业务角色。然后将此业务角色分配给单个用户。

有关详细信息，请参阅 如何从模板创建业务角色 （在[产品帮助](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) 对于 SAP S/4HANA Cloud Public 版本 。

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） | 登录 |
| --- | --- | --- | --- | --- |
| 产品配置建模器 | SAP_BR_PRODUCT_CONFIG_MODELER | 变式配置 | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST | 主数据 - 产品 / 产品治理 | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### 所需组织单位

主数据的某些段取决于公司的组织单位，常规（中央）数据不取决于组织单位或公司代码。下表提供了这些不同数据段及其相关组织单位的概览：

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 基本数据 | 独立于组织单位 | 物料描述（短文本）、物料编号、物料组、基本计量单位等。 | 物料主数据记录的基本数据仅存在一次。 | 不适用 |
| 销售数据 | 工厂、销售组织、分销渠道 | 税收数据、项目类别组等。 | 对于使用物料主记录的企业结构的每个工厂标识，都可以存在工厂数据。 | 工厂：____________ 销售组织：__________ 分销渠道：__________ |

### 必填和可选主数据

主数据记录可能 参考其他主数据 。下表 提供要在主数据中使用的可选和强制主数据对象的概览。 数据记录。

|  |
| --- |
| 备注 需要巴西特定字段才能获得正确的税收计算。支票 巴西发票 - JD0 中的 定义 BR 特定字段 主数据 章节（针对物料主数据）。 |

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### 数据创建的主要参数

在本节中，我们将介绍一些影响主数据行为的基本参数 记录，并且始终需要用于创建物料主数据记录：

#### 分组和编号范围

借助物料类型，系统确定哪些数据段（视图）可以 或者哪些字段为必填字段或可选字段。根据物料类型， 系统还会确定物料的编号范围。在 SAP 标准内容中，所有 物料类型使用相同的编号范围定义

#### 行业部门

标准内容仅提供一个行业部门 M。目前，这在 SAP 中可见 仅 GUI

## 概览表

此主记录由下表中提供的多个段组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建可配置物料主数据 - 基本数据](#unique_11) [第 ] 页 8 | 主数据专家 - 产品数据 | 创建物料 (MM01) | 创建物料主数据 - 基本数据。 |
| [创建特征](#unique_12) [第 ] 页 10 | 产品配置建模器 | 管理特征 (CT04) | 已创建特征。 |
| [创建类](#unique_13) [第 ] 页 12 | 产品配置建模器 | 管理类 (CL02) | 类已创建。 |
| [创建配置参数文件](#unique_14) [第 ] 页 14 | 产品配置建模器 | VC 建模环境 (PMEVC) | 配置参数文件已创建。 |
| [创建物料主数据 - 分类](#unique_15) [第 ] 页 15 | 主数据专家 - 产品数据 | 创建物料 (MM01) | 创建物料主数据 - 分类。 |
| [创建变式定价](#unique_16) [第 ] 页 16 | 产品配置建模器 | VC 建模环境 (PMEVC) | 变式条件映射到特征值。 |
| [创建产品主数据 - 销售数据/销售税数据](#unique_17) [第 ] 页 17 | 主数据专家 - 产品数据 | 创建物料 (MM01) | 创建物料主数据 - 销售数据（销售税数据）。 |

## 测试过程

本节介绍属于此主数据的每个段或流程步骤的过程。 记录。

### 创建可配置物料主数据 - 基本数据

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此流程步骤中，为物料主数据创建基本数据视图。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建物料 (MM01) 。 | 应用随即打开。 |  |
| 3 | 输入物料基本数据 | 在 创建物料（初始屏幕） 屏幕， 输入以下内容：材料 ： <CBPTS001>工业 部门 ： M备注 如果隐藏行业部门输入字段，则不输入 必需。当未提供行业部门进行输入时， 字段在深色中用 填充。物料类型 ： KMAT - 可配置物料 | 因此， 选择视图 屏幕。 |  |
| 4 | 选择视图 | 在 选择视图 屏幕上，选择 基本数据 1 以及 基本数据 2 ，然后选择 继续 。 | 因此， 创建物料（可配置物料） 屏幕。 |  |
| 5 | 输入基本数据 | 在 创建物料 CBPTS001（可配置物料） 屏幕上的 基本数据 1 标签中，输入物料描述（短文本）。例如，输入 <基于消耗的电动工具> 。 |  |  |
| 6 | 输入基本数据 | 在 基本数据 1 选项卡（ 常规 数据 部分中，输入以下内容：基本单位 度量 ： <PC>一般项目类别组 ： <0003> |  |  |
| 7 | 输入基本数据 | 在 中 维度/EAN 部分中，输入以下内容：重量单位 ： 千克选择 基本数据 2 标签。 |  |  |
| 8 | 输入基本数据 | 在 基本数据 2 标签上，无需进行任何输入。按下 输入 。 | 因此， 到达最后一个数据视图 屏幕显示消息： 您即将退出。你呢？ 是否要先保存此物料的数据？ 。 |  |
| 9 | 保存数据 | 在 到达最后一个数据视图 屏幕上，选择 是 。 | 因此， 创建物料（初始屏幕） 屏幕。创建并保存基本数据。 |  |

### 创建特征

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此流程步骤中，创建特征。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 打开管理客户主数据 | 打开 管理特征 (CT04) 。 | 应用随即打开。 | 创建、更改和显示模式的公用屏幕。 |
| 3 | 输入特征名称 | 输入以下内容并选择 创建 ：特征 ： <类别> | 因此， 创建特征 屏幕。 | 中的值 有效自 字段是 自动填充。如果特征 <CATEGORY> 已存在，则创建 特性 <CATEGORY>_Vnn，其中 nn 正在运行 number。 |
| 4 | 输入基本数据 | 在 基本数据 标签上，输入以下内容：因此， 基本数据 部分：描述 ： <类别>状态 ： 已发布 （缺省值）因此， 格式 部分：数据类型 ： 字符格式字符数 ： <15>区分大小写 ： <取消选择>因此， 值分配 部分：选择 单值 单选按钮。取消选择 可限制 复选框。 |  |  |
| 5 | 输入值 | 在 价值 选项卡（ 允许值 部分中，输入以下内容。特性值 ：<标准><HIGH_END>描述 ：<标准电动工具><高端电动工具>选择 缺省值 复选框 <标准> 值。 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 已创建特征。 |  |
| 7 | 创建另一特征 | 输入以下内容并选择 创建 ：特征 ： <CATEGORY_VARCOND> |  |  |
| 8 | 输入基本数据 | 在 基本数据 标签上，输入以下内容：因此， 基本数据 部分：描述 ： <变式条件键值>状态 ： 已发布（缺省）因此， 格式 部分：数据类型 ： 字符格式字符数 ： <26>区分大小写 ： <已选择>因此， 值分配 部分：选择 多个值 单选按钮。取消选择 可限制 复选框。 |  |  |
| 9 | 输入附加数据 | 在 附加数据 标签上，输入以下内容：因此， 表字段参考 部分：表名称 ： SDCOM字段名称 ： VKOND因此， 值分配的行为 部分：未做好输入准备 ： <取消选择> |  |  |
| 10 | 保存特征 | 选择 保存 。 |  |  |

### 创建类

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此流程步骤中，创建类类型为 300 的类。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理类 (CL02) 。 | 应用随即打开。 | 创建、更改和显示模式的公用屏幕。 |
| 3 | 输入类名称 | 输入以下内容并选择 创建 ：类别 ： <类别>类类型 ： 300 | 因此， 创建类 屏幕。 | 中的值 有效自 字段自动填充。如果类 <CATEGORY> 已存在，则创建类 <CATEGORY>_Vnn，其中 nn 是运行编号。 |
| 4 | 输入基本数据 | 在 基本数据 标签上，输入以下内容：在 中 基本数据 部分：描述 ： <功率 工具类别>状态 ： 已发布 （缺省值）在 中 相同分类 部分：选择 不检查 收音机 按钮（缺省）。 |  | 如果使用相同的分类，则可以选择检查方式（警告 message、error、none）。 |
| 5 | 输入特征 | 在 特征 标签上，输入以下内容：特征 ： <类别>特征 ： <CATEGORY_VARCOND> |  |  |
| 6 | 保存排定课程 | 选择 保存 。 | 类已创建。 |  |

### 创建配置参数文件

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此流程步骤中，创建配置参数文件。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 VC 建模环境 (PMEVC) 。 | 应用随即打开。 |  |
| 3 | 输入配置模型数据 | 在初始屏幕上，输入以下内容并选择 输入模型 ：材料 ： <CBPTS001>类类型 ： 300（缺省） | 随即显示配置屏幕。 |  |
| 4 | 创建配置参数文件 | 在 中 对象 部分，右键单击 <CBPTS001> 并选择 创建 配置参数文件 。在 中 创建配置参数文件 对话框中，进行以下输入：配置参数文件 ： <CBPT_CP_V01>选择 继续 。 | 因此， 配置参数文件 屏幕随即显示在右侧面板中， 在 基本数据 标签。 |  |
| 5 | 保存配置参数文件 | 选择 保存 。 | 配置参数文件已创建。 |  |

### 创建物料主数据 - 分类

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此流程步骤中，为物料主数据创建分类视图。

前提条件

您必须完成上一部分中的步骤，[创建可配置物料主数据 - 基本数据](#unique_11) [第 ] 页 8，然后再继续 节。如上一过程中所述，在保存基本数据条目后开始该过程。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建物料 (MM01) 。 | 应用随即打开。 |  |
| 3 | 输入物料基本数据 | 在 创建物料（初始屏幕） 中，输入以下内容：材料 ： <CBPTS001>行业部门 ： M备注 如果隐藏行业部门输入字段，则无需输入。当行业部门不是 针对条目提供，该字段在深色内填充。物料类型 ： KMAT – 可配置物料 | 因此， 选择视图 屏幕。 |  |
| 4 | 选择视图 | 在 选择视图 屏幕上，选择 分类 以及 选择 继续 。 | 因此， 类类型 (1) 屏幕。 |  |
| 5 | 输入类类型 | 在 中 限制级别 部分中，输入以下内容并选择 继续 ：类类型描述 ： 变式类型 ： 300 | 因此， 分类 屏幕。 |  |
| 6 | 输入分类数据 | 在 分类 屏幕的 短期岗位 标签上，输入以下数据： 在 类别 列，然后选择 保存 ：<类别>在 下 类 CATEGORY 的值 - 对象 <CBPTS001> 标签上，在 中输入以下数据： 价值 列，然后选择 保存 ：<标准><HIGH_END> | 您的数据已保存。 |  |

### 创建变式定价

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

变式条件映射到特征值。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 VC 建模环境 (PMEVC) 。 | 应用随即打开。 |  |
| 3 | 输入配置模型数据 | 在初始屏幕上，输入以下内容并选择 输入模型维护 ：材料 ： <CBPTS001>类类型 ： 300（缺省） | 随即显示配置屏幕。 |  |
| 4 | 创建变式定价 | 在 中 对象 部分，双击 <CBPTS001> ，然后选择 变式 定价 标签。选择 更改 并输入以下内容：特征 ： <类别>特性值 ： <HIGH_END>变式条件 ： <HIGH_END> |  |  |
| 5 | 保存配置 | 选择 保存 。 | 变式定价已创建。 |  |

### 创建产品主数据 - 销售数据/销售税数据

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

在此流程步骤中，为物料主数据创建销售数据视图。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建物料 (MM01) 。 | 应用随即打开。 |  |
| 3 | 输入物料基本数据 | 在 创建物料（初始屏幕） 中，输入以下内容：材料 ： <CBPTS001>行业部门 ： M备注 如果隐藏行业部门输入字段，则不输入 必填。当行业部门未提供进入时， 字段在深色中用 填充。物料类型 ： KMAT - 可配置物料 | 因此， 选择视图 屏幕。 |  |
| 4 | 选择视图 | 在 选择视图 屏幕上，选择 销售：销售组织数据 1 ， 销售：销售组织 数据 2 ，以及 销售：一般/工厂数据 ，然后选择 继续 。 | 因此， 组织级别 屏幕。 |  |
| 5 | 输入组织级别数据 | 在 组织级别 屏幕的 组织级别 部分，进行以下操作 条目并选择 继续 ：工厂 ：例如， <1010> 。销售组织 ：例如， <1010 代表工厂 1010> 。分销渠道 ：例如， <10> 。 | 因此， 创建物料（可配置物料） 屏幕。您会在屏幕底部收到以下系统消息： 物料已存在并将被扩展 。 |  |
| 6 | 输入销售数据 | 在 创建物料 CBPTS001（可配置物料） 屏幕的 销售：销售组织 1 标签，输入相应的值 税收分类 。通常，这是值 1 ，表示完全应税。按下 输入 。 | 因此， 销售：销售组织 2 标签。输入的值指示物料（通常）完全 应税。 |  |
| 7 | 输入销售数据 | 在 销售：销售组织 2 选项卡（ 分组条件 部分中，输入以下内容并 按 输入 ：项目类别组 ： <0003> | 因此， 销售：一般/工厂 标签。 |  |
| 8 | 输入销售数据 | 在 销售：一般/工厂 选项卡（ 常规数据 部分中，输入以下内容并 按 输入 ：可用性检查 ：例如， <NC> 。 | 因此， 到达最后一个数据视图 屏幕显示消息： 您即将退出。是否要保存 此物料的数据首先吗？ 。 |  |
| 9 | 保存数据 | 选择 是 基于 到达最后一个数据视图 屏幕。 | 因此， 主数据 - 产品 屏幕。您的数据已保存。 |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-product-master-for-consumption-based-billing]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-325]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-dados-mestre-do-produto-para-faturamento]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-maestro-de-productos-para-factura]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 12,807 chars in the whole document
