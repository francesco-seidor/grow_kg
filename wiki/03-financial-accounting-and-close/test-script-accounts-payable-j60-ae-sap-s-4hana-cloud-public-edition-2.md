---
id: 03-financial-accounting-and-close/test-script-accounts-payable-j60-ae-sap-s-4hana-cloud-public-edition-2
title: "Test Script: Accounts Payable (J60_AE) - SAP S/4HANA Cloud Public Edition 2608, United Arab Emirates (J60_S4CLD2608_BPD_EN_AE)"
description: "SAP test script J60_AE for Accounts Payable (UAE, company code 3310): prerequisites, BRF+ setup and step-by-step procedures for invoices, payment runs, approvals, reporting."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/accounts-payable]
aliases: [J60_S4CLD2608_BPD_EN_AE]
keywords: [Accounts Payable and Payment Runs, accounts payable, supplier invoice entry, payment run, bank payment approval, payment media, down payments, brf+ output settings, business partner certificates, vendor certificate validity]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J60_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1306
topic: 03-financial-accounting-and-close/accounts-payable
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Accounts Payable (J60_AE) - SAP S/4HANA Cloud Public Edition 2608, United Arab Emirates (J60_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J60_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Accounts Payable and Payment Runs** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 18-09-26 |
| --- | --- |
|  | Accounts Payable (J60_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc241659894)

[2 Prerequisites 7](#_Toc241659895)

[2.1 System Access 7](#_Toc241659896)

[2.2 Roles 7](#_Toc241659897)

[2.3 Master Data, Organizational Data, and Other Data 8](#_Toc241659898)

[2.4 Business Conditions 11](#_Toc241659899)

[2.5 Preliminary Steps 12](#_Toc241659900)

[2.5.1 Maintain Payment Approver for Bank Accounts 12](#_Toc241659901)

[2.5.2 Define Payment Medium Format Variants (Optional) 12](#_Toc241659902)

[2.5.3 BRF+ Settings 15](#_Toc241659903)

[2.5.3.1 BRF+ Settings for Payment Advice 15](#_Toc241659904)

[2.5.3.2 BRF+ Settings for Supplier Balance Confirmation 18](#_Toc241659905)

[2.5.3.3 BRF+ Settings for Item Interest Calculation 22](#_Toc241659906)

[2.5.3.4 BRF+ Settings for Payment List 27](#_Toc241659907)

[2.5.4 Add Fields to Items (Optional) 29](#_Toc241659908)

[2.5.5 Maintain Business Users 31](#_Toc241659909)

[2.5.6 Business Partner Certificates 32](#_Toc241659910)

[2.5.6.1 Activate Business Partner Certificates Functionality 32](#_Toc241659911)

[2.5.6.2 Define Business Partner Certificate IDs 33](#_Toc241659912)

[2.5.6.3 Assign Business Partner Certificates to Country/Region 34](#_Toc241659913)

[3 Overview Table 36](#_Toc241659914)

[4 Test Procedures 44](#_Toc241659915)

[4.1 Preparation of Payments 44](#_Toc241659916)

[4.1.1 Maintain Business Partner 44](#_Toc241659917)

[4.1.2 Maintain Business Partner Certificate 46](#_Toc241659918)

[4.1.3 Display Supplier List 47](#_Toc241659919)

[4.1.4 Netting of AR/AP Items (Optional) 48](#_Toc241659920)

[4.1.5 Available Amounts for Payment Program (Optional) 50](#_Toc241659921)

[4.2 Invoice Entry without Purchase Order 52](#_Toc241659922)

[4.2.1 Invoice Entry Without Purchase Order 52](#_Toc241659923)

[4.2.2 Invoice Entry for One-Time Supplier without Purchase Order 54](#_Toc241659924)

[4.2.3 Park and Post Invoice 56](#_Toc241659925)

[4.2.3.1 Park Invoice 56](#_Toc241659926)

[4.2.3.2 Post Invoice 58](#_Toc241659927)

[4.3 Recurring Supplier Invoices 60](#_Toc241659928)

[4.3.1 Create Recurring Supplier Invoice 60](#_Toc241659929)

[4.3.2 Review Recurring Supplier Invoice 63](#_Toc241659930)

[4.3.3 Schedule Recurring Supplier Invoice Posting 64](#_Toc241659931)

[4.4 Mass Upload 66](#_Toc241659932)

[4.4.1 Mass Import for Supplier Invoices 66](#_Toc241659933)

[4.5 Invoice Payment Preparation 69](#_Toc241659934)

[4.5.1 View Supplier Line Items 69](#_Toc241659935)

[4.5.2 Manage Payment Blocks 71](#_Toc241659936)

[4.5.3 View Supplier Balance 72](#_Toc241659937)

[4.6 Payment Run 73](#_Toc241659938)

[4.6.1 Schedule Payment Proposals 74](#_Toc241659939)

[4.6.2 Revise Payment Proposal 76](#_Toc241659940)

[4.6.3 Release Payment Proposal 77](#_Toc241659941)

[4.6.4 Mass Reverse Payment Run (Optional) 79](#_Toc241659942)

[4.6.5 View Payment List 80](#_Toc241659943)

[4.7 Payment Plans 81](#_Toc241659944)

[4.8 Single Outgoing Payment 84](#_Toc241659945)

[4.8.1 Create Single Outgoing Payment (Indirect) 84](#_Toc241659946)

[4.9 Online Payments 86](#_Toc241659947)

[4.9.1 Free Form Payment Request 86](#_Toc241659948)

[4.9.2 Review or Edit Free Form Payment Request 87](#_Toc241659949)

[4.9.3 Process Free Form Payment 88](#_Toc241659950)

[4.10 Manual Payment Online 90](#_Toc241659951)

[4.10.1 Post Outgoing Payment 90](#_Toc241659952)

[4.11 Payment Approval 91](#_Toc241659953)

[4.11.1 Bank Payment Approval (Optional based on Cash Management) 92](#_Toc241659954)

[4.11.1.1 Approval by First Approver 93](#_Toc241659955)

[4.11.1.2 Rejection 94](#_Toc241659956)

[4.11.1.3 Approval by Second Approver 95](#_Toc241659957)

[4.12 Payment Media 96](#_Toc241659958)

[4.12.1 Create Payment Media 96](#_Toc241659959)

[4.12.2 Manual Creation of Payment Media 97](#_Toc241659960)

[4.12.3 Manual Deletion of Payment Media 99](#_Toc241659961)

[4.13 Payment Advices 100](#_Toc241659962)

[4.13.1 Print or Email Payment Advice 100](#_Toc241659963)

[4.13.2 Schedule Payment Advices (Optional) 102](#_Toc241659964)

[4.14 Correspondence 103](#_Toc241659965)

[4.15 Incorrect Posting 107](#_Toc241659966)

[4.15.1 Reset Cleared Items 107](#_Toc241659967)

[4.15.2 Reset and Reverse Cleared Items 108](#_Toc241659968)

[4.15.3 Schedule Jobs to Reset Cleared Items (Optional) 109](#_Toc241659969)

[4.16 Down Payments 111](#_Toc241659970)

[4.16.1 Create Down Payment Request 111](#_Toc241659971)

[4.16.1.1 Create Down Payment Request 111](#_Toc241659972)

[4.16.1.2 Create Down Payment Request with Workflow 112](#_Toc241659973)

[4.16.1.2.1 Create Team 113](#_Toc241659974)

[4.16.1.2.2 Create Workflow 114](#_Toc241659975)

[4.16.1.2.3 Create Supplier Down Payment Request for Approval 116](#_Toc241659976)

[4.16.1.2.4 Review Down Payment Request 118](#_Toc241659977)

[4.16.1.2.5 Process Down Payment Request Approval 119](#_Toc241659978)

[4.16.2 Post Down Payment 121](#_Toc241659979)

[4.16.3 Invoice Entry 124](#_Toc241659980)

[4.16.4 Post Outgoing Payment 125](#_Toc241659981)

[4.16.5 Clear Open Items 126](#_Toc241659982)

[4.17 Optional: Interest Calculation 128](#_Toc241659983)

[4.17.1 Optional: Schedule Interest Calculation Jobs 128](#_Toc241659984)

[4.17.2 Optional: Manage Interest Runs 130](#_Toc241659985)

[4.17.3 Optional: Display Interest Runs 131](#_Toc241659986)

[4.18 Guarantees Received 132](#_Toc241659987)

[4.18.1 Guarantees Received 132](#_Toc241659988)

[4.18.2 Reverse Guarantees 133](#_Toc241659989)

[4.19 Periodic Activities 134](#_Toc241659990)

[4.19.1 Check Open Balances 134](#_Toc241659991)

[4.19.2 Create Supplier Balance Confirmation 134](#_Toc241659992)

[4.19.3 Manage Supplier Balance Confirmations 136](#_Toc241659993)

[4.19.4 Print Supplier Balance Confirmation 137](#_Toc241659994)

[4.20 Invoice Management Reporting 138](#_Toc241659995)

[4.20.1 Accounts Payable Overview 138](#_Toc241659996)

[4.20.2 Days Payable Outstanding 140](#_Toc241659997)

[4.20.3 Overdue Payables 141](#_Toc241659998)

[4.20.4 Future Payables 142](#_Toc241659999)

[4.20.5 Cash Discount Forecast 142](#_Toc241660000)

[4.20.6 Cash Discount Utilization 143](#_Toc241660001)

[4.20.7 Invoice Processing Analysis 144](#_Toc241660002)

[4.20.8 Invoice Processing Time 145](#_Toc241660003)

[4.20.9 Aging Analysis 146](#_Toc241660004)

[4.20.10 Aging Report for Accounts Payable 146](#_Toc241660005)

[4.20.11 Automatic and Manual Payments Analysis 147](#_Toc241660006)

[4.20.12 Supplier Payments Analysis 148](#_Toc241660007)

[4.20.13 Display Item Change Log 149](#_Toc241660008)

[4.21 Vendor Certificate Validity Check 150](#_Toc241660009)

[5 Appendix 156](#_Toc241660010)

[5.1 Display Process Flow Accounts Payable 156](#_Toc241660011)

[5.2 Disable Period Check for Material Master (Optional) 157](#_Toc241660012)

[5.3 Monitor Payments 158](#_Toc241660013)

[5.3.1 Monitor Payments 159](#_Toc241660014)

## Purpose

Overview

With Accounts Payable, you manage your open payable invoices that are automatically created from purchasing processes.

You manage and control open items with various analytical tools. You plan future payables and analyze the outcome of payments, such as utilization of cash discounts and days payables outstanding.

Automate processing of your outstanding payables and monitor payment progress. Optionally, you can also include a two-step approval for all outgoing payments.

Connect to SAP Multi-Bank Connectivity (MBC) to streamline the connectivity to the banks for payments and bank statements. Alternatively, you can also download generated payment files.

For applicable countries or regions, you can also print checks.

This business process focuses on the following activities:

Complete Supplier Master Data

Invoice Entry without Purchase Order

Mass Upload

Invoice Payment Preparation:

- Manage Payment Blocks
- Manage Supplier Line Items

Payment Run:

- Schedule Payment Proposals
- Revise Payment Proposal
- Mass Reverse Payment Run
- View Payment List

Single Outgoing Payment

Manual Payment Online

Payment Approval

Correspondence

Incorrect Posting

Down Payments

Interest Calculation (Optional)

Periodic Activities

Invoice Management Reporting:

- Days Payable Outstanding
- Overdue Payables
- Future Payables
- Cash Discount Forecast
- Cash Discount Utilization
- Invoice Process Time
- Aging Analysis
- Automatic and Manual Payments
- Open Payments Analysis

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

- Vendor master data has been created.
- Invoices have been posted to accounting.
- Complete Business Conditions.
- Execute Preliminary Steps.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Country-specific subrole: Accounts Payable Accountant for United Arab Emirates | SAP_BR_AP_ACCOUNTANT_AE |  |  |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Master Data Specialist - Business Partner Data te | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Manager | SAP_BR_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The business process is enabled with organization-specific master data, examples are provided in the following table.

Operational Focus

SAP delivers standard values for more than one operational focus area, such as Services, Manufacturing, or Trade. You may find more than one master data table. Use the master data that matches the operational focus of your company (Services, Manufacturing, or Trade).

|  |
| --- |
| Note Additional Default ValuesYou can test the scenario with other SAP default values that have the same characteristics. |

Use the following master data in the process steps described in this document:

You've entered the master data required to go through the procedures of this scenario. Ensure that the following scenario-specific master data exists before you test this scenario.

Master Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101301 |  |  |
| Material Master | * |  | Material type DIEN, SEMI, HAWA |
| House Bank | AEBK1AEBK2 |  | The AEBK2 value is used for non-MBC payments. Make sure that the solution is installed with demo data to be able to test both banks. |
| Account ID | AEAC1 AEAC2 |  |  |
| Bank G/L Account | 11001000 |  |  |
| Supplier | For Company Code 3310, use:333000013330000233300273 for one-time supplier |  |  |
| Payment Method | See the following table for Payment Methods (PM) and Payment Method Formats (PMF) |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |

Payment Methods and Payment Medium Formats

Use the following table for payment methods (PM) and payment medium formats (PMF).

| PM | Name of Payment Method | PMF for MBC House Bank AEBK1 | PMF for File Download (AEBK2 demo data)* |
| --- | --- | --- | --- |
| F | Foreign Bank Transfer | AE _CGI_XML_CT | AE _CGI_XML_CT |
| T | Bank Transfer Domestic | AE_CGI_XML_CT | AE_CGI_XML_CT |

|  |
| --- |
| Note For *, the AEBK2 value is demo data. Ensure that the solution is installed with demo data to test this value. |

### Business Conditions

Invoices to be paid must be available. You can enter new invoices by running the purchase process in Material Management.

| Test Script/Scenario | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | Must be run before this test script. Invoices are created and posted to accounting. |
| J13 - Service and Material Procurement – Project-Based Services | Must be run before this test script. Invoices have been created and posted to accounting. |
| BFA - Basic Bank Account Management | Bank account master data is processed. |
| BFB - Basic Cash Operations | Outgoing payment to vendors is integrated with a bank. |
| J77 - Advanced Bank Account Management | Bank accounts and approvers in banks have been defined. |
| J78 - Advanced Cash Operations | Preliminary steps in Prerequisites are performed.Payment approvers are defined. The Outgoing Payment with Bank Communication Management (BCM) process is executed. |
| J58 - Accounting and Financial Close | Posting periods are open. |
| BNZ - Create New Open MM Posting Period - MDS | MM posting periods are open. |
| BNX - Consumable Purchasing | Execute the Activate Flexible Workflow for Supplier Invoice preliminary step. |
| 1LQ - Output Management | Ensure that you set up printers, create a print queue, and/or set up email. These activities are in the Setup Instructions document. |

### Preliminary Steps

#### Maintain Payment Approver for Bank Accounts

Purpose

In this activity, you maintain the payment signatories for existing bank accounts. Payment signatories work as approvers in the optional [Payment Approval](#unique_8) [page ] 91 topic.

|  |
| --- |
| Note For more information, in the Advanced Cash Operations (J78) test script, see Prerequisites > Preliminary Steps . |

Prerequisite

Two sample bank accounts are created in the system.

Procedure

|  |
| --- |
| Note In the Advanced Cash Operations (J78) test script, execute all steps in the Preliminary Steps section. |

|  |
| --- |
| Caution This step is only needed for customers who adopt full Cash Management, which needs an additional license for SAP Cash Management; otherwise, Basic Cash Management is adopted and you can skip this step. |

#### Define Payment Medium Format Variants (Optional)

Purpose

In this activity, you create, change, and assign selection variants for payment medium formats. You can then use these variants when creating payment media using the Payment Medium Workbench.

Selection variants are needed to generate the Payment Medium.

Prerequisite

- Payment Methods are specified and assigned to your country/region and company code.
- Payment Medium Formats are assigned to your Payment Methods.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country/region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Accounts Payable

1. For the row with Item Name of Payment Medium Formats, choose Details (>).
2. For the Create/Assign Selection Variants (Alternative) row, choose Configure.
3. Continue with the procedure in the table below.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Configuration Steps | In the dialog box, select the Payment Medium Format to process, for example:Payt Mdm Format: AE_CGI_XML_CTNote Ensure that you select a Payment Medium Format that's valid for your country/region and was installed in your solution. For more information, see the Payment Methods (PM) and Payment Medium Formats (PMF) table in the Master Data, Organizational Data, and Other Data topic under Prerequisites. | The Change View "Payment Medium Format: Format for Variants": Details view is displayed. |  |
| 2 | Variant Creation | Caution The selected Payment Medium Format determines which fields are available.When defining the Payment Medium Format from the prior step, the CoCd, House Bk fields are available. On the row of the company code and house bank you're processing, for example Co. Code: 3310 and House bank: AEBK1 , enter the following:Selection Variant: <any description (14 characters max.)>Note If the selected variant already exists, create a variant by entering a new description. Or you can keep the same variant and change the parameters as described in the next step. | Selection variant is created and assigned. |  |
| 3 | Save | Choose Save and then Exit. | Variant is created, assigned, and saved. |  |

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create/Assign Selection Variants (Alternative).
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Configuration Steps | In the dialog box, select the Payment Medium Format to process, for example:Payt Mdm Format: AE_CGI_XML_CTNote Ensure that you select a Payment Medium Format that's valid for your country/region and was installed in your solution. For more information, see the Payment Methods (PM) and Payment Medium Formats (PMF) table in the Master Data, Organizational Data, and Other Data topic under Prerequisites. | The Change View "Payment Medium Format: Format for Variants": Details view is displayed. |  |
| 2 | Variant Creation | Caution The selected Payment Medium Format determines which fields are available.When defining the Payment Medium Format from the prior step, the CoCd, House Bk fields are available. On the row of the company code and house bank you're processing, for example Co. Code: 3310 and House bank: AEBK1 , enter the following:Selection Variant: <any description (14 characters max.)>Note If the selected variant already exists, create a variant by entering a new description. Or you can keep the same variant and change the parameters as described in the next step. | Selection variant is created and assigned. |  |
| 3 | Save | Choose Save and then Exit. | Variant is created, assigned, and saved. |  |

#### BRF+ Settings

##### BRF+ Settings for Payment Advice

Purpose

In this activity, you define the system determination of output parameters for payment advice for printing and e-mail.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination. | The Output Parameter Determination view is displayed. |  |
| 3 | Output Type | In the Select Business Rules section, choose:Show Rules for: Payment AdviceDetermination Step: Output Type | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Add Rules | Choose the Edit button. Under Table Contents, choose the + (Insert New Row) button and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Sep.Paymt.Adv.: X (Yes)Output type: PAYM_ADVDispatch Time: 1 (Immediately) |  |  |
| 5 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 6 | Receiver | In the Select Business Rules section, choose:Show Rules for: Payment AdviceDetermination Step: Receiver | Details are displayed in the Maintain Business Rules section. |  |
| 7 | Add Rules | Choose the Edit button. Under Table Contents choose the + (Insert New Row) button and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVSupplier: isn't initialCustomer: leave blankRole: HExclusive Indicator: (false)Choose + to insert a row and enter the following:Output type: PAYM_ADVSupplier: leave blankCustomer: isn't initialRole: SExclusive Indicator: (false) |  |  |
| 8 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 9 | Channel | In the Select Business Rules section, chooseShow Rules for: Payment AdviceDetermination Step: Channel | Details are displayed in the Maintain Business Rules section. |  |
| 10 | Add Rules | Choose the Edit button. Under Table Contents choose the + (Insert New Row) button and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVChannel: PRINT (Printout)Exclusive Indicator: - (false)Choose the + (Insert New Row) button to insert a row and enter the following:Output type: PAYM_ADVChannel: EMAIL (email)Exclusive Indicator: - (false) |  |  |
| 11 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 12 | Printer Settings | In the Select Business Rules section, chooseShow Rules for: Payment AdviceDetermination Step: Printer Settings | Details are displayed in the Maintain Business Rules section. |  |
| 13 | Add Rules | Choose the Edit button. Under Table Contents choose the + (Insert New Row) button to insert a row and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVPrint Queue: For example, QUEUE_PAYM_ADV or choose the print queue defined in your systemNumber of Copies: 1 |  |  |
| 14 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 15 | Email Settings | In the Select Business Rules section, choose:Show Rules for: Payment AdviceDetermination Step: Email Settings | Details are displayed in the Maintain Business Rules section. |  |
| 16 | Add Rules | Choose the Edit button. Under Table Contents choose the + (Insert New Row) button and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVSender Email: <sender email address>Email Template: FFO_PAYM_ADVICE_EMAIL_TEMPLATE |  |  |
| 17 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 18 | Output Relevance | In the Select Business Rules section, choose:Show Rules for: Payment AdviceDetermination Step: Output Relevance | Details are displayed in the Maintain Business Rules section. |  |
| 19 | Add Rules | Choose the Edit button. Under Table Contents choose the + (Insert New Row) button to insert a row and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVRelevance Indicator: X (True) |  |  |
| 20 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 21 | Form Template | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 22 | Add Rules | Choose the Edit button. Under Table Contents choose the + (Insert New Row) button and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVForm Template: FIN_FO_PAYM_ADVICEForm Language: For example, E (English). | Rule data is entered. |  |
| 23 | Activate Rules | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 24 | Email Recipient | To specify the email address of the recipient of the payment advice, follow the instructions described in Test Procedures > Preparation of Payments > Maintain Business Partner , in the Correspondence step. |  |  |

##### BRF+ Settings for Supplier Balance Confirmation

Purpose

In this activity, you define the system determination of output parameters for printing a balance confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |  |
| 3 | Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Output Type | Details display in the Maintain Business Rules section. |  |
| 4 | Add Rules | Choose the Edit button. Under Table Contents choose the + button to insert a row and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: LETTERDispatch Time: 1 (Immediately)Choose the + button to insert a row.Make the following entries:Output type: CHECKLISTDispatch Time: 1 (Immediately) |  |  |
| 5 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 6 | Receiver | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Receiver | Details display in the Maintain Business Rules section. |  |
| 7 | Add Rules | Choose the Edit button. Under Table Contents choose the + button to insert a row and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: LETTERAccount type: K (Vendors)Role: KExclusive Indicator: - (false)Choose the + button to insert a row. Make the following entries:Output type: LETTERAccount type: D (Customers)Role: DExclusive Indicator: - (false)Choose the + button to insert a row. Make the following entries:Output type: CHECKLISTAccount type: Leave blankRole: CExclusive Indicator: - (false). |  |  |
| 8 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 9 | Channel | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Channel | Details display in the Maintain Business Rules section. |  |
| 10 | Add Rules | Choose the Edit button. Under Table Contents choose the + button to insert a row and enter the following by choosing button. On the … or selecting Direct Value Input from the dropdown in each field:Output type: LETTERChannel: PRINTExclusive Indicator button. On the: - (false)Choose the + button to insert new row. Make the following entries:Output type: CHECKLISTChannel: PRINTExclusive Indicator: - (false) |  |  |
| 11 | Insert New Row | Choose Insert New Row. |  |  |
| 12 | Enter Details | Make the following entries:Output Type: LETTERChannel: EMAILExclusive Indicator: - (false) |  |  |
| 13 | Activate | Choose Activate. In the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 14 | Form Template | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Form Template | Details display in the Maintain Business Rules section. |  |
| 15 | Add Rules | Choose the Edit button. Under Table Contents choose the + button to insert a row and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: LETTERForm Template: FIN_FO_BLNC_CNFRM_LTTRChoose the + button to insert a row and make the following entries:Output type: CHECKLISTForm Template: FIN_FO_BLNC_CNFRM_CHKLST | Rule data is entered. |  |
| 16 | Activate Rules | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 17 | Output Relevance | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Output Relevance | Details display in the Maintain Business Rules section. |  |
| 18 | Add Rules | Choose the Edit button. Under Table Contents choose the + button to insert a row and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: LETTERRelevance Indicator: X (True)Choose the + button to insert a row.Make the following entries:Output type: CHECKLISTRelevance Indicator: X (True) |  |  |
| 19 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 20 | Printer Settings | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Printer Settings |  |  |
| 21 | Add Rules | Choose the Edit button. Under Table Contents choose the + button to insert a row and enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: LETTERPrint Queue: DEFAULT or use the one defined in your system.Number of Copies: 1Choose the + button to insert a row. Make the following entries:Output type: CHECKLISTPrint Queue: DEFAULT or enter the queue defined in your systemNumber of Copies: 1 |  |  |
| 22 | Activate | Choose the Activate button. On the Confirm Activation dialog box, choose Yes. | Rules activate. |  |
| 23 | Email Settings | In the Select Business Rules section, choose:Show Rules For: Balance ConfirmationDetermination Step: Email Settings |  |  |
| 24 | Add Rules | Choose Edit. |  |  |
| 25 | New Row | In Table Contents, choose + (Insert New Row). |  |  |
| 26 | enter Details | Make the following entries:Output Type: LETTERSender Email: <sender email address>Email Template: FIN_BLNC_CNFRM_EMAIL_TMPL_LTTR |  |  |
| 27 | Activate | Choose Activate. | The Confirm Activation dialog box is displayed. |  |
| 28 | Confirm | Choose Yes. | The rules are activated. |  |

##### BRF+ Settings for Item Interest Calculation

Purpose

In this activity, you define the system determination of output parameters for item interest calculation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |  |
| 3 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Item Interest CalculationDetermination Step: Output Type | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Maintain Business Rules | Expand the Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and enter or verify the following:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: INTEREST_LETTERand choose OK.From the Dispatch Time field dropdown, select Direct Value Input.Dispatch Time: 1 (Immediately) or 2 (Scheduled)and choose OK. |  |  |
| 5 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | The Objects saved and activated notification displays. |  |
| 6 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Item Interest CalculationDetermination Step: Receiver |  |  |
| 7 | Maintain Business Rules | If necessary, expand the Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Receiver Account Type field dropdown, select Direct Value Input.AcctTy.Rec.IntCalc: = K (Suppliers)and choose OK.From the Role field dropdown, select Direct Value Input.Role: = Kand choose OK.From the Exclusive Indicator field dropdown, select Direct Value Input.Exclusive Indicator: X (true)and choose OK.Choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Receiver Acct Type field dropdown, select Direct Value Input.AcctTy.Rec.IntCalc: = D (Customers)and choose OK.From the Role field dropdown, select Direct Value Input.Role: = Dand choose OK.From the Exclusive Indicator field dropdown, select Direct Value Input.Exclusive Indicator: X (true)and choose OK. |  |  |
| 8 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | The Objects saved and activated notification displays. |  |
| 9 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Item Interest CalculationDetermination Step: Channel |  |  |
| 10 | Maintain Business Rules | If necessary, expand the Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Channel field dropdown, select Direct Value Input.Channel: PRINTand choose OK.From the Exclusive Indicator field dropdown, select Direct Value Input.Exclusive Indicator: - (false)and choose OK.Choose + (Insert New Row) and enter the following:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Channel: EMAILand choose OK.From the Exclusive Indicator field dropdown, select Direct Value Input.Exclusive Indicator: - (false)and choose OK. |  |  |
| 11 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | The Objects saved and activated notification displays. |  |
| 12 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Item Interest CalculationDetermination Step: Printer Settings |  |  |
| 13 | Maintain Business Rules | If necessary, expand the Maintain Business Rules section.Choose Edit .In the Table Contents section, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Print Queue field dropdown, select Direct Value Input.Print Queue: DEFAULT or use the one defined in your systemNumber of Copies: 1and choose OK. |  |  |
| 14 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | The Objects saved and activated notification displays. |  |
| 15 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Item Interest CalculationDetermination Step: Email Settings |  |  |
| 16 | Maintain Business Rules | If necessary, expand the Maintain Business Rules section.Choose Edit .In the Table Contents section, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output type field dropdown, select Direct Value Input.Email Template: FFO_ITEM_INTEREST_EMAIL_TPLand choose OK. |  |  |
| 17 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | The Objects saved and activated notification displays. |  |
| 18 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Item Interest CalculationDetermination Step: Form Template |  |  |
| 19 | Maintain Business Rules | Expand the Maintain Business Rules section.Choose Edit.In the Table Contents section, choose + (Insert New Row).Make or verify the following entries:#: <next higher number>From the Debit/Credit field dropdown, select Direct Value Input.Debit/Credit: = S (Debit)and choose OK.Note The Form Template column is at the far right of the table. Use the scroll bar along the bottom of the table to scroll right to display for the following two entries.From the Form Template field dropdown, select Direct Value Input.Form Template: FFO_ITEM_INTEREST_LETTER_Dand choose OK.Choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Debit/Credit field dropdown, select Direct Value Input.Debit/Credit: = H (Credit)and choose OK.Note The Form Template column is at the far right of the table. Use the scroll bar along the bottom of the table to scroll right to display for the following two entries.From the Form Template field dropdown, select Direct Value Input.Form Template: FFO_ITEM_INTEREST_LETTER_Cand choose OK. |  |  |
| 20 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | The Objects saved and activated notification displays. |  |
| 21 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Item Interest CalculationDetermination Step: Output Relevance |  |  |
| 22 | Maintain Business Rules | If necessary, expand the Maintain Business Rules section.Choose Edit.On Table Contents choose + (Insert New Row) and enter the following:#: <next higher number>From the Relevance Indicator field dropdown, select Direct Value Input.Relevance Indicator: X (True)and choose OK. |  |  |
| 23 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | The Objects saved and activated notification displays. |  |

##### BRF+ Settings for Payment List

Purpose

In this activity, you define the system determination of output parameters of the payment list for printing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination view is displayed. |  |
| 3 | Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Output Type | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTDispatch Time: 1 (Immediately) | The Confirm Activation dialog box is displayed. |  |
| 5 | Activate | Choose Yes. | Rules are activated. |  |
| 6 | Receiver | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Receiver | Details are displayed in the Maintain Business Rules section. |  |
| 7 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTIndicator: Only P…: =X (Yes)Role: PPExclusive Indicator: (false)Choose + to insert a row.Enter the following:Output type: PAYM_LISTIndicator: Only P…: =falseRole: PLExclusive Indicator: (false) | The Confirm Activation dialog box is displayed. |  |
| 8 | Activate | Choose Yes. | Rules are activated. |  |
| 9 | Channel | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Channel | Details are displayed in the Maintain Business Rules section. |  |
| 10 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTChannel: PRINT (Printout)Exclusive Indicator: - (false) | The Confirm Activation dialog box is displayed. |  |
| 11 | Activate | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 12 | Printer Settings | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Printer Settings | Details are displayed in the Maintain Business Rules section. |  |
| 13 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTPrint Queue: For example, DEFAULT or choose the print queue defined in your systemNumber of Copies: 1 | The Confirm Activation dialog box is displayed. |  |
| 14 | Activate | Choose Yes. | Rules are activated. |  |
| 15 | Form Template | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 16 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries:Output type: PAYM_LISTRole: PLForm Template: FIN_FO_PAYM_LIST_V2Choose + to insert a row.Enter the following:Output type: PAYM_LISTRole: PPForm Template: FIN_FO_PAYM_LIST_V2Choose Activate | The Confirm Activation dialog box is displayed. |  |
| 17 | Activate Rules | Choose Yes. | Rules are activated. |  |
| 18 | Output Relevance | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Output Relevance | Details are displayed in the Maintain Business Rules section. |  |
| 19 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTRelevance Indicator: X (True) | The Confirm Activation dialog box is displayed. |  |
| 20 | Activate | Choose Yes. | Rules are activated. |  |

#### Add Fields to Items (Optional)

Use

The administrator can optionally add data source extensions and field names to Manage Supplier Line Items (F0712). This option allows making more user fields available when managing items.

Prerequisite

Extensibility should only be tested in extensibility systems. Contact your system administrator to check if your system is enabled for extensibility for the Custom Fields (F1481) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Custom Fields (F1481). |  |  |
| 3 | Create New Extension | Choose the Data Source Extensions tab. |  |  |
| 4 | Create New Extension | Choose + (Create). | The New Data Source Extension dialog box displays. |  |
| 5 | Enter Properties | Make the following entries and choose Create:Data Source: Supplier Line ItemsDescription: <description of the data source>Extension ID: The description is automatically added to the ID | A view displays of the new data source extension. |  |
| 6 | Add Fields | Choose the <> Toggle Field Path button to switch the Field Path to show Item at the top of the table. Expand the Item > _Supplier node until you find the items you want to add. To add them, select the Selected checkbox next to the field to add.Note Ensure that your choices are under the _Supplier node. | Selected items display in the Selected Fields column. |  |
| 7 | Save | Choose Save. | All the nodes of the Field Path table collapse and your selections display in the Selected Fields table. |  |
| 8 | Publish | Choose Publish. | The Data Source Extensions view of Custom Fields and Logic displays with all of the extensions. To verify your new extension, use the Search field. |  |

#### Maintain Business Users

Purpose

In this activity, you assign business roles to a business user:

1. Assign SAP_BR_MANAGER to use and display the My Inbox - All Items (F0862) app.
2. Assign SAP_BR_AP_ACCOUNTANT to:
    - Display the journal entry details in My Inbox
    - Access the Verify Supplier Down Payment Requests (F7103), Verify Supplier Down Payment Requests - Approver Inbox (F7102), and Verify Supplier Down Payment Requests - Approver Outbox (F7101) apps

Prerequisite

You created business users.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Users (F1303). | The Maintain Business Users view displays. |  |
| 3 | Search | Make the following entries and choose Go :User Name: AP_MANAGER | Your selection is displayed. |  |
| 4 | Select | Choose the displayed entry. | Details of the user are displayed. |  |
| 5 | Person ID | In the General > Personal Data section, make a note of the Person ID. This value is used later in the Create Team process steps (Team Owners and Team Members rows). |  |  |
| 6 | Assign | In the Assigned Business Roles section, choose Add. |  |  |
| 7 | Assign | Search for and select SAP_BR_MANAGER and choose Apply.Search for and select SAP_BR_AP_ACCOUNTANT and choose OK. |  |  |
| 8 | Save | Choose Save. | The business roles are assigned and saved. |  |

#### Business Partner Certificates

##### Activate Business Partner Certificates Functionality

Purpose

In this activity, you activate the business partner certificate functionality for the FI supplier and customer roles.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Database and Data Management

Sub Application Area: Business Partner

1. For the row with Item Name of General Settings, choose Details (>).
2. For the Activate Business Partner Certificates Functionality row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Activate Business Partner Certificates Functionality.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and choose Save:BP Role: <enter the relevant role>Note For Accounts Payable, select FI Supplier. For Accounts Receivable, select FI Customer.Active: Selected |  |  |

##### Define Business Partner Certificate IDs

Purpose

In this activity, you define the business partner certificate IDs and descriptions for different types of certificates for your business partners. You use these certificate IDs to maintain certificate details for your business partners in the business partner master data. You also use them to define business partner-relevant processes based on the business requirements in a country/region.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Database and Data Management

Sub Application Area: Business Partner

1. For the row with Item Name of General Settings, choose Details (>).
2. For the Define Business Partner Certificates IDs row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Business Partner Certificates IDs.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and choose Save:Certificate ID: <certificate ID>Certificate Desc.: <certificate description> |  |  |

##### Assign Business Partner Certificates to Country/Region

Purpose

In this activity, you assign business partner certificate IDs to different countries/regions, and specify whether the certificate IDs are mandatory, require an attachment, and their default validity.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Database and Data Management

Sub Application Area: Business Partner

1. For the row with Item Name of General Settings, choose Details (>).
2. For the Assign Business Partner Certificates to Country row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Business Partner Certificates to Country.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and choose Save:C/R: <country/region>Cert.ID: <certificate ID from prior topic>Certificate Description: <description>Mandatory: <select the appropriate value>Attachment: <select if attachments are required>Valid For: <certificate validity period>Time Unit: <unit for validity> |  |  |

## Overview Table

The Accounts Payable scenario consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Preparation of Payments

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Business Partner](#unique_20) [page ] 44 | Accounts Payable Accountant | Maintain Business Partner (BP) | The Business Partner is maintained. |
| [Maintain Business Partner Certificate](#unique_21) [page ] 46 | Accounts Payable Accountant or Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | You maintained certificate data for the supplier. |
| [Display Supplier List](#unique_22) [page ] 47 | Accounts Payable Accountant | Display Supplier List (F1861) | The Supplier is displayed. |
| [Netting of AR/AP Items (Optional)](#unique_23) [page ] 48 | Accounts Payable Accountant | Maintain Business Partner (BP) | The Business Partner is maintained. |
| [Available Amounts for Payment Program (Optional)](#unique_24) [page ] 50 | Accounts Payable Manager | Enter Available Amounts for Payment Program (S_ALR_87001486) | Available amounts are defined. |

Invoice Entry without Purchase Order

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Invoice Entry Without Purchase Order](#unique_25) [page ] 52 | Personalized User based on the SAP_BR_AP_ACCOUNTANTBusiness Role ID | Create Supplier Invoice (F0859) | The invoice is created. |
| [Invoice Entry for One-Time Supplier without Purchase Order](#unique_26) [page ] 54 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | The invoice is created. |
| [Park Invoice](#unique_27) [page ] 56 | Personalized User based on the SAP_BR_AP_ACCOUNTANTBusiness Role ID | Create Supplier Invoice (F0859) | Invoice is parked. |
| [Post Invoice](#unique_28) [page ] 58 | Personalized User based on the SAP_BR_AP_ACCOUNTANTBusiness Role ID | Supplier Invoices List (F1060A) | Invoice is posted. |

Recurring Supplier Invoices

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Recurring Supplier Invoice](#unique_29) [page ] 60 | Accounts Payable Accountant | Manage Recurring Supplier Invoices (F4312) | Recurring invoices are created. |
| [Review Recurring Supplier Invoice](#unique_30) [page ] 63 | Accounts Payable Accountant | Manage Recurring Supplier Invoices (F4312) | Recurring invoices are reviewed. |
| [Schedule Recurring Supplier Invoice Posting](#unique_31) [page ] 64 | Accounts Payable Accountant | Schedule Accounts Payable Jobs (F2257) | A background job is created. |

Mass Upload

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Mass Import for Supplier Invoices](#unique_32) [page ] 66 | Accounts Payable Accountant | Import Supplier Invoices (F3041) | Invoices are imported and posted. |

Invoice Payment Preparation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [View Supplier Line Items](#unique_33) [page ] 69 | Accounts Payable Accountant | Manage Supplier Line Items (F0712) | Supplier open items are displayed |
| [Manage Payment Blocks](#unique_34) [page ] 71 | Accounts Payable Accountant | Manage Payment Blocks (F0593A) | You reviewed blocked invoices and items. Relevant items are unblocked or reblocked with reasons. |
| [View Supplier Balance](#unique_35) [page ] 72 | Accounts Payable Accountant | Display Supplier Balances (F0701A) | Supplier Balance is displayed. |

Payment Run

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Payment Proposals](#unique_36) [page ] 74 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | Invoices to be paid are proposed. |
| [Revise Payment Proposal](#unique_37) [page ] 76 | Accounts Payable Accountant | Revise Payment Proposals (F0771) | You reviewed and revised the proposals. |
| [Release Payment Proposal](#unique_38) [page ] 77 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | Payments are processed. |
| [Mass Reverse Payment Run (Optional)](#unique_39) [page ] 79 | Accounts Payable Accountant | Schedule Accounts Payable Jobs (F2257) | The payment run is reversed. |
| [View Payment List](#unique_40) [page ] 80 | Accounts Payable Accountant | Display Payment Lists (S_P99_41000099) | You viewed the payment list. |

Payment Plans

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Payment Plans](#unique_41) [page ] 81 | Accounts Payable Accountant | Manage Payment Plans (F4806)Schedule Accounts Payable Jobs (F2257) | You created a job and executed the payment run. |

Single Outgoing Payment

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Single Outgoing Payment (Indirect)](#unique_42) [page ] 84 | Accounts Payable Accountant | Manage Supplier Line Items (F0712) | Single outgoing payment is generated. |

Online Payments

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Free Form Payment Request](#unique_43) [page ] 86 | Accounts Payable Accountant | My Free Form Payments (F2564) | The request is created. |
| [Review or Edit Free Form Payment Request](#unique_44) [page ] 87 | Cash Management Specialist | Process Free Form Payments (F8654) | The request is posted. |
| [Process Free Form Payment](#unique_45) [page ] 88 | Cash Management Specialist | Process Free Form Payments (F8654) | The request is released. |

Manual Payment Online

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Outgoing Payment](#unique_46) [page ] 90 | Accounts Payable Accountant | Post Outgoing Payments (F1612) | Outgoing payments are posted. |

Payment Approval

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Bank Payment Approval (Optional based on Cash Management)](#unique_47) [page ] 92 | See Basic Cash Operations (BFB) |  | Payment released |
| [Approval by First Approver](#unique_48) [page ] 93 | Accounts Payable Manager | Approve Bank Payments (F0673A) | The Approve Bank Payments app displays. |
| [Rejection](#unique_49) [page ] 94 | See the Advanced Cash Operations (J78) test script | See the Advanced Cash Operations (J78) test script |  |
| [Approval by Second Approver](#unique_50) [page ] 95 | Cash Manager | Approve Bank Payments (F0673A) | The Approve Bank Payments app displays. |

Create Payment Media

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Payment Media](#unique_51) [page ] 96 |  | See the Advanced Cash Operations (J78) test script for more information. The batch item status should be Payment Medium Created. |  |
| [Manual Creation of Payment Media](#unique_52) [page ] 97 | Accounts Payable Accountant | Create Payment Media - for Payment Runs (F7711) | You manually created the payment media. |
| [Manual Deletion of Payment Media](#unique_53) [page ] 99 | Accounts Payable Accountant | Create Payment Media - for Payment Runs (F7711) | You manually deleted the payment media. |

Payment Advice

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Print or Email Payment Advice](#unique_54) [page ] 100 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | Payment advice is generated and an email is sent. |
| [Schedule Payment Advices (Optional)](#unique_55) [page ] 102 | Accounts Payable Accountant | Schedule Accounts Payable Jobs (F2257) | You scheduled the job. |

Correspondence

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Correspondence](#unique_56) [page ] 103 | Accounts Payable Accountant | Create Correspondence (F0744A) / Manage Journal Entries (F0717A) | You created correspondence. |

Incorrect Posting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Reset Cleared Items](#unique_57) [page ] 107 | Accounts Payable Accountant | Reset Cleared Items (F2223) | The document is reset. |
| [Reset and Reverse Cleared Items](#unique_58) [page ] 108 | Accounts Payable Accountant | Reset Cleared Items (F2223) | The document is reset and reversed. |
| [Schedule Jobs to Reset Cleared Items (Optional)](#unique_59) [page ] 109 | Accounts Payable Accountant | Schedule Jobs to Reset Cleared Items (F9296) | You scheduled jobs to reset cleared items. |

Down Payments

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Down Payment Request](#unique_60) [page ] 111 | Accounts Payable Accountant | Manage Supplier Down Payment Requests (F1688) | A down payment request is posted. |
| [Create Team](#unique_61) [page ] 113 | Accounts Payable Manager | Manage Teams and Responsibilities - Supplier Down Payment Requests (F7483) | You created a team. |
| [Create Workflow](#unique_62) [page ] 114 | Accounts Payable Manager | Manage Workflows - Supplier Down Payment Requests (F7100) | You created a workflow. |
| [Create Supplier Down Payment Request for Approval](#unique_63) [page ] 116 | Accounts Payable Accountant | Verify Supplier Down Payment Requests (F7103) | You created a supplier down payment request. |
| [Review Down Payment Request](#unique_64) [page ] 118 | Accounts Payable Manager | Verify Supplier Down Payment Requests - Approver Inbox (F7102) or My Inbox - All Items (F0862) | You reviewed the down payment request. |
| [Process Down Payment Request Approval](#unique_65) [page ] 119 | Accounts Payable Manager | Verify Supplier Down Payment Requests - Approver Inbox (F7102) or My Inbox - All Items (F0862) | You approved the down payment request. |
| [Invoice Entry](#unique_66) [page ] 124 |  |  | The invoice amount should be larger than the down payment amount posted in previous step. |
| [Post Outgoing Payment](#unique_67) [page ] 125 | Accounts Payable Accountant | Post Outgoing Payments (F1612) | You posted an outgoing payment. |
| [Clear Open Items](#unique_68) [page ] 126 | Accounts Payable Accountant | Clear Outgoing Payments - Manual Clearing (F1367) | You cleared invoices and down payments. |

Optional: Interest Calculation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Optional: Schedule Interest Calculation Jobs](#unique_69) [page ] 128 | Accounts Payable Accountant | Schedule Interest Calculation Jobs (F4176) |  |
| [Optional: Manage Interest Runs](#unique_70) [page ] 130 | Accounts Payable Accountant | Manage Interest Runs (F4485) |  |
| [Optional: Display Interest Runs](#unique_71) [page ] 131 | Accounts Payable Accountant | Manage Interest Runs (F4485) |  |

Guarantees Received

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Guarantees Received](#unique_72) [page ] 132 | Accounts Payable Accountant | Manage Guarantees Received (F7933) | You created a guarantee. |
| [Reverse Guarantees](#unique_73) [page ] 133 | Accounts Payable Accountant | Manage Guarantees Received (F7933) | You reversed a guarantee. |

Periodic Activities

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Check Open Balances](#unique_74) [page ] 134 |  | Follow the instructions in the [View Supplier Line Items](#unique_33) [page ] 69 test procedure. |  |
| [Create Supplier Balance Confirmation](#unique_75) [page ] 134 | Accounts Payable Accountant | Schedule Accounts Payable Jobs (F2257) | The Balance confirmation is managed. |
| [Manage Supplier Balance Confirmations](#unique_76) [page ] 136 | Accounts Payable Accountant | Manage Balance Confirmations - For Suppliers (F2959) | The Supplier Balance confirmation is managed. |
| [Print Supplier Balance Confirmation](#unique_77) [page ] 137 | Accounts Payable Accountant | Manage Balance Confirmations - For Suppliers (F2959) | The Balance confirmation is generated. |

Invoice Management Reporting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Accounts Payable Overview](#unique_78) [page ] 138 | Accounts Payable Manager | Accounts Payable Overview (F2917) | The Accounts Payable Overview is generated. |
| [Days Payable Outstanding](#unique_79) [page ] 140 | Accounts Payable Manager | Days Payable Outstanding - Last 12 Months (F1740) | You reviewed the days payable outstanding. |
| [Overdue Payables](#unique_80) [page ] 141 | Accounts Payable Manager | Overdue Payables - Today (F1746) | You listed Overdue Payables. |
| [Future Payables](#unique_81) [page ] 142 | Accounts Payable Manager | Future Payables - Today (F1743) | You listed Future Payables. |
| [Cash Discount Forecast](#unique_82) [page ] 142 | Accounts Payable Manager | Cash Discount Forecast - Available Amount (F1735) | You reviewed potential discount opportunities. |
| [Cash Discount Utilization](#unique_83) [page ] 143 | Accounts Payable Manager | Cash Discount Utilization - Today (F1736) | You reviewed discount utilization. |
| [Invoice Processing Analysis](#unique_84) [page ] 144 | Accounts Payable Manager | Invoice Processing Analysis - Today (F1745) | You analyzed invoice processing throughput and bottlenecks. |
| [Invoice Processing Time](#unique_85) [page ] 145 | Accounts Payable Manager | Invoice Processing Time - Today (F1745) | You viewed the invoice processing analysis report. |
| [Aging Analysis](#unique_86) [page ] 146 | Accounts Payable Manager | Aging Analysis - Payable Amount (F1733) | You reviewed payables aging. |
| [Aging Report for Accounts Payable](#unique_87) [page ] 146 | Accounts Payable Manager | Aging Report for Accounts Payable (F4401) | You viewed the aging report. |
| [Automatic and Manual Payments Analysis](#unique_88) [page ] 147 | Accounts Payable Manager | Automatic and Manual Payments - Payments for Last Year (F1749) | You analyzed automatic and manual payments. |
| [Supplier Payments Analysis](#unique_89) [page ] 148 | Accounts Payable Manager | Supplier Payment Analysis - Open Payments (F1750) | You analyzed open or unapplied supplier payments. |
| [Display Item Change Log](#unique_90) [page ] 149 | Accounts Payable Manager | Display Item Change Log - Supplier (F7795) | The logged changes for journal entries are displayed. |

Vendor Certificate Validity Check

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Vendor Certificate Validity Check](#unique_91) [page ] 150 | Accounts Payable Accountant or a Master Data Specialist - Business Partner Data | Check Supplier Certificate Validity - United Arab Emirates | Vendor certificate is validated. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Preparation of Payments

#### Maintain Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Vendor master records are used by both the Accounting component and the Purchasing component.

Prerequisite

The supplier master record has been entered, but some specific information, for example the payment method, is missing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Select Supplier | Make the following entry and choose Start:Business Partner: 33300001 | The partner is displayed in the pane in the lower part of the view. |  |
| 4 | Select Partner | Select the partner in the lower pane and double-click the business partner. | The Display Organization:33300001 view displays. |  |
| 5 | Change BP role | Enter the following values:Display in BP role: Supplier (Fin.Accounting) | The Display Organization:33300001, role Supplier (Fin. Accounting) view displays. |  |
| 6 | Edit Supplier | Choose the Switch between Display and Change button to change the data to update. | The Business Partner Master Data can now be edited. |  |
| 7 | Company Code Data | Choose the Company Code button.Choose the Supplier: Account Management tab.Make the following entries:Interest Indicator: 01Choose the Supplier: Correspondence tab. |  |  |
| 8 | Enter Accounting Clerk | In the Correspondence section, make the following entries:Clerk Abbrev.: <Choose any available>Clrks Internet add.: <email address> | The accounting clerk is changed. |  |
| 9 | Save | Choose Save. | Changes are saved. |  |
| 10 | Payment Methods | Choose the Supplier: Payment Transactions tab. |  |  |
| 11 | Payment Methods | In the Automatic Payment Transactions section, select one or more of the following Payment Methods:T | You've chosen payment methods. |  |
| 12 | Save | Choose Save. | Changes are saved. |  |
| 13 | Navigation | To change or display other master data settings, change the BP role and navigate through the available tabs as follows:Display in BP role: For example, Business Partner (Gen.) or Supplier | Settings for the selected BP role display and can be edited. |  |
| 14 | Save Supplier | Choose the Save button after completing your changes. | The changes to Business Partner Master Data are saved. |  |

#### Maintain Business Partner Certificate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Companies doing business in your country/region must have a certificate issued by the legal authorities. The Business Partner Certificates functionality enables you to maintain the certificate details of your business partner (customer and supplier) in new tabs and information about the certificate's validity. You can use these certificate details in your business processes, such as invoicing and payments.

Prerequisites

Ensure that you've completed the following preliminary steps:

- [Activate Business Partner Certificates Functionality](#unique_16) [page ] 32
- [Define Business Partner Certificate IDs](#unique_17) [page ] 33
- [Assign Business Partner Certificates to Country/Region](#unique_18) [page ] 34

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant or a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). |  |  |
| 3 | Select Supplier | Choose Open BP, then make the following entry and press Enter:Business Partner: 33300001 | The Display Organization: 33300001 view is displayed. |  |
| 4 | Change BP Role | Enter the following values:Display in BP role: Supplier (Fin. Accounting) | The Display Organization: 33300001 role Supplier (Fin. Accounting) view is displayed. |  |
| 5 | Edit Supplier | Choose the Switch between Display and Change button to change the data and update. | The Business Partner Master Data is available for editing. |  |
| 6 | Certificate | Choose the Certificates tab.Note This tab is only visible if you're activating business partner certificates for the FI Supplier business partner role. |  |  |
| 7 | Add Certificate | Choose Insert Row. Make the following entries:Country/Region: <your two-character country code>Certificate ID: <certificate ID>Certificate No.: <certificate number>Valid From: <start date for certificate validity>Valid To: <end date for certificate validity>Region: <region>Main Certificate: Selected | The business partner certificate is added to supplier 33300001. |  |
| 9 | Save | Choose Save | Changes are saved. The certificate status changes to Active. |  |

#### Display Supplier List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The supplier list lets you search by company code, city, country, bank key, posting block, and deletion flag. It shows suppliers with additional details like bank key, bank account, payment methods, posting block or deletion flag. You can choose a supplier from the displayed list and drill down to the fact sheet of the supplier.

Prerequisite

Supplier master data is maintained for the company code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Supplier List (F1861). |  |  |
| 3 | Company Code | Make the following entries and choose Go:Company code: 3310Note If the field is not visible, choose Adapt Filters. Select the necessary filters and choose Go. | A dropdown list of suppliers for company code 3310 displays. |  |
| 4 | Supplier Number | In the Supplier column, choose a supplier number. | A dialog box displays. |  |
| 5 | Supplier Number | On the top of the dialog box, choose the supplier number. | The system displays a fact sheet on the supplier with information such as general information, contact numbers, minimum order value for purchasing organizations, materials, purchase order, invoices, purchase contract, activities, and evaluations. |  |

#### Netting of AR/AP Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you set up a Business Partner (BP) for netting of Account Receivable (AR) and Account Payable (AP) items within one company code.

When you perform a payment run for a business partner set up for netting, the payment amount is the net amount of its open past due AR and AP items.

|  |
| --- |
| Note This task is optional because the created business partner must have the supplier as a customer. Our solution content doesn't deliver any business partners created as supplier and customer, so to perform this activity, you must manually create the Business Partner master records. |

Prerequisite

The supplier master record has been created.

The customer master record has been created.

Supplier and Customer have the same number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Select Supplier | Choose Open BP.Make the following entry:Business Partner: any BP created as supplier and customerand choose Enter. | The Display Organization:Business Partner # view displays. |  |
| 4 | Change BP role Supplier | Enter the following values:Display in BP role: Supplier (Fin.Accounting) | The Display Organization:Business Partner #, role Supplier (Fin.Accounting) view displays. |  |
| 5 | Edit Supplier | Choose the Switch between Display and Change button to change the data to update. | The Business Partner Master Data can now be edited. |  |
| 6 | General Data | Choose the Vendor: General Data tab and in General Data section make the following entry:Customer: <Customer Number> (number is the same as the supplier). |  |  |
| 7 | Company Code Data | Choose the Company Code button. |  |  |
| 8 | Payments Vendor | Choose the Vendor: Payment Transactions tab. | You're on the Vendor: Payment Transactions tab. |  |
| 9 | Clearing Vendor | In the Automatic Payment Transactions section, select:Clearing w. customer: Selected | Clearing is activated. |  |
| 10 | Save | Choose Save and if warning is displayed, ignore it by choosing No. | Changes are saved. |  |
| 11 | Change BP role Customer | Enter the following values:Display in BP role: Customer (Fin.Accounting) |  |  |
| 12 | General Data | Choose the Customer: General Data tab. |  |  |
| 13 | General Data | In the General Data section, make the following entries:Supplier: <supplier number>Note The supplier number is the same as the customer number. |  |  |
| 14 | Company Code | Choose the Company Code button. |  |  |
| 15 | Payments Customer | Choose the Customer: Payment Transactions tab. | You're on the Customer: Payment Transactions tab. |  |
| 16 | Clearing Customer | In the Automatic Payment Transactions section, select:Clearing w. Vendor: Selected | Clearing has been activated. |  |
| 17 | Save | Choose Save. | Changes are saved. |  |

#### Available Amounts for Payment Program (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The payment program checks whether the selected bank accounts have sufficient funds for payments. For accounts at house banks, you can set available amounts separately for incoming and outgoing payments. For outgoing payments, set the maximum amount that can be paid. For incoming payments, set the limit up to which payments can be received into a bank account. If a payment exceeds this limit, the program selects another bank. The available amounts you set determine which bank account processes the payment. Make sure to update these amounts before each payment run.

The payment program doesn't split payment amounts. If a bank account lacks sufficient funds for a payment, the program selects another account. If no bank account has enough funds to cover the entire payment, the payment is not made.

Prerequisite

Two sample bank accounts are created in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Enter Available Amounts for Payment Program (S_ALR_87001486). | The Determine Work Area: Entry dialog box displays. |  |
| 3 | Company Code | Enter the following and choose Continue (Enter):Company Code: <Any company code> | The Change View “Available Amounts for Payment Program”: Overview view is displayed. |  |
| 4 | New Entries | Choose New Entries. | The New Entries: Overview of Added Entries view is displayed. |  |
| 5 | House Banks and Account IDs | For each of the House Banks and Accounts IDs to be defined, enter the following and choose Save:House Bank: <Any House Bank>Account ID: <Any Account ID>Days: <Any>Currency: <Any>Available for outgoing payment: <Any Amount>Scheduled incoming payment: Don’t change |  |  |
| 6 | Delete | To delete a row, select the checkbox for the row to delete and choose Delete. In the dialog box, choose Continue. | The row is deleted. |  |
| 7 | Save | Choose Save. | The entry is deleted and the change is saved. |  |

### Invoice Entry without Purchase Order

#### Invoice Entry Without Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter a supplier invoice without reference to a purchase order. Payment is made in local currency or you can pay invoices in foreign currency. For example, for a German company, you can pay invoices in USD, and for the U.S., you can pay invoices in EUR.

|  |
| --- |
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_93) [page ] 157 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using a personalized user.Note Don't use the generic Accounts Payable Accountant user. Create a personalized user based on the business role IDSAP_BR_AP_ACCOUNTANT. |  |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The Manage Supplier Invoices (F0859) view displays. |  |
| 3 | Dialog Box | If the Data from Previous Invoice Entry Exist dialog box displays, choose No. |  |  |
| 4 | General Information | In the Basic Data section, enter the following data:Transaction: InvoiceInvoicing Party: <supplier>Company Code: 3310Gross Invoice Amount: 1000Note If the entry is tax relevant, change the amount according to the tax rate from step 6.Currency: For example, AEDInvoice Date: <Today's date>Posting Date: <Today's date>Reference: <any>Business Place: DXBNote After choosing the selection box, enter the company code, 3310, and choose Go. Then select the business place. |  |  |
| 5 | G/L Account Items | In the G/L Account Items section, choose Add.Make the following entries:Debit/Credit: DebitG/L Account: For example,61061000Amount 1000Item text: <any text> |  |  |
| 6 | Account Assignment | In the G/L Account Items, choose Add. Choose Show Details to expand the selection.Make the following entries:Cost Center: <Any cost center>If the General Ledger account is tax relevant, in the Tax section, enter Tax Date and any other mandatory fields.Payment section:Tax Date: <enter today's date>Note The Tax Date field is only visible in countries/regions where it is needed. |  |  |
| 7 | Post | Choose Post.Note The supplier invoice number generated is a logistics document number. To find or review the finance document number (Journal Entry), see the Invoice Payment Preparation > View Supplier Line Items task. | The Success dialog box displays, showing the document numbers created. |  |
| 8 | Exit | Choose No. |  |  |

#### Invoice Entry for One-Time Supplier without Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an invoice without purchase order for a one-time supplier.

Prerequisite

Business partner master data for a one-time supplier already exists.

The payment method for a one-time supplier is maintained in business partner master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice - Advanced (MIRO). |  |  |
| 3 | Navigation | If the system prompts you, make the following entries and choose Continue:Company Code: 3310 | The Enter Incoming Invoice screen is displayed. |  |
| 4 | Basic Data | On the Basic Data tab, enter the following data:Invoice Date: Today's datePosting Date: Today's dateReference: anyAmount: 1000Currency: AEDCalculate Tax: SelectedTax Code: <Input Tax Code>Note If you enter a G/L account that is subject to tax, ensure that you enter an appropriate tax code. |  |  |
| 5 | Payment | In the Payment tab, enter the following data:BaselineDt: Today's datePyt Terms: 0001 |  |  |
| 6 | Details | In the Details tab, enter the following data:Inv. Party: 33300273 |  |  |
| 7 | G/L Account Items | In the G/L Account section, make the following entries and press Enter:G/L Account: 65100000Amount in doc.curr.: 1000Cost Center: 33101201 |  |  |
| 8 | Post | Choose the Post button. | The Address and Bank Data dialog box is displayed. |  |
| 9 | Address and Bank Data | Enter the address and bank information and choose Continue:Street: anyPO Box : <post box number>PO Box Postal Code : <postal code>Note For your country, the field validations for the address data may be different. Keep this in mind when entering address data. | The Information dialog box displays the new document number. |  |
| 10 | Exit | Choose Exit. |  |  |

#### Park and Post Invoice

##### Park Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, an invoice is parked.

Prerequisite

A personalized business user has been created based on the business role ID: SAP_BR_AP_ACCOUNTANT

Assign the following business catalog to your personalized business user:

| Business Catalog | Business Catalog ID |
| --- | --- |
| Accounts Payable - Supplier Invoice Parking | SAP_MM_BC_INV_PARK_PC |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using a personalized user. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The Manage Supplier Invoices (F0859) view displays. |  |
| 3 | Park | Follow the steps described in previous Invoice Entry without Purchase Order procedure, except at test step Post, choose the Park button.Tip When using approval workflow with this procedure, the Consumable Purchasing (BNX) test script provides additional information and procedures that you must execute. Follow the preliminary steps described in Activate Flexible Workflow for Supplier Invoice and then use the Create Supplier Invoice procedure for reference. | The document is parked. |  |

Create new business catalog and assign to business user (OPTIONAL)

The following procedure is optional if all prerequisites are met.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Roles (F1492). |  |  |
| 3 | New | Choose New.In the New Business Role dialog box, make the following entries and choose Create:Business Role Description: Accounts Payable ParkBusiness Role ID: AP_PARKChoose Assigned Business Catalogs, and choose Add. Select the following entries and choose OK:Business Catalog: Accounts Payable - Supplier Invoice ParkingBusiness Catalog ID: SAP_MM_BC_INV_PARK_PCChoose Maintain Restrictions.Choose Write, Read, Value Help.In the dropdown, select Unrestricted.Choose Read, Value Help.In the dropdown, select Unrestricted.Choose Back. |  |  |
| 4 | Save | Choose Save. |  |  |
| 5 | Assign | Choose Edit.Choose Assigned Business Users and choose Add, then select your personalized <User Name> and choose Ok. |  |  |
| 6 | Save | Choose Save. |  |  |

##### Post Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, an invoice is posted.

Prerequisite

Create a personalized business user based on the business role ID: SAP_BR_AP_ACCOUNTANT

Assign the following business catalog to the personalized business user:

| Business Catalog | Business Catalog ID |
| --- | --- |
| Accounts Payable - Supplier Invoices | SAP_MM_BC_INV_PROCESS_PC |

An invoice has been parked.

Procedure: Post Invoice

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using a personalized user. |  |  |
| 2 | Access the SAP Fiori App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List (Version 2) (F1060A) view displays. |  |
| 3 | Search | Choose Go or enter a selection criteria before executing the search, for example:Invoicing Party: <any>Status: ParkedCompany Code: <any> | List of invoices display. |  |
| 4 | Select | Choose any document with status Parked by selecting the row. | The Supplier Invoice view displays. |  |
| 5 | Edit | Choose Edit to change any available fields as needed. |  |  |
| 6 | Post | Choose Post. | Document is posted. |  |

Create new business catalog and assign to business user (OPTIONAL)

The following procedure is optional if all prerequisites are met.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Roles (F1492). |  |  |
| 3 | New | Choose New and make the following entries:Business Role Description: Accounts Payable PostBusiness Role ID: AP_POSTChoose Assigned Business Catalogs and choose Add . Select the following entries and then choose Ok:Business Catalog: Accounts Payable - Supplier InvoicesBusiness Catalog ID: SAP_MM_BC_INV_PROCESS_PCChoose Maintain Restrictions.Choose Write, Read, Value Help.In the dropdown, select Unrestricted.Choose Read, Value Help.In the dropdown, select Unrestricted.Choose Back. |  |  |
| 4 | Activate | Choose Save. |  |  |
| 5 | Assign | Choose Edit.Choose Assigned Business Users, and choose Add, then select your personalized User Name and choose OK. |  |  |
| 6 | Activate | Choose Save. |  |  |

### Recurring Supplier Invoices

#### Create Recurring Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a recurring invoice, which is a type of invoicing where a supplier or merchant automatically charges a customer for goods or services at regular intervals.

|  |
| --- |
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_93) [page ] 157 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

Prerequisites

You executed procedures to create a recurring supplier invoice.

Business conditions are met.

Posting periods are open.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Recurring Supplier Invoices (F4312). | The Manage Recurring Supplier Invoices (F4312) view is displayed. |  |
| 3 | Create | Choose Create. |  |  |
| 4 | General Information | In the Basic Data section, enter the following data:Document Type: KRCompany Code: 3310Gross Invoice Amount: <gross invoice amount>Note If entry is tax relevant change the amount according to the tax rate from step 6.Currency: For example, AEDReference: <any>Invoicing Party: 33300001Recurrence Start Date: <Today’s date>Currency conversion Rule: For example, Use current exchange rate |  |  |
| 5 | G/L Account Items | In the G/L Account Item section, choose Create and make the following entries:Debit/Credit: DebitG/L Account: <account>, for example, 61400000Item Amount: 100 |  |  |
| 6 | More Details | In the G/L Account Items section, choose > to display more details.Make the following entries and choose Apply:Tax Code: <Input Tax Code>Cost Center: <Any cost center> |  |  |
| 7 | Payment | In the Payment section, make the following entries:Terms of Payment: 0001 |  |  |
| 8 | Recurrence | In the Recurrence section, make the following entries:Recurrence Pattern: For example, MonthlyInterval in Months: 1Occur Day in a Month: 1stEnd Recurrence By: End dateEnd Date: <Today’s date + 3 months> |  |  |
| 9 | Create | Choose Create. | The Manage Recurring Supplier Invoices view is displayed.A Posting Forecast is displayed in the Postings section. |  |
| 10 | Execute | Choose Execute. Make the following entries:Up to Date: <End of Month date>Note The supplier invoice number generated is a logistics document number. To find or review the finance document number (Journal Entry), see the [View Supplier Line Items](#unique_33) [page ] 69 task. | The Execute Recurrent Posting dialog box is displayed. |  |
| 11 | Execute Until Date | Make the following entries and choose Execute:Up to date: <end of month date> |  |  |
| 12 | Copy | Once you create and post the recurring supplier invoice, you can copy it.Return to the initial view of this app. Select a posted recurring document and choose Copy. Modify any fields in the copied invoice and choose Create. | You created a new recurring supplier invoice. |  |

#### Review Recurring Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can review, edit, and execute an existing recurring supplier invoice.

Prerequisites

You created a recurring supplier invoice.

Business Conditions are met. Posting periods are open.

|  |
| --- |
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_93) [page ] 157 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Recurring Supplier Invoices (F4312). | The Manage Recurring Supplier Invoice view is displayed. |  |
| 3 | Search | In the search criteria fields, make the following entries and choose Go:Company Code: 3310Invoicing Party: 33300001 | A list of recurring supplier invoices is displayed according to your search criteria. The Posting Status column shows how many recurring invoices have been posted. |  |
| 4 | Execute | For unposted invoices, select the checkbox for a document and choose Execute. | A dialog box is displayed. |  |
| 5 | Enter Data | Make the following entries and choose Execute:Up to Date: <End of Month date>Note A dialog box may appear after execution. Review the message and close the dialog box. | A document number is generated. |  |
| 6 | Details | Select a document and choose Navigation (>). |  |  |
| 7 | Edit | Choose Edit to make changes to unposted documents. For posted documents, you can only edit the end date or recurrence.Once you're done with your changes, choose Save. |  |  |

#### Schedule Recurring Supplier Invoice Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job for a recurring supplier invoice.

Prerequisites

You've created a recurring supplier invoice.

Business Conditions are met. Posting periods are open.

|  |
| --- |
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_93) [page ] 157 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accounts Payable Jobs (F2257). | The Application Jobs view is displayed. |  |
| 3 | Create Job | Choose Create. |  |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Schedule Automatic Posting for Recurring Supplier InvoiceJob Name: Schedule Automatic Posting for Recurring Supplier Invoice |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: SelectRecurrence Pattern: Single RunNote Choose Define Recurrence Pattern to schedule a regular pattern run. Depending on the chosen pattern, different options become available to populate. |  |  |
| 6 | Parameters | In the General Selection section, make the following entries:Company Code: 3310Document Number: <document number>Note Add any other entry to fine-tune the selection.In the Posting Parameters section, make the following entries:Due Date (Job Run Date /- X Days): <any number> |  |  |
| 7 | Check | Choose Check to verify that entries are complete and correct. |  |  |
| 8 | Schedule | Choose Schedule. | The job is scheduled. |  |

### Mass Upload

#### Mass Import for Supplier Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app is used when there are a large number of invoices arriving for the company, such as:

- Recurring invoices
- Posting of regular acquisitions
- Posting of travel expenses

|  |
| --- |
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_93) [page ] 157 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

Prerequisite

Create an electronic spreadsheet with the invoice details to be uploaded (with a maximum of 500 items in a single file).

Business Partner (BP) master data exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant . |  |  |
| 2 | Access the SAP Fiori App | Open Import Supplier Invoices (F3041) | The Import Supplier Invoices (F3041) view displays. |  |
| 3 | Download | For Destination, select Local.Choose Download (Download Template) to download the spreadsheet template and choose:Template Language: For example, EnglishFormat: For example, *.xlsx, for MS Excel WorkbookChoose Download to continue. |  |  |
| 4 | Enter Details | Enter the following content into the template data sections:Note The template has hidden columns. If you don't see a field, unhide the columns as needed.Note Ensure that you use the correct date format in the template.Header data sectionInvoice ID: For example, 12345001Company Code (4): 3310Transaction (1): 1Invoicing Party (10): 33300001Reference (16): <any text with maximum number of 16 characters>Document Date: <Today's date MM/DD/YYYY>Posting Date: <Today's date MM/DD/YYYY>Document Type (2): KRDocument Header Text (25): <any text with maximum number of 25 characters>Currency: AEDGross Invoice Amount in Document Currency: 1050Business Place (4): DXBDate for Determining Tax Rates: <tax calculation dates> (Optional: Depends on country/region setting)G/L Account Items sectionAccount (10): For example, 63001000Item Text (50): <any text with maximum number of 50 characters>Debit/Credit (1) S=Debit, H=Credit: SAmount in Document Currency: For example, 1000Note The Gross Invoice Amount in Document Currency field may have a different value, depending on, where applicable, the chosen Tax Code.Tax Code (2): V2Cost Center (10): 33101201 |  |  |
| 5 | Upload | To upload a file, choose Browse and select the file to upload. | File is uploaded and the Worklist section displays Inv. Status Draft for items uploaded. |  |
| 6 | Check | Select the checkbox of the documents to be checked and choose Check. | Any items containing errors are identified in the Invoice Status column with red icons. Otherwise, a green flag icon displays for correct entries. |  |
| 7 | Review the Log | To view log, select the checkbox of the documents and choose Show Log. | Details of logs are displayed. |  |
| 8 | Correct any Errors | Select the item to review and correct any errors. | Supplier invoice application is displayed showing details of uploaded item.The Draft Status column changes to a green flag icon after correcting the error and returning to the worklist. |  |
| 9 | Correct any Errors in Supplier Invoice Application | If the supplier invoice application reveals any errors, correct those errors and return to the worklist. |  |  |
| 10 | Post | Select the checkboxes for the documents to post and choose Post.Tip To use approval workflow with this app, the Consumable Purchasing (BNX) test script provides additional information and procedures that must be executed. Follow the preliminary step described in Activate Flexible Workflow for Supplier Invoice and then use the Create Supplier Invoice procedure for reference. | Items are posted. |  |

### Invoice Payment Preparation

#### View Supplier Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, all Accounts Payable (AP) line items are listed and you can modify some fields of a document to be paid.

Prerequisite

AP invoices are available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Line Items (F0712). | The Manage Supplier Line Items (F0712) view displays. |  |
| 3 | Data Entry and Search | Make the following entries and choose Go:Supplier: <any>Company Code: 3310Status: Open ItemsOpen on Key Date: <Today's date>Item Type: Normal ItemsNote As an option, choose the Gear (Settings) button to add columns to the Items table when the Administrator has added new fields. For more information, see the [Add Fields to Items (Optional)](#unique_14) [page ] 29 preliminary step.If you add columns to the table, you can save the view as a variant. Additionally, you can use the additional fields as filters in Adapt Filters. | Supplier line items are displayed according to your search criteria. |  |
| 4 | Item details | Select a journal entry and choose Manage Journal Entry. | Document details are displayed. |  |
| 5 | Edit | Choose the Edit button. |  |  |
| 6 | Edit Line Items | Select a line item (for example, Posting View Item 000001) and change one or more of the following, as needed:Item TextPayment MethodHouse bankHouse Bank AccountBaseline DatePayment TermsAnd so on |  |  |
| 7 | Save | Choose Save.Choose Back. | Your changes are saved and maintained. |  |

#### Manage Payment Blocks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity reviews and releases blocked invoices as part of the logistics invoice verification process. You can block on the supplier level or open item level.

When an invoice is blocked, Financial Accounting can't pay the invoice. Invoices can be blocked either automatically or manually depending on the payment block reason and release in the configuration.

Prerequisite

A vendor invoice was blocked for payment either automatically when invoice was created or manually by editing the supplier line items using the Manage Supplier Line Items (F0712) SAP Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Payment Blocks (F0593A). |  |  |
| 3 | Search | Make the following entries and choose Go:Company Code: <company code> | A list of suppliers is displayed. |  |
| 4 | Select Supplier | For one of the suppliers, choose Details (>). | The right pane displays supplier details. |  |
| 5 | Block Supplier | Choose Block Supplier. | The Block Supplier dialog box is displayed. |  |
| 6 | Enter Details | Make the following entries and choose OK:Payment Block Reason: <reason for blocking>Note: <explanatory text for the blocking reason> | The Status field changes to Account Blocked. |  |
| 7 | Unblock Supplier | Choose Unblock Supplier. | The Status field changes to Unblocked. |  |
| 8 | Select Item | In the Open Items area, select an open item's checkbox and choose the Block Items button.Note You can also choose the Details (>) button at the end of the row and then choose the Block Items button in the new right pane. | The Block Items dialog box is displayed. |  |
| 9 | Block Item | Make the following entries and choose OK:Payment Block Reason: <reason for blocking>Note: <explanatory text for the blocking reason> | The Status field changes to Item Blocked. |  |
| 10 | Unblock Item | In the Open Items area, select an open item's checkbox and choose the Unblock Items button.Note You can also choose the Details (>) button at the end of the row and then choose the Unblock Items button in the new right pane. | The Status field changes to Unblocked. |  |

#### View Supplier Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the supplier balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Supplier Balances (F0701A). | The Display Supplier Balances (Version 2) (F0701A) view is displayed. |  |
| 3 | Data Entry and Search | Make the following entries and choose Go:Supplier: <Supplier>Company Code: 3310(mandatory)Fiscal Year: <Current Year> | Balances are displayed per period for your supplier. |  |
| 4 | View Balances | Choose any of the following tabs to see different views of the supplier balance:BalancesSpecial G/LCompare | Different views of supplier balances are displayed. |  |
| 5 | View Period | In any row, select an existing amount in the Debit, Credit, or Balance column. | The Manage Supplier Line Items view is displayed. |  |

### Payment Run

Purpose

This section describes posting payments using the automatic payment program.

Prerequisites

You executed the [Define Payment Medium Format Variants (Optional)](#unique_9) [page ] 12 procedure in Preliminary Steps.

If necessary, review and execute the [Available Amounts for Payment Program (Optional)](#unique_24) [page ] 50 procedure.

Invoices are posted and are open for payment. For more information, see the Manage Supplier Line Items (F0712) app (unblock the item to be paid for payment).

Payment methods are defined in the Maintain Business Partner procedure.

All prerequisites in [Business Conditions](#unique_6) [page ] 11 are met.

All the previous procedures described in the Invoice Payment Preparation section are executed.

#### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity selects the invoices to be paid.

Prerequisite

The [Define Payment Medium Format Variants (Optional)](#unique_9) [page ] 12 procedure in the [Prerequisites](#unique_2) [page ] 7 section has been executed.

Review and execute (if necessary), the [Available Amounts for Payment Program (Optional)](#unique_24) [page ] 50 procedure.

The BRF+ Settings procedures, described in the Preliminary Steps topic, under Prerequisites are executed.

Invoices are posted, past due and are open for payment. For more information, see the Business Conditions section of this document.

Invoices are past due.

Use [Invoice Payment Preparation](#unique_33) procedures to change the payment terms or due date of an invoice so it can be paid.

All steps for the procedures in the [Invoice Payment Preparation](#unique_33) section must be executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). | The Manage Automatic Payments (F0770) view displays. |  |
| 3 | Create View | Choose Create Parameter. | The New Parameter dialog box is displayed. |  |
| 4 | Data Entry | Make the following entries and choose Create Parameter:Run Date: <today's date>Identification: <any five character description, such as SPAY1> | The Automatic Payment Parameters view is displayed. |  |
| 5 | Data Entry | Make the following entries:Basic section:Posting Date: <today's date>Docs entered up to: <today's date>Additional Log: ONPayment Controls section:Company Code: 3310Next payment date: <today's date + 5 days>Tip This is only recommended for testing purposes.If an invoice isn't overdue, but needs to be included in the payment run, choose a date that is after the invoice's due date.Payment method: for example, DOpen Item Selection section:Supplier: <supplier>Note For the Payment Method field, verify that the payment method is valid in the supplier master record.If it is necessary to post a down payment request, add a Free Selection and then enter the following:Special G/L ind. (BSEG-UMSKZ): F |  |  |
| 6 | Single Invoice (Optional) | To execute a payment for a single invoice, make the following entries in the Open Item Selection by populating any of the Free Selection # fields available:Document Number (BKPF-BELNR): <Document Number> |  |  |
| 7 | Save the Parameters | Choose Save. | The system displays the message Parameter has been saved. The status changes to Parameter Created. |  |
| 8 | Schedule Proposal | Choose Schedule > Proposal . | The Schedule Proposal dialog box is displayed. |  |
| 9 | Data Entry | Make the following entries and choose Schedule:Start Date: today's dateStart immediately: Select | The system displays the message Proposal has been scheduled.The status changes to Proposal Created. |  |
| 10 | View the Proposal | Choose the Proposal Processed tab. |  |  |
| 11 | Display | Choose the Go button. | The proposal is displayed in the list. |  |

#### Revise Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review invoices to be paid.

|  |
| --- |
| Caution Make sure that there are no other Payment Run Identification Proposals pending to be executed which might be using the same supplier as proposal created in previous step. If payment proposals exist, they must be processed or deleted, otherwise no payment proposal is generated for your proposal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Revise Payment Proposals (F0771) app. | The Revise Payment Proposals screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all proposals is displayed. |  |
| 4 | Select Identification | Choose Details (>) for the proposal you want to edit (for example, SPAY1 ). | The view Schedule Payment Proposal of the selected Identification is displayed. |  |
| 5 | Edit Payment (Optional) | In the Payments tab, select the rows to edit, and choose Edit Payment. | The Edit Payment dialog box is displayed. |  |
| 6 | Make Entries (Optional) | Change desired options and choose OK to continue.Payment method: <payment method>House Bank: <house bank>Account ID: <account>Payee Bank: <payee bank>Due Date: <date> |  |  |
| 7 | Payment List | Choose Export to PDF. | A new view displays the payment list. You can download or print the form from here. |  |
| 8 | Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You may unblock or reallocate and pay them by using the buttons in the view.Note A Sanctioned Party List screening happens if the Compliance Management with SAP Global Trade Services (24J) was activated. If the screening blocks a payment as a result of this SAP GTS check, contact your GTS team to take the proper actions. |  |  |

#### Release Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to release the payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Automatic Payments (F0770) app. | The Manage Automatic Payments screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all payment runs is displayed. |  |
| 4 | Proposal Processing | Choose the Proposal Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example, SPAY1 ) and choose Schedule Payment. | The Schedule Payment dialog box is displayed. |  |
| 6 | Schedule Payment | Make the following entries:Start Date: <Today's date>Start immediately: Selectand choose Schedule. | The system message Payment has been scheduled is displayed. The status changes to Payment Posted. The log shows how many postings or payments were generated. |  |
| 7 | View the payment | Choose the Payments Processed tab. | The status changes to Payment posted.Note If the status is Payment finished, review if the chosen documents can be paid (execute the steps starting with the Payment and Exceptions header. |  |
| 8 | View Log postings | Select the line of your payment run Identification and in the Log column, choose Log Details.Note If the Log column doesn't show, choose the Settings button. Select the Log field and choose OK. | The log shows how many postings were generated. |  |
| 9 | Close Dialog | Choose OK. | The Log Details dialog box closes. |  |
| 10 | Payments and Exceptions | Choose Details (>) . | The view displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You can sort the information by payment method, country/region, and so on. Select the view to display in the field below Summary. | Amounts are sorted by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions. | Details are displayed for payments or exceptions generated (such as payment document, payment order, included items, and so on). |  |
| 13 | Payment List | On the Payments tab, choose Export to PDF. | A view displays the payment list. From here, you can preview, print, or download the list. |  |
| 14 | Payments Navigation | On the Payments tab, for the desired item, choose Details (>).When you're done, choose Back at the top to exit this view. | Payment item details are displayed. |  |

#### Mass Reverse Payment Run (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Under certain circumstances and only in exceptional situations, you may need to reverse a payment run. A mass reversal might be necessary, for example, if you've executed a payment run by mistake or you entered an incorrect posting date for the payment run.

Prerequisite

You can only reverse payment documents in a payment run if you haven't started any follow-on processes. The program prevents any reversal in the following cases:

- You've already created payment media or batch.
- The system has already created entries in the payment register or check management.
- The payments are already undergoing the approval process of SAP Bank Communication Management (BCM).
- If a batch number exists, you must reset if you want to reverse a payment run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accounts Payable Jobs (F2257). | The Application Jobs view displays. |  |
| 3 | Create Job | Choose Create. |  |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Reverse Payment RunJob Name: Reverse Payment Run |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Parameters | Make the following entries and choose Check:Run Date: <date of payment run to be reversed>Identification: <ID of payment run to be reversed>Test Run: DeselectedReversal Reason: <reason for reversal> | Verify that the entries are complete and correct. |  |
| 7 | Schedule | Choose Schedule. | The job is scheduled. |  |

#### View Payment List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the payment list.

Prerequisite

You executed a payment run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Payment Lists (S_P99_41000099). |  |  |
| 3 | Selection | Enter the following:Program run date: <Date of payment run>Identification feature: <Identification of payment run>Proposal run only: Only select to display data that comes from the payment proposal, not from the paymentNote Additional fields are available for selection. Enter or modify fields according to your requirements. |  |  |
| 4 | Execute | Choose Execute.After reviewing the list, choose Exit to return to Payment List view. | Payment list displays. |  |

### Payment Plans

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity lets you schedule payment runs using different scheduling options according to your payments needs.

After a payment plan has been created and activated, a job is generated and a payment run is executed automatically according to scheduled criteria.

|  |
| --- |
| Note If the customer has bought and implemented Outgoing Payment with BCM Approval Process, the approval process is required. If payment approvals are required, the payment medium is only generated after approvals are executed. |

Prerequisite

The [Define Payment Medium Format Variants (Optional)](#unique_9) [page ] 12 procedure in the section has been executed.

Review and execute (if necessary), the [Available Amounts for Payment Program (Optional)](#unique_24) [page ] 50 procedure in the Preparation of Payments section.

The BRF+ Settings procedures under [Prerequisites](#unique_2) [page ] 7 are executed.

Invoices are posted, past due, and are open for payment. For more information, see the [Business Conditions](#unique_6) [page ] 11 section of this document.

Invoices are past due.

Use the Invoice Payment Preparation procedures to change the payment terms or due date of an invoice so it can be paid.

All steps for the procedures in the Invoice Payment Preparation section must be executed.

|  |
| --- |
| Note When you create a plan, you can group payment plans using categories with the Category field. You must first create categories.Via the Manage Your Solution app or the SAP Central Business Configuration project experience portal, access the Define Payment Plan Categories configuration step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Payment Plans (F4806). | The Manage Payment Plans view displays. |  |
| 3 | Create View | Choose Create. |  |  |
| 4 | General Information | In the General Information section, make the following entries:Plan Name: <Any description>Note The app doesn't currently prevent you from creating plans with the same name. Ensure that you use unique names when creating plans.Company Code: 3310Category: <leave blank> (see note in Prerequisites above)Payment Method: <Any outgoing payment method available in your country>Payment Run ID: <any ID description (five characters max.)> |  |  |
| 5 | Selections | In the Selections section, make the following entries:Supplier Selection: 33300001 |  |  |
| 6 | Payment Schedule | In the Payment Schedule section > Recurrence Pattern area, make the following entries:Recurrence Type: D (Daily)Recurrence Frequency: <leave blank>Note If you need to make payments every other day, enter 2 in the Recurrence Frequency field. For every third day, enter 3 (and so on for similar recurrence frequencies). You can also use the same logic for monthly and yearly recurrence types.In the Recurrence Range area, make the following entries:Start Date: <Today’s date>End Date: <Today’s date + 3>In the Date Specifications area, make the following entries:Posting Date: 01 (Run date)Docs Entered Up To: 01 (Run date) |  |  |
| 7 | Create | Choose Create. |  |  |
| 8 | Activate | Select your new payment plan and choose Activate. | A background job is created. |  |
| 9 | Exit | Go back to the SAP Fiori launchpad main view. | The SAP Fiori launchpad is displayed. |  |
| 10 | Background Job | Open Schedule Accounts Payable Jobs (F2257). |  |  |
| 11 | Search | Choose Go. | A list of all available background jobs display, |  |
| 12 | Job Details | Find the created job that uses the Automatic Scheduling of the Payment Program job template with the description containing the payment plan name. For that job, choose Navigate to the job details. | Job details are displayed. |  |
| 13 | Payment Run | After the job is executed according to scheduling criteria, a payment run is created and executed.With the Schedule Accounts Payable Jobs app, choose your job then Navigate to the job details. In the Run Details > Payment Run > Identification section, check the payment run ID. Use the Manage Automatic Payments app to review the executed job. | The executed payment run can be reviewed. |  |

### Single Outgoing Payment

Purpose

This section describes how a manual outgoing payment of bank transfer is created.

After payment approval, the payment medium file is created and sent to Multi-Bank Connectivity (MBC) for further processing.

|  |
| --- |
| Note For more information, see the Advanced Cash Operations (J78) test script or Basic Cash Operations (BFB) test script. |

Prerequisites

Invoices are posted and are due with one of the following payment methods:

- F
- I
- T

All steps from Invoice Payment Preparation have been executed.

#### Create Single Outgoing Payment (Indirect)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this process to pay a single invoice exact amount without discounts. Depending on the payment method and payment format (and possibly the bank) that is chosen, output can go to either Multi-Bank Connectivity (MBC), file download, or check print.

Prerequisite

You executed the [Define Payment Medium Format Variants (Optional)](#unique_9) [page ] 12 preliminary step procedure.

The vendor master record is created and a payment method is assigned.

|  |
| --- |
| Caution Make sure that there are no other payment run identification proposals pending to be executed using the same supplier. If payment proposals exist, they must be processed or deleted. Otherwise, no payment can be generated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Line Items (F0712). | The Manage Supplier Line Items (F0712) view displays. |  |
| 3 | Data Entry and Search | Make the following entries and choose the Go button.Supplier: <any>Company Code: 3310Status: Open ItemsOpen on Key Date: <Today's date>Item Type: Normal ItemsChoose the Go button to display a list of all vendor items . | Supplier line items are displayed according to your search criteria. |  |
| 4 | Select | To select a document number to pay, select the appropriate checkbox in the first column. | The Create Single Payment option activates. |  |
| 5 | Choose Create Manual Payment | Choose Create Single Payment. | The Create Single Payment view is displayed. |  |
| 6 | Data Entry | Make the following entries and choose Create.Payment Details section:Value Date: today's date | The details of the posted document display. |  |
| 7 | Create | Choose the Create button.Caution A warning is displayed if the house bank isn't defined in document to be paid. Payment is done using the master data definition. You can choose Accept to continue. | Payment run Mxxxx of <date> has been scheduled view displays. |  |
| 8 | Payment | To review the payment, see the previous Payment Run procedures. | Payment approval and SAP Multi-Bank Connectivity steps can be executed.Optional: Review the Payment Approval steps. |  |

### Online Payments

#### Free Form Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Free-form payments can trigger payments without referencing a business transaction. When you create a free-form payment, the bank information of the business partner master data doesn't have to be in the system, nor does the amount of the payment transaction have to be represented by an open item. This activity creates a payment request.

Prerequisites

The [Define Payment Medium Format Variants (Optional)](#unique_9) [page ] 12 procedure in the Preliminary Steps section is executed.

The business partner exists, and bank data and payment method are updated in Business Partner (BP) master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open My Free Form Payments (F2564). |  |  |
| 3 | Create | Choose Create. | The New Payment Request section displays. |  |
| 4 | Type | Make the following entry:Payment Request Type: For Supplier |  |  |
| 5 | Business Partner | In the Payee area, make the following entry:Supplier: 33300001 |  |  |
| 6 | Payee | In the Payee Bank Details area, make the following entry:Remember When entering values manually, either enter or select using the drilldown button. Ensure that Payee Bank Country, Payee Bank Key, and Payee Account Number. fields have automatically populated.Suplr Bnk Details ID: 0001Note Bank Details are found using the Maintain Business Partner (BP) app on the Payment Transactions tab. |  |  |
| 7 | Posting Data | In the Posting Data When entering values area, make the following entry:Company Code: 3310 |  |  |
| 8 | House Bank | In the House Bank area, make the following entries:Paying Company Code: 3310House Bank: AEBK1Account ID: AEAC1 |  |  |
| 9 | Payment Data | In the Payment Data area, make the following entries:Payt Currency Amount: <any>Currency: AEDPayment Methods: <any>Value Date: <Today's date> |  |  |
| 10 | Create the Payment | Choose Create | The Payment Request is created and saved. |  |

#### Review or Edit Free Form Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a free form payment request is reviewed or edited.

Prerequisite

A free form payment request has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Process Free Form Payments (F8654) . |  |  |
| 3 | Search | Make the following entry and choose Go:Company Code: 3310 | A list of created requests is displayed. |  |
| 4 | Request | Choose the previously created request (with the Created status). | The details of the chosen request display. |  |
| 5 | Edit (Optional) | Before posting, you can change fields, if required. Choose Edit and after completing any changes, choose Save. | Changes are saved. |  |
| 6 | Post | Note Before posting, ensure that any changes made to fields are saved.Choose Post and confirm by choosing Post. | The request status changes to Posted. |  |

#### Process Free Form Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Free-form payments can trigger payments without referencing a business transaction. After you create and post a free-form payment, you must release it to generate the payment.

|  |
| --- |
| Caution If the customer bought and implemented Outgoing Payment with BCM Approval Process, the approval process is required. |

Prerequisite

A free-form payment request is created.

The business partner exists.

The payment method is updated in business partner master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Process Free Form Payments (F8654). |  |  |
| 3 | Search | Enter search criteria (for example) and choose Go:Company Code: 3310 | A list of payment requests is displayed. |  |
| 4 | Select | Select a request. |  |  |
| 5 | Post | Choose Post. In the dialog box, confirm by choosing Post. |  |  |
| 6 | Release | Choose Release. In the dialog box, confirm by choosing Release. | The request is released, a payment run ID is created, and payment is generated. |  |
| 7 | Log | To check the application log for your payment run ID, use the Automatic Payment Transactions for Payment Requests (F111) app. |  |  |

### Manual Payment Online

#### Post Outgoing Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post outgoing payments either manually or automatically. The manual posting process is described in the following example. The manual outgoing payment generated in this step doesn't go through an approval process and doesn't create a payment medium.

Prerequisites

Review the house bank assignment to G/L account before you start the test so that you can use the proper G/L account in step 3 General Information in the Procedure section below.

To review, select the house bank and company code to test and use the Manage Bank Accounts (F1366A) app. In the app, go to House Bank Account Connectivity > House Bank Account Data > G/L Account Data .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments (F1612) view displays. |  |
| 3 | General Information | Make the following entries:General Information sectionCompany Code: 3310Posting Date: <Today's date>Journal Entry Date: <Today's date>Value Date: <Today's date>Reference (optional): <reference>Journal Entry Type: KZHeader Text: <header text>Bank Data sectionHouse Bank / Account: AEBK1/AEAC1 or AEBK2/AEAC2G/L Account: 11001000 (see Prerequisites above)Amount / Currency: <amount to pay on existing invoice>, for example, 119,00AEDFees: OptionalAssignment: OptionalExchange Rate: OptionalAmount / CCode Currency: Optional | A list of open items is displayed in the Open Items \| Standard section. |  |
| 4 | Open Item Selection | In the Open Item Selection section, make the following entries:Supplier Account: 33300001and choose the Show Items button. |  |  |
| 5 | Select/Deselect | Select an item to pay, and in the Clear column, choose Clear. | The item to pay transfers to the Items to be Cleared / Standard section. |  |
| 6 | Post | Choose Post.Note The generated payment doesn't require approval. | The system displays Journal entry xxxxxxxxxx was successfully posted in company code 3310 notification. |  |
| 7 | Display | To view the posted document, choose Display. | The posted document is displayed. |  |
| 8 | Back | Choose the Back button. | The system displays Journal entry has already been posted. You can now post a new payment notification. |  |
| 9 | Dismiss notification | Choose OK to dismiss the notification. |  |  |

### Payment Approval

Purpose

This section describes how the outgoing payment of bank transfer is approved. After payment approval, payment medium file is created.

|  |
| --- |
| Note Steps in this chapter come from the Advanced Cash Operations (J78) test script. If you have adopted Cash Management Full, you require an additional license for SAP Cash Management. |

|  |
| --- |
| Note If the customer has bought and implemented Outgoing Payment with BCM Approval Process, the approval process is required. |

Prerequisites

Invoices have been posted and are open for payment. For more information, see the Business Conditions section in this document.

All steps in Invoice Payment Preparation are executed.

All steps in Payment Run are executed.

The approvers are maintained for the bank account master data. For more information, see Maintain Payment Approver for Bank Accounts from the Advanced Cash Operations (J78) test script.

|  |
| --- |
| Caution You can find the procedure for Monitor Payments (F2388) in the Appendix (see [Monitor Payments](#unique_96) [page ] 158). The original procedure can be found in the Advanced Cash Operations (J78) test script.IMPORTANT: If a procedure or app is mentioned in the following subtopics and details are not included, use the Advanced Cash Operations (J78) test script to review and/or execute them. |

#### Bank Payment Approval (Optional based on Cash Management)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In SAP S/4HANA, a bank communication management (BCM) batch should be approved by two approvers. After the approval process is done, the payment medium is created automatically.

No matter the source of BCM batch, payment run of suppliers/customers or payment run of bank transfer, the BCM batch should go through the approval process.

|  |
| --- |
| Caution If you've implemented Outgoing Payment with SAP Bank Communication Management Approval Process (an additional license is required for SAP Bank Communication Management), the approval process is required. |

|  |
| --- |
| Note For more information, see the Advanced Cash Operations (J78) test script. |

Prerequisite

BCM batches are created successfully for the payment run of bank transfer.

The approvers are maintained for the bank account master data. For more information, see Maintain Payment Approver for Bank Accounts.

Procedure

|  |
| --- |
| Note In the Advanced Cash Operations (J78) test script, execute all steps in the Approval of Bank Transfer section. |

##### Approval by First Approver

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager.Note The user assigned to Signatory Group G001 in the Prerequisites section, Maintain Payment Approver for Bank Accounts. |  |  |
| 2 | Access the SAP Fiori app | Open Approve Bank Payments (F0673A). |  |  |
| 3 | Maintain Filters | Make the following entries and choose Go.Paying Company Code: 3310 |  |  |
| 4 | Review Payment Batch and Items | Choose the For Review tab, review to ensure that the batches are correct. | All items are correct and the batches can be approved. |  |
| 5 | Select Batch to be Approved | Select the payment batch for approval.If more than one batch must be approved, select the checkbox for the batches to approve. |  |  |
| 6 | Approve | Choose Approve. Enter the note and choose OK to confirm the dialog box. | The payment is approved and appears on the Reviewed tab. |  |
| 7 | (Optional) Undo Approval | Choose the Reviewed tab and select the payments to be discarded.Choose Discard Changes from the top right of the view.To confirm the dialog box, choose Discard Changes.Note This optional step is only necessary when you want to undo the approval. | The payment is discarded. it displays on the For Review tab. |  |
| 8 | Submit Reviewed Batch | Choose the Reviewed tab and select the payments to be submitted. Choose the Approve and Submit button. To confirm the dialog box, choose Submit. | The batch is submitted. |  |
| 9 (Optional) | Submit Verification Token (Optional) | On the dialog box Confirm Submission of Reviewed Batches, make the following entry and choose Submit.VerificationToken: < Insert the Passcode from App SAP Authenticator on your mobile phone and insert it here>Note This step is only required when you enable two-factor authentication using SAP Cloud Identity Services - Identity Authentication (IAS) for the Approve Bank Payments (F0673A) app. | The payment is sent to the Second Approver and no longer appears on the Reviewed tab. |  |
| 10 | Check Batch Status and Next Approver | Check the batch status and next approvers via App Monitor Payments (F2388), see step Monitor Payments. | The batch status is In Approval. The next approvers are displayed. For example: Cash Manager. |  |

##### Rejection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During the bank payment approval process, a bank communication management (BCM) batch is rejected.

Procedure

Review or execute the following steps in the Advanced Cash Operations (J78) test script:

- Approval of Bank Transfer
    - Reject by First Approver (Option)
    - Process Rejected Payment Document (Option)

##### Approval by Second Approver

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager.Note The user assigned to Signatory Group G002 in the Prerequisites section, Maintain Payment Approver for Bank Accounts. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Approve Bank Payments (F0673A). | The Approve Bank Payments app displays. |  |
| 3 | Maintain Filters | Make the following entries and choose Go.Paying Company Code: 3310 |  |  |
| 4 | Review Payment Batch and Items | Choose the For Review tab to ensure if the batches are correct. | All items are correct and the batches can be approved. |  |
| 5 | Select Batch to be Approved | Select the payment batch for approval.If more than one batch must be approved, select the checkbox for the batches to approve. |  |  |
| 6 | Approve | Choose Approve.Choose OK to confirm the dialog box. | The global payment is approved and appears on the Reviewed tab. |  |
| 7 | Submit Reviewed Batch | Choose the Reviewed tab and select the payments to be submitted, choose Submit.On the dialog box, choose Submit. | The payment is submitted. |  |
| (Optional) | Submit Verification Token (Optional) | On the Confirm Submission of Reviewed Batches dialog box, make the following entries and choose Submit:VerificationToken: < Insert the Passcode from App SAP Authenticator on your mobile phone and insert it here>, make the following entry and chooseNote This step is only required when you enable two-factor authentication using SAP Cloud Platform Identity Authentication (IAS) for the Approve Bank Payments app. | The payment is finally approved and no longer appears on the Reviewed tab. |  |
| 8 | Check Batch Status | Check the batch status and next approvers via App Monitor Payments (F2388), see step Monitor Payments. | The batch status is Payment Medium Created. The Reference Number is generated. |  |

### Payment Media

#### Create Payment Media

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the payment media automatically.

|  |
| --- |
| Note If payment approvals are required, the payment media is only generated after approvals are executed. |

Prerequisite

The [Define Payment Medium Format Variants (Optional)](#unique_9) [page ] 12 procedure in the Preliminary Steps section, under Prerequisites, has been executed. This is optional for the Cloud release.

Bank Integration with File Interface (1EG) and/or Bank Integration with SAP Multi-Bank Connectivity (16R) scope items are activated to generate the payment medium.

Payment approvals have been executed.

If you've implemented Outgoing Payment with SAP Bank Communication Management Approval Process (additional license required), the approval process is required.

Procedure

If the Full Cash Management is implemented with BCM (Bank Communication Management), after the outgoing payment is executed, and the BCM batch of this outgoing payment is approved (described in the Approval and Bank Integration step in Advanced Cash Operations (J78) test script), the payment medium file is created automatically.

If the Basic Cash Management is implemented, after the payment run is executed, the payment medium file is created automatically if the payment method is using the payment medium workbench (PMW) format.

For SAP Multi-Bank Connectivity, review the Bank Integration with SAP Multi-Bank Connectivity (16R) test script.

For Manual File Download, review the Bank Integration with File Interface (1EG) test script.

#### Manual Creation of Payment Media

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Payment media is usually automatically created after a payment run but if it fails to be created, in this activity payment media creation can be re-triggered.

|  |
| --- |
| Note This procedure isn't applicable and isn't supported for Bank Communication Management (BCM). |

Prerequisite

You performed a payment run that failed to create the payment media.

In the [Release Payment Proposal](#unique_38) [page ] 77 topic, follow the procedure steps to View Log Postings, then check for and fix errors in payment media creation.

In the Appendix, in the [Monitor Payments](#unique_97) [page ] 159 topic, review the payment run batch, then check for and fix errors in payment media creation. For more information about this process, review the Advanced Cash Operations (J78) test script.

|  |
| --- |
| Note You must fix all errors to successfully create the payment media if it wasn’t automatically generated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Payment Media - for Payment Runs (F7711). | The Create Payment view is displayed. |  |
| 3 | Search | If desired, enter search criteria to narrow the results and choose Go . | Your selection is displayed. |  |
| 4 | Select | Select the row with a Status of No Payment in File for a payment run ID.The number in the Completed Payments column should be zero. |  |  |
| 5 | Create Payment Media | Choose either Create Payment Media > for Payment Group or Create Payment Media > from Payment Run . |  |  |
| 6 | Confirm | Complete the required information and choose Create. | Payment media is created.The number changes in the Payments in File column. |  |
| 7 | Log | Choose View Change Log.Make the following entries and choose Go:Date: <date>Category: FBPM_NEWSubcategory: CPM | The following logs are displayed:Log for DeletionLog for Creation from Payment RunCreation for Payment Group |  |

#### Manual Deletion of Payment Media

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Payment media is automatically created after a payment run but if you have to reverse a payment run (review [Mass Reverse Payment Run (Optional)](#unique_39) [page ] 79), you must delete the payment media before you execute a reversal run.

|  |
| --- |
| Caution This procedure isn't applicable and isn't supported for Bank Communication Management (BCM). |

Prerequisites

You executed a payment run and payment media was created.

Per the appendix step [Monitor Payments](#unique_96) [page ] 158, review the payment run batch and check that the payment media is created. For more information, see the Advanced Cash Operations (J78) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Payment Media - for Payment Runs (F7711). |  |  |
| 3 | Search | If desired, enter search criteria to narrow results and choose Go. |  |  |
| 4 | Select Row | Select a row with a Status 0 in the Payment in File column. |  |  |
| 5 | Delete Payment Media | Choose Delete.Caution If a payment run contains multiple payment groups (group numbers), all groups and their associated files are deleted. | A dialog box is displayed. |  |
| 6 | Confirm | Choose Delete. | Payment media group is deleted. The row for the selected payment run is no longer shown.Once the payment media group is deleted, you can execute a reversal of a payment run. For BCM, the batch number needs to be reset too (See [Mass Reverse Payment Run (Optional)](#unique_39) [page ] 79). |  |
| 7 | Reverse Deletion | To reverse the payment media deletion, choose Create Payment Media > from Payment Run .Make the following entries for the previously deleted item:Payment Run Date: <date>Payment Run ID: <payment run ID> | The deleted payment media file is recreated. |  |

### Payment Advices

#### Print or Email Payment Advice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review or print a payment advice. An email is sent automatically after the payment has been approved.

|  |
| --- |
| Note If you've implemented Extended Cash Management (additional license required), the approval process is required. |

Prerequisite

The email address is updated in Business Partner (BP) master data.

|  |
| --- |
| Caution You can also maintain the email in BRF Settings, but if email addresses are maintained in both BRF and BP Master Data, the ones in BRF are used. If the conditions in BRF cannot be met (for example, Company Code is different from payment run), the email is sent to the ones in BP Master Data. We recommend to only maintain it in one place such as BP Master Data. |

Payment Run is executed and the approval process is executed.

The BRF + Settings procedures, described in the Preliminary Steps topic, under Prerequisites are executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). | The Manage Automatic Payments (F0770) view displays. |  |
| 3 | Go | Note If necessary, to find the payment run, make a selection in the Run Date field.Choose Go. |  |  |
| 4 | View Payment | Choose the Payments Processed tab. | The Items pane shows payments that are posted, finished, or with payment medium deleted. |  |
| 5 | Payments | To review the payment, for the selected payment run, choose Details (>) at the right of the row. |  |  |
| 6 | Select | Choose the Payments tab. |  |  |
| 7 | Open Payment Item | For a payment item line, choose Details (>) at the right of the row. |  |  |
| 8 | Output Items | Choose the Output Items tab. |  |  |
| 9 | Preview | For an Item ID, in the Display column, choose Display Document (PDF icon). | The PDF document displays in a new browser tab. |  |
| 10 | Print | Choose Print, then close the browser tab. |  |  |
| 11 | Email | In the Output Details section, select a row of the Channel column with a value of EMAIL and choose Send Output.Note If Status is In Error, review the email address format. After correcting it, select the checkbox and choose Resend. | An email is sent. |  |
| 12 | Close | Choose Back twice. |  |  |

#### Schedule Payment Advices (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to schedule payment advices to create and send them out via email.

If payment advices were already created and sent in a payment run, this step doesn’t need to be executed.

Prerequisite

The email address is updated in Business Partner (BP) master data as described in Maintain Business Partner or under the [BRF+ Settings for Payment Advice](#unique_10) [page ] 15 preliminary step procedure.

The payment run is executed.

The approval process is executed.

You executed the [BRF+ Settings for Payment Advice](#unique_10) [page ] 15 procedure in Prerequisites > Preliminary Steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accounts Payable Jobs (F2257). | The Application Jobs view displays. |  |
| 3 | Create Job | Choose Create. |  |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Create and Send Payment Advices to PayeesJob Name: Create and Send Payment Advices to Payees |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | Make the following entries:Run Date: <date>Identification: <Payment Run ID>Note To restrict the job execution, you can enter additional criteria with the fields in Further Selections Parameters. |  |  |
| 7 | Check | Choose Check to verify that entries are complete and correct. |  |  |
| 8 | Schedule | Choose Schedule. | You scheduled the job. |  |
| 9 | Review | After the job is finished, follow the steps in the [Print or Email Payment Advice](#unique_54) [page ] 100 procedure. |  |  |

### Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, open items correspondence is created.

Prerequisite

Invoices and payments have been posted.

Business Partner (BP) master data (such as email address, and so on) are updated.

If correspondence SAP09 Internal Document is chosen, a journal entry number is necessary before executing the report. It is recommended to use Procedure B, or use the Manage Journal Entries (F0717A) SAP Fiori app to find a journal entry number.

Procedure A

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Correspondence (F0744A). | The Create Correspondence (Version 2) (F0744A) view displays. |  |
| 3 | Data Entry | In the Parameters tab, make the following entries:Company Code: 3310Correspondence: <report>Note Select any of the following reports:SAP06 - Account StatementSAP08 - Open Item ListSAP09 - Internal Document when using this output, we recommend using Procedure B | Depending on the selected report, different fields are displayed below these two fields. |  |
| 4 | Supplier Information | In the Parameters area, make the following entries and press Enter:Note Depending on the report you selected in the Correspondence field, only certain of the following fields are displayed. Only enter content in the displayed fields.Supplier: SelectedSupplier: <Any supplier number>Open at key date: <Any date>Postings from: <Any date>Posting to: <Any date> | Supplier details are entered. |  |
| 5 | Actions | Use the buttons to:PreviewSend EmailPrint. | Correspondence is created according to the selected criteria.Note If the Reference field is populated in the FI document, the reference text is displayed in the form Document number column. Otherwise, the document number is displayed.The correspondence form language depends on the Business Partner (BP) language settings in the BP master data. |  |

Procedure B

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A) | The Manage Journal Entries view displays. |  |
| 3 | Select Journal Entry | Make the following entries and choose Go.Company Code: 3310Ledger Group: emptyJournal Entry Type: (optional) For example, SAJournal Entry: <empty>Journal Entry Date: (optional) <date>Period: (optional) <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> | Selected journal entries are displayed in the Journal Entries list. |  |
| 4 | Manage Journal Entry | For a journal entry number, choose Details (>) at the right of the row. | The Manage Journal Entries view displays with the document details. |  |
| 5 | Correspondence | Choose Create Correspondence. | The Create Correspondence view displays. |  |
| 6 | Entry View | In the Parameters area, enter:Company Code: 3310Correspondence: SAP09 (Internal Document - Entry View)Note Two fields may appear (Journal Entry, Fiscal Year). They should already show values from the journal entry number you chose. | Available fields display and are populated automatically. |  |
| 7 | Actions | Use the buttons to:PreviewSend EmailPrint. | Correspondence is created according to the selected criteria. |  |
| 8 | Exit | Choose Home to exit. | SAP Fiori launchpad displays. |  |
| 9 | Ledger View | Repeat steps 1–5 and select:Company Code: 3310Correspondence: SAP09 (Internal Document - Ledger View) | Available fields display and are populated automatically. |  |
| 10 | Parameters | Choose Advanced Parameters and make the following entry:Ledger: <Any ledger, for example 0L> |  |  |
| 11 | Actions | Use the buttons to:PreviewSend EmailPrintNote Some steps (such as Send Email) might require additional information to complete the action. | Correspondence is created according to the selected criteria. |  |

### Incorrect Posting

#### Reset Cleared Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reset a cleared item.

|  |
| --- |
| Caution Resetting a large number of cleared documents can cause system performance issues. If you have more than 1000 items to process, the system automatically creates a scheduled job using Schedule Jobs to Reset Cleared Items (F9296). For more information, see [Schedule Jobs to Reset Cleared Items (Optional)](#unique_59) [page ] 109. |

Prerequisite

Invoices and payments are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Reset Cleared Items (F2223). | The Reset Cleared Items (F2223) view displays. |  |
| 3 | Search | Make the following entries and choose Go:Company Code: 3310 | Clearing entries are shown in the lower pane. |  |
| 4 | Execute | To select a document to process, choose the Details (>) button at the right of the row. | The Clearing Entry view displays. |  |
| 5 | Reset | Choose Reset. | The system displays the Clearing XXXXXXX reset notification. |  |
| 6 | Continue | Choose OK to continue. |  |  |

#### Reset and Reverse Cleared Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reset and reverse a payment. You may need to perform a reversal because a payment was not approved or because the bank could not execute the payment.

|  |
| --- |
| Caution Resetting a large number of cleared documents can cause system performance issues. If you have more than 1000 items to process, the system automatically creates a scheduled job using Schedule Jobs to Reset Cleared Items (F9296). For more information, see [Schedule Jobs to Reset Cleared Items (Optional)](#unique_59) [page ] 109. |

Prerequisite

Invoices and payments are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Reset Cleared Items (F2223). | The Reset Cleared Items (F2223) view displays. |  |
| 3 | Search | Make the following entries and choose Go:Company Code: 3310 | Clearing entries are shown in the lower pane. |  |
| 4 | Process | To select a document to process, choose the Details (>) button at the right of the row. | The Clearing Entry view displays. |  |
| 5 | Reset and Reverse | Choose Reset and Reverse. | The Reverse Journal Entry dialog box is displayed. |  |
| 6 | Make Entries | Make the following entries and choose OK:Reversal Reason: Wrong postingPosting Date: Today's date | The system displays the message Document posted XXXXXX in company code XXXX. |  |
| 7 | Continue | Choose the OK button. | The Reset Cleared Items view is displayed. |  |

#### Schedule Jobs to Reset Cleared Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule jobs to reset cleared items. This activity can be run manually, if needed. If you have run Reset Cleared Items (F2223) and have more than 1000 items to clear, this transaction is automatically executed to prevent performance issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Schedule Jobs to Reset Cleared Items (F9296). | The Schedule Jobs to Reset Cleared Items view is displayed. |  |
| 3 | Create | Choose Create. | The New Job: Reset Cleared Items view is displayed. |  |
| 4 | Enter Job Details | Make the following entries and choose Step 2:Job Template: Reset Cleared ItemsJob Name: Reset Cleared Items |  |  |
| 5 | Enter Job Details | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Job Details | Make the following entries and choose Schedule:Clearing entry: <entry number>Company Code: 3310Fiscal Year: <fiscal year>, for example, 2026Note If you are performing a reversal along with the reset, enter additional information into the fields in the Reversal Parameters pane. | The Application Jobs view is displayed. |  |
| 7 |  | To refresh the review, choose the Go button. When the report status is Finished, choose the document button in the Results column for the job you scheduled. | Review the log results. |  |

### Down Payments

#### Create Down Payment Request

##### Create Down Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a down payment request is created.

Prerequisite

The Supplier master record has been entered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Down Payment Requests (F1688). | The Manage Supplier Down Payment Requests (F1688) view displays. |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Header Data | In the Header area, make the following entries:Company Code: 3310Journal Entry date: <Today’s date>Posting date: <Today’s date>Journal Entry Type: KZTransaction Currency: AEDHeader Text: <header text> |  |  |
| 5 | Enter Items Data | In the Items area, enter the following and press Enter:Supplier: 33300001Amount: 10Trg. Spec. G/L Ind: A (Default value, don't change)To view more details, choose > (Add Line Item). Enter the following data:Tax Code: <Input Tax Code>Note The posting date is used as the tax calculation date.Due On: <Today’s date>Business Place: 3310and choose Enter. |  |  |
| 6 | Post | Choose Post. | The Success view displays the journal entry number posted. |  |
| 7 | Other | Select your next action on the Success view:DisplayPost NextGo to Worklist |  |  |

##### Create Down Payment Request with Workflow

Purpose

The workflow is a general function that allows to define condition-based workflows for approval processes.

Prerequisite

You've executed the Business Conditions and Preliminary Steps.

###### Create Team

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a team that uniquely identifies the approvers in runtime based on predelivered conditions.

Prerequisites

You've executed the Business Conditions and Preliminary Steps.

Business Partners are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Teams and Responsibilities - Supplier Down Payment Requests (F7483). | The Manage Teams and Responsibilities view is displayed. |  |
| 3 | Create | Choose Create. | The Team view is displayed. |  |
| 4 | General Information | In the General Information section, make the following entries:Name: <Any name>Global ID: <Keep same as Name field>Description: <Any description>Status: EnabledType: FIAP_DPRV (Supplier Down Payment Request Verification) |  |  |
| 6 | Team Owners | In the Team Owners section, add the user with the AP Manager role (if not already assigned, choose Create to add it):Business Partners: <person ID> (from [Maintain Business Users](#unique_15) [page ] 31 preliminary step) |  |  |
| 7 | Team Members | In the Team Members, section, choose Create.Select the user who is the approver and choose OK:Business Partners: <person ID> (from [Maintain Business Users](#unique_15) [page ] 31 preliminary step)In the Functions column, assign a function for the approver (BP):Functions: Supplier Down Payment Request Approver |  |  |
| 8 | Save | Choose Create. | The team is created. |  |

###### Create Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define and activate a supplier down payment request workflow for approval process.

Prerequisite

A team is created and responsibilities are assigned.

|  |
| --- |
| Note Make sure that only your workflow is activated or your workflow is first in the order. If not, creating a supplier down payment request fails. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Manager. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Workflows - Supplier Down Payment Requests (F7100). | The Manage Workflows view displays. |  |
| 3 | Create | Choose Create. | The New Workflow view displays. |  |
| 4 | Header | In the Header section, make the following entry:Workflow Name: <Any name> |  |  |
| 5 | Properties | In the Properties section, make the following entries:Description: <Any description>Valid from: <Today’s date>Valid To: < Today’s date + 1 year> |  |  |
| 6 | Start Conditions | In the Start Conditions section, define any preconditions that must be met before you start the workflow.To add a precondition, choose + and define the precondition. You can add more preconditions by choosing + again. | You added preconditions to the workflow. If the start conditions aren't met, the workflow doesn't execute. |  |
| 7 | Workflow Step 1 | In the Steps section, choose Create.In the Header section, enter the following:Step Name: <Any name>Step Type: Manually Verify and ApproveIn the Recipients section, enter the following:Assignment By: TeamTeam : <team> (created in subchapter Create Team)Step to be completed by: One of the recipientsIn Step Conditions enter the following:Company Code equals to: 3310Choose + (Create another condition) and add:Total Amount in Company Code Currency >=: 100 AEDIn Exception Handling, enter the following:RejectRequired Action: Do nothingAction Result: Cancel WorkflowSend BackRequired Action: Do nothingAction Result: Cancel WorkflowChoose Create. |  |  |
| 8 | Workflow Step 2 | Create a second workflow step.In the Steps section, choose Create.In the Header section, enter the following:Step Name: <Any name>Step Type: Post Submitted DocumentChoose Create. |  |  |
| 9 | Activate | Choose Save.Choose Activate. | The workflow is activated.Make sure that only your workflow is activated or your workflow is in the first order. Otherwise, creating a Supplier Down Payment Request with Workflow fails. |  |
| 10 | Order | To change the order of a created workflow, in the Manage Workflows view, select a workflow and choose Define Order. Use the up and down arrows to move the workflow. When done, choose Save. |  |  |

###### Create Supplier Down Payment Request for Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you start a workflow to send a supplier down payment request for approval.

Prerequisite

You performed the preliminary steps.

You assigned the SAP_BR_MANAGER role to business users.

A team is created and responsibilities are assigned.

A workflow is created and activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Open the SAP Fiori App | Open Verify Supplier Down Payment Requests (F7103). |  |  |
| 3 | Create | Choose Create.Make the following entries:Header section:Company Code: 3310Journal Entry Date: <Today’s date>Posting Date: <Today’s date>Journal Entry Type: KZTransaction currency: <currency>Items section:Supplier: <any>, for example, 33300001Trg. Spec. G/L Ind. : AAmount: 1000Due on: <due date>Note Depending on the country/region, you may need to enter data in other fields (such as tax data, due date and so on). Enter them as needed. | A new view displays. |  |
| 4 | Submit | Choose Submit. | A dialog box appears indicating Journal Entry … submitted successfully. |  |
| 5 | Display | Choose Display to view the entry.After viewing the entry, go back to the main app screen. Look for the recently created entry and choose it to see the details again, then choose Show Approval Status to view status.Choose Back to go to the previous screen. |  |  |

###### Review Down Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the approver reviews a request with the possibility to display more details, such as account assignments.

Prerequisite

Preliminary steps are executed.

Business Users are assigned the SAP_BR_MANAGER role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Open the SAP Fiori App | Open Verify Supplier Down Payment Requests - Approver Inbox (F7102) or My Inbox - All Items (F0862). |  |  |
| 3 | Selection | In the All tasks pane, select the supplier down payment request to review. | Details of the task display in the right pane. |  |
| 4 | View Settings | In the Items section, choose Settings (Gear icon).Select additional fields to be displayed and choose OK:Trg. Spec. G/L. Ind.Main Asset No.SegmentEtc. | The chosen fields are displayed. |  |
| 5 | Log | Choose Show log. | You can review the Workflow log and Task log. |  |
| 6 | Comments | To enter a comment, choose Show Details, enter an optional comment and choose Submit. |  |  |
| 7 | Other options | Other option available before approving a workflow include:RejectSend BackClaim: Item remains in your inbox. When chosen, the button changes to Release.Suspend: Choose a date to process. The item disappears from the inbox. This item appears again as the suspend date approaches.Forward: Use this to enter a new processor. This item appears in the new processor’s inbox. |  |  |
| 8 | Done | Once you review the request, proceed to the approval procedure. |  |  |

###### Process Down Payment Request Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the approver approves a request.

Prerequisite

Preliminary steps are executed.

Business Users are assigned the SAP_BR_MANAGER role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Open the SAP Fiori App | Open Verify Supplier Down Payment Requests - Approver Inbox (F7102) or My Inbox - All Items (F0862). |  |  |
| 3 | Selection | In the All tasks pane, select the supplier down payment request to be approved. | Details of the task display in the right pane. |  |
| 4 | Log | Choose Show log. | You can review the Workflow log and Task log. |  |
| 5 | Comments (optional) | If you want to enter a comment, choose Show Details, enter an optional comment and choose Submit. |  |  |
| 6 | Approve | Choose Approve. | The system displays a dialog box. |  |
| 7 | Submit | Optionally, you can add a note.Choose Submit. | The task is processed successfully and no longer appears in the All tasks pane. The request for approval is sent automatically to the second approver. |  |
| 8 | View | To view approvals, use the Verify Supplier Down Payment Requests - Approver Outbox (F7101) app to see the details of the approved items. |  |  |

#### Post Down Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a payment for a down payment request is generated. Depending on your normal payment process for payments, this procedure can also be executed by running automatic payments.

In a test environment where you primarily want to test the process for down payments, it's easier to use the Post Outgoing Payment SAP Fiori app to generate the same postings.

You can't use both the Post Outgoing Payments (F1612) and the Manage Automatic Payments (F0770) SAP Fiori apps for the same down payment. Therefore, if you want to generate a payment medium (for example, a check), use the Manage Automatic Payments (F0770) app in the second step instead of the Post Outgoing Payments (F1612) app.

Two procedure tables are included. Use the first one to post down payments with down payment requests. Use the second one to post them without the requests.

Prerequisite

A down payment request has been posted.

Choose a down payment request from the previous step.

Procedure - Post Down Payment with Down Payment Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments (F1612) view displays. |  |
| 3 | Enter Payment Data | Make the following entries:General Information sectionCompany Code: 3310Posting Date: <today's date>Journal Entry Date: <today's date>Value Date: <today's date>Reference (optional): < your reference>Journal Entry Type: KZHeader Text: <header text>Bank Data section:G/L Account: 11001000House Bank / Account: AEBK1/AEAC1Amount / Currency: 100 AEDNote Adjust the amount if tax relevant.Fees: OptionalAssignment: OptionalExchange Rate: OptionalAmount / CCode Currency: OptionalOpen Item Selection Account area:Account Type / Account ID: SupplierSupplier Account: 33300001and choose Show Items. | A list of open items is displayed in the Open Items section. |  |
| 4 | Select More | To display only the special G/L transactions, choose Select More, and from the dialog box, select the dropdown menu to include:Line Item Type: Special G/LNote To display the Special G/L indicator, choose Settings. In Columns, select the Special G/L checkbox and choose OK. | Document with special G/L transactions is displayed. |  |
| 5 | Select/Deselect | Select a down payment request to pay. On the Clear column, choose Clear. | The down payment to pay is transferred to the Items to be Cleared section. |  |
| 6 | Post | Choose Post. | The system displays Success and the Journal entry xxxxxxxxxx was successfully posted in company code #### notification . |  |

Procedure - Post Down Payment without Down Payment Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments (F1612) view displays. |  |
| 3 | Enter Payment Data | Make the following entries:General Information sectionCompany Code: 3310Posting Date: <today's date>Journal Entry Date: <today's date>Value Date: <today's date>Reference (optional): < your reference>Journal Entry Type: KZHeader Text: <header text>Bank Data section:G/L Account: 11001000House Bank / Account: AEBK1/AEAC1Amount / Currency: 100 AEDNote Adjust the amount if tax relevant.Fees: OptionalOpen Item Selection Account area:Account Type / Account ID: SupplierSupplier Account: 33300001 | A list of open items is displayed in the Open Items section. |  |
| 4 | Post on Account | Choose the Post on Account tab.In the Line Items section, check the default values:Account Type: SupplierCompany Code: 3310Supplier: 33300001 |  |  |
| 5 | Special G/L Indicator | In the line item, make the following entries:Special G/L: A (down payment)Debit Amt (EUR): 100.00Choose > to expand the line item details. If required, enter any missing data (for example, Tax Code: V0) | The line item is validated (a green check is displayed). The Balance indicator changes to 0.00. |  |
| 6 | Simulate | Choose Simulate. | The Simulated Journal Entry view is displayed. Check that the simulation looks correct. |  |
| 7 | Post | Choose Post. | The system displays Success and the Journal entry xxxxxxxxxx posted notification. |  |

#### Invoice Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, an invoice is entered and cleared against a down payment.

Prerequisite

A down payment has been posted.

Choose a down payment request from previous step.

Procedure

Execute the Invoice Entry without Purchase Order test procedure in this document. The invoice amount must be larger than the down payment amount posted in previous procedure.

#### Post Outgoing Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this process to make a payment to an invoice where a down payment is applied. The payment should be equal to the amount of the invoice, less the down payment amount.

Prerequisite

An invoice was posted (as completed in the previous procedure). A down payment is posted (as described in the Post Down Payment procedure). A payment amount should be equal to the invoice amount, less the down payment amount. The open balance of the invoice is equal to the down payment posted.

To generate a payment medium (such as a check), do the following:

1. Execute the Clear Open Items test procedure. This activity clears the down payment against the invoice to be paid. The down payment amount appears in the Allocated Amount column with a different sign for each document. In the Allocated Amount column of the invoice journal entry, enter the amount that reduces the balance to zero.
2. Access the Manage Automatic Payments SAP Fiori app to pay the invoice and clearing document. As a result, a payment is generated for the difference.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments (F1612) view displays. |  |
| 3 | Enter Payment Data | Make the following entries and choose Show Items.General Information sectionCompany Code: 3310Posting Date: <Today's date>Journal Entry Date: <Today's date>Value Date: <Today's date>Reference (optional): < your reference>Journal Entry Type: KZBank Data sectionG/L Account: 11001000House Bank / Account ID: AEBK1/AEAC1Amount / Currency: Invoice amount less downpayment amount AEDFees: OptionalAssignment: OptionalExchange Rate: OptionalAmount / CCode Currency: OptionalOpen Item Selection Account area:Account Type / Account ID: SupplierSupplier Account: 33300001Choose Show Items. | A list of open items is displayed in the Open Items section. |  |
| 4 | Select/Deselect | From the Open Items section, select the invoice to pay, and in the Clear column, choose Clear. | The invoice where the payment is applied is transferred to the Items to be Cleared section. |  |
| 5 | Allocate | In the Items to be Cleared section, enter the following:Allocated Amount: Invoice amount less the down payment amountand choose Enter | The balance is zero. |  |
| 6 | Post | Choose Post. | The system displays the Success view with Journal entry xxxxxxxxxx successfully posted notification. |  |

#### Clear Open Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manually clear open items.

Prerequisite

The invoices are posted. Down payments are posted (as described in the previous procedure, Post Down Payment). Payments are applied to an invoice, as described in the previous procedure, Post Outgoing Payment.

|  |
| --- |
| Note When the payment medium must be generated, execute this procedure before the previous step, Post Outgoing Payment. For more information, see the Prerequisites of Post Outgoing Payment |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear Outgoing Payments - Manual Clearing (F1367) | The Clear Outgoing Payments (F1367) view displays. |  |
| 3 | Clear Open Items | Choose the Clear Open Items button. | The Clear Open Items dialog box is displayed. |  |
| 4 | Enter Supplier Information | Make the following entries and choose OK:Company Code: 3310Supplier: 33300001 |  |  |
| 5 | Filter | Select the Journal Entry Type column header. Choose Go to Table Settings. | The View Settings dialog box is displayed. |  |
| 6 | Journal Entry Type | Choose the Filter tab.Make the following entries and choose OK:Journal Entry Type: KA | A list of open items to be cleared is displayed. |  |
| 7 | Select More | To display open items and special G/L transactions, choose Select More and choose:Line Item Type: Normal Open Items and Special G/L Transactions | Normal open items and special G/L transactions are displayed in Open Items section. |  |
| 8 | Open Item Selection | In the Open Items section, select the invoice where you applied the payment in the Post Outgoing Payment procedure. Choose the down payment posted in the Post Down Payment procedure by choosing the Clear button in the Clear column of each Journal entry. | When the invoice is chosen, the assigned payment is also selected. In the Items to Be Cleared section, the balance of the open item (invoice) is displayed.Down payment is moved to the Items to Be Cleared section. The balance is zero. |  |
| 9 | Simulate (Optional) | Before posting, you can simulate the posting if needed. | A view showing the posting to be created, when the document is posted, displays. |  |
| 10 | Post | Choose the Post button. | The system displays Success. The document number, company code, and year created display and option buttons to Display or go to the Payment List are available. |  |

### Optional: Interest Calculation

#### Optional: Schedule Interest Calculation Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule the interest calculation jobs.

Prerequisites

Master data for interest calculation (interest indicator) is maintained in the Maintain Business Partner topic.

Past due invoices exist (at least a month or more overdue).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Interest Calculation Jobs (F4176). | The Application Jobs view displays. |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Calculate Item Interest for Accounts PayableJob Name: Calculate Item Interest for Accounts Payable |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | In the Parameters section, make the following entries and choose Schedule:Supplier account: for example, 33300001Company Code: 3310Interest Indicator: for example, 01Interest Calculation To: <for example, last day of current month>Test Run: Selected if you want to do a test run; Deselected if you want to do an actual run | The Application Jobs view is displayed. |  |
| 7 | View Report | To refresh the review, choose the Go button. When the report status is Finished, choose the document button in the Results column for the job you scheduled.Note You can also choose the Log button in the scheduled job row. When you do so, the job log is displayed, showing the output items. You can click on the output item link to display additional details. | The Document (ID xxxxxxx) view is displayed. The report shows the status of the journal entry document, and shows information such as the journal entry number, the amounts, and the interest. |  |
| 8 | View Report | Review the document, then choose Back. |  |  |
| 9 | Run Actual Report | If you performed a test run in step 5, repeat steps 6-8 with Test Run deselected to perform an actual run. |  |  |

#### Optional: Manage Interest Runs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the interest runs. If needed, you can reverse an interest run or resend an interest letter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Interest Runs (F4485). |  |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Company Code: 3310Supplier: for example, 33300001 | Documents are displayed in the Interest Documents pane. |  |
| 4 | View Interest Document | For the row for your interest document, choose Details (>) at the right of the row. | The Interest Run view is displayed for that document. The Items Subject to Interest pane shows related journal entry items, while the Output Items pane shows any outputs (for example, print or email) and their status. |  |
| 5 | Back | Choose Back. |  |  |
| 6 | Reverse Interest Runs (Optional) | If needed, you can select the checkbox for an item and choose Reverse Calculated Interests.In the Enter Reverse Parameters dialog box, make the following entries and choose Confirm:Reversal Reason: <reversal reason> | The Messages dialog box displays the document posting. |  |
| 7 | Resend Interest Letter (Optional) | If needed, you can select the checkbox for an item and choose Send Interest Letters.On the Send Interest Letters dialog box, choose Yes to send the interest letter. | The Sent Interest Letters dialog box displays messages about the output channels from which the interest letters are sent. |  |

#### Optional: Display Interest Runs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the interest runs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Interest Runs (F4485). |  |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Company Code: 3310 | A list of documents displays in the Interest Documents pane. |  |
| 4 | View Interest Document | For the row for your interest document, choose the arrow button at the right of the row. | The Interest Run view is displayed for that document. The Items Subject to Interest pane shows related journal entry items, while the Output Items pane shows any outputs (for example, print or email) and their status. |  |

### Guarantees Received

#### Guarantees Received

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to create a guarantee.

|  |
| --- |
| Note To define or change a reconciliation account, use one of the following options:Manage Your Solution app: In Configure Your Solution, choose Application Area: Finance, Sub Application Area: General Ledger, Item Name: Chart of Accounts, Configuration Steps: Automatic Account Determination. Make and save your entries.SAP Central Business Configuration: In the Business Process Configuration app, search for Automatic Account Determination. Choose the link to go to the SAP S/4HANA Cloud Public Edition system and log on as a Configuration Expert - Business Process Configuration. Make and save your entries. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Guarantees Received (F7933). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries and choose Post:General Information:Company Code: 3310Document Date: <Date>Posting Date: < Today’s Date>Date: < Today’s Date>Document Type: <KA>Transaction Currency: <Co. Code currency>, for example, AEDLine Item Detail:Supplier: <supplier number >Amount in Transaction Currency: <Amount >Due On: <today's date + # days> | The guarantee is created.Note Once a decision is reached and action is taken on the received guarantee, the guarantee can be reversed. For more information, see the [Reverse Guarantees](#unique_73) [page ] 133 procedure. |  |

#### Reverse Guarantees

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to reverse a guarantee.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Guarantees Received (F7933). |  |  |
| 3 | Enter Details | Select an entry and choose Reverse. | A dialog box is displayed. |  |
| 4 | Reverse | Confirm the reversal | The guarantee is reversed. |  |

### Periodic Activities

#### Check Open Balances

Purpose

This activity lists all Accounts Payable line items.

Prerequisites

Invoices are created but not paid.

Procedure

Follow the instructions in the [View Supplier Line Items](#unique_33) [page ] 69 test procedure.

#### Create Supplier Balance Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to create a supplier balance confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accounts Payable Jobs (F2257). | The Application Jobs view displays. |  |
| 3 | Create Job | Choose Create. |  |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Supplier Balance ConfirmationJob Name: Supplier Balance Confirmation |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: SelectRecurrence Pattern: Single Run |  |  |
| 6 | Parameters | Make the following entries:General Selections section:Company Code: 3310Reconciliation Key Date: <Today’s date>, verify the date or enter if necessaryOutput Control section:For no reply, enter:Description: <any>Date of Issue: <Today’s date>.No Reply: SelectFor reply, enter:Description: <any>Date of Issue: <Today’s date>No Reply: DeselectDate for Reply: <Today’s date + 7>Reply To: <any Business Partner>Note The Business Partner must have a valid address. |  |  |
| 7 | Check | Choose Check to verify that entries are complete and correct. |  |  |
| 8 | Schedule | Choose Schedule. | The job is scheduled. |  |

#### Manage Supplier Balance Confirmations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure lets you manage open balance confirmation letters and track the actual status. You can enable the user to check open balances and confirm the amount in the system during the year-end closing to an external auditor.

Prerequisite

Invoices are created but aren't paid.

The BRF + Settings procedures, described in the Preliminary Steps topic, under Prerequisites are executed.

Balance Confirmation is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Balance Confirmations - For Suppliers (F2959) |  |  |
| 3 | Search | Make the following entries and choose Go:Company Code: <Any Company Code number> | A list of balance confirmations displays. |  |
| 4 | Select from List | Select any row from the balance confirmations list and choose Details (>). | Details are displayed. |  |
| 5 | Preview | In the Output Details section, in the Display row, choose Display Document. | The document displays. |  |
| 6 | Resend | In the Output Details section, select and flag the checkbox of an item with Completed status and then choose either:Duplicate: For a resend on a completed item, it creates a new duplicate of the output item. To send again, select the duplicated item and choose Send Output.orRetry: For a resend on an erroneous item, it retries to send the same item again. | The document is sent again. |  |
| 7 | Status | To update the status, refresh the page. | Status is updated. |  |

#### Print Supplier Balance Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure allows printing open balance confirmation letters.

Prerequisite

Invoices are created but aren't paid.

The Balance Confirmation is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Balance Confirmations - For Suppliers (F2959). | The Manage Supplier Balance Confirmations (F2959) view displays. |  |
| 3 | Search | Make the following entries:Company Code: <any Company Code number>and choose Go: | A list of balance confirmations displays. |  |
| 4 | Selection | Select any row and choose Details (>). | Details are displayed. |  |
| 5 | Preview | In the Output Details section, from the Display row, choose Display Document. | Document displays. |  |
| 6 | Print | Choose the Print button. | Document prints. |  |

### Invoice Management Reporting

#### Accounts Payable Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure guides you through the Account Payable Overview. In this activity, you review an overview of relevant figures and statistics related to the accounts payable process. The Accounts Payable Overview (F2917) SAP Fiori app offers a central point of entry and an overview of the department.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager.Note Once you log on, you can customize fields to be displayed by default. To do so, choose User > Settings > Default Values , then add the Display Currency, Company Code, and Supplier fields. Save your changes. |  |  |
| 2 | Access the SAP Fiori App | Open Accounts Payable Overview (F2917). | The Accounts Payable Overview (F2917) view displays. |  |
| 3 | Edit Criteria | Make the following entries and choose Go:Display Currency: <Your Company Code currency>Company Code: <any>Note You can also enter values in other fields, such as Supplier, Accounting Clerk, and so on. | Relevant figures and statistics display.Some of the available cards include:Blocked InvoicesBlocked Invoices - Chart ViewPosted InvoicesPayables AgingCash Discount UtilizationDays Payable Outstanding IndirectDays Payable Outstanding DirectPosted Invoices in Current PeriodParked InvoicesQuick LinksSuppliers with Debit BalancesInvoices Blocked in Supplier Master DataMy InboxDue Invoices Free for PaymentInvoice Processing Statistics |  |
| 4 | Navigate to Options | There are different, available options for reviewing figures and statistics.You can change the global filters if needed. The visible cards can be customized.Each card mentioned in the prior step provides you with functions to view and manage various accounts payable functions and information. | Figures and statistics display according to available options you select. |  |

#### Days Payable Outstanding

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view a report showing days payable outstanding.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Days Payable Outstanding - Last 12 Months (F1740). | The Days Payable Outstanding view displays. |  |
| 3 | Navigation | To change the view, choose the drill-down button or buttons in the first row of the report.Note If you're using a filter using predefined buttons (such as Accounting Clerk, Company Code, and so on), to display all available values after choosing the desired button, you may need to choose Search without entering any values to see all of them. | Different views can be displayed. |  |
| 4 | Detailed Analysis | Choose the Jump To button.Choose Days Payable Outstanding - Detailed Analysis. | The Days Payable Outstanding view displays. |  |
| 5 | Selection | To change a view, choose +Add Analysis Step.Select any of the displayed options. As you choose more options, more options are displayed. Select your preference and then select the chart type:TimeCompany CodeCustomerCountry/Region of SupplierDue PeriodNote You can choose the +Add Analysis Step button again to display more analyses. | Different views are displayed. |  |
| 6 | Save | Under the Unnamed Analysis Path button, choose Save As. Enter a name to save your current selection. | The view is saved and can be accessed later to view the information with this type of analysis. |  |
| 7 | Open | Under the Unnamed Analysis Path button, choose Open.Select a previously saved analysis and choose OK. | The button displays the name of the selected analysis. |  |

#### Overdue Payables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view any payables that are overdue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Overdue Payables - Today (F1746). | The Overdue Payables view displays. |  |
| 3 | Navigation | To change the view, choose the drill-down button or buttons in the first row of the report. | Different views can be displayed. |  |

#### Future Payables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the analysis of Future Payables.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Future Payables - Today (F1743). | The Future Payables view displays. |  |
| 3 | Navigation | To change the view, choose the drill-down button or buttons in the first row of the report. | Different views can be displayed. |  |

#### Cash Discount Forecast

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the analysis of Cash Discount Forecast.

Prerequisites

You must have at least one invoice in open status using payment terms that give a discount (for example, payment term 0006 (Before End of the month 4% cash discount)).

The app only reports key figures if there are invoices in the system with discounts. If no key figures are shown, create a supplier invoice with a payment term that includes a discount if you pay early (such as payment term 0006). The discounts only appear after the payment run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Discount Forecast - Available Amount (F1735). | The Cash Discount Forecast view displays. |  |
| 3 | Navigation | To change the view, choose the drill-down button or buttons in the first row of the report. | Different views can be displayed. |  |

#### Cash Discount Utilization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the analysis of Cash Discount Utilization.

Prerequisites

You must have at least one invoice in open status using payment terms that give a discount (for example, payment term 0006 (Before End of the month 4% cash discount)).

The app only reports key figures if there are payments executed where it was possible to utilize the offered discount. If no key figures are shown, create a supplier invoice with a payment term that includes a discount if you pay early (for example payment term 0006) and then pay this invoice. The discounts only appear after the payment run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Discount Utilization - Today (F1736). | The Cash Discount Utilization view displays. |  |
| 3 | Navigation | To change the view, choose the drill-down button or buttons in the first row of the report. | Different views can be displayed. |  |

#### Invoice Processing Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the analysis of Invoice Processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Invoice Processing Analysis - Today (F1745). | The Invoice Processing Analysis view displays. |  |
| 3 | Navigation | To change the view, choose the Toggle Filter icon at the right of the view to modify the filters.Required filters are marked with an asterisk (*).Note Additional filters are available.Above the graph, a dropdown menu provides additional filtering options.Additional buttons, above the graph are used to change the display layout or view results as a table. | Views display according to your selection. |  |

#### Invoice Processing Time

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the analysis of invoice processing time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Invoice Processing Time - Today (F1745). | The Invoice Processing Time view is displayed. |  |
| 3 | Navigation | To change the view, choose Adapt Filters at the right of the view to modify the filters.Required filters are marked with an asterisk (*).Note Additional filters are available.Above the graph, a dropdown menu provides additional filtering options.Additional buttons above the graph are used to change the display layout or view results as a table. | Views display according to your selection. |  |

#### Aging Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the Aging Analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Aging Analysis - Payable Amount (F1733). | The Aging Analysis view displays. |  |
| 3 | Navigation | To change the view, choose the drilldown button available at the top of the graph or select the text in the first column of the report.Above the graph are additional buttons you use to change the display layout of the graph. | Views displays according to your selection. |  |

#### Aging Report for Accounts Payable

Use

In this activity, you view a report that shows the aging for accounts payable. The AP Manager can analyze the payable amounts to suppliers by aging interval. These intervals allow the accounts payable manager to quickly recognize the payments due in the present month, the following month, and so on.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager |  |  |
| 2 | Access the SAP Fiori App | Open Aging Report for Accounts Payable (F4401). |  |  |
| 3 | Filter Selection | This view provides several filters:Company CodeG/L AccountAccount GroupSupplierChoose any of the available filters and set a value according to your reporting needs. | The view is filtered according to your selection. When you set a value, a graph and details are shown per supplier and reconciliation account. |  |

#### Automatic and Manual Payments Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view payments done automatically and manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Automatic and Manual Payments - Payments for Last Year (F1749). | The Automatic and Manual Payments view displays. |  |
| 3 | Navigation | To change the view, choose the drilldown button available at the top of the graph or select the text in the first column of the report.Above the graph are more buttons you use to change the display layout of the graph. | Different views can be displayed:By CompanyBy CurrencyBy SupplierBy User |  |

#### Supplier Payments Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the supplier payments analysis. The report displays payments that aren't applied to supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Supplier Payment Analysis - Open Payments (F1750). | The Supplier Payment Analysis view displays. |  |
| 3 | Navigation | To change the view, choose the drilldown button available at the top of the graph or select the text in the first column of the report.Above the graph are additional buttons you use to change the display layout of the graph. | Different views can be displayed:By CompanyBy CurrencyBy SupplierBy User |  |

#### Display Item Change Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display, sort, and analyze logged changes for journal entries. The report provides better control and tracks changes performed manually by different users on payable items.

Prerequisite

Invoices are created.

Payment is created.

Changes in documents are made before generating this report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Display Item Change Log - Supplier (F7795). |  |  |
| 3 | Select | Make the following entries and choose Go:Document Type: <select any type>Company Code: 3310Changed On: <interval of dates>Fiscal Year: <current year> |  |  |
| 4 | Results | The information of all journal entries is shown per the selection and the changes in each of the changed journal entries can be viewed. |  |  |
| 5 | Exit | Choose Back to exit. |  |  |

### Vendor Certificate Validity Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In many of Middle East and North African (MENA) countries, companies doing business are required to have some type of certificate as a government requirement. Vendors are required to store the information related to these certificates together with the vendor master record.

The vendor certificates functionality enables the maintenance of information related to existing vendor certificates in the vendor master along with information related to its validity.

1. Chamber of Commerce Certificate
2. Commercial Registration
3. Trade License
4. Contractors Classification Certificate

Prerequisite

In many MENA countries, companies to do business are required having some type of certificate as a government requirement. Vendors are required to store the information related to these certificates together with the vendor master record.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant or a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner (BP) view is displayed. |  |
| 3 | Select Supplier | Make the following entry and press Enter:Business Partner:33300001 | The Display Organization:33300001 view is displayed. |  |
| 4 | Change BP Role | Enter the following values:Display in BP role: Supplier (Fin. Accounting) | The Display Organization:33300001. role Supplier (Fin. Accounting) view is displayed. |  |
| 5 | Edit Supplier | Choose the Switch between Display and Change button to change the data and update. | The Business Partner Master Data is available for editing. |  |
| 6 | Choose Company Code Data | Choose the Company Code button and choose Enter.Note You must choose Enter for the Vendor: Ctry-Spec. Enh. tab to display. |  |  |
| 7 | Vendor: Ctry-Spec. Enh. Tab | Choose the Vendor: Country-Spec. Enh. tab. | Note For each newly added vendor certificate, you must set the Main Certificate field. |  |
| 8 | Add Vendor Certificate | In the MENA: Vendor Certificate section, choose Insert Row and make the following entries:Main Certificate: SelectedCertificate ID: TRCertificate No.: 121Valid From: For example, 01/01/2010Valid To: For example, 12/31/2030Registration City: For example, CAIRO | The vendor certificate is added. |  |
| 9 | Repeat for Additional Vendor Certificate | Repeat the previous step using the following values:Certificate ID: TFCertificate No.: 122Valid From: For example, 01/01/2010Valid To: For example, 12/31/2030Registration City: For example, CAIRO | Additional vendor certificate is added. |  |
| 10 | Repeat for Vendor Certificate | Repeat step 8, using the following values:Certificate ID: CRCertificate No.: 123Valid From: For example, 01/01/2010Valid To: For example, 12/31/2030Registration City: For example, CAIRO | Additional vendor certificate is added. |  |
| 11 | Save | Choose Save. | Changes are saved. |  |

Procedure to Check Vendor Certificate Validity

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Check Supplier Certificate Validity - United Arab Emirates. | The Supplier Certificate Validity Check view is displayed. |  |
| 3 | Enter First Selection Criteria | Make the following entries:Company Code: 3310Validity Date: for example, 12/31/2031and choose Execute. | The vendor certificate list displays. |  |
| 4 | Block Vendor | Select the checkbox for the vendor certificate row with:Certificate ID: CRNote TR and TF Certificate IDs aren't available for this application.Choose Block/Unblock and Save.Choose Log to review details. | Vendor certificate is blocked. |  |
| 5 | Return to Selection Criteria | Choose Back. |  |  |
| 6 | Enter Selection Criteria | Make the following entries:Company Code: 3310Validity Date: for example, 12/31/2022and choose Execute. | The vendor certificate list displays. |  |
| 7 | Unblock Vendor | Select the checkbox for the vendor certificate row with:Certificate ID: CRNote TR and TF Certificate IDs aren't available for this application.Choose Block/Unblock and Save.Choose Log to review details. | Vendor certificate is unblocked. |  |
| 8 | Return to SAP Fiori Launchpad | Return to the SAP Fiori launchpad. |  |  |
| 9 | Access the SAP Fiori App | Open Schedule Supplier Certificate Validity Check (F1240). | The Application Jobs view is displayed. |  |
| 10 | Create Application Job | Choose Create. | The New Job view appears. |  |
| 11 | Choose Job Template | On the General Information section, select a job template, for example, Vendor Certificate Validity. |  |  |
| 12 | Enter Scheduling Options | On the Scheduling Options section, you can choose to start immediately or choose a time to run the job. Either you selectStart Immediately: selectedOr to schedule a different start time, make the following entries:Start: <current time or future time to start job>Time Zone: <time zone>Note To choose other time zones or for additional Scheduling Options, select Add More Scheduling Options. In the Scheduling Information dialog box, the additional time zones and scheduling options are available.Recurrence: selectedRecurrence Pattern: For example, WeeklyEvery: For example, 1On: For example, MondayEnd: OptionalRun Only on Working Days: selectedIf Date Falls on Non-working Day: Run on Next Working DayCalendar: For example, United Arab Emirates (Standard)and choose OK. | The job runs immediately or to the options you specify. |  |
| 13 | Enter Parameter Section | On the Parameter Section, make the following entries:Company Code: 3310Vendor: 33300001>Certificate ID: leave blankValidity Date: For example, 12/31/2031and choose Automatic (Background Run). |  |  |
| 14 | Run the Application Job | Choose Schedule to run the application job. |  |  |
| 15 | View the Application Job | On the Application Job view, make the following entry:Date From To: For example, <current day>and choose Go. | The result list of Vendor Certificate Jobs displays. The status of the application job appears in the Status column.The vendor certificate is blocked. |  |
| 16 | Create Another Application Job | Repeat steps 8 to 13 and at the Parameter Section, make the following entries:Company Code: 3310Vendor: 33300001Certificate ID: leave blankValidity Date: 12/31/2017and choose Automatic (Background Run). |  |  |
| 17 | Run the Application Job | Choose Schedule to run the application job. |  |  |
| 18 | View the Application Job | On the Application Job view, make the following entry:Date From To: For example, <current day>and choose Go. | The result list of Vendor Certificate Jobs displays. The status of the application job appears in the Status column.The vendor certificate is unblocked. |  |

## Appendix

### Display Process Flow Accounts Payable

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app graphically displays the relationship between individual business objects of the Accounts Payable work area. This shows as a process flow, displaying information about the business object for each stage of the process (such as purchase orders, goods movements, incoming invoices, journal entries and clearing entries). Additionally, it provides the ability to view missing business objects.

Prerequisite

Documents that generate the accounts payable (AP) process are created. For example:

- Purchase Order
- Invoice
- Payment
- Clearing

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Process Flow - Accounts Payable (F2691). |  |  |
| 3 | Data Entry | Make the following entries and choose Go:Document Type: Select document type, from the dropdown list, according to the origin of the document:All document typesPurchase orderGoods movementIncoming invoiceJournal entryClearing entryDifferent entry fields are required, depending on which document type you select. For example:Document Number: <document number per document type selected>Note Entering a document number automatically applies values for other fields.Company Code: 3310Fiscal year: Current year | A Process Flow displays the stage of the process of the selected document and additional details. |  |
| 4 | Review | Choose to display the information about the document in a process flow or a tabular view. | The view displays according to your selection. |  |
| 5 | Exit | Choose Back to exit. |  |  |

### Disable Period Check for Material Master (Optional)

Purpose

By default, the system checks if the corresponding period is open to post a supplier invoice. This activity disables the period check or material master records. Disabling the period check means that the system doesn't perform the check for G/L account postings and postings to assets. The check still occurs for direct postings to the material and for invoices that reference purchase orders.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Sourcing and Procurement

Sub Application Area: Invoice Processing

1. For the row with Item Name of Incoming Invoice, choose Details (>).
2. For the Disable Period Check for Material Master row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Disable Period Check for Material Master.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Disable Check | In the Disable MM Period Check pane, make the following entries:No Check: Selected |  |  |
| 2 | Save | Choose Save. | The period check is disabled. |  |

### Monitor Payments

Use

The Monitor Payments step originates from the Advanced Cash Operations (J78) test script. For more information about the process, go to the test script for J78.

#### Monitor Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Monitor Payments (F2388) app, you can display an overview of your payment batches. You can view the statuses of batches and individual payments at different processing stages.

In different stages of a BCM batch's lifecycle, the app displays different batch/batch item status.

- Payment Batch Created: Batch is created and waits for first approval.
- In Approval: Batch is approved at least once, though not final approval.
- Payment Medium Created: Batch successfully completes approval process and the payment medium is created.
- Accepted by Bank: The payment medium has been sent to the bank and the bank sends responds with a payment status message accepting the payment instruction. This can also be fulfilled through Multi-Bank Connectivity (MBC).
- Stmt. Received: Batch is reconciled by a bank statement.

|  |
| --- |
| Note The Monitor Payments app incorporates SWIFT gpi reason codes to indicate the status of payments. External entities, such as banks, use reason codes to communicate the status of SWIFT gpi payments. Your entity receives these external Status Reason Codes and translates them into internal reason codes. One internal reason code may be mapped to many external reason codes. You, as the key user for configuration, can create reason codes and map them to external reason codes. |

|  |
| --- |
| Note (Optional) You may use the configuration activities Fix Errors for Payment Batches to configure remediations in Preliminary Steps. You also have taken the required actions to enable fixing functionalities, for example, manually resetting and reversing several payment documents to enable the 'Mass Reset and Reverse' functionality or rejecting or reversing all payment documents to enable setting the status 'Automatically Rejected' (IBC20). Then you can find remediations on the Remediations tab on the batch details screen of the Monitor Payments (F2388) app. They are fixing functions you can use to correct common problems with payment batches. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Payments (F2388). |  |  |
| 3 | Find the Newly Created Batch | Maintain your filter and choose Go. Choose the New tab. | All newly created batches are displayed on the New tab. You can find the batch you created earlier in the process. |  |
| 4 | Verify the Batch Status | Verify the batch status in the Bank Status Text column. The status should be Payment Batch Created. | Note If the approval list in bank master data is empty, all payment will be rejected or approved depending on the value customized in the Define Automatic Approval/Rejection for Bank Account Master Data preliminary step in the Advanced Cash Operations (J78) test script. |  |
| 5 | Check Details | Select your cash flow item, and choose > (Details). | Detailed information for this batch is displayed. |  |
| 6 | Check Approver | In the header section, choose Approvers to check who are the first approvers for the batch. Close the dialog box when you're done. | All approvers used in the first approver step are shown (for example: Accounts Payable Manager). |  |

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
- see-also :: [[03-financial-accounting-and-close/test-script-monitoring-of-goods-and-invoice-receipts-2v7-ae-876]]
- see-also :: [[03-financial-accounting-and-close/integration-of-payment-advice-with-buyers-and-suppliers-2mb-ae-test-sc]]
- see-also :: [[10-procurement/test-script-automated-invoice-settlement-2lh-ae-831]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J60_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 246,893 chars in the whole document
