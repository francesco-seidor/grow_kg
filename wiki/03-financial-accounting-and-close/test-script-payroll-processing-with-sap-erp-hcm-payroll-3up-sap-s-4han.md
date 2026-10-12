---
id: 03-financial-accounting-and-close/test-script-payroll-processing-with-sap-erp-hcm-payroll-3up-sap-s-4han
title: "Test Script: Payroll Processing with SAP ERP HCM Payroll (3UP) - SAP S/4HANA Cloud Public Edition (3UP_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3UP: cost center replication, payroll posting to FI from HCM Payroll, plus US/CA, ES, PT, BR, CO procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/payroll-posting-integration]
aliases: [3UP_S4CLD2608_BPD_EN_XX]
keywords: [Payroll Posting Integration (Employee Central Payroll and…, payroll posting, cost center replication, hcm payroll integration, test scripts, third-party remittance, withholding tax return, brazil branch data, colombia dian reporting, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UP_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-973
topic: 03-financial-accounting-and-close/payroll-posting-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Payroll Processing with SAP ERP HCM Payroll (3UP) - SAP S/4HANA Cloud Public Edition (3UP_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UP_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Payroll Posting Integration (Employee Central Payroll and HCM Payroll)** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Payroll Processing with SAP ERP HCM Payroll (3UP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232833977)

[2 Prerequisites 4](#_Toc232833978)

[2.1 Additional Manual Configuration 4](#_Toc232833979)

[2.2 System Access 4](#_Toc232833980)

[2.3 Roles 4](#_Toc232833981)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232833982)

[2.5 Business Conditions 6](#_Toc232833983)

[3 Overview Table 7](#_Toc232833984)

[4 Test Procedures 8](#_Toc232833985)

[4.1 Cost Center Replication 8](#_Toc232833986)

[4.1.1 Maintain Cost Center 8](#_Toc232833987)

[4.1.2 View Cost Center Data 10](#_Toc232833988)

[4.2 Payroll Posting 11](#_Toc232833989)

[4.2.1 Execute Live Posting Run 12](#_Toc232833990)

[4.2.2 Release and Post Documents 16](#_Toc232833991)

[4.2.3 View Transferred Documents in SAP S/4HANA 17](#_Toc232833992)

[4.3 Country/Region-Specific Procedures 18](#_Toc232833993)

[4.3.1 USA and Canada 18](#_Toc232833994)

[4.3.1.1 Third-Party Remittance 18](#_Toc232833995)

[4.3.1.2 Create Evaluation Run 18](#_Toc232833996)

[4.3.1.3 Create Posting Documents 21](#_Toc232833997)

[4.3.1.4 Post Documents to SAP S/4HANA Cloud Public Edition 22](#_Toc232833998)

[4.3.1.5 View Transferred Documents in SAP S/4HANA 23](#_Toc232833999)

[4.3.1.6 View Confirmation 24](#_Toc232834000)

[4.3.2 Spain 25](#_Toc232834001)

[4.3.2.1 Withholding Tax Return 25](#_Toc232834002)

[4.3.2.1.1 Withholding Tax Return 26](#_Toc232834003)

[4.3.2.1.2 View the Employment Tax Report 28](#_Toc232834004)

[4.3.3 Portugal 29](#_Toc232834005)

[4.3.3.1 Withholding Tax Return 29](#_Toc232834006)

[4.3.3.1.1 Withholding Tax Return 30](#_Toc232834007)

[4.3.3.1.2 View the Employment Tax Report 32](#_Toc232834008)

[4.3.4 Brazil 33](#_Toc232834009)

[4.3.4.1 Branch Data in Brazilian Reports 33](#_Toc232834010)

[4.3.4.1.1 Define Branch Data 34](#_Toc232834011)

[4.3.4.1.2 View Branch Data in CAGED Report 35](#_Toc232834012)

[4.3.5 Colombia 36](#_Toc232834013)

[4.3.5.1 DIAN Statutory Reporting 36](#_Toc232834014)

[4.3.5.1.1 DIAN 36](#_Toc232834015)

[4.3.5.1.2 Run Statutory Report in SAP S/4HANA Cloud Public Edition 37](#_Toc232834016)

[5 Appendix 39](#_Toc232834017)

[5.1 Process Integration 39](#_Toc232834018)

## Purpose

Overview

For customers considering integration between SAP ERP HCM Payroll and SAP S/4HANA Cloud Public Edition, this scope item gives you the security of direct connectivity to post your payroll results to your financial system in SAP S/4HANA Cloud Public Edition using web services, such as for cost center validation, accounting assignment checks, or journal entry display. In addition, it ensures the availability of all cost center data in the payroll system.

Based on the additional country/region-specific posting functionalities, ensure that the corresponding country/region is supported and has no limitations via SAP Note 2767439.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/8afea33e19a23f8cde70570d1abefd4e)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP ERP HCM Payroll |  |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

SAP S/4HANA Cloud Public Edition System

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT | Test user: userid, Password: password |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Test user: userid, Password: password |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER | Test user: userid, Password: password |

SAP ERP HCM Payroll System

| Business User | Name | Log On |
| --- | --- | --- |
| HR ADMINISTRATOR | All Admin rights | Test user: userid, Password: password |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master Data | Value | Details | Comments |
| --- | --- | --- | --- |
| Company code | 1010 | Company Code (DE) | Company Code for S/4HANA and SAP ERP HCM Payroll system. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

|  |
| --- |
| Note The following master data script reference is only relevant for Brazil. |

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| JD0 | Nota Fiscal Brazil |

### Business Conditions

|  |
| --- |
| Note Payroll is not a part of the setup for this scope item. It is a prerequisite to have a successful payroll run. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

- Cost Center Replication:

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Cost Center](#unique_9) [page ] 8 | Cost Accountant - Overhead | Manage Cost Centers - Old Version (F1443A) | A new cost center has been created and an existing one has been updated. |
| [View Cost Center Data](#unique_10) [page ] 10 | HR Administrator | KS03 | The data of the new cost center and the updated cost centers has been viewed. |

- Payroll Posting:

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Execute Live Posting Run](#unique_11) [page ] 12 | HR Administrator | PC00_M99_CIPE01 |  |
| [Release and Post Documents](#unique_12) [page ] 16 | HR Administrator | PCP0 |  |
| [View Transferred Documents in SAP S/4HANA](#unique_13) [page ] 17 | General Ledger Accountant | Manage Journal Entries (F0717A) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Cost Center Replication

In the following chapters, the procedures for executing the cost center replication from SAP S/4HANA to SAP ERP HCM Payroll system is described. At high level, changes to the existing cost center hierarchy are performed in SAP S/4HANA. The changes are then replicated automatically to SAP ERP HCM Payroll system, where they can be checked for correctness.

#### Maintain Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Cost Accountant - Overhead maintains one or several cost centers. It refers to:

- creating a new cost center in an already replicated cost center hierarchy
- updating an already replicated cost center, including name and description maintenance in different languages

|  |
| --- |
| Note In all these cases, a delta replication is triggered: the newly created cost center within the hierarchy or the adaptions performed on the existing cost center are transferred to SAP ERP HCM Payroll system. |

Prerequisite

The SAP S/4HANA system must support multiple languages.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP S/4HANA via the SAP Fiori launchpad as Cost Accountant - Overhead . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Cost Centers - Old Version (F1443A) app. | The Manage Cost Centers screen is displayed. |  |
| 3 | Enter Controlling Area | Select the  icon, and choose Settings.In the upcoming Settings dialog box, choose Default Values.In the CO Area field, choose A000 from the value help, and choose Save. |  |  |
| 4 | Search Existing Cost Centers | Back on the Manage Cost Center screen, enter criteria as appropriate, and choose Go. From the list of search results, select a cost center. |  |  |
| 5 | Add New Cost Center | Choose Add. | The Cost Center: New screen is displayed in addition to the Manage Cost Center screen. |  |
| 6 | Enter Basic Information of New Cost Center | In the New Cost Center section, make the following entries:Controlling Area: defaults to A000 (leave as is)Cost Center: cost center IDValid From: validity start dateValid To: defaults to system high date; accept the appropriate data otherwise leave as it is.In the Reference section, choose a controlling area, and a cost center as reference, if appropriate.Choose Continue. | You are progressed to the next screen for the cost center creation. |  |
| 7 | Enter Master Data of New Cost Center | In the General Data section, make the following entries:Cost Center: cost center nameCost Center Description: cost center descriptionPerson Responsible: cost center managerCost Center Category: Choose from value helpUser Responsible: optionally you can enter user ID of the person for the cost centerDepartment: optionally you can enter the name of the department to which the cost center belongsIn the Organizational Units section, make the following entries:Hierarchy Area: Choose from value helpCompany Code: Choose from value helpBusiness Area: Choose from value helpCurrency: defaulted to USD based on company code Choose; read-only fieldProfit Center: Choose from value help |  |  |
| 8 | Save New Cost Center | Choose Save. | A success message is generated by the system about saving the data. |  |
| 9 | Exit Cost Center Creation Screen | Close the Cost Center Creation screen. | You return to the Manage Cost Center page. |  |
| 10 | Search Cost Center to be Changed | On the Manage Cost Center screen, in the Standard section, enter search criteria using the value helps, and choose Go. | The cost centers matching your search criteria are listed in the Search Results section of the Manage Cost Center screen.If search criteria is not listed in the search results, you can choose the cost center from the existing controlling area. |  |
| 11 | Choose Cost Center to be Changed | In the Search Results list, mark the cost center you want to change, and choose Edit. | The screen Cost Center: cost center ID, cost center name is displayed in addition to the Manage Cost Center screen. |  |
| 12 | Update Cost Center Data | On the Cost Center: cost center ID, cost center name screen, modify for example the description, and choose Save. | A success message is generated by the system about saving the data. |  |
| 13 | Exit Cost Center Edit Screen | Close the Cost Center Creation screen. | You return to the Manage Cost Center page. |  |

#### View Cost Center Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the updated cost center data has been replicated correctly to the SAP ERP HCM Payroll system. You ensure that the new cost center has been replicated and the existing cost centers have been updated as expected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP ERP HCM Payroll system as HR Administrator. | The SAP Easy Access Menu screen is displayed. |  |
| 2 | Display Cost Center | To display the cost center data, choose one of the following navigation paths:On the SAP Easy Access Menu screen, choose Accounting > Controlling > Cost Center Accounting > Master Data > Cost Center > Individual Processing > Display .Alternatively, run the transaction KS03. | The Display Cost Center screen is displayed. |  |
| 3 | Enter Controlling Area | In the dialog box, enter the Controlling Area: A000. | The dialog box is closed, and the Display Cost Center screen is displayed again. |  |
| 4 | Search Cost Center | On the Display Cost Center screen, in the Cost Center field, enter the <Cost Center ID>, which was created earlier in the SAP S/4HANA system and which was replicated to the SAP ERP HCM Payroll system. |  |  |
| 5 | Check Updated Cost Center Data | Check if the changed data, for example the description, has been replicated correctly from the SAP S/4HANA system to the SAP ERP HCM Payroll system. |  |  |

### Payroll Posting

Purpose

The HR Administrator executes the payroll run for a selected payroll area for a certain pay period.

The system accesses a country/region-specific payroll program. It determines the current payroll period from the payroll control record and performs payroll using the values the Payroll Process Administrator entered in the payroll program.

Prerequisite

- The employee to be hired must be existing in the system and the corresponding master data must be maintained.

Procedure

- Maintain Payroll Control Record
- Run Payroll Simulation
- Release Payroll Area for productive run
- Execute Payroll Productive run with no errors
- Simulate the Posting Run
- Exit Payroll

#### Execute Live Posting Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The payroll has been completed and the HR Administrator begins the posting process to the financial module.

|  |
| --- |
| Note To run a production posting run, the payroll control record must be in status Exit Payroll. For simulation runs, the payroll control record can be left in status Released for Correction. |

The posting run to Financial Accounting (FI for short) creates a posting document that is transferred to FI, and the information is used to post a FI document. The information is reflective of the Expense and Liability posting for Payroll.

Posting to accounting includes the evaluation of the payroll results, the creation of summarized documents, and their posting in the accounting components.

|  |
| --- |
| Note The documents created in posting to accounting contain summarized information. However, if you’re provided with authorization, you can trace back which information (from the payroll results) the posting documents are based on for a specific personnel number. |

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
| Note A simulation of a posting run has to be executed before and after completing payroll. In this way, you can recognize posting-relevant errors in the payroll results early, and avoid errors when creating a productive posting run. The simulation and productive run are executed using the same transaction as mentioned here. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP ERP HCM Payroll system as HR Administrator. | The SAP Easy Access Menu screen is displayed. |  |
| 2 | Access Transaction Posting Run | Run the transaction PC00_M99_CIPE01. | The Posting to Accounting: Create Posting Run screen is displayed. |  |

Payroll Period:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 3 | Payroll Time Period (current) | For productive runs, choose the value Current Payroll Period from the dropdown list as the time period that is to be processed. | The current period is chosen as the default value. |  |
| 4 | Payroll Area | Caution Use one payroll area at a time. Don’t run payroll area ranges.The area for which posting to financial accounting is simulated.In the Payroll Area field, choose US (HR-US for monthly) from the dropdown list. |  |  |
| 5 | Payroll Time Period (other than the current) | Enter a desired time period for simulation purposes only. |  |  |

Criteria Selection:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 6 | Personnel Number | If you’re running the payroll for all employees in that payroll area, enter no data in the Personnel Number field. |  |  |
| 7 | Payroll Area | Caution Use one payroll area at a time. Don’t run payroll area ranges.In the Payroll Area field, choose US (HR-US for monthly) from the dropdown list. |  |  |

Run Attributes:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 8 | Off-cycle Payroll Run | If you're not processing an off-cycle payroll run, enter no data.If you're processing an off-cycle payroll run, enter the following data:If you process a regular payroll run, enter no data in the Payroll Type field.If you process a special payroll run, enter data in the Payroll Type field by choosing from the dropdown list.To differentiate between multiple special payroll runs from the same day, enter data in the second field.Enter the date of the special payroll run in the third field. |  |  |
| 9 | Type of Document Creation | To choose Live posting run as type of document to be created for postings, enter the value P. |  |  |
| 10 | Output Log | Note Ensure that you use this option only for one employee at a time. If you choose the Display Log option for all employees, it increases payroll runtime and produces the output log for everybody. The output log is for debugging purposes only, and wouldn’t make sense to be run for the entire payroll area.If you want to print an output log of the posting entry, select the Output Log checkbox. |  |  |
| 11 | Description of Posting Run | If necessary, enter a description to identify the FI document. |  |  |

Specify posting date:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 12 | Access Period Definition | The Acc. to Period Definition field is based on the payroll period calendar. Don't enter data. |  |  |
| 13 | Access Payment Date | Flag the Acc. to Payment Date field, which is equal to the posting date. |  |  |
| 14 | Enter Posting Date | Enter the posting date. |  |  |

Data for document creation:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 15 | Document Date | In the Document Date field, enter the posting date of the FI document.Note If the Document Date field is left empty, the current date is used as default. |  |  |
| 16 | Posting Variant | In the Posting Variant field, enter SAP as the standard variant, that determines the FI document type, and the default line item text. |  |  |
| 17 | Execute Posting Run | To execute the posting run, proceed with the following steps:To generate a productive posting document, choose Execute.To view the documents, on the Evaluation of Posting Item screen, choose Posting Run Overview.On the Display posting runs screen, the payroll postings are listed in a table, together with their status. To view the payroll postings, select the appropriate checkbox in the Payroll column, and choose Display Settlement Documents.On the Posting to Accounting: Document overview screen, the documents relevant to the chosen payroll posting are listed in a table, together with their status.To view the line items of these documents, select the appropriate checkbox in the Document column, and choose Display line items.Note Viewing the line items of documents makes sense when these documents have the status Incorrect. In this case, you can view the appropriate error messages, and solve the issues before performing a productive financial accounting posting run. | After the successful run, you’re redirected to the Posting to Accounting: Document Overview screen.The status of the created posting run is changed to Documents Created, and is saved with an ID. The status of the accompanying posting documents is changed to Created. An index of all processed payroll results is created. This index makes it possible to trace the creation of a document item although the documents have been summarized. |  |

#### Release and Post Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR Administrator processes the financial accounting posting run.

When checking a productive posting run and the accompanying posting documents, the HR Administrator ensures that all posting documents are technically correct with appropriate content. To post the posting documents, the HR Administrator has to release all posting documents before starting the posting run.

The posting run receives the status All documents released, and the HR Administrator can post the posting documents. All the posting documents belonging to a posting run are to be posted together in the Accounting component. Individual posting documents can’t be posted.

Prerequisite

A financial accounting posting run has been created with the status Documents created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP ERP HCM Payroll system as HR Administrator. | The SAP Easy Access Menu screen is displayed. |  |
| 2 | Edit Posting Runs | To display the cost center data, choose one of the following navigation paths:On the SAP Easy Access Menu screen, choose Human Resources > Payroll > International > Subsequent Activities > Per Payroll Period > Posting to Accounting > Edit Posting Runs .Alternatively, run the transaction PCP0. | The Edit Posting Runs screen is displayed. |  |
| 3 | Display Posting Run | On the Display posting Runs screen, choose the posting documents to be released, and then choose the Display Settlement Documents icon. |  |  |
| 4 | Release Documents | To release the documents, proceed with the following steps:To choose the documents to be released, on the Posting to Accounting: Document screen, select the appropriate checkbox in the Document column of the table. To release the document, choose Release document.In the dialog box, choose Yes to release the posting documents, or No to terminate the process.Choose Back.To identify the document in the SAP S/4HANA system, note down the document type and the posting run number. |  |  |
| 5 | Post Documents | To post the documents, proceed with the following steps:The posting run status All documents released is displayed. Choose the posting run, and in the SAP menu, choose Edit > Post documents .In the dialog box, choose Immediately or Create job to start the posting to Finance, or Cancel to cancel the reversal. | The posting documents were posted in the components affected in accounting. The posting run has the status Documents posted. |  |

#### View Transferred Documents in SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP S/4HANA via the SAP Fiori launchpad as General Ledger Accountant. |  |  |
| 2 | Access App | Open the Manage Journal Entries (F0717A) app. | The Manage Journal Entries screen is displayed. |  |
| 3 | Search for Transferred Documents | On the Manage Journal Entries screen, set the relevant search filters, and choose Go. | A search result list is displayed. |  |
| 3 | Select Transferred Documents | From the search result list, choose  , to select the desired document and to show the document details on the Journal Entry (xxx) - Entry View screen.Note In the Header Text column, a number is displayed. This number is a combination of the Document Type, and the Run Number from the posting document, which was posted from the SAP ERP HCM Payroll system, for example, PP0000000001. | On the Journal Entry (xxx) - Entry View screen, a general ledger account document, and a vendor document is displayed for the transferred posting document. |  |

### Country/Region-Specific Procedures

This chapter is only relevant, if you have any country/region-specific functionality, which requires additional procedures in addition to international payroll posting. You can find the supported countries in the following sections with additional functionalities.

#### USA and Canada

##### Third-Party Remittance

Purpose

The HR Administrator executes the payroll run for a selected payroll area for a certain pay period. In this test case, the accumulated federal withholding taxes, which were deduced from employees’ payment during payroll execution, are sent to the tax authority.

##### Create Evaluation Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The HR Administrator validates the following items:

- Vendors are created in the SAP ERP HCM Payroll system, and are synchronized with the SAP S/4HANA system.
- HR payees are configured according to the payment methods Bank Transfer (T) and Check (C).
- The infotypes (0001, 0002, 0006, 0007, 0008, 0009, 0207, 0208, 0209, 0210) are maintained for all employees to be included in the payroll run.
- The payroll has been executed successfully without any errors, and is in Exit state.
- The result table has an entry for withholding tax.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP ERP HCM Payroll system as HR Administrator. |  |  |
| 2 | Access Transaction | To display the cost center data, choose one of the following navigation paths:On the SAP Easy Access Menu screen, choose Human Resources > Payroll > Americas > USA > Subsequent Activities > Per Payroll Period > Evaluation > Third-Party Remittance > Evaluate Remittance (New) .Alternatively, run the transaction PC00_M99_URME. |  |  |

Payroll Time Period:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 3 | Payroll Time Period (current) | For productive runs, choose the value Current Payroll Period from the dropdown list as the time period that is to be processed. | The current period is chosen as the default value. |  |
| 4 | Payroll Area | Caution Use one payroll area at a time. Don’t run payroll area ranges.The area for which posting to financial accounting is simulated.In the Payroll Area field, choose US (HR-US for monthly) from the dropdown list. |  |  |
| 5 | Payroll Time Period (other than the current) | Enter a desired time period for simulation purposes only. |  |  |

Selection Criteria:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 6 | Personnel Number | If you’re running the payroll for all employees in that payroll area, enter no data in the Personnel Number field. |  |  |
| 7 | Payroll Area | Caution Use one payroll area at a time. Don’t run payroll area ranges.In the Payroll Area field, choose US (HR-US for monthly) from the dropdown list. |  |  |

HR Payee Type to be posted:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 8 | HR Payee Type | In the Payee Type field, select a value from the value help. |  |  |

Control Data:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 9 | ALV Control | Select a view according to your requirements.Default is the Grid view. |  |  |

Level of Details:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 10 | Make a Selection | Select the checkboxes for which the information is required. |  |  |

Detail for List Output:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 11 | Include Period Information | If the period information is required, select the Period Information checkbox. |  |  |

Processing Option:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 12 | Production Mode | Choose the Production Mode. |  |  |

Display Log:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 13 | Display Log | Select the Display Log checkbox. |  |  |
| 14 | Execute | Choose Execute. | For the evaluation, run the Successful status is displayed. |  |

##### Create Posting Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The evaluation run was successful, and the symbolic accounts are synchronized with the G/L accounts in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP ERP HCM Payroll system as HR Administrator. |  |  |
| 2 | Access Transaction | To display the cost center data, choose one of the following navigation paths:On the SAP Easy Access Menu screen, choose Human Resources > Payroll > Americas > USA > Subsequent Activities > Per Payroll Period > Evaluation > Third-Party Remittance > Create Posting Run .Alternatively, run the transaction PC00_M99_URMP. |  |  |
| 3 | Posting Data Selection | Enter the following data:Company Code: (for example) 1710Due Date: <current date> |  |  |
| 4 | Transfer Parameters | Enter the following data:Text on Posting Run: (for example) 3PR PostingPosting Date: <current date>Posting Variant: SAPDocument Date: <current date> |  |  |
| 5 | Processing Option | Choose Production. |  |  |
| 6 | Execute | Choose Execute. |  |  |

Result

The posting run is in the Successful status, and a posting document of type TP has been created in the system. To check the document, run the transaction PCP0. After that, search for the newly created entry with your user and the posting document type TP. Deselect the Simulation checkbox. Once you open the document, you see that several documents have been created. Open each document, and make sure that one of them is of document type G/L Account Document and others are Vendor Documents.

##### Post Documents to SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The evaluation run was successful, and the posting documents were created successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP ERP HCM Payroll system as HR Administrator. |  |  |
| 2 | Access Transaction | To display the cost center data, choose one of the following navigation paths:On the SAP Easy Access Menu screen, choose Human Resources > Payroll > Americas > USA > Subsequent Activities > Per Payroll Period > Evaluation > Third-Party Remittance > Process Posting Run.Alternatively, run the transaction PCP0. |  |  |
| 3 | Search for Entries | On the Display Posting Run screen, in the Posting Third-Party Remittance section, look for the posting document, which was created in section [Create Posting Documents](#unique_20) [page ] 21. |  |  |
| 4 | Release Documents | Open the entry with the posting document, and select all of the documents. In the menu bar, choose Release Documents.Go back to the Display Posting Run screen.The status of the Third-Party Remittance has changed from Documents Created to All Documents Released. |  |  |
| 5 | Post the Documents | Select the released document, and choose Post Documents. | On the next screen, in the Post Documents section, the system message Documents Posted Successfully is displayed. |  |

Result

You've posted your documents to SAP S/4HANA Cloud Public Edition. Note down the reference number of all the posted documents. The reference number looks, for example, like this: HR0000000001 or HRGRNX0000000001.

##### View Transferred Documents in SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP S/4HANA via the SAP Fiori launchpad as General Ledger Accountant. |  |  |
| 2 | Access App | Open the Manage Journal Entries (F0717A) app. | The Manage Journal Entries screen is displayed. |  |
| 3 | Search for Transferred Documents | On the Manage Journal Entries screen, set the relevant search filters, and choose Go. | A search result list is displayed. |  |
| 3 | Select Transferred Documents | From the search result list, choose  , to select the desired document and to show the document details on the Journal Entry (xxx) - Entry View screen.Note In the Header Text column, a number is displayed. This number is a combination of the Document Type, and the Run Number from the posting document, which was posted from the SAP ERP HCM Payroll system, for example, PP0000000001. | On the Journal Entry (xxx) - Entry View screen, a general ledger account document, and a vendor document is displayed for the transferred posting document. |  |

##### View Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

In the SAP S/4HANA system, the posted documents are successfully paid out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP ERP HCM Payroll system as HR Administrator. |  |  |
| 2 | Access Transaction | Run the transaction SE38. |  |  |
| 3 | Search for Entries | On the Program Name screen, enter the report name RPURMR00, and start the search. |  |  |
| 4 | Selection Screen | On the selection screen, enter the Company Code, and the HR Document Reference Number, which you've noted down before. |  |  |
| 5 | Remittance Overview | In the Acknowledgment Number column, check if it contains any numbered value. If it has any random number value, then the documents have successfully been paid out. |  |  |

Result

The documents are posted successfully to the SAP S/4HANA system, and the acknowledgment has been received.

#### Spain

The HR ADMINISTRATOR executes the payroll run for a selected payroll area for a certain pay period. In this test case the collected Federal Withholding taxes from employees’ payment during payroll execution will be send to the Tax Authority.

##### Withholding Tax Return

Use

The Employment Tax (IRPF) reports for the Tax Office (forms 190) can be paid out from the SAP S/4HANA Cloud Public Edition system and can be seen in SAP ERP HCM System. HR ADMINISTRATOR executes the payroll run for a selected payroll area for a certain pay period. In this test case, the collected Federal Withholding taxes from employees’ payment during payroll execution will be sent to the Tax Authority.

###### Withholding Tax Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The Accounts Payable Manager validates the following items:

- A business partner (vendor) of the type person has been created with the supplier role in the SAP S/4HANA system.
- The supplier role has the required company code assigned for Spain.
- The company code has been assigned with all relevant accounting information along with withhold tax types.
- For the withholding tax type, the Subject to Withholding Tax checkbox is selected.
- An invoice with the previous business partner has been created with tax amount and has been posted.
- The invoice has been paid out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as an Accounts Payable Manager for Spain. |  |  |
| 2 | Access App | Open the Prepare Withholding Tax Return - Spain (S_PL0_09000447) app. | The Withholding Tax Return screen is displayed. |  |
| 3 | Vendor Selection | On the Vendor Selection screen, select a Vendor Account, and a Company Code.Note Use the same business partner (vendor), which was used in the prerequisites. |  |  |
| 4 | Country Variant | In the Country Variant field, enter ES.The area for which posting to financial accounting is simulated. |  |  |
| 5 | Output Control | Select the Fill table for DME checkbox. |  |  |
| 6 | Execute | Choose Execute. |  |  |

Selection Criteria:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 7 | Personnel Number | Personnel numbers of the employees to be processed.If you’re running the payroll for all employees in that payroll area, enter no data in the Personnel Number field. |  |  |
| 8 | Payroll area | Caution Use one payroll area at a time. Don’t run payroll area ranges.Enter the same value as In the Payroll area field, choose US (HR-US for monthly) from the dropdown list. |  |  |

HR Payee Type to be posted:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 9 | HR Payee Type | In the Payee Type field, select a value from the value help. |  |  |

Control Data:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 10 | ALV Control | Select a view according to your requirements.Default is the Grid view. |  |  |

Level of Details:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 11 | Make a Selection | Select the checkboxes for which the information is required. |  |  |

Detail for List Output:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 12 | Include Period Information | If the period information is required, select the Period Information checkbox. |  |  |

Processing Option:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 13 | Production Mode | Choose the Production Mode. |  |  |

Display Log:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 14 | Display Log | Select the Display Log checkbox. |  |  |
| 15 | Execute | Choose Execute. | For the evaluation, run the Successful status is displayed. |  |

Result

The withholding tax return has been successfully executed and the information has been transferred back to the SAP ERP HCM Payroll system. The evaluation run is in the Successful status.

###### View the Employment Tax Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The withholding tax return has been successfully executed, and the transferred documents from the SAP ERP HCM Payroll system to the SAP S/4HANA system are successfully paid out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP ERP HCM Payroll system as HR Administrator. |  |  |
| 2 | Access Transaction | Run the transaction SE38. | The Employment Tax (IRPF) report screen is displayed. |  |
| 3 | Search for Entries | In the Program Name screen, enter the report name RPC190E0, and choose Execute. |  |  |
| 4 | Selection Screen | In the Period section, choose Other Period.On the Selection of Results screen, enter the required data.Select the Accounting Data checkbox. |  |  |
| 5 | Execute | Choose Execute. |  |  |
| 6 | Display log | Review the display log. |  |  |

Result

The Vendor Name, and the amount for which the withholding tax has been paid out in the SAP S/4HANA system are displayed.

#### Portugal

The HR ADMINISTRATOR executes the payroll run for a selected payroll area for a certain pay period. In this test case the collected Federal Withholding taxes from employees’ payment during payroll execution will be send to the Tax Authority.

##### Withholding Tax Return

Use

The Employment Tax (IRPF) reports for the Tax Office (forms 190) can be paid out from the SAP S/4HANA Cloud Public Edition system and can be seen in SAP ERP HCM System. HR ADMINISTRA-TOR executes the payroll run for a selected payroll area for a certain pay period. In this test case the collected Federal Withholding taxes from employees’ payment during payroll execution will be send to the Tax Authority.

###### Withholding Tax Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The Accounts Payable Manager validates the following items:

- A business partner (vendor) of the type person has been created with the supplier role in the SAP S/4HANA system.
- The supplier role has the required company code assigned for Spain.
- The company code has been assigned with all relevant accounting information along with withhold tax types.
- For the withholding tax type, the Subject to Withholding Tax checkbox is selected.
- An invoice with the previous business partner has been created with tax amount and has been posted.
- The invoice has been paid out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as an Accounts Payable Manager for Spain. |  |  |
| 2 | Access App | Open the Prepare Withholding Tax Return - Spain (S_PL0_09000447) app. | The Withholding Tax Return screen is displayed. |  |
| 3 | Vendor Selection | On the Vendor Selection screen, select a Vendor Account, and a Company Code.Note Use the same business partner (vendor), which was used in the prerequisites. |  |  |
| 4 | Country Variant | In the Country Variant field, enter PT.The area for which posting to financial accounting is simulated. |  |  |
| 5 | Output Control | Select the Fill table for DME checkbox. |  |  |
| 6 | Execute | Choose Execute. |  |  |

Selection Criteria:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 7 | Personnel Number | Personnel numbers of the employees to be processed.If you’re running the payroll for all employees in that payroll area, enter no data in the Personnel Number field. |  |  |
| 8 | Payroll area | Caution Use one payroll area at a time. Don’t run payroll area ranges.Enter the same value as In the Payroll area field, choose US (HR-US for monthly) from the dropdown list. |  |  |

HR Payee Type to be posted:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 9 | HR Payee Type | In the Payee Type field, select a value from the value help. |  |  |

Control Data:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 10 | ALV Control | Select a view according to your requirements.Default is the Grid view. |  |  |

Level of Details:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 11 | Make a Selection | Select the checkboxes for which the information is required. |  |  |

Detail for List Output:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 12 | Include Period Information | If the period information is required, select the Period Information checkbox. |  |  |

Processing Option:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 13 | Production Mode | Choose the Production Mode. |  |  |

Display Log:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 14 | Display Log | Select the Display Log checkbox. |  |  |
| 15 | Execute | Choose Execute. | For the evaluation, run the Successful status is displayed. |  |

Result

The withholding tax return has been successfully executed and the information has been transferred back to the SAP ERP HCM Payroll system. The evaluation run is in the Successful status.

###### View the Employment Tax Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The withholding tax return has been successfully executed, and the transferred documents from the SAP ERP HCM Payroll system to the SAP S/4HANA system are successfully paid out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP ERP HCM Payroll system as HR Administrator. |  |  |
| 2 | Access Transaction | Run the transaction SE38. | The Employment Tax (IRPF) report screen is displayed. |  |
| 3 | Search for Entries | In the Program Name screen, enter the report name RPC190E0, and choose Execute. |  |  |
| 4 | Selection Screen | In the Period section, choose Other Period.On the Selection of Results screen, enter the required data.Select the Accounting Data checkbox. |  |  |
| 5 | Execute | Choose Execute. |  |  |
| 6 | Display log | Review the display log. |  |  |

Result

The Vendor Name, and the amount for which the withholding tax has been paid out in the SAP S/4HANA system are displayed.

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

###### Define Branch Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The Accounts Payable Manager validates the following items:

- A business place for a Brazilian Tax Entity (CNPJ) has been created in the SAP S/4HANA system.
- The business place has the company code for Brazil assigned.
- The company code has been assigned with all relevant accounting information.

Procedure

For more information on how to define BR-specific fields for a business place, and on how to create master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| JD0 | Nota Fiscal Brazil |

Result

The branch data is defined and maintained in the SAP S/4HANA system.

###### View Branch Data in CAGED Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The following items need to be validated:

- The branch data is present in the SAP S/4HANA system.
- An employee has been hired in that branch in a Brazilian company.
- An employee has all the required infotypes (0000, 0002, 0001, 0006, 0007, 0008, 0009, 0021, 0057, 0016).
- An employee has the info type 0016 with complementary information compared to info type 0398 (legal information).
- The payroll for that employee has been executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP ERP HCM Payroll system as HR Administrator. |  |  |
| 2 | Access Transaction | Run the transaction SE38. |  |  |
| 3 | Run Report | On the Program Name screen, enter the report name HBRCAGED, and choose Execute. | The CAGED/GREU report is displayed. |  |
| 4 | Select Result | On the Further Selections screen, add the Personnel Number as a filter.On the Selection of Results screen, enter the Personnel Number, and the Company Code.In the Period section, enter the period in which the payroll was executed for that employee.Choose Execute. |  |  |
| 5 | Display TemSe File | Review the result. | The branch data is displayed in the TemSe File. |  |

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

###### Run Statutory Report in SAP S/4HANA Cloud Public Edition

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
| 2 | Access the SAP Fiori App | On the Home screen, choose Run Statutory Reports (Colombia DIAN). |  |  |
| 3 | Vendor Selection | On the Report Selection screen, for Report Name, select the Colombia DIAN - Format 1001 and for Country/Region, select CO.Chose Go. |  |  |
| 4 | Check Generated Report | Choose the report to launch the details. On the Generated tab, select the report. Next, on the Legal Reporting tab, view the payment document as XML format. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

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
> Flagged while digesting this document, not verified: Portugal section reuses Spain content (prerequisites reference Spain company code, Spain app and US payroll area), so it may not reflect Portugal-specific requirements.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/payroll-processing-with-sap-successfactors-employee-central-payroll-1n]]
- related-to :: [[01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UP_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 60,502 chars in the whole document
