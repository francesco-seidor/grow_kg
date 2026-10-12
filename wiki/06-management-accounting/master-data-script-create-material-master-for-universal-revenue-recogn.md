---
id: 06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn
title: "Master Data Script: Create Material Master for Universal Revenue Recognition (7R8) (7R8_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for creating URR test materials and their sales prices for Sell from Stock, fixed price project and service contract scenarios."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/event-based-revenue-recognition-sell-from-stock]
aliases: [7R8_S4CLD2608_Master_Data_EN_XX]
keywords: [Event-Based Revenue Recognition for Sell from Stock, material master, universal revenue recognition, sell from stock, service products, fixed price projects, service contracts, material prices, business roles, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-533
topic: 06-management-accounting/event-based-revenue-recognition-sell-from-stock
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Material Master for Universal Revenue Recognition (7R8) (7R8_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Sell from Stock** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Material Master for Universal Revenue Recognition (7R8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904872)

[2 Prerequisites 3](#_Toc233904873)

[2.1 System Access 3](#_Toc233904874)

[2.2 Roles 3](#_Toc233904875)

[2.3 Required Organizational Units 3](#_Toc233904876)

[3 Overview Table 4](#_Toc233904877)

[4 Create Material Master Data for Sell from Stock Integration Scenario (SFS) 5](#_Toc233904878)

[4.1 Trading Goods: URR_MAT1_NORM 5](#_Toc233904879)

[4.2 Service Product for One-Time Service: URR_MAT1_SERV 7](#_Toc233904880)

[5 Create Material Master Data for Fixed Price Customer Project Integration Scenario 10](#_Toc233904881)

[5.1 URR_FPPRJ_1 10](#_Toc233904882)

[6 Create Material Master Data for Service Contract Integration Scenario 13](#_Toc233904883)

[6.1 URR_SRVCONT1 13](#_Toc233904884)

[7 Set Prices for Materials 15](#_Toc233904885)

[7.1 Price for Trading Goods for SFS: URR_MAT1_NORM 15](#_Toc233904886)

[7.2 Price for Service Product for One-Time Service: URR_MAT1_SERV 17](#_Toc233904887)

[7.3 Price for Service Contract Material: URR_SRVCONT1 18](#_Toc233904888)

## Purpose

This document provides a guide on how to create material master data records including prices for different Universal Revenue Recognition (URR) integration scenarios: URR integrated with Sell from Stock, URR integrated with Customer Service Projects and URR integrated with Service Contract.

The guide includes the description of data segments that are relevant for the master data to work in an URR process and fields which need to be filled with input values in the data segments. Data segments and fields that are not relevant for the scope are not described in this document although they may appear on the UI.

Material Master Data that is created as described here can be used for URR processes:

| Material Master ID | Description | Usage |
| --- | --- | --- |
| URR_MAT1_NORM | URR Test Material 1 NORM | This material is used in URR Sell from Stock integration scenario |
| URR_MAT2_NORM | URR Test Material 2 NORM | This material is used in URR Sell from Stock integration scenario |
| URR_MAT1_SERV | URR Test Material1 TAD | This material is used in URR Sell from Stock integration scenario |
| URR_FPPRJ_1 | URR Test Material Fix Price Customer Proj. | This material is used in URR Customer Project integration scenario |
| URR_SRVCONT1 | URR Test Material Service Contract | This material is used in URR Service Contract integration scenario |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Organizational Unit to be Used for DE | Organizational Unit to be Used for US |
| --- | --- | --- | --- |
| Create Material | Plant | 1010 (Plant 1 DE) | 1710 (Plant 1 US) |
| Create Material | Sales Organization | 1010 (Dom. Sales Org DE) | 1710 (Dom. Sales Org US) |
| Create Material | Distribution Channel | 10 (Direct Sales) | 10 (Direct Sales) |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Create Material Master Data for Sell from Stock Integration Scenario (SFS)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Trading Goods: URR_MAT1_NORM](#unique_6) [page ] 5 | Master Data Specialist - Product Data | Create Material |  |
| [Service Product for One-Time Service: URR_MAT1_SERV](#unique_7) [page ] 7 | Master Data Specialist - Product Data | Create Material |  |

Table 2: Create Material Master Data for Fixed Price Customer Project Integration Scenario

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [URR_FPPRJ_1](#unique_8) [page ] 10 | Master Data Specialist - Product Data | Create Material |  |

Table 3: Create Material Master Data for Service Contract Integration Scenario

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [URR_SRVCONT1](#unique_9) [page ] 13 | Master Data Specialist - Product Data | Create Material |  |

Table 4: Create Material Master Data for Service Contract Integration Scenario

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Price for Trading Goods for SFS: URR_MAT1_NORM](#unique_10) [page ] 15 | Pricing Specialist | Set Material Prices |  |
| [Price for Service Product for One-Time Service: URR_MAT1_SERV](#unique_11) [page ] 17 | Pricing Specialist | Set Material Prices |  |
| [Price for Service Contract Material: URR_SRVCONT1](#unique_12) [page ] 18 | Pricing Specialist | Set Material Prices |  |

## Create Material Master Data for Sell from Stock Integration Scenario (SFS)

### Trading Goods: URR_MAT1_NORM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose APP Create Material (if APP is not available in the screen you can try searching app Create Material). | The Create Material (Initial Screen) is displayed. |  |
| 3 | Input Material Number and Material Type | On the screen Create Material (Initial Screen) make the following entries:Product Number: URR_MAT1_NORMMaterial Type: Trading GoodsThen choose Continue (Enter). | You have input the material number and material type for the new material master data.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic Data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataAccounting1Then choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1010 (Plant 1 DE)Sales Org.: 1010 (Dom. Sales Org DE)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Basic Data 1 view is displayed. |  |
| 6 | Maintain View: Basic Data 1 | In the Basic data 1 view, maintain the following values:Descr.: URR Test Material1 NORMBase Unit of Measure: PC (Piece)Material Group: L001 (Trading Materials)GenItemGroup: NORM (Standard item)Gross Weight: 1Net Weight: 1Unit of Weight: KGVolume: 1Volume Unit: M3Then press Enter. | Basic data is maintained.After pressing Enter, the Sales: sales org. 1 view is displayed. |  |
| 7 | Maintain View: Sales: sales org. 1 | In the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: X <selected>Tax dataTax classification: 0Then choose Enter. | Sales organizational data 1 is maintained. The Sales: sales org. 2 view is displayed. |  |
| 8 | Maintain View: Sales: sales org. 2 | On the Sales: sales org. 2 view, maintain the following entry:Gen. item cat. Grp: NORM (Standard Item)Item category group: NORM (Standard Item)Then choose Enter. | Sales organizational data 2 is maintained. The Sales: General/Plant view is displayed. |  |
| 9 | Maintain View: Sales: General/Plant | On the Sales: General/Plant view, maintain the following values:Base Unit of Measure: PC (Piece)Gross Weight: 1KGNet Weight: 1Availability Check: NCTrans. Grp: 0001Loading Grp: 0001Profit Center: Y1041Then choose Enter. | General Sales data is maintained. The Accounting 1 view is displayed. |  |
| 10 | Maintain View: Accounting 1 | On the Accounting 1 view, in the Current Period section, make the following entry:Base Unit of Measure: PCValuation Class: 3100Standard Price: 16Per. Unit Price: 16Price Unit: 1Price Control: VFuture Price: emptyThen choose Save. | Accounting data is maintained.The Material Master Data is saved. |  |
| 11 | Create more material master data for testing if required | Create more material master following naming convention URR_MAT*_NORM (eg: URR_MAT2_NORM, URR_MAT3_NORM, etc.) with different standard price. | More test material master data are created. | For CE 2502, URR_MAT1_NORM and URR_MAT2_NORM are delivered as demo data, so the user doesn’t need to create them manually.If more material master data is required for the sell from stock integration scenario testing, please follow the steps of this section to create more materials. |

### Service Product for One-Time Service: URR_MAT1_SERV

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose APP Create Material (if APP is not available in the screen you can try searching app Create Material). | The Create Material (Initial Screen) is displayed. |  |
| 3 | Input Material Number and Material Type | On the Create Material (Initial Screen) make the following entries:Product Number: URR_MAT1_SERVMaterial Type: Service ProductThen choose Continue (Enter). | You have input the material number and material type for the new material master data.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic Data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataAccounting1Then choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1010 (Plant 1 DE)Sales Org.: 1010 (Dom. Sales Org DE)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Basic Data 1 view is displayed. |  |
| 6 | Maintain View: Basic Data 1 | In the Basic data 1 view, maintain the following values:Descr.: URR Test Material1 SERVBase Unit of Measure: H(Hours)Material Group: YBMM01 (Non-Stock Materials with ID)GenItemGroup: SERV (Service)Then press Enter. | Basic data is maintained.After pressing Enter, the Sales: sales org. 1 view is displayed. |  |
| 7 | Maintain View: Sales: sales org. 1 | In the Sales: sales org. 1 view, maintain the following values:General dataDelivering Plant: 1010Cash Discount: X <selected>Tax dataTax classification: 0Then choose Enter. | Sales organizational data 1 is maintained. The Sales: sales org. 2 view is displayed. |  |
| 8 | Maintain View: Sales: sales org. 2 | On the Sales: sales org. 2 view, maintain the following entry:Gen. item cat. Grp: SERV(Service)Item category group: SERV(Service)Then choose Enter. | Sales organizational data 2 is maintained. The Sales: General/Plant view is displayed. |  |
| 9 | Maintain View: Sales: General/Plant | On the Sales: General/Plant view, maintain the following values:Profit Center: YB600Then choose Enter. | General Sales data is maintained. The Accounting 1 view is displayed. |  |
| 10 | Maintain View: Accounting 1 | On the Accounting 1 view, in the Current Period section, make the following entry:Valuation Class: 3300Standard Price: 20Price Unit: 1Then choose Save. | Accounting data is maintained.The Material Master Data is saved. |  |

## Create Material Master Data for Fixed Price Customer Project Integration Scenario

### URR_FPPRJ_1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose APP Create Material (if APP is not available in the screen you can try searching app Create Material). | The Create Material (Initial Screen) is displayed. |  |
| 3 | Input Material Number and Material Type | On the Create Material (Initial Screen) make the following entries:Product Number: URR_FPPRJ_1Material Type: Service ProductThen choose Continue (Enter). | You have input the material number and material type for the new material master data.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic Data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataAccounting1Then choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1010 (Plant 1 DE)Sales Org.: 1010 (Dom. Sales Org DE)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Basic Data 1 view is displayed. |  |
| 6 | Maintain View: Basic Data 1 | In the Basic data 1 view, maintain the following values:Descr.: URR Test Material1 SERVBase Unit of Measure: AU(Activity unit)Material Group: P000 (Contract Type)GenItemGroup: PSFP (Fixed Price Item)Then press Enter. | Basic data is maintained.After pressing Enter, the Sales: sales org. 1 view is displayed. |  |
| 7 | Maintain View: Sales: sales org. 1 | In the Sales: sales org. 1 view, maintain the following values:General dataDelivering Plant: 1010Cash Discount: X <selected>Tax dataTax classification: 0Then choose Enter. | Sales organizational data 1 is maintained. The Sales: sales org. 2 view is displayed. |  |
| 8 | Maintain View: Sales: sales org. 2 | On the Sales: sales org. 2 view, maintain the following entry:Gen. item cat. Grp: PSFP (Fixed Price Item)Acct Assmt Grp Mat: Y1 (Fixed Price)Item category group: PSFP (Fixed Price Item)Then choose Enter. | Sales organizational data 2 is maintained. The Sales: General/Plant view is displayed. |  |
| 9 | Maintain View: Sales: General/Plant | On the Sales: General/Plant view, maintain the following values:Profit Center: YB101Then choose Enter. | General Sales data is maintained. The Accounting 1 view is displayed. |  |
| 10 | Maintain View: Accounting 1 | On the Accounting 1 view, in the Current Period section, make the following entry:Valuation Class: 3300Standard Price: 30Price Unit: 1Then choose Save. | Accounting data is maintained.The Material Master Data is saved. |  |
| 11 | Create more material master data for testing if required | Create more material master with naming convention URR_FPPRJ* (eg: URR_FPPRJ3, URR_FPPRJ4, etc.) with different standard price if it’s required. | More test material master data are created. |  |

## Create Material Master Data for Service Contract Integration Scenario

### URR_SRVCONT1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose APP Create Material (if APP is not available in the screen you can try searching app Create Material). | The Create Material (Initial Screen) is displayed. |  |
| 3 | Input Material Number and Material Type | On the Create Material (Initial Screen) make the following entries:Product Number: URR_SRVCON1Material Type: Service ProductThen choose Continue (Enter). | You have input the material number and material type for the new material master data.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic Data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataPurchasingThen choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1010 (Plant 1 DE)Sales Org.: 1010 (Dom. Sales Org DE)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Basic Data 1 view is displayed. |  |
| 6 | Maintain View: Basic Data 1 | In the Basic data 1 view, maintain the following values:Descr.: URR Test Material 1 Service ContractBase Unit of Measure: AU(Activity unit)Material Group: P001 (Services)GenItemGroup: SCNP (Serv. Contract Prod.)Then press Enter. | Basic data is maintained.After pressing Enter, the Sales: sales org. 1 view is displayed. |  |
| 7 | Maintain View: Sales: sales org. 1 | In the Sales: sales org. 1 view, maintain the following values:General dataBase Unit of Measure: AU(Activity unit)Material Group: P001 (ServicesThen choose Enter. | Sales organizational data 1 is maintained. The Sales: sales org. 2 view is displayed. |  |
| 8 | Maintain View: Sales: sales org. 2 | On the Sales: sales org. 2 view, maintain the following entry:Gen. item cat. Grp SCNP (Serv. Contract Prod.)Then choose Enter. | Sales organizational data 2 is maintained. The Sales: General/Plant view is displayed. |  |
| 9 | Maintain View: Sales: General/Plant | On the Sales: General/Plant view, maintain the following values:Base Unit of Measure: AU (Activity unit)Then choose Enter. | General Sales data is maintained. The Accounting 1 view is displayed. |  |
| 10 | Maintain View: Purchasing | On the Purchasing view, make the following entry:Base Unit of Measure: AU (Activity unit)Material Group: P001 (Services)Then choose Save. | Accounting data is maintained.The Material Master Data is saved. |  |

## Set Prices for Materials

### Price for Trading Goods for SFS: URR_MAT1_NORM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales (VK12). | The Change Condition Records view is displayed. |  |
| 3 | Pricing Condition Type | In the Change Condition Records view, enter the following information:Condition Type: PPR0Then click Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key Combination view, choose the Material with release status option.Then click Choose. | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, maintain the following information:Sales Organization: 1010 (Dom. Sales Org DE)Distribution Channel: 10 (Direct Sales)Material: URR_MAT1_NORMValid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Change Price Condition | In the Change Price Condition (PPR0): Overview view, maintain the following data for material:Material: URR_MAT1_NORMAmount: for example, 25.00Unit: EURValid From: <Date> for example, today’s dateClick Enter. | Price conditions has been maintained. |  |
| 7 | Save | Choose Save. | The prices have been defined. |  |
| 8 | Go Back and Access App Again | In the Change Condition Records view, enter the following information:Condition Type: PSAMThen choose Enter. | The Key Combination view is displayed. |  |
| 9 | Key Combination | In the Key Combination view, choose the Material with release status option.Then choose Enter. | The Change Price (PSAM): Selection view is displayed. |  |
| 10 | Selection | In the Change Price (PSAM): Selection view, maintain the following information:Sales Organization: 1010 (Dom. Sales Org DE)Distribution Channel: 10 (Direct Sales)Material: URR_MAT1_NORMValid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PSAM): Overview view is displayed. |  |
| 11 | Change Price Condition | In the Change Price Condition (PSAM): Overview view, maintain the following data for material:Material: URR_MAT1_NORMAmount: for example, 35.00Unit: EURValid From: <Date> for example, today’s dateChoose Enter. | Price conditions has been maintained. |  |
| 12 | Save | Choose Save. | The price has been defined. |  |

### Price for Service Product for One-Time Service: URR_MAT1_SERV

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales (VK12). | The Change Condition Records view is displayed. |  |
| 3 | Pricing Condition Type | In the Change Condition Records view, enter the following information:Condition Type: PPR0Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose the Material with release status option.Then choose Choose (Enter). | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, maintain the following information:Sales Organization: 1010 (Dom. Sales Org DE)Distribution Channel: 10 (Direct Sales)Material: URR_MAT1_SERVValid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PPR0): Overview view, maintain the following data for material:Material: URR_MAT1_SERVAmount: for example, 25.00Unit: EURValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for service products SRV_01 has been maintained. |  |
| 7 | Save | Choose Save. | The prices for the service products have been defined. |  |
| 8 | Go Back and Access App Again | In the Change Condition Records view, enter the following information:Condition Type: PSAMThen choose Enter. |  |  |
| 9 | Key Combination | In the Key Combination view, choose the Material with release status option.Then choose Enter. | The Change Price (PSAM): Selection view is displayed. |  |
| 10 | Selection | In the Change Price (PSAM): Selection view, maintain the following information:Sales Organization: 1010 (Dom. Sales Org DE)Distribution Channel: 10 (Direct Sales)Material: URR_MAT1_SERVValid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PSAM): Overview view is displayed. |  |
| 11 | Change price condition | In the Change Price Condition (PSAM): Overview view, maintain the following data for material:Material: URR_MAT1_SERVAmount: for example, 35.00Unit: EURValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for service products SRV_01 has been maintained. |  |
| 12 | Save | Choose Save. | The price has been defined. |  |

### Price for Service Contract Material: URR_SRVCONT1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales (VK12). | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PSI1Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose Material .Then choose Enter. | The Change Price (PSI1): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PSI1): Selection view, maintain the following information:Sales Organization: 1010 (Dom. Sales Org DE)Distribution Channel: 10 (Direct Sales)Material: URR_SRVCONT1Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PSI1): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PSI1): Overview view, maintain the following data:Material: URR_SRVCONT1Amount: for example, 90.00Unit: for example, EURValid From: <Date> for example, today’s dateChoose Enter. | Price conditions is maintained. |  |
| 7 | Save | Choose Save. | The price has been defined. |  |

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
> Flagged while digesting this document, not verified: Service contract step 3 uses product number URR_SRVCON1 while the rest of the document uses URR_SRVCONT1

> [!warning] Conflict
> Flagged while digesting this document, not verified: URR_FPPRJ_1 description given as 'URR Test Material1 SERV', same as URR_MAT1_SERV, though the overview table names it 'URR Test Material Fix Price Customer Proj.'

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/7r8-537]]
- related-to :: [[06-management-accounting/master-data-script-item-master-for-universal-revenue-recognition-7r8-j]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-mestre-de-materiais-para-realizacao-de-re]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-maestro-de-materiales-para-el-reconocim]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 30,816 chars in the whole document
