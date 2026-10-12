---
id: 14-maintenance-service-and-projects/mds-5be-master-data-script-create-configurable-service-products-435
title: "主数据脚本: 创建可配置服务产品 - MDS (5BE) (Master Data Script: Create Configurable Service Products) (5BE_S4CLD2608_Master_Data_ZH_XX)"
description: "Chinese machine-translated SAP S/4HANA Cloud 2608 master data script (5BE): characteristics, classes, configuration profiles, pricing and variants for configurable service products."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/configurable-service-products]
aliases: [5BE_S4CLD2608_Master_Data_ZH_XX]
keywords: [Configurable Service Products and Advanced Variant…, configurable service products, characteristics, classes, configuration profiles, variant pricing, material variants, service contracts, service orders, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_ZH_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-435
topic: 14-maintenance-service-and-projects/configurable-service-products
language: ZH
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 主数据脚本: 创建可配置服务产品 - MDS (5BE) (Master Data Script: Create Configurable Service Products) (5BE_S4CLD2608_Master_Data_ZH_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_ZH_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Service Products and Advanced Variant Configuration** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | 主数据脚本SAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 创建可配置服务产品 - MDS (5BE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目录

[1 目的 3](#_Toc233897647)

[2 前提条件 4](#_Toc233897648)

[2.1 系统访问 4](#_Toc233897649)

[2.2 角色 4](#_Toc233897650)

[2.3 所需组织单位 4](#_Toc233897651)

[2.4 必需和运营主数据 5](#_Toc233897652)

[2.5 预备步骤（必选） 5](#_Toc233897653)

[3 概览表 7](#_Toc233897654)

[4 过程 8](#_Toc233897655)

[4.1 为服务合同创建可配置服务产品 8](#_Toc233897656)

[4.1.1 创建特征 8](#_Toc233897657)

[4.1.2 创建类 11](#_Toc233897658)

[4.1.3 为合同创建可配置服务产品 12](#_Toc233897659)

[4.1.4 创建配置参数文件 15](#_Toc233897660)

[4.1.5 设置价格 16](#_Toc233897661)

[4.2 为服务订单创建可配置服务产品 19](#_Toc233897662)

[4.2.1 创建特征 19](#_Toc233897663)

[4.2.2 创建类 23](#_Toc233897664)

[4.2.3 为服务订单创建可配置服务产品 24](#_Toc233897665)

[4.2.4 创建配置参数文件 27](#_Toc233897666)

[4.2.5 设置价格 28](#_Toc233897667)

[4.3 创建服务产品的物料变式 31](#_Toc233897668)

[4.3.1 设置物料变式的价格 34](#_Toc233897669)

## 目的

注意！这是未审核准确性的机器翻译文档。要发送有关翻译的反馈，您可以在 SAP Signavio Process Navigator 中针对您的国家/地区版本在范围项目页面上创建客户工单。

在本文档中，您可以找到有关如何为服务合同和服务订单创建可配置服务产品以及相关价格的描述。该描述包括与主数据相关的数据段，以便在“常规”系统环境中工作。读取器主要学习哪些数据段和字段通常需要使用输入值填充。本文档不描述与 SAP Best Practices 的 S/4 HANA 内容交付范围无关的字段，尽管这些字段可能显示在 UI 上。

按此处描述创建的可配置服务产品，可用于服务 合同处理和服务订单处理。为了利用可配置的 服务产品，请参阅 使用高级变式配置的服务管理 (6GS) 范围项目或 使用高级变式配置的服务合同管理 (6GU)。

可用于服务合同和服务订单的产品配置功能与范围项目 22T- 使用变式配置设置可配置模型中进一步描述的功能相同。

## 前提条件

### 系统访问

| 系统 | 明细 |
| --- | --- |
| 系统 | 可通过 SAP Fiori 快速启动板访问。系统管理员为您提供用于访问分配给您的角色的各种应用的 URL。 |

### 角色

使用 SAP 提供的以下业务角色模板创建业务角色并分配 提供给你的测试用户。

| 名称 | 标识 |
| --- | --- |
| 产品配置建模器 | SAP_BR_PRODUCT_CONFIG_MODELER |
| 主数据专家 - 产品数据 | SAP_BR_PRODMASTER_SPECIALIST |
| 定价专家 | SAP_BR_PRICING_SPECIALIST |

此外，以下角色与负责以下内容的配置用户相关： 必填 预备步骤 描述如下：

| 名称 | 标识 |
| --- | --- |
| 配置专家 - 业务流程配置 | SAP_BR_BPC_EXPERT |

### 所需组织单位

主数据的一些段取决于公司的组织单位， 常规 （中央）数据不取决于组织单位或公司代码。因此， 下表提供了这些不同数据段及其相关 组织单位：

| 数据段 | 取决于 | 要使用的组织单位 | 备注 |
| --- | --- | --- | --- |
| 创建物料 | 工厂 | 1710（工厂 1 美国） | 对于德国，使用 1010（工厂 1 DE） |
| 创建物料 | 销售组织 | 1710（国内销售组织 - US） | 对于德国，使用 1010（国内销售组织 - DE） |
| 创建物料 | 分销渠道 | 10（直销） | 对于德国，使用 10（直销） |

### 必需和运营主数据

物料主数据记录可能参考其他主数据。下表提供了要在物料主数据记录中使用的可选和必填主数据对象的概览。

|  |
| --- |
| 备注 需要巴西特定字段才能获得正确的税收计算。支票 巴西发票 - JD0 中的 定义 BR 特定字段 主数据 章节（针对物料主数据）。 |

| 主数据对象 | 在数据段中使用 | 必填/可选 | 备注 |
| --- | --- | --- | --- |
| 利润中心 |  | 必填 | 需要将利润中心分配到物料（产品）主数据 用于正确的评估流程。 |

### 预备步骤（必选）

使用

按照下列步骤所述创建可配置服务产品之前，必须首先启用现有物料类型 SERV（服务）以使用分类数据。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 配置专家 - 业务流程配置 。 | 随即显示 SAP Fiori 快速启动板。 |  |
| 2 | 访问应用 | 打开 管理您的解决方案 应用。 | 因此， 管理您的解决方案 显示 APP。 |  |
| 3 | 配置您的解决方案 | 在 管理您的解决方案 屏幕上，选择 配置 您的解决方案 。 | 因此， 配置您的解决方案：实现阶段 屏幕是 显示。 |  |
| 4 | 打开配置的产品项目 | 在搜索过滤器中，输入以下内容：应用范围 ： <数据库和数据 管理子应用程序范围 ： 产品选择 产品 记录（在搜索中） results。 | 因此， 配置您的解决方案 - 产品 屏幕是 显示。 |  |
| 5 | 配置您的解决方案 - 产品 | 在 中 配置步骤 部分，用于 定义 物料类型的属性 ，选择 配置 。 | 因此， 定义物料类型的属性：更改 屏幕是 显示。 |  |
| 6 | 物料类型 SERV 的未清属性 | 双击 SERV – 服务产品 条目。 | 因此， 定义物料类型的属性：更改：详细信息 屏幕 已显示。 |  |
| 7 | 启用分类 | 在 中 用户部门 列表中选择 分类 。注意 在配置中保存更改之前，请确保 中预先存在的选择 用户 部门 清单也是 已选择。 |  |  |
| 8 | 保存数据 | 选择 保存 。 |  |  |

结果

创建 SERV – 服务产品类型的产品时， 分类 标签页。

## 概览表

此主记录由下表中提供的多个段组成。

| 细分 | 业务角色 | 应用/事务 | 预期结果 |
| --- | --- | --- | --- |
| [创建特征](#unique_8) [第 ] 页 8 | SAP_BR_PRODUCT_CONFIG_MODELER | 管理特征 | 已创建服务合同类的特征。 |
| [创建类](#unique_9) [第 ] 页 11 | SAP_BR_PRODUCT_CONFIG_MODELER | 管理类 | 已创建类。 |
| [为合同创建可配置服务产品](#unique_10) [第 ] 页 12 | SAP_BR_PRODMASTER_SPECIALIST | 创建物料 | 创建服务合同的服务产品。 |
| [创建配置参数文件](#unique_11) [第 ] 页 15 | SAP_BR_PRODUCT_CONFIG_MODELER | VC 建模环境 | 配置参数文件已创建。 |
| [设置价格](#unique_12) [第 ] 页 16 | SAP_BR_PRICING_SPECIALIST | 设置物料价格 | 已定义价格。 |
| [创建特征](#unique_13) [第 ] 页 19 | SAP_BR_PRODUCT_CONFIG_MODELER | 管理特征 | 已创建服务合同类的特征。 |
| [创建类](#unique_14) [第 ] 页 23 | SAP_BR_PRODUCT_CONFIG_MODELER | 管理类 | 已创建类。 |
| [为服务订单创建可配置服务产品](#unique_15) [第 ] 页 24 | SAP_BR_PRODMASTER_SPECIALIST | 创建物料 | 已创建服务订单的服务产品。 |
| [创建配置参数文件](#unique_16) [第 ] 页 27 | SAP_BR_PRODUCT_CONFIG_MODELER | VC 建模环境 | 配置参数文件已创建。 |
| [设置价格](#unique_17) [第 ] 页 28 | SAP_BR_PRICING_SPECIALIST | 设置物料价格 | 已定义服务产品的价格。 |
| [创建服务产品的物料变式](#unique_18) [第 ] 页 31 | SAP_BR_PRODMASTER_SPECIALIST | 创建物料 | 为可配置服务产品创建物料变式。 |
| [设置物料变式的价格](#unique_19) [第 ] 页 34 | SAP_BR_PRICING_SPECIALIST | 设置物料价格 | 已定义物料变式的价格。 |

## 过程

本节介绍属于此主数据的每个段或流程步骤的过程。 记录。

### 为服务合同创建可配置服务产品

#### 创建特征

目的

在此活动中，创建可在可配置服务产品中进行选择的特征，并且可以为其维护单个变式价格。

过程

特征 VARKOND（变式条件代码）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理特征 。在 特征 屏幕中，维护 特征 ： VARKOND然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入基本数据 | 在 中 基本数据 区域中，维护以下数据：描述 ： 变式条件键值状态 ： 已发布数据类型 ： 字符格式字符数 ： 26区分大小写 ： 已选择多个值 ： 已选择 |  |  |
| 4 | 输入描述 | （可选）在 维护描述 标签页。 |  |  |
| 5 | 输入附加数据 | 导航到 附加数据 标签页并维护以下数据：表名称 ： SDCOM字段名称 ： VKOND未做好输入准备 ： 已选择不显示 ： 已选择 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 新特征已创建。 |  |

特征 SERVICE_CHANNEL（服务通道）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理特征 。在 特征 屏幕中，维护 特征 ： SERVICE_CHANNEL然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入基本数据 | 在 中 基本数据 区域中，维护以下数据：描述 ： 服务通道状态 ： 已发布数据类型 ： 字符格式字符数 ： 20多个值 ： 已选择需要输入 ： 已选择 |  |  |
| 4 | 输入描述 | （可选）在 维护描述 标签页。 |  |  |
| 5 | 输入值 | 导航到 价值 标签页并维护以下数据：特征值/描述 ： 电子邮件/电子邮件支持特征值/描述 ： 电话/电话支持 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 新特征已创建。 |  |

特征 PREVENTIVE_MAINTENANCE（预防性维护）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理特征 。在 特征 屏幕中，维护 特征 ： PREVENTIVE_MAINTENANCE然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入基本数据 | 在 中 基本数据 区域中，维护以下数据：描述 ： 预防性维护状态： 已发布数据类型 ： 字符格式字符数 ： 20多个值 ： 已选择需要输入 ： 已选择 |  |  |
| 4 | 输入描述 | （可选）在 维护描述 标签页。 |  |  |
| 5 | 输入值 | 导航到 价值 标签页并维护以下数据：特征值/描述 ： 每年/每年特征值/描述 ： HALFYEARLY / 每半年特征值/描述 ： 每季度/每季度 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 新特征已创建。 |  |

#### 创建类

目的

在此活动中，您将创建一个类，将上一章节中的特征分配到该类。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理类 。在 类别 屏幕上，维护以下数据：类别 ： SERVICE_CONTRACT_C类类型 ： 300 变式然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入基本数据 | 在 中 基本数据 区域中，维护以下数据：描述 ： 服务合同类状态 ： 已发布不检查 ： 已选择 |  |  |
| 4 | 输入特征 | 导航到 特征 标签页并维护以下数据：VARKONDSERVICE_CHANNELPREVENTIVE_MAINTENANCE | 相关特征将分配到类。 |  |
| 5 | 保存类 | 选择 保存 。 | 新类即被创建。 |  |

#### 为合同创建可配置服务产品

目的

在此活动中，维护可在服务合同中使用的可配置服务产品。

|  |
| --- |
| 备注 需要巴西特定字段才能获得正确的税收计算。检查创建 为主数据定义巴西特定字段章节中的主数据（巴西）(JD0_BR) （针对物料主数据）。 |

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 选择 创建物料 链接位于 管理产品主数据 磁贴。 | 因此， 创建物料（初始屏幕） 显示 。 |  |
| 3 | 输入物料标识和类型 | 在 创建物料（初始屏幕） 维护 以下条目：材料 ： SRV_CONTR_CONFIG行业部门 ： M如果 行业部门 输入字段已隐藏，无需输入。物料类型 ： 服务产品然后选择 继续（回车） 。 |  |  |
| 4 | 选择基本数据视图 | 在 选择视图 对话窗口中，选择 基本数据 1 视图，然后选择 继续（回车） 。在 组织级别 对话框中，输入 以下：工厂：1710销售组织： 1710分销渠道：10备注 对于 DE，输入工厂/销售组织/分销渠道作为 1010/1010/10 | 因此， 创建物料 SRV_CONTR _CONFIG 视图为 显示。 |  |
| 5 | 输入基本数据 | 在 基本数据 1 视图中，维护以下值：描述 ： 可配置服务 合同基本计量单位 ： AU（活动单位）物料组 ： P001（服务）一般项目组 ： SCNP（服务合同产品）物料可配置： 已选择导航到 附加数据 并维护以下数据：语言 ： 德国物料描述 ： Konfigurierbarer Servicevertrag然后选择 保存 。 | 产品已创建，并且 创建物料（初始屏幕） 视图。 |  |
| 6 | 选择销售视图 | 在 创建物料（初始屏幕） 视图、 维护物料 SRV_CONTR_CONFIG ，然后选择 继续（回车） 。在 选择视图 对话窗口中，选择以下视图：销售：销售组织数据 1销售：销售组织数据 2销售：一般/工厂数据然后选择 继续（回车）。 | 因此， 组织级别 对话框窗口。 |  |
| 7 | 选择组织级别 | 在 组织级别 对话窗口中，维护以下值：工厂 ： 1710（工厂 1 美国）销售组织 . ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）备注 注释：对于 DE，维护 1010/1010/10 信息。然后选择 继续（回车） 。 | 因此， 销售：销售组织 1 视图。 |  |
| 8 | 输入销售组织数据 (1) | 在 销售：销售组织 1 视图中，维护以下值：常规数据• 现金折扣 ：X <已选择>税务数据• 税收分类 ：1（全额税）然后选择 输入 。 | 因此， 销售：销售组织 2 视图。 |  |
| 9 | 输入销售组织数据 (2) | 在 销售：销售组织 2 视图中，维护以下条目：项目类别组 ： SCNP（服务合同产品）然后选择 输入 。 | 因此， 销售：一般/工厂 视图。 |  |
| 10 | 输入一般销售数据 | 在 销售：一般/工厂 视图中，维护以下值：基本计量单位 ： AU（活动单位）工作持续时间 ： 1 HR然后选择 保存 。仅针对波兰：选择 输入 而不是 保存 。 | 因此， 创建物料（初始屏幕） 视图。 |  |
| 仅适用于波兰 | 输入销售数据 | 在 中 国际贸易：出口 部分，输入以下数据：控制代码。 ：例如， 41.00.30.0然后选择 保存 。 | 因此， 创建物料（初始屏幕） 视图。 |  |
| 11 | 选择分类视图 | 在 创建物料（初始屏幕） 视图、 维护物料 SRV_CONTR_CONFIG ，然后选择 继续（回车） 。在 选择视图 对话窗口中，选择以下视图：分类然后选择 继续（回车）。 | 因此， 分类 视图。 |  |
| 12 | 输入分类 | 在 类类型 对话窗口中，选择 变式 (300) 条目，然后选择 复制 。在 分类 视图中，维护以下数据：类别 ： SERVICE_CONTRACT_C选择 输入 显示特征 指派给类。在 中 类 SERVICE_CONTRACT_C 的值 屏幕区域中，为每个特征打开值帮助并选择所有可用值。然后选择 保存 。 | 因此， 创建物料（初始屏幕） 视图。 |  |

#### 创建配置参数文件

目的

在此活动中，您可以在变式配置建模器中创建配置参数文件。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 VC 建模环境 。在 变式配置建模环境的初始屏幕 屏幕上，维护以下数据：材料 ： SRV_CONTR_CONFIG类类型 ： 300（变式）然后选择 输入模型 。 | 因此， SRV_CONTR_CONFIG 的配置 屏幕。 |  |
| 3 | 创建配置参数文件 | 在 中 对象 列中，右键单击 SRV_CONTR_CONFIG 条目并选择 创建配置参数文件 。在 创建配置参数文件 对话窗口中，维护以下数据：配置参数文件 ： SRV_CONTR_CONF无更改编号 . ： 已选择然后选择 继续（回车）。在 中 对象 窗格中，双击 SRV_CONTR_CONFIG 物料。打开 变式定价 标签页，请选择 更改 ，然后选择 展开列表 。维护分配到可配置的所有特征 除 VARKOND 特征外的产品。此外，请确保 维护所有变式条件和描述。因此， 变式条件在价格条件中使用 维护。例如，对于 特征/特征值 / 变式条件 / 变式条件描述 ， 维护：SERVICE_CHANNEL / 电子邮件 / 电子邮件 /电子邮件 支持SERVICE_CHANNEL/电话/电话/电话 支持PREVENTIVE_MAINTENANCE / 年/年/ 每年PREVENTIVE_MAINTENANCE / HALFYEARLY / HALFYEARLY / 每半年PREVENTIVE_MAINTENANCE / 每季度 / 季度 / 每季度然后选择 保存 。 | 因此， SRV_CONTR_CONFIG 的配置 屏幕。 |  |

#### 设置价格

目的

在此活动中，维护可配置服务产品的标准价格条件记录，以及可配置变式的变式价格记录。

过程

条件类型：PSI1（服务合同项目的价格）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 设置物料价格 。 | 因此， 更改条件记录 视图。 |  |
| 3 | 输入条件类型 | 在 更改条件记录 视图，维护 条件类型 ： PSI1 (服务合同价格), 然后选择 输入 。 | 因此， 组合键 视图。 |  |
| 4 | 选择关键字组合 | 在 中 关键字组合 视图，选择 材料然后选择 输入 。 | 因此， 更改价格 (PSI1)：选择 视图。 |  |
| 5 | 选择 | 在 更改价格 (PSI1)：选择 视图中，维护以下信息：销售组织 ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）材料 ：SRV_CONTRACT（服务合同产品）生效日期 ： <日期> ，例如， 当天日期然后选择 执行 。 | 因此， 更改价格条件 (PPSI)：概览 视图。 |  |
| 6 | 输入价格条件 | 在 更改价格条件 (PSI1)：概览 视图中，维护以下数据：材料 ： SRV_CONTR_CONFIG （可配置服务合同）金额 ：例如， 200.00单位 ：例如， 美元有效自 ： <日期> 例如，当天日期选择 输入 。然后选择 保存 。 | 服务产品 SRV_CONTR_CONFIG 的标准价格已 维护。 |  |

条件类型：VASE（变式价格）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 设置物料价格 。 | 因此， 更改条件记录 视图。 |  |
| 3 | 输入条件类型 | 在 更改条件记录 视图，维护 条件类型 ： VASE （变式价格）， 然后选择 输入 。 | 因此， 更改变式价格 视图。 |  |
| 4 | 输入销售数据 | 在 更改变式价格 (VASE)：选择 视图中，维护以下信息：销售组织 ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）材料 ： SRV_CONTR_CONFIG （可配置服务合同）生效日期 ： <日期> 例如，当天日期然后选择 执行 。 | 因此， 更改变式价格条件 (VASE)：概览 视图。 |  |
| 5 | 输入变式条件 | 在 更改变式价格条件 (VASE)：概览 视图中，维护您在上一章中维护的所有变式条件的价格，例如：变体/金额/单位 ：电子邮件/30 美元电话/50 美元每年 / 250 美元HALFYEARLY / 135 USD每季度/90 美元选择 输入 并验证您的输入。然后选择 保存 。 | 已维护变式价格条件。 |  |

### 为服务订单创建可配置服务产品

#### 创建特征

目的

在此活动中，创建可在可配置服务产品中进行选择的特征，并且可以为其维护单个变式价格。

过程

特征 VARKOND（变式条件代码）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理特征 。在 特征 屏幕的 字段中， 特征 ：输入 VARKOND然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入基本数据 | 在 中 基本数据 区域，输入以下数据：描述 ： 变式条件键值状态 ： 已发布日期类型 ： 字符格式字符数 ： 26区分大小写 ： 已选择多个值 ： 已选择 |  |  |
| 4 | 输入描述 | 或者，您可以在 维护描述 标签页。 |  |  |
| 5 | 输入附加数据 | 导航到 附加数据 标签页并输入以下数据：表名称 ： SDCOM字段名称 ： VKOND未做好输入准备 ： 已选择不显示 ： 已选择 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 已创建新的变式条件代码。 |  |

特征 CAR_WASH_TYPE（洗车类型）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理特征 。在 特征 屏幕的 字段中， 特征： 输入 CAR_WASH_TYPE然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入基本数据 | 在 中 基本数据 区域，输入以下数据：描述 ： 洗车类型状态 ： 已发布日期类型 ： 字符格式字符数 ： 20单值 ： 已选择需要输入 ： 已选择 |  |  |
| 4 | 输入描述 | 或者，您可以在 维护描述 标签页。 |  |  |
| 5 | 输入值 | 导航到 价值 标签页并输入以下数据：特征值/描述 ： 基本/ 基本清洗特征值/描述 ： 标准/ 标准洗手特征值/描述 ： 高级 / 高级洗手 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 新特征已创建。 |  |

特征 CAR_SIZE（汽车尺寸）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理特征 。在 特征 屏幕的 字段中， 特征： 输入 CAR_SIZE然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入基本数据 | 在 中 基本数据 区域，输入以下数据：描述 ： 汽车尺寸状态： 已发布日期类型 ： 字符格式字符数 ： 20单值 ： 已选择需要输入 ： 已选择 |  |  |
| 4 | 输入描述 | 或者，您可以在 维护描述 标签页。 |  |  |
| 5 | 输入值 | 导航到 价值 标签页并输入以下数据：特征值/描述 ： S / 小型特征值/描述 ： M / 中等特征值/描述 ： L / 大型 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 新特征已创建。 |  |

特征 EXTRA_POLISH（附加波兰语）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理特征 。在 特征 屏幕的 字段中， 特征： 输入 EXTRA_POLISH然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入基本数据 | 在 中 基本数据 区域，输入以下数据：描述 ： 额外波兰语状态： 已发布日期类型 ： 字符格式字符数 ： 10单值 ： 已选择需要输入 ： 已选择 |  |  |
| 4 | 输入描述 | 或者，您可以在 维护描述 标签页。 |  |  |
| 5 | 输入值 | 导航到 价值 标签页并输入以下数据：特征值/描述 ： 是/是特征值/描述 ： 否/否 |  |  |
| 6 | 保存特征 | 选择 保存 。 | 新特征已创建。 |  |

#### 创建类

目的

在此活动中，您将创建一个类，将上一章节中的特征分配到该类。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 管理类 。在 类别 屏幕上，输入以下数据：类别 ： CAR_WASH类类型 ： 300（变式）然后选择 创建 。 | 随即显示附加屏幕区域。 |  |
| 3 | 输入类名称 | 在 类屏幕 ，输入以下数据：类别 ： CAR_WASH类类型 ： 300（变式）然后选择 创建 |  |  |
| 4 | 输入基本数据 | 在 中 基本数据 区域，输入以下数据：描述 ： 汽车 清洗状态 ： 已发布不检查 ： 已选择 |  |  |
| 5 | 输入特征 | 导航到 特征 标签页并维护以下数据：VARKONDCAR_WASH_TYPECAR_SIZEEXTRA_POLISH | 相关特征将分配到类。 |  |
| 6 | 保存类 | 选择 保存 。 | 新类即被创建。 |  |

#### 为服务订单创建可配置服务产品

目的

在此活动中，维护可在服务中使用的可配置服务产品 订单。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 选择 创建物料 应用。 | 因此， 创建物料（初始屏幕） 显示 。 |  |
| 3 | 输入物料标识和类型 | 在 创建物料（初始屏幕） ，输入 以下数据：材料 ： CAR-WASH_CONF如果 行业部门 输入字段已隐藏，无需输入。物料类型 ： SERV 服务产品然后选择 继续（回车） 。 |  |  |
| 4 | 选择基本数据视图 | 在 组织级别 对话框中，输入以下数据：工厂 ： 1710（工厂 1 美国）销售组织 . ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）注释：对于 DE，输入 1010/1010/10 信息。然后选择 继续（回车） 。 | 因此， 创建物料 CAR-WASH _CONF 视图为 显示。 |  |
| 5 | 输入基本数据 | 在 基本数据 1 标签上，输入以下数据：描述 . ： 可配置洗车基本计量单位 ： AU（活动单位）物料组 ： P001（服务）一般项目类别组 ： SRVP（服务 产品）物料可配置： 已选择导航到 附加数据 并维护以下数据：语言 ： 德国物料描述 ： Konfigurierbare Autowäsche然后选择 保存 。 | 产品已创建，并且 创建物料（初始屏幕） 视图。 |  |
| 6 | 选择销售视图 | 在 创建物料（初始屏幕） 视图，在 字段 物料、 输入 CAR-WASH_CONF ，然后选择 继续 （输入） 。在 选择视图 对话框中，选择以下视图：销售：销售组织数据 1销售：销售组织数据 2销售：一般/工厂数据然后选择 继续（回车）。 | 因此， 组织级别 对话框窗口。 |  |
| 7 | 选择组织级别 | 在 组织级别 对话框中，输入以下数据：工厂 ： 1710（工厂 1 美国）销售组织 . ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）注释：对于 DE，输入 1010/1010/10 信息。然后选择 继续（回车） 。 | 因此， 销售：销售组织 1 视图。 |  |
| 8 | 输入销售组织数据 (1) | 在 销售：销售组织 1 标签上，输入以下数据：常规数据• 现金折扣 ：X <已选择>税务数据• 税收分类 ：1（全额税）然后选择 输入 。 | 因此， 销售：销售组织 2 视图。 |  |
| 9 | 输入销售组织数据 (2) | 在 销售：销售组织 2 标签上，输入以下数据：项目类别组 ： SRVP（服务产品）然后选择 输入 。 | 因此， 销售：一般/工厂 视图。 |  |
| 10 | 输入一般销售数据 | 在 销售：一般/工厂 标签上，输入以下数据：基本计量单位 ： AU（活动单位）工作持续时间 ： 1 HR然后选择 保存 。仅针对波兰：选择 输入 而不是 保存 。 | 因此， 创建物料（初始屏幕） 视图。 |  |
| 仅适用于波兰 | 输入销售数据 | 在 国际贸易：出口 选项卡（在 区域中） 外贸日期 ，输入以下数据：控制代码。 ：例如， 41.00.30.0然后选择 保存 。 |  |  |
| 11 | 选择分类视图 | 在 创建物料（初始屏幕） 视图，在 字段 材料 输入 CAR-WASH_CONF ，然后选择 继续 （输入） 。在 选择视图 对话框中，选择以下视图：分类然后选择 继续（回车）。 | 因此， 分类 视图。 |  |
| 12 | 输入分类 | 在 类类型 对话框中，选择 变式 (300) 条目，然后选择 复制 。在 分类 视图中，输入以下数据：类别 ： CAR_WASH选择 输入 显示分配到类的特征。在 中 类 CAR_WASH 的值 屏幕区域中，为每个特征打开值帮助并选择所有可用值。然后选择 保存 。 | 将特征分配到物料。 |  |

#### 创建配置参数文件

目的

在此活动中，您可以在变式配置建模器中创建配置参数文件。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 产品配置建模器 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 VC 建模环境 。在 变式配置建模环境的初始屏幕 屏幕上，输入以下数据：材料 ： CAR-WASH_CONF类类型 ： 300（变式）然后选择 输入模型 。 | 因此， CAR_WASH_CONF 的配置 屏幕。 |  |
| 3 | 创建配置参数文件 | 在 中 对象 列中，右键单击 CAR-WASH_CONF 条目并选择 创建配置参数文件 。在 创建配置参数文件 对话框中，输入以下数据：配置参数文件 ： CAR-WASH_CONF无更改编号 . ： 已选择然后选择 继续（回车）。在 中 对象 列中，双击 CAR-WASH_CONF 条目。打开 变式定价 标签页，然后选择 更改 。然后选择 展开 列表 。输入分配给可配置产品的所有特征，VARKOND 特征除外。此外，请确保输入 变式条件 以及 描述 给所有人。变式条件用于价格条件维护。例如，对于 特征/特征值/变式条件/变式条件描述 ，输入：CAR_WASH_TYPE / BASIC / C_W_T_B / 基本CAR_WASH_TYPE / STANDARD / C_W_T_S / 标准CAR_WASH_TYPE / PREMIUM / C_W_T_P / 高级版CAR_SIZE / S / C_S_S / 小CAR_SIZE / M / C_S_M / 中CAR_SIZE / L / C_S_L / 大EXTRA_POLISH / 是 / E_P_Y / 是EXTRA_POLISH / NO / E_P_N / 否然后选择 保存 。 | 为所有特征创建变式条件。 |  |

#### 设置价格

目的

在此活动中，维护可配置服务产品的标准价格条件记录，以及可配置变式的变式价格记录。

过程

条件类型：PPR0（价格）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 设置物料价格 。 | 因此， 更改条件记录 视图。 |  |
| 3 | 输入条件类型 | 在 更改条件记录 视图，在字段 条件类型 ：输入 PPR0（价格）， 然后选择 输入 。 | 因此， 组合键 视图。 |  |
| 4 | 选择关键字组合 | 在 中 关键字组合 视图，选择 材料然后选择 输入 。 | 因此， 更改价格 (PPR0)：选择 视图。 |  |
| 5 | 选择 | 在 更改价格 (PPR0)：选择 视图中，输入以下数据：销售组织 ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）材料 ： CAR-WASH_CONF（洗车） 可配置）生效日期 ： <日期> ，例如， 当天日期然后选择 执行 。 | 因此， 更改价格条件 (PPR0)：概览 视图。 |  |
| 6 | 输入价格条件 | 在 更改价格条件 (PPR0)：概览 视图中，输入以下数据：材料 ： CAR-WASH_CONF（洗车） 可配置）金额 ：例如， 10.00单位 ：例如， 美元有效自 ： <日期> 例如，当天日期选择 输入 。然后选择 保存 。 | 创建服务产品的标准价格。 |  |

条件类型：PVA0（变式价格）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 设置物料价格 。 | 因此， 更改条件记录 视图。 |  |
| 3 | 输入条件类型 | 在 更改条件记录 视图，维护 条件类型 ： PVA0（变式价格）， 然后选择 输入 。 | 因此， 更改变式价格 视图。 |  |
| 4 | 输入销售数据 | 在 更改变式价格 (PVA0)：选择 视图中，维护以下信息：销售组织 ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）材料 ： CAR-WASH_CONF （可配置服务合同）生效日期 ： <日期> 例如，当天日期然后选择 执行 。 | 因此， 更改变式价格条件 （ PVA0): 概览 视图。 |  |
| 5 | 输入变式条件 | 在 创建变式价格条件 (PVA0)：概览 视图中，输入您在上一章创建的所有变式条件的价格，例如：变体/金额/单位 ：C_W_T_B/5 美元C_W_T_S/8 美元C_W_T_P/12 美元C_S_S/2 美元C_S_M/4 美元C_S_L/10 美元选择 输入 并验证您的输入。然后选择 保存 。 | 变式价格条件已创建。 |  |

PVA1（变式价格 %）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 设置物料价格 。 | 因此， 更改条件记录 视图。 |  |
| 3 | 输入条件类型 | 在 更改条件记录 视图，在字段 条件类型 ：输入 PVA1 变式价格 (%)， 然后选择 输入 。 | 因此， 更改变式价格 (% PVA1) 视图。 |  |
| 4 | 输入销售数据 | 在 更改变式价格 (% (PVA1): 选择 视图中，输入以下数据：销售组织 ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）材料 ： CAR-WASH_CONF生效日期 ： <日期> 例如，当天日期然后选择 执行 。 | 因此， 更改变式价格 (%) 条件 (PVA1) ：概览 视图。 |  |
| 5 | 输入变式条件 | 在 创建变式价格 (%) 条件 (PVA1)：概览 视图中，输入所有相关变式条件的条件记录，例如：变体/金额/单位 ：E_P_Y / 20%E_P_N / -10%选择 输入 并验证您的输入。然后选择 保存 。 | 变式价格条件已创建。 |  |

### 创建服务产品的物料变式

目的

在此活动中，使用预定义配置创建物料变式， 用于服务订单。变式的主记录链接到可配置的 产品使用其特征。

过程

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 主数据专家 - 产品数据 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 选择链接 创建物料 管理产品主数据 磁贴。 | 因此， 创建物料（初始屏幕） 显示 。 |  |
| 3 | 输入物料标识和类型 | 在 创建物料（初始屏幕） 输入 以下数据：材料 ： CAR-WASH-VAR行业部门 ： 机械工程如果 行业部门 输入字段已隐藏，无需输入。物料类型 ： SERV 服务产品然后选择 继续（回车） 。在 选择视图 对话框中，选择 基本数据 1选择 组织级别 |  |  |
| 4 | 选择组织级别 | 在 组织级别 对话框中，输入以下数据：工厂 ： 1710（工厂 1 美国）销售组织 ： 1710（国内 销售组织 (US)分销渠道 ： 10 直接销售备注 对于 DE，输入 1010/1010/10 分别为。然后选择 继续（回车） 。 | 因此， 创建物料 CAR-WASH-VAR 视图。 |  |
| 5 | 输入基本数据 | 在 基本数据 1 标签上，输入以下数据：描述 ： 洗车 变式基本计量单位 ： AU（活动单位）物料组 ： P001（服务）一般项目组 ： SRVP（服务产品）物料可配置： 未选定跨工厂 CM： CAR-WASH_CONF选择 配置变式在视图中 变式配置选择以下特征：汽车尺寸： 小型额外波兰语： 是洗车类型： 标准洗手选择 完成然后，选择 保存 。 | 产品已创建，并且 创建物料（初始屏幕） 视图。 |  |
| 6 | 选择销售视图 | 在 创建物料（初始屏幕） 视图，在字段 物料、 输入 CAR-WASH-VAR ，然后选择 继续（回车） 。在 选择视图 对话框中，选择以下视图：销售：销售组织数据 1销售：销售组织数据 2销售：一般/工厂数据然后，选择 继续（回车）。 | 因此， 组织级别 对话框窗口。 |  |
| 7 | 选择组织级别 | 在 组织级别 对话框中，输入以下数据：工厂 ： 1710（工厂 1 美国）销售组织 . ： 1710（国内销售组织 - US）分销渠道 ： 10 直接销售备注 对于 DE，输入 1010/1010/10 分别为。然后，选择 继续（回车） 。 | 因此， 销售：销售组织 1 视图。 |  |
| 8 | 输入销售组织数据 (1) | 在 销售：销售组织 1 标签上，输入以下数据：常规数据• 现金折扣 ：X <已选择>• 税务数据• 税收分类 ：1（全额税）然后，选择 输入 。 | 因此， 销售：销售组织 2 视图。 |  |
| 9 | 输入销售组织数据 (2) | 在 销售：销售组织 2 标签上，输入以下数据：项目类别组 ： SRVP（服务产品）然后，选择 输入 。 | 因此， 销售：一般/工厂 视图。 |  |
| 10 | 输入一般销售数据 | 在 销售：一般/工厂 标签上，输入以下数据：基本计量单位 ： AU（活动单位）工作持续时间 ： 1 HR然后，选择 保存 。 | 因此， 创建物料（初始屏幕） 视图。 |  |

#### 设置物料变式的价格

目的

在此活动中，维护变式的标准价格条件记录。

过程

条件类型：PPR0（价格）

| 测试步骤编号 | 测试步骤名称 | 指令 | 预期结果 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 登录 | 以 身份登录 SAP Fiori 快速启动板 定价专家 。 | 因此， 主页 页面。 |  |
| 2 | 访问应用 | 打开 设置物料价格 。 | 因此， 更改条件记录 视图。 |  |
| 3 | 输入条件类型 | 在 更改条件记录 条件类型 ：输入 PPR0 （价格）， 然后选择 输入 。 | 因此， 组合键 视图。 |  |
| 4 | 选择关键字组合 | 在 中 关键字组合 视图，选择 物料含 发布状态然后，选择 输入 。 | 因此， 更改价格 (PPR0)：选择 视图。 |  |
| 5 | 选择 | 在 更改价格 (PPR0)：选择 视图中，输入以下数据：销售组织 ： 1710（国内销售组织 - US）分销渠道 ： 10（直销）材料 ： CAR-WASH-VAR（洗车变式）生效日期 ： <日期> ，例如，当天日期然后，选择 执行 。 | 因此， 更改价格条件 (PPR0)：概览 视图。 |  |
| 6 | 输入价格条件 | 在 更改价格条件 (PPR0)：概览 视图中，输入以下数据：材料 ： CAR-WASH-VAR（洗车 VAR）金额 ：例如， 20.00单位 ：例如， 美元有效自 ： <日期> 例如，当天日期选择 输入 。然后，选择 保存 。 | 为变式创建标准价格。 |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: PSI1 selection step uses material SRV_CONTRACT while the price condition entry uses SRV_CONTR_CONFIG

> [!warning] Conflict
> Flagged while digesting this document, not verified: Contract product uses material type 'Service Product' while the service order product uses SERV; item category group SCNP vs SRVP

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-configurable-service-product-mds-5be-431]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-5be-433]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-configurable]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_ZH_XX.docx` — full document · extracted with `mammoth` · 22,488 chars in the whole document
