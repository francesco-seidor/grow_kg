---
id: 03-financial-accounting-and-close/payroll-processing-with-sap-successfactors-employee-central-payroll-1n
title: Payroll Processing with SAP SuccessFactors Employee Central Payroll (1NL) - Test Script (1NL_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1NL: cost center replication, payroll posting to FI, and country-specific procedures (US, ES, PT, BR, CO)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/payroll-posting-integration]
aliases: [1NL_S4CLD2608_BPD_EN_XX]
keywords: [Payroll Posting Integration (Employee Central Payroll and…, payroll posting, cost center replication, posting run release, third-party remittance, withholding tax return, test scripts, brazil branch data, colombia dian reporting, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NL_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-747
topic: 03-financial-accounting-and-close/payroll-posting-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Payroll Processing with SAP SuccessFactors Employee Central Payroll (1NL) - Test Script (1NL_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NL_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Payroll Posting Integration (Employee Central Payroll and HCM Payroll)** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Payroll Processing with SAP SuccessFactors Employee Central Payroll (1NL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858613)

[2 Prerequisites 4](#_Toc232858614)

[2.1 System Access 4](#_Toc232858615)

[2.2 Roles 4](#_Toc232858616)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232858617)

[2.4 Additional Manual Configuration 5](#_Toc232858618)

[3 Overview Table 6](#_Toc232858619)

[4 Test Procedures 7](#_Toc232858620)

[4.1 Cost Center Replication 7](#_Toc232858621)

[4.1.1 Maintain Cost Center 7](#_Toc232858622)

[4.1.2 View Cost Center Data 9](#_Toc232858623)

[4.2 Payroll Posting 11](#_Toc232858624)

[4.2.1 Execute Live Posting Run 11](#_Toc232858625)

[4.2.2 Release and Post Documents 15](#_Toc232858626)

[4.2.3 View Transferred Documents in SAP S/4HANA Cloud Public Edition 16](#_Toc232858627)

[4.3 Country/Region-Specific Procedures 17](#_Toc232858628)

[4.3.1 USA and Canada 17](#_Toc232858629)

[4.3.1.1 Third-Party Remittance 17](#_Toc232858630)

[4.3.1.1.1 Create Evaluation Run 17](#_Toc232858631)

[4.3.1.1.2 Create Posting Documents 20](#_Toc232858632)

[4.3.1.1.3 Post Documents to SAP S/4HANA Cloud Public Edition 21](#_Toc232858633)

[4.3.1.1.4 View Transferred Documents in SAP S/4HANA Cloud Public Edition 23](#_Toc232858634)

[4.3.1.1.5 View the Confirmation in Employee Central Payroll 23](#_Toc232858635)

[4.3.2 Spain 24](#_Toc232858636)

[4.3.2.1 Withholding Tax Return 24](#_Toc232858637)

[4.3.2.1.1 Withholding Tax Return 25](#_Toc232858638)

[4.3.2.1.2 View the Employment Tax Report in SAP SuccessFactors Employee Central Payroll 26](#_Toc232858639)

[4.3.3 Portugal 27](#_Toc232858640)

[4.3.3.1 Withholding Tax Return 27](#_Toc232858641)

[4.3.3.1.1 Withholding Tax Return 27](#_Toc232858642)

[4.3.3.1.2 View the Employment Tax Report in SAP SuccessFactors Employee Central Payroll 28](#_Toc232858643)

[4.3.4 Brazil 29](#_Toc232858644)

[4.3.4.1 Branch Data in Brazilian Reports 29](#_Toc232858645)

[4.3.4.2 Branch Information 30](#_Toc232858646)

[4.3.4.3 View Branch Data in CAGED Report 30](#_Toc232858647)

[4.3.5 Colombia 31](#_Toc232858648)

[4.3.5.1 DIAN Statutory Reporting 31](#_Toc232858649)

[4.3.5.1.1 DIAN 32](#_Toc232858650)

[4.3.5.1.2 View Social Insurance Contribution in SAP S/4HANA Cloud Public Edition 33](#_Toc232858651)

[5 Appendix 34](#_Toc232858652)

[5.1 Process Integration 34](#_Toc232858653)

[5.1.1 Preceding Processes 34](#_Toc232858654)

## Purpose

Overview

For customers who want to integrate SAP SuccessFactors Employee Central Payroll and SAP S/4HANA Cloud Public Edition, this scope item gives you the security of direct connectivity to post your payroll results to your financial system in SAP S/4HANA Cloud Public Edition using Web Services. As an example, this can be used to validate cost centers, check accounting assignments, or display journal entries. In addition, it ensures the availability of all cost center data in the payroll system.

Based on the additional country/region-specific posting functionality, ensure that the corresponding country/region is supported and has no limitations via SAP Notes 2707220 and 3537575.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP SuccessFactors Employee Central | Accessible via SAP GUI or web-based GUI, your system administrator provides you with the URL and system IDs to access the system. |

### Roles

SAP S/4HANA Cloud Public Edition

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER |  |

SAP SuccessFactors Employee Central

| Business Role | Business Role ID | Log On |
| --- | --- | --- |
| Administrator - HR Info | SAP_BR_ADMINISTRATOR_HRINFO |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master Data | Value | Details | Comments |
| --- | --- | --- | --- |
| Company code | 1710 | Company code USA | Company code for SAP S/4HANA Cloud Public Edition and SAP SuccessFactors Employee Cental Payroll |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/a9dd572ca5667d09365d87ad57496dc2)

## Overview Table

This scope item consists of several process steps, reports, or items provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

- Cost Center Replication:

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Cost Center](#unique_8) [page ] 7 | Cost Accountant - Overhead | Manage Cost Centers - Old Version (F1443A) | A new cost center has been created and an existing one has been updated. |
| [View Cost Center Data](#unique_9) [page ] 9 | Administrator - HR Info | KS03 | The data of the new cost center and the updated cost centers has been viewed. |

- Payroll Posting:

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Execute Live Posting Run](#unique_10) [page ] 11 | Administrator - HR Info | PC00_M99_CIPE01 |  |
| [Release and Post Documents](#unique_11) [page ] 15 | Administrator - HR Info | PCP0 |  |
| [View Transferred Documents in SAP S/4HANA Cloud Public Edition](#unique_12) [page ] 16 | General Ledger Accountant | Manage Journal Entries (F0717A) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Cost Center Replication

The following sections describe the procedures for executing the cost center data replication from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central Payroll. At high level, this process is as follows: you change the existing cost center hierarchy in SAP S/4HANA Cloud Public Edition. The changes are then replicated automatically to the SAP SuccessFactors Employee Central Payroll system, where they can be checked for correctness.

#### Maintain Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The Cost Accountant - Overhead maintains one or several cost centers. That means that the accountant either creates a new cost center in an already replicated cost center hierarchy, or updates an already replicated cost center, including name and description maintenance in different languages.

|  |
| --- |
| Note In both cases, a delta replication is triggered. The newly created cost center within the hierarchy or the adaptations performed on the existing cost center are transferred to SAP SuccessFactors Employee Central Payroll. |

Prerequisite

The SAP S/4HANA system must support multiple languages.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Cost Accountant - Overhead. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access Appropriate Fiori App | Open Manage Cost Centers - Old Version (F1443A). |  |  |
| 3 | Enter Controlling Area | Choose the My Area icon on the upper left corner of the screen. From the area, which expands, choose Settings.In the upcoming Settings dialog box, choose Default Values.In the CO Area field, choose A000 from the value help and choose Save. |  |  |
| 4 | Search Existing Cost Centers | Back on the Manage Cost Center screen, enter criteria as appropriate and choose Go. From the list of search results, mark a cost center. |  |  |
| 5 | Add a New Cost Center | Choose Add in the lower right corner of the screen. | A new screen, Cost Center: New, opens in addition to the Manage Cost Center screen. |  |
| 6 | Enter Basic Information of New Cost Center | In the New Cost Center section of the screen, make the following entries:Controlling Area: defaults to A000; leave as isCost Center: cost center IDValid From: validity start dateValid To: defaults to system high date; enter the appropriate data or leave as it is.In the Reference section of the screen, choose a controlling area and cost center as reference, if appropriate.Then choose Continue. |  |  |
| 7 | Enter Master Data of New Cost Center | In the General Data section, make the following entries:Cost Center: cost center name.Cost Center Description: cost center description.Person Responsible: cost center manager.Cost Center Category: Choose from value help.User Responsible: optionally, you can enter user ID of the person for the cost center.Department: optionally, you can enter the name of the department to which the cost center belongs.In the Organizational Units section, make the following entries:Hierarchy Area: Choose from value help.Company Code: Choose from value help.Business Area: Choose from value help.Currency: defaulted to USD based on company code. This is a read-only field.Profit Center: Choose from value help. |  |  |
| 8 | Save New Cost Center | Choose Save on the upper left corner. | A success message is generated by the system about saving the data. |  |
| 9 | Exit Cost Center Creation Screen | Choose the browser close. | You return to the Manage Cost Center page. |  |
| 10 | Search Cost Center to be Changed | On the Manage Cost Center screen, in the Standard section, enter search criteria using the value help and choose Go. | The cost centers matching your search criteria are listed in the Search Results section of the Manage Cost Center screen.If your search criteria aren’t listed in the search results, you can choose the cost center from the existing controlling area. |  |
| 11 | Choose Cost Center to be Changed | In the Search Results list, mark the cost center you want to change and choose Edit in the lower right corner of the screen. | A new screen, Cost Center: cost center ID, cost center name, opens in addition to the Manage Cost Center screen. |  |
| 12 | Update Cost Center Data | On the Cost Center: cost center ID, cost center name screen, modify for example the description, and choose the Save icon in the upper left corner. | A success message is generated by the system about saving the data. |  |
| 13 | Exit Cost Center Edit Screen | Choose the browser close. | You return to the Manage Cost Center page. |  |

#### View Cost Center Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

The Administrator - HR Info checks whether the cost center updates have been replicated correctly to SAP SuccessFactors Employee Central Payroll system. You ensure that the new cost center has been replicated and the existing cost centers have been updated as expected.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as Administrator - HR Info. | The SAP Easy Access Menu page is displayed. |  |
| 2 | Search Newly Created Cost Center | SAP Easy Access menu path:Accounting > Controlling > Cost Center Accounting > Master Data > Cost Center > Individual Processing > Display .Alternatively, access it via transaction code KS03. |  |  |
| 3 | Enter Controlling Area | In the dialog box, enter the Controlling Area A000. | The Display Cost Center: Initial Screen is displayed. |  |
| 4 | Enter Cost Center | On the Display Cost Center: Initial Screen, enter the cost center ID, which was created earlier in your SAP S/4HANA system, in the Cost Center field. Alternatively, you can search the Cost Center from the search help. Search and select the new cost center you’ve created in SAP S/4HANA and replicated to SAP SuccessFactors Employee Central Payroll. |  |  |
| 5 | Choose Enter | Check if the new cost center has been replicated correctly from SAP S/4HANA.For details on the field mapping between SAP S/4HANA and SAP SuccessFactors Employee Central Payroll, refer to the table at the end of this test step. |  |  |
| 6 | Search Updated Cost Center | SAP Easy Access menu path:Accounting > Controlling > Cost Center Accounting > Master Data > Cost Center > Individual Processing > Display .Alternatively, access it via transaction code KS03. |  |  |
| 7 | Enter Cost Center | On the Display Cost Center: Initial Screen, enter the cost center ID, which was created earlier in your SAP S/4HANA system, in the Cost Center field. Alternatively, you can search the Cost Center from the search help. Search and select the new cost center you’ve created in SAP S/4HANA and replicated to SAP SuccessFactors Employee Central Payroll. |  |  |
| 8 | Check Updated Cost Center Data | Check if the changed data, for example the description, has been replicated correctly from SAP S/4HANA. |  |  |

### Payroll Posting

Use

The Administrator - HR Info executes the payroll run for a selected payroll area for a certain pay period.

The system accesses a country/region-specific payroll program. It determines the current payroll period from the payroll control record and performs payroll using the values the Payroll Process Administrator entered in the payroll program.

In order to proceed to the next steps, the payroll must be executed successfully without any errors and should be in Exit state. The processing of payroll isn’t part of this test script.

#### Execute Live Posting Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Payroll has been completed and the Administrator - HR Info begins the posting process to the financial system.

|  |
| --- |
| Note To run a production posting run, the payroll control record must be in status Exit Payroll. For simulation runs, the payroll control record can be left in status Released for Correction. |

The posting run to Financial Accounting (FI) creates a posting document that is transferred to SAP S/4HANA Cloud Public Edition, and the information is used to post an FI document. The information is reflective of the expense and liability posting for Payroll.

Posting to accounting includes the evaluation of the payroll results, the creation of summarized documents, and posting them in the accounting components.

|  |
| --- |
| Note The documents created in posting to accounting contain summarized information. However, provided you have authorization, you can trace back which information (from the payroll results) the posting documents are based on for a specific personnel number. |

When posting to accounting, the following activities are to be performed:

- Creating a Posting Run
- Checking a Posting Run
- Checking the Posting Documents
- Releasing Posting Documents
- Posting Documents
- Checking Accounting Documents
- Checking the Completeness of the Postings
- Subsequent Activities in Financial Accounting

|  |
| --- |
| Note A simulation of a posting run must be executed before and after completing the payroll. In this way, you can recognize posting-relevant errors in the payroll results early and avoid errors when creating a productive posting run. The simulation and productive run are executed using the same transaction as mentioned here. |

Procedure

The Administrator - HR Info checks for payroll execution and verifies that the status of the payroll is in Exit state.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP SuccessFactors Employee Central Payroll as Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the transaction Posting Run | SAP Easy Access menu path:Human Resources > Payroll > Americas > USA > Subsequent Activities > Per Payroll Period > Evaluation > Posting to Accounting > Execute Posting Run .Alternatively, access it via transaction code PC00_M99_CIPE. | The Posting to Accounting: Create Posting Run page is displayed. |  |

Payroll Period:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Period | The time-period to be processed.For productive runs, choose value Current Payroll Period from the dropdown list. | The default value is the current period. |  |
| 2 | Payroll area | The area for which posting to financial accounting is simulated.Use the dropdown menu for valid options. Select US (HR-US for monthly).Note The payroll area may be different in your system. Use the payroll area for which the payroll has been executed. | Caution Use one payroll area at a time. Don’t run payroll area ranges. |  |
| 3 | Period | Payroll time period other than the current.The user inputs the time period to process. There’s no dropdown menu. | For simulation only. |  |

Selection Criteria:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Personnel number | Personnel numbers of the employees to be processed.Leave empty if you’re running the payroll for all employees in that payroll area. | For productive runs, don’t enter any values. Leave empty instead. |  |
| 2 | Payroll area | The area for which posting to financial accounting is simulated.Use the dropdown menu for valid options.Enter the same value as in the Payroll area field from the payroll period section. | Caution Don’t run for payroll area ranges. |  |

Run Attributes:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Off-cycle payroll run | Leave empty unless processing an off-cycle payroll run | Used for the special, or off-cycle payroll run.Empty value in the first field Payroll Type indicates a regular payroll run. Use dropdown menu to choose a payroll type if it’s a special payroll run.The second field is used to differentiate between multiple special payroll runs from the same day.The third field is the date of the special payroll run. |  |
| 2 | Type of document creation | Type of document to be created for postings. Enter value P using value help. | Value P means live posting run. |  |
| 3 | Output log | An indicator that specifies whether or not an output log of the posting entry is to be displayed.If you want to print the entire entry, select this box. |  |  |
| 4 | Text on posting run | Text to be delivered on the FI document.Enter text to identify the posting document if necessary. |  |  |

Specify posting date:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Acc. to period definition | Leave empty.Based on payroll period calendar. | Ensure that you use this option only for one employee at a time.If you choose the Display Log option for all employees, it increases payroll runtime and produces the output log for everybody. The output log is for debugging purposes only and wouldn’t make sense to be run for the entire payroll area. |  |
| 2 | Acc. to payment date | Pay date, flag this field. | The posting date is equal to pay date. |  |
| 3 | Manually | Leave empty. | Posting date to be entered manually. |  |

Data for document creation:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Document date | FI document posting dateIf left empty, current date is used as default. |  |  |
| 2 | Posting variant | Variant that determines FI document type, and line item text defaults.SAP is the standard variant. |  |  |
| 3 | Execute posting run | Choose Execute to generate productive posting document. After the successful run, a new screen appears. | You’re redirected to the Posting to Accounting: Document overview screen. |  |

Result

The created posting run acquires the Documents Created status and is saved. It has a clear number. The status of the accompanying posting documents changes to Created. An index of all processed payroll results is created. This index makes it possible to trace creation of a document item although the documents have been summarized.

#### Release and Post Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The Administrator - HR Info processes the financial accounting posting run.

When checking a productive posting run and the accompanying posting documents, the HR Administrator ensures that all posting documents are technically correct with appropriate contents. To post the posting documents, the Administrator - HR Info has to release all posting documents first for the posting run.

The posting run receives the status All documents released, and the HR Administrator can post the posting documents. All the posting documents belonging to a posting run are to be posted together in the Accounting component. Individual posting documents can’t be posted.

Prerequisite

A financial accounting posting run has been created with the status of Documents created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the transaction, Edit Posting Run | SAP Easy Access menu path:Human Resources > Payroll > Americas > USA > Subsequent Activities > Per Payroll Period > Evaluation > Posting to Accounting > Process Posting Run .Alternatively, access it via transaction code PCP0. | The Display Posting Runs page is displayed. |  |
| 3 | Display Posting Run | On the Display posting runs screen, choose the posting documents to be released and then choose the Display Settlement Documents icon. |  |  |
| 4 | Release Documents | On the Posting to Accounting: Document overview screen, choose the documents to be released by choosing the appropriate checkbox in the Document column of the table. Choose the Release document pushbutton to release the document.In the dialog box, choose Yes to release the posting documents or No to terminate the process.Choose Back. | Note down the type and run number to identify the document in the SAP S/4HANA system. |  |
| 5 | Return to the previous screen | Go back to the Display Posting Run screen. The status of the document that you’ve released should be All documents released. |  |  |
| 6 | Post Documents | Choose the document that was released, and choose the icon Post documents.In the dialog box, choose Immediately or Create job to start the posting to Finance (or Cancel, to cancel the reversal). |  |  |

Result

The posting documents were posted to the appropriate components in Accounting. The posting run has the status Documents posted.

#### View Transferred Documents in SAP S/4HANA Cloud Public Edition

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
| 1 | Log On | Log on to SAP Fiori launchpad as an General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | On the Home screen, open the Manage Journal Entries (F0717A) app. |  |  |
| 3 | Search for Entries | On the Manage Journal Entries (F0717A) screen, enter selection criteria as appropriate, for example, Company Code and Posting Date (Period) for which the document has been posted in EC Payroll system. Choose Go.In the search results, look for Header Text, which is the combination of the Document Type and the Run Number from the posting document that was posted from SAP SuccessFactors Employee Central Payroll, for example PP0000000001. |  |  |

### Country/Region-Specific Procedures

This section is only relevant if you have any country/region-specific functionality, which requires additional procedures on top of the international payroll posting. You find details for the respective countries/regions in the following subsections.

#### USA and Canada

##### Third-Party Remittance

Use

The Administrator - HR Info executes the payroll run for a selected payroll area for a certain pay period. In this test case, the accumulated federal withholding taxes, which were deduced from employees’ payment during payroll execution, are sent to the tax authority.

###### Create Evaluation Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The Administrator - HR Info validates the following items:

- Vendors are created in SAP SuccessFactors Employee Central Payroll and are synchronized with SAP S/4HANA Cloud Public Edition.
- HR payees are configured according to the payment method bank transfer (T) and check (C).
- Infotypes (0001,0002,0006,0007,0008,0009,0207,0208,0209,0210) are maintained for all employees to be included in the payroll run.
- Payroll has been executed successfully without any errors and is in Exit state.
- The Result table has an entry for withholding tax.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the Transaction | SAP Easy Access menu path:Human Resources > Payroll > Americas > USA > Subsequent Activities > Per Payroll Period > Evaluation > Third-Party Remittance > Evaluate Remittance (New)Alternatively, access it via transaction code PC00_M99_URME. |  |  |

Payroll Period:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Time Period | The time period to be processed.The default value is the current period.For productive runs, choose the value Other Payroll Period from the dropdown list. |  |  |
| 2 | Payroll Area | The area for which posting to financial accounting is simulated.Use the dropdown menu for valid options. Select US (HR-US for monthly).Note The payroll area may be different in your system, Use the payroll area for which the payroll has been executed.Caution Use one payroll area at a time. Don’t run payroll area ranges. |  |  |
| 3 | Time Period | Payroll time period other than the current.The user enters the time period to process. There’s no dropdown menu. |  |  |

Selection Criteria:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Personnel Number | Personnel numbers of the employees to be processed.Leave empty if you’re running the payroll for all employees in that payroll area. |  |  |
| 2 | Payroll Area | The area for which posting to financial accounting is simulated.Use the dropdown menu for valid options.Enter the same value as in the Payroll Area field from the payroll period section.Caution Don’t run for payroll area ranges. |  |  |

HR Payee Type to be posted:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | HR Payee Type | Select the payee type from the value help. |  |  |

Control Data:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | ALV Control | Select a view according to your requirements. | Default is Grid View. |  |

Level of Details on double-click:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Make a Selection | Check the boxes for which the information is required. |  |  |

Detail for list output:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Include Period Info | Check this box if period information is required. |  |  |

Processing Option:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Production Mode | Choose Production Mode. |  |  |

Display Log:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Display Log | Check the box for Display Log. |  |  |
| 2 | Execute | Choose Execute. |  |  |

Result

The evaluation run should have the status Successful.

###### Create Posting Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The evaluation run was successful and the symbolic accounts are synchronized with the G/L accounts in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the Transaction | SAP Easy Access menu path:Human Resources > Payroll > Americas > USA > Subsequent Activities > Per Payroll Period > Evaluation > Third-Party Remittance > Create Posting Run .Alternatively, access it via transaction code PC00_M99_URMP. |  |  |
| 3 | Posting Data Selection | Company Code: Choose the correct company code, for example, 1710.Due Date: Enter the current date. |  |  |
| 4 | Transfer Parameters | Text on Posting Run: For example, 3PR Posting.Posting Date: Enter the current date.Posting variant: SAP.Document Date: |  |  |
| 5 | Processing Option | Choose Production. |  |  |
| 6 | Execute | Choose Execute. |  |  |

Result

The posting run has the status Successful and a posting document type TP has been created in the system. You can check the document by entering transaction code PCP0 and searching for the newly created entry with your user and document type TP. The checkbox for Simulation must be unchecked. Once you open the document, you see that several documents have been created. Open each document and make sure that one of them is the document type G/L Account Document and others are Vendor Documents.

###### Post Documents to SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The evaluation run was successful and the posting documents were created successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the Transaction | SAP Easy Access menu path:Human Resources > Payroll > Americas > USA > Subsequent Activities > Per Payroll Period > Evaluation > Third-Party Remittance > Process Posting Run .Alternatively, access it via transaction code PCP0. |  |  |
| 3 | Search for Entries | In the Display Posting Run screen, in the Posting Third-Party Remittance section, look for the posting document that was created in section [Create Posting Documents](#unique_19) [page ] 20. |  |  |
| 4 | Release Documents | Open the entry with the posting document and select all the documents inside it. In the menu bar, choose the button that says Release Documents.Go back to the Display Posting Run screen.The status of the Third-Party Remittance has changed from Documents Created to All Documents Released. |  |  |
| 5 | Post the Documents | Select the released document and choose Post Documents in the menu bar.In the next screen, in the Post Documents section, the message text is Documents Posted Successfully. |  |  |

Result

You've posted your documents to SAP S/4HANA Cloud Public Edition. Note down the reference number of all the posted documents. The reference number looks, for example, like this: HR    0000000001   or HRGRNX0000000001.

###### View Transferred Documents in SAP S/4HANA Cloud Public Edition

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | On the Home screen, choose Manage Journal Entries (F0717A). |  |  |
| 3 | Search for Entries | On the Manage Journal Entries (F0717A) screen, enter selection criteria as appropriate, for example, Company Code and Posting Date (Period) for which the document has been posted in SAP SuccessFactors Employee Central Payroll system.Choose Go.In the Filter settings of the list, add the Reference column.In the search results, look for the reference numbers that were posted in SAP SuccessFactors Employee Central Payroll.For each document, you find two entries: one general ledger account document and one vendor document. |  |  |

###### View the Confirmation in Employee Central Payroll

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The posted documents in SAP S/4HANA Cloud Public Edition are successfully paid out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as an Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the Transaction | Open the transaction code SE38. | . |  |
| 3 | Search for Entries | In the Program Name screen, enter the report name RPURMR00 and execute it. |  |  |
| 4 | Selection Screen | In the selection screen, enter the company code and the HR document reference number that you've noted down before. |  |  |
| 5 | Remittance Overview | In the column Acknowledgment number, check if it contains any numbered value. If it has any random number value, then the documents have successfully been paid out. |  |  |

Result

The documents are posted successfully to SAP S/4HANA Cloud Public Edition and the acknowledgment has been received.

#### Spain

##### Withholding Tax Return

Use

The employment tax reports (IRPF) for the tax office (forms 190) can be paid out from SAP S/4HANA Cloud Public Edition and can be seen in SAP SuccessFactors Employee Central Payroll.

###### Withholding Tax Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The Accounts Payable Manager validates the following items:

- A business partner (vendor) of type Person with role Supplier has been created in SAP S/4HANA Cloud Public Edition.
- The supplier role has the company code for Spain assigned.
- The company code has been assigned with all relevant accounting information and with withhold tax types.
- For the withholding tax type, the checkbox is enabled.
- An invoice with the business partner and a tax amount has been created and posted.
- The invoice has been paid out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | On the Home screen, choose Prepare Withholding Tax Return - Spain (S_PL0_09000447) |  |  |
| 3 | Vendor Selection | On the Vendor Selection screen, select the Vendor Account and Company Code.Note Use the same business partner that is mentioned in the prerequisites. |  |  |
| 4 | Country/region Variant | In the field country/region Variant, select ES. |  |  |
| 5 | Output Control | Unselect Form Printout and select the checkbox Fill Table for DME. |  |  |
| 6 | Execute | Choose Execute. |  |  |

Result

The tax return has been successfully withheld and the information has been transferred back to SAP SuccessFactors Employee Central Payroll.

###### View the Employment Tax Report in SAP SuccessFactors Employee Central Payroll

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The tax return has been successfully withheld in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as an Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the Transaction | Open transaction code SE38. | The Employment Tax (IRPF) report page is displayed. |  |
| 3 | Search for Entries | On the Program Name screen, enter the report name RPC190E0 and press Enter. |  |  |
| 4 | Selection Screen | In the Period section, select Other Period.In the Selection of Results screen, enter the required entries.Select the checkbox for Accounting Data.Choose Execute. |  |  |
| 5 | Display Log | View the result. |  |  |

#### Portugal

##### Withholding Tax Return

Use

The employment tax reports (IRPF) for the tax office (forms 190) can be paid out from SAP S/4HANA Cloud Public Edition and can be seen in SAP SuccessFactors Employee Central Payroll.

###### Withholding Tax Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The Accounts Payable Manager validates the following items:

- A business partner (vendor) of type Person with role Supplier has been created in SAP S/4HANA Cloud Public Edition.
- The supplier role has the company code for Spain assigned.
- The company code has been assigned with all relevant accounting information and with withhold tax types.
- For the withholding tax type, the checkbox is enabled.
- An invoice with the business partner and a tax amount has been created and posted.
- The invoice has been paid out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager. |  |  |
| 2 | Access the SAP Fiori App | On the Home screen, choose Withholding Tax Return (PT). |  |  |
| 3 | Vendor Selection | On the Vendor Selection screen, select the Vendor Account and Company Code.Note Use the same business partner that is mentioned in the prerequisites. |  |  |
| 4 | Country/region Variant | In the field country/region Variant, select PT. |  |  |
| 5 | Output Control | Unselect Form Printout and select the checkbox Fill Table for DME. |  |  |
| 6 | Execute | Choose Execute. |  |  |

Result

The tax return has been successfully withheld and the information has been transferred back to SAP SuccessFactors Employee Central Payroll.

###### View the Employment Tax Report in SAP SuccessFactors Employee Central Payroll

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The tax return has been successfully withheld in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as an Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the Transaction | Open transaction code SE38. | The Employment Tax (IRPF) report page is displayed. |  |
| 3 | Search for Entries | On the Program Name screen, enter the report name RPC190E0 and press Enter. |  |  |
| 4 | Selection Screen | In the Period section, select Other Period.In the Selection of Results screen, enter the required entries.Select the checkbox for Accounting Data.Choose Execute. |  |  |
| 5 | Display Log | View the result. |  |  |

#### Brazil

##### Branch Data in Brazilian Reports

Use

Brazilian HCM solutions use a function to retrieve data from the financial system in SAP S/4HANA Cloud Public Edition using web services.

The Brazilian reports and functionalities that use branch data retrieved from the financial system are:

- eSocial events such as S-1000 and S-1005
- HBR3RDE0 - Lista de contribuições a Terceiros
- HBRMANAD - Manual Normativo de Arquivos Digitais - MANAD
- HBRGPS00 - Impressão do formulario de GPS
- HBRDARF0 - Relatório DARF
- HBRCEDT0 - Comprovante de remuneração
- HBRCAGED - CAGED: relatório e arquivo

##### Branch Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The Accounts Payable Manager validates the following items: A business place for a Brazilian Tax Entity (CNPJ) has been created in SAP S/4HANA Cloud Public Edition. The business place has the company code for Brazil assigned.

The company code has been assigned with all relevant accounting information.

Procedure

To create specific fields for business place, please refer to scope item Create Master Data for Brazil (JD0_BR).

Result

Branch data is maintained in SAP S/4HANA Cloud Public Edition.

##### View Branch Data in CAGED Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The branch data is present in SAP S/4HANA Cloud Public Edition.

An employee has been hired in that branch in a brazilian company.

An employee has all the required infotypes (0000,0002,0001,0006,0007,0008,0009,0021,0057,0016).

An employee has infotype 0016 with complementary information in infotype 0398 (Legal information).

The payroll for that employee has been executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as an Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the Transaction | Open transaction code SE38. |  |  |
| 3 | Run Report | On the Program Name screen, enter the report name HBRCAGED and press F8. | The CAGED/GREU report is displayed. |  |
| 4 | Selection Screen | In Further Selections, add Personnel Number as a filter.In the Selection of Results screen, enter the Personnel Number and Company Code.In the Period section, inform the period in which the payroll was executed for that employee.Choose Execute. |  |  |
| 5 | Display Temse File | View the result. | Branch data is displayed correctly. |  |

Result

CAGED report was executed successfully and branch data can be viewed correctly in Tesme file.

#### Colombia

##### DIAN Statutory Reporting

Use

Social insurance contributions (DIAN) can be sent from SAP SuccessFactors Employee Central Payroll to SAP S/4HANA Cloud Public Edition.

Use the DIAN (HCODIAN0) report to generate payroll data that is relevant for magnetic media according to the requirements of the Taxes and Customs Office of Colombia (DIAN).

###### DIAN

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The Accounts Payable Manager validates the following items:

- A business partner (vendor) of type Person with role Supplier has been created in SAP S/4HANA Cloud Public Edition.
- The supplier role has the company code for Colombia assigned.
- The company code has been assigned with all relevant accounting information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central Payroll as an Administrator - HR Info. | The SAP Easy Access menu page is displayed. |  |
| 2 | Access the Transaction | Execute transaction PC00_M38_DIAN. | The DIAN report page is displayed. |  |
| 3 | Selection Screen | In the Period section, choose Other Period. Choose Execute. |  |  |
| 4 | Display Log | View the result. |  |  |

Result

The corresponding data has been successfully transferred to SAP S/4HANA Cloud Public Edition.

###### View Social Insurance Contribution in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The social contibution has been successfully withheld in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | On the Home screen, choose RUN STATUTORY REPORT (Colombia DIAN). |  |  |
| 3 | Vendor Selection | On the Report Selection screen, choose Colombia DIAN – Format 1001 for report name and CO for Country/Region. Choose Go. | A list of statutory reports is displayed. |  |
| 4 | New Run | Choose the New Run button in the top-right corner. |  |  |
| 5 | Check the Generated Report | Choose the report to launch the details: On the Generated tab, select the report. On the Legal Reporting tab, view the payment document in XML format. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| JB1 - Exception-Based Core HR with SAP SuccessFactors Employee Central | Cost center replication from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central System. |

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
> Flagged while digesting this document, not verified: Portugal withholding tax return prerequisites refer to the company code for Spain, apparently copied from the Spain section

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c]]
- related-to :: [[03-financial-accounting-and-close/test-script-payroll-processing-with-sap-erp-hcm-payroll-3up-sap-s-4han]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NL_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 55,323 chars in the whole document
