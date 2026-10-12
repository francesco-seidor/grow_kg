---
id: 08-sales-order-management/royalties-settlement-for-sales-55i-ae-test-script-sap-s-4hana-cloud-pu
title: "Royalties Settlement for Sales (55I_AE) - Test Script, SAP S/4HANA Cloud Public Edition (55I_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 55I (AE, 2608): configuring and testing royalties settlement with condition contracts, process variants, workflow, intercompany and subscription cases."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/condition-contract-settlement]
aliases: [55I_S4CLD2608_BPD_EN_AE]
keywords: ["Rebates, Commissions and Royalties Settlement", royalties settlement, condition contracts, process variants, approval workflow, two-step settlement, intercompany royalties, delta accruals, graduated scales, service rendered date]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55I_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1070
topic: 08-sales-order-management/condition-contract-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Royalties Settlement for Sales (55I_AE) - Test Script, SAP S/4HANA Cloud Public Edition (55I_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55I_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Rebates, Commissions and Royalties Settlement** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Royalties Settlement for Sales (55I_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232856182)

[2 Prerequisites 5](#_Toc232856183)

[2.1 System Access 5](#_Toc232856184)

[2.2 Roles 5](#_Toc232856185)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232856186)

[2.4 Preliminary Steps 8](#_Toc232856187)

[2.4.1 Posting of Accruals with Transactional Documents (Optional) 9](#_Toc232856188)

[2.4.2 Prepare Transactional Data (Optional) 11](#_Toc232856189)

[2.4.3 Activate Condition Contract Types (Optional) 12](#_Toc232856190)

[2.4.4 Define Condition Contract Process Variants (Optional) 14](#_Toc232856191)

[2.4.4.1 Define Process Variant for Using the Workflow 15](#_Toc232856192)

[2.4.4.2 Define Process Variant for Tax Free Royalties 17](#_Toc232856193)

[2.4.4.3 Define Process Variant for Split Criteria Usage in Settlement 19](#_Toc232856194)

[2.4.4.4 Define Process Variant for Business Volume Selection Criteria Usage 22](#_Toc232856195)

[2.4.4.5 Define Process Variant for Contract Determination 25](#_Toc232856196)

[2.4.4.6 Define Process Variant for Handling Royalties in Service Contracts 27](#_Toc232856197)

[2.4.4.7 Define Process Variant for Intercompany Royalties Settlement 29](#_Toc232856198)

[2.4.4.8 Define Process Variant for Royalties on Paid Invoices 32](#_Toc232856199)

[2.4.4.9 Define Process Variant to Activate Business Volume Selection by Service Rendered Date 35](#_Toc232856200)

[2.4.4.10 Maintain Automatic Account Determination 38](#_Toc232856201)

[2.4.5 Configure Intercompany Royalties Settlement (Optional) 41](#_Toc232856202)

[2.4.5.1 Activate Condition Contract Types for Intercompany Royalties Settlement 42](#_Toc232856203)

[2.4.5.2 Specify Business Partner for Company Codes 42](#_Toc232856204)

[2.4.5.3 Maintain Settings for Export Tax 44](#_Toc232856205)

[2.4.5.4 Specify Tax Code Mapping 46](#_Toc232856206)

[2.4.6 Configure Approval Workflow (Optional) 48](#_Toc232856207)

[2.4.6.1 Create Business Roles for Workflow Processing 48](#_Toc232856208)

[2.4.6.2 Manage Teams and Responsibilities 49](#_Toc232856209)

[2.4.6.3 Manage Workflow for Condition Contracts - Release Contract 51](#_Toc232856210)

[2.4.6.4 Manage Workflow for Condition Contracts - Release Settlement 52](#_Toc232856211)

[2.4.6.5 Manage Workflow for Settlement Documents 53](#_Toc232856212)

[3 Overview Table 55](#_Toc232856213)

[4 Test Procedures 59](#_Toc232856214)

[4.1 Royalties Settlement Processing 59](#_Toc232856215)

[4.1.1 Create Condition Contract 59](#_Toc232856216)

[4.1.2 Check Business Volume (Optional) 63](#_Toc232856217)

[4.1.3 Delta Accruals Settlement (Optional) 65](#_Toc232856218)

[4.1.4 Check Settlement Document for Delta Accruals Settlement (Optional) 66](#_Toc232856219)

[4.1.5 Partial Settlement (Optional) 67](#_Toc232856220)

[4.1.6 Check Settlement Document for Partial Settlement (Optional) 68](#_Toc232856221)

[4.1.7 Final Settlement 71](#_Toc232856222)

[4.1.8 Check Settlement Document for Final Settlement (Optional) 72](#_Toc232856223)

[4.2 Two-Step Royalties Settlement Processing 72](#_Toc232856224)

[4.2.1 Create Condition Contract 72](#_Toc232856225)

[4.2.2 Check Business Volume (Optional) 76](#_Toc232856226)

[4.2.3 Delta Accruals Settlement (Optional) 76](#_Toc232856227)

[4.2.4 Partial Settlement (Optional) 76](#_Toc232856228)

[4.2.5 Collect Parked Settlement Documents for Transfer to Accounting (Optional) 77](#_Toc232856229)

[4.2.6 Final Settlement 78](#_Toc232856230)

[4.2.7 Collect Parked Settlement Documents from Final Settlement 78](#_Toc232856231)

[4.3 Royalties Settlement Processing with Approval Workflow 78](#_Toc232856232)

[4.3.1 Create Condition Contract 78](#_Toc232856233)

[4.3.2 Request Approval to Release Condition Contract 82](#_Toc232856234)

[4.3.3 Trigger Rework of Condition Contract (Optional) 83](#_Toc232856235)

[4.3.4 Rework Condition Contract (Optional) 84](#_Toc232856236)

[4.3.5 Release Condition Contract 85](#_Toc232856237)

[4.3.6 Check Business Volume (Optional) 86](#_Toc232856238)

[4.3.7 Delta Accruals Settlement (Optional) 86](#_Toc232856239)

[4.3.8 Request Release of Condition Contract for Settlement 86](#_Toc232856240)

[4.3.9 Release Condition Contract for Settlement 87](#_Toc232856241)

[4.3.10 Partial Settlement (Optional) 88](#_Toc232856242)

[4.3.11 Approve Release of Partial Settlement Document to Accounting (Optional) 88](#_Toc232856243)

[4.3.12 Final Settlement 89](#_Toc232856244)

[4.3.13 Approve Release of Final Settlement Document to Accounting 89](#_Toc232856245)

[4.4 Royalties Settlement Processing with Graduated Scales 90](#_Toc232856246)

[4.5 Royalties Settlement Processing Using Service Rendered Date for Business Volume Selection 91](#_Toc232856247)

[4.6 Royalties Related to Service Contracts (Optional) 92](#_Toc232856248)

[4.7 Intercompany Royalties Settlement Processing 94](#_Toc232856249)

[4.7.1 Create Condition Contract 95](#_Toc232856250)

[4.7.2 Check Business Volume (Optional) 98](#_Toc232856251)

[4.7.3 Final Settlement 98](#_Toc232856252)

[4.7.4 Check Settlement Document for Final Settlement (Optional) 99](#_Toc232856253)

[4.8 Royalties Settlement with Licensor for Subscription Business 102](#_Toc232856254)

[4.8.1 Create Condition Contract 102](#_Toc232856255)

[4.8.2 Delta Accruals Settlement (Optional) 103](#_Toc232856256)

[4.8.3 Partial Settlement (Optional) 103](#_Toc232856257)

[4.8.4 Final Settlement 103](#_Toc232856258)

[4.9 Final Settlement with Adjustments (Optional) 103](#_Toc232856259)

[4.10 Royalties Unlikelihood (Optional) 105](#_Toc232856260)

[4.11 Reverse Settlement Document (Optional) 105](#_Toc232856261)

[5 Follow-Up Processes 107](#_Toc232856262)

[5.1 Accounts Payable (Optional) 107](#_Toc232856263)

[5.2 General Ledger Reporting and CO-PA Reporting (Optional) 107](#_Toc232856264)

## Purpose

The Royalties Settlement scope item concerns the subsequent settlement of royalty conditions agreed upon with a licensor. You use condition contracts from Condition Contract Management to enter the royalty agreements with the licensors. In a condition contract, you specify the royalties recipient, organizational and process control parameter, the business volume selection criteria, the royalty conditions and the settlement calendar with settlement dates for delta accrual, partial and final settlement. The delta accruals settlement reflects a procedure in which accruals for royalties are not posted together with the transactional documents but subsequently in a specific settlement run. In the partial and final settlements of a condition contract you perform the royalties calculation based on business volume and royalty conditions and you create the settlement documents reflecting an invoice from the licensors for the granting license rights in sales deals. Settlement documents are usually immediately released to accounting. You can also create a two-step condition contract to collect and post settlement documents of different condition contracts in one journal entry to accounting. A special royalties scenario is the settlement between company codes when subsidiary companies must transfer some of the revenue to the parent company under license agreements. If licensed products such as software applications or cloud services are sold through subscription business, the business volume determination involves a mapping of commercial products to materials in settlement documents.

This scope item is closely related to sales business process as described for instance in the Sell from Stock (BD9) scope item. Ideally, the condition contract is created first before you start to enter sales orders in the system. However, you can also create condition contracts subsequently with a validity period starting in the past. Also, royalties processing and sales transactions run in parallel in that sense that you process partial settlements for billing documents entered continuously during the condition contract’s validity period.

After describing the general process flow, two special aspects are addressed at the end of the test script. When a defined minimum sales turnover for a royalties eligibility will probably not be reached, you are obliged to reverse existing accruals and prevent creating new accruals. This requirement is fulfilled with the help of an unlikelihood condition maintained in the condition contract. In addition, you can maintain conditions for adjusting the (final) settlement amount in the condition contract. You typically agree upon such adjustments with the licensor when there is a dissonance concerning the relevant business volume. You can maintain a condition for adjusting the business volume, for an additional royalties amount and for a final fixed royalties amount.

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
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Contract Manager - Royalties | SAP_BR_CONTR_MGR_ROYALTIES | Royalties | SAP_BR_CONTR_MGR_ROYALTIES |  |
| Settlement Clerk - Royalties | SAP_BR_SETL_CLERK_ROYALTIES | Royalties Settlement | SAP_BR_SETL_CLERK_ROYALTIES |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Tax Specialist | SAP_BR_TAX_SPECIALIST | Tax Rates | SAP_BR_TAX_SPECIALIST |  |

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
| Supplier (Licensor) | 33300096 |  |  |
| Purchasing Organization | 3310 |  |  |
| Purchasing Group | 001 |  |  |
| Company Code | 3310 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |

### Preliminary Steps

The business volume for royalties settlement is determined from billing documents. To prepare transactional test data you can follow the Sell from Stock (BD9) scope item and create sales orders, deliveries, and billing documents. To execute the BD9 scope item, materials must be available in stock. In the following we describe how you can set up an initial stock for materials when there is no or only low stock.

Define condition contract process variants to also test variations of the core process. A process variant is used to define limited variations for condition contract maintenance and settlement that are configured for a condition contract type without changing the overall character of the process defined by a condition contract type. In this chapter we describe process variants for different purposes. Note that you can also combine settings from these process variants. If you assign a condition contract process variant to a new condition contract you have to enhance the account determination settings. The process variant is a key field in the relevant condition table. We describe how you maintain account determination settings for the first process variant for approval workflow. Proceed in the same way for all other process variants that you want to test.

If you want to test the approval workflow as one of the possible process variations you have to maintain additional workflow settings and define teams and responsibilities. In contrast to sales rebates and sales commission processing, SAP currently does not provide a dedicated business role for a manager who monitors the royalties processing. Such a role within the Financial Operations area is planned when further scope items for Settlement Management will be provided. Because of that, SAP abstained from an assignment of workflow relevant business catalogs to business roles for royalties processing in the business content. Accordingly, this is the first step you have to do when maintaining workflow settings as described in chapter Assign Workflow Relevant Business Catalogs to Business Roles. To establish the workflow the Sales Manager has been chosen in this test script as business role for approval steps. In principle, you can choose another business role. Note that the assignment of business catalogs SAP_SD_BC_CC_WIAPPROVE_PC Sales – Condition Contract Approval and SAP_SD_BC_SDOC_WIAPRV_PC Sales – Condition Contract Settlement Document Approval is already maintained when either the Sales Rebate Processing or Sales Commissions - External Sales Representative scope item is active. Here, the assignment is part of the business content. Anyway, you have to assign business catalog SAP_SD_BC_CC_WIREWORK_PC Sales – Condition Contract Rework to business role SAP_BR_CONTR_MGR_ROYALTIES Contract Manager – Royalties.

#### Posting of Accruals with Transactional Documents (Optional)

Purpose

Accruals can be created when you post transactional documents ‒ billing documents released to accounting in this scope item ‒ or you can post accruals in an accumulated form with a specific settlement run called Delta Accruals Settlement as described in the test procedures. You can also combine the procedures, for instance, to determine a more accurate accruals amount in a weekly delta accruals run by considering all transactional documents.

To post accruals with released billing documents, you must include the accruals condition type in the pricing procedure of the sales order in an appropriate manner. As usual, this pricing element will be copied to the billing document. Below we describe the best practice approach that you include the condition type at the bottom of the pricing procedure. Note that you can similarly post accruals for other scope items (sales rebates, commissions) in parallel when you include the corresponding accruals condition types in the same way.

Posting accruals with transactional documents requires that you create the condition contract with the accruals condition before you create royalties relevant sales orders, so that the accruals condition is found during pricing of a sales order item. Relevant condition contracts are determined by matching sales order and condition contract data. If the system finds more than one relevant condition contract, you will accordingly get several lines for the accruals condition types in the pricing elements. When you create a condition contract with a validity period starting in the past, you can schedule a delta accruals settlement to post accruals for already created billing documents. Then you continue to post accruals with the transactional documents. When you want to create a new condition contract without specifying a customer as the business volume selection criterion, define a condition contract process variant as described in chapter Define Process Variant for Contract Determination and enter it for the condition contract.

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
| 7 | Add Accruals Condition Type | Choose New Entries and make the following entries:Step Number: <number higher than maximum hitherto>Condition Type: RRA1Alt. Cndn Base Value: 213Accruals: 0R1Choose Save. | Accruals condition type has been added to pricing procedure. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Go to Pricing Procedures Overview | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Set Pricing Procedures.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Pricing Procedures: Change screen displays. |  |
| 3 | Go to Control Data | Select the relevant pricing procedure and choose Procedures – Control Data in Dialog Structure. | The control data for the pricing procedure with the Reference Step Overview table is displayed in the working area. |  |
| 4 | Add Accruals Condition Type | Choose New Entries and make the following entries:Step Number: <number higher than maximum hitherto>Condition Type: RRA1Alt. Cndn Base Value: 213Accruals: 0R1Choose Save. | Accruals condition type has been added to pricing procedure. |  |

Routine 213 for the alternative calculation of condition base value has the following function: When you enter a condition contract, you can set the amount fields group on the Settlement Data tab page. This parameter controls for which amount field from the business volume data the system transfers data to the pricing procedure of the settlement document. As default, the net amount is used, but you can also specify a subtotal of the pricing procedure. As mentioned, during pricing the system determines the relevant condition contracts for the accruals condition types, and formula 213 reads the corresponding amounts field group and sets the condition base value accordingly. Therefore, there is no need to specify the From Step in the line with accruals condition type.

#### Prepare Transactional Data (Optional)

Purpose

The business volume for royalties settlement is determined from billing documents for most cases. To prepare transactional test data, you can follow the Sell from Stock (BD9) scope item, which describes the sales process from a standard sales order to a billing document.

For royalties settlement based on paid billing documents, the business volume is determined from paid billing documents, which means the related accounting documents need to be cleared. To prepare transactional test data, you can follow steps described in the scope items Sell from Stock (BD9) and Accounts Receivable (J59).

For the special case of Intercompany Royalties based on Revenue Recognized Amounts, the business volume is determined from accounting documents created by the revenue recognition process. You can carry out the revenue recognition as described in scope items Event-Based Revenue Recognition – Sell from Stock (1K2) or Event-Based Revenue Recognition – Service Documents (3M3) or Event-Based Revenue Recognition – Subscription Billing (5DQ), depending on the scenario that you want to test, to create some transactional data.

Preparing transactional data is a required step. You can perform this step before or after creating the condition contract, or after each settlement run.

When you want to use the royalties recipient as business volume selection criterion, you enter the royalties recipient business partner ID for partner function RR Royalties Recipient on the Partner tab for sales order items. When you enter the royalties recipient business partner ID on header level, the system copies it down to new sales order items.

Procedure

Complete all the activities described in Sell from Stock (BD9) scope item's test script using the master data from this document.

|  |
| --- |
| Note If you want to use the optional link between Sell from Stock (BD9) scope item and Condition Contract Settlement, this reference only works if you use consistent master data (such as business partner and material for the sales order and the royalty condition contract). |

#### Activate Condition Contract Types (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you activate the condition contract types for intercompany royalties settlement and subscription billing.

|  |
| --- |
| Note Representing a new business scenario, the condition contract types for intercompany royalties settlement are blocked in the delivered business content in accordance with the guideline that UI changes should be avoided after a release upgrade. Without block these condition contract types would appear on the pop-up window for condition contract selection when you create a new condition contract. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5a | Go to Configuration Details and Remove Block | Choose Configure on the right to Configure Condition Contract Types for Customer Condition Contract.In column Block, choose Not Blocked – Can be Used for the condition contract types you use in the test procedures:0RI1 Royalties Intercompany Subscription Bill0RI2 Royalties Intercompany Billing Document0RI3 Royalties Intercompany Revenue Recognit.Choose Save. | The condition contract types are no longer blocked. |  |
| 5b | Go to Configuration Details and Remove Block | Choose Configure on the right to Configure Condition Contract Types for Supplier Condition Contract.In column Block, choose Not Blocked – Can be Used for the condition contract types you use in the test procedures:0RS3 Royalties, Subscription Billing0RS4 Royalties, Subscription Billing, 2StepChoose Save. | The condition contract types are no longer blocked. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Condition Contract Types for Customer Condition Contract.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3a | Go to Configuration Details and Remove Block | Choose Configure on the right to Configure Condition Contract Types for Customer Condition Contract.In column Block, choose Not Blocked – Can be Used for the condition contract types you use in the test procedures:0RI1 Royalties Intercompany Subscription Bill0RI2 Royalties Intercompany Billing Document0RI3 Royalties Intercompany Revenue Recognit.Choose Save. | The condition contract types are no longer blocked. |  |
| 3b | Go to Configuration Details and Remove Block | Choose Configure on the right to Configure Condition Contract Types for Supplier Condition Contract.In column Block, choose Not Blocked – Can be Used for the condition contract types you use in the test procedures:0RS3 Royalties, Subscription Billing0RS4 Royalties, Subscription Billing, 2StepChoose Save. | The condition contract types are no longer blocked. |  |

#### Define Condition Contract Process Variants (Optional)

This chapter describes the definition of condition contract process variants to also test variations of the core process. A process variant is used to define limited variations for condition contract maintenance and settlement that are configured for a condition contract type without changing the overall character of the process defined by a condition contract type. In this chapter, we describe process variants for different purposes. Note that you can also combine settings from these process variants.

For the use of condition contract process variant, you must also enhance the account determination settings. The process variant is a key field in the relevant condition table. We describe how you maintain account determination settings for the first process variant for approval workflow. Proceed in the same way for all other process variants that you want to test.

When you create a new condition contract and you want to apply the process variations of a condition contract process variant, enter the condition contract process variant on the Basic Data tab page.

##### Define Process Variant for Using the Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate the workflow for royalties processing.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Royalties Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Process Variants Overview | Choose Configure on the right of Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZR01 Royalties with WorkflowSettlement Management Status Group: RoyaltiesDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created. |  |
| 7 | Assign Condition Contract Types to the Process Variant | Double click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save.Note If you want to make use of the workflow feature, enter this condition contract process variant when you create a new royalty condition contract. | The relevant condition contract type is assigned to newly created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZR01 Royalties with WorkflowSettlement Management Status Group: RoyaltiesDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created. |  |
| 4 | Assign Condition Contract Types to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save.Note If you want to make use of the workflow feature, enter this condition contract process variant when you create a new royalty condition contract. | The relevant condition contract type is assigned to newly created process variant. |  |

##### Define Process Variant for Tax Free Royalties

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant which controls that royalties are treated tax-free.

Some countries, like the USA, do not offer tax services. When royalties are regarded as a service, taxation will be set to zero for the royalties amount. Tax-free royalties are achieved with this process variant in which you set the tax indicator for materials to zero. This tax indicator setting is transferred to pricing of a settlement run by a configured transfer rule.

If you want to treat royalties tax-free, make sure that you assign the condition contract process variant when you create a new condition contract.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Royalties Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR02 Tax Free RoyaltiesChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save. | The condition contract type is assigned to newly created process variant. |  |
| 8 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 3310Tax Indicator for Material: 0Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variants | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR02 Tax Free RoyaltiesChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save. | The condition contract type is assigned to newly created process variant. |  |
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

Split criteria for condition contract settlement – defined in Customizing in the profiles for business volume determination – are used to point up the contribution of different business objects to the overall royalties amount. In the profile for business volume determination relevant for royalties settlement, some split criteria, such as material or profit center, are defined as always active. The usage of these split criteria cannot be influenced with a condition contract process variant. But there are other split criteria which are defined as inactive until activated by a process variant. Note that for the test of an additionally activated split criterion you also have to prepare the business volume data accordingly with different values for the split criterion.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Royalties Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR03 Royalties Split Criteria Adaptation | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save. | The condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate/Deactivate Split Criteria for Settlement | Double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: Royalties SettlementField Name: select from field help list, for example AUFNRUsage as Split Criterion: select from the dropdown list as used or not usedNote In case of Subscriptions, if you want the Provider Contract information to appear in the Journal Entries resulting from the settlement process, then please maintain the following entries:PROVIDERCONTRACTPROVIDERCONTRACTITEMSETTLMTADDLREFDOCCATThis is valid for Condition Contract Types that are relevant for Subscription Billing - 0RI1, 0RI3, 0RS3 and 0RS4.Choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variants | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Condition Contract Process Variants and create the following settings. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR03 Royalties Split Criteria Adaptation | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save. | The condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate/Deactivate Split Criteria for Settlement | Select the Process Variant created before, and then double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: Royalties SettlementField Name: select from field help list, for example AUFNRUsage as Split Criterion: select from the dropdown list as used or not usedNote In case of Subscriptions, if you want the Provider Contract information to appear in the Journal Entries resulting from the settlement process, then please maintain the following entries:PROVIDERCONTRACTPROVIDERCONTRACTITEMSETTLMTADDLREFDOCCATThis is valid for Condition Contract Types that are relevant for Subscription Billing - 0RI1, 0RI3, 0RS3 and 0RS4.Choose Save. | The split criteria usage is changed with the process variant. |  |

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

To allow high flexibility in the business volume selection, the set of field combinations for royalties settlement provides many business volume selection criteria. However, this larger number can complicate the maintenance of business volume selection criteria in the condition contract, as users need to find the desired field combination in a long list when they want to enter a new line. With a suitable condition contract process variant, you can reduce the scope of business volume selection criteria to the relevant ones.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Define Contract Process Variants | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR04 Royalties Selection Criteria Adaptation | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save. | The condition contract type is assigned to newly-created process variant. |  |
| 8 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Royalties SettlementField Combination: select from field help list, for example, 0035Note You can choose 0069 for Customer Hierarchy.Usage of Field Combination: select from the drop down list as used or not usedChoose Save. | The usage of field combination is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Condition Contract Process Variants | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Condition Contract Process Variants and create the following settings. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR04 Royalties Selection Criteria Adaptation | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save. | The usage of field combination is changed with the process variant. |  |
| 5 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Royalties SettlementField Combination: select from field help list, for example, 0035Note You can choose 0069 for Customer Hierarchy.Usage of Field Combination: select from the dropdown list as used or not used.Choose Save. | The usage of field combination is changed with the process variant. |  |

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
| 4 | Open Configuration Item for Royalties Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR07 Contract Determination Single Sales DealChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Relevant for Contract Determination: All CustomersChoose Save. | The condition contract type is assigned to newly created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variants | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR07 Contract Determination Single Sales DealChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Relevant for Contract Determination: All CustomersChoose Save. | The condition contract type is assigned to newly created process variant. |  |

##### Define Process Variant for Handling Royalties in Service Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant for handling royalties related to a service contract.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Royalties Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZR05 Royalties for Service ContractsNo Accruals Reversal at Partial Settlement: <selected>Recognition Adjustment Active: <selected>Choose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save. | The condition contract type is assigned to newly-created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variants | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Condition Contract Process Variants and create the following settings. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZR05 Royalties for Service ContractsNo Accruals Reversal at Partial Settlement: <selected>Recognition Adjustment Active: <selected>Choose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Choose Save. | The condition contract type is assigned to newly-created process variant. |  |

##### Define Process Variant for Intercompany Royalties Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant for intercompany royalties settlement.

In the invoicing company code, the plant that you specify in the company code specific settings is used to determine the profit center from plant-material master data for commercial products used in subscription business. As a prerequisite, the plant and profit center information for the invoicing company code should be present in the master data of the commercial product.

In the billed company code, the profit center is determined from business volume data.

In the following procedure, we describe the settings when company code 1010 is the invoicing party and company code 1710 the bill-to party.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Royalties Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR06 Intercompany Royalties SettlementChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RI1, 0RI2, or 0RI3Note To assign condition contract types to the process variant, first follow the steps in Activate Condition Contract Types (Optional) to activate 0RI1, 0RI2, or 0RI3.Choose Save. | The condition contract type is assigned to newly created process variant. |  |
| 8 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 1010Tax Indicator for Material: 0Plant for CO Data: 1010Choose Save. |  |  |
| 9 | Define Business Volume Selection Criteria (if needed, for Intercompany Royalties for Revenue Recognized Amounts) | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Royalties Intercompany Revenue RecognitionField Combination: 0065 G/L AccountThis criterion can then be used in the Condition Contract, in addition to Product Sold, if you want to have additional refinement in business volume selection. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variants | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZR06 Intercompany Royalties SettlementChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RI1, 0RI2, or 0RI3Note To assign condition contract types to the process variant, first follow the steps in Activate Condition Contract Types (Optional) to activate 0RI1, 0RI2, or 0RI3.Choose Save. | The condition contract type is assigned to newly created process variant. |  |
| 5 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 1010Tax Indicator for Material: 0Plant for CO Data: 1010Choose Save. |  |  |
| 6 | Define Business Volume Selection Criteria (if needed, for Intercompany Royalties for Revenue Recognized Amounts) | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Royalties Intercompany Revenue RecognitionField Combination: 0065 G/L AccountThis criterion can then be used in the Condition Contract, in addition to Product Sold, if you want to have additional refinement in business volume selection. |  |  |

##### Define Process Variant for Royalties on Paid Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate the usage of business volume table groups for the business volume determination. This enables that the royalties amount calculation only considers paid invoices.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR08 Royalties on Paid InvoicesChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Note Add further condition contract types if you want to test the process variant for other royalties scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate Usage of Business Volume Table Group | Double-click on Business Volume Table Group on the left of the screen.Choose New Entries and make the following entries:Profile: 0RS1BVTab Grp.: 0R01Usage: select from the dropdown list, Use in Condition Contract SettlementClick Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZR08 Royalties on Paid InvoicesChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate Usage of Business Volume Table Group | Double-click on Business Volume Table Group on the left of the screen.Choose New Entries and make the following entries:Profile: 0RS1BVTab Grp.: 0R01Usage: select from the dropdown list, Use in Condition Contract SettlementClick Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

##### Define Process Variant to Activate Business Volume Selection by Service Rendered Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a condition contract process variant that enables you to use of service rendered date instead of billing date for the selection of billing documents to determine the business volume.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Define Contract Process Variants | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR09 BusVol Selection by Service Rendered Date | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Business Volume Selection Date Type: 0001 Service Rendered DateChoose Save. | The condition contract type is assigned to newly-created process variant. |  |
| 8 | Enter Condition Types / Tables | This step is to ensure that only that accrual condition type which works with Service Rendered Date is selectable when creating your condition contract with this process variant.Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries to set the condition type RRA1 to inactive:Application: V Sales/DistributionCond.Type Group: 0R01Condition Type: RRA1Usage of Condition Level: 1 InactiveRepeat the current step. Make the following entries to activate condition type RRAA:Application: V Sales/DistributionCond.Type Group: 0R01Condition Type: RRAAUsage of Condition Level: 2 ActiveClick Enter and choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Condition Contract Process Variants | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Condition Contract Process Variants and create the following settings. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZR09 BusVol Selection by Service Rendered Date | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0RS1Business Volume Selection Date Type: 0001 Service Rendered DateChoose Save. | The usage of field combination is changed with the process variant. |  |
| 5 | Enter Condition Types / Tables | This step is to ensure that only that accrual condition type which works with Service Rendered Date is selectable when creating your condition contract with this process variant.Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries to set the condition type RRA1 to inactive:Application: V Sales/DistributionCond.Type Group: 0R01Condition Type: RRA1Usage of Condition Level: 1 InactiveRepeat the current step. Make the following entries to activate condition type RRAA:Application: V Sales/DistributionCond.Type Group: 0R01Condition Type: RRAAUsage of Condition Level: 2 ActiveClick Enter and choose Save. |  |  |

##### Maintain Automatic Account Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you specify G/L accounts for royalties processing.

If you assign a condition contract process variant to a new condition contract you have to enhance the account determination settings. The process variant is a key field in the relevant condition table.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

In the following steps, we show how to create the necessary entry for the first defined process variant ZR01 Royalties with Workflow.

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
| 8 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condition Type: KORR Royalties SettlementCompany Code: 3310Process Variant: ZR01Account Key: 0R1 Royalties SettlementG/L Account: 61500200Accruals Acc.: 21772000Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 9 | Review in the Information and Save | Choose Save. | The G/L account assignment is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Automatic Account Determination 1. Area screen displays. |  |
| 3 | Fill in Basic Information | Make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L AccountsChoose Step 2. | The Automatic Account Determination 2. Parameters screen displays. |  |
| 4 | Fill in Relevant Information | Make the following entries:Chart of Accounts: YCOAApplication: VCondition Table: 016Choose Step 3. | The Automatic Account Determination 3. Account Assignments screen displays. |  |
| 5 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condition Type: KORR Royalties SettlementCompany Code: 3310Process Variant: ZR01Account Key: 0R1 Royalties SettlementG/L Account: 61500200Accruals Acc.: 21772000Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 6 | Review in the Information and Save | Choose Save. | The G/L account assignment is saved. |  |

#### Configure Intercompany Royalties Settlement (Optional)

This chapter describes the preliminary steps to set up the intercompany royalties settlement. Before, perform necessary preliminary steps as described in the Subscription Management with Sales Billing (57Z) scope item’s test script to enable proration for the royalties amount calculation in case that billing documents from subscription business transactions are used as business volume documents and you would like to calculate intercompany royalties per license.

As first step, activate the condition contract types for intercompany royalties settlement as described in the chapter [Activate Condition Contract Types for Intercompany Royalties Settlement](#unique_22) [page ] 42.

Second, create business partners that represent involved company codes. Maintain the supplier master data for the business partner representing the invoicing company code and the customer master data for the business partner representing the invoice-receiving company code. Then assign these business partners to company codes as described in the chapter [Specify Business Partner for Company Codes](#unique_23) [page ] 42.

Third, make sure that you have maintained a condition record for the output tax condition type TTX1 as described in the chapter [Maintain Settings for Export Tax](#unique_24) [page ] 44.

Fourth, specify the tax code mapping between the tax code used in the customer invoice and the tax code in the corresponding supplier invoice as described in the chapter [Specify Tax Code Mapping](#unique_25) [page ] 46.

Fifth, create a condition contract process variant as described in the chapter [Define Process Variant for Intercompany Royalties Settlement](#unique_17) [page ] 29.

Additionally, specify the G/L accounts for the new condition contract process variant created before as described in the chapter [Maintain Automatic Account Determination](#unique_20) [page ] 38. Optionally, create new appropriate G/L accounts for posting the revenue in the invoicing company code and the costs in the invoice-receiving company code as described in the Accounting and Financial Close (J58) scope item's test script. You can use G/L accounts 41001500 Revenue Affiliate – Product and 66999910 ICO Lease Expense – Real Estate as copy template.

You must enhance the account determination settings when assigning a condition contract process variant to a new condition contract by following the steps in the chapter [Maintain Automatic Account Determination](#unique_20) [page ] 38.

For example, assign the relevant G/L account as shown in the table below:

| Application | Condition type | Chart of Accts | Company Code | Process Variant | Account Key | G/L Account |
| --- | --- | --- | --- | --- | --- | --- |
| V | KORR | YCOA | 1010 | ZR06 | 0R2 | 41001500 |
| V | KORR | YCOA | 1010 | ZR06 | 0R3 | 66999910 |
| V | KORR | YCOA | 1710 | ZR06 | 0R2 | 41001500 |
| V | KORR | YCOA | 1710 | ZR06 | 0R3 | 66999910 |

Make the adjustment based on your system's custom settings.

##### Activate Condition Contract Types for Intercompany Royalties Settlement

Please refer to chapter Activate Condition Contract Types (Optional) to activate the condition contract types 0RI1 Royalties Intercompany Subscription Bill and/or 0RI2 Royalties Intercompany Billing Document.

##### Specify Business Partner for Company Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you assign business partners to company codes. For the company code that creates the customer invoice, you also specify the sales area used for the invoice. In the business partner master for the company code that receives the invoice, you must maintain the Sales and Distribution data for this sales area.

First, maintain the business partners that represent the involved company codes by following the master data scripts BND – Create Customer Master - MDS and BNE – Create Supplier Master - MDS. Maintain supplier master data for the business partner representing the invoicing company code, and customer master data for the business partner representing the invoice-receiving company code.

In the following procedure, we describe the settings when company code 1010 is the invoicing party and company code 1710 the bill-to party.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Royalties Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Organizational Settings for Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Settlement Settings for Intercompany Processes configuration step. | The Settlement Settings for Intercompany Processes: Change screen displays. |  |
| 6 | Create Entry for Invoicing Party | Choose New Entries and make the following entries for the invoicing company code:Company Code: 1010Supplier: Business partner representing company code 1010Sales Organization: 1010Distribution Channel: 10Division: 00Click Enter. | The invoicing party is created. |  |
| 7 | Create Entry for Bill-To Party | Choose New Entries and make the following entries for the invoice receiving company code:Company Code: 1710Customer: Business partner representing company code 1710Click Enter and choose Save. | The bill-to party is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Settlement Settings for Intercompany Processes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Go to Configuration Details | Choose Configure on the right to Settlement Settings for Intercompany Processes configuration step. | The Settlement Settings for Intercompany Processes: Change screen displays. |  |
| 4 | Create Entry for Invoicing Party | Choose New Entries and make the following entries for the invoicing company code:Company Code: 1010Supplier: Business partner representing company code 1010Sales Organization: 1010Distribution Channel: 10Division: 00Click Enter. | The invoicing party is created. |  |
| 5 | Create Entry for Bill-To Party | Choose New Entries and make the following entries for the invoice receiving company code:Company Code: 1710Customer: Business partner representing company code 1710Click Enter and choose Save. | The bill-to party is created. |  |

##### Maintain Settings for Export Tax

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check and, if required, maintain export tax condition records for involved company codes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Tax Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Tax Rates - Sales (F6972). | The Manage Tax Rates - Sales screen displays. |  |
| 3 | Check Condition Record | On the Manage Tax Rates - Sales screen, make the following entries and choose Go.Editing Status: AllFilter Method: Filter with Specified CriteriaCondition Type: TTX1Key Combination: 011Valid On: TodayDeparture Ctry/Reg.: DE | Selected condition records are displayed in the Condition Records table. |  |
| 4 | Check Condition Records | In the Condition Records table, check the existence for the following key fields:Condition Type: TTX1Condition Table: 011Departure Ctry/Reg.: DEDest. Country/Region: USTax Class.1 Customer: <tax classification of customer representing billed company code>Tax Class. Material: 4 Not taxab. noVATret.Note Usually, the tax classification of the customer is 1 Liable for Tax. |  |  |
| 5 | Create Condition Record (If Required) | Choose Create and create a condition record for the mentioned key fields. Enter the corresponding tax rate and the tax code.Choose Save. | The required condition record for export taxes is created. |  |

##### Specify Tax Code Mapping

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you specify the tax code mapping between tax codes used in the customer invoice and tax codes used in the supplier invoice. Tax code mapping is also required when the intercompany settlement is not liable for tax. In the following procedure description, we describe the mapping of tax codes for zero tax between Germany and US.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Royalties Settlement | Enter the following filters:Application Area: SalesSub Application Area: Royalties Settlement for SalesIn the items table, select the item with item name: Organizational Settings for Royalties Settlement. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Tax Code Mapping configuration step. | The Define Tax Code Mapping: Display screen displays. |  |
| 6 | Open Tax Code Mapping | Select use case 01 Intercompany Inbound and double-click Tax Code Mapping on the left of the screen. | The Define Tax Code Mapping: Change screen displays. |  |
| 7 | Create Entry for Zero Tax | Choose New Entries and make the following entries:Source Company Code: 1010Target Company Code: 1710Tax Code: A3Target Tax Code: I0Click Enter and choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Organizational Settings for Royalties Settlement.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Royalties Settlement screen displays. |  |
| 3 | Go to Configuration Details | Choose Configure on the right to Define Tax Code Mapping configuration step. | The Define Tax Code Mapping: Display screen displays. |  |
| 4 | Open Tax Code Mapping | Select use case 01 Intercompany Inbound and double-click Tax Code Mapping on the left of the screen. | The Define Tax Code Mapping: Change screen displays. |  |
| 5 | Create Entry for Zero Tax | Choose New Entries and make the following entries:Source Company Code: 1010Target Company Code: 1710Tax Code: A3Target Tax Code: I0Click Enter and choose Save. |  |  |

#### Configure Approval Workflow (Optional)

If you want to test the approval workflow as one of the possible process variations, you have to maintain additional workflow settings and define teams and responsibilities. In contrast to sales rebates and sales commission processing, SAP currently does not provide a dedicated business role for a manager who monitors the royalties processing. Such a role within the Financial Operations area is planned when further scope items for Settlement Management will be provided. Because of that, SAP abstained from an assignment of workflow relevant business catalogs to business roles for royalties processing in the business content. Accordingly, this is the first step you have to do when maintaining workflow settings as described in chapter Create Business Roles for Workflow Processing.

To establish the workflow, the Sales Manager is created in this test script as business role for approval steps. In principle, you can choose and create another business role. Note that the assignment of business catalogs SAP_SD_BC_CC_WIAPPROVE_PC (Sales – Condition Contract Approval) and SAP_SD_BC_SDOC_WIAPRV_PC (Sales – Condition Contract Settlement Document Approval) is already maintained when either the Sales Rebate Processing or Sales Commissions - External Sales Representative scope item is active. Here, the assignment is part of the business content. Anyway, you need to create a new business role with business catalog SAP_SD_BC_CC_WIREWORK_PC (Sales – Condition Contract Rework) and assign user SAP_BR_CONTR_MGR_ROYALTIES ( Contract Manager – Royalties) to it.

##### Create Business Roles for Workflow Processing

Purpose

In this activity, you create new business roles with workflow relevant business catalogs to enable the workflow processing for Contract Manager – Royalties and Sales Manager.

We describe how you create a new business role with business catalog SAP_SD_BC_CC_WIREWORK_PC (Sales – Condition Contract Rework) to which you assign user SAP_BR_CONTR_MGR_ROYALTIES (Contract Manager – Royalties).

In the same way, you create a new business role with business catalogs SAP_SD_BC_CC_WIAPPROVE_PC (Sales – Condition Contract Approval) and SAP_SD_BC_SDOC_WIAPRV_PC (Sales – Condition Contract Settlement Document Approval) to which you assign user SAP_BR_SALES_MANAGER (Sales Manager).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Business Roles (F1492). | The Maintain Business Roles screen displays. |  |
| 3 | Create Business Role | Choose New at the bottom of the screen.In the New Business Role pop-up window, make the following entries:Business Role ID: for example, BR_CONTR_MGR_ROYALTIES_WFBusiness Role Description: for example, Contract Manager Royalties – WorkflowChoose Create. | The Contract Manager - Royalties screen displays. |  |
| 4 | Assign Business Catalogs | On the Assigned Business Catalogs tab, choose Add.In the Add Business Catalogs pop-up window, enter SAP_SD_BC_CC_WIREWORK_PC in the search box and choose Search. Select the Sales - Condition Contract Rework line and choose OK.In the Dependencies section, select the Business Catalog line and choose OK. | The business catalogs are assigned to the business role Contract Manager - Royalties. |  |
| 5 | Assign Business User | On the Assigned Business Users tab, choose Add.In the Add Business Users pop-up window, enter CONTR_MGR_ROYALTIES in the search box and choose Search. Select the CONTR_MGR_ROTALTIES line and choose OK. | The business user Contract Manager - Royalties is assigned. |  |
| 6 | Change Access Categories and Save | Go back to the General Role Details tab.In the Access Categories section, for Write, Read, Value Help field, select Unrestricted from the dropdown list.Choose Save at the bottom. | The access categories are changed and the new business role is created. |  |

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain the teams and responsibilities for royalties settlement workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create a New Team | Choose Create. | The Team screen displays. |  |
| 4 | Enter General Information | Make the following entries and choose Enter:Name: for example, <CCM_TEST_TEAM_SD_(Country Code)>Description: for example, <Condition Contract Management Team Sales (Country Name)>Status: EnabledType: SCMTV Sales Condition Contract Team TypeCondition Contract Category: 0R | The team is created. |  |
| 5 | Add Team Members | In Team Members, choose Create.From Items section, select a business partner checkbox and choose OK.Business Partner: <Sales_Manager> | The Team screen displays. |  |
| 6 | Add Function to Team Members | In the Functions field, choose Select. In the Select: Functions window, choose the following functions, and choose OK.SCCM_F1: Condition Contract Release ApprovalSCCM_F2: Condition Contract Settlement Release ApprovalChoose Save to save the team. | Team is saved. |  |
| 7 | Create a New Team | Go back and choose Create. | The Team screen displays. |  |
| 8 | Enter General Information | Make the following entries and choose Enter:Name: for example, <STLMT_TEST_TEAM_SD_(Country Code)>Description: for example, <Settlement Management Team Sales (Country Name)>Status: EnabledType: SMT Settlement ManagementChoose Enter.SettlmtDocType: 0R11 | The team is created. |  |
| 9 | Add Team Members | In Team Members, choose Create.From Items section, select a business partner checkbox and choose OK.Business Partner: <Sales_Manager> | The Team screen displays. |  |
| 10 | Add Function to Team Members | In the Functions field, choose Select. In the Select: Functions window, choose the following functions, and choose OK.STLMTAPR: <Settlement Document Approver>Choose Create. | Team is saved. |  |
| 11 | Check Team Status | Navigate to the Manage Teams and Responsibilities worklist, and verify the status of the team by selecting Go.The status should be Enabled. | Team status is enabled. |  |

##### Manage Workflow for Condition Contracts - Release Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for the release of condition contracts.

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

In this activity, you maintain workflow settings to release the settlement for condition contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflows screen displays. |  |
| 3 | Select Relevant Workflow | Select Settlement Release of Condition Contract in the top left dropdown list.Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for Settlement Release of Cond. Contract - Single StepChoose Create under the Steps. | The New Step screen displays. |  |
| 5 | Input Workflow Details | Make the following entries:Step Type: Release of Condition Contract for SettlementRole: Condition Contract Settlement Release ApprovalRequired Action for Rework Condition Contract: Rework of Condition Contract for Settlement ReleaseAction Result: Restart WorkflowChoose Create. | The New Workflow screen displays. |  |
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

In this activity, you maintain workflow settings for the release of settlement documents related to condition contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Settlement Documents (F3681). | The Manage Workflows screen displays. |  |
| 3 | Create New Workflow | Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for the Approval of Settlement Document (To Accounting)Under Steps, choose Create. | The New Step screen displays. |  |
| 5 | Input Details | Make the following entries:Step Type: Release of Settlement DocumentRole: Settlement Document ApproverChoose Create. | The New Workflow screen displays. |  |
| 6 | Create New Step | Under Steps, choose Create. | The New Step screen displays. |  |
| 7 | Input Details | Make the following entries:Step Type: Automatic Change of Settlement Document StatusChoose Create. | The New Workflow screen displays. |  |
| 8 | Save Workflow | Choose Save. | The Workflow Details screen displays. |  |
| 9 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction /App Name | Expected Results |
| --- | --- | --- | --- |
| Royalties Settlement Processing |  |  |  |
| [Create Condition Contract](#unique_33) [page ] 59 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Check Business Volume (Optional)](#unique_34) [page ] 63 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_35) [page ] 65 | Settlement Clerk - Royalties | Settle Condition Contracts (WB2R_SV_ROYL) |  |
| [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_36) [page ] 66 | Settlement Clerk - Royalties | Manage Settlement Documents (F3254) |  |
| [Partial Settlement (Optional)](#unique_37) [page ] 67 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Check Settlement Document for Partial Settlement (Optional)](#unique_38) [page ] 68 | Settlement Clerk - Royalties | Manage Settlement Documents (F3254) |  |
| [Final Settlement](#unique_39) [page ] 71 | Settlement Clerk - Royalties | Settle Condition Contracts (WB2R_SV_ROYL) |  |
| [Check Settlement Document for Final Settlement (Optional)](#unique_40) [page ] 72 | Settlement Clerk - Royalties | Manage Settlement Documents (F3254) |  |
| Two-Step Royalties Settlement Processing |  |  |  |
| [Create Condition Contract](#unique_41) [page ] 72 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Check Business Volume (Optional)](#unique_42) [page ] 76 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_43) [page ] 76 | Settlement Clerk - Royalties | Settle Condition Contracts (WB2R_SV_ROYL) |  |
| [Partial Settlement (Optional)](#unique_44) [page ] 76 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Collect Parked Settlement Documents for Transfer to Accounting (Optional)](#unique_45) [page ] 77 | Settlement Clerk - Royalties | Collect Settlement Documents (WZRC) |  |
| [Final Settlement](#unique_46) [page ] 78 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Collect Parked Settlement Documents from Final Settlement](#unique_47) [page ] 78 | Settlement Clerk - Royalties | Collect Settlement Documents (WZRC) |  |
| Royalties Settlement Processing with Approval Workflow |  |  |  |
| [Create Condition Contract](#unique_48) [page ] 78 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Request Approval to Release Condition Contract](#unique_49) [page ] 82 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Trigger Rework of Condition Contract (Optional)](#unique_50) [page ] 83 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Rework Condition Contract (Optional)](#unique_51) [page ] 84 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Release Condition Contract](#unique_52) [page ] 85 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Check Business Volume (Optional)](#unique_53) [page ] 86 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_43) [page ] 76 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Request Release of Condition Contract for Settlement](#unique_54) [page ] 86 | Settlement Clerk - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Release Condition Contract for Settlement](#unique_55) [page ] 87 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Partial Settlement (Optional)](#unique_56) [page ] 88 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Approve Release of Partial Settlement Document to Accounting (Optional)](#unique_57) [page ] 88 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Final Settlement](#unique_58) [page ] 89 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Approve Release of Final Settlement Document to Accounting](#unique_59) [page ] 89 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Royalties Settlement Processing with Graduated Scales](#unique_60) [page ] 90 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Royalties Settlement Processing Using Service Rendered Date for Business Volume Selection](#unique_61) [page ] 91 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Royalties Related to Service Contracts (Optional)](#unique_62) [page ] 92 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Intercompany Royalties Settlement Processing](#unique_63) [page ] 94 |  |  |  |
| [Create Condition Contract](#unique_64) [page ] 95 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Check Business Volume (Optional)](#unique_65) [page ] 98 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Final Settlement](#unique_66) [page ] 98 | Settlement Clerk - Royalties | Manage Scheduling Worklists - Settlement Management (F5856) |  |
| [Check Settlement Document for Final Settlement (Optional)](#unique_67) [page ] 99 | Settlement Clerk - Royalties | Manage Settlement Documents (F3254) |  |
| [Royalties Settlement with Licensor for Subscription Business](#unique_68) [page ] 102 |  |  |  |
| [Create Condition Contract](#unique_69) [page ] 102 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Delta Accruals Settlement (Optional)](#unique_70) [page ] 103 | Settlement Clerk - Royalties | Settle Condition Contracts (WB2R_SV_ROYL) |  |
| [Partial Settlement (Optional)](#unique_71) [page ] 103 | Settlement Clerk - Royalties | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Final Settlement](#unique_72) [page ] 103 | Settlement Clerk - Royalties | Settle Condition Contracts (WB2R_SV_ROYL) |  |
| [Final Settlement with Adjustments (Optional)](#unique_73) [page ] 103 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Royalties Unlikelihood (Optional)](#unique_74) [page ] 105 | Contract Manager - Royalties | Manage Condition Contracts - Royalties (F5414) |  |
| [Reverse Settlement Document (Optional)](#unique_75) [page ] 105 | Settlement Clerk - Royalties | Reverse Settlement Documents - Condition Contracts (WB2R_CANCEL_DOCS) |  |

## Test Procedures

This chapter comprises the test procedures for different royalties settlement scenarios covered by this scope item.

The first section Royalties Settlement Processing describes the basic royalties settlement scenario with the creation of the corresponding condition contract and the execution of the delta accruals, partial and final settlement. Settlement documents created in partial settlements and in the final settlement are immediately released to accounting.

The second section Two-Step Royalties Settlement Processing describes an alternative settlement procedure when you have several royalties agreements with the same licensor. In the partial settlements and in the final settlement for the different condition contracts, you first create so called parked settlement documents that are not transferred to accounting. In a second step, you collect the parked settlement documents to create a collective settlement document, which is then transferred in one journal entry to accounting. Thus, you reduce the workload for the accounting module and you have the information for the royalties settlement with a licensor in one journal entry.

The third section Royalties Settlement Processing with Approval Workflow describes how you can include approval steps in the royalties settlement processing. The description refers to the basic royalties settlement scenario, but it can be applied similar for the two-step settlement scenario. The approval workflow comprises three features: approval for the release of a condition contract, for the settlement of a condition contract, and for the settlement document for a transfer to accounting. You can choose whether you want to use one of these features, or two or all three.

Finally, we describe several special cases. First, you can use this scope item to process royalties for service contracts in combination with the allocation of expenses regarding the accounting periods of the service contract duration. The next scenario concerns the intercompany royalties settlement between a parent company as licensor and subsidiaries as licensees. The two-sided settlement document that you create in a settlement combines the customer invoice in the parent company code and the corresponding supplier invoice in the subsidiary company code. Business volume data can originate from usual sales transactions or from subscription business. The combination of the basic royalties process with business volume determination from subscription business is subject matter of the next chapter.

Furthermore, it is shown how you can maintain conditions for adjusting the (final) settlement amount in the condition contract, and finally how you maintain an unlikelihood condition in a condition contract for the case that a royalties eligibility will probably not be reached.

During the condition contract creation, you can also use a customer hierarchy node in combination with condition contract types for customers. Only hierarchies of type Customer Hierarchy – Sales can be used.

### Royalties Settlement Processing

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for a licensor as condition contract partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Contract Manager - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Royalties (F5414). | The Manage Condition Contracts - Royalties screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Royalties screen, choose Create.Select the following Condition Contract Type:0RS1 Royalties Settlement |  |  |
| 4 | Enter Condition Contract Details | On the Create Royalties Settlement screen, make the following entries and press Enter:Supplier: 33300096From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant (Optional) | On the Basic Data tab, enter one of the condition contract processes, which varies from the basic scenarios. Then choose Enter:Option A:Process Variant: ZR02 Tax Free RoyaltiesOption B:Process Variant: ZR03 Royalties Split Criteria AdaptationOption C:Process Variant: ZR04 Royalties Selection Criteria AdaptationOption D:Process Variant: ZR08 Royalties on Paid InvoicesNote When you enter process variant ZR08 to enable the process variation for royalties on paid invoices, you must also specify business volume table group 0R01 Royalties Only Paid Invoices on the Settlement Data tab.The application does not differentiate between partially and fully paid billing documents, and always takes the full amount in either case. |  |  |
| 6 | Enter Purchasing Data | On the Purchasing tab, make and check the following entries:Purch. Organization: 3310Purchasing Group: 001Company Code: 3310 |  |  |
| 7 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned then the text will not appear in the output form as in the German business partners the communication language German is maintained. |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the entries you need and choose Enter. For example,Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Select New Line.Make the entries you need and press Enter. For example,Field Combination: 0025 Royalties RecipientInclusion Indicator (Incl/Excl): InclusiveRoyalties Recipient: 33300096Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer.Note When you want to use the royalties recipient as business volume selection criterion, you have to enter the royalties recipient in sales order items for partner function RR. When you have already created such sales orders when processing scope item Sell from Stock (BD9), you enter here the royalties recipient you have used. |  |  |
| 9 | Check/Enter Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts PayableIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This is always the case for Fixed Amount condition contracts but can also happen when you do a settlement before you have created transactional documents. |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and press Enter.Settlement Date: for example, <validity end of condition contract>Settlement Date Type: Final SettlementSelect New Line.Make the following entries and press Enter.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and press Enter.Settlement Date: for example, <today's date>Settlement Date Type: Delta AccrualsNote The creation of the line with Settlement Date Type: Delta Accruals is optional. The creation of the line with Settlement Date Type: Partial Settlement is optional. |  |  |
| 11 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and press Enter.Condition Type: RRS1 RoyaltiesCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scale |  |  |
| 12 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and press Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and press Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 13 | Enter Condition Data | In the Conditions area, select New Condition.Make the following entries and press Enter.Condition Type: RRA1 Royalties AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Note This condition is used to calculate the amount for accruals. |  |  |
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

Use this step after you have prepared transactional data, that is billing documents related to a condition contract for a licensor.

If you are using the process variant for paid invoices in the condition contract, then you need to post incoming payments for the billing documents that you want to consider for your test. The steps are explained in the scope item Accounts Receivable (J59).

Note

You can repeat this process step at every point in time in the test procedure. It’s recommendable to check the business volume before you start a settlement run to enable a control of the business volume determined for a settlement document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Business Volume - Condition Contracts (WB2R_BUSVOL). | The Business Volume for Condition Contracts screen displays |  |
| 3 | Select Condition Contract | On the Business Volume for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract created in this test>Business Volume Base: From ContractOutput Level Business Volume: Settlement Date and Split Criteria |  |  |
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

Use this step if you have executed the prepare transactional data scenario for the condition contract for a licensor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Condition Contracts (WB2R_SV_ROYL). | The Settlement of Supplier Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Settlement of Supplier Condition Contracts screen, make the following entries and choose Execute:Settlement Date: for example, <today's date>Settlement Date Type: 3 Delta AccrualsCondition Contract: <number of condition contract created in this test>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No Filter | Settlement document for posting delta accruals is created. |  |
| 4 | Check Log | Check the log of the delta accruals settlement.Make a note of the settlement document created. |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Documents screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the delta accruals settlement and click the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transferred to Accounting. | The posting status is Accounting document has been created (C). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data, check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 7 | Check Pricing of Items | Click an item in the table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all the items. | The system has determined the relevant business volume and displays it for condition type RRBV Royalties Bus Volume.The system has calculated the accruals amount with the relevant conditions maintained in the condition contract. |  |
| 8 | Check Journal Entry | Go back to the Settlement Document screen.Under Document Flow, choose the main customer journal entries. Click the icon right to the box and select Display Journal Entries from the pop-up window. | You see the financial posting as below. |  |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 61500200 (Royalties for Sales) | <Accruals amount> | 0 |
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

Use this step if you have executed the Sell from Stock (BD9) scenario related to this royalty condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Condition Contracts (WB2R_SV_ROYL). | The Settlement of Supplier Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Settlement of Supplier Condition Contracts screen, make the following entries and choose Execute.Settlement Date: for example, <tomorrow's date>Settlement Date Type: 1 Partial SettlementCondition Contract: <number of condition contract created in this test>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No FilterTake a note of the number of the invoice created. | The Log for Supplier Condition Contract Settlement screen displays. A settlement document is created. Accruals are reversed. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Document screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the partial settlement and click the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transferred to Accounting. | The posting status is Accounting document has been created (C). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data, check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Partner Data | Under Partner Data, check the partner information. | You see the partner data maintained in the master data. |  |
| 7 | Check Document Items | Under Items, check the items of the settlement document. | The system has created the items according to the split criteria. |  |
| 8 | Check Pricing of Items | Click an item in the table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all the items. | The system has determined the relevant business volume and displays it for condition type RRBV Royalties Bus Volume. The system has calculated the royalties amount with condition type RRS1 maintained in the condition contract and the input tax with the percentage for full tax. The system shows the amount of reversed accruals for condition type RRA2 and the amount for excess accruals for condition type RRA5. |  |
| 9 | Check Output | Go back to the Settlement Document screen, under Output Items, check the output items.Find the item with Channel: Print and choose Open File under Display. | You see the output print form. |  |
| 10 | Check Journal Entries | Under Document Flow, choose the main customer journal entries. Click the icon right to the box and select Display Journal Entries from the pop-up window. | You see the financial posting as below.The accruals reversal amount is the difference between the amount of reversed accruals and the excess accruals as mentioned in step 8. |  |
| 11 | Check Texts | Go back to the Manage Settlement Documents screen.In the Settlement Documents table, click the settlement document number and select Display Settlement Document from the pop-up window.Choose Header Texts. Under Texts, check the text information. | For text type Contract Text for Output/Forms, you see the text maintained in the condition contract for text type Text for Settlement Document. |  |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 21100000 | 0 | <Royalties amount + Input tax> |
| 61500200 | <Royalties amount> | 0 |
| 12600000 | <Input tax> | 0 |
| 61500200 | 0 | <Accruals reversal amount> |
| 21772000 | <Accruals reversal amount> | 0 |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Condition Contracts (WB2R_SV_ROYL). | The Settlement of Supplier Condition Contracts screen displays. |  |
| 3 | Select Condition Contract Type | On the Settlement of Supplier Condition Contracts screen, make the following entries and choose Execute.Settlement Date: for example, <end of current year date>Settlement Date Type: Final SettlementCondition Contract: <number of condition contract created in this test>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No FilterTake a note of the number of the invoice created. | The Log for Supplier Condition Contract Settlement screen displays. A settlement document representing a supplier invoice is created. Accruals are reversed. |  |

#### Check Settlement Document for Final Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Please follow process steps of chapter Check Settlement Document for Partial Settlement (Optional) in section Royalties Settlement Processing.

Note the following difference: for the pricing elements of the settlement document items, check that all accruals are reversed. That means the amount for excess accruals for condition type RRA5 is zero.

### Two-Step Royalties Settlement Processing

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for a licensor as condition contract partner involving a settlement in two steps.

More than one condition contract is required for two-step condition contract processing. Please follow the steps below to create multiple condition contracts for further processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Contract Manager - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Royalties (F5414). | The Manage Condition Contracts - Royalties screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Royalties screen, choose Create.Select the following Condition Contract Type:0RS2 Royalties Settlement，2step |  |  |
| 4 | Enter Condition Contract Details | On the Create Royalties Settlement, 2step screen, make the following entries and press Enter:Supplier: 33300096From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Purchasing Data | On the Purchasing tab, make and check the following entries:Purch. Organization: 3310Purchasing group: 001Company Code: 3310 |  |  |
| 6 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned then the text will not appear in the output form as in the German business partners the communication language German is maintained. |  |
| 7 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line.Make the following entries and press Enter.Field Combination: 0025 Royalties RecipientInclusion Indicator (Incl/Excl): InclusiveRoyalties Recipient: 33300096Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer.Note When you want to use the royalties recipient as business volume selection criterion, you have to enter the royalties recipient in sales order items for partner function RR. When you have already created such sales orders when processing scope item Sell from Stock (BD9), you enter here the royalties recipient you have used. |  |  |
| 8 | Check/Enter Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts PayableIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This is always the case for Fixed Amount condition contracts but can also happen when you do a settlement before you have created transactional documents. |  |  |
| 9 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and press Enter.Settlement Date: for example, <validity end of condition contract>Settlement Date Type: Final SettlementSelect New Line.Make the following entries and press Enter.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and press Enter.Settlement Date: for example, <today's date>Settlement Date Type: Delta AccrualsNote The creation of the line with Settlement Date Type: Delta Accruals is optional. The creation of the line with Settlement Date Type: Partial Settlement is optional. |  |  |
| 10 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and press Enter.Condition Type: RRS1 RoyaltiesCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scale |  |  |
| 11 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and press Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and press Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 12 | Enter Condition Data | In the Conditions area, select New Condition.Make the following entries and press Enter.Condition Type: RRA1 Royalties AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Note This condition is used to calculate the amount for accruals. |  |  |
| 13 | Release Condition Contract | Choose Release. |  |  |
| 14 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

#### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps in chapter Check Business Volume (Optional) in section Royalties Settlement Processing.

#### Delta Accruals Settlement (Optional)

Please follow process steps of chapter Delta Accruals Settlement (Optional) in section Royalties Settlement Processing.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the delta accruals settlement you can optionally check the created settlement documents as described in chapter Check Settlement Document for Delta Accruals Settlement (Optional) in section Royalties Settlement Processing.

#### Partial Settlement (Optional)

Please follow process steps of chapter Partial Settlement (Optional) in section Royalties Settlement Processing.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the partial settlement you can optionally check the created parked settlement documents as described in chapter Check Settlement Document for Partial Settlement (Optional) in section Royalties Settlement Processing.

Note the following differences: The posting status is Blocked for Accounting. Accordingly, there is no journal entry related to a parked settlement document. In addition, there is also no output related to a parked settlement document.

#### Collect Parked Settlement Documents for Transfer to Accounting (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you collect parked settlement documents from partial settlement in order to create a collective settlement document for transfer to accounting.

Prerequisite

As prerequisite for this process step, you have created several condition contracts with condition contract type 0RS2 Royalties Settlement, 2 step and you have performed the partial settlement for these condition contracts as described in chapter [Partial Settlement (Optional)](#unique_37) [page ] 67.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access Collect Settlement Documents | Open Collect Settlement Documents (WZRC).On the Create Collective Documents from Settlement Documents screen, make the following entries and choose Execute.Document Number: <numbers of settlement documents for partial settlements created before>Check Run Only: <do not select> | The Create Collective Documents from Settlement Documents screen displays. |  |

|  |
| --- |
| Note After you have processed this step you can optionally check the created collective settlement document as described in chapter Check Settlement Document for Partial Settlement (Optional) in section Royalties Settlement Processing. |

#### Final Settlement

Please follow process steps of chapter Final Settlement in section Royalties Settlement Processing.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the final settlement you can optionally check the created parked settlement documents as described in chapter Check Settlement Document for Partial Settlement (Optional) in section Royalties Settlement Processing.

Note the following differences: The posting status is Blocked for Accounting. Accordingly, there is not journal entry related to a parked settlement document. In addition, there is also no output related to a parked settlement document.

#### Collect Parked Settlement Documents from Final Settlement

Purpose

In this process step, you collect parked settlement documents from final settlement in order to create a collective settlement document for transfer to accounting.

Prerequisite

As prerequisite for this process step, you have created several condition contracts with condition contract type 0RS2 Royalties Settlement, 2 step and you have performed the final settlement for these condition contracts as described in chapter [Final Settlement](#unique_39) [page ] 71.

Procedure

Process the steps described in the chapter [Collect Parked Settlement Documents for Transfer to Accounting (Optional)](#unique_45) [page ] 77.

|  |
| --- |
| Note After you have processed this step you can optionally check the created collective settlement document as described in chapter Check Settlement Document for Final Settlement (Optional) in section Royalties Settlement Processing. |

### Royalties Settlement Processing with Approval Workflow

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract with approval process activated for a licensor as condition contract partner.

Prerequisite

As prerequisite for this process step, you have completed the steps mentioned in preliminary steps for creating a process variant to activate the approval process, and successfully configured the approval workflow described in Configure Approval Workflow (Optional) section.

Procedure

In the following steps, we show how to create a condition contract for condition contract type 0RS1 Royalties Settlement with activated approval process.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Contract Manager - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Royalties (F5414). | The Manage Condition Contracts - Royalties screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Royalties screen, choose Create.Select the following Condition Contract Type:0RS1 Royalties Settlement |  |  |
| 4 | Enter Condition Contract Details | On the Create Royalties Settlement screen, make the following entries and press Enter:Supplier: 33300096From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant | On the Basic Data screen, make the following entry and press Enter:Process Variant: ZR01 Royalties with Workflow |  |  |
| 6 | Enter Purchasing Data | On the Purchasing tab, make and check the following entries:Purch. Organization: 3310Purchasing group: 001Company Code: 3310 |  |  |
| 7 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned then the text will not appear in the output form as in the German business partners the communication language German is maintained. |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line.Make the following entries and press Enter.Field Combination: 0025 Royalties RecipientInclusion Indicator (Incl/Excl): InclusiveRoyalties Recipient: 33300096Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer.Note When you want to use the royalties recipient as business volume selection criterion, you have to enter the royalties recipient in sales order items for partner function RR. When you have already created such sales orders when processing scope item Sell from Stock (BD9), you enter here the royalties recipient you have used. |  |  |
| 9 | Check/Enter Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Supplier: As Accounts PayableIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This is always the case for Fixed Amount condition contracts but can also happen when you do a settlement before you have created transactional documents. |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and press Enter.Settlement Date: for example, <validity end of condition contract>Settlement Date Type: Final SettlementSelect New Line.Make the following entries and press Enter.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and press Enter.Settlement Date: for example, <today's date>Settlement Date Type: Delta AccrualsNote The creation of the line with Settlement Date Type: Delta Accruals is optional. The creation of the line with Settlement Date Type: Partial Settlement is optional. |  |  |
| 11 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and press Enter.Condition Type: RRS1 RoyaltiesCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scale |  |  |
| 12 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and press Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and press Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 13 | Enter Condition Data | In the Conditions area, select New Condition.Make the following entries and press Enter.Condition Type: RRA1 Royalties AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Note This condition is used to calculate the amount for accruals. |  |  |
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

In this process step, you request an approval for the release of a royalty condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Royalties (F5414). | The Manage Condition Contracts - Royalties screen displays. |  |
| 3 | Request Release of Condition Contract | Find the condition contract for which you want to request an approval for release.Choose Change Condition Contract after clicking condition contract number.Choose Menu > Edit > Request Approval .Choose Save. | The status for the condition contract now should be:NewApproval RequestedThe condition contract with the request for release approval goes to Sales Manager's Inbox. |  |

#### Trigger Rework of Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the status of a royalty condition contract and trigger a rework of the condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Display the Relevant Condition Contract | Find the condition contract for which Contract Manager - Royalties has requested for release: Release Condition Contract XXXXXXXXXXX. | The details of the condition contract display on the right of the screen. |  |
| 4 | Check Condition Contract Data and Send Back for Rework | Check the Settlement Lock Status and Status of the condition contract.Now the settlement lock status is Not Locked and the status is New.As the Contract Manager - Royalties has not set the status to Locked for Settlement, click Rework.On the Submit Decision pop-up window, enter a decision note: for example, please set the condition contract to Locked for Settlement.Choose Submit. | The condition contract is sent back to Contract Manager - Royalties. |  |

#### Rework Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you rework on a royalty condition contract in order to set the Locked for Settlement status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Check the Condition Contract and Go to Change Mode | Open the notification: Rework Condition Contract XXXXXXXXXXX.Choose Show Details at the bottom and check the comments on the right side of the screen. Under the Comments tab, there is a message from the Sales Manager: please set the condition contract to Locked for Settlement.Choose Hide Details at the bottom and choose More Details on the upper right of the screen.On the Display Royalties Settlement screen, choose Menu > Condition Contract > Change. | You check the comment from the Sales Manager and go to the change mode for condition contract. |  |
| 4 | Set Condition Contract to Locked for Settlement Status | On the Change Royalties Settlement screen, choose Menu > Edit > Lock Settlement.Choose Save.Choose Continue in the pop-up window. | The settlement lock status is changed to Locked and the status for condition contract is New. |  |
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

In this process step, you release a royalty condition contract in an approval workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Release Condition Contract | Find the condition contract that Contract Manager - Royalties has just requested an approval for release: Release Condition Contract XXXXXXXXXXX.Choose Release at the bottom.Choose Submit in the pop-up window. | The condition contract for royalties settlement is released now. |  |

#### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps in chapter Check Business Volume (Optional) in section Royalties Settlement Processing.

#### Delta Accruals Settlement (Optional)

Please follow process steps of chapter Delta Accruals Settlement (Optional) in section Royalties Settlement Processing.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the delta accruals settlement you can optionally check the created settlement documents as described in chapter Check Settlement Document for Delta Accruals Settlement (Optional) in section Royalties Settlement Processing.

#### Request Release of Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request an approval for the settlement of a condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Royalties (F5414). | The Manage Condition Contracts - Royalties screen displays. |  |
| 3 | Request Release for Settlement | Find the condition contract for which you want to request the approval to release it for settlement. Choose Change Condition Contract via More Links when choosing condition contract number.Choose Menu > Edit > Request Settlement Approval .Choose Save.Choose Continue in the dialog box.Note Choose Menu > Edit > Lock Settlement before clicking Request Settlement Approval if you haven't executed steps in chapter Rework Condition Contract (Optional). | The status for condition contract now should be:ReleasedLocked for SettlementSettlement Approval RequestedThe condition contract with the request to approve the corresponding settlement appears in the inbox of the Sales Manager. |  |

#### Release Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a royalty condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Release Condition Contract for Settlement | Find the condition contract for which Settlement Clerk - Royalties has just requested the release for settlement.Position the notification: Release Condition Contract XXXXXXXXXX for Settlement in the inbox.Choose Release.Choose Submit in the dialog box. | The condition contract is released now for settlement. |  |

#### Partial Settlement (Optional)

Please follow process steps of chapter Partial Settlement (Optional) in section Royalties Settlement Processing.

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
| 3 | Approve Release to Accounting | Find the settlement document for which the release to accounting has to be approved. The approval request was triggered automatically after the settlement has been processed by the Settlement Clerk - Royalties.Position the notification: Approve Settlement XXXXXXXXXXX in the inbox.Choose Approve.Choose Submit in the dialog box. | The settlement document is released to accounting. |  |

|  |
| --- |
| Note You can check the settlement document by following process steps of chapter Check Settlement Document for Partial Settlement (Optional) in section Royalties Settlement Processing. |

#### Final Settlement

Please follow process steps of Final Settlement in section Royalties Settlement Processing.

On the selection screen, enter the different condition contracts belonging to this test.

#### Approve Release of Final Settlement Document to Accounting

Purpose

In this process step, you approve the release of the settlement document - created in final settlement - to Accounting.

Procedure

Process the steps described in the chapter [Approve Release of Partial Settlement Document to Accounting (Optional)](#unique_57) [page ] 88.

|  |
| --- |
| Note You can check the settlement document by following process steps of chapter Check Settlement Document for Final Settlement (Optional) in section Royalties Settlement Processing. |

### Royalties Settlement Processing with Graduated Scales

The default calculation of the scales that are set up in the condition table in condition contracts works like volume pricing. This means that on the execution of settlements, the application would apply the rate of the tier that it finds when looking for the business volume, on the entire amount and not only the delta amount:

If you set up the conditions as for example:

| Business Volume | Royalty Percentage |
| --- | --- |
| (From) 1,000 EUR | 10% |
| (From) 6,000 EUR | 20% |
| (From) 10,000 EUR | 30% |

Then the settlement run would calculate the royalties as follows:

| Business Volume found at the time of settlement | Total Effective Royalty at the time of settlement |
| --- | --- |
| 999 EUR | 0 EUR |
| 6,000 EUR | 1,200 EUR |
| 11,000 EUR | 3,300 EUR |

However, if you would like to set up graduated scales that work like tiered pricing instead of volume pricing, then you need to set up the condition contract slightly differently.

Follow the steps as in the chapter [Create Condition Contract](#unique_33) [page ] 59. In step 9, choose the value of the field Settlement Calculation Method as Graduated-To-Scale. Then in step 12, maintain the scales with scale type as To-scale.

Thereafter, if you set up the conditions as for example:

| Business Volume | Royalty Percentage |
| --- | --- |
| (To-scale) 1,000 EUR | 0% |
| (To-scale) 5,000 EUR | 10% |
| (To-scale) 11,000 EUR | 20% |
| (To-scale) 999,999 EUR | 30% |

Then the settlement run would calculate the royalties as follows:

| Business Volume found at the time of settlement | Total Effective Royalty at the time of settlement |
| --- | --- |
| 1,000 EUR | 0 EUR |
| 5,000 EUR | 400 EUR |
| 11,000 EUR | 1,600 EUR (= 400 EUR +1,200 EUR) |

In the example above, the calculation works in the following manner.

When business volume is found to be 1,000 EUR, then the first tier with 0% royalties is applicable. Hence, the royalty is 0 EUR.

When business volume is found to be 5,000 EUR, then the second condition rate with 10% royalties is applicable on the difference of business volumes between the first and second scales. Hence, the royalty is calculated as 400 EUR.

When business volume is found to be 11,000 EUR, then three condition rates would be applicable. This means that the royalty would be calculated at the rate of 0% for 1,000 EUR, 10% for 4,000 EUR and 20% for the remaining 6,000 EUR, resulting in 0, 400 and 1,200 EUR, respectively. Hence, the total royalty value comes to 1,600 EUR.

### Royalties Settlement Processing Using Service Rendered Date for Business Volume Selection

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

- 0RS1 – Royalties Settlement
- 0RS2 – Royalties Settlement, 2step

To enable this feature, follow the steps described in the chapter [Create Condition Contract](#unique_33) [page ] 59 with the following differences:

- In step 5, choose Process Variant ZR09 as explained in chapter [Define Process Variant to Activate Business Volume Selection by Service Rendered Date](#unique_19) [page ] 35.
- In step 13, select condition type RRAA.

|  |
| --- |
| Caution In case of returns, the service rendered date can differ based on the type of return. For further details about how the service rendered date is filled, consult your Sales and Distribution experts. |

|  |
| --- |
| Note If you have different rates for different periods, then you need to create the settlement calendar with Final Settlement dates for each period for those rates to be correctly applied. Using the service rendered date for business volume selection can cause subsequent billing documents posted after a contract's final settlement to be excluded from settlement. For example, if the original billing document is created in December, final settlement runs in January, and a subsequent billing document is posted in February with a service rendered date in December, the subsequent billing document may not be considered in the final settlement because the contract has already been settled. To capture such late billing documents, you can use delta settlements in subsequent settlement runs. |

### Royalties Related to Service Contracts (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section deals with royalties processing for service contracts in combination with a cost recognition of the royalties amount for the different fiscal periods within the service contract validity.

The condition contract for this test procedure has the same validity period as the service contract. The royalties amount is settled in the first month of the condition contract, and the cost recognition adjustment is achieved by additional delta accruals settlements scheduled for each fiscal period. The final settlement only reverses the accruals and locks the condition contract.

The cost recognition adjustment is controlled by a specific condition contract process variant that you assign to the new condition contract. In the business volume selection criteria, you specify the relevant service contract.

For more information about processing service contracts, see scope item 3MO -Service Contract Management.

Procedure

Enter a condition contract similar to the procedure described in chapter Royalties Settlement Processing with the following specifics.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Condition Contract Validity | On the Condition Contact screen, make the following entries:Valid From: for example, <validity start date of service contract>Valid To: for example, <validity end date of service contract>Note Usually you specify the validity period of the service contract also for the condition contract. However, the system does not provide a check for an identical validity. You have to ensure that organizationally. |  |  |
| 2 | Enter Process Variant and Business Volume Selection Criteria | In the Basic Data tab, choose New Entries:Process Variant: ZR05 Royalties for Service ContractsChoose Enter.In the Business Volume Selection Criteria tab, choose New Line. Select Field Combination 0047 and then choose Copy.In the new line created, make the following entries:Service Doc Type: for example, SC1Service Document: <service contract number created before>Service Document Item: <service contract item created before> |  |  |

In the settlement calendar, enter additional 12 settlement dates for delta accruals settlement for each month’s end within the condition contract validity. That means the first delta accruals settlement is at the end of the current month, the last coincides with the final settlement date at the end of the condition contract validity. Additionally, enter a partial settlement within the current month for instance for the current day.

Perform the partial settlement and then the delta accruals settlements and check the created settlement documents as described in section Royalties Settlement Processing. Be aware that the correct cost recognition adjustment for fiscal periods only happens when the delta accruals settlement runs at the specified settlement date. However, this procedure is required to illustrate the settlement postings. Let’s assume the following amounts. The service contract amount is 1200 AED. The royalties percentage is 10% so that the royalties amount is 120 AED.

First, check the settlement document for the partial settlement. In the pricing elements of the item, you see the royalties amount 120 AED for condition type RRS1 Royalties in the second line of the pricing procedure. In the line with condition type MWVS Input Tax, you see the calculated input tax. The following line shows the resulting gross amount. Relevant for the cost recognition adjustment in this document is the line for condition type RRA5 Royalties AccrSettl, which shows the royalties amount with a negative sign similar to an accruals reversal. Now check the accounting document. First, you see the usual posting for a partial settlement, the credit entry for the licensor for the gross amount and debit entries for the royalties amount (net value) on the Royalties for Sales P/L account, and the input tax on the corresponding tax account. In the following lines, you see the consequence of the negative value for condition type RRA5 from the pricing elements. You see a credit posting for the Royalties for Sales P/L account and a debit posting for the Sales Commis. Provi. accruals account. This is typical for a 'payment first, cost activation later' scenario. These lines balance the cost account – which is the Royalties for Sales P/L account in this case – and transfer the costs to a clearing account, i.e. the Sales Commis. Provi. accruals account. With the following delta accruals settlements, you reduce the proportionate amount on the clearing account and activate (transfer back) the costs on the P/L account.

Now, check the settlement documents for the delta accruals settlement to control this cost activation. First, you see that the settlement amount for each month is 10 AED. When you look at the pricing elements, you see how this net amount is derived from the royalties amount for condition type RRS1, a negative amount for condition type RRD5 Cost Recogn. Adjust controlling the cost recognition adjustment, the negative royalties amount for condition type RRS2 Royalties PartSetRev representing the partial settlement reversal, and the – now positive – amount for the condition type RRD2 Royalties Accr Total for posted accruals. The (absolute) amount for RRD5 and RRD2 is decreased by 10 AED month by month. In the accounting document for a delta accruals settlement document, you see the cost activation by a debit entry for the Royalties for Sales P/L account and a credit posting for the Sales Commis. Provi. accruals account. The final settlement has a settlement amount of zero, it only locks the condition contract.

### Intercompany Royalties Settlement Processing

Purpose

This section deals with the settlement of royalties between two company codes.

In many industries, subsidiary companies must transfer some of the revenue to the parent company under license agreements. The parent company is usually a leader in product development, often secured by patent rights, marketing and distribution have been decentralized through the subsidiaries in order to make better use of knowledge of local market specificities. Business volume relevant for settlement can result from the sale of physical goods. Often, however, the licensed products are rights of use of non-physical goods such as software applications or cloud services, which are usually sold through subscription business.

In the following test procedure, we describe the settlement of royalties related to the subscription business. Here, the commercial or sold products are the relevant business objects for profitability analysis and not the component materials (one-time, recurring, usage). Accordingly, the sold product is mapped to the material in settlement documents so that the material split criterion becomes effective for the sold product. In the business volume selection criteria, you can specify both the sold products as well as the component materials for instance to restrict the royalties to the recurring component only. In accordance with the usual settlement procedures, a monthly final settlement is set for the condition contracts. Since settlement is therefore carried out in accordance with the posting periods, the accruals posting function is not required and is therefore not active for the condition contracts. To perform a settlement, you must create a scheduling worklist.

Intercompany Royalties based on Revenue Recognized Amounts

This requirement usually arises for companies operating a subscription-based business or any kind of business which has to consider deferred revenue. It can be used in Sell from Stock scenario as well.

For example, if a company offers a subscription that spans 12 months and it is billed annually, the total billed amount would be divided into 12 parts and each part would be recognized as revenue each month. In scenarios where intercompany royalties need to be settled monthly, only the revenue recognized for each month would contribute to the business volume used for royalty calculation.

If you want to differentiate between different charges for subscription products (e.g., one-time and recurring charges) in business volume selection, you need to create separate products for those charges and use accordingly while creating the subscription.

Prerequisite

You have activated condition contract type 0RI1 Royalties Intercompany Subscription Bill, 0RI2 Royalties Intercompany Billing Document, or 0RI3 Royalties Intercompany Revenue Recognit. as described in chapter Activate Condition Contract Types (Optional).

|  |
| --- |
| Caution Exercise caution when using condition contract types 0RI1 and 0RI3. Type 0RI1 uses the billing documents as the basis for business volume, whereas type 0RI3 relies on only the revenue recognized amounts. If you mistakenly create two condition contracts with the same selection criteria—one using type 0RI1 and the other using type 0RI3, it will lead to double postings during settlement because the revenue recognized amount is just a portion of the billing amount that has been entered into the accounting books with a different categorization. |

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for a royalties agreement between company codes. Company code 1010 is licensor and invoicing party, company code 1710 is licensee and bill-to party. We assume that the business volume originates from subscription business with the sales of licenses. Accordingly, only the recurring component of commercial products is relevant. The royalty fee is based on the number of sold licenses. Proration is considered based on settings described in the Subscription Management with Sales Billing (57Z) test script.

If you want to consider only revenue recognized amounts, then you need to carry out revenue recognition steps as described in Event-Based Revenue Recognition – Subscription Billing (5DQ) test script. This will be possible only for Condition Contract Type 0RI3.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Contract Manager - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Royalties (F5414). | The Manage Condition Contracts - Royalties screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Royalties screen, choose Create.Select the following Condition Contract Type:0RI1 Royalties Intercompany Subscription BillIf you want to settle intercompany royalties for only those amounts that result from revenue recognition, select the following Condition Contract Type:0RI3 Royalties Intercompany Revenue Recognit. |  |  |
| 4 | Enter Condition Contract Details | On the Create Royalties Intercompany Subscription Bill screen, enter the validity period and press Enter:From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant | On the Basic Data tab, make the following entry and choose Enter:Process Variant: ZR06 Intercompany Royalties Agreement |  |  |
| 6 | Enter Responsibility Area | On the Responsibility Area tab, make and check the following entry:Company Code: 1010 |  |  |
| 7 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned then the text will not appear in the output form as in the German business partners the communication language German is maintained. |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0003 Sales OrgInclusion Indicator (Incl/Excl): InclusiveSales Organization: 1710Select New Line.Make the following entries and choose Enter.Field Combination: 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: SEATSSelect New Line.Make the following entries and choose Enter.Field Combination: 0068 Product SoldInclusion Indicator (Incl/Excl): InclusiveProduct Sold: <Commercial Product from Subscription Business>Note If you use 0RI3, then you need to use field combination 0071 Product Sold, instead of 0009 and 0068. The postings made by revenue recognition process don't have the information about the components of the Product Sold.Optionally, add further commercial products that you want to consider. |  |  |
| 9 | Check/Enter Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Customer: As Accounts ReceivableIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This is always the case for Fixed Amount condition contracts but can also happen when you do a settlement before you have created transactional documents.Note If you use Condition Contract Type 0RI3, then in the Settlement Data tab, Amount Fields Group will be set to “0RR1 Recognized Revenue in Company Code Currency”. |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, for the Final Settlement Calendar, select an appropriate value from the dropdown list and choose Generate Calendar. |  |  |
| 11 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and press Enter.Condition Type: RRS1 RoyaltiesCalculation Type: QuantityCondition Rate: for example, <10>Condition Currency: EURPricing Unit: 1Unit of Measure: <Base Unit of Measure used in the product master data>, for example, EAValid From: for example, <today's date>Valid To: for example, <validity end of condition contract> |  |  |
| 12 | Release Condition Contract | Choose Release. |  |  |
| 13 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

#### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps in chapter Check Business Volume (Optional) in section Royalties Settlement Processing.

#### Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a final settlement for the condition contract using the scheduling worklist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Scheduling Worklists - Settlement Management (F5856). | The Manage Scheduling Worklists screen displays. |  |
| 3 | Create Scheduling Worklist | On the Manage Scheduling Worklists screen, choose Create.On the following dialog screen, make the following entries and choose Continue:Scheduling Worklist Template: Settlement of Condition ContractsScheduling Worklist Run Category: Productive Run | The Scheduling Worklists screen displays with the ID of the new scheduling worklist. |  |
| 4 | Enter General Information | In the General Information section, enter the job execution date and time, the posting date, and the document date. | Scheduling and document dates are entered. |  |
| 5 | Enter Scheduling Worklist Items | In the Items section, choose Create and make the following entries:Condition Contract: <number of condition contract created in this test>Settlement Date: for example, <today's date>Settlement Date Type: Final SettlementThen choose Create. | The scheduling worklist is created. |  |
| 6 | Schedule the Job | On the Scheduling Worklist screen, choose Schedule. | The background job is scheduled. |  |
| 7 | Check Execution (Optional) | Choose Back.On the Manage Scheduling Worklist screen, enter the ID of the scheduling worklist in the Scheduling Worklist ID field and choose Go.Check that the Last Run Status is Execution Successful when the job execution date and time is reached. | The selected scheduling worklist appears in the Scheduling Worklists table. |  |

#### Check Settlement Document for Final Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the two-sided settlement document and accounting documents for final settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Document screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the final settlement and click the corresponding line. | Under General Information > Settlement Partner , you see data for the customer and supplier side. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transferred to Accounting. | The posting status is Accounting document has been created (C). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data , check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Partner Data | Under Partner Data, check the partner information. | You see the partner data maintained in the master data of the two involved business partners. |  |
| 7 | Check Document Items | Under Items, check the items of the settlement document. | The system has created the items according to the split criteria. The settlement quantity considers the proration factors of the subscription business documents. |  |
| 8 | Check Pricing of Items | Click an item in the table. On the following Settlement Document Item screen, under Pricing Elements, check the supplier and customer pricing elements of the settlement document item.Repeat this step for all the items. | For the leading customer pricing, the system has determined the relevant business volume and displays it for condition type RRBV Royalties Bus Volume. The system has calculated the royalties amount with condition type RRS1 maintained in the condition contract and the output tax according to the export tax settings. The net amount of the customer pricing is used for condition type RRNI in the supplier pricing. |  |
| 9 | Check Output | Go back to the Settlement Document screen, under Output Items, check the output items.Find the item with Channel: Printout and choose Open File under Display.Repeat this for channel Email. | You see the output print and email form. |  |
| 10 | Check Journal Entries | Under Document Flow, choose element Main Customer Journal Entry. Click the icon right to the box and select Display Journal Entries – New Version from the pop-up window.Repeat this procedure for flow element Main Journal Entry. | You see the financial posting for the customer and vendor invoice as below. |  |
| 11 | Display Intercompany Transaction | On the Journal Entry screen, under General Information, click on the Intercompany Transaction number. | The Manage Journal Entries screen displays with the journal entries for the customer and vendor invoice. |  |
| 12 | Check Texts | Go back to the Manage Settlement Documents screen.In the Settlement Documents table, click the settlement document number and select Display Settlement Document from the pop-up window.Choose Header Texts. Under Texts, check the text information. | For text type Contract Text for Output/Forms, you see the text maintained in the condition contract for text type Text for Settlement Document. |  |

Financial Posting

Financial Posting for Customer Invoice

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 12100000 (Receivables Domestic) | <Royalties amount> | 0 |
| 41001530 (Revenue Affiliated - Royalties) | 0 | <Royalties amount> |

Financial Posting for Vendor Invoice

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 21100000 (Payables Domestic) | 0 | <Royalties amount> |
| 66999930 (Royalties for Sales) | <Royalties amount> | 0 |

### Royalties Settlement with Licensor for Subscription Business

Purpose

This section deals with the royalties settlement scenario that is a combination of the basic royalties scenario and the determination of the business volume from subscription business. Related condition contract types are 0RS3 and 0RS4. Common with the basic royalties scenario is the entry of the licensor as business partner, the posting of accruals with transactional documents or with delta accruals settlements, and optional partial settlements. Settlement documents are also created in the same way. On the other hand, you enter business volume selection criteria characteristic for the subscription business as for instance the sold product. And again, we have the mapping of sold products to materials in the settlement documents. As a variant of this scenario, using condition contract type 0RS4, you can also apply the two-step settlement procedure as described in chapter Two-Step Royalties Settlement Processing.

The test procedure is very similar to the basic process variant so that we only describe the differences. Focal point is to check the mapping of sold products to materials in settlement documents.

Prerequisite

You have activated condition contract type 0RS3 Royalties, Subscription Billing and 0RS4 Royalties, Subscription Billing, 2Step as described in chapter Activate Condition Contract Types (Optional).

#### Create Condition Contract

Please refer to chapter [Create Condition Contract](#unique_33) [page ] 59 to create a royalties condition contract with business volume determination from subscription business. There are the following differences:

1. Condition Contract Type. Please select condition contract type 0RS3 or 0RS4.
2. Business Volume Selection Criteria. You can choose from selection criteria characteristic for billing documents origination from subscription business.

|  |
| --- |
| Note Field Combination 0025 Royalties Recipient is not supported as the Business Volume Selection Criterion for business volume based on subscription billing. |

You can check the business volume related to this condition contract at any time in the process as described in chapter [Check Business Volume (Optional)](#unique_34) [page ] 63.

#### Delta Accruals Settlement (Optional)

Please refer to steps in chapter [Delta Accruals Settlement (Optional)](#unique_35) [page ] 65 with the condition contract you created before.

After processing the delta accruals settlement, you can optionally check the settlement document as described in chapter [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_36) [page ] 66. Control that the system has mapped sold products to materials in the settlement document and applied other split criteria as for instance the profit center.

#### Partial Settlement (Optional)

Please refer to the steps of chapter [Partial Settlement (Optional)](#unique_37) [page ] 67 to do partial settlement for your condition contract. In this step, you also reverse the accruals posted before.

After processing the partial settlement, you can optionally check the settlement documents as described in chapter [Check Settlement Document for Partial Settlement (Optional)](#unique_38) [page ] 68. Again, control the mapping of sold products to materials in the settlement document.

#### Final Settlement

Please refer to [Final Settlement](#unique_39) [page ] 71 to do final settlement for your condition contract.

After processing the final settlement, you can optionally check the settlement documents refer to [Check Settlement Document for Final Settlement (Optional)](#unique_40) [page ] 72.

### Final Settlement with Adjustments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you enter conditions in the condition contract to adjust the final royalty amount before you process the final settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Royalties (F5414). | The Manage Condition Contracts - Royalties screen displays. |  |
| 3 | Change Condition Contract | On the Manage Condition Contracts - Royalties screen, select the relevant condition contract and choose More Links.Choose from More Links > Change Condition Contract . |  |  |
| 4 | Enter Condition Data for Royalty Condition | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition.Make one of the following entries and choose Enter.Adjustment of business volumeCondition Type: RRBD Royalties BusV DeltaValid From: for example, <today's date>Valid to: for example, <validity end of condition contract>Condition Rate: for example, 100 AEDAdjustment of royalty amountCond. Type: RRJ1 Royalties AdjustmentValid From: for example, <today's date>Valid to: for example, <validity end of condition contract>Condition Rate: for example, 20 AEDEntry of a fixed settlement amountCond. Type: RRV1 Royalties VerifiedValid From: for example, <today's date>Valid to: for example, <validity end of condition contract>Condition Rate: for example, 1000 AEDNote The conditions entered here are used to adjust the royalty amount. You can also choose Condition Contract / Material as condition level. You then also specify the material for a condition record. In case the Valid From and Valid To date are copied from the condition contract validity according to user settings, you can check and change these dates if necessary. |  |  |
| 5 | Save Condition Contract | Choose Save. |  |  |

After you have maintained the conditions to adjust the royalty amount, you perform the final settlement as described in the chapter Final Settlement in section Royalties Settlement Processing. Then check the created settlement document as described in Check Settlement Document for Final Settlement (Optional) in section Royalties Settlement Processing. In the pricing elements, particularly check that the system has determined the royalty amount using the conditions for adjustment.

### Royalties Unlikelihood (Optional)

Purpose

During the creation of the condition contract (step Create Condition Contract in Royalties Settlement Processing section), when entering the conditions, you have the option to use the condition: Royalties Unlikelihd. You use condition type Royalties Unlikelihd in case the minimum sales turnover will not be reached and therefore no accruals should be created or existing accruals should be reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Condition Data (Optional) | In the Conditions area, select New Condition.Make the following entries and press Enter.Condition Type: RRU1 Royalties UnlikelihdCondition Rate: for example, <100%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract> |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Royalties. | The SAP Fiori launchpad displays. |  |
| 2 | Access Reverse Settlement Documents | Open Reverse Settlement Documents - Condition Contracts (WB2R_CANCEL_DOCS). | The Reverse Settlement Documents for Condition Contracts screen displays. |  |
| 3 | Reverse Settlement Documents for Condition Contracts | On the Reverse Settlement Documents for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract(s) created in this test>Check Run Only: <unselect this checkbox>Choose Execute.Choose Continue in the pop-up window. | The Log for Reversal of Settlement Documents - Live Run screen displays. All settlement documents for the selected condition contract(s) are reversed. |  |

## Follow-Up Processes

You have finished all the activities that are part of the business process described in this document.

To accomplish the subsequent activities of this business process, use the master data from this document and carry out the process steps described in one or more of the following scope items.

### Accounts Payable (Optional)

Purpose

In this process step, you open payables invoices that are automatically created from purchasing processes with Accounts Payables.

Procedure

Complete the activities described in the Test Script of the scope item Accounts Payable (J60) using the open supplier invoices created running the Royalties Settlement for Sales (55I).

### General Ledger Reporting and CO-PA Reporting (Optional)

Purpose

After completing the activities in this test script, it is possible to run General Ledger Reporting and CO-PA Reporting connected with the accounts which were used in this royalties settlement process. Log on as General Ledger Accountant or Sales Accountant and run the reports which apply to your needs and check the postings on your accounts. Please refer to Accounting and Financial Close (J58) scope item to Manage G/L Account Master Data and Manage Financial Statement Versions.

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
- related-to :: [[08-sales-order-management/sales-rebate-processing-1b6-ae-test-script-sap-s-4hana-cloud-public-ed]]
- related-to :: [[08-sales-order-management/test-script-condition-contract-with-customer-hierarchy-consumer-produc]]
- related-to :: [[08-sales-order-management/test-script-sales-commissions-external-sales-representative-2tt-ae-863]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55I_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 206,907 chars in the whole document
