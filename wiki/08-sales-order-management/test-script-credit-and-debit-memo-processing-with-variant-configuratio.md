---
id: 08-sales-order-management/test-script-credit-and-debit-memo-processing-with-variant-configuratio
title: "Test Script: Credit and Debit Memo Processing with Variant Configuration (7TZ_AE) (7TZ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item 7TZ: credit/debit memo requests with variant configuration, approval workflow, billing."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/debit-and-credit-memo-processing]
aliases: [7TZ_S4CLD2608_BPD_EN_AE]
keywords: [Debit and Credit Memo Processing, credit memo requests, debit memo requests, variant configuration, credit memo approval workflow, billing block removal, billing documents, item category assignment, cloud badi approval reason, approval reasons]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TZ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1228
topic: 08-sales-order-management/debit-and-credit-memo-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Credit and Debit Memo Processing with Variant Configuration (7TZ_AE) (7TZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Debit and Credit Memo Processing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Credit and Debit Memo Processing with Variant Configuration (7TZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860626)

[2 Prerequisites 4](#_Toc232860627)

[2.1 System Access 4](#_Toc232860628)

[2.2 Roles 4](#_Toc232860629)

[2.3 Master Data and Organizational Data 5](#_Toc232860630)

[2.4 Business Conditions 6](#_Toc232860631)

[2.5 Preliminary Steps 7](#_Toc232860632)

[2.5.1 Remove Billing Block from Order Type 7](#_Toc232860633)

[2.5.2 Change Default Item Category Assignment via SSCUI 8](#_Toc232860634)

[2.5.3 Preliminary Steps for Credit Memo Request (Optinal) 11](#_Toc232860635)

[2.5.3.1 Define and Assign Approval Reasons 11](#_Toc232860636)

[2.5.3.2 Implement Cloud BADI 13](#_Toc232860637)

[2.5.3.3 Manage Teams and Responsibilities 15](#_Toc232860638)

[2.5.3.4 Set up Workflow 16](#_Toc232860639)

[3 Overview Table 19](#_Toc232860640)

[4 Test Procedures 20](#_Toc232860641)

[4.1 Create Credit Memo Requests with Reference 20](#_Toc232860642)

[4.2 Create Credit Memo Requests without Reference (Optional) 21](#_Toc232860643)

[4.3 Approve/Reject/Rework Credit Memo Request (Optional) 24](#_Toc232860644)

[4.4 Remove Billing Block 25](#_Toc232860645)

[4.5 Create Credit Memo 26](#_Toc232860646)

[4.6 Create Debit Memo Requests with Reference 28](#_Toc232860647)

[4.7 Create Debit Memo Requests without Reference (Optional) 29](#_Toc232860648)

[4.8 Remove Billing Block 32](#_Toc232860649)

[4.9 Create Debit Memo 32](#_Toc232860650)

[5 Appendix 35](#_Toc232860651)

[5.1 Process Integration 35](#_Toc232860652)

[5.2 Succeeding Processes 35](#_Toc232860653)

[5.3 Scheduling Job (Alternative) 35](#_Toc232860654)

[5.3.1 Job Scheduling for Billing Creation (Alternative) 35](#_Toc232860655)

[5.3.2 Job Scheduling for Billing Release (Alternative) 36](#_Toc232860656)

[5.3.3 Job Scheduling for Billing Output (Alternative) 37](#_Toc232860657)

## Purpose

Overview

This scope item covers the credit memo and debit memo process with variant configuration materials. It explains how to create a credit memo request or debit memo request, either with reference to a sales order or without reference.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data and Organizational Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4HANA Cloud Public Edition system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

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

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1YT - Make-to-Order Production with Variant Configuration | You have completed the steps described in the Test Script 1YT - Make-to-Order Production with Variant Configuration, note down created sales order number and billing number for further use. |
| 4R6 - Sales Processing using Third-Party with Variant Configuration | You have completed the steps described in the Test Script 4R6 - Sales Processing using Third-Party with Variant Configuration. |

### Preliminary Steps

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

#### Change Default Item Category Assignment via SSCUI

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note The new item category G2VC and L2VC had been delivered and assigned as default item category for credit memo and debit memo for Third-Party with Variant Configuration scenario from the 2602 delivery. In case you still would like to use the original G2N and L2N as default item category, use this SSCUI to change back. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Pricing | Enter the following filters:Application Area: SalesSub Application Area: Sales Order Management and ProcessingIn the items table, select the item with item name: Assign Item Category (102807). | The Configure Your Solution - Assign Item Category: Change screen displays. |  |
| 5 | Go to Assign Item Category Change Overview | Choose Configure on the right to the Assign Item Category configuration step. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Go to Control Data | Select the relevant item category assignment for credit and debit. |  |  |
| 7 | Change Item Category Assignment for Credit Memo Request | Choose Entries and make the following entries:SaTy: CRItCGr: 0002DfltC: G2VCMLtCa: GMCSMLtCa: G2NChoose Save. |  |  |
| 8 | Change Item Category Assignment for Debit Memo Request | Choose Entries and make the following entries:SaTy: DRItCGr: 0002DfltC: L2VCMLtCa: LMCSMLtCa: L2NChoose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Item Category.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Go to Control Data | Select the relevant item category assignment for credit and debit. |  |  |
| 4 | Change Item Category Assignment for Credit Memo Request | Choose Entries and make the following entries:SaTy: CRItCGr: 0002DfltC: G2VCMLtCa: GMCSMLtCa: G2NChoose Save. |  |  |
| 5 | Change Item Category Assignment for Debit Memo Request | Choose Entries and make the following entries:SaTy: DRItCGr: 0002DfltC: L2VCMLtCa: LMCSMLtCa: L2NChoose Save. |  |  |

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

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Credit Memo Requests with Reference](#unique_14) [page ] 20 | Internal Sales Representative | Manage Credit Memo Requests (F1989) |  |
| [Create Credit Memo Requests without Reference (Optional)](#unique_15) [page ] 21 | Internal Sales Representative | Manage Credit Memo Requests (F1989) |  |
| [Approve/Reject/Rework Credit Memo Request (Optional)](#unique_16) [page ] 24 | Internal Sales Representative | My Inbox - All Items (F0862) |  |
| [Remove Billing Block](#unique_17) [page ] 32 | Internal Sales Representative | Manage Credit Memo Requests - Version 2 (F1989A) |  |
| [Create Credit Memo](#unique_18) [page ] 26 | Internal Sales Representative | Create Billing Documents (F0798) |  |
| [Create Debit Memo Requests with Reference](#unique_19) [page ] 28 | Sales Manager | Manage Debit Memo Requests (F1988) |  |
| [Create Debit Memo Requests without Reference (Optional)](#unique_20) [page ] 29 | Sales Manager | Manage Debit Memo Requests (F1988) |  |
| [Remove Billing Block](#unique_17) [page ] 32 | Internal Sales Representative | Manage Debit Memo Requests - Version 2 (F1988A) |  |
| [Create Debit Memo](#unique_21) [page ] 32 | Internal Sales Representative | Create Billing Documents (F0798) |  |

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

### Create Credit Memo Requests with Reference

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
| 2 | Access the App | Open Manage Credit Memo Requests (F1989). | The Manage Credit Memo Requests screen displays. |  |
| 3 | Navigate to Create Credit Memo Request | On Manage Credit Memo Requests screen, choose Create Credit Memo Request. | The Create screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Continue.Credit Memo Request Type: Credit Memo Request (CR)Note Regarding an existing order or billing document: Choose Create with Reference. Enter the billing document number or sales order number (which you created in preliminary scope item 1YT) and choose Continue. | The Create Credit Memo Request Overview screen displays. |  |
| 5 | Check VC Information | Select the item. Choose the Item Details: Configurations.Check the variant configuration information from the original sales order. |  |  |
| 6 | Check Pricing | Double-click sales order item and select Conditions tab. Pricing of variant components displays.Check the condition value of condition type PVA0.Choose Back. |  |  |
| 7 | Save Entries | Save your entries. | The order is saved and a billing block is assigned to the Credit Memo. |  |

### Create Credit Memo Requests without Reference (Optional)

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
| 2 | Access the App | Open Manage Credit Memo Requests (F1989). | The Manage Credit Memo Requests screen displays. |  |
| 3 | Navigate to Create Credit Memo Request | On the Manage Credit Memo Request screen, choose Create Credit Memo Request. | The Create Credit Memo Request screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Continue.Credit Memo Request Type: Credit Memo Request (CR) | The Create Credit Memo Request Overview screen displays. |  |
| 5 | Enter Order Quantity | Make the following entries and choose Enter:Sold-to Party: 33100001Order Reason: <poor quality>Customer Reference: <Customer Reference Number>Product: CM-FL-V00Target Quantity: <For example, 1 PC>Billing Date: <billing date> | The input-order quantities are entered. |  |
| 6 | Enter Characteristic Value | Choose value for characteristics below and choose Done.For material CM-FL-V00:Fork Size: <Small>Power Source: <Combustion, Electrical>Lifter Model: <Heavy, Standard>Wheel Type: <Cushion Tires, Pneumatic Tires>CR_SIZE: <Small, Medium, Large>Counterweight: <5.000 kg>AVC Count: <one, two, three>Battery Capacity(Ah): <50, 80, 140>Net Value: Varies according to characteristic valueFor material CM-MLFL-KM-VXX:On the Default Group tab:Lifter Model: <Heavy, Standard>Power Source: <Combustion>CR_SIZE: <Small, Medium, Large>AVC Count: <one, two, three>On the Technical tab:Fork Size: <Small, Normal, Large>Wheel Type: <Cushion Tires, Pneumatic Tires>The combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automaticallyWheel Type: Cushion Tires or Pneumatic TiresFork Size: Small or Medium or LargeCombination Two:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion Tires is filled in automatical-lyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Combination Three:Lifter Model: StandardPower Source: ElectricalWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Battery Capacity (Ah): 50 or 80 or 140 (140 only available when fork size is L)Choose Toggle Structure Panel icon on the top right corner.Choose product SF-FL-FORKSEAT-VXX in the Configuable item panel.Choose value for the following characteristic and choose Done.Seat Color: Black, White or GreySeat Type: Standard, Heavy Duty, or Air suspensionNote Heavy Duty is only selectable if the fork lifter model is Heavy. |  |  |
| 7 | Check Pricing | Double-click sales order item and select Conditions tab. Pricing of variant components displays.Check the condition value of condition type PVA0.Choose Back. |  |  |
| 8 | Save Entries | Save your entries. | The order is saved and a billing block is assigned to the Credit Memo. |  |

### Approve/Reject/Rework Credit Memo Request (Optional)

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

### Remove Billing Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove the billing block assigned to the credit memo by the sales order entry procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Credit Memo Requests - Version 2 (F1989A). | The Manage Credit Memo Requests - Version 2 screen displays. |  |
| 3 | Find Document | Enter the document number you created in last step and choose Go. | The document appears. |  |
| 4 | Remove Billing Block | Choose the document and select Billing Block -> Remove Billing Block at the bottom of the screen. |  |  |

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

### Create Debit Memo Requests with Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a billing document and debit the customer's account.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Debit Memo Requests (F1988). | The Manage Debit Memo Requests screen displays. |  |
| 3 | Navigate to Create Debit Memo Request | On Manage Debit Memo Requests screen, choose Create Debit Memo Requests.Note Regarding an existing order or billing document: Choose Create with Reference. Enter the billing document number or sales order number (which you created in preliminary scope item 1YT) and choose Copy. |  |  |
| 4 | Enter Debit Memo Request Type | Make the following entries and choose Continue.Debit Memo Request Type: Debit Memo Request (DR) | The Debit Memo Request Overview screen displays. |  |
| 5 | Check VC Information | Select the item. Choose Item Details: Configurations.Check the variant configuration information from the original sales order. |  |  |
| 6 | Check Pricing | Double-click sales order item and select the Conditions tab. Pricing of variant components displays.Check the condition value of condition type PVA0.Choose Back. |  |  |
| 7 | Save | Save your entries. | The order is saved and a billing block is assigned to the debit memo. |  |

### Create Debit Memo Requests without Reference (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a billing document and debit the customer's account.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Debit Memo Requests (F1988). | The Manage Debit Memo Requests screen displays. |  |
| 3 | Navigate to Create Debit Memo Request | On Manage Debit Memo Requests screen, choose Create Debit Memo Requests. |  |  |
| 4 | Enter Debit Memo Request Type | Make the following entries and choose Continue.Debit Memo Request Type: Debit Memo Request (DR) | The Debit Memo Request Overview screen displays. |  |
| 5 | Input Order Quantity | Make the following entries and choose Enter:Sold-to Party: 33100001Order reason: <Order reason>Customer Reference: <Customer Reference Number>Product : CM-FL-V00Target Quantity: For example, 1 PCNote If you create the debit memo request regarding an existing order or billing document, input the quantity: for example, 1 PC. | The input order quantities are entered. |  |
| 6 | Enter Characteristic Value | Choose value for characteristics below and choose Done.For material CM-FL-V00:Fork Size: <Small>Power Source: <Combustion, Electrical>Lifter Model: <Heavy, Standard>Wheel Type: <Cushion Tires, Pneumatic Tires>CR_SIZE: <Small, Medium, Large>Counterweight: <5.000 kg>AVC Count: <one, two, three>Battery Capacity(Ah): <50, 80, 140>Net Value: Varies according to characteristic valueFor material CM-MLFL-KM-VXX:On the Default Group tab:Lifter Model: <Heavy, Standard>Power Source: <Combustion>CR_SIZE: <Small, Medium, Large>AVC Count: <one, two, three>On the Technical tab:Fork Size: <Small, Normal, Large>Wheel Type: <Cushion Tires, Pneumatic Tires>The combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automaticallyWheel Type: Cushion Tires or Pneumatic TiresFork Size: Small or Medium or LargeCombination Two:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion Tires is filled in automatical-lyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Combination Three:Lifter Model: StandardPower Source: ElectricalWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Battery Capacity (Ah): 50 or 80 or 140 (140 only available when fork size is L)Choose Toggle Structure Panel icon on the top right corner.Choose product SF-FL-FORKSEAT-VXX in the Configuable item panel.Choose value for the following characteristic and choose Done.Seat Color: Black, White or GreySeat Type: Standard, Heavy Duty, or Air suspensionNote Heavy Duty is only selectable if the fork lifter model is Heavy. |  |  |
| 7 | Check Pricing | Double-click sales order item and select the Conditions tab. Pricing of variant components displays.Check the condition value of condition type PVA0.Choose Back. |  |  |
| 8 | Save | Save your entries. | The order is saved and a billing block is assigned to the debit memo. |  |

### Remove Billing Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove the billing block assigned to the debit memo by the sales order entry procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Debit Memo Requests - Version 2 (F1988A). | The Manage Debit Memo Requests - Version 2 screen displays. |  |
| 3 | Find Document | Enter the document number you created in last step and choose Go. | The document appears. |  |
| 4 | Remove Billing Block | Choose the document and select Billing Block -> Remove Billing Block at the bottom of the screen. |  |  |

### Create Debit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a debit memo and debit the customer's account.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings at the bottom bar, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON |  |  |
| 4 | Search Billing Due Items | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Select Billing Item(s) | Select row(s) of a sales document created previously, and choose Create Billing Documents. | The Billing Documentsscreen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Debit Memo (L2) and maintain billing date, for example, <current date>, then choose OK. | The new billing document is created. |  |
| 7 | Save Billing Document | On the Billing Document (F1901) screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | The system generates a billing invoice. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000 Rev Domestic Prod12100000 G/L ACC | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search Billing Document | Enter the Billing document number recorded in previous step. Choose Enter. | The billing document displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Update New Attachment (Optional) | In the Edit mode, add, delete, and update the attachments. Choose Save in the footer bar. |  |  |
| 7 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update these texts. Save your changes by choosing Save in the footer bar. |  |  |

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
> Flagged while digesting this document, not verified: Workflow example names the level-1 workflow 'First Approver - No conditions' and 'Net Value over AED 500', while the text says under AED 500 needs no approval; exact handling at 500/1000 boundaries is unspecified.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/invoice-correction-process-with-credit-memo-bkl-ae-test-script-sap-s-4]]
- related-to :: [[08-sales-order-management/test-script-credit-memo-processing-1ez-ae-sap-s-4hana-cloud-public-edi]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-debit-memo-processing-1f1-ae-sap-s-4hana-cloud-public-edit]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-invoice-correction-process-with-debit-memo-bdq-ae-1257]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 60,316 chars in the whole document
