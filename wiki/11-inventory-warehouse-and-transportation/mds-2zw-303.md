---
id: 11-inventory-warehouse-and-transportation/mds-2zw-303
title: 创建批次管理主数据 - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_ZH_XX)
description: "Chinese (machine-translated) SAP S/4HANA Cloud Public 2608 master data script 2ZW: batch management master data (characteristics, classes, sort order, search and derivation strategies)."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/batch-management-master-data]
aliases: [2ZW_S4CLD2608_Master_Data_ZH_XX]
keywords: [Batch Management Master Data, batch management, batch characteristics, batch classes, sort order, batch search strategy, batch derivation, batch determination, business roles, production batch search]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-303
topic: 11-inventory-warehouse-and-transportation/batch-management-master-data
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 创建批次管理主数据 - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Batch Management Master Data** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建批次管理主数据 - MDS (2ZW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 2](#_Toc233897501)

[2 前提条件 3](#_Toc233897502)

[2.1 系统访问 3](#_Toc233897503)

[2.2 角色 3](#_Toc233897504)

[3 概览表 4](#_Toc233897505)

[4 测试过程 5](#_Toc233897506)

[4.1 创建特征 5](#_Toc233897507)

[4.2 创建类 6](#_Toc233897508)

[4.3 创建排序顺序 8](#_Toc233897509)

[4.4 为库存管理创建批次搜索策略记录 9](#_Toc233897510)

[4.5 创建生产的批次搜索策略记录 11](#_Toc233897511)

[4.6 创建销售和分销的批次搜索策略记录 13](#_Toc233897512)

[4.7 创建发送方物料的派生策略 15](#_Toc233897513)

[4.8 创建接收方物料的派生策略 17](#_Toc233897514)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

批次管理主数据包括批次规范、排序顺序（排序规则）和批次中的批次搜索策略记录 determination。

批次规格描述批次的技术性质、物理属性和化学性质。存储批次规格，例如批次 状态或活性成分效力，作为分类系统中的特征。

您可以使用分类系统将物料规范分配到批次的物料。这些物料规范 被分配给与物料批次相同的类。因此，您可以使用相应的 公差范围。例如，这些目标值用于质量检验或收货交易期间（如果 需要立即对批次进行分类。这些值还用于可用性检查。

在物料中，存储所有特征的目标范围。由于批次属于与物料相同的类，因此批次 自动接收物料的特性。对于每个单独的批次，输入准确的实际值。

不同流程（库存管理、生产、销售和分销）中的批次确定不同 criteria。维护条件需要排序顺序和批次搜索策略记录。

通过排序顺序，您可以了解批次确定搜索结果中的批次是按升序还是降序排序 个特征值。

在批次确定的批次搜索策略中，您可以定义系统查找批次所依据的值， 包括流程（例如，移动类型、订单类型或工厂）和物料编号的属性。仅当条件记录为 这些批次可以根据排序顺序和批次规范进一步排序和确定。

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
| 物料清单工程师 | SAP_BR_BOM_ENGINEER | 物料清单 | SAP_BR_BOM_ENGINEER |  |
| 主数据专家 - 批次数据 | SAP_BR_BATCH_MASTER_SPCLST | 主数据 - 批次 | SAP_BR_BATCH_MASTER_SPCLST |  |

## 概览表

此范围项目由下表中列出的多个流程步骤组成：

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 流程步骤 | 业务角色 | 事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建特征](#unique_6) [第 ] 页 5 | 物料清单工程师 | 管理特征 (CT04) | 已创建特征。 |
| [创建类](#unique_7) [第 ] 页 6 | 物料清单工程师 | 管理类 (CL02) | 类已创建。 |
| [创建排序顺序](#unique_8) [第 ] 页 8 | 主数据专家 - 批次数据 | 创建排序顺序 (CU70) | 已创建排序顺序。 |
| [为库存管理创建批次搜索策略记录](#unique_9) [第 ] 页 9 | 主数据专家 - 批次数据 | 管理搜索策略 - 库存管理 (MBC2) | 已创建批次搜索策略记录。 |
| [创建生产的批次搜索策略记录](#unique_10) [第 ] 页 11 | 主数据专家 - 批次数据 | 管理搜索策略 - 生产 (COB2) | 已创建批次搜索策略记录。 |
| [创建销售和分销的批次搜索策略记录](#unique_11) [第 ] 页 13 | 主数据专家 - 批次数据 | 管理搜索策略 - 销售和分销 (VCH2) | 已创建批次搜索策略记录。 |
| [创建发送方物料的派生策略](#unique_12) [第 ] 页 15 | 主数据专家 - 批次数据 | 管理派生策略 - 发送方 (DVS2) | 已创建发送方物料的派生策略。 |
| [创建接收方物料的派生策略](#unique_13) [第 ] 页 17 | 主数据专家 - 批次数据 | 管理派生策略 - 接收方 (DVR2) | 已创建接收方物料的派生策略。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 创建特征

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建特征的说明。

过程

当用户访问向您提供 时，请使用以下过程 管理特征 (CT04) 应用。

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 物料清单工程师 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理特征 (CT04) 。 | 因此， 特征 屏幕。备注 创建、更改和显示模式的公用屏幕。 |  |
| 3 | 输入特征名称 | 输入以下内容并选择 创建 。特征 ： <您的特征名称> | 因此， 基本数据 屏幕选项显示。备注 中的值 有效自 字段是 自动填充。 |  |
| 4 | 输入基本数据 | 输入以下内容并选择 保存 ：基本数据 部分：描述 ： <输入您的描述>状态 ： 已发布 （默认）格式 部分：数据类型 ： <选择格式>值分配 部分：选择 单值 单选按钮。 | 备注 所选格式的其他字段在 格式 部分。请相应地维护。 |  |
| 5 | 输入检查值 | 在 价值 选项卡（ 允许 价值 部分中，为此输入允许的值 特征。 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 已创建特征。 |  |

### 创建类

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建类的说明。

前提条件

您必须完成上一部分，[创建特征](#unique_6) [第 ] 页 5，然后再继续 部分。

过程

当用户访问向您提供 时，请遵循以下过程 管理类 (CL02) 应用。

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 物料清单工程师 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理类 (CL02) 。 | 因此， 类别 屏幕。备注 它是创建、更改和显示模式的通用屏幕。 |  |
| 3 | 输入类名称 | 输入以下内容并选择 创建 ：类别 ： <类 名称>类类型 ： 023 | 因此， 创建类 屏幕。备注 因此， 有效自 字段自动填充 具有值。 |  |
| 4 | 输入基本数据 | 在 基本数据 标签上，执行以下操作 条目：在 中 基本数据 部分：描述 ： <类 描述>状态 ： 已发布 |  |  |
| 5 | 输入特征标签 | 选择 特征 标签并进行以下输入 将您创建的特征分配给此类，然后按 输入 ：在 中 特征 列：特征 ： <特征 名称> | 因此， 描述 以及 数据 类型 自动填写特征字段 具有值。 |  |

### 创建排序顺序

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建排序顺序的说明。

前提条件

您必须完成该部分 创建特征 在你之前 继续本节。

过程

当用户访问向您提供 时，请使用以下过程 创建排序顺序 (CU70) 应用。

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 批次数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 创建排序顺序 (CU70) 。 | 因此， 创建排序顺序 屏幕 显示 。 |  |
| 3 | 输入排序顺序名称 | 输入以下内容并选择 。 创建 图标：排序顺序 ： <排序 序列名称> | 因此， 创建排序顺序：基本数据 屏幕显示。 |  |
| 4 | 输入基本数据 | 维护排序顺序名称旁的描述，并 选择 特征 。描述 ： <排序 序列描述> | 因此， 创建排序顺序：特性 屏幕显示。 |  |
| 5 | 输入排序顺序详细信息 | 选择 新条目 维护 以下列，并选择 保存 ：特征 ： <特征名称>升序 ： XDscending ： ‘ ’ | 创建排序顺序。备注 您可以指定升序或降序。 |  |

### 为库存管理创建批次搜索策略记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建搜索策略的说明， 批确定。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 批次数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 随即显示 SAP Fiori 快速启动板。 | 打开 管理搜索策略 - 库存管理 (MBC2) 。 | 因此， 更改批次搜索策略：初始 屏幕 随即显示。 |  |
| 3 | 输入策略类型 | 输入以下内容并选择 。 更改 ：策略类型 ： <策略类型，例如 YB11>备注 可通过自助服务配置策略类型 配置 UI。 | 弹出窗口 组合键 显示 。 |  |
| 4 | 选择 组合键 | 在弹出窗口中 组合键 ，选择一个 从下列选项中选择 选择 ：移动类型/工厂/物料工厂/物料移动类型/物料移动类型/工厂移动类型 | 因此， 更改业务伙伴：批次编号 (YB11)： 选择 随即显示。 | 因此， 关键字组合 取决于 策略类型 你选择. 如果所选策略中只有一个键值组合，则不会显示弹出窗口。 |
| 5 | 输入您的选择 | 要指定记录，请输入以下属性： 根据所选键值组合显示，然后选择 执行 ：货物移动类型 ： <货物移动类型>工厂 ： <工厂>材料 ： <物料 编号> | 因此， 更改 BP: 批号 (YB11) : 快速 输入 随即显示。 |  |
| 6 | 详细输入策略记录 | 要创建新记录，应输入以下内容： 并选择 保存 ：材料 ： <物料 编号>如果需要，您还可以指定以下属性： 每条记录：批次拆分数允许更改对话批次确定显示计量单位数量建议允许过量交货选择类型 |  |  |
| 7 | 维护选择条件 可选 | 进一步维护批次的选择条件 记录中物料的特性值，选择记录 并选择 选择条件 。 | 因此， 更改业务伙伴：分类 显示 。 |  |
| 8 | 维护排序顺序（可选） | 要维护特定记录的排序顺序，请选择记录 并选择 排序 。 | 因此， 更改 BP: 批号 (YB11) : 排序 规则 随即显示。 |  |

### 创建生产的批次搜索策略记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建搜索策略的说明， 批确定。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 批次数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理搜索策略 - 生产 (COB2) 。 | 因此， 更改批次搜索策略：初始 屏幕 随即显示。 |  |
| 3 | 输入策略类型 | 输入以下内容并选择更改：策略类型 ： <策略类型，例如 YB11>备注 可通过自助服务配置策略类型 配置 UI。 | 因此， 更改业务伙伴：批次编号 (YB11)： 选择 随即显示。备注 键值组合未显示，因为只有一个键值 在生产中为 YB11 配置的组合 |  |
| 4 | 输入您的选择 | 要指定记录，请输入以下属性： 根据所选键值组合显示，然后选择 执行 ：订单类型 ： <订单 类型>工厂 ： <工厂>材料 ： <物料 编号> | 因此， 更改 BP: 批号 (YB11) : 快速 输入 随即显示。 | 因此， 关键字组合 取决于 策略类型 你选择. 如果所选策略中只有一个键值组合，则不会显示弹出窗口。 |
| 5 | 详细输入策略记录 | 要创建新记录，应输入以下内容： 并选择 保存 ：材料 ： <物料 编号>如果需要，您还可以指定以下属性： 每条记录：批次拆分数允许更改对话批次确定显示计量单位数量建议允许过量交货选择类型 |  |  |
| 6 | 维护选择条件 可选 | 进一步维护批次的选择条件 记录中物料的特性值，选择记录 并选择 选择条件 。 | 因此， 更改业务伙伴：分类 显示 。 |  |
| 7 | 维护排序顺序（可选） | 要维护特定记录的排序顺序，请选择记录 并选择 排序 。 | 因此， 更改 BP: 批号 (YB11) : 排序 规则 随即显示。 |  |

### 创建销售和分销的批次搜索策略记录

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建搜索策略的说明， 批确定。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 批次数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理搜索策略 - 销售和分销 (VCH2) 。 | 更改批次搜索策略：初始屏幕 显示 。 |  |
| 3 | 输入策略类型 | 输入以下内容并选择更改：策略类型 ： <策略类型，例如 YB11>备注 可通过自助服务配置策略类型 配置 UI。 | 弹出窗口 组合键 显示 。 |  |
| 4 | 选择关键字组合 | 在弹出窗口中 组合键 ，选择一个 从下列选项中选择 选择 ：客户/物料材料 | 因此， 更改业务伙伴：批次编号 (YB11)： 选择 随即显示。 | 因此， 关键字组合 取决于 策略类型 你选择. 如果所选策略中只有一个键值组合，则不会显示弹出窗口。 |
| 5 | 输入您的选择 | 要指定记录，请输入以下属性： 根据所选键值组合显示，然后选择 执行 ：客户 ： <客户 标识>材料 ： <物料 编号> | 因此， 更改 BP: 批号 (YB11) : 快速 输入 随即显示。 |  |
| 6 | 详细输入策略记录 | 要创建新记录，应输入以下内容： 并选择 保存 ：材料 ： <物料 编号>如果需要，您还可以指定以下属性： 每条记录：批次拆分数允许更改对话批次确定显示计量单位数量建议允许过量交货选择类型 |  |  |
| 7 | 维护选择条件 可选 | 进一步维护批次的选择条件 记录中物料的特性值，选择记录 并选择 选择条件 。 | 因此， 更改业务伙伴：分类 显示 。 |  |
| 8 | 维护排序顺序（可选） | 要维护特定记录的排序顺序，请选择记录 并选择 排序 。 | 因此， 更改 BP: 批号 (YB11) : 排序 规则 随即显示。 |  |

### 创建发送方物料的派生策略

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建策略记录的说明，这些策略记录用于在批次派生期间确定发送方物料的属性。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 批次数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理派生策略 - 发送方 (DVS2) 。 | 因此， 派生 - 更改搜索策略：初始 屏幕。 |  |
| 3 | 输入策略类型 | 输入以下内容并选择 更改 ：策略类型 ： <策略类型> | 弹出窗口 组合键 随即显示。 | 在该步骤之前，您需要根据需要完成以下配置步骤：批次派生的编号范围确定批次派生中发送批次 |
| 4 | 选择关键字组合 | 在弹出窗口中 组合键 ，从以下选项中选择一个，然后选择 选择 ：<关键字组合 1><关键字组合 2>… | 因此， 更改 <策略类型>：选择 屏幕。 | 因此， 关键字组合 取决于 策略类型 选择。 |
| 5 | 输入您的选择 | 要指定记录，请输入基于所选 组合键 ，以及 选择 执行 ：发送方物料 ： <发送方物料标识><关键字段> ： <键值>… | 因此， 更改 <策略类型>：快速输入 屏幕。 |  |
| 6 | 输入您的策略记录 | 要创建新记录，应输入以下条目，然后选择 保存 ：发送方物料 ： <发送方物料标识>要进一步维护发送方物料的详细信息，请选择一条记录并选择 。 明细 。 | 因此， 更改 <策略类型>：详细信息 屏幕。 |  |
| 7 | 维护策略记录详细信息 | 在 中 已发送属性（字段/特征） 部分中，输入以下内容并选择 。 保存 ：属性 ： <发送方物料标识>Field ： <缺省选中>特征 ： <缺省情况下未选中> |  |  |

### 创建接收方物料的派生策略

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建策略记录的说明，这些策略记录用于在批次派生期间确定接收方物料的属性。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 批次数据 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理派生策略 - 接收方 (DVR2) 。 | 因此， 派生 - 更改搜索策略：初始 屏幕。 |  |
| 3 | 输入策略类型 | 输入以下内容并选择 更改 ：策略类型 ： <策略类型> | 弹出窗口 组合键 随即显示。 | 在该步骤之前，您需要根据需要完成以下配置步骤：批次派生的编号范围确定批次派生中接收批次 |
| 4 | 选择关键字组合 | 在弹出窗口中 组合键 ，从以下选项中选择一个，然后选择 选择 ：<关键字组合 1><关键字组合 2>… | 因此， 更改 <策略类型>：选择 屏幕。 | 因此， 关键字组合 取决于 策略类型 您 选择。 |
| 5 | 输入您的选择 | 要指定记录，请输入基于所选 组合键 ，以及 选择 执行 ：接收方物料 ： <接收方物料标识><关键字段> ： <键值>… | 因此， 更改 <策略类型>：快速输入 屏幕。 |  |
| 6 | 输入您的策略记录 | 要创建新记录，应输入以下条目，然后选择 保存 ：接收方物料 ： <接收方物料标识>要进一步维护接收方物料的详细信息，请选择一条记录并选择 。 明细 。 | 因此， 更改 <策略类型>：详细信息 屏幕。 |  |
| 7 | 维护策略记录详细信息 | 在 选项卡下 属性 中的 接收的属性（字段/特征） 部分，输入 以下条目，并选择 保存 ：属性 ： <接收方物料标识>Field ： <缺省选中>特征 ： <缺省情况下未选中>要维护每个属性的规则，请选择一个属性并选择标签 规则 然后可以维护 以下规则：控制派生规则发送方字段为空覆盖接收方批次调用清单中的级别接收方未发送如果有多个发送方，则值选择规则比较布尔值多值特征 |  |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-batch-management-master-data-mds-2zw-299]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-301]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-administracao-de-lotes-2z]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-crear-datos-maestros-de-gestion-de-lotes-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 13,294 chars in the whole document
