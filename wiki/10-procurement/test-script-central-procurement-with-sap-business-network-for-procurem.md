---
id: 10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem
title: "Test Script: Central Procurement with SAP Business Network for Procurement (6BJ) (6BJ_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6BJ: central purchase orders and supplier confirmations via SAP Business Network."
cluster: 10-procurement
tags: [kb/procurement, topic/central-procurement]
aliases: [6BJ_S4CLD2608_BPD_EN_XX]
keywords: ["Central Requisitioning, Purchasing and Purchase Contracts", central procurement, sap business network, test script, purchase order creation, purchase order import, purchase order approval, central purchase orders, central supplier confirmation, supplier order confirmation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BJ_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1161
topic: 10-procurement/central-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Central Procurement with SAP Business Network for Procurement (6BJ) (6BJ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BJ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Requisitioning, Purchasing and Purchase Contracts** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Central Procurement with SAP Business Network for Procurement (6BJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232826023)

[2 Prerequisites 4](#_Toc232826024)

[2.1 Additional Manual Configuration 4](#_Toc232826025)

[2.2 System Access 4](#_Toc232826026)

[2.3 Roles 4](#_Toc232826027)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232826028)

[2.5 Preliminary Steps 6](#_Toc232826029)

[2.5.1 Activate Flexible Workflow for Purchase Orders 6](#_Toc232826030)

[2.5.2 Configure Flexible Workflow for Purchase Order 8](#_Toc232826031)

[2.5.3 Configure Flexible Workflow for Central Supplier Confirmations 9](#_Toc232826032)

[3 Overview Table 11](#_Toc232826033)

[4 Test Procedures 12](#_Toc232826034)

[4.1 Create Purchase Order 12](#_Toc232826035)

[4.2 Change Purchase Order (Optional) 13](#_Toc232826036)

[4.3 Import Purchase Orders 14](#_Toc232826037)

[4.4 Approve Purchase Order (Optional) 16](#_Toc232826038)

[4.5 Manage Purchase Orders Centrally 17](#_Toc232826039)

[4.6 Display Purchase Order (as a Supplier in SAP Business Network) 18](#_Toc232826040)

[4.7 Create Confirmation (as a Supplier in SAP Business Network (Optional)) 19](#_Toc232826041)

[4.8 Create Central Supplier Confirmation 20](#_Toc232826042)

[4.9 Approve Central Supplier Confirmation (Optional) 21](#_Toc232826043)

[4.10 Check Central Supplier Confirmation 22](#_Toc232826044)

[4.11 Check Purchase Order Confirmation (Optional) 23](#_Toc232826045)

## Purpose

Overview

Integrating SAP S/4HANA Cloud Public Edition with SAP Business Network through SAP Integration Suite, managed gateway for spend management and SAP Business Network supports the exchange of documents related to standard procurement processes, such as purchase orders and order confirmations.

Create central purchase orders in central procurement hub system by pooling purchase orders from connected systems, such as SAP ERP, SAP S/4HANA Cloud Public Edition, SAP S/4HANA or ECC. The purchase orders are sent to SAP Business Network and the required suppliers are notified. Suppliers submit their order confirmation through SAP Business Network. The supplier's order confirmation is sent from SAP Business Network to either hub or connected system. As soon as the supplier starts the release and approval process for a purchase order, the status is updated in the connected system.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b0abaabf383f5f411c3f148f3a16faba)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | The SAP S/4HANA Cloud Public Edition system acts as a hub system when it's connected to multiple connected systems.Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Connected System | Any ERP system with release ERP 6.0 and EHP 6 and higher with the HUBERPI add-on is considered as a connected system.Any SAP S/4HANA Cloud Private Edition system with release 1709 and higher with the HUBS4IC add-on is considered as a connected system.Any SAP S/4HANA Cloud Public Edition system with release 2308 or higher is considered as a connected system. |
| SAP Business Network | Access on [supplier.ariba.com](https://supplier.ariba.com) with the SAP Business Network Buyer and Supplier accounts. Your system administrator provides you with logon data. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_MM_SPT_CNTRL_PURCHASING_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 1010 | Plant 1 DE |  |
| Storage Location | 101A | Std. storage 1 |  |
| Storage Location | 101B | Std. storage 2 |  |
| Company Code | 1010 | Company Code 1010 |  |
| Purchase Organization | 1010 | Purch. Org. 1010 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor / Supplier | 10300085 | Vendor domestic German Ariba |  |
| Material | TG001 | Trading Good for Regular Procurement (PD planning) |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |
| BNG | Free Goods Processing |
| BNM | Free Goods Processing |

### Preliminary Steps

#### Activate Flexible Workflow for Purchase Orders

Use

This procedure describes how to activate the flexible workflow for purchase orders.

Prerequisites

To carry out the following activity, a business user with a business role must exist. The business role must contain the business catalog SAP_CORE_BC_COM (Communication Management), for example, the business role SAP_BR_ADMINISTRATOR (Administrator) is required.

Additionally, the business role SAP_BR_BPC_EXPERT must be assigned to the user

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Your Solution (APS_BCT_SPRO) app. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 4 | Search for Application Area | On the Configure Your Solution: Realize Phase screen, set the following search filters:Application Area: Sourcing and ProcurementSub Application Area: Operational Procurement | A search result list is displayed. |  |
| 5 | Select Configuration Item | From the search result list, select the Purchase Order Processing configuration item. | The Configure Your Solution - Purchase Order Processing screen is displayed. |  |
| 6 | Select Configuration Step | On the Configure Your Solution - Purchase Order Processing screen, in the Configuration Steps section, choose Configure for the Activate Flexible Workflow for Purchase Orders configuration step. | The Document Types Purchase order Change screen is displayed. |  |
| 7 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type: NB (Standard PO)Scenario based workflow: Select the checkbox. | The scenario-based workflow is active for standard purchase orders.If you’re asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue.Choose Save. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). |  |  |
| 3 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type: NB (Standard PO)Scenario based workflow: Select the checkbox. | The scenario-based workflow is active for standard purchase orders.If you’re asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue.Choose Save. |  |

#### Configure Flexible Workflow for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, you configure your release conditions for the approval of purchase orders.

|  |
| --- |
| Note Before you start this procedure, ensure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Access App | Open the Manage Workflows for Purchase Orders (F2872) app. | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow for Supplier Quotations | Choose Create. On the New Workflow screen, enter a workflow name in the Workflow Name field, for example, Test Workflow for Purchase Order.Select the Start Conditions tab. In the Only start the workflow if all of the following preconditions are met: field, select Purchasing group of purchase order is from the dropdown list and enter 001.Choose Create Alternative Preconditions and enter the following data:In the Only start the workflow if all of the following preconditions are met: field, select Total net amount of purchase order is greater than from the dropdown list and enter the following data:Amount: 100Currency: EURSelect the Steps tab. Choose Create.On the New Step screen, select the Header tab. In the Step Type field, select Release of Purchase Order from the dropdown list.Select the Recipients tab and select the following settings:Assignment By: RoleRole: Manager of Workflow InitiatorStep to be completed by: One of the recipientsChoose Create > Save . | The workflow for a purchase order is created. |  |
| 4 | Activate Workflow Item | On the Workflow Details screen, select the workflow item that you've created and choose Activate. | The workflow item is activated. |  |

#### Configure Flexible Workflow for Central Supplier Confirmations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, you configure your release conditions for the central supplier confirmation.

|  |
| --- |
| Note Before you start this procedure, ensure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Access App | Open the Manage Workflows for Central Supplier Confirmations (F6635) app. | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow for Supplier Quotations | Choose Create. On the New Workflow screen, enter a workflow name in the Workflow Name field, for example, Test Workflow for Central Supplier COnfirmations.Select the Start Conditions tab. In the Only start the workflow if all of the following preconditions are met: field, select Purchasing organization of centrally managed purchase order is from the dropdown list and enter your purchasing organization.Select the Steps tab. Choose Create.On the Automatic Release of Central Supplier Confimation screen, select the Header tab. In the Step Type field, select Release of Central Supplier Confirmation from the dropdown list.Select the Recipients tab and select the following settings:Assignment By: UserUser: <Purchasing Manager>Step to be completed by: One of the recipientsChoose Create > Save . | The workflow for a purchase order is created. |  |
| 4 | Activate Workflow Item | On the Workflow Details screen, select the workflow item that you've created and choose Activate. | The workflow item is activated. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_11) [page ] 12 | Purchaser | Manage Purchase Orders (F0842A) | A new purchase order is created. The system message Purchase order has been created is displayed. |
| [Change Purchase Order (Optional)](#unique_12) [page ] 13 | Purchaser | Manage Purchase Orders (F0842A) | The purchase order is saved. The system message Purchase Order xxx updated. is displayed. |
| [Import Purchase Orders](#unique_13) [page ] 14 | Configuration Expert - Business Process Configuration | Schedule Import of Purchasing Documents (F3268) | The purchase order import is completed. |
| [Approve Purchase Order (Optional)](#unique_14) [page ] 16 | Purchasing Manager | My Inbox - All Items (F0862) | The purchase order is approved. |
| [Manage Purchase Orders Centrally](#unique_15) [page ] 17 | Purchaser - Central Procurement | Manage Purchase Orders Centrally (F3292) |  |
| [Display Purchase Order (as a Supplier in SAP Business Network)](#unique_16) [page ] 18 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The purchase order is displayed. |
| [Create Confirmation (as a Supplier in SAP Business Network (Optional))](#unique_17) [page ] 19 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The purchase order is confirmed. |
| [Create Central Supplier Confirmation](#unique_18) [page ] 20 | Purchaser - Central Procurement | Manage Central Supplier Confirmations (F6634) | The central supplier confirmation is created. |
| [Approve Central Supplier Confirmation (Optional)](#unique_19) [page ] 21 | Warehouse Clerk | Post Goods Receipt for Inbound Delivery (F2502) | The goods receipt for inbound delivery is posted. |
| [Check Central Supplier Confirmation](#unique_20) [page ] 22 | Purchaser - Central Procurement | Manage Central Supplier Confirmations (F6634) | You've checked the central supplier confirmation. |
| [Check Purchase Order Confirmation (Optional)](#unique_21) [page ] 23 | Purchaser | Manage Purchase Orders (F0842A) | You've checked whether the approval or rejection information of the central supplier confirmation is synced to the purchase order. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a purchase order in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori Launchpad as Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Enter Purchase Order Data | Choose Create.On the General Information tab, in the Basic Data section, enter the following data:Purchase Order Type: Standard PO (NB)Supplier: 10300085Currency: EUROn the General Information tab, in the Organization section, enter the following data:Purchasing Group: 001Purchasing Organization: 1010Company Code: 1010On the Items tab, choose Create, and enter the following data:Material: SP001Plant: 1010Order Quantity: 100 PCNet Order Price: 100 EURPrice Unit: 1 PCTo see further details of the line item, choose  . The Purchase Order Item screen is displayed.On the Supplier Confirmation Control tab, enter the following data:Confirmation control: Confirmations (Select the checkbox.) |  |  |
| 4 | Change Delivery Address | Go to the Delivery Address tab. Change the delivery address according to your business requirements.Choose Apply. | The delivery address is changed and the New Purchase Order screen is displayed. |  |
| 5 | Attach File | Go to the Attachments tab. To upload an attachment, choose Upload.Select an attachment and choose Open. | The uploaded file is displayed in the Attachments section. |  |
| 6 | Save Purchase Order | To save the purchase order, choose Order. | A new purchase order is created. The system message Purchase order has been created is displayed.Note Write down the purchase order number to use it for further configuration steps. |  |

### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed.A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Select the row of a purchase order. | The Edit Purchase Order xxx screen is displayed. The purchase order is opened in Change mode. |  |
| 4 | Change Purchase Order | Change certain field values of the purchase order according to your business requirements. | The purchase order values are changed. |  |
| 5 | Check Purchase Order for Completeness | Choose Simulate. | The purchase order is complete. |  |
| 6 | Follow Up on Error Messages | If an error or warning message is displayed, a correction of the purchase order data is necessary. If no message is displayed, the purchase order is complete. |  |  |
| 7 | Save Purchase Order | To save the purchase order, choose Submit. | The purchase order is saved. The system message Purchase Order xxx updated. is displayed. |  |

### Import Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a purchase order is created in the connected system, you can schedule the import of the purchasing documents to the hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Schedule Import of Purchasing Documents (F3268) app. | The Application Jobs screen is displayed. |  |
| 3 | Create New Import Job | On the Application Jobs screen, choose Create.On the Template Selection screen, enter the following data according to your business requirements:Job Template: Import Purchase Orders from Connected SystemsJob Name: Import Purchase Orders from Connected SystemsChoose Step 2.Go to the Scheduling Options screen and enter the following data according to your business requirements:Start Immediately: Select the checkbox.Choose Step 3.On the Parameters screen, enter the following data according to your business requirements:Import Type: Ad Hoc ImportConnected System ID: <Connected System ID>, for example QIASCCDocument Type: <Purchase Order Document Type in Connected System>, for example, CPOPurchase Order from: <Purchase Order Document Number created in Connected System>Purchase Order to: <Purchase Order Document Number created in Connected System> | The Application Jobs Detail screen is displayed. |  |
| 4 | Schedule the Job | Choose Schedule. | The Import Purchase Orders from Connected Systems job is scheduled. |  |
| 5 | Check Import Job Status | On the Application Jobs screen, choose Log for the job you've scheduled.Check the import status in the Job Details. | The purchase order import is completed. |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve a purchase order in the hub system.

|  |
| --- |
| Note Purchase orders with a net value of 500 USD (global release amount is configured in USD, and converted to the country/region currency amount), or more require an approval (for Purchasing Group 001 and 003). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen with a list of already created purchase orders that need to be approved is displayed. |  |
| 3 | Select Purchase Order | To search for a specific purchase order, enter the required search criteria.From the search result list, select a purchase order. | The Purchase Order xxx is displayed.Purchase orders without follow-on documents (w/o status Follow-On Documents), and a net value of 500 USD or more have the status In Approval. |  |
| 4 | Approve the Purchase Order | Choose Approve.If required, enter the approval reason. Choose Submit. | The purchase order is approved. |  |

### Manage Purchase Orders Centrally

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manage the purchase order centrally in the hub system, ater it was imported from the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders Centrally (F3292) app. | The Manage Purchase Orders Centrally screen is displayed |  |
| 3 | Search for Purchase Orders | To search for a specific purchase order, enter the required search criteria.From the search result list, select a purchase order.Note By default, the Unified Key Mapping filter that enables the search and display of purchase order attributes is enabled. This search is based on the key mapping of suppliers and materials in the hub system. You can also disable the Unified Key Mapping switch to perform the regular search of purchase order items. To do this, choose Adapt Filters and disable the filter. | The Central Purchase Order screen is displayed. |  |
| 4 | Review Purchase Order | On the Central Purchase Order screen, review the data of your purchase order.Note To display your purchase order in the connected system, you can choose Open Document. |  |  |
| 5 | Display Output Details | On the Central Purchase Order screen, go to the Output Management section.If the purchase order document is in status Active or Release, you can check its output details.Note If the Dispatch Time is in status Scheduled, use the Schedule Output for Centrally Managed Purchase Order (F5471) app to schedule the output.To enable output management, go to the Schedule Import of Purchasing Documents (F3268) app to enable the Import Texts for Purchasing Documents from Connected Systems job template. |  |  |

### Display Purchase Order (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select the Purchase Order | Choose Orders > Purchase Orders . Select a Purchase Order ID. | The purchase order is displayed. |  |

### Create Confirmation (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Purchase Orders .Open the Search Filters pane. In the Date Range field, choose Last 24 Hours from the dropdown list. Choose Search. | A list of newly created purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Confirm Purchase Order | Choose Create Order Confirmation > Confirm Entire Order . Enter the following data:Supplier Reference:: PO Confirmation for MaterialEst. Delivery Date: <Delivery Date>Choose Next > Submit . | The status of the purchase order is changed to Confirmed. |  |
| 5 | Return to Orders and Releases | To return to the list of purchase orders, choose Done. | The list of purchase orders is displayed. |  |

### Create Central Supplier Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create the central supplier confirmation for a purchase order in the hub system.

|  |
| --- |
| Note If the confirmation comes via SBN, the system creates an automatic confirmation. You don't need to perform this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Central Supplier Confirmations (F6634) app. | The Manage Central Supplier Confirmation screen is displayed |  |
| 3 | Create Central Supplier Confirmation | On the Manage Central Supplier Confirmation screen, choose Create.On the Central Supplier Confirmation screen, enter your purchase order number in the Reference Purchase Order field. |  |  |
| 4 | Create Confirmation Item | Go to the Confirmation Item section and choose Create.On the Central Supplier Confirmation Item screen, enter your purchase order item number in the Item field. |  |  |
| 5 | Create Confirmation Line | Go to the Confirmation Line section and choose Create.On the Confirmation Line screen, enter the following data according to your business requirements:Delivery Date: TodayConfirmed Quantity: <Confirmed Quantity>Choose Apply. |  |  |
| 6 | Create Supplier Confirmation | On the Central Supplier Confirmation screen, choose Create. | The central supplier confirmation is created. |  |

### Approve Central Supplier Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve the central supplier confirmation in the hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchasing Manager. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F6012) app. | The My Inbox screen is displayed. |  |
| 3 | Search for Central Supplier Confirmation | On the My Inbox screen, enter your central supplier confirmation number in the search area. Choose Search. |  |  |
| 4 | Approve Central Supplier Confirmation | Select the central supplier confirmation and choose Approve. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Optionally, enter an approval reason and choose Submit. | The central supplier confirmation is approved. |  |

### Check Central Supplier Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the central supplier confirmation for a purchase order in the hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Central Supplier Confirmations (F6634) app. | The Manage Central Supplier Confirmation screen is displayed |  |
| 3 | Select Central Supplier Confirmation | On the Manage Central Supplier Confirmation screen, select the central supplier confirmation that you've created in [Create Central Supplier Confirmation](#unique_18) [page ] 20. | The Central Supplier Confirmation screen is displayed. |  |
| 4 | Open Central Supplier Confirmation | Expand the Item Details section and go to the Confirmations tab.Check whether the central supplier confirmation number in the Reference column matches the purchase order confirmation number in SAP Business Network. | You've checked the central supplier confirmation. |  |

### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check whether the approval or rejection information of the central supplier confirmation is synced to the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed |  |
| 2 | Access App | Open the Manage Purchase Orders Centrally (F3292) app. | On the Manage Purchase Orders Centrally screen, a list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Select the row of the purchase order you created in [Create Purchase Order](#unique_11) [page ] 12. | The Standard PO XXX screen is displayed. |  |
| 4 | Open Confirmations | Expand the Item Details section and check whether the approval or rejection information of the central supplier confirmation is synced to the purchase order. | You've checked whether the approval or rejection information of the central supplier confirmation is synced to the purchase order. |  |

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
> Flagged while digesting this document, not verified: Overview Table lists 'Approve Central Supplier Confirmation (Optional)' as role Warehouse Clerk with app Post Goods Receipt for Inbound Delivery (F2502), while the test procedure for that step uses the Purchasing Manager role and My Inbox - All Items (F6012).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Purchase order approval threshold differs: the Approve Purchase Order note says orders of 500 USD or more need approval (purchasing groups 001 and 003), while the sample flexible workflow starts for purchasing group 001 with total net amount greater than 100 EUR.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample master data lists material TG001, but the Create Purchase Order step enters material SP001, which is not in the master data table.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchasing-2xt-88]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BJ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 40,177 chars in the whole document
