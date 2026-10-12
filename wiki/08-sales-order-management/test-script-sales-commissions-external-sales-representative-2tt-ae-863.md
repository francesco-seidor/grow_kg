---
id: 08-sales-order-management/test-script-sales-commissions-external-sales-representative-2tt-ae-863
title: "Test Script: Sales Commissions – External Sales Representative (2TT_AE) (2TT_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for external sales commission settlement via condition contracts: prerequisites, variants, workflow, settlement steps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/condition-contract-settlement]
aliases: [2TT_S4CLD2608_BPD_EN_AE]
keywords: ["Rebates, Commissions and Royalties Settlement", sales commissions, condition contracts, commission settlement, process variants, delta accruals, approval workflow, paid billing documents, subscription billing, single sales deal]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TT_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-863
topic: 08-sales-order-management/condition-contract-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Commissions – External Sales Representative (2TT_AE) (2TT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Rebates, Commissions and Royalties Settlement** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 31-07-26 |
| --- | --- |
|  | Sales Commissions – External Sales Representative (2TT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc237130459)

[2 Prerequisites 5](#_Toc237130460)

[2.1 System Access 5](#_Toc237130461)

[2.2 Roles 5](#_Toc237130462)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc237130463)

[2.4 Preliminary Steps 8](#_Toc237130464)

[2.4.1 Posting of Accruals with Transactional Documents (Optional) 8](#_Toc237130465)

[2.4.2 Prepare Transactional Data (Optional) 11](#_Toc237130466)

[2.4.3 Activate Condition Contract Types (Optional) 11](#_Toc237130467)

[2.4.4 Define Condition Contract Process Variants (Optional) 13](#_Toc237130468)

[2.4.4.1 Define Process Variant for Using the Workflow 14](#_Toc237130469)

[2.4.4.2 Define Process Variant for Tax Free Commissions 16](#_Toc237130470)

[2.4.4.3 Define Process Variant for Split Criteria Usage in Settlement 18](#_Toc237130471)

[2.4.4.4 Define Process Variant for Business Volume Selection Criteria Usage 21](#_Toc237130472)

[2.4.4.5 Define Process Variant for Contract Determination 24](#_Toc237130473)

[2.4.4.6 Define Process Variant for Commissions on Paid Invoices 26](#_Toc237130474)

[2.4.4.7 Define Process Variant to Activate Condition Table for Product Hierarchy 29](#_Toc237130475)

[2.4.4.8 Define Process Variant to Activate Business Volume Selection by Service Rendered Date 32](#_Toc237130476)

[2.4.4.9 Maintain Automatic Account Determination 35](#_Toc237130477)

[2.4.5 Configure Approval Workflow (Optional) 38](#_Toc237130478)

[2.4.5.1 Manage Teams and Responsibilities 38](#_Toc237130479)

[2.4.5.2 Manage Workflow for Condition Contracts - Release Contract 40](#_Toc237130480)

[2.4.5.3 Manage Workflow for Condition Contracts - Release Settlement 41](#_Toc237130481)

[2.4.5.4 Manage Workflow for Settlement Documents 43](#_Toc237130482)

[2.4.6 Adapt G/L Account for Accruals (Optional) 44](#_Toc237130483)

[3 Overview Table 45](#_Toc237130484)

[4 Test Procedures 49](#_Toc237130485)

[4.1 Commission Processing – Billing Document 49](#_Toc237130486)

[4.1.1 Create Condition Contract 49](#_Toc237130487)

[4.1.2 Check Business Volume (Optional) 54](#_Toc237130488)

[4.1.3 Delta Accruals Settlement (Optional) 55](#_Toc237130489)

[4.1.4 Check Settlement Document for Delta Accruals Settlement (Optional) 56](#_Toc237130490)

[4.1.5 Partial Settlement (Optional) 57](#_Toc237130491)

[4.1.6 Check Settlement Document for Partial Settlement (Optional) 59](#_Toc237130492)

[4.1.7 Final Settlement 61](#_Toc237130493)

[4.1.8 Check Settlement Document for Final Settlement 62](#_Toc237130494)

[4.2 Commission Processing – Billing Document Paid 62](#_Toc237130495)

[4.2.1 Post Incoming Payments (Optional) 63](#_Toc237130496)

[4.2.2 Create Condition Contract 65](#_Toc237130497)

[4.2.3 Check Business Volume (Optional) 69](#_Toc237130498)

[4.2.4 Delta Accruals Settlement (Optional) 70](#_Toc237130499)

[4.2.5 Partial Settlement (Optional) 70](#_Toc237130500)

[4.2.6 Final Settlement 70](#_Toc237130501)

[4.3 Commission Processing – Subscription Billing 70](#_Toc237130502)

[4.3.1 Create Condition Contract 71](#_Toc237130503)

[4.3.2 Check Settlement Documents 71](#_Toc237130504)

[4.4 Commission Processing – Settlement Document 71](#_Toc237130505)

[4.4.1 Create Condition Contract 72](#_Toc237130506)

[4.5 Commission Processing – Single Sales Deal 75](#_Toc237130507)

[4.5.1 Create Condition Contract 76](#_Toc237130508)

[4.5.2 Check Pricing Element of Sales Order Item 76](#_Toc237130509)

[4.5.3 Final Settlement 76](#_Toc237130510)

[4.5.4 Check Settlement Document for Final Settlement (Optional) 76](#_Toc237130511)

[4.6 Commission Processing with Approval Workflow 77](#_Toc237130512)

[4.6.1 Create Condition Contract 77](#_Toc237130513)

[4.6.2 Request Approval to Release Condition Contract 81](#_Toc237130514)

[4.6.3 Trigger Rework of Condition Contract (Optional) 82](#_Toc237130515)

[4.6.4 Rework Condition Contract (Optional) 83](#_Toc237130516)

[4.6.5 Release Condition Contract 84](#_Toc237130517)

[4.6.6 Check Business Volume (Optional) 85](#_Toc237130518)

[4.6.7 Delta Accruals Settlement (Optional) 85](#_Toc237130519)

[4.6.8 Request Release of Condition Contract for Settlement 85](#_Toc237130520)

[4.6.9 Release Condition Contract for Settlement 86](#_Toc237130521)

[4.6.10 Partial Settlement (Optional) 87](#_Toc237130522)

[4.6.11 Approve Release of Partial Settlement Document to Accounting (Optional) 87](#_Toc237130523)

[4.6.12 Final Settlement 88](#_Toc237130524)

[4.6.13 Approve Release of Final Settlement Document to Accounting 88](#_Toc237130525)

[4.7 Commission Processing with Graduated Scales 89](#_Toc237130526)

[4.8 Commission Processing with Conditions Maintained for Product Hierarchy Nodes 90](#_Toc237130527)

[4.9 Commission Processing Using Service Rendered Date for Business Volume Selection 91](#_Toc237130528)

[4.10 Final Settlement with Adjustments (Optional) 92](#_Toc237130529)

[4.11 Commission Unlikelihood (Optional) 94](#_Toc237130530)

[4.12 Reverse Settlement Document (Optional) 95](#_Toc237130531)

[5 Follow-Up Processes 97](#_Toc237130532)

[5.1 Accounts Payable (Optional) 97](#_Toc237130533)

[5.2 General Ledger Reporting and CO-PA Reporting (Optional) 97](#_Toc237130534)

## Purpose

The Sales Commissions Settlement scope item concerns the subsequent settlement of sales commission conditions agreed upon with an external sales agent. You use condition contracts from Condition Contract Management to enter the sales commission agreements with the external sales agents. In a condition contract, you specify the commission recipient, organizational and process control parameter, business volume selection criteria, sales commission conditions, and the settlement calendar with settlement dates for delta accrual, partial and final settlement. The delta accruals settlement reflects a procedure in which accruals for commissions are not posted together with the transactional documents but subsequently in a specific settlement run. In the partial and final settlements of a condition contract you perform the sales commission calculation based on business volume and commission conditions, and you create the settlement documents reflecting an invoice from the external sales agents for the arrangement of sales deals.

This scope item supports several process variants resulting from different data sources for the business volume determination. In the basic scenario, the data source is SD billing documents without check for payment and as a variation of the corresponding settlement process, you can choose to only consider paid billing documents. In the so called ‘Commissions on Commissions’ process variant, settlement documents for commissions form the data source. And in the ‘Commissions for Single Sales Deals’ variant, the accruals index table is used as data source.

This scope item is closely related to the business process of Sell from Stock (BD9) scope item. Ideally, the condition contract is created first before you start to enter sales orders in the system. However, you can also create condition contracts subsequently with a validity period starting in the past. Also, sales commissions processing and sales transactions run in parallel in that sense that you process partial settlements for billing documents entered continuously during the condition contract’s validity period.

After describing the general process flow, two special aspects are addressed at the end of the test script. When a defined minimum sales turnover for a commissions eligibility will probably not be reached, you are obliged to reverse existing accruals and prevent creating new accruals. This requirement is fulfilled with the help of an unlikelihood condition maintained in the condition contract. In addition, you can maintain conditions for adjusting the (final) settlement amount in the condition contract. You typically agree upon such adjustments with the external sales agent when there is a dissonance concerning the relevant business volume. You can maintain a condition for adjusting the business volume, for an additional commission amount and for a final fixed commission.

In addition, you can also configure workflows to include the approval process for condition contracts, release of condition contract for settlement and partial and final settlement documents. You can define workflow preconditions for releasing condition contracts and settlement documents. An approver can choose to approve, reject or send the documents for rework to the document initiator. The approval process starts when a workflow with one or more steps is activated and the preconditions you have assigned to it are met.

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
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Contract Manager - Commissions | SAP_BR_CONTR_MGR_COMMSN | Commissions and Incentives | SAP_SD_SPT_COMMSN_MNTN_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Settlement Clerk - Commissions | SAP_BR_SETL_CLERK_COMMSN | Commissions and Incentives | SAP_SD_SPT_COMMSN_PROC_PC |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No batch. |  |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No batch. |  |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch-controlled (FIFO strategy). |  |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch-controlled (Exp. Date). |  |
| Sold-to Party | 3310000333100008 | Domestic UAE Customer 3Domestic UAE Customer 8 | You can test the scope item using another domestic customer.33100005 is for credit management.33100008 is for material listing/exclusion. 33100009 is for customer material record and POD (Proof-of-Delivery). |
| Ship-to party | 3310000333100008 | Domestic UAE Customer 3Domestic UAE Customer 8 |  |
| Payer | 3310000333100008 | Customer domestic 03Domestic UAE Customer 8 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |
| Supplier (External Sales Agent) | 33300095 |  |  |
| Purchasing Organization | 3310 |  |  |
| Purchasing Group | 001 |  |  |
| Company Code | 3310 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Preliminary Steps

#### Posting of Accruals with Transactional Documents (Optional)

Purpose

Accruals can be created when you post transactional documents ‒ billing documents released to accounting in this scope item ‒ or you can post accruals in an accumulated form with a specific settlement run called Delta Accruals Settlement as described in the test procedures. You can also combine the procedures, for instance, to determine a more accurate accruals amount in a weekly delta accruals run by considering all transactional documents.

To post accruals with released billing documents, you must include the accruals condition type in the pricing procedure of the sales order in an appropriate manner. As usual, this pricing element will be copied to the billing document. Below we describe the best practice approach that you include the condition type at the bottom of the pricing procedure. Note that you can similarly post accruals for other scope items (sales rebates, royalties) in parallel when you include the corresponding accruals condition types in the same way.

Posting accruals with transactional documents requires that you create the condition contract with the accruals condition before you create commission relevant sales orders, so that the accruals condition is found during pricing of a sales order item. Relevant condition contracts are determined by matching sales order and condition contract data. If the system finds more than one relevant condition contract, you will accordingly get several lines for the accruals condition types in the pricing elements. When you create a condition contract with a validity period starting in the past, you can schedule a delta accruals settlement to post accruals for already created billing documents. Then you continue to post accruals with the transactional documents. When you want to create a new condition contract without specifying a customer as the business volume selection criterion, define a condition contract process variant as described in chapter Define Process Variant for Contract Determination and enter it for the condition contract.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Pricing | Enter the following filters:Application Area: SalesSub Application Area: Price ManagementIn the items table, select the item with item name: Pricing. | The Configure Your Solution - Pricing screen displays. |  |
| 5 | Go to Pricing Procedures Overview | Choose Configure on the right to Set Pricing Procedures configuration step. | The Set Pricing Procedures: Change screen displays. |  |
| 6 | Go to Control Data | Select the relevant pricing procedure and choose Procedures – Control Data in Dialog Structure. | The control data for the pricing procedure with the Reference Step Overview table is displayed in the working area. |  |
| 7 | Add Accruals Condition Type | Choose New Entries and make the following entries:Step Number: <number higher than maximum hitherto>Condition Type: RCA1Alt. Cndn Base Value: 213Accruals: 0C1Choose Save. | Accruals condition type has been added to pricing procedure. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Go to Pricing Procedures Overview | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Set Pricing Procedures.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Pricing Procedures: Change screen displays. |  |
| 3 | Go to Control Data | Select the relevant pricing procedure and choose Procedures – Control Data in Dialog Structure. | The control data for the pricing procedure with the Reference Step Overview table is displayed in the working area. |  |
| 4 | Add Accruals Condition Type | Choose New Entries and make the following entries:Step Number: <number higher than maximum hitherto>Condition Type: RCA1Alt. Cndn Base Value: 213Accruals: 0C1Choose Save. | Accruals condition type has been added to pricing procedure. |  |

If you want to use the sales commissions variant Commissions Processing – Single Sales Deals, add condition type RCA9 in the same way.

Routine 213 for the alternative calculation of condition base value has the following function: When you enter a condition contract, you can set the amount fields group on the Settlement Data tab page. This parameter controls for which amount field from the business volume data the system transfers data to the pricing procedure of the settlement document. As default, the net amount is used, but you can also specify a subtotal of the pricing procedure. As mentioned, during pricing the system determines the relevant condition contracts for the accruals condition types, and formula 213 reads the corresponding amounts field group and sets the condition base value accordingly. Therefore, there is no need to specify the From Step in the line with accruals condition type.

#### Prepare Transactional Data (Optional)

Purpose

For Commissions External: Billing Document process, the business volume for commission settlement is determined from billing documents. To prepare transactional test data, you can follow the Sell from Stock (BD9) scope item, which describes the sales process from a standard sales order to a billing document.

For Commission External: Billing Document Paid process, the business volume for commission settlement is determined from paid billing documents, which means the related accounting documents need to be cleared. To prepare transactional test data, you can follow the steps described in the scope items Sell from Stock (BD9) and Accounts Receivable (J59).

Preparing transactional data is a required step. You can perform this step before or after creating the condition contract, or after each settlement run.

When you want to use the commission recipient as business volume selection criterion, you enter the commission recipient business partner ID for partner function ES External Sales Agent on the Partner tab for sales order items. When you enter the commission recipient business partner ID on header level, the system copies it down to new sales order items.

Procedure

Complete all the activities described in Sell from Stock (BD9) scope item's test script using the master data from this document.

|  |
| --- |
| Note If you want to use the optional link between Sell from Stock (BD9) scope item and Condition Contract Settlement, this reference only works if you use consistent master data (such as business partner and material for the customer sales order and the customer condition contract). |

For the sales commission processing using an external sales agent as condition contract partner, select an external sales agent from the chapter [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 6 and execute Sell from Stock (BD9) scope item. In the sales order, you need to assign the partner role, ES, to a supplier, for example 33300095. Then follow the Chapter [Create Condition Contract](#unique_9) [page ] 49.

#### Activate Condition Contract Types (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you activate the condition contract types for post-test procedure.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - External Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Configure Condition Contract Types for Supplier Condition Contracts. | The Configure Condition Contract Types for Sup..: Change screen displays. |  |
| 6 | Remove Block | In column Block, choose Not Blocked – Can be Used for the condition contract types you need for post-test procedure:0CC1 Commission External: Settlement Document0CS5 Commission Ext: Bill Doc DirectSettlement0CS7 Commission External: Subscription BillChoose Save. | The condition contract types are no longer blocked. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Condition Contract Types for Supplier Condition Contracts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - External Commission Settlement screen displays. |  |
| 3 | Remove Block | In column Block, choose Not Blocked – Can be Used for the condition contract types you need for post-test procedure:0CC1 Commission External: Settlement Document0CS5 Commission Ext: Bill Doc DirectSettlement0CS7 Commission External: Subscription BillChoose Save. | The condition contract types are no longer blocked. |  |

#### Define Condition Contract Process Variants (Optional)

This chapter defines condition contract process variants to also test variations of the core process. A process variant is used to define limited variations for condition contract maintenance and settlement that are configured for a condition contract type without changing the overall character of the process defined by a condition contract type.

In this chapter we describe process variants for different purposes. Note that you can also combine settings from these process variants. If you assign a condition contract process variant to a new condition contract you have to enhance the account determination settings. The process variant is a key field in the relevant condition table. We describe how you maintain account determination settings for the first process variant for approval workflow. Proceed in the same way for all other process variants that you want to test.

##### Define Process Variant for Using the Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate the workflow for sales commission processing.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Process Variants Overview | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variant": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZC01 Sales Commission with WorkflowSettlement Management Status Group: CommissionsDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created. |  |
| 7 | Assign Condition Contract Types to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0CS1Choose Save.Note If you want to make use of the workflow feature, enter this condition contract process variant when you create a new commissions condition contract. | The relevant condition contract type is assigned to newly-created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZC01 Sales Commission with WorkflowSettlement Management Status Group: CommissionsDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created. |  |
| 4 | Assign Condition Contract Type to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0CS1Choose Save.Note If you want to make use of the workflow feature, enter this condition contract process variant when you create a new commissions condition contract. | The relevant condition contract type is assigned to newly-created process variant. |  |

##### Define Process Variant for Tax Free Commissions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant which controls that sales commissions are treated tax-free.

Some countries, like the USA, do not offer tax services. When sales commissions are regarded as a service, taxation will be set to zero for the sales commission amount. Tax-free sales commissions are achieved with this process variant in which you set the tax indicator for materials to zero. This tax indicator setting is transferred to pricing of a settlement run by a configured transfer rule.

If you want to treat sales commissions tax-free, make sure that you assign the condition contract process variant when you create a new condition contract.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Commissions | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variant": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC02 Sales Commissions with Tax Free GoodsChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Type to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Choose Save. | The condition contract type is assigned to newly-created process variant. |  |
| 8 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 3310Tax Indicator for Material: 0Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC02 Sales Commissions with Tax Free GoodsChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Choose Save. | The condition contract type is assigned to newly-created process variant. |  |
| 5 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 3310Tax Indicator for Material: 0Choose Save. |  |  |

##### Define Process Variant for Split Criteria Usage in Settlement

Purpose

In this activity, you create a condition contract process variant to activate further split criteria defined in the profiles for business volume determination.

Split criteria for condition contract settlement – defined in Customizing in the profiles for business volume determination - are used to point up the contribution of different business objects to the overall sales commission amount. In the profile for business volume determination relevant for sales commission settlement, some split criteria, such as material or profit center, are defined as always active. The usage of these split criteria cannot be influenced with a condition contract process variant. But there are other split criteria which are defined as inactive until activated by a process variant. Note that for the test of an additionally activated split criterion you also have to prepare the business volume data accordingly with different values for the split criterion.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variant": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC03 Sls Commission Split Criteria Adaptation | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Choose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate/Deactivate Split Criteria for Settlement | Double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: <settlement document type>, for example, 0CS1 Commission External: Billing DocumentField Name: select from field help list, for example AUFNRUsage as Split Criterion: select from the dropdown list as used or not usedNote In case of Subscriptions, if you want the Provider Contract information to appear in the Journal Entries resulting from the settlement process, then please maintain the following entries:PROVIDERCONTRACTPROVIDERCONTRACTITEMSETTLMTADDLREFDOCCATThis is valid for Condition Contract Types that are relevant for Subscription Billing - 0CS7.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC03 Sls Commission Split Criteria Adaptation | The process variant is created. |  |
| 4 | Assign Condition Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Choose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate/Deactivate Split Criteria for Settlement | Double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: <settlement document type>, for example, 0CS1 Commission External: Billing DocumentField Name: select from field help list, for example AUFNRUsage as Split Criterion: select from the dropdown list as used or not usedNote In case of Subscriptions, if you want the Provider Contract information to appear in the Journal Entries resulting from the settlement process, then please maintain the following entries:PROVIDERCONTRACTPROVIDERCONTRACTITEMSETTLMTADDLREFDOCCATThis is valid for Condition Contract Types that are relevant for Subscription Billing - 0CS7.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

##### Define Process Variant for Business Volume Selection Criteria Usage

Purpose

In this activity, you create a condition contract process variant to change the usage of business volume selection criteria defined in the relevant set of field combinations.

To allow high flexibility in the business volume selection, the set of field combinations for sales commission settlement provides many business volume selection criteria. However, this larger number can complicate the maintenance of business volume selection criteria in the condition contract as the user needs to find the desired field combination in a long list when he wants to enter a new line. With a suitable condition contract process variant you can reduce the scope of business volume selection criteria to the relevant ones.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variant": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC04 Commission Selection Criteria Adaptation | The process variant is created. |  |
| 7 | Assign Condition Contract Types to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0CS1Choose Save. | The relevant condition contract type is assigned to newly- created process variant. |  |
| 8 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: External Commission SettlementField Combination: select from field help list, for example, 0035Note You can choose 0069 for Customer Hierarchy.Usage of Field Combination: select from the dropdown list as used or not usedChoose Save. | The usage of field combination is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Condition Contract Process Variants | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC04 Commission Selection Criteria Adaptation | The process variant is created. |  |
| 4 | Assign Condition Contract Type to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0CS1Choose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: External Commission SettlementField Combination: select from field help list, for example, 0035Note You can choose 0069 for Customer Hierarchy.Usage of Field Combination: select from the dropdown list as used or not usedChoose Save. | The usage of field combination is changed with the process variant. |  |

##### Define Process Variant for Contract Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to adapt the condition contract determination in the pricing of a sales order which is required when you do not specify a customer as business volume selection criterion.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Commissions | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variant": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC05 Contract Determination Single Sales DealChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Type to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entries:Contract Type: 0CS1Relevant for Contract Determination: All CustomersChoose Save. | The condition contract type is assigned to newly-created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC05 Contract Determination Single Sales DealChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entries:Contract Type: 0CS1Relevant for Contract Determination: All CustomersChoose Save. | The condition contract type is assigned to newly-created process variant. |  |

##### Define Process Variant for Commissions on Paid Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to enable the use of business volume table groups for business volume determination. This ensures that the commission amount calculation considers only paid invoices.

This approach is applicable when the condition contract type 0CS3 does not meet business requirements. For a comparison between condition contract type 0CS3 and condition contract type 0CS1 used with process variant ZC06, refer to the Commissions Processing – Billing Document Paid section in the Test Procedures.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC06 Sales Commission on Paid InvoicesChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Note Add further condition contract types if you want to test the process variant for other external commission scenarios, for example, 0CS7. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate Usage of Business Volume Table Group | Double-click on Business Volume Table Group on the left of the screen.Choose New Entries and make the following entries:Profile: 0CS1BVTab Grp.: 0C01Usage: select from the dropdown list, Use in Condition Contract SettlementNote Add more Profile and BVTab Grp entries if you want to test the process variant for other external commission scenarios, for example, 0CS7.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZC06 Sales Commission on Paid InvoicesChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Note Add further condition contract types if you want to test the process variant for other external commission scenarios, for example, 0CS7. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate Usage of Business Volume Table Group | Double-click on Business Volume Table Group on the left of the screen.Choose New Entries and make the following entries:Profile: 0CS1BVTab Grp.: 0C01Usage: select from the dropdown list, Use in Condition Contract SettlementNote Add more Profile and BVTab Grp entries if you want to test the process variant for other external commission scenarios, for example, 0CS7.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

##### Define Process Variant to Activate Condition Table for Product Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a condition contract process variant that allows you to activate condition table for product hierarchy.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC07 Activate Condition for Product HierarchyChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Note Add further condition contract types if you want to test the process variant for other sales commission scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Enter Condition Types / Tables | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries:Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCS1Table Number: 4CVUsage of Condition Level: 2 ActiveRepeat the current step if you need to active more condition types such as RCA1.Click Enter and choose Save.Optionally, you can set product hierarchy as a split criterion by selecting Field Name: PRODH_UNIV_SALES_PARNT_NODID in step 8 in chapter [Define Process Variant for Split Criteria Usage in Settlement](#unique_14) [page ] 18. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZC07 Activate Condition for Product HierarchyChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Note Add further condition contract types if you want to test the process variant for other sales commission scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Enter Condition Types / Tables | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries:Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCS1Table Number: 4CVUsage of Condition Level: 2 ActiveRepeat the current step if you need to active more condition types such as RCA1.Click Enter and choose Save.Optionally, you can set product hierarchy as a split criterion by selecting Field Name: PRODH_UNIV_SALES_PARNT_NODID in step 8 in chapter [Define Process Variant for Split Criteria Usage in Settlement](#unique_14) [page ] 18. |  |  |

##### Define Process Variant to Activate Business Volume Selection by Service Rendered Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a condition contract process variant that enables you to use service rendered date instead of billing date for the selection of billing documents to determine the business volume.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: External Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC08 BusVol Selection by Service Rendered DateChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Business Volume Selection Date Type: 0001 Service Rendered DateNote Add further condition contract types if you want to test the process variant for other sales commission scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Enter Condition Types / Tables | This step is to ensure that only that accrual condition type which works with Service Rendered Date is selectable when creating your condition contract with this process variant.Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries to set the condition type RCA1 to inactive:Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCA1Usage of Condition Level: 1 InactiveRepeat the current step. Make the following entries to activate condition type RCAA.Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCAAUsage of Condition Level: 2 ActiveClick Enter and choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZC08 BusVol Selection by Service Rendered DateChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CS1Business Volume Selection Date Type: 0001 Service Rendered DateNote Add further condition contract types if you want to test the process variant for other sales commission scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Enter Condition Types / Tables | This step is to ensure that only that accrual condition type which works with Service Rendered Date is selectable when creating your condition contract with this process variant.Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries to set the condition type RCA1 to inactive:Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCA1Usage of Condition Level: 1 InactiveRepeat the current step. Make the following entries to activate condition type RCAA.Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCAAUsage of Condition Level: 2 ActiveClick Enter and choose Save. |  |  |

##### Maintain Automatic Account Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you specify G/L account for sales commission processing.

If you assign a condition contract process variant to a new condition contract, you have to enhance the account determination settings. The process variant is a key field in the relevant condition table.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

In the following steps, we show how to create the necessary entry for the first defined process variant ZC01 Sales Commission with Workflow.

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Chart of Accounts | Enter the following filters:Application Area: FinanceSub Application Area: General LedgerIn the items table, select the item with item name: Chart of Accounts. | The Configure Your Solution – Chart of Accounts screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Automatic Account Determination configuration step. | The Automatic Account Determination 1. Area screen displays. |  |
| 6 | Fill in Basic Information | Make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L AccountsChoose Step 2. | The Automatic Account Determination 2. Parameters screen displays. |  |
| 7 | Fill in Relevant Information | Make the following entries:Chart of Accounts: YCOAApplication: VCondition Table: 016Choose Step 3. | The Automatic Account Determination 3. Account Assignments screen displays. |  |
| 8 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condition Type: KORC Commission SettlementCompany Code: 3310Contract Process Variant: ZC01Account Key: 0C1 Commission SettlementG/L Account: 61500000Accruals Acc.: 21772000Note If you have accruals, you can assign a second set of G/L accounts.Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 9 | Review in the Information and Save | Choose Save. | The G/L account assignment is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Automatic Account Determination 1. Area screen displays. |  |
| 3 | Fill in Basic Information | Make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L AccountsChoose Step 2. | The Automatic Account Determination 2. Parameters screen displays. |  |
| 4 | Fill in Relevant Information | Make the following entries:Chart of Accounts: YCOAApplication: VCondition Table: 016Choose Step 3. | The Automatic Account Determination 3. Account Assignments screen displays. |  |
| 5 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condition Type: KORC Commission SettlementCompany Code: 3310Contract Process Variant: ZC01Account Key: 0C1 Commission SettlementG/L Account: 61500000Accruals Acc.: 21772000Note If you have accruals, you can assign a second set of G/L accounts.Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 6 | Review in the Information and Save | Choose Save. | The G/L account assignment is saved. |  |

#### Configure Approval Workflow (Optional)

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain the teams and responsibilities for sales commission workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create a New Team | Choose Create. | The Team screen displays. |  |
| 4 | Enter General Information | Make the following entries and choose Enter:Name: for example, <CCM_TEST_TEAM_SD_(Country Code)>Description: for example, <Condition Contract Management Team Sales (Country Name)>Status: EnabledType: SCMTV Sales Condition Contract Team TypeCondition Contract Category: 0C | The team is created. |  |
| 5 | Add Team Members | In Team Members, choose Create.From Items section, select a business partner checkbox and choose OK.Business Partner: for example, <Sales_Manager> | The Team screen displays. |  |
| 6 | Add Function to Team Members | In the Functions field, choose Select. In the Select: Functions window, choose the following functions, and choose OK.SCCM_F1: Condition Contract Release ApprovalSCCM_F2: Condition Contract Settlement Release ApprovalChoose Save to save the team. | The team is saved. |  |
| 7 | Create a New Team | Go back and choose Create. | The Team screen displays. |  |
| 8 | Enter General Information | Make the following entries and choose Enter:Name: for example, <STLMT_TEST_TEAM_SD_(Country Code)>Description: for example, <Settlement Management Team Sales (Country Name)>Status: EnabledType: SMT Settlement ManagementSettlmtDocType: 0C11 | The team is created. |  |
| 9 | Add Team Members | In Team Members, choose Create.From Items section, select a business partner checkbox and choose OK.Business Partner: for example, <Sales_Manager> | The Team screen displays. |  |
| 10 | Add Function to Team Members | In the Functions field, choose Select. In the Select: Functions window, choose the following functions, and choose OK.STLMTAPR: Settlement Document ApproverChoose Create. | The team is saved. |  |
| 11 | Check Team Status | Navigate to the Manage Teams and Responsibilities worklist, and verify the status of the team by selecting Go.The status should be Enabled. | The team status is enabled. |  |

##### Manage Workflow for Condition Contracts - Release Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for condition contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflows screen displays. |  |
| 3 | Select Relevant Workflow | Select Release Condition Contract in the top left dropdown list.Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for Release of Condition Contract - Single Step Level ApprovalUnder Steps, choose Create. | The New Step screen displays. |  |
| 5 | Input Details | Make the following entries:Step Type: Release of Condition ContractRole: Condition Contract Release ApprovalIn the Exception Handling section, make the following settings for Rework Condition Contract:Required Action: Rework of Condition ContractAction Result: Restart WorkflowChoose Create. | The New Workflow screen displays. |  |
| 6 | Save Workflow | Choose Save. | The Workflow Details screen displays. |  |
| 7 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

##### Manage Workflow for Condition Contracts - Release Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for condition contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflows screen displays. |  |
| 3 | Select Relevant Workflow | Select Settlement Release of Condition Contract in the top left dropdown list.Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for Settlement Release of Cond. Contract - Single StepChoose Create under Steps. | The New Step screen displays. |  |
| 5 | Input Workflow Details | Make the following entries:Step Type: Release of Condition Contract for SettlementRole: Condition Contract Settlement Release ApprovalRework Condition Contract:Required Action: Rework of Condition Contract for Settlement ReleaseAction Result: Restart WorkflowChoose Create. | The New Workflow screen displays. |  |
| 6 | Save Workflow | Choose Save. | The Workflow Details screen displays. |  |
| 7 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

##### Manage Workflow for Settlement Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for condition contracts settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Settlement Documents (F3681). | The Manage Workflows screen displays. |  |
| 3 | Create New Workflow | Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for the Approval of Settlement Document (To Accounting)Under Steps, choose Create. | The New Step screen displays. |  |
| 5 | Input Details | Make the following entries:Step Type: Release of Settlement DocumentRole: Settlement Document ApproverChoose Create. | The New Workflow screen displays. |  |
| 6 | Create New Step | Under Steps, choose Create. | The New Step screen displays. |  |
| 7 | Input Details | Make the following entry:Step Type: Automatic Change of Settlement Document StatusChoose Create. | The New Workflow screen displays. |  |
| 8 | Save Workflow | Choose Save. | The Workflow Details screen displays. |  |
| 9 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

#### Adapt G/L Account for Accruals (Optional)

Purpose

This preliminary step is only required when you want to use the Commission Processing – Single Sales Deal process variant. Because the commission settlement in this process variant is based on the feature for posting accruals with transactional documents, the posting for the journal entry related to the settlement document has been adapted for simplification reasons. However, this requires a small change for G/L account 21772000 used for accruals to allow tax posting.

Procedure

Check the Accounting and Financial Close (J58) scope item's test script for maintaining G/L account master data. For G/L account 21772000 and relevant company codes, enter –(Only input tax allowed) for the tax category. Alternatively, if you do not want to change the existing G/L account, create a new G/L account, optionally as a copy of 21772000, and make the required setting for the new G/L account. In the latter case, adapt the account determination as described in chapter Maintain Automatic Account Determination.

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction /App Name | Expected Results |
| --- | --- | --- | --- |
| Commission Processing – Billing Document |  |  |  |
| [Create Condition Contract](#unique_9) [page ] 49 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Check Business Volume (Optional)](#unique_27) [page ] 54 | Settlement Clerk - Commissions | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_28) [page ] 55 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_29) [page ] 56 | Settlement Clerk - Commissions | Manage Settlement Documents (F3254) |  |
| [Partial Settlement (Optional)](#unique_30) [page ] 57 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Check Settlement Document for Partial Settlement (Optional)](#unique_31) [page ] 59 | Settlement Clerk - Commissions | Manage Settlement Documents (F3254) |  |
| [Final Settlement](#unique_32) [page ] 61 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Check Settlement Document for Final Settlement](#unique_33) [page ] 62 | Settlement Clerk - Commissions | Manage Settlement Documents (F3254) |  |
| [Commission Processing – Billing Document Paid](#unique_34) [page ] 62 |  |  |  |
| [Post Incoming Payments (Optional)](#unique_35) [page ] 63 | Accounts Receivable Accountant | Post Incoming Payments (F1345) |  |
| [Create Condition Contract](#unique_36) [page ] 65 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Check Business Volume (Optional)](#unique_37) [page ] 69 | Settlement Clerk - Commissions | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_38) [page ] 70 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Partial Settlement (Optional)](#unique_39) [page ] 70 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Final Settlement](#unique_40) [page ] 70 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Commission Processing – Subscription Billing](#unique_41) [page ] 70 |  |  |  |
| [Create Condition Contract](#unique_42) [page ] 71 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Check Settlement Documents](#unique_43) [page ] 71 | Settlement Clerk - Commissions | Manage Settlement Documents (F3254) |  |
| [Commission Processing – Settlement Document](#unique_44) [page ] 71 |  |  |  |
| [Create Condition Contract](#unique_45) [page ] 72 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Commission Processing – Single Sales Deal](#unique_46) [page ] 75 |  |  |  |
| [Create Condition Contract](#unique_47) [page ] 76 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Check Pricing Element of Sales Order Item](#unique_48) [page ] 76 | Settlement Clerk - Commissions |  |  |
| [Final Settlement](#unique_49) [page ] 76 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Check Settlement Document for Final Settlement (Optional)](#unique_50) [page ] 76 | Settlement Clerk - Commissions | Manage Settlement Documents (F3254) |  |
| Commission Processing with Approval Workflow |  |  |  |
| [Create Condition Contract](#unique_51) [page ] 77 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Request Approval to Release Condition Contract](#unique_52) [page ] 81 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Trigger Rework of Condition Contract (Optional)](#unique_53) [page ] 82 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Rework Condition Contract (Optional)](#unique_54) [page ] 83 | Contract Manager - Commissions | My Inbox - All Items (F0862) |  |
| [Release Condition Contract](#unique_55) [page ] 84 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Check Business Volume (Optional)](#unique_56) [page ] 85 | Settlement Clerk - Commissions | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_57) [page ] 85 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Request Release of Condition Contract for Settlement](#unique_58) [page ] 85 | Settlement Clerk - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Release Condition Contract for Settlement](#unique_59) [page ] 86 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Partial Settlement (Optional)](#unique_60) [page ] 87 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Approve Release of Partial Settlement Document to Accounting (Optional)](#unique_61) [page ] 87 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Final Settlement](#unique_62) [page ] 88 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SV_ECOM) |  |
| [Approve Release of Final Settlement Document to Accounting](#unique_63) [page ] 88 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Commission Processing with Graduated Scales](#unique_64) [page ] 89 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Commission Processing with Conditions Maintained for Product Hierarchy Nodes](#unique_65) [page ] 90 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Commission Processing Using Service Rendered Date for Business Volume Selection](#unique_66) [page ] 91 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Final Settlement with Adjustments (Optional)](#unique_67) [page ] 92 | Contract Manager - Commissions | Manage Condition Contracts - External Commissions (F5989) |  |
| [Commission Unlikelihood (Optional)](#unique_68) [page ] 94 | Contract Manager - Commissions |  |  |
| [Reverse Settlement Document (Optional)](#unique_69) [page ] 95 | Settlement Clerk - Commissions | Reverse Settlement Documents - Condition Contracts (WB2R_CANCEL_DOCS) |  |

## Test Procedures

This chapter comprises the test procedures for different commission processing variants covered by this scope item. These variants result from different data sources for the business volume determination.

In the basic scenario described in the following first section, the data source is billing documents in sales without a payment check. As a first variation of the corresponding settlement process, you can choose to only consider paid billing documents. In the third section, you determine the business volume from billing documents that result from subscription billing transactions.

In the Commissions on Commissions business scenario, settlement documents for commissions form the data source. And in the Commissions for Single Sales Deals scenario, it is the accruals index table.

For each of these process variants you can also configure a workflow process. This is subject matter of section Commission Processing with Approval Workflow.

Finally, we describe some special aspects with chapters Final Settlement with Adjustments, Commission Unlikelihood, and Reverse Settlement Document.

During the condition contract creation, you can also use a customer hierarchy node in combination with condition contract types for customers. Only hierarchies of type Customer Hierarchy – Sales can be used.

### Commission Processing – Billing Document

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for an external sales agent as Condition Contract Partner.

In the following steps, we show how to create a 0CS1 Commissions External: Billing Document condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - External Commissions (F5989). | The Manage Condition Contracts - External Commissions screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - External Commissions screen, choose Create.Select the following Condition Contract Type:0CS1 Commission External: Billing Document |  |  |
| 4 | Enter Condition Contract Details | On the Create Commission External: Billing Document screen, make the following entries and choose Enter:Supplier: 33300095From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant (Optional) | On the Basic Data tab, enter one of the condition contract process variants which varies the basic scenarios. Then choose Enter:Option A:Process Variant: ZC02 Sales Commissions with Tax Free GoodsOption B:Process Variant: ZC03 Sls Commission Split Criteria AdaptationOption C:Process Variant: ZC04 Commission Selection Criteria Adaptation |  |  |
| 6 | Enter Purchasing Data | On the Purchasing tab, make and check the following entries:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310 |  |  |
| 7 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned then the text will not appear in the output form as in the German business partners the communication language German is maintained. |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line.Make the following entries and choose Enter.Field Combination: 0026 Commission RecipientInclusion Indicator (Incl/Excl): InclusiveCommission Recipient: 33300095Note When you want to use the commission recipient as business volume selection criterion, you have to enter the commission recipient in sales order items for partner function ES. When you have already created such sales orders when processing scope item Sell from Stock (BD9), you enter here the commission recipient you have used.Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer. |  |  |
| 9 | Check Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts PayableIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This is always the case for Fixed Amount condition contracts but can also happen when you do a settlement before you have created transactional documents. |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Continue.Settlement Date: for example, <validity end of condition contract>Settlement Date Type: Final SettlementSelect New Line.Make the following entries and choose Continue.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and choose Continue.Settlement Date: for example, <today's date>Settlement Date Type: Delta AccrualsNote The creation of the line with Settlement Date Type: Delta Accruals is optional. The creation of the line with Settlement Date Type: Partial Settlement is optional. |  |  |
| 11 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and choose Enter.Condition Type: RCS1 CommissionCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scaleNote In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 12 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 13 | Enter Condition Data | In the Conditions Area, select New Condition.Make the following entries and choose Enter.Condition Type: RCA1 Commission AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Note This condition is used to calculate the amount for accruals.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 14 | Release Condition Contract | Choose Release. |  |  |
| 15 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

#### Check Business Volume (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the business volume for the condition contract.

Prerequisites

Use this step if you have prepared transactional data to create billing documents related to a condition contract for an external sales agent.

Note

You can repeat this process step at every point in time in the test procedure. It’s recommendable to check the business volume before you start a settlement run to enable a control of the business volume determined for a settlement document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Business Volume - Condition Contracts (WB2R_BUSVOL). | The Business Volume for Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Business Volume for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract created in the previous step>Business Volume Base: From ContractOutput Level Business Volume: Settlement Date and Split Criteria |  |  |
| 4 | Check Business Volume for Condition Contracts | Choose Execute. | Business volume is determined based on the existing billing documents. |  |

#### Delta Accruals Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a delta accruals settlement for the condition contract. With this delta accruals settlement, you post accruals for the billing documents related to the condition contract.

Prerequisites

Use this step if you have executed the Sell from Stock scenario for the condition contract for an external sales agent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Sales Commissions (WB2R_SV_ECOM). | The Settlement of Supplier Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Settlement of Supplier Condition Contracts screen, make the following entries and choose Execute:Settlement Date: for example, <today's date>Settlement Date Type: 3 Delta AccrualsCondition Contract: <number of condition contract created in this test>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No Filter | The settlement document for posting delta accruals is created. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Documents screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the delta accruals settlement and click the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transfer to Accounting. | The posting status is Accounting document has been created (C). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data, check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 7 | Check Pricing of Items | Click an item in the table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all the items. | The system has determined the relevant business volume and displays it for condition type RCBV Commision BusVol.The system has calculated the accruals amount with the relevant conditions maintained in the condition contract. |  |
| 8 | Check Journal Entry | Go back to the Settlement Document screen.Under Document Flow, choose the main customer journal entries. Click the icon right to the box and select Display Journal Entries from the pop-up window. | You see the financial posting as below. |  |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 61500000 (Sales Commissions) | <Accruals amount> | 0 |
| 21772000 (Sales Commis. Provi.) | 0 | <Accruals amount> |

#### Partial Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a partial settlement for the condition contract. In this step, you also reverse the accruals posted before.

Prerequisite

Use this step if you have executed the Sell from Stock (BD9) scenario related to this commission condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Sales Commissions (WB2R_SV_ECOM). | The Settlement of Supplier Condition Contracts screen displays. |  |
| 3 | Select Condition Contract Type | On the Settle Sales Commission screen, make the following entries and choose Execute.Settlement Date: for example, <tomorrow's date>Settlement Date Type: 1 Partial SettlementCondition Contract: <number of condition contract created in this test>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No FilterTake a note of the number of the invoice created. | The Log for Supplier Condition Contract Settlement screen displays. A settlement document is created. Accruals are reversed. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Document screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the partial settlement and click the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transferred to Accounting. | The posting status is Accounting document has been created (C). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data, check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Partner Data | Under Partner Data, check the partner information. | You see the partner data maintained in the master data. |  |
| 7 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 8 | Check Pricing of Items | Click an item in the table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all the items. | The system has determined the relevant business volume and displays it for condition type RCBV Commission BusVol. The system has calculated the commissions amount with condition type RCS1 maintained in the condition contract and the input tax with the percentage for full tax. The system shows the amount of reversed accruals for condition type RCA2 and the amount for excess accruals for condition type RCA5. |  |
| 9 | Check Output | Go back to the Settlement Document screen, under Output Items, check the output items.Find the item with Channel: Print and choose Open File under Display. | You see the output print form. |  |
| 10 | Check Journal Entries | Under Document Flow, choose the main customer journal entries. Click the icon right to the box and select Display Journal Entries from the pop-up window. | You see the financial posting as below.The accruals reversal amount is the difference between the amount of reversed accruals and the excess accruals as mentioned in step 8. |  |
| 11 | Check Texts | Go back to the Manage Settlement Documents screen.In the Settlement Documents table, click the settlement document number and select Display Settlement Document from the pop-up window.Choose Header Texts. Under Texts, check the text information. | For text type Contract Text for Output/Forms, you see the text maintained in the condition contract for text type Text for Settlement Document. |  |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 21100000 (Paybls Domestic) | 0 | <Sales commissions amount + Input tax> |
| 61500000 (Sales Commissions) | <Sales commissions amount> | 0 |
| 12600000 (Input Tax (VST)) | <Input tax> | 0 |
| 61500000 (Sales Commissions) | 0 | <Accruals reversal amount> |
| 21772000 (Sales Commis. Provi.) | <Accruals reversal amount> | 0 |

#### Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a final settlement for the condition contract. In this step, you also reverse the accruals posted before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Sales Commissions (WB2R_SV_ECOM). | The Settlement of Supplier Condition Contracts screen displays. |  |
| 3 | Select Condition Contract Type | On the Settlement of Supplier Condition Contracts screen, make the following entries and choose Execute.Settlement Date: for example, <end of current year date>Settlement Date Type: Final SettlementCondition Contract: <Number of condition contract created in this test>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No FilterTake a note of the number of the invoice created. | The Log for Supplier Condition Contract Settlement screen displays. A settlement document representing a supplier invoice is created. Accruals are reversed. |  |

#### Check Settlement Document for Final Settlement

Please follow process steps of [Check Settlement Document for Partial Settlement (Optional)](#unique_31) [page ] 59.

Note the following difference: for the pricing elements of the settlement document items, check that all accruals are reversed. That means the amount for excess accruals for condition type RCA5 is zero.

### Commission Processing – Billing Document Paid

Purpose

This section outlines two available methods for configuring condition contracts to settle commissions based on paid billing documents:

1. Using Condition Contract Type 0CS3

In this method, both accruals and settlement values are calculated based only on paid (cleared) billing documents.

1. Using Condition Contract Type 0CS1 with Process Variant ZC06 (or 0CS7 for Subscription Billing)

In this method, you can use condition contract type 0CS1 together with the process variant ZC06 Sales Commission on Paid Invoices, as described in the section Define Process Variant for Commissions on Paid Invoices.

Accruals are calculated based on all billing documents regardless of whether they are paid (cleared) or open. But the settlement is performed using business volume only from the paid (cleared) billing documents.

Alternatively, condition contract type 0CS7 can be used when billing data comes from SAP Subscription Billing.

|  |
| --- |
| Note The application does not differentiate between partially and fully paid billing documents, and always takes the full amount in either case. |

Prerequisite

You have activated condition contract type 0CS7 Commission External Subscription Bill as described in chapter Activate Condition Contract Types (Optional).

#### Post Incoming Payments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you post the incoming payments from the customer.

|  |
| --- |
| NoteThis is an optional step and applies to condition contract type 0CS3 – Commission External: Billing Doc Paid. It also applies when using condition contract type 0CS1 with process variant ZC06 – Sales Commission on Paid Invoices, or 0CS7 for Subscription Billing.If you are testing Commissions Processing: Billing Document Paid scenario, and accounting document is not cleared, you have to follow the steps below. For other options of making incoming posting to clear account receivables, refer to Accounts Receivable (J59) scope item. |

Prerequisites

Invoices are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Incoming Payments (F1345). | The Post Incoming Payments screen displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code: 3310Posting Date: <date>Journal Entry Date: <date>Value Date: for example, <today's date>Journal Entry Type: DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank Data area.G/L Account: 11001060House Bank/Account ID: AEBK1/AEAC1 or AEBK2/AEAC2Amount: <customer invoice amount>Note If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency: AED |  |  |
| 5 | Enter Open Items | Make the following entries:Customer Account: 33100001Choose Propose Items. | The open items display in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Down Payment | Note Only execute this step if the payment is for an invoice where a down payment will be applied.In the Items to Be Cleared column,Allocated Amount: enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be appliedChoose Enter. | The balance is zero and the document can be posted. |  |
| 8 | Post Entries | Choose Post. | The Activated dialog box displays details of document number generated. |  |
| 9 | Post on Account | Repeat steps 1 to 4. |  |  |
| 10 | Enter Data | Choose Post on account and make the following entries:Account Type: CustomerCustomer: 33100001Credit Amount: same amount as in step 4 |  |  |
| 11 | Save | Choose Post. | Document is posted. |  |

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for an external sales agent as Condition Contract Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - External Commissions (F5989). | The Manage Condition Contracts - External Commissions screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - External Commissions screen, choose Create.Select the following Condition Contract Type:Option A:0CS3 Commission External: Billing Doc PaidOption B:0CS1 Commission External: Billing Document or0CS7 Commission External: Subscription BillNote To use condition contract type 0CS1 or 0CS7, select the process variant ZC06 on the Basic Data tab. |  |  |
| 4 | Enter Condition Contract Details | On the Create Commission External: Billing Doc Paid screen, make the following entries and choose Enter:Supplier: 33300095From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Purchasing Data | On the Purchasing tab, make and check the following entries:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310 |  |  |
| 6 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned, then the text will not appear in the output form, as in the German business partners the communication language German is maintained. |  |
| 7 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line. Make the following entries and choose Enter.Field Combination: 0026 Commission RecipientInclusion Indicator (Incl/Excl): InclusiveCommission Recipient: 33300095Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer.Note When you want to use the commission recipient as business volume selection criterion, you have to enter the commission recipient in sales order items for partner function ES. When you have already created such sales orders when processing scope item Sell from Stock (BD9), you enter here the commission recipient you have used. |  |  |
| 8 | Check Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts PayableIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This is always the case for Fixed Amount condition contracts but can also happen when you do a settlement before you have created transactional documents.If you have selected the process variant for external commission on paid invoices in step 3, make the following entry and choose Enter:Business Volume Table Group: 0C01 External Commission Only Paid Invoices |  |  |
| 9 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Enter.Settlement Date: for example, <validity end of condition contract>Settlement Date Type: Final SettlementSelect New Line.Make the following entries and choose Enter.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and choose Enter.Settlement Date: for example, <today's date>Settlement Date Type: Delta AccrualsNote The creation of the line with Settlement Date Type: Delta Accruals is optional. The creation of the line with Settlement Date Type: Partial Settlement is optional. |  |  |
| 10 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and choose Enter.Condition Type: RCS1 CommissionCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scaleNote In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 11 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 12 | Enter Condition Data | In the Conditions Area, select New Condition.Make the following entries and choose Enter.Condition Type: RCA1 Commission AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Note This condition is used to calculate the amount for accruals.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 13 | Release Condition Contract (Optional) | Choose Release. |  |  |
| 14 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

#### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps of [Check Business Volume (Optional)](#unique_27) [page ] 54.

#### Delta Accruals Settlement (Optional)

Please follow process steps of chapter [Delta Accruals Settlement (Optional)](#unique_28) [page ] 55. On the selection screen, enter the different condition contracts belonging to this test. After you have processed the delta accruals settlement you can optionally check the created settlement documents as described in chapter [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_29) [page ] 56.

#### Partial Settlement (Optional)

Please follow steps in [Partial Settlement (Optional)](#unique_30) [page ] 57. On the selection screen, enter the different condition contracts belonging to this test. After you have processed the partial settlement you can optionally check the created settlement documents as described in chapter [Check Settlement Document for Partial Settlement (Optional)](#unique_31) [page ] 59.

#### Final Settlement

Please follow steps in [Final Settlement](#unique_32) [page ] 61. On the selection screen, enter the different condition contracts belonging to this test. After you have processed the final settlement you can optionally check the created settlement documents as described in chapter [Check Settlement Document for Partial Settlement (Optional)](#unique_31) [page ] 59.

### Commission Processing – Subscription Billing

Purpose

This section deals with a variant for the commission processing that uses billing documents from subscription billing as data source.

For this variant, there is the following special feature. In subscription billing, the commercial or sold products are the relevant business objects for profitability analysis and not the component materials (one-time, recurring, usage). Accordingly, the sold product is mapped to the material in settlement documents so that the material split criterion becomes effective for the sold product. In the business volume selection criteria, you can specify both the sold products as well as the component materials for instance to restrict the commissions to the recurring component only.

This process variant is represented by condition contract type 0CS7 Commission External Subscription Bill. The test procedure is very similar to the basic process variant so that we only describe the differences to the basic variant.

Prerequisite

You have activated condition contract type 0CS7 Commission External Subscription Bill as described in chapter Activate Condition Contract Types (Optional).

#### Create Condition Contract

Please refer to chapter [Create Condition Contract](#unique_9) [page ] 49 to create the condition contract except for the following differences:

1. Condition Contract Type. Select condition contract type 0CS7 Commission External Subscription Bill.
2. Business Volume Selection Criteria. Choose field combination 0068 Product Sold to specify relevant commercial products used in subscription billing.

|  |
| --- |
| Note Materials attributes such as material group or material price group are not available as business volume selection criteria in this process variant. In billing document items resulting from subscription billing, these attributes refer to the component materials and are therefore not appropriate to specify the relevant commercial products. |

#### Check Settlement Documents

Please refer to chapters [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_29) [page ] 56 and [Check Settlement Document for Partial Settlement (Optional)](#unique_31) [page ] 59 to check settlement documents with the following addition aspect:

In step Check Document Items control that the commercial products from subscription billing appear as products.

### Commission Processing – Settlement Document

Purpose

This section deals with a variant for the commission processing that uses another data source to determine the relevant business volume: settlement documents for commissions. Accordingly, this variant is sometimes called commissions on commissions. An example for this scenario is that a parent company pays an additional (usual lower) commission amount on top of the commission amount that the sales company pays to an external sales agent. This process variant is represented by condition contract type 0CC1 Commission External: Settlement Document.

Again, the test procedure is very similar to the basic process variant. As a main difference, we describe how you can specify the settlement document with commissions in the business volume selection criteria.

Delta accruals settlements usual do not play a role for this process variant. Partial and final settlement are processed as described for the basic process variant. When you check a settlement document, control that the business volume amount of an item in the new settlement document is identical to the commission amount in the item of the first commission settlement document.

Prerequisite

You have activated condition contract type 0CC1 Commission External: Settlement Document as described in chapter Activate Condition Contract Types (Optional).

You have run the sales commission for the first payment so that settlement documents with commissions are available from partial or final settlement.

#### Create Condition Contract

Purpose

In this process step, you create a condition contract for an external sales agent as condition contract partner with previous settlement documents for commissions as business volume base. You can select settlement documents using business object related selection criteria such as materials. Alternatively, you can also specify the condition contract controlling the first commissions payment as selection criterion as shown below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - External Commissions (F5989). | The Manage Condition Contracts - External Commissions screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - External Commissions screen, choose Create.Select the following Condition Contract Type:0CC1 Commission External: Settlement Document |  |  |
| 4 | Enter Condition Contract Details | On the Create Commission External: Billing Document screen, make the following entries and choose Enter:Supplier: 33300095From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Purchasing Data | On the Purchasing tab, make and check the following entries:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310 |  |  |
| 6 | Enter Header Text | On the Header Texts tab, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned then the text will not appear in the output form as in the German business partners the communication language German is maintained. |  |
| 7 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line.Make the following entries and choose Enter.Field Combination: 0045 Condition ContractInclusion Indicator (Incl/Excl): InclusiveCondition Contract: <condition contract for first commission> |  |  |
| 8 | Check Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts PayableIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This is always the case for Fixed Amount condition contracts but can also happen when you do a settlement before you have created transactional documents. |  |  |
| 9 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Continue.Settlement Date: for example, <validity end of condition contract>Settlement Date Type: Final SettlementSelect New Line.Make the following entries and choose Continue.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and choose Continue.Settlement Date: for example, <today's date>Settlement Date Type: Delta AccrualsNote The creation of the line with Settlement Date Type: Delta Accruals is optional. The creation of the line with Settlement Date Type: Partial Settlement is optional. |  |  |
| 10 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and choose Enter.Condition Type: RCS1 CommissionCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scaleNote In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 11 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 12 | Enter Condition Data | In the Conditions Area, select New Condition.Make the following entries and choose Enter.Condition Type: RCA1 Commission AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Note This condition is used to calculate the amount for accruals.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 13 | Release Condition Contract | Choose Release. |  |  |
| 14 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

### Commission Processing – Single Sales Deal

Purpose

This section deals with a variant for the commission processing that allows you to specify the commission amount individually for each sales order item. This variant is based on the feature for posting accruals with transactional documents. In the condition contract, you do not specify a commission condition but only an accruals condition. This accruals condition is used to determine the accruals default value for a sales order item, now also representing the commission amount. As amount and condition value are now editable for this condition type in the pricing elements of the sales order item, you can change the commission amount if required.

As usual for an accruals condition, the accruals / commission amount is posted to the accruals index table. In the final settlement, the commission amount is extracted from the accruals index table and inserted in the pricing elements of a settlement document without further calculation. The business volume, still visible in the pricing elements of a settlement document item, is for information only.

This process variant is represented by condition contract type 0CS5 Commission Ext: Bill Doc DirectSettlemnt. Because the commission settlement is based on the feature for posting accruals with transactional documents, delta accruals and partial settlement do not play a role for this process variant and are therefore not active for the condition contract type. In the following test procedure description, we only focus on the specifics.

Prerequisite

You have activated condition contract type 0CS5 Commission Ext: Bill Doc DirectSettlemnt as described in chapter Activate Condition Contract Types (Optional).

You have enhanced relevant pricing procedures for sales orders with condition type RCA9 as described in chapter Posting of Accruals with Transactional Documents (Optional).

You must create the condition contract first, so that the system can determine the accruals condition in the pricing for a sales order item.

#### Create Condition Contract

Please refer to chapter [Create Condition Contract](#unique_9) [page ] 49 to create the condition contract except for the following differences:

1. Condition Contract Type. Select condition contract type 0CS5 Commission Ext: Bill Doc DirectSettlemnt.
2. Settlement Calendar. You can only specify dates for final settlement.
3. Condition Area. Enter a condition record for condition type RCA9.

#### Check Pricing Element of Sales Order Item

Please refer to test script of Sell from Stock (BD9) to display pricing elements of a sales order item. Check that the commission amount for condition type RCA9 is calculated according to your entries in the condition contract. If required, change the amount or condition value for the commission condition type.

#### Final Settlement

Please refer to chapter [Final Settlement](#unique_32) [page ] 61 to perform a final settlement for your condition contract.

#### Check Settlement Document for Final Settlement (Optional)

Please follow the process steps in chapter [Check Settlement Document for Partial Settlement (Optional)](#unique_31) [page ] 59.

First, note the following difference for the pricing elements: Check that the total commission amount is displayed for condition type RCAS Commission AccrSettl and that the tax is calculated for this amount.

Second, check the simplification of postings for the journal entry. As the process variant for single sales deal is based on the feature for posting accruals with transactional documents, the usual accruals reversal posting with a partial or final settlement is not required. When you bring together the postings of the journal entry and the posting for accruals with the billing document, you see that G/L account 21772000 for accruals is balanced. Remaining journal entry items correspond to the first three lines of the financial posting shown in chapter Check Settlement Document for Delta Accruals Settlement (Optional).

Financial Posting

Journal Entry for Settlement Document

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 21100000 (Paybls Domestic) | 0 | <Accruals amount + Input tax> |
| 21772000 (Sales Commis. Provi.) | <Accruals amount> | 0 |
| 12600000 (Input Tax (VST)) | <Input tax> | 0 |

Accruals Posting with Billing Document

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 61500000 (Sales Commissions) | <Sales commissions amount> | 0 |
| 21772000 (Sales Commis. Provi.) | 0 | <Accruals amount> |

### Commission Processing with Approval Workflow

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for an external sales agent as Condition Contract Partner.

In the following steps, we show how to create a 0CS1 Commissions External: Billing Document condition contract with approval process active.

Prerequisite

As prerequisite for this process step, you have complete steps mentioned in preliminary steps for creating a process variant with approval process active and performed chapters for configuring approval workflow in Configure Approval Workflow (Optional).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - External Commissions (F5989). | The Manage Condition Contracts - External Commissions screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - External Commissions screen, choose Create.Select the following Condition Contract Type:0CS1 Commission External: Billing Document |  |  |
| 4 | Enter Condition Contract Details | On the Create Commission External: Billing Document screen, make the following entries and choose Enter:Supplier: 33300095From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant | On the Basic Data tab, make the following entries and choose Enter:Process Variant: ZC01 Sales Commission with Workflow |  |  |
| 6 | Enter Purchasing Data | On the Purchasing tab, make and check the following entries:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310 |  |  |
| 7 | Enter Header Text | On the Header Texts tab, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned then the text will not appear in the output form as in the German business partners the communication language German is maintained. |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line. Make the following entries and choose Enter.Field Combination: 0026 Commission RecipientInclusion Indicator (Incl/Excl): InclusiveCommission Recipient: 33300095Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer.Note When you want to use the commission recipient as business volume selection criterion, you have to enter the commission recipient in sales order items for partner function ES. When you have already created such sales orders when processing scope item Sell from Stock, you enter here the commission recipient you have used. |  |  |
| 9 | Check Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts PayableIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This is always the case for Fixed Amount condition contracts but can also happen when you do a settlement before you have created transactional documents. |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Enter.Settlement Date: for example, <validity end of condition contract>Settlement Date Type: Final SettlementSelect New Line.Make the following entries and choose Enter.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and choose Enter.Settlement Date: for example, <today's date>Settlement Date Type: Delta AccrualsNote The creation of the line with Settlement Date Type: Delta Accruals is optional. The creation of the line with Settlement Date Type: Partial Settlement is optional. |  |  |
| 11 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and choose Enter.Condition Type: RCS1 CommissionCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scaleNote In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 12 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 13 | Enter Condition Data | In the Conditions Area, select New Condition.Make the following entries and choose Enter.Condition Type: RCA1 Commission AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Note This condition is used to calculate the amount for accruals.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 14 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

#### Request Approval to Release Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request an approval for releasing a commission condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - External Commissions (F5989). | The Manage Condition Contracts - External Commissions screen displays. |  |
| 3 | Request Release of Condition Contract | In the Condition Contracts table, choose the line with the condition contract for which you want to request an approval for release.Choose Change Condition Contract after clicking on condition contract number.Choose Menu > Edit > Request Approval .Choose Save. | The status for the condition contract now should be:NewApproval RequestedThe condition contract with the request for release approval goes to Sales Manager's Inbox. |  |

#### Trigger Rework of Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the status of a commission condition contract and trigger a rework of the condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Display the Relevant Condition Contract | Find the condition contract for which Contract Manager – Commissions has just requested the approval for release: Release Condition Contract XXXXXXXXXXX. | The details of the condition contract display on the right of the screen. |  |
| 4 | Check Condition Contract Data and Send Back for Rework | Check the Settlement Lock Status and Status of the condition contract.Now the settlement lock status is Not Locked and the status is New.As the Contract Manager – Commissions has not set the status to be Locked for Settlement, choose Rework.On the Submit Decision pop-up window, enter a decision note, for example, please set the condition contract to Locked for Settlement.Choose Submit. | The condition contract is sent back to Contract Manager – Commissions. |  |

#### Rework Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you rework a commission condition contract in order to set the Lock for Settlement status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Check the Notification and Go to Change Mode | Open the notification: Rework Condition Contract XXXXXXXXXXX.Choose Show Details at the bottom and check the comments on the right side of the screen. Under the Comments tab, there is a message from the Sales Manager: please set the condition contract to Locked for Settlement.Choose Hide Details at the bottom and choose More Details on the upper right of the screen.On the Display External Commissions screen, choose Menu > Condition Contract > Change . | You check the comment from the Sales Manager and go to the change mode for condition contract. |  |
| 4 | Set Condition Contract to Locked for Settlement Status | On the Change External Commissions screen, choose Menu > Edit > Lock Settlement .Choose Save.Choose Continue in the dialog box. | The settlement lock status is changed to Locked and the status for condition contract is New. |  |
| 5 | Complete Rework for the Condition Contract | Choose Rework Completed at the bottom.On the Submit Decision pop-up window, enter a decision note: for example, the condition contract is set to Locked for Settlement.Choose Submit. | The condition contract is sent to Sales Manager for release approval again. |  |

#### Release Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a commission in an approval workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Release Condition Contract | Find the condition contract for which Contract Manager – Commissions has just requested an approval for release: Release Condition Contract XXXXXXXXXXX.Choose Release at the bottom.Choose Submit in the dialog box. | The condition contract is released now. |  |

#### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps of [Check Business Volume (Optional)](#unique_27) [page ] 54.

#### Delta Accruals Settlement (Optional)

Please follow steps in [Delta Accruals Settlement (Optional)](#unique_28) [page ] 55.

#### Request Release of Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a commission condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - External Commissions (F5989). | The Manage Condition Contracts - External Commissions screen displays. |  |
| 3 | Send Condition Contract for Release of Settlement | Find the condition contract for which you want to request the approval to release it for settlement. Choose Change Condition Contract via More Links when choosing condition contract number.Choose Menu > Edit > Request Settlement Approval .Choose Save.Choose Continue in the dialog box.Note Please choose Menu > Edit > Lock Settlement before clicking Request Settlement Approval if you haven't executed steps in chapter [Rework Condition Contract (Optional)](#unique_54) [page ] 83. | The status for the condition contract now should be:ReleasedLocked for SettlementSettlement Approval RequestedNow the request to release condition contract goes to Sales Manager's Inbox. |  |

#### Release Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Release Condition Contract for Settlement | Find the condition contract for which Settlement Clerk – Commissions has just requested an approval for release.Position the notification: Release Condition Contract for settlement XXXXXXXXXXX in the inbox.Choose Release.Choose Submit in the dialog box. | The condition contract is released now for settlement. |  |

#### Partial Settlement (Optional)

Please follow process steps of chapter [Partial Settlement (Optional)](#unique_30) [page ] 57.

On the selection screen, enter the different condition contracts belonging to this test. After you have processed the partial settlement you can optionally check the created settlement documents as described in chapter [Check Settlement Document for Partial Settlement (Optional)](#unique_31) [page ] 59.

#### Approve Release of Partial Settlement Document to Accounting (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you approve the release of the settlement document - created in partial settlement - to Accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Approve Release to Accounting | Find the settlement document for which the release to accounting has to be approved. The approval was triggered automatically after the settlement has been processed by the Settlement Clerk – Commissions.Position the notification: Approve Settlement XXXXXXXXXXX in the inbox.Choose Approve.Choose Submit in the dialog box. | The settlement document is released to accounting. |  |

#### Final Settlement

Please follow process steps of chapter [Final Settlement](#unique_32) [page ] 61.

On the selection screen, enter the different condition contracts belonging to this test.

|  |
| --- |
| Note Since the workflow is activated, in this step, you will see the following messages including: |

Contract XXXXXXXXXXX locked after final settlement

Document XXXXXXXXXXX with document status Workflow Release Required is blocked for follow-on documents

Document XXXXXXXXXXX saved (no accounting document generated)

Document XXXXXXXXXXX is processed with reference XXXXXXXXXXX

#### Approve Release of Final Settlement Document to Accounting

In this process step, you approve the release of the settlement document - created in final settlement - to Accounting.

Process the steps described in the chapter [Approve Release of Partial Settlement Document to Accounting (Optional)](#unique_61) [page ] 87.

### Commission Processing with Graduated Scales

The default calculation of the scales that are set up in the condition table in condition contracts works like volume pricing. This means that on the execution of settlements, the application would apply the rate of the tier that it finds when looking for the business volume, on the entire amount and not only the delta amount:

If you set up the conditions as for example:

| Business Volume | Commission Percentage |
| --- | --- |
| (From) 1,000 EUR | 10% |
| (From) 6,000 EUR | 20% |
| (From) 10,000 EUR | 30% |

Then the settlement run would calculate the commissions as follows:

| Business Volume found at the time of settlement | Total Effective Commission at the time of settlement |
| --- | --- |
| 999 EUR | 0 EUR |
| 6,000 EUR | 1,200 EUR |
| 11,000 EUR | 3,300 EUR |

However, if you would like to set up graduated scales that work like tiered pricing instead of volume pricing, then you need to set up the condition contract slightly differently.

Follow the steps as in the chapter [Create Condition Contract](#unique_9) [page ] 49. In step 9, choose the value of the field Settlement Calculation Method as Graduated-To-Scale. Then in step 12, maintain the scales with scale type as To-scale.

Thereafter, if you set up the conditions as for example:

| Business Volume | Commission Percentage |
| --- | --- |
| (To-scale) 1,000 EUR | 0% |
| (To-scale) 5,000 EUR | 10% |
| (To-scale) 11,000 EUR | 20% |
| (To-scale) 999,999 EUR | 30% |

Then the settlement run would calculate the commissions as follows:

| Business Volume found at the time of settlement | Total Effective Commission at the time of settlement |
| --- | --- |
| 1,000 EUR | 0 EUR |
| 5,000 EUR | 400 EUR |
| 11,000 EUR | 1,600 EUR (= 400 EUR +1,200 EUR) |

In the example above, the calculation works in the following manner.

When business volume is found to be 1,000 EUR, then the first tier with 0% commission is applicable. Hence, the commission is 0 EUR.

When business volume is found to be 5,000 EUR, then the second condition rate with 10% commission is applicable on the difference of business volumes between the first and second scales. Hence, the commission is calculated as 400 EUR.

When business volume is found to be 11,000 EUR, then three condition rates would be applicable. This means that the commission would be calculated at the rate of 0% for 1,000 EUR, 10% for 4,000 EUR and 20% for the remaining 6,000 EUR, resulting in 0, 400 and 1,200 EUR, respectively. Hence, the total commission value comes to 1,600 EUR.

### Commission Processing with Conditions Maintained for Product Hierarchy Nodes

In condition contracts, another condition table V 4CV Condition Contract/Product Hierarchy enables you to maintain different condition rates for several product hierarchy nodes in a single contract for sales external commissions.

One good practice is to include the same hierarchy nodes also in the business volume selection criteria, to make the selection of transactional documents as precise as possible. By doing this, you will see the business volumes only for those products which are part of the hierarchy nodes in your condition tables and subsequently, the products which were not part of the hierarchy will not be considered during the settlement run. If you don’t maintain the condition contract in this manner, then even the products which are not part of the hierarchy will be part of the settlement but with 0 values, because no condition rate will be found for them, unless you have maintained conditions for those products additionally.

Please note that you will need to select the sub-nodes of the product hierarchy and not the root node, in the condition maintenance.

Follow the steps as in the chapter [Create Condition Contract](#unique_9) [page ] 49. In step 5, enter process variant ZC07 Activate Condition for Product Hierarchy as explained in chapter [Define Process Variant to Activate Condition Table for Product Hierarchy](#unique_18) [page ] 29. Then in step 11, select V 4CV Condition Contract/Product Hierarchy in the condition table dropdown and maintain the condition lines for the product hierarchy nodes as you need.

Split Criterion Usage in Process Variant

If your business need is to consider the product hierarchy information stored in the transactional data during the lifetime of the condition contract, even if the product hierarchy has been modified during that period, then in the process variant you should set the product hierarchy as a split criterion and include the same hierarchy nodes also in the business volume selection criteria. The impact of this is explained with an example below.

Product Hierarchy

| Hierarchy Node | Type | Product | Valid From | Valid To |
| --- | --- | --- | --- | --- |
| PH1 | Root |  | January 1st of the current year | December 31st of the current year |
| PH1-1 | Sub-node |  |  |  |
|  |  | TG11 |  |  |
|  |  | TG12 |  |  |
| PH1-2 | Sub-node |  |  |  |
|  |  | TG15 |  |  |

In this example, let's assume that on the March 31st of the current year, product TG11 is removed from the hierarchy.

Condition Contract Validity – January 1st of the current year – December 31st of the current year

Condition Rate – 10% for PH1-1

Partial Settlement Date – October 30th of the current year

The billing documents generated for the period January 1st of the current year to March 31st of the current year for product TG11, will include the hierarchy information PH1-1. The ones generated after that time, will not include the hierarchy information in them. At the time of settlement, the application will look at the data maintained in the billing documents and the ones having the hierarchy node in them will be considered for the business volume.

However, if your business need is to consider the product hierarchy only as it is at the time of settlement, then you should not set the split criterion for product hierarchy in the process variant. In that case, for the same example above, at the time of settlement, the application will find that TG11 is not part of the sub-node PH1-1 and therefore, it will not consider the business volume from the billing documents for TG11. But please note that if you have added new products to the hierarchy after the billing documents had been generated, then those billing documents will not have the information of the hierarchy stored in them and hence, will not be considered.

### Commission Processing Using Service Rendered Date for Business Volume Selection

In the standard scenario, the system uses the billing date to determine the business volume and the corresponding rates for settlement. However, there are some business scenarios where the business volume impacted by subsequent debit or credit memos (for example, price corrections or customer returns) needs to be considered for the same period as the original sales. One example of such a scenario is when rates vary across multiple periods within a condition contract’s validity duration. To handle these scenarios, you can use the service rendered date for business volume selection instead of the standard billing date, provided that the service rendered date of the subsequent billing document is the same as the service rendered date of the original billing document. This ensures that subsequent billing documents are processed using the rate from the original transaction period.

Example

Consider an agreement with different monthly rates. If you use the billing date:

| Transaction | Period | Amount | Rate | Calculation | Settlement Amount |
| --- | --- | --- | --- | --- | --- |
| Sale | January | $ 100 | 10% | $ 100 * 10% | $ 10 |
| Return | March | -$ 50 | 15% | -$ 50 * 15% | -$ 7.5 |

The business volume for the return is considered at 15%, which is higher than the 10% rate granted in January prior to the return.

If you use the service rendered date:

| Transaction | Period | Amount | Rate | Calculation | Settlement Amount |
| --- | --- | --- | --- | --- | --- |
| Sale | January | $ 100 | 10% | $ 100 * 10% | $ 10 |
| Return | March | -$ 50 | 15% | -$ 50 * 10% (January) | -$ 5 |

The business volume for the return is considered at the January rate of 10%, reflecting the rate originally granted.

This functionality is supported only for billing document–based calculations and applies to the following condition contract types:

- 0CS1 – Commission External: Billing Document
- 0CS5 – Commission Ext: Bill Doc Direct Settlement

To enable this feature, follow the steps described in the chapter [Create Condition Contract](#unique_9) [page ] 49 with the following differences:

- In step 5, choose Process Variant ZC08 as explained in chapter [Define Process Variant to Activate Business Volume Selection by Service Rendered Date](#unique_19) [page ] 32.
- In step 13, select condition type RCAA.

|  |
| --- |
| Caution In case of returns, the service rendered date can differ based on the type of return. For further details about how the service rendered date is filled, consult your Sales and Distribution experts. |

|  |
| --- |
| Note If you have different rates for different periods, then you need to create the settlement calendar with Final Settlement dates for each period for those rates to be correctly applied. Using the service rendered date for business volume selection can cause subsequent billing documents posted after a contract's final settlement to be excluded from settlement. For example, if the original billing document is created in December, final settlement runs in January, and a subsequent billing document is posted in February with a service rendered date in December, the subsequent billing document may not be considered in the final settlement because the contract has already been settled. To capture such late billing documents, you can use delta settlements in subsequent settlement runs. |

### Final Settlement with Adjustments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you enter conditions in the condition contract to adjust the final commission amount before you process the final settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - External Commissions (F5989). | The Manage Condition Contracts - External Commissions screen displays. |  |
| 3 | Change Condition Contract | On the Manage Condition Contracts - External Commissions screen, select the relevant condition contract and choose More Links.Choose Change Condition Contract from More Links. |  |  |
| 4 | Enter Condition Data for Rebate Condition | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition.Make one of the following entries and choose Enter.Adjustment of business volume:Cond. Type: RCBD Commission BusV DeltaValid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Condition Rate: for example, <100> AEDAdjustment of commission amount:Cond. Type: RCJ1 Commission AdjustmentValid From: for example, <today's date>Valid To: for example, <end of current year>Condition Rate: for example, <20> AEDEntry of a fixed settlement amount:Cond. Type: RCV1 Commission VerifiedValid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Condition Rate: for example, <1000> AEDNote The conditions entered here are used to adjust the commission amount. You can also choose Condition Contract / Material as condition level. You then also specify the material for a condition record. In case the Valid From and Valid To date are copied from the condition contract validity according to user settings, you can check and change these dates if necessary. |  |  |
| 5 | Save Condition Contract | Choose Save. |  |  |

After you have maintained the conditions to adjust the commission amount, you perform the final settlement as described in the chapter [Final Settlement](#unique_32) [page ] 61. Then check the created settlement document as described in [Check Settlement Document for Final Settlement](#unique_33) [page ] 62. In the pricing elements, particularly check that the system has determined the commission amount using the conditions for adjustment.

### Commission Unlikelihood (Optional)

Purpose

During the creation of the condition contract (Chapter [Create Condition Contract](#unique_51) [page ] 77) when entering the conditions, you have the option to use the condition: commission unlikelihood. You use condition type commission unlikelihood in case the minimum sales turnover will not be reached and therefore no accruals should be created or existing accruals should be reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Condition Data (Optional) | In the Conditions area, select New Condition.Make the following entries and choose Enter.Condition Type: RCU1 Commission UnlikelihoodCondition Rate: for example, <100%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract> |  |  |

### Reverse Settlement Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you reverse a settlement document for the condition contract.

Prerequisite

You have processed the settlement run to the condition contract(s).

Procedure

The steps below are using Reverse Settlement Documents Condition Contracts (WB2R_CANCEL_DOCS) for reversing settlement documents for the selected condition contract(s). You can use Reverse Settlement Document (WZR4) to reverse a single settlement document. You can also use Reverse Settlement Documents (WAB_CANCEL_B) to reverse several settlement documents together.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access Reverse Settlement Documents | Open Reverse Settlement Documents - Condition Contracts (WB2R_CANCEL_DOCS). | The Reverse Settlement Documents for Condition Contracts screen displays. |  |
| 3 | Reverse Settlement Documents for Condition Contracts | On the Reverse Settlement Documents for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract(s) created in this test>Check Run Only: <unselect this checkbox>Choose Execute.Choose Continue in the pop-up window. | The Log for Reversal of Settlement Documents - Live Run screen displays. All settlement documents for the selected condition contract(s) are reversed. |  |

## Follow-Up Processes

You have finished all the activities that are part of the business process described in this document.

To accomplish the subsequent activities of this business process, use the master data from this document and carry out the process steps described in one or more of the following scope items.

### Accounts Payable (Optional)

Purpose

In this process step, you open payables invoices that are automatically created from purchasing processes with Accounts Payables.

Procedure

Complete the activities described in the test script of the scope item Accounts Payable (J60) using the open supplier invoices created running the scope item Sales Commissions – External Sales Representative (2TT).

### General Ledger Reporting and CO-PA Reporting (Optional)

Purpose

After completing the activities in this test script, it is possible to run General Ledger Reporting and CO-PA Reporting connected with the accounts which were used in this sales commission process. Log on as General Ledger Accountant or Sales Accountant and run the reports which apply to your needs and check the postings on your accounts. Please refer to Accounting and Financial Close (J58) scope item to Manage G/L Account Master Data and Manage Financial Statement Versions.

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
- related-to :: [[08-sales-order-management/margin-optimization-sap-solution-extensions-by-vistex-7uq-test-script]]
- related-to :: [[08-sales-order-management/royalties-settlement-for-sales-55i-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[08-sales-order-management/sales-rebate-processing-1b6-ae-test-script-sap-s-4hana-cloud-public-ed]]
- related-to :: [[08-sales-order-management/test-script-condition-contract-with-customer-hierarchy-consumer-produc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 172,545 chars in the whole document
