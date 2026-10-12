---
id: 08-sales-order-management/test-script-sales-quotation-bdg-ae-sap-s-4hana-cloud-public-edition-26
title: "Test Script: Sales Quotation (BDG_AE) - SAP S/4HANA Cloud Public Edition 2608 (BDG_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script (AE) for Sales Quotation: roles, sample data, optional approval-workflow setup, and create/approve/change/reject steps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-quotations]
aliases: [BDG_S4CLD2608_BPD_EN_AE]
keywords: [Sales Quotations, sales quotation, quotation approval, approval reasons, cloud badi, teams and responsibilities, sales document workflows, quotation rework, quotation rejection, quotation changes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDG_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1253
topic: 08-sales-order-management/sales-quotations
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Quotation (BDG_AE) - SAP S/4HANA Cloud Public Edition 2608 (BDG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Quotations** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Quotation (BDG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861733)

[2 Prerequisites 4](#_Toc232861734)

[2.1 System Access 4](#_Toc232861735)

[2.2 Roles 4](#_Toc232861736)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861737)

[2.4 Preliminary Steps 7](#_Toc232861738)

[2.4.1 Preliminary Steps for Quotation Approval (Optional) 7](#_Toc232861739)

[2.4.1.1 Define and Assign Approval Reasons 7](#_Toc232861740)

[2.4.1.2 Implement Cloud BAdI 9](#_Toc232861741)

[2.4.1.3 Manage Teams and Responsibilities 11](#_Toc232861742)

[2.4.1.4 Set up Workflow 12](#_Toc232861743)

[2.4.2 Create Condition Records (Optional) 15](#_Toc232861744)

[2.4.3 Manage Situation Types (Optional) 15](#_Toc232861745)

[3 Overview Table 17](#_Toc232861746)

[4 Test Procedures 18](#_Toc232861747)

[4.1 Create Sales Quotation 18](#_Toc232861748)

[4.2 Process Sales Quotation Approval (Optional) 20](#_Toc232861749)

[4.2.1 Withdraw from Approval 21](#_Toc232861750)

[4.2.2 Approve/Reject/Rework Quotation 22](#_Toc232861751)

[4.2.3 Rework Sales Quotation 23](#_Toc232861752)

[4.2.3.1 Change Quotation (Optional) 23](#_Toc232861753)

[4.2.3.2 Set Quotation as Rework not Required 24](#_Toc232861754)

[4.2.3.3 Release the Reworked Quotation 25](#_Toc232861755)

[4.3 Change Quotation 26](#_Toc232861756)

[4.4 Reject Sales Quotation 27](#_Toc232861757)

[5 Appendix 29](#_Toc232861758)

[5.1 Process Integration 29](#_Toc232861759)

[5.1.1 Succeeding Processes 29](#_Toc232861760)

## Purpose

Overview

This scope item starts when requests for quotations are received from customers. Quotations are created in the system and can be either accepted or rejected by customers.

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

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG10 | Trad.Good 10,PD,Third PartyTrading Good for regular Trading (MRP planning) with item category group CBOR.no Serial no.; no batch |  |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no Serial no.; no batch | Substituted material: C01_MD. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.no Serial no.; no batch | Substituted material: C02_MD. |
| Material | TG13 | Trad.Good 13,Reorder Point,Thrd PartyTrading Good for Regular Trading (reorder point planning) with item category group CBNA.no batch |  |
| Material | TG14 | Trad.Good 14,PD,Bought-In,H14Trading material with item category group CBUK (Reorder point planning, bought in item).no batch |  |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFOno Serial no.; batch-controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ).Substituted material: C03_MD |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDno Serial no.; batch-controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ).Substituted material: C04_MD |
| Material | SM0001 | Service Material 01 |  |
| Material | NS0002 | Non-Stock Material 02 |  |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the scope item Make-to-Order Production with Variant Configuration (1YT). |
| Sold-to party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Preliminary Steps

#### Preliminary Steps for Quotation Approval (Optional)

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Basic Functions | All entries display in Configuratio Items section. |  |
| 5 | Find the Entry | Find the entry with Sales Document Approvals item name and choose arrow at the item end. | The Configure Your Solution - Sales Document Approvals screen displays. |  |
| 6 | Navigate to Define Reasons Screen | In Configuration Steps section, choose Configure in the Actions column for Define Reasons for Approval Requests step. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 7 | Define Approval Reason | Choose New Entries, enter the following data, and choose Save.Approval Request Reason ID: for example: ZQT1Approval Request Reason: for example: Document needs approval | Approval reason is defined. |  |
| 8 | Navigate to Assign Reasons Screen | In Configuration Steps section, choose Configure in the Actions column for Define Reasons for Approval Requests step. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 9 | Assign Approval Reason to Quotation | Choose New Entries, enter the following data, and choose Save.Ducoment Category: BApproval Request Reason: for example: ZQT1 | Approval reason is assigned to quotation. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Reasons for Approval Requests | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Reasons for Approval Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Reasons for Approval Requests: Overview screen displays. |  |
| 3 | Define Approval Reason | Choose New Entries, enter the following data, and choose Save.Approval Request Reason ID: for example: ZQT1Approval Request Reason: for example: Document needs approval | Approval reason is defined. |  |
| 4 | Open Assign Reasons for Approval Requests | Go to the Business Processes Configuration app, search for the following activity: Define Reasons for Approval Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Reasons for Approval Requests: Overview screen displays. |  |
| 5 | Assign Approval Reason to Quotation | Choose New Entries, enter the following data, and choose Save.Ducoment Category: BApproval Request Reason: for example: ZQT1 | Approval reason is assigned to quotation. |  |

##### Implement Cloud BAdI

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Business Add-In (BAdI) SD_APM_SET_APPROVAL_REASON is called whenever a sales document is saved by a business user. It determines whether a sales document needs to be sent to an approver and, if so, set an approval request reason on sales document header level.

This means that if you want to use the workflow for the approval of sales documents, implementing this BAdI is a prerequisite. In the Manage Sales Document Workflows app, you define additional preconditions and approval steps.

When the system sets an approval request reason for a sales document, the approval workflow is triggered automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Custom Logic (F6957). | The Custom Logic screen displays. |  |
| 3 | Search or Create Custom Logic | In the search box, input below information, and choose Go.Set Approval Request Reasons for Sales DocumentsCheck if the status of the custom logic is published.If not, please choose the customer logic and choose Publish.Note If there is no relevant custom logic, please go to step 4 to 6 to create your custom logic. | The Custom Logic is ready to use |  |
| 4 | Input Extension Point | Choose Create, make the following entry, and then choose Search:Extension points: SD_APM_SET_APPROVAL_REASON | The New Implementation screen displays. |  |
| 5 | Create Custom Logic | Choose the extension points and choose Step 2. In the section of Implementation ID, make following entries:Implementation Description: Set Approval Request Reasons for Sales DocumentsImplementation ID: for example, YY1_SETAPPROVALREQUESTREASONSFChoose Review.Choose Create. | The custom logic is created. |  |
| 6 | Publish the Custom Logic | Back to Custom Logic screen, and choose the custom logic you created in the last step.Choose Publish. | Custom logic is published. |  |
| 7 | Add/change Coding (Optional) | You can change the code of the custom logic if needed.Choose the custom logic and click the line.Choose Open Code Editor in the header of the screen.Choose Edit to change/add code.For example:Sample Codeif salesdocument-sddocumentcategory = 'B' and salesdocument-sddocumentreason = '005'. salesdocapprovalreason = 'ZQT1'. endif.Note Please note that it is possible to have sales document approvals also for other categories of sales documents.The coding mentioned above can be seen as independent coding that can be added to the BAdI implementation without removing possible other codingYou can choose Show Sample Code to copy the suggested sample code if needed.Choose Publish to save the code you created or added. | The code for custom logic is changed. |  |

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain the teams and responsibilities for quotation workflow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). |  |  |
| 3 | Create A New Team | Choose Create Team. |  |  |
| 4 | Enter General Information | Make the following entries and press Enter:Name: Quotation WorkflowDescription: Quotation WorkflowStatus: Ready to UseType: SALES |  |  |
| 5 | Add Team Members | On Team Members tab, choose Add.From the Items section, select a Business Partner checkbox and choose OK.Last Name: SalesManager | The Select: Business Partner screen displays.Team member sales manager is added. |  |
| 6 | Add Function to Team Members | In the Function field, choose Select. On the Select: Functions screen, select the following functions, and choose OK.CMR1LVLA: Sales Document Approver -Level 1CMR2LVLA: Sales Document Approver -Level 2 |  |  |
| 7 | Save | Choose Save. | User created a new team and appropriate function(s) have been assigned to the business user(s) to be configured as approver(s). |  |

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

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Document Workflows (F3014). | The Manage Workflows screen displays. |  |
| 3 | Add the First Workflow | Choose Workflow for Sales Quotations next to Workflow.Choose Add.Note If the workflow has already been defined, please skip below steps. | The New Workflow screen displays. |  |
| 4 | Maintain General Data | Make the following entries.In the Header tab:Name: <Second Approver- Net Value over 1000 AED> |  |  |
| 5 | Set Preconditions | Under Preconditions tab, chooseNet Amount is greater than, then enter below data:Currency: AEDAmount: 1000Choose Save. | Preconditions are set. |  |
| 6 | Add Steps | From the Steps section, choose Add. | The New Step screen displays. |  |
| 7 | Create First Workflow | Select the following entries from dropdown lists:Under the Header tab:Type: Release of Sales QuotationUnder the Recipients tab:Assignment By: RoleRole: Sales Document Approver - Level 2Under the Exception Handling tab:Name: Rework Sales QuotationRequired Action: Rework of Sales QuotationAction Result: Restart WorkflowChoose Add to append this step to the workflow and choose Save. | The first workflow is created. |  |
| 8 | Add the Second Workflow | Choose Back to the Manage Workflows screen.Choose Add. | The New Workflow screen displays. |  |
| 9 | Maintain General Data | Make the following entries.Under the Header tab:Name: <First Approval- No Conditions> |  |  |
| 10 | Add Steps | From the Steps section, choose Add. | The New Step screen displays. |  |
| 11 | Create Second Workflow | Select the following entries from dropdown lists:Under the Header tab:Type: Release of Sales QuotationUnder the Recipients tab:Assignment By: RoleRole: Sales Document Approver - Level 1Under the Exception Handling tab:Name: Rework Sales QuotationRequired Action: Rework of Sales QuotationAction Result: Restart WorkflowChoose Add to append this step to the workflow and choose Save. | The second workflow is created. |  |
| 12 | Activate Workflows | Choose Back to the Manage Workflow screen.Choose Define Order. Adjust the order as below:Second Approver- Net Value over 1000 AED: Order 1First Approver-No Conditions: Order 2Choose Activate to active the workflows. | Workflows are activated. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

#### Manage Situation Types (Optional)

Purpose

In this procedure, you configure the situation type by using template.

Procedure

|  |
| --- |
| Note Please make sure scope item 31N - Situation Handling is activated if you want to execute this step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947). | The Manage Situation Types screen displays. |  |
| 3 | Select the template to copy | Search for SD_EXPIRING_QUOTATION and Choose Go.Select the the latest version SD_EXPIRING_QUOTATION, then choose Copy. | The Situation Type screen displays. |  |
| 4 | Maintain the situation | Make the following entries and choose Save:ID: Z_EXP_QuotationName: Quotation SituationIn the Conditions tab, make the attribute value to configure the conditions to use this functionIn the Batch Job Scheduling tab:Time Zone: CETStart Batch Job At: 14:00In the Situation Display tab:Resend Notification: CheckIn the Notification Recipients tab:Choose Add Team Category, and in the pop up window, choose SALES and choose SelectMaintain Member Function from drop-down window if necessary;Choose Create. | Then situation type is maintained. |  |
| 5 | Enable this situation type | In the pop up window, Choose Yes to enable the situation type. | The situation type is enabled. |  |

## Overview Table

The test script Sales Quotation consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | APP/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Quotation](#unique_13) [page ] 18 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |
| [Process Sales Quotation Approval (Optional)](#unique_14) [page ] 20 |  |  |  |
| [Withdraw from Approval](#unique_15) [page ] 21 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |
| [Approve/Reject/Rework Quotation](#unique_16) [page ] 22 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Rework Sales Quotation](#unique_17) [page ] 23 |  |  |  |
| [Change Quotation (Optional)](#unique_18) [page ] 23 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |
| [Set Quotation as Rework not Required](#unique_19) [page ] 24 | Internal Sales Representative | My Inbox - All Items (F0862) |  |
| [Release the Reworked Quotation](#unique_20) [page ] 25 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Change Quotation](#unique_21) [page ] 26 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |
| [Reject Sales Quotation](#unique_22) [page ] 27 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |

## Test Procedures

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as: Apps, factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data or find related objects.

How to access and check a factsheet:

- Log onto the SAP Fiori Launchpad using the respective user e.g Internal Sales Representative.
- Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your Search Criteria and choose the business object type, e.g.: Sales orders from drop-down menu in 1st field, enter sales order number in 2nd field and choose Search, The sales order is listed.
- Choose the sales order number link, the system navigates to factsheet screen and sales order related information is integrated and summarized in one Fiori page. You can get detailed data via choosing the corresponding links.

There are factsheets available for the following objects: (Visible depending on the assigned role)

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo

### Create Sales Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) screen displays. |  |
| 3 | Navigate to Create Sales Quotation Screen | On the Manage Sales Quotations (F1852) screen, choose Create Quotation. |  |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Enter:Quotation Type <Quotation Type> For example, QT (Quotation)Note If desired, you can enter the organizational data. |  |  |
| 5 | Enter Quotation Details | Make the following entries, and choose Enter.Sold-to Party: <Sold-to Party> For example, 33100001Ship-to Party: <Ship-to Party> For example, 33100001Valid to: <Enter a Date> For example, one year after todayMaterial : <Material Number, or, Substituted Material> For example, TG11 or C01_MDOrder Quantity: <Quantity, for example, 5>If you would like to use Sales order approval workflow, please maintain the following:Order Reason: newspaper advertisementNote If you would like to offer free-of-charge material to customer, maintain the item category as below:• Item category: CBQX (for material TG11)• Item category: CBQ3 (for material TG10)• Item category: CBQ4 (for material TG13) |  |  |
| 6 | Save | Choose Save . | The quotation is created. |  |
| 7 | Check Quotation Status | Choose Display.At the menu bar on the top of the screen, choose More > Goto > Header > Status .In the Processing Status section, check if the Approval Status field exists. If yes, it means quotation workflow is triggered. Then go to [Process Sales Quotation Approval (Optional)](#unique_14) [page ] 20 chapter. If the Approval Status field doesn't exist, then go to [Change Quotation](#unique_21) [page ] 26 chapter. | The Display Quotation XXXXX: Overview screen displays.The Display Quotation XXXXX: Header Data screen displays. |  |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) screen displays. |  |
| 3 | Search For Sales Quotation | Enter search term(s) in filter bar and choose Go.For example: enter sales quotation number in field Sales Quotation. | Sales quotation is displayed in result list. |  |
| 4 | Navigate to Sales Quotation Screen | Click sales quotation number and choose Display quotation. | The Display Quotation xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Quotation xxx: Overview Screen, choose from menu Header Output Preview. |  |  |
| 6 | Display Print Preview | On the Display Quotation xxx: Output Screen, select the line already created for the print output and choose Display Document . | Preview for PDF document displays. |  |

### Process Sales Quotation Approval (Optional)

|  |
| --- |
| Note Only relevant if below conditions are fulfilled:Approval reason(s) is defined and assigned, details refer to the Define and Assign Approval Reasons chapter.The Cloud BAdI that returns an approval reasons is implemented, details refer to the Implement Cloud BADI chapter.Total amount of the quotation is not less than 100 AED.Order reason is 005. |

#### Withdraw from Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to withdraw quotation approval.

Prerequisites

Sales manager doesn’t make approval decision yet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) screen displays. |  |
| 3 | Search for Sales Quotation | Enter search terms in filter bar, and choose Go.For example: enter sales quotation number in the Sales Quotation field. | Sales quotation displays in result list. |  |
| 4 | Navigate to Sales Quotation Screen | Choose the arrow at the end of quotation row. | The Display Quotation xxx: Overviewscreen displays. |  |
| 5 | Withdraw Approval Request | In the menu bar at the top, choose More > Edit > Additional Functions > Withdraw Approval Request .Choose Continue to confirm the information shown as The approval request for sales document XXXXXXX was withdrawn. | The approval request is withdrawn. |  |
| 6 | Change Quotation | On the Change Quotation: Overview screen, make some changes, for example:Valid to: <Enter a Date> | Approval status is changed to In Approval. |  |

#### Approve/Reject/Rework Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release, reject, or request rework.

Prerequisites

Approval status of the quotation is In Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox - All Items (F0862).Note You can also choose Notifications icon on the top-right corner to navigate to My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve/Reject/Rework Quotation | You receive the notification of the quotation. Choose one from the options on the bottom bar.Option 1: ReleaseOption 2: RejectOption 3: Request Rework | The Submit Decision dialog box displays. |  |
| 5 | Submit | Enter some comments and choose Submit. | Based on above decisions, choose next steps accordingly:• Release: the whole process ends, no subsequent step is needed.• Reject: the whole process ends, no subsequent step is needed.• Request Rework: go to Rework Quotation chapter. |  |

#### Rework Sales Quotation

|  |
| --- |
| Note Only relevant if the workflow is set as Request Rework by sales manager previously. After sales manager requests rework, sales representative either changes quotation or directly sets "rework not required" without any quotation change. Choose one from the following activities Change Quotation and Set Quotation as Rework not Required alternatively. |

##### Change Quotation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change the quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) screen displays. |  |
| 3 | Search for Sales Quotation | Enter search terms in filter bar, and choose Go.For example: enter sales quotation number in Sales Quotation field. | Sales quotation is displayed in result list. |  |
| 4 | Navigate to Sales Quotation Screen | Choose sales quotation number and choose Change quotation. | The Change Quotation xxx: Overview screen displays. |  |
| 5 | Change Quotation | Make the following entries and choose Enter:Order Quantity <Quantity>, for example, 10 |  |  |
| 6 | Save | Save your entries. | The quantity is changed in the quotation document. |  |

##### Set Quotation as Rework not Required

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Sales representative can set rework not required if no change for quotation is needed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | You receive a notification in the notification section.Open My Inbox - All Items (F0862) app to proceed to the notification or choose the notification in the notification section. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Done | Check the inbox items, and choose Rework not Required. | Set item to rework not required. |  |

##### Release the Reworked Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the reworked quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | You receive a notification in the notification sectionOpen My Inbox - All Items (F0862) app to proceed to the notification or choose the notification in the notification section. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve Quotation | You receive the notification of the reworked quotation. Choose Release and input the comment if necessary. Choose Submit. | The reworked quotation is released. |  |

### Change Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to change sales quotation to meet customer's requirements, such as changing quotation quantity.

|  |
| --- |
| Note After you have completed this activity:Option A: If the customer rejects the sales quotation, go to [Reject Sales Quotation](#unique_22) [page ] 27 step.Option B: If the customer accepts the sales quotation, go to Appendix step. |

Prerequisites

Only relevant when quotations do not need to be approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) screen displays. |  |
| 3 | Search for Sales Quotation | Enter search terms in filter bar, and choose Go.For example: enter sales quotation number in Sales Quotation field. | Sales quotation is displayed in result list. |  |
| 4 | Navigate to Sales Quotation Screen | Choose sales quotation number and choose Change quotation. | The Change Quotation xxx: Overview screen displays. |  |
| 5 | Change Quotation | Make the following entries and choose Enter:Order Quantity <Quantity>, for example, <10> |  |  |
| 6 | Save | Save your entries. | The quantity is changed in the quotation document. |  |

### Reject Sales Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to enter reasons for customer rejections of a sales quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) screen displays. |  |
| 3 | Search for Sales Quotation | Enter search term(s) in filter bar and choose Go.For example: enter sales quotation number in Sales Quotation field. | Sales quotation is displayed in result list. |  |
| 4 | Reject All Items | Select your quotation entry and choose Reject All Items. | The Reject All Items dialog box displays. |  |
| 5 | Choose Rejection Reason | Choose an appropriate reason in the dropdown menu and choose OK. | Quotation is rejected. |  |

|  |
| --- |
| Note In the Quotation Conversion Rates app, you may monitor the proportion of quotations, which have been converted into sales orders.You may select from dropdown list in the top-left corner, such as, customer or sales organization, to display a percentage graph, that which shows you how many quotations have been converted into sales orders. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Sell from Stock (BD9) (optional) | Process sequence for a standard sales process (sell from stock) with a customer.Using the master data from this document, complete relevant activities described in the test script Sell from Stock (BD9).When creating the Sales Order, create it with reference using the sales quotation number. |
| Situation Handling (31N) (optional) | Complete the activities described in test script Situation Handling (31N) to trigger a situation when an open quotation will expire. The situation shall be notified to the responsible employee (defined within responsibility management).Possible dimension for Situation Handling:Order Net ValueSales OrganizationSold-to PartyOverall StatusQuotation valid dateConversion RateDays Before Expiry |

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
- see-also :: [[08-sales-order-management/sales-inquiry-1iq-ae-test-script-726]]
- see-also :: [[08-sales-order-management/test-script-sales-order-processing-with-customer-down-payment-bkj-ae-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 44,809 chars in the whole document
