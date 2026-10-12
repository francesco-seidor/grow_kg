---
id: 10-procurement/test-script-central-sourcing-3zf-sap-s-4hana-cloud-public-edition-990
title: "Test Script: Central Sourcing (3ZF) - SAP S/4HANA Cloud Public Edition (3ZF_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3ZF Central Sourcing: central RFQ, supplier quotation, award, central contract or PO follow-ons."
cluster: 10-procurement
tags: [kb/procurement, topic/central-sourcing]
aliases: [3ZF_S4CLD2608_BPD_EN_XX]
keywords: [Central Sourcing and Central Procurement, central sourcing, central request for quotation, central supplier quotation, supplier quotation award, central purchase contract, purchase order creation, test prerequisites, business roles, pro-rata vat]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3ZF_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-990
topic: 10-procurement/central-sourcing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Central Sourcing (3ZF) - SAP S/4HANA Cloud Public Edition (3ZF_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3ZF_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Sourcing and Central Procurement** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Central Sourcing (3ZF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232831033)

[2 Prerequisites 4](#_Toc232831034)

[2.1 System Access 4](#_Toc232831035)

[2.2 Roles 4](#_Toc232831036)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232831037)

[2.4 Additional Manual Configuration 5](#_Toc232831038)

[2.5 Business Conditions 5](#_Toc232831039)

[2.6 Setting up Pro-rata VAT New Tax Codes (Optional) 6](#_Toc232831040)

[3 Overview Table 7](#_Toc232831041)

[4 Test Procedures 8](#_Toc232831042)

[4.1 Create Central Request for Quotation 8](#_Toc232831043)

[4.2 Manage Central Request for Quotations 10](#_Toc232831044)

[4.3 Create Central Supplier Quotation 10](#_Toc232831045)

[4.4 Manage Central Supplier Quotations 12](#_Toc232831046)

[4.5 Create Follow-on Documents 13](#_Toc232831047)

[4.5.1 Scenario 1: Create Central Purchase Contract and Distribution 13](#_Toc232831048)

[4.5.1.1 Display Central Purchase Contracts 14](#_Toc232831049)

[4.5.1.2 Check Local Contract - In Connected System 15](#_Toc232831050)

[4.5.2 Scenario 2: Create Purchase Order 16](#_Toc232831051)

[4.5.2.1 Display Purchase Order - In Connected System 17](#_Toc232831052)

[4.5.2.2 Post Goods Receipt - In Connected System 18](#_Toc232831053)

[4.5.2.3 Create Supply Invoice - In Connected System 18](#_Toc232831054)

## Purpose

Overview

Central Sourcing provides centralized access and visibility into sourcing process across industries with deep integration into the system landscape. It is connected to the customer's ERP systems and exchanges purchasing documents (such as purchase requisitions, purchase orders, and contracts) in the connected systems.

This scope item offers one platform where a procurement specialist can work centrally on purchase requisitions from multiple ERP systems to identify the ideal source of supply. A request for quotation (RFQ) can be created for multiple requisitions from different ERP systems. The supplier quotations received can be maintained and an RFQ can be awarded. Follow-on actions (like creating a central contract or purchase order in the corresponding ERP system) can be centrally controlled in the hub system.

Strategic procurement tasks including Supplier Management benefit from the transparency and the possibility to initiate strategic activities from a central digital procurement control center.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition HUB system | Identifies the SAP S/4HANA Cloud Public Edition system from releases 1905. The SAP S/4HANA Cloud Public Edition system acts as a hub system when it is connected to multiple connected systems.Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Connected System | Any ERP system from release ERP6.0 and EHP6 above with add-on HUBERPI is considered as the connected system.Any SAP S/4HANA Cloud Private Edition 1709 and higher, with add-on HUBS4IC is considered as connected system.Any SAP S/4HANA Cloud Public Edition 2502 is considered as connected system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_MM_SPT_CNTRL_PURCHASING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Central Purchase Organization | 1010 | Purch. Org. 1010 |  |
| Central Purchase group | 001 | Group 001 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS – MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c34553e09ad629a0fe53c7cc8fefdb10)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2XT – Central Purchasing | To run through this test script, the Central Purchase Requisition must be created according to 2XT - Central Purchasing scope item. The prerequisites of 2XT must be fulfilled, and the following steps of test procedure must be completed before the test procedure of this test script is started:Create Purchase RequisitionImport Purchase RequisitionsManage Purchase Requisitions Centrally |
| 2ME – Central Purchase Contracts | To run through this test script, the prerequisites of 2ME must be fulfilled. |

### Setting up Pro-rata VAT New Tax Codes (Optional)

For the Netherlands you have the option (in case it is relevant for you) to configure tax codes especially for pro-rata VAT (partially deductible and non-deductible VAT). To achieve this, you need to perform the following steps:

- Create pro-rata tax codes that can trigger the automatic split of deductible and non-deductible portion (SSCUI 101016)
- Define pro-rata coefficients (SSCUI 103619)

Based on this configuration the system can then automatically split the input VAT into deductible and non-deductible portions when an incoming invoice is posted, using the coefficient that is valid for the company code and the tax code on the relevant date.

The coefficient represents the portion of the input tax that can be deducted, for example, if the pro-rata coefficient is 90% and the standard VAT rate is 21%, then 18.9% is deductible and 2.1% is non-deductible.

|  |
| --- |
| Note When creating new tax codes you also need to configure the account assignment for your new tax codes (SSCUI 100297) and you need to make the necessary settings (SSCUI 103011) to make sure your newly created tax codes are also reported in the VAT return. |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Central Request for Quotation](#unique_10) [page ] 8 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Manage Central Request for Quotations](#unique_11) [page ] 10 | Purchaser - Central Procurement | Manage Central RFQs (F3974) |  |
| [Create Central Supplier Quotation](#unique_12) [page ] 10 | Purchaser - Central Procurement | Manage Central RFQs (F3974) |  |
| [Manage Central Supplier Quotations](#unique_13) [page ] 12 | Purchaser - Central Procurement | Manage Central Supplier Quotations (F3975) |  |
| [Scenario 1: Create Central Purchase Contract and Distribution](#unique_14) [page ] 13 | Purchaser - Central Procurement | Manage Central Supplier Quotations (F3975) |  |
| [Display Central Purchase Contracts](#unique_15) [page ] 14 | Purchaser - Central Procurement | ECC |  |
| [Scenario 2: Create Purchase Order](#unique_16) [page ] 16 | Purchaser - Central Procurement | Create Purchase Orders from Central Quotations (F4104) |  |
| [Display Purchase Order - In Connected System](#unique_17) [page ] 17 | Purchaser | ECC |  |
| [Post Goods Receipt - In Connected System](#unique_18) [page ] 18 | Warehouse Clerk | ECC |  |
| [Create Supply Invoice - In Connected System](#unique_19) [page ] 18 | Accounts Payable Accountant | ECC |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Central Request for Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase requisitions from different connected systems get replicated (extracted) to the SAP S/4HANA Procurement hub system and will be available for sourcing in the app Process Purchase Requisitions - Deprecated (F1048). You are unable to find a source of supply for the PR items, but you can select multiple requisition items and create central RFQ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Manage Purchase Requisistions Centrally screen is displayed. |  |
| 3 | Start Central RFQ creation | Select the checkbox of multiple purchase requisition items and choose Create Document, choose Create Central RFQ to create a new central RFQ. | The Central Request for Quotation screen is displayed. |  |
| 4 | Enter Central RFQ data | On the Central Central RFQ screen, navigate to the General Information section and make the following entries:RFQ Type(default value): Internal RFQRFQ Description: <enter the description>Language Key : for example, ENQuotation Deadline: <today>Central Purchasing Group: 001Central Purchasing Organization: 1010Central Company Code : 1010Follow-On Doc. Type: for example, MKNote The follow-on doc. type defined here will determine the available option in central supplier quotation as mentioned in section Create Follow-on Documents. For example:For Quantity Contract (MK) or Value Contract (WK), the option is Create Central Contract in Central Supplier Quotation.For Purchase Order (PO), the opiton is Create Purchase Order in Central Supplier Quotation.If you leave this field blank, both options are available in central supplier quotation.Validity Per. Start (does not exist for follow-on doc. type PO): <today>Validity Period End (does not exist for follow-on doc. type PO): <today + 1 month>In the Delviery and Payment Terms section, make the following entries:Target Value: for example, 200 EURCurrency: EURIn the Items section, the selected purchase requisition items are listed.Ensure the data is correct.In the Bidders section, make the following entry:Supplier: for example, VEND_SPROCNote The supplier must be same as the existing one in the connected system. You can refer to master data script Create Supplier Master - MDS to create supplier in SAP S/4HANA Cloud Public Edition hub system.Choose Create. | The central RFQ is created. |  |

### Manage Central Request for Quotations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can maintain the additional details like Bidders, Payment Terms and Incoterms for Central RFQ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central RFQs (F3974). | The Manage Central RFQs screen is displayed. |  |
| 3 | Search Central RFQ | On the Manage Central RFQs screen, enter search criteria to search your Central RFQ.Then choose your Central RFQ. | Your Central RFQ is displayed. |  |
| 4 | Edit the Central RFQ data | You can change the content. For example, change the Quotation Deadline, or add a RFQ Description.Supplier: 10300001Choose Save.Choose Publish. | The Central RFQ is updated and published. The status is changed from In Preparation to Published. |  |

### Create Central Supplier Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create central supplier quotations with respect to the central RFQ, maintain the price and pricing details, and submit the quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central RFQs (F3974). | The Manage Central RFQs screen is displayed. |  |
| 3 | Search Central RFQ | On the Manage Central RFQs screen, enter search criteria to search your central RFQ.Then choose your central RFQ. | Your central RFQ is displayed. |  |
| 4 | Publish Central Spplier Quotation | On the Central Request for Quotation screen, choose Publish on the upper right corner. | Your central RFQ is published. |  |
| 5 | Create First Central Supplier Quotation | On the Central Request for Quotation screen, select supplier VEND_SPROC in the Bidders section and choose Create Quotation.On the Central Supplier Quotation screen and in the General Information section, make the following entry:Quotation Submission Date: <today>In the Items section, make the following entry:Net Order Price : 2000Choose Create. | The first central supplier quotation is created. |  |
| 6 | Submit First Supplier Quotation | On the Supplier Quotation screen, choose Submit. | The central supplier quotation is submitted. |  |

### Manage Central Supplier Quotations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can display the Central Supplier Quotations for different Suppliers and award the best Supplier Quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central Supplier Quotations (F3975). | The Manage Central Supplier Quotations screen is displayed. |  |
| 3 | Search Central Supplier Quotation | On the Manage Central Supplier Quotations screen, enter search criteria to search your Central Supplier Quotations.Then choose one of your Central Supplier Quotations. | Your Central Supplier Quotation displays. |  |
| 4 | Display or Edit the Data | Check the data of Central Supplier Quotation and then choose Edit on the upper right corner. Change the details if required.Choose Save. |  |  |
| 6 | Award Central Supplier Quotation | Select one Central Supplier Quotation with best-priced items and choose Award. | Central Supplier Quotation is awarded. |  |

### Create Follow-on Documents

#### Scenario 1: Create Central Purchase Contract and Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create a central contract from the awarded supplier quotation. This step refers to the scope item 2ME - Central Purchase Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central Supplier Quotations (F3975). | The Manage Central Supplier Quotations screen is displayed. |  |
| 3 | Search Central Supplier Quotations | On the Manage Central Supplier Quotations screen, enter search criteria to search your entral Supplier Quotations.Then choose your awarded Central Supplier Quotation. | Your Central Supplier Quotation is displayed. |  |
| 4 | Create Central Purcahse Contract | On the Central Supplier Quotation screen, choose Create Follow-On Document on the upper right corner and then choose Create Central Contract.Note Please ensure that the Follow-on Doc. Type is Quantity Contract (MK) or Value Contract (WK) is maintained or left blank when you create the Central Request for Quotation, otherwise the option is not available here. | The Central Purchase Contract screen is displayed. |  |
| 5 | Enter Central Purcahse Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contact Type: Quantity ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 1010Central Purchasing Group: 001Supplier: VEND_SPROCCurrency: EURYou can check Flexible Distribution to allow more than 100% distribution.In the Items section, make the following entries:Target Quantity: for example, 10Choose Release.Note If click on Save In Preparation, the document will be saved with In Preparation status, no approval or distribution will be triggered. | The Central Purchase Contract is created. |  |

##### Display Central Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check the distribution status and local contract in central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen is displayed. |  |
| 3 | Search central contract | On the Manage Central Purchase Contracts screen, enter search criteria to search your central purchase contract.Then choose your central purchase contract. | Your central contract is displayed. |  |
| 4 | Check distribution status and local contract number | On the Central Purchase Contracts screen, navigate to the Items section and choose the item entry.On the Central Purchase Contract Item screen, navigate to the Distributed Outline Agreements section.You can check the local contract/schedule agreement number in column Outline Agreements.If Distribution Status is Error in Distribution, you can choose Information in the column of Error Information to check detail error information. After error is fixed in connected system, you can select the line and choose Reinitiate Distribution to distribute central purchase contract again. |  |  |

##### Check Local Contract - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check the contract which is a copy of the central contract in connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system to which employee belongs as a Purchaser - Central Procurement . |  |  |
| 2 | Check Local Outline Agreements | Check the local contract distributed from central contract with transaction ME33K.If Info Record Update Code is assigned in contract distribution, you can check the updated info record by choosing Environment > Info Record in local contract / scheduling agreement.The account assignment category U(Unknown) for free text and '' (Blank) for material are currently supported as account assignment category for central contract item. |  |  |

#### Scenario 2: Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create Purchase Order based on the Central Supplier Quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central Supplier Quotations (F3975). | The Manage Central Supplier Quotations screen is displayed. |  |
| 3 | Search Central Supplier Quotations | On the Manage Central Supplier Quotations screen, enter search criteria to search your Central Supplier Quotations.Then choose your awarded Central Supplier Quotation. | Your Central Supplier Quotation is displayed. |  |
| 4 | Create Purchase Order | On the Central Supplier Quotation screen, choose Create Follow-On Document on the upper right corner and choose Create Purchase Order.Note Please ensure that the Follow-on Doc. Type Purchase Order (PO) is maintained or left blank when you create the Central Request for Quotation, otherwise the option is not available here. | The Create Purchase Order screen is displayed. |  |
| 5 | Enter Purcahse Order data | On the Create Purchase Order screen, navigate to General Information section and make the following entries:Purchasing Organization: 1000Purchasing Group: 001Choose Order.Note down the created purchase order number to check in the connected system later, or click on the hyperlink of the purchase order number. The WebGUI of connected system will be opened in the new session. | The Purchase Order is created. |  |

##### Display Purchase Order - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a purchase order is created in hub system, you can check the purchase order in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system as a Purchaser. |  |  |
| 2 | Display Purchase Order | Check the purchase order with transaction ME23N. |  |  |

##### Post Goods Receipt - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system as a Warehouse Clerk . |  |  |
| 2 | Post Goods Receipt | Post goods receipt with TransactionMIGO | Goods Receipt is posted in connected system. |  |

##### Create Supply Invoice - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

|  |
| --- |
| Caution For Netherlands, in case pro-rata VAT is relevant for you, please make sure you meet the prerequisites as mentioned in Prerequisites. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system as an Accounts Payable Accountant . |  |  |
| 2 | Create Invoice Verification | Create supplier invoice with Transaction Code MIRO.Choose Invoice. | Invoice is created in the connected system. |  |

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
> Flagged while digesting this document, not verified: Scenario 2 enters Purchasing Organization 1000 whereas the RFQ and contract steps and sample data use organization 1010

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-automation-of-central-procurement-quote-with-sap-business]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3ZF_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 31,597 chars in the whole document
