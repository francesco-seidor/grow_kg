---
id: 08-sales-order-management/customer-returns-bkp-ae-test-script-sap-s-4hana-cloud-public-edition-1
title: "Customer Returns (BKP_AE) Test Script, SAP S/4HANA Cloud Public Edition (BKP_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script for scope item BKP (Customer Returns, AE localization, 2608): prerequisites, roles, three return scenarios, refunds, appendix jobs."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-returns-and-refunds]
aliases: [BKP_S4CLD2608_BPD_EN_AE]
keywords: [Customer Returns and Refunds, customer returns, returns order creation, returns order approval, material inspection, refund determination, credit memos, replacement delivery, inspection at customer site, return to supplier]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKP_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1281
topic: 08-sales-order-management/customer-returns-and-refunds
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Customer Returns (BKP_AE) Test Script, SAP S/4HANA Cloud Public Edition (BKP_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKP_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Returns and Refunds** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Customer Returns (BKP_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Customer Returns (BKP_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232862016)

[2 Prerequisites 5](#_Toc232862017)

[2.1 System Access 5](#_Toc232862018)

[2.2 Roles 5](#_Toc232862019)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232862020)

[2.4 Business Conditions 9](#_Toc232862021)

[2.5 Additional Manual Configuration 10](#_Toc232862022)

[2.6 Preliminary Steps 10](#_Toc232862023)

[2.6.1 Create Info Records 10](#_Toc232862024)

[2.6.2 Set Initial Stock for Material 12](#_Toc232862025)

[2.6.3 Maintain Returns Supplier 13](#_Toc232862026)

[2.6.4 Create Condition Records (Optional) 14](#_Toc232862027)

[2.6.5 Preliminary Steps for Returns Order Approval (Optional) 15](#_Toc232862028)

[2.6.5.1 Define and Assign Approval Reasons 15](#_Toc232862029)

[2.6.5.2 Implement Cloud BADI 17](#_Toc232862030)

[2.6.5.3 Manage Teams and Responsibilities 19](#_Toc232862031)

[2.6.5.4 Set Up Workflow 20](#_Toc232862032)

[3 Overview Table 22](#_Toc232862033)

[4 Test Procedures 26](#_Toc232862034)

[4.1 Scenario 1: Goods are Returned to Seller 26](#_Toc232862035)

[4.1.1 Create Returns Order 26](#_Toc232862036)

[4.1.2 Process Returns Order Approval (Optional) 33](#_Toc232862037)

[4.1.2.1 Withdraw from Approval 33](#_Toc232862038)

[4.1.2.2 Approve/Reject/Rework Returns Order 34](#_Toc232862039)

[4.1.2.3 Rework Returns Order 36](#_Toc232862040)

[4.1.2.3.1 Check the Notifications 36](#_Toc232862041)

[4.1.2.3.2 Change Returns Order 37](#_Toc232862042)

[4.1.2.3.3 Release the Reworked Returns Order 37](#_Toc232862043)

[4.1.3 Execute Picking 38](#_Toc232862044)

[4.1.4 Post Goods Receipt 39](#_Toc232862045)

[4.1.5 Perform Material Inspection 40](#_Toc232862046)

[4.1.6 Determine Refund 42](#_Toc232862047)

[4.1.7 Display Returns Overview 44](#_Toc232862048)

[4.1.8 Refund Customer with Credit Memo (Option A) 45](#_Toc232862049)

[4.1.8.1 Create Credit Memo 45](#_Toc232862050)

[4.1.9 Refund Customer with Replacement Product (Option B) 47](#_Toc232862051)

[4.1.9.1 Create Free-of-Charge Delivery 48](#_Toc232862052)

[4.1.9.2 Execute Picking 49](#_Toc232862053)

[4.1.9.3 Post Goods Issue 50](#_Toc232862054)

[4.1.9.4 Create Pro-forma Invoice 52](#_Toc232862055)

[4.1.9.5 Create Customer Invoice 54](#_Toc232862056)

[4.1.10 Send Back to Customer (Option C) 56](#_Toc232862057)

[4.1.10.1 Execute Picking 56](#_Toc232862058)

[4.1.10.2 Posting Goods Issue 57](#_Toc232862059)

[4.2 Scenario 2: Goods are Inspected at Customer Site 58](#_Toc232862060)

[4.2.1 Create Returns Order 58](#_Toc232862061)

[4.2.2 Change Returns Order 59](#_Toc232862062)

[4.2.3 Refund Customer with Credit Memo 62](#_Toc232862063)

[4.2.3.1 Create Credit Memo 62](#_Toc232862064)

[4.2.4 Refund Customer with Replacement Material 64](#_Toc232862065)

[4.2.4.1 Create Free-of-Charge Delivery 64](#_Toc232862066)

[4.2.4.2 Execute Picking 65](#_Toc232862067)

[4.2.4.3 Post Goods Issue 66](#_Toc232862068)

[4.2.4.4 Create Pro-forma Invoice 68](#_Toc232862069)

[4.2.4.5 Create Customer Invoice 69](#_Toc232862070)

[4.2.5 Initiate Normal Return 71](#_Toc232862071)

[4.3 Scenario 3: Goods are Returned to Supplier via Seller 71](#_Toc232862072)

[4.3.1 Create Returns Order 72](#_Toc232862073)

[4.3.2 Execute Picking 75](#_Toc232862074)

[4.3.3 Post Goods Receipt 76](#_Toc232862075)

[4.3.4 Perform Material Inspection 77](#_Toc232862076)

[4.3.5 Determine Refund 78](#_Toc232862077)

[4.3.6 Display Returns Overview 80](#_Toc232862078)

[4.3.7 Refund Customer with Credit Memo (Option A) 81](#_Toc232862079)

[4.3.7.1 Create Credit Memo 81](#_Toc232862080)

[4.3.8 Refund Customer with Replacement Product (Option B) 83](#_Toc232862081)

[4.3.8.1 Create Free-of-Charge Delivery 84](#_Toc232862082)

[4.3.8.2 Execute Picking 85](#_Toc232862083)

[4.3.8.3 Post Goods Issue 86](#_Toc232862084)

[4.3.8.4 Create Pro-forma Invoice 87](#_Toc232862085)

[4.3.8.5 Create Customer Invoice 89](#_Toc232862086)

[4.3.9 Return Goods to Supplier via Seller 91](#_Toc232862087)

[4.3.9.1 Create Outbound Delivery 91](#_Toc232862088)

[4.3.9.2 Perform Picking and Post Goods Issue 92](#_Toc232862089)

[4.3.9.3 Create Supplier Credit Memo 94](#_Toc232862090)

[5 Appendix 96](#_Toc232862091)

[5.1 Process Integration 96](#_Toc232862092)

[5.2 Scheduling Job (Alternative) 96](#_Toc232862093)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 96](#_Toc232862094)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 97](#_Toc232862095)

[5.2.3 Job Scheduling for Billing Creation (Alternative) 98](#_Toc232862096)

[5.2.4 Job Scheduling for Billing Release (Alternative) 99](#_Toc232862097)

[5.2.5 Job Scheduling for Billing Output (Alternative) 100](#_Toc232862098)

[5.3 Succeeding Processes 101](#_Toc232862099)

## Purpose

Overview

This scope item covers three customer return scenarios:

1.) Return to seller: A returns order is created (optionally with reference to the original billing document or sales document). Once saved, a returns delivery is automatically generated. After goods receipt, the inspection takes place at the warehouse. The user can influence when the refunding documents are created: either directly, when releasing the returns order, or after the inspection. Finally, the user can decide on the compensation type for the customer: either shipping a replacement or paying a credit memo.

2.) Return to seller with inspection at customer site: The seller decides to perform the inspection at the customer site before initiating a physical return.

3.) Return to supplier via seller: After inspection at seller, the products should be shipped back to supplier. The supplier decides on the refund towards the seller, while the seller decides on the compensation towards the customer.

The progress of the return process can be monitored using returns overview.

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Master Data, Organizational Data, and Other Data

This table provides the master data used for the current baseline.

Essential master and organizational data were created in your SAP S/4HANA Cloud Public Edition system in the implementation phase, such as the data that reflect the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics. |

Check your SAP system to find out which other material master data exists.

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. |

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No Serial no.; no batch. |  |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No Serial no.; no batch. |  |
| Material | TG10 | Trad.Good 10,PD,Third PartyNo Serial No.; no batch. |  |
| Material | TG13 | Trading Good for Regular Trading (reorder point planning) with item category group CBNANo batch. |  |
| Material | TG14 | Trad.Good 14,PD,Bought-In,H14Trading material with item category group CBUK (bought in item)No batch. |  |
| Material | CM-FL-V00 | Forklift | Only use if you have activated Make-to-Order Production with Variant Configuration (1YT) scope item. |
| Material | TG20 | Trading Good for Reg. Trading (reorder point planning) |  |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO |  |
| Sold-to Party | 3310000333100001 | Domestic UAE Customer 3Domestic UAE Customer 1 |  |
| Ship-to Party | 3310000333100001 | Domestic UAE Customer 3Domestic UAE Customer 1 |  |
| Payer | 3310000333100001 | Customer domestic 03Domestic UAE Customer 1 |  |
| Supplier | 33300006 | Domestic UAE Supplier 6 |  |
| Plant | 33103320 |  |  |
| Storage Location | 331A332A331R |  |  |
| Shipping Point | 3310331R |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| Plant | 3320 |  | Serves for cross-plant material replacement functionality |
| Storage Location | 332A |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Before running BKP - Customer Returns, complete all activities in test script BD9 using master data, which is listed in the previous section [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 7 and note down the created document numbers of sales order and billing document for further use. |
| BD3 - Sales Processing using Third-Party with Shipping Notification | Before running BKP - Customer Returns, complete all activities in test script BD3 using master data, which is listed in the previous section [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 7 and note down the created document numbers of sales order and billing document for further use. |
| BDK - Sales Processing Using Third-Party Without Shipping Notification | Before running BKP - Customer Returns, complete all activities in test script BDK using master data, which is listed in the previous section [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 7 and note down the created document numbers of sales order and billing document for further use. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Before running BKP - Customer Returns, complete all activities in test script BDN using master data, which is listed in the previous section [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 7 and note down the created document numbers of sales order and billing document for further use. |
| BKA - Free Goods Processing | Before running BKP - Customer Returns, complete all activities in test script BKA using master data, which is listed in the previous section [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 7 and note down the created document numbers of sales order and billing document for further use. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1830e6c7b31ea8b1f697a83f6ed7a12e)

### Preliminary Steps

#### Create Info Records

Purpose

This process step shows you how to create info records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen displays. |  |
| 3 | Open New Purchasing Info Records | Choose Create on the right corner of the screen. | The New Purchasing Info Record screen displays. |  |
| 4 | Enter Header Data | Go to Header tab, make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300006Material: TG11Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Go to Delivery and Quantity tab, and make the following entries:Delivery Time in Days: <Delivery Time>, for example, <1>Under Delivery Tolerance in %: <Under Delivery Tolerance>, for example, <10>Over Delivery Tolerance in %: <Over Delivery Tolerance>, for example, <10>Tax Code: <Input Tax Code>Tax Rate Valid From: For example: TodayOrder Unit: <Order Unit>, for example, <PC>Standard Order Quantity: <Standard Order Quantity>, for example, <1>On the lower right, and lower left sides of the screen, check the following entry boxes if necessary:Unlimited Delivery: <Checked>Goods-Receipt-Based Invoice Verification: <Checked>No Evaluated Receipt Settlement: <Checked>Order Acknowledgment Requirement: <Checked> | Delivery and Quantity data is added. |  |
| 6 | Enter Condition Data | Go to Conditions tab, choose Create. Enter the following data:Valid From: <Valid from Date>Amount: 10Pricing Unit: <Pricing Unit>, for example, <1>Valid to: <Valid to Date>Currency: AEDChoose Apply. | Condition data is added. |  |
| 7 | Save | Choose Save. | You saved a Purchasing Info. Record. |  |
| 8 | Repeat the Same Steps and Create Three New Info Records | Repeat the same steps and create three new info records with below two sets of master data:Supplier: 33300006, Material: TG10Supplier: 33300006, Material: TG13Supplier: 33300006, Material: TG14Supplier: 33300006, Material: TG12Supplier: 33300006, Material: TG20Supplier: 33300006, Material: TG21 |  |  |

Result

The purchasing info records are created.

#### Set Initial Stock for Material

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). It only displays this way if it was your last transaction. So the action for the user should be to select Reference Document for MIGO Transaction > Other. | The Goods Receipt Other screen displays. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : TG10, TG11, TG12, TG13, TG14 TG20 , TG21 |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: <Enter a Plant>Storage Location: <Enter a Storage Location> |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post. |  |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

#### Maintain Returns Supplier

Purpose

To enable shipping processing is carried out for supplier return, mark the supplier as returns supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Maintain Business Partner (BP). | Maintain Business Partner screen displays. |  |
| 3 | Open BP | Go to menu path Business Partner > Open.In dialog box Open business partner, maintain the following data and choose Enter:Business Partner: 33300006 | Display Organization screen appears. |  |
| 4 | Change BP Role | Choose Supplier in Display in BP role field.Note The technical key of this BP role is FLVN01. |  |  |
| 5 | Open Purchasing Organization Data | Choose Purchasing at the top of the screen. | Purchasing Organization screen appears. |  |
| 6 | Enter Purchasing Data | Choose the following data and choose Transfer:Purchasing Organization: 3310 |  |  |
| 7 | Switch to Change Mode | Follow the menu path Business Partner > Display > Change to switch change mode. |  |  |
| 8 | Set Supplier as Returns Supplier | Choose Purchasing Data tab, scroll down to Additional Purhasing Data sub-area, set flag in checkbox Returns Supplier. | Dialog box Customer Default Data appears. |  |
| 9 | Map Supplier to Customer | Deselect checkbox Current Customer.Enter 33100006 in field BusinessPartner and choose Okay.Choose Continue to confirm Customer Successfully Mapped information. |  |  |
| 10 | Save | Choose Save.Choose OK to close information dialog. |  |  |

|  |
| --- |
| Note If error message Customer XX can not be mapped as it does not have sales area YY appears when ticking Returns Supplier checkbox, assign the relevant sales area to the customer in the Sales and Distribution screen of the effected business partner.For more details, please refer to SAP note[2943152](https://me.sap.com/notes/2943152). |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

#### Preliminary Steps for Returns Order Approval (Optional)

##### Define and Assign Approval Reasons

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define and assign approval reasons.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Choose Configure Your Solution | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter selection criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Basic Functions | All entries display in All Items section. |  |
| 5 | Navigate to Details | Find the entry with item name Document Approvals and choose arrow at the item end. | Configure Your Solution – Document Approvals screen displays. |  |
| 6 | Navigate to Details | In Configuration Steps section, choose Configure in column Actions for step Define Reasons for Approval Requests. | Change View “Define Reasons for Approval Requests”: Overview screen displays. |  |
| 7 | Define Approval Reason | Choose New Entries, make the following data and choose Save.Approval Request Reason ID:for example: ZRE1Approval Request Reason: for example: Returns | Approval reason is defined. |  |
| 8 | Navigate to Details | In Configuration Steps section, choose Configure in column Actions for step Assign Reasons for Approval Requests. | Change View “Assign Reasons for Approval Requests”: Overview screen displays |  |
| 9 | Assign Approval Reason | Choose New Entries, make the following data and choose Save.Document Category: HApproval Request Reason: for example: ZRE1 | Approval reason is assigned to Returns. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Reasons for Approval Requests | Go to the Business Processes Configuration app and search for the following activity: Define Reasons for Approval Requests.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Display View "Define Reasons for Approval Requests": Overview screen displays. |  |
| 3 | Define Approval Reason | Choose New Entries, make the following data and choose Save.Approval Request Reason ID:for example: ZRE1Approval Request Reason: for example: Returns | Approval reason is defined. |  |
| 4 | Open Assign Reasons for Approval Requests | Go to the Business Processes Configuration app and search for the following activity: Assign Reasons for Approval Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Display View "Assign Reasons for Approval Requests": Overview screen displays. |  |
| 5 | Assign Approval Reason | Choose New Entries, make the following data and choose Save.Document Category: HApproval Request Reason: for example: ZRE1 | Approval reason is assigned to Returns. |  |

##### Implement Cloud BADI

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Business Add-In (BAdI) SD_APM_SET_APPROVAL_REASON is called whenever a sales document is saved by a business user. It determines whether a sales document needs to be sent to an approver and, if so, sets an approval request reason on sales document header level.

This means that if you want to use the workflow for the approval of sales documents, implementing this BAdI is a prerequisite. In the Manage Sales Document Workflows app, you then define additional preconditions and approval steps.

When the system sets an approval request reason for a sales document, the approval workflow is triggered automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Custom Logic (F6957). | The Custom Logic screen displays. |  |
| 3 | Search for Implementations | On the top search bar, enter the below data and choose Go. Choose Filters to the field Extension Point ID visible if hidden.Extension Point ID: SD_APM_SET_APPROVAL_REASONIf the implementation does not exist, perform steps 4 and 5, otherwise directly execute step 5. |  |  |
| 4 | Create New Implementation | Choose Create, and search for the below data:Extension Point: SD_APM_SET_APPROVAL_REASONSelect above extension point and choose Step 2. Add the filter if needed.Choose Step 3 and make following entries:Implementation Description: Set Approval Request Reasons for Sales DocumentsImplementation ID: for example, YY1_SETAPPROVALREQUESTREASONChoose Review.Choose Create.Choose Publish.Choose Back. | New implementation is created. |  |
| 5 | Maintain Code | Choose the implementation row, and choose Open Code Editor.On the left Published Code area, choose Edit. Maintain your code for returns order and choose Save and Publish.for example:Sample Codeif salesdocument-sddocumentcategory = 'H' and salesdocument-totalnetamount > 1000. salesdocapprovalreason = 'ZRE1'. endif. |  |  |

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain the teams and responsibilities for returns order workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create a New Team | Choose Create. | The New Team screen displays. |  |
| 4 | Enter General Information | Make the following entries and press enter.Name: SD_RETURN_APPROVALDescription: Customer Return ApprovalStatus: EnabledType: SALES |  |  |
| 5 | Add Team Members | On the Team Members tab, choose Create.From the Items section, select the following Business Partner and choose OK.Last Name: SalesManager |  |  |
| 6 | Add Function to Team Members | Choose F4 in the Functions field. From the Select: Functions window, choose the appropriate entries and choose OK, for example:CMR1LVLA |  |  |
| 7 | Create | Choose Create. | User created a new team and appropriate function(s) have been assigned to the business user(s) to be configured as approver(s). |  |

##### Set Up Workflow

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Document Workflows (F3014). | The Workflows screen displays. |  |
| 3 | Create Workflow | Choose Workflow for Customer Returns next to Workflows.Choose Create. | The New Workflow window displays. |  |
| 4 | Maintain General Data | Make the following entry.In the Header tab,Workflow Name: Customer Returns Workflow |  |  |
| 5 | Set Preconditions | In the Start Conditions area, make the following entry and press Save.Start Conditions: Sales documents type is CBAR | Precondition is set. |  |
| 6 | Add Step | In the Steps section, choose Create. | The New step screen displays. |  |
| 7 | Enter Details | Make the following entries:In the Header tab:Step Name: Returns Order ApprovalStep Type: Release of Customer ReturnAssignment By: RoleRole: Customer Return Approver - Level 1Step to be completed by: One of the recipientsIn the Exception Handling tab:Required Action: Rework of Customer ReturnAction Result: Restart workflowChoose Create.Choose Save.Choose Activate. | Workflow is created and activated.Note System supports multiple-level approval, you can add more steps to design different roles to approve returns order with Step Conditions. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Scenario 1: Goods are Returned to Seller |  |  |  |
| [Create Returns Order](#unique_18) [page ] 26 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Returns order is created. |
| [Process Returns Order Approval (Optional)](#unique_19) [page ] 33 |  |  |  |
| [Withdraw from Approval](#unique_20) [page ] 33 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Returns order is withdrawn for further change before approval. |
| [Approve/Reject/Rework Returns Order](#unique_21) [page ] 34 | Sales Manager | My Inbox (F2097) | Approval decision is made. |
| [Rework Returns Order](#unique_22) [page ] 36 |  |  |  |
| [Check the Notifications](#unique_23) [page ] 36 | Returns and Refund Clerk | My Inbox (F2097) |  |
| [Change Returns Order](#unique_24) [page ] 37 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Returns order is changed. |
| [Release the Reworked Returns Order](#unique_25) [page ] 37 | Sales Manager | My Inbox (F2097) | The reworked returns order is released. |
| [Execute Picking](#unique_26) [page ] 38 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done for the returns delivery. |
| [Post Goods Receipt](#unique_27) [page ] 39 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted for returns delivery. |
| [Perform Material Inspection](#unique_28) [page ] 40 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Determine Refund](#unique_29) [page ] 42 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Refund determination is checked or triggered. |
| [Display Returns Overview](#unique_30) [page ] 44 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Document flow is displayed. |
| Refund Customer with Credit Memo |  |  |  |
| [Create Credit Memo](#unique_31) [page ] 45 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| Refund Customer with Replacement Product |  |  |  |
| [Create Free-of-Charge Delivery](#unique_32) [page ] 48 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Replacement delivery is created. |
| [Execute Picking](#unique_33) [page ] 49 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done. |
| [Post Goods Issue](#unique_34) [page ] 50 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue is posted for delivery. |
| [Create Pro-forma Invoice](#unique_35) [page ] 52 | Billing Clerk | Create Billing Documents (F0798) | Pro-forma invoice is created. |
| [Create Customer Invoice](#unique_36) [page ] 54 | Billing Clerk | Create Billing Documents (F0798) | Customer invoice is created. |
| Send Back to Customer |  |  |  |
| [Execute Picking](#unique_37) [page ] 56 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Posting Goods Issue](#unique_38) [page ] 57 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| Scenario 2: Goods are Inspected at Customer Site |  |  |  |
| [Create Returns Order](#unique_39) [page ] 58 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Return sales order is created. |
| [Change Returns Order](#unique_40) [page ] 59 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Inspection result is recorded, subsequent document is created for some cases. |
| Refund Customer with Credit Memo |  |  |  |
| [Create Credit Memo](#unique_41) [page ] 62 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| Refund Customer with Replacement Product |  |  |  |
| [Create Free-of-Charge Delivery](#unique_42) [page ] 64 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery free of charge is created. |
| [Execute Picking](#unique_43) [page ] 65 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done. |
| [Post Goods Issue](#unique_44) [page ] 66 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue is posted for delivery. |
| [Create Pro-forma Invoice](#unique_45) [page ] 68 | Billing Clerk | Create Billing Documents (F0798) | Pro-forma invoice is created. |
| [Create Customer Invoice](#unique_46) [page ] 69 | Billing Clerk | Create Billing Documents (F0798) | Customer invoice is created. |
| [Initiate Normal Return](#unique_47) [page ] 71 |  |  |  |
| Scenario 3: Goods are Returned to Supplier via Seller |  |  |  |
| [Create Returns Order](#unique_48) [page ] 72 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) |  |
| [Execute Picking](#unique_49) [page ] 75 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done for the returns delivery. |
| [Post Goods Receipt](#unique_50) [page ] 76 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted for returns delivery. |
| [Perform Material Inspection](#unique_51) [page ] 77 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection result is recorded, subsequent material document is created. |
| [Determine Refund](#unique_52) [page ] 78 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Refund decision is made. |
| [Display Returns Overview](#unique_53) [page ] 80 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Document flow is displayed. |
| Refund Customer with Credit Memo (Option A) |  |  |  |
| [Create Credit Memo](#unique_54) [page ] 81 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| Refund Customer with Replacement Material (Option B) |  |  |  |
| [Create Free-of-Charge Delivery](#unique_55) [page ] 84 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Replacement delivery is created. |
| [Execute Picking](#unique_56) [page ] 85 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue is posted for delivery. |
| [Post Goods Issue](#unique_57) [page ] 86 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue is posted for delivery. |
| [Create Pro-forma Invoice](#unique_58) [page ] 87 | Billing Clerk | Create Billing Documents (F0798) | Pro-forma invoice is created. |
| [Create Customer Invoice](#unique_59) [page ] 89 | Billing Clerk | Create Billing Documents (F0798) | The outbound delivery is created. |
| Return Goods to Supplier via Seller |  |  |  |
| [Create Outbound Delivery](#unique_60) [page ] 91 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | The outbound delivery is created. |
| [Perform Picking and Post Goods Issue](#unique_61) [page ] 92 | Shipping Specialist | Change Outbound Delivery (VL02N) | The outbound delivery is posted. |
| [Create Supplier Credit Memo](#unique_62) [page ] 94 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Credit memo invoice receipt is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around example, 60 minutes. The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as: Apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

- Log on to the SAP Fiori Launchpad using the respective user example, Internal Sales Representative.
- Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your search criteria and choose the business object type, example: Customer Returns from dropdown menu in first field, enter customer returns order number in second field and choose Search, The sales order is listed.
- Choose the sales order number link, the system navigates to fact sheet screen and returns order-related information is integrated and summarized in one Fiori page. You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects (Visible depending on the assigned role):

- Sales (return) order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Scenario 1: Goods are Returned to Seller

#### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order.

|  |
| --- |
| Note This chapter mainly introduces follow-up activity 0001 - Receive into Plant after which material inspection needs to be performed for further inventory movement of returned materials. If you can specify the final destination of the returned materials when creating returns order and expect to skip subsequent material inspection chapter, just choose one alternatively from below:* 0002 - Immediately Move to Free Available Stock* 0003 - Immediately Move to Scrap* 0014 - Immediately Move to Specified StockWith above follow-up activities 0002, 0003, or 0014, it is mandatory to maintain inspection result in returns order. Once return order is saved and released (if relevant to returns order approval, need to process returns order approval), returns delivery, picking and goods receipt will be generated automatically in background, next run the refund relevant steps:[Determine Refund](#unique_29) [page ] 42[Display Returns Overview](#unique_30) [page ] 44Refund Customer with Credit Memo or [Refund Customer with Replacement Product (Option B)](#unique_64) [page ] 47 |

Prerequisite

You must have billing document or sales order as reference (refer to [Business Conditions](#unique_6) [page ] 9).

|  |
| --- |
| NoteValuation of Returned Product with Reference to SalesGenerally returned product is valuated based on price of material master data, user has the option to activate the functionality of valuating the returned product with reference to preceding sales process with below steps:Depending on your environment in SAP S/4HANA Cloud Public Edition, use SSCUI 106396 in SAP Fiori Launchpad or configuration activity Configure Returns Order Type for Standard Return in SAP Central Business Configuration to activate the function of Valuation with Reference to Sales for CBAR order type.Mark checkbox Valuate with Reference as X in app Manage Customer Returns - Version 2 (F4832).Optional: You can enable Valuate with Reference as default value on plant level via SSCUI 106585 in SAP Fiori Launchpad or configuration activity Define Default Values for Customer Returns Apps, it will accelerate the user input when creating returns order in app Manage Customer Returns - Version 2 (F4832).Suspend ValuationGenerally, you take over the product ownership from the customer and the product is valuated when you refund a customer with either a replacement or a credit memo. There may be scenarios where you want to refund the customer but do not expect the refund to signal the decision on the ownership because the product inspection has not been completed yet. In such cases, perform the following steps to suspend product valuation until final logistical follow-up activity is confirmed in product inspection.Depending on your environment in SAP S/4HANA Cloud Public Edition, use SSCUI 106396 in SAP Fiori Launchpad or configuration activity Configure Returns Order Type for Standard Return in SAP Central Business Configuration to activate the function of suspending product valuation.Check the checkbox Suspend Valuation of the returns item of CBAR order which is created via app Manage Customer Returns - Version 2 (F4832)Optional: You can enable Suspend Valuation as default value on plant level via SSCUI 106585 in SAP Fiori Launchpad or configuration activity Define Default Values for Customer Returns Apps, it will accelerate the user input when creating returns order in app Manage Customer Returns - Version 2 (F4832).Automatic Inspection After Goods ReceiptProduct inspection is normally mandatory in customer returns after goods receipt. You need to manually input material inspection result and confirm your logistical follow-up activity. You have option to skip the manual material inspection by automating it, with different business reasons, such as:Returned product inspection is processed out of standard customer returns.Migrate your returns solution from lean return (BDD - product inspection is not required) to customer returns (BKP - product inspection is expected).Inspection result is available and logistical follow-up can be decided earlier before product is received.Perform the following steps to activate automatic inspection in CBAR order creation:Depending on your environment in SAP S/4HANA Cloud Public Edition, use SSCUI 106396 or configuration activity Configure Returns Order Type for Standard Return in SAP Central Business Configuration to activate the function of automatic inspection.Check the checkbox Automatic Inspection After Goods Receipt, maintain field inspection code and next follow-up activity of the returns item of CBAR order created via app Manage Customer Returns - Version 2 (F4832).Optional: You can enable Automatic Inspection as default values on plant level via SSCUI 106585 in SAP Fiori Launchpad or configuration activity Define Default Values for Customer Returns Apps, it will accelerate the user input when creating returns order in app Manage Customer Returns - Version 2 (F4832). |

|  |
| --- |
| Note For configurable material, e.g.: CM-FL-V00, BKP supports the return process with limitation including variant configuration not visible in CBAR/GA2 order.Recommend you to activate and run scope item 7KW - Customer Returns for Material with Variant Configuration.If scope item 7KW is not activated in your system yet and you want to run BKP for configurable material return process as workaround, please manually maintain default item categories for below entries in SSCUI 102807 - Assign Item Categories before you create returns order:Sales Document TypesItem Category GroupDefault Item CategoryCBAR0002RENVGA20002GAN2 |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832).Note For serial number managed material TG20 , use app Manage Customer Returns (F2651) to create returns order in which serial number functionality is enabled. | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Create Returns Order | Choose Create with Reference, then choose Create from Invoice.System also supports to create CBAR order for below cases:From sales order: click Create with Reference, then choose Create from Sales Order.From sales order without charge: click Create with Reference, then choose Create from Sales Order Without Charge.No Reference: click Create. | The Create from Invoice pop-up screen displays. |  |
| 4 | Maintain Data | Enter the following data and then choose Select Items.Returns Order Type: Standard Return (CBAR)Invoice: Billing document number created previously |  |  |
| 5 | Maintain Returned Quantity | Select the item(s) to be returned and enter the return quantity, then choose Continue. |  |  |
| 6 | Enter Data | Under tab General Information, enter the following data:Return Order Reason: for example, Standard Return (009)Under tab Items, choose the arrow button at the end of the item, and enter the following data.In section Product:Return Reason: for example, Product damaged (003)In section Follow-up Activity:Follow-up Activity: for example, Receive into Plant (0001)Only for material TG21:In section Item DataBatch: <Batch number>Note Optional: System recommends defaulted values in some mandatory fields if there are over 3000 returns items existing for return document type CBAR.For example: Returns Order Reason.For more information, refer to chapter Create Return Orders with Recommendations in scope item 73P - Sales Order Automation. |  |  |
| 6a | Optional: | In section Follow-up Activity, set the flag in the following checkboxes if you need to activate corresponding functionalities. For more information, refer to the prerequisite part.Value with Reference: XAutomatic Inspection After Goods Receipt: XIn section Refund, set the flag in the following checkbox if you need to suspend product valuation. For more information, refer to the prerequisite part.Suspend Valuation: X |  |  |
| 7 | Choose One of the Following Options | The user can influence the point in time when the refunding document must be created: Either immediately when the returns order is saved and released or at a later point of time. Combination of the refund setting determines follow-up document creation. Choose one among the following options to continue:Note If item category is RBPN - Ret Foc Proforma, directly choose option 8 - No Refund. |  |  |
| 7a | Option 1: Execute Refund with Credit Memo Request Immediately | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Credit MemoRefund Code: <select one from down-drop list>, for example, 10%.Note Refund deduction (condition type DRE1) is determined automatically based on the refund code entered.The following steps guides you how to define more refund codes and related condition records:Define returns refund codes via SSCUI 104235Maintain condition records for DRE1 using the Set Material Prices – Sales app. For more details, refer to master data script Create Sales Pricing Condition - MDS (BET).Refund Control: Create Credit Memo RequestChoose Save and Release. | returns order is created.Note If returns order approval is not triggered, returns delivery is generated automatically.Otherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 7b | Option 2: Execute Refund with Replacement Order Immediately | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Replacement ProductRefund Control: Create Replacement OrderChoose Save and Release. | Returns order is created.Note If returns order approval is not triggered, returns delivery is generated automatically.Otherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 7c | Option 3: Refund on Hold, Choose Credit Memo as Temporary Refund Type | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Credit MemoRefund Code: <Select one from down-drop list>, for example, 10%.Refund Control: Decide LaterChoose Save and Release. | Returns order is created.Note If returns order approval is not triggered, returns delivery and credit memo request are generated automatically.Otherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 7d | Option 4: Refund on Hold, Choose Replacement Product as Temporary Refund Type | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Replacement ProductRefund Control: Decide LaterChoose Save and Release. | Returns order is created.Note If returns order approval is not triggered, returns delivery and credit memo request are generated automatically.Otherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 7f | Option 6: Execute Refund with Credit Memo | Enter the following data or action then choose Apply:In the Follow-Up Activity section:Product Received: XIn the Refund section:Refund Type: Credit MemoRefund Code: 10% (select from dropdown list)Refund Control: Create Credit Memo | Returns order is created.If returns order approval is not triggered, subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryCredit memoOtherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved.Next please complete the following chapter:[Process Returns Order Approval (Optional)](#unique_19) [page ] 33[Perform Material Inspection](#unique_28) [page ] 40 |  |
| 7g | Option 7: Execute Refund with Immediate Delivery | Enter the following data or action then choose Apply:In the Follow-up Activity section:Product Received: XIn the Refund section:Refund Type: Replacement ProductRefund Control: Immediate Delivery | Returns order is created.If returns order approval is not triggered, subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryReplacement order (SDF)Outbound delivery for replacement order (SDF)Goods Issue for SDFNext please complete the following chapter:[Process Returns Order Approval (Optional)](#unique_19) [page ] 33[Perform Material Inspection](#unique_28) [page ] 40Refund Customer with Replacement Material – Create Pro-forma InvoiceRefund Customer with Replacement Material – Create Customer Invoice |  |
| 7h | Option 8: No Refund | Enter the following data or action, then choose Apply:In the Refund section:Refund Control: No RefundChoose Save and Release. | Returns order is created.Note If the approval process of returns order is not triggered, returns delivery will be generated automatically.If the approval process is triggered, the returns order status will change to:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 8 | Check Process Flow | Under the Process Flow tab, check dependent documents in process flow. Make a note of the follow-up document numbers for further use. | The Display Returns Order screen displays. |  |

|  |
| --- |
| Note If freight was maintained in previous delivery document header and material was partly returned regarding billing document, please check (or change if necessary) freight amount for condition type YBHD in the header(s) of returns order (and credit memo request document if it is generated automatically) using the role Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP) and the Change Sales Order tile.If requested delivery date is reached and delivery document has not been created, warning information delivery issue will show in process flow as a reminder. Once delivery document is generated later, such alert will disappear. |

#### Process Returns Order Approval (Optional)

|  |
| --- |
| Note Only relevant if below conditions are fulfilled:Preliminary steps of returns order approval are performed, details see chapter [Preliminary Steps for Returns Order Approval (Optional)](#unique_12) [page ] 15.Total amount of the returns order is not less than 1000. |

##### Withdraw from Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, returns order creator withdraws the returns order waiting for approval and do some necessary change.

Prerequisites

The approver doesn’t approve returns order which keeps In Approval as approval status.

Procedure

| Test Step # | Test Step Name | Instruction | Pass / Fail / Comment |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |
| 3 | Withdraw and Edit Returns Order | Find your returns order with approval status In Approval.Choose the arrow at end of the return order to navigate to Returns Order screen, choose Withdraw Approval Request.Message The approval request for sales document 6XXXXXXX was withdrawn appears, choose Close to confirm the message.Choose Edit and do necessary change in editable fields.Choose Save and Release. | Approval status is changed to In Approval. |

##### Approve/Reject/Rework Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, sales manager makes approval decision: release, reject or request rework.

Prerequisites

Approval status of the returns order is In Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox (F2097).Note You can also choose Notifications on top-right corner to navigate to My Inbox screen. | The My Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve/Reject/Rework Returns Order | You receive the notification of the returns order. Choose one from the following options, enter the comment if necessary.Option 1: ReleaseOption 2: RejectOption 3: Request rework | The dialog box Submit Decision displays. |  |
| 5 | Submit | Enter some comments and choose Submit.Based on above decisions, choose next steps accordingly:Release:Returns delivery is generated, credit memo request/replacement order is created automatically if the field Refund Control is set as Create Credit Memo Request or Create Replacement Order in [Create Returns Order](#unique_18) [page ] 26, next perform [Execute Picking](#unique_26) [page ] 38.Reject: the whole process ends, no subsequent step is needed.Request Rework: go to the next chapter. |  |  |

##### Rework Returns Order

|  |
| --- |
| Note Only relevant if the workflow is set as request rework by sales manager previously. |

###### Check the Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the notifications.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox (F2097). | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Check Inbox | Check the inbox items with relative returns order. | Orders which need to be reworked are displayed.If rework is not required, returns clerk can set Rework not Required in the inbox.If rework is required, go to next chapter . |  |

###### Change Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, returns order creator changes the returns order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Enter search terms in the filter bar, and choose Go.For example: enter returns order number in Returns Order field. | Returns order is displayed in result list. |  |
| 4 | Navigate to Returns Order Screen | Choose the arrow at the end of the returns order.Choose Edit. |  |  |
| 5 | Change Returns Order | Under the Items tab, make the following entry:Order Quantity: <Quantity>, for example, 50 |  |  |
| 6 | Save | Choose Save and Release. |  |  |

###### Release the Reworked Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, sales manager releases the reworked returns order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | You will receive a notification in the notification section.Choose My Inbox (F2097) app to proceed to the notification or click on the notification in the notification section. | The My Inbox window displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed |  |
| 4 | Approve | You will receive the notification of the reworked returns order. Choose Release and enter the comment if necessary.Choose Submit. | The reworked returns order is released. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, picking is done for returns delivery created previously. This process step shows you how to perform picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 331R |  |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, input quantity equal to delivery quantity in the Picked Qty field. |  |  |
| 7 | Maintain Serial Number(Optional) | For TG20, maintain serial numbers via menu path Extras > Serial Numbers . |  |  |
| 8 | Choose Enter | Press Enter. |  |  |
| 9 | Save | Choose Save. | The delivery is picked. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received, goods receipt is posted for returns delivery. This process step shows you how to post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Goods Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 331R. |  |  |
| 5 | Post Goods Receipt | Mark the relevant delivery and choose Post Goods Issue. Choose date of today from the dialog box. | The goods receipt is posted. |  |

#### Perform Material Inspection

The material inspection takes place after the returned goods have been received in the warehouse. The further handling of the returned goods is decided.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material inspection takes place after the returned goods have been received in the warehouse. The further handling of the returned goods is decided. This process step shows you how to perform material inspection.

Prerequisite

The returned goods are received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Delivery Items Waiting for Inspection: <select>Delivery: <enter returns delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item Tab | Choose Item tab. |  |  |
|  | Inspection Split (Optional) | If different inspection results need to be recorded for the same delivery item, perform below actions, otherwise you can directly skip this step.Select the delivery item and choose Create Split Item, then run steps 5-6 for all inspection items. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data, and press Enter:Inspection Code: <enter inspection code>Inspected Quantity: <enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm.For Send back to customer scenario, Inspection Code: 0004 Decision not possible. |  |  |
| 6 | Maintain Follow-up Activity | In the Logistical Follow-up subarea, enter the following data and press Enter:Follow-up Activity: <enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001.Choose suitable Follow-Up Activity from below options according to your subsequent scenarios:0011 Transfer to Free Available Stock0012 Transfer to Scrap0015 Transfer to Specified Stock0018 Transfer to Scrap for Customer0021 Send Back to Customer0023 goods receipt quantity correction |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection Status shows Inspected, which means all received materials are inspected completely. | All received materials are inspected completely. |  |
| 8 | Save and Confirm | In menu bar at the top of screen, choose Save and Confirm.Note Do not choose Save Inspection Results at the bottom right of the screen, as subsequent material documents will not be automatically generated. | Inspection result is recorded, and goods movement is posted accordingly. |  |

|  |
| --- |
| Note If you want to perform in-house repair process for returned product, complete below activities:Activate the scope item In-House Repair.Refer to In-House Repair, execute steps mentioned in chapter Create Returns Order and Returns Delivery (Option B). |

#### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, refund decision is made or checked: either refund the customer with a credit memo or compensate with a replacement product. For repair business, you may choose No Refund if no refund for customer.

Prerequisite

For cross-plant material replacement functionality, please ensure second organizational entities including plant 1020/shipping point 1020/storage location 102A and relevant assignment are set up correctly, detailed please see chapter [Additional Manual Configuration](#unique_7) [page ] 10.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar to add if it is hidden. Enter the following data and choose Go:Returns Order : <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the field Refund Progress and then take next action accordingly:<100%: Refund determination is not completed. Go to Section A and then Section B.100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund is determined with reference to product inspection results | Option 1: Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoRefund Code: <a percentage number>, for example, 10% RefundChoose OK.Select the item and choose Release Selected Items.Note For send back to customer scenario, enter the following data:Refund Type: No RefundCMR Rejection Reason: 59 Damaged by customer | Refund setting is maintained, and credit memo request document is created in background. |  |
| Section A: Refund is determined with reference to product inspection results | Option 2: Product Replacement | On the Items to Be Refunded tab, choose Change Refund in Refund Details column for the return item.Enter the following data:Refund Type: Replacement ProductReplacement Product: <Product>Supplying Plant: 3310 (same to returned plant) or 3320 (Second plant)Replacement Quantity: <Quantity> / PCChoose OKSelect the item and choose Release Selected Items.Note By default, replacement material is same to returned product and supplying plant is same to returned plant.System also supports cross-plant product replacement and different product replacement. | Refund setting is maintained, and replacement order document is created in background. |  |
| Section B: Check refund determination result | Check refund results | On the Completed Items tab, refund result is displayed. Follow-up document number is shown in Refund Details column. Make a note of document number for further use. You can click the created document number to check detailed information. | The refund result displays. |  |

#### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the progress of returns process. All dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Search for returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Order Overview | Click the created returns order number 6XXXXXXX and choose Display Customer Return. | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Document Flow | On Returns tab, choose Returns Overview in Returns Control area. | The Returns Overview for Returns Order 6XXXXXXX - 10 screen displays. |  |
| 6 | Check Document Flow | In Document Number column, make a note of follow-up document number(s) of credit memo request or replacement order (subsequent delivery free of charge) for further use.For send back to customer scenario, make a note of follow-up document number of Send Back to Customer/Outbound delivery for further use. |  |  |

|  |
| --- |
| Note After you have completed this activity:Option A: If credit memo request is generated, go to the Refund Customer with Credit Memo chapter.Option B: If replacement order is generated, go to the Refund Customer with Replacement Product chapter.Option C: If outbound delivery for sending back to customer is generated, go to the Send Back to Customer chapter. |

#### Refund Customer with Credit Memo (Option A)

##### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo.

Procedure

Table 3: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) display(s) in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Documents (F0798) screen displays. |  |
| 6 | Maintain Billing Type and Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Table 4: Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search Billing Document | Enter the billing document number recorded previously, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update new Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

#### Refund Customer with Replacement Product (Option B)

|  |
| --- |
| Note For product TG14 (with item category group CBUK – bought in item)By default, replacement product is directly provided to customer from seller’s stock, in the case of immediate refund with replacement order, system also supports you to manually switch item category to CBXB in the created replacement order which triggers sales order specific procurement. After receiving product from the supplier, seller send it as replacement product to customer.Complete the following chapters mentioned in Sales of Non-Stock Item with Order-Specific Procurement (BDN) test script using the master data listed below:Create Purchase OrderApprove and Release Purchase Order (Optional)Post Goods ReceiptEnter Vendor Invoice |

| Master Data | Sample Value |
| --- | --- |
| Material | TG14 |
| Supplier | 33300006 |

##### Create Free-of-Charge Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how a free-of-charge delivery is created with reference to replacement order.

Prerequisite

Replacement order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310 or 3320Planned Creation Date: <delivery selection date>Order: <replacement order number created previously> |  |  |
| 4 | Create Delivery | Select your items and choose Create Deliveries. |  |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to perform picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Data | Make the following entries, and choose Execute:Shipping Point: 3310 or 3320Only Picking without WM: <select the checkbox> |  |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking screen, select your delivery note and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, enter the following data:If batch spilt exists, choose Batch Split Exists to expand sub item(s): Picked Qty : <quantity equal to delivery Qty>If batch split doesn't exist, Picked Qty: <quantity equal to delivery Qty> |  |  |
| 7 | Maintain Serial Number(Optional) | For TG20, maintain serial numbers via menu path Extras > Serial Numbers . |  |  |
| 8 | Enter | Press Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been picked. |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Goods Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 3310 or 3320 |  |  |
| 5 | Post Goods Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date and choose Continue in the dialog box. | The goods issue is posted. |  |

Financial Postings

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Goods (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Deliveryscreen, enter the Delivery number and choose Continue. From the Delivery xxxxxxxx Display: Overview screen, choose More > Extras > Delivery Output > Output Control | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is posted. |  |

##### Create Pro-forma Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a pro-forma invoice with reference to delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Maintain the settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose the billing type Pro Forma Invoice for Delivery (F8)and billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save and billing date, such as the current date, and then choose. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Pro-forma invoice is generated. |  |

|  |
| --- |
| Note Alternatively, it is supported to create pro-forma (type F5) with reference to replacement order. |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search for Billing Document | Input the pro-forma invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 7 | Update New Text (optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |

##### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create ‘F2’ type of invoice, and transfer costs to accounting accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Keep the settings below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Invoice (F2) and maintain Billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Customer invoice is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 44002000Sales Disc Domestic | 41000000Rev Domestic Prod |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | Input the pro-forma invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel Billing Docs. | Log displayed: Billing Document Canceled. |  |
| 7 | Update New attachment (optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 8 | Update New Text (optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |

#### Send Back to Customer (Option C)

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to perform picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | For Picking | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Data | On the Outbound Deliveries for Picking screen, make the following entry:Shipping Point: 3310 |  |  |
| 5 | Select the Only Picking without WM checkbox and choose Execute | Select the Only Picking without WM checkbox and choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day’s Workload for Picking screen. Select your outbound delivery and choose Change Outbound Delivery. |  |  |
| 7 | Input Picked Quantity | On the Return to Customer xxxxxxxx change: Overview screen, choose Picking. Input quantity in the Picked Qty field. | Picking status is set to complete if picked quantity and delivery quantity is equal. Deviations in quantity can be solved by the function Copy Picked Quantity as Delivery Quantity. |  |
| 8 | Save Document | Choose Save. |  |  |

##### Posting Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. Choose today’s date and choose Continue in the dialog box. | The goods issue is posted. |  |

### Scenario 2: Goods are Inspected at Customer Site

Context

In this scenario, goods are inspected at customer site firstly, follow-up actions are taken depending on inspection result:

- Option 1: Customer complaint is unjustified; return is reject without refund; product remains at customer site.
- Option 2: Customer complaint is justified; seller refunds customer with credit memo; product remains at customer site.
- Option 3: Customer complaint is justified; seller refunds customer with replacement product; product remains at customer site.
- Option 4: Material status is unclear; material is returned to seller’s stock for further inspection; refund decision is made later: credit memo or replacement material.

#### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create return sales order, and material inspection is performed at customer site firstly.

Prerequisites

Goods were shipped to customer by seller or third-party supplier, sales order number, and billing document number are noted down.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Navigate to Customer Returns Screen | Choose Create with Reference, then choose Create from Invoice. | The Create from Invoice pop-up screen displays. |  |
| 4 | Maintain Data | Enter the following data and then choose Select Items.Returns Order Type: Standard Return (CBAR)Invoice: Reference billing document number | The Create from Invoice XXXXXXXXX pop-up screen displays. |  |
| 5 | Maintain Returned Quantity | Select the item(s) to be returned and enter the return quantity, then choose Continue. | The Returns Order screen displays. |  |
| 6 | Enter Data | Under tab General Information, enter the following data:Return Order Reason: for example, Standard Return(009)Under tab Items, choose the arrow button at the end of the item, and enter the following data.In section Product:Return Reason: for example, Product damaged (003)In section Follow-up Activity:Follow-up Activity: for example, Inspection at Customer Site (0008) |  |  |
| 7 | Save Returns Order | Choose Save. | Returns order is updated. |  |

|  |
| --- |
| Note If returns order approval is triggered, next complete returns order approval with reference to [Process Returns Order Approval (Optional)](#unique_19) [page ] 33. |

#### Change Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Inspection result at customer site is recorded, follow-up activity is specified, refund parameters are set. This process step shows you how to change returns order.

Prerequisites

Field sales representative went to customer site to perform inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden.Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Item Details | Choose the arrow at the end of the item. | The Returns Order screen displays. |  |
| 5 | Edit | On the right-top corner of screen, choose Edit. |  |  |
| 6 | Navigate to Item Details | Under Items tab, choose the arrow at the end of the item.Only for material TG21:In section Item DataBatch: <Batch number> | The Returns Order Item screen displays. |  |
| 7 | Choose One of the Following Options | According to inspection result and alignment with customer, choose one among the following options to continue: |  |  |
| 7a | Option 1: Customer complaint is unjustified, return is rejected without refund | Enter the following data under Follow-up Activities section:Follow-Up Activity: Product Remains at Customer Site (0013)Inspection Code: Not OKComment: <Meaningful texts>Choose Rejection Reason on the top right corner, then choose Set Rejection Reason. In Set Rejection Reason pop-up screen, make the following choice and choose Set Rejection Reason.Reason for Rejection: <Available reason>, for example, Rejected by Selling Company (62)Choose Apply.Choose Save and Release. | Returns order is released; refund requirement is refused; no further action will be taken. |  |
| 7b | Option 2: Customer complaint is justified, product remains at customer site, seller refunds customer with credit memo | Enter the following data and choose Apply.In section Follow-up Activity:Follow-Up Activity: Product Remains at Customer Site (0013)Inspection Code: Partly OKComment: <Meaningful texts>In section Refund:Refund Type: Credit MemoRefund Code: <select one from dropdown list>, for example, 10%Refund Control: Create Credit Memo RequestChoose Save and Release.On the Returns Order screen, under tab Process Flow, note down the follow-up document number of credit memo request for further use. | Returns order is released; credit memo request is generated automatically. Next execute the Refund Customer with Credit Memo chapter. |  |
| 7c | Option 3: Customer complaint is justified, product remains at customer site, seller refunds customer with replacement material | Enter the following data and then choose Apply.In the Follow-up Activities section, enter the following data:Follow-Up Activity: Product Remains at Customer Site (0013)Inspection Results: Not OKComments: <Meaningful texts>In the Refund section:Refund Type: Replacement ProductRefund Control: Create Replacement OrderChoose Save and Release.On the Returns Order screen, under tab Process Flow, note down follow-up document number of replacement order for further use. | Returns order is released, subsequent replacement order (SDF or delivery free of charge order) is generated automatically. Next execute the Refund Customer with Replacement Material chapter. |  |
| 7d | Option 4: Material status is unclear, material will be returned to seller’s stock for further inspection | Enter the following data and then choose Apply.In the Follow-up Activities section, enter the following data:Follow-Up Activity: Receive into plant (0001)Inspection Results: Decision not possibleInspected at Customer Site: <Select>Comments: <Meaningful texts>In the Refund section:Refund Type: Replacement Product or Credit MemoRefund Code: <choose one percentage number>, for example, 030 30% Refund if Credit memo is chosen as the refund type previously.Refund Control: Decide LaterChoose Save and Release.On the Returns Order screen, under tab Process Flow, note down subsequent returns delivery (Adv. Returns Delivery) number for further use. | Returns order is released, returns delivery is generated automatically. Next, execute the Initiate Normal Return chapter. |  |

#### Refund Customer with Credit Memo

##### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo from a credit memo request.

Prerequisite

Option 2 in [Change Return Order](#unique_40) activity is completed, credit memo request is created previously.

Procedure

Table 5: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Setting.Keep the settings below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Credit memo is generated. |  |

Table 6: Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search Billing Document | Enter the billing document number recorded previously in the Manage Billing Documents field and choose Enter. | The billing document created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the created Billing Document screen, go to the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

#### Refund Customer with Replacement Material

##### Create Free-of-Charge Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a free-of-charge delivery with reference to SDF (replacement order) document.

Prerequisite

Option 3 in activity 4.2.2 [Change Returns Order](#unique_40) [page ] 59 is completed, and subsequent free-of-charge delivery (replacement order) is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <delivery selection date>Order: <replacement order number created previously> |  |  |
| 4 | Create Delivery | Select your replacement order item(s) and choose Create Deliveries. |  |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to perform picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Only Picking without WM: <Check the checkbox> |  |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking screen, select your delivery note and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, enter the following data:If batch spilt exists, choose Batch Split Exists to expand sub item(s): Picked Qty : <quantity equal to delivery Qty>If batch split doesn't exist, Picked Qty: <quantity equal to delivery Qty> |  |  |
| 7 | Enter | Press Enter. |  |  |
| 8 | Save | Choose Save. | The delivery is picked. |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Goods Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping Point: 3310 |  |  |
| 5 | Post Goods Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date and choose Continue in the dialog box. | The goods issue is posted |  |

Financial Postings

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Goods (HAWA) | 54083000Consptn Trde Gds | 13600000Inventory TradingGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the Delivery number and choose Continue. From the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is posted. |  |

##### Create Pro-forma Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a pro-forma invoice with reference to delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose the billing type Pro Forma Invoice for Delivery (F8) and billing date, such as the current date, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Pro-forma invoice is generated. |  |

Alternatively, it is supported to create pro-forma (type F5) with reference to replacement order.

##### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create F2 type of invoice, and costs are transferred to accounting accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings .Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Invoice (F2) and maintain Billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | In the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Customer invoice is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 44002000Sales Disc Domestic | 41000000Rev Domestic Prod |

#### Initiate Normal Return

Purpose

In the case that material status is unclear after inspection at customer site, they will be returned to seller’s stock for further inspection, refund decision will be made later.

Prerequisite

Option 4 in the activity [Change Returns Order](#unique_40) [page ] 59 is completed, returns delivery is created previously.

Procedure

Complete the following activities described in the Scenario 1: Goods are Returned to Seller section:

- [Execute Picking](#unique_26) [page ] 38
- [Post Goods Receipt](#unique_27) [page ] 39
- [Perform Material Inspection](#unique_28) [page ] 40
- [Determine Refund](#unique_29) [page ] 42
- [Display Returns Overview](#unique_30) [page ] 44
- or

### Scenario 3: Goods are Returned to Supplier via Seller

|  |
| --- |
| Note To ensure supplier return is carried out using shipping processing, below data need to be maintained correctly before scenario 3 return process is run:Business Role IDAppInstructionsExpected ResultSAP_BR_BUPA_MASTER_SPECIALISTMaintain Business Partner (BP)Open BP 33300006 with BP role FLVN01 Supplier (defined), switch to Purchasing > Purchasing Data tab, in Additional Purchasing Data sub-area, set flag in checkbox Returns supplier. For details, please refer to [Maintain Returns Supplier](#unique_10) [page ] 13.Set flag Returns supplier in supplier master data.SAP_BR_BPC_EXPERTManage Your Solution (F1241)Maintain correct relationship between plant and sales organization / distribution channel via SSCUI 101926 or activity Define Shipping Data for Plants as below:Plant: 3310Sales Organization: 3310Distribution Channel: 10Sales organization and distribution channel are assigned to the plant. |

#### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order.

Prerequisites

You must have billing document or sales order as reference (refer to [Business Conditions](#unique_6) [page ] 9).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Create Customer Return with Reference | Choose Create with Reference, then choose Create from Invoice. | The Create from Invoice pop-up screen displays. |  |
| 4 | Maintain Data | Enter the following data and then choose Select Items.Returns Order Type: Standard Return (CBAR)Invoice: Reference billing document number | The Create from Invoice XXXXXXXXX pop-up screen displays. |  |
| 5 | Maintain Return Quantity | Select the item(s) to be returned and enter the return quantity, then choose Continue. | The Returns Order screen displays. |  |
| 6 | Maintain Data | Under tab General Information, enter the following data:Return Order Reason: for example, Standard Return(009)Under tab Items, choose the arrow button at the end of the item, and enter the following data.In section Product:Return Reason: for example, Product damaged (003)Customer Reference Date: inform the date in which customer return NF-e was issuedIn section Follow-up Activity:Follow-up Activity: for example, Ship to Supplier (0005)Supplier: 33300006Only for material TG21:In section Item DataBatch: <Batch number> |  |  |
| 7 | Choose One of the Following Options | The user can influence the point in time when the refunding document must be created. Either immediately when the returns order is saved and released or at a later point of time. Combination of the refund setting determines follow-up document creation. System provides four options for your reference. Choose one among them to continue: |  |  |
| 7a | Option 1: Execute Refund with Credit Memo Request Immediately | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Credit MemoRefund Control: Create Credit Memo RequestRefund Code: <select one from down-drop list>, for example, 10%.Choose Save and Release. | Returns order is created.Note If returns order approval is not triggered, returns delivery and credit memo request are generated automatically.Otherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 7b | Option 2: Execute Refund with Replacement Order Immediately | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Replacement ProductRefund Control: Create Replacement OrderChoose Save and Release. | returns order is created.Note If returns order approval is not triggered, returns delivery and replacement order are generated automatically.Otherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 7c | Option 3: Refund on Hold, Choose Credit Memo as Temporary Refund Type | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Credit MemoRefund Code: <Select one from down-drop list>, for example, 10%.Refund Control: Decide LaterChoose Save and Release. | Returns order is created.Note If returns order approval is not triggered, returns delivery is generated automatically.Otherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 7d | Option 4: Refund on Hold, Choose Replacement Product as Temporary Refund Type | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Replacement ProductRefund Control: Decide LaterChoose Save and Release. | Returns order is created.Note If returns order approval is not triggered, returns delivery is generated automatically.Otherwise, returns order status shows as below:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 7e | Option 5: No Refund | In the Refund section, enter the following data or action, then choose Apply:Refund Control: No RefundChoose Save and Release. | Returns order is created.Note If the approval process of returns order is not triggered, returns delivery will be generated automatically.If the approval process is triggered, the returns order status will change to:Approval status = In ApprovalRelease status = Not ReleasedSubsequent documents will be created after returns order is approved. |  |
| 8 | Check Process Flow | Under the Process Flow tab, check dependent documents in process flow. Make a note of the follow-up document numbers for further use. | The dependent document(s) display(s). |  |

If freight was maintained in previous delivery document header and material was partly returned regarding billing document, please check (or change if necessary) freight amount for condition type YBHD in the header(s) of returns order (and credit memo request document if it is generated automatically) using the role Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP) and the Change Sales Order tile. If requested delivery date is reached and delivery document has not been created, warning information delivery issue shows in process flow as a reminder. Once delivery document is generated later, such alert disappears.

|  |
| --- |
| Note If returns order approval is triggered, next complete returns order approval with reference to [Process Returns Order Approval (Optional)](#unique_19) [page ] 33. |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform picking for returns delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: for example, 331R. |  |  |
| 5 | Change Outbound Deliveries | On the Day's Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, input quantity equal to delivery quantity in the Picked Qty field. |  |  |
| 7 | Enter | Choose Enter. |  |  |
| 8 | Save | Choose Save. | The delivery is picked. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods receipt when the returned material is received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Goods Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: for example, 331R |  |  |
| 5 | Post Goods Receipt | Mark the relevant delivery and choose Post Goods Issue. Choose today’s date from the dialog box. | The goods receipt is posted. |  |

#### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform material inspection after the warehouse received the returned goods. The further handling of the returned goods is decided.

Prerequisite

The returned goods are received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Delivery Items Waiting for Inspection: <select>Delivery: <enter returns delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Item | Choose the Item tab. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data and press Enter:Inspection Code: <enter inspection code>Inspected Quantity: <enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Check Follow-up Activity | In the Logistical Follow-Up subarea, ensure the following data is maintained:Follow-Up Activity: 0005 Ship to SupplierSupplier : <enter Supplier>, for example, 33300006 |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection Status shows Inspected, which means all received materials are inspected completely. | All received materials are inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm. | Inspection result is recorded, and goods movement is posted accordingly. |  |

#### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to make or check a refund decision. You can either refund the customer with a credit memo or compensate him or her with replacement product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order : <returns order number 6XXXXXXX> | returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the field Refund Progress and then take next action accordingly:<100%: Refund determination is not completed. Go to Section A and then Section B.100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund is Determined with Reference to Material Inspection Results | Option 1: Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoRefund Code: <a percentage number>, for example, 10% refund.Choose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and credit memo request document is created in background. |  |
| Section A: Refund is Determined with Reference to Material Inspection Results | Option 2: Material Replacement | On the Items to Be Refunded tab, choose Change Refund in Refund Details column for the return item.Enter the following data:Replacement Product: <Material>Supplying Plant: <Plant>Replacement Quantity: <Quantity> / PCChoose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and replacement order document is created in background. |  |
| Section B: Check Refund Determination Result | Check Refund Results | On the Completed Items tab, refund result is displayed. Follow-up document number is shown in Refund Details column. Make a note of document number for further use. You can click the created document number to check detailed information. | The refund result displays. |  |

#### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the return process' progress. You may see all dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Order Overview Screen | Click the created returns order number 6XXXXXXX and choose Display Customer Return . | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Navigate to Document Flow Screen | On Returns tab, choose Returns Overview in Returns Control area. | The Returns Overview for Returns Order 6XXXXXXX - 10 screen displays. |  |
| 6 | Check Document Flow | In Document Number column, make a note of follow-up document number(s) for further use:Credit memo request or replacement order (subsequent delivery free of charge):________________________Returns Purchase Order: _______________________ |  |  |

After you have completed this activity, choose option A or option B, then perform all steps in chapter Return Goods to Supplier via Seller:

Option A: If credit memo request is generated, go to the Refund Customer with Credit Memo chapter.

Option B: If replacement order is generated, go to the Refund Customer with Replacement Material chapter.

#### Refund Customer with Credit Memo (Option A)

##### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo.

Procedure

Table 7: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Maintain settings as below.Set Billing Data and type before billing: ON.Create separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ON.Display Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) display(s) in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Documents (F0798) screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Table 8: Manage billing documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the app | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search for the Billing Document | Enter the billing document number recorded previously in the Billing Document field, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display the Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

#### Refund Customer with Replacement Product (Option B)

For product TG14 (with item category group CBUK – bought in item):

By default, replacement product is directly provided to customer from seller’s stock, in the case of immediate refund with Replacement Order, system also supports you to manually switch item category to CBXB in the created replacement order which triggers sales order specific procurement. After receiving product from the supplier, seller send it as replacement product to customer.

Complete the following chapters mentioned in BDN - Sales of Non-Stock Item with Order-Specific Procurement test script using master data listed in BKP:

- Create Purchase Order
- Approve and Release Purchase Order (Optional)
- Post Goods Receipt
- Enter Vendor Invoice

| Master Data | Sample Value |
| --- | --- |
| Material | TG14 |
| Supplier | 33300006 |

##### Create Free-of-Charge Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a free-of-charge delivery with reference to replacement order.

Prerequisite

Replacement order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Continue:Shipping point: 3310.Planned Creation Date: <Delivery selection date>Order: <Replacement order number created previously> |  |  |
| 4 | Create Delivery | Select your items and choose Create Deliveries. | Delivery is created with a number ______________ |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to perform picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: for example, 331R.Only Picking without WM: <select the checkbox> |  |  |
| 5 | Change Outbound Deliveries | On the Day's Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, enter the following data:If batch spilt exists, choose Batch Split Exists to expand sub item(s): Picked Qty : <quantity equal to delivery Qty>If batch split doesn't exist, Picked Qty: <quantity equal to delivery Qty> |  |  |
| 7 | Choose Enter | Choose Enter. |  |  |
| 8 | Save | Choose Save. | The delivery has been picked. |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Good Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping Point: 3310 |  |  |
| 5 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date and choose Continue in the dialog box. | The goods issue is posted |  |

Financial Postings

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the Delivery number and choose Continue. From the Delivery xxxxxxxx Display: Overview screen, choose Menu > Outbound Delivery > Issue Delivery Output. | The Output Details screen is displayed. |  |
| 4 | Print Preview | Select the line with the Output Type Delivery Note and choose Print Preview . | A preview of the print document displays. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is posted. |  |

##### Create Pro-forma Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a pro-forma invoice with reference to delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose the billing type Pro Forma Invoice for Delivery (F8) and billing date, such as the current date, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | In the Billing Document screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Pro-forma invoice is generated. |  |

Alternatively, it is supported to create pro-forma (type F5) with reference to replacement order.

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | Input the pro-forma invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Manage Billing Documents screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 7 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |

##### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create F2 type of invoice, and costs are transferred to accounting accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Invoice (F2) and maintain Billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | In the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Customer invoice is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 44002000Sales Disc Domestic | 41000000Rev Domestic Prod |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | Input the customer invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel Billing Docs. | Log displayed: Billing Document Canceled. |  |
| 7 | Update New attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |

#### Return Goods to Supplier via Seller

##### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create outbound delivery.

Prerequisite

Returns purchase order is created in chapter [Perform Material Inspection](#unique_51) [page ] 77, its number is noted down in chapter [Display Returns Overview](#unique_53) [page ] 80.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B) | The Purchase Orders, Fast Display screen displays. |  |
| 3 | Enter Data | In the head area:Shipping Point: 331RDelivery creation dates (From): <delivery creation From date> Delete the default dateDelivery creation dates (To) <delivery creation To date> Delete the default dateCalc Rule: <calculation rule>, for example, 2.Go to the Purchase Orders Tab and make the following entries then choose Execute:Purchasing Document: Enter the purchase order that is recorded in step: [Display Returns Overview](#unique_53) [page ] 80. | Activities Due for Shipping "Purchase Orders, Fast Display" screen displays. PO due for delivery is listed. |  |
| 4 | Create A Delivery | Select the line of purchase order from the list.Choose Background to create delivery in Background. | Activities Due for Shipping "Purchase Orders, Fast Display" screen displays. |  |
| 5 | Check Delivery Number | Choose More > Show/Hide Delivery , and note down the returns delivery number shown in the Document field. | A returns delivery is created. |  |

##### Perform Picking and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform picking, to ship returned material back to the supplier, and to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery (VL02N) screen, make the following entry and choose Enter.Outbound Delivery: Enter an Outbound delivery that created in last step: [Create Outbound Delivery](#unique_60) [page ] 91 | The Returns (Pur. Ord.) XXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter Picking Data | On the Returns (Pur. Ord.) XXXXXXXX Change: Overview screen, choose the Picking tab, make the following entries:Picked quantity: <picked quantity>Choose Save . | The system shows the message: Returns (Pur.Ord.) xxxxxxxx has been saved. The screen return to Change Outbound Delivery (VL02N) screen. |  |
| 5 | Post Goods Issue | On the Change Outbound Delivery (VL02N) screen, choose Post Goods Issue. | Returns (Pur.Ord.) 8XXXXXXX has been saved. |  |

|  |
| --- |
| Note If you (the seller) have decided to ship the material back to supplier and the supplier sends a replacement material (instead of a credit note), please skip next chapter [Create Supplier Credit Memo](#unique_62) [page ] 94 and execute the following chapters mentioned in the test script BMK - Return to Supplier:Receive Replacement Material (Optional)Post Goods Receipt(Optional)Follow-Up Activities For Replacement Material(Optional)Check Invoice Document (Optional) |

##### Create Supplier Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a supplier credit memo.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Enter Company Code | Open Create Supplier Invoice - Advanced (MIRO). Make following entries and choose Enter.Company Code: 3310Note Company code can only be edited by choosing More > Edit > Switch | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | Transaction: < Credit Memo>Go to Basic Data tab:Invoice date: <Today>Posting Date: <Today>Reference: <Fill the Reference Information>Tax Code： <Input Tax Code>Calculate Tax: <Selected>Tax Amount: <value in return PO Calculate Tax> | The Enter Incoming Invoice: Company Code XXXX screen displays. |  |
| 4 | Find Purchase Order References | Go to PO Reference tab, make the following entries:Reference Document Category :<Purchase Order/Scheduling Agreement>Purchase Order: <Enter a PO you created previously>Choose Enter. |  |  |
| 5 | Check the Purchase Order Items Data | Check Amount, Quantity, and Tax Code. | The Purchase Order Item table displays. The amount and the quantity correspond to the values of the Goods Issue. |  |
| 6 | Simulate Credit Memo and Check Messages | Choose Simulate (Ctrl+Shift+F7).If there are no differences (or if the value is within the defined tolerance), a new Simulation screen appears. You can check the simulation results. |  |  |
| 7 | Post Credit Memo | Choose Post. | The Invoice is posted. The system displays the message Document no. 51xxxxxxxx created. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Scheduling Job (Alternative)

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

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Sales Order Fulfillment Monitoring and Operations (BKK) (optional) | Using the master data from this document, complete the following activities described in the test script:Review sections: Incomplete SD Documents (deliveries) and Review Outbound Deliveries for Goods Issue |

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
> Flagged while digesting this document, not verified: Determine Refund prerequisite refers to second plant 1020/shipping point 1020/storage location 102A, while the sample data and refund steps use second plant 3320 (storage location 332A).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/customer-returns-for-non-stock-and-service-materials-3te-ae-test-scrip]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-involving-supplier-by-message-exchange-3q]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-with-direct-shipment-from-customer-to-sup]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKP_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 170,600 chars in the whole document
