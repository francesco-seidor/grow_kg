---
id: 08-sales-order-management/test-script-credit-memo-processing-1ez-ae-sap-s-4hana-cloud-public-edi
title: "Test Script: Credit Memo Processing (1EZ_AE) - SAP S/4HANA Cloud Public Edition 2608, United Arab Emirates (1EZ_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script for scope item 1EZ_AE: UAE credit memo requests, optional AED-threshold approval workflow, credit memo billing, PEPPOL eDocument cockpit, billing jobs."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/debit-and-credit-memo-processing]
aliases: [1EZ_S4CLD2608_BPD_EN_AE]
keywords: [Debit and Credit Memo Processing, credit memo requests, credit memo billing, credit memo approval, approval workflow, peppol e-invoicing, edocument cockpit, approval reasons, cloud badi, teams and responsibilities]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1EZ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-715
topic: 08-sales-order-management/debit-and-credit-memo-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Credit Memo Processing (1EZ_AE) - SAP S/4HANA Cloud Public Edition 2608, United Arab Emirates (1EZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1EZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Debit and Credit Memo Processing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Credit Memo Processing (1EZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232846839)

[2 Prerequisites 4](#_Toc232846840)

[2.1 System Access 4](#_Toc232846841)

[2.2 Roles 4](#_Toc232846842)

[2.3 Master Data and Organizational Data 5](#_Toc232846843)

[2.4 Preliminary Steps 7](#_Toc232846844)

[2.4.1 Create Reference Order or Billing (Optional) 7](#_Toc232846845)

[2.4.2 Remove Billing Block from Order Type 8](#_Toc232846846)

[2.4.3 Preliminary Steps for Credit Memo Request (Optinal) 10](#_Toc232846847)

[2.4.3.1 Define and Assign Approval Reasons 10](#_Toc232846848)

[2.4.3.2 Implement Cloud BADI 12](#_Toc232846849)

[2.4.3.3 Manage Teams and Responsibilities 14](#_Toc232846850)

[2.4.3.4 Set up Workflow 15](#_Toc232846851)

[2.4.4 Create Condition Records (Optional) 17](#_Toc232846852)

[2.4.5 Preliminary Steps for Electronic Invoicing (PEPPOL) 17](#_Toc232846853)

[2.4.5.1 Define Identification Types for Business Partners 18](#_Toc232846854)

[2.4.5.2 Maintain Company Code Data (FINSC_T001Z_N) 20](#_Toc232846855)

[2.4.5.3 Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552) 22](#_Toc232846856)

[2.4.5.4 Maintain Business Partner Master Data 25](#_Toc232846857)

[2.4.5.5 Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301) 26](#_Toc232846858)

[2.4.5.6 Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304) 27](#_Toc232846859)

[2.4.6 Optional Steps for Electronic Invoicing (PEPPOL) 29](#_Toc232846860)

[2.4.6.1 Business Partner Master Data Maintenance for Electronic Invoicing (Optional) 29](#_Toc232846861)

[2.4.6.2 Value Mapping Maintenance for Electronic Invoicing (Optional) 30](#_Toc232846862)

[3 Overview Table 35](#_Toc232846863)

[4 Test Procedures 36](#_Toc232846864)

[4.1 Create Credit Memo Requests 36](#_Toc232846865)

[4.2 Create Attachment for Credit Memo Request (Optional) 38](#_Toc232846866)

[4.3 Process Credit Memo Request Approval (Optional) 39](#_Toc232846867)

[4.3.1 Withdraw from Approval 40](#_Toc232846868)

[4.3.2 Approve/Reject/Rework Credit Memo Request (Optional) 41](#_Toc232846869)

[4.3.3 Rework Credit Memo Request 42](#_Toc232846870)

[4.3.3.1 Check the Notifications 42](#_Toc232846871)

[4.3.3.2 Change Credit Memo Request 43](#_Toc232846872)

[4.4 Create Credit Memo 44](#_Toc232846873)

[4.5 Create Attachment for Billing (Optional) 46](#_Toc232846874)

[4.6 eDocument Cockpit 47](#_Toc232846875)

[4.7 Add Text in Billing Document (Optional) 49](#_Toc232846876)

[5 Appendix 51](#_Toc232846877)

[5.1 Process Integration 51](#_Toc232846878)

[5.2 Succeeding Processes 51](#_Toc232846879)

[5.3 Scheduling Job (Alternative) 51](#_Toc232846880)

[5.3.1 Job Scheduling for Billing Creation (Alternative) 51](#_Toc232846881)

[5.3.2 Job Scheduling for Billing Release (Alternative) 52](#_Toc232846882)

[5.3.3 Job Scheduling for Billing Output (Alternative) 53](#_Toc232846883)

## Purpose

Overview

A credit memo request is created with the amount to be credited and placed on a billing block for review. It is then released to become billing relevant and appear on the billing due list. The periodic billing process creates a credit memo to be sent to the customer and posts a journal entry.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |

### Master Data and Organizational Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this test script.

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the test script with other SAP Best Practices default values that have the same characteristics. |

|  |
| --- |
| Note Using Your Own Master DataYou also can use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch. |  |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No serial number, no batch. |  |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy). | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG) (BLP). |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP). |
| Material | SM0001 | Service Material 01 |  |
| Material | NS0002 | Non-Stock Material 02 |  |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the scope item Make-to-Order Production with Variant Configuration (1YT). |
| Sold-to party | 33100001 | Domestic UAE Customer 1 | You can test the scope item using another domestic customer. |
| Ship-to party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Preliminary Steps

#### Create Reference Order or Billing (Optional)

Purpose

As an option, you can create Reference or Billing Orders to use when creating credit memo requests.

Follow procedures described in following process documents to create Reference Orders or Billing Orders:

| IDs | Titles |
| --- | --- |
| BD9 | Sell from Stock |
| BD3 | Sales Processing using Third-Party with Shipping Notification |
| BDK | Sales Processing Using Third-Party Without Shipping Notification |
| BDN | Sales of Non-Stock Item with Order-Specific Procurement |
| BDH | Sales Order Entry with One-Time Customer |
| BKJ | Sales Order Processing with Customer Down Payment |
| BKA | Free Goods Processing |
| BKZ | Sales Order Processing with Invoice List and Collective Billing |

#### Remove Billing Block from Order Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from sales order type via SSCUI.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configue Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Allication Area: SalesSub Allication Area: Sales order Management and Processing | All entries display in theConfiguration Items section. |  |
| 5 | Find the Entry | Find the entry with Configure Sales Document types item name and choose the arrow icon at the item end. | The Configure Your Solution - Sales Documents screen displays. |  |
| 6 | Navigate to Configure Sales Document Types | In the Configuration Steps section, choose Configure in the Actions column for Configure Sales Document Types step. | The Change View "Configure sales Document Types": Overview screen displays. |  |
| 7 | Choose Sales Document Type | Choose Item CR and double click it. | The Change View "Configure sales Document Types": Detail screen displays. |  |
| 8 | Remove Billing Block | Remove entry Y8 in Billing Block. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Sales Document Types | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Configure Sales Document types and create the following settings. | The Change View "Configure sales Document Types": Overview screen displays. |  |
| 3 | Choose Sales Document Type | Choose Item CR and double click it. | The Change View "Configure sales Document Types": Detail screen displays. |  |
| 4 | Remove Billing Block | Remove entry Y8 in Billing Block. |  |  |

#### Preliminary Steps for Credit Memo Request (Optinal)

##### Define and Assign Approval Reasons

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to define and assign approval reasons via SSCUI.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configue Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Basic Functions | All entries display in the Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Sales Document Approvals item name and choose the arrow icon at the item end. | The Configure Your Solution - Sales Document Approvals screen displays. |  |
| Perform the following steps 6-7 to define approval reason. |  |  |  |  |
| 7 | Navigate to Define Reasons Screen | In the Configuration Steps section, choose Configure in the Actions column for Define Reasons for Approval Requests step. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 8 | Define Approval Reason | Choose New Entries, enter the following data and choose Save.Approval Request Reason ID: for example: ZCR1Approval Request Reason: for example: Document needs approval | Approval reason is defined. |  |
| Perform the following steps 8-9 to assign approval reason to Credit Memo Request. |  |  |  |  |
| 10 | Navigate to Assign Reasons Screen | In the Configuration Steps section, choose Configure in the Actions column for Assign Reasons for Approval Requests step. | The Assign Reasons for Approval Requests: Overview screen displays. |  |
| 11 | Assign Approval Reason to Sales Order | Choose New Entries, enter the following data and choose Save.Document Category: KApproval Request Reason: for example: ZCR1 | Approval reason is assigned to sales order. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| Perform the following steps 2-3 to define approval reason. |  |  |  |  |
| 3 | Navigate to Define Reasons Screen | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Reasons for Approval Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 4 | Define Approval Reason | Choose New Entries, enter the following data and choose Save.Approval Request Reason ID: for example: ZCR1Approval Request Reason: for example: Document needs approval | Approval reason is defined. |  |
| Perform the following steps 4-5 to assign approval reason to Credit Memo Request. |  |  |  |  |
| 6 | Navigate to Assign Reasons Screen | xOn the Configuration Activities tab and search for the following activity: Assign Reasons for Approval Requests.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Reasons for Approval Requests: Overview screen displays. |  |
| 7 | Assign Approval Reason to Sales Order | Choose New Entries, enter the following data and choose Save.Document Category: KApproval Request Reason: for example: ZCR1 | Approval reason is assigned to sales order. |  |

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

This means that if you want to use the workflow for the approval of sales documents, implementing this BADI is a prerequisite. In the Manage Credit Memo Requests (F1989) app, you define additional preconditions and approval steps.

When the system sets an approval request reason for a sales document, the approval workflow is triggered automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Custom Fields and Logic (Obsolete) (F1481). | The Custom Fields and Logic screen displays. |  |
| 3 | Navigate to Custom Logic | In the menu bar at the top, choose Custom Logic. | The Enhancement Implementations section displays. |  |
| 4 | Create Enhancement Implementation | Choose Create.Make the following entries and choose Create:Business Context: Sales： Sales DocumentBADI Description: Set Approval Request Reasons for Sales DocumentsImplementation Description: for example, Set Approval Reason for Sales DocumentsImplementation ID： Generated by default | The Draft Logic section displays. |  |
| 5 | Add Coding | Choose Draft, implement your logic in Draft Logic section, for example:if salesdocument-sddocumentcategory = 'K' and salesdocument-sddocumentreason = '005'.salesdocapprovalreason = 'ZCR1'.endif.Note It is possible to have sales document approvals for other categories of sales documents. The coding above can be taken as independent coding which can be added to the BAdI implementation without removing possible other coding. |  |  |
| 6 | Save and Publish | Choose Save Draft.Choose Publish. | Custom logic is published. |  |

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain the teams and responsibilities for credit memo workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create A New Team | Choose Create. | The Team screen displays. |  |
| 4 | Enter General Information | Make the following entries and press Enter:Name: credit memo workflowDescription: credit memo workflowStatus: EnabledType: SALES | Users created a new team and appropriate function(s) have been assigned to the business user(s) to be configured as approver(s).The Select: Business Partner screen displays. |  |
| 5 | Add Team Members | In Team Members, choose Create.From the Items section, select a Business Partner checkbox and choose OK.Last Name: Sales Manager | The Team screen displays. |  |
| 6 | Add Function to Team Members | In the Functions field, choose Select. In the Select: Functions dialog box, choose the following functions, and choose OK.CMR1LVLA: Sales Document Approver - Level 1CMR2LVLA: Sales Document Approver - Level 2Choose Save to save the team. | Team is saved. |  |
| 7 | Check Team Status | Chosse Save. | Team status is ready to use. |  |

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

In below example, if net amount of the credit memo request is more than AED 1000, "Sales Document Approver - Level 2" can approve. If net amount of the credit memo request is more than AED 500 but less than AED 1000, "Sales Document Approver - Level 1" can approve. If net value of the credit memo request is less than AED 500, no approval is required.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Document Workflows (F3014). | The Manage Workflows screen displays. |  |
| 3 | Create Workflows | Choose Workflows for Credit Memo Requests next to Workflow.Choose Add.Note If the workflow has already been defined, skip step 4 to 10. | The New Workflow screen displays. |  |
| 4 | Maintain workflow for 2nd level approve | Make the following entries.In the Header tab:Name: <Second Approver- Net Value over 1000 AED> |  |  |
| 5 | Set Preconditions | On the Preconditions tab, choose Net Amount is greater than, then enter below data:Currency: AEDAmount: 1000 | Preconditions are set. |  |
| 6 | Add Steps | From the Steps section, choose Add.Make the following entries.In the Header tab:Type: Release of credit memo requestIn the Recipients tab:Assignment By: RoleRole: Sales Document Approver - Level 2In the Exception Handling tab:Name: Rework Credit Memo RequestRequired Action: Rework of Credit Memo RequestAction Result: Restart WorkflowChoose Add to append this step to the workflow and choose Save. | The first workflow is created. |  |
| 7 | Create Another Workflow | Choose Back to the Manage Workflows screen.Choose Add. | The New Workflow screen displays. |  |
| 8 | Maintain Workflow for 1st Level Approve | Make the following entries.In the Header tab:Name: First Approver- No conditions |  |  |
| 9 | Add Steps | From the Steps section, choose Add.Make the following entries.In the Header tab:Type: Release of credit memo requestIn the Recipients tab: Assignment By: RoleRole: Sales Document Approver - Level 1In the Exception Handling tab:Name: Rework Credit Memo RequestRequired Action: Rework of Credit Memo RequestAction Result: Restart WorkflowChoose Add to append this step to the workflow and choose Save. | The first level approve workflow is created. |  |
| 10 | Activate Workflows | Choose Back to the Manage Workflow screen.Choose Define Order. Adjust the order as below:Second Approver - Net Value over AED 1000: Order 1First Approver- Net Value over AED 500: Order 2Choose Activate to active the workflows. | Workflows are activated. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

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

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Credit Memo Requests](#unique_23) [page ] 36 | Internal Sales Representative | Manage Credit Memo Requests - Version 2 (F1989A) | The Manage Credit Memo Requests screen displays. |
| [Create Attachment for Credit Memo Request (Optional)](#unique_24) [page ] 38 | Internal Sales Representative | Manage Credit Memo Requests - Version 2 (F1989A) |  |
| Process Credit Memo request Approval (Optional) |  |  |  |
| [Withdraw from Approval](#unique_25) [page ] 40 | Internal Sales Representative | Manage Credit Memo Requests - Version 2 (F1989A) |  |
| [Approve/Reject/Rework Credit Memo Request (Optional)](#unique_26) [page ] 41 | Sales Manager | My Inbox - All Items (F0862) | Make the decision to approve, reject and rework the credit memo request. |
| Rework Credit Memo Request |  |  |  |
| [Check the Notifications](#unique_27) [page ] 42 | Internal Sales Representative | My Inbox - All Items (F0862) |  |
| [Change Credit Memo Request](#unique_28) [page ] 43 | Internal Sales Representative | Manage Credit Memo Requests - Version 2 (F1989A) |  |
| [Create Credit Memo](#unique_29) [page ] 44 | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |

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

### Create Credit Memo Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a billing document and credit the customer's account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Credit Memo Requests - Version 2 (F1989A). | The Manage Credit Memo Requests - Version 2 screen displays. |  |
| 3 | Navigate to Create Credit Memo Request | Choose Create. | The Create screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Continue.Credit Memo Request Type: Credit Memo Request (CR)Note Regarding an existing order or billing document: Choose Create with Reference. Enter the billing document number or sales order number and choose Continue. | The Create Credit Memo Request Overview screen displays. |  |
| 5 | Enter Order Quantity | Make the following entries and choose Enter:Sold-to Party: 33100001Order Reason: <poor quality>Customer Reference: <Customer Reference Number>Product: <Material Number>Target Quantity: <For example, 1 PC>Note If you create the credit memo request regarding an existing order or billing document, input the quantity: for example, 1 PC.Billing Date: <billing date>Product: <material number>Quantity: for example, 1 PC | The input-order quantities are entered. |  |
| 6 | Save Entries | Save your entries. | The order is saved and a billing block is assigned to the Credit Memo. |  |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Credit Memo Requests - Version 2 (F1989A). | The Manage Credit Memo Requests - Version 2 screen displays. |  |
| 3 | Search for Sales Order | Enter search terms in filter bar and choose Go.For example, enter Credit Memo Request number in the Credit Memo Request field. | Credit Memo requests display in the result list. |  |
| 4 | Navigate to Sales Order Screen | Choose sales order number and select Display Credit Memo Request. |  |  |
| 5 | Check Output Condition | On the Display Credit Memo Req xxx: Overview screen, choose More Extras Output Header Edit.Note Partner function Employee Responsible is prerequisite for credit memo request output. It can be added under Partners tab of credit memo request header. | The document prints. |  |
| 6 | Display Print Preview | On the Display Credit Memo Req xxx: Output screen, select the line already created for the print output.Choose Display PDF Document. | Choose your local destination.Choose Print. |  |

|  |
| --- |
| Note In the Manage Credit Memo Requests - Version 2 (F1989A) app, you can navigate to a fact sheet screen:On the Manage Credit Memo Requests - Version 2 screen, enter search terms in the filter bar and choose Go.In search result, select your credit memo request number and choose Credit Memo Request Number. |

### Create Attachment for Credit Memo Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for a credit memo request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Credit Memo Requests - Version 2 (F1989A). | The Manage Credit Memo Requests - Version 2 screen displays. |  |
| 3 | Navigate to Display Credit Memo Request Screen | On the Manage Credit Memo Requests - Version 2 screen, enter the respective order number created in previous step in the Cedit Memo Requests and choose Go.Choose the credit memo request line that displays. |  |  |
| 4 | Create Attachment for Credit Memo Request | Choose Change, then choose Services for Object on the top right corner of screen, choose Create Attachment. | The Import File screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and Choose Open, then choose Save. | The attachment is successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of screen, choose Attachment List. | Attachment brings up in the Service: Attachment list screen. |  |

### Process Credit Memo Request Approval (Optional)

|  |
| --- |
| Note Only relevant if below conditions are fulfilled:Approval reason(s) is defined and assigned, details refer to the Define and Assign Approval Reasons chapter.The Cloud BADI that returns an approval reasons are implemented, details refer to the Implement Cloud BADI chapter.Total amount of the order is not less than AED 500. |

#### Withdraw from Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the internal sales representative withdraw sales order approval.

Prerequisite

Sales manager doesn’t make approval decision yet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Credit Memo Requests - Version 2 (F1989A). | The Manage Credit Memo Requests - Version 2 screen displays. |  |
| 3 | Navigate to Manage Credit Memo Requests | On the Manage Credit Memo Request - Version 2, enter the respective credit memo request number created in previous step in the Credit Memo Requests and choose Go.Choose the credit memo request, and choose Change Credit Memo Request. | The Display Credit Memo Request xxx: Overview screen displays. |  |
| 4 | Withdraw Approval Request | In the menu bar at the top, choose Edit > Additional Functions > >Withdraw Approval Request .Choose Continue to confirm the information shown as The approval request for sales document XXXXXXX was withdrawn. | The approval request is withdrawn. |  |
| 5 | Change Credit Memo Request | On the Change Credit Memo Request: Overview screen, make some changes, for example:Valid to: <Enter a Date> | Approval status is changed to In Approval. |  |

#### Approve/Reject/Rework Credit Memo Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, sales manager makes approval decision: release, reject or request rework.

Prerequisite

Approval status of the Credit Memo Request is In Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox - All Items (F0862).You can also choose the Notifications icon on the top right corner to navigate to the My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve/Reject/Rework | You receive the notification of the credit memo request. Choose one from the options on the bottom bar.Option 1: ReleaseOption 2: RejectOption 3: Request Rework | The Submit Decision dialog box displays. |  |
| 5 | Sumbit | Enter some comments and choose Submit. | Based on above decisions, choose next steps accordingly:Release: the whole process ends, no subsequent step is needed.Reject: the whole process ends, no subsequent step is needed.Request Rework: go to the Rework Credit Memo Requests chapter. |  |

#### Rework Credit Memo Request

|  |
| --- |
| Note Only relevant if the workflow is set as Request Rework by sales manager previously. |

##### Check the Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, internal sales representative check the notifications.

Prerequisite

Approval status of the sales order is To be reworked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox - All Items (F0862).You can also choose Notifications icon on the top right corner to navigate to the My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Check Inbox | Check the inbox items with relative Credit Memo Request. | Orders which needs to be reworked are displayed.If rework is not required, sales representative can be set "Rework not Required" in the inbox.If rework is required, go to the Change Credit Memo Request chapter. |  |

##### Change Credit Memo Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, internal sales representative change the credit memo request.

Prerequisite

Approval status of the credit memo request is rework.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Credit Memo Requests - Version 2 (F1989A). | The Manage Credit Memo Requests - Version 2 screen displays. |  |
| 3 | Navigate to Credit Memo Request | On the Manage Credit Memo Request - Version 2 screen, enter the respective credit memo request number created in previous step, and choose Go.Choose the arrow icon of the sales order line that displays. | The Display Credit Memo Request xxx: Overview screen displays. |  |
| 4 | Navigate to Credit Memo Request | Choose Change. | The Change Credit Memo Request xxx: Overview screen displays. |  |
| 5 | Change Credit Memo Request | On the Change Credit Memo Request xxx: Overview screen, make some changes and save, for example:Order Quantity: <Enter a New Quantity> | Approval status is changed to In Approval if the order amount is higher than amount set in the Implement Cloud BADI chapter.If amount > AED 500, go to the Process Credit Memo Request Approval chapter. |  |

### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a billing document and credit the customer’s account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Setting in the bottom bar.You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically Post Billing Documents: ONDisplay Billing Document After Creation: ON |  |  |
| 4 | Search for Billing List | From the search condition, enter a criteria if necessary. | Sales documents display. |  |
| 5 | Choose Individual Billing Document | Select a row of SD document created previously.Choose Create Billing Documents. | The Create Billing Documents (F0798) screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Credit Memo (G2) and maintain billing date, for example, <current date>.Choose OK. | The new billing document is created. |  |
| 7 | Display Billing Document after Creation | On the Billing Document (F1901) screen, choose Save.Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000 Rev Domestic Prod | 41000000 Rev Domestic Prod0 | none |

### Create Attachment for Billing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachments for billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F2250). | The Display Billing Documents screen displays. |  |
| 3 | Enter Billing Number | On the Display Billing Documents screen, enter <the respective invoice number created in previous step>, and choose Continue. | The Debit Memo xxx Display: Overview of Billing Items screen displays. |  |
| 4 | Create Attachment | Choose Change Bill. Doc., choose Services for Object in the upper right corner of screen, choose Create Attachment. | The Import File Screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.On the Open screen, choose local path and file, select Open. | The attachment is successfully created. |  |
| 6 | Check Attachment | Choose Services for Object in the top right corner of screen, choose Attachment list. | Attachment displays on the Service: Attachment list screen. |  |

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

### Add Text in Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to add a text in billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Billing Documents (VF02) . |  |  |
| 3 | Enter Billing Number | On the Change Billing Documents screen, enter the respective billing document number created in the previous step.Press Enter. | The billing document is displayed. |  |
| 4 | Enter External Invoice Number and Date | Choose Display Header Details, then choose Header Texts tab.On the left side, choose External Number of Invoice text type, and enter your External Invoice Number.Repeat the same for External Date of Invoice and enter the date. | The relevant text is added. |  |
| 5 | Enter Invoice Revision Number and Date (Optional) | Choose the Display Header Details and then choose the Header Texts tab.On the left side, double-click the text type Invoice Revision Number and enter your Invoice Revision Number. Repeat the same for Invoice Revision Date and enter the date. | The relevant text is added. |  |
| 6 | Save Changes | Save your changes by choosing Save in the footer bar. | The billing document is saved. |  |

Display Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Billing Documents (VF03) . | The Display Billing Documents screen displays. |  |
| 3 | Enter Billing Number | On the Display Billing Documents screen, enter the respective billing document number and choose Continue. | The billing document is displayed. |  |
| 4 | Check Output Condition | On the Invoice xxxxxxxx (F2) Display: Overview of Billing Items screen, choose More > Goto > Header > Output. |  |  |
| 5 | Display PDF Document | On the Invoice xxxxxxxx (F2) Display: Output screen, select output item with Output Type BILLING_DOCUMENT and Form Template SDBIL_INVOICE_RU. Choose Display PDF Document. | Preview for PDF document displays |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Succeeding Processes

| Process | Business Condition |
| --- | --- |
| Accounts Receivable(J59) (optional) | Post a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Order Fulfillment Monitoring and Operations(BKK) | This test script describes the collection of periodic activities, such as day’s ending activities.Using the master data from this document, complete the following activities described in the test script:Sales Order Fulfillment Monitoring and Operations (BKK) (sections Review Sales Documents Blocked for Billing, Review Billing Due List, Review Log of Collective Invoice Creation and Review List of Blocked (for accounting) Billing Documents) |

### Scheduling Job (Alternative)

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
> Flagged while digesting this document, not verified: UAE (AE) script gives Malaysia-specific instructions in the PEPPOL preliminary steps: local version is set to Malaysia for 'Define Identification Types' and 'Maintain Company Code Data', and the BP step refers to a 'Malaysia participant ID', while the process-communication step sets United Arab Emirates.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Optional step 'Remove Billing Block from Order Type' removes entry Y8 for sales document type CR, yet the credit memo request step expects a billing block to be assigned on save, and the Purpose describes the request as placed on billing block for review before release.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/invoice-correction-process-with-credit-memo-bkl-ae-test-script-sap-s-4]]
- related-to :: [[08-sales-order-management/test-script-credit-and-debit-memo-processing-with-variant-configuratio]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-debit-memo-processing-1f1-ae-sap-s-4hana-cloud-public-edit]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-invoice-correction-process-with-debit-memo-bdq-ae-1257]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1EZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 90,141 chars in the whole document
