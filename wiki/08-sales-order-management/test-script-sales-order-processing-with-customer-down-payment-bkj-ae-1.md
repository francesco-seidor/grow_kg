---
id: 08-sales-order-management/test-script-sales-order-processing-with-customer-down-payment-bkj-ae-1
title: "Test Script: Sales Order Processing with Customer Down Payment (BKJ_AE) (BKJ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (BKJ_AE, UAE) for sales order processing with customer down payment, with PEPPOL e-invoicing prerequisites."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-contracts-and-down-payments]
aliases: [BKJ_S4CLD2608_BPD_EN_AE]
keywords: [Sales Contracts and Customer Down Payments, customer down payment, sales order processing, milestone billing plan, down payment request, incoming payments, delivery block, billing documents, electronic invoicing, edocument cockpit]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKJ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1278
topic: 08-sales-order-management/sales-contracts-and-down-payments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Order Processing with Customer Down Payment (BKJ_AE) (BKJ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKJ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Contracts and Customer Down Payments** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Order Processing with Customer Down Payment (BKJ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862561)

[2 Prerequisites 4](#_Toc232862562)

[2.1 System Access 4](#_Toc232862563)

[2.2 Roles 4](#_Toc232862564)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862565)

[2.4 Business Conditions 7](#_Toc232862566)

[2.5 Preliminary Steps 7](#_Toc232862567)

[2.5.1 Set Initial Stock for Material 7](#_Toc232862568)

[2.5.2 Create Condition Records (Optional) 9](#_Toc232862569)

[2.5.3 Set Delivery Block Automatically in Milestone Billing Plan (Optional) 9](#_Toc232862570)

[2.5.4 Remove Delivery Block Reason Code Automatically in Milestone Billing Plan (Optional) 11](#_Toc232862571)

[2.5.5 Preliminary Steps for Electronic Invoicing (PEPPOL) 13](#_Toc232862572)

[2.5.5.1 Define Identification Types for Business Partners 13](#_Toc232862573)

[2.5.5.2 Maintain Company Code Data (FINSC_T001Z_N) 16](#_Toc232862574)

[2.5.5.3 Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552) 18](#_Toc232862575)

[2.5.5.4 Maintain Business Partner Master Data 20](#_Toc232862576)

[2.5.5.5 Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301) 21](#_Toc232862577)

[2.5.5.6 Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304) 23](#_Toc232862578)

[2.5.6 Optional Steps for Electronic Invoicing (PEPPOL) 25](#_Toc232862579)

[2.5.6.1 Business Partner Master Data Maintenance for Electronic Invoicing (Optional) 25](#_Toc232862580)

[2.5.6.2 Value Mapping Maintenance for Electronic Invoicing (Optional) 26](#_Toc232862581)

[2.5.7 Check Advanced Down Payment Processing for Item Category CBAO, CTAD, and CTAX 30](#_Toc232862582)

[3 Overview Table 32](#_Toc232862583)

[4 Test Procedures 33](#_Toc232862584)

[4.1 Create Sales Orders with Billing Plan 33](#_Toc232862585)

[4.2 Change Sales Orders (Remove Billing Block) 36](#_Toc232862586)

[4.3 Create Attachment for Sales Order (Optional) 37](#_Toc232862587)

[4.4 Create Down Payment Request 38](#_Toc232862588)

[4.5 Post a Down Payment 40](#_Toc232862589)

[4.6 Create Delivery 42](#_Toc232862590)

[4.7 Create Attachment for Delivery (Optional) 44](#_Toc232862591)

[4.8 Execute Picking 45](#_Toc232862592)

[4.9 Check Batches (Optional) 46](#_Toc232862593)

[4.10 Post Goods Issue 47](#_Toc232862594)

[4.11 Change Sales Orders (Remove Billing Block) 49](#_Toc232862595)

[4.12 Billing 50](#_Toc232862596)

[4.13 eDocument Cockpit 52](#_Toc232862597)

[4.14 Create Attachment for Billing (Optional) 54](#_Toc232862598)

[5 Appendix 56](#_Toc232862599)

[5.1 Process Integration 56](#_Toc232862600)

[5.2 Succeeding Processes 56](#_Toc232862601)

[5.3 Scheduling Job (alternative) 56](#_Toc232862602)

[5.3.1 Job Scheduling for Delivery Creation (Alternative) 56](#_Toc232862603)

[5.3.2 Job Scheduling for Goods Issue Deliveries (Alternative) 57](#_Toc232862604)

[5.3.3 Job Scheduling for Billing Creation (Alternative) 58](#_Toc232862605)

[5.3.4 Job Scheduling for Billing Release (Alternative) 59](#_Toc232862606)

[5.3.5 Job Scheduling for Billing Output (Alternative) 60](#_Toc232862607)

[5.4 Restart Error Messages to Re-process Delivery Block Removal (Alternative) 61](#_Toc232862608)

## Purpose

Overview

In this process, you create requests for down payment, record the receipt of the down payment, and create a final invoice after the deduction of the received down payment and a receipt of the final amount due on the invoice. The process uses the billing plan functionality in Sales and Distribution. The integrated process allows the maintenance of proper document flow between the sales and financial transactions.

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
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4 HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics. Check your SAP system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. |

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFOno Serial no.; batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH) (BLJ) (BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDno Serial no.; batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH) (BLJ) (BLP).See sections Business Conditions and Preliminary Steps. |
| Material | SM0001 | Service Material 01 | Only use if you have activated the building block Sell of Services Material (2B4) (2B5) (2B6). |
| Material | NS0002 |  |  |
| Sold-to party | 33100004 | Domestic UAE Customer 4 |  |
| Ship-to party | 33100004 | Domestic UAE Customer 4 |  |
| Payer | 33100004 | Customer domestic 04 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information about creating master data, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Script documentation.

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:run through the Procurement of Direct Materials (J45) process orcreate stock using Fiori Launchpad tile (for details see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Closing MM Period and Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up-to-date. |

### Preliminary Steps

#### Set Initial Stock for Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods Receipt & Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : <Material Number> . |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: <Enter a Plant>Storage Location: <Enter a Storage Location> |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post. |  |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

#### Set Delivery Block Automatically in Milestone Billing Plan (Optional)

Purpose

This optional process step shows you how to set delivery block to sales order items in sales order processing with milestone billing plan.

You can set delivery block automatically with help of SSCUI 102792 Define Date Categories for Billing Plan Types, when using milestone billing plan. Once delivery block reason code is selected from this SSCUI, the delivery block will be set in the schedule lines of corresponding sales order items.

If Apply to BOMs checkbox is selected, the delivery block can be set in all BOM items when at least for one BOM item with billing plan the corresponding delivery block reason code has been selected.

Once down payment is received – steps in chapter [Post a Down Payment](#unique_10) [page ] 40 have been completed, delivery block will be removed automatically.

|  |
| --- |
| Note If there is an existing delivery block reason code in a schedule line, it will not be overwritten by the delivery block reason code from billing plan date category. And the delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in SSCUI Define Date Categories for Billing Plan Types. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241)Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Configuration Item for Billing Plans | Enter the following filters:Application Area: SalesSub-Application Area: Sales BillingItem Name: Billing Plans | The Configure Your Solution - Billing Plans screen displays. |  |
| 5 | Go to Maintain Date Categories for Milestone Billing Plans Overview | Choose Configure on the right of Define Date Categories for Billing Plan Types. | The Change View "Define Date Categories for Billing Plan Types": Overview screen displays. |  |
| 6 | Go to Maintain Date Categories for Milestone Billing Plans Detail | Select the line to be edited, for example the line with Billing Plan type 90 and Date Category 04.Choose Details. | The Change View "Define Date Categories for Billing Plan Types": Details screen displays. |  |
| 7 | Set Delivery Block | In the Billing Data area, set delivery block from drop down list, for example, choose 53 Check Prepayment. | Delivery block is set. |  |
| 8 | Set Apply to BOMs (Optional for Sales Kits) | Press Enter after setting delivery block. Select checkbox Apply to BOMs and choose Save. | Apply to BOMs is set.Note Once this checkbox is set, delivery block will be set to all Sales BOM items. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Activity | Go to the Business Processes Configuration app and search for the following activity: Define Date Categories for Billing Plan Types.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system.Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Date Categories for Billing Plan Types": Overview screen displays. |  |
| 3 | Go to Maintain Date Categories for Milestone Billing Plans Detail | Select the line to be edited, for example the line with Billing Plan type 90 and Date Category 04.Choose Details. | The Change View "Define Date Categories for Billing Plan Types": Details screen displays. |  |
| 4 | Set Delivery Block | In the Billing Data area, set delivery block from drop down list, for example, choose 53 Check Prepayment. | Delivery block is set. |  |
| 5 | Set Apply to BOMs (Optional for Sales Kits) | Press Enter after setting delivery block. Select checkbox Apply to BOMs and choose Save. | Apply to BOMs is set.Note Once this checkbox is set, delivery block will be set to all Sales BOM items. |  |

#### Remove Delivery Block Reason Code Automatically in Milestone Billing Plan (Optional)

Prerequisites

The preliminary steps to this chapter are described in chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_9) [page ] 9. Only after setting automatic delivery block can the automatic removal of delivery block reason code be enabled.

Purpose

This optional process step shows you how to remove delivery block reason code automatically in milestone billing plan.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241)Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Configuration Item for Billing Plans | Enter the following filters:Application Area: SalesSub-Application Area: Sales BillingItem Name: Billing Plans | The Configure Your Solution - Billing Plans screen displays. |  |
| 5 | Access the Configuration Activity | Choose Configure for Define Billing Plan Types for Milestone Billing. | The Define Billing Plan Types for Milestone Billing screen displays. |  |
| 6 | Remove Delivery Block | Select the line to be edited, for example the line with Billing Plan Type 90, choose the checkbox Relevant for Down Payments, and choose Save. | Delivery block reason code will be removed automatically after the down payment is cleared.Note The delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_9) [page ] 9. |  |

Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP CBC page displays. |  |
| 2 | Access the Activity | Go to the Business Processes Configuration app and search for the following activity: Define Billing Plan Types for Milestone Billing.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Billing Plan Types for Milestone Billing screen displays. |  |
| 3 | Remove Delivery Block | Select the line to be edited, for example the line with Billing Plan Type 90, choose the checkbox Relevant for Down Payments, and choose Save. | Delivery block reason code will be removed automatically after the down payment is cleared.Note The delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_9) [page ] 9. |  |

#### Preliminary Steps for Electronic Invoicing (PEPPOL)

These settings are optional, but necessary if you want to test eDocuments Cockpit for PEPPOL.

Purpose

To be able to run the step e-Document Cockpit for PEPPOL United Arab Emirates, the following prerequisites should be met:

- Define Identification Types for Business Partners (SSCUI 103654)
- Maintain Additional Parameters (FINSC_T001Z_N)
- Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552)
- Maintain Business Partner Master Data
- Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301)
- Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304)

##### Define Identification Types for Business Partners

Purpose

Define identification type (ID Type) for the unique identification number your business partner received from the service provider.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Change Local Version | Click Set Local Version and switch to Malysia in view of Manage Your Solution. | Change local version as Malaysia. |  |
| 4 | Open Configure Your Solution | Click and choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 5 | Search Relevant Activities | Enter the following filters:Application Area: Database and Data ManagementSub Application Area: Business PartnerIn the items table, select the item with item name: Define Identification Types. | The result displays. |  |
| 6 | Navigate to Define Identification Types | Select the searched item and into view of Configure Your Solution - Business Partner.Select Define Identification Types in right section under tab of Configuration Steps.Click Configure and go to the view of Define Identification Types: Change. | The result displays. |  |
| 7 | Maintain Settings | Choose New Entries and get into the view of New Entries: Details of Added Entries.Make the following entries and save:ID Type: AELRIDDescription: Legal Registration IndentifierID Category: AELRIDOrganization: XPersons: XGroups: XID Type: AELRACDescription: Legal Registration Auth./Ctry.ID Category: AELRACOrganization: XPersons: XGroups: XChoose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Identification Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Define Identification Types screen displays. |  |
| 3 | Maintain Settings | Choose New Entries and get into the view of New Entries: Details of Added Entries.Make the following entries and save:ID Type: AELRIDDescription: Legal Registration IndentifierID Category: AELRIDOrganization: XPersons: XGroups: XID Type: AELRACDescription: Legal Registration Auth./Ctry.ID Category: AELRACOrganization: XPersons: XGroups: XChoose Save. |  |  |

##### Maintain Company Code Data (FINSC_T001Z_N)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to add tax information to company code by configuration step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Set local Version | Choose Set Local Version.In the dropdown list, choose Malsysia, and then choose Set Local Version. |  |  |
| 5 | Choose Application Area | Make the following entries:Application Area: FinanceSub Application Area: Master and Organizational Data |  |  |
| 6 | Go to Configuration Details | On the Configure Your Solution screen, search for the following configuration step: Maintain Additional Parameters. Choose Go.In the search result, select the configuration activity and go to the next screen.On the Configure Your Solution - Maintain Additional Parameters screen，go to the configuration step Maintain Additional Parameters and choose Configure. | The Maintain Additional Parameters screen is displayed. |  |
| 7 | Create Additional Parameters | Create the following entries:Company Code: 3310Maintain AE tax numbers for this business partner:Parameter Type: AELRID (Legal Registration Identifier)Parameter Value: <123456>Parameter Type: AELRAC (Legal Registration Auth./Ctry.)Parameter Value: <Ministry>Parameter Type: SAPAE1 (Tax Identification Number)Parameter Value: <1234567890>Choose Save. | The new Additional Parameters are created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Additional Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configuration Your Solution- Maintain Additional Parameters screen is displayed. |  |
| 3 | Create Additional Parameters | Create the following entries:Company Code: 3310Maintain AE tax numbers for this business partner:Parameter Type: AELRID (Legal Registration Identifier)Parameter Value: <123456>Parameter Type: AELRAC (Legal Registration Auth./Ctry.)Parameter Value: <Ministry>Parameter Type: SAPAE1 (Tax Identification Number)Parameter Value: <1234567890>Choose Save. | The new Additional Parameters are created. |  |

##### Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to define process communication through Cloud services by configuration step. In this activity, you define, for a given company code, if an eDocument process integrates with SAP Document and Reporting Compliance, Cloud edition (using the standard integration or other types of integration) to exchange electronic documents with external communication parties.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Set Local Version | Choose Set Local Version.In the dropdown list, Choose United Arab Emirates, and then choose Set Local Version. |  |  |
| 5 | Choose Application Area | Make the following entries:Application Area: Application Platform and InfrastructureSub Application Area: Legal Compliance |  |  |
| 6 | Go to Configuration Details | On the Configure Your Solution screen, search for the following configuration step: Define Process Communication Through Cloud Services. Choose Go.On the Configure Your Solution - Define Process Communication Through Cloud Services screen, go to the configuration step Define Process Communication Through Cloud Services and choose Configure. | The Define Process Communication Through Cloud Services screen is displayed. |  |
| 7 | Create Process Communication Through Cloud Services | Create the following entries:Company Code: 3310Maintain the entries as following:BUKRS: 3310Process: AEINVSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosBUKRS: 3310Process: AEINVINSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosChoose Save. | The new Process Communication Through Cloud Services is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Process Communication Through Cloud Services.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configuration Your Solution- Define Process Communication Through Cloud Services screen is displayed. |  |
| 3 | Create Process Communication Through Cloud Services | Create the following entries:Company Code: 3310Maintain the entries as following:BUKRS: 3310Process: AEINVSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosBUKRS: 3310Process: AEINVINSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosChoose Save. | The new Process Communication Through Cloud Services is created. |  |

##### Maintain Business Partner Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you add tax information to Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data Test. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Enter:Business Partner: XXXXXXXX |  |  |
| 4 | Enter Business Partner | Hover over the text and choose the Switch Between Display and Change (F6) button to switch to change mode. |  |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:Customer (Fin.Accouting) (FLCU00) |  |  |
| 6 | Maintain United Arab Emirates Tax Numbers | On the Identification tab, on the Tax Numbers screen, maintain the following data for this business partner:Category: AE0Tax Number Long: <123456789012345>Category: AE1Tax Number Long: <1234567890> |  |  |
| 6 | Save Your Data | Save your entries. |  |  |

##### Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301)

Purpose

In this activity, you define the party identification types that business partners use in the PEPPOL network.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution.In the Set Country Version dialog box, select the country from the dropdown menu and choose Set Country Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: Application Platform and InfrastructureSub Application Area: Legal Compliance | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Settings for Peppol item name and choose arrow at the item end. | The Configure Your Solution - Settings for Peppol screen displays. |  |
| 6 | Navigate to Assign Party ID Types to Business Partner | For the Assign Party ID Types to Business Partner row, choose Configure. | The Assign Party ID Types to Business Partner screen displays. |  |
| 7 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Partner ID: <business partner ID>Type: C CustomerParty ID type: AE:TINE-mail: <select this only if the customer cannot receive electronic invoices> |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app.Search for the Assign Party ID Types to Business Partner activity and choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Party ID Types to Business Partner screen displays. |  |
| 3 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Partner ID: <business partner ID>Type: C CustomerParty ID type: AE:TINE-mail: <select this only if the customer cannot receive electronic invoices> |  |  |

##### Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304)

Purpose

In this activity, you maintain the party identification types (party ID type) that your company uses in the exchange channels in the PEPPOL network.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution.In the Set Country Version dialog box, select the country from the dropdown menu and choose Set Country Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: Application Platform and InfrastructureSub Application Area: Legal Compliance | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Settings for Peppol item name and choose arrow at the item end. | The Configure Your Solution - Settings for Peppol screen displays. |  |
| 6 | Navigate to Assign Party ID Types to Companies | For the Assign Party ID Types to Companies row, choose Configure. | The Assign Party ID Types to Companies screen displays. |  |
| 7 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Company code: 3310Party ID type: AE:TIN |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app.Search for the Assign Party ID Types to Companies activity and choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Party ID Types to Companies screen displays. |  |
| 3 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Company code: 3310Party ID type: AE:TIN |  |  |

#### Optional Steps for Electronic Invoicing (PEPPOL)

##### Business Partner Master Data Maintenance for Electronic Invoicing (Optional)

Purpose

To run the steps in electronic invoicing, you must maintain the identification number and tax number category for customer master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Master Data Specialist - Business Partner Data Test. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Enter:Business Partner: for example, 33100003 | The view of Display Organization displays. |  |
| 4 | Switch to Change Mode | On the Display Organization: XXXXXXXX screen, choose Switch Between Display and Change. |  |  |
| 5 | Go to Identification Tab | On the Change Organization: XXXXXXXX screen, choose Business Partner (Gen.) in the Change in BP Role field.Choose Identification tab . |  |  |
| 6 | Maintain ID Type and Tax numbers for Business Partner | On the Identification tab, in the Identification Numbers screen, maintain Malaysia participant ID for this Business Partner:ID Type: AELRIDIdentification Number: for example, <123456> |  |  |
| 7 | Save Your Data | Choose Save. |  |  |

##### Value Mapping Maintenance for Electronic Invoicing (Optional)

Purpose

To run the step in electronic invoicing, you must maintain the value mapping for eDocument UBL.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. | The SAP Fiori launchpad dis-plays. |  |
| 2 | Access the App | Open Configure Value Mapping (/AIF/VMAP_CONF). | The Configure Value Mapping view is displayed. |  |
| 3 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_ALLOW_COND_TYPE |  |  |
| 4 | Switch to Change Mode | On the Display Value Mapping screen, choose Switch Between Display and Change. |  |  |
| 5 | Maintain Value Mapping | On the Change Value Mapping screen, click Append, choose append number.Maintain the following detail:Reason Code: <number of code>, for example, 95Reason Description: <description of code>, for example, DiscountCondition Type: <value>, for example, YK07Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. |  |  |
| 6 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value Mapping screen displays. |  |
| 7 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_CHARGE_COND_TYPE |  |  |
| 8 | Switch to Change Mode | On the Display Value Mapping screen, choose Switch Between Display and Change. |  |  |
| 9 | Maintain Value Mapping | On the Change Value Mapping screen, click Append, choose append number.Maintain the following detail:Reason Code: <number of code>, for example, RVReason Description: <description of code>, for example, LoadingCondition Type: <value>, for example, DRV1Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 10 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value Mapping screen displays. |  |
| 11 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_DISTR_CHANNEL |  |  |
| 12 | Switch to Change Mode | On the Display Value Mapping screen, choose Switch Between Display and Change. |  |  |
| 13 | Maintain Value Mapping | On the Change Value Mapping screen, click Append, choose append number.Maintain the following detail:Distribution Channel: <number of code>, for example, 60Sales Org.: <value>, for example, 3310Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 14 | Back | Choose Back to go to the screen Configure Value Mapping. |  |  |
| 15 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_LEGAL_FORM |  |  |
| 16 | Switch to Change Mode | On the Display Value Mapping screen, choose Switch Between Display and Change. |  |  |
| 17 | Maintain Value Mapping | On the Change Value Mapping screen, click Append, choose append number.Maintain the following detail:Invoice Code: <number of code>, for example, 1Legal Form.: <value>, for example, FZMaintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 18 | Back | Choose Back to go to the screen Configure Value Mapping. |  |  |
| 19 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_PAYM_MEANS_CODE |  |  |
| 20 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 21 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <value 1>Payment Method: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. |  |  |
| 22 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value mapping screen displays. |  |
| 23 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_TAX_CATEGORY |  |  |
| 24 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 25 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <number of index>Tax code: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 26 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value mapping screen displays. |  |
| 27 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_TAX_EXEMPT_CODE |  |  |
| 28 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 29 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <number of index>Tax Code: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 30 | Back | Choose Back to go to the screen Configure Value Mapping. |  |  |
| 31 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_PROFIT_MARGIN_PP |  |  |
| 32 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 33 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Pricing Procedure: <value>Sales Org.: 3310Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. |  |  |
| 34 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value mapping screen displays. |  |
| 35 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_RVS_CHRG_MECH |  |  |
| 36 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 37 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <number of index>Material Group: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 38 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value mapping screen displays. |  |
| 39 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_ITEM_CATEGORY_SD |  |  |
| 40 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 41 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <yes/no>Item Category: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |

#### Check Advanced Down Payment Processing for Item Category CBAO, CTAD, and CTAX

Purpose

Once Advanced Down Payment Processing (ADP) is activated for any of these item categories, you can no longer use that item category for the classical down payment process in new sales orders. Ensure that Advanced Down Payment Processing is disabled for item categories CBAO, CTAD, and CTAX if you want to continue using the classical down payment process.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Configuration Activity | Search for the configuration activity Configure Item Categories (ID: 103411).In the All Items table, select the line for Sales Documents.In the Configuration Steps section, choose Configure in the line for Configure Item Categories activity. | The Configure Item Categories: Change screen is displayed. |  |
| 5 | Select Item Category CBAO, CTAD, and CTAX | In the Configure Item Categories table, select the checkbox for item category CBAO, CTAD, and CTAX, and choose Details button. | The Configure Item Categories: Change: Details screen is displayed. |  |
| 6 | Check Advanced Down Payment Processing | In the General Control section, ensure that the checkbox Advanced Down Payment Processing is not selected. | Advanced down payment processing is now inactive for items of item category CBAO, CTAD, and CTAX. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Activity | Go to the Business Processes Configuration app and search for the following activity: Configure Item Categories.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Item Categories: Change screen is displayed. |  |
| 3 | Select Item Category CBAO, CTAD, and CTAX | In the Configure Item Categories table, select the checkbox for item category CBAO, CTAD, and CTAX, and choose Details button. | The Configure Item Categories: Change: Details screen is displayed. |  |
| 4 | Check Advanced Down Payment Processing | In the General Control section, ensure that the checkbox Advanced Down Payment Processing is not selected. | Advanced down payment processing is now inactive for items of item category CBAO, CTAD, and CTAX. |  |

## Overview Table

The scope item Sales Order Processing with Customer Down Payment consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Orders with Billing Plan](#unique_23) [page ] 33 | Internal Sales Representative | Manage Sales Orders (F1873) | Order Saved and Order Confirmation sent to printer. |
| [Change Sales Orders (Remove Billing Block)](#unique_24) [page ] 36 | Internal Sales Representative | Change Sales Orders | Sales order is changed to allow for creation of down payment request |
| [Create Attachment for Sales Order (Optional)](#unique_25) [page ] 37 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Down Payment Request](#unique_26) [page ] 38 | Billing Clerk | Create Billing Documents (F0798) | Customer account is debited. A down payment request is generated. |
| [Post a Down Payment](#unique_10) [page ] 40 | Accounts Receivable Accountant | Post Incoming Payments (F1345) | The down payment is posted. |
| [Create Delivery](#unique_27) [page ] 42 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| [Create Attachment for Delivery (Optional)](#unique_28) [page ] 44 | Shipping Specialist | Display Outbound Delivery (VL03N) | The Display Outbound Delivery: Initial screen displays. |
| [Execute Picking](#unique_29) [page ] 45 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done. |
| [Check Batches (Optional)](#unique_30) [page ] 46 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Post Goods Issue](#unique_31) [page ] 47 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Change Sales Orders (Remove Billing Block)](#unique_32) [page ] 49 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Billing](#unique_33) [page ] 50 |  | Create Billing Documents - VF01 (VF01) |  |
| [Create Attachment for Billing (Optional)](#unique_34) [page ] 54 | Billing Clerk | Manage Billing Documents (F0797) |  |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as: apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

1. Log on to the SAP Fiori launchpad as a respective user, for example, Internal Sales Representative.
2. Access the Enterprise Search Bar by choosing the magnifying glass icon in the upper right corner.
3. The Enterprise Search bar displays two filter fields next to the search icon: all dropdown menu and a search field. Enter your Search Criteria and choose the business object type, for example, select Sales orders from the dropdown menu, and enter a sales order number in the search field and choose Search, the sales order lists.
4. Choose the sales order number link. The system navigates to the fact sheet screen and sales order related information is integrated and summarized in one Fiori page. You can get detailed data by choosing the corresponding links.

There are fact sheets available for the following objects (visible depending on the assigned role):

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Create Sales Orders with Billing Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to require a down payment from the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, choose Create and select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Sales Document Type: <sales order type> , for example, OR (Standard Order)Sales organization: 3310Distribution channel: 10Division: 00Choose Continue. | The Create Standard Order: Overview screen displays. |  |
| 5 | Enter Customer Number | Make the following entries:Sold-To Party: 33100004Customer Reference: <Reference>Cust. Ref. Date: <Date>Choose Enter. |  |  |
| 6 | Enter Order Details | Make the following entries:Order Reason: <Order Reason>Material: <material number>Order Quantity: <quantity>, for example, 10Item Category:CBAO Milestone-Bill.Plan for Trading goods.CTAD Milest.-Bill.Plan SV for Service material SM0001.CTAX MilstBillPl NonStock for Non-stock material NS0002.Note A service product SM0001 is used in the sales order. It allows the sales of services without delivery and direct (order-related) billing. You may skip the chapters from [Create Delivery](#unique_27) [page ] 42 to [Post Goods Issue](#unique_31) [page ] 47.Batch: <batch number> The step is optional.Note The billing of this business process is order-related. This means that the down payment request and the final invoice only contain the information that is available from the sales order like material, quantity, and batch number. If you need a batch number on the down payment request and the final invoice you must enter it already in the sales order.Choose Enter. |  |  |
| 7 | Choose Billing Plan | Select the item. Choose Menu > Goto > Item > Billing Plan .Note Alternatively, you can assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . The header billing plan will be applied to all items with item category CBAO, CTAD or CTAX. Amount is proportionally to the value of the items participating in the down payment process distributed to the items. |  |  |
| 8 | Enter Details | For the first line item (Down Payment), make the following entries for the advance payment:Billing Date: <billing date>. For example, enter today's date.Bill Value: <amount of billing>. For example: Down Payment amountDate category (DCat): 04 | You can create more than one Down Payment by using same entries as 1st Down Payment. |  |
| 9 | Enter Details | For the second line item (Final Invoice), make the following entries for the advance payment:Billing Date: <billing date>. For example, enter today's date.Date category (DCat): 02 |  |  |
| 10 | Enter | Choose Enter. Confirm system messages with enter if necessary. | Final Invoice related data is determined. For example, in Bill value field, the amount of billing is calculated by the system. |  |
| 11 | Back | Choose Back. |  |  |
| 12 | Save | Save your entries. |  |  |

|  |
| --- |
| Note Via SSCUI Maintain Date Categories for Milestone Billing Plans, you can assign a delivery block reason code to milestone billing plan. In this case, when creating a sales order and using this billing plan together with item category CBAO (Milestone Bill.Plan), the delivery block reason code will be copied to the schedule lines. If you delete the billing plan from sales order afterwards, the schedule lines will not be updated automatically. In case the item category or schedule line category changes afterwards, delivery block reason code will still be kept. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose Go. For example, enter sales order number in the Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right side of the Sales Order item and navigate to Display Standard Order xxx: Overview screen. | The Display Sales Order xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Menu > Extras > Output > Header > Edit . |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from a sales order.

Prerequisite

The billing block must be manually removed for the first down payment request to be processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go: for example, enter sales order number in Sales Order field. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Select the sales order number and choose Change Sales Orders - VA02 (VA02). | The Change Sales Order xxx: Overview screen displays. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose Menu > Goto > Item > Billing plan .Note Alternatively, If you assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Remove Billing Block | In the Dates section, in the Block column delete the billing block for the Down payment item (keep the billing block for the Final Invoice item). |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

### Create Attachment for Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2screen displays. |  |
| 3 | Navigate to Change Sales Order Screen | On the Manage Sales Orders - Version 2 screen, enter the respective order number created in previous step and choose Go.Click the sales order number and choose Change Sales Order - VA02. |  |  |
| 4 | Create Attachment for Sales Order | Choose Services for Object on the top right corner of screen, choose Create Attachment. | The File Upload screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of screen, choose Attachment List. | Attachment brings up on the Service: Attachment list screen. |  |

### Create Down Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a down payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798) under Sales > Billing Documents . | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings at the bottom bar. You can make the settings as follows :Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose Sales Document | More than one SD document item appear in Billing Due List Items table, select the row relevant to down payment request, and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Down payment request (FAZ) and maintain billing date, for example current date, then choose Create. | The draft billing document is created. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | Billing document is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 21191000 Down payment requests (customers) | none | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797) under Sales - Billing Document | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document | Enter the billing document number recorded previously in Billing Document field and choose Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document screen displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to Output Items the last assignment block. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select certain Billing document and choose Cancel billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete, and update the attachments.Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete and update the texts.Save your changes by choosing Save in the footer bar. |  |  |

### Post a Down Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a down payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Incoming Payments (F1345). | The Post Incoming Payments (F1345) screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Propose Items:General Information area:Company Code: 3310Posting Date: Current dateJournal Entry Date: <Current date>Value Date: Current datePeriod: Current periodJournal Entry Type: DZ (Customer Payment)Bank Data areaG/L Account (Company Code CoA): 11001010House Bank: AEBK1Bank Account: AEAC1Amount: Down Payment Amount / AEDNote Enter the amount of the journal entry the customer has been debited with in the previous step (billing value plus value added tax).Open Item Selection areaAccount Type/Account ID: Customer / 33100004 |  |  |
| 4 | Search for Down Payment Request | Choose Select More.In Line Item Type field, select checkbox in Special G/L Transactions and deselect other values from drop-down menu, then choose OK. | Select More dialog box displays.All down payment request documents which meet the conditions are listed in Open Items table. |  |
| 5 | Select Down Payment Request | Choose Clear in the down payment request document entry in Open Items table. | The item is copied to Items to Be Cleared table. |  |
| 6 | Post | Choose Post. | Success dialog box pop ups, the information Journal entry 14XXXXXXXX successfully posted displays. |  |
| 7 | Display Journal Entry | Choose Display. | The Manage Journal Entries screen displays. Detailed information involved in down payment journal entry is shown. |  |

|  |
| --- |
| Note After the down payment is cleared, the delivery block set from SSCUI Define Date Categories for Billing Plan Types in chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_9) [page ] 9 can be removed automatically if the checkbox Relevant for Down Payments is flagged in SSCUI Define Billing Plan Types for Milestone Billing for billing plan type 90.The delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in SSCUI Define Date Categories for Billing Plan Types. |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 11001060 Bank Account21191500 Tax sett.dwn pmt cus | 21190000 Down Payments - Customers22000000 Output tax (MWS) | none |

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: <shipping point> for example, 3310Planned Creation Date: <Delivery selection date>Order: <Sales order number created previously> |  |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. | A delivery is triggered to be created. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note With app Analyze Delivery Logs (F0870A), you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, for example: created by and additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry:If delivery is created successfully, delivery number is shown on tab Deliveries, else, you can display the exact message type, text and also the related sales document on tab Messages. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) | The Change Outbound Delivery (VL02N) screen displays |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the delivery number and click Continue.From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

### Create Attachment for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Display Outbound Delivery: Initial screen displays. |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <the outbound delivery number created in previous step> and choose Continue. | The Display Outbound Delivery xxx: Overview screen displays. |  |
| 4 | Create Delivery Attachment | Choose Services for Object on the top right corner of screen, choose Services for Object and then choose Create Attachment. | The File Upload screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object, then choose Attachment List. | Attachment shows up on Service: Attachment List screen. |  |

### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | Choose your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |

### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the batch number assigned to the material.

Prerequisites

Execute this step if batch management is used, such as TG21 and TG22.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <outbound delivery number>, and choose Enter. |  |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, go to the Batch field, and check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5 | Save Document | Choose Save. |  |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

|  |
| --- |
| Note For non-stock material NS0002, you may use App Change Outbound Delivery for posting goods issue to delivery document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpaddisplays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Make the following entry and choose Execute:Shipping Point/Receiving Pt: 3310 |  |  |
| 4 | Post Goods Issue | Select your outbound delivery note, and choose Post Goods Issue.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested, the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount displays.To check the financial document, use the Warehouse Clerk role, and access the Display Material Document List - Deprecated (MB51) app. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove a billing block from a sales order.

Prerequisite

COGS has been recognized. To recognize revenue in the same month to keep FI and PA in synch, the billing block must be removed manually to process the final invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar, and choose Go:Sales Order: <Sales Order Number> | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Select sales order number and choose Changes Sales Orders. | Sales order is displayed in result list. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose Menu > Goto > Item > Billing Plan .Note Alternatively, If you assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Delete Billing Block | In the Dates section, in the Block column, delete the billing block for the Final Invoice item. |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

### Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to bill a customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01) under Sales - Billing Document. | The Create Billing Document screen displays. |  |
| 3 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 4 | Choose Sales Document | Select the row of SD Document created previously and choose Create Billing Documents. | The dialog box Create Billing Documents displays. |  |
| 5 | Maintain Billing Type and Billing Date | Choose billing type F2 Invoice (F2) and maintain Billing Date, for example, <current date>, then choose OK. | Prepaid down payment is displayed as a separate item in the final invoice document. |  |
| 6 | Save Billing Document | On the Billing Document screen, choose Save. The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Billing document is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Rcvbls Domestic21190000 Down Payments - Customers22000000 Output tax (MWS) | 41000000 Rev Domestic Prod12100000 Rcvbls Domestic21191500 Tax sett.dwn pmt cus22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797) under Sales - Billing Document | The screen Manage Billing Document displays. |  |
| 2 | Search the Billing Document | Enter the billing document number recorded previously choose Enter. | The billing document which is created previously displays. |  |
| 3 | Display the Billing Document | Select the billing document item, and choose Display. | The billing document screen displays. |  |
| 4 | Check Output Condition | On the Billing Document screen go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select certain Billing document and choose Cancel billing Document. | There is a log displayed, Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete and update the texts. Save your changes by pressing Save in the footer bar. |  |  |

### eDocument Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you change or maintain the status of your eDocument.

|  |
| --- |
| Note Starting with the SAP S/4HANA Cloud 2208 release, if you are a new customer and want to enable advanced eDocument features such as eDocument Submit, Cancel and Reject, you must first activate the Document and Reporting Compliance features for your country/region. Otherwise, only Display mode is available. For more information, refer to Activate Document and Reporting Compliance Features in the Preliminary Steps section of the test script for scope item Document and Reporting Compliance (5XU). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open eDocument Cockpit (EDOC_COCKPIT). | The eDocument Cockpit view is displayed. |  |
| 3 | Select eInvoice Document | Make the following entries:Source Document: <Invoice number from prior steps>Note You can also search for your invoice. In the Results Overview section, expand your country/region to display your country's/region's eInvoice . | The eInvoice screen for your country/region displays. |  |
| 4 | Submit eInvoice | Select the row and choose Submit.Note The submission of the eDocument requires a connection to the SAP Cloud Platform. | The eDocument status updates with a Message Text: Action successfully executed: SUBMIT. |  |
| 5 | Review status | Review the eDocument status. The possible status of submitted eDocument:Accepted by receiving Access PointeDocument CreatedError at Sending Access PointSending RequestedReceived by Access PointError at Receiving Access Point |  |  |
| 6 | Display eDocument | Select the row for an eDocument with Accepted by receiving Access Point status.From dropdown for Display, select Display/Preview XML. | The eDocument in XML format is shown. |  |
| 7 | Display Source Document | Select the row of an eDocument and from the Go to dropdown, select Source Document. | A view displays of the original transaction that generated the eDocument (source document). |  |
| 8 | Back | Choose < (Back) to return to the previous view. |  |  |
| 9 | Review History of eDocument | From the Goto dropdown, select History to review the eDocument history. | The view displays the last process steps and statuses from selected eDocument. |  |
| 10 | Back | When completing your review, choose the Back button at the bottom of the view to return to the previous view. |  |  |
| 11 | Review Application Log | From the Goto dropdown, select Application Log.When there are no errors, a No Application Log found for the selected eDocument notification displays at the bottom of the view.If there are errors, an Application Log dialog box displays with information about the error. Review the message and choose Continue to close the dialog box. |  |  |
| 12 | Message Dashboard | Access Message Dashboard.If you encounter errors, a dialog box displays information about the error. Review the message and choose Continue to close the dialog box. |  |  |
| 13 | Cancel eDocument | To cancel an eDocument, choose the row of an eDocument with Created, Sending Requested, Error at Send. Acc. Point, or Val. Error at Rec. Acc. Point status.From the buttons above the list, from the More dropdown, select Cancel eDocument. | The status of eDocument changes to eDocument Cancelled and the status icon turns to green color |  |
| 14 | Delete eDocument | To delete an eDocument, choose a row from the list with a Created status.Mark the eDocument in status Created.From the buttons above the list, from the More dropdown, select Delete eDocument. | At the bottom of the view a Number of eDocuments that have been deleted: 1 notification displays. |  |

### Create Attachment for Billing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an attachment for a billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Search Billing | Make the following entry, and choose Enter:Billing Document: <Billing Document Number Created Previously> |  |  |
| 4 | Choose Billing Number | On the Manage Billing Documents screen, select your billing document created in the previous step, and choose Display. | The Billing Document screen displays. |  |
| 5 | Edit | On the Billing Documents screen, choose Edit. |  |  |
| 6 | Create Billing Attachment | Scroll down and choose Upload in the ATTACHMENTS section. | The Open File screen displays. |  |
| 7 | Import File | In the Open window, select a local path or file and choose Open.Choose Save. | The attachment is successfully created. |  |
| 8 | Check Attachment | In the ATTACHMENTS section, you can see the uploaded document. Choose the document you want to open. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following test script:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | In this activity you post the incoming payment.Complete all activities described in the test script: Accounts Receivable (J59) (Sections Section Post Incoming Payments) using the master data from this document. |
| Sales Order Fulfillment Monitoring and Operations (BKK) (optional) | Complete all activities described in the scope item: Sales Order Fulfillment Monitoring and Operations (BKK) (Sections Review Sales Documents blocked for billing, Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents) using the master data from this document. |

### Scheduling Job (alternative)

#### Job Scheduling for Delivery Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job screen displays. The Job Template should be Schedule Delivery Creation for Sales Orders. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details displays. |  |

#### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. The Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. The screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details are displayed. |  |

#### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

#### Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template defaultly should be Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details displays. |  |

#### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

### Restart Error Messages to Re-process Delivery Block Removal (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you use chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_9) [page ] 9 and chapter [Remove Delivery Block Reason Code Automatically in Milestone Billing Plan (Optional)](#unique_11) [page ] 11 to set and remove delivery block reason code automatically, but the delivery block from sales order schedule line is not automatically removed after the down payment is cleared, you can use steps in this chapter to check error and re-process the removal of delivery block reason code.

Preliminary Procedures

In the following steps, you can assign recipients to users for message monitoring for recipient name SD_DOWN_PAYMENT_RECIPIENT. Here we use a user with user ID CONF_EXPERT_BUS_NET_INT as example.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Assign Recipients to Users (F2949) | The Assign Recipients to User screen displays. |  |
| 3 | Select/Add User | Search the user with assigned recipients on the left side of the screen, for example search with user ID CONF_EXPERT_BUS_NET_INT. Select this user.If there is no existing user with user ID CONF_EXPERT_BUS_NET_INT, choose Add User bottom on the left of the screen.On the pop-up window, make the following entry and click Add.Name/ID: CONF_EXPERT_BUS_NET_INT | The Recipients for User screen displays with the selected user. |  |
| 4 | Assign Recipients | Choose Assign. | The Assign Recipients screen displays |  |
| 5 | Enter Assign Recipients Details | On the Assign Recipients pop-up window, make the following entries:Namespace: /SDDP (Sales Document with Down Payment)Recipient Name: SD_DOWN_PAYMENT_RECIPIENTMessage Type: Application Error or Technical ErrorAnd select the checkbox for the following fields:OverviewTechnical UserChoose Assign. | The Recipients is assigned to the selected user. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Monitoring Overview - SAP Application Interface Framework (F4515) | The Message Monitoring Overview screen displays. |  |
| 3 | Select the Time | On the Message Monitoring Overview screen, select time for message monitoring, for example: Passed Hour.Choose Go. | The result with selected period displays. |  |
| 4 | Open Messages | Find out the card for /SDDP - SO_DP_RFC – 1 and click on the error. | The error messages display. |  |
| 5 | Restart Messages | Select the error message(s) for the sales document(s) pending for removal of delivery block reason code.Choose Restart. | The message(s) restarted. |  |
| 6 | Check Messages (Optional) | Deselect the Error status and click on Go. | The messages details display with the updated status. |  |

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
> Flagged while digesting this document, not verified: The UAE (AE) script tells the user to set the local/country version to Malaysia when defining identification types for business partners and maintaining company code data, and describes a Malaysia participant ID for the business partner, while the process communication step selects United Arab Emirates; the intended country version is inconsistent within the document.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKJ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 109,870 chars in the whole document
