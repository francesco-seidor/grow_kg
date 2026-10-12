---
id: 03-financial-accounting-and-close/test-script-purchase-order-accruals-2vb-ae-sap-s-4hana-cloud-public-ed
title: "Test Script: Purchase Order Accruals (2VB_AE) - SAP S/4HANA Cloud Public Edition (2VB_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2VB: purchase order accruals and simulation, with prerequisites, roles, apps, steps."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/service-entry-sheet-accruals]
aliases: [2VB_S4CLD2608_BPD_EN_AE]
keywords: [Service Entry Sheet Based Accruals, purchase order accruals, accrual engine, periodic accruals, accrual review, accrual posting simulation, threshold variants, accrual workflows, accrual monitoring reports, purchase order deferrals]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VB_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-878
topic: 03-financial-accounting-and-close/service-entry-sheet-accruals
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Purchase Order Accruals (2VB_AE) - SAP S/4HANA Cloud Public Edition (2VB_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VB_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Service Entry Sheet Based Accruals** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Purchase Order Accruals (2VB_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850757)

[2 Prerequisites 4](#_Toc232850758)

[2.1 System Access 4](#_Toc232850759)

[2.2 Roles 4](#_Toc232850760)

[2.3 Master Data and Organizational Data 5](#_Toc232850761)

[2.4 Preliminary Steps 6](#_Toc232850762)

[2.4.1 Define Accrual Item Types and Methods for MM Purchase Order Items (Optional) 6](#_Toc232850763)

[2.4.2 Create Purchase Order 8](#_Toc232850764)

[2.4.3 Approve Purchase Order 10](#_Toc232850765)

[3 Overview Table 11](#_Toc232850766)

[4 Test Procedures 13](#_Toc232850767)

[4.1 Purchase Order Accruals 13](#_Toc232850768)

[4.1.1 Manage Workflows for Purchase Order Accruals Review 13](#_Toc232850769)

[4.1.2 Transfer Purchase Orders (Optional) 14](#_Toc232850770)

[4.1.3 Propose Periodic Accruals 15](#_Toc232850771)

[4.1.4 My Inbox - Review Purchase Order Accruals 16](#_Toc232850772)

[4.1.5 Review Purchase Order Accruals for Cost Accountant 17](#_Toc232850773)

[4.1.6 Post Periodic Accruals 19](#_Toc232850774)

[4.1.7 Analyze Accrual Postings 20](#_Toc232850775)

[4.1.8 Display Purchase Order Accruals 21](#_Toc232850776)

[4.1.9 Display Accrual Object Items 22](#_Toc232850777)

[4.1.10 Display Periodic Accrual Amounts 23](#_Toc232850778)

[4.2 Simulate Purchase Order Accruals 24](#_Toc232850779)

[4.2.1 Simulate Posting Run 24](#_Toc232850780)

[4.2.2 Display Simulated Accrual Postings 25](#_Toc232850781)

[4.2.3 Compare Simulated and Actual Accrual Postings 26](#_Toc232850782)

[5 Appendix 28](#_Toc232850783)

[5.1 Define Threshold Variants 28](#_Toc232850784)

## Purpose

Overview

Accruals must be posted when liabilities are incurred by a third party and related costs are not yet posted. This solution supports the typical period-end closing activity – accruals postings with the reference to purchase orders. You can also choose to activate the deferrals solution in Purchase Order Accruals to let accruals and deferrals for a purchase order seamlessly work together with automation.

Based on the SAP S/4HANA Cloud Public Edition accrual engine, this solution offers flexible configuration options for calculating and posting the purchase order accruals. It also provides the option to review the monthly accrual amounts and supports monitoring and the approval of accruals.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2VB_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |

### Master Data and Organizational Data

Default Values

The organizational structure and master data of your company was created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Accounts | YCOA |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |

### Preliminary Steps

#### Define Accrual Item Types and Methods for MM Purchase Order Items (Optional)

Purpose

In this activity, you assign company codes to purchase order transfer variants. You can enable the creation of purchase order deferrals in addition to purchase order accruals by assigning Purchase Order Transfer Variant SDFR to your company code.

|  |
| --- |
| Note Purchase Order Transfer Variant SDEF is assigned as the Default Variant for PO Data Transfer. You can make a transfer variant the standard variant for all company codes by setting the Dflt Var PO Transfer indicator in the Variants for purchase order data transfer view. If there are no other assignments for a company code, the system always uses this default variant. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Open | Open Purchase Order Accruals. |  |  |
| 6 | Select Configuration Step | For the Define Accrual Item Types and Methods for MM Purchase Order Items step, choose Configure. | The Change View "Variants for purchase order data transfer": Overview screen displays. |  |
| 7 | Access Configuration | Double-click Assign company code to transfer variant to access the view. | The Change View "Assign company code to transfer variant": Overview screen displays. |  |
| 8 | Assign Company Code To Transfer Variant | Choose New Entries.Make the following entries and choose Save:Company Code: 3310PO Transfer Variant: SDFR | The company code is assigned to transfer variant SDFR. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Accrual Item Types and Methods for MM Purchase Order Items.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Accrual Item Types and Methods for MM Purchase Order Items screen is displayed. |  |
| 3 | Access Configuration | Double-click Assign company code to transfer variant. | The Change View "Assign company code to transfer variant": Overview screen displays. |  |
| 4 | Assign Company Code To Transfer Variant | Choose New Entries.Make the following entries and choose Save:Company Code: 3310PO Transfer Variant: SDFR | The company code is assigned to transfer variant SDFR. |  |

#### Create Purchase Order

Purpose

In this activity, you create a purchase order item with an account assignment.

|  |
| --- |
| Note By default, accruals are only created for purchase orders that have Document TypeNB and Item Category<empty>. The purchase order must represent the purchase of a consumable product, i.e., the purchase order must have an account assignment. |

|  |
| --- |
| Note Purchase orders with the following conditions can be transferred to the Accrual Engine for deferrals calculation:Purchase ScenarioItem CategoryProduct Type GroupLean Service<empty>2Enhanced LimitE2Consumable Product<empty>1 |

|  |
| --- |
| Note The accrual object corresponding to a purchase order is generated when the purchase order is released. In S/4HANA Cloud, a purchase order is created with the status "In Release". So long as the purchase order has this status, it will not be considered by the accrual engine. There is an automatic flexible workflow which releases the purchase order. Normally, the workflow is executed within a few seconds after the purchase order is saved. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Enter Supplier | Make the following entry:Supplier: 33300001 |  |  |
| 4 | Expand Header | Choose Expand Header. |  |  |
| 5 | Enter Organizational Data | Navigate to the Org. Data tab and make the following entries:Purchasing Organization: 3310Purchasing Group: 001Company Code: 3310 |  |  |
| 6 | Enter Item Data | In the Item Overview, make the following entries:Acct Ass. Cat.: K (Cost center)Material: TG0011PO Quantity: for example, 10Order Unit: PCDelivery Date: <current date>Net Price: for example, 100Currency: AEDPlant: 3310 |  |  |
| 7 | Enter Account Assignment for Item | Select the item and choose Choose PO Item.Navigate to Account Assignment and make the following entries:G/L Account: 51600000Cost Center: 33101101 |  |  |
| 8 | Save | Choose Save. | The purchase order is created. Note down the purchase order number. |  |

#### Approve Purchase Order

Purpose

In this procedure, you release a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the SAP Fiori launchpad as Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox - All Items (F0862) . | A list of created purchase orders displays. |  |
| 3 | Search for Purchase Order | Enter the purchase order number in the search area, then choose Search. |  |  |
| 4 | Release Purchase Order | Select the purchase order and choose Approve. | The Submit Decision screen displays. |  |
| 5 | Approve the Purchase Order | Choose Submit. | The purchase order is approved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Purchase Order Accruals

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Workflows for Purchase Order Accruals Review](#unique_10) [page ] 13 | General Ledger Accountant | Manage Workflows for Purchase Order Accruals Review (F3625) | The workflow for purchase order accruals is created and activated. |
| [Transfer Purchase Orders (Optional)](#unique_11) [page ] 14 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job is executed and the purchase orders are transferred to the accrual engine. |
| [Propose Periodic Accruals](#unique_12) [page ] 15 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job is executed and the purchase order accruals are scheduled. |
| [My Inbox - Review Purchase Order Accruals](#unique_13) [page ] 16 | Purchaser | My Inbox - All Items (F0862) | The purchase order is reviewed and the status is set accordingly. |
| [Review Purchase Order Accruals for Cost Accountant](#unique_14) [page ] 17 | Cost Accountant - Overhead | Review Purchase Order Accruals - For Cost Accountant (F3552) | The purchase order is reviewed and the status is set accordingly. |
| [Post Periodic Accruals](#unique_15) [page ] 19 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job is executed and the accrued purchase orders are posted. |
| [Analyze Accrual Postings](#unique_16) [page ] 20 | General Ledger Accountant | Analyze Accrual Postings (F3732) | A customizable overview of accrual postings displays key information for monitoring purchase order accruals. |
| [Display Purchase Order Accruals](#unique_17) [page ] 21 | General Ledger Accountant | Display Purchase Order Accruals (F3928) | The details of individual purchase orders and line items are displayed, e.g., their lifecycle, review history, and account assignment. |
| [Display Accrual Object Items](#unique_18) [page ] 22 | General Ledger Accountant | Display Accrual Object Items (F4899) | The accrual objects items for the specified selection criteria are displayed. |
| [Display Periodic Accrual Amounts](#unique_19) [page ] 23 | General Ledger Accountant | Display Periodic Accrual Amounts (F4900) | The periodic accrual amounts for a specified fiscal year period are displayed. |

Table 3: Simulate Purchase Order Accruals

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Simulate Posting Run](#unique_20) [page ] 24 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job is executed and the postings are simulated. |
| [Display Simulated Accrual Postings](#unique_21) [page ] 25 | General Ledger Accountant | Accrual Postings - With Simulation (W0183) | The simulated postings of purchase order accrual objects are displayed. |
| [Compare Simulated and Actual Accrual Postings](#unique_22) [page ] 26 | General Ledger Accountant | Accrual Postings - Simulated / Posted (W0184) | A comparison of simulated and actual postings of purchase order accrual objects is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Purchase Order Accruals

#### Manage Workflows for Purchase Order Accruals Review

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you determine the workflow for purchase order accruals review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Workflows for Purchase Order Accruals Review (F3625). | The Manage Workflows screen displays. |  |
| 3 | Create New Workflow | Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter Data | Make the following entries:Header section:Workflow Name: for example, Workflow for PO AccrualsStart Conditions section:Company Code: 3310 |  |  |
| 5 | Create New Step | In the Steps section, choose Create | The New Step screen displays |  |
| 6 | Create New Step | Make the following entries and choose Create:Header section:Step Type: Review Purchase Order AccrualRecipients section:Assignment By: for example, RoleRole: for example, Determined automatically |  |  |
| 7 | Save Workflow | Choose Save. | The workflow is saved. |  |
| 8 | Activate Workflow | Select the workflow and choose Activate. | The workflow is activated. |  |

#### Transfer Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you transfer purchase orders to the accrual engine.

|  |
| --- |
| Note This activity must only be performed if the system already contains purchase orders prior to the activation of this scope item. This action must only be performed once. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accruals Jobs (F3778). | The Application Jobs screen displays. |  |
| 3 | Create a new job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter data | Make the following entries and choose Schedule:Template Selection section:Job Template: Purchase Order Accruals - Transfer Purchase Orders to Accrual EngineJob Name: Purchase Order Accruals - Transfer Purchase Orders to Accrual EngineChoose Step 2.Scheduling Options section:Start immediately: SelectedChoose Step 3.Parameters:Company Code: 3310Purchasing Document: <optional>Item: <optional> | The job is created and started immediately. |  |

#### Propose Periodic Accruals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule purchase order accruals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accruals Jobs (F3778). | The Application Jobs screen displays. |  |
| 3 | Create a new job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter data | Make the following entries and choose Schedule:Template Selection section:Job Template: Purchase Order Accruals - Propose Periodic AccrualsJob Name: Purchase Order Accruals - Propose Periodic AccrualsChoose Step 2.Scheduling Options section:Start immediately: SelectedChoose Step 3.Parameters:Last Day of Period: <date>Company Code: 3310Ledger Group: <optional>Accrual Object: <optional>Accrual Subobject: <optional>Accrual Item Type: <optional> | The job is created and started immediately. |  |

#### My Inbox - Review Purchase Order Accruals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the accrued purchase orders.

|  |
| --- |
| Note Only items with the review type E (Explicit review required) will appear in My Inbox for manual review. |

|  |
| --- |
| Note For accrual item type SCSTPLN, review of periodic accrual amounts must be active. Navigate to configuration activity Define Accrual Item Types and ensure that the column Review Act is selected. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Change the Purchase Order | On the left side of the screen, select the purchase order item for review and make the following changes:Revised Planned Costs: for example, 10000Adjustment Reason: for example, Proposed accrual amount was too high (S1) | Note The accrual value can also be changed by changing the Percentage of Completion, which directly changes the Revised Planned Costs. |  |
| 4 | Save | Choose Confirm. | The new purchase order item accrual value is saved. |  |

#### Review Purchase Order Accruals for Cost Accountant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To follow a four-eyes principle, managers in accounting need an overview of all critical tasks and milestones during financial close. These should allow for steps to be taken to ensure quality and timeliness, and to be reviewed and approved. Each task and milestone subject to approval must be shown with all result objects and all relevant attributes. This ensures that overall period closing or year-end closing is done in time, ready for legal reporting, and with completeness and correctness of books.

|  |
| --- |
| Note There are three different review types for accruals items:A (Automatically reviewed: Amount is below upper threshold)B (No review required: Amount is below lower threshold)E (Explicit review required)Only items with the review type E (Explicit review required) must be manually reviewed. |

|  |
| --- |
| Note If the creation of purchase order deferrals is enabled, deferrals are displayed but cannot be reviewed. |

|  |
| --- |
| Note For accrual item type SCSTPLN, review of periodic accrual amounts must be active. Navigate to configuration activity Define Accrual Item Types and ensure that the column Review Act is selected. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access App | Open Review Purchase Order Accruals - For Cost Accountant (F3552). |  |  |
| 3 | Display the Purchase Order List | Make the following entries and choose Go:Fiscal Year Period: for example, <PPP.YYYY>Company Code: 3310Review Type: E (Explicit review required) | The purchase order list for review is displayed.Note The purchase orders are displayed in a tabular view:All: displays reviewed and unreviewed purchase ordersUnreviewed: displays the purchase orders that are not reviewedReview Finished: displays the reviewed purchase orders |  |
| 4 | Unreviewed Purchase Orders | Choose the Unreviewed tab. |  |  |
| 5 | Review Purchase Orders | Select a purchase order and choose Edit. | The Edit Accruals Items screen displays. |  |
| 6 | Edit Purchase Order Accrual Value Manually | Change the following entries and choose Confirm and Save:Revised PoC: for example, 90%Adjustment Reason: for example, S1 (Proposed accrual amount was too high) | Note The accruals values can also be changed by changing the Revised Costs (TC), which directly changes the Revised PoC.The purchase order is saved with the new accruals values. |  |
| 7 | Confirm Review | Select a purchase order and choose Confirm Review. | The purchase order is reviewed and displays on the Review Finished tab. |  |

#### Post Periodic Accruals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the accrued purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accruals Jobs (F3778). | The Application Jobs screen displays. |  |
| 3 | Create a new job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter data | Make the following entries and choose Schedule:Template Selection section:Job Template: Purchase Order Accruals - Post Periodic AccrualsJob Name: Purchase Order Accruals - Post Periodic AccrualsChoose Step 2.Scheduling Options section:Start immediately: SelectedChoose Step 3.Parameters:Last Day of Period: <date>Company Code: 3310Ledger Group: <optional>Accrual Object: <optional>Accrual Subobject: <optional>Accrual Item Type: <optional>Note You can select Rev. on First Day of Next Perd if you want the reversal of periodic accrual posting to take place on the first day of the next period. If you leave this check box empty, the system posts the accrual reversal on the last day of the next period. | The job is created and started immediately. |  |

#### Analyze Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app enables access to key information for monitoring purchase order accruals. A range of filters provides a customizable overview of accrual postings.

|  |
| --- |
| Note The Line Item Type filter is set to display Offsetting Line Items by default. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Analyze Accrual Postings (F3732). | The Analyze Accrual Postings screen displays. |  |
| 3 | Maintain Selection | Using the Compact Filter, enter the following in the filter bar and choose Go:Display Currency: EURLedger: 0LCompany Code: 3310Fiscal Period: for example, <current period>Fiscal Year: for example, <current year>Line Item Type: Offsetting Line Items |  |  |

#### Display Purchase Order Accruals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app enables a comprehensive overview of purchase order accruals and deferrals. You can view details of individual purchase orders and line items, e.g., their lifecycle, review history, account assignment, and postings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Purchase Order Accruals (F3928). | The Display Purchase Order Accruals screen displays. |  |
| 3 | Maintain Selection | Enter the following in the filter bar and choose Go:Company Code: 3310Lifecycle Status: P (In Process)Cost Center: <optional> |  |  |
| 4 | Display Purchase Order Item | Select a purchase order item of a purchasing document from the list and choose Details. | The details of <purchasing document> - <item> - <account assignment number> display.Note You can view the account assignment of the purchase order item under Account Assignments. |  |
| 5 | Display Item Data | Under Item Data, choose Details of the accrual item listed. | The Accruals Overview, Review History, and Postings for the item display. |  |

#### Display Accrual Object Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this master data list, you can view the details of individual accrual objects, e.g., their lifecycle, accrual item type, and total accrual amount (TC).

|  |
| --- |
| Note You must first run the Simulate Accrual Postings job to display the correct value for the following amounts:Accumulated A/D Amt (TC) (Accumulated Accrual/Deferral Amount)Period A/D Amt (TC) (Period Accrual/Deferral Amount)Remaining A/D Amt (TC) (Remaining Accrual/Deferral Amount) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Accrual Object Items (F4899). | The Display Accrual Object Items screen displays. |  |
| 3 | Maintain Selection | Enter the following in the filter bar and choose Go:Key Date: for example, <today's date>Component: POAC (Purchase Order Accruals)Company Code: 3310Lifecycle Status: P | The accrual objects items for the specified selection criteria are displayed. |  |

#### Display Periodic Accrual Amounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this report, you can view periodic accrual amounts for a specified fiscal year period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Periodic Accrual Amounts (F4900). | The Display Periodic Accrual Amounts screen displays. |  |
| 3 | Maintain Selection | Enter the following in the filter bar and choose Go:Fiscal Year Period: for example, <current period>Company Code: 3310 | The periodic accrual amounts display for the specified period. |  |

### Simulate Purchase Order Accruals

#### Simulate Posting Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you simulate the posting of purchase order accrual objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accruals Jobs (F3778). | The Application Jobs screen displays. |  |
| 3 | Create a New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Data | Make the following entries and choose Schedule:Template Selection section:Job Template: Purchase Order Accruals - Simulate Accrual PostingsJob Name: Purchase Order Accruals - Simulate Accrual PostingsChoose Step 2.Scheduling Options section:Start Immediately: SelectedChoose Step 3.Parameters:Company Code: 3310Accrual Object: <accrual object> | The job is created and started immediately. |  |

#### Display Simulated Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view simulated postings of purchase order accrual objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Accrual Postings - With Simulation (W0183). | The Accrual Postings With Simulation - Query screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Valid to Date: for example, <last day of lifecycle>Company Code: 3310Fiscal Year: for example, <current year>Fiscal Period: for example, <current period>Component: for example, POACAccrual Object: <accrual object> | The reports displays the data specified by your query.Note Once accruals are posted for an accrual object, only the actual posted accrual amount will be displayed. |  |

#### Compare Simulated and Actual Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view and compare simulated postings with actual postings of purchase order accrual objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Accrual Postings - Simulated / Posted (W0184). | The Simulated Posted Compare - Query screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Valid to Date: for example, <last day of lifecycle>Company Code: 3310Fiscal Year: for example, <current year>Fiscal Period: for example, <current period>Component: for example, POACAccrual Object: <accrual object> | The reports displays the data specified by your query for comparison. |  |

## Appendix

### Define Threshold Variants

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you set the threshold amounts for periodic accrual amounts. Any items below the Lower Threshold Amount do not require review. Any items above the Upper Threshold Amount must be reviewed manually. All items that fall between the two thresholds are automatically reviewed.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Open | Open Purchase Order Accruals. |  |  |
| 6 | Select Configuration Step | For the Define Threshold Variants step, choose Configure. | The Change View "Threshold Variants for Revw/Approval of Periodic Accr. Amnts" screen displays. |  |
| 7 | Configure Threshold Variants | Make the following entries and choose Save:Lower Threshold Amount: <amount>Upper Threshold Amount: <amount> | New threshold amounts have been saved for a Threshold Variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Threshold Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Threshold Variants screen is displayed. |  |
| 3 | Configure Threshold Variants | Make the following entries and choose Save:Lower Threshold Amount: <amount>Upper Threshold Amount: <amount> | New threshold amounts have been saved for a Threshold Variant. |  |

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
- related-to :: [[03-financial-accounting-and-close/service-entry-sheet-based-accruals-63l-ae-1143]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VB_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 44,679 chars in the whole document
