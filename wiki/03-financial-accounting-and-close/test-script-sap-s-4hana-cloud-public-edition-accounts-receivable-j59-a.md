---
id: 03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounts-receivable-j59-a
title: "Test Script: SAP S/4HANA Cloud Public Edition - Accounts Receivable (J59_AE) (J59_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script for Accounts Receivable scope item J59 (United Arab Emirates), release 2608: prerequisites, preliminary config and step-by-step test procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/accounts-receivable]
aliases: [J59_S4CLD2608_BPD_EN_AE]
keywords: [Accounts Receivable, test procedures, dunning, incoming payments, down payments, bank statement reprocessing, interest calculation, balance confirmation, electronic invoicing, brf+ output determination]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J59_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1305
topic: 03-financial-accounting-and-close/accounts-receivable
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP S/4HANA Cloud Public Edition - Accounts Receivable (J59_AE) (J59_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J59_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Accounts Receivable** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Accounts Receivable (J59_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232863259)

[2 Prerequisites 6](#_Toc232863260)

[2.1 System Access 6](#_Toc232863261)

[2.2 Roles 6](#_Toc232863262)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232863263)

[2.4 Business Conditions 8](#_Toc232863264)

[2.5 Preliminary Steps 10](#_Toc232863265)

[2.5.1 Define Accounting Clerk 10](#_Toc232863266)

[2.5.2 BRF+ Settings 10](#_Toc232863267)

[2.5.2.1 BRF+ Settings for Customer Balance Confirmation 10](#_Toc232863268)

[2.5.2.2 BRF+ Settings for Item Interest Calculation 17](#_Toc232863269)

[2.5.2.3 BRF+ Settings for Dunning Notice (Optional) 22](#_Toc232863270)

[2.5.2.3.1 Download Standard Template 22](#_Toc232863271)

[2.5.2.3.2 Upload Custom Template 24](#_Toc232863272)

[2.5.2.3.3 Assign Form Template 25](#_Toc232863273)

[2.5.2.3.4 Dunning Output Determination 26](#_Toc232863274)

[2.5.2.4 BRF+ Settings for FI Customer Invoice 29](#_Toc232863275)

[2.5.3 Preliminary Steps for Electronic Invoicing (PEPPOL) 34](#_Toc232863276)

[2.5.3.1 Define Identification Types for Business Partners 34](#_Toc232863277)

[2.5.3.2 Maintain Company Code Data (FINSC_T001Z_N) 36](#_Toc232863278)

[2.5.3.3 Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) 37](#_Toc232863279)

[2.5.3.4 Maintain Business Partner Master Data 38](#_Toc232863280)

[2.5.3.5 Assign Party ID Types to Business Partner (EDOEUBUPAV) 39](#_Toc232863281)

[2.5.3.6 Assign Party ID Types to Companies (EDOEUCOMPV) 40](#_Toc232863282)

[2.5.3.7 Optional Steps for Electronic Invoicing (PEPPOL) 41](#_Toc232863283)

[2.5.3.7.1 Business Partner Master Data Maintenance for Electronic Invoicing (Optional) 41](#_Toc232863284)

[2.5.3.7.2 Value Mapping Maintenance for Electronic Invoicing (Optional) 42](#_Toc232863285)

[2.5.4 Number Range to Business Places Assignment for a New Fiscal Year 46](#_Toc232863286)

[2.5.5 Manage Situation Types (Optional) 48](#_Toc232863287)

[2.5.6 Add Fields to Items (Optional) 50](#_Toc232863288)

[2.5.7 Manage Default Account Assignments 51](#_Toc232863289)

[2.5.8 Assign Reason Codes For Write-Off 52](#_Toc232863290)

[2.5.9 Business Partner Certificates 54](#_Toc232863291)

[2.5.9.1 Activate Business Partner Certificates Functionality 54](#_Toc232863292)

[2.5.9.2 Define Business Partner Certificate IDs 55](#_Toc232863293)

[2.5.9.3 Assign Business Partner Certificates to Country/Region 56](#_Toc232863294)

[3 Overview Table 58](#_Toc232863295)

[4 Test Procedures 63](#_Toc232863296)

[4.1 Preparation of Payments 63](#_Toc232863297)

[4.1.1 Maintain Business Partners 63](#_Toc232863298)

[4.1.2 Maintain Business Partner Certificate 65](#_Toc232863299)

[4.1.3 Display Customer List 67](#_Toc232863300)

[4.2 Enter Invoice Without Sales Order 68](#_Toc232863301)

[4.2.1 Enter Invoice Without Sales Order 68](#_Toc232863302)

[4.3 Mass Upload 70](#_Toc232863303)

[4.3.1 Mass Import of Customer Invoices 70](#_Toc232863304)

[4.4 Invoice Reporting 72](#_Toc232863305)

[4.4.1 Create Dunning Notices 73](#_Toc232863306)

[4.4.2 Manage My Dunning Proposals 75](#_Toc232863307)

[4.4.3 Display Dunning History 77](#_Toc232863308)

[4.4.4 Open Correspondence 78](#_Toc232863309)

[4.4.5 Display Correspondence History 81](#_Toc232863310)

[4.5 Invoice Management Reporting 82](#_Toc232863311)

[4.5.1 Accounts Receivable Overview 82](#_Toc232863312)

[4.5.2 Monitor Overdue Receivables 83](#_Toc232863313)

[4.5.3 Monitor Overdue Receivables by Risk Class 84](#_Toc232863314)

[4.5.4 Future Receivables 85](#_Toc232863315)

[4.5.5 Total Receivables 86](#_Toc232863316)

[4.5.6 Days Sales Outstanding 87](#_Toc232863317)

[4.5.7 Dunning Level Distribution 88](#_Toc232863318)

[4.5.8 Days Beyond Terms 89](#_Toc232863319)

[4.5.9 Display Item Change Log 90](#_Toc232863320)

[4.5.10 Cash Collection Tracker 91](#_Toc232863321)

[4.6 Down Payments 92](#_Toc232863322)

[4.6.1 Create Down Payment Request 92](#_Toc232863323)

[4.6.2 Display Down Payment Request 94](#_Toc232863324)

[4.6.3 Post Down Payment 95](#_Toc232863325)

[4.6.4 Enter Invoice Without Sales Order 97](#_Toc232863326)

[4.6.5 Post Incoming Payments 98](#_Toc232863327)

[4.6.6 Clear Incoming Down Payments 100](#_Toc232863328)

[4.6.7 Clear Open Items Manually 101](#_Toc232863329)

[4.7 Incoming Payments 103](#_Toc232863330)

[4.7.1 Incoming Payment with Electronic Bank Statement 103](#_Toc232863331)

[4.7.1.1 Daily Cash Operations – Bank Statement 103](#_Toc232863332)

[4.7.1.2 Cash Application Intelligence Integration 104](#_Toc232863333)

[4.7.1.3 Reprocess Bank Statement Items 104](#_Toc232863334)

[4.7.1.4 Manage Enrichment Rules for Bank Statement Processing (Optional) 108](#_Toc232863335)

[4.7.1.5 Manage Value Extraction for Bank Statements (Optional) 109](#_Toc232863336)

[4.7.1.6 Manage Bank Statement Processing Rules (Optional) 110](#_Toc232863337)

[4.7.1.7 Obtain Payment Advices Manually (Optional) 113](#_Toc232863338)

[4.7.1.8 Manage Payment Advice 114](#_Toc232863339)

[4.7.1.9 Clear Credit/Debit Memos Manually 117](#_Toc232863340)

[4.7.2 Incoming Payment without Electronic Bank Statement 119](#_Toc232863341)

[4.7.2.1 Post Incoming Payments 119](#_Toc232863342)

[4.7.3 Incorrect Posting 121](#_Toc232863343)

[4.7.3.1 Reset Cleared Items 121](#_Toc232863344)

[4.7.3.2 Reset and Reverse Cleared Items 122](#_Toc232863345)

[4.7.3.3 Schedule Jobs to Reset Cleared Items (Optional) 123](#_Toc232863346)

[4.7.3.4 Reverse Individual Documents 125](#_Toc232863347)

[4.8 Invoice Collection Preparation 126](#_Toc232863348)

[4.8.1 Display Customer Balances 126](#_Toc232863349)

[4.8.2 Manage Customer Line Items 127](#_Toc232863350)

[4.9 Interest Calculation 129](#_Toc232863351)

[4.9.1 Schedule Interest Calculation Jobs 129](#_Toc232863352)

[4.9.2 Manage Interest Runs 131](#_Toc232863353)

[4.9.3 Display Interest Runs 132](#_Toc232863354)

[4.10 Guarantees Made 133](#_Toc232863355)

[4.10.1 Guarantees Made 133](#_Toc232863356)

[4.10.2 Reverse Guarantees 134](#_Toc232863357)

[4.11 Periodic Activities 135](#_Toc232863358)

[4.11.1 Check Open Balances 135](#_Toc232863359)

[4.11.2 Create Balance Confirmation 135](#_Toc232863360)

[4.11.3 Manage Balance Confirmations 137](#_Toc232863361)

[4.11.4 Print Customer Balance Confirmation 138](#_Toc232863362)

[4.11.5 Bad Debt Write-Off 139](#_Toc232863363)

[4.12 eDocument Cockpit 141](#_Toc232863364)

[5 Appendix 143](#_Toc232863365)

[5.1 Display Process Flow Accounts Receivable 143](#_Toc232863366)

[5.2 Manage Payment Advice 144](#_Toc232863367)

## Purpose

Overview

With Accounts Receivable, you manage open receivables invoices that are automatically created from sales processes. Using various analytical tools, you can manage and control open items to optimize accounts receivables handling. The primary source of incoming payments is incoming bank statements that are loaded within the Cash Management process and automatically reconciled with open invoices. User-friendly views simplify and streamline the post processing of open items.

Alternatively, you can manually post incoming payments and easily reconcile the payment with an open item. Several analytical tools are available to monitor the receivables, allowing you to react quickly if you discover a declining payment discipline among your customers. You can effortlessly generate dunning letters for overdue items and track your customers' dunning history.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

System Access

|  |  |  |
| --- | --- | --- |
|  | Type of Data | Details |
| System | System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Receivable Accountant for United Arab Emirates | SAP_BR_AR_ACCOUNTANT_AE | Accounts Receivable | SAP_FIN_SPT_AR_ACCOUNTING_GLO_PC |  |
| Accounts Receivable Manager | SAP_BR_AR_MANAGER | Accounts Receivable | SAP_BR_AR_MANAGER |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you've installed an SAP Best Practices Package, you can use the following package scenario data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Controlling Area | A000 |  |  |
| Customer | 3310000133100002 |  |  |
| House Bank | AEBK1/AEAC1 |  |  |
| Bank G/L Account | 11001000 |  |  |
| Cost Center | 33101101 |  |  |
| Profit Center | YB700 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNH | Create Profit Center - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J14 - Sales Order Processing – Project-Based Services | Execute to create and post invoices to accounting before running this test script. |
| BD9 - Sell from Stock | Execute to create and post invoices to accounting before running this test script.Caution Not valid for SAP S/4HANA Professional Services Cloud. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Execute to create and post invoices to accounting before running this test script. |
| BFB - Basic Cash Operations | Execute to upload bank statements. |
| BDQ - Invoice Correction Process with Debit Memo | Execute to create debit memos that are manually cleared in this test script.Caution Not valid for SAP S/4HANA Professional Services Cloud. |
| BKL - Invoice Correction Process with Credit Memo | Execute to create credit memos that are manually cleared in this test script.Caution Not valid for SAP S/4HANA Professional Services Cloud. |
| BKJ - Sales Order Processing with Customer Down Payment | Execute the creation of the down payment request before running this test script.Caution Not valid for SAP S/4HANA Professional Services Cloud. |
| J58- Accounting and Financial Close | Execute to create open posting periods. |
| 31N - Situation Handling | This scope item must be executed before doing any of the situation handling steps in this script. |

The following technical configurations must be established to test this scope item :

Integration to Other Applications

| Integration Scenario | Application Name | Details |
| --- | --- | --- |
| Tax Determination | Vertex |  |
| Bank Connectivity | Multi-Bank Connectivity | Connectivity is configured to send payment instructions to the bank and receive bank statements from the bank. |
| Load Electronic Bank Statements |  | Bank statements are loaded into financials, automatically, through a standard interface to banks. You don't set up the interface to the banks first.You should be able to adjust the reconciliation rules for the bank statement, but the interface is part of the service available with the private option. |

### Preliminary Steps

#### Define Accounting Clerk

Purpose

In this activity, you add, change, or remove accounting clerks. Add the user testing this script as an accounting clerk, so that the user can test the dunning letter activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager . |  |  |
| 2 | Access the SAP Fiori App | Open Define Accounting Clerks (S_ALR_87003335). | The Change View "Accounting Clerks": Overview view is displayed. |  |
| 3 | New Entries | Choose New Entries. | The Overview of Added Entries view is displayed. |  |
| 4 | Enter Accounting Clerk Data | Make the following entries and choose Save:Company Code: 3310Clerk: < Any two alphanumeric characters>Name of Accounting Clerk: <name of clerk>Office User: <Your user id or user id of Accounts Receivable Accountant>Note Office User is a mandatory field. | You created a new accounting clerk. |  |

#### BRF+ Settings

##### BRF+ Settings for Customer Balance Confirmation

Purpose

In this activity, you define the system determination of output parameters for printing a balance confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |  |
| 3 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Output Type | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Add Rules | Expand the Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and enter or verify the following:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: LETTERand choose OK.From the Dispatch Time field dropdown, select Direct Value Input.Dispatch Time: 1 (Immediately)or 2 (Scheduled)and choose OK.Note 2 is used for Print Bundling and is the preferred setting according to central guidance.Choose Insert New Row and enter the following:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: CHECKLISTand choose OK.From the Dispatch Time field dropdown, select Direct Value Input.Dispatch Time: 1 (Immediately)or 2 (Scheduled)and choose OK.Note 2 is used for Print Bundling and is the preferred setting according to central guidance. |  |  |
| 5 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | The system displays the Objects saved and activated notification. |  |
| 6 | Determine Receiver | In the Select Business Rules section, choose:Show Rules for: Balance ConfirmationDetermination Step: Receiver. | Details are displayed in the Maintain Business Rules section. |  |
| 7 | Add Rules | If necessary, expand the Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: = LETTERand choose OK.From the Account Type field dropdown, select Direct Value Input.Account type: = K (Suppliers)and choose OK.From the Role field dropdown, select Direct Value Input.Role: = Kand choose OK.From the Exclusive Indicator field dropdown, select Direct Value Input.Exclusive Indicator: - (false)and choose OK.Choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: = LETTERand choose OK.From the Account Type field dropdown, select Direct Value Input.Account type: = D (Customers)and choose OK.From the Role field dropdown, select Direct Value Input.Role: = Dand choose OK.From the Exclusive Indicator field dropdown, select Direct Value Input.Exclusive Indicator: - (false)and choose OK.Choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: CHECKLISTand choose OK.From the Account Type field dropdown, select Direct Value Input.Account type: leave blankand choose OK.From the Role field dropdown, select Direct Value Input.Role: Cand choose OK.From the Exclusive Indicator field dropdown, select Direct Value Input.Exclusive Indicator: - (false)and choose OK. |  |  |
| 8 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | Rules are activated. |  |
| 9 | Determine Channel | In the Select Business Rules section, chooseShow Rules for: Balance ConfirmationDetermination Step: Channel | Details are displayed in the Maintain Business Rules section. |  |
| 10 | Add Rules | If necessary, expand Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: = LETTERand choose OK.From the Channel field dropdown, select Direct Value Input.Channel: PRINTand choose OK.Choose + (Insert New Row) and enter the following:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: = CHECKLISTand choose OK.From the Output Type field dropdown, select Direct Value Input.Channel: PRINTand choose OK. |  |  |
| 11 | Insert New Row | Choose the Insert New Row button. |  |  |
| 12 | Enter Details | Make the following entries:Output Type: LETTERChannel: EMAILExclusive Indicator: - (false) |  |  |
| 13 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | Rules are activated. |  |
| 14 | Determine Form Template | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 15 | Add Rules | Expand the Maintain Business Rules section.Choose Edit.In the Table Contents section, choose + (Insert New Row).Make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: = LETTERand choose OK.Note The Form Template column is at the far right of the table. Use the scroll bar along the bottom of the table to scroll right to display for the following two entries.From the Form Template field dropdown, select Direct Value Input.Form Template: FIN_FO_BLNC_CNFRM_LTTRand choose OK.Choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: CHECKLISTand choose OK.From the Form Template field dropdown, select Direct Value Input.Form Template: FIN_FO_BLNC_CNFRM_CHKLSTand choose OK. | Rule data is entered. |  |
| 16 | Activate Rules | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | Rules are activated. |  |
| 17 | Determine Output Relevance | In the Select Business Rules section, make the following entries:Show Rules for: Balance ConfirmationDetermination Step: Output Relevance | Details are displayed in the Maintain Business Rules section. |  |
| 18 | Add Rules | If necessary, expand the Maintain Business Rules section.Choose Edit.On Table Contents choose + (Insert New Row) and enter the following:#:<next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: = LETTERand choose OK.From the Relevance Indicator field dropdown, select Direct Value Input.Relevance Indicator: X (True)and choose OK.Choose + (Insert New Row) and make or verify the following entries:#:<next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: = CHECKLISTand choose OK.From the Relevance Indicator field dropdown, select Direct Value Input.Relevance Indicator: X (True)and choose OK. |  |  |
| 19 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. | Rules are activated. |  |
| 20 | Determine Printer Settings | In the Select Business Rules section, chooseShow Rules for: Balance ConfirmationDetermination Step: Printer Settings |  |  |
| 21 | Add Rules | If necessary, expand the Maintain Business Rules section.Choose Edit .In the Table Contents section, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: = LETTERand choose OK.From the Print Queue field dropdown, select Direct Value Input.Print Queue: DEFAULT or use the one defined in your systemNumber of Copies: 1Choose Insert New Row and enter the following:#:<next higher number>Output type: = CHECKLISTNote The Print Queue and the Number of Copies columns are at the far right of the table. Use the scroll bar along the bottom of the table to scroll right to display for the following two entries.From the Print Queue field dropdown, select Direct Value Input.Print Queue:DEFAULT or <enter print queue defined in your system>and choose OK.From the Number of Copies field dropdown, select Direct Value Input.Number of Copies: 1and choose OK. |  |  |
| 22 | Activate | Choose Activate.Confirm the Confirm Activation dialog box by selecting Yes. |  |  |
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

##### BRF+ Settings for Dunning Notice (Optional)

###### Download Standard Template

Purpose

In this activity, you create a new dunning template that matches your business requirements. You download the standard template and make edits to the text.

Prerequisite

The following preliminary steps require that Adobe Lifecycle Designer is downloaded and installed. Log on as an Administrator role to the SAP Fiori launchpad and open the Install Additional Software (F1261) app. The Adobe Lifecycle Manager is available for download at that location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Form Templates (F1434). | The Maintain Form Templates (F1434) view displays. |  |
| 3 | Access the Templates | Choose the Predelivered Templates tab. |  |  |
| 4 | Access the Templates | Make the following entry and press Enter:Form Template name: FIN_FO_DUNN_NOTE |  |  |
| 5 | Access the Templates | In the Predelivered Templates section for content, choose >. | Available languages are displayed for FIN_FO_DUNN_NOTE form template. |  |
| 6 | Dunning Notice | In the Available Languages section, select an available language (for example, English) and choose the Download button on that row.A Download Language dialog box is displayed. Select the country/region version from theSelect Form Template Master: For example, APOC_DEMO_FORM_MASTER_AENote The country/region abbreviation at the end of the template file name indicates the language of the selected file.Choose OK. | Form templates are saved to a zip file.Note Templates are saved to a format that only Adobe Lifecycle Designer can open. For more information, see the Prerequisites section for this procedure. |  |
| 7 | Edit Form Template | From the saved zip file, choose the FIN_FO_DUNN_NOTE (xdp file type).Open and edit the file with Adobe Lifecycle Designer and save the edited file to a local folder.Restriction A prefix of YY1_ is added to the file name. The name of the file can only have 30 characters total, that is 26 characters in addition to the 4 characters of the prefix.Note If you use multiple language templates, each language must have its own YY1_ file. | Form template file is edited as per business requirement and is ready for upload. |  |

###### Upload Custom Template

Purpose

In this activity, you upload the custom template that you created in the previous procedure.

Prerequisite

The file you created in [Download Standard Template](#unique_10) [page ] 22 is available.

|  |
| --- |
| Note In a starter system, the key user extensibility feature is deactivated. To add a new custom template in the starter system, implement [SAP Note 2283716](https://me.sap.com/notes/%20SAP%20Note%202283716). The key user extensibility feature comes activated in the Q and the P systems. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | . |  |
| 2 | Access the SAP Fiori App | Open Maintain Form Templates (F1434). | The Maintain Form Templates (F1434) view displays. |  |
| 3 | New Custom Template | From the default Custom Templates view, choose New. | The Create Form Template dialog box is displayed. |  |
| 4 | Create New Template | Make the following entries and choose OK:Form Template Name: <name of the template from previous procedure>Remember The name of the YY1_ file can't exceed 30 total characters (4 prefix characters and 26 additional characters).Language: <language used when you created the custom YY1_ file>Select Form Template File: Choose Browse to locate and choose the YY1_ file from your local folder. | In the Details section, your custom template form displays.Your new form template is ready for upload. |  |
| 5 | Return to Custom Templates Section | Choose Back. | Details of the YY1_ custom form template display in the Custom Templates section. |  |

###### Assign Form Template

Purpose

In this activity, you assign the custom form templates to the standard solution. Without this assignment, custom templates can't be used in the BRF+ configuration.

Prerequisite

The YY1_ custom template form you created in the previous procedures is available in the system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Output Management

1. For the row with Item Name of Output Control, choose Details (>).
2. For the Assign Form Templates row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Form Templates.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Assign Form Templates | Make the following entries and choose Save:In the General Section:Application Object Type: FFO_DUNNOutput Type: DUNN_NOTICEForm Template ID: <Your YY1_ template created in the previous procedures> | The new form template (for PDF/print) is created. |  |
| 3 | Go Back | Choose Back until you return to the Configure Your Solution view. |  |  |
| 4 | Assign Email Template | In the Assign Email Templates row, choose Configure. |  |  |
| 5 | New Entries | Choose New Entries. |  |  |
| 6 | Define Template | Make the following entries and choose Save:Application Object Type: FFO_DUNNOutput Type: DUNN_NOTICEEmail Template ID: FIN_FO_DUNN_NOTE_EMAIL (or your own template) |  |  |

###### Dunning Output Determination

Purpose

In this activity, you define the form template output determination for printing dunning notices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination view is displayed. |  |
| 3 | Maintain Business Rules | In the Select Business Rules section, make the following entries:Show Rules for: DunningDetermination Step: Form Template | Details display in the Maintain Business Rules section. |  |
| 4 | Add Rules | Expand the Maintain Business Rules section and choose Edit.In the Table Contents section, choose Insert New Row and make the following entries:#: <enter the next number in series>Output type: DUNN_NOTICE (Dunning Notice)Company Code: 3310Dunn.Procedure: 1001Dunning Level: 1Form Template: <Name of previously created YY1_ file>Note Since a different YY1_ file must be created for each language, continue with the instructions when you have additional YY1_ files to add.Choose Insert New Row and enter the following:#: <next higher number in series>Output Type: DUNN_NOTICE (Dunning Notice)Company Code: 3310Dunn.Procedure: 1001Dunning Level: 2Form Template: <Enter name of your second YY1_ file>For additional YY1_ files, insert additional rows and repeat the steps, giving each new YY1_ a different number for Dunning Level.Note The order of entries in the table determines the priority of the dunning form. The default template contains no restricting parameters. If it remains in the first row, it is picked for all outputs (for example, all languages). We recommend moving it to the bottom of the table as a fallback option when no other parameters fit.For example:If you maintained the dunning form templates in English and German languages in position 1 and 2 and filled in the Form Language column, the standard form template is at position 3.For English and German, the system picks the respective forms based on the Language restriction criterion. For French, it skips the first two entries and chooses the form template in position 3, since this is the first form template which without restricting criteria. | Rule data is maintained. |  |
| 5 | Activate Rules | Choose Activate and a Confirm Activation dialog box appears with a Do you really want to activate Form Template? notification.Choose Yes. | The system displays the message Objects saved and activated. |  |
| 6 | Select Business Rules | In the Select Business Rules section, make the following entries:Show Rules for: DunningDetermination Step: Channel |  |  |
| 7 | Insert New Row | Expand the Maintain Business Rules section and choose Edit.In the Table Contents section, choose Insert New Row. |  |  |
| 8 | Enter Details | Make the following entries:Output Type: DUNN_NOTICEChannel: EMAIL |  |  |
| 9 | Insert New Row | In the Table Contents section, choose Insert New Row. |  |  |
| 10 | Enter Details | Make the following entries:Output Type: DUNN_NOTICEChannel: PRINT |  |  |
| 11 | Check Activation | Choose Check. |  |  |
| 12 | Activate | Choose Activate. | The Confirm Activation dialog box displays. |  |
| 13 | Confirm | Choose Yes. | The system displays the message Objects saved and activated. |  |
| 14 | Select Business Rules | In the Select Business Rules section, make the following entries:Show Rules for: DunningDetermination Step: Email Settings |  |  |
| 15 | Insert New Row | Expand the Maintain Business Rules section and choose Edit.In the Table Contents section, choose Insert New Row. |  |  |
| 16 | Enter Details | Make the following entries:Output Type: DUNN_NOTICEEmail Template: FIN_FO_DUNN_NOTE_EMAIL (or your custom email template) |  |  |
| 17 | Check Activation | Choose Check. |  |  |
| 18 | Activate | Choose Activate. | The Confirm Activation dialog box displays. |  |
| 19 | Confirm | Choose Yes. | The system displays the message Objects saved and activated. |  |

##### BRF+ Settings for FI Customer Invoice

Purpose

In this activity, you configure the BRF+ settings for FI customer invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |  |
| 3 | Determine Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Accounting DocumentDetermination Step: Output Type | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Add Rules | Expand the Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and enter or verify the following:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: INVOICEand choose OK.From the Dispatch Time field dropdown, select Direct Value Input.Dispatch Time: 1 (Immediately)or 2 (Scheduled)and choose OK. |  |  |
| 5 | Activate | Choose Activate. Confirm the Confirm Activation dialog box by choosing Yes. | The system displays the Objects saved and activated notification. |  |
| 6 | Determine Receiver | In the Select Business Rules section, choose:Show Rules for: AccountingDocumentDetermination Step: Receiver. | Details are displayed in the Maintain Business Rules section. |  |
| 7 | Add Rules | Expand the Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: Invoiceand choose OK.In the Role field dropdown, select Direct Value Input.Role: BPand choose OK.From the Exclusive Indicator field dropdown, select Direct Value Input.Exclusive Indicator: - (false)and choose OK. |  |  |
| 8 | Activate | Choose Activate. Confirm the Confirm Activation dialog box by choosing Yes. | Rules are activated. |  |
| 9 | Determine Channel | In the Select Business Rules section, chooseShow Rules for: Accounting DocumentDetermination Step: Channel | Details are displayed in the Maintain Business Rules section. |  |
| 10 | Add Rules | If necessary, expand Maintain Business Rules section.Choose Edit.In Table Contents, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: INVOICEand choose OK.From the Mode field dropdown, select Direct Value Input.Mode: 1From the Channel field dropdown, select Direct Value Input.Channel: PRINTand choose OK.Exclusive Indicator: - (false)Choose + (Insert New Row) and enter the following:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: INVOICEand choose OK.From the Mode field dropdown, select Direct Value Input.Mode: IFrom the Output Type field dropdown, select Direct Value Input.Channel: EMAILExclusive Indicator: - (false)and choose OK. |  |  |
| 11 | Activate | Choose Activate. Confirm the Confirm Activation dialog box by choosing Yes. | Rules are activated. |  |
| 12 | Determine Form Template | In the Select Business Rules section, make the following entries:Show Rules for: Accounting DocumentDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 13 | Add Rules | Expand the Maintain Business Rules section.Choose Edit.In the Table Contents section, choose + (Insert New Row).Make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: INVOICECorr. Identifier: SAP21and choose OK.Note The Form Template column is at the far right of the table. Use the scroll bar along the bottom of the table to scroll right to display for the following two entries.From the Form Template field dropdown, select Direct Value Input.Form Template: FIN_FO_CORR_FICUS_INVand choose OK. | Rule data is entered. |  |
| 14 | Activate Rules | Choose Activate. Confirm the Confirm Activation dialog box by choosing Yes. | Rules are activated. |  |
| 15 | Determine Output Relevance | In the Select Business Rules section, make the following entries:Show Rules for: Accounting DocumentDetermination Step: Output Relevance | Details are displayed in the Maintain Business Rules section. |  |
| 16 | Add Rules | If necessary, expand the Maintain Business Rules section.Choose Edit.On Table Contents choose + (Insert New Row) and enter the following:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: INVOICEand choose OK.From the Relevance Indicator field dropdown, select Direct Value Input.Relevance Indicator: X (True)and choose OK. |  |  |
| 17 | Activate | Choose Activate. Confirm the Confirm Activation dialog box by choosing Yes. | Rules are activated. |  |
| 18 | Determine Printer Settings | In the Select Business Rules section, chooseShow Rules for: Accounting DocumentDetermination Step: Printer Settings |  |  |
| 19 | Add Rules | If necessary, expand the Maintain Business Rules section.Choose Edit .In the Table Contents section, choose + (Insert New Row) and make or verify the following entries:#: <next higher number>From the Output Type field dropdown, select Direct Value Input.Output type: INVOICEand choose OK.From the Print Queue field dropdown, select Direct Value Input.Print Queue: DEFAULT or <your system-defined output queue>Number of Copies: 1 |  |  |
| 20 | Activate | Choose Activate. Confirm the Confirm Activation dialog box by choosing Yes. |  |  |
| 21 | Email Settings | In the Select Business Rules section, choose:Show Rules For: Accounting DocumentDetermination Step: Email Settings |  |  |
| 22 | Add Rules | Choose Edit. |  |  |
| 23 | New Row | In Table Contents, choose + (Insert New Row). |  |  |
| 24 | Enter Details | Make the following entries:Output Type: INVOICESender Email: <sender email address>Corr. Identifier: SAP21Note If the Corr. Identifier column can't be found in the table, choose the Table Settings button. Choose Insert Column -> From Context Data Objects. Choose Condition Parameters of Application-> Corr. Identifier. Scroll down the list and clear selections on other objects. Choose OK. The Corr. Identifier column is then visible in the table.Email Template: FIN_CUSINV_EMAIL_TEMPL |  |  |
| 25 | Activate | Choose Activate. | The Confirm Activation dialog box is displayed. |  |
| 26 | Confirm | Choose Yes. | The rules are activated. |  |

#### Preliminary Steps for Electronic Invoicing (PEPPOL)

Purpose

To run the test procedure step e-Document Cockpit for PEPPOL United Arab Emirates, you must meet the following prerequisites:

- Define Identification Types for Business Partners
- Maintain Additional Parameters (FINSC_T001Z_N)
- Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV)
- Maintain Business Partner Master Data
- Assign Party ID Types to Business Partner (EDOEUBUPAV)
- Assign Party ID Types to Companies (EDOEUCOMPV)

##### Define Identification Types for Business Partners

Purpose

In this activity, you define the identification types for the unique ID number your business partner received from the service provider.

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

1. For the row with Item Name of Business Partner, choose Details (>).
2. For the Define Identification Types row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Identification Types.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 |  | Choose New Entries. |  |  |
| 2 |  | Make the following two entries and choose Save:Entry 1:ID Type: AELRIDDescription: Legal Registration IdentifierID Category: AELRIDOrganization: SelectedPersons: SelectedGroups: SelectedEntry 2:ID Type: AELRACDescription: Legal Registration Auth./Ctry.ID Category: AELRACOrganization: SelectedPersons: SelectedGroups: Selected |  |  |

##### Maintain Company Code Data (FINSC_T001Z_N)

Purpose

In this activity, you add tax information to the company code.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Master and Organizational Data

1. For the row with Item Name of Company and Company Codes, choose Details (>).
2. For the Maintain Additional Parameters row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Maintain Additional Parameters.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 |  | Choose New Entries. |  |  |
| 2 |  | Make the following entries and choose Save:Company Code: 3310Parameter Type: AELRID (Legal Registration Identifier)Parameter Value: <value>, for example, 123456Parameter Type: AELRAC (Legal Registration Auth./Ctry.)Parameter Value: <value>, for example, MinistryParameter Type: SAPAE1 (Tax Identification Number)Parameter Value: <value>, for example, 1234567890 |  |  |

##### Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV)

Purpose

This procedure defines the process communication through Cloud services. For a given company code, you define how an eDocument process integrates with SAP Document and Reporting Compliance, Cloud edition (using the standard integration or other types of integration) to exchange electronic documents with external communication parties.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Legal Compliance

1. For the row with Item Name of General Settings for eDocument, choose Details (>).
2. For the Define Process Communication Through Cloud Services row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Process Communication Through Cloud Services.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 |  | Choose New Entries. |  |  |
| 2 |  | Create the following entries and choose Save:Company Code: 3310BUKRS: 3310Process: AEINVSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosBUKRS: 3310Process: AEINVINSERVICE: X Cloud Edition: Peppol Exchange or Country/Region Scenarios | The process communication is created. |  |

##### Maintain Business Partner Master Data

Purpose

In this activity, you add tax information to your business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). |  |  |
| 3 | Enter Business Partner | Make the following entries and press Enter:Business Partner: <business partner number> |  |  |
| 4 | Change Mode | Choose Switch Between Display and Change to go into change mode. |  |  |
| 5 | Change BP Role | In the Change in BP Role field, select Customer (Fin.Accounting) (FLCU00). |  |  |
| 6 | Enter Details | On the Identification tab, in Tax Numbers, make the following entries and choose Save:Category: AE0Tax Number Long: <long form tax number>, for example, 123456789012345Category: AE1Tax Number Long: <long form tax number>, for example, 1234567890 |  |  |

##### Assign Party ID Types to Business Partner (EDOEUBUPAV)

Purpose

In this activity, you define the party identification types that business partners use in the PEPPOL network.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Legal Compliance

1. For the row with Item Name of Settings for Peppol, choose Details (>).
2. For the Assign Party ID Types to Business Partner row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Party ID Types to Business Partner.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 |  | Choose New Entries. |  |  |
| 2 |  | Make the following entries and choose Save:Type: C CustomerParty ID Type: AE:TINE-Mail: <select this only if the customer can't receive electronic invoices> |  |  |

##### Assign Party ID Types to Companies (EDOEUCOMPV)

Purpose

In this activity, you define the party identification types that your company uses in the exchange channels in the PEPPOL network.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Legal Compliance

1. For the row with Item Name of Settings for Peppol, choose Details (>).
2. For the Assign Party ID Types to Companies row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Party ID Types to Companies.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 |  | Choose New Entries. |  |  |
| 2 |  | Make the following entries and choose Save:Company Code: 3310Party ID Type: AE:TIN |  |  |

##### Optional Steps for Electronic Invoicing (PEPPOL)

###### Business Partner Master Data Maintenance for Electronic Invoicing (Optional)

Purpose

In this activity, you add the identification number and tax number category for customer master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). |  |  |
| 3 | Enter Business Partner | Make the following entries and press Enter:Business Partner: <business partner number>, for example, 33100003 |  |  |
| 4 | Change Mode | Choose Switch Between Display and Change to go into change mode. |  |  |
| 5 | Change BP Role | In the Change in BP Role field, select Customer (Fin.Accounting) (FLCU00). |  |  |
| 6 | Enter Details | On the Identification tab, in Identification Numbers, make the following entries and choose Save:ID Type: AELRIDIdentification Number: <ID number>, for example, 123456 |  |  |

###### Value Mapping Maintenance for Electronic Invoicing (Optional)

Purpose

In this activity, you maintain the value mapping for eDocument UBL

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Configure Value Mapping (/AIF/VMAP_CONF). |  |  |
| 3 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_ALLOW_COND_TYPE | The Display Value Mapping view is displayed. |  |
| 4 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 5 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Reason Code: <number of code>, for example, 95Reason Description: <code description>, for example, DiscountCondition Type: <condition type>, for example, YK07Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 6 | Back | Choose Back. |  |  |
| 7 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_CHARGE_COND_TYPE | The Display Value Mapping view is displayed. |  |
| 8 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 9 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Reason Code: <number of code>, for example, RVReason Description: <code description>, for example, LoadingCondition Type: <condition type>, for example, DRV1Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 10 | Back | Choose Back. |  |  |
| 11 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_DISTR_CHANNEL | The Display Value Mapping view is displayed. |  |
| 12 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 13 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Reason Code: <number of code>, for example, 60Sales Org.: <value>, for example, 3310Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 14 | Back | Choose Back. |  |  |
| 15 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_LEGAL_FORM | The Display Value Mapping view is displayed. |  |
| 16 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 17 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Invoice Code: <number of code>, for example, 1Legal Form: <form value>, for example, FZMaintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 18 | Back | Choose Back. |  |  |
| 19 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_PAYM_MEANS_CODE | The Display Value Mapping view is displayed. |  |
| 20 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 21 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Value: <value>, for example, 1Payment Method: <payment method>Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 22 | Back | Choose Back. |  |  |
| 23 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_TAX_CATEGORY | The Display Value Mapping view is displayed. |  |
| 24 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 25 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Value: <index number>Tax Code: <tax code>Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 26 | Back | Choose Back. |  |  |
| 27 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_TAX_EXEMPT_CODE | The Display Value Mapping view is displayed. |  |
| 28 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 29 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Value: <index number>Tax Code: <tax code>Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 30 | Back | Choose Back. |  |  |
| 31 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_PROFIT_MARGIN_PP | The Display Value Mapping view is displayed. |  |
| 32 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 33 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Pricing Procedure: <pricing procedure>Sales Org: 3310Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 34 | Back | Choose Back. |  |  |
| 35 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_RVS_CHRG_MECH | The Display Value Mapping view is displayed. |  |
| 36 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 37 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Value: <index number>Material Group: <material group>Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 38 | Back | Choose Back. |  |  |
| 39 | Enter Namespace and Value Mapping | Make the following entries and choose Execute:Namespace: /EDUBLValue Mapping: AE_ITEM_CATEGORY_SD | The Display Value Mapping view is displayed. |  |
| 40 | Change Mode | Choose the Switch Between Display and Change to go into change mode. | The Change Value Mapping view is displayed. |  |
| 41 | Maintain Value Mapping | Choose Append.Choose the append number, then maintain the following information:Value: <yes/no>Item Category: <item category>Maintain all value mappings in the next line items.Choose Save after maintaining the necessary entries. |  |  |
| 42 | Back | Choose Back. |  |  |

#### Number Range to Business Places Assignment for a New Fiscal Year

Purpose

In this procedure, you verify that a number range is assigned for a new fiscal year. Steps 1–8 of this activity are to verify that the number range is assigned. When the number range isn't assigned for a new fiscal year, you complete step 9 to configure the Number Range to Business Places for a new fiscal year.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Assign Number Ranges to Business Places.
6. For the Assign Number Ranges to Business Places for Official Doc. Numbering MENA row, choose Configure.
7. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Number Ranges to Business Places for Official Doc. Numbering MENA.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Verify Values for Current Fiscal Year | Verify the following entries:CoCd: 3310Document Class: ACMDate: <Beginning of Current Year>Exp.date: <End of Current Year>Prefix:20No.gp: ACM001No.: 01CoCd: 3310Document Class:AINDate: <Beginning of Current Year, for example, 01/01/2020>Exp.date: <End of Current Year, for example, 12/31/2020>Prefix:10No.gp: AIN001No.: 01Note If values for the new fiscal year do not appear in the list, you proceed to the next step. If the values for the new fiscal year do appear, choose Cancel to return to the previous view. |  |  |
| 2 | Add Values for New Fiscal Year | If the values for the new fiscal year don't appear in the list, choose New Entries to add.Make the following entries:First line:CoCd: 3310Document Class:ACMDate: <Beginning of New Fiscal Year>Exp.date: <End of New Fiscal Year>Prefix:20No.gp: ACM001No.: 01Second line:CoCd: 3310Document Class:AINDate: <Beginning of New Fiscal Year, for example, 01/01/2020>Exp.date: <End of New Fiscal Year, for example, 12/31/2020>Prefix:10No.gp: AIN001No.: 01and choose Save from the bottom of the view. | New fiscal year values added. |  |

Result

The assignment of the number range to the business place is active for the current fiscal year.

#### Manage Situation Types (Optional)

Purpose

As an optional activity, customers can create a situation type as a copy of the situation template. Situation types allow you to manage the different circumstances that are critical to your business processes by automatically notifying the right users either as soon as a situation occurs or at a defined time. Situation types create situation instances, send notifications, and display the situation message, including related information, in the corresponding app.

In this activity, you create an invoice skipped situation type for the [Manage Payment Advice](#unique_26) [page ] 114 test procedure under the Incoming Payments with Electronic Bank Statement section.

The purpose of this situation is to notify users about accounts receivable payment advices that appear to have skipped a high-value invoice or invoices within the due date range of invoices covered. For example, if ten invoices are payable at the end of a month and only nine are mentioned on the payment advice, it indicates to the relevant Accounting Clerk that they may want to contact the affected customer for the balance. The situation is only initialized if the excluded invoices comprise more than 50% of the total balance due within the given date range (that is, only if the potentially missing amount is significant). Only debit items are considered. The situation can only map payment advice items to accounts receivable open items using the invoice reference numbers, so it may not function properly for manual invoices, debit notes, or similar.

Standard Templates and Ready-to-Use Situation Types

Standard templates are predefined by SAP.

Standard templates can only be copied, although the copy becomes a ready-to-use situation type that you adapt and enable for productive use.

Ready-to-use situation types can be copied, edited, enabled, disabled, and deleted. When you delete a ready-to-use situation type, all related instances and monitored data are also deleted.

Situation types can be translated into various languages. The texts for the standard templates are already translated into a set of languages that can serve as a basis for your translations.

|  |
| --- |
| Note Ensure that Situation Handling (31N) is activated first if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). |  |  |
| 3 | Select Type | Choose the Situation Templates tab.Choose Go. | The Situation Type view displays. |  |
| 4 | Select a Template | Select the checkbox for the row of FIN_PAYMENTADVICEINVOICESKIPPED, and then choose Copy. | A New Situation Type view displays. |  |
| 5 | Maintain Admin Information | Make the following entries:ID: ZFIN_PAYMENTADVICEINVOICESKIPPEDNote The Z in the ID, indicates that you've created this copy of the template.Name: An Invoice is skipped in Payment AdviceDisplay Sequence: Medium is default, with setting from Very High to Very Low | The situation type is maintained. |  |
| 6 | Maintain Situation Display | In the Situation Display area, enter the following:In-App Situation Message section:Short Description: <use default>Details: <use default>Notification Message area:Secure Text: <use default>Public Text: <use default>Resend Notifications: <use default>, Selected. |  |  |
| 7 | Save | Choose Create.Confirm the Do you want to enable the situation type? message by choosing Yes. |  |  |

#### Add Fields to Items (Optional)

Use

As an option, the administrator adds data source extensions and field names to Manage Customer Line Items (F0711). This option allows making more user fields available when managing items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Custom Fields (F1481). |  |  |
| 3 | Create New Extension | Choose the Data Source Extensions tab.Choose the + (Create) button. | A New Data Source Extension dialog box displays. |  |
| 4 | Enter Properties | Enter the following and choose Create:Data Source: Customer Line ItemsDescription: <description of the data source>Extension ID: The description is automatically added to the ID | A view displays of the new data source extension. |  |
| 5 | Add Fields | Choose the < > (Toggle Field Path) button to switch the Field Path so Item displays at the top of the table. Under the Field Selection tab, expand the Item node and other nodes in the table and select the items to add.Note Ensure that your choices are under the _Customer node. | Selected items display in the Selected Fields column. |  |
| 6 | Save | Choose the Save button. | All the nodes of the Field Path table collapse and your selections display in the Selected Fields table. |  |
| 7 | Publish | Choose the Publish button. | The Data Source Extensions view of Custom Fields and Logic displays with all the extensions. To verify your new extension, use the Search field. |  |

#### Manage Default Account Assignments

Purpose

In this activity, you manage default account assignments. This prerequisite is used in the [Mass Import of Customer Invoices](#unique_29) [page ] 70 topic.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Settings

1. For the row with Item Name of Journal Entries, choose Details (>).
2. For the Manage Default Account Assignments row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage Default Account Assignments.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. | The "Manage Default Account Assignments": Change view is displayed. |  |
| 2 | Enter Details | Make the following entries and choose Save:CoCd: <company code>Cost Elem.: <cost element>, for example, 41000400PrfSeg: Selected | Note Use the revenue accounts you plan to use in the template XLS file from the [Mass Import of Customer Invoices](#unique_29) [page ] 70 topic. Make these entries for each company code. |  |

#### Assign Reason Codes For Write-Off

Purpose

In this activity, you assign a reason code to write off bad debts. This preliminary step is required for the [Bad Debt Write-Off](#unique_31) [page ] 139 test procedure step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accounts, choose Details (>).
2. For the Automatic Account Determination row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app.
3. Search for the Automatic Account Determination activity and choose Go to Activity to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
4. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Details | In the 1. Area section, make the following entries and choose Step 2:Area: Financial AccountingSubarea: Accounts Receivable and Accounts PayableProcess: Define Accounts for Payment Transactions |  |  |
| 2 | Enter Details | In the 2. Parameters section, make the following entries and choose Step 3:Transaction Key: ZDIChart Of Accounts: YCOA |  |  |
| 3 | Edit Rules | In the 3. Account Assignments section, choose Edit Rules. | The Edit Rules dialog box is displayed. |  |
| 4 | Reason Code | Select the Reason Code checkbox and choose OK.Note For certain countries/regions who use VAT or have specific tax requirements, you can select the Tax Code checkbox to make the field available for those use cases. |  |  |
| 5 | Add | Choose Add. | A new row is added below the existing row. |  |
| 6 | Reason Code and Accounts | Make the following entries and choose Review:Reason Code: <reason code>, for example, 200G/L Account - Debit: <debit account>, for example, 62010000G/L Account - Credit: <credit account>, for example, 62010000 |  |  |
| 7 | Save | Review your entries. Once done, choose Save. |  |  |

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

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Preparation of Payments

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Business Partners](#unique_36) [page ] 63 | Accounts Receivable Accountant | Maintain Business Partner (BP) | Customer Master Data is created. |
| [Maintain Business Partner Certificate](#unique_37) [page ] 65 | Accounts Receivable Accountant or Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | You maintained the business partner certificate. |
| [Display Customer List](#unique_38) [page ] 67 | Accounts Receivable Accountant | Display Customer List (F2640) | Customer List is created. |

Enter Invoice without Sales Order

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Enter Invoice Without Sales Order](#unique_39) [page ] 68 | Accounts Receivable Accountant | Create Outgoing Invoices (FB70) | Invoice is created. |

Mass Upload

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Mass Import of Customer Invoices](#unique_29) [page ] 70 | Accounts Receivable Accountant | Upload Customer Open Items (F4051) | Customer invoices are imported. |

Invoice Reporting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Dunning Notices](#unique_40) [page ] 73 | Accounts Receivable Accountant | Dunning history displays. | Dunning history displays. |
| [Manage My Dunning Proposals](#unique_41) [page ] 75 | Accounts Receivable Accountant | My Dunning Proposals (F2435) | Dunning proposal is created, managed. |
| [Display Dunning History](#unique_42) [page ] 77 | Accounts Receivable Accountant | Display Dunning History (F2328) | Dunning history is displayed. |
| [Open Correspondence](#unique_43) [page ] 78 | Accounts Receivable Accountant | Create Correspondence (F0744A) or Manage Journal Entries (F0717A) | Correspondence is created. |
| [Display Correspondence History](#unique_44) [page ] 81 | Accounts Receivable Accountant | Display Correspondence History (F2934) | Correspondence history is displayed. |

Invoice Management Reporting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Accounts Receivable Overview](#unique_45) [page ] 82 | Accounts Receivable Manager | Accounts Receivable Overview (F3242) | Figures and statistics display according to available options. |
| [Monitor Overdue Receivables](#unique_46) [page ] 83 | Accounts Receivable Manager | Overdue Receivables - Today (F1747) | The app returns a graphical overview for the overdue receivables. |
| [Monitor Overdue Receivables by Risk Class](#unique_47) [page ] 84 | Accounts Receivable Manager | Overdue Receivables - by Risk Class (F2539) | A graphical overview for the overdue receivables displays. |
| [Future Receivables](#unique_48) [page ] 85 | Accounts Receivable Manager | Future Receivables - Today (F1744) | A graphical overview for the future receivables displays. |
| [Total Receivables](#unique_49) [page ] 86 | Accounts Receivable Manager | Total Receivables - Today (F1748) | A graphical overview for the total receivables displays. |
| [Days Sales Outstanding](#unique_50) [page ] 87 | Accounts Receivable Manager | Days Sales Outstanding - Last 12 Months (F1741) | An overview of Days Sales Outstanding report displays. |
| [Dunning Level Distribution](#unique_51) [page ] 88 | Accounts Receivable Manager | Dunning Level Distribution - Today (F1742) | A graphical overview for the dunning level distribution displays. |
| [Days Beyond Terms](#unique_52) [page ] 89 | Accounts Receivable Manager | Days Beyond Terms - Last 12 Months (F1739) | A graphical overview for the days beyond terms displays |
| [Display Item Change Log](#unique_53) [page ] 90 | Accounts Receivable Manager | Display Item Change Log - Customer (F7796) | Display logged changes for journal entries. |
| [Cash Collection Tracker](#unique_54) [page ] 91 | Accounts Receivable Accountant | Cash Collection Tracker - Accounts Receivable (F2925) | Cash Collection Tracker Accounts Receivable is generated. |

Down Payments

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Down Payment Request](#unique_55) [page ] 92 | Accounts Receivable Accountant | Manage Customer Down Payment Requests (F1689) | A journal entry is posted. |
| [Display Down Payment Request](#unique_56) [page ] 94 | Accounts Receivable Accountant | Manage Customer Down Payment Requests (F1689) | A list of down payment requests displays. |
| [Post Down Payment](#unique_57) [page ] 95 | Accounts Receivable Accountant | Post Incoming Payments (F1345) | The payment is posted. |
| [Enter Invoice Without Sales Order](#unique_58) [page ] 97 | Accounts Receivable Accountant | Create Outgoing Invoices (FB70) | Invoice is created. |
| [Post Incoming Payments](#unique_59) [page ] 98 | Accounts Receivable Accountant | Post Incoming Payments (F1345) | The payment is posted. |
| [Clear Incoming Down Payments](#unique_60) [page ] 100 | Accounts Receivable Accountant for United Arab Emirates | Clear Incoming Down Payments - Clear Incoming Down Payments (F8969) | You cleared the invoice. |
| [Clear Open Items Manually](#unique_61) [page ] 101 | Accounts Receivable Accountant | Clear Incoming Payments - Manual Clearing (F0773) | The item is manually cleared. |

Incoming Payments

Incoming Payment with Electronic Bank Statement

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Daily Cash Operations – Bank Statement](#unique_62) [page ] 103 |  | Follow the steps in the Bank Statement test procedure of the Basic Cash Operations (BFB) test script. |  |
| [Cash Application Intelligence Integration](#unique_63) [page ] 104 |  | Follow the procedures described in the Cash Application Integration (1MV) test script | Improvement to Cash Application Intelligence is realized. |
| [Reprocess Bank Statement Items](#unique_64) [page ] 104 | Cash Management Specialist | Reprocess Bank Statement Items (F1520) | The items are processed. |
| [Manage Enrichment Rules for Bank Statement Processing (Optional)](#unique_65) [page ] 108 | Cash Management Specialist | Manage Enrichment Rule Sets - For Bank Statements (F9062) | You created enrichment rules. |
| [Manage Value Extraction for Bank Statements (Optional)](#unique_66) [page ] 109 | Cash Management Specialist | Manage Values Extraction Rules - For Bank Statements (F9297) | You managed the value extraction rules. |
| [Manage Bank Statement Processing Rules (Optional)](#unique_67) [page ] 110 | Accounts Receivable Accountant | Manage Processing Rules - For Bank Statements (F3555) | A reprocessing rule is created. |
| [Obtain Payment Advices Manually (Optional)](#unique_68) [page ] 113 | Accounts Receivable Accountant | This operation occurs outside of the system. | Payment advices are received. |
| [Manage Payment Advice](#unique_26) [page ] 114 |  | Manage Payment Advices - Deprecated (F2550) | Payment advices are created, changed, or deleted. |
| [Clear Credit/Debit Memos Manually](#unique_69) [page ] 117 | Accounts Receivable Accountant | Clear Incoming Payments - Manual Clearing (F0773) | Items are cleared. |

Incoming Payment without Electronic Bank Statement

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Incoming Payments](#unique_70) [page ] 119 | Accounts Receivable Accountant | Post Incoming Payments (F1345) | Items are posted. |

Incorrect Posting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Reset Cleared Items](#unique_71) [page ] 121 | Accounts Receivable Accountant | Reset Cleared Items (F2223) | A cleared document is reset. |
| [Reset and Reverse Cleared Items](#unique_72) [page ] 122 | Accounts Receivable Accountant | Reset Cleared Items (F2223) | A document is reset and reversed. |
| [Schedule Jobs to Reset Cleared Items (Optional)](#unique_73) [page ] 123 | Accounts Receivable Accountant | Schedule Jobs to Reset Cleared Items (F9296) | You scheduled the job to reset cleared items. |
| [Reverse Individual Documents](#unique_74) [page ] 125 | General Ledger Accountant | Manage Journal Entries (F0717A) | A document is reversed. |

Invoice Collection Preparation

|  |  |  |  |
| --- | --- | --- | --- |
| Process Step | Business Role | Transaction/App |  |
| [Display Customer Balances](#unique_75) [page ] 126 | Accounts Receivable Accountant | Display Customer Balances (F0703A) | A table of customer balances displays. |
| [Manage Customer Line Items](#unique_76) [page ] 127 | Accounts Receivable Accountant | Manage Customer Line Items (F0711) | Customer line items are edited |

Interest Calculation

|  |  |  |  |
| --- | --- | --- | --- |
| Process Step | Business Role | Transaction/App |  |
| [Schedule Interest Calculation Jobs](#unique_77) [page ] 129 | Accounts Receivable Accountant | Schedule Interest Calculation Jobs (F4176) | You scheduled the interest calculation jobs. |
| [Manage Interest Runs](#unique_78) [page ] 131 | Accounts Receivable Accountant | Manage Interest Runs (F4485) | You managed the interest runs. |
| [Display Interest Runs](#unique_79) [page ] 132 | Accounts Receivable Accountant | Manage Interest Runs (F4485) | You displayed the interest runs. |

Guarantees Made

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Guarantees Made](#unique_80) [page ] 133 | Accounts Receivable Accountant | Manage Guarantees Made (F7934) | You created the guarantee. |
| [Reverse Guarantees](#unique_81) [page ] 134 | Accounts Receivable Accountant | Manage Guarantees Made (F7934) | You reversed the guarantee. |

Periodic Activities

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Check Open Balances](#unique_82) [page ] 135 |  |  | Open balances are reviewed. |
| [Create Balance Confirmation](#unique_83) [page ] 135 | Accounts Receivable Accountant | Schedule Accounts Receivable Jobs (F2366) | Balance Confirmation is managed. |
| [Manage Balance Confirmations](#unique_84) [page ] 137 | Accounts Receivable Accountant | Manage Balance Confirmations - For Customers (F2834) | Balance Confirmation is generated. |
| [Print Customer Balance Confirmation](#unique_85) [page ] 138 | Accounts Receivable Accountant | Manage Balance Confirmations - For Customers (F2834) | Balance Confirmation is printed. |
| [Bad Debt Write-Off](#unique_31) [page ] 139 | Accounts Receivable Accountant | Write Off Receivables (F6728) | Unrecoverable items are written off. |

Table 3: eDocument Cockpit

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [eDocument Cockpit](#unique_86) [page ] 141 | Billing Clerk | eDocument Cockpit (EDOC_COCKPIT) | You checked the eDocument status. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Preparation of Payments

#### Maintain Business Partners

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you assign a dunning procedure to a customer to be able to execute the Collections Management procedure.

Prerequisites

- Accounting clerk is defined with User ID assigned. For more information, see the [Define Accounting Clerk](#unique_7) [page ] 10 step.
- The customer master record is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). |  |  |
| 3 | Select Customer | Make the following entries and choose Start:Find: Business PartnerBy: NumberBusiness Partner: 33100001From the list that displays, double-click the row of the Business Partner result. | The Display Organization : <number> view displays. |  |
| 4 | Change Role | Make the following entry:Display in BP role: Customer(Fin. Accounting) | The Display Organization : <number> role FI Customer view displays. |  |
| 5 | Edit Customer | Choose Switch between Display and Change to change the data to update. |  |  |
| 6 | Company Code Data | Choose Company Code at the top.Choose the Customer: Account Management tab.Make the following entries:Interest Indicator: 01Choose the Customer: Correspondence tab. |  |  |
| 7 | Define Accounting Clerk | In the Correspondence section, choose the button next to the Accounting Clerk entry to search by accounting clerk abbreviations.A Clerk Abbreviation dialog box displays the available accounting clerks by name and abbreviation code.Select the row with <Tester> (your name) and choose Copy.Note The <Tester> of this procedure was previously defined as the accounting clerk. For more information, see the [Define Accounting Clerk](#unique_7) [page ] 10 step. | The accounting clerk is changed. |  |
| 8 | Define Dunning | In the Dunning Data section, make the following entries:Dunning Procedure: 1001Dunning Block: Not blockedDunning Clerk: <Tester>Note The <Tester> name entered as a dunning clerk must be the same name used in the previous step for accounting clerk.Clrk's Internet add.: <Email address for clerk (recipient of dunning letter)> | The dunning procedure is assigned. |  |
| 9 | Save | Choose Save. | Changes are saved. |  |
| 10 | Navigation | Using the Switch between Display and Change tab, change or display other master data settings, change the BP role, and navigate through the available tabs. Review the following areas:Display in BP role: Business Partner (Gen.) or Customer (FI.Accounting)and apply any changes, as required. | Settings display according to the chosen business partner role. Edit setting to your requirements. |  |
| 11 | Save Customer | Choose Save after completing your changes. |  |  |

#### Maintain Business Partner Certificate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The companies doing business in your country/region must have certificates issued by the legal authorities. The Business Partner Certificates functionality enables you to maintain the certificate details of your business partner (customer and supplier) in new tabs and information about the certificate's validity. You can use these certificate details in your business processes, such as invoicing and payments.

Prerequisites

Ensure that you have completed the following preliminary steps:

- [Activate Business Partner Certificates Functionality](#unique_32) [page ] 54
- [Define Business Partner Certificate IDs](#unique_33) [page ] 55
- [Assign Business Partner Certificates to Country/Region](#unique_34) [page ] 56

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant or a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). |  |  |
| 3 | Select Customer | Make the following entry and press Enter:Business Partner: 33100001 | The Display Organization: 33100001 view is displayed. |  |
| 4 | Change BP Role | Enter the following values:Display in BP role: Customer (Fin. Accounting) | The Display Organization: 33100001 Role Customer (Fin. Accounting) view is displayed. |  |
| 5 | Edit Customer | Choose the Switch between Display and Change button to change the data and update. | The Business Partner Master Data is available for editing. |  |
| 6 | Certificate Tab | In the Customer General Data view, choose the Certificates tab.Note This tab is only visible if you are activating business partner certificates for the FI Customer business partner role. |  |  |
| 7 | Add Customer Certificate | Choose Insert Row and make the following entries:Country/Region:<country/region>Certificate ID:<certificate ID>Certificate No.: <certificate number>Valid From: <start date of certificate validity>Valid To: <end date of certificate validity>Region: <region>Main Certificate: Selected | The business partner certificate is added to customer 33100001. |  |
| 8 | Save | Choose Save. | Changes are saved. |  |

#### Display Customer List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can quickly access customer master data information and for validation purposes (for example, identify fields with missing data by checking for blanks).

Prerequisites

Business partners are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Customer List (F2640). | The Display Customer List view is displayed. |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Company Code: 3310Customer: 33100001 (optional) | An Items table displays with information of the Business Partner such as:• Company Code• Customer• City• Phone• E-Mail• Clerk Abbreviation• Financial Payment Terms• Dunning Procedure• Dunning Block |  |
| 4 | Explore Other Views | Click the blue link for a customer name in the Name of Customer column. The Customer Details dialog box displays information about the customer.Click the blue link for a customer in the Customer column. The dialog box displays a list of links for additional process functions, for example, Clear Incoming Payments, Process Receivables, and so on. | The customer detail information is displayed. |  |

### Enter Invoice Without Sales Order

#### Enter Invoice Without Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, customer invoices are posted in accounting and journal entries are created.

Prerequisites

Customer master record has been entered.

Ensure that the Number Range to Business Places Assignment for a New Fiscal Year procedure under the Preliminary Steps section of the Prerequisites has been completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Outgoing Invoices (FB70). | The Enter Customer Invoice: Company Code # view displays. |  |
| 3 | Company Code | Choose Company Code. | The Enter Company Code dialog box is displayed. |  |
| 4 | Company Code | Enter or verify your company code (3310) and choose Continue. |  |  |
| 5 | Basic Data | Make the following entries:Customer: <customer number>Invoice date: <Today’s date>Reference: <any>Posting Date: <Today’s date>Amount: <any> and AED.Currency Key: <company code currency>Calculate Tax: SelectedBusiness Place: DXB |  |  |
| 6 | Payment Tab | Choose the Payment tab and enter the following:Bline Date: Today’s datePmnt Terms: 0001Payt Meth.: <optional> |  |  |
| 7 | Line Items | Scroll down and enter the following in the line item table:G/L Acct: 41000400D/C: CreditAmount in doc. curr.: <Check amount that was entered in the basic data>Tax Code: <output tax code> |  |  |
| 8 | Profitability Segment | Continue in the Items table and for the Profit.segment column, select the field button. | The Assignment to a Profitability Segment dialog box is displayed. |  |
| 9 | Profitability Segment | Make the following entries and choose Derivation:Customer: <customer number>Make the following entries and choose Continue:Profit Center: <any> | The dialog box closes and you return to the Enter Customer Invoice view. |  |
| 10 | Post | Choose Post to save. | Journal Entry is posted. |  |

### Mass Upload

#### Mass Import of Customer Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app is used when there are many outgoing invoices and accruals.

Prerequisite

Create an electronic spreadsheet with the invoice details to be uploaded (with a maximum of 500 items in a single file).

Business Partner (BP) master data exists.

Ensure that you completed the [Manage Default Account Assignments](#unique_28) [page ] 51 topic in Preliminary Steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Upload Customer Open Items (F4051). |  |  |
| 3 | Download | Choose Download (Download Template) to download the spreadsheet template and choose:Template Language: For example, EnglishFormat: For example, *.xlsx, for MS Excel WorkbookChoose Download to continue. |  |  |
| 4 | Enter Details | Enter the following content into the template data sections:Note The template has hidden columns. If you don't see a field, unhide the columns as needed.Note Ensure that you use the correct date format in the template.Header data sectionDocument Sequence Number: <sequence number, increasing sequentially> (you must enter this manually)Company Code (4):3310Transaction (1): 1 (invoice) or 2 (credit memo)Customer (10): 33100001Reference (16): <any text with maximum number of 16 characters>Document Date: <Today's date MM/DD/YYYY>Posting Date: <Today's date MM/DD/YYYY>Document Type (2): DR (invoice) or DG (credit memo)Document Header Text (25): <any text with maximum number of 25 characters>Transaction Currency (5): AEDGross Invoice Amount: 1050Business Place (4): DXBG/L Account Items sectionG/L Account (10): For example, 41000400Item Text (50): <any text with maximum number of 50 characters>Debit/Credit (1) S=Debit, H=Credit: S (Debit) or H (credit)Item Amount: For example, 1050Note The Item Amount field may have a different value, depending on, where applicable, the chosen Tax Code.Tax Code (2): V2Profit Center (10): YB700Reporting Segment: <reporting segment> (optional; if left blank, the system derives the value from master data)Functional Area: <functional area> (optional; if left blank, the system derives the value from master data) |  |  |
| 5 | Upload | To upload a file, choose Browse and select the file to upload. | File is uploaded and the Worklist section displays Inv. Status Draft for items uploaded. |  |
| 6 | Check | Select the checkbox of the documents to be checked and choose Check. | Any items containing errors are identified in the Invoice Status column with red icons. Otherwise, a green flag icon displays for correct entries. |  |
| 7 | Review the Log | To view log, select the checkbox of the documents and choose Show Log. | Details of logs are displayed. |  |
| 8 | Correct any Errors | Select the item to review and correct any errors. | Customer invoice application is displayed showing details of uploaded item.The Draft Status column changes to a green flag icon after correcting the error and returning to the worklist. |  |
| 9 | Correct any Errors in Customer Invoice Application | If the customer invoice application reveals any errors, correct those errors and return to the worklist. |  |  |
| 10 | Post | Select the checkboxes for the documents to post and choose Post. | Items are posted.Note To view posting details, choose the View Application Jobs button. |  |

### Invoice Reporting

|  |
| --- |
| Note SAP offers the following two scope items for collections and disputes, both of which require additional licenses.Collections and Dispute Management (BFC)Collections and Dispute Automation (7MA)If you implemented either of these, perform the steps in the appropriate test script.If you haven't implemented either of these, continue with the procedures in this test script. |

#### Create Dunning Notices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create and schedule a dunning run and print dunning notices to customers. The activity is considered automatic as the system selects the overdue open items, determines the dunning level of the accounts in question, and creates dunning notices.

This activity finds items to dun for all customers assigned to a dunning clerk, accounting clerk, and a dunning procedure.

Two dunning procedures are provided:

- 1001 - Dunning notice every 14 days, 4 dunning levels
- 1002 - Dunning notice, 30 days after the invoice has been created

Prerequisites

- Maintain customer master data, role FLCU00 Customer Fin Accounting, Company Code 3310, Customer Correspondence tab:
    - Assign dunning procedure: 1001
    - Assign Accounting Clerk and Dunning Clerk (if different, Dunning Clerk has higher priority): 01
    - Dunning block isn't set for customer
    - There are invoices past due
- Ensure that the Dunning history for the last dunning run is 14 days old or older, otherwise no dunning proposal is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Dunning Notices (F150). | The Dunning view displays. |  |
| 3 | Create Dunning Run | On the Status tab, make the following entries:Run on: <today's date>Identification: for example, 001Choose the Parameter tab and make the following entries:Dunning date: <today's date>Docmts Posted Up To: <today's date>Company Code: 3310Customer: 33100001 |  |  |
| 4 | Save Parameters | Choose Save at the bottom of the view. |  |  |
| 5 | Schedule Dunning Run | Choose the Status tab.Choose Schedule at the top of the view.In the dialog box, make the following entries and choose Continue:Output device: LP01 | A Schedule Selection and Print dialog box displays. |  |
| 6 | Enter Job Parameters | Make the following entries and choose Dispatch:Start date: <today's date>Start time: <leave as is>Start immediately: checkDunn. Print with Scheduling: SelectedOutput device: LP01 | The Status view displays.The Select and print Running status displays.No dunning notices generated to be sent.No dunning notices printed.A notification displays at the bottom of the view that the dunning job was scheduled successfully. |  |
| 7 | Print Dunning List | Choose Refresh from the bottom of the view.Select Dunning list.In the dialog box that appears, enter or verify the following:Program: RFMAHN21Choose Continue. | The Dunning Proposal displays. |  |
| 8 | Sample Printout | After you completed your review the Dunning list, choose the < (Back) button.Choose the Sample printout tab.If an Output Parameters dialog box appears, enter the following:Output Device: LP01and choose Continue. | A Schedule Sample Printout dialog box displays. |  |
| 9 | Schedule Sample Printout | On the Job parameters section, make or verify the following entries:Start date: <today's date>Start immediately: SelectedOn the Printout section, make or verify the following entry:Output device: LP01On the Customer (from/to) section, make the following entry:Customer: 33100001and choose Display. | A document in PDF format displays and all items dunned display in the dunning notice. |  |
| 10 | Dunning History | After you completed your review the document, choose the < (Back) button to return to the Dunning view.Choose the More tab to display a dropdown menu of available options.For example, choose Goto > Dunn. History and the FI Dunning - Dunning History view displays.Make the following entries:Account type: DCompany code: 3310Customer: 33100001and choose Execute from the bottom of the view. | The dunning history displays with a list of dates when the customer was dunned. |  |

#### Manage My Dunning Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes creating dunning proposals, and printing and emailing dunning notices to customers.

In this activity, you create dunning proposals for all customers assigned to a dunning clerk, accounting clerk, or to a dunning procedure.

Two dunning procedures are set up:

- 1001 - Dunning notice every 14 days, 4 dunning levels
- 1002 - Dunning notice, 30 days after the invoice has been created

Prerequisites

- Maintain customer master data role Customer Fin Accounting, Company Code 3310, Correspondence tab:
    - Assign dunning procedure : 1001
    - Assign Accounting Clerk and Dunning Clerk (if different, Dunning Clerk has higher priority) : 01 For more information, see the [Define Accounting Clerk](#unique_7) [page ] 10 step.
    - Ensure that a dunning block isn't set for the customer
    - Ensure that there are invoices past due
- Verify in the dunning history that the last dunning run is 14 days old or more - otherwise no dunning proposals are created
- Dunning proposals initiated from outside the app should create separate dunning runs for each dunning clerk. Dunning runs for multiple clerks can't be processed and remain in the app.

|  |
| --- |
| Caution If you already created dunning notices and there's nothing to dun for the customer, this app won't create any dunning proposals. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open My Dunning Proposals (F2435). | A dialog box displays a list of all the dunning proposals with information of customer, company code, value, and other fields. |  |
| 3 | Dunning | Select Create Dunning Proposal and choose Create. | A message displays that the dunning proposal is now being created and the dunning proposals are created. |  |
| 4 | Notice | To preview the dunning notice, select the checkbox of the row to view the preview notice.In the Preview Notice column, select Preview Notice.A PDF icon is displayed in the Preview Notice column.When done checking the notice, choose Close at the bottom of the notice view. | The Dunning Notice displays on the view with options to download, print, zoom, or set a dunning block. |  |
| 5 | Printing | Choose the Send Dunning Notices option at the bottom of the view.Note Dunning notices are created for all proposals, regardless of individual row selection.A Send Dunning Notices dialog box is displayed, providing two options. Select Send dunning notices to the printer and choose Send.A new field with a unique ID of the queue appears. Select the printer from the dropdown menu and choose Send. | Dunning is printed and customer master is updated in the Company code → Correspondence tab. |  |
| 6 | Set Dunning Block | Review the line item and select the Set Dunning Block. The following options appear :DisputedPromise to PayTo be Clarified with Sales DepartmentLegal DepartmentOther ReasonSelect one of the options and a message appears that the dunning block was set successfully. In the Dunning Block column of the list, a letter that identifies the option of the dunning block is displayed. | Dunning block is set for the line item. |  |

#### Display Dunning History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the dunning history is displayed.

Prerequisites

At least one dunning letter has been generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Dunning History (F2328). | The Dunning History view displays. |  |
| 3 | Search Criteria | Select your desired search criteria and choose Go. | A list of dunning notices displays. |  |
| 4 | Show Details | Select the row of a dunning notice to display and choose Show Details. | The Dunning Notice view with all details is displayed. |  |

#### Open Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create open items correspondence. There are two options for this procedure:

When choosing correspondence SAP09 (Internal Document), a journal entry number is necessary before executing the report. We recommend that you use Procedure B and the Manage Journal Entries (F0717A) SAP Fiori app to find a journal entry number and then create the correspondence.

For the other correspondence reports, use Procedure A.

Prerequisite

Invoices and payments are posted.

Business Partner (BP) master data (such as email address, and so on) are updated.

Procedure A - Create Correspondence

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Correspondence (F0744A). |  |  |
| 3 | Select | Make the following entries:Company Code: 3310Correspondence: Select any of the following reports:SAP06 (Account Statement)SAP08 (Open Item List)SAP09 (Internal Document)SAP13 (Customer Statement)SAP21 (FI Customer Invoice)Note Only when selecting the SAP09 report, follow the steps in Procedure B. | Report is selected. |  |
| 4 | Data Entry | Depending on the Correspondence value selected above, different fields are displayed.For SAP06, make the following entries:Customer: SelectedCustomer: <Any customer number>Postings From: <Any date>Postings To: <Any date>Last Statement: <Any date>For SAP13, make the following entries:Customer: SelectedCustomer: <Any customer number>Last Statement: <Any date>Current Statement: <any date>For SAP08, make the following entries:Customer: SelectedCustomer: <Any customer number>Open at Key Date: <any date>For SAP09 (entry view) and SAP21, make the following entries:Journal Entry: <journal entry>Fiscal year: <fiscal year>For SAP09 (ledger view), make the following entries:Journal Entry: <journal entry>Fiscal year: <fiscal year>Ledger: <ledger> |  |  |
| 5 | Actions | Use the buttons at the bottom of the view to preview, email, and print the correspondence.Note When choosing Send Email or Print, populate the required fields in the dialog box to complete the process. | Correspondence is created according to the selected criteria. |  |

Procedure B - Manage Journal Entries

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an General Ledger Accountant . |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries view displays. |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Ledger Group: emptyJournal Entry Type: (optional) For example, SAJournal Entry: <empty>Journal Entry Date: (optional) <date>Period:(optional) <period>Fiscal Year: <year of posting document>Posting Date(optional): <date> | Selected journal entries are displayed in the Journal Entries list. |  |
| 4 | Manage Journal Entry | Select a journal entry number and choose Manage Journal Entry. | The Journal Entry - Entry View view displays with the document details. |  |
| 5 | Correspondence | Choose Create Correspondence. | The Create Correspondence view displays. |  |
| 6 | Entry View | Select the following:Correspondence: SAP09 (Internal Document - Entry View) | Available fields display and are populated automatically. |  |
| 7 | Actions | Use the buttons to:PreviewPrintSend Email. | Correspondence is created according to the selected criteria. |  |
| 8 | Exit | Choose Home to exit. | SAP Fiori launchpad displays. |  |
| 9 | Ledger View | Repeat steps 1–5 and select:Correspondence: SAP09 (Internal Document - Ledger View) | Available fields display and are populated automatically. |  |
| 10 | Parameters | Choose Advanced Parameters.Make the following entry:Correspondence: <Any ledger, for example 0L> |  |  |
| 11 | Actions | Use the buttons to:PreviewPrintSend Email. | Correspondence is created according to the selected criteria. |  |

#### Display Correspondence History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays a history of the correspondence sent to a customer.

Prerequisite

Correspondence is created and sent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Display Correspondence History (F2934) |  |  |
| 3 | Search | Select any desired search criteria and choose Go. | A list of correspondence history records is displayed. |  |
| 4 | Details | Select a row to display. | Details are displayed. |  |

### Invoice Management Reporting

#### Accounts Receivable Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure guides you through the accounts receivable overview. In this activity, you review an overview of relevant figures and statistics related to the accounts receivable process. The Accounts Receivable Overview (F3242) app offers a central point of entry and an overview of the department.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager.Note Once you log on, you can customize fields to be displayed by default. To do so, choose User > Settings > Default Values , then add the Display Currency, Company Code, and Supplier fields. Save your changes. |  |  |
| 2 | Access the SAP Fiori App | Open Accounts Receivable Overview (F3242). |  |  |
| 3 | Edit Criteria | Make the following entries and choose Go:Display Currency: AEDNote You can change the currency If needed.Net Due Interval 1: for example, 30Net Due Interval 2: for example, 60Net Due Interval 3: for example, 90Company Code: <any> | Relevant figures and statistics display in the lower part of the screen.Some of the cards displayed are:Quick LinksAR Aging AnalysisMy InboxDays Sales OutstandingCash Collection TrackerAR BreakdownTop 10 Debtors |  |
| 4 | Navigate to Options | There are different, available options for reviewing figures and statistics.You can change the global filters if needed. The visible cards can be customized.Each card mentioned in the prior step provides you with functions to view and manage various accounts payable functions and information | Figures and statistics display according to available options. |  |

#### Monitor Overdue Receivables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the status of overdue items. Different predelivered graphs are available.

Prerequisite

Open invoices are available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Overdue Receivables - Today (F1747). | A graphical overview for the overdue receivables displays. |  |
| 3 | Explore Receivables | Choose the drilldown button next to By Due Period or choose the bar in the graphic, and select an option. | A graph or list is displayed according to the selection. |  |

#### Monitor Overdue Receivables by Risk Class

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you, monitor the overdue receivables via the report of overdue payments. This report is a list of customers classified by risk. You can search the report by risk class, company code, country/region, customer, credit segment, G/L account, or currency. The output provides a graph displaying customer risk classification. You can export the graph into a fact sheet for analysis.

Prerequisite

Customer master data is maintained for company codes.

Invoices are posted and past due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Overdue Receivables - by Risk Class (F2539). | A graphical overview for the overdue receivables is displayed. |  |
| 3 | Navigation | To change the graph view, choose the drill-down button or other buttons for the report.At the top of the graph view, there are additional buttons you can use to change the display layout of the graph. | A graph or list is displayed according to the selection.•Risk Class•Company Code•Country Key•Customer |  |

#### Future Receivables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the analytical app displays the Key Performance Indicator (KPI) for Future Receivables.

Prerequisite

Invoices are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Future Receivables - Today (F1744). |  |  |
| 3 | Navigation | To change the view, use any of the navigation options:Use the dropdown list to view by By Due Period, By Customer (Top 10 Receivables, Chart), By Company Customer (Top 10 Receivables, Table), By Company Code (Chart), or the By Company Code (Table).Use the View By icon to filter by available dimensions, for example Company Code, Region, or Accounting Clerk.Switch between chart or table views.Switch the chart type view, for example Bar Chart, Line Chart, or Heat Map.Your selected view can be exported to a spreadsheet or sent as an email. | Different views display. |  |

#### Total Receivables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Key Performance Indicator (KPI) for Total Receivables.

Prerequisite

Invoices are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Total Receivables - Today (F1748). |  |  |
| 3 | Navigation | To change the view, use any of the navigation options:Use the dropdown list to view by By Due Period, By Top 10 Customers, By Company Code, or the By Accounting Clerk.Use the View By button to filter by available dimensions (for example Company Code or Account Group).Switch between chart or table views.Switch the chart type view, for example Bar Chart, Line Chart, or Heat Map.Your selected view can be exported to a spreadsheet or sent as an email. |  |  |

#### Days Sales Outstanding

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The analytical app displays the key performance indicator (KPI) Days Sales Outstanding. This KPI is the average number of days it takes for your company to collect receivables. A high Days Sales Outstanding (DSO) figure can indicate that your company is taking too long to collect money.

Prerequisite

Invoices are posted and unpaid.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Days Sales Outstanding - Last 12 Months (F1741). |  |  |
| 3 | Navigation | To change the view, choose the View By button or other available buttons in the report.You can view days sales outstanding (DSO) figures in a chart or table according to company code, customer, country/region, accounting clerk, and month. | Different views are displayed. |  |
| 4 | Detailed Analysis | Choose Jump To > Days Sales Outstanding - Detailed Analysis . |  |  |
| 5 | Selection | To change a view, choose + (Add Analysis Step). Select any of the options displayed; every time you choose an option more options are displayed. Select any of them until you select the Chart type:Time :Company Code :Customer:Country of Customer :Due Period:Note You can choose the + Add Analysis Step button again to display more analysis. | Different views are displayed. |  |
| 6 | Save | In the Unnamed Analysis Path area, choose the Related Options button, then choose Save As to save your current selection. Enter a name and choose OK. | The view is saved. You can access it later to view the information with this type of analysis. |  |
| 7 | Open | In the Unnamed Analysis Path area, choose the Related Options button, then choose Open. Select a previously saved analysis and choose OK. | The Unnamed Analysis Path button shows name of selected saved analysis. |  |

#### Dunning Level Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Key Performance Indicator (KPI) Dunning Level Distribution (open dunning amounts per dunning level and customer).

Prerequisite

Dunning is generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Dunning Level Distribution - Today (F1742). |  |  |
| 3 | Navigation | To change the view, use any of the navigation options:Use the dropdown list to view By Dunning Level or the By Customer (Top 10 Overdue) .Use the View By icon to filter by available dimensions, for example Company Code, Region, and so on.Switch between chart or table views.Switch the chart type view, for example Column Chart, Doughnut Chart, Heat Map, and so on.Your selected view can be exported to a spreadsheet or sent by email. | Different views display. |  |

#### Days Beyond Terms

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the key performance indicator (KPI) for Days Beyond Terms (DBT). You gain an insight into the payment history of your customers and how effectively your company collects payments. A high DBT figure indicates that your company is taking too long to collect payments.

Prerequisite

Invoices are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Days Beyond Terms - Last 12 Months (F1739). |  |  |
| 3 | Navigation | To change the view, use any of the navigation options:Use the dropdown list to view by By Period, Ratio Payments Within Terms/Beyond Terms, or the By Customer (Top 10 Overdue).Use the View By button to filter by available dimensions, for example Company Code, Calendar Month, and so on.Switch between chart or table views.Switch the chart type view, for example Line Chart, Waterfall Chart, Heat Map, and so on.Your selected view can be exported to a spreadsheet. | Different views display. |  |

#### Display Item Change Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display, sort, and analyze logged changes for journal entries. This report provides better control and tracks changes performed manually by different users on payable items.

Prerequisites

Invoices are created.

Payments are created.

Prior to report generation, the documents are changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Display Item Change Log - Customer (F7796). |  |  |
| 3 | Select | Enter the following data and choose Go:Document Type: <document type>, for example, DocumentsFiscal Year: <any>Changed on: <interval of dates>Company Code: 3310 | The Items pane shows all relevant journal entries. |  |
| 4 | Exit | You can view additional information by clicking on entries under Journal Entry, Customer, and so on. When done, choose Back. |  |  |

#### Cash Collection Tracker

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the actual cash collection progress against the target performed by the collection specialists.

Prerequisites

Invoices are created.

Some invoices are collected and some remain open.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Collection Tracker - Accounts Receivable (F2925). |  |  |
| 3 | Enter Criteria | Make the following entries and choose Go:As of Date: <Today’s date>Period Type: <Period Type>Display Currency: <Company Code currency>Exchange Rate Type: M |  |  |
| 4 | Available Views | Select any of the available views:By Company CodeBy Accounting ClerkBy Customer | The list updates and displays according to the selected view. |  |

### Down Payments

#### Create Down Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a down payment request.

Prerequisite

The customer master record has been entered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Down Payment Requests (F1689). |  |  |
| 3 | Create | Choose the Create button. |  |  |
| 4 | Header Criteria | Make the following entries:Company Code: 3310Journal Entry Date: Today’s datePosting date: Today’s dateJournal Entry Type: DZTransaction Currency: AED |  |  |
| 5 | Items Criteria | Enter the following:Customer: 33100001Amount: for example, 1000Tax Code: for example, <enter a tax code if necessary>Trg. Spec. G/L Ind: A (Default value, don't change) Choose > to see more details and enter the following data:Due on: Today’s dateChoose Enter. |  |  |
| 6 | Post | Choose Post. | The Success view is displayed showing the journal entry number posted. |  |
| 7 | Additional Actions | Select the desired action in the Success view:DisplayPost NextGo to Worklist |  |  |

#### Display Down Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the down payment request.

Prerequisite

A down payment request is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Down Payment Requests (F1689). |  |  |
| 3 | Search | Make the following entries and choose Go:Company Code: 3310Posted By: <today’s date> | A list of Down Payment Requests is displayed according to search criteria. |  |
| 4 | Select | In the Journal Entry column, select the document number to display. On the dialog box that displays, choose the document number. | The Manage Journal Entries view displays the details of the selected journal entry. |  |
| 5 | View | Review the details of selected journal entry. |  |  |
| 6 | Back | Choose < (Back) to return to previous view. | The Manage Customers Down Payment Requests view displays. |  |

#### Post Down Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a payment for a down payment request.

Prerequisite

A down payment request is posted. Use a previously created down payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345). |  |  |
| 3 | General Information | Make the following entries in the General Information area:Company Code: 3310Posting date: <date>Journal Entry Date: <date>Value date: <today's date>Type: DZ |  |  |
| 4 | Bank Data | Make the following entries in the Bank Data area:G/L Account: 11001060House Bank/Account ID: <House Bank> and <Account ID>Amount: <Down payment request amount>Amount/CCode Currency: <amount>AED |  |  |
| 5 | Open Item Selection | Make the following entries in the Open item selection area:Account Type/Account ID: Select Customer from the dropdown and enter 33100001 for the Account ID.Payment Reference: <Down payment request document number>Choose Propose Items . | The open items list displays.If you enter the document created in the previous Create Down Payment Request procedure directly in the Payment Reference field, and choose Propose Items, the down payment document is automatically transferred to the Items to be cleared section. |  |
| 6 | Select More | Choose Select More. Select the checkbox for Special G/L Transactions and choose OK.To choose the items to clear, choose the Clear button from the last column. | The selected item in Payment Reference is transferred to Items to Be Cleared view. |  |
| 7 | Post Entries | Choose Post. | The Success dialog box displays details of the document number generated. |  |
| 8 | Other | In the Success dialog box, select the following options:DisplayPost Next Payment. |  |  |

#### Enter Invoice Without Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Customer invoices are posted in accounting. In this activity, you create journal entries.

Prerequisites

Customer master records have been entered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Outgoing Invoices (FB70). | The Enter Customer Invoice view displays. |  |
| 3 | Basic Data | Choose Company Code and enter your company code.Make the following entries:Customer: <customer number>Invoice date: <Today’s date>Posting date: <Today’s date>Reference: <any>Amount: <any>Currency Key: <co.code currency>Calculate Tax: selected |  |  |
| 4 | Payment Tab | Bline Date: <Today’s date>Payt Terms: 0001Payt Meth.: <optional> |  |  |
| 5 | Line Items | G/L Acct: 41000400D/C: CreditAmount in Document Currency: <Check amount that was entered in the basic data>Tax Code: <Sales Tax Code> |  |  |
| 6 | Profitability Segment | In the Profit.segment column, select button and enter:Customer: <customer number>Profit Center: <any>Choose Derivation and then choose Continue. |  |  |
| 7 | Post | Choose Post to save. | Journal Entry is posted. |  |

#### Post Incoming Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the incoming payments from the customer.

For a payment of an invoice where a down payment is applied, the incoming payment amount should be the remainder invoice balance (the remainder invoice balance is the invoice value less the down payment to be applied).

|  |
| --- |
| Note To meet eInvoicing requirements to provide down payment details in the invoice's eDocument, use the Clear Incoming Down Payments - Clear Incoming Down Payments (F8969) app. |

Prerequisites

Invoices are posted.

Down Payments: A down payment has been posted. Select an open invoice (use app Manage Customer Line Items) to apply the posted down payment from step Post Down Payment. The invoice value must be larger than the down payment posted. The incoming payment value in this step is the invoice value less the down payment posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345). |  |  |
| 3 | Enter General Information | Make the following entries in the General Information area and choose OK:Company Code: 3310Posting date: <date>Journal Entry date: <date>Value date: <today’s date>Journal Entry Type: DZ |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank data area.G/L Account: 11001060House Bank/Account ID: AEBK1/AEAC1Amount: <customer invoice amount>Note If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency: AED |  |  |
| 5 | Enter Open Item Selection | Make the following entries:Customer Account: 33100001Choose the Propose Items button. | The open items are displayed in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to the Items to be Cleared view. |  |
| 7 | Down Payment | Caution Only execute this step if the payment is for an invoice where a down payment is to be applied.In the Items to Be Cleared column Allocated Amount, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Choose Enter. | The balance is zero and the document can be posted. |  |
| 8 | Post Entries | Choose the Post button. | The Activated dialog box displays details of document number generated. |  |
| 9 | Post on Account | Repeat steps 1 to 4. |  |  |
| 10 | Enter Data | Choose Post on account and enter the following:Account Type: CustomerCustomer: 33100001Credit Amount: same amount as in step 4. |  |  |
| 11 | Save | Choose Post. | Document is posted. |  |

#### Clear Incoming Down Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you clear the invoice against one or more down payments. Using this app, the posted clearing document includes references to both the invoice and the corresponding down payments.

Prerequisites

Invoices and down payments are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad a an Accounts Receivable Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Clear Incoming Down Payments - Clear Incoming Down Payments (F8969). |  |  |
| 3 | Enter Customer Information | Make the following entries and choose OK:Customer: <customer>, for example, 33100001Company Code: <company code>, for example, 3310 | The system displays a list of open invoices to be cleared. |  |
| 4 | Select Invoice | Select an invoice and choose > (Navigation). | The Open AP/AR Items pane shows the down payment transactions. |  |
| 5 | Clear Invoice Against Down Payment | To choose a posted down payment, choose Clear in the last column for each down payment document. | Once a down payment is chosen, the balance is displayed in the Items to be Cleared pane. |  |
| 6 | Simulate (Optional) | Before you post, you can choose to simulate the posting. | A view displays a simulated view of the posting to be created if you post the document. |  |
| 7 | Post | Choose Post. | The system displays the Success message, along with a document number, company code, and year created. You can then choose to display details or go to the Payment List. |  |

#### Clear Open Items Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, open items in customer accounts are posted.

Prerequisites

- Invoices are posted
- Down payments are posted
- Incoming payments are posted

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear Incoming Payments - Manual Clearing (F0773). |  |  |
| 3 | Enter Customer Information | Choose the Clear Open Items button.Make the following entries and choose OK:Customer: 33100001Company Code: 3310 | A list of open payments still to be cleared is displayed. |  |
| 4 | Select More | To display open Items and special G/L transactions, choose Select More (…) button, and choose:Line Item Type: Normal Open Items and special G/L Transactions | Normal open Items and special G/L transactions are displayed in Open Items section. |  |
| 5 | Clear Open Item Against Down Payment | Caution Only execute this step if you're clearing an open item (invoice) against a down payment.In the Open Items section, select the invoice where you applied the incoming payment in the Post Incoming Payment step, then choose the down payment posted in the Post Down Payment step by choosing the Clear button in the last column of each journal entry.Skip the next test step and continue to the Simulate (Optional) step or choose Post. | When the invoice is chosen, the assigned incoming payment is also selected. In the Items to Be Cleared section, the balance of the open item (invoice) displays.The down payment is moved to the Items to Be Cleared section. The balance becomes zero. Verify at the top of the view. |  |
| 6 | Open Item Selection | Note Skip this test step if you executed the prior step in this table.In the Open Items section, choose items to clear by clicking the Clear button in the last column.Note The sum of the chosen open items to be cleared must be zero, check that the Balance is zero (top right) so the posting can occur. | The item to be cleared is transferred to the Items To be Cleared section on the right of the view. |  |
| 7 | Simulate (Optional) | Before you post, you have the option to simulate the posting. | A view showing the posting to be created when the document is posted displays. |  |
| 8 | Post | Choose the Post button at the bottom of the view. | The system displays Success and also displays the document number, company code, and year created with option buttons to Display or go to the Payment List. |  |

### Incoming Payments

#### Incoming Payment with Electronic Bank Statement

##### Daily Cash Operations – Bank Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, Cash Management loads bank statements for the bank accounts each day. During the loading process, a rule-based framework tries to assign each cash flow on the bank statement to an item on a clearing account or match it with an open invoice in Accounts Receivable.

Procedure

Follow the steps in the Bank Statement test procedure of the Basic Cash Operations (BFB) test script.

##### Cash Application Intelligence Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Typically, the rule-based assignment of incoming payments can't match all incoming payment to open Accounts Receivables invoices. With the help of machine learning, you can improve the matching rate.

Procedure

If the interface to Cash Application Intelligence is activated, follow the procedures described in the Cash Application Integration (1MV) test script.

##### Reprocess Bank Statement Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The bank credits the collection, the direct debit, the deposited checks, and a bank transfer from a customer to your account. The primary purpose of this activity is to address bank statement items that aren't automatically cleared. Posting of the bank statement in these cases clears the open items for the bank account.

Prerequisite

A bank statement was previously uploaded or entered manually. For more information, see the Basic Cash Operations (BFB) test script.

|  |
| --- |
| Note (Optional): The Cash Application Integration (1MV) scope item is activated (an additional license is required). 1MV acts with machine learning in the system. When the optional Cash Application Integration (1MV) scope item is activated, more choices are available when completing the Apply Rules step. You're allowed to select multiple rules from the Apply Rules list. Without 1MV, you're allowed only one rule selection, at a time, to apply. If you use 1MV, manual posting actions are sent to the Cash Application Integration (1MV) scope item so that it can learn and determine proposals for the new reprocessing rule template. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Reprocess Bank Statement Items (F1520). | The Reprocess Bank Statement Items (F1520) view is displayed. |  |
| 3 | Search | Make the following entries and choose Go:Company Code: 3310House Bank: AEBK1House Bank Account: AEAC1Posting Status: Select Posting not Started and Not completed | A list of Bank Statement Items displays. The Processing Status column displays the current processing status.Note You have two options:Reprocess a single bank statement itemReprocess multiple bank statement itemsChoose the appropriate option from the two options presented below. |  |
|  | Option 1 | Option 1: Reprocess a single bank statement item |  |  |
| 4 | Select Bank Statement Item | To select a bank statement to reprocess, in the Reprocess column, choose Details (>). | A Bank Statement details view is displayed. |  |
| 5 | Details | In the Details area, verify or enter the following data:Account type: <Customer or G/L account>Posting Date: <Today's date>Payment Amount: <Amount of invoice to clear>Journal Entry Type: for example, DZNote If necessary, you can adapt the Memo Line field value. Doing so changes the Memo Line Version field value to Revised. You can also change the Procg. Instruction field value to determine how to handle the Memo Line field value. If you want to restore the original value of the Memo Line field, you can choose the Undo button near the Memo Line Version field. | Depending on the statement item that you're processing, you must choose a customer or a vendor to be able to balance the clearing document.A list of invoices displays at the bottom half of the view in the Open Items section.Note If necessary, you can also create a dispute case, for example, if a customer short pays an invoice. |  |
| 6 | Clear | In the Open Items pane, select the invoice to clear that matches the amount from the Details section. In the Clear column, choose the Clear button.Note Additional functions are available above the Open Items pane, such as Post on Account, G/L Items, Post to G/L Account, and so on. | The invoice is transferred to the Items to be Cleared section. The balance amount on the header must be zero for the item to be cleared.Note You can also post on supplier/customer accounts or to G/L accounts. To do so, choose the Post on Account tab or Post to G/L Account tab, enter the account information and amount, then choose Post. |  |
| 7 | Post | Choose the Post button. | The success view displays the journal entry number posted.The document created can be displayed too. |  |
|  | Option 2 | Option 2: Reprocess multiple bank state items |  |  |
| 4 | Settings | In the Bank Statement Items table, verify that the Bank Statement Items Memo Line column is visible. If not visible, choose the Settings button and add the column by choosing the checkbox and then choose OK. |  |  |
| 5 | Select Bank Statement Items | Select one or more bank statement items.Either:If you're reprocessing multiple company codes or bank accounts, you can filter the items list by choosing the column and selecting Filter from the dropdown list. Enter your filter criteria in the Define Filters dialog box and choose OK.If you canceled the previous step and created a rule, choose the Apply Rule button.Choose the rule from the dialog box and choose Filter by Rule. The item list filters by the selected rule.Note You can only select a single rule for filtering, multiple rule selections aren't possible.Caution If the rule condition does not match a selected item, the rule isn't applied and the item isn't processed.Or:If you're reprocessing items using a single company code and bank account, select the checkboxes for items from the list or make no selection to apply a rule to all items in the list.Choose Apply Rule.Remember Once you select Apply Rule, it automatically selects whether the rule is applied to all bank statement items or only applied to your selected items. Ensure that you select the bank statement items before choosing Apply Rule.Note If you canceled the previous step and created a rule, choose the Apply Rule button. Choose the rule from the dialog box and choose Filter by Rule. The item list filters by the selected rule. If the rule condition doesn't match a selected item, the rule isn't applied, and the item isn't processed.Caution If the rule isn't available and must be created, choose Cancel and proceed to the next step. | The Apply Rule dialog box displays. |  |
| 6 | (Optional) Manage Rules | Choose the Manage Rules tab.A Manage Bank Statement Reprocessing Rules view is displayed.To create a rule, proceed to the next [Manage Bank Statement Processing Rules (Optional)](#unique_67) [page ] 110 procedure and follow the instructions to create a rule.When completed, choose Back to return to the Reprocess Bank Statement Items view. Select one or more bank statement items or make no selection to apply the rule to all items and then choose Apply Rule to continue with these steps. |  |  |
| 7 | Apply Rule | Either enter the rule name in the Search field or select rules from the list and choose Apply Rule.Note If you activated the Cash Application Integration (1MV) scope item, more options are available. When you've activated 1MV, you can select multiple rules from the Apply Rules dialog box to apply. Without 1MV, you only select one rule at a time to apply and repeat this step to add more rules.Choose OK for the Success dialog box with a notification about the rule being scheduled that displays. | The Process Status for the bank statement items selected display an Info: This Item is being processed as a scheduled job icon. |  |
| 8 | Open the Reprocessing Screen | Select a bank statement item and from the Reprocess column, choose the > (Open the Reprocessing Screen) button. | A Bank Statement details view is displayed. |  |
| 9 | Review (Optional) | To review, choose the Applied Rules Log and choose the Status Information. Navigate to the Job Log icon for your job to review the log details. |  |  |

##### Manage Enrichment Rules for Bank Statement Processing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create and manage rules to enrich bank statement items. These rules let you add missing information or overwrite incomplete details in your bank statement items. This ensures that processing rules can handle the items correctly in a later step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist |  |  |
| 2 | Access the SAP Fiori App | Open Manage Enrichment Rule Sets - For Bank Statements (F9062). |  |  |
| 3 | Create | Choose Create. | The New Pre-processing Rule view is displayed. |  |
| 4 | Enter Details | Make the following entries:Enrichment Rule Set section:Description: <description>Target Field: <target field>, for example, CustomerCompany Code section (you may need to choose Create in this section to enter information):Company Code: <company code>, for example, 3310House Bank: <house bank ID>, for example, xxBK1House Bank Account: <house bank account>, for example, xxAC1 |  |  |
| 5 | New Value Extraction | Choose the Value Extraction tab. |  |  |
| 6 | New Value Extraction | Select the F4 Help in the field, then choose an option from the dialog box. |  |  |
| 7 | Enrichment Rules | Choose the Enrichment Rules tab. |  |  |
| 8 | Enrichment Rules | Make the following entries:Attribute: <attribute>, for example, company codeOption: <select an option>, for example, contains, equal to, or not equal toValue: <value>, for example, 1010Select action: <action>, for example, SetValue: <value for customer>, for example, 12345Note You can add more rules by choosing Add. |  |  |
| 9 | Create Rule | Choose Create at the bottom of the view. | The enrichment rule is created. |  |

##### Manage Value Extraction for Bank Statements (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the value extraction for bank statements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist |  |  |
| 2 | Access the SAP Fiori App | Open Manage Values Extraction Rules - For Bank Statements (F9297). | The view displays a list of current value extractions. |  |
| 3 | Create Rule | Choose Create. | The New Object pane opens to the right. |  |
| 4 | Value Extraction | On the Value Extraction tab, make the following entries:Description: <description of extraction rules>, for example, ReferenceValue Type: <value type>Note For countries/regions that support IBAN, you can use IBAN or Reference. For all other countries, use Reference.Company Code: <company code>, for example, 3310 |  |  |
| 5 | Extraction Pattern | On the Extraction Pattern tab, choose Create. |  |  |
| 6 | Extraction Pattern | Make the following entries:Action: <action type>, for example, SEARCHSearch Terms: <terms to search for>, for example, INVExtract: SelectedNote You can choose Create again to add more pattern rows. | You entered patterns for the extraction’s rules. |  |
| 7 | Simulate | On the Simulation tab, to test your extraction rule, enter some text in the field and choose Test. | The results of the test are displayed below the Simulation Text field. |  |
| 8 | Create | When you are satisfied with the performance of the rule, choose Create. |  |  |
| 9 | Activate | When you are ready to activate the rule, choose the Activate toggle near the top of the right pane (in the Value Extraction tab). |  |  |

##### Manage Bank Statement Processing Rules (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional activity, you create a bank processing rule.

|  |
| --- |
| Note Rules can be shared. By default, the sharing is turned off. To share a rule, go into an existing rule and set the Share Rule slider to Yes. Shared rules are visible on the Shared Rules tab on the Manage Processing Rules (F3555) view. |

|  |
| --- |
| Note You can automate rules. For more information, see Advanced Bank Statement Automation (4X8).For more information on creating and using processing rules, see [Manage Processing Rules - For Bank Statements](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/d6fe6526b26f46e59d9d1dd0f7427fe3.html?version=LATEST) on SAP Help Portal.Rules can also be automatically applied. To do so, choose Automate Rule, make the necessary selections in the resulting dialog box, and set the Activate Rule for Automation slider to Yes. Automated rules are visible on the Automated Rules tab on the Manage Processing Rules (F3555) view. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist.Note This procedure can also be performed by users with the Accounts Receivable Accountant role. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Processing Rules - For Bank Statements (F3555). | The Manage Processing Rules (F3555) view is displayed. |  |
| 3 | Create Rule | To add a new rule, choose Create. | The Processing Rule view displays. |  |
| 4 | Add Rule Criteria | Enter the following data:Description: <any description of the rule>Rule For: Select either Outgoing Payment or Incoming Payment |  |  |
| 5 | Add Action Type | Select an Action Type for the available list to fit your requirements:G/L PostingAP/AR PostingClear in SequenceCaution When you select a different action type, an If you change the action type when creating or modifying a processing rule, the data entered previously in the action will be lost when you save your change to this action type warning notification displays. Choose OK to confirm.Each action type selection displays a different set of fields.Note After the next step for defining the Condition, the following steps provide information for each Action Type option. |  |  |
| 6 | Add Condition Criteria | In the Condition area, enter the following data:Tip Predefined conditions and value ranges are provided in dropdowns. Here are two examples. First example, select Company Code for the Attribute, the Options are notations of values, select EQ for equals. The From and To fields are a value range and since Company Code equals, add 3310 in the From field. Second example, select Amount for the Attribute, and Select less than or equal to, in Option, and then add the least amount in From and the equals value in To .Attribute: <attribute>Option: <option>From: <value>To: <value>Note For the fields above, define conditions as needed for your particular use case (for example, Memo Line, House Bank, and so on).In the Conditions pane, choose Create to add another condition. |  |  |
| 7 | Action Type: G/L Posting | If you selected the G/L Posting for action type, follow this step. Skip this step if you selected a different Action Type.In the Post to G/L Account, enter the following:Note You only enter either a Profit Center or a Cost Center, not both, depending on the type of posting. If the G/L account is a cost element, then cost center is required. If the G/L account is a balance sheet item, then profit center is required.Account: <G/L account>Profit Center: For example, OptionalCost Center: For example, <cost center>Proceed to step 10. |  |  |
| 8 | Action Type: AP/AR Posting | If you selected the AP/AR Posting for action type, follow this step. Skip this step if you selected a different Action Type.In the Post to AP/AR Account, enter the following:Note You only enter either a Customer or a Supplier, not both, depending on the type of posting.Customer: <customer>Supplier: <supplier>Assignment Reference: OptionalDocument Item Text: OptionalProceed to step 10. |  |  |
| 9 | Action Type: Clear as Sequence | If you selected the Clear in Sequence for action type, follow this step. Skip this step if you selected a different Action Type.In the Clear in Sequence section, enter the following and choose Create:Processing Instruction: <processing instruction>Reason Code: <reason code> | You created the processing instruction. |  |
| 10 | Save | Choose Create. | The new rule is saved. |  |

##### Obtain Payment Advices Manually (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you obtain payment advice with information about invoices paid, discounts taken, and the total payment amount that is received by mail, fax, or email from the customers.

Procedure

This activity happens outside of the system and is used by the Accounts Receivable Accountant to get information about invoices paid with payments found on the bank statement. This information can also be used in the next procedure in this section, Clear Open Items Manually.

##### Manage Payment Advice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create, display, change, and delete payment advice. The advice explains the usage of the payment and is used for clearing.

A payment advice note contains the incoming payment details required to allocate and clear the relevant open item.

|  |
| --- |
| Note To add a payment advice, you can either use an existing payment advice file or create the advice manually. |

|  |
| --- |
| Note We also provide a newer version of the app ( Manage Payment Advices (F2550A)). For more information, see the [Manage Payment Advice](#unique_90) [page ] 144 step in the Appendix. |

Prerequisite

A business partner exists.

An open incoming payment document exists (document posted on account).

An OPTIONAL prerequisite is completing the Manage Situation Types procedure in the Preliminary Steps section of the Prerequisites, allowing you to complete the (Optional) Monitor Notification steps at the end of this procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Payment Advices - Deprecated (F2550). |  |  |
| 3 | Choice - Import Payment Advice File | Either follow this step when you have an existing payment advice file or skip to the Add Manually step when no payment advice file is available.Note If you don't have a payment advice file, skip to the Choice - Manually Create Payment Advice step.Caution The Import option is only available if you've licensed and activated Cash Application Integration (1MV). If you haven't, skip to the Choice - Manually Create Payment Advice step. |  |  |
| 4 | Choose Import | When you have an existing payment advice file, choose the Import button. | The Import Payment Advices dialog box displays. |  |
| 5 | Import Existing File | Enter the Company Code value.Either drag and drop the file on to the dialog box or choose Create to navigate to the local folder and select the file.Choose Process. | The file is uploaded and appears in the table under the Confirmation Pending tab of the Manage Payment Advices view. |  |
| 6 | Select Payment Advices | Select your new Payment Advices from the table. | A Payment Advice Draft view appears. |  |
| 7 | Review and Confirm | Select the Payment Advice Items tab and review the list of invoices that display. When your review is complete, choose the Confirm and Next button.To continue, skip to step 15. |  |  |
| 8 | Choice - Manually Create Payment Advice | When no payment advice file is available, use the following steps. |  |  |
| 9 | Add Manually | Choose Add Manually (+) to create the manual payment advice. | The Payment Advice view displays. |  |
| 10 | General Information | In the General Information section, enter the following data:Company Code: 3310Payment Amount: 500Currency: AEDCustomer: 33100001 |  |  |
| 11 | Payment Advice Items | In the Payment Advice Items section, new lines are added automatically once a field in the existing line is filled in. |  |  |
| 12 | More Fields | Select Setting, activate the following fields by selecting the checkbox:Alternative AccountAlternative Company CodeAssignmentChoose OK to continue. | Fields are displayed. |  |
| 13 | Payment Advice Items | In the Payment Advice Items section, enter the following data:Document: Incoming payment document numberDocument Date: <Date when the document was posted>.Payment Amount: <Total payment amount>Alternative Account: <customer number>Alternative Company Code: 3310Assignment number: <document number>If there are more documents, select Add (+) and enter required data. |  |  |
| 14 | Save | Choose Save. |  |  |
| 15 | Change Payment Advice |  |  |  |
| 16 | Enter Search Criteria | Enter search criteria:Editing Status: AllCompany Code: 3310 |  |  |
| 17 | Execute Query | Choose the Go button. | A table shows the information of all payment advices. |  |
| 18 | Select | Select the payment advice number to open it. | Payment advice details are displayed. |  |
| 19 | Edit | Choose Edit button and make any changes that are required. |  |  |
| 20 | Save | Choose Save. |  |  |
| 21 | Delete Payment Advice |  |  |  |
| 22 | Search | Repeat steps 15-18.In the Manage Payment Advices view, select the payment advice to be deleted. |  |  |
| 23 | Delete | Choose Delete. | A notification displays, asking to confirm deletion. |  |
| 24 | Confirm | Choose Delete. | Payment advice is deleted. |  |
| 25 | (Optional) Monitor Notification | When the Manage Situation Types procedure in the Preliminary Steps section of the Prerequisites has been completed, the following steps are available to you. |  |  |
| 26 | Open Notifications | Choose the Notifications button at the top right of the view.Choose the payment advice notification generated by the system. |  |  |
| 27 | Review Notification | The payment advices details for the notification display.Choose Back. |  |  |

##### Clear Credit/Debit Memos Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post debit memos and credit memos to customer accounts. Also, this process can be used to clear debit and credit memos created in the Invoice Correction Process with Debit Memo (BDQ) and Invoice Correction Process with Credit Memo (BKL) test scripts.

|  |
| --- |
| Caution Invoice Correction Process with Debit Memo(BDQ) and Invoice Correction Process with Credit Memo (BKL) aren't valid for Finance Cloud Edition. Skip these steps if using Finance Cloud Edition. |

Prerequisites

You must have open items.

You executed the Invoice Correction Process with Debit Memo (BDQ) and Invoice Correction Process with Credit Memo (BKL) test scripts. Postings are created using customer 33100001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear Incoming Payments - Manual Clearing (F0773). |  |  |
| 3 | Enter Customer Information | Choose the Clear Open Items button.Make the following entries and choose OK:Customer: 33100001Company Code : 3310 | A list of open payments still to be cleared displays. |  |
| 4 | Open Item Selection | In the Open Items section, select the items to clear and choose the Clear button from the Clear column.Note The sum of the chosen open items to be cleared must be zero. Check if the Balance is zero (top right), so the posting can occur. | The item to be cleared is transferred to Items To be Cleared section on the right side of screen. |  |
| 5 | Simulate (Optional) | Before you post, you have the option to simulate the posting by choosing the Simulate button. | A view displays a simulated posting to be created when the document is posted. |  |
| 6 | Post | Choose the Post button at the bottom of the screen. | The system displays a Success notification. Showing the document number, company code, and year created. Option buttons to Display or go to the Payment List are available. |  |

#### Incoming Payment without Electronic Bank Statement

##### Post Incoming Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the incoming payments from the customer. For a payment of an invoice where a down payment is applied, the incoming payment amount should be the remainder invoice balance (the remainder invoice balance is the invoice value less the down payment to be applied).

Prerequisites

Invoices are posted.

Down Payments: A down payment is posted. Select an open invoice (use the Manage Customer Line Items (F0711) app) to apply the down payment posted from the previous Post Down Payment procedure. The invoice value must be larger than the down payment posted. The incoming payment value in this activity is the invoice value, less the down payment posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345) | The Post Incoming Payments view displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code: 3310Posting date: dateJournal Entry date: dateValue date: today’s dateJournal Entry Type: DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank data area.House Bank/Account ID: AEBK1/AEAC1G/L Account: <account (not a bank subaccount)> (see note)Note To determine the account value, log in as a Cash Management Specialist and open Manage Bank Accounts (F1366A). Enter your Company Code, House Bank, and House Bank Account and choose Go. Choose Details for the row. Choose House Bank Account Connectivity, then in the House Bank Account Data section, make a note of the value in the G/L Account field. Use this value for the G/L Account field above.Amount: customer invoice amountNote If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency: AED |  |  |
| 5 | Enter Open Items | Make the following entries:Customer Account: 33100001 \|Choose the Propose Items button. | The open items are displayed in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Down Payment | Note Only execute this step if the payment is for an invoice where a down payment is applied.In the Items to Be Cleared column, Allocated Amount, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Choose Enter. | The balance is zero and the document can be posted. |  |
| 8 | Post Entries | Choose Post. | The Activated dialog box displays details of document number generated. |  |
| 9 | Post on Account | Repeat steps 1–4. |  |  |
| 10 | Enter Data | Choose Post on account and enter the following:Account Type: CustomerCustomer: 33100001Credit Amount: same amount as in step 4. |  |  |
| 11 | Save | Choose Post. | Document is posted. |  |

#### Incorrect Posting

##### Reset Cleared Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reset a cleared document.

|  |
| --- |
| Caution Resetting a large number of cleared documents can cause system performance issues. If you have more than 1000 items to process, the system automatically creates a scheduled job using Schedule Jobs to Reset Cleared Items (F9296). For more information, see [Schedule Jobs to Reset Cleared Items (Optional)](#unique_73) [page ] 123. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Reset Cleared Items (F2223). |  |  |
| 3 | Search | Make the following entries and choose Go:Company Code: 3310Fiscal Year of Clearing Journal: <Current year> | A filtered list is displayed. |  |
| 4 | Execute | From the Clearing Entry list, choose the arrow icon > at the right of the row to reset. | The Clearing Entry view displays. |  |
| 5 | Reset | Choose the Reset button. | A Success dialog box displays with a Clearing XXXXXXX reset notification. |  |
| 6 | Save | Choose OK. |  |  |

##### Reset and Reverse Cleared Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reset and reverse a document that should not have been cleared.

|  |
| --- |
| Caution Resetting a large number of cleared documents can cause system performance issues. If you have more than 1000 items to process, the system automatically creates a scheduled job using Schedule Jobs to Reset Cleared Items (F9296). For more information, see [Schedule Jobs to Reset Cleared Items (Optional)](#unique_73) [page ] 123. |

Prerequisite

Invoices and payments are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Reset Cleared Items (F2223). |  |  |
| 3 | Search | Make the following entries and choose Go:Company Code : 3310Clearing Fisc. Year: <Current year> | The Clearing Entries list shows the filtered criteria. |  |
| 4 | Open Clearing Entry | Select the row of the clearing entry document and choose the > button at the right of the row. | The Clearing Entry view displays. |  |
| 5 | Process | Choose Reset and Reverse. | The Reverse Journal Entry dialog box is displayed. |  |
| 6 | Enter Reversal Data | Make the following entries and choose OK:Reversal Reason: For example, Wrong postingPosting date : <Today’s date> | The Success dialog box displays the message Document XXXXXX was posted in company code XXXX. |  |
| 7 | Continue | Choose OK. |  |  |

##### Schedule Jobs to Reset Cleared Items (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Schedule Jobs to Reset Cleared Items (F9296). | The Schedule Jobs to Reset Cleared Items view is displayed. |  |
| 3 | Create | Choose Create. | The New Job: Reset Cleared Items view is displayed. |  |
| 4 | Enter Job Details | Make the following entries and choose Step 2:Job Template: Reset Cleared ItemsJob Name: Reset Cleared Items |  |  |
| 5 | Enter Job Details | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Job Details | Make the following entries and choose Schedule:Clearing entry: <entry number>Company Code: 3310Fiscal Year: <fiscal year>, for example, 2026Note If you are performing a reversal along with the reset, enter additional information into the fields in the Reversal Parameters pane. | The Application Jobs view is displayed. |  |
| 7 |  | To refresh the review, choose the Go button. When the report status is Finished, choose the document button in the Results column for the job you scheduled. | Review the log results. |  |

##### Reverse Individual Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This transaction is used in General Ledger Accounting, in the area of Accounts Payables, and Accounts Receivables. It is used to display, edit, and reverse a document created in the financial modules.

|  |
| --- |
| Note Starting with the SAP S/4HANA Cloud 2208 release, if you are a new customer and want to enable advanced eDocument features such as eDocument Submit, Cancel and Reject, you must first activate the Document and Reporting Compliance features for your country/region. Otherwise, only Display mode is available. For more information, refer to Activate Document and Reporting Compliance Features in the Preliminary Steps section of the test script for scope item Document and Reporting Compliance (5XU). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Search Document | Make the following entries and choose Go:Company Code: <Any>Journal Entry Type: <Any>Period: <period>Fiscal Year: <year of the posted document>Posting Date: <posting date> | The system displays a list of document numbers. |  |
| 4 | Select Document | Select the Journal Entry to reverse and choose Reverse. | The Reverse Journal Entries view displays. |  |
| 5 | Enter Data | Make the following entries and choose OK:Reversal Reason: <Any>Posting Date: <today’s date>Tax Reporting Date: <today’s date>Period: optionalNote Use if reversing a check payment.Check Void Reason: Use if reversing a check payment | The Document is reversed by xxxxxx notification displays. |  |

### Invoice Collection Preparation

#### Display Customer Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, an overview of the payments and customer account balances is provided.

Prerequisite

Invoices are available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Customer Balances (F0703A). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Customer: 33100001Company Code: 3310Fiscal Year: <Current Year> | A table displays with the open balances per month for the year selected.The balances are displayed for the selected fiscal year. |  |
| 4 | Explore Balance Views | To navigate in the different views of the customer balance, select Balances, Special GL, or Compare.Choose Go after selecting the different view. | The different views of customer balances display. |  |

#### Manage Customer Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display and change line items in a customer account.

Prerequisite

Invoices are available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Line Items (F0711). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Customer: 33100001Company Code: 3310 |  |  |
| 4 | (Optional) Add Columns | As an option, choose the Gear (Settings) button to add columns to the Items table when the Administrator has added new fields.Note If you add columns to the table, you can save the view as a variant. For more information, see the [Add Fields to Items (Optional)](#unique_27) [page ] 50 preliminary step. Additionally, you can use the additional fields as filters in Adapt Filters. |  |  |
| 5 | Status | Select the Status in the filters and choose Go.If you choose All Items, the system displays all the account items.You can also choose to display only Open Items or Cleared Items. | The Items table displays the results of your criteria. |  |
| 6 | Date and Item Type | Make the following entries in the filters area:Clearing Date: <Today’s date>Note The Clearing Date field is only visible if you chose the Cleared Items status in the prior step. If you chose another status, the field is not available and you can ignore entry for it.Item Type: Normal Items |  |  |
| 7 | Execute Search | Choose the Go button. | The customer line items display according to your search criteria. |  |
| 8 | Change Document | Select a line item by choosing the checkbox of first column. |  |  |
| 9 | Change Document | Choose Edit Line Items. | The Edit Line Items dialog box displays. |  |
| 10 | Make Changes | Make required changes or additions to the line item from these available sections:Payment dataDunning DataAdditional data |  |  |
| 11 | Confirm Change | Choose the OK button. | The system displays the message Items Changed. |  |

### Interest Calculation

#### Schedule Interest Calculation Jobs

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

Open receivables exist in the system that satisfy the interest calculation requirements. The interest indicator must be assigned to the business partner and is explained in the Maintain Business Partners step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Interest Calculation Jobs (F4176). | The Application Jobs view displays. |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Calculate Item Interest for Accounts ReceivableJob Name: Calculate Item Interest for Accounts Receivable |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Customer Account: 33100001Company Code: 3310Interest Indicator: for example, 01Interest Calculation To: <for example, last day of current month>Test Run: Selected if you want to do a test run; Deselected if you want to do an actual run | The Application Jobs view is displayed. |  |
| 7 | View Report | To refresh the review, choose the Go button. When the report status is Finished, choose the document button in the Results column for the job you scheduled.Note You can also choose the Log button in the scheduled job row. When you do so, the job log is displayed, showing the output items. You can click on the output item link to display additional details. | The Document (ID xxxxxxx) view is displayed. The report shows the status of the journal entry document, and shows information such as the journal entry number, the amounts, and the interest. |  |
| 8 | View Report | Review the document, then choose Back. |  |  |
| 9 | Run Actual Report | If you performed a test run in step 6, repeat steps 6–8 with Test Run deselected to perform an actual run. |  |  |

#### Manage Interest Runs

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Interest Runs (F4485). |  |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Company Code: 3310Customer: 33100001 | A list of documents display in the Interest Documents pane. |  |
| 4 | View Interest Document | For the row for your interest document, choose the arrow button at the right of the row. | The Interest Run view is displayed for that document. The Items Subject to Interest pane shows related journal entry items, while the Output Items pane shows any outputs (for example, print or email) and their status. |  |
| 5 | Reverse Calculated Interests (Optional) | If needed, you can select the checkbox for an item and choose Reverse Calculated Interests.In the Enter Reverse Parameters dialog box, make the following entries and choose Confirm:Reversal Reason: <reversal reason> | The Messages dialog box displays the document posting. |  |
| 6 | Resend Interest Letter (Optional) | If needed, you can select the checkbox for an item and choose Send Interest Letters.On the Send Interest Letters dialog box, choose Yes to send the interest letter. | The Sent Interest Letters dialog box displays messages about the output channels from which the interest letters are sent. |  |

#### Display Interest Runs

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Interest Runs (F4485). |  |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Company Code: 3310 | A list of documents display in the Interest Documents pane. |  |
| 4 | View Interest Document | For the row for your interest document, choose the arrow button at the right of the row. | The Interest Run view is displayed for that document. The Items Subject to Interest pane shows related journal entry items, while the Output Items pane shows any outputs (for example, print or email) and their status. |  |

### Guarantees Made

#### Guarantees Made

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to create a guarantee.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Guarantees Made (F7934). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries and choose Post:General Information:Company Code: 3310Document Date: <Date>Posting Date: < Today’s Date>Date: < Today’s Date>Document Type: DATransaction Currency: <Co. Code currency>, for example, AEDLine Item Detail:Customer: <customer number >Amount in Transaction Currency: <Amount >Due On: <today's date + # days> | The guarantee is created.Note Once a decision is reached and action is taken on the made guarantee, the guarantee can be reversed. For more information, see the [Reverse Guarantees](#unique_81) [page ] 134 procedure. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Guarantees Made (F7934). |  |  |
| 3 | Enter Details | Select an entry and choose Reverse. | A dialog box is displayed. |  |
| 4 | Reverse | Confirm the reversal. | The guarantee is reversed. |  |

### Periodic Activities

#### Check Open Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step lists all Accounts Receivable line items.

Prerequisite

Invoices are created but not collected.

Procedure

To check open balances, follow the instructions from the previous procedure Invoice Collection Preparation > Manage Customer Line Items .

#### Create Balance Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a balance confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accounts Receivable Jobs (F2366). |  |  |
| 3 | Create | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Customer Balance ConfirmationJob Name: Customer Balance Confirmation |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | Make the following entries:General Selections section:Company Code: 3310Reconciliation Key Date: <Today’s date>Output Control section:Note Enter the values either for no reply or for reply.For no reply -Description: <any>Date of Issue: <Today’s date>No Reply: SelectedFor reply -Description: <any>Date of Issue: <Today’s date>No Reply: DeselectedDate of Reply: <Today’s date + 7>Reply To: <any business partner>Note The business partner must have a valid address.Use Print Bundling: When this box is selected, all letters are bundled into one print request. This results in the system sending all balance confirmation letters in a single print request, with the checklist being one separate output item.Tip We recommend selecting the print bundling option to simplify sending balance confirmation letters. |  |  |
| 7 | Check | Choose Check to verify that your entries are complete and correct. | The system displays the message You can go ahead and schedule your job. |  |
| 8 | Schedule | Choose Schedule. | The job is scheduled. |  |

#### Manage Balance Confirmations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage open balance confirmation letters and track the actual status. You can check open balances and confirm the amount in the system during the year-end closing to an external auditor.

Prerequisites

- Invoices are created and not collected.
- Preliminary steps for BRF settings are executed.
- Balance confirmation is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Balance Confirmations - For Customers (F2834). |  |  |
| 3 | Search | Make the following entry and choose Go:Company Code: <any> | A list of customer balance confirmations displays. |  |
| 4 | Selection | Select a row to display its details and status. | The Customer Balance Confirmation details view display. |  |
| 5 | Preview | In the Output Details section, in the Display column, choose Display Document. | The document displays in a new view. |  |

#### Print Customer Balance Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you print balance confirmation letters.

Prerequisites

- Invoices are created and not collected.
- Balance confirmation is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Balance Confirmations - For Customers (F2834). |  |  |
| 3 | Search | Make the following entries and choose Go:Company Code: <any> | A list of customer balance confirmations displays. |  |
| 4 | Selection | Select a row to display its details and status. | The Customer Balance Confirmation displays with details of the selected balance confirmation. |  |
| 5 | Preview | In the Output Details section, in the Display column, choose Display Document. | The document displays. |  |
| 6 | Print | Choose Print on the document. | The document prints. |  |

#### Bad Debt Write-Off

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Bad debt is a loss that a company incurs when credit that has been extended to customers becomes worthless, either because the debtor is bankrupt, has financial problems, or because it can't be collected. It's expensed on the income statement. Recognizing bad debt leads to an offsetting reduction to accounts receivable on the balance sheet – though businesses retain the right to collect funds should the circumstances change.

In this activity, you select customer invoices that are unrecoverable and post financial entries.

Prerequisites

Invoices are created but are not recoverable.

You must have customers in financial distress with debit balances that have to be zeroed out on the balance sheet.

You must have executed the [Assign Reason Codes For Write-Off](#unique_30) [page ] 52 preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Write Off Receivables (F6728). |  |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Company Code: 3310Customer: <customer> | The Receivables pane shows a list of results. |  |
| 4 | Details | For the row you want to work with, choose > (Details). | The Write-Off Receivables view is displayed. |  |
| 5 | Write Off | Note If necessary, change the values in the header area of the view to filter the list of items in the Accounts Receivable pane.In the Accounts Receivable pane, for the item you want to write off, choose the Write-Off >> button at the right of the row. | The line item is transferred to the Write-Off pane at the bottom right of the view. |  |
| 6 | Review and Post | In the Write-Off pane, review your line item. When you are done, choose Post.Note If you encounter an error during posting, you must ensure that the G/L account isn't tax-relevant. Log on as a General Ledger Accountant, then open the Manage G/L Account Master Data (F0731A) app. Search for the account using the Company Code View, using your company code. Choose the account in the results. In Controlling Data, under Account Control, select the Posting Without Tax Allowed checkbox, and save your changes. |  |  |

### eDocument Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change or maintain your eDocument status.

Prerequisites

To enable advanced eDocument features (such as eDocument Submit, Cancel, and Reject), new customers must first activate the Document and Reporting Compliance features for your country or region. For more information, see the Document and Reporting Compliance (5XU) test script, in the Prerequisites > Preliminary Steps > Activate Document and Reporting Compliance Features topic.

You must have set up an SAP BTP connection. Ensure that the communication system and communication arrangement are set up before you test this tep. For more information, see the setup instructions for Integrating with Peppol Exchange on the SAP Help Portal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk |  |  |
| 2 | Access the SAP Fiori App | Open eDocument Cockpit (EDOC_COCKPIT). |  |  |
| 3 | Select eInvoice Document | Make the following entry:Source Document: <invoice number from previous steps>Note You can also search for your invoice. In the Results Overview section, expand the nodes to find your local invoice. |  |  |
| 4 | Submit eInvoice | Select the row and choose Submit.Note To submit an eDocument, you must have an SAP BTP connection. See the Prerequisites section above for more information. | The eDocument status displays the message Action successfully executed: SUBMIT. |  |
| 5 | Review Status | Review the eDocument status. | Possible statuses for submitted eDocuments include:Acknowledged by ServiceRejected by ServiceValidation Passed |  |
| 6 | Display eDocument | Select the row for an eDocument with Accepted by receiving Access Point status.Choose Display > Display/Preview XML (or to display a PDF, Display > Display PDF . | The eDocument is shown in XML (or PDF) format. |  |
| 7 | Display Source Document | Select the row of an eDocument and choose Go To > Source Document . | A view displays of the original transaction that generated the eDocument (source document). |  |
| 8 | Back | Choose Back. |  |  |
| 9 | Review eDocument History | To review the eDocument history, choose Go To > History . | The view displays the last process steps and statuses from selected eDocument. |  |
| 10 | Back | Choose Back. |  |  |
| 11 | Review Application Log | Choose Go To > Application Log .When there are no errors, a No Application Log found for the selected eDocument notification displays at the bottom of the view.If there are errors, an Application Log dialog box displays with information about the error. Review the message and choose Continue to close the dialog box. |  |  |
| 12 | Message Dashboard | Access Message Dashboard.If you encounter errors, a dialog box displays information about the error. Review the message and choose Continue to close the dialog box. |  |  |
| 13 | Cancel eDocument | To cancel an eDocument, select the row of an eDocument with Created status and choose More > Cancel eDocument . | The status of eDocument changes to eDocument Cancelled and the status icon turns green. |  |
| 14 | Delete eDocument | To delete an eDocument, choose a row from the list with a Created status.Select an eDocument in status Created and choose More > Delete eDocument . | At the bottom of the view a Number of eDocuments that have been deleted: 1 notification displays. |  |

## Appendix

### Display Process Flow Accounts Receivable

Purpose

This app lets you graphically display the relationship between individual business objects of the Accounts Receivable work area (for example, sales orders, deliveries, clearing, accounting, and quotations).

Prerequisite

Documents that generate the Accounts Receivable process must be created, for example:

- Outgoing invoice
- Sales order
- Clearing
- Payment

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Process Flow - Accounts Receivable (F2692). |  |  |
| 3 | Data Entry | Make the following entries and choose Go:Document Type: <document type>Note Select a document type according to the origin of the document.Document Number: <any document number according to document type selected>Note If you select either Journal Entry or Clearing Entry in the Document Type field, additional fields appear:Fiscal year: <Current year>Company Code: 3310 | The Process Flow pane shows the selected document and its relationships to other documents in the process flow. |  |
| 4 | Exit | Choose Back. |  |  |

### Manage Payment Advice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create, display, change, and delete payment advice. The advice explains the usage of the payment and is used for clearing.

A payment advice note contains the incoming payment details required to allocate and clear the relevant open item.

|  |
| --- |
| Note For more information on the Manage Payment Advices (F2550A) app, see the [Manage Payment Advices (New Version)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/b52c712083694a649f04b3f2ee8211f4.html?version=LATEST) page on the SAP Help Portal. |

Prerequisite

A business partner exists.

An open incoming payment document exists (document posted on account).

An OPTIONAL prerequisite is completing the [Manage Situation Types (Optional)](#unique_25) [page ] 48 procedure in the Preliminary Steps section of the Prerequisites, allowing you to complete the (Optional) Monitor Notification process in this procedure.

Procedure - Manually Create Payment Advice

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Payment Advices (F2550A). |  |  |
| 3 | Add Manually | Choose Create. | The Payment Advice view displays. |  |
| 4 | General Information | In the General Information section, enter the following data:Company Code: 3310Subledger: Accounts ReceivableSupplier: 33100001Payment Amount: 500Currency: AED |  |  |
| 5 | Payment Advice Items | In the Payment Advice Items section, new lines are added automatically once a field in the existing line is filled in. |  |  |
| 6 | More Fields | Choose the Settings (gear) button.Select the following checkboxes and choose OK:Alternative AccountAlternative Company CodeAssignment | Fields are displayed. |  |
| 7 | Payment Advice Items | In the Payment Advice Items section, enter the following data:Reference: <reference document number>Document Date: <Date when the document was posted>.Payment Amount: <Total payment amount>Alternative Account: <customer number>Alternative Company Code: 3310Assignment : <document number>If there are more documents to add, enter them on a new row. |  |  |
| 8 | Create | Choose Create. |  |  |

Procedure - Change Payment Advice

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Payment Advices (F2550A). |  |  |
| 3 | Enter Search Criteria | Enter search criteria and choose Go:Editing Status: AllCompany Code: 3310 | A table shows the information of all payment advices. |  |
| 4 | Select | For a payment advice number, choose > (Details) at the right of the row. | Payment advice details are displayed. |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Save | Make any changes and choose Save. |  |  |

Procedure - Delete Payment Advice

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Payment Advices (F2550A). |  |  |
| 3 | Enter Search Criteria | Enter search criteria and choose Go:Editing Status: AllCompany Code: 3310 | A table shows the information of all payment advices. |  |
| 4 | Search | In the Manage Payment Advices view, select the payment advice to be deleted. |  |  |
| 5 | Delete | Choose Delete. | A notification displays, asking to confirm deletion. |  |
| 6 | Confirm | Choose Delete. | Payment advice is deleted. |  |

Procedure - Monitor Notification

If you performed the [Manage Situation Types (Optional)](#unique_25) [page ] 48 procedure in Preliminary Steps, the following procedure is available to you.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Open Notifications | Choose the Notifications button at the top right of the view.Choose the payment advice notification generated by the system. |  |  |
| 3 | Review Notification | The payment advices details for the notification display.Choose Back. |  |  |

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
> Flagged while digesting this document, not verified: Overview table lists Manage Payment Advices - Deprecated (F2550) while the appendix documents newer F2550A; both appear in the same script

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample customer is given as 3310000133100002 in the master data table but 33100001 in the test procedures

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/customer-payments-1s0-ae-test-script-760]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J59_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 230,608 chars in the whole document
