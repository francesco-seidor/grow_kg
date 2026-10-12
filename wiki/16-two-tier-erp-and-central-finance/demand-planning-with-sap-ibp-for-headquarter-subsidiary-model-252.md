---
id: 16-two-tier-erp-and-central-finance/demand-planning-with-sap-ibp-for-headquarter-subsidiary-model-252
title: Demand Planning with SAP IBP for Headquarter-Subsidiary model (S4CLD2608_2T_DP_IBP)
description: "Two-Tier ERP customer guide: SAP IBP demand planning for HQ-subsidiary model with scope items, integration setup, roles and test script ending in PIR transfer."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/supply-and-demand-planning]
aliases: [S4CLD2608_2T_DP_IBP]
keywords: [Two-Tier MRP Visibility and Demand Planning, demand planning, two-tier erp, sap ibp integration, statistical forecasting, planned independent requirements, historical data cleansing, scope items, communication arrangements, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Supply Chain Planning/S4CLD2608_2T_DP_IBP.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-252
topic: 16-two-tier-erp-and-central-finance/supply-and-demand-planning
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Demand Planning with SAP IBP for Headquarter-Subsidiary model (S4CLD2608_2T_DP_IBP)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Supply Chain Planning/S4CLD2608_2T_DP_IBP.docx`, extracted with `mammoth`. Grouped under **Two-Tier MRP Visibility and Demand Planning** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| S/4HANA CloudPublic Edition June 2026English |  |
|  | Two-Tier ERP: Demand Planning with SAP IBP for Headquarter - Subsidiary model |
|  | Customer Guide |

Copyright

© 2021 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 15.07.2025 | Initial version of document |

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, push buttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Contents

[**Demand Planning with SAP IBP for Headquarter-Subsidiary model** 6](#_Toc203548392)

[Purpose 6](#_Toc203548393)

[Value Proposition 6](#_Toc203548394)

[Business Requirements 6](#_Toc203548395)

[Two-Tier Solution 6](#_Toc203548396)

[Business Process Details 6](#_Toc203548397)

[Scope Item 6](#_Toc203548398)

[Prerequisites 7](#_Toc203548399)

[Process Flow 8](#_Toc203548400)

[Technical Requirements 9](#_Toc203548401)

[Integration Requirements by using CI/iflows 9](#_Toc203548402)

[Integration Requirements by using Cloud Integration for Data Services (CI-DS) 12](#_Toc203548403)

[Test Script 13](#_Toc203548404)

[Prerequisites 13](#_Toc203548405)

[5.2 Role at Subsidiary 14](#_Toc203548406)

[5.3 Role at Headquarters 14](#_Toc203548407)

[5.4 Role at IBP 15](#_Toc203548408)

[5.5 Master Data, Organizational Data, and Other Data 15](#_Toc203548409)

[5.6 Overview Table 17](#_Toc203548410)

[5.7 Test Procedures 17](#_Toc203548411)

[5.7.1 Integrate historical sales orders at subsidiary location 18](#_Toc203548412)

[5.7.2 Integrate historical sales orders at headquarter location 18](#_Toc203548413)

[5.7.3 Check data integration in SAP IBP 18](#_Toc203548414)

[5.7.4 Cleanse Historical Data 18](#_Toc203548415)

[5.7.5 Run Statistical forecasting 19](#_Toc203548416)

[5.7.6 Analyse and Adjust forecasting results 20](#_Toc203548417)

[5.7. 7 Transfer Planned Independent Requirements 21](#_Toc203548418)

## **Demand Planning with SAP IBP for Headquarter-Subsidiary model**

## Purpose

This document will provide a detailed process of a demand planning scenario with SAP IBP in a Two-Tier ERP headquarters-subsidiary model using process flow, technical requirements, and testing procedures. The solution is designed for business processes where the headquarter (HQ) with its multiple sales subsidiaries is responsible for overall demand consolidation, while the regional subsidiaries handle local sales forecasts based on market conditions.

## Value Proposition

### Business Requirements

This scenario is particularly beneficial for organizations operating in a two-tier structure, where the subsidiary interacts directly with customers by receiving demand and subsequently shares it with the Headquarters.

The use case for this could be with industries such as consumer automotive parts or consumer products where the headquarter maintains planning integrity, while subsidiaries influence local demand variations.

### Two-Tier Solution

Through a Two-Tier ERP solution, seamless orchestration of process between headquarters, subsidiary and SAP IBP can be done along with below integration points.

1. All the master data is maintained at the headquarters.
2. Sales orders for a material from headquarters and subsidiary locations is integrated with SAP IBP.
3. SAP IBP receives the sales orders from both locations.
4. Statistical forecast is generated at the product level in SAP IBP on the combined sales orders.
5. Final statistical forecast is converted into consensus demand which is transferred back at headquarters as planned independent requirements (PIR)

## Business Process Details

### Scope Item

| Scope Item | Business Condition |
| --- | --- |
| BD9 | Sell from stock |
| BJ5 | Make to Stock Production – Discrete Manufacturing |
| 78P | IBP for demand – demand forecast for SAP S/4HANA Cloud, public edition |

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Subsidiary should be running on SAP S/4HANA Cloud Public Edition system and Headquarters should run on SAP S/4HANA cloud Private Edition, SAP S/4HANA On Premise or ECC
- Activate the Scope BD9 at the Subsidiary’s SAP S/4HANA Cloud Public Edition system
- Activate the scope item 78P at the IBP Tenant for Public cloud
- Activate the scope item BJ5 in the headquarter
- If headquarter is involved in the local sales, then activate the scope item BD9 at headquarter as well
- The Headquarters and Subsidiary should have business partner , product master data aligned for this business process to work.
- Latest IBP excel add-in to be installed in the client system.
- Communication Scenario to be set for Cloud Integration with IBP in S4 HANA Public cloud Edition
- SAP_COM_0008 - Product Integration
- SAP_COM_0009 - Business Partner, Customer, and Supplier Integration
- SAP_COM_0104 - Production Planning Integration
- Communication Scenario to be set for Cloud Integrator Data Services with IBP in S4 HANA cloud private Edition
- SAP_COM_0931 – Planning - Integration Suit – Cloud Integration

### Process Flow

<!-- image omitted: unnamed -->

**Tier1**

-
    - Master data for material and location is maintained at headquarters.
    - Master data and sales order history from headquarter for the relevant materials are sent to SAP IBP via CI-DS (Cloud integrator data services)

**Tier2**

-
    - Sales order history from subsidiaries for the same material are sent to SAP IBP via cloud integrator

**SAP IBP**

-
    - Master data from headquarters is received in SAP IBP at corresponding product, location and customer master.
    - Receives sales orders from both headquarters and subsidiary as Actual sales quantity in SAP IBP
    - Pre-processing algorithm is run on sales orders history to cleanse the data and missing values are adjusted.
    - Statistical forecast algorithm is run on the adjusted actual sale quantities at product level (combining sales orders of the product at both locations)
    - The statistical forecast generated at product level is transferred to headquarter as planned independent requirement (PIR)

**Tier 1**

-
    - Headquarter receives Planned Independent Requirements (PIR) from SAP IBP for processing/production.

The following integration points are depicted in the process flow diagram:

1. Transfer of master and transactional data from headquarters to SAP IBP via cloud integration for data services (CI-DS)
2. Transfer of sales order data from subsidiary to SAP IBP via Cloud interface (CI)
3. Statistical forecast is transformed into PIRs and sent back to headquarters via CI-DS

## Technical Requirements

This section covers the process of setting up integration of SAP S/4HANA Cloud Public Edition system and SAP S/4HANA cloud Private Edition system with SAP IBP covering the main prerequisites such as Communication arrangements, Cloud connector and API’s (Application programming interfaces) that are required to enable the direct integration between the systems.

### Integration Requirements by using Cloud Integrator

**Create communication System in SAP IBP:**

<!-- image omitted: unnamed -->

**<!-- image omitted: unnamed -->**

**<!-- image omitted: unnamed -->**

Create Communication Arrangement

<!-- image omitted: A screenshot of a computer

AI-generated content may be incorrect. -->

<!-- image omitted: A screenshot of a computer

AI-generated content may be incorrect. -->

<!-- image omitted: A screenshot of a computer

AI-generated content may be incorrect. -->

<!-- image omitted: A screenshot of a computer

AI-generated content may be incorrect. -->

For detailed CI setup, you can refer to [Set- up instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/IBP/Library/Configuration/S4C_IBP2502_Set-Up_EN_XX.docx) for SAP Best practice scope item [78P](https://me.sap.com/processnavigator/SolS/EARL_SolS-034/2502/SolP/78P?region=DE).

### Integration Requirements by using Cloud Integration for Data Services (CI-DS)

**Create communication System in SAP IBP:**

In the **Communication Systems application** in SAP IBP, maintain the connection for CIDS by providing the host name and outbound communication details.

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

For detailed CI setup, you can refer to [Set- up instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/IBP/Library/Configuration/TSP_IBP2502_Set-Up_EN_XX.docx) for SAP Best practice scope item [11V](https://me.sap.com/processnavigator/SolS/EARL_SolS-034/2502/SolP/11V?region=DE).

## Test Script

### Prerequisites

The test scenario can be built in the following Two-tier system landscape:

| System | Details |
| --- | --- |
| SAP S/4HANA cloud private edition - Headquarters | SAP S/4HANA cloud private edition / On- Premise system /ECC |
| SAP S/4HANA Cloud Public Edition system - Subsidiary | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Integrated Business Planning (IBP) | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### 5.2 Role at Subsidiary

Assign the following business roles to your individual test users at Subsidiary.

Note The following roles are provided as example roles from SAP. You can use these as templates to create your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK |  |
| Sales Manager | SAP_BR_SALES_MANAGER |  |
| Administrator | SAP_BR_ADMINISTRATOR |  |

Assign the following business roles to your individual test users.

### 5.3 Role at Headquarters

The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK |  |
| Sales Manager | SAP_BR_SALES_MANAGER |  |
| Production Planner | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Administrator | SAP_BR_ADMINISTRATOR |  |

For more information about business roles, refer to Assigning business roles to a user in the [Administration Guide for the Implementation of SAP S/4HANA](https://help.sap.com/viewer/S4HANA1709_AdminGuide).

#### 5.4 Role at IBP

The following business roles to be assigned in SAP IBP as a planner

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Demand Planner (IBP) | SAP_BR_DEMAND_PLANNER_IBP |  |
| Configuration Expert (IBP) | SAP_BR_CONFIG_EXPERT_IBP |  |

### 5.5 Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data were created in your S/4 HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, Services, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values and enables you to go through the process steps of this scope item.

Note Additional Master Data (Default Values)

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP system to find out which other material master data exists.

Note Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data.

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Master Data maintained in Subsidiary on SAP S4 HANA public system

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading |  |
| Plant | 1010 | Plants at subsidiary |  |
| Sales organization | 1010 | Sales Organization |  |
| Distribution Channel | 10 | Distribution Channel |  |
| Division | 00 | Division |  |

Use your own master data or the following sample data to go through the test procedure. Below is the Master data maintained at headquarters in SAP S/4HANA Cloud Private Edition.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading |  |
| Plant | 10101710 |  |  |
| Sales organization | 1010 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Company Code | 1010 | Company Code 1010 |  |

## 5.6 Overview Table

| Test Step # | Test Step Name | Business Role | Expected Result |
| --- | --- | --- | --- |
| 1 | Integrate historical sales orders at subsidiary location to SAP IBP | SAP Integration Suite administrator. | Sales orders pushed from subsidiary via CI to SAP IBP |
| 2 | Integrate historical sales orders at headquarter location to SAP IBP |  | Sales orders pushed from headquarters via CI DS to SAP IBP |
| 3 | Check data integration in SAP IBP | Demand Planner | Master data and transactional records successfully received from headquarters and subsidiary |
| 4. | Cleanse Historical Data | Demand Planner | For any missing value and/or any outlier detected, data is overwritten for key figure Adj. Total Actuals Qty. with cleansed data values |
| 5 | Run Statistical forecasting | Demand Planner | Final statistical forecast is generated based on given parameters. |
| 6 | Analyse and adjust forecasting results | Demand Planner | The results after adjustment is reflected in the KF Demand Planning Qty Final |
| 7 | Transfer Planned Independent Requirements | Demand Planner | Demand has been pushed from IBP and transformed into PIRs in headquarters |

### 5.7 Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### 5.7.1 Integrate historical sales orders at subsidiary location

The sales orders for the material at the subsidiary location are sent to SAP IBP as transactional data via cloud interface (CI)

### 5.7.2 Integrate historical sales orders at headquarter location

The sales orders for the material at headquarters location are sent to SAP IBP as transactional data via cloud integration for data services (CIDS)

### 5.7.3 Check data integration in SAP IBP

Using the *Data Integration jobs* application in SAP IBP, check for the inbound master and transactional data using the task name from CI DS and iflow name from CI. Subsequently, planning view can also be used to load the data using Microsoft excel add-in for IBP. Sales orders are received from subsidiary as actuals quantity (ACTUALSALESQTY) and Sales orders from headquarters (ACTUALSALESQTY1) in SAP IBP.

A new key-figure is created in SAP IBP (TOTALACTUALSQTY) to consolidate sales order values from headquarters and subsidiary for the material which is then used to create the forecasted demand.

### 5.7.4 Cleanse Historical Data

The detailed steps to create a statistical forecast model are listed in the below table:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Unified Planning Business Role | The Fiori Launchpad with access to the Manage Forecast Models application is displayed. |  |
| 2 | Open Manage Forecast Models application | Select the Create model option on the page. Select Planning area | New Forecast Model page opens |  |
| 3 | Create new forecast model | Under General Tab, give Model name, and time phases details. | Details are saved |  |
| 4 | Cleanse Historical data | Under Pre-processing steps tab, select “+” button to select “*Substitute missing values*” option from Available Algorithms.Input for Algorithm: TOTALACTUALSQTYSave result in:ADJTOTALACTUALSQTYChoose Save. | Details are savedFor any missing value and/or any outlier detected, data is overwritten for key figure Adj. Total Actuals Qty. with cleansed data values. |  |
| 5 | Run Pre-processing algorithm | Open planning view template “2T Demand planning” using SAP IBP excel add-inNavigate to tab “Data cleansing” | The following key figures are displayed with data:Total Actuals QtyAdj. Total Actuals QtyThe Adj. Total Actuals Qty KF contains cleansed data. (Missing values are substituted with mean) |  |

### 5.7.5 Run Statistical forecasting

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Unified Planning Business Role | The Fiori Launchpad with access to the Manage Forecast Models application is displayed. |  |
| 2 | Open Manage Forecast Models application | Select the Create model option on the page. Select Planning area | New Forecast Model page opens |  |
| 3 | Create new forecast model | Under General Tab, give Model name, and time phases details. | Details are saved |  |
| 4 | Create Forecasting steps | Give following details:Main Input: ADJTOTALACTUALSQTYSave Forecast in:STATISTICALFORECASTQTYChoosing forecasting model based on MAPEChoose Save. | Details are saved. |  |
| 5 | Run Forecasting model | Navigate to Application jobs application form FIORI launchpad and schedule a new job using the template “Basic statistical forecast” | The job is executed. Analyse the results. |  |

### 5.7.6 Analyse and Adjust forecasting results

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Display results | Open planning view template “2T Demand planning” using SAP IBP excel add-in.Navigate to tab “Forecast adjustments” | The following key figures are displayed with data. If no data was adjusted yet, both key figures contain the same data:Demand Planning QtyDemand Planning Qty FinalIf no forecast adjustments have been made so far, the following key figure is displayed with no data:Demand Planning Qty Adj. |  |
| 2. | Adjust forecasted value | Adjust KF Demand Planning Qty Adj. if required.Click Save | In case of adjustments, Demand Planning Qty Final shows the same value as key figure Demand Planning Qty. Adj. |  |

### 5.7. 7 Transfer Planned Independent Requirements

Using the Application jobs application in SAP IBP, schedule the copy operator job for Consensus Demand to transfer the PIRs via CIDS.

In the SAP S/4HANA Private Cloud system, check the planned independent requirements that were integrated from SAP IBP to Headquarters.

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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/material-requirement-planning-visibility-in-two-tier-erp-232]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Supply Chain Planning/S4CLD2608_2T_DP_IBP.docx` — full document · extracted with `mammoth` · 23,260 chars in the whole document
