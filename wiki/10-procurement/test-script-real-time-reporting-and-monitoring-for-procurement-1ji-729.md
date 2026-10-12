---
id: 10-procurement/test-script-real-time-reporting-and-monitoring-for-procurement-1ji-729
title: "Test Script: Real-Time Reporting and Monitoring for Procurement (1JI) (1JI_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud 2608 test script for scope item 1JI: roles, prerequisites and tests of Procurement Overview, analytical list pages and Spend Dashboard."
cluster: 10-procurement
tags: [kb/procurement, topic/procurement-analytics]
aliases: [1JI_S4CLD2608_BPD_EN_XX]
keywords: [Procurement Analytics and Monitoring, procurement analytics, procurement overview page, purchase contract monitoring, rfq monitoring, purchase order monitoring, supplier confirmations, scheduling agreements, material price variance, central procurement]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1JI_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-729
topic: 10-procurement/procurement-analytics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Real-Time Reporting and Monitoring for Procurement (1JI) (1JI_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1JI_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Procurement Analytics and Monitoring** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Real-Time Reporting and Monitoring for Procurement (1JI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851581)

[2 Prerequisites 4](#_Toc232851582)

[2.1 System Access 4](#_Toc232851583)

[2.2 Roles 4](#_Toc232851584)

[2.2.1 Roles for Procurement Overview Page 4](#_Toc232851585)

[2.2.2 Roles for Monitor Purchase Contract Items Analytical List Page 6](#_Toc232851586)

[2.2.3 Roles for Monitor RFQ Items Analytics List Page 6](#_Toc232851587)

[2.2.4 Roles for Monitor Purchase Order Items Analytics List Page 6](#_Toc232851588)

[2.2.5 Roles for Monitor Supplier Confirmations Analytics List Page 7](#_Toc232851589)

[2.2.6 Roles for Monitor Scheduling Agreement Items Analytics List Page 7](#_Toc232851590)

[2.2.7 Roles for Material Price Variance Analytics List Page 7](#_Toc232851591)

[2.2.8 Roles for Monitor Central Purchase Contract Items Analytics List Page 8](#_Toc232851592)

[2.2.9 Roles for Monitor Purchase Order Items Centrally Analytics List Page 8](#_Toc232851593)

[2.2.10 Roles for Material Price Comparison Analytics List Page 8](#_Toc232851594)

[2.2.11 Roles for Overdue Purchase Order Items 9](#_Toc232851595)

[2.2.12 Roles for Purchase Order Value and Scheduling Agreement Value 9](#_Toc232851596)

[2.2.13 Roles for Purchasing Spend Dashboard 9](#_Toc232851597)

[2.2.14 Roles for Supplier Invoice Inbound Automation Rate 10](#_Toc232851598)

[2.3 Preliminary Steps 10](#_Toc232851599)

[2.3.1 Business Conditions 10](#_Toc232851600)

[2.3.2 Setup Analytical Reporting Currencies (Optional) 11](#_Toc232851601)

[2.3.3 Schedule Job for Migration of Purchasing Data (Optional) 11](#_Toc232851602)

[2.3.4 Enable Performance Optimization for Purchasing Analytics Apps (Optional) 12](#_Toc232851603)

[3 Overview Table 13](#_Toc232851604)

[4 Test Procedures 15](#_Toc232851605)

[4.1 Procurement Overview Page 15](#_Toc232851606)

[4.2 Monitor Purchase Contract Items Analytics List Page 19](#_Toc232851607)

[4.3 Monitor RFQ Items Analytics List Page 21](#_Toc232851608)

[4.4 Monitor Purchase Order Items Analytics List Page 22](#_Toc232851609)

[4.5 Monitor Supplier Confirmations Analytics List Page 23](#_Toc232851610)

[4.6 Monitor Scheduling Agreement Items Analytics List Page 25](#_Toc232851611)

[4.7 Material Price Variance Analytics List Page 27](#_Toc232851612)

[4.8 Embedded Analytics in Supplier Object Page 28](#_Toc232851613)

[4.9 Monitor Central Purchase Contract Items Analytics List Page 28](#_Toc232851614)

[4.10 Monitor Purchase Order Items Centrally Analytics List Page 29](#_Toc232851615)

[4.11 Overdue Purchase Order Items 31](#_Toc232851616)

[4.12 Purchase Order Value and Scheduling Agreement Value 32](#_Toc232851617)

[4.13 Purchasing Spend Dashboard 33](#_Toc232851618)

[4.13.1 Story Tabstrip: Overview 34](#_Toc232851619)

[4.13.2 Story Tabstrip: Details 36](#_Toc232851620)

[4.13.3 Story Tabstrip: Context 37](#_Toc232851621)

[4.13.4 Story Tabstrip: Off Contract Overview 38](#_Toc232851622)

[4.13.5 Story Tabstrip: Off Contract Details 40](#_Toc232851623)

[4.14 Supplier Invoice Inbound Automation Rate 41](#_Toc232851624)

## Purpose

Overview

The Procurement Overview Page presents key information and tasks for a purchaser. It displays all relevant information on a single page, using attractive and efficient actionable cards for various content types. The user-friendly experience makes viewing, filtering, and acting upon data simple, faster and smarter – even on mobile devices. Analytical list pages are also provided to monitor purchase contract items, supplier confirmation, and purchase order items.

The purchaser views a high-level overview of important information, such as expiring contracts, overdue purchase orders or urgent purchase requisitions as well as an overview of different procurement KPIs. With these KPIs, the purchaser can easily determine the performance of suppliers, monitor non-managed spend or purchasing spend, and quickly discover trends and potential areas of improvement.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

#### Roles for Procurement Overview Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

To use the Procurement Overview Page (F1990) app, end users are required to have the SAP_MM_BC_PRC_OVP_PC business catalog assigned to their users (this business catalog is also included in the SAP_BR_BUYER and the SAP_BR_PURCHASER business roles). The table below shows which cards require which business catalog in the Procurement Overview Page (F1990).

|  |
| --- |
| Note The prefix for the names of the corresponding business catalog roles is “SAP_BCR_MM_*”. For example, the business catalog role for catalog “SAP_MM_BC_PO_PROCESS” is “SAP_BCR_MM_PO_PROCESS”. |

| Card | Business Catalog (Original) | Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- | --- | --- |
| Monitor Purchase Order Items | SAP_MM_BC_PC_PROCESS_MCSAP_MM_BC_PC_PROCESS | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Monitor Purchase Requisition Items | SAP_MM_BC_PC_PROCESS | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Monitor Purchase Contracts | SAP_MM_BC_PC_PROCESS_MC | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Monitor RFQs | SAP_MM_BC_RFQ_PROCESS_PC | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Monitor Supplier Confirmations | SAP_MM_BC_PRC_OVP_PC | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Purchase Order Items | SAP_MM_BC_PRC_OVP_PC | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Open Activities | SAP_MM_BC_SUP_ACT_MGT_PC | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Purchasing Spend | SAP_MM_BC_PUR_STRATEGY | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Non-Managed Spend | SAP_MM_BC_PUR_STRATEGY | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Off-Contract Spend | SAP_MM_BC_PUR_STRATEGY | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Supplier Performance Monitoring | SAP_MM_BC_PUR_STRATEGY | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Purchase Requisition Touch Rate | SAP_MM_BC_PUR_STRATEGY | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Purchase Requisition Item Types | SAP_MM_BC_PUR_STRATEGY | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Supplier Performance Monitoring Including Questionnaire Score | SAP_MM_BC_PRC_OVP_PC | Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |

#### Roles for Monitor Purchase Contract Items Analytical List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Monitor RFQ Items Analytics List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Monitor Purchase Order Items Analytics List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Monitor Supplier Confirmations Analytics List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Monitor Scheduling Agreement Items Analytics List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Material Price Variance Analytics List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Monitor Central Purchase Contract Items Analytics List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_MM_SPT_CNTRL_PURCHASING_PC |  |

#### Roles for Monitor Purchase Order Items Centrally Analytics List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_MM_SPT_CNTRL_PURCHASING_PC |  |

#### Roles for Material Price Comparison Analytics List Page

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Overdue Purchase Order Items

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Purchase Order Value and Scheduling Agreement Value

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Purchasing Spend Dashboard

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

#### Roles for Supplier Invoice Inbound Automation Rate

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Preliminary Steps

#### Business Conditions

Follow the procedures described in the following scope items to create the corresponding business data if needed.

| Scope Item | Business Condition |
| --- | --- |
| 18J - Requisitioning | Follow the scope item to create the corresponding business data. |
| BMD - Purchase Contract | Follow the scope item to create the corresponding business data. |
| BMK - Return to Supplier | Follow the scope item to create the corresponding business data. |
| BMR - Scheduling Agreements in Procurement | Follow the scope item to create the corresponding business data. |
| BMY - Subcontracting | Follow the scope item to create the corresponding business data. |
| BNX - Consumable Purchasing | Follow the scope item to create the corresponding business data. |
| J45 - Procurement of Direct Materials | Follow the scope item to create the corresponding business data. |
| 19C - Activity Management in Procurement | Follow the scope item to create the corresponding business data. |
| 19E - Supplier Classification and Segmentation | Follow the scope item to create the corresponding business data. |
| 1XF - Request for Price | Follow the scope item to create the corresponding business data. |
| 2ME - Central Purchase Contracts | Follow the scope item to create the corresponding business data. |

#### Setup Analytical Reporting Currencies (Optional)

Purpose

In this procedure, you can set up two analytical reporting currencies that are used in various analytical KPIs and queries in SAP S/4HANA Procurement. If user selects one of the two configured reporting currencies as display currency in an analytical KPI, the system doesn't convert the reporting currency to display currency at runtime. This enhances the performance of the KPI.

Procedure

Please refer to the steps in Prerequisites > Preliminary Step > Setup Analytical Reporting Currencies (Optional) on Scope Item SL4.

#### Schedule Job for Migration of Purchasing Data (Optional)

Purpose

In this procedure, you migrate purchasing data for analytics. Enter migration options and some additional parameters to migrate the data. Migration of data leads to performance optimization in purchasing analytics apps.

Procedure

Please refer to the steps in Prerequisites > Preliminary Step > Schedule Job for Migration of Purchasing Data (Optional) on Scope Item SL4.

#### Enable Performance Optimization for Purchasing Analytics Apps (Optional)

Purpose

In this procedure, you migrate purchasing data for analytics. Enter migration options and some additional parameters to migrate the data. Migration of data leads to performance optimization in purchasing analytics apps.

Procedure

Please refer to the steps in Prerequisites > Preliminary Step > Enable Performance Optimization for Purchasing Analytics Apps (Optional) on Scope Item SL4.

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Procurement Overview Page](#unique_24) [page ] 15 | Purchaser | Procurement Overview (F1990) | The Procurement Overview page is running properly. |
| [Monitor Purchase Contract Items Analytics List Page](#unique_25) [page ] 19 | Purchaser | Monitor Purchase Contract Items (F2423) | The Monitor Purchase Contract Items page is running properly. |
| [Monitor RFQ Items Analytics List Page](#unique_26) [page ] 21 | Purchaser | Monitor RFQ Items (F2425) . | The Monitor RFQ Items Analytics List page is running properly. |
| [Monitor Purchase Order Items Analytics List Page](#unique_27) [page ] 22 | Purchaser | Monitor Purchase Order Items (F2358) | The Monitor Purchase Order Items Analytics List page is running properly. |
| [Monitor Supplier Confirmations Analytics List Page](#unique_28) [page ] 23 | Purchaser | Monitor Supplier Confirmations (F2359) | The Monitor Supplier Confirmations Analytics List page is running properly. |
| [Monitor Scheduling Agreement Items Analytics List Page](#unique_29) [page ] 25 | Purchaser | Monitor Purchase Scheduling Agreement Items (F3143) | The Monitor Scheduling Agreement Items Analytics List page is running properly. |
| [Material Price Variance Analytics List Page](#unique_30) [page ] 27 | Purchaser | Material Price Variance (F3294) | The Material Price Variance Analytics List page is running properly |
| [Embedded Analytics in Supplier Object Page](#unique_31) [page ] 28 | Purchaser | Supplier (F0354) | The Supplier Object page is running properly. |
| [Monitor Central Purchase Contract Items Analytics List Page](#unique_32) [page ] 28 | CENTRAL_PURCHASER | Monitor Central Purchase Contract Items (F3492) | The Monitor Central Purchase Contract Items page is running properly. |
| [Monitor Purchase Order Items Centrally Analytics List Page](#unique_33) [page ] 29 | CENTRAL_PURCHASER | Monitor Purchase Order Items Centrally (F3676) | The Monitor Purchase Order Items Centrally page is running properly. |
| [Overdue Purchase Order Items](#unique_34) [page ] 31 | Purchaser | Overdue Purchase Order Items - Number and Value (F0343) | The Overdue Purchase Order Items app is running properly. |
| [Purchase Order Value and Scheduling Agreement Value](#unique_35) [page ] 32 | Purchaser | Purchase Order Value and Scheduling Agreement Value - Since the beginning of last year (F1378) | The Purchase Order Value and Scheduling Agreement Value app is running properly. |
| [Purchasing Spend Dashboard](#unique_36) [page ] 33 | Purchaser | Purchasing Spend Dashboard (F4517) | The Purchasing Spend Dashboard app is running properly. |
| [Supplier Invoice Inbound Automation Rate](#unique_37) [page ] 41 | Purchaser | Supplier Invoice Inbound Automation Rate - By Origin (F4518) | The Purchasing Spend Dashboard app is running properly. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Procurement Overview Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

You have implemented the Procurement Overview Page (F1990) app.

Purpose

With the following steps, you can test if the Procurement Overview Page (F1990) is running correctly.

Procedure

Table 1: Procurement Overview Page: General Test – Purchaser

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the Procurement Overview Page App | Open the Procurement Overview (F1990) app. | Check that the app is starting and the following cards are shown including content (the exact names may vary):Monitor Purchase ContractsMonitor Purchase Requisition Items,Monitor Purchase Order ItemsMonitor RFQs,Monitor Supplier Confirmations,Purchase Order Items |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Procurement Overview page.Extra fields can be added to the smart filter bar via Adapt Filters and selecting More Filters in the dialog box.The content of the cards shown is filtered via the corresponding fields in the smart filter bar.Enter different values in the different fields of the global filter. | Check if the content of the corresponding cards is filtered accordingly. |  |
| 4 | Pass On Filter Criteria to Corresponding App | If you have an active filter criteria (for example, filtered via a specific supplier), click the different card headers. | Check if the filter values from the Procurement Overview page have been applied in the corresponding App / KPI drilldown as well. |  |
| 5 | Hide Cards | Choose the User Icon at the top left of the page.Choose Manage Cards.Disable various cards via the toggle buttons in the dialog box and choose OK.In the same way, you can add the cards to the overview page again (or simply choose Reset in the Manage Cards dialog box).In addition, you can drag and drop the cards on the Procurement Overview page. | Check if the cards can be rearranged, hidden, and displayed again. |  |

Table 2: Procurement Overview Page: Card-Specific Test – Purchaser

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Monitor Purchase Contracts, Monitor Purchase Requisition Items, Monitor Purchase Order Items, Monitor RFQs, Monitor Supplier Confirmations, Purchase Order Items | After launching the Procurement Overview Page, investigate the cards:Monitor Purchase ContractMonitor Purchase Requisition ItemsMonitor Purchase Order ItemsMonitor RFQsMonitor Supplier ConfirmationsPurchase Order Items | The data is displayed properly. |  |
| 1.1 | Header Navigation to Apps | Choose the headers of these cards. | The corresponding app should be started, for example. Manage Purchase Contracts, Manage Purchase Requisitions, Monitor Purchase Order Items, Manage RFQs, Monitor Supplier Confirmations, Monitor Purchase Order Items. |  |
| 1.2 | Item Navigation to Apps | Choose items of these cards. | The lines should navigate to the corresponding Object Page / Display Transaction (Purchase Contracts, Request for Quotation, Purchase Orders Items, Monitor Supplier Confirmation). The Purchase Requisition Items navigate to a prefiltered Manage Purchase Requisitions app. |  |
| 1.3 | For Monitor Purchase Order Items, Switch Overdue and In Approval | Change the view from Overdue to In Approval and back again. | The data is displayed properly. |  |
| 1.4 | For Monitor Purchase Requisition Items, Switch Unsourced and Open Card | Change the view from Unsourced to Open and back again. | The data is displayed properly. |  |
| 1.5 | For Monitor Supplier Confirmations Card | Change the view among Missing Confirmation, Delivery Date Variance, Quantity Variance. | The data is displayed properly. |  |
| 1.6 | For Purchase Order Items Card | Investigate the Purchase Order Items card. | The data is displayed properly. |  |
| 1.6.1 | Navigation to KPI Drilldown Card | Select the card. | The corresponding KPI Drilldown app is launched. |  |

Table 3: Procurement Overview Page: General Test - Purchaser

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the Procurement Overview Page | Open the Procurement Overview app. | Check that the Procurement Overview app is starting and the following cards are displayed including content (the exact names may vary)Purchasing Spend (with Sub Menu Purchasing Spend Trend)Non-Managed SpendOff-Contract SpendSupplier Performance Monitoring (with Sub Menu Supplier Evaluation Trend)Purchase Requisition Item TypesPurchase Requisition Touch RateOpen ActivitiesSupplier Performance Monitoring Including Questionnaire Score |  |
| 3 | Use the Global Filters | The smart filter bar for the global filter is displayed at the top of the Procurement Overview screen.Extra fields can be added to the smart filter bar via Adapt Filters and selecting More Filters in the dialog box.The content of the shown cards is filtered via the corresponding fields in the smart filter bar.Enter different values in the different fields of the global filter. | Check if the content of the corresponding cards is filtered accordingly. |  |
| 4 | Pass On Filter Criteria to the Corresponding App | If you have an active filter criteria (for example, filtered via a specific supplier), choose the different card headers. | Check if the filter values from the Procurement Overview page have been applied in the corresponding App / KPI drilldown as well. |  |
| 5 | Hide Cards | Choose the user icon at the top right of the page.Choose Manage Cards.Disable various cards via the toggle buttons in the dialog box and choose OK.In the same way, you can add the cards again to the overview page (or simply choose Reset in the Manage Cards dialog box).In addition, you can drag and drop the cards on the Procurement Overview page. | Check that cards can be rearranged, hidden, and displayed again. |  |

Table 4: Procurement Overview Page: Card-Specific Test – Purchaser

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Purchasing Spend, Non-Managed Spend, Off-Contract Spend | Investigate the following cards: Purchasing Spend, Non-Managed Spend, Off-Contract Spend. | Check that the data is displayed properly. |  |
| 1.1 | Switch by Supplier and by Material Group | Change the view from Supplier to Material Group and back again. | Check that the data is displayed properly. |  |
| 1.2 | Header Navigation to KPI Drilldown | Choose the headers of these cards. | The corresponding KPI drilldown app (for example, Non-Managed Spend) should be launched. |  |
| 1.3 | Item Navigation to KPI Drilldown | Choose items of these cards. | The corresponding KPI drilldown app (for example, Non-Managed Spend) should be launched – with an active filter of the selected supplier / material group from the card. |  |
| 2 | Supplier Performance Monitoring, Supplier Performance Monitoring including Questionnaire Score | Investigate the following cards: Supplier Performance Monitoring and Supplier Performance Monitoring including Questionnaire Score | Check that the data is displayed properly. |  |
| 2.1 | Header Navigation | Choose the card header. | The corresponding KPI drilldown app should be launched. |  |
| 2.2 | Data-Point Navigation | Choose a supplier bubble. | The corresponding KPI drilldown app should be launched – with an active filter of the selected data point from the card. |  |
| 3 | Purchase Requisition Touch Rate, Purchase Requisition Item Types | Investigate the following cards: Purchase Requisition Touch Rate, Purchase Requisition Item Types. | Check that the data is displayed properly. |  |
| 3.1 | Navigation | Choose the card header. | The corresponding KPI drilldown app should be launched. |  |

### Monitor Purchase Contract Items Analytics List Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the following steps, you can test if the Monitor Purchase Contract Items app is running correctly.

Prerequisite

You have implemented the Monitor Purchase Contract Items app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the Monitor Purchase Contract Items App | Open the Monitor Purchase Contract Items (F2423) . | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections. |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Monitor Purchase Contract Items.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the cards shown is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | The corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page which can toggle to the visual filter view. Choose a part of the donut chart to filter data. | Check if the two charts work as visual filters:Contract items by Validity StatusContract items by Latest ReleaseCheck if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different Views on Content Part | Choose the chart view and list view at the top right of the page. | The chart view and list view are displayed. |  |
| 6 | Drilldown by Dimension | Choose Detais (the first icon button) on the icon bar. In the dialog box, choose one dimension to drill to a more detailed data level. | The drilldown function should work properly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type on the icon bar. In the dialog box, choose one chart type. | You are able to change the chart type. |  |
| 8 | Show Released Values | Go to the table section and view single contract items. For items whose released value is not equal to 0, purchase orders have been created against that contract item. Choose Contract Consumption Trend. | The historical trend of the contract usage is displayed. |  |

### Monitor RFQ Items Analytics List Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the following steps, you can test if the Monitor RFQ Items (F2425) app is running correctly.

Prerequisite

You have implemented the Monitor RFQ Items (F2425) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the Monitor RFQ Items App | Open the Monitor RFQ Items (F2425) . | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections. |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Monitor RFQ Items.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the cards shown is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page, which can toggle to the Visual Filter view. Choose a part of the donut chart to filter data. | Check if the two donut charts work as visual filters.RFQ items by Quotation Deadline StatusRFQ items by Quotation StatusCheck if the content of the corresponding data is filtered accordingly.Check if the line chart works as a visual filter:RFQ Item by Quotation Deadline |  |
| 5 | Toggle to Different View on Content Part | Choose Chart View and Table View at the top right of the page. | The table view and chart view are displayed. |  |
| 6 | Drilldown by Dimension | Choose Details (the first icon button) on the icon bar. In the dialog box, choose one dimension to drill to a more detailed data level. | The drilldown function works correctly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type (the seventh icon button) on the icon bar. In the dialog box, choose one chart type. | The chart type can be changed. |  |
| 8 | Filter from Chart | Select Awarded Quotation Value of a specific material group from the bar chart. | Check the table result. |  |

### Monitor Purchase Order Items Analytics List Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the following steps, you can test if the Monitor Purchase Order Items (F2358) app is running in a correct way.

Prerequisite

You have implemented the Monitor Purchase Order Items (F2358) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the Monitor Purchase Order Items App | Open Monitor Purchase Order Items (F2358) . | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections. |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Monitor Purchase Order Items (F2358) app.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown cards is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page, which can toggle to the Visual Filter view. Choose a part of donut chart to filter data. | Check if the visual filters work properly.Donut chart: Item Count by Next Delivery StatusLine chart: Item Count by Next DeliveryBar chart: Item Count by Internal StatusCheck if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different View on Content Part | Choose Chart and Table View and Chart View, and Table View at the top right of the page. | Check if the table view and chart view are displayed or not. |  |
| 6 | Drilldown by Dimension | Choose Details (the first icon button) on the icon bar. In the dialog box, choose one dimension to drill to a more detailed level data. | Check if the drilldown function works correctly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type (the seventh icon button) on the icon bar. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |
| 8 | Filter from Chart | Select the PO value of a specific material group from the bar chart. | Check the table result. |  |

### Monitor Supplier Confirmations Analytics List Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the following steps, you can test if the Monitor Supplier Confirmations (F2359) app is running in a correct way.

Prerequisite

You have implemented the Monitor Supplier Confirmations (F2359) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the Monitor Supplier Confirmation App | Open the Monitor Supplier Confirmations (F2359). | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections. |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Monitor Supplier Confirmations (F2359) app.Extra fields can be added to or removed from the Smart Filter Bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown cards is filtered via the corresponding fields in the Smart Filter Bar.Additional fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown cards is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page, which can toggle to the Visual Filter view. Choose a part of the donut chart to filter data. | Check if the visual filters work properly.Donut chart: PD items by order statusLine chart: PD items by Delivery Schedule DateBar chart: Schedule Line Quantity Value by supplier in K EURCheck if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different View on Content Part | Choose Chart and Table View, Chart View, and Table View at the top right of the page. | Check if the table view and chart view are displayed or not. |  |
| 6 | Drilldown by Dimension | Choose Show Details (the first icon button) on the icon bar. In the dialog box, choose one dimension to drill to a more detailed level data. | Check if the drilldown function works correctly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type (the seventh icon button) on the icon bar. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |
| 8 | Filter from Chart | Select the PO value of a specific supplier from the bar chart. | Check the table result. |  |

### Monitor Scheduling Agreement Items Analytics List Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the following steps, you can test if the Monitor Purchase Scheduling Agreement Items (F3143) is running in a correct way.

Prerequisite

You have implemented the Monitor Purchase Scheduling Agreement Items (F3143) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the Monitor Scheduling Agreement Items App | Open the Monitor Purchase Scheduling Agreement Items (F3143) app. | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections. |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Monitor Purchase Scheduling Agreement Items (F3143) app.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown cards is filtered via the corresponding fields in the smart filter bar.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown cards is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page, which can toggle to the Visual Filter view. Choose a part of the donut chart to filter data. | Check if the visual filters work properly.Bar chart: Release Amount by SupplierDonut chart: number of items by Validity StatusDonut chart: number of items by Delivery StatusLine chart: number of items by Next DeliveryDonut chart: Number of Items by Release StatusCheck if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different View on Content Part | Choose Chart and Table View, Chart View, and Table View at the top right of the page. | Check if the table view and chart view are displayed or not. |  |
| 6 | Drilldown by Dimension | Choose Detail (the first icon button) on the icon bar. In the dialog box, choose one dimension to drill to a more detailed level data. | Check if the drill-down function work correctly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type (the seventh icon button) on the icon bar. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |
| 8 | Filter from Chart | Select the Schedule value of a specific supplier from the bar chart. | Check the table result. |  |

### Material Price Variance Analytics List Page

Purpose

You have implemented the Material Price Variance (F3294) app. With the following steps, you can test if Material Price Variance (F3294) is running in a correct way.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Material Price Variance (F3294). | The app is displayed. The page contains two sections: The top section is a filter section and the following section is the data and chart section. |  |
| 3 | Usage of Global Filter | The smart filter bar for the global filter is displayed at the top of the Material Price Variance (F3294) app.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown cards is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page, which can toggle to the Visual Filter view. To filter the data, choose a part of donut. | Check if the visual filters work properly.Bar chart: Net Price by Plant in EURBar chart: Invoice Amount by Supplier in EURBar chart: Number of Changes by Purchase ContractBar chart: Number of Changes by Purchasing Info RecordDonut chart: Released Amount by Document Type in EUR |  |
| 5 | Toggle to a Different View on the Content part | Choose Chart View and Table View at the top right of the page. | Check if the table view and chart view are displayed or not. |  |
| 6 | Drilldown by Dimension | Choose Details on the icon bar. In the dialog box, choose one dimension to drill to a more detailed level data. | Check if the drilldown function works correctly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type on the icon bar. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |

### Embedded Analytics in Supplier Object Page

Purpose

You have supplier master data and procurement documents available. With the following steps, you can test if the Supplier Object page displays embedded analytics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad is displayed. |  |
| 2 | Starting the Global Search | Go to the upper right corner of the SAP Fiori launchpad and open the search for going to Supplier Object Page. | The search field is displayed. |  |
| 3 | Search for One Supplier | Enter a supplier name. | According to the search term, purchasing documents and supplier master data are displayed as search results. |  |
| 4 | Choose One Supplier | Select a supplier category on the left side of the screen and choose one supplier. | The Object page Supplier is displayed |  |
| 5 | Embedded Analytics | Go to the Purchasing Spend, Contract Spend, Purchase Requisition Item Types, and Evaluation Scores tabs. | Check if the charts work correctly. |  |

### Monitor Central Purchase Contract Items Analytics List Page

Purpose

After having implemented the Monitor Central Purchase Contract Items (F3492) app, you can check whether it's running correctly. The following steps explain how to do so.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a CENTRAL_PURCHASER |  |  |
| 2 | Start the App | Open the Monitor Central Purchase Contract Items (F3492) . |  |  |
| 3 | Usage of Global Filter | In the upper part of the screen, you see the smart filter bar for the global filter.You can add or remove fields from the smart filter bar by selecting Filters. A dialog box opens and in this dialog box, you can select or unselect filters as required.The content of the shown cards is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page, which can toggle to the Visual Filter view. Choose a part of the chart to filter data. | Check if the Visual Filters work properly.Bar chart: Release Amount by SupplierDonut chart: number of items by Validity StatusDonut chart: number of items by Delivery StatusLine chart: number of items by Next DeliveryCheck if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different View on Content Part | Choose the Chart and Table View, Chart View, and Table View in the upper right part of the screen. | Check that Table View and Chart View are displayed correctly. |  |
| 6 | Drill Down by Dimension | Choose the View By icon (second icon on the icon bar). In the dialog box that opens, choose one dimension to drill down to a more detailed level. | Check if the drill-down function works correctly. |  |
| 7 | Change Chart Type | Choose the Selected Chart Type icon. In the dialog box that opens, choose one chart type. | Check if changing the chart type works correctly. |  |
| 8 | Show Released Values | Go to the table section and view single contract items. For items whose released value is not equal to 0, purchase orders have been created against that contract item. | Check the historical trend of contract usage. |  |

### Monitor Purchase Order Items Centrally Analytics List Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the following steps, you can test if the Monitor Purchase Order Items Centrally Analytics List Page app is running in a correct way.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a CENTRAL_PURCHASER | Log on system successfully. |  |
| 2 | Access the App | Open Monitor Purchase Order Items Centrally. | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections. |  |
| 3 | Usage of Global Filter | The smart filter bar for the global filter is displayed at the top of the Monitor Purchase Order Items Centrally app.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown cards is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose the Visual Filter on the top-right of page, which can toggle to visual filter view. Choose part of donut to filter data. | Check if the visual filters work properly.Bar chart: Total Value by Material GroupBar chart: Total Value by SupplierBar chart: Total Value by Purch OrganizationDonut chart: Item Count by Next Delivery StatusLine chart: Item Count by Next DeliveryCheck if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different View on Content Part | Choose Chart and Table View and Chart View, and Table View at the top right of the page. | Check if the table view and chart view are displayed or not. |  |
| 6 | Drill Down by Dimension | Choose the first icon button Show Details on the icon bar. On the popup window, choose one dimension to drill to more detail level data. | Check if the drill-down function works correctly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type (the seventh icon button) on the icon bar. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |
| 8 | Filter from Chart | Select the PO value of a specific material group from the bar chart. | Check the table result. |  |

### Overdue Purchase Order Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

With the following steps, you can test if the Overdue Purchase Order Items app is running in a correct way.

Prerequisite

You have implemented the Overdue Purchase Order Items app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the App | Open the Overdue Purchase Order Items app. | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections. |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Overdue Purchase Order Items app.Extra fields can be added to or removed from the smart filter bar via Filters . A dialog box opens and in this dialog box, you can select or unselect filters as required.The content of the shown chart is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Different View on Content Part | Choose Chart View , Table View at the top right of the page. | Check if the list view and chart view are displayed or not. |  |
| 5 | Change Dimension | Choose dropdown box in the top-left in the chart section. In the dropdown box, choose one dimension to get different view | Check if the function works correctly. |  |
| 6 | Change Chart Type | Choose Setting (the sixth icon button) on the icon bar. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |

### Purchase Order Value and Scheduling Agreement Value

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

With the following steps, you can test if the Purchase Order Value and Scheduling Agreement Value app is running in a correct way.

Prerequisite

You have implemented the Purchase Order Value and Scheduling Agreement Value app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Start the App | Open the Purchase Order Value and Scheduling Agree-ment Value app. | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections. |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Purchase Order Value and Scheduling Agreement Value app.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown chart is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered according-ly. |  |
| 4 | Toggle to Different View on Content Part | Choose Chart View , Table View at the top right of the page. | Check if the list view and chart view are displayed or not. Choose dropdown box in the top-left in the chart section. In the dropdown box, choose one dimension to get different view |  |
| 5 | Change Dimension | Choose dropdown box in the top-left in the chart section. In the dropdown box, choose one dimension to get different view | Check if the function works correctly. |  |
| 6 | Change Chart Type | Choose Settings (the sixth icon button) on the icon bar. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |

### Purchasing Spend Dashboard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have already implemented Purchasing Spend Dashboard. Please check if it is running correctly.

The Purchasing Spend Dashboard includes analytic tabs from different management perspectives.

Table 5:

| Tab# | Tab Name |
| --- | --- |
| 1 | Overview |
| 2 | Details |
| 3 | Context |
| 4 | Off Contract Overview |
| 5 | Off Contract Details |

Table 6: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Purchasing Spend Dashboard (F4517). | The overview page is launched successfully and the Purchasing Spend Dashboard is displayed. |  |

#### Story Tabstrip: Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Overview tabstrip

Table 7:

| Chart/Card# | Card Name |
| --- | --- |
| 1 | Purchase Order Net Amount Overview Current Year |
| 2 | Purchase Order Net Amount Overview Previous Year |
| 3 | Purchase Order Net Amount Overview Variance% |
| 4 | Purchase Order Net Amount by Quarter (QoQ) |
| 5 | Purchase Order Net Amount by Trend |
| 6 | Purchase Order Net Amount Analytics(YoY) by Supplier |
| 7 | Purchase Order Net Amount Analytics(YoY) by Material Group |
| 8 | Purchase Order Net Amount Analytics(YoY) by Purchasing Group |
| 9 | Purchase Order Net Amount Analytics(YoY) by Plant |
| 10 | Purchase Order Net Amount Analytics(YoY) by Purchasing Organization |
| 11 | Purchase Order Net Amount Analytics(YoY) per Supplier Country |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip |  | In the story, by default the Overview tab is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_PURCHASEORDERVALUEQUERY .In the Set Variables for C_PURCHASEORDERVALUEQUERY dialog box, enter the prompt values and choose Set.For example:Display Currency*: EURRelative Date Function*: PREVIOUSYEARTODATE | The charts will refresh with data you have selected. |  |

#### Story Tabstrip: Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Details tabstrip

Table 8:

| Chart/Card# | Card Name |
| --- | --- |
| 1 | Summary KPI Number of Supplier in Previous Year |
| 2 | Summary KPI Number of Supplier in Current Year |
| 3 | Summary KPI Number of Purchase Order in Previous Year |
| 4 | Summary KPI Number of Purchase Order in Current Year |
| 5 | Purchase Order Net Amount Details by Material Group |
| 6 | Purchase Order Net Amount Details by Supplier |
| 7 | Purchase Order Net Amount Details by Supplier Country |
| 8 | Purchase Order Net Amount Details by Plant |
| 9 | Purchase Order Net Amount Details by Purchase Organization |
| 10 | Purchase Order Net Amount Details by Purchasing Group |
| 11 | Purchase Order Net Amount by Spend Category |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Details tabstrip. | The Details tab is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_PURCHASEORDERVALUEQUERY .In the Set Variables for C_PURCHASEORDERVALUEQUERY dialog box, enter the prompt values and choose Set.For example:Display Currency*: EURRelative Date Function*: PREVIOUSYEARTODATE | The charts will refresh with data you have selected. |  |
| 3 | Adjust Input Control | In the top, choose several input controls | Charts in this tabstrip will refresh with data you have selected. |  |

#### Story Tabstrip: Context

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Context tabstrip

Table 9:

| Chart/Card# | Card Name |
| --- | --- |
| 1 | Purchase Order Net Amount Overtime Analytics Last 12 Months |
| 2 | Purchase Order Net Amount Overtime Analytics by Cost Center Top 5 |
| 3 | Purchase Order Net Amount Overtime Analytics by Cost Center |
| 4 | Purchase Order Net Amount |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Context tabstrip. | The Context tab is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_PURCHASEORDERVALUEQUERY .In the Set Variables for C_PURCHASEORDERVALUEQUERY dialog box, enter the prompt values and choose Set.For example:Display Currency*: EURRelative Date Function*: PREVIOUSYEARTODATE | The charts will refresh with data you have selected. |  |
| 3 | Adjust Input Control | In the top, choose several input controls | Charts in this tabstrip will refresh with data you have selected. |  |

#### Story Tabstrip: Off Contract Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Off Contract Overview tabstrip

Table 10:

| Chart/Card# | Card Name |
| --- | --- |
| 1 | Off Contract Spend Amount Overview Current Year |
| 2 | Off Contract Spend Amount Overview Previous Year |
| 3 | Off Contract Spend Amount Overview Off Contract Spend in Current Year |
| 4 | Off Contract Spend Amount Overview Off Contract Spend in Previous Year |
| 5 | Off Contract Spend Amount by Quarter |
| 6 | Off Contract Spend Amount by Trend |
| 7 | Off Contract Spend Amount by Supplier |
| 8 | Off Contract Spend Amount by Purchasing group |
| 9 | Off Contract Spend Amount by Plant |
| 10 | Off Contract Spend Amount by Purchasing Organization |
| 11 | Off Contract Spend Amount by Supplier Country |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Off Contract Overview tabstrip. | The Off Contract Overview tab is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_PURGSPENDOFFCONTRACT .In the Set Variables for C_PURGSPENDOFFCONTRACT dialog box, enter the prompt values and choose Set.For example:Display Currency*: EURRelative Date Function*: PREVIOUSYEARTODATE | The charts will refresh with data you have selected. |  |
| 3 | Adjust Input Control | In the top, choose several input controls | Charts in this tabstrip will refresh with data you have selected. |  |

#### Story Tabstrip: Off Contract Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Off Contract Details tabstrip

Table 11:

| Chart/Card# | Card Name |
| --- | --- |
| 1 | Off Contract Spend Amount Overview Current Year by Material Group |
| 2 | Off Contract Spend Amount Overview Current Year by Supplier |
| 3 | Off Contract Spend Amount Overview Current Year by Supplier Country |
| 4 | Off Contract Spend Amount Overview Current Year by Plant |
| 5 | Off Contract Spend Amount Overview Current Year by Purchasing Organization |
| 6 | Off Contract Spend Amount Overview Current Year by Purchasing Group |
| 7 | Off Contract Spend Amount overtime Analytics Amount&Percentage by Purch.Organization |
| 8 | Off Contract Spend Amount overtime Analytics by Purchase Order |
| 9 | Off Contract Spend Amount overtime Analytics Last 12 Months |
| 10 | Off Contract Spend Amount overtime Analytics by Material Group top 5 |
| 11 | Off Contract Spend Amount overtime Analytics by Material Group |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Off Contract Details tabstrip. | The Off Contract Details tab is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_PURGSPENDOFFCONTRACT .In the Set Variables for C_PURGSPENDOFFCONTRACT dialog box, enter the prompt values and choose Set.For example:Display Currency*: EURRelative Date Function*: PREVIOUSYEARTODATE | The charts will refresh with data you have selected. |  |
| 3 | Adjust Input Control | In the top, choose several input controls | Charts in this tabstrip will refresh with data you have selected. |  |

### Supplier Invoice Inbound Automation Rate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

With the following steps, you can test if the Supplier Invoice Inbound Automation Rate app is running in a correct way.

Prerequisite

You have implemented the Supplier Invoice Inbound Automation Rate app.

Table 12: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Supplier Invoice Inbound Automation Rate app. | The page contains two main sections. The top section is the filter section and the lower part contains the data and chart sections.. |  |
| 3 | Use the Global Filter | The smart filter bar for the global filter is displayed at the top of the Supplier Invoice Inbound Automation Rate app.Extra fields can be added to or removed from the smart filter bar via Filters and selecting or deselecting Filters in the dialog box.The content of the shown chart is filtered via the corresponding fields in the smart filter bar.Enter different values in different fields of the global filter. | Check if the content of the corresponding data is filtered accordingly. |  |
| 4 | Toggle to Different View on Content Part | Choose Tabular View and Chart View at the top right of the page. | Check if the list view and chart view are displayed or not. Choose dropdown box in the top-left in the chart section. In the dropdown box, choose one dimension to get different view. |  |
| 5 | Change Dimension | Choose dropdown box in the top-left in the chart section. In the dropdown box, choose one dimension to get different view. | Check if the function works correctly. |  |

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
> Flagged while digesting this document, not verified: Procurement Overview Page Hide Cards steps place the user icon at the top left in Table 1 but at the top right in Table 3 of the same document.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[10-procurement/test-script-vendor-performance-consumer-products-6a6-ae-1154]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1JI_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 79,438 chars in the whole document
