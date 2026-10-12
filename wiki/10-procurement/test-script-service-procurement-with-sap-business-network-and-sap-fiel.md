---
id: 10-procurement/test-script-service-procurement-with-sap-business-network-and-sap-fiel
title: "Test Script: Service Procurement with SAP Business Network and SAP Fieldglass (4R2) (4R2_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4R2: service PO, Fieldglass SOW/events, service entry sheet, Business Network invoice, payment."
cluster: 10-procurement
tags: [kb/procurement, topic/service-procurement-fieldglass]
aliases: [4R2_S4CLD2608_BPD_EN_XX]
keywords: [Service Procurement with SAP Fieldglass and Business Network, service procurement, purchase order creation, purchase order approval, flexible workflow, sap business network, sap fieldglass, service entry sheet, supplier invoice, automatic payments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R2_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1044
topic: 10-procurement/service-procurement-fieldglass
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Service Procurement with SAP Business Network and SAP Fieldglass (4R2) (4R2_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R2_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Service Procurement with SAP Fieldglass and Business Network** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Procurement with SAP Business Network and SAP Fieldglass (4R2) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232834001)

[2 Prerequisites 4](#_Toc232834002)

[2.1 Additional Manual Configuration 4](#_Toc232834003)

[2.2 System Access 4](#_Toc232834004)

[2.3 Roles 4](#_Toc232834005)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232834006)

[2.5 Business Conditions 6](#_Toc232834007)

[2.6 Preliminary Steps 6](#_Toc232834008)

[2.6.1 Activate Flexible Workflow for Purchase Orders 6](#_Toc232834009)

[2.6.2 Configure Flexible Workflow for Purchase Order 8](#_Toc232834010)

[2.6.3 Configure Workflow for Lean Services 9](#_Toc232834011)

[3 Overview Table 10](#_Toc232834012)

[4 Test Procedures 12](#_Toc232834013)

[4.1 Create Purchase Order with Multiple Line Items 12](#_Toc232834014)

[4.2 Approve Purchase Order(Optional) 14](#_Toc232834015)

[4.3 Display Purchase Order in SAP Business Network 15](#_Toc232834016)

[4.4 Create Order Confirmation in SAP Business Network 16](#_Toc232834017)

[4.5 Display Purchase Order Confirmation 17](#_Toc232834018)

[4.6 Display Statement of Work in SAP Fieldglass 18](#_Toc232834019)

[4.7 Create and Submit Event in SAP Fieldglass 19](#_Toc232834020)

[4.8 Approve Event in SAP Fieldglass 20](#_Toc232834021)

[4.9 Display Service Entry Sheet in SAP Business Network 21](#_Toc232834022)

[4.10 Display Service Entry Sheet 22](#_Toc232834023)

[4.11 Approve Service Entry Sheet (Optional) 22](#_Toc232834024)

[4.12 Create Supplier Invoice with SES Relation in SAP Business Network 23](#_Toc232834025)

[4.13 Release Supplier Invoice for Payment 24](#_Toc232834026)

[4.14 Display Invoice Status Change in SAP Business Network 25](#_Toc232834027)

[4.15 Display Supplier Invoice in SAP Fieldglass 26](#_Toc232834028)

[4.16 Pay Single Invoice (Optional) 27](#_Toc232834029)

[4.16.1 Schedule Payment Proposal (Optional) 27](#_Toc232834030)

[4.16.2 Revise Payment Proposal (Optional) 29](#_Toc232834031)

[4.16.3 Release Payment Proposal (Optional) 30](#_Toc232834032)

[4.17 Send Payment Advice to Supplier (Optional) 32](#_Toc232834033)

[4.18 Display Remittance Advice (Optional) 33](#_Toc232834034)

## Purpose

The scope item covers limited items with reference to contracts and can be conducted with different optional steps. Service procurement using free text description of services or product master in procurement documents is also supported.

The service fulfillment can be steered and monitored with the supplier side statement of work, supplier time sheets, and service entry sheets. Afterwards, the invoicing process is triggered.

The scope item covers standard service items and can be conducted with different optional steps. Service procurement using free text description of services in procurement documents is also supported.

Overview

This scope item covers the creation and approval of purchase orders for services. Alternatively, the process can be triggered via the creation of a purchase requisition, which is later converted to a purchase order.

The service fulfillment can be steered and monitored with the supplier side statement of work, supplier time sheets, and service entry sheets. Afterwards, the invoicing process is triggered.

The scope item covers standard service items and can be conducted with different optional steps. Service procurement using free text description of services in procurement documents is also supported.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisitesfor conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/cae4ea434d9df05ba462eb59290f9b5b)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Ariba | Accessible via Ariba portal. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Fieldglass | Accessible via Fieldglass portal. Your system administrator provides you with the URL to access the Fieldglass system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Space) | ID (Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT_PROCUREMT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

The master data consists of standardized SAP Best Practice default values and enables you to go through the process steps of this scope item.

|  |
| --- |
| Note You can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) . |

The master data in the following table is a sample data if your system have been set up for Germany.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 1010 | Plant 1 DE |  |
| Storage Location | 101A | Std. storage 1 |  |
| Company Code | 1010 | Company Code 1010 |  |
| Purchase Organization | 1010 | Purch. Org. 1010 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor / Supplier | 10300091 | Vendor domestic United States Ariba |  |
| Material Group | L001 | Account Billed |  |
| Material | TG0011 | Trading Good for Regular Procurement (PD planning) |  |
| Service ID | SM001 |  |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 42K - Automation of Source-to-Pay with SAP Business Network | You have activated the scope item and completed the steps described in the [Set-Up Instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/42K_Set-Up_EN_XX.pdf). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the BNZ - Create New Open MM Posting Period - MDS master data script. Posting period is up to date. |
| J60 - Accounts Payable | Update BP master data with payment method T.Review and execute Invoice payment preparation section. |

### Preliminary Steps

#### Activate Flexible Workflow for Purchase Orders

Purpose

In this procedure, you activate flexible workflow for purchase orders.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241) |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution |  |  |
| 4 | Search for Application Area | On the Configure Your Solution: Realize Phase screen, set the following search filters:Application Area: Sourcing and ProcurementSub Application Area: Operational Procurement |  |  |
| 5 | Select Configuration Item | From the search result list, select the Purchase Order Processing configuration activity and go to the next screen. | The Configure Your Solution – Purchase Order Processing screen is displayed. |  |
| 6 | Select Configuration Step | On the Configure Your Solution – Purchase Order Processing screen, go to the Activate Flexible Workflow for Purchase Orders configuration step and choose Configure. | The Document Types Purchase O rder Change screen is displayed. |  |
| 7 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type: NB (Standard PO)Scenario based workflow: select the checkbox | The scenario-based workflow is active for standard purchase orders.If you are asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue .Choose Save . |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 2 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 3 | Open Active Flexible Workflow | Go to the Business Processes Configuration app.To locate the activity in the tree view, search for the following activity: Purchase Order Processing.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 4 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type : NB (Standard PO)Scenario based workflow : select the checkbox | The scenario-based workflow is active for standard purchase orders.If you are asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue .Choose Save . |  |

#### Configure Flexible Workflow for Purchase Order

Purpose

In this procedure, you configure your release conditions for Purchase Order Approval.

When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Open Manage Workflow for Purchase Order | Open Manage Workflows for Purchase Orders (F2872) | The Manage Workflow screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Add and make following entries:Name : <Test Workflow for Purchase Order>Description: <Test Workflow for Purchase Order>In the Preconditions area, select Purchasing group of purchase order is and make following entry:Purchasing group of purchase order is: <Your purchasing group>Choose Add another condition and make following entries:Choose Total net amount of purchase order is greater than withPrice : 100Currency : EURIn Step Sequence area, choose the Add button and make following entries:Type : Release Purchase OrderRecipients Role : Manager of Workflow InitiatorSelect To be completed by one recipient .Choose Add and then Save . | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the newly created workflow item and choose Activate . | The workflow item is now activated. |  |

#### Configure Workflow for Lean Services

Purpose

In this procedure you configure your release conditions for Service Entry Sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Workflows for Service Entry Sheets - Lean Services (F3173) app. | The Manage Workflows screen is displayed. |  |
| 3 | Create Mangae Workflow | Choose Add and make the following entries.Name: <Automatic Release of Service Entry Sheet>Description: <Workflow for Service entry Sheet>In Step Sequence area, choose the Add button and make following entries:Type: Automatic Release of Service Entry SheetIn the RECIPIENTS area by default the following entry will be available:The recipients are determined automatically.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the newly created workflow item and choose Activate. | The workflow item is now activated. |  |

## Overview Table

This scope item consists of several <choose the appropriate entity: process steps, reports, items> provided in the table below.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order with Multiple Line Items](#unique_13) [page ] 12 | Purchaser | My Inbox - All Items (F0862) |  |
| [Approve Purchase Order(Optional)](#unique_14) [page ] 14 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Display Purchase Order in SAP Business Network](#unique_15) [page ] 15 | Supplier |  |  |
| [Create Order Confirmation in SAP Business Network](#unique_16) [page ] 16 | Supplier |  |  |
| [Display Purchase Order Confirmation](#unique_17) [page ] 17 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Display Statement of Work in SAP Fieldglass](#unique_18) [page ] 18 | Supplier |  |  |
| [Create and Submit Event in SAP Fieldglass](#unique_19) [page ] 19 | Supplier |  |  |
| [Approve Event in SAP Fieldglass](#unique_20) [page ] 20 | Supplier |  |  |
| [Display Service Entry Sheet in SAP Business Network](#unique_21) [page ] 21 | Supplier |  |  |
| [Display Service Entry Sheet](#unique_22) [page ] 22 | Purchaser |  |  |
| [Approve Service Entry Sheet (Optional)](#unique_23) [page ] 22 | Purchasing Manager | My Inbox |  |
| [Create Supplier Invoice with SES Relation in SAP Business Network](#unique_24) [page ] 23 | Supplier |  |  |
| [Release Supplier Invoice for Payment](#unique_25) [page ] 24 | Accounts Payable Accountant | Supplier Invoices List |  |
| [Display Invoice Status Change in SAP Business Network](#unique_26) [page ] 25 | Supplier |  |  |
| [Display Supplier Invoice in SAP Fieldglass](#unique_27) [page ] 26 | Supplier |  |  |
| [Pay Single Invoice (Optional)](#unique_28) [page ] 27 |  |  |  |
| [Schedule Payment Proposal (Optional)](#unique_29) [page ] 27 | Accounts Payable Accountant | Manage Automatic Payments (F0770) |  |
| [Revise Payment Proposal (Optional)](#unique_30) [page ] 29 | Accounts Payable Accountant | Revise Payment Proposals (F0771) |  |
| [Release Payment Proposal (Optional)](#unique_31) [page ] 30 | Accounts Payable Accountant | Manage Automatic Payments (F0770) |  |
| [Send Payment Advice to Supplier (Optional)](#unique_32) [page ] 32 | Accounts Payable Accountant | Manage Automatic Payments (F0770) |  |
| [Display Remittance Advice (Optional)](#unique_33) [page ] 33 | Supplier |  |  |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Create Purchase Order with Multiple Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the purchaser creates a lean services purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | In the Purchase Orders Processing group, open Manage Purchase Orders (F0842A) app. | The Manage Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Choose Create button.Enter all of the necessary data.On the General Information tab fill in:Purchase Order Type: Standard PO (NB)Supplier: <10300091>Currency: EURPurchasing Group: 001Purchasing Organization: 1010Company Code: 1010On the Delivery and Invoice tab enter following data:Payment Terms: 14 Days 3%, 20/2%, 30 Net (0003) | The Purchase Requisition list is displayed depending on the material. |  |
| 4 | Create Service Item | On the Items tab, in the Purchase Order Items section, choose Create and enter the following data:Short Text: Service 1Material Group: Services (P001)Plant: 1010Order Quantity: 10 HRNet Order Price: 100 EURPrice unit: 1 HRTo see further details of the line item, choose >. The Purchase Order Item screen is displayed.On the General Information tab enter following data:Product Type Group: Services (2)Account Assignment Category: Cost Center KOn the Process Control tab:Goods Receipt: Set (Select the checkbox)Invoice Receipt: Set (Select the checkbox)Goods-Receipt-Based Invoice Verification: Set (Select the checkbox)On the Tax tab enter following data:Tax Code: V0On the Schedule Lines Items tab enter following data: in:Start of Performance Period: TodayEnd of Performance Period: Today + 5 daysOn the Supplier Confirmation Control tab enter following data:Conformation Control: order conf. onlyOn the Account Assignment tab enter following data:G/L Account: 61002000Cost Center: 10101001Choose Apply button. |  |  |
| 5 | Create Limit Item | On the LimitItems tab, in the Purchase Order Items section, choose Create and enter the following data:Short Text: Limit itemExpected Value: 1000 EUROverall Limit: 1200 EURAccount Assignment Category: Cost center (K)Product Type Group: Service (2)Plant: 1010To see further details of the limit item, choose >. The Purchase Order Item screen is displayed.On the General Information tab enter following data:Material Group: Services (2)On the Process Control tab:Goods Receipt: Set (Select the checkbox)Goods-Receipt-Based Invoice Verification: Set (Select the checkbox)On the Tax tab enter following data:Tax Code: V0On the Schedule Lines Items tab enter following data: in:Start of Performance Period: TodayEnd of Performance Period: Today + 5 daysOn the Supplier Confirmation Control tab enter following data:Conformation Control: order conf. onlyOn the Account Assignment tab enter following data:G/L Account: 61002000Cost Center: 10101001Choose Apply button. |  |  |
| 6 | Save Purchase Order | Choose Order button. | A new purchase order is created. |  |

### Approve Purchase Order(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country currency amount) or more require an approval (for Purchasing Group 001 and 003).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fall/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchasing Manager | The Fiori Launchpad is displayed. |  |
| 2 | Open Approve Purchase Order | Open My Inbox - All Items (F0862) | The My Inbox screen is displayed. A list of already created Purchase Orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for Purchase Order xxx and select. | The Purchase Order xxx is displayed.The Purchase Orders without follow on documents(w/o status Follow On Documents) and a net value of 500 USD or more have the status In Approval |  |
| 4 | Approve the Purchase Order | Choose the Approve button, enter the approval reason if needed, then choose Submit. |  |  |

### Display Purchase Order in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log into the SAP Business Network as a supplier and display the purchase order in the SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the SAP Business Network as a Supplier on supplier.ariba.com. | The SAP Business Network Home screen is displayed. |  |
| 2 | Select the Purchase Order | On the Home screen, choose Orders > Orders and Releases , and select the Purchase Order ID. | The Purchase Order is displayed in status New. |  |

### Create Order Confirmation in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the supplier confirms the purchase order in the Aria Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the SAP Business Network as a Supplier on supplier.ariba.com. | The SAP Business Network Home screen is displayed. |  |
| 2 | List New Purchase Order | On the Home screen, choose Order > Orders and Releases .Open the Search Filters pane. In the Date Range field, choose Last 24 Hours from the dropdown list. Choose Search. | A list of newly created purchase order is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Confirm Purchase Order | Choose Create Order Confirmation > Confirm Entire Order . Enter the following data:Confirmation #: PO Confirmation for ServiceChoose Next > Submit . | The status of the purchase order is changed to Confirmed . |  |
| 5 | Return to Orders and Releases | To return to the list of purchase orders, choose Done . | The order status changed to 'Confirmed'. |  |

### Display Purchase Order Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the purchaser order confirmation is displayed in SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instructions | Expect ed Results | Pass/Fall/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A) | The Manage Purchase Orders screen with a list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Select the row of the purchase order you created in previous step. | The Standard PO XXX screen is displayed. |  |
| 4 | Review Order Confirmations | Navigate to the Item Details section for each of the available items and choose the Supplier Confirmations tab.When the conformation from your SAP Business Network supplier has been sent, you see an additional line showing following information:CC (Confirm. Cat.): ABQuantity: x | The purchase order confirmation is displayed. |  |

### Display Statement of Work in SAP Fieldglass

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the automatically created Statement of Work in SAP Fieldglass.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Pass / Fail/ Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fieldglass as a Supplier. |  |  |
| 2 | Display Statement of Work | On the Home screen, navigate to the View tab and select Services > Statement of Work . On the Statement of Work screen, navigate to the Name > Enter Criteria field and search for the newly created Purchase Order ID. | The newly created Statement of Work for the respective Purchase Order is displayed with ID similar to 'DLABTQ00000619'. |  |
| 3 | Verify Status | Select the link under the SOW ID to navigate to the Statement of Work.Check the status of the Statement of Work. It should be displayed as Approved.On the Characteristics tab, you can verify the purchase order data. | The status of Statement of Work is approved. |  |

### Create and Submit Event in SAP Fieldglass

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create and submit the Event in SAP Fieldglass.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fieldglass as a Supplier.On the top right corner of the screen, navigate to the dropdown list under the logged user name. Under Linked Accounts, choose Supplier Account Administrator. | You are acting as a supplier in SAP Fieldglass. |  |
| 2 | Display Statement of Work | On the Home screen, navigate to the View tab and select Services > Statement of Work . On the Statement of Work screen, navigate to the Name > Enter Criteria field and search for the newly created Purchase Order ID. | The newly created Statement of Work for the respective Purchase Order is displayed. |  |
| 3 | View Characteristics | Choose the Characteristics tab.All Purchase Order line items should be visible. |  |  |
| 4 | Mark as complete | Choose the first line item, for example Hierarchy Service 1. The event line opens.Select the Mark as Complete button.Enter today's date (this date needs to be in between the Purchase Order line start and end date).Select an Approver from the dropdown list.Choose Continue and Submit.Note If your line item is a Limit Item, choose the Itemize button and enter the following data:Completed Date: today's dateSelect an Approver from the dropdown list.Rate / Unit: for example 100 / HRUnits: for example 10Choose Calculate Totals, then Submit.Repeat the steps for all available line items.Verify in the second line on the SOW Characteristics tab that the status is displayed as Pending Approval. |  |  |

### Approve Event in SAP Fieldglass

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you approve the newly created Event in SAP Fieldglass.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fieldglass as a Supplier.On the top right corner of the screen navigate to the dropdown list under the logged username. Under Linked Accounts, choose Approver. | You are acting as the approver for the newly created Event in SAP Fieldglass. |  |
| 2 | Approve Event | On the Home screen, navigate to the Notifications button on the top right corner of the screen.Choose Event > Approve .On the Your Work Items \| Event screen, search for the Event ID that you've noted down in the previous step, select it and choose Approve.On the popup Event screen, choose Approve.In case you have created more than one Event, search for the second Event you've noted down in the previous step, select it and approve it. | A success message appears. |  |

### Display Service Entry Sheet in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the Service Entry Sheet in SAP Business Network as a Supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the SAP Business Network as a Supplier on supplier.ariba.com. |  |  |
| 2 | Display Service Entry Sheet | On the Home screen, choose Fulfillment > Service Sheets . In the Search Filters area enter the following data:Order number: <related purchase order ID>Select Search.Select Service Sheet # for related PO.Under Detail tab verify the Service Sheet data. |  |  |

### Display Service Entry Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Service entry Sheet is displayed in SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser . |  |  |
| 2 | Open Manage Service Entry Sheets App | In the Service Entry Sheet Processing group, open Manage Service Entry Sheets app. (Incase Approval workflow is configured follow the Approval Process in the next procedure). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Select Service Entry Sheet | Select the row with the Service Entry Sheet number you created in previous step.Choose Show Details button and verify if the Approval Status is Approved. | The Service Entry Sheet details screen is displayed. |  |

### Approve Service Entry Sheet (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you approve a Service Entry Sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchasing Manager . | The Fiori launchpad is displayed. |  |
| 2 | Open Inbox | Open My Inbox app. | The My Inbox screen is displayed. A list of already created Service Entry Sheets with needed approval is displayed. |  |
| 3 | Select Service Entry Sheet | Enter Purchase Order ID into the Se a rc h field. List of Service Entry Sheets for this Purchase Order will be displayed. | Service Entry Sheet is displayed. |  |
| 4 | Approve the Service Entry Sheet | Choose the Release button. Enter the approval reason if needed, then choose Submit . |  |  |

### Create Supplier Invoice with SES Relation in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice. The supplier logs on to SAP Business Network, selects the purchase order to be invoiced and creates the supplier invoice against it.

|  |
| --- |
| Note Based on the system configurations, the invoice could have been created automatically immediately after the service entry sheet has been approved in the SAP S/4HANA system. If the purchase order is in status Invoiced, skip the procedure and continue with [Release Supplier Invoice for Payment](#unique_25) [page ] 24. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the SAP Business Network as a Supplier on supplier.ariba.com. | The SAP Business Network Home screen is displayed. |  |
| 2 | Select the Purchase Order to be invoiced | Choose Orders > Orders and Releases , select the purchase order to be invoiced. Choose Create Invoice > Standard Invoice . | The Create Invoice screen is displayed. |  |
| 3 | Enter Invoice Header Data | Enter the invoice number <XXX> . |  |  |
| 4 | Enter Taxes. | In the TAX area, enter the Rate (%) : 0% , and choose Update .If you are asked to fill in the Category field, please choose Sales Tax .In the Line Items area, select the check box for the respective Service Sheet. | Tax entered. |  |
| 5 | Post Invoice | Select Next to get to the Invoice Submission screen. Review the invoice details and choose Submit .If the system requires a Remit To ID , choose Invoice Header - View/Edit Addresses , and enter make the following entry:Remit To ID : 1000 | The Order Status gets updated to Invoiced. |  |

### Release Supplier Invoice for Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to release the supplier invoice for payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Open Supplier Invoice List | Open the Supplier Invoices List app. | The Supplier Invoices list screen is displayed. |  |
| 3 | Search for Blocked Supplier Invoices | On the Supplier Invoices List screen, search for your invoice, which is in Status: Posted from SAP Ariba or Blocked for Payment. | If an invoice has been blocked for payment, a Blocked for Payment: Yes message is displayed. In order to release the supplier invoice, please proceed with step 4. |  |
| 4 | Release the Invoice | Choose Release. | The invoice is released. |  |

### Display Invoice Status Change in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log on to the SAP Business Network as a Supplier and display the status of the updated purchase order.

Prerequisites

The steps described in [Create Supplier Invoice with SES Relation in SAP Business Network](#unique_24) [page ] 23 have been performed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the SAP Business Network as a Supplier on supplier.ariba.com. | The SAP Business Network Home screen is displayed. |  |
| 2 | Display Invoice | Choose Invoices > Invoices .Display the invoice related to the previously created Purchase Order (XXX). | The invoice is displayed. |  |
| 3 | Check Invoice Status | The invoice status should be Sent or Approved . |  |  |

### Display Supplier Invoice in SAP Fieldglass

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the automatically created Invoice in SAP Fieldglass.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fieldglass as a Supplier.On the top right corner of the screen navigate to the dropdown list under the logged username. Under Linked Accounts choose Supplier Account Administrator. | You are acting as a supplier in SAP Fieldglass. |  |
| 2 | Display Event | On the Home screen, navigate to the View tab and select Services > Statement of Work .On the Statement of Work screen, navigate to the Name Enter Criteria field. Search for the newly created Purchase Order ID and select it.Navigate to the Characteristics tab.Choose the Purchase Order line item, which is in status Invoiced. |  |  |
| 3 | Review Statement of Work invoice | Navigate to the Related tab.Under Related Documents, navigate to SOW Invoice and choose the link in the ID column.Review the invoice details. | Invoice document is displayed. |  |

### Pay Single Invoice (Optional)

Purpose

This section describes how to post payment using the automatic payment program.

Prerequisites

Invoices have been posted and are open for payment.

Payment methods to use have been defined in the Business Partner Master Data (check test script J60 - Accounts Payable , step Complete Supplier Master Data ).

#### Schedule Payment Proposal (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to select the invoice to be paid. When a vendor has been paid directly via an online banking system, you the manually add the information to the SAP S/4HANA Cloud Public Edition System.

Prerequisite

An open invoice is available. For more information, see the Business Conditions .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant . |  |  |
| 2 | Access App | Open the app Manage Automatic Payments (F0770). | The Manage Automatic Payments screen is displayed. |  |
| 3 | Create Automatic Payment Parameter | To create an automatic payment parameter, choose Create Parameter , and enter the following data:Run Date : <today’s date>Identification : <any five character description, such as SPAY1>Choose Create . | The Automatic Payment Parameters screen is displayed. |  |
| 4 | Data Entry | In the Basic section, enter the following data:Posting Date : <today’s date>Docs Entered Up To : <today’s date>Enable the Additional Log toggle.In the Payment Controls section, enter the following data:Company Code: <Your Company Code>Next Payment Date : <today’s date + 40 days>Note Adjust the date according to payment terms.Payment Metho d: T, FNote Verify that the payment method is valid in the supplier master record.In the Open Item section, enter the following data:Supplier : <Your Supplier>If you need to execute a payment for a single invoice, choose Document Number (BKPF BELNR) from the dropdown list of the Free Selection 1 and enter a document number.Choose Save . | The system message Parameter has been saved is displayed. The status changes to Parameter Created . |  |
| 5 | Schedule Proposal | Choose Schedule -> Proposal | The Schedule Proposal popup window is displayed. |  |
| 6 | Data Entry | On the Schedule Proposal popup window, enter the following data:Start Date : <today’s date>Start Immediately : Select the checkbox.Choose Schedule . | The system message Proposal is created is displayed.The status changes to Proposal Created . |  |
| 7 | View Proposal | On the Manage Automatic Payments screen, select the Proposal Proce ssed tab. | Alist of processed proposal items is displayed. |  |
| 8 | View Log for Outgoing Payment | On the Manage Automatic Payme n ts screen, select the Payments Processed tab.In the Log column of your payment run, choose Notes .Note If the Log column isn’t displayed, choose Settings . Select the Log checkbox and choose OK . | The log displays the program’s selection. The SAP S/4HANA Cloud Public Edition system is updated with the information about the outgoing payment. |  |

#### Revise Payment Proposal (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review invoices to be paid.

Caution : Make sure that there are no other Payment Run Identification Proposals pending to be executed which might be using the same supplier as proposal created in previous step. If payment proposals exist, they must be processed or deleted, otherwise no payment proposal is generated for your proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant . |  |  |
| 2 | Access App | Open app Revise Payment Proposals (F0771). | The Review P ayment Proposals screen is displayed. |  |
| 3 | Go | Choose the Go button. | A list of all proposals displays. |  |
| 4 | Select | Choose the > button from the Open column in the proposal you want to edit (for example, SPAY1). | The view Schedule Payment Proposal of selected Identification displays. |  |
| 5 | Edit Payment | In the Payments tab, select the rows to edit and choose the Edit Payment button. | The Edit Payment dialog box displays. |  |
| 6 | Make Entries | Change desired options and choose OK to continue.Payment method : <payment method>House Bank : <house bank>Account ID : <account>Payee Bank : <payee bank>Due date : <date> |  |  |
| 7 | Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You may unblock or reallocate and pay them by using the buttons in the view. |  |  |

#### Release Payment Proposal (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant . |  |  |
| 2 | Access App | Open app Manage Automatic Payments (F0770). | The Manage Automatic Payments screen is displayed. |  |
| 3 | Go | Choose the Go button. | A list of all payment runs is displayed. |  |
| 4 | Proposal Processing | Choose the Proposal Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example, SPAY1 ) and choose Schedule . | The Schedule Payment dialog box displays. |  |
| 6 | Schedule Payment | Make the following entries:Start Date : <today’s date>Start Immediately : Select the checkbox.Choose Schedule . | The system displays the Payment has been scheduled notification. The status changes to Payment Posted . The log shows how many postings or payments were generated. |  |
| 7 | View the payment | Choose the Payment Processed tab. | The status changes to Payment posted . |  |
| 8 | View Log postings | Select the line of your payment run Identification and in the Log column, choose Notes .Note If the Log column isn’t displayed, choose Settings . Select the Log checkbox and choose OK . | The log shows how many postings were generated. |  |
| 9 | Close Dialog | Choose OK . | The Log Details dialog box closes. |  |
| 10 | Payments and Exceptions | In the Open column, choose the navigation right arrow. | The view displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You can sort the information by payment method, country, and so on. Select the view to display in the field below Summary . | Amounts are stored by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions . | Details are displayed for payments or exceptions generated (such as payment document, payment order, included items, and so on). |  |
| 13 | Payments Navigation | In the Open column, choose the navigation right arrow to display item details of the payment.When you are done, choose Back at the top to exit this view. | Payment item details are displayed. |  |

### Send Payment Advice to Supplier (Optional)

Purpose

A Payment Advice is automatically generated and sent to the supplier via SAP Business Network.

Prerequisite

Payments have been approved. The SAP Business Network Supplier Account ID is created for vendor <Your Supplier ID >

Procedure

|  |
| --- |
| Note Only execute this steps if the payment advice was not sent to SAP Business Network automatically. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Automatic Payments (F0770) app. | The Manage Automatic Payments screen is displayed. |  |
| 3 | Go | Choose the Go button. |  |  |
| 4 | View the payment | Choose the Payment Processed tab. |  |  |
| 5 | Payments | Select the line of the payment run Identification to review and in the Open column, choose Open . |  |  |
| 6 | Select | Choose PAYMENTS and in the Open column, choose Open . |  |  |
| 7 | Output Items | Choose Output Items . |  |  |
| 8 | Review | In the Output Items section check that Status of Output Type PAYM_ADV_CXML is Completed . |  |  |
| 9 | Resend | If the status is not Completed , select the checkbox of Output Type PAYM_ADV_CXML and choose Resend . | Status is set to Completed . |  |
| 10 | Close | Choose Back twice. |  |  |

### Display Remittance Advice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display the remittance advice in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Business Network as a Supplier. | The SAP Business Network Home screen is displayed. |  |
| 2 | View Remittance | Choose Inbox -> More -> Remittances .In the Transaction # column, select the remittance to display all details. | The Remittance Advice: XXX (Paid) screen is displayed. |  |

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
> Flagged while digesting this document, not verified: PO approval threshold is inconsistent within the document: workflow set-up uses total net amount greater than 100 EUR, while the approval step states POs of 500 USD or more require approval (purchasing groups 001 and 003).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/external-workforce-procurement-via-sap-fieldglass-22k-test-script-sap]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R2_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 53,133 chars in the whole document
