---
id: 08-sales-order-management/mds-5ng-477
title: 主数据脚本 - 创建位置替代和排除 - MDS (5NG) (5NG_S4CLD2608_Master_Data_ZH_XX)
description: Chinese machine-translated SAP S/4HANA Cloud master data script (5NG) for creating plant and storage location substitutions and exclusions in Fiori apps.
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NG_S4CLD2608_Master_Data_ZH_XX]
keywords: ["Product, Plant and Storage Location Substitution", plant substitution, plant exclusion, storage location substitution, storage location exclusion, substitution reasons, substitution groups, substitution controls, order fulfillment manager role, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-477
topic: 08-sales-order-management/product-and-location-substitution
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 主数据脚本 - 创建位置替代和排除 - MDS (5NG) (5NG_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建位置替代和排除 - MDS (5NG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897776)

[2 前提条件 4](#_Toc233897777)

[2.1 系统访问 4](#_Toc233897778)

[2.2 角色 4](#_Toc233897779)

[2.3 所需组织单位 4](#_Toc233897780)

[2.4 必需主数据 5](#_Toc233897781)

[2.5 工厂替代的初步步骤 5](#_Toc233897782)

[2.5.1 创建工厂替代原因（可选） 5](#_Toc233897783)

[2.5.2 为工厂替代创建组（可选） 6](#_Toc233897784)

[2.5.3 创建工厂替代控制（可选） 8](#_Toc233897785)

[2.6 存储地点替代的初步步骤 9](#_Toc233897786)

[2.6.1 创建存储地点替代原因（可选） 9](#_Toc233897787)

[2.6.2 为存储地点替代创建组（可选） 11](#_Toc233897788)

[2.6.3 创建存储地点替代控制（可选） 12](#_Toc233897789)

[3 概览表 14](#_Toc233897790)

[4 测试过程 15](#_Toc233897791)

[4.1 工厂替代 15](#_Toc233897792)

[4.1.1 创建工厂替代 15](#_Toc233897793)

[4.1.2 创建工厂排除 16](#_Toc233897794)

[4.2 存储地点替代 18](#_Toc233897795)

[4.2.1 创建存储地点替代 18](#_Toc233897796)

[4.2.2 创建存储地点排除 20](#_Toc233897797)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您将找到如何为您的 创建位置替代和排除主数据 SAP S/4HANA Cloud Public 版本 系统。

替代和排除支持位置类型工厂和存储地点。

工厂替代是一种用于将一个工厂替换为另一个工厂的技术。出于各种原因，可以创建工厂替代。 例如：

- 源工厂正在维护中
- 源工厂在控制区域中
- 产品库存在源工厂中不可用

工厂排除允许客户排除工厂作为替代。例如，可以为工厂创建工厂排除 临时关闭。

存储地点替代是一种技术，用于将一个存储地点替换为同一工厂内的另一个存储地点。A 出于各种原因，可以创建存储地点替代。例如：

- 源存储地点不可用
- 产品库存 在工厂 的源存储地点 中不可用

存储地点排除允许客户排除货源位置作为替代位置。

## 前提条件

本部分汇总了执行系统、用户、主数据、组织数据、其他测试数据和业务条件方面测试的所有前提条件。

### 系统访问

| 系统 | 明细 |
| --- | --- |
| 系统 | 可通过 SAP Fiori 快速启动板访问。系统管理员为您提供用于访问分配给您的角色的各种应用的 URL。 |

### 角色

| 名称（角色模板） | ID（角色模板） | 名称（快速启动板空间） | 标识（快速启动板空间） | 登录 |
| --- | --- | --- | --- | --- |
| 订单履行经理 | SAP_BR_ORDER_FULFILLMNT_MNGR | 订单履行管理 | SAP_BR_ORDER_FULFILLMNT_MNGR |  |

### 所需组织单位

组织结构反映贵公司的结构。

工厂替代品可以取决于公司的组织单位（销售组织和分销渠道）。它也可以独立于组织单位。

存储地点替代取决于公司的组织单位（工厂）。始终与组织单位相关。

下表提供了相关组织单位的概览。

| 数据段 | 取决于 | 字段示例 | 备注 | 要使用的组织单位 |
| --- | --- | --- | --- | --- |
| 工厂替代和工厂排除 | 销售组织 |  | 销售组织在 PlantSubstitution/Exclusion 中不是必需的。在没有销售组织限制的情况下可以进行工厂替代/排除。 | 销售组织：____________ |
| 工厂替代和工厂排除 | 分销渠道 |  | 分销渠道在工厂替代/排除中不是必填项。工厂替代/排除可以在没有分销渠道限制的情况下发生。 | 分销渠道：____________ |
| 存储地点替代和存储地点排除 | 工厂 |  | 工厂在存储地点替代/排除中为必填项。无法在没有工厂的情况下进行存储地点替代/排除。 | 工厂：1010 |

### 必需主数据

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 不适用 | 不适用 | 不适用 | 不适用 |

### 工厂替代的初步步骤

#### 创建工厂替代原因（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建工厂替代/排除原因的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代原因 - 位置 (F5313) 。 | 因此， 管理替代原因 - 位置 屏幕是 显示。 |  |
| 3 | 选择创建 | 在 管理替代原因 - 位置 屏幕， 选择 创建 。 | 因此， 管理替代原因 - 位置创建 屏幕 显示 。 |  |
| 4 | 输入原因 | 在 中 抬头 部分中，输入以下内容。位置类型 ： <工厂>原因 ： <输入新的工厂原因代码 替代，例如 NEW_PLANT> |  |  |
| 5 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建原因 。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 原因描述创建 屏幕。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分中，输入以下内容：语言代码 ： <输入适用于原因的语言，例如 EN 英语>原因描述 ： <输入描述原因的文本，例如，新工厂可用> |  |  |
| 8 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建描述 。 |  |

#### 为工厂替代创建组（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了为工厂替代/排除创建组的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代组 - 位置 (F5311) 。 | 因此， 管理替代组 - 位置 屏幕。 |  |
| 3 | 选择创建 | 在 管理替代组 - 位置 屏幕， 选择 创建 。 | 因此， 管理替代组 - 位置创建 屏幕 显示 。 |  |
| 4 | 输入组 | 在 中 抬头 部分中，输入以下内容：位置类型 ： <工厂>分组 ： <输入新的替代组，例如 SOUTH_REGION> |  |  |
| 5 | 创建数据 | 选择 创建 。 | 显示系统消息 组已创建 。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 组描述创建 屏幕。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分中，输入以下内容：语言代码 ： <输入适用于组的语言，例如 EN 英语>组描述 ： <输入描述组的文本，例如，南部区域可用的工厂> |  |  |
| 8 | 创建数据 | 选择 创建 。 | 显示系统消息 组描述已创建 。 |  |
| 9 | 选择返回 | 在 中 标题 部分，选择 < （返回）。 | 因此， 管理替代组 - 位置 屏幕是 显示。 |  |
| 10 | 激活组数据 | 选择 生效 。 | 系统消息显示 状态已更改 。 |  |

#### 创建工厂替代控制（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了为工厂替代/排除控制创建控制的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代控制 - 位置 (F5312) 。 | 因此， 管理替代控制 - 位置 屏幕。 |  |
| 3 | 选择创建 | 在 管理替代控制 - 地点 屏幕上，选择 创建 。 | 因此， 管理替代控制 - 位置创建 屏幕 显示 。 |  |
| 4 | 输入控制 | 在 中 抬头 部分中，输入以下内容。位置类型 ： <工厂>控制 ： <输入替代的新控制，例如，地区> |  |  |
| 5 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建控制 。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 控制描述创建 屏幕。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分中，输入以下内容：语言代码 ： <输入适用于 控制，例如，EN 英语>控制描述 ： <输入描述控件的文本，例如，区域控件> |  |  |
| 8 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建控制描述 。 |  |
| 9 | 选择返回 | 在 中 标题 部分，选择 < （返回）。 | 因此， 管理替代控制 - 位置 屏幕。 |  |
| 10 | 分配组 | 在 中 已分配组 部分，选择 指定 。 | 因此， 将组分配到控制 对话框。 |  |
| 11 | 选择组 | 在 中 将组分配到控制 对话框，搜索并选择 分组 。例如，选择 分组 <SOUTH_REGION>选择 指定 。 | 显示系统消息 组已分配。 |  |

### 存储地点替代的初步步骤

#### 创建存储地点替代原因（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建存储地点替代/排除原因的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代原因 - 位置 (F5313) 。 | 因此， 管理替代原因 - 位置 屏幕。 |  |
| 3 | 选择创建 | 在 管理替代原因 - 位置 屏幕， 选择 创建 。 | 因此， 原因 屏幕。 |  |
| 4 | 输入原因 | 在 中 抬头 部分中，输入以下内容。位置类型 ： <存储 位置>原因 ： <输入存储地点替代的新原因代码，例如 NEW_SLOC> |  |  |
| 5 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建原因。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 原因描述 屏幕。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分中，输入以下内容：语言代码 ： <输入适用于原因的语言，例如 EN 英语>原因描述 ： <输入描述原因的文本，例如，新存储地点可用> |  |  |
| 8 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建描述 。 |  |

#### 为存储地点替代创建组（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了为存储地点替代/排除创建组的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代组 - 位置 (F5311) 。 | 因此， 管理替代组 - 位置 屏幕。 |  |
| 3 | 选择创建 | 在 管理替代组 - 位置 屏幕上，选择 创建 。 | 因此， 管理替代组 - 位置创建 屏幕 显示 。 |  |
| 4 | 输入组 | 在 中 抬头 部分中，输入以下内容：位置类型 ： <存储 位置>分组 ： <输入新替代组，例如 COLD_STORAGE> |  |  |
| 5 | 创建数据 | 选择 创建 。 | 显示系统消息 组已创建 。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 组描述创建 屏幕。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分中，输入以下内容：语言代码 ： <输入适用于组的语言，例如 EN 英语>组描述 ： <输入描述组的文本，例如，冷存储项目的存储地点> |  |  |
| 8 | 创建数据 | 选择 创建 。 | 显示系统消息 组描述已创建 。 |  |
| 9 | 选择返回 | 在 中 标题 部分，选择 < （返回） | 因此， 管理替代组 - 地点 屏幕是 显示。 |  |
| 10 | 激活组数据 | 选择 生效 。 | 系统消息显示 状态已更改 。 |  |

#### 创建存储地点替代控制（可选）

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了为存储地点替代/排除控制创建控制的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代控制 - 位置 (F5312) 。 | 因此， 管理替代控制 - 地点 屏幕。 |  |
| 3 | 选择创建 | 在 管理替代控制 - 地点 屏幕， 选择 创建 。 | 因此， 管理替代控制 - 位置创建 屏幕。 |  |
| 4 | 输入控制 | 在 中 抬头 部分中，输入以下内容。位置类型 ： <存储 位置>控制 ： <输入替代的新控制，例如 STORAGE_TYPE> |  |  |
| 5 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建控制 。 |  |
| 6 | 选择创建 | 在 中 描述 部分，选择 创建 。 | 因此， 控制描述创建 屏幕。 |  |
| 7 | 输入描述数据 | 在 中 描述 部分中，输入以下内容：语言代码 ： <输入适用于 控制，例如，EN 英语>控制描述 ： <输入描述控制的文本，例如，仓储类型的控制> |  |  |
| 8 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建控制描述 。 |  |
| 9 | 选择返回 | 在 中 标题 部分，选择 <（后退） 。 | 因此， 管理替代控制 - 位置 屏幕。 |  |
| 10 | 分配组 | 在 中 已分配组 部分，选择 指定 。 | 因此， 将组分配到控制 对话框。 |  |
| 11 | 选择组 | 在 中 将组分配到控制 对话框，搜索并选择 分组 。例如，选择 分组 <COLD_STORAGE>选择 指定 。 | 显示系统消息 组已分配。 |  |

## 概览表

此范围项目由下表中提供的流程细分组成。

|  |
| --- |
| 备注 如果系统管理员已在 SAP Fiori 快速启动板上启用空间和页面，则主页将仅包含用于执行业务角色典型任务的必要应用。您可以使用搜索栏 () 查找主页上不包含的所有其他（可搜索）应用[2434549](https://me.sap.com/notes/2434549)）。如果要个性化设置主页并包括隐藏应用，请导航到您的用户参数文件并选择 应用查找器 。 |

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建工厂替代](#unique_14) [第 ] 页 15 | 订单履行经理 | 管理替代 - 位置 (F5314) | 已创建工厂替代记录。 |
| [创建工厂排除](#unique_15) [第 ] 页 16 | 订单履行经理 | 管理排除 - 位置 (F5315) | 已创建工厂排除记录。 |
| [创建存储地点替代](#unique_16) [第 ] 页 18 | 订单履行经理 | 管理替代 - 位置 (F5314) | 已创建存储地点替代记录。 |
| [创建存储地点排除](#unique_17) [第 ] 页 20 | 订单履行经理 | 管理排除 - 位置 (F5315) | 已创建存储地点排除记录。 |

## 测试过程

本部分介绍属于此范围项目的每个流程步骤的测试过程。

### 工厂替代

#### 创建工厂替代

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建工厂替代的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代 - 位置 (F5314) 。 | 因此， 管理替代 - 位置 屏幕。 |  |
| 3 | 选择创建 | 在 中 管理替代 - 位置 视图，位于 工厂 部分，选择 创建 。 | 因此， 管理替代 - 位置 显示创建屏幕的灵活列布局。 |  |
| 4 | 输入抬头数据 | 在 中 抬头 部分中，输入以下内容：工厂 ： <输入需要替代项的工厂>替代工厂 ： <输入 替代>销售组织 ： <销售组织编号>分销渠道 ： <分销渠道编号>要创建替代，必须指定工厂和替代工厂数据。 |  |  |
| 5 | 输入基本信息数据 | 在 中 基本信息 部分中，输入以下内容：原因 ： <输入创建替代的原因。例如，NEW_PLANT>分组 ： <输入替代组。例如，SOUTH_REGION>有效自 ： <输入有效期的开始日期和时间>有效期至 ： <输入有效期的结束日期和时间>时区 ： <输入有效期适用的时区>以上条目是可选的。 |  |  |
| 6 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建替代 。 |  |
| 7 | 激活工厂替代数据 | 选择 生效 。 | 显示系统消息 状态已更改 。 |  |
| 8 | 显示图形 | 选择 查看图形 | 因此， 显示工厂网络图形 屏幕。 |  |

#### 创建工厂排除

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建工厂排除的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理排除 - 位置 (F5315) 。 | 因此， 管理排除 - 位置 屏幕。 |  |
| 3 | 选择创建 | 在 中 管理排除 - 位置（工厂） 视图，选择 创建 。 | 因此， 工厂排除 屏幕。 |  |
| 4 | 输入抬头数据 | 在 中 抬头 部分中，输入以下内容：工厂 ： <输入需要从替代中排除的工厂>销售组织 ： <销售组织编号>分销渠道 ： <分销渠道编号>工厂是创建排除的必填项。 |  |  |
| 5 | 输入基本信息数据 | 在 中 基本信息 部分中，输入以下内容：原因 ： <输入排除工厂的原因>分组 ： <输入适用于工厂排除的组>有效自 ： <输入有效期的开始日期和时间>有效期至 ： <输入有效期的结束日期和时间>时区 ： <输入有效期适用的时区>以上条目是可选的。 |  |  |
| 6 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建排除 。 |  |
| 7 | 激活工厂排除数据 | 选择 生效 。 | 显示系统消息 状态已更改 。 |  |

### 存储地点替代

#### 创建存储地点替代

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建存储地点替代的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理替代 - 位置 (F5314) 。 | 因此， 管理替代 - 位置 屏幕。 |  |
| 3 | 选择存储地点 | 在 管理替代 - 位置 屏幕上，选择 存储地点 标签。 | 因此， 管理替代 - 位置（存储地点） 屏幕。 |  |
| 4 | 选择创建 | 在 存储地点 标签上，选择 创建 。 | 因此， 管理替代 - 位置 显示创建屏幕的灵活列布局。 |  |
| 5 | 输入抬头数据 | 在 中 抬头 部分中，输入以下内容：工厂 ： <工厂编号>存储地点 ： <输入存储地点，需要 替代>替代存储地点 ： <输入替代人>工厂和替代存储地点数据是创建子任务的必填项，而存储地点是可选的。工厂为 选择存储地点时缺省选中。 |  |  |
| 6 | 输入基本信息数据 | 在 中 基本信息 部分中，输入以下内容：原因 ： <输入创建替代的原因。例如，NEW_SLOC>分组 ： <输入替代组。例如，COLD_STORAGE>有效自 ： <输入有效期的开始日期和时间>有效期至 ： <输入有效期的结束日期和时间>时区 ： <输入有效期适用的时区>以上条目是可选的。 |  |  |
| 7 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建替代 。 |  |
| 8 | 激活存储地点替代数据 | 选择 生效 。 | 显示系统消息 状态已更改 。 |  |
| 9 | 显示图形 | 选择 查看图形 。 | 因此， 显示存储地点网络图形 屏幕。 |  |

#### 创建存储地点排除

测试管理

客户项目：填写项目特定部件。

|  |  |  |  |
| --- | --- | --- | --- |
| 测试用例标识 | <X.XX> | 测试日期： |  |
| 测试人员姓名： |  | 持续时间： |  |
| 业务角色： |  | 职责： | <说明服务提供商、客户或共同服务提供商和客户> |

目的

以下过程提供了创建存储地点排除的说明。可用的应用取决于您分配的角色。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录到 SAP Fiori 快速启动板 订单履行经理 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问 SAP Fiori 应用 | 打开 管理排除 - 位置 (F5315) 。 | 因此， 管理排除 - 位置 屏幕。 |  |
| 3 | 选择存储地点 | 在 中 管理排除 - 位置 视图，选择 存储地点 。 | 因此， 管理排除 - 位置（存储地点） 屏幕。 |  |
| 4 | 选择创建 | 在 中 管理排除 - 位置（存储地点） 视图，选择 创建 。 | 因此， 管理排除 - 位置创建 屏幕。 |  |
| 5 | 输入抬头数据 | 在 中 抬头 部分中，输入以下内容：工厂 ： <工厂编号>存储地点 ： <输入存储 需要从替代中排除的位置>工厂和存储地点都是排除的必填项。 |  |  |
| 6 | 输入基本信息数据 | 在 中 基本信息 部分中，输入以下内容：原因 ： <输入排除存储地点的原因>分组 ： <输入适用于存储地点排除的组>有效自 ： <输入有效期的开始日期和时间>有效期至 ： <输入有效期的结束日期和时间>时区 ： <输入有效期适用的时区>以上条目是可选的。 |  |  |
| 7 | 创建数据 | 选择 创建 。 | 显示系统消息 已创建排除 。 |  |
| 8 | 激活存储地点排除数据 | 选择 生效 。 | 显示系统消息 状态已更改 。 |  |

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
- related-to :: [[08-sales-order-management/lokationsersetzung-und-ausschluss-anlegen-sds-5ng-472]]
- related-to :: [[08-sales-order-management/master-data-script-create-location-substitution-and-exclusion-mds-5ng]]
- related-to :: [[08-sales-order-management/mds-5ng-475]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-e-exclusao-de-local-mds-5ng]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 14,962 chars in the whole document
