---
id: 03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-earmarked-funds-78s-1205
title: Test Script SAP S/4HANA Cloud Public Edition - Earmarked Funds (78S) (78S_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 78S Earmarked Funds in SAP S/4HANA Cloud Public Edition: reservation, precommitment, commitment, supplier invoice, workflow approval."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/earmarked-funds]
aliases: [78S_S4CLD2608_BPD_EN_XX]
keywords: [Earmarked Funds, funds reservation, funds precommitment, funds commitment, vendor invoice, workflow approval, document type configuration, scope item testing, budget consumption, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/78S_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1205
topic: 03-financial-accounting-and-close/earmarked-funds
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Earmarked Funds (78S) (78S_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/78S_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Earmarked Funds** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Earmarked Funds (78S) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232827535)

[2 Prerequisites 3](#_Toc232827536)

[2.1 System Access 3](#_Toc232827537)

[2.2 Roles 3](#_Toc232827538)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232827539)

[2.4 Additional Manual Configuration 5](#_Toc232827540)

[2.5 Business Conditions 5](#_Toc232827541)

[2.6 Update Cost Center with Public Sector Management Account Assignments (for PSM only) 6](#_Toc232827542)

[3 Overview Table 7](#_Toc232827543)

[4 Test Procedures 8](#_Toc232827544)

[4.1 Create Funds Reservation 8](#_Toc232827545)

[4.2 Create Funds Precommitment 10](#_Toc232827546)

[4.3 Create Funds Commitment 12](#_Toc232827547)

[4.4 Vendor Invoice with Reference to a Funds Commitment 14](#_Toc232827548)

[4.5 Approving an Earmarked Fund 16](#_Toc232827549)

[4.5.1 Create an EF Document Type for Workflow Approval 16](#_Toc232827550)

[4.5.2 Define the Workflow 18](#_Toc232827551)

[4.5.3 Create a Reservation Subject to Approval and Approve a Reservation 20](#_Toc232827552)

## Purpose

Overview

Earmarked funds are business transactions that claim already allocated budget for expected expenditures. The following business transactions are grouped together under the term Earmarked Funds:

- Funds reservations
- Funds precommitments
- Funds commitments

This document contains a description of the following procedures:

- How to create transactional data as commitments for your SAP S/4HANA Cloud Public Edition system.
- How to display an earmarked funds document.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

The test should be conducted in the following system:

| System | Details |
| --- | --- |
| System | Accessible from the SAP Fiori launchpad. Your system administrator provides you with the URL required to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, see How to Create a Business Role for a Key User in the [product assistance](https://help.sap.com/viewer/a630d57fc5004c6383e7a81efee7a8bb/latest/en-US/8fa28e0107984d42a99b9eea67856cea.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Budget Specialist - Funds Management | SAP_BR_BUDGET_SPECIALIST | Budgeting | SAP_BR_BUDGET_SPECIALIST |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data for your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, according to the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Fund | <fund, for example, G1100> | Mandatory | Derived automatically |
| Functional Area | <functional area, for example, 1000> | Mandatory |  |
| Budget Period | <current year> | Mandatory |  |
| Cost Center | cost center, for example, 17101101> | Mandatory | Replace with the cost center in your company code, such as xxxx1202 and xxxx1801 |
| Account Number | 61100000 | Mandatory |  |
| Budget Account |  | Mandatory | Entered in the account number field. |
| Grant | NRG | NRG | Delivered |
| WBS Element |  | Optional |  |
| Profit Center |  | Optional | Derived automatically |
| Segment |  | Optional | Derived automatically |
| Company Code | <company code, for example, 1710> |  | Replace 1710 with your company code xxxx. See also the cost center section above. |

You can find general information about creating master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |
| 47C | Create Fund - MDS |
| 47D | Create Budget Period - MDS |
| 47E | Create Functional Area - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| 7CB | Update Cost Center with Public Sector Management Account Assignments |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/6d535b74c4cf2eb762b3ec35dadb5368)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 6YU – Government Budget Management | The steps executed by the budget specialist to consume budget. |

### Update Cost Center with Public Sector Management Account Assignments (for PSM only)

Purpose

As a prerequisite for public sector implementations, you are required to maintain additional data for the cost center master records used to post the transactions in this script.

Procedure

Follow the steps as described in the master data scope item 7CB - Update Cost Center with Public Sector Management Account Assignments .

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Funds Reservation](#unique_10) [page ] 8 | Budget Specialist - Funds Management | Manage Earmarked Funds (F4657) | Funds reservation is created |
| [Create Funds Precommitment](#unique_11) [page ] 10 | Budget Specialist - Funds Management | Manage Earmarked Funds (F4657) | Funds precommitment is created |
| [Create Funds Commitment](#unique_12) [page ] 12 | Budget Specialist - Funds Management | Manage Earmarked Funds (F4657) | Funds commitment is created |
| [Vendor Invoice with Reference to a Funds Commitment](#unique_13) [page ] 14 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | A supplier invoice is created. |
| [Create an EF Document Type for Workflow Approval](#unique_14) [page ] 16 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | EF document type for workflow approval is created. |
| [Define the Workflow](#unique_15) [page ] 18 | Configuration Expert - Business Process Configuration | Manage Workflows for Earmarked Funds (F6951) | Workflow is defined. |
| [Create a Reservation Subject to Approval and Approve a Reservation](#unique_16) [page ] 20 | Budget Specialist - Funds Management | Manage Earmarked Funds (F4657) | Reservation subject to approval is created. |

## Test Procedures

This section describes the procedures that apply to each process step associated with this scope item. You can also use these procedures to test the creation of master data.

### Create Funds Reservation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Budget Specialist - Funds Management | The SAP Fiori launchpad appears. |  |
| 2 | Check Available Budget | Run the Budget AVC Overview - Overall Available Budget (F2163) Fiori appSelect the master data below and make a note of the following figures; Consumable amount, consumed amount and available amount | The budget report appears. |  |
| 3 | Open Manage Earmarked Funds . | Frontend Fiori App:Open Manage Earmarked Funds (F4657). | The Manage Earmarked Funds Documents (F4657) screen appears. |  |
| 4 | Enter General Data | On the Earmarked Funds screen select Create Funds Reservation.Enter the General Data on the dialog box:Document Type: ReservationCompany Code: <company code, for example, 1710>Transaction currency : <currency code, for example, USD>Document Date: <today>Posting Date: <today>Click on Create. | The Funds Reservation - General Data is entered. |  |
| 5 | Enter Document Item | On the Earmarked Funds section for document items, select Create.In the Item Details make the following entries:Total Amount: 100Cost Center: <company code, for example, 17101101>Account Number: 61100000Click Enter.This master data should be derived (if not, please enter it manually).Functional Area: <functional area, for example, 1000>Grant: NRGFund: <fund, for example, G1100>Budget Period: <current year>Click Apply | The Funds Reservation-Document Item is entered. |  |
| 6 | Save the Funds Reservation Document. | Click Create. | A system message appears informing you that the document has been saved. |  |
| 7 | Check Budget Consumption | Click on Budget AVC Overview - Overall Available Budget (F2163).Check the budget consumption for the master data to which you posted the earmarked fund document.Fund: <fund, for example, G1100>Cost Center: <cost center, for example, 17101101>In the Budget Consumption Detail the following entries should be visible:Amount Type: Original Amount (ORIG)Budget Consumption Type: Funds Reservation (81)Amount: 100 | The budget report shows the respective budget consumption. |  |

### Create Funds Precommitment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Prerequisities

You have executed the scope item procedure [Create Funds Reservation](#unique_10) [page ] 8.

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Check Available Budget | Run the Budget AVC Overview - Overall Available Budget (F2163) Fiori appSelect the master data below and make a note of the following figures; Consumable amount, consumed amount and available amount | The budget report is displayed. |  |
| 3 | Open Manage Earmarked Funds | Frontend Fiori App:Open Manage Earmarked Funds (F4657). | The Manage Earmarked Funds Documents (F4657) screen appears. |  |
| 4 | Enter General Data | On the Manage Earmarked Funds Documents (F4657) screen, choose Create Funds Precommitment.Enter the General Data on the dialog box:Document Type: PrecommitmentCompany Code: <company code, for example, 1710>Transaction Currency : <currency code, for example, USD>Document Date: <today>Posting Date: <today>Click Create. | The Funds Precommintment-General Data is entered. |  |
| 5 | Enter Document Item | In the Earmarked Funds section for document items, select Create.In the Item Details make the following entries:Total Amount: 90Funds Reservation: <the one you created above>Funds Reservation Item: 1This master data should be defaulted from the funds reservation (if not, please enter it manually).Functional Area: <functional area, for example, 1000>Grant: NRGFund: <fund, for example, G1100>Budget Period: <current year>Cost Center: < cost center, for example, 17301101>Account Number: 61100000Click Apply. | The Funds Precommitment-Document Item is entered. |  |
| 6 | Save the Funds Precommitment Document | Click Save. | A system message appears informing you that the document has been saved. |  |
| 7 | Check Budget Consumption | Check the budget consumption for the master data to which you posted the earmarked fund document.Fund: <fund, for example, G1100>Cost Center: <cost center, for example, 17101101>In the Budget Consumption Detail the following additional entries should be visible:Amount Type: Reduction (REDU)Budget Consumption Type: Funds Reservation (81)Amount: 90Next line:Amount Type: Original Amount (ORIG)Budget Consumption Type: Funds Precommitment (82)Amount: 90 | The budget report shows the same budget consumption as above. |  |

### Create Funds Commitment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Prerequisities

You have executed the scope item procedure Create Funds Precommitment.

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Check Available Budget | Run the Budget AVC Overview - Overall Available Budget (F2163) Fiori appSelect the master data below and make a note of the following figures; Consumable amount, consumed amount and available amount | The budget report is displayed. |  |
| 3 | Open Manage Earmarked Funds | Frontend Fiori app:Open Manage Earmarked Funds (F4657). | The Manage Earmarked Funds Documents (F4657) screen appears. |  |
| 4 | Enter General Data | On the Manage Earmarked Funds Documents (F4657) screen, choose Create Funds Commitment.Enter the General Data on the dialog box:Document Type: CommitmentCompany Code: <company code, for example, 1710>Transaction currency : <currency code, for example, USD>Document Date: <today>Posting Date: <today>Click on create. | The Funds Commintment screen opens in the editing mode. |  |
| 5 | Enter Document Item | In the Earmarked Funds section for document items, select Create.In the Item Details make the following entries:Total Amount: 80Funds Precommitment: <the one you created above>Funds Precommitment item: 1This master data should be defaulted from the funds precommitment (if not, please enter it manually).Functional Area: <functional area, for example, 1000>Grant: NRGFund: <fund, for example, G1100>Budget Period: <current year>Cost Center: <cost center, for example, 17101101>Account Number: 61100000Click Apply. | The Funds Precommitment-Document Item is entered. |  |
| 6 | Save the Funds Precommitment Document | Click on Save. | A system message appears informing you that the document has been saved. |  |
| 7 | Check Budget Consumption | Check the budget consumption in the master data to which you posted the earmarked funds document.Fund: <fund, for example, G1100>Cost Center: <cost center, for example, 17101101>In the Budget Consumption Detail the following additional entries should be visible:Amount Type: Reduction (REDU)Budget Consumption Type: Funds Precommitment (82)Amount: 90Next line:Amount Type: Original Amount (ORIG)Budget Consumption Type: Funds Commitment (65)Amount: 80 | The budget report shows the same budget consumption as above. |  |

### Vendor Invoice with Reference to a Funds Commitment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter a supplier invoice with reference to an earmarked fund.

Procedure

Prerequisites

You have executed the scope item procedure to create a funds commitment document.

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using a personalized user.Do not use the generic Accounts Payable Accountant user. Create a personalized user based on the business role ID SAP_BR_AP_ACCOUNTANT |  |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice (F0859) view appears. |  |
| 3 | Dialog Box | If the Data from Previous Invoice Entry Exist dialog box appears, choose No. |  |  |
| 4 | General Information | In the Basic Data section, enter the following data:Transaction: InvoiceCompany Code: <company code, for example, 1710>Invoicing Party: <invoicing party, for example, 17300001>Gross Invoice Amount: <the amount of the Funds Commitment>Currency: <currency code, for example, USD>Invoice Date: <Today's date>Posting Date: <Today's date>Reference: <any> |  |  |
| 5 | G/L Account Items | In the G/L Account Items section, choose Add to add a new item.Make the following entries:Debit/Credit: DebitG/L Account 61061000Amount 80 |  |  |
| 6 | Account Assignment | Under G/L Accounts, choose > (Expand/Collapse) to expand the selection, make the following entries:In Earmarked Funds References, make the following entries (use a EF you created previously) and choose Enter.Earmarked Fund: <EF number>Note: This master data should be defaulted from the Funds Commitment document (if not, please enter it manually).Cost Center: <cost center, for example, 17101101>Fund: <fund, for example, G1100>Budget Period: <current year>Grant: NRGFunctional Area: <functional area, for example, 1000>If the General Ledger account is tax- relevant, in the Tax section, select Propose Tax.Payment area:Baseline Payment Dte: <enter today's date>If not enough budget is available, PSM Availability Control (AVC) might show a warning message. If this happens, you can still continue with the posting. | All items for the selected Earmarked Funds are added. |  |
| 7 | Post invoice | Choose Post.Note The supplier invoice number generated is a logistics document number. To find or review the finance document number (journal entry), see the Invoice Payment Preparation > View Supplier Line Items task. | The invoice is posted. The system displays the message that the invoice xxx has been posted and document no. 51xxxxxxxx has been created. |  |
| 8. | Check Budget Consumption | Check the budget consumption for the master data to which you posted the earmarked fund document.Fund: <fund, for example, G1100>Cost Center: <cost center, for example, 17101101>In the Budget Consumption Detail the following aditional entries should be visible:Amount Type: Reduction (REDU)Budget Consumption Type: Funds Commitment (65)Amount: 80Next line:Amount Type: Original Amount (ORIG)Budget Consumption Type: expense (99)Amount: 80 | The Budgeting report shows the same budget consumption as above | . |

### Approving an Earmarked Fund

#### Create an EF Document Type for Workflow Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you set up a workflow to approve a reservation using a workflow.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as the Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open the Manage Your Solution (F1241) app | Frontend Fiori App:Open Manage Your Solution (F1241). | The Manage Your Solution (F1241)screen appears. |  |
| 3 | Open theConfigure Your Solution app | Frontend Fiori App:Open the Configure Your Solution (F2962) app. | The Configure Your Solution screen appears. |  |
| 4 | Configure the document type | Search using the following criteria:Application Area: Public SectorSub Application Area: Earmarked FundsClick on the configuration item: Earmarked Funds and locate the Define Document Types for Earmarked Funds.Click Configure in the configuration step: Define Document Types for Earmarked Funds | The configuration: Define Document Types for Earmarked Funds appears. |  |
| 5 | Configure a new document type | Click on New Entries and enter the following values:Doc Category: 030Document Type: WFDocument Type Description: Reservation with WorkflowNumber Range: 30Field Status Group: SG10Tolerance Key: ST01Click Start WorkflowTemplate Type: ST01Click save and exit the transaction. | The configuration dialog Define Document Types for Earmarked Funds is open. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in the SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open the document types for earmarked funds | Go to the Business Processes Configuration app and search for the activity Define Document Types for Earmarked Funds.Choose the line item in the search result to see more details about this configuration activity.Choose Go to Activity to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Define Document Types for Earmarked Funds”: Overview screen appears. |  |
| 3 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Document Types for Earmarked FundsChoose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Document Types for Earmarked Funds screen appears. |  |
| 4 | Configure a new document type | Click on New Entries and enter the following values:Doc Category: 030Document Type: WFDocument Type Description: Reservation with WorkflowNumber Range: 30Field Status Group: SG10Tolerance Key: ST01Click Start WorkflowTemplate Type: ST01Choose save and exit the transaction. | The configuration dialog Define Document Types for Earmarked Funds is open. |  |

#### Define the Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the user Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the SAP Fiori App | Open Manage Workflows for Earmarked Funds (F6951). | The Manage Workflows for Earmarked Funds (F6951) view appears showing the existing list of workflows. |  |
| 3 | Workflows | Choose Create | The dialog for the New Workflow appears |  |
| 4 | New Workflow | Enter the following data:Workflow Name: “New Workflow for Reservations”Start Condition: (first field) Document Type or Earmarked Funds is; (second field) WFIn the Steps section, choose Create. | The new step view appears. |  |
| 5 | New Step | Enter the following data:Header Section:Step Type: Manual Approval of Earmarked FundsRecipient Section:Assignment By: RoleRole: Users with Business Catalog: Earmarked Fund - Document ApprovalChoose Create and then Save in the New Workflow dialog | A success message appears. The workflow is saved. |  |
| 6 | Activate Workflow | Choose Activate | The new workflow appears in the list of workflows with the status Active. |  |
| 7 | Change Workflow Order | Choose Define Order.The Define Order dialog appears.Select your Workflow and choose Move to move the selected workflow to the top.Choose Save . | Your workflow appears as the first workflow in the list with Order 1. |  |

#### Create a Reservation Subject to Approval and Approve a Reservation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2. | Open Manage Earmarked Funds . | Frontend Fiori App:Open Manage Earmarked Funds (F4657). | The Manage Earmarked Funds Documents (F4657) screen appears. |  |
| 3. | Enter General Data | On the Earmarked Funds screen select Create Funds Reservation.Enter the General Data on the dialog box:Document Type: Reservation with WorkflowCompany Code: <company code, for example, 1710>Transaction currency: <currency code, for example, USD>Document Date: <today>Posting Date: <today>Click on Create. | The Funds Reservation - General Data is entered. |  |
| 4 | Enter a Document Item | In the Earmarked Funds section for document items, select Create.In the Item Details make the following entries:Amount Changed: 100Cost Center: <cost center, for example, 17101101>Account Number: 61100000Click Enter.This master data should be derived (if not, please enter it manually).Functional Area: <functional area, for example, 1000>Grant : NRGFund: <fund, for example, G1100>Budget Period: <current year>Click Apply | The Funds Reservation - Document Item is entered. |  |
| 5 | Save the Funds Reservation Document. | Click Create. | A system message appears informing you that the document has been saved and the workflow has been started. The status of the reservation is “In Approval” and on the tab Approval Details you can see that the processor of the workflow is the BUDGET_RESPONSIBLE. |  |
| 6. | Log On | Log on to the SAP Fiori launchpad as the budget responsible. | The SAP Fiori launchpad appears. |  |
| 7 | Open My Inbox. | Frontend Fiori App:Open My Inbox (F0862) | The My Inbox (F0862) screen appears. |  |
| 8. | Select Workflow Item | The Reservation appears on the left hand side of the screen under All Tasks.Click on the task | The details of the reservation appear on the right hand side of the screen |  |
| 9. | Approve the reservation | Choose Approve .Enter a Decision Note and choose Submit . | The reservation is approved and the workflow task disappears from the inbox. |  |

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
> Flagged while digesting this document, not verified: Internal inconsistency: in the Funds Commitment test, the commitment Total Amount is 80 but the expected budget consumption shows a Reduction (REDU) of Funds Precommitment (82) of 90; the same amounts are not otherwise reconciled.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Internal inconsistency: the Funds Precommitment item step says cost center 17301101 (stated to default from the reservation), while the reservation and every consumption check use cost center 17101101.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[03-financial-accounting-and-close/test-script-fund-accounting-7au-sap-s-4hana-cloud-public-edition-1206]]
- see-also :: [[17-leasing-and-real-estate/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana]]
- see-also :: [[17-leasing-and-real-estate/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/78S_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 34,050 chars in the whole document
