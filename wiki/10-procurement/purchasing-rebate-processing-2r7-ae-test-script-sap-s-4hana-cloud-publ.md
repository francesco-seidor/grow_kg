---
id: 10-procurement/purchasing-rebate-processing-2r7-ae-test-script-sap-s-4hana-cloud-publ
title: "Purchasing Rebate Processing (2R7_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2R7_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 2R7 (AE) Purchasing Rebate Processing: config prerequisites, condition contract types, settlements, workflow, fixed amounts, scales, reversal."
cluster: 10-procurement
tags: [kb/procurement, topic/purchasing-rebates]
aliases: [2R7_S4CLD2608_BPD_EN_AE]
keywords: [Purchasing Rebate Processing, condition contracts, contract process variants, delta accruals settlement, partial settlement, final settlement, two-step settlement, rebate approval workflow, graduated scale determination, fixed amount agreements]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2R7_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-855
topic: 10-procurement/purchasing-rebates
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Purchasing Rebate Processing (2R7_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2R7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2R7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Purchasing Rebate Processing** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Purchasing Rebate Processing (2R7_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Purchasing Rebate Processing (2R7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232849966)

[2 Prerequisites 5](#_Toc232849967)

[2.1 System Access 5](#_Toc232849968)

[2.2 Roles 5](#_Toc232849969)

[2.3 Master Data and Organizational Data 6](#_Toc232849970)

[2.4 Preliminary Steps 8](#_Toc232849971)

[2.4.1 Posting of Accruals with Transactional Documents (Optional) 8](#_Toc232849972)

[2.4.2 Prepare Transactional Data 10](#_Toc232849973)

[2.4.3 Activate Condition Contract Types for Fixed Amount Agreements (Optional) 11](#_Toc232849974)

[2.4.4 Define Contract Process Variants 13](#_Toc232849975)

[2.4.4.1 Define Process Variant for Using Flexible Workflow 13](#_Toc232849976)

[2.4.4.2 Define Process Variant for Tax Free Goods 15](#_Toc232849977)

[2.4.4.3 Define Process Variant for Split Criteria Usage in Settlement 18](#_Toc232849978)

[2.4.4.4 Define Process Variant for Business Volume Selection Criteria Usage 21](#_Toc232849979)

[2.4.4.5 Define Process Variant to Configure Material Groups as Condition Level 23](#_Toc232849980)

[2.4.4.6 Define Process Variant to Configure Settings for Fixed Amount Agreements 26](#_Toc232849981)

[2.4.4.7 Define Process Variant Scale to Enable Selection of Different Bases for Rebate Calculation and Scale Determination 29](#_Toc232849982)

[2.4.4.8 Maintain Automatic Account Determination 31](#_Toc232849983)

[2.4.5 Configure Flexible Workflow (Optional) 35](#_Toc232849984)

[2.4.5.1 Manage Team and Responsibilities 35](#_Toc232849985)

[2.4.5.2 Manage Flexible Workflow for Condition Contract 37](#_Toc232849986)

[2.4.5.3 Manage Flexible Workflow for Condition Contract Settlement 38](#_Toc232849987)

[2.4.5.4 Manage Flexible Workflow for Settlement Document 39](#_Toc232849988)

[3 Overview Table 41](#_Toc232849989)

[4 Test Procedures 46](#_Toc232849990)

[4.1 Goods Related A/P Settlement Based on Supplier Invoices 47](#_Toc232849991)

[4.1.1 Create Supplier Condition Contract 47](#_Toc232849992)

[4.1.2 Check Business Volume (Optional) 50](#_Toc232849993)

[4.1.3 Delta Accruals Settlement (Optional) 51](#_Toc232849994)

[4.1.4 Check Settlement Document for Delta Accruals Settlement (Optional) 53](#_Toc232849995)

[4.1.5 Partial Settlement (Optional) 54](#_Toc232849996)

[4.1.6 Check Settlement Document for Partial Settlement (Optional) 55](#_Toc232849997)

[4.1.7 Final Settlement 57](#_Toc232849998)

[4.1.8 Check Settlement Document for Final Settlement Document (Optional) 59](#_Toc232849999)

[4.2 Service Related A/R Settlement Based on Supplier Invoices 61](#_Toc232850000)

[4.2.1 Create Supplier Condition Contract 61](#_Toc232850001)

[4.2.2 Delta Accruals Settlement (Optional) 62](#_Toc232850002)

[4.2.3 Partial Settlement (Optional) 62](#_Toc232850003)

[4.2.4 Final Settlement 63](#_Toc232850004)

[4.3 A/P and A/R Settlement Based on GR Material Documents 63](#_Toc232850005)

[4.3.1 Create Supplier Condition Contract 63](#_Toc232850006)

[4.3.2 Delta Accruals Settlement (Optional) 67](#_Toc232850007)

[4.3.3 Partial Settlement (Optional) 67](#_Toc232850008)

[4.3.4 Final Settlement 67](#_Toc232850009)

[4.4 Two-Step Processing for Settlement 68](#_Toc232850010)

[4.4.1 Create Supplier Condition Contract 68](#_Toc232850011)

[4.4.2 Delta Accruals Settlement (Optional) 68](#_Toc232850012)

[4.4.3 Partial Settlement (Optional) 69](#_Toc232850013)

[4.4.4 Collect Parked Settlement Documents from Partial Settlement (Optional) 69](#_Toc232850014)

[4.4.5 Final Settlement 70](#_Toc232850015)

[4.4.6 Collect Parked Settlement Documents from Final Settlement 70](#_Toc232850016)

[4.5 Purchasing Rebate Processing with Workflow 71](#_Toc232850017)

[4.5.1 Create Supplier Condition Contract 72](#_Toc232850018)

[4.5.2 Request Approval to Release Condition Contract 75](#_Toc232850019)

[4.5.3 Trigger Rework of Condition Contract (Optional) 76](#_Toc232850020)

[4.5.4 Rework Condition Contract (Optional) 77](#_Toc232850021)

[4.5.5 Release Supplier Condition Contract 78](#_Toc232850022)

[4.5.6 Delta Accruals Settlement (Optional) 78](#_Toc232850023)

[4.5.7 Request Release of Condition Contract for Settlement 79](#_Toc232850024)

[4.5.8 Release Supplier Condition Contract for Settlement 80](#_Toc232850025)

[4.5.9 Partial Settlement (Optional) 80](#_Toc232850026)

[4.5.10 Approve Release of Partial Settlement Document to Accounting (Optional) 81](#_Toc232850027)

[4.5.11 Final Settlement 81](#_Toc232850028)

[4.5.12 Approve Release of Final Settlement Document to Accounting 82](#_Toc232850029)

[4.6 Purchase Rebate Processing with Graduated Scale Determination 82](#_Toc232850030)

[4.7 Purchasing Rebate Processing – Fixed Amount Agreements 83](#_Toc232850031)

[4.7.1 Basic Processing 84](#_Toc232850032)

[4.7.2 Cost Recognition for Fiscal Periods 86](#_Toc232850033)

[4.7.3 Fixed Amount Settlement Proportionally Across Fiscal Periods 88](#_Toc232850034)

[4.7.4 Fixed Amount Distribution to Business Objects 88](#_Toc232850035)

[4.7.5 Fixed Amount Settlement on Multiple Products 89](#_Toc232850036)

[4.8 Purchase Rebate Processing with Different Bases for Rebate Calculation and Scale Determination 89](#_Toc232850037)

[4.8.1 Create Supplier Condition Contract 90](#_Toc232850038)

[4.8.2 Delta Accruals Settlement (Optional) 93](#_Toc232850039)

[4.8.3 Partial Settlement (Optional) 94](#_Toc232850040)

[4.8.4 Final Settlement 94](#_Toc232850041)

[4.9 Final Settlement with Adjustments (Optional) 95](#_Toc232850042)

[4.10 Reverse Settlement Documents - Condition Contracts (Optional) 97](#_Toc232850043)

[5 Appendix 99](#_Toc232850044)

[5.1 Process Integration 99](#_Toc232850045)

[5.1.1 Succeeding Processes 99](#_Toc232850046)

[5.2 General Ledger Reporting and CO-PA Reporting (Optional) 99](#_Toc232850047)

[5.3 Time-Dependent Tax 99](#_Toc232850048)

## Purpose

The Purchasing Rebate Processing scope item concerns the subsequent settlement of rebate conditions agreed upon with a supplier. You use condition contracts from Condition Contract Management to enter the rebate agreements with the suppliers. In a condition contract, you specify, beside organizational and process control parameter, the business volume selection criteria, the rebate conditions and the settlement calendar with settlement dates for delta accrual, partial and final settlement. The delta accruals settlement reflects a procedure in which accruals are not posted together with the transactional documents but subsequently in a specific settlement run. In the partial and final settlements of a condition contract you perform the rebate calculation based on business volume and rebate conditions and you create the settlement documents to claim the rebate payments from the supplier. This scope item supports two data sources for the business volume determination: supplier invoices, usually applied for an amount based rebate calculation, and material documents of goods receipt postings usually applied for quantity or weight/volume based rebate calculation.

In addition, you can also configure workflows to include the approval process for condition contracts, release of condition contract for settlement and settlement documents. You can define workflow preconditions for releasing condition contracts and settlement documents. An approver can choose to approve, reject or send the documents for rework to the document initiator. The approval process starts when a workflow with one or more steps is activated and the preconditions you have assigned to it are met.

This scope item involves two ways of how to settle the condition contract depending on the character of the rebate agreement. When you regard rebates as subsequent abatement of the purchase price for procured materials you perform a so-called goods related settlement as accounts payable to create a credit memo with the supplier as payer. In this case, the taxation is consistent with the taxation in the procurement process. When the rebate agreement reflects a service rendered for the supplier you perform a settlement as account receivable to create an invoice for the supplier. The taxation for the rebate amount is carried out according to a service.

Another process variant concerns the transfer of settlement documents to accounting. Usually, you create settlement documents that are immediately released to accounting. In addition, you can also create a two-step condition contract to collect and post settlement documents of different condition contracts in one journal entry to accounting. When you create and process a two-step condition contract, the reversal of the accruals and the customer revenues is not posted until the creation of the collective settlement document.

This scope item extends the business process for the Procurement of Direct Materials (scope item J45). Ideally, the condition contract is created first before you start to enter purchasing documents in the system. However, you can also create condition contracts subsequently with a validity period starting in the past. Also, purchasing rebate processing and procurement run in parallel in that sense that you process partial settlements for purchasing documents entered continuously during the condition contract’s validity period.

This test script indicates that you can either create transactional data (supplier invoices or material documents for goods receipt) before you create the supplier condition contract or afterwards. If you create transactional data before you create the supplier condition contract, you can still create further transactional data after creation of the condition contract because purchasing rebate processing and procurement run in parallel in the sense that you process partial settlements for purchasing documents entered continuously during the condition contract’s validity period.

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
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Business Partner Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

### Master Data and Organizational Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc.no batch | Material TG0011 used for testing with condition contract type 0PI1/0PI2/0PG1/0PG2.Both TG0011 and TG0015 can be used for testing with condition contract type 0PI3/0PI4/0PG3/0PG4. |
| Material | TG0015 | Trading Good 00115,PD,Regular Proc. | Both TG0011 and TG0015 can be used for testing with condition contract type 0PI3/0PI4/0PG3/0PG4. |
| Material | TG0013 | Trading Good 0013,PD,Regular Proc. |  |
| Supplier | 33300010 | Local Supplier | Can be used for settlement as accounts payable and as accounts receivable |
| Purchasing Organization | 3310 |  |  |
| Purchasing Group | 001/ 002 |  | Depending on material |
| Company Code | 3310 |  |  |
| Plant | 3310 |  |  |
| Storage location | 331A |  |  |
| Sales organization | 3310 |  | Required for settlement type ‘As Accounts Receivable’ |
| Distribution channel | 10 |  | Required for settlement type ‘As Accounts Receivable’ |
| Division | 00 |  | Required for settlement type ‘As Accounts Receivable’ |
| Currency | AED |  |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| 2SW | Create Tax Condition - MDS |
| BND | Create Customer Master - MDS |

### Preliminary Steps

#### Posting of Accruals with Transactional Documents (Optional)

Purpose

Accruals can be created when you post transactional documents ‒ supplier invoices released to accounting or material documents for goods receipt in this scope item ‒ or you can post accruals in an accumulated form with a specific settlement run called Delta Accruals Settlement as described in the test procedures. You can also combine the procedures, for instance, to determine a more accurate accruals amount in a weekly delta accruals run by considering all transactional documents. Posting accruals with transactional documents is only appropriate in the goods related purchasing rebate scenarios (see test procedures). When you post accruals with transactional documents, the accruals amount is considered in the material valuation during goods receipt posting.

To post accruals with released supplier invoices or with material documents for goods receipt, you must include the accruals condition type in the pricing procedure of the purchase order in an appropriate manner. Below we describe the best practice approach that you include the condition type at the bottom of the pricing procedure.

Posting accruals with transactional documents requires that you create the condition contract with the accruals condition before you create Purchase Rebate relevant purchase orders, so that the accruals condition is found during pricing of a purchase order item. Relevant condition contracts are determined by matching purchase order and condition contract data. If the system finds more than one relevant condition contract, you will accordingly get several lines for the accruals condition types in the pricing elements. When you create a condition contract with a validity period starting in the past, you can schedule a delta accruals settlement to post accruals for already created supplier invoices or material documents documents. Then you continue to post accruals with the transactional documents. The accruals amount posted with delta accruals settlement is not considered in the material valuation.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Pricing | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Master DataIn the items table, select the item with item name: Pricing. | The Configure Your Solution - Pricing screen displays. |  |
| 5 | Go to Pricing Procedures Overview | Choose Configure on the right to Set Calculation Schema – Purchasing configuration step. | The Set Calculation Schema – Purchasing: Change screen displays. |  |
| 6 | Go to Control Data | Select the relevant pricing procedure and choose Schemas – Control Data in Dialog Structure. | The control data for the pricing procedure with the Reference Step Overview table is displayed in the working area. |  |
| 7 | Add Accruals Condition Type | Choose New Entries and make the following entries:Step Number: <number higher than maximum hitherto>Condition Type: REA1Alt. Cndn Base Value: 213Accruals: 0PAChoose Save. | Accruals condition type has been added to pricing procedure. |  |

Routine 213 for the alternative calculation of condition base value has to following function: When you enter a condition contract, you can set the amount fields group on the Settlement Data tab page. This parameter controls for which amount field from the business volume data the system transfers data to the pricing procedure of the settlement document. As default, the net amount is used, but you can also specify a subtotal of the pricing procedure. As mentioned, during pricing the system determines the relevant condition contracts for the accruals condition types, and formula 213 reads the corresponding amounts field group and sets the condition base value accordingly. Therefore, there is no need to specify the From Step in the line with accruals condition type.

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Go to Pricing Procedures Overview | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Set Calculation Schema – Purchasing.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Calculation Schema – Purchasing: Change screen displays. |  |
| 3 | Go to Control Data | Select the relevant pricing procedure and choose Schemas – Control Data in Dialog Structure. | The control data for the pricing procedure with the Reference Step Overview table is displayed in the working area. |  |
| 4 | Add Accruals Condition Type | Choose New Entries and make the following entries:Step Number: <number higher than maximum hitherto>Condition Type: REA1Alt. Cndn Base Value: 213Accruals: 0PAChoose Save. | Accruals condition type has been added to pricing procedure. |  |

Routine 213 for the alternative calculation of condition base value has the following function: When you enter a condition contract, you can set the amount fields group on the Settlement Data tab page. This parameter controls for which amount field from the business volume data the system transfers data to the pricing procedure of the settlement document. As default, the net amount is used, but you can also specify a subtotal of the pricing procedure. As mentioned, during pricing the system determines the relevant condition contracts for the accruals condition types, and formula 213 reads the corresponding amounts field group and sets the condition base value accordingly. Therefore, there is no need to specify the From Step in the line with accruals condition type.

#### Prepare Transactional Data

Purpose

To prepare transactional test data, you can follow scope item Procurement of Direct Materials (J45).

This step is required and can be executed before or after you create the condition contract and after each settlement run.

Note

The steps in this chapter are prerequisite to execute chapters [Test Procedures](#unique_8) [page ] 46.

Procedure

Complete the activities described in the Procurement of Direct Materials (J45) using the master data of this document. You do not need to perform all steps described in Procurement of Direct Materials (J45). You can focus on the following steps:

Create Purchase Order

Post Goods Receipt

Create Supplier Invoice

#### Activate Condition Contract Types for Fixed Amount Agreements (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you activate the condition contract types for fixed amount agreements.

|  |
| --- |
| Note Representing a new business scenario, the condition contract types for fixed amount agreements are blocked in the delivered business content in accordance with the guideline that UI changes should be avoided after a release upgrade. Without block these condition contract types would appear on the pop-up window for condition contract selection when you create a new condition contract. |

|  |
| --- |
| Note You must also create a condition contract process variant for the profit center determination for fixed amount agreements. For more information, see chapter [Define Process Variant to Configure Settings for Fixed Amount Agreements](#unique_10) [page ] 26. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Supplier Condition Contract Types | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Purchasing Rebate ManagementIn the items table, select the item with item name: Purchasing Rebate Settlement. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Configure Condition Contract Types for Supplier Condition Contracts. | The "Configure Condition Contract Types for Supplier Condition Contracts": Change screen displays. |  |
| 6 | Remove Block | In column Block, choose <Not Blocked – Can be Used> for condition contract type 0PF1 and/or 0PF2.Choose Save. | The condition contract types are no longer blocked. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Supplier Condition Contract Types and Settl. Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Configure Supplier Condition Contract Types..": Change screen displays. |  |
| 3 | Remove Block | In column Block, choose <Not Blocked – Can be Used> for condition contract type 0PF1 and/or 0PF2.Choose Save. | The condition contract types are no longer blocked. |  |

#### Define Contract Process Variants

This chapter describes the definition of condition contract process variants to also test variations of the core process. A process variant is used to define limited variations for condition contract maintenance and settlement that are configured for a condition contract type without changing the overall character of the process defined by a condition contract type. In this chapter, we describe process variants for different purposes. Note that you can also combine settings from these process variants.

For the use of condition contract process variant, you must also enhance the account determination settings. The process variant is a key field in the relevant condition table. We describe how you maintain account determination settings for the first process variant for approval workflow. Proceed in the same way for all other process variants that you want to test.

When you create a new purchasing rebate condition contract and you want to apply the process variations of a condition contract process variant, enter the condition contract process variant on the Basic Data tab page.

##### Define Process Variant for Using Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate the workflow for purchasing rebate processing.

|  |
| --- |
| Note This chapter is prerequisite to execute [Purchasing Rebate Processing with Workflow](#unique_13) [page ] 71. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Purchase Rebate Settlement | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Purchasing Rebate ManagementIn the items table, select the item with item name: Purchasing Rebate Settlement. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZP01 Test Purchase Rebates with WorkflowSettlement Management Status Group: Purchase RebateDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: Approval Process Is ActiveChoose Save. | The process variant is created and approval process is activated for condition contract, condition contract for settlement and settlement document. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: for example, 0PI1Choose Save.Note Add further condition contract types if you want to test the process variant for other purchasing rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZP01 Test Purchase Rebates with WorkflowSettlement Management Status Group: Purchase RebateDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created and approval process is activated for condition contract, condition contract for settlement and settlement document. |  |
| 4 | Assign Condition Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entries:Contract Type: for example, 0PI1Choose Save.Note Add further condition contract types if you want to test the process variant for other purchasing rebate scenarios. | The relevant contract type is assigned to newly-created process variant. |  |

##### Define Process Variant for Tax Free Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant which controls that purchasing rebate is treated tax-free.

Some countries, like the USA, do not offer tax services. When purchasing rebate is regarded as a service, taxation will be set to zero for the purchasing rebate amount. Tax-free purchasing rebate is achieved with this process variant in which you set the tax indicator for materials to zero. This tax indicator setting is transferred to pricing of a settlement run by a configured transfer rule.

If you want to treat purchasing rebate tax-free, make sure that you assign the condition contract process variant when you create a new condition contract.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Purchasing Rebate Settlement | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Purchasing Rebate ManagementIn the items table, select the item with item name: Purchasing Rebate Settlement. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZP02 Purchasing Rebates with Tax Free GoodsSettlement Management Status Group: Purchase RebateDefault Application Status for Settlement Documents: ReleasedChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: for example, 0PI1Choose Save.Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 3310Tax Indicator for Material: 0Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZP02 Purchasing Rebates with Tax Free GoodsSettlement Management Status Group: Purchase RebateDefault Application Status for Settlement Documents: ReleasedChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: for example, 0PI1Choose Save.Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 3310Tax Indicator for Material: 0Choose Save. |  |  |

##### Define Process Variant for Split Criteria Usage in Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate further split criteria defined in the profiles for business volume determination.

Split criteria for condition contract settlement – defined in Customizing in the profiles for business volume determination – are used to point up the contribution of different business objects to the purchasing rebate amount. In the profile for business volume determination relevant for purchasing rebate settlement, some split criteria, such as material or profit center, are defined as always active. The usage of these split criteria cannot be influenced with a condition contract process variant. But there are other split criteria which are defined as inactive until activated by a process variant. Note that for the test of an additionally activated split criterion you also have to prepare the business volume data accordingly with different values for the split criterion.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Purchasing Rebate Settlement | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Purchasing Rebate ManagementIn the items table, select the item with item name: Purchasing Rebate Settlement. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to the Define Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZP04 Split Criteria AdaptationChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: for example, 0PI1Note Add further condition contract types if you want to test the process variant for other purchasing rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate/Deactivate Split Criteria for Settlement | Double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: for example, 0PI1Field Name: select from field help list, for example, MATKLUsage as Split Criterion: select from the dropdown list as used or not used.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZP04 Split Criteria AdaptationChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contracy Type: for example, 0PI1Note Add further condition contract types if you want to test the process variant for other purchasing rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate/Deactivate Split Criteria for Settlement | Double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: for example, 0PI1Field Name: select from field help list, for example, MATKLUsage as Split Criterion: select from the dropdown list as used or not used.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

##### Define Process Variant for Business Volume Selection Criteria Usage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to change the usage of business volume selection criteria defined in the relevant set of field combinations.

To allow high flexibility in the business volume selection, the set of field combinations for purchasing rebate settlement provides many business volume selection criteria. However, this larger number can complicate the maintenance of business volume selection criteria in the condition contract as the user needs to find the desired field combination in a long list when he wants to enter a new line. With a suitable condition contract process variant, you can reduce the scope of business volume selection criteria to the relevant ones.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Purchasing Rebate Settlement | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Purchasing Rebate ManagementIn the items table, select the item with item name: Purchasing Rebate Settlement. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to the Define Contract Process Variant configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZP03 Selection Criteria AdaptationChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: for example, 0PI1Note Add further condition contract types if you want to test the process variant for other purchasing rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combination: Purchase RebateField Combination: select the criteria you want to hideUsage of Field Combination: Not Used as Business Volume Selection CriterionChoose Save. | The usage of field combination is changed with the process variant. |  |

|  |
| --- |
| Note If you use supplier invoices with lines for freight costs and you want to exclude freight costs from purchasing rebates, enter field combination 0061 Item Category of Supplier Invoice with usage Used as Business Volume Selection Criterion and specify this business volume selection criterion with initial value in a new condition contract. |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZP03 Selection Criteria AdaptationChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: for example, 0PI1Note Add further condition contract types if you want to test the process variant for other purchasing rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combination: Purchase RebateField Combination: select the criteria you want to hideUsage of Field Combination: Not Used as Business Volume Selection CriterionChoose Save. | The usage of field combination is changed with the process variant. |  |

|  |
| --- |
| Note If you use supplier invoices with lines for freight costs and you want to exclude freight costs from purchasing rebates, enter field combination 0061 Item Category of Supplier Invoice with usage Used as Business Volume Selection Criterion and specify this business volume selection criterion with initial value in a new condition contract. |

##### Define Process Variant to Configure Material Groups as Condition Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to change the usage of condition levels for condition records.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Purchasing Rebate Settlement | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Purchasing Rebate ManagementIn the items table, select the item with item name: Purchasing Rebate Settlement. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZP05 Condition Level AdaptationChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: for example, 0PI1Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Change the Usage of Condition Level | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries:Application:Cond.Type Group: 0P01Condition Type: for example, REJ1Table Number: for example, 4ABUsage of Condition Level: ActiveClick Enter and choose Save. | The usage of condition level is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZP05 Condition Level AdaptationChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: for example, 0PI1Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Change the Usage of Condition Level | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries:Application: VCond.Type Group: 0P01Condition Type: for example, REJ1Table Number: for example, 4ABUsage of Condition Level: ActiveClick Enter and choose Save. | The usage of condition level is changed with the process variant. |  |

##### Define Process Variant to Configure Settings for Fixed Amount Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to specify settings for fixed amount agreements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Purchasing Rebate Settlement | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Purchasing Rebate ManagementIn the items table, select the item with item name: Purchasing Rebate Settlement. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to the Define Contract Process Variant configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZP06 Fixed Amount AgreementAmount Split Across Periods: StandardIf you want to carry out cost recognition for fiscal periods, select the following two entries:No Accruals Reversal at Partial Settlement: <selected>Recognition Adjustment Active: <selected>Choose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0PF1, 0PF2 | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate Fixed Amount Settlement Proportionally Across Fiscal Periods (Optional) | If you want to settle the fixed amount proportionally across fiscal periods, you can activate the amount split function in the general settings.Double-click Condition Contract Types on the left of the screen.In the General Settings section, set the field Amount Split Periods Partial Settlement to Yes from the dropdown list. |  |  |
| 9 | Specify Plant | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: <your company code>, for example, 3310Plant for CO Data: <your plant for determine control data>, for example, 3310Choose Save. | The plant is specified for profit center. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZP06 Fixed Amount AgreementAmount Split Across Periods: StandardIf you want to carry out cost recognition for fiscal periods, select the following two entries:No Accruals Reversal at Partial Settlement: <selected>Recognition Adjustment Active: <selected>Choose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0PF1, 0PF2 | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Specify Plant | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: <your company code>, for example, 3310Plant for CO Data: <your plant for determine control data>, for example, 3310Choose Save. | The plant is specified for profit center. |  |

##### Define Process Variant Scale to Enable Selection of Different Bases for Rebate Calculation and Scale Determination

Purpose

In this activity, you define a condition contract process variant that enables the specification of business volume for rebates separately from the business volume used to determine the rebate scale. For example, if you have a range of products and want the rebate scale to be determined based on the transaction data from the entire range, while the rebate itself only applies to a specific subset of those products, you can achieve this by creating this process variant and utilizing it within the condition contract.

|  |
| --- |
| Note This step is prerequisite to execute [Purchase Rebate Processing with Different Bases for Rebate Calculation and Scale Determination](#unique_19) [page ] 89. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Purchasing Rebate Settlement | Enter the following filters:Application Area: Sourcing and ProcurementSub Application Area: Purchasing Rebate ManagementIn the items table, select the item with item name: Purchasing Rebate Settlement.. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZP07 Purchasing Rebates with different basesChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0PI3Choose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Define Selection Groups | Double-click on Selection Groups on the left of the screen.Choose New Entries and make the following entries:Profile: 0PI2 (Purchasing Rebate: Supplier Invoice,Good)Group: 0PRB (Rebate Base)Usage: 2 Use in Condition Contract SettlementMake the following entries for line 2:Profile: for example, 0PI2 (Purchasing Rebate: Supplier Invoice,GoodGroup: 0PSB (Scale Baes)Usage: 2 Use in Condition Contract SettlementIf you create for contract type 0PI1/0PI2/0PG1/0PG2, then you need to choose profile 0PI1. If you create for contract type 0PI3/0PI4/0PG3/0PG4, then you need to choose profile 0PI2.Choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Purchasing Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZP07 Purchasing Rebates with with different basesChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0PI3Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Define Selection Groups | Double-click on Selection Groups on the left of the screen.Choose New Entries and make the following entries:Profile: 0PI2Group: 0PRBUsage: 2 Use in Condition Contract Settlement Make the following entries for line 2:Profile: for example, 0PI2Group: 0PSBUsage: 2 Use in Condition Contract SettlementIf you create for contract type 0PI1/0PI2/0PG1/0PG2, then you need to choose profile 0PI1 or 0PG1. If you create for contract type 0PI3/0PI4/0PG3/0PG4, then you need to choose profile 0PI2 or 0PG2.Choose Save. | The split criteria usage is changed with the process variant. |  |

##### Maintain Automatic Account Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain automatic account determination for specific contract process variant.

|  |
| --- |
| Note If you assign the process variant to your condition contract, then the step is required if you need to settle the condition contract. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Chart of Accounts | Enter the following filters:Application Area: FinanceSub Application Area: General LedgerIn the items table, select the item with item name: Chart of Accounts. | The Configure Your Solution - Chart of Accounts screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Automatic Account Determination configuration step. | The Automatic Account Determination 1. Area screen displays. |  |
| 6 | Maintain G/L Account Assignment | On the Automatic Account Determination screen, make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L AccountsChoose Step 2 and make the following entries:Chart of Accounts: YCOAApplication: V Sales/DistributionCondition table: 016 Company Code / Contract Process Variant / Account KeyChoose Step 3.On the Automatic Account Determination screen, choose Add and make one or both of following entries according to your requirement:Line 1:Condition Type: KORP (Purchasing Rebate)Company Code: 3310Contract Process Var: for example, ZP01Account Key: 0P1(Purchasing Rebate)G/L Account:72532000Accruals Acc.: 21771000Line 2:Condition Type: KORP (Purchasing Rebate)Company Code: 3310Contract Process Var: for example, ZP01Account Key: 0P2(Pur Rebate GoodsRel)G/L Account:72531000Accruals Acc.: 21771000Choose Review.Choose Save. | The G/L account assignment is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Automatic Account Determination screen displays. |  |
| 3 | Go to Configuration Details | On the Automatic Account Determination screen, make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L accountsChoose Step 2 and make the following entries:Chart of Accounts: YCOAApplication: V Sales/DistributionCondition table: 016 Company Code / Contract Process Variant / Account KeyChoose Step 3.On the Automatic Account Determination screen, choose Add and make one or both of following entries according to your requirement:Line 1:Condition Type: KORP (Purchasing Rebate)Company Code: 3310Contract Process Var: for example, ZP01Account Key: 0P1(Purchasing Rebate)G/L Account:72532000Accruals Acc.: 21771000Line 2:Condition Type: KORP (Purchasing Rebate)Company Code: 3310Contract Process Var: for example, ZP01Account Key: 0P2(Pur Rebate GoodsRel)G/L Account:72531000Accruals Acc.: 21771000Choose Review.Choose Save. | The G/L account assignment is saved. |  |

#### Configure Flexible Workflow (Optional)

##### Manage Team and Responsibilities

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Procurement (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create a New Team | Choose Create. |  |  |
| 4 | Enter General Information | In the General Information section, make the following entries and choose Enter:Name: ZCCM_TEST_TEAM_MMDescription: Condition Contract Management Team PurchaseGlobal ID: ZCCM_TEST_TEAM_MMStatus: EnabledType: SCMTM Purchasing Condition Contract Team TypeChoose Enter.Go to Responsibility Definition area, and make the following entry:Condition Contract Category: 0P Purchasing Rebate |  |  |
| 5 | Add Team Members and Assign Function to Team Members | In the Team Members section, choose Create and make the following entry:Business Partner: select from F4 help, for example, search Last Name for PurchasingManager to get the User IDNote The user must be an employee user.In the Functions field, choose F4 to select.In the Select: Functions window, select the following two functions, and choose OK.Functions:SCCM_F1 Condition Contract Release ApprovalSCCM_F2 Condition Contract Settlement Release Approval | The Select: Business Partner screen displays. |  |
| 6 | Save Team for Condition Contract | Choose Create and choose Back to go back to Manage Teams and Responsibilities screen. | The team is saved. |  |
| 7 | Create Team and Responsibilities for Settlement | Choose Create. |  |  |
| 8 | Enter General Information | Make the following entries:Name: ZSTLM_TEST_TEAM_MMDescription: Settlement Management Team PurchaseStatus: EnabledType: SMPUR Purchasing Settlement Management Team TypeChoose Enter.Go to Responsibility Definitions and make the following entry:SettlmtDocType: <settlement document type used for workflow approval process>, for example, 0P11Note 0P11 is for condition contract type 0PI1/0PG1. 0P21 is for condition contract type 0PI2/0PG2. 0PA2 is for condition contract type 0PI3/0PG3. 0PB2 is for condition contract type 0PI4/0PG4.Note Please make sure that the related settlement document type is maintained so that the purchasing manager can approve the settlement document. | The team is created. |  |
| 9 | Add Team Members and Assign Function to Team Members | In the Team Members section, choose Create and make the following entry:Business Partner: select from F4 help, for example, search Last Name for PurchasingManager to get the User IDNote The user must be an employee user.In the Functions field, choose F4 to select.In the Select: Functions window, select the following function, and choose OK.Functions: STLMTAPR Settlement Document ApproverChoose Create to create the team. | The Select: Business Partner screen displays. And the team is saved. |  |
| 10 | Save Team for Condition Contract for Settlement | Choose Back to go back to Manage Teams and Responsibilities screen. |  |  |
| 11 | Check Team Status | On the screen Manage Teams and Responsibilities, verify the status of the team by selecting Enabled in field Status and choose Go.Ensure that your teams are in the list. | The team is ready to use. |  |

##### Manage Flexible Workflow for Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you configure your release conditions for release condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow | Select Workflows: Release Condition Contract. Choose Create, and make following entry:Workflow Name: Test Workflow for Release of Condition ContractUnder Steps, choose Create and make the following entry:Step Type: Release of Condition ContractUnder Recipients, make the following entry:Role: Condition Contract Release ApprovalUnder Exception Handling, make the following entries for Rework Condition Contract：Required Action: Rework of Condition ContractAction Result: Restart WorkflowChoose Create. Choose Save. | The workflow is created successfully. |  |
| 4 | Activate Workflow Item | Choose Back. Select the newly-created workflow item and choose Activate. | The workflow item is activated. |  |

##### Manage Flexible Workflow for Condition Contract Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you configure release conditions of condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow | Select Settlement Release of Condition Contract, and then choose Create, and make following entries:Workflow Name: Test Workflow for Settlement Release of Condition ContractSteps: CreateStep Type: Release of Condition Contract for SettlementRecipients: Role: Condition Contract Settlement Release ApprovalOn the Exception Handling tab, make following entries：Rework Condition Contract:Required Action: Rework of Condition Contract for Settlement ReleaseAction Result: Restart WorkflowChoose Create. Choose Save. | The workflow of condition contract settlement is configured. |  |
| 4 | Activate Workflow Item | Choose Back. Select the newly-created workflow item and choose Activate. | The workflow item is activated. |  |

##### Manage Flexible Workflow for Settlement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you configure release conditions for release settlement document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Settlement Documents (F3681). | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow | Choose Create, and make following entries:Workflow Name: Test Workflow for the approval of Settlement Document (To Accounting)Maintain Step Sequence 1:Steps: CreateStep Type: Release of Settlement DocumentRecipients: Role: Settlement Document ApproverChoose Create.Maintain Step Sequence 2:Steps: CreateStep Type: Automatic Change of Settlement Document StatusChoose Create. Choose Save. | The workflow of settlement document is configured. |  |
| 4 | Activate Workflow Item | Choose Back. Select the newly-created workflow item and choose Activate. | The workflow item is activated. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Goods Related A/P Settlement Based on Supplier Invoices](#unique_27) [page ] 47 |  |  |  |
| [Create Supplier Condition Contract](#unique_28) [page ] 47 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) | Condition contract is created. |
| [Check Business Volume (Optional)](#unique_29) [page ] 50 | Accounts Payable Accountant | Display Business Volume - Condition Contracts (WB2R_BUSVOL) | Supplier invoices or material documents from scope item no J45 appear in business volume. |
| [Delta Accruals Settlement (Optional)](#unique_30) [page ] 51 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | Accruals are posted according to the pricing conditions specified in the condition contract. |
| [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_31) [page ] 53 | Accounts Payable Accountant | Manage Settlement Documents (F3254) | Check the relevant Accounting document. |
| [Partial Settlement (Optional)](#unique_32) [page ] 54 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.Accounts Payable Accountantii) Customer Invoice (settlement document) is created, existing accruals are reversed |
| [Check Settlement Document for Partial Settlement (Optional)](#unique_33) [page ] 55 | Accounts Payable Accountant | Manage Settlement Documents (F3254) | Check the relevant Accounting document. |
| [Final Settlement](#unique_34) [page ] 57 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.ii) Customer invoice (settlement document) is created, existing accruals are reversed. |
| [Check Settlement Document for Final Settlement Document (Optional)](#unique_35) [page ] 59 | Accounts Payable Accountant | Manage Settlement Documents (F3254) | Check the relevant Accounting document. |
| [Service Related A/R Settlement Based on Supplier Invoices](#unique_36) [page ] 61 |  |  |  |
| [Create Supplier Condition Contract](#unique_37) [page ] 61 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) | Condition contract is created. |
| [Delta Accruals Settlement (Optional)](#unique_38) [page ] 62 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | Accruals are posted according to the pricing conditions specified in the condition contract. |
| [Partial Settlement (Optional)](#unique_39) [page ] 69 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.Accounts Payable Accountantii) Customer Invoice (settlement document) is created, existing accruals are reversed |
| [Final Settlement](#unique_40) [page ] 63 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.ii) Customer invoice (settlement document) is created, existing accruals are reversed. |
| [A/P and A/R Settlement Based on GR Material Documents](#unique_41) [page ] 63 |  |  |  |
| [Create Supplier Condition Contract](#unique_42) [page ] 63 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) | Condition contract is created. |
| [Delta Accruals Settlement (Optional)](#unique_43) [page ] 68 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | Accruals are posted according to the pricing conditions specified in the condition contract. |
| [Partial Settlement (Optional)](#unique_44) [page ] 67 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.Accounts Payable Accountantii) Customer Invoice (settlement document) is created, existing accruals are reversed |
| [Final Settlement](#unique_45) [page ] 67 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.ii) Customer invoice (settlement document) is created, existing accruals are reversed. |
| [Two-Step Processing for Settlement](#unique_46) [page ] 68 |  |  |  |
| [Create Supplier Condition Contract](#unique_47) [page ] 68 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) | Condition contract is created. |
| [Delta Accruals Settlement (Optional)](#unique_43) [page ] 68 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | Accruals are posted according to the pricing conditions specified in the condition contract. |
| [Partial Settlement (Optional)](#unique_39) [page ] 69 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.Accounts Payable Accountantii) Customer Invoice (settlement document) is created, existing accruals are reversed |
| [Collect Parked Settlement Documents from Partial Settlement (Optional)](#unique_48) [page ] 69 | Accounts Payable Accountant | Collect Settlement Documents (WZRC) | Collective Documents is created from Settlement Documents. |
| [Final Settlement](#unique_40) [page ] 63 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.ii) Customer invoice (settlement document) is created, existing accruals are reversed. |
| [Collect Parked Settlement Documents from Final Settlement](#unique_49) [page ] 70 | Accounts Payable Accountant | Collect Settlement Documents (WZRC) | Collective Documents is created from Settlement Documents. |
| [Purchasing Rebate Processing with Workflow](#unique_13) [page ] 71 |  |  |  |
| [Create Supplier Condition Contract](#unique_50) [page ] 72 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) | Condition contract is created. |
| [Request Approval to Release Condition Contract](#unique_51) [page ] 75 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) | The request for condition contract release is created. |
| [Trigger Rework of Condition Contract (Optional)](#unique_52) [page ] 76 | Purchasing Manager | My Inbox - All Items (F0862). | Trigger rework for the condition contract. |
| [Rework Condition Contract (Optional)](#unique_53) [page ] 77 | Purchaser | My Inbox - All Items (F0862). | Complete rework for the condition contract. |
| [Release Supplier Condition Contract](#unique_54) [page ] 78 | Purchasing Manager | My Inbox - All Items (F0862). | Supplier Condition Contract is released. |
| [Delta Accruals Settlement (Optional)](#unique_55) [page ] 78 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | Accruals are posted according to the pricing conditions specified in the condition contract. |
| [Request Release of Condition Contract for Settlement](#unique_56) [page ] 79 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) | Condition contract is saved. |
| [Release Supplier Condition Contract for Settlement](#unique_57) [page ] 80 | Purchasing Manager | My Inbox - All Items (F0862) | A supplier condition contract for settlement is released. |
| [Partial Settlement (Optional)](#unique_58) [page ] 80 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.Accounts Payable Accountantii) Customer Invoice (settlement document) is created, existing accruals are reversed |
| [Approve Release of Partial Settlement Document to Accounting (Optional)](#unique_59) [page ] 81 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Final Settlement](#unique_60) [page ] 81 | Accounts Payable Accountant | Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR) | i) Supplier credit memo (settlement document) is created, existing accruals are reversed.ii) Customer invoice (settlement document) is created, existing accruals are reversed. |
| [Approve Release of Final Settlement Document to Accounting](#unique_61) [page ] 82 | Purchasing Manager | My Inbox - All Items (F0862) | Settlement is approved. |
| [Final Settlement with Adjustments (Optional)](#unique_62) [page ] 95 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) |  |
| [Purchase Rebate Processing with Graduated Scale Determination](#unique_63) [page ] 82 |  |  |  |
| [Purchasing Rebate Processing – Fixed Amount Agreements](#unique_64) [page ] 83 |  |  |  |
| [Basic Processing](#unique_65) [page ] 84 | Purchaser | Manage Condition Contracts - Supplier Rebates (F6740) |  |
| [Cost Recognition for Fiscal Periods](#unique_66) [page ] 86 |  |  |  |
| [Fixed Amount Settlement Proportionally Across Fiscal Periods](#unique_67) [page ] 88 |  |  |  |
| [Fixed Amount Distribution to Business Objects](#unique_68) [page ] 88 |  |  |  |
| [Fixed Amount Settlement on Multiple Products](#unique_69) [page ] 89 |  |  |  |
| [Create Supplier Condition Contract](#unique_70) [page ] 90 | Purchaser |  |  |
| [Delta Accruals Settlement (Optional)](#unique_71) [page ] 93 |  |  |  |
| [Partial Settlement (Optional)](#unique_72) [page ] 94 |  |  |  |
| [Final Settlement](#unique_73) [page ] 94 |  |  |  |
| [Final Settlement with Adjustments (Optional)](#unique_62) [page ] 95 |  |  |  |
| [Reverse Settlement Documents - Condition Contracts (Optional)](#unique_74) [page ] 97 | Accounts Payable Accountant | Manage Condition Contracts - Supplier Rebates (F6740) |  |

## Test Procedures

This chapter comprises the test procedures for different purchasing rebates processing variants covered by this scope item. The variant differentiation results from two basic types of the rebate agreements, two different data sources, and two ways for the settlement procedure.

In the first type of rebate agreement you regard rebates as subsequent abatement of the purchase price for procured materials. In this case, you perform a so-called goods related settlement as accounts payable to create a credit memo with the supplier as payer. The taxation is consistent with the taxation in the procurement process. When in contrast the rebate agreement reflects a service rendered for the supplier you perform a settlement as account receivable to create an invoice for the supplier. The taxation for the rebate amount is carried out according to a service.

This scope item supports two data sources for the business volume determination: supplier invoices, usually applied for an amount based rebate calculation, and material documents of goods receipt postings usually applied for quantity or weight/volume based rebate calculation.

Another process variation concerns the transfer of settlement documents to accounting. Usually, you create settlement documents that are immediately released to accounting. But you can also apply an alternative settlement procedure when you have several purchasing rebate agreements with the same supplier. In the partial settlements and in the final settlement for the different condition contracts you first create so called parked settlement documents that are not transferred to accounting. In a second step you collect the parked settlement documents to create a collective settlement document which is then transferred in one journal entry to accounting. Thus you reduce the workload for the accounting module and you have the information for the purchasing rebates settlement with a supplier in one journal entry.

The test procedure for the different variants is very similar. To avoid unnecessary recurrences of identical test sequences we therefore decided for the following approach.

In the first section Goods Related A/P Settlement Based on Supplier Invoices, we describe the test sequence for the most important process variant – goods related A/P settlement based on supplier invoices with direct release of settlement document to accounting – in detail. This process variant is represented by condition contract type 0PI3. The description comprises the creation of the corresponding condition contract, the business volume control, the execution of the delta accruals, partial and final settlement, and guidelines for checking settlement results.

In the following sections we only describe the differences, and when test sequences are identical we refer to the first section. The second section Service Related A/R Settlement Based on Supplier Invoices deals with the second type of rebate agreement, supplier invoice as data source and immediate release of settlement document to accounting remain. The corresponding condition contract type is 0PI1. The main difference here is the taxation of the rebate amount and the type of the settlement document (invoice to supplier).

In the third section A/P and A/R Settlement based on GR Material Documents, we look at the two process variants for which material documents for goods receipt form the data source. We consider both types of rebate agreements with the direct release of settlement documents to accounting, condition contract types here are 0PG3 and 0PG1. In this section we also describe rebate conditions based on quantities.

The last section Two-Step Processing for Settlement is about the two-step settlement procedure for the four variants mentioned before. Related condition contract types are 0PI4, 0PI2, 0PG4, and 0PG2. We describe the specific step for the creation of the collective settlement document only once for the goods related A/P settlement based on supplier invoices. This step has to be executed similarly for the other three variants.

For each of these process variants you can also configure a workflow process. This is subject matter of section Purchasing Rebate Processing with Workflow. Again we only describe the specific steps in detail, for other test sequences we refer to the first section. And we only describe the procedure for the basic process variant, the workflow steps for the other seven process variants are identical.

Finally, we describe some special aspects with chapters Final Settlement with Adjustments, Purchasing Rebate Processing – Fixed Amount Agreements and Reverse Settlement Documents – Condition Contracts.

### Goods Related A/P Settlement Based on Supplier Invoices

This section describes the test sequence for the most important or basic variant for purchasing rebates processing – goods related A/P settlement based on supplier invoices with direct release of settlement documents to accounting. This process variant is represented by condition contract type 0PI3. In this process variant you regard rebates as subsequent abatement of the purchase price for procured materials. You perform a so-called goods related settlement as accounts payable to create a credit memo with the supplier as payer. The taxation for the rebate amount is consistent with the taxation in the procurement process as the tax code is copied from the business volume.

The detailed description comprises the creation of the corresponding condition contract, the business volume control, the execution of the delta accruals, partial and final settlement, and guidelines for checking settlement results.

As known, the purchasing rebates process runs in parallel to the regular procurement process. Accordingly, we recommend to create new supplier invoices (see chapter Prepare Transactional Data) between the different settlement runs to check the evolution of accruals and rebate amounts. For this, you can also repeat the delta accruals settlement and partial settlement processing step as described. To check that the taxation is consistent with the taxation in the procurement process prepare supplier invoices with materials that have a different tax classification so that the corresponding taxation varies.

#### Create Supplier Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for a supplier as condition contract partner.

Note

Please execute chapter [Prepare Transactional Data](#unique_7) [page ] 10 before or after you create a supplier condition contract, Or you can't settle the condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Supplier Rebates (F6740). | The Manage Condition Contracts - Supplier Rebates screen displays. |  |
| 3 | Create New Condition Contract | On the Manage Condition Contracts - Supplier Rebates screen, choose Create. | The Select Condition Contract Type screen displays. |  |
| 4 | Select Condition Contract Type for A/P Settlement | In the dialog box Select Condition Contract Type, select the following condition contract type:0PI3 Purchasing Rebate: Supplier Invc, Goods |  |  |
| 5 | Enter Condition Contract Details | On the Create Purchasing Rebate screen, make the following entries and choose Enter:Supplier: 33300010From: for example, <today's date>To: for example, <end of current year> | The screen title varies with the selected condition contract type. |  |
| 6 | Enter Organizational Data | On the Purchasing tab, make and check the following entries, and choose Enter:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310 |  |  |
| 7 | Maintain Header Text in Condition Contract (Optional) | On the Header Texts tab, choose value for following field and then choose Create Header Text:Text Type: <your text type>Language: <your language>For example, you can maintain your text for every text type as following:Internal Text: <your internal contract text>External Text: <your external contract text>Text for Settlement Document: <your contract text for settlement document> |  |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, select New Line, make the following entries and choose Enter.Field Combination: 0002 SupplierInclude/Exclude: InclusiveSupplier: 33300010Field Combination: 0009 MaterialInclude/Exclude: InclusiveMaterial: for example, TG0011 | If you performed the steps described in the prerequisite chapter: [Prepare Transactional Data](#unique_7) [page ] 10, enter here the supplier number that you used to create the purchase order.Optionally, you can specify further materials as selection criterion. |  |
| 9 | Enter Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts Payable |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line, make the following entries and choose Continue.Settlement Date: for example, <end of current year>Settlement Date Type: Final SettlementSelect New Line, make the following entries and choose Continue.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial Settlement (Optional)Select New Line, make the following entries and choose Continue.Settlement Date: for example, <today's date>Settlement Date Type: Delta Accruals (Optional)Note If you maintain settlement calendar for Partial Settlement, you must execute chapter [Partial Settlement (Optional)](#unique_32) [page ] 54 to do Partial Settlement before Final Settlement. | The creation of the line with Settlement Date Type: Delta accruals is optional.The creation of the line with Settlement Date Type: Partial settlement is optional. |  |
| 11 | Enter Condition Data for Rebate Condition | In the Conditions area, make the following entry:Condition Table: Condition ContractSelect New Condition, make the following entries, and then choose Enter.Condition Type: RES1 RebateCalculation Type: for example, PercentageValid From: for example, <today's date>Valid To: for example, <end of current year>Condition Rate: for example, <1>Scale Type: Base scaleScale Basis Type: Value scaleNote In the condition contract maintenance, you can choose the calculation type for the rebate and accruals conditions. However, note that the calculation type for a settlement based on supplier invoices is usually Percentage. For a settlement based on material documents, you usually use Quantity, Net Weight, Gross Weight, Volume, or Points as the calculation type. Other calculation types are not suitable. | This condition is used to calculate the rebate amount.You can also choose Condition Contract / Material as the condition level. You then also specify the material for a condition record.If the Valid From and Valid To dates have been copied from the condition contract validity according to the user settings, you can check and change these dates if required. |  |
| 12 | Enter Scale Data (Optional) | Select the condition line, choose New Scale Level, make the following entries, and then choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1>Select the first created condition line, choose New Scale Level, make the following entries, and then choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> | The condition rate, condition currency, pricing unit, and unit of measure are copied from the condition line. Only the condition rate is ready for input. |  |
| 13 | Enter Condition Data for Accruals Condition (Optional) | In the Conditions area, select New Condition, make the following entries and then choose Enter.Condition Type: REA1 Rebate AccrualsCalculation Type: for example, PercentageCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <end of current year> | This condition is used to calculate the amount for accruals.If the Valid From and Valid To dates have been copied from the condition contract validity according to the user settings, you can check and change these dates if required. |  |
| 14 | Release Condition Contract | Choose Release. |  |  |
| 15 | Save Condition Contract | Choose Save. Make a note of the condition contract number: __________. |  |  |

#### Check Business Volume (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the business volume for the supplier condition contract.

Note

You can repeat this process step at every point in time in the test procedure. It’s recommendable to check the business volume before you start a settlement run to enable a control of the business volume determined for a settlement document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Business Volume - Condition Contracts (WB2R_BUSVOL). | The Business Volume for Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Business Volume for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract created in the previous step>Business Volume Base: From ContractOutput Level Business Volume: Settlement Date |  |  |
| 4 | Check Business Volume for Condition Contracts | Choose Execute. | The system displays the business volume.Business volume value REBV is determined from the previously created supplier invoices. |  |

#### Delta Accruals Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a delta accruals settlement for the supplier condition contract. With this delta accruals settlement you post accruals for the supplier invoice documents related to the condition contract.

Prerequisites

Perform this step if you have executed the [Prepare Transactional Data](#unique_7) [page ] 10 for the supplier condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Settle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR).. | The Settlement of Supplier Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Settlement of Supplier Condition Contracts screen，make the following entries：Settlement Date: for example, <today's date>Settlement Date Type: 3 Delta AccrualsCondition Contract: <number of condition contract created in the previous step>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunFilter: No Filter |  |  |
| 4 | Execute | Choose Execute.Choose Continue to display the settlement document. | The Log for Supplier Condition Contract settlement screen displays to show information 1 contracts settled without errors. Choose Continue to show Condition Contract Settlement Messages.Settlement document for delta accruals is created. |  |

#### Check Settlement Document for Delta Accruals Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the settlement document and accounting document for the delta accruals settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Documents screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the delta accruals settlement and click the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transfer to Accounting. | The posting status is C (Accounting document has been created). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data, check the reference information. | Field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Document Items | Under Items, check the items of the settlement documents.Click an item in the table. | The system has created the items according to the split criteria. |  |
| 7 | Check Pricing of Items | On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat step 6 and 7 for all items. | The system has determined the relevant business volume and displays it for condition type REBV Rebate Bus Volume.The system has calculated the accruals amount with the relevant conditions maintained in the condition contract. |  |

Journal entry:

A/P Settlement:

| Supplier | Revenue Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010or any other supplier used for the purchasing rebate processing. | 72531000 Gain from Supplier Rebate (MM) | 21771000 Accrued Supplier Rebate | n/a |

#### Partial Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a partial settlement for the supplier condition contract. In this step you also reverse the accruals posted before.

Prerequisites

Perform this step if you have executed the chapter [Prepare Transactional Data](#unique_7) [page ] 10.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access Condition Contract Settlement | OpenSettle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR). | The Settlement of Condition Customer Contracts screen displays. |  |
| 3 | Process Partial Settlement for Condition Contract | On the Settlement of Supplier Condition Contracts screen, make the following entries:.Settlement Date: <settlement date according to settlement calendar>Settlement Date Type: 1 Partial SettlementCondition Contract: <number of condition contract(s) created in the previous step>Posting Date: for example, <tomorrow's date>Document Date: for example, <tomorrow's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunFilter: No FilterChoose Execute.Choose Continue to display the settlement document.Take a note of the number of the settlement document created. | The Log for Supplier Condition Contract settlement screen displays. Supplier invoice (A/R settlement) is created. Accruals are reversed. |  |

#### Check Settlement Document for Partial Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the settlement document and accounting document for partial settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Settlement Document: Display screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the partial settlement and click the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transfer to Accounting. | The posting status is C (Accounting document has been created). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data , check the reference information. | Field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Partner Data | Under Partner Data, check the Partner information. |  |  |
| 7 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 8 | Check Pricing of Items | Click an item in the table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat step 6 and 7 for all items. | The system has determined the relevant business volume and displays it for condition type REBV Rebate Business Volume. The system has calculated the rebate amount with condition type RES1 maintained in the condition contract and the input tax with the percentage for full tax. The system shows the amount of reversed accruals for condition type REA2 and the amount for excess accruals for condition type REA5. |  |
| 9 | Check Output | Under Output Items, check the output items. Choose Display Document for an item to display the output print form. |  |  |
| 10 | Check Text of Settlement Document | Choose Back to screen Manage Settlement Documents.Choose your settlement document number and choose Display Settlement Document.On the screen Display Purchase Rebate Account Receivable (0P15) 6XXXXXXXXX, choose your settlement document and choose Header Texts.Choose tab Texts to check your text. |  |  |

Journal entry:

A/P Settlement:

| Supplier | Gain Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010 or any other supplier used for the purchasing rebate processing. | 72531000 Gain from Supplier Rebate (MM) | 21771000 Accrued Supplier Rebate | 12600000 Input Tax (VST) |

#### Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a final settlement for the supplier condition contract.

Prerequisites

Perform this step if you have executed the chapter [Prepare Transactional Data](#unique_7) [page ] 10 for the supplier condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access Condition Contract Settlement | OpenSettle Condition Contracts - Supplier Rebates(WB2R_SV_SUPR). | The Settlement of Supplier Condition Contracts screen displays. |  |
| 3 | Process Final Settlement for Condition Contract | On the Settlement of Supplier Condition Contracts screen, make the following entries and choose Execute.Settlement Date: for example, <end of current year>Settlement Date Type: Final SettlementCondition Contract: <number of condition contract created in the previous step>Please make sure the settlement date of every settlement data type is the same as the settlement data of condition contract.Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunFilter: No FilterChoose Continue to display the settlement document.Take a note of the number of the settlement document created. | The Log for Supplier Condition Contract settlement screen displays. Supplier invoice (A/R settlement) is created. Accruals are reversed. |  |
| 4 | Open Text in Settlement Document (Optional) | Navigate to the home page.In the Purchasing Rebate Processing section, choose Change Settlement Document.Enter the settlement document number and choose Continue.Choose Header Texts. |  |  |
| 5 | Maintain Text in Settlement Document (Optional) | You should see the following text types:Internal TextExternal Text for Output/FormsContract Text for Output/FormsDouble-click text type Contract Text for Output/Forms, you should see the text for settlement document which you have maintained in the condition contract for text type Text for Settlement Document English.You can add additional line of text: for example, <my additional comment to the contract text in the partial settlement document>You can also maintain Internal Text or External Text for Output/Forms for this settlement document. |  |  |

#### Check Settlement Document for Final Settlement Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the settlement document and accounting document for final settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Settlement Document: Display screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the partial settlement and click the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transfer to Accounting. | The posting status is C (Accounting document has been created). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data , check the reference information. | Field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Partner Data | Under Partner Data, check the partner information. |  |  |
| 7 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 8 | Check Pricing of Items | Click an item in the table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat step 6 and 7 for all items. | The system has determined the relevant business volume and displays it for condition type REBV Rebate Business Volume. The system has calculated the rebate amount with condition type RES1 maintained in the condition contract and the input tax with the percentage for full tax. The system shows the amount of reversed accruals for condition type REA2 and the amount for excess accruals for condition type REA5. |  |
| 9 | Check Output | Under Output Items, check the output items. Choose Display Document for an item to display the output print form. |  |  |
| 10 | Check Text of Settlement Document | Choose Back to screen Manage Settlement Documents.Choose your settlement document number and choose Display Settlement Document.On the screen Display Purchase Rebate Account Receivable (0P15) 6XXXXXXXXX, choose your settlement document and choose Header Texts.Choose tab Texts to check your text. |  |  |

Journal entry:

A/R Settlement:

| Supplier | Revenue Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010 or any other supplier used for the purchasing rebate processing. | 72531000 Gain from Supplier Rebate (MM) | 21771000 Accrued Supplier Rebate | 12600000 Input Tax (VST) |

### Service Related A/R Settlement Based on Supplier Invoices

This section deals with the first process variant for purchasing rebates processing – service related A/R settlement based on supplier invoices with direct release of settlement documents to accounting. This process variant is represented by condition contract type 0PI1. In contrast to basic process variant you regard the rebate agreement as a service rendered for the supplier. Accordingly, you perform a settlement as account receivable to create an invoice for the supplier. The taxation for the rebate amount is carried out according to a service.

The test procedure is very similar to the basic process variant so that we only describe the differences. Focal point is to check the different type of the settlement document (invoice to supplier instead of credit memo) and the different taxation of the rebate amount.

#### Create Supplier Condition Contract

Please refer to chapter [Create Supplier Condition Contract](#unique_28) [page ] 47 to create supplier condition contract for Service Related A/R Settlement Based on Supplier Invoices except for the following two fields:

1. Supplier Condition Contract Type. Please select condition contract type 0PI1 of condition contract for Service Related A/R Settlement Based on Supplier Invoices.
2. Settlement Data. On the Settlement Data tab page, the value of Settlement Type Supplier should be: As Accounts Receivable.

#### Delta Accruals Settlement (Optional)

Please refer to steps in chapter [Delta Accruals Settlement (Optional)](#unique_30) [page ] 51 with the condition contract you created in chapter [Service Related A/R Settlement Based on Supplier Invoices](#unique_36) [page ] 61.

After processing the delta accruals settlement, you can optionally check the settlement documents refer to chapter [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_31) [page ] 53.

Journal entry:

A/R Settlement:

| Supplier | Revenue Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010or any other supplier used for the purchasing rebate processing. | 72532000 Gain from Supplier Rebate (SD) | 21771000 Accrued Supplier Rebate | n/a |

#### Partial Settlement (Optional)

Please refer to the steps of chapter [Partial Settlement (Optional)](#unique_32) [page ] 54 to do partial settlement for your condition contract. In this step, you also reverse the accruals posted before.

After processing the partial settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Partial Settlement (Optional)](#unique_33) [page ] 55.

Journal entry:

A/R Settlement:

| Supplier | Revenue Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010or any other supplier used for the purchasing rebate processing. | 72532000 Gain from Supplier Rebate (SD) | 21771000 Accrued Supplier Rebate | 22000000 Output tax (MWS) |

#### Final Settlement

Please refer to [Final Settlement](#unique_34) [page ] 57 to do final settlement for your condition contract.

After processing the final settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Final Settlement Document (Optional)](#unique_35) [page ] 59.

Journal entry:

A/R Settlement:

| Supplier | Revenue Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010or any other supplier used for the purchasing rebate processing. | 72532000 Gain from Supplier Rebate (SD) | 21771000 Accrued Supplier Rebate | 22001000 Sales Tax Accrued |

### A/P and A/R Settlement Based on GR Material Documents

This section deals with two process variants that use another data source to determine the relevant business volume: material documents for goods receipt postings related to purchase orders. Similar to the first two test procedure sections, you can perform a settlement as accounts payable, represented by condition contract type 0PG3, or a settlement as accounts receivables, represented by condition contract type 0PG1, according to the character of the rebate agreement. Again, the test procedure is very similar to the basic process variant. As a main difference, we describe how you maintain the rebate condition for a quantity based rebate calculation, which is often applied in case of GR material documents as data source.

#### Create Supplier Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for a supplier. The condition contract is settled based on GR material document.

Note

Please execute chapter [Prepare Transactional Data](#unique_7) [page ] 10 before or after you create a supplier condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Supplier Rebates (F6740). | The Manage Condition Contracts - Supplier Rebates screen displays. |  |
| 3 | Create New Condition Contract | On the Manage Condition Contracts - Supplier Rebates screen, choose Create. | The Select Condition Contract Type screen displays. |  |
| 4 | Select Condition Contract Type for A/P Settlement | In the dialog box Select Condition Contract Type, select one of the following Condition Contract Types:0PG1 Purchasing Rebate:Good Receipt0PG3 Purchasing Rebate:Good Receipt, Goods |  |  |
| 5 | Enter Condition Contract Details | On the Create Purchasing Rebate screen, make the following entries and choose Enter:Supplier: 33300010From: for example, <today's date>To: for example, <end of current year> | The screen title varies with the selected condition contract type. |  |
| 6 | Enter Organizational Data | On the Purchasing tab page, make and check the following entries, and choose Enter:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310If you create with condition contract type 0PG1, on the Sales tab, make the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 7 | Maintain Header Text in Condition Contract (Optional) | On the Header Texts tab page, choose text types along with a corresponding language, and then choose Create Header Text:Language: <your language>Internal Text: <your internal contract text>External Text: <your external contract text>Text for Settlement Document: <contract text for settlement document> |  |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, select New Line, make the following entries and choose Enter.Field Combination: 0002 SupplierInclude/Exclude: InclusiveSupplier: 33300010Field Combination: 0009 MaterialInclude/Exclude: InclusiveMaterial: for example, TG0011 | If you performed the steps described in the prerequisite chapter: [Prepare Transactional Data](#unique_7) [page ] 10, enter here the supplier number that you used to create the purchase order.Optionally, you can specify further materials as selection criterion. |  |
| 9 | Enter Settlement Data | On the Settlement Data tab page, check the following entry:Condition contract type with A/P settlement (condition contract type 0PG3)Settlement Type Supplier: As Accounts PayableorCondition contract type with A/R settlement (condition contract type 0PG1)Settlement Type Supplier: As Accounts Receivable |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab page, select New Line, make the following entries.Settlement Date: for example, <end of current year>Settlement Date Type: Final SettlementChoose Continue.Select New Line, make the following entries.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial Settlement (Optional)Choose Continue.Select New Line, make the following entries.Settlement Date: for example, <today's date>Settlement Date Type: Delta Accruals (Optional)Choose Continue.Note If you maintain settlement calendar for Partial Settlement, you must execute chapter [Partial Settlement (Optional)](#unique_44) [page ] 67 to do Partial Settlement before Final Settlement. | The creation of the line with Settlement Date Type: Delta accruals is optional.The creation of the line with Settlement Date Type: Partial settlement is optional. |  |
| 11 | Enter Condition Data for Rebate Condition | In the Conditions area, make the following entries:Condition Table: Condition ContractSelect New Condition, make the following entries, and then choose Enter.Condition Type: RES1 RebateValid From: for example, <today's date>Valid To: for example, <end of current year>Calculation Type: for example, QuantityCondition Rate: for example, <1>Condition Currency: AEDPricing Unit: 1Unit of Measure: PCScale Type: Base scaleScale Basis Type: Quantity scaleNote In the condition contract maintenance, you can choose the calculation type for the rebate and accruals conditions. However, note that the calculation type for a settlement based on supplier invoices is usually Percentage. For a settlement based on material documents, you usually use Quantity, Net Weight, Gross Weight, Volume, or Points as the calculation type. Other calculation types are not suitable. | This condition is used to calculate the rebate amount.You can also choose Condition Contract / Material as the condition level. You then also specify the material for a condition record.If the Valid From and Valid To dates have been copied from the condition contract validity according to the user settings, you can check and change these dates if required. |  |
| 12 | Enter Scale Data (Optional) | Select the condition line, choose New Scale Level, make the following entries, and then choose Enter.Scales: for example, <1000>Scale UoM: PCCondition Rate: for example, <1>Select the first created condition line, choose New Scale Level, make the following entries, and then choose Enter.Scales: for example, <2000>Scale UoM: PCCondition Rate: for example, <2> | The condition rate, condition currency, pricing unit, and unit of measure are copied from the condition line. Only the condition rate is ready for input. |  |
| 13 | Enter Condition Data for Accruals Condition (Optional) | In the Conditions area, select New Condition, make the following entries and then choose Enter.Condition Type: REA1 Rebate AccrualsValid From: for example, <today's date>Valid To: for example, <end of current year>Calculation Type: for example, QuantityCondition Rate: for example, <2>Condition Currency: AEDPricing Unit: 1Unit of Measure: PC | This condition is used to calculate the amount for accruals.If the Valid From and Valid To dates have been copied from the condition contract validity according to the user settings, you can check and change these dates if required. |  |
| 14 | Release Condition Contract | Choose Release. |  |  |
| 15 | Save Condition Contract | Choose Save. Make a note of the condition contract number: __________. |  |  |

#### Delta Accruals Settlement (Optional)

Please refer to steps in chapter [Delta Accruals Settlement (Optional)](#unique_30) [page ] 51 with the condition contract you created for [A/P and A/R Settlement Based on GR Material Documents](#unique_41) [page ] 63.

After processing the delta accruals settlement, you can optionally check the settlement documents refer to chapter [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_31) [page ] 53.

#### Partial Settlement (Optional)

Please refer to the steps of chapter [Partial Settlement (Optional)](#unique_32) [page ] 54 to do partial settlement for your condition contract. After processing the partial settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Partial Settlement (Optional)](#unique_33) [page ] 55.

#### Final Settlement

Please refer to [Final Settlement](#unique_34) [page ] 57 to do final settlement for your condition contract.

After processing the final settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Final Settlement Document (Optional)](#unique_35) [page ] 59.

### Two-Step Processing for Settlement

The Two-Step Purchasing Rebates Processing describes an alternative settlement procedure when you have several purchasing agreements (condition contracts) with the same supplier. In the partial settlements and in the final settlement for the different condition contracts you first create so called parked settlement documents that are not transferred to accounting. In a second step you collect the parked settlement documents to create a collective settlement document which is then transferred in one journal entry to accounting. Thus you reduce the workload for the accounting module and you have the information for the purchasing rebate processing with a supplier in one journal entry.

In the following, we describe the two-step processing for the goods related settlement as accounts payable based on supplier invoices represented by condition contract type 0PI4. The two-step processing for the other two purchasing rebate scenarios runs in a similar way.

#### Create Supplier Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Please refer to chapter [Create Supplier Condition Contract](#unique_28) [page ] 47 to create supplier condition contract except for the following fields:

For Two Step Processing - Goods Related A/P Settlement Based on Supplier Invoice or GR Material Documents:

1. Supplier Condition Contract Type. Please select condition contract type 0PI4 (based on supplier invoice) or 0PG4 (based on GR material documents) of condition contract for Goods Related A/P Settlement based on supplier invoice or GR material documents.

For Two Step Processing - Service Related A/R Settlement Based on Supplier Invoice or GR Material Documents:

1. Supplier Condition Contract Type. Please select condition contract type 0PI2 (based on supplier invoice) or 0PG2 (based on GR material documents) of condition contract for Service Related A/R Settlement based on supplier invoice or GR material documents.
2. Settlement Data. On the Settlement Data tab page, the value of Settlement Type Supplier should be: As Accounts Receivable.

#### Delta Accruals Settlement (Optional)

Please refer to steps in chapter [Delta Accruals Settlement (Optional)](#unique_30) [page ] 51 with the condition contract you created for [A/P and A/R Settlement Based on GR Material Documents](#unique_41) [page ] 63.

After processing the delta accruals settlement, you can optionally check the settlement documents refer to chapter [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_31) [page ] 53.

#### Partial Settlement (Optional)

Please refer to the steps of chapter [Partial Settlement (Optional)](#unique_32) [page ] 54 to do partial settlement for your condition contract. After processing the partial settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Partial Settlement (Optional)](#unique_33) [page ] 55.

#### Collect Parked Settlement Documents from Partial Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you use the 2-step condition contract, the reversal of the accruals together with the customer revenues for the partial settlements is not posted until the creation of the collective settlement document.

Prerequisites

Perform this step if you have executed the chapter [Partial Settlement (Optional)](#unique_39) [page ] 69 for Condition Contract type 0PI2 or 0PG2.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the App | Open Collect Settlement Documents (WZRC). |  |  |
| 3 | Create Collective Documents | On the Create Collective Document from Settlement Documents screen, make the following entries and choose Execute.Document Numbers: <numbers of settlement documents 61XXXXXXXX for partial settlements created before>Check Run Only: <do not select>Choose Execute. | The Create Collective Documents from Settlement Documents screen displays. |  |

|  |
| --- |
| Note After creating collective document from partial settlement, you can optionally check the settlement document. Refer to chapter [Check Settlement Document for Partial Settlement (Optional)](#unique_33) [page ] 55. |

#### Final Settlement

Please refer to [Final Settlement](#unique_34) [page ] 57 to do final settlement for your condition contract.

After processing the final settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Final Settlement Document (Optional)](#unique_35) [page ] 59.

#### Collect Parked Settlement Documents from Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you use the 2-step condition contract, the reversal of the accruals together with the customer revenues for the final settlements is not posted until the creation of the collective settlement document.

Prerequisites

Perform this step if you have executed the chapter Final Settlement for Condition Contract of type 0PI2/0PI4 or 0PG2/0PG4.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the App | Open Collect Settlement Documents (WZRC). |  |  |
| 3 | Create Collective Documents | On the Collective Document from Settlement Documents screen, make the following entries and choose Execute.Document Numbers: <numbers of settlement documents 6XXXXXXXXX for final settlements created before>Check Run Only: <do not select>Choose Execute.. | The Create Collective Documents from Settlement Documents screen displays. |  |

|  |
| --- |
| Note After creating collective document from final settlement, you can optionally check the settlement document. Refer to chapter [Check Settlement Document for Final Settlement Document (Optional)](#unique_35) [page ] 59. |

### Purchasing Rebate Processing with Workflow

In each of cases described in previous chapter, you can configure a workflow process. In the following we describe the procedure for the settlement as account receivable.

Prerequisite

Please make sure to execute the following steps to activate flexible workflow for purchasing rebate processing:

1. Execute chapter [Define Process Variant for Using Flexible Workflow](#unique_12) [page ] 13.
2. Execute chapter [Maintain Automatic Account Determination](#unique_20) [page ] 31.
3. Execute chapter [Configure Flexible Workflow (Optional)](#unique_21) [page ] 35.
4. In step 6 of chapter [Create Supplier Condition Contract](#unique_50) [page ] 72, you need to assign the process variant to your condition contract.

#### Create Supplier Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Note

Please execute chapter [Prepare Transactional Data](#unique_7) [page ] 10 before or after you create a supplier condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Supplier Rebates (F6740). | The Manage Condition Contracts - Supplier Rebates screen displays. |  |
| 3 | Create New Condition Contract | On the Manage Condition Contracts - Supplier Rebates screen, choose Create. | The Select Condition Contract Type screen displays. |  |
| 4 | Select Condition Contract Type for A/R Settlement | In the dialog box Select Condition Contract Type, select the following Condition Contract Type:0PI1 Purchasing Rebate: Supplier Invoice |  |  |
| 5 | Enter Condition Contract Details | On the Create Purchasing Rebate: Supplier Invoice screen, make the following entries and choose Enter:Supplier: 33300010From: for example, <today's date>To: for example, <end of current year> | The screen title varies with the selected condition contract type. |  |
| 6 | Maintain Basic Data | On the Basic Data tab page, enter the following data and choose Enter.Process Variant: the process variant maintained in chapter [Define Contract Process Variants](#unique_11) [page ] 13, for example, <ZP01> |  |  |
| 7 | Enter Organizational Data | On the Purchasing tab page, make and check the following entries, and choose Enter:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310On the Sales tab, make the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00 | The sales area data entered on the Sales tab page are required to create the invoice settlement document for the supplier. |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, select New Line, make the following entries and choose Enter.Field Combination: 0002 SupplierInclude/Exclude: InclusiveSupplier: 33300010Field Combination: 0009 MaterialInclude/Exclude: InclusiveMaterial: for example, TG0011 | If you performed the steps described in the prerequisite chapter [Prepare Transactional Data](#unique_7) [page ] 10, enter here the supplier number that you used to create the purchase order.Optionally, you can specify further materials as selection criterion. |  |
| 9 | Enter Settlement Data | On the Settlement Data tab page, check the following entry:Settlement Type Supplier: As Accounts Receivable |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab page, select New Line, make the following entries and choose Enter.Settlement Date : for example, <end of current year>Settlement Date Type: Final SettlementChoose Continue.Select New Line, make the following entries and choose Enter.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementChoose Continue.Select New Line, make the following entries and choose Enter.Settlement Date: for example, <today's date>Settlement Date Type: Delta Accruals | The creation of the line with Settlement Date Type: Delta accruals is optional.The creation of the line with Settlement Date Type: Partial settlement is optional. |  |
| 11 | Enter Condition Data for Rebate Condition | In the Conditions area, make the following entry:Condition Table: Condition ContractSelect New Condition, make the following entries, and then choose Enter.Condition Type: RES1 RebateCalculation Type: for example, PercentageCondition Rate: for example, <1>Valid From: for example, <today's date>Valid To: for example, <end of current year>Scale Type: Base scaleScale Basis Type: Value scaleNote The calculation type for a settlement based on supplier invoices is usually Percentage. For a settlement based on material documents, you usually use Quantity, Net Weight, Gross Weight, Volume, or Points as the calculation type. Other calculation types are not suitable. | This condition is used to calculate the rebate amount.You can also choose Condition Contract / Material as the condition level. You then also specify the material for a condition record.If the Valid From and Valid To dates have been copied from the condition contract validity according to the user settings, you can check and change these dates if required. |  |
| 12 | Enter Scale Data (Optional) | Select the condition line, choose New Scale Level, make the following entries, and then choose Enter.Scales: for example, <1000>Condition currency: AEDCondition Rate: for example, <1%>Select the first created condition line, choose New Scale Level, make the following entries, and then choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> | The condition rate, condition currency, pricing unit, and unit of measure are copied from the condition line. Only the condition rate is ready for input. |  |
| 13 | Enter Condition Data for Accruals Condition | In the Conditions area, select New Condition, make the following entries and then choose Enter.Condition Type: REA1 Rebate AccrualsCalculation Type: for example, PercentageCondition Rate: for example, <2>Valid From: for example, <today's date>Valid To: for example, <end of current year> | This condition is used to calculate the amount for accruals.If the Valid From and Valid To dates have been copied from the condition contract validity according to the user settings, you can check and change these dates if required. |  |
| 14 | Save Condition Contract | Choose Save. Make a note of the condition contract number: __________. |  |  |

#### Request Approval to Release Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request a rebate condition contract for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Supplier Rebates (F6740). | The Manage Condition Contracts - Supplier Rebates screen displays. |  |
| 3 | Lock Settlement for Condition Contract | In the Condition Contracts table, find the condition contract that you want to request an approval for release.Click on the condition contract number and choose Change Condition Contract.On the Change Condition Contract screen, choose Edit → Lock Settlement. |  |  |
| 4 | Request Release of Condition Contract | Choose Edit → Request Approval.Choose Save. | The status for the condition contract is changed to:Settlement Lock Status: LockedStatus: NewNow the request to release the condition contract goes to Purchasing Manager's Inbox. |  |

#### Trigger Rework of Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check a rebate condition contract and send it back for rework.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Display the Relevant Condition Contract and Check the Status | Find the condition contract for which Purchaser has just requested the approval for release: Release Condition Contract XXXXXXXXXX.Check the current status of the condition contract. | The details of the condition contract display on the right of the screen.The current status of the condition contract displays as follows:Settlement Lock Status: LockedStatus: New |  |
| 4 | Send Back for Rework | If you request Purchaser to change the condition contract, choose Rework at the bottom of the screen.In the Submit Decision dialog box, enter a decision note and choose Submit. | The condition contract is sent back to Purchaser. |  |

#### Rework Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you rework on a rebate condition contract to change some value, for example, settlement date or rebate percentage.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The Condition Contract screen displays. |  |
| 3 | Check the Notification and Go to Change Mode | Choose Rework Condition Contract XXXXXXXXXX on the left of the screen.Choose Show Details at right bottom of the screen. Under the Comments tab, there is a message from the Purchasing Manager.Choose Hide Details at the bottom and choose More Details on the upper right of the screen.On the Display Purchasing Rebate: Supplier Invoice screen, choose Menu > Condition Contract > Change . | You check the comment from the Purchasing Manager and go to the change mode for condition contract. |  |
| 4 | Change Condition Contract | Change the condition contract according to the request of the Purchasing Manager.Choose Save.Choose Continue in the pop-up window. |  |  |
| 5 | Complete Rework for the Condition Contract | Choose Rework Completed at the bottom.In the Submit Decision dialog box, enter a decision note if needed.Choose Submit. | The condition contract is sent to Purchasing Manager for release approval again. |  |

#### Release Supplier Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you approve the release of the supplier condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Purchasing Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The Condition Contract screen displays. |  |
| 3 | Release Condition Contract | Find the condition contract for which Purchaser has just requested an approval for release: Release Condition Contract XXXXXXXXXX.Choose Release at the bottom of the screen.In the Submit Decision dialog box, enter a decision note if needed and choose Submit. | The condition contract is released now. |  |

#### Delta Accruals Settlement (Optional)

Please follow the steps in chapter [Delta Accruals Settlement (Optional)](#unique_30) [page ] 51 with the condition contract you create previously.

After processing the delta accruals settlement, you can optionally check the settlement documents refer to chapter [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_31) [page ] 53.

#### Request Release of Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the condition contract is set as locked for settlement, you need to request approval for this condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Supplier Rebates (F6740). | The Manage Condition Contracts - Supplier Rebates screen displays. |  |
| 3 | Change Condition Contract | On the Manage Condition Contracts - Supplier Rebates screen, choose your condition contract and choose Change Condition Contract. |  |  |
| 4 | Request Settlement Approval | On the Change Condition Contract screen, choose Edit → Request Settlement Approval. | The status for condition contract now should be:ReleasedLocked for SettlementSettlement Approval Requested |  |
| 5 | Save Condition Contract | Save condition contract. |  |  |

#### Release Supplier Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a supplier condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of previously created condition contracts is displayed. |  |
| 3 | Release Condition Contract for Settlement | Find the condition contract for which Purchaser has just requested for release the settlement.Select Release Condition Contract XXXXXXXXXX for Settlement and choose Release at right bottom of the screen. |  |  |
| 4 | Enter Release Reason | In the Submit Decision dialog box, enter a decision note if needed, and then choose Submit. | The condition contract is now released for settlement. |  |

#### Partial Settlement (Optional)

Please follow the steps in chapter [Partial Settlement (Optional)](#unique_32) [page ] 54 with the condition contract you created previously.

#### Approve Release of Partial Settlement Document to Accounting (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you approve the release of the settlement document to accounting and the journal entry document is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of previously created condition contract is displayed. |  |
| 3 | Approve Release to Accounting | Find the settlement document for which the release to accounting has to be approved. The approval was triggered automatically after the settlement has been processed by the Accounts Payable Accountant.Select the item Approve Settlement Document XXXXXXXXXX and choose Approve at right bottom of the screen.Enter comment if needed, and then choose Submit. | After processing the partial settlement, you can optionally check the settlement documents refer to chapter [Check Settlement Document for Partial Settlement (Optional)](#unique_33) [page ] 55.The settlement document is now released to accounting. |  |

Note

As workflow for settlement document is active, the Journal entry for settlement will only be generated after you perform this step. After you approve the partial settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Partial Settlement (Optional)](#unique_33) [page ] 55.

#### Final Settlement

Please refer to [Final Settlement](#unique_34) [page ] 57 to do final settlement for your condition contract.

#### Approve Release of Final Settlement Document to Accounting

Please refer to the steps in chapter [Approve Release of Partial Settlement Document to Accounting (Optional)](#unique_59) [page ] 81 to approve final settlement document.

Note

After you approve the final settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Final Settlement Document (Optional)](#unique_35) [page ] 59.

### Purchase Rebate Processing with Graduated Scale Determination

The default calculation of the scales that are set up in the condition table in condition contracts works like volume pricing. This means that on the execution of settlements, the application would apply the rate of the tier that it finds when looking for the business volume, on the entire amount and not only the delta amount:

If you set up the conditions as for example:

| Business Volume | Rebate Percentage |
| --- | --- |
| (From) 1,000 EUR | 10% |
| (From) 6,000 EUR | 20% |
| (From) 10,000 EUR | 30% |

Then the settlement run would calculate the rebates as follows:

| Business Volume found at the time of settlement | Total Effective Rebate at the time of settlement |
| --- | --- |
| 999 EUR | 0 EUR |
| 6,000 EUR | 1,200 EUR |
| 11,000 EUR | 3,300 EUR |

However, if you would like to set up graduated scales that work like tiered pricing instead of volume pricing, then you need to set up the condition contract slightly differently.

Follow the steps as in the chapter [Create Supplier Condition Contract](#unique_50) [page ] 72. In step 9, choose the value of the field Settlement Calculation Method as Graduated-To-Scale. Then in step 11, maintain the scales with scale type as To-scale.

Thereafter, if you set up the conditions as for example:

| Business Volume | Rebate Percentage |
| --- | --- |
| (To-scale) 1,000 EUR | 0% |
| (To-scale) 5,000 EUR | 10% |
| (To-scale) 11,000 EUR | 20% |
| (To-scale) 999,999 EUR | 30% |

Then the settlement run would calculate the rebates as follows:

| Business Volume found at the time of settlement | Total Effective Rebate at the time of settlement |
| --- | --- |
| 1,000 EUR | 0 EUR |
| 5,000 EUR | 400 EUR |
| 11,000 EUR | 1,600 EUR (= 400 EUR +1,200 EUR) |

In the example above, the calculation works in the following manner.

When business volume is found to be 1,000 EUR, then the first tier with 0% rebate is applicable. Hence, the rebate is 0 EUR.

When business volume is found to be 5,000 EUR, then the second condition rate with 10% rebate is applicable on the difference of business volumes between the first and second scales. Hence, the rebate is calculated as 400 EUR.

When business volume is found to be 11,000 EUR, then three condition rates would be applicable. This means that the rebate would be calculated at the rate of 0% for 1,000 EUR, 10% for 4,000 EUR and 20% for the remaining 6,000 EUR, resulting in 0, 400 and 1,200 EUR, respectively. Hence, the total rebate value comes to 1,600 EUR.

### Purchasing Rebate Processing – Fixed Amount Agreements

This section deals with fixed amount agreements as a special process variant for purchasing rebate processing. The characteristic feature for this purchasing rebate process variant is that you enter a fixed amount for the rebate condition in the condition contract. You can again distinguish several scenarios which we describe in the following subchapters.

In the basic scenario, you just enter one or several fixed amount(s) that you pay out to the supplier with a final settlement. As for other purchasing rebate process variants, you can also perform a two-step settlement when there are several fixed amount agreements with a supplier. When you want to distribute the fixed amount to the different fiscal periods within the condition contract validity, you schedule additional delta accruals settlement runs. This distribution can happen before or after the payout of the fixed amount. Additionally, you can also involve business volume data to distribute the fixed amount to business objects.

For the basic scenario and for the scenario with fixed amount distribution to fiscal periods, you use condition contract types 0PF1 Purchasing Rebate: Fixed Amount and 0PF2 Purchasing Rebate:Fixed Amount, 2Step. For the scenario with business volume data, you can use for instance condition contract type 0PI1.

Prerequisite

Please make sure to execute the following chapters before you continue the following process steps:

1. Execute [Activate Condition Contract Types for Fixed Amount Agreements (Optional)](#unique_9) [page ] 11 to unblock condition contract types 0PF1 and 0PF2.
2. Execute [Define Process Variant to Configure Settings for Fixed Amount Agreements](#unique_10) [page ] 26.
3. Execute [Maintain Automatic Account Determination](#unique_20) [page ] 31.

#### Basic Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you execute the purchasing rebate process for fixed amount agreements. You first create the condition contract with one or several condition record(s) for fixed amounts. Then you run the corresponding final settlement(s).

Note

Please execute chapter [Prepare Transactional Data](#unique_7) [page ] 10 before or after you create a supplier condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Supplier Rebates (F6740). | The Manage Condition Contracts - Supplier Rebates screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Supplier Rebates screen, choose Create.In the dialog box Select Condition Contract Type, select the following condition contract type:Purchasing Rebate: Fixed Amount | The Select Condition Contract Type screen displays. |  |
| 4 | Enter Condition Contract Details | On the Create Purchasing Rebate: Fixed Amount screen, make the following entries and choose Enter:Supplier: 33300010From: for example, <today's date>To: for example, <end of current year> | The screen title varies with the selected condition contract type. |  |
| 5 | Enter Basic Data | On the Basic Data tab, make and check the following entries, and choose Enter:Process Variant: ZP06Note ZP06 is defined in chapter [Define Process Variant to Configure Settings for Fixed Amount Agreements](#unique_10) [page ] 26. |  |  |
| 6 | Enter Organizational Data | On the Purchasing tab, make and check the following entries, and choose Enter:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310On the Sales tab, make and check the following entries, and choose Enter.Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 7 | Enter Settlement Data | On the Settlement Data tab, enter the following entry:Settlement Material: for example, TG0011 |  |  |
| 8 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line, make the following entries and choose Continue.Settlement Date: for example, <end of current year>Settlement Date Type: Final SettlementSelect New Line, make the following entries and choose Continue.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementNote If you maintain settlement calendar for Partial Settlement, you must execute chapter [Partial Settlement (Optional)](#unique_32) [page ] 54 to do Partial Settlement before Final Settlement. | The creation of the line with Settlement Date Type: Delta accruals is optional.The creation of the line with Settlement Date Type: Partial settlement is optional. |  |
| 9 | Enter Condition Record for Rebate | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition. Make the following entries, and then choose Enter.Condition Type: RES1 RebateCalculation Type: Fixed AmountCondition Rate: <any amount>Condition Currency: <any currency, best company code currency>Valid From: for example, <today's date>Valid To: for example, <end of validity period> |  |  |
| 10 | Release Condition Contract | Choose Release. |  |  |
| 11 | Save Condition Contract | Choose Save. Make a note of the condition contract number: __________. |  |  |

#### Cost Recognition for Fiscal Periods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you execute the purchasing rebate process for fixed amount agreements in combination with a cost recognition of the fixed amount for the different fiscal periods within the condition contract validity. For this cost recognition adjustment, you schedule an additional delta accruals settlement run for each fiscal period.

In a first process variant, we describe a cost recognition adjustment before the payout of the fixed amount. Here the accruals amount is successively built up with the delta accruals settlements. For the test we have chosen data that make settlement postings comprehensible. Afterwards we describe a distribution subsequent to an immediate payout. Here, the fixed amount is used to activate a positive accruals amount reflecting a claim. In the following delta accruals settlements, you reduce the accruals amount and assign the monthly share to the purchasing rebate P/L account.

Prerequisite

Please execute chapter Define Process Variant to Configure Settings for Fixed Amount Agreements before you settle the condition contract for following variants.

Procedure Variant 1

Enter a condition contract with one fixed amount condition record as described in the previous section. The validity of the condition contract is one year starting on the first day of the current month and ending on the last day of the previous month in the next year. The fixed amount is 1200 AED.

In the settlement calendar, enter additional 12 settlement dates for delta accruals settlement for each month’s end within the condition contract validity. That means the first delta accruals settlement is at the end of the current month, the last coincides with the final settlement date at the end of the condition contract validity.

Perform the delta accruals settlements for each settlement date and check the created settlement documents as described in section Goods Related A/P Settlement Based on Supplier Invoices. Be aware that the correct cost recognition adjustment for fiscal periods only happens when the delta accruals settlement runs at the specified settlement date. However, this procedure is required to illustrate the settlement postings.

First, check the accounting document related to a delta accruals settlement document. You will see that the accruals amount is 100 AED for each month. Then check the pricing for the settlement document items. You see that condition type REBV Rebate Business Vol. does not appear as business volume determination does not play a role for condition contract type 0PF1 (and 0PF2). The initial accruals amount 1200 AED set by condition type RES1 corresponds to the entered fixed amount. In the next line, you see condition type RED5 Cost Recogn. Adjust which controls the cost recognition adjustment. In the first settlement document the initial accruals amount 1200 is reduced by 11/12 (= 1100 AED), in the second settlement document by 10/12 (= 1000 AED) and so on. In the last settlement document the amount for RED5 is zero. Starting with the second settlement document you also see the already posted accruals amount in the line of condition type RED2 Rebate Accr Total which further reduces the actual accruals amount in the calculation. In the second settlement document this amount is 100 AED, in the third settlement document 200 AED and so on. As a result of the calculation the amount for each delta accruals settlement is 100 AED. When you check the settlement document of the final settlement, you see a revenue posting for the customer with the fixed amount increased by the corresponding tax and the reversal of the total accruals amount of 1200 AED.

Procedure Variant 2

Enter a condition contract with one fixed amount condition record as described in the previous section. The validity of the condition contract is one year starting on the first day of the current month and ending on the last day of the previous month in the next year. The fixed amount is 1200 AED.

In the settlement calendar, enter additional 12 settlement dates for delta accruals settlement for each month’s end within the condition contract validity. That means the first delta accruals settlement is at the end of the current month, the last coincides with the final settlement date at the end of the condition contract validity. Additionally, enter a partial settlement within the current month for instance for the current day.

Perform the partial settlement and then the delta accruals settlements and check the created settlement documents as described in section Goods Related A/P Settlement Based on Supplier Invoices. Be aware that the correct cost recognition adjustment for fiscal periods only happens when the delta accruals settlement runs at the specified settlement date. However, this procedure is required to illustrate the settlement postings.

First, check the settlement document for the partial settlement. In the pricing elements of the item, you see the fixed amount 1200 AED as rebate for condition type RES1 Rebate in the first line of the pricing procedure. In the line with condition type RETO Rebate Tax Outbound, you calculate the corresponding VAT tax. The following line shows the resulting gross amount. Relevant for the cost recognition adjustment in this document is the line for condition type REA5 Rebate AccrualsSettl which shows the fixed amount with a negative sign similar to an accruals reversal. Now check the accounting document. First, you see the usual posting for a partial settlement, the credit entry for the customer for the gross amount and debit entries for the fixed amount (net value) on the Purchasing Rebate P/L account and the output tax on the corresponding tax account. In the following lines you see the consequence of the negative value for condition type REA5 from the pricing elements. You see a credit posting for the Purchasing Rebate P/L account and a debit posting for the Accrd Volume Rebate accruals account. This is typical for a ‘payment first, cost activation later’ scenario. These lines balance the cost account – which is the Purchasing Rebate P/L account in this case – and transfer the costs to a clearing account, i.e. the Accrd Volume Rebate accruals account. With the following delta accruals settlements you reduce the proportionate amount on the clearing account and activate (transfer back) the costs on the P/L account.

Now, check the settlement documents for the delta accruals settlement to control this cost activation. First, you see that the settlement amount for each month is 100 AED. When you look at the pricing elements, you see how this net amount is derived from the fixed amount for condition type RES1, a negative amount for condition type RED5 Cost Recogn. Adjust controlling the cost recognition adjustment, the negative fixed amount for condition type RES2 Rebate PartSettl Rev representing the partial settlement reversal, and the – now positive – amount for the condition type RED2 Rebate Accr Total for posted accruals. The (absolute) amount for RED5 and RED2 is decreased by 100 AED month by month. In the accounting document for a delta accruals settlement document, you see the cost activation by a debit entry for the Purchasing Rebate P/L account and a credit posting for the Accrd Volume Rebate accruals account. The final settlement has a settlement amount of zero, it only locks the condition contract.

#### Fixed Amount Settlement Proportionally Across Fiscal Periods

For condition contract types 0PF1 Purchasing Rebate: Fixed Amount and 0PF2 Purchasing Rebate: Fixed Amount, 2step, the default behavior is that a condition contract with a fixed amount is settled in a manner where the total allocation is settled upon the first partial settlement, regardless of the delta accrual distribution across periods.

To ensure that the fixed amount is distributed across partial settlements, make sure that you complete the step 8 in the [Define Process Variant to Configure Settings for Fixed Amount Agreements](#unique_10) [page ] 26 before using the process variant ZP06 Fixed Amount Agreement in the condition contract.

Example

A condition contract has a fixed amount of 12,000 AED. Settlement dates include monthly delta accruals of 1,000 AED and quarterly partial settlements. During the settlement run, the default partial settlement for March would be 12,000 AED. However, if you use the defined process variant for the condition contract, the partial settlement for March would be 3,000 AED.

The table below provides a detailed comparison of the calculations for the two methods:

| Default | Process Variant Used |
| --- | --- |
| Delta accruals for January = 1,000 AED | Delta accruals for January = 1,000 AED |
| Delta accruals for February = 2,000 AED – 1,000 AED = 1,000 AED | Delta accruals for February = 2,000 AED – 1,000 AED = 1,000 AED |
| Delta accruals for March = 3,000 AED – 2,000 AED = 1,000 AED | Delta accruals for March = 3,000 AED – 2,000 AED = 1,000 AED |
| Partial settlement for March = 12,000 AED | Partial settlement for March = 1,000 AED * 3 = 3,000 AED |
| Accruals released = 3000 AED | Accruals released = 3000 AED |

#### Fixed Amount Distribution to Business Objects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you execute the purchasing rebate process for fixed amount agreements in combination with the assignment of the fixed amount to business objects according to their contribution to the overall business volume.

Prerequisite

We recommend preparing transactional in a way that the assignment becomes comprehensible. For instance, prepare business volume of two material with a 2:1 relationship. In the condition contract, enter business volume selection criteria accordingly and use a fixed amount that can be divided by 3.

Procedure

Use condition contract type 0PG1 to enter a condition contract with one fixed amount condition record as described in the section Goods Related A/P Settlement Based on Supplier Invoices. In addition, specify business volume selection criteria.

Perform the final settlement and check the created settlement document. Control that the fixed rebate amount has been distributed to the settlement document items according to the contribution of each item to the overall business volume. When you have prepared business volume data according to the recommendation above, you see two items in the settlement document with a rebate amount of 200 AED and 100 AED, respectively.

#### Fixed Amount Settlement on Multiple Products

Follow the steps described in the [Basic Processing](#unique_65) [page ] 84 chapter in the Purchasing Rebate Processing – Fixed Amount Agreements section.

To specify multiple products and fixed amounts for each of them, in step 10, you can select Condition Contract / Material in the Condition Table dropdown and maintain materials and the corresponding fixed amounts as you need.

If you do this, the settlement material maintained in the header will not be considered but will remain as a fallback.

### Purchase Rebate Processing with Different Bases for Rebate Calculation and Scale Determination

In the following steps, we explain how to create the condition contract using the process variant ZP07 (explained in section the chapter Define Process Variant Scale to Enable Selection of Different Bases for Rebate Calculation and Scale Determination) to specify different bases for rebate calculation and scale determination.

The following is an detailed example.

Example:

Consider there being 4 materials M1, M2, M3 and M4.

Business Volume is to be determined from Materials M1, M2, M3, M4 for deriving the scale for rebate, but rebate is applicable only for M1, M2, M3.

Scales:

If Business Volume > 20000, rebate rate = 2%

If Business Volume > 30000, rebate rate = 3%

At the time of Settlement:

Total purchase = $ 31,000

=> Rebate Scale = 3%

Total purchase excl M4 = $ 27,000

Rebate = $ 27,000 x 3% = $ 810

Based on this example, during the condition contract creation, you will have to set the Selection Group for M1, M2 and M3 as blank, while for M4, you would need to set it as 0PSB.

In the following, we explain how to create the condition contract using the process variant ZS09 described in chapter Define Process Variant for Different Bases for Rebate Calculation and Scale Determination to specify different bases for rebate calculation and scale determination. The test procedure is very similar to the basic process variant, so we only describe the differences to the basic scenario.

#### Create Supplier Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for a supplier as condition contract partner.

Note

Please execute chapter [Prepare Transactional Data](#unique_7) [page ] 10 before or after you create a supplier condition contract, Or you can't settle the condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Supplier Rebates (F6740). | The Manage Condition Contracts - Supplier Rebates screen displays. |  |
| 3 | Create New Condition Contract | On the Manage Condition Contracts - Supplier Rebates screen, choose Create. | The Select Condition Contract Type screen displays. |  |
| 4 | Select Condition Contract Type for A/P Settlement | In the dialog box Select Condition Contract Type, select the following condition contract type:for example, 0PI3 Purchasing Rebate: Supplier Invoice,Goods |  |  |
| 5 | Enter Condition Contract Details | On the Create Purchasing Rebate screen, make the following entries and choose Enter:Supplier: 33300010From: for example, <today's date>To: for example, <end of current year> | The screen title varies with the selected condition contract type. |  |
| 6 | Maintain Basic Data | On the Basic Data tab page, enter the following data and choose Enter.Process Variant: the process variant maintained in chapter [Purchase Rebate Processing with Different Bases for Rebate Calculation and Scale Determination](#unique_19) [page ] 89 for example, ZP07 |  |  |
| 7 | Enter Organizational Data | On the Purchasing tab, make and check the following entries, and choose Enter:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310 |  |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, select New Line, make the following entries and choose Enter.Field Combination: 0002 SupplierInclude/Exclude: InclusiveSupplier: 33300010Select New Line, make the following entries and choose Enter.Field Combination: 0009 MaterialInclude/Exclude: InclusiveMaterial: for example, TG0011Select New Line, make the following entries and choose Enter.Field Combination: 0009 MaterialInclude/Exclude: InclusiveMaterial: for example, TG0015,Selection Group: 0PSB Scale BaseNote If you do not provide a value for Selection Group, then the business volume originating from that material will be eligible for rebate as well as for scale determination.If you use the value 0PRB for the Selection Group, then the business volume originating from material will be eligible for rebate but not for scale determination.If you use 0PSB for the Selection Group, then the business volume originating from that material will be eligible for scale determination but not for rebate. | If you performed the steps described in the prerequisite chapter: [Prepare Transactional Data](#unique_7) [page ] 10, enter here the supplier number that you used to create the purchase order.Optionally, you can specify further materials as selection criterion. |  |
| 9 | Enter Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts Payable |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line, make the following entries and choose Enter.Settlement Date: for example, <end of current year>Settlement Date Type: Final SettlementSelect New Line, make the following entries and choose Continue.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line, make the following entries and choose Continue.Settlement Date: for example, <today's date>Settlement Date Type: Delta Accruals | The creation of the line with Settlement Date Type: Delta accruals is optional.The creation of the line with Settlement Date Type: Partial settlement is optional. |  |
| 11 | Enter Condition Data for Rebate Condition | In the Conditions area, make the following entry:Condition Table: Condition ContractSelect New Condition, make the following entries, and then choose Enter.Condition Type: RES1 RebateCalculation Type: for example, PercentageValid From: for example, <today's date>Valid To: for example, <end of current year>Condition Rate: for example, 1%Scale Type: Base scaleScale Basis Type: Value scaleNote The calculation type for a settlement based on supplier invoices is usually Percentage. For a settlement based on material documents, you usually use Quantity, Net Weight, Gross Weight, Volume, or Points as the calculation type. Other calculation types are not suitable. | This condition is used to calculate the rebate amount.You can also choose Condition Contract / Material as the condition level. You then also specify the material for a condition record.If the Valid From and Valid To dates have been copied from the condition contract validity according to the user settings, you can check and change these dates if required. |  |
| 12 | Enter Scale Data (Optional) | Select the condition line, choose New Scale Level, make the following entries, and then choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, 1%Select the first created condition line, choose New Scale Level, make the following entries, and then choose Enter.Scales: for example, <5000>Unit: AEDCondition Rate: for example, <2%> | The condition rate, condition currency, pricing unit, and unit of measure are copied from the condition line. Only the condition rate is ready for input. |  |
| 13 | Enter Condition Data for Accruals Condition | In the Conditions area, select New Condition, make the following entries and then choose Enter.Condition Type: REA1 Rebate AccrualsCalculation Type: for example, PercentageCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <end of current year> | This condition is used to calculate the amount for accruals.If the Valid From and Valid To dates have been copied from the condition contract validity according to the user settings, you can check and change these dates if required. |  |
| 14 | Release Condition Contract | Choose Release. |  |  |
| 15 | Save Condition Contract | Choose Save. Make a note of the condition contract number: __________. |  |  |

#### Delta Accruals Settlement (Optional)

Please refer to steps in chapter [Delta Accruals Settlement (Optional)](#unique_30) [page ] 51 with the condition contract you created in chapter [Goods Related A/P Settlement Based on Supplier Invoices](#unique_27) [page ] 47.

After processing the delta accruals settlement, you can optionally check the settlement documents refer to chapter [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_31) [page ] 53.

Journal entry:

A/R Settlement:

| Supplier | Revenue Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010or any other supplier used for the purchasing rebate processing. | 72531000 Gain from Supplier Rebate (MM) | 21771000 Accrued Supplier Rebate | n/a |

#### Partial Settlement (Optional)

Please refer to the steps of chapter [Partial Settlement (Optional)](#unique_32) [page ] 54 to do partial settlement for your condition contract. In this step, you also reverse the accruals posted before.

After processing the partial settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Partial Settlement (Optional)](#unique_33) [page ] 55.

Journal entry:

A/R Settlement:

| Supplier | Revenue Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010or any other supplier used for the purchasing rebate processing. | 72531000 Gain from Supplier Rebate (MM) | 21771000 Accrued Supplier Rebate | N/A |

#### Final Settlement

Please refer to [Final Settlement](#unique_34) [page ] 57 to do final settlement for your condition contract.

After processing the final settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Final Settlement Document (Optional)](#unique_35) [page ] 59.

Journal entry:

A/R Settlement:

| Supplier | Revenue Account | Accrual Account | Tax Account |
| --- | --- | --- | --- |
| 33300010or any other supplier used for the purchasing rebate processing. | 72531000 Gain from Supplier Rebate (MM) | 21771000 Accrued Supplier Rebate | N/A |

### Final Settlement with Adjustments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Note

Before you process the final settlement, you can enter conditions in the condition contract used to adjust the final rebate amount.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Supplier Rebates (F6740). | The Manage Condition Contracts - Supplier Rebates screen displays. |  |
| 3 | Create New Condition Contract | On the Manage Condition Contracts - Supplier Rebates screen, select the relevant condition contract and choose Change Contract. | The Select Condition Contract Type dialog screen displays. |  |
| 4 | Enter Condition Data for Rebate Condition | In the Conditions Area, select the following entry:Condition Table: Condition ContractSelect New Condition.Make one of the following entries and choose Enter.Adjustment of business volumeCondition Type: REBD Rebate BusVol DeltaValid From: for example, <today's date>Valid To: for example, <end of current year>Calculation Type: Fixed amountCondition Rate: for example, <100>CondCurr: AEDAdjustment of rebate valueCondition Type: REJ1 Rebate AdjustmentValid From: for example, <today's date>Valid To: for example, <end of current year>Calculation Type: Fixed amountCondition Rate: for example, <20>CondCurr: AEDEntry of a fixed settlement amountCondition Type: REV1 Rebate VerifiedValid From: for example, <today's date>Valid To: for example, <end of current year>Calculation Type: Fixed amountCondition Rate: for example, <1000>CondCurr: AED | The conditions entered here are used to adjust the rebate amount.If the Valid From and Valid To date is copied from the condition contract validity according to user settings, you can check and change these dates if required. |  |
| 5 | Save Condition Contract | Choose Save. |  |  |
| 6 | Perform Final Settlement | Perform procedure as described in [Final Settlement](#unique_34) [page ] 57. |  |  |

### Reverse Settlement Documents - Condition Contracts (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

You have processed the settlement run to the condition contract(s).

Note

Once you need to reverse settlement document, you can execute this step.

Procedure

The steps below are using Reverse Settlement Documents - Condition Contracts (WB2R_CANCEL_DOCS) for reversing settlement documents for the selected condition contract(s). You can use Reverse Settlement Document (WZR4) to reverse a single settlement document. You can also use Reverse Settlement Documents (WAB_CANCEL_B) to reverse several settlement documents together.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Reverse Settlement Documents - Condition Contracts (WB2R_CANCEL_DOCS). | The Reverse Settlement Documents for Condition Contracts screen displays. |  |
| 3 | Reverse Settlement Document for Condition Contract | On the Reverse Settlement Documents for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract(s) created in this test>Check Run Only: <unselect this checkbox>Choose Execute.Choose Continue in the pop-up window. | The Log for Reversal of Settlement Documents - Live Run screen displays. All settlement documents for the selected condition contract(s) are reversed. |  |
| 4 | Review the Reversal of Settlement Documents | On the screen Log for Reversal of Settlement Documents - Live Run, choose the log and choose Contract.Check the reversal of settlement documents. | The Display Purchasing Rebate: Supplier Invoice screen displays. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Description |
| --- | --- |
| J60-Accounts Payable | You can complete the related activities described in the script of scope item J60 - Accounts Payable using the open supplier credit memo created in scope item 2R7. |
| J59-Accounts Receivable | You can complete the related activities described in the script of scope item J59- Accounts Receivable using the open customer invoices created in scope item 2R7. |

### General Ledger Reporting and CO-PA Reporting (Optional)

After completing the activities in this test script, it is possible to run General Ledger Reporting and CO-PA Reporting connected with the accounts which were used in this Purchasing rebate process. Log on as General Ledger Accountant and run the reports which apply to your needs and check the postings on your accounts. Please refer to scope item Accounting and Financial Close to Manage G/L Account Master Data and Manage Financial Statement Versions.

### Time-Dependent Tax

Time-Dependent Tax feature is only valid for goods related condition contract types.

For more details concerning the activation of the Time-Dependent Tax feature and the maintenance of time dependent tax rates see [Time-Dependent Taxes (TDT)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/8fd78f3974b84e478dc99ae1ae1afc16.html).

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
> Flagged while digesting this document, not verified: Process variant for different bases is created as ZP07 in the configuration chapter but later referred to as ZS09 in the Different Bases test procedure.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[08-sales-order-management/royalties-settlement-for-sales-55i-ae-test-script-sap-s-4hana-cloud-pu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2R7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 194,973 chars in the whole document
