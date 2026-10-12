---
id: 13-quality-ehs-and-compliance/test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana
title: "Test Script: Chemical Compliance in the Value Chain (31J_AE) - SAP S/4HANA Cloud Public Edition 2608 (31J_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 31J_AE: compliance marketability checks on sales orders, DG classification, market and customer assessments, with prerequisites."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/chemical-compliance-and-marketability]
aliases: [31J_S4CLD2608_BPD_EN_AE]
keywords: [Chemical Compliance and Product Marketability, compliance marketability check, sales order blocking, product market assessment, marketability assessment release, customer compliance check, dangerous goods classification, unpackaged products, compliance purposes, product master compliance relevance]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31J_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-893
topic: 13-quality-ehs-and-compliance/chemical-compliance-and-marketability
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Chemical Compliance in the Value Chain (31J_AE) - SAP S/4HANA Cloud Public Edition 2608 (31J_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31J_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Chemical Compliance and Product Marketability** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 28-08-26 |
| --- | --- |
|  | Chemical Compliance in the Value Chain (31J_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc239509346)

[2 Prerequisites 4](#_Toc239509347)

[2.1 System Access 4](#_Toc239509348)

[2.2 Roles 4](#_Toc239509349)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc239509350)

[2.4 Business Conditions 6](#_Toc239509351)

[2.5 Preliminary Steps 6](#_Toc239509352)

[2.5.1 Create Product Master Records Set as Compliance Relevant 7](#_Toc239509353)

[2.5.2 Create Stock 10](#_Toc239509354)

[2.5.3 Create Compliance Purposes 12](#_Toc239509355)

[2.5.4 Create Unpackaged Products, Link to Product Master, and Assign Compliance Purpose 14](#_Toc239509356)

[3 Overview Table 19](#_Toc239509357)

[4 Test Procedures 21](#_Toc239509358)

[4.1 Create Sales Order with Negatively Assessed Marketability 21](#_Toc239509359)

[4.1.1 Create Sales Order for a Product with Compliance Relevance Indicated 21](#_Toc239509360)

[4.1.2 Check Status of Sales Order (Optional) 23](#_Toc239509361)

[4.1.3 Process Request from Logistics and Assess Markets for a Product as Not Allowed 25](#_Toc239509362)

[4.2 Create Sales Order with Positively Assessed Marketability 26](#_Toc239509363)

[4.2.1 Create Sales Order for a Product with Compliance Relevance Indicated 26](#_Toc239509364)

[4.2.2 Classify Unpackaged Product as No Dangerous Goods 28](#_Toc239509365)

[4.2.3 Process Compliance Request from Logistics and Assess Marketability Requirements 30](#_Toc239509366)

[4.2.4 Check Status of Sales Order 33](#_Toc239509367)

[4.3 Customer Compliance Check During Sales Orders 35](#_Toc239509368)

[4.3.1 Create Sales Order for a Product with Compliance Relevance Indicated 35](#_Toc239509369)

[4.3.2 Classify Unpackaged Product as No Dangerous Goods 37](#_Toc239509370)

[4.3.3 Process Compliance Request from Logistics, Set Market to *Allowed*, and Set Risk Level 39](#_Toc239509371)

[4.3.4 Process Compliance Request from Logistics and Release Customer Assessment 41](#_Toc239509372)

[4.3.5 Check Status of Sales Order 43](#_Toc239509373)

## Purpose

This scope item describes the compliance marketability check in sales order processing.

Overview

This scope item manages the compliance marketability checks in sales order processes and during outbound delivery.

For every product included in a sales order or sales quotation that is defined as relevant for compliance, it must be verified if the sale into the specified country/region and to the specified customer is allowed. The result of the marketability check may block the follow-on documents or initiate a request for the product stewardship department.

If selling is possible only under restrictions, the internal sales representative can initiate an approval process. The product stewardship department processes the approval request and approves or rejects the sale.

The sales documents are also blocked if selling isn't possible or hasn't yet been assessed. A request is created for the product stewardship department if the assessment for a country/region and customer hasn't yet been done.

For any compliance-relevant product included in a sales order or sales quotation, it must be verified if selling to the country/region and for the customer is allowed. The result of the marketability check may block the follow-on documents or initiate a request for the product stewardship department.

If selling is possible only under restrictions, the internal sales representative can initiate an approval process. The product stewardship department processes the approval request and approves or rejects the sale.

The sales documents are also blocked if selling isn't possible or hasn't been assessed yet. If the assessment for a country/region and customer hasn't been done yet, a request is created for the product stewardship department .

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Dangerous Goods Specialist - Product Compliance | SAP_BR_DG_SPLST_PCL | Dangerous Goods | SAP_BR_DG_SPLST_PCL |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents products, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sold-to Party (Customer) | 33100003 | Domestic UAE Customer 3 | For sales order of your product copied from FGPC01 |
| Ship-to Party (Customer) | 33100003 | Domestic UAE Customer 3 | For sales order of your product copied from FGPC01 |
| Payer (Customer) | 33100003 | Domestic UAE Customer 3 | For sales order of your product copied from FGPC01 |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Product | FGPC01 | Product Number: FGPC01Product Type: FERTProduct Description: Product Compliance Finished GoodCompliance Relevant: Yes | To be copied to create your own products |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | The scope item of this document is an extension of the BD9 scope item. Therefore, the BD9 must be implemented and tested beforehand. |

### Preliminary Steps

To run through this scope item, you must first carry out the preliminary steps:

1. [Create Product Master Records Set as Compliance Relevant](#unique_8) [page ] 7
2. [Create Stock](#unique_9) [page ] 10
3. [Create Compliance Purposes](#unique_10) [page ] 12
4. [Create Unpackaged Products, Link to Product Master, and Assign Compliance Purpose](#unique_11) [page ] 14

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

#### Create Product Master Records Set as Compliance Relevant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you need three unique product master records for semifinished goods, as well as three unique product master records for finished goods. You create these records in the following steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Data (SAP_BR_PRODMASTER_SPECIALIST). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Product Master Data (F1602). | The app opens. |  |
| 3 | Search for Product | Enter the product FGPC01 in the Search field. | The list of products is narrowed down to the ones that match the fuzzy search. |  |
| 4 | Select Product | Select the checkbox of the entry for Product Compliance Finished Good (FGPC01) | The row is highlighted in blue. |  |
| 5 | Copy Product | Choose Copy. | The Select Organizational Data to Copy dialog appears for product Product Compliance Finished Good (FGPC01) with Plants and Distribution Chains preselected. |  |
| 6 | Select Organizational Data to Copy | Remove the selection for plants and distribution chains, and choose OK. | The Create Master Data Record dialog is displayed. |  |
| 7 | Create Record | Add the product number and description:Product Number: SG<XXXXX>01(replace <XXXXX> with your name)Note The number has to start with SG because of the standard number range.Product Type: Open the value help and choose HALB (Semifinished Product)Product Group: Open the value help and choose L003 (Semi-Finished Goods).Description: Semi <your name> 01Then choose OK. | The dialog closes, and the Product screen is displayed for your product. |  |
| 8 | Check Compliance Relevance | Choose the Product Compliance tab. In the Compliance Relevant dropdown list, check if Yes is already selected. If not, select Yes. | In the Product Compliance section, the compliance relevance is set to Yes. |  |
| 9 | Add Valuation Area | In the Valuation Areas section, choose Create. | The Valuation Area screen opens. |  |
| 10 | Select Valuation Area and Valuation Class | Open the value help for Valuation Area, and select 3310. Then open the value help for Valuation Class, and select 7900 (Semifinished Goods). Then choose Apply. | On the Product screen, the valuation area 3310 with valuation class 7900 has been added to the Valuation Areas table.Note If an extra empty row appears in the Valuation Areas table, delete it. |  |
| 11 | Choose Create | Choose Create. If any duplicate warnings appear, choose Create again in the Validation Messages dialog. | A message indicates that the master data record has been created. |  |
| 12 | Copy Product | On the Product screen for your new product, choose Copy. | The Select Organizational Data to Copy dialog appears for your recently created product, with Plants and Distribution Chains preselected. |  |
| 13 | Select Organizational Data to Copy | Keep the selections for plants and distribution chains, and choose OK. | The Create Master Data Record dialog is displayed. |  |
| 14 | Create Record | Add the product number and description:Product Number: SG<XXXXX>02(replace <XXXXX> with your name)Description: Semi <your name> 02Then choose OK. | The Product screen is displayed for your product. |  |
| 15 | Create Product and Copy Again | Repeat steps 11–13. | The Create Master Data Record dialog is displayed. |  |
| 16 | Create Record | Add the product number and description:Product Number: SG<XXXXX>03(replace <XXXXX> with your name)Description: Semi <your name> 03Then choose OK. | The Product screen is displayed for your product. |  |
| 17 | Choose Create | Choose the Create button and close any duplicate warnings by choosing Create again in the Validation Messages dialog. | A message indicates that the master data record has been created.You've now created three master data records for semifinished goods, copied and adapted from Product Compliance Finished Good (FGPC01). |  |
| 18 | Navigate Back | Navigate back until you're on the Manage Product Master Data screen. | The Manage Product Master Data screen is displayed. |  |
| 19 | Search for Product | Enter the product FGPC01 in the Search field. | The list of products is narrowed down to the ones that match the fuzzy search. |  |
| 20 | Select Product | Select the checkbox of the entry for Product Compliance Finished Good (FGPC01) | The row is highlighted in blue. |  |
| 21 | Copy Product | Choose Copy. | The Select Organizational Data to Copy dialog appears for product Product Compliance Finished Good (FGPC01) with Plants and Distribution Chains preselected. |  |
| 22 | Select Organizational Data to Copy | Keep the selection for plants and distribution chains and choose OK. | The Create Master Data Record dialog is displayed. |  |
| 23 | Create Record | Add the product number and description:Product Number: FG<XXXXX>01(replace <XXXXX> with your name)Note The number has to start with FG because of the standard number range.Description: Finished <your name> 01Then choose OK. | The Product screen is displayed for your product. |  |
| 24 | Choose Create | Choose the Create button and close any duplicate warnings by choosing Create again in the Validation Messages dialog. | A message indicates that the master data record has been created. |  |
| 25 | Copy Product | On the Product screen for your new product, choose Copy. | The Select Organizational Data to Copy dialog appears for your recently created product, with Plants and Distribution Chains preselected. |  |
| 26 | Select Organizational Data to Copy | Keep the selection for plants and distribution chains, and choose OK. | The Create Master Data Record dialog is displayed. |  |
| 27 | Create Record | Add the product number and description:Product Number: FG<XXXXX>02(replace <XXXXX> with your name)Description: Finished <your name> 02Then choose OK. | The Product screen is displayed for your product. |  |
| 28 | Create Product and Copy Again | Repeat steps 24–26. | The Create Master Data Record dialog is displayed. |  |
| 29 | Create Record | Add the product number and description:Product Number: FG<XXXXX>03(replace <XXXXX> with your name)Description: Finished <your name> 03Then choose OK. | The Product screen is displayed for your product. |  |
| 30 | Choose Create | Choose the Create button and close any duplicate warnings by choosing Create again in the Validation Messages dialog. | A message indicates that the master data record has been created.You've now created three finished goods, copied and adapted from Product Compliance Finished Good (FGPC01). |  |

#### Create Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, the materials must be available in stock. You fill the inventory with stock in the following steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Warehouse Clerk (SAP_BR_WAREHOUSE_CLERK). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Post Goods Movement (MIGO). | The app opens. |  |
| 3 | Input Movement Type | Make the following entry and press Enter:First dropdown list: Goods ReceiptSecond dropdown list: Other | The Goods Receipt Other screen is displayed. |  |
| 4 | Input on the Goods Receipt Other Screen: Material Tab | On the Goods Receipt Other screen: Material tab, make the following entry and press Enter:Material: FG<your name>01 | The first Material field is filled with the description Finished <your name> 01.The second Material field is filled with FG<your name>01. |  |
| 5 | Input on the Goods Receipt Other Screen: Quantity Tab | On the Goods Receipt Other screen: Quantity tab, make the following entry and press Enter:Qty in Unit of Entry: 99999Unit of Entry: BT | The system sets the correct thousands separator for the number (for example, 99999 changes to 99,999). |  |
| 6 | Input on the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other screen: Where tab, make the following entries and press Enter:Movement Type: 561 - Receipt per initial entry of stock balances into unrestricted usePlant: 3310Storage Location: 331A | The movement type code remains unchanged, and the plant and storage location codes are replaced with their descriptions:Movement Type: 561Plant: Plant 1 AEStorage Location: Std. storage 1 |  |
| 7 | Save Your Entries | Choose Post. | A message confirms that the material document has been posted.The Goods Receipt Other screen is still displayed with the following values selected:First dropdown list: Goods ReceiptSecond dropdown list: Other |  |
| 8 | Input on the Goods Receipt Other Screen: Material Tab | On the Goods Receipt Other screen: Material tab, make the following entry and press Enter:Material: FG<your name>02 | The first Material field is filled with the description Finished <your name> 02.The second Material field is filled with FG<your name>02. |  |
| 9 | Input and Save Your Entries | Repeat steps 5–7. | A message confirms that the material document has been posted.The Goods Receipt Other screen is still displayed with the following values selected:First dropdown list: Goods ReceiptSecond dropdown list: Other |  |
| 10 | Input on the Goods Receipt Other Screen: Material Tab | On the Goods Receipt Other screen: Material tab, make the following entry and press Enter:Material: FG<your name>03 | The first Material field is filled with the description Finished <your name> 03.The second Material field is filled with FG<your name>03. |  |
| 11 | Input and Save Your Entries | Repeat steps 5–7. | A message confirms that the material document has been posted.The Goods Receipt Other screen is still displayed with the following values selected:First dropdown list: Goods ReceiptSecond dropdown list: OtherYou have now added stock for all three of your finished goods. |  |

#### Create Compliance Purposes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you have to create the compliance purposes that you assign to unpackaged products. You create compliance purposes in the following steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Compliance Purposes (F2632). | The app opens. |  |
| 3 | Create Compliance Purpose | Choose Create. | The Compliance Purpose screen is displayed. |  |
| 4 | Create Compliance Purpose Name | Choose Create in the Compliance Purpose Names section. | A row with empty Language and Name fields appears. |  |
| 5 | Enter Language | Enter the language code for any language (for example, EN for English) in the Language field, and then select the language from the dropdown list that appears. | The language code appears in the Language field. |  |
| 6 | Enter Compliance Purpose Name | Enter <your name> PMA-SLC, DG in the Name field. | The name <your name> PMA-SLC, DG appears in the Name field. |  |
| 7 | Create Compliance Purpose with Name | Choose Create. | The compliance purpose is created, and the compliance purpose name is displayed at the top under the Compliance Purpose screen title. |  |
| 8 | Edit Compliance Purpose | Choose Edit. | The app is in edit mode. |  |
| 9 | Add Compliance Requirements | In the Compliance Requirements section, choose Add. | The Assign Compliance Requirements dialog opens. |  |
| 10 | Select Compliance Requirements | Search for and select the following compliance requirements, and then choose Select:World-SIN List StatusUNRTDGADRADN49 CFRIATA-DGRRIDTDGIMDG-Code | The added compliance requirements are displayed in the Compliance Requirements section. |  |
| 11 | Save Compliance Purpose | Choose Save. | The compliance purpose is saved, and the app switches to display mode. |  |
| 12 | Activate Compliance Purpose | Choose Activate. | A success message indicates that the compliance purpose was activated. |  |
| 13 | Copy Compliance Purpose | Choose Copy. | The Compliance Purpose screen is displayed with the data copied from the compliance purpose you created previously. This action enables you to create a second compliance purpose with similar data. |  |
| 14 | Adapt Compliance Purpose Name | In the Compliance Purpose Names section, delete the Duplicate: prefix and change the name to <your name> PMA-CCC, DG. | The Name field is adapted. |  |
| 15 | Delete Assignment to EU-REACH SVHC Status | In the Compliance Requirements section, select the compliance requirement World-SIN List Status. Then choose Delete. In the warning dialog that appears, choose Delete. | A message appears that the assignment to the compliance requirement has been deleted. |  |
| 16 | Add Compliance Requirement | In the Compliance Requirements section, choose Add. | The Assign Compliance Requirements dialog opens. |  |
| 17 | Select World-First Order Check | Search for and select the compliance requirement World-First Order Check, and then choose Select. After the dialog has closed, choose Create on the Compliance Purpose screen. | The added compliance requirement is displayed in the Compliance Requirements section. The compliance purpose is created, and the app switches to display mode. |  |
| 18 | Activate Compliance Purpose | Choose Activate. | A success message indicates that the compliance purpose was activated.You have now created and activated two compliance purposes:<Your name> PMA-SLC, DG: Compliance purpose for substance list check within product marketability, and dangerous goods<Your name> PMA-CCC, DG: Compliance purpose for customer compliance check within product marketability, and dangerous goods |  |

#### Create Unpackaged Products, Link to Product Master, and Assign Compliance Purpose

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you need compliance views of the unpackaged products. In the following steps, you create the unpackaged products, link them to the relevant product master records, and assign the relevant compliance purposes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The app opens. |  |
| 3 | Create Unpackaged Product | Choose Create. | The New Product dialog is displayed. |  |
| 4 | Enter Header Data for New Product and Save | In the New Product dialog, proceed as follows:Define an internal name for your unpackaged product: <your name> UP 1.In the Product Categorization field, select Mixture.Deselect the Safety Data Sheet Required checkbox.The rest stays default.Choose Save. | The dialog closes, and the Unpackaged Product - Basic Compliance Data screen opens and displays the internal name that you defined. |  |
| 5 | Switch to Edit Mode | Choose Edit. | The app is in edit mode. |  |
| 6 | Assign Related Product in Product Master | In the Related Products in Product Master section, choose the value help for the first empty field in the Product in Product Master column. | The Select: Product in Product Master dialog opens. |  |
| 7 | Search for Semifinished Good | Enter SG<your name>01 in the search field, and then press Enter. | The list of products is narrowed down to the ones that match the fuzzy search. |  |
| 8 | Select Semifinished Good | Choose the row for the semifinished good that you searched for. | The dialog closes, and SG<your name>01 appears in the row. |  |
| 9 | Save the Unpackaged Product | On the Unpackaged Product - Basic Compliance Data screen, choose Save. | The unpackaged product is saved, and the app reverts to display mode. The product name and product number of the newly assigned semifinished good are displayed at the top. |  |
| 10 | Add Packaged Product | In the Related Compliance Views table in the Packaged Products section, choose Create. | The Create Packaged Product dialog opens. |  |
| 11 | Enter Product | Enter FG<your name>01, and select it from the dropdown list that appears. Then choose Save. | The Create Packaged Product dialog closes, and the packaged product is added to the Related Compliance Views table. |  |
| 12 | Navigate Back | Navigate back. | The Manage Basic Compliance Data - Unpackaged Products screen is displayed. |  |
| 13 | Create Unpackaged Product | Choose Create. | The New Product dialog is displayed. |  |
| 14 | Enter Header Data for New Product and Save | In the New Product dialog, proceed as follows:Define an internal name for your unpackaged product: <your name> UP 1.In the Product Categorization field, select Mixture.Deselect the Safety Data Sheet Required checkbox.The rest stays default.Choose Save. | The dialog closes, and the Unpackaged Product - Basic Compliance Data screen opens and displays the internal name that you defined. |  |
| 15 | Switch to Edit Mode | Choose Edit. | The app in edit mode. |  |
| 16 | Assign Related Product in Product Master | In the Related Products in Product Master section, choose the value help for the first empty field in the Product in Product Master column. | The Select: Product in Product Master dialog opens. |  |
| 17 | Search for Semifinished Good | Enter SG<your name>02 in the search field, and then press Enter. | The list of products is narrowed down to the ones that match the fuzzy search. |  |
| 18 | Select Semifinished Good | Select the row for the semifinished good that you searched for. | The dialog closes, and SG<your name>02 appears in the row. |  |
| 19 | Save the Unpackaged Product | Choose Save. | The unpackaged product is saved, and the app reverts to display mode. The product name and product number of the newly assigned semifinished good are displayed at the top. |  |
| 20 | Add Packaged Product | In the Related Compliance Views table in the Assigned Products section, choose Create. | The Create Packaged Product dialog opens. |  |
| 21 | Enter Product | Enter FG<your name>02, and select it from the dropdown list that appears. Then choose Save. | The Create Packaged Product dialog closes, and the packaged product is added to the Related Compliance Views table. |  |
| 22 | Edit Unpackaged Product | Choose Edit. | The app is in edit mode. |  |
| 23 | Select Assigned Compliance Purpose | In the Application, Uses, Markets and Purposes section, Assigned Compliance Purposes table, select Product Default Compliance Purpose. | The row is highlighted in blue. |  |
| 24 | Remove Default Compliance Purpose | Choose Remove, and confirm the removal in the dialog that appears. | The default compliance purpose is removed. |  |
| 25 | Add Compliance Purpose | For the Assigned Compliance Purposes table, choose Add. | The Assign Compliance Purposes dialog is displayed. |  |
| 26 | Choose Your Compliance Purpose for Product Marketability | Search for <your name> PMA-SLC, DG. Select it, and then choose OK. | The compliance purpose is added to the Assigned Compliance Purposes table. |  |
| 27 | Save Unpackaged Product | Choose Save. | A success message confirms that the unpackaged product has been saved. |  |
| 28 | Navigate Back | Navigate back. | The Manage Basic Compliance Data - Unpackaged Products (F2641) screen is displayed. |  |
| 29 | Create Unpackaged Product | Choose Create. | The New Product dialog is displayed. |  |
| 30 | Enter Header Data for New Product and Save | In the New Product dialog, proceed as follows:Define an internal name for your unpackaged product: <your name> UP 3.In the Product Categorization field, select Mixture.Deselect the Safety Data Sheet Required checkbox.The rest stays default.Choose Save. | The dialog closes, and the Unpackaged Product - Basic Compliance Data screen opens and displays the internal name that you defined. |  |
| 31 | Switch to Edit Mode | Choose Edit. | The app is in edit mode. |  |
| 32 | Assign Related Product in Product Master | In the Related Products in Product Master section, choose the value help for the first empty field in the Product in Product Master column. | The Select: Product in Product Master dialog opens. |  |
| 33 | Search for Semifinished Good | Enter SG<your name>03 in the search field, and then press Enter. | The list of products is narrowed down to the ones that match the fuzzy search. |  |
| 34 | Select Semifinished Good | Select the row for the semifinished good that you searched for. | The dialog closes, and SG<your name>03 appears in the row. |  |
| 35 | Save the Unpackaged Product | Choose Save. | The unpackaged product is saved, and the app reverts to display mode. The product name and product number of the newly assigned semifinished good are displayed at the top. |  |
| 36 | Add Packaged Product | In the Related Compliance Views table in the Assigned Products section, choose Create. | The Create Packaged Product dialog opens. |  |
| 37 | Enter Product | Enter FG<your name>03, and select it from the dropdown list that appears. Then choose Save. | The Create Packaged Product dialog closes, and the packaged product is added to the Related Compliance Views table. |  |
| 38 | Edit Unpackaged Product | Choose Edit. | The app is in edit mode. |  |
| 39 | Select Assigned Compliance Purpose | In the Application, Uses, Markets and Purposes section, Assigned Compliance Purposes table, select Product Default Compliance Purpose. | The row is highlighted in blue. |  |
| 40 | Remove Default Compliance Purpose | Choose Remove, and confirm the removal in the dialog that appears. | The default compliance purpose is removed. |  |
| 41 | Add Compliance Purpose | For the Assigned Compliance Purposes table, choose the Add button. | The Assign Compliance Purposes dialog is displayed. |  |
| 42 | Choose Your Compliance Purpose for Customer Compliance Check | Search for <your name> PMA-CCC, DG. Select it, and then choose OK. | The compliance purpose is added to the Assigned Compliance Purposes table. |  |
| 43 | Save Unpackaged Product | Choose Save. | A success message confirms that the unpackaged product has been saved.You've created three unpackaged products with your own semifinished and finished goods assigned. For two of the products, you've removed the default compliance purpose and replaced it with one of your own compliance purposes. |  |

## Overview Table

This scope item consists of several process steps provided in the table.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order for a Product with Compliance Relevance Indicated](#unique_13) [page ] 21 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order is created. |
| [Check Status of Sales Order (Optional)](#unique_14) [page ] 23 | Internal Sales Representative | Sales Order Fulfillment - Analyze and Resolve Issues (F0029A) | You can check marketability issues with the sales order. You are alerted that there are no safety data sheets and no compliance assessment available for the requested product. |
| [Process Request from Logistics and Assess Markets for a Product as Not Allowed](#unique_15) [page ] 25 | Product Stewardship Specialist - Product Compliance | Process Requests from Logistics - For Dangerous Goods (F3342) | The sales order is blocked. |
| [Create Sales Order for a Product with Compliance Relevance Indicated](#unique_16) [page ] 26 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order is created. |
| [Classify Unpackaged Product as No Dangerous Goods](#unique_17) [page ] 28 | Dangerous Goods Specialist - Product Compliance | My Unpackaged Dangerous Goods (F3643) | The unpackaged product is classified as no dangerous goods. |
| [Process Compliance Request from Logistics and Assess Marketability Requirements](#unique_18) [page ] 30 | Product Stewardship Specialist - Product Compliance | Process Requests from Logistics - For Dangerous Goods (F3342) | The compliance request is processed and the marketability assessments are released as compliant. |
| [Check Status of Sales Order](#unique_19) [page ] 33 | Internal Sales Representative | Sales Order Fulfillment - Analyze and Resolve Issues (F0029A) | The check shows that the product is approved for selling to the country/region of the customer. |
| [Create Sales Order for a Product with Compliance Relevance Indicated](#unique_20) [page ] 35 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order is created. |
| [Classify Unpackaged Product as No Dangerous Goods](#unique_21) [page ] 37 | Product Stewardship Specialist - Product Compliance | My Unpackaged Dangerous Goods (F3643) | The unpackaged product is classified as no dangerous goods. |
| [Process Compliance Request from Logistics, Set Market to Allowed, and Set Risk Level](#unique_22) [page ] 39 | Product Stewardship Specialist - Product Compliance | Process Requests from Logistics - For Dangerous Goods (F3342) | A high risk level is set for the unpackaged product. |
| [Process Compliance Request from Logistics and Release Customer Assessment](#unique_23) [page ] 41 | Product Stewardship Specialist - Product Compliance | Process Requests from Logistics - For Dangerous Goods (F3342) | The compliance request is processed and the customer assessment is released as compliant. |
| [Check Status of Sales Order](#unique_24) [page ] 43 | Internal Sales Representative | Manage Sales Orders (F1873) | The check shows that the product is approved for selling to the country/region of the customer. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Order with Negatively Assessed Marketability

#### Create Sales Order for a Product with Compliance Relevance Indicated

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative creates a sales order for a product with customer first-order check enabled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Create Sales Order | Choose Create > Create Sales Order - VA01 . | The Create Sales Documents screen is displayed. |  |
| 4 | Enter the Order | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order: Overview screen is displayed. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:In the header:Sold-To Party: 33100003Ship-To Party: 33100003Cust. Reference: <Any customer reference text>Cust. Ref. Date: <Today's date>In the Sales tab:Deliver.Plant: 3310 | The Create Standard Order: Overview screen is still displayed. |  |
| 6 | Enter Order Item | On the Create Standard Order: Overview screen, in the All Items section, make the following entries for the first sales order item, and then press Enter:Material: FG<your name>01Order Quantity: 1Un (Sales Unit): BTPlnt (Plant): 3310Double-click in the row for the sales order item. On the Country/Region tab, if available, enter 00 as the tax code. If this tab not available, still stay on the same screen, as it is needed for the next step. | The item is added to the standard order and the Create Standard Order: Item Data screen is displayed. |  |
| 7 | Item Data – Mandatory Pricing Condition | On the Conditions tab of the Create Standard Order: Item Data screen, add a row to the Pricing Elements table:CnTy: PPR0Amount: <Any numerical amount>Crcy: <Any currency code>Press Enter.Choose Save.Navigate back to Create Standard Order: Overview. | The pricing error is resolved and the condition type is added. |  |
| 8 | Save Document | Choose the Save button.Make a note of the sales order number: __________. | The order is saved and the order number is shown in the footer.A log opens in which two messages are displayed, indicating the following:No dangerous goods assessment exists, and a request has been initiated.No marketability assessment exists, and a request has been initiated. |  |

#### Check Status of Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative analyzes sales documents based on the given issues types. Marketability issues are visualized in the Delivery Block in Sales Orders and Delivery Issue in Sales Orders issue types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Under Internal Sales > Internal Sales Overview > Insights , open Sales Order Fulfillment - Analyze and Resolve Issues (F0029A). | The Sales Order Fulfillment Issues screen is displayed. |  |
| 3 | Search for Marketability Issues | Switch the header filter view by choosing the <!-- image omitted: unnamed -->(Compact Filter) icon.Choose Adapt Filters. In the dialog, in the Add Filter dropdown, select the Product Marketability Status filter attribute.In the newly added Product Marketability Status dropdown, select the following values:Blocked – Not ApprovedBlocked – Not MarketablePartially Blocked – Not ApprovedPartially Blocked – Not MarketableIn the Adapt Filters dialog, choose OK. | The dialog closes, and the Sales Order Fulfillment Issues screen is displayed. |  |
| 4 | Apply Filter | In the header, choose Go. | The Sales Documents with Issues table is filtered for any sales documents with blocked or partially blocked marketability. |  |
| 5 | Select the Status Value for Display | Choose the <!-- image omitted: unnamed -->(Settings) icon for the Sales Documents with Issues table (not the Sales Documents with Issues diagram).In the View Settings dialog, use the search field to search for Product Marketability Status. Select Product Marketability Status if it's not already selected, and then choose OK. | The table shows the marketability header status for the sales documents. |  |
| 6 | Select the Sales Order | In the main search field on the Sales Order Fulfillment Issues screen, enter the sales order number for the product FG<your name>01 from the test procedure [Create Sales Order for a Product with Compliance Relevance Indicated](#unique_13) [page ] 21. | The sales order appears in the Sales Documents with Issues table. |  |
| 7 | Navigate to Tracking of Sales Order Details | Choose the <!-- image omitted: unnamed -->(Details) icon for the row of the sales document with Delivery Block in Sales Orders in the Issue column and Blocked – Not Marketable or Partially Blocked in the Product Marketability Status column.Note If you can't see the Product Marketability Status column, scroll right.If more than one entry fulfills these criteria, choose the first entry. | The Track Sales Order Details screen is displayed. |  |
| 8 | View Item Processing Details | Under the Fulfillment Standard Order <Sales Order Number> heading, choose the Items tab. | The Item Processing Details table is displayed. |  |
| 9 | Navigate to Compliance Information | In the Item Processing Details table, choose the hyperlink for the product.If a link to Display Compliance Information for Products exists, choose it. Otherwise, choose More Links, then select the checkbox for Display Compliance Information for Products, then choose OK, and then choose the Display Compliance Information for Products link. | You navigate to the Compliance Information - For Products (F3226) app, Product Marketability tab, Sales View. |  |
| 10 | Check the Product Marketability Tab, Sales View | Check the map in the Product Marketability tab, Sales View. | The country/region of the customer 33100003 (Domestic US Customer 3) is highlighted in orange. |  |
| 11 | View Compliance Status | Choose the highlighted country/region. | The <Country/Region> - Selling dialog opens. The marketability status is Requested. |  |
| 12 | Check the Product Marketability Tab, Production View | Close the dialog, and then choose Production View in the Product Marketability tab. | No countries/regions are highlighted on the map. |  |
| 13 | Check the Safety Data Sheets Tab | Choose the Safety Data Sheets tab. | An information message indicates that no safety data sheets are required for this product. |  |
| 14 | Check the Dangerous Goods Tab | Choose the Dangerous Goods tab. | The International Transport table indicates that transport via aircraft cargo, aircraft passenger, and deep water are forbidden. |  |

#### Process Request from Logistics and Assess Markets for a Product as Not Allowed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Product Compliance section, under Basic, choose the Process Requests from Logistics (F3342) tile. | The monitor screen for unprocessed requests is displayed. |  |
| 3 | Search for Request | Enter FG<your name>01 in the Search field and then press Enter. | The list is filtered and only the requests that match the fuzzy search are displayed. |  |
| 4 | Select Request | Choose the request with the following attributes:Business Process / Area: Sell In / <Country/Region>Initiating Process: Extend Business ProcessSource of Request: Sales Order | The request for opens in a new pane with the heading Finished <your name> 01. |  |
| 5 | Edit Assessments | In the Finished <your name> 01 pane, in the Edit Market Assessments section, choose Edit Assessments. | The Market Assessment screen opens. |  |
| 6 | Switch to Edit Mode | Choose Edit. | The app is in edit mode. |  |
| 7 | Open Dialog | In the Assessment for Countries/Regions, for the Product Market Assessments table, choose Add. | The Assign Countries/Regions dialog opens. |  |
| 8 | Add Country/Region | Select the country/region of 33100003 (Domestic UAE Customer 3). Then choose OK. | The country/region of 33100003 (Domestic UAE Customer 3) is added to the Product Market Assessment table. |  |
| 9 | Open Market Assessment for Country/Region | Choose the row of the newly added country/region. | A new pane opens with the details of the country/region. |  |
| 10 | Set Assessment Status | Under Assessment for One Country/Region > Generally Valid > Compliance per Business Process , set the value of the Assessment Status for Sales field to Not Allowed. Then choose Apply | The pane for the country/region closes. In the Product Market Assessments table, Not Allowed appears in the Sell In column. |  |
| 11 | Save the Assessment | Choose Save. | The Market Assessment screen switches to display mode.Due to the negative assessment, the sales order is blocked. |  |

### Create Sales Order with Positively Assessed Marketability

#### Create Sales Order for a Product with Compliance Relevance Indicated

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative creates a sales order for a product with customer first-order check enabled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Create Sales Order | Choose Create > Create Sales Order - VA01 . | The Create Sales Documents screen is displayed. |  |
| 4 | Enter the Order | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order: Overview screen is displayed. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:In the header:Sold-To Party: 33100003Ship-To Party: 33100003Cust. Reference: <Any customer reference text>Cust. Ref. Date: <Today's date>In the Sales tab:Deliver.Plant: 3310 | The Create Standard Order: Overview screen is still displayed. |  |
| 6 | Enter Order Item | On the Create Standard Order: Overview screen, All Items section, make the following entries for the first sales order item, and then press Enter:Material: FG<your name>02Order Quantity: 1Un (Sales Unit): BTPlnt: 3310Double-click in the row for the sales order item. On the Country/Region tab, if available, enter 00 as the tax code. If this tab is not available, still stay on the same screen, as it's needed for the next step. | The item is added to the standard order and the Create Standard Order: Item Data screen is displayed. |  |
| 7 | Item Data – Mandatory Pricing Condition | On the Conditions tab of the Create Standard Order: Item Data screen, add a row:CnTy: PPR0Amount: <Any numerical amount>Crcy: <Any currency code>Press Enter.Choose Save.Navigate back to Create Standard Order: Overview. | The pricing error is resolved, and the condition type is added. |  |
| 8 | Save Document | Choose the Save button.Make a note of the sales order number: __________. | The order is saved and the order number is shown in the footer.A log opens in which two messages are displayed, indicating the following:No dangerous goods assessment exists, and a request has been initiated.Restrictions apply, and an approval is requested. |  |

#### Classify Unpackaged Product as No Dangerous Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dangerous Goods Specialist - Product Compliance sees that there are unpackaged products that have to be classified according to the dangerous goods regulations. The Dangerous Goods Specialist - Product Compliance classifies an unpackaged product according to the assigned regulations as no dangerous goods and allows the transport for all the regulations.

If the business feature Dangerous Goods Integration into Value Chain is activated, the minimum data maintenance for safety data sheets is required to remove the sales order blocking status. You can activate this business feature via scope item 5OJ.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Dangerous Goods Specialist - Product Compliance (SAP_BR_DG_SPLST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Dangerous Goods > Classification section, open the My Unpackaged Dangerous Goods (F3643) app. | The My Unpackaged Dangerous Goods (F3643) screen is displayed and shows a list of unpackaged products on the For My Responsible Unit tab page. |  |
| 3 | Search Unpackaged Dangerous Good | Enter SG<your name>02 in the Search field. | The Unpackaged Products list is filtered to the products that match the fuzzy search. |  |
| 4 | Select Unpackaged Dangerous Good | Choose the row for the product that you searched for. | The Classify Unpackaged Dangerous Good (F3642) app opens and displays the released analytical composition and a list with all assigned dangerous goods regulations. |  |
| 5 | Select Regulation | In the Basic Classification section, choose the row for the ADR regulation (for example, ADR 2025). | The Classify Dangerous Good (F4465) app opens and displays the Dangerous Goods - Classification Details screen to edit the classification data for the selected regulation (for example, ADR 2025).Note that the app ID (for example, F4465 for ADR) varies depending on the selected regulation. |  |
| 6 | Classify Unpackaged Product as Dangerous Goods | Choose Edit and, in the Classification section, select Classified As: No Dangerous Goods. | The Dangerous Good - Classification Details screen displays Classified As: No Dangerous Goods. |  |
| 7 | Set Transport Permission | In the Transport Permission section, select Transport Permission: Allowed. | Transport of the dangerous good is allowed according to the ADR regulation. |  |
| 8 | Save the Classification | After checking the classification data, choose Save. | A message indicates that the classification data is saved. |  |
| 9 | Navigate Back | Navigate back to the Classify Unpackaged Dangerous Good (F3642) app. | The Classify Unpackaged Dangerous Good (F3642) app opens and displays for the ADR regulation that the product is classified as no dangerous goods and that the transport is allowed. |  |
| 10 | Classify Product According to the Other Regulations | Select the checkbox for the ADR regulation and choose Apply Classification to Other Regulations.In the dialog, select all regulations by selecting the checkbox in the Regulation column. Then choose Apply Classification. | The dialog closes, and the system applies the classification you did according to ADR to all other selected regulations and saves the classifications as a draft version. |  |
| 11 | Release Classifications | In the Regulations table, select all regulations in progress except the UNRTDG regulation or regulations by selecting the checkbox in the Regulation column and then deselecting the checkbox for the UNRTDG regulation or regulations. Then choose Release.In the Release dialog, choose Save Drafts and Release. | The dialog closes, and the released classifications are displayed in the Released section of the Regulations table.Note that if you release all regulations, the product is no longer displayed in the My Unpackaged Dangerous Goods (F3643) app. |  |

#### Process Compliance Request from Logistics and Assess Marketability Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance sees a new request from logistics in the worklist for a new product that is compliance relevant. The Product Stewardship Specialist - Product Compliance accepts the request by completing the marketability assessment for the country/region of the production plant, which unblocks the sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the Product Stewardship Specialist - Product Compliance role is displayed. |  |
| 2 | Access App | In the Product Compliance section, under Basic, choose the Process Requests from Logistics (F3342) tile. | The Process Requests from Logistics screen is displayed and shows the list of unprocessed requests. |  |
| 3 | Search and Select Request | Enter FG<your name>02 in the Search field and then press Enter. | The list is filtered for the entries that match the fuzzy search. |  |
| 4 | Navigate to the Request Object Page | Choose the line for the unprocessed request for the product that you searched for, Sell In / <country/region of Domestic UAE Customer 3> in the Business Process / Area column, Extend Business Process in the Initiating Process column, and Sales Order in the Source of Request column to navigate to the Compliance Request from Logistics screen. | The Compliance Request from Logistics screen is displayed. |  |
| 5 | Edit Market Assessments | Check that the following information is displayed:Under Request Details:Requester: Example InternalSalesRepSales Order: The sales order number from the sales order you created in a previous stepCustomer: Domestic UAE Customer 3Product in Product Master: <your name> Finished 02 (FG<your name>02)Under Request Steps > View Basic Compliance Data :Compliance View Type: Packaged ProductPackagedCompliance View - Packaged: FG<your name>03Logistics Roles: Sold, TransportedUnpackagedCompliance View - Unpackaged: <your name> UP 2Logistics Roles: Sold, Transported, ProducedApplications: –View Compliance Purpose Assignments > Assigned Compliance Purposes > Compliance Purpose > > : <your name> PMA-SLC, DGOnce you've verified this information, choose Edit Assessments under Edit Market Assessments. | The Market Assessment screen opens. On this screen, the Related Packaged Products table contains one entry with Finished <your name> 02 in the Product Name column and FG<your name>05 in the Product in Product Master column. |  |
| 8 | Switch to Edit Mode | Choose Edit. | The app is in edit mode. |  |
| 8 | Add Country/Region | For the Product Market Assessments table under Assessment for Countries/Regions, choose Add. | The Assign Countries/Regions dialog opens. |  |
| 9 | Select Country/Region | Select the country/region from the sales order, which appeared in the Area field of the compliance request. Then choose OK. | The country/region is added to the Product Market Assessments table. |  |
| 10 | Open Country/Region Assessment | Choose the row for the newly added country/region. | The details for the country/region assessment open in a new pane. |  |
| 11 | Choose Compliance Requirement Version | Choose the assessment of the first compliance requirement version in the Compliance Requirement Versions table that hasn't been released yet. The compliance requirement version is the latest version of World SIN List Status for which no released marketability assessment exists. | The Marketability Assessment screen is displayed. |  |
| 12 | Switch to Edit Mode | On the Marketability Assessment screen, choose Edit. | The app is in edit mode. |  |
| 13 | Set Marketability Status | On the Marketability Assessment screen, under Compliance Details, set the marketability status to Compliant. | The Compliant value is displayed in the Marketability Status field. |  |
| 14 | Save Your Assessment | Choose Save. | A success message indicates that the compliance assessment has been saved. |  |
| 15 | Release Marketability Assessment | Choose Release. | A success message indicates that the compliance assessment has been released. |  |
| 16 | Navigate Back | Navigate back. | On the details pane of the Assess Markets - For Products app, in the Compliance Requirement Versions table, Compliant appears in the Marketability Status column, and today's date appears in the Released On column for the newly assessed compliance requirement version. |  |
| 17 | Assess remaining compliance requirement versions | For any remaining compliance requirement versions that haven't been assessed yet, repeat steps 11–16. | All compliance requirement versions are released and compliant. |  |
| 18 | Set Compliance for Sales | On the details pane of the Assess Markets - For Products app, in the Assessment for One Country/Region section, under Generally Valid, open the dropdown list for the Assessment Status for Sales field and select Allowed. Then choose Apply. | The details pane closes. In the Assessment for Countries/Regionssection, in the Product Market Assessments table, Allowed appears in the Sell In column. |  |
| 19 | Save the Assessment | On the Market Assessment screen, choose Save. | Your entries are saved, and the app is in display mode.The sales order is no longer blocked. |  |

#### Check Status of Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative analyzes sales documents based on the given issues types. Marketability issues are visualized in the Delivery Block in Sales Orders and Delivery Issue in Sales Orders issue types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Under Internal Sales > Insights , open Sales Order Fulfillment - Analyze and Resolve Issues (F0029A). | The analytic list page for orders with issues is displayed. |  |
| 3 | Search for Marketability Issues | Switch the header filter view by choosing the <!-- image omitted: unnamed -->(Compact Filter) icon.Choose Adapt Filters. Select the Product Marketability Status filter attribute, and then choose OK.For the Product Marketability Status filter, select the value OK – Approved.Confirm the new filter settings by choosing Go. | The list is filtered for any sales documents with approved marketability. |  |
| 4 | Select the Status Value for Display | Choose the <!-- image omitted: unnamed -->(Settings) icon for the Sales Documents with Issues table (not the Sales Documents with Issues diagram).Use the search field to search for Product Marketability Status. Select Product Marketability Status if it's not already selected, and then choose OK. | The table shows the marketability header status for the sales documents. |  |
| 5 | Select the Sales Order | Use the main search field on the Sales Order Fulfillment Issues screen to search for the sales order from the test procedure [Create Sales Order for a Product with Compliance Relevance Indicated](#unique_16) [page ] 26. This sales order is for the product FG<your name>02. | The sales order appears in the Sales Documents with Issues table. |  |
| 6 | Navigate to Tracking of Sales Order Details | Choose the <!-- image omitted: unnamed -->(Details) icon for the row of the sales document with Delivery Block in Sales Orders in the Issue column and OK – Approved in the Product Marketability Status column.Note If you can't see the column, scroll right.If more than one entry fulfills these criteria, choose the first entry. | The Track Sales Order Details screen is displayed. |  |
| 7 | View Item Processing Details | Under the Fulfillment Standard Order <Sales Order Number> heading, choose the Items tab. | The Item Processing Details table is displayed. |  |
| 8 | Navigate to Compliance Information | In the Item Processing Details table, choose the hyperlink for the product.If a link to Display Compliance Information for Products exists, choose it. Otherwise, choose More Links, then select the checkbox for Display Compliance Information for Products, then choose OK, and then choose the Display Compliance Information for Products link. | You navigate to the Compliance Information - For Products (F3226) app, Product Marketability tab, Sales View. |  |
| 9 | Check the Product Marketability Tab, Sales View | Check the map in the Product Marketability tab, Sales View. | The country/region of the customer 33100003 (Domestic US Customer 3) is highlighted in green. |  |
| 10 | View Compliance Status | Choose the highlighted country/region. | The <Country/Region> - Selling dialog opens. The compliance status is Allowed. |  |
| 11 | Check the Product Marketability Tab, Production View | Choose Production View in the Product Marketability tab. | The country/region of the customer 33100003 (Domestic US Customer 3) is highlighted in green. |  |
| 12 | View Compliance Status | Choose the highlighted country/region. | The <Country/Region> - Producing dialog opens. The compliance status is Allowed. |  |
| 13 | Check the Dangerous Goods Tab | Choose the Dangerous Goods tab. | The International Transport table indicates that transport via aircraft cargo, aircraft passenger, and deep water are pending. No countries/regions are highlighted on the map. |  |

### Customer Compliance Check During Sales Orders

#### Create Sales Order for a Product with Compliance Relevance Indicated

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative creates a sales order for a product with customer first-order check enabled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Create Sales Order | Choose Create > Create Sales Order - VA01 . | The screen to create a sales order is displayed. |  |
| 4 | Enter the Order | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order: Overview screen is displayed. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:In the header:Sold-To Party: 33100003Ship-To Party: 33100003Cust. Reference: <Any customer reference text>Cust. Ref. Date: <Today's date>In the Sales tab:Deliver.Plant: 3310 | The Create Standard Order: Overview screen is still displayed. |  |
| 6 | Enter Order Item | On the Create Standard Order: Overview screen, All Items section, make the following entries for the first sales order item, and then press Enter:Material: FG<your name>03Order Quantity: 1Un (Sales Unit): BTPlnt (Plant): 3310Double-click in the row for the sales order item. On the Country/Region tab, if available, enter 00 as the tax code. If this tab not available, still stay on the same screen, as it is needed for the next step. | The item is added to the standard order and the Create Standard Order: Item Data screen is displayed. |  |
| 7 | Item Data – Mandatory Pricing Condition | On the Conditions tab of the Create Standard Order: Item Data screen, add a row:CnTy: PPR0Amount: <Any numerical amount>Crcy: <Any currency code>Press Enter.Save.Navigate back to Create Standard Order: Overview. | The pricing error is resolved and the condition type is added. |  |
| 8 | Save Document | Choose the Save button.Make a note of the sales order number: __________. | The order is saved and the order number is shown in the footer.A log opens in which a message indicates that no marketability assessment exists for the product and that a request has been initiated. |  |

#### Classify Unpackaged Product as No Dangerous Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dangerous Goods Specialist - Product Compliance sees that there are unpackaged products that have to be classified according to the dangerous goods regulations. The Dangerous Goods Specialist - Product Compliance classifies an unpackaged product according to the assigned regulations as no dangerous goods and allows the transport for all the regulations.

If the business feature Dangerous Goods Integration into Value Chain is activated, the minimum data maintenance for safety data sheets is required to remove the sales order blocking status. You can activate this business feature via scope item 5OJ.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Dangerous Goods Specialist - Product Compliance (SAP_BR_DG_SPLST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Dangerous Goods > Classification section, open the My Unpackaged Dangerous Goods (F3643) app. | The My Unpackaged Dangerous Goods (F3643) screen is displayed and shows a list of unpackaged products on the For My Responsible Unit tab page. |  |
| 3 | Search Unpackaged Dangerous Good | Enter SG<your name>03 in the Search field. | The Unpackaged Products list is filtered to the products that match the fuzzy search. |  |
| 4 | Select Unpackaged Dangerous Good | Choose the row for the product that you searched for. | The Classify Unpackaged Dangerous Good (F3642) app opens and displays the released analytical composition and a list with all assigned dangerous goods regulations. |  |
| 5 | Select Regulation | In the Basic Classification section, choose the row for the ADR regulation (for example, ADR 2025). | The Classify Dangerous Good (F4465) app opens and displays the Dangerous Goods - Classification Details screen to edit the classification data for the selected regulation (for example ADR 2025).Note that the app ID (for example, F4465 for ADR) varies depending on the selected regulation. |  |
| 6 | Classify Unpackaged Product as Dangerous Goods | Choose Edit and, in the Classification section, select Classified As: No Dangerous Goods. | The Dangerous Good - Classification Details screen displays Classified As: No Dangerous Goods. |  |
| 7 | Set Transport Permission | In the Transport Permission section, select Transport Permission: Allowed. | Transport of the dangerous good is allowed according to the ADR regulation. |  |
| 8 | Save the Classification | After checking the classification data, choose Save. | A message indicates that the classification data is saved. |  |
| 9 | Navigate Back | Navigate back to the Classify Unpackaged Dangerous Good (F3642) app. | The Classify Unpackaged Dangerous Good (F3642) app opens and displays for the ADR regulation that the product is classified as no dangerous goods and that the transport is allowed. |  |
| 10 | Classify Product According to the Other Regulations | Select the checkbox for the ADR regulation and choose Apply Classification to Other Regulations.In the dialog, select all regulations by selecting the checkbox in the Regulation Version column. Then choose Apply Classification. | The dialog closes, and the system applies the classification you did according to ADR to all other selected regulations and saves the classifications as a draft version. |  |
| 11 | Release Classifications | In the Basic Classification table, select all regulations in progress except the UNRTDG regulation or regulations by selecting the checkbox in the Regulation Version column and then deselecting the checkbox for the UNRTDG regulation or regulations. Then choose Release.In the Release dialog, choose Save Drafts and Release. | The dialog closes, and the released classifications are displayed in the Released section of the Regulations table.Note that if you release all regulations, the product is no longer displayed in the My Unpackaged Dangerous Goods (F3643) app. |  |

#### Process Compliance Request from Logistics, Set Market to Allowed, and Set Risk Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance sees a new request from logistics in the worklist for a new product that is compliance relevant. The Product Stewardship Specialist - Product Compliance accepts the request by starting the marketability assessment for the country/region of the production plant. The Product Stewardship Specialist - Product Compliance sets a high risk level for the unpackaged product, which requires a customer assessment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the Product Stewardship Specialist - Product Compliance role is displayed. |  |
| 2 | Access App | In the Product Compliance section, under Basic, choose the Process Requests from Logistics (F3342) tile. | The Process Requests from Logistics screen is displayed and shows the list of unprocessed requests. |  |
| 3 | Search and Select Request | Enter FG<your name>03 in the Search field and then press Enter. | The list is filtered for the entries that match the fuzzy search. |  |
| 4 | Navigate to the Request Object Page | Choose the row for the unprocessed request for FG<your name>03, with Sell In / <country/region of customer Domestic UAE Customer 3> in the Business Process / Area column, Extend Business Process in the Initiating Process column, and Sales Order in the Source of Request column. | The Compliance Request from Logistics screen is displayed. |  |
| 5 | Edit Assessments | Check that the following information is displayed:Under Request Details:Requester: Example InternalSalesRepSales Order: The sales order number from the sales order you created in a previous stepCustomer: Domestic UAE Customer 3Product in Product Master: <your name> Finished 03 (FG<your name>03)Under Request Steps > View Basic Compliance Data :Compliance View Type: Packaged ProductPackagedCompliance View - Packaged: FG<your name>03Logistics Roles: Sold, TransportedUnpackagedCompliance View - Unpackaged: <your name> UP 3Logistics Roles: Sold, Transported, ProducedApplications: –View Compliance Purpose Assignments > Assigned Compliance Purposes > Compliance Purpose > > : <your name> PMA-CCC, DGOnce you've verified this information, choose Edit Assessments under Edit Market Assessments. | The Market Assessment screen is displayed. |  |
| 6 | Add Country/Region | On the Market Assessment screen, under Assessment for Countries/Regions > Product Market Assessments , choose Add. | The Assign Countries/Regions dialog opens. |  |
| 7 | Assign Country/Region | Select the country/region of Domestic UAE Customer 3. Then choose OK. | The country/region of Domestic UAE Customer 3 is added to the Product Market Assessments table. |  |
| 8 | Open Product Market Assessment | In the Product Market Assessments table, choose the row of the newly added country/region. | The pane for the selected country/region opens. |  |
| 9 | Set Assessment Status | Under Generally Valid > Compliance per Business Process , set the Assessment Status for Production and Assessment Status for Sales values to Allowed. | Under Generally Valid > Compliance per Business Process , Allowed appears in the Assessment Status for Production and Assessment Status for Sales fields. |  |
| 10 | Choose Marketability Assessment | In the Compliance Requirement Versions table, choose the row for the latest version of the World-First Order Check compliance requirement version for which no released marketability assessment exists. | The Marketability Assessment screen is displayed. |  |
| 11 | Switch to Edit Mode | Choose Edit. | The app is in edit mode. |  |
| 12 | Set Marketability Status | In the Compliance Details section, set the risk level to Class 1. Then choose Save. | The marketability status changes to Customer Assessment Required. |  |
| 13 | Release Marketability Assessment | Choose Release. | A success message states that the compliance assessment is released. |  |
| 14 | Navigate Back | Navigate back. | In the Compliance Requirement Versions table, in the row for the latest World-First Order Check compliance requirement version, Customer Assessment Required appears in the Marketability Status column, and today's date appears in the Released On column. |  |
| 15 | Apply Changes | In the pane for the selected country/region, choose Apply. | The pane closes, and the main Market Assessment screen expands. |  |
| 16 | Save Your Assessment | On the Market Assessment screen, choose Save. | A success message confirms that your changes were saved. |  |

#### Process Compliance Request from Logistics and Release Customer Assessment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance sees a new request from logistics in the worklist for a product that requires a customer assessment. The Product Stewardship Specialist - Product Compliance accepts the request by starting the marketability assessment for the customer of the product against the assigned compliance requirement version based on the Customer Compliance Check compliance pattern..

In this process step, the assessment is set to Compliant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the Product Stewardship Specialist - Product Compliance role is displayed. |  |
| 2 | Access App | In the Product Compliance section, under Basic, choose the Process Requests from Logistics (F3342) tile. | The Process Requests from Logistics screen is displayed and shows the list of unprocessed requests. |  |
| 3 | Search and Select Request | Enter FG<your name>03 in the Search field and then press Enter. | The list is filtered for the entries that match the fuzzy search. |  |
| 4 | Navigate to the Request Object Page | Choose the row for the unprocessed request for FG<your name>03, with Sell In in the Business Process column and Customer Assessment Required in the Initiating Process column, to navigate to the Compliance Request from Logistics screen. | The Compliance Request from Logistics screen is displayed. |  |
| 5 | Start Handover to Assessment | Check that the following information is displayed:Under Request Details:Requester: Example InternalSalesRepSales Order: The sales order number from the sales order you created in a previous stepCustomer: Domestic UAE Customer 3Product in Product Master: FG<your name>03 (<your name> Finished 03)Under Compliance View:Packaged Product: <your name> Finished 03Logistics Roles of Packaged Product: Sold, TransportedUnpackaged Product: <your name> Finished 03Logistics Roles of Unpackaged Product: Sold, Transported, ProducedUnder Countries/Regions to Verify: The sell-to country/region of Domestic UAE Customer 3 (as indicated in the customer description - for example, the United Status for “Domestic US Customer 3”)Under Compliance Purposes to Verify: <your name> PMA_CCC, DGOnce you've verified this information, choose Ready for Assessment. | The Ready for Assessment dialog is displayed.The dialog displays the product, assigned unpackaged product, added countries/regions, and an empty field for added compliance purposes. |  |
| 6 | Complete Handover to Assessment | In the Ready for Assessment dialog, choose Assess Now. | The Ready for Assessment dialog is closed.The Manage Customer Compliance for Products screen is displayed. |  |
| 7 | Choose Marketability Assessment | Choose the row of the marketability assessment that appears in the In Progress tab of the Marketability Assessments table. The compliance requirement version is the latest version of World-First Order Check for which no released marketability assessment exists. | The Marketability Assessment screen is displayed. |  |
| 8 | Edit Marketability Assessment | Choose Edit. | The app is in edit mode. |  |
| 9 | Set Marketability Status | In the Compliance Details section, choose Compliant from the Marketability Status dropdown menu. | Compliant is displayed as the marketability status. |  |
| 10 | Save Marketability Assessment | Choose Save. | A message indicates that your changes have been saved. |  |
| 11 | Release Marketability Assessment | Choose Release. | A message indicates that the compliance assessment has been released. |  |
| 12 | Navigate Back | Navigate back. In the Marketability Assessments table on the Manage Customer Compliance for Products screen, choose the Released tab. | The Manage Customer Compliance for Products screen is displayed. The marketability assessment that you released in the previous step has moved from the In Progress tab to the Released tab of the Marketability Assessments table. |  |

#### Check Status of Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative analyzes sales documents based on the given issue types. Marketability issues are visualized in the Delivery Block in Sales Orders and Delivery Issue in Sales Orders issue types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Under Internal Sales > Sales Processing > Monitoring , open Sales Order Fulfillment - Analyze and Resolve Issues (F0029A). | The analytic list page for orders with issues is displayed. |  |
| 3 | Search for Marketability Issues | Switch the header filter view by choosing the <!-- image omitted: unnamed -->(Compact Filter) icon.Choose Adapt Filters. Select the Product Marketability Status filter attribute, and then choose OK.For the Product Marketability Status filter, select the value OK – Approved.Confirm the new filter settings by choosing Go. | The list is filtered for any sales documents with approved marketability. |  |
| 4 | Select the Status Value for Display | Choose the <!-- image omitted: unnamed -->(Settings) icon for the Sales Documents with Issues table (not the Sales Documents with Issues diagram).Use the search field to search for Product Marketability Status. Select the checkbox for Product Marketability Status if it's not already selected, and then choose OK. | The table shows the marketability header status for the sales documents. |  |
| 5 | Select the Sales Order | Use the main search field on the Sales Order Fulfillment Issues screen to search for the sales order from the test procedure [Create Sales Order for a Product with Compliance Relevance Indicated](#unique_20) [page ] 35. This is the sales order for the product FG<your name>03. | The sales order appears in the Sales Documents with Issues table. |  |
| 6 | Navigate to Tracking of Sales Order Details | Choose the <!-- image omitted: unnamed -->(Details) icon for the row of the sales document with Delivery Block in Sales Orders in the Issue column and OK – Approved in the Product Marketability Status column.Note If you can't see the column, scroll right.If more than one entry fulfills these criteria, choose the first entry. | The Track Sales Order Details screen is displayed. |  |
| 7 | View Item Processing Details | Choose the Items tab. | The Item Processing Details table is displayed. |  |
| 8 | Navigate to Compliance Information | In the Item Processing Details table, choose the hyperlink for the product.If a link to Display Compliance Information for Products exists, choose it. Otherwise, choose More Links, then select the checkbox for Display Compliance Information for Products, then choose OK, and then choose the Display Compliance Information for Products link. | You navigate to the Compliance Information - For Products (F3226) app, Product Marketability tab, Sales View. |  |
| 9 | Check the Product Marketability Tab, Sales View | Check the map in the Product Marketability tab, Sales View. | The country/region of the customer 33100003 (Domestic US Customer 3) is highlighted in green. |  |
| 10 | View Compliance Status | Choose the highlighted country/region. | The <Country/Region> - Selling dialog opens. The compliance status is Allowed. |  |
| 11 | Check the Product Marketability Tab, Production View | Choose Production View in the Product Marketability tab. | The country/region of the customer 33100003 (Domestic US Customer 3) is highlighted in green. |  |
| 12 | View Compliance Status | Choose the highlighted country/region. | The <Country/Region> - Producing dialog opens. The compliance status is Allowed. |  |
| 13 | Check the Dangerous Goods Tab | Choose the Dangerous Goods tab. | The International Transport table indicates that transport via aircraft cargo, aircraft passenger, and deep water are pending. No countries/regions are highlighted on the map. |  |

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
> Flagged while digesting this document, not verified: Sample master data names customer 33100003 as 'Domestic UAE Customer 3' (UAE) but expected results in the status-check procedures describe it as 'Domestic US Customer 3' (US), so the customer's country/region is stated inconsistently.

> [!warning] Conflict
> Flagged while digesting this document, not verified: In 'Process Compliance Request from Logistics and Assess Marketability Requirements' the request is for FG<your name>02, yet the expected data lists packaged FG<your name>03, unpackaged '<your name> UP 2' and a Product in Product Master of FG<your name>05, which do not match the three products created in the preliminary steps.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/substance-volume-tracking-4ol-ae-test-script-sap-s-4hana-cloud-public]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-assess-marketability-of-a-product-31h-ae-sap-s-4hana-cloud]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-chemical-compliance-approval-for-purchased-material-and-su]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31J_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 90,347 chars in the whole document
