---
id: 10-procurement/test-script-guided-buying-capability-with-sap-ariba-buying-2nv-ae-836
title: "Test Script: Guided Buying Capability with SAP Ariba Buying (2NV_AE) (2NV_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2NV (AE): guided buying with SAP Ariba Buying, from shopping cart to PR, PO, GR/SES and supplier invoice."
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-guided-buying]
aliases: [2NV_S4CLD2608_BPD_EN_AE]
keywords: [Guided Buying with SAP Ariba Buying, guided buying, shopping cart, purchase requisition, purchase requisition approval, flexible workflow, purchase order creation, service entry sheet, goods receipt, supplier invoice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NV_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-836
topic: 10-procurement/ariba-guided-buying
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Guided Buying Capability with SAP Ariba Buying (2NV_AE) (2NV_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NV_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Guided Buying with SAP Ariba Buying** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Guided Buying Capability with SAP Ariba Buying (2NV_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849636)

[2 Prerequisites 4](#_Toc232849637)

[2.1 Additional Manual Configuration 4](#_Toc232849638)

[2.2 System Access 4](#_Toc232849639)

[2.3 Roles 4](#_Toc232849640)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232849641)

[2.5 Business Conditions 6](#_Toc232849642)

[2.6 Preliminary Steps 7](#_Toc232849643)

[2.6.1 Check Flexible Workflow for Purchase Requisition Approval 7](#_Toc232849644)

[2.6.2 Configure Flexible Workflow for Purchase Requisition 8](#_Toc232849645)

[2.6.3 Automatic PO Creation from PR (Optional) 9](#_Toc232849646)

[2.6.4 Configure the Commodity Code Mapping Policy for Limit Items (Optional) 10](#_Toc232849647)

[2.6.5 Configure Automatic Creation of Reservation for Inventory Items (Optional) 11](#_Toc232849648)

[2.6.6 Create Catalogs for Inventory Items (Optional) 12](#_Toc232849649)

[3 Overview Table 13](#_Toc232849650)

[4 Test Procedures 15](#_Toc232849651)

[4.1 Open Guided Buying App (Optional) 15](#_Toc232849652)

[4.2 Create Shopping Cart 16](#_Toc232849653)

[4.3 Create Purchase Requisition 20](#_Toc232849654)

[4.4 Approve Shopping Cart 21](#_Toc232849655)

[4.5 Update Purchase Requisition 22](#_Toc232849656)

[4.6 Create Reservation (Automated) 23](#_Toc232849657)

[4.7 Display Shopping Cart 24](#_Toc232849658)

[4.8 Post Goods Movement 24](#_Toc232849659)

[4.9 Create Purchase Order (Automated) 25](#_Toc232849660)

[4.9.1 Create Purchase Order (Manually) 26](#_Toc232849661)

[4.10 Display Shopping Cart 27](#_Toc232849662)

[4.11 Create Service Entry Sheet 27](#_Toc232849663)

[4.12 Display Shopping Cart 29](#_Toc232849664)

[4.13 Post Goods Receipt 29](#_Toc232849665)

[4.14 Display Shopping Cart 31](#_Toc232849666)

[4.15 Create Supplier Invoice 32](#_Toc232849667)

[4.16 Display Shopping Cart 33](#_Toc232849668)

[5 Appendix 34](#_Toc232849669)

[5.1 Process Integration 34](#_Toc232849670)

[5.1.1 Preceding Processes 34](#_Toc232849671)

[5.1.2 Succeeding Processes 34](#_Toc232849672)

## Purpose

Overview

The guided buying capability creates a simple, smart, and elegant purchasing experience that increases user engagement across all spend areas. Guided buying serves as a central place where all buyers can shop across all goods and services. It enables procurement and individual line-of-business owners to specify procurement policies and inform and guide users whenever there appear to be policy conflicts. These capabilities enable purchasers to collaborate directly with suppliers and other procurement users in the context of the procurement need, making procurement more efficient.

Users find items across catalogs, including partial items, forms, and suppliers in a single search box. All spend contracted through supplier-provided catalogs and punch-out catalogs is available for the user to search. Using online shopping as an example, users can filter items by price or manufacturer.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/fd05fe374d3c479883be7590513b9db0)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table, you still see the master data used for the current baseline.

Essential master data and organizational data were created in your SAP S/4HANA Cloud Public Edition system in the implementation phase. It includes data that reflects the organizational structure of your company and master data that suits its operational focus. For example, master data for materials, vendors, and customers.

This master data consists of standardized SAP Best Practices default values and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values, which have the same characteristics.Check your SAP system to look out for other existing material master data.Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material Group | L001 | Account Billed |  |
| Plant | 3310 | Plant 1 AE |  |
| Vendor | 33300080 |  |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| G/L Account | 65100000 |  |  |
| Cost Center | 33101201 |  |  |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. So you must have completed the following processes and fulfilled the following business conditions before going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 1NT - Project Control – Finance | Project Financial Control |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period master data script. Posting Period is up to date. |

### Preliminary Steps

#### Check Flexible Workflow for Purchase Requisition Approval

Purpose

In this procedure, you activate flexible workflow for purchase requisition approval.

In our test script, it describes a scenario in which the purchase requisition is manually approved in the Ariba realm and automatically approved in SAP S/4HANA Cloud Public Edition.

If you want an automatic approval process for purchase requisition in SAP S/4HANA Cloud Public Edition, you have to process the following steps:

- Check Flexible Workflow for Purchase Requisition Approval
- Configure Flexible Workflow for Purchase Requisition

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search for the following configuration step: Activate Flexible Workflow for Purchase Requisitions. Choose Go.In the search result, select the configuration activity and go to the next screen.On the Configure Your Solution - Requirements processing screen, go to the Activate Flexible Workflow for Purchase Requisitions and choose Configure. | The Document Types Purchase Requisitions Change screen is displayed. |  |
| 5 | Activate Flexible Workflow for PR Approval | Check whether the following entry is selected for NB and NBS:scenario based workflow: X | The Flexible workflow is active for Purchase Requisitions with Document Type: NB and NBS. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Requisitions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase Requisitions Change screen is displayed. |  |
| 3 | Activate Flexible Workflow for PR Approval | Check whether the following entry is selected for NB and NBS:scenario based workflow: X | The Flexible workflow is active for Purchase Requisitions with Document Type: NB and NBS. |  |

#### Configure Flexible Workflow for Purchase Requisition

Purpose

In our test script, it describes a scenario in which the purchase requisition is manually approved in the Ariba realm and automatically approved in SAP S/4HANA Cloud Public Edition.

If you want an automatic approval process for Purchase requisition in SAP S/4HANA Cloud Public Edition, do as follows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert. |  |  |
| 2 | Open Manage Workflow for Purchase Requisitions | Open Manage Workflows for Purchase Requisitions (F2705). |  |  |
| 3 | Create Manage Workflow | Select Release of Purchase Requisition Item, choose Add , and then enter the following details:Name: <Enter a workflow name, for example, PR Workflow for Ariba>Preconditions: <From the dropdown list, choose External approval status of purchase requisition item is>ExternalApprovalStatus: AStep Sequence: AddStep Type: Automatic Release of Purchase Requisition ItemChoose Add and then Save. | The automatic workflow for Purchase Requisition is configured. |  |
| 4 | Activate Workflow Item | Select the newly created workflow item and choose Activate. | The workflow item is now activated. |  |
| 5 | Define Order | Choose Define Order.In the dialog box, adjust the workflow that you created accordingly, so that the order of the workflow is Number 1 in the queue. | Define the priority for workflow. |  |

#### Automatic PO Creation from PR (Optional)

This step is valid only if you want to automate the Purchase Order creation process.

Prerequisites

The Schedule Purchasing Jobs - Advanced (F1702) app must be available.

Procedure

|  |
| --- |
| Note For SAP Central Business Configuration, log on to the project experience in SAP Central Business Configuration. Go to the Business Processes Configuration app. Then continue from there with the relevant step given in the procedure.Otherwise, proceed as follows: |

1. Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data.
2. Open the Maintain Business Partner (BP) app.
3. On the Maintain Business Partner screen, choose the Find tab on the left navigation pane.
    - Find: Business Partner
    - By: Vendor Number
    - Supplier: 33300080

, for example

1. Choose Enter and double-click the Partner ID on the left navigation panel.
2. On the Display Organization: <XXXXXXXX> screen:
    - Business Partner: 33300080, for example
    - Display in BP role: Supplier
3. Choose Purchasing, and under Purchasing Organization, choose Purchasing Data.
4. In the Additional Purchasing Data tab, select Automatic PO.

|  |
| --- |
| Note Ensure that you are now in Change mode. |

1. Log out.
2. Log on to the SAP Fiori launchpad using the Purchaser role.
3. Open the Schedule Purchasing Jobs - Advanced (F1702) app.
4. Choose New.
5. In the General Information section:
    - Job Template: Automatic Creation of Purchase Orders from Requisitions
    - For Single Run:
        - Select the Start Immediately checkbox.
        - Start: <Start Date> <Start Time>
6. For Recurring:
    - Choose Add More Scheduling Options.
    - Select the Start Immediately checkbox.
    - Select the Recurrence checkbox.
    - Recurrence Pattern: <Hourly or Daily>, for example
    - End: <Select After or By>
7. In the Parameter Section area, under Header Specific Selection:
    - Fixed Supplier: <Supplier number>
8. Under Item Specific Selection:
    - Material Group: L001, for example
9. Under New Purchase Order, select Per Requisition.

#### Configure the Commodity Code Mapping Policy for Limit Items (Optional)

This step is valid only if you want to add limit items in guided buying requests for goods and lean services that correspond to the item category 'E' in SAP S/4HANA Cloud Public Edition. Limit items are procured without following the goods receipt and the service sheet processes. The requests for limit items are characterized by validity periods to define the effective dates of the procurement process and predefined amount limits to control item prices.

Purpose

In this procedure, you configure your commodity code mapping policy to define the commodity codes for which users can create standing orders.

Procedure

To configure your commodity code mapping policy, see the instructions at [How to Configure Your Commodity Code Mapping Policy](https://help.sap.com/viewer/855d3e61ce304b1cb81987bdc5322911/cloud/en-US/f761946d2edc4a20abfb9645e954ecef.html?q=How%20to%20configure%20your%20commodity%20code%20mapping%20policy).

#### Configure Automatic Creation of Reservation for Inventory Items (Optional)

This step is valid only if you want to purchase an inventory item.

|  |
| --- |
| Note As a prerequisite, the requested item must have an open, unrestricted stock. You can check this using Fiori app Display Stock Overview (log on as Warehouse Clerk). |

Purpose

In this procedure, you configure the automatic creation of reservation for a purchasing group and material group combination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert. |  |  |
| 2 | Open Settings for Creation of Reservation | Open Settings for Creation of Reservation. |  |  |
| 3 | Maintain Values | Under General Settings section, enter the following details:Rules: <Goods Issue (03)>Movement Type: <GI for cost center (201)>Under Requisition Identifiers section, enter the purchasing group and material group combination for which you want to enable the atutomatic creation of reservation:Purchasing Group: <enter the purchasing group of the inventory item, for example, 002>Material Group: <enter the material group of the inventory item, for example, L001>Auto-Reservation: ONCheck Unrestricted Stock Only: <If the checkbox is selected, then the checking rule is bypassed, and availability is determined based only on the stock that is available for unrestricted use.>Choose Save. |  |  |

#### Create Catalogs for Inventory Items (Optional)

This step is valid only if you want to purchase an inventory item.

Purpose

In this procedure, the supplier or buyer will create the catalogs for inventory items, which can be purchased via SAP Ariba Buying (with guided buying capability enabled).

Procedure

Both supplier and buyer can create the catalog for inventory items by first preparing the Catalog Interchange Format (CIF) file. For more detailed information about CIF, see [Topics about CIF catalogs](https://help.sap.com/viewer/43cc25c2fa9d4789b058784e816a2af8/LATEST/en-US/dd8ab5cbf0181014b2b3f8e513c6b6ee.html).

Suppliers can create and publish catalogs via SAP Network for Trading Partners, see the instructions at [How to create and publish catalogs](https://help.sap.com/viewer/1e9220c0f83d42d097418c387d3bea9b/LATEST/en-US/ddaf99d2f01810148790eb55a113e8aa.html).

Buyers can import local catalogs for SAP Ariba Procurement solutions, see the instructions at [How to import local catalogs](https://help.sap.com/viewer/c9b2518a80f1409aae8660cd58612a65/LATEST/en-US/6a6064a8c1da1014922ef287e2d82c26.html).

## Overview Table

The Guided Buying Capability with SAP Ariba Buying (2NV) scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | BusinessRole | App/Transaction | Expected Result |
| --- | --- | --- | --- |
| [Open Guided Buying App (Optional)](#unique_15) [page ] 15 | Employee | Custom tile created in the set-up instructions (in the Create Guided Buying App chapter) | The Guided Buying with SAP Ariba Buying login screen is displayed.Note User will log in to Guided Buying automatically, if the Single Sign-On for SAP Ariba is configured. |
| [Create Shopping Cart](#unique_16) [page ] 16 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is created and transferred to the SAP S/4HANA Cloud Public Edition system. |
| [Create Purchase Requisition](#unique_17) [page ] 20 | Purchaser | Display Purchase Requisitions (ME5A) | Purchase Requisition Details are displayed in the SAP S/4HANA Cloud Public Edition system, with Block ID: Blocked by requester. |
| [Approve Shopping Cart](#unique_18) [page ] 21 | Compliance Approver (GRC) | Guided Buying with SAP Ariba Buying | Shopping cart is approved. |
| [Update Purchase Requisition](#unique_19) [page ] 22 | Purchaser | Display Purchase Requisitions (ME5A) | Purchase Requisition Details are displayed in the SAP S/4HANA Cloud Public Edition system, with Block ID: Not Blocked. |
| [Create Reservation (Automated)](#unique_20) [page ] 23 | Automated step | Automated step | Reservation is created in the SAP S/4HANA Cloud Public Edition system. |
| [Display Shopping Cart](#unique_21) [page ] 24 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with reservation ID. |
| [Post Goods Movement](#unique_22) [page ] 24 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Create Purchase Order (Automated)](#unique_23) [page ] 25 | Automated step | Automated ( Schedule Purchasing Jobs - Advanced (F1702)) step | PO is created from PR in the SAP S/4HANA Cloud Public Edition system. |
| [Create Purchase Order (Manually)](#unique_24) [page ] 26 | Purchaser | Manual ( Process Purchase Requisitions - Deprecated (F1048)) | PO is created from PR in the SAP S/4HANA Cloud Public Edition system. |
| [Display Shopping Cart](#unique_25) [page ] 27 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with PO number. |
| [Create Service Entry Sheet](#unique_26) [page ] 27 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | Service Entry Sheet is created in the SAP S/4HANA Cloud Public Edition system. |
| [Display Shopping Cart](#unique_27) [page ] 29 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with service entry sheet number. |
| [Post Goods Receipt](#unique_28) [page ] 29 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | GR is created from PR in the SAP S/4HANA Cloud Public Edition system. |
| [Display Shopping Cart](#unique_29) [page ] 31 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with GR number in SAP Ariba Buying. |
| [Create Supplier Invoice](#unique_30) [page ] 32 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Invoice is created in the SAP S/4HANA Cloud Public Edition system. |
| [Display Shopping Cart](#unique_31) [page ] 33 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with Invoice number in SAP Ariba Buying. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Open Guided Buying App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you open Guided Buying with SAP Ariba Buying.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Employee. |  |  |
| 2 | Go to Menu Path | For example, choose Purchase Requisition Processing > Guided_Buying (created in the set-up instructions, in the Create Guided Buying App chapter). | The Guided Buying with SAP Ariba Buying login screen appears in a new window.Note User will log in to Guided Buying automatically, if the Single Sign-On for SAP Ariba is configured. |  |

### Create Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you see newly created shopping cart in Guided Buying with SAP Ariba Buying.

Procedure

Option 1 - Create shopping cart for a non-catalog item:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. |  |  |
| 2 | Go to Menu Path | On the right navigation pane, choose Quick Links, and then select Request Adhoc Item. |  |  |
| 3 | Maintain Values | Maintain the required parameters.Note On the upper left, you can choose to create the purchase requisition for goods or for lean service, by selecting Goods or Services.The following are the field names and example values for Goods:For limit items:Product Name: <Free text of the product you want to purchase>Category: <Category configured during your Ariba Buying setup for goods limit items>Description: <Free text>This is a limit item: <select the checkbox>Start date: <Today>End date: <Today+7>Expected value: 100Overall limit: 150For non-limit items:Product Name: <Free text of the product you want to purchase>Category: <Category configured during your Ariba Buying setup for goods>Description: <Free text>Quantity: 10Unit of Measure: EachUnit price: 10The following are the field names and example values for Services:For limit items:Service Name: <Free text of the service you want to purchase>Category: <Category configured during your Ariba Buying setup for service limit items>Description: <Free text>This is a limit item: <select the checkbox>Start date: <Today>End date: <Today+7>Expected value: 100Overall limit: 150For non-limit items:Service Name: <Free text of the service you want to purchase>Category: <Category configured during your Ariba Buying setup for service>Description: <Free text>Quantity: 1Unit of Measure: Choose the UoM for your serviceService Amount: 10 |  |  |
| 4 | Add to Cart and Checkout | Choose Add to Cart and in the dialog box, choose Checkout. |  |  |
| 5 | Maintain Parameters | In the checkout screen, maintain the required parameters.Note The values given are example values.DataTitle: <Free text>Need-by Date: <Today+1>Vendor: <Vendor configured during your SAP Ariba Buying setup, which is mapped to supplier 33300080>.AccountingAccount Assignment: <K> <Cost Center>Account Type: <Cost Center>Bill To: <1710>G/L Account: <65100000>Cost Center: 33101201ShippingPlant: 3310Purchasing Group: 001Deliver To: <Employee name>AttachmentsOptional input based on your requirements: drag and drop your attachments here, or choose the browse button to upload your fileOthersCommodity Code: <Category you selected when creating the shopping cart>Item Category: <Material or Service, depending on the item type you are purchasing>Payment Terms: <Net45>Purch Org: 3310 |  |  |
| 6 | Send Request | Choose Submit.Note After the requisition is submitted, it is now supported for adding an additional line item while editing the non-limit items requisition. | A message appears informing you that you've sent your request for approval. |  |
| 7 | Note down the PR number | Note down the number PR<XXXX>. | PR<XXXX> status: Submitted |  |
| 8 | Note down the ERP Reference ID | Note down the ERP Reference ID number. (This is the PR number created in the SAP S/4HANA Buyer system.) |  |  |

Option 2 - Create shopping cart for an inventory item:

|  |
| --- |
| Note In order to test with an inventory item, you need to first complete chapters [Configure Automatic Creation of Reservation for Inventory Items (Optional)](#unique_12) [page ] 11 and [Create Catalogs for Inventory Items (Optional)](#unique_13) [page ] 12 as mentioned in the Preliminary Steps section. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. |  |  |
| 2 | Search for the inventory item | On the upper pane, search for the inventory item that you've configured in Preliminary Steps. |  |  |
| 3 | Maintain Values | Maintain the required parameters.Quantity: 1 |  |  |
| 4 | Add to Cart and Checkout | Choose Add to Cart and in the dialog box, choose Checkout. |  |  |
| 5 | Maintain Parameters | In the checkout screen, maintain the required parameters.Note The values given are example values.DataTitle: <Free text>Need-by Date: <Today+1>AccountingAccount Assignment: <K> <Cost Center>Account Type: <Cost Center>Bill To: <1710>G/L Account: <65100000>Cost Center: 17101201ShippingPlant: 1710Purchasing Group: 001Deliver To: <Employee name>OthersPurch Org: 1710 |  |  |
| 6 | Send Request | Choose Submit. | A message appears informing you that you've sent your request for approval. |  |
| 7 | Note down the PR number | Note down the number PR<XXXX>. | PR<XXXX> status: Submitted |  |
| 8 | Note down the ERP Reference ID | Note down the ERP Reference ID number. (This is the PR number created in the SAP S/4HANA Buyer system.) |  |  |

### Create Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the purchase requisition will be created automatically in the SAP S/4HANA Cloud Public Edition system. You can display the newly created purchase requisition in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Access App | Open Display Purchase Requisitions (ME5A).Note If you want to display the fields Telephone, Fax, Street 2, and Street 3 in the Delivery Address of purchase requisition items, you can use the Process Purchase Requisitions (V2) (F1048A) app and adapt the user interface (UI) of this app with key user adaptation. For details, refer to the Adding a UI Element section of [Making UI Changes (Object Pages)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/54270a390b194c3e97be2424592c3352.html). To be able to make any UI changes, the Extensibility - Key User Adaptation (SAP_CORE_BC_EXT_FLEX) business catalog needs to be assigned to your business role. |  |  |
| 3 | Enter PR Number | On the List Display of Purchase Requisitions screen, enter the PR number, select the Also List Held PReqs check box, and choose Execute. This is the ERP Reference ID number you had noted down in the previous step. |  |  |
| 4 | Display PR | Choose the Purchase requisition, and choose Details. |  |  |
| 5 | Check status | On the Display Purchase Req. XXXXXXXX screen, choose the Status tab.The Block ID is: Blocked by requester. |  |  |

### Approve Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver logs on to the Guided Buying with SAP Ariba Buying to approve the shopping cart.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Compliance Approver (GRC). | The Guided Buying Home page is displayed. |  |
| 2 | Open Your Approvals | Choose the Your Approvals tab. |  |  |
| 3 | To Approve | On the Your Approvals screen, choose the To Approve tab. |  |  |
| 4 | Select PR for Approval | Search for PRXXXX, which was created in the previous step. |  |  |
| 5 | Approve PR | Choose Approve. |  |  |
| 6 | Comments for Approval | In the Approve request dialog box, enter comments and choose Approve. |  |  |
| 7 | Repeat the Steps | Repeats the steps from 1 to 6 for all the other approvers. | The status of PRXXXX changes from Submitted to Approved or Approved In External System. |  |

### Update Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the purchase requisition will be updated automatically in the SAP S/4HANA Cloud Public Edition system. You can display the updated purchase requisition in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Access App | Open Display Purchase Requisitions (ME5A). |  |  |
| 3 | Enter PR Number | On the List Display of Purchase Requisitions screen, enter the PR number, select the Also List Held PReqs check box, and choose Execute. This is the ERP Reference ID number you had noted down previously. |  |  |
| 4 | Display PR | Choose the Purchase requisition, and choose Details. |  |  |
| 5 | Check Status | On the Display Purchase Req. XXXXXXXX screen, choose the Status tab.The Block ID is: Not Blocked. |  |  |

### Create Reservation (Automated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you're testing with an inventory item.

In this activity, the reservation will be created automatically in the SAP S/4HANA Cloud Public Edition system.

Prerequisites

Automatic reservation creation is configured for a purchasing group and material group combination of your inventory item, as mentioned in the Preliminary Steps.

Procedure

The reservation will be created automatically in the SAP S/4HANA Cloud Public Edition system.

### Display Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you're testing with an inventory item.

In this activity, you check the shopping cart to see the updated reservation ID from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. | The Guided Buying Home page is displayed. |  |
| 2 | Display Shopping Cart | On the Recently Viewed left navigation panel, select the shopping cart that you've created earlier. | Shopping cart is displayed with details. |  |
| 3 | PO Number Updated in PR | Under the History tab, in the summary column, you see a message with a reservation ID. | Make a note of the reservation ID. |  |

### Post Goods Movement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you're testing with inventory items.

In this activity, you post the goods issue in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Open Post Goods Movement | Open Post Goods Movement (MIGO). |  |  |
| 3 | Search for reservation | Choose A07 Goods Issue, and R09 Reservation, input the reservation ID <reservation ID> that you've noted down in the previous step and choose Enter. |  |  |
| 4 | Check Delivery Quantity | Under Quantity, check the delivery quantity, enter all necessary entries, for example Storage Location, Item OK, and so on. |  |  |
| 5 | Post | Choose Post. | A message dialog box appears with the Material Document number.Note This material document number will not be updated in Guided Buying with SAP Ariba Buying. |  |

### Create Purchase Order (Automated)

Purpose

A PO is automatically created from PR.

Prerequisites

PR is created and the Automatic PO creation is scheduled in the SAP S/4HANA Cloud Public Edition system.

Procedure

This step is automatically generated if a job has been scheduled.

#### Create Purchase Order (Manually)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step, together with subsequent steps of goods receipt and invoice creation, are optional if you're testing with inventory items.

In this activity, the purchaser creates PO in the SAP S/4HANA Cloud Public Edition system. This step can only be carried out if Automatic PO creation from PR isn't scheduled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Open App | Open Process Purchase Requisitions - Deprecated (F1048) under Purchase Order Processing.Note If you're testing with a lean service procurement, choose Purchase Order Processing > Create Purchase Order Advanced , and select the GR-Bsd IV checkbox on the Invoice tab at item level. | A list of Requisitions is displayed. |  |
| 3 | Search for Purchase Requisition | In the Search field, enter the PR number that you've noted in the Create Shopping Cart step.Choose Go. | The Purchase Requisition list is displayed depending on the material. |  |
| 4 | Prepare Purchase Order | Select the Purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order. | The Purchase Order Preview screen is displayed. |  |
| 5 | Create Purchase Order | Select the Purchase Order Type with Standard PO and choose Save. | The purchase order is created. |  |
| 6 | Back to Manage Purchase Requisition | In the dialog box, make a note of the purchase order number and choose OK. | Purchase Requisition list is displayed again. |  |

### Display Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the shopping cart to see the updated PO number from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. | The Guided Buying Home page is displayed. |  |
| 2 | Display Shopping Cart | On the Recently Viewed left navigation panel, click the shopping cart that you had created in the earlier step. | Shopping cart is displayed with details. |  |
| 3 | PO Number Updated in PR | Under the History tab, in the summary column, you see a message with ERP Order IDs.On the header of the Items section, you see the Purchase Orders created in Guided Buying with SAP Ariba Buying for each line item. | The PR status is changed from Approved by External System to Ordered. Check whether the Purchase Order created in SAP S/4HANA Cloud Public Edition and the number updated in the History tab are the same.Note down the purchase order number for each line item. |  |

### Create Service Entry Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you're testing with a lean service procurement. Skip this step if you’re testing with a goods procurement.

In this activity, you create the service entry sheet in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Open Manage Service Entry Sheets | Open Manage Service Entry Sheets - Lean Services (F2027). |  |  |
| 3 | Enter Field Values | Choose Create.On the Service Entry Sheets screen, enter the following details:Name of Service Entry Sheet: <SES Name>, for example, SES Lean testingReference Purchase Order: <Purchase order you created in the previous step>Choose Enter.In the Items area, enter the following details for each item:Performance Date: <Any date within the service time period you defined when creating the purchase requisition in Guided Buying with SAP Ariba Buying>Stated Quantity: <Stated Quantity>, for example 10Choose Save. | Service Entry Sheet is saved. |  |
| 4 | Send to Approval | Choose Send to Approval on the top-right corner. | Service Entry Sheet is sent for approval. |  |
| 5 | Check Service Entry Sheet Status | On the Manage Service Entry Sheets screen, search for the service entry sheet created above and check the status. The service entry sheet has the status Approved (manually or automatically), depending on the Flexible Workflow being configured.Note For more information about how to configure the workflow, refer to the test script of scope item 22Z. | Check the Service Entry Sheet status. |  |

### Display Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you're testing with a lean service procurement. Skip this step if you’re testing with a goods procurement.

In this activity, the employee checks the shopping cart in Guided Buying to see the updated entry sheet number from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. | The Guided Buying Home page is displayed. |  |
| 2 | Display Shopping Cart | On the Recently Viewed navigation panel on the left, choose the shopping cart that you had created in the previous step. |  |  |
| 3 | Entry Sheet Number Updated in PR | On the History tab, in the summary column, you see a message with the service entry sheet number, for example, of the service sheet created in SAP S/4HANA Cloud Public Edition. ERP Service Sheet ID: xxx. | Check whether the entry sheet created in the SAP S/4HANA Cloud Public Edition system and the number updated are the same. |  |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you're testing with a non-limit items procurement. Skip this step if you’re testing with a limit items procurement.

In this activity, you post the goods receipt either in the SAP S/4HANA Cloud Public Edition system or in Guided Buying with SAP Ariba Buying.

|  |
| --- |
| Note If you're testing with a lean service procurement, the Goods Receipt is created automatically. So, you don't have to perform the following steps manually again. |

Procedure

Option 1 - Post the goods receipt in SAP S/4HANA Cloud Public Edition:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Open Confirm Receipt of Goods | Open Post Goods Receipt for Purchasing Document (F0843). |  |  |
| 3 | Search for Purchase Requisition | Enter the Purchase order <PO number> that you've noted down in the previous step and choose Enter.Else, select your Purchase Requisition from the list. |  |  |
| 4 | Check Delivery Quantity | Under Items, enter Delivered as <same as open quantity>. |  |  |
| 5 | Post | Choose Post. | A message dialog box appears with the Material Document number.Make a note of this number. |  |

Option 2 - Post the goods receipt in Guided Buying with SAP Ariba Buying:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as an Employee. | The Guided Buying Home page is displayed. |  |
| 2 | Open Your Requests | Choose the Your Requests tab. |  |  |
| 3 | To Receive | On the Your Requests tab, choose the To Receive tab. |  |  |
| 4 | Submit Goods Receipt | Find the Purchase Order number which was created in Guided Buying with SAP Ariba Buying, and enter the following:Accepted: <enter the quantity you want to receive, for example 10>Final Receipt: <select the checkbox if all quantities are accepted>Choose Submit. |  |  |

### Display Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the employee checks the shopping cart in Guided Buying to see the updated GR number from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. | The Guided Buying Home page is displayed. |  |
| 2 | Display Shopping Cart | On the Recently Viewed left navigation panel, choose the shopping cart that you had created in the earlier step. | Shopping cart is displayed with details. |  |
| 3 | GR Number Updated in PR | Under the History tab, in the summary column, you see a success message with GR number. | The PR status is changed from Ordered to Received. Check whether the GR created in SAP S/4HANA Cloud Public Edition and the number updated are the same. |  |

### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the accountant creates a supplier invoice in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Create Supplier Invoice (F0859). |  |  |
| 3 | Enter General Data | Enter the following details:Transaction: InvoiceCompany Code: 3310, for exampleInvoice Date: <Today's date>Posting Date: <Today's date>Gross Invoice Amount: Value in PO Calculate TaxInvoicing Party: 33300080, for exampleReference: <XXX> (Reference invoice number from the invoicing party) |  |  |
| 4 | Enter Purchase Order References | In Purchase Order References, check the references.Enter the following details (using the purchase order you had created previously):References Document Category: <Purchase Order/Scheduling Agreement>Purchase Order: <XXX> |  |  |
| 5 | Check the Purchase Order Items data | Check the Amount, Quantity, and Tax Code. |  |  |
| 6 | Post the Invoice | Choose Post. | The invoice is created. |  |

### Display Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the employee checks the shopping cart in Guided Buying to see the updated Invoice number from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. | The Guided Buying Home page is displayed. |  |
| 2 | Display Shopping Cart | On the Recently Viewed left navigation panel, choose the shopping cart that you had created in the earlier step. | Shopping cart is displayed with details. |  |
| 3 | Invoice Number Updated in PR | Under the History tab, in the summary column, you see a success message with invoice number. | The PR status is changed from Received to Invoiced. Check whether the invoice created in SAP S/4HANA Cloud Public Edition and the number updated are the same. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You must have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| ScopeItem_Name (J45) | ScopeItem_BusinessCondition |
| ScopeItem_Name (22Z) | ScopeItem_BusinessCondition |
| ScopeItem_Name (ScopeItem_ID) | ScopeItem_BusinessCondition |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| ScopeItem_Name () | ScopeItem_BusinessCondition |
| ScopeItem_Name (ScopeItem_Id) | ScopeItem_BusinessCondition |

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
- related-to :: [[10-procurement/test-script-guided-buying-for-central-procurement-with-sap-ariba-buyin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NV_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 55,971 chars in the whole document
