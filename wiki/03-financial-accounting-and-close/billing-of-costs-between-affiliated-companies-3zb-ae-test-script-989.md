---
id: 03-financial-accounting-and-close/billing-of-costs-between-affiliated-companies-3zb-ae-test-script-989
title: Billing of Costs Between Affiliated Companies (3ZB_AE) - Test Script (3ZB_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3ZB_AE (UAE): billing costs between affiliates via PO, sales order, billing, EDI and supplier invoice."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/intercompany-cost-billing]
aliases: [3ZB_S4CLD2608_BPD_EN_AE]
keywords: [Billing of Costs Between Affiliated Companies, intercompany cost billing, purchase order creation, purchase order approval, sales order update, billing documents, supplier invoices, flexible workflow, edi message monitoring, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3ZB_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-989
topic: 03-financial-accounting-and-close/intercompany-cost-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Billing of Costs Between Affiliated Companies (3ZB_AE) - Test Script (3ZB_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3ZB_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Billing of Costs Between Affiliated Companies** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Billing of Costs Between Affiliated Companies (3ZB_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Billing of Costs Between Affiliated Companies (3ZB_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854211)

[2 Prerequisites 4](#_Toc232854212)

[2.1 System Access 4](#_Toc232854213)

[2.2 Roles 4](#_Toc232854214)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854215)

[2.4 Additional Manual Configuration 7](#_Toc232854216)

[2.5 Business Conditions 7](#_Toc232854217)

[2.6 Preliminary Steps 8](#_Toc232854218)

[2.6.1 Create Info Record (Optional) 8](#_Toc232854219)

[2.6.2 Configure Flexible Workflow for Purchase Order 9](#_Toc232854220)

[2.6.2.1 Check Flexible Workflow for Purchase Order Approval 9](#_Toc232854221)

[2.6.2.2 Configure Flexible Workflow for Purchase Order 11](#_Toc232854222)

[2.6.3 Configure Flexible Workflow for Supplier Invoice 12](#_Toc232854223)

[2.6.3.1 Activate Flexible Workflow for Supplier Invoice 12](#_Toc232854224)

[2.6.3.2 Update Cost Center for User Responsible 14](#_Toc232854225)

[2.6.3.3 Update Profit Center for User Responsible 14](#_Toc232854226)

[2.6.3.4 Check Workflow for Supplier Invoice 15](#_Toc232854227)

[2.6.4 Edit User-Specific Parameters for Supplier Invoices (Optional) 16](#_Toc232854228)

[2.6.4.1 Change Material (Services) Master Data - Purchasing Data 17](#_Toc232854229)

[2.6.4.2 Change Supplier Master Data - Purchasing Organization Data 18](#_Toc232854230)

[3 Overview Table 19](#_Toc232854231)

[4 Test Procedures 20](#_Toc232854232)

[4.1 Create Purchase Order 20](#_Toc232854233)

[4.2 Change Purchase Order (Optional) 22](#_Toc232854234)

[4.3 Approve Purchase Order (Optional) 23](#_Toc232854235)

[4.3.1 Check Purchase Order Approval Details (Optional) 24](#_Toc232854236)

[4.3.2 Preview Purchase Order (Optional) 24](#_Toc232854237)

[4.4 Update Sales Order 25](#_Toc232854238)

[4.5 Process Sales Order Approval (Optional) 26](#_Toc232854239)

[4.6 Create Billing Document 27](#_Toc232854240)

[4.7 Check Supplier Invoice 28](#_Toc232854241)

[4.8 Release Supplier Invoice (Optional) 29](#_Toc232854242)

[4.9 Approve Supplier Invoice (Optional) 30](#_Toc232854243)

[4.10 EDI Message Monitoring (Optional) 31](#_Toc232854244)

[5 Appendix 33](#_Toc232854245)

[5.1 Process Integration 33](#_Toc232854246)

[5.1.1 Succeeding Processes 33](#_Toc232854247)

## Purpose

Overview

A company wants to bill costs to an affiliate. The affiliate creates a purchase order to reflect that a vendor invoice is expected. In the sending company, a customer order including costs to be billed (and a margin if relevant) is created. The customer order is billed and is sent to the affiliate, creating a supplier invoice with reference to the purchase order.

Via activation of B2B scenarios, you can achieve process automation between sending company and affiliate.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Company Code | 3320 | Company Code 3320 |  |
| Plant | 3310 | Plant 1 AE |  |
| Plant | 3330 | Plant 3 AE |  |
| Supplier | 33403320 |  |  |
| Purchase Organization | 3310 | Purchase Organization 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Purchasing Group | 003 | Group 003 |  |
| Material | SM0001 | Service Material 01 |  |
| Material Group | YBMM01 | Non-Sto Mat. w. ID |  |
| Cost Center | 33101501 | R&D Cost center |  |
| Cost Center | 33101601 | Marketing Cost Center |  |
| Sold-to Party | 33401010 | Domestic UAE Customer 10 |  |
| Payer | 33403310 |  |  |
| Sales Organization | 3330 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BND | Create Customer Master - MDS |
| 31X | Create Product Master of type "Service Product" - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/21c83d8efdca26db56c1b8be58d3afe9)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the test script BNZ's master data script. Posting Period is up to date. |
| 2EJ - Integration of Procurement with External Suppliers | This scope item should be activated in the same counry of this scope item. |
| 2EL - Integration of Sales with External Buyers | This scope item should be activated in the same counry of this scope item. |
| 2EQ - Sale of Services | This scope item should be activated in the same counry of this scope item. |
| 22Z - Procurement of Services | This scope item should be activated in the same counry of this scope item. |

### Preliminary Steps

#### Create Info Record (Optional)

Purpose

This process step shows you how to create info records for procure process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Purchasing Info Records | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create in the Info Records area. | The New Purchasing Info Record screen displays. |  |
| 4 | Enter Header Data | On the Header tab, make the following entries:Info Record Description: <Enter short text>Purchasing Organization: 3310Supplier: 33403320Material: SM0001Plant: 3310Purchasing Group: 003 | The Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | On the Delivery and Quantity tab, make the following entries:Delivery Time in Days: <Delivery Time>, for example, 5Under Delivery Tolerance in %: <Under Delivery Tolerance>, for example, 10Over Delivery Tolerance in %: <Over Delivery Tolerance>, for example, 10Tax Code: <Tax Code>, for example, <Input Tax Code>Order Unit: <Order Unit>, for example, HStandard Order Quantity: <Standard Order Quantity>, for example, 1Select the following entries if required:Unlimited Delivery: <unselected>Goods-Receipt-Based Invoice Verification: <unselected>No Evaluated Receipt Settlement : <selected>Order Acknowledgement Requirement: <unselected> | The Delivery and Quantity data is added. |  |
| 6 | Enter Condition Data | On the Conditions tab, choose Create. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>, for example, 21Pricing Unit: <Pricing Unit>, for example, 1Valid To: <Valid to Date>Currency: <Currency>, for example, AEDChoose Apply. | The Condition data is added. |  |
| 7 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

Result

The purchasing info record is created.

#### Configure Flexible Workflow for Purchase Order

##### Check Flexible Workflow for Purchase Order Approval

Purpose

This process step shows you how to check flexible workflow for purchase order approval.

Make sure flexible workflow for purchase order with NB document is activated, and flexible workflow for purchase order approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version . | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search Activate Flexible Workflow for Purchase Orders, then choose Go.Select the line of the item and go to next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen displays. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: NBScenario based workflow:XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: NBScenario based workflow:XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The scenario based workflow is active for document type: NB.

##### Configure Flexible Workflow for Purchase Order

Purpose

This process step shows you how to configure your release conditions for purchase order approval.

When you start to process this step, make sure that the flexible workflow for purchase document type NB has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Create and make following entries:Name: <Test Workflow for Purchase Order>On the Start Conditions tab, make the following entries:Purchasing group of purchase order is: Purchasing Group: 003Choose Add and make the following entries:Total net amount of purchase order is greater than: Price: 500Currency: AEDOn the Step Sequence tab, choose Add and make the following entries on the next screen:Type: Release Purchase OrderOn the Recipients tab:Assignment: <select User from dropdown list>, <choose Purchasing_manager from F4 help>Step to be completed by: <One of the recipients>Choose Add and choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the just created workflow item and choose Activate. | The workflow item is activated. |  |

|  |
| --- |
| Note Make sure default workflow automatic release of purchase order is activated. |

#### Configure Flexible Workflow for Supplier Invoice

##### Activate Flexible Workflow for Supplier Invoice

Purpose

This process step shows you how to activate flexible workflow for supplier invoice.

If you want to use the flexible workflow to approve the supplier invoice, you have to process the step: Activate Flexible Workflow for Supplier Invoice.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | Search Activate Flexible Workflow for Supplier Invoice, choose configuration with name Incoming Invoice from search result, then choose Configure on the right of configuration steps with name Activate Flexible Workflow for Supplier Invoices. | The Change View "Activate Flexible Workflow for Supplier Invoices": Detail screen displays. |  |
| 5 | Active Flexible Workflow for Supplier Invoices | Select the following checkboxes:Payment Block: Flexible Workflow is ActiveRelease Completed Invoice: Flexible Workflow is ActiveChoose Save.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Supplier Invoices.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Active Flexible Workflow for Supplier Invoices | Select the following checkboxes:Payment Block: Flexible Workflow is ActiveRelease Completed Invoice: Flexible Workflow is ActiveChoose Save.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |  |

Result

The scenario based workflow is activated for supplier invoices.

##### Update Cost Center for User Responsible

Purpose

This process step shows you how to configure your release conditions for service entry sheets approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Cost Centers - Old Version (F1443A). | The Manage Cost Centers displays. |  |
| 3 | Filter Cost Center | Enter the following as filter:Cost Center: for example, 33101501Choose Go, select cost center in search results, then choose Edit. | The cost center detail information screen displays. |  |
| 4 | Input User Responsible | On the General Information tab, make the following entries:User Responsible: <search with F4>, for example, <Purchasing_Manager>Person Responsible : for example, <Purchasing_Manager> |  |  |
| 5 | Save Data | Choose Save. | Cost center is saved. |  |

##### Update Profit Center for User Responsible

Purpose

This process step shows you how to configure your release conditions for invoice approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Profit Centers - Old Version (F3516). | The Manage Profit Centers screen displays. |  |
| 3 | Filter Profit Center | Enter the following as filter:Profit Center: for example, <YB600>Choose Go, select profit center in search results, then choose Edit. | The profit center detail information screen displays. |  |
| 4 | Input User Responsible | On the General Information tab, make the following entries:User Responsible: <search with F4>, for example, <Purchasing_Manager>Person Responsible : for example, <Purchasing_Manager> |  |  |
| 5 | Save Data | Choose Save. | Profit center is saved. |  |

##### Check Workflow for Supplier Invoice

Purpose

This process step shows you how to make sure workflow for supplier invoice is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Supplier Invoices (F2873). | The Manage Workflows screen displays. |  |
| 3 | Check Workflow for Parked Invoice as Complete | In the Workflows dropdown list, choose Workflow for Parked Invoice as Complete, make sure workflow Release completed invoice is in active status. If not, select it and choose Activate.Choose the line and go to the Workflow Details screen. Go to the Step Sequence tab, and check the Recipients column which defines the user who handles invoice in the particular step, for example, Creator of Purchase Order, Cost Center Responsible or Profit Center Responsible. If this particular user doesn’t have My Inbox (F2097) APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to the business role of the user. This action is also required for other invoice workflow. | The workflow item is activated. |  |
| 4 | Check Workflow for Blocked Invoice | In the Workflows dropdown list, choose Workflow for Blocked Invoice, make sure workflow Release blocked Invoice by Accounting Responsibles is in active status. If not, select it and choose Activate. | The workflow item is activated. |  |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

This process step shows you how to edit user-specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Edit Supplier Invoice Settings (F3813). | The Edit Supplier Invoice Settings screen displays. |  |
| 3 | Set Parameter | Select the parameter Display Journal Entry: XIf parameter is checked, the system message contains invoice and journal entry number when invoice is created.If parameter is unchecked, the system message contains invoice number only when invoice is created.When this parameter is changed, it will be effective immediately for the Create Supplier Invoice (F0859) App. However, user needs to log out and log on again to make it effective for this App. | Change has been saved successfully. |  |

Result

The Display Journal Entry parameter has been set successfully.

##### Change Material (Services) Master Data - Purchasing Data

Purpose

This process step shows you how to change material (services) master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Material (MM02). | The Change Material (Initial Screen) displays. |  |
| 3 | Enter Material Basic Data | On the Change Material screen, make the following entries:Material: <Material>, for example, SM0001Choose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Choose Views | On the Select View(s) screen, choose Purchasing and Continue. | The Organizational Levels displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, make the following entry in the Organizational level section:Plant: <Plant>, for example, 3310Choose Continue. | The Change Material XXXXX (Services) displays. |  |
| 6 | Select Autom.PO | Autom.PO: <selected> | Autom.PO is selected. |  |
| 7 | Save Your Data | Choose Save. | The material master data is updated. |  |

Result

The Autom.PO checkbox is selected.

##### Change Supplier Master Data - Purchasing Organization Data

Purpose

This process step shows you how to change the supplier master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner | On the Maintain Business Partner screen, make the following entries.Business Partner: <Supplier>, for example, 33403320Choose Enter. | The Supplier information screen displays. |  |
| 4 | Change BP Role | In the Change in BP role field, choose the following value: Supplier(defined) |  |  |
| 5 | Open Purchasing Organization Data | Choose Purchasing. | The Change Organization: XXXXXXXX, role Supplier screen displays. |  |
| 6 | Enter Purchasing Data | Choose Switch Organization.Make the following data and press Enter:Purch. Organization: <Purchasing Organization>, for example, 3310 |  |  |
| 7 | Select Automatic PO Checkbox | Go to the Purchasing Data tab in the Additional Purchasing Data section, make the following data:Automatic PO: <selected> | The Automatic PO checkbox is selected. |  |
| 8 | Save Your Data | Choose Save. | The supplier change is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below：

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_19) [page ] 20 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Change Purchase Order (Optional)](#unique_20) [page ] 22 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Approve Purchase Order (Optional)](#unique_21) [page ] 23 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Check Purchase Order Approval Details (Optional)](#unique_22) [page ] 24 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Preview Purchase Order (Optional)](#unique_23) [page ] 24 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Update Sales Order](#unique_24) [page ] 25 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Process Sales Order Approval (Optional)](#unique_25) [page ] 26 |  |  |  |
| [Create Billing Document](#unique_26) [page ] 27 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Check Supplier Invoice](#unique_27) [page ] 28 | Accounts Payable Accountant | Supplier Invoices List (F1060A) |  |
| [Release Supplier Invoice (Optional)](#unique_28) [page ] 29 | Accounts Payable Accountant | Supplier Invoices List (F1060A) |  |
| [Approve Supplier Invoice (Optional)](#unique_29) [page ] 30 | Accounts Payable Accountant | Supplier Invoices List (F1060A) |  |
| [EDI Message Monitoring (Optional)](#unique_30) [page ] 31 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) |  |

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

This process step shows you how to formalize a specific requirement for a service from the vendor by creating a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays. |  |
| 3 | Create Order | Choose Create．On the Purchase Order screen, make the following entries:On the General Information tab:Supplier: 33403320Currency: AEDPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310Note If you want the purchase order to be assigned to an approver, then total PO amount should be higher than 500 AED for purchasing groups 003.You can choose one of the cases below.On the Items tab, choose Create and make the following entries for each item:Material: SM0001Plant: 3310Order Quantity: <Order Quantity>, for example, 1HChoose the item and go to the Purchase Order Item screen.On the General Information tab:Account Assignment Category: Cost centerNet Order Price: <Net Order Price>, for example, 20On the Process Control tab:Goods Receipt: <unselected>Goods-Receipt-Based Invoice Verification: <unselected>On the Tax tab:Tax Code: <Input Tax Code>On the Schedule Lines tab:Start of Performance Period: <Today>End of Performance Period: <Today + 30 days>On the Account Assignment tab:Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Choose Apply, then go back to the Purchase Order screen. |  |  |
| 4 | Check Purchase Order for Completeness | On the Purchase order screen, choose Messages.If the system displays an error message, correct the purchase order.If no error message displays, the purchase order can be submitted. |  |  |
| 5 | Save Purchase Order | Choose Order. | The purchase order is created. |  |

### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen displays. |  |
| 3 | Search for Purchase Order | Enter the purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the purchase order you want to change, then go to the Purchase Order screen.Choose Edit. | The Purchase Order screen displays.The purchase order is opened in change mode. |  |
| 5 | Change Purchase Order | Change certain field values of the purchase order. | The purchase order values are changed. |  |
| 6 | Check Purchase Order for Completeness | On the Purchase order screen, choose the Messages.If the system displays an error message, correct the purchase order;if no error message displays, the purchase order can be submitted. |  |  |
| 7 | Save Purchase Order | Choose Order. | The purchase order is saved. |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release a purchase order as a purchasing manager.

A prerequisite is the existence of a purchase order that can be released. Purchasing group is 003 and all purchase orders with a total value of 500 AED or more require an approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of already created purchase orders displays. |  |
| 3 | Search for Purchase Order Status | Enter the purchase order number in the search area, then choose Search. | The purchase orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Open Approve Purchase Orders | On the My Inbox screen, select the purchase order from the left screen. | The My Inbox screen displays. |  |
| 5 | Approve Purchase Order | On the Release Purchase Order screen, confirm your created purchase order information.Choose Approve.On the Submit Decision screen, add note if necessary and choose Submit. | The purchase order is approved. |  |

#### Check Purchase Order Approval Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check an existing purchase order's approval details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen displays. |  |
| 3 | Search for Purchase Order | Enter the purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the purchase order you want to preview, then go to the Purchase Order screen. | The Purchase Order screen displays. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The purchase order's approval details display. |  |

#### Preview Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to preview an existing purchase order form.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen displays. |  |
| 3 | Search for Purchase Order | Enter the purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the purchase order you want to preview, then go to the Purchase Order screen. | The Purchase Order screen displays. |  |
| 5 | Preview the Purchase Order | Go to the Output Management tab.In the Output Details area, choose the button Display Document next to Display:.Note Click the button Show More per Row in the upper right corner of table Output Management to expand the Output Details area. | The Purchase Order review screen displays.Note Follow the step 4.8 [Release Supplier Invoice (Optional)](#unique_28) [page ] 29 to check the status of the EDI message generated with the purchase order. |  |

### Update Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to update the sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Automatically Generated Sales Order | On the Manage Sales Orders screen, enter purchase order number in the Customer Reference field and choose Go. Make a note of the sales order number: __________. | Automatically created Sales Order is listed. |  |
| 4 | Navigate to Sales Order Screen | Choose the Sales Order Number line. | The Display Sales Orders xxx: Overview screen displays. |  |
| 5 | Update Item Price (Cost) | Choose Change, and then select line item and navigate to item conditions. Enter manually calculated value of the cost in pricing condition type PPR0.Check if pricing conditions PCE1 and PCE2 are containing value as pecified in purchase order item.Repeat this steps for all other line items. | Sales order net value is updated. |  |
| 6 | Save Document | Choose Save Document. | The order is saved and the order confirmation is printed out. |  |

### Process Sales Order Approval (Optional)

Purpose

This process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval described in the test script of Sell from Stock (BD9) scope item.

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a billing document by referring to the sales order created in the above step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar. You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The default billing setting is saved. |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document (s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of sales document created previously and choose Create. | The Creating Billing Documents screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: <current date>, then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________ | The system generates an invoice for billing:Material: Services (SERV)Debited Accounts: 10401010 Rcvbls Domestic DE Customer 3Credited Accounts: 41000000 Rev Domestic Prod22000000 Output tax (MWS)Cost Element / CO Object: none |  |
| 8 | Access the App | Open Manage Billing Documents (F0797) | The Manage Billing Documents screen displays. |  |
| 9 | Search for Previous Billing Document | In the billing document number recorded in the previous step, choose Enter. | The billing document created in the previous step displays. |  |
| 10 | Display Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 11 | Check Output Condition | On the Manage Billing Documents screen, choose the last Output Items tab. | There is one or moren than one entry in the item with BIL L ING_DOCUMENT output type. |  |
| 12 | Display Print Preview | On the Manage Billing Documents screen, choose Preview.Note You can also click the button Show More per Row in the upper right corner of table Output Items to expand the Output Details area. Then choose the button Display Document next to Display: to display PDF document. | Preview for PDF document displays. |  |
| 13 | Check Status of the EDI Output | Check the status of the output item with the Output Type EDI. | The status is Completed (4). Step 4.8 Release Supplier Invoice (Optional) can be refered to check the details of the purchase order message. |  |
| 14 | Cancel Billing Document (Optional) | Select certain billing document, and choose Cancel Billing Docs. | There is a log displays: Billing Document Canceled. |  |

### Check Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the supplier invoice which is created by EDI message of the billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as role Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Create Billing Documents screen displays. |  |
| 3 | Search for Supplier Invoice List | Enter in the Reference field with the billing document created in the previous step and choose Go. | The List of Supplier Invoices screen displays. |  |
| 4 | Check the Details of the Supplier Invoice | Select the line of the supplier invoiceNote A dialog displays with information: Invoice is of type Supplier Invoice - Advanced. Invoice is processed in advanced mode in a different browser tab. Select OK to open the Advanced Mode or select Cancel to stay in the current screen. | The Supplier Invoice screen displays. |  |

### Release Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to releasea blocked supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an approver set in preliminary step.Approver is set in preliminary step Update Cost Center for User Responsible. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice screen displays. |  |
| 4 | Approve Supplier Invoice | On the Release Blocked Invoice XXXXXXXX screen, choose Release.On the Submit Decision screen, add note if necessary and choose Submit. | Task is successfully processed. |  |

### Approve Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to approve a supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Supplier Invoices list screen displays. |  |
| 3 | Filter Supplier Invoice List | Fill in search criterial fields or leave them blank, and choose Go. | The Supplier Invoices list displays. |  |
| 4 | Check Supplier Invoice Detail | In the Supplier Invoiceslist, select an invoice document by selecting the entire row, which is blocked for payment. | The invoice document displays. |  |
| 5 | Release the Invoice | Choose Release. | The invoice is released. |  |
| 6 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

### EDI Message Monitoring (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor th EDI messages.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR). | The Interface Monitor screen displays. |  |
| 3 | Select a specific Date or a Date Range | Select one specific date or enter From (Date / Time): and To (Date/Time):, then chooseSearch. | The EDI messages created in the date or date range display in the Result List. |  |
| 4 | Choose a Number to View Details | In the Result List section, you can view the namespace that you entered in the Assign Recipients to Users (F2949) App. Select the number under the All Messages column of the Namespace / Interface. | The Monitoring and Error Handling screen displays. |  |
| 5 | Display Details of an EDI Message | On the left pane, you can expand the nodes to see how many messages are transferred in the brackets. On the right pane, you can see the details about an EDI message. | The message details display on the right screen. |  |

## Appendix

### Process Integration

The process to be test in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) |  |
| Accounts Payable (J60) |  |
| Real-Time Reporting and Monitoring for Procurement (1JI) |  |

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
- related-to :: [[03-financial-accounting-and-close/intercompany-billing-for-cross-company-cost-accounting-postings-4an-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3ZB_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 52,499 chars in the whole document
