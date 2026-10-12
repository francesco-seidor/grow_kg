---
id: 08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-sell-from-stock-bd9-ae-12
title: Test Script SAP S/4HANA Cloud Public Edition - Sell from Stock (BD9_AE) (BD9_S4CLD2608_BPD_EN_AE)
description: "SAP test script (2608, UAE/AE) for scope item BD9 Sell from Stock: prerequisites, sales order to billing and PEPPOL eDocument test steps, approvals, jobs."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sell-from-stock]
aliases: [BD9_S4CLD2608_BPD_EN_AE]
keywords: [Sell from Stock Order-to-Cash, sell from stock, sales order creation, outbound delivery, picking and goods issue, billing documents, preliminary billing, sales order approval, preliminary billing approval, electronic invoicing peppol]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD9_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1250
topic: 08-sales-order-management/sell-from-stock
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Sell from Stock (BD9_AE) (BD9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sell from Stock Order-to-Cash** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sell from Stock (BD9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232861504)

[2 Prerequisites 5](#_Toc232861505)

[2.1 System Access 5](#_Toc232861506)

[2.2 Roles 5](#_Toc232861507)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232861508)

[2.4 Additional Manual Configuration 9](#_Toc232861509)

[2.5 Business Conditions 10](#_Toc232861510)

[2.6 Preliminary Steps 10](#_Toc232861511)

[2.6.1 Set Initial Stock for Material 10](#_Toc232861512)

[2.6.2 Set Relevant for Proof of Delivery in BP Master Data (Optional) 12](#_Toc232861513)

[2.6.3 Create Template Item Proposal (Optional) 12](#_Toc232861514)

[2.6.4 Create Condition Records (Optional) 13](#_Toc232861515)

[2.6.5 Product Hierarchy 14](#_Toc232861516)

[2.6.5.1 Extend Product Hierarchy Materials (Optional) 14](#_Toc232861517)

[2.6.5.2 Maintain Product Hierarchy Condition(Optional) 16](#_Toc232861518)

[2.6.5.3 Maintain Product Hierarchy to Distribution Chain (Optional) 18](#_Toc232861519)

[2.6.5.4 Define Relevant Date for Product Hierarchy Determination (Optional) 18](#_Toc232861520)

[2.6.6 Import Sales Orders (Optional) 20](#_Toc232861521)

[2.6.7 Create Sales Order with Selling Recommender (Optional) 21](#_Toc232861522)

[2.6.7.1 Assign Customer Procedure for Product Proposal to Business Partner 21](#_Toc232861523)

[2.6.7.2 Create Sales Orders for Selling Recommender 21](#_Toc232861524)

[2.6.7.3 Schedule Job for Intelligent Proposal 22](#_Toc232861525)

[2.6.8 Preliminary Steps for Sales Order Approval (Optional) 23](#_Toc232861526)

[2.6.8.1 Define and Assign Approval Reasons 23](#_Toc232861527)

[2.6.8.2 Implement Cloud BADI 25](#_Toc232861528)

[2.6.8.3 Manage Teams and Responsibilities 27](#_Toc232861529)

[2.6.8.4 Set up Workflow 28](#_Toc232861530)

[2.6.9 Preliminary Steps for Preliminary Billing Approval (Optional) 31](#_Toc232861531)

[2.6.9.1 Define and Assign Approval Reasons 31](#_Toc232861532)

[2.6.9.2 Implement Cloud BADI 33](#_Toc232861533)

[2.6.9.3 Manage Teams and Responsibilities 35](#_Toc232861534)

[2.6.9.4 Set up Workflow 36](#_Toc232861535)

[2.6.10 Number Range to Business Places Assignment for a New Fiscal Year 39](#_Toc232861536)

[2.6.11 Preliminary Steps for Electronic Invoicing (PEPPOL) 42](#_Toc232861537)

[2.6.11.1 Define Identification Types for Business Partners 43](#_Toc232861538)

[2.6.11.2 Maintain Company Code Data (FINSC_T001Z_N) 45](#_Toc232861539)

[2.6.11.3 Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552) 47](#_Toc232861540)

[2.6.11.4 Maintain Business Partner Master Data 50](#_Toc232861541)

[2.6.11.5 Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301) 51](#_Toc232861542)

[2.6.11.6 Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304) 52](#_Toc232861543)

[2.6.12 Optional Steps for Electronic Invoicing (PEPPOL) 54](#_Toc232861544)

[2.6.12.1 Business Partner Master Data Maintenance for Electronic Invoicing (Optional) 54](#_Toc232861545)

[2.6.12.2 Value Mapping Maintenance for Electronic Invoicing (Optional) 55](#_Toc232861546)

[3 Overview Table 60](#_Toc232861547)

[4 Test Procedures 62](#_Toc232861548)

[4.1 Set Credit Limit (Optional) 62](#_Toc232861549)

[4.2 Complete Sales Quotation (Optional) 63](#_Toc232861550)

[4.3 Create Sales Order 63](#_Toc232861551)

[4.4 Create Sales Order Using IFRS15 Bundling Functionality (Optional) 67](#_Toc232861552)

[4.5 Create Attachment for Sales Order (Optional) 68](#_Toc232861553)

[4.6 Review Blocked Sales Orders (Optional) 69](#_Toc232861554)

[4.7 Process Sales Order Approval (Optional) 69](#_Toc232861555)

[4.7.1 Withdraw from Approval 70](#_Toc232861556)

[4.7.2 Approve/Reject/Rework Sales Order 71](#_Toc232861557)

[4.7.3 Rework Sales Order 72](#_Toc232861558)

[4.7.3.1 Check the Notifications 72](#_Toc232861559)

[4.7.3.2 Change Sales Order 73](#_Toc232861560)

[4.8 Advanced Available-to-Promise Processing (Optional) 74](#_Toc232861561)

[4.9 Create Delivery 75](#_Toc232861562)

[4.10 Handling Unit Management (Optional) 76](#_Toc232861563)

[4.11 Create Attachment for Delivery (Optional) 77](#_Toc232861564)

[4.12 Execute Picking 78](#_Toc232861565)

[4.13 Check Batches (Optional) 79](#_Toc232861566)

[4.14 Maintain Serial Numbers (Optional) 80](#_Toc232861567)

[4.15 Split Outbound Delivery (Optional) 81](#_Toc232861568)

[4.16 Add Freight Costs (Optional) 82](#_Toc232861569)

[4.17 Post Goods Issue 83](#_Toc232861570)

[4.18 Proof of Delivery (Optional) 84](#_Toc232861571)

[4.19 Create Preliminary Billing Document (Optional) 86](#_Toc232861572)

[4.20 Process Preliminary Billing Approval (Optional) 87](#_Toc232861573)

[4.20.1 Finalize the Preliminary Billing Document 87](#_Toc232861574)

[4.20.2 Rework from Approval 88](#_Toc232861575)

[4.20.3 Approve/Reject/Rework Preliminary Billing Document 89](#_Toc232861576)

[4.20.4 Rework Preliminary Billing Document 90](#_Toc232861577)

[4.20.4.1 Check the Notifications 91](#_Toc232861578)

[4.20.4.2 Change Preliminary Billing Document 92](#_Toc232861579)

[4.21 Create Partial Billing Document (Optional) 93](#_Toc232861580)

[4.22 Create Billing Document 93](#_Toc232861581)

[4.23 eDocument Cockpit 96](#_Toc232861582)

[4.24 Create Attachment for Billing (Optional) 98](#_Toc232861583)

[5 Appendix 99](#_Toc232861584)

[5.1 Process Integration 99](#_Toc232861585)

[5.1.1 Succeeding Processes 99](#_Toc232861586)

[5.2 Scheduling Job (alternative) 99](#_Toc232861587)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 99](#_Toc232861588)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 100](#_Toc232861589)

[5.2.3 Job Scheduling for Preliminary Billing Documents Creation (Alternative) 101](#_Toc232861590)

[5.2.4 Job Scheduling for Billing Creation (Alternative) 102](#_Toc232861591)

[5.2.5 Job Scheduling for Billing Release (Alternative) 103](#_Toc232861592)

[5.2.6 Job Scheduling for Billing Output (Alternative) 104](#_Toc232861593)

## Purpose

Overview

Sell-from-Stock provides a streamlined approach to order fulfillment. The Sell-from-Stock process is designed to efficiently manage and track the sales and shipment of existing inventory. It expedites order fulfillment, accurately recognizes revenue, and maintains precise financial accounting.

The process begins with the creation of a customer and a standard sales order, tailored to the specific customer and their requirements. Upon completion of order picking, the shipping specialist updates the inventory to reflect the outgoing stock. This inventory relief step documents the precise quantity of goods being shipped to the customer. With the posting of the goods issue, revenue is formally recognized, and the cost of goods sold is recorded in the financial accounting system. Once the goods are delivered, the delivery can be invoiced. For preliminary alignment with customers, an optional preliminary billing document can be generated from the billing due list items. This allows for any necessary adjustments before the final billing documents, which customers are expected to settle, are created.

For more information on bundling functionality relevant to IFRS 15, see SAP Note 2524569.

For details on the bundling functionality for IFRS 1w5, see [2524569](https://me.sap.com/notes/2524569) .

A preliminary billing document can be created from the billing due list items as an optional step. You can show it to customers for alignment and changes as needed. The final billing documents are created for the customer settlement.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/BD9_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch | See Business Conditions and Preliminary Steps sections .Use TG11 to test customer material, recorded with customer 33100009. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No serial number, no batch | See Business Conditions and Preliminary Steps sections. |
| Material | TG20 | Trad.Good 12,Reorder Point,Reg.Trad. | Only use if you have activated Serial Number Managment (BLL). |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP) building block.See Business Conditions and Preliminary Steps sections. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP) building block.See Business Conditions and Preliminary Steps sections. |
| Material | TG11_PH_CO21TG11_PH_CO30UTG11_PH_CO30TG11_PH_CW12TG11_PH_CW14TG11_PH_GP200TG11_PH_GP300TG11_PH_PPTG11_PH_WC | Trading Goods for Product HierarchyNo serial number, no batch | Only use if you have activated Product Hierarchy relevant (4EM) (4EN) building block.See Business Conditions and Preliminary Steps sections. |
| Material | IF11 | Trading Good for IFRS SFS Test Material 1 | Only use if you have activated Event-Based Revenue Recognition for Sale from Stock (BRT) (BRU)(37A) building block.See Business Conditions and Preliminary Steps sections. |
| Material | IF12 | Trading Good for IFRS SFS Test Material 2 | Only use if you have activated Event-Based Revenue Recognition for Sale from Stock (BRT) (BRU)(37A) building block.See Business Conditions and Preliminary Steps sections. |
| Material | CM-FL-V00 | Forklift | Only use if you have activated Make-to-Order Production with Variant Configuration (1YT). |
| Material | SM0001 | Service Material 01 |  |
| Material | NS0002 | Non-stock Material 02 |  |
| Sold-to Party | 331000033310000533100008331000093310000833100009 | Domestic UAE Customer 3Domestic UAE Customer 5 | You can test the scope item using another domestic customer.33100005 is for credit management.33100008 is for material listing or exclusion33100009 is for customer material record and POD (Proof-of-Delivery) |
| Ship-to Party | 33100003331000053310000833100009 | Domestic UAE Customer 3Domestic UAE Customer 5 |  |
| Payer | 33100003331000053310000833100009 | Customer domestic 03Customer domestic 05 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |
| 6N3 | Create Customer Hierarchy Master Data Script |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e9718dcb7c964bb736ee48ffe4a2c207)

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials (J45) test script process.Or create stock using Post Goods Movement app (refer to Preliminary Steps section for details). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO).It only displays it that way if it was your last transaction. So the action for the user should be to select Reference Document for MIGO Transaction > Other. | The Goods Receipt Otherscreen displays. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods Receipt |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen : Material tab, make the following entry and choose Enter:Material : <Material Number> |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant: <Plant>Storage Location: <Storage Location> |  |  |
| 7 | Input on the Goods Receipt Other screen: Batch tab | On the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Current Date or a Past Date>Note Only relevant for batch-relevant material. |  |  |
| 8 | Enter the Goods Receipt Other Screen: Serial Number Tab | On the Goods Receipt Other screen: Serial Numbers tab, enter the serial number of your received material.Note Only relevant for material TG20 |  |  |
| 9 | Save Your Entries | Choose Post. |  |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

#### Set Relevant for Proof of Delivery in BP Master Data (Optional)

Purpose

To run the step, you must maintain the Proof of Delivery (POD)-relevant indicator for customer master data. From demo data, only customer 33100009 has been set, following procedure can help you to set POD relevant for other customer master data if necessary.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Start.Double click the line item of Business Partner: 33100009 |  |  |
| 4 | Go to Shipping Tab | On the Change Organization:XXXXXXXX screen, choose Customer (Defined) in the Change in BP Role field.Choose Sales and Distribution in the Menu > More menu, then select Shipping tab . |  |  |
| 5 | Set POD - Relevant | Select POD - Relevant checkbox. |  |  |
| 6 | Save | Choose Save. |  |  |

#### Create Template Item Proposal (Optional)

Purpose

This process helps you to create template for item proposal if you want to use the optional step, copy item proposal to sales order, later on, in the process step, sales order entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Item Proposals (F2583). | The Manage Sales Item Proposals screen displays. |  |
| 3 | Create New Object | On the Manage Sales Item Proposals Screen, choose Create. | The Sales Item Proposal Screen displays. |  |
| 4 | Enter Item Proposal Details | On the Sales Item Proposal screen, in the Header Data tab, and make the following entries:Sales Document Type: PVSales Organization: 3310Distribution Channel: 10Division: 00Description: < For example, Item Proposal Template>Valid-From Date: <For example, Current Date>Valid-To Date: <For example, Current Date + 1 Year> |  |  |
| 5 | Enter Item Proposal Details | In the Products tab, choose Create:Material Number: <Material Number>Target Quantity: <Target Quantity> |  |  |
| 6 | Save the Entry | Choose Create. |  |  |

#### Create Condition Records (Optional)

Purpose

In case you have fine-tuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

#### Product Hierarchy

##### Extend Product Hierarchy Materials (Optional)

Purpose

The procedure helps you to extend material organization. It is only relevant If you use ANC procedure to have the new country version, you need to manually extend the materials to your organization

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access the App | Open Create Material (MM01) |  |  |
| 3 | Search for materials | Make below entries and choose ContinueMaterial : TG11_PH_CO21Material Type: Trading Goods |  |  |
| 4 | Select Views | In the pop up screen of Select View(s), select below views and choose Org.Levels:Basic Data 1Basic Data 2Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataInternational Trade: ExportPurchasingInternational Trade: ImportMRP 1MRP 2MRP 3MRP 4General Plant Data / Storage 1General Plant Data / Storage 2Accounting 1Accounting 2 |  |  |
| 5 | Input Organization inforamtion | In the pop up screen of Organization levels, input below entries and choose Continue:Plant: 3310Stor.Loc.: 331A/331RSales Org:3310Distribution Channel:10Note If message The material already exists and will be extended displays, please ignore it. |  |  |
| 6 | Input Detail | On the new screen of Create Material XXXXX (trading Goods),In the tab of Sales: sales org.1,DescriptionTax DataChoose Enter.In tab of Sales: sales org.2,Item Category Group: NORMChoose Enter.In tab of Sales: General/Plant,Profit Center: YB700Choose Enter.In tab of MRP 1,MRP Type: PDMRP Controller: 001Lot Sizing Procedure: EXChoose Enter.In tab of MRP 2,Planned Deliv. Time: 10 daysChoose Enter.In tab of Accounting 1,Valuation Class: 3100Standard Price: 6Per. Unit Price: 6Choose Enter.Choose Save. |  |  |
| 7 | Repeat step 1 to step 6 for other materials | Repeat Step 1 to Step 6 for below materialsTG11_PH_CO30UTG11_PH_CO30TG11_PH_CW12TG11_PH_CW14TG11_PH_GP200TG11_PH_GP300TG11_PH_PPTG11_PH_WC | The materials are extended |  |

##### Maintain Product Hierarchy Condition(Optional)

Purpose

This process helps you to maintain Product Hierarchy condition DPH1.It is only relevant If you use ANC procedure to have the new country version, you need to manually maintain the product hierarchy condition for your organization

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist. |  |  |
| 2 | Access the App | Open Set Material Prices - Sales (VK12) | The Manage Product Hierarchy Assignments(F4240) view displays. |  |
| 3 | Pricing Condition Type PPR0 | On the Change Condition Records view, enter the following information:Condition Type: PPR0Choose Menu Condition>CreateChoose Material with release Status, and choose Choose. |  |  |
| 4 | Input price of PPR0 | On the Screen of Create Price Condition (PPR0): Fast Entry, input below entries and choose Save.Sales Org:3310Distribution Channel:10Amount: input pricingMaterial: Materials expended in last chapterChoose Save.Choose Back. | Condition record for PPR0 is maintained |  |
| 5 | Pricing Condition Type DPH1 | On the Screen of Create Condition Records, enter the following information:Condition Type: DPH1Choose Enter. |  |  |
| 6 | Input entries for DPH1 | On the Screen of Create Product Hierarchy Condition(DPH1): Fast Entry, make entries below:Sales Oraganization: 3310Distribution channel:10Prod. Hier. Node:ADJUST_JOINT_PLIERSAmount :10-Unit: %Calculat. Type: AProd. Hier. Node: COMB_WRENCHESAmount :8-Unit: %Calculat. Type:AProd. Hier. Node: CUTTING_PLIERSAmount: 6-Unit: %Calculat. Type: AProd. Hier. Node: WRENCHESAmount :5-Unit: %Calculat. Type: AChoose Save | Condition record for DPH1 is saved. |  |

##### Maintain Product Hierarchy to Distribution Chain (Optional)

Purpose

This process helps you to maintain Product Hierarchy to Distribution Chain if you are using Product Hierarchy relevant materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Product Hierarchy Assignments (F4240). | The Manage Product Hierarchy Assignments (F4240) screen displays. |  |
| 3 | Create New Object | Choose Create. | The Create Product Hierachy Assignment Screen displays. |  |
| 4 | Enter General Information | On the Create Product Hierachy Assignment screen, in the General Information tab, make the following entries:Purpose: 02 SalesSales Organization: 3310Valid From: <For example, Current Date>Valid To: <For example, Current Date + 1 Year>Product Hierachy: TOOLS |  |  |
| 5 | Save the Entry | Choose Create. |  |  |

##### Define Relevant Date for Product Hierarchy Determination (Optional)

Purpose

This process step shows you how to define relevant date for product hierarchy determination.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: SalesSub Application Area: Sales Master Data Management | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Configure master data for materials and product hierarchies in sales item name and choose arrow at the item end. | The Configure Your Solution - Materials screen displays. |  |
| 6 | Navigate to SSCUI | In Configuration Steps section, choose Configure in the Actions column for Define Relevant Date for Product Hierarchy Determination (SSCUI ID: 103303) step. | The Date Relevant for Hierarchy Determination screen displays. |  |
| 7 | Set Data Relevant for Hierarchy Determination | Choose New Entries, enter the following data, and choose Save.Propose of Product Hierarchy: SalesSales Org: 3310Distribution Channel: 10Relevant Date for Det. Of Prod. Hier: for example, Pricing Date | Data relevant for Hierarchy determination is set |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Relevant Date for Product Hierarchy Determination | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Relevant Date for Product Hierarchy Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Date Relevant for Hierarchy Determination screen displays. |  |
| 3 | Set Data Relevant for Hierarchy Determination | Choose New Entries, enter the following data, and choose Save.Propose of Product Hierarchy: SalesSales Org: 3310Distribution Channel: 10Relevant Date for Det. Of Prod. Hier: for example, Pricing Date | Data relevant for Hierarchy determination is set |  |

#### Import Sales Orders (Optional)

Purpose

In this activity, You can import the sales order with template file.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Import Sales Orders (F4293). | The Import Sales Orders (F4293) view displays. |  |
| 3 | Download Template | Choose Download Template to download a template file. |  |  |
| 4 | Upload Template | Input all the mandatory fields in the template file and choose Browse to upload the file. |  |  |
| 5 | Import Sales Order | Choose Import to import the Sales orders. |  |  |
| 6 | Check Logs | In the Pop-up Information window, choose View History to check the log. | The Sales order is imported |  |

#### Create Sales Order with Selling Recommender (Optional)

##### Assign Customer Procedure for Product Proposal to Business Partner

Purpose

In this activity, you assign customer procedure for product proposal to a business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Master Data (F0850A). | The Manage Customer Master Data view displays. |  |
| 3 | Choose Business Partner | Input following entry and choose Go.Business Partner: for example, 33100003 |  |  |
| 4 | Choose Sales Area | Choose the Business Partner and click the lineOn the new screen, choose Edit.Choose the tab of Sales Areas, then chooseCompany Code: for example 3310Click the line. |  |  |
| 5 | Input PP Customer Procedure | In the new screen, choose tab Sales Area Details, make the following entry, and choose Apply.PP customer Procedure : for example AChoose Apply and Save. | The PP customer procedure has assigned to business partner. |  |

##### Create Sales Orders for Selling Recommender

Purpose

As the product proposal is based on historical data, at least three sales orders are required to derive a product proposal.

In this activity, you create sales orders to get historical data for setting up selling recommender.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Order - Version 2 screen displays. |  |
| 3 | Navigate to Create Order Screen | On the Manage Sales Order - Version 2 screen, choose Create. |  |  |
| 4 | Enter Data | On the Create Sales Order screen, make the following entries and choose Continue:Salers Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: for example 33100003Ship-to Party: for example 33100003Customer References: Selling RecommenderMaterial Number: <Material Number>Quantity: <Quantity> |  |  |
| 6 | Save the Order | Choose Create. Make a note of the sales order number: __________.If you have installed the Free Goods Processing scope item in your system, and used material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter. |  |  |

##### Schedule Job for Intelligent Proposal

Purpose

In this activity, You create and process Jobs for intelligent proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Intelligent Product Proposal (F5139). |  |  |
| 3 | Create Job | On the Application Jobs screen, choose Create. |  |  |
| 4 | Enter Data | On theNew Job: Template for Backgorund Job of Intelligent Product Proposal Screen, make the following entries:Job Template: Template for Background Job of Intelligent Product ProposalJob Name: Template for Background Job of Intelligent Product ProposalChoose Step 2, in the tab of Scheduling Options, choose Define Recurrence Pattern, On the pop-up screen, make following entries:Start Immediately: XRecurrence Pattern:Single RunChoose OKChoose Step 3, in the tab of Parameters, make the following entries:Create Again: XSales Organization: 3310Choose Schedule. |  |  |

#### Preliminary Steps for Sales Order Approval (Optional)

##### Define and Assign Approval Reasons

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to define and assign approval reasons.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: SalesSub Application Area: Basic Functions | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Sales Document Approvals item name and choose arrow at the item end. | The Configure Your Solution - Sales Document Approvals screen displays. |  |
| 6 | Navigate to Define Reasons Screen | In Configuration Steps section, choose Configure in the Actions column for Define Reasons for Approval Requests step. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 7 | Define Approval Reason | Choose New Entries, enter the following data, and choose Save.Approval Request Reason ID: for example, ZOR1Approval Request Reason: for example, Document needs approval | Approval reason is defined. |  |
| 8 | Navigate to Assign Reasons Screen | In Configuration Steps section, choose Configure in the Actions column for Assign Reasons for Approval Requests step. | The Change View"Assign Reasons for Approval Requests"Overview screen displays. |  |
| 9 | Assign Approval Reason to Sales Order | Choose New Entries, enter the following data, and choose Save.Document Category: CApproval Request Reason: for example, ZOR1 |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Reasons for Approval Requests | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Reasons for Approval Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 3 | Define Approval Reason | Choose New Entries, enter the following data, and choose Save.Approval Request Reason ID: for example, ZOR1Approval Request Reason: for example, Document needs approval | Approval reason is defined. |  |
| 4 | Open Define Reasons for Approval Requests | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Reasons for Approval Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View"Assign Reasons for Approval Requests"Overview screen displays. |  |
| 5 | Assign Approval Reason to Sales Order | Choose New Entries, enter the following data, and choose Save.Document Category: CApproval Request Reason: for example, ZOR1 |  |  |

##### Implement Cloud BADI

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Business Add-In (BADI) SD_APM_SET_APPROVAL_REASON is called whenever a sales document is saved by a business user. It determines whether a sales document needs to be sent to an approver and, if so, set an approval request reason on sales document header level.

This means that if you want to use the workflow for the approval of sales documents, implementing this BAdI is a prerequisite. In the Manage Sales Document Workflows (F2190) app, you define additional preconditions and approval steps.

When the system sets an approval request reason for a sales document, the approval workflow is triggered automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Custom Logic (F6957). | The Custom Logic screen displays. |  |
| 3 | Search or Create Custom Logic | In the Search Box input below information, and choose Go:Set Approval Request Reasons for Sales DocumentsCheck if the status of the custom logic is published.If not, please choose the customer logic and choose Publish.Note If there is no relevant custom logic exists, please go to step 4 to 6 to create the custom logic | The Custom Logic is ready to use. |  |
| 4 | Input Extension Point | Choose Create and make the following entries and choose Search:Extension points: SD_APM_SET_APPROVAL_REASON | The New Implementation section displays |  |
| 5 | Create Custom Logic | Choose the extension points and choose Step 2, In the section of Implementation ID, make following entries:Implementation Description: Set Approval Request Reasons for Sales DocumentsImplementation ID: for example YY1_SETAPPROVALREQUESTREASONChoose Review.Choose Create. | The Custom Logic is created |  |
| 6 | Publish the Custom Logic | Back to Custom Logic Screen, choose the custom logic you created in the last step, and choose Publish. | The Custom logic is published. |  |
| 7 | Add/change Coding (Optional) | You can change the code of the custom logic if needed.Choose the custom logic and click the line.Choose Open Code Editor in the header of the screen.Choose Edit to change/add the codefor example:If salesdocument-sddocumentcategory = 'C' and salesdocument-sddocumentreason = '005'. salesdocapprovalreason = 'ZOR1'. endif.Note Please note that it is possible to have sales document approvals also for other categories of sales documents.The coding mentioned above can be seen as independent coding that can be added to the BAdI implementation without removing possible other codingYou can choose Show Sample Code to copy the suggested sample code if needed.Choose Publish to save the code you created or added. | The code for custom logic is changed |  |

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain the teams and responsibilities for sales order workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). |  |  |
| 3 | Create A New Team | Choose Create. |  |  |
| 4 | Enter General Information | Make the following entries and choose Enter:Name: Sales Order WorkflowDescription: Sales Order WorkflowStatus: EnabledType: SALES | The Draft Logic section displays |  |
| 5 | Add Team Members | On Team Members tab, choose Create.From the Items section, select a Business Partnercheck box and choose OK.Last Name: Sales Manager | The Select: Business Partner screen displays.Team member sales manager is added. |  |
| 6 | Add Function to Team Members | In Function field, choose Select. On the Select: Functions screen, select the following functions, and choose OK.CMR1LVLA: Sales Document Approver -Level 1CMR2LVLA : Sales Document Approver -Level 2 |  |  |
| 7 | Save and Publish | Choose Save Draft. | User created a new team and appropriate function(s) have been assigned to the business user(s) to be configured as approver(s). |  |

##### Set up Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set up workflow.

In below example, if total amount of the sales order is more than 1000 USD, “Sales Document Approver - Level 2” can approve. If total amount of the sales order is less than 1000 USD, “Sales Document Approver - Level 1” can approve.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Document Workflows (F3014). | The Manage Workflows screen displays. |  |
| 3 | Create the First Workflow | Choose Workflow for Sales Orders next to Workflow.Choose Add.Note If the workflow has already be defined, please skip step 4 to 10. | The New Workflow screen displays. |  |
| 4 | Maintain General Data | Make the following entries.In the Header tab:Name: <Second Approver- Net Value over 1000> |  |  |
| 5 | Set Preconditions | Make the following entries and choose Save:Preconditions:Net Amount is greater thanCurrency: AEDAmount: 1000Choose Save. | Preconditions are set. |  |
| 6 | Add Steps | From the Step Sequence section, choose Add.Select the following entries from dropdown lists:Under the Header tab:Type: Release of Sales orderUnder the Recipients tab:Assignment By: RoleRole: Sales Document Approver - Level 2Under the Exception Handling tab:Name: Rework Sales orderRequired Action: Rework of Sales orderAction Result: Restart WorkflowChoose Add to append this step to the workflow and choose Save. | The New Step screen displays.The first workflow is created. |  |
| 7 | Create the Second Workflow | Choose Back to the Manage Workflows screen.Choose Add. | The New Workflow screen displays. |  |
| 8 | Maintain General Data | Make the following entries.Under the Header tab:Name: <First Approval- No Conditions |  |  |
| 9 | Add Steps | From the Step Sequence section, choose Add.Make the following entries:Under the Header tab:Type: Release of Sales orderUnder the Recipients tab:Assignment By: RoleRole: Sales Document Approver - Level 1Under the Exception Handling tab:Name: Rework Sales orderRequired Action: Rework of Sales orderAction Result: Restart WorkflowChoose Add to append this step to the workflow and choose Save. | The New Step screen displays.The second workflow is created. |  |
| 10 | Activate Workflows | Choose Back to the Manage Workflow screen.Choose Define Order. Adjust the order as below:Second Approver- Net Value over 1000: Order 1First Approver-No Conditions: Order 2Choose Activate to active the workflows. | Workflows are activated. |  |

#### Preliminary Steps for Preliminary Billing Approval (Optional)

##### Define and Assign Approval Reasons

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to define and assign approval reasons.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: SalesSub Application Area: Basic Functions | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Document Approvals item name and choose arrow at the item end. | The Configure Your Solution - Document Approvals screen displays. |  |
| 6 | Navigate to Define Reasons Screen | In Configuration Steps section, choose Configure in the Actions column for Define Reasons for Approval Requests step. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 7 | Define Approval Reason | Choose New Entries, enter the following data, and choose Save.Approval Request Reason ID: for example, ZPBDApproval Request Reason: for example, Preliminary Billing Document needs approval | Approval reason is defined. |  |
| 8 | Navigate to Assign Reasons Screen | In Configuration Steps section, choose Configure in the Actions column for Assign Reasons for Approval Requests step. | The Change View"Assign Reasons for Approval Requests"Overview screen displays. |  |
| 9 | Assign Approval Reason to Preliminary Billing | Choose New Entries, enter the following data, and choose Save.Document Category: PBD Preliminary Billing DocumentApproval Request Reason: for example, ZPBD |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Reasons for Approval Requests | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Reasons for Approval Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 3 | Define Approval Reason | Choose New Entries, enter the following data, and choose Save.Approval Request Reason ID: for example, ZPBDApproval Request Reason: for example, Preliminary Billing Document needs approval | Approval reason is defined. |  |
| 4 | Open Assign Reasons for Approval Requests | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Reasons for Approval Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View"Assign Reasons for Approval Requests"Overview screen displays. |  |
| 5 | Assign Approval Reason to Preliminary Billing | Choose New Entries, enter the following data, and choose Save.Document Category: PBD Preliminary Billing DocumentApproval Request Reason: for example, ZPBD |  |  |

##### Implement Cloud BADI

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Business Add-In (BADI) SD_BIL_APM_SET_APPROVAL_REASON is called whenever a preliminary Billing is saved by a business user. It determines whether a preliminary billing need to be sent to an approver and, if so, set an approval request reason on preliminary billing level.

This means that if you want to use the workflow for the approval of sales documents, implementing this BAdI is a prerequisite. In the Manage Preliminary Billing Document Workflows (F4274) app, you define additional preconditions and approval steps.

When the system sets an approval request reason for a sales document, the approval workflow is triggered automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Custom Logic (F6957). | The Custom Logic screen displays. |  |
| 3 | Search or Create Custom Logic | In the Search Box input below information, and choose Go:Set Approval Request Reasons for Preliminary Billing DocumentsCheck if the status of the custom logic is published.If not, please choose the customer logic and choose Publish.Note If there is no relevant custom logic exists, please go to step 4 to 6 to create the custom logic | The Custom Logic is ready to use. |  |
| 4 | Input Extension Point | Choose Create and make the following entries and choose Search:Extension points: SD_BIL_APM_SET_APPROVAL_REASON | The New Implementation section displays |  |
| 5 | Create Custom Logic | Choose the extension points and choose Step 2, In the section of Implementation ID, make following entries:Implementation Description: Set Approval Request Reasons for Preliminary Billing DocumentsImplementation ID: for example YY1_ PBD_APPROVAL_REASONChoose Review.Choose Create. | The Custom Logic is created |  |
| 6 | Publish the Custom Logic | Back to Custom Logic Screen, choose the custom logic you created in the last step, and choose Publish. | The Custom logic is published. |  |
| 7 | Add/change Coding (Optional) | You can change the code of the custom logic if needed.Choose the custom logic and click the line.Choose Open Code Editor in the header of the screen.Choose Edit to change/add the codefor example:IF billingprocdocument-totalnetamount > 1000.salesdocapprovalreason = billingprocdocapprovalreason = 'ZPBD'. ENDIF.Note Please note that it is possible to have sales document approvals also for other categories of sales documents.The coding mentioned above can be seen as independent coding that can be added to the BAdI implementation without removing possible other codingYou can choose Show Sample Code to copy the suggested sample code if needed.Choose Publish to save the code you created or added. | The code for custom logic is changed |  |

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain the teams and responsibilities for preliminary billing document workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). |  |  |
| 3 | Create A New Team | Choose Create. |  |  |
| 4 | Enter General Information | Make the following entries and choose Enter:Name: for example, Preliminary Billing Document Approval WorkflowDescription: Preliminary Billing Document Approval WorkflowStatus: EnabledType: SBILLING |  |  |
| 5 | Set Value at Responsibility Definitions section | You can put criteria as per your approval conditions, for example, BillingDocu-mentType = F2 |  |  |
| 6 | Add Team Members | On Team Members tab, choose Create.From the Items section, select a Business Partnercheck box and choose OK.For example, Last Name: Your Manager’s Last NameNote Please contact your system Administrator if you are not sure if a business part-ner’s role is enough for preliminary billing document approval. The business role should contain the catalog SAP_SD_BC_BIL_MYINBOX_PC. | The Select: Business Partner screen displays.Team member is added. |  |
| 7 | Add Function to Team Members | In Function field, choose Select. On the Select: Functions screen, select the following functions, and choose OK.SBILAPRL1: Billing Process Document Approver - Level 1SBILAPRL2 : Billing Process Document Approver - Level 2 |  |  |
| 8 | Save the new Team | Choose Save at the bottom of the screen. | User created a new team and appropriate function(s) have been assigned to the business user(s) to be configured as approver(s). |  |

##### Set up Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set up workflow.

In below example, if total amount of the preliminary billing document is less than 500 EUR, no approval is required. If total amount of the preliminary billing document is more than 500 EUR and less than 1000 EUR, “Billing Process Document Approver - Level 1” can approve it. If total amount of the preliminary billing document is more than 1000 EUR, it needs “Billing Process Document Approver - Level 1” to approve it first, then needs “Billing Process Document Approver - Level 2” approve it.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Preliminary Billing Document Workflows (F4274). | The Manage Workflows screen displays. |  |
| 3 | Create a Workflow | Choose Add.Note If the workflow has already be defined, you can check if existing one(s) meet your approval conditions before creating a new one. | The New Workflow screen displays. |  |
| 4 | Maintain Header and Step Properties Sector | Make the following entries.Workflow Name: <It’s mandatory to have a workflow name>Filling in Description, Valid from and Valid to fields are optional. |  |  |
| 5 | Set Preconditions in “Start Conditions” sector | Make the following entries and choose Save:Preconditions:Net Amount is greater thanCurrency: EURAmount: 500Choose Save. | Preconditions are set. |  |
| 6.1 | Add StepsStep 1 | From the Steps section, choose Add.Select the following entries from dropdown lists:In the Header tab:Step Name: Step 1Step Type: Release of Preliminary Billing DocumentIn the Recipients tab:Assignment By: RoleRole: Billing Process Document Approver - Level 1In the Step Conditions tab:Set conditions to this step:Select Net Amount is greater thanCurrency: EURNet Value: 500In the Deadlines tab:You can set approval deadlines if required by choosing Add.In the Exception Handling tab:Name: Rework Preliminary Billing DocumentRequired Action: Rework of Preliminary Billing DocumentAction Result: Restart WorkflowChoose Add to append this step to the workflow. | The New Step screen displays.The first approval level in this workflow is created. |  |
| 6.2 | Add StepsStep2 | From the Steps section, choose Create.Select the following entries from dropdown lists:In the Header tab:Step Name: Step 2Step Type: Release of Preliminary Billing DocumentIn the Recipients tab:Assignment By: RoleRole: Billing Process Document Approver - Level 2In the Step Conditions tab:Set conditions to this step:Select Net Amount is greater thanCurrency: EURNet Value: 1000In the Deadlines tab:You can set approval deadlines if required by choosing Add.In the Exception Handling tab:Name: Rework Preliminary Billing DocumentRequired Action: Rework of Preliminary Billing DocumentAction Result: Restart WorkflowChoose Add to append this step to the workflow and choose Save. | The New Stepscreen displays.The second approval level in this workflow is created.And the whole workflow is saved. |  |
| 7 | Activate Workflows | Choose Back to the Manage Workflow screen.Click the Radio button and choose Activate to active the workflows. | Workflows are activated. |  |

#### Number Range to Business Places Assignment for a New Fiscal Year

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Set Local Version | Ensure that your local version is correct, it appears under the Realize section.To change the version, choose the Set Local Version button at the bottom of the view. In the dialog, select your local version from the list and choose Set Local Version. | The local version displays under the Realize section. |  |
| 4 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 5 | Enter Criteria | Make the following entry in the Search field: Assign Number Ranges to Business Places, and then choose Enter. | A filter list of All Items display. |  |
| 6 | Select Item | Select the Official Document Numbering item name. | An Official Document Numbering column appears. |  |
| 7 | Choose a Configuration Step | In the Configuration Steps section, on the Assign Number Ranges to Business Places for Official Doc. Numbering MENA step, choose Configure. | The Change View "Assign Number Ranges to Business Places": Overview displays. |  |
| 8 | Verify Values for Current Fiscal Year | Verify the following entries:CoCd: 3310Document Class: ACMDate: <Beginning of Current Year>Exp.date: <End of Current Year>Prefix:20No.gp: ACM001No.: 01CoCd: 3310Document Class:AINDate: <Beginning of Current Year,for example, 01/01/2020>Exp.date: <End of Current Year,for example, 12/31/2020>Prefix:10No.gp: AIN001No.: 01Note If values for the new fiscal year do not appear in the list, you proceed to the next step. If the values for the new fiscal year do appear, choose Cancel to return to the previous view. |  |  |
| 9 | Add Values for New Fiscal Year | If the values for the new fiscal year do not appear in the list, choose New Entries to add.Make the following entries:First line:CoCd: 3310Document Class:ACMDate: <Beginning of New Fiscal Year>Exp.date: <End of New Fiscal Year>Prefix:20No.gp: ACM001No.: 01Second line:CoCd: 3310Document Class:AINDate: <Beginning of New Fiscal Year,for example, 01/01/2020>Exp.date: <End of New Fiscal Year,for example, 12/31/2020>Prefix:10No.gp: AIN001No.: 01and choose Save from the bottom of the view. | New fiscal year values added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Number Ranges to Business Places.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Verify Values for Current Fiscal Year | Verify the following entries:CoCd: 3310Document Class: ACMDate: <Beginning of Current Year>Exp.date: <End of Current Year>Prefix:20No.gp: ACM001No.: 01CoCd: 3310Document Class:AINDate: <Beginning of Current Year,for example, 01/01/2020>Exp.date: <End of Current Year,for example, 12/31/2020>Prefix:10No.gp: AIN001No.: 01Note If values for the new fiscal year do not appear in the list, you proceed to the next step. If the values for the new fiscal year do appear, choose Cancel to return to the previous view. |  |  |
| 4 | Add Values for New Fiscal Year | If the values for the new fiscal year do not appear in the list, choose New Entries to add.Make the following entries:First line:CoCd: 3310Document Class:ACMDate: <Beginning of New Fiscal Year>Exp.date: <End of New Fiscal Year>Prefix:20No.gp: ACM001No.: 01Second line:CoCd: 3310Document Class:AINDate: <Beginning of New Fiscal Year,for example, 01/01/2020>Exp.date: <End of New Fiscal Year,for example, 12/31/2020>Prefix:10No.gp: AIN001No.: 01and choose Save from the bottom of the view. | New fiscal year values added. |  |

Result

Assign Number Range to Business Place is active for Current Fiscal Year.

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

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Set Credit Limit (Optional)](#unique_39) [page ] 62 | Credit Controller |  | Credit Limit for 33100005 Customer has been set. |
| [Complete Sales Quotation (Optional)](#unique_40) [page ] 63 |  |  |  |
| [Create Sales Order](#unique_41) [page ] 63 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Create Sales Order Using IFRS15 Bundling Functionality (Optional)](#unique_42) [page ] 67 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Create Attachment for Sales Order (Optional)](#unique_43) [page ] 68 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Review Blocked Sales Orders (Optional)](#unique_44) [page ] 69 |  |  |  |
| [Process Sales Order Approval (Optional)](#unique_45) [page ] 69 |  |  |  |
| [Withdraw from Approval](#unique_46) [page ] 70 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Approve/Reject/Rework Sales Order](#unique_47) [page ] 71 | Sales Manager | My Inbox- All Items |  |
| [Rework Sales Order](#unique_48) [page ] 72 |  |  |  |
| [Check the Notifications](#unique_49) [page ] 72 | Internal Sales Representative | My Inbox- All Items |  |
| [Change Sales Order](#unique_50) [page ] 73 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Advanced Available-to-Promise Processing (Optional)](#unique_51) [page ] 74 |  |  |  |
| [Create Delivery](#unique_52) [page ] 75 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Create Attachment for Delivery (Optional)](#unique_53) [page ] 77 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Execute Picking](#unique_54) [page ] 78 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Check Batches (Optional)](#unique_55) [page ] 79 | Shipping Specialist | Change Outbound Delivery (VL02N) | Batch numbers are checked |
| [Maintain Serial Numbers (Optional)](#unique_56) [page ] 80 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Split Outbound Delivery (Optional)](#unique_57) [page ] 81 | Shipping Specialist | Split Outbound Delivery (VLSP) |  |
| [Add Freight Costs (Optional)](#unique_58) [page ] 82 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Post Goods Issue](#unique_59) [page ] 83 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Proof of Delivery (Optional)](#unique_60) [page ] 84 | Shipping Specialist | POD - Change Outbound Delivery |  |
| [Create Preliminary Billing Document (Optional)](#unique_61) [page ] 86 | Billing Clerk | Create Preliminary Billing Documents (F2876) |  |
| [Finalize the Preliminary Billing Document](#unique_62) [page ] 87 | Billing Clerk | Manage Preliminary Billing Documents (F2875) |  |
| [Rework from Approval](#unique_63) [page ] 88 | Billing Clerk | Manage Preliminary Billing Documents (F2875) |  |
| [Approve/Reject/Rework Preliminary Billing Document](#unique_64) [page ] 89 | Billing approval | My Inbox (F2097) |  |
| [Rework Preliminary Billing Document](#unique_65) [page ] 90 |  |  |  |
| [Check the Notifications](#unique_66) [page ] 91 | Billing Clerk | My Inbox (F2097) |  |
| [Change Preliminary Billing Document](#unique_67) [page ] 92 | Billing Clerk | Manage Preliminary Billing Documents (F2875) |  |
| [Create Partial Billing Document (Optional)](#unique_68) [page ] 93 | Billing Clerk | Create Billing Documents - VF01 (VF01) |  |
| [Create Billing Document](#unique_69) [page ] 93 | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |
| [Create Attachment for Billing (Optional)](#unique_70) [page ] 98 | Billing Clerk | Display Billing Documents (VF03) | The Display Billing Document screen displays. |

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

### Set Credit Limit (Optional)

Follow the procedure for Set Credit Limit process steps in the Basic Credit Management (BD6) scope item.

Purpose

In this process, a credit limit is set for the used customer.

Procedure

Complete all the activities described in the test script of Basic Credit Management (BD6) scope item.

|  |
| --- |
| Note The credit limit currency in all company codes is set to use the group currency which is defined when the solution is activated. |

### Complete Sales Quotation (Optional)

Purpose

This scope item describes the process for a standard sales quotation.

Procedure

Complete all the activities described in the test script of Sales Quotation (BDG) scope item.

|  |
| --- |
| Note If you want to use the optional link between Sales Quotation (BDG) and Sell from Stock (BD9) scope items, this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Navigate to Create Order Screen | On the Manage Sales Order screen, and choose Create > Create Sales Orders - VA01. |  |  |
| 4 | Enter Data | On the Create Sales Order screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330 |  |  |
| 5 | Enter Order Details | If you would like to use listing and exclusion, continue with Enter listed/ excluded Material Numbers step.If you would like to use customer material record information, continue with Enter Customer Material Number step.On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Customer References: <PO number>Note If you have done the Prerequisite steps for Create Sales orders with selling recommender, you will get items proposed in the sales order based on your historical data. You can choose Copy Prod. Proposal Qty to fulfill the quantities, or maintain them manually, for the items you don’t need, keep the quantity blank.Material Number: <Material Number>Note To use Bundling Functionality in Context of IFRS15, create a sales order with two line items, use material IF11 for the first line item, and IF12 for the second line item.For further information regarding bundling functionality in context of IFRS 15, refer to SAP Note [2524569](https://me.sap.com/notes/2524569).Quantity: <Quantity>If you would like to use Sales order approval workflow, please maintain:Order Reason: 005 Newspaper AdvertisementIf you would like to use item proposal, continue with the next step. |  |  |
| 6 | Copy Item Proposal to Sales Order (Optional) | On the Create Standard Order: Overview screen, choose Propose Items.In the Propose Items dialog box, input item proposal created in preliminary step in Sales Document.Then choose Default with Quantity. | Material and quantity recorded in item proposal are copied to sales order item. |  |
| 7 | Check Product Hierarchy information (Optional) | If you used Product Hierarchy relevant Material, On the Create Standard Order: Overview screen, choose the line item for Product Hierarchy Material, and choose Display Item Details Botton.On the Create Standard Order: Item Data Screen, Navigate to Sales B tab, check the Product Hierarchy information under Product Hierarchy (Purpose: Sales)Navigate to Conditions tab, check the Product Hierarchy condition DPH1.Choose Back to back to header level. | Product Hierarchy information and relevant discount condi-tion type appears. |  |
| 8 | Enter Data (Optional) | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: 33100008Ship-to Party: 33100008Customer References: <Customer References>. Enter a customer purchase order number as reference.Enter the following Material Numbers: TG11, TG12 and TG20Quantity: <Quantity> For example, 1 PC. | Material TG11 is listed, and can be entered without error message.Material TG12 is excluded. Message Material TG12 has been excluded appears.Material TG20 is not listed. Message Material TG20 is not listed and therefore not allowed is processed.You can use extra controls into product (material) listing and exclusion and influence product salability according to your business needs. please check link :https://help.sap.com/viewer/DRAFT/a376cd9ea00d476b96f18dea1247e6a5/2005.500/en-US/7df6956efb9245c898a36c05f4b81efe.html |  |
| 9 | Remove Not Listed Materials (Optional) | If you have selected the customer for listing/ exclusion, remove Materials TG12 and TG20 if a dialog box appears. | Sales Order can be saved only if materials TG12 and TG20 have been removed. |  |
| 10 | Enter Customer Material Number (Optional) | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: 33100009Ship-to Party: 33100009Customer References: <Customer References>. Enter a customer purchase order number as reference.Customer Material Number: <Description from Customer Material Info. Record>, such as CUS_AE_TG11.Quantity: <Quantity>. For example, 1 PC. | Material TG11 is automatically determined from customer material info record, and copied into the sales order. If the sales unit is maintained in the customer's material info record, it will be automatically determined and displayed in the Sales Unit field.You can open Manage Customer Material to edit, or to display the customer material information. |  |
| 11 | Save Document | Choose Save. Make a note of the sales order number: __________.Note If you have installed the Free Goods Processing scope item in your system, and used material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter.If you are using TG12 in testing, the following warning may appear: Reorder point for item 000010 has been exceeded: 10 PC. To skip this warning, choose Enter. | The order is saved and the order confirmation is printed out. |  |

|  |
| --- |
| NoteIf Advanced Available-to-Promise Processing(1JW), the price relevant scope item, is activated, Product Allocation Check can be carried out when allocations are set up (done from 1JW). In any cases, a PAC Product Allocation Check is carried out. Based on the results of the checks, if requested availability cannot be fulfilled, the delivery proposal screen during sales order processing shows up and you decide based on the results of the checks.In a case where only Basic Available-to-Promise Processing (2LN) scope item is activated, the system triggers an availability check (no allocation check) and provides deliver proposal if the availability situation cannot be fulfilled. |

Printing form - Output Management

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Search for Sales Order | Enter search terms in filter bar and choose GoFor example, enter sales order number in Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Click sales order number, and choose Display Sales Orders.Note If there is not a Display Sales Orders, then click More Links. Select Display Sales Orders, and choose OK. | The Display Sales Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Header Output Preview .Select the line with Output type ORDER_CONFIRMATION and choose Display Document. | The document displays. |  |

|  |
| --- |
| Note It can also be navigated to a fact sheet screen in the Manage Sales Orders app:On Manage Sales Orders screen, enter search terms in filter bar, and choose Go.In search result, click your sales order number, and choose sales order number. |

### Create Sales Order Using IFRS15 Bundling Functionality (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note If you created a sales order with two line items using material IF11 and IF12 in the section [Create Sales Order](#unique_41) [page ] 63, follow the process below.For further information regarding bundling functionality in context of IFRS 15, please refer to SAP Note [2524569](https://me.sap.com/notes/2524569). |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose GoFor example, enter sales order number in Sales Order field. | Sales Order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Click sales order number, and choose Display Sales Orders .Note If there is not a Display Sales Orders , click Define Links. Select Display Sales Orders, and choose OK. | The Display Sales Orders xxx: Overview screen displays. |  |
| 5 | Check Condition Types | Select the line item, and choose Item Conditions. | The standalone selling price is displayed under condition type PSAM in the Amounts and Condition Value fields. |  |

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

### Review Blocked Sales Orders (Optional)

Follow the procesure for Review Blocked Sales Orders process step in the Basic Credit Management (BD6) scope item.

Purpose

In this process you review the sales orders that might have been blocked due to the credit limit check.

Procedure

Complete the activities of Review and Release or Reject a Sales Order described in the test script of Basic Credit Management (BD6) scope item.

### Process Sales Order Approval (Optional)

|  |
| --- |
| Note Only relevant if below conditions are fulfilled:Approval reason(s) is defined and assigned, details refer to the Define and Assign Approval Reasons chapter.The Cloud BAdI that returns an approval reasons is implemented, details refer to the Implement Cloud BADI chapter.Order reason is 005. |

#### Withdraw from Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to withdraw order approval.

Prerequisites

Sales manager has not yet made an approval decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Display Sales Order Screen | On the Manage Sales Orders screen, enter the respective order number created in previous step in the Sales Order and choose Go.Choose the sales order line that displays and choose the arrow. | The Display xxx Order xxx: Overview screen displays. |  |
| 4 | Withdraw Approval Request | In the menu bar at the top, choose More > Edit > Additional Functions > Withdraw Approval Request.Choose Continue to confirm the information shown as The approval request for sales document XXXXXXX was withdrawn. | The approval request is withdrawn.The Change xxx Order xxx: Overview screen displays. |  |
| 5 | Change Sales Order | On the Change xxx Order xxx: Overview screen, make some changes, for example:Valid to: <Enter a Date> | Approval status is changed to In Approval. |  |

#### Approve/Reject/Rework Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to make approval decision: release, reject or request rework.

Prerequisites

Approval status of the order is In Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox (F2097).Note You can also choose Notifications icon on the top-right corner to navigate to My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve/Reject/Rework Order | You receive the notification of the order. Choose one from the options on the bottom bar.Option 1: ReleaseOption 2: RejectOption 3: Request Rework | The Submit Decision dialog box displays. |  |
| 5 | Sumbit | Enter some comments and choose Submit. | Based on above decisions, choose next steps accordingly:• Release: the whole process ends, no subsequent step is needed.• Reject: the whole process ends, no subsequent step is needed.• Request Rework: go to Rework Sales order chapter. |  |

#### Rework Sales Order

|  |
| --- |
| Note Only relevant if the workflow is set as Request rework by sales manager previously. |

##### Check the Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the notifications.

Prerequisite

Approval status of the sales order is To be reworked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox (F2097).Note You can also choose Notifications icon on the top-right corner to navigate to My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Check Inbox | Check the inbox items with relative sales order. | Orders which needs to be reworked are displayed.• If rework is not required, sales representative can set Rework not Required in the inbox.• If rework is required, go to Change Sales Order chapter. |  |

##### Change Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to change sales order.

Prerequisites

Approval status of the sales order is rework.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Display Sales Order Screen | On the Manage Sales Orders screen, enter the respective order number created in previous step in the Sales Order and choose Go.Choose the arrow of the sales order line that displays. | The Display xxx Order xxx: Overview screen displays. |  |
| 4 | Navigate to Sales Order Screen | Choose Change. | The Change xxx Order xxx: Overview screen displays. |  |
| 5 | Change Sales Order | On the Change xxx Order xxx: Overview screen, make some changes and save, for example:Order Quantity: <Enter a New Quantity> | Approval status is changed to In Approval if the order amoun is higher than amount set in Implement Cloud BADI chapter.If amount >500 USD, go to Process Sales Order Approval chapter. |  |

### Advanced Available-to-Promise Processing (Optional)

Purpose

Follow the procedures in the Basic Available-to-Promise Processing (2LN) and Advanced Available-to-Promise Processing (1JW) scope item. This scope item describes the optional process for Advanced Available-to-Promise Processing.

1. From 2LN, the user can Trigger / Schedule BOP, execute a BOP Run and Monitor BOP Run.
2. From 1JW, the user can execute Release for Delivery.

Procedure

Complete all the activities described in the test script of Advanced Available-to-Promise Processing (1JW) scope item.

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully. Delivery number displays on Deliveries tab. |  |

|  |
| --- |
| Note Depending on the scope item settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management. |

To avoid open deliveries, ensure there is sufficient inventory quantity at the time for delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.

You may increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).

You may change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.

You may change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation Rejected with An Error Message.

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, Created by and other additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) |  |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the Delivery Number, and choose Continue.From the Outbound Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Outbound Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Outbound Delivery: Output screen, select the line with the DELIVERY_PICK_LIST Output Type, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

### Handling Unit Management (Optional)

Purpose

You can execute packing for delivery items right in a outbound delivery.

Procedure

Complete all the activities described in the test script of Handling Unit Management (4MM) scope item.

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

### Maintain Serial Numbers (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain serial number to the material.

Prerequisites

Run this step if Serial Number is used, such as TG20.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter the outbound delivery number, and choose Enter. |  |  |
| 4 | Navigate to Serial Numbers | On the Delivery XXXXXXXXX Change: Overview screen, choose Menu > Extras > Serial Numbers . |  |  |
| 5 | Maintain Serial Numbers | On the Maintain Serial Numbers screen, choose Create serial number automatically and choose Continue. |  |  |
| 6 | Save Document | Choose Save. |  |  |

### Split Outbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you split up single or multiple items from an existing, completely picked Outbound Delivery and move them to a new delivery document before posting Goods Issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Split Outbound Delivery (VLSP). |  |  |
| 3 | Enter Shipping Point | On the Split Outbound Delivery screen, make the following entry:Shipping Point:3310 |  |  |
| 4 | Enter Outbound Delivery | To speed up selection, make the following entry on the same screen:Outbound Delivery: <your Outbound Delivery Document Number> |  |  |
| 5 | Choose Split Profile | In the Split Profile field, make the following entry, and select the following value from the list:Split Profile: 0003 (Delivery Split - LE Components) |  |  |
| 6 | Start Selection | Choose Execute. | A list of outbound delivery items for the selected shipping point and outbound delivery displays. |  |
| 7 | Select Items for Split | Select the items that would become part of a new delivery or that would be split from the current delivery.Enter <Split Quantity> and choose Save Split. | The selected items display with a new delivery document number.The items not selected for the split still appear with the former document number. |  |

### Add Freight Costs (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to add the actual freight costs to the Outbound Delivery after knowing the exact weights and freight charges.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number, and choose Enter. |  |  |
| 4 | Open Conditions | From the menu, choose Menu > Goto > Header > Conditions . |  |  |
| 5 | Enter Condition Type | In the Condition Type column, input below entry (It’s allowed to enter each one or all of them):YBHD - FreightFPA1 - Packaging feeFIN1 - Insurance fee |  |  |
| 6 | Enter Freight Cost | In the Amount column, enter freight cost (such as YBHD 5, FPA1 10, FIN1 10).Note If condition type YBHD is added, the system distributes the entered amount across the delivery items. The distribution is executed on the basis of the net weight of each item.If condition type YBHD is not added, the distribution is executed the entered amount to the last item. |  |  |
| 7 | Save | Save your outbound delivery. | Freight Costs are added to the Outbound Delivery and will be later copied to the Invoice. |  |

|  |
| --- |
| Note The system distributes the entered amount across the delivery items. The distribution is executed on the basis of the net weight of each item. See also SAP Note [1921287](https://me.sap.com/notes/1921287)Pricing with Scale Conditions in Delivery with Batch Split. When you use the POD functionality (proof of delivery), freight costs in the delivery are not adjusted according to the quantities, weight and volume reported back in the POD. Freight costs are adjusted in the invoice based on POD. |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point/Receiving Pt: 3310 |  |  |
| 4 | Post Goods Issue | Select your outbound delivery note, and choose Post Goods Issues.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

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
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Proof of Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you record the quantities as confirmed by the respective customer after physical arrival of goods delivered. Thus document the right quantities that should become subject to billing to this customer.

This is only possible for Outbound Deliveries if the customer master data have been maintained in a way that this customer is "POD-relevant" (on sales area level).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery - Proof of Delivery (VLPOD). |  |  |
| 3 | Enter Outbound Delivery | On the same screen, make the following entry, and choose Continue:Outbound Delivery: <your Outbound Delivery Document Number> | The selected Outbound Delivery Document screen displays, and Overview POD tab becomes active. |  |
| 4 | Quantity Difference | If there is a quantity difference between shipping and receiving, go to step 5 and 6. |  |  |
| 5 | Enter POD Delivery Reason (Optional) | In the line with the item for which a differing quantity was reported by the customer, make the following entry or select the following value from the list:Reason: <DFG2(Underdelivery, reason unknown)> |  |  |
| 6 | Enter Deviation (Optional) | In the Quantity Difference field, go to Sales Unit (Qty Diffin Sales Un), enter <respective quantity (differs from the expected Delivery Quantity as per the Outbound Delivery Item)>, and choose Enter. | The quantity displayed for the respective item in the POD quantity field has been recalculated (Quantity Difference subtracted from Delivery Quantity).The value for POD Status field has changed to B (Differences Reported). |  |
| 7 | Confirm Delivery Proof | Choose Confirm Proof of Delivery. | The POD Date field has been filled with the current date.The value for the POD Status field has changed to C (Confirmed). |  |
| 8 | Save | Choose Save. | The Outbound Delivery document is saved with confirmation for actually delivered quantities.These will be used for the consecutive billing step. |  |

### Create Preliminary Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the billing clerk creates preliminary billing documents based on these billing due list items, adjusts view settings and filters to customize your experience.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Billing Documents (F2876). | The Create Preliminary Billing Documents screen displays. |  |
| 3 | Search for Billing Due List Items | To enable a filter, type in a value directly to trigger autosuggest and press Enter, or use the input help to choose a value. | The Sales Document is displayed in the result. |  |
| 4 | Define Preliminary Billing Settings | Choose Preliminary Billing Settings at the bottom and make the following settings:Set billing date and enter before creating Preliminary billing document - OFFCreate separate preliminary billing document for each item of billing due list - OFFDisplay preliminary billing document after creation - ON |  |  |
| 5 | Adjusting Settings | Choose Settings above the worklist to open the View Settings view.Each of the four tabs (Columns, Sort, Filter, Group) lets you perform a different function.The Columns tab allows you to add or remove columns from the worklist.You can search for the names of columns using the search field.You can choose Move Up or Move Down to change the order of the columns in the worklist.Choose Restore to restore the default. |  |  |
| 6 | Select An Item to Create Preliminary Billing Document | Select the document and choose Create | The Manage Preliminary Billing Documents screen displays. |  |
| 7 | In the Manage Preliminary Billing Documents App | The preliminary billing document with ID Pxxxxxxxx has been created. | The system generates a Preliminary Billing Document for billing. |  |
| 8 | Define Billing Settings | Choose Billing Settings at the bottom and make the following settings:Automatically Post Billing Documents - OFFDisplay Billing Document after creation - ON |  |  |
| 9 | Select the Preliminary Billing Document to be Invoiced | Select the Preliminary Billing Document you have created and choose Create Billing Document. | The system generates an invoice for sales document automatically. |  |

|  |
| --- |
| Note If you finished the above steps and created both the preliminary billing document and billing document, then please skip the next step Create billing Document. |

### Process Preliminary Billing Approval (Optional)

|  |
| --- |
| Note Only relevant if below conditions are fulfilled:Approval reason(s) is defined and assigned, details refer to the Define and Assign Approval Reasons chapter.The Cloud BAdI that returns an approval reasons is implemented, details refer to the Implement Cloud BADI chapter.Total amount of the order is not less than 500 USD. |

#### Finalize the Preliminary Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to send the preliminary billing document to approval process by finalizing the preliminary billing document.

Prerequisites

Automatically finalize preliminary billing documents after creation has not been turned on in Preliminary Billing Settings at Create Preliminary Billing App.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Preliminary Billing Documents (F2875). | The Manage Preliminary Billing Documents screen displays. |  |
| 3 | Navigate to Display Preliminary Billing Document Screen | On the Manage Preliminary Billing Documents screen, enter the preliminary billing document number created in previous step in the Preliminary Billing Document and choose Go. | The Preliminary Billing Document displays. |  |
| 4 | Finalize the Preliminary Billing Document | Highlight the Preliminary Billing Document by choosing the checkbox in front of the preliminary billing document number, choose Finalize.Note If Automatically finalize preliminary billing documents after creation is turned on in Preliminary Billing Settings at Create Preliminary Billing App, the document will set to Finalized status and In Approval status automatically. | The preliminary billing document is finalized and goes into approval process if it meets approval criteria set in prelimianry steps. |  |

#### Rework from Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to rework preliminary billing document from approval process.

Prerequisites

Preliminary Billing Document approver(s) have not made approval decision yet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Preliminary Billing Documents (F2875). | The Manage Preliminary Billing Documents screen displays. |  |
| 3 | Navigate to Display Sales Order Screen | On the Manage Preliminary Billing Documents screen, enter the Preliminary Billing Documents number created in previous step in the Preliminary Billing Documents and choose Go.Choose the Preliminary Billing Documents line that displays and choose the arrow. | The Display Preliminary Billing Documents xxx: Overview of items screen displays. |  |
| 4 | Rework Request | In the menu bar at the top, choose Change and then choose Rework. | The approval request is withdrawn.The Change Preliminary Billing Document xxx: Overview of items screen displays. |  |
| 5 | Change Preliminary Billing Document | On the Change Preliminary Billing Document xxx: Overview of items screen, make some changes and choose Save. | Approval status is changed to In Approval. |  |

#### Approve/Reject/Rework Preliminary Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to make approval decision: release, reject or request rework.

Prerequisites

Approval status of the order is In Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing approver you set in preliminary step. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox (F2097).Note You can also choose Notifications icon on the top-right corner to navigate to My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve/Reject/Rework Order | You receive the notification of the order. Choose one from the options on the bottom bar.Option 1: ReleaseOption 2: RejectOption 3: Request Rework | The Submit Decision dialog box displays. |  |
| 5 | Sumbit | Enter some comments and choose Submit. | Based on above decisions, choose next steps accordingly:• Release: this can be final status or document can send to approval again by using rework• Reject: the whole process ends, no subsequent step is needed.• Request Rework: go to Rework Preliminary Billing Document chapter. |  |

#### Rework Preliminary Billing Document

Only relevant if the workflow is set as Request rework previously.

##### Check the Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the notifications.

Prerequisite

Approval status of the preliminary billing document is to be reworked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox (F2097).Note You can also choose Notifications icon on the top-right corner to navigate to My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Check Inbox | Check the inbox items with relative sales order. | Preliminary billing documents which need to be reworked are displayed. |  |

##### Change Preliminary Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to change preliminary billing document.

Prerequisite

Approval status of the preliminary billing document is Rework.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Preliminary Billing Documents (F2875). | The Manage Preliminary Billing Documents screen displays. |  |
| 3 | Navigate to Display Pre-liminary Billing Document Screen | On the Manage Preliminary Billing Documents screen, enter the respective preliminary billing document number created in previous step and choose Go.Click the arrow of the preliminary billing document line that displays. | The Display Preliminary Billing Document xxx: Overview of items screen displays. |  |
| 4 | Choose Change | Choose Change. | The Change Preliminary Billing Document xxx: Overview of items screen displays. |  |
| 5 | Change Preliminary Billing Document | Make the necessary changes to this preliminary billing document and save it. | Approval status is changed to In Approval if the document amount is higher than amount set in Imple-ment Cloud BADI chapter.If amount >500 EUR, go to Approve/ Reject/ Rework Preliminary Billing Document chapter. |  |

### Create Partial Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create partial billing document. As described in [482506](https://me.sap.com/notes/482506), partial billing does not support material with batch split.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Input Delivery Number | Make the following entry, and choose Selection List:Document: <Delivery document> |  |  |
| 4 | Input Open Quantity | Choose the item, change Open quantity to smaller quantity, then choose Copy. |  |  |
| 5 | Save Billing Document | Choose Save. | The system generates an invoice for billing. |  |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Create Billing Document

Table 3: Overview

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with TMP xxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Document screen, choose Save.The draft version billing document with TMP xxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

Financial Postings

Table 4: Overview

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) |  | 41000000Rev Domestic Prod | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested you can see the financial document created in the IFRS ledger (Ledger Group 2L). |

Manage Billing Documents

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Search Billing Document | Enter the Billing document number recorded in previous step. Choose Enter. | The billing document created in previous step displays |  |
| 4 | Display Billing document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 5 | Check Output Condition | Choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT |  |
| 6 | Display Print Preview | Choose Preview. | Preview for PDF document displays. |  |
| 7 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel Billing Docs. | Message Billing Document Canceled displays. |  |
| 8 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing Save button in the footer bar. |  |  |
| 9 | Update New Text (Optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by pressing Save button in the footer bar. |  |  |

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

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Posting a Customer Invoice in Accounting and so on.Using the master data from this document, complete the following activities described in the test script:• Accounts Receivable (Sections Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items) |
| BKK - Sales Order Fulfillment Monitoring and Operations(Optional) | This scope item describes the collection of periodic activities, such as day ending activities or legal requirements.Using the master data from this document, complete all the activities described in the Test Script of the scope item: Sales Order Fulfillment Monitoring and Operations (BKK) (Chapters Review Sales Documents blocked for billing , Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents). |

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

#### Job Scheduling for Preliminary Billing Documents Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating preliminary billing documents.

This app can be used as an alternative instead of the manual creation of preliminary billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Creation of Preliminary Billing Documents (F4563). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Preliminary Billing Creation Schedule | Choose New to define a new job for preliminary billing creation. | The New Job screen displays. Job Template defaultly should be Preliminary Billing Document Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message You can go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A preliminary billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Preliminary Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Go, and the job list will refresh. | The log details displays. |  |

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
> Flagged while digesting this document, not verified: Sales order approval thresholds are inconsistent: the workflow purpose text says 1000 USD, the configuration step uses currency AED 1000, and the change-sales-order step refers to amount >500 USD.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Preliminary billing approval note says total amount not less than 500 USD, while the workflow example and rework step use EUR 500/1000.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/sell-from-stock-with-invoice-creation-before-goods-issue-7ua-ae-test-s]]
- related-to :: [[08-sales-order-management/test-script-sell-from-stock-consumer-products-5hl-ae-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 176,956 chars in the whole document
