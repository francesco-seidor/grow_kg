---
id: 03-financial-accounting-and-close/test-script-cash-application-integration-1mv-740
title: "Test Script: Cash Application Integration (1MV) (1MV_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1MV Cash Application Integration: ML invoice matching, lockbox reprocessing, payment advice extraction."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/cash-application]
aliases: [1MV_S4CLD2608_BPD_EN_XX]
keywords: [Cash Application with Machine Learning, cash application, machine learning model training, bank statement reprocessing, lockbox processing, payment advice extraction, intelligent scenario management, business roles, communication scenarios, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MV_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-740
topic: 03-financial-accounting-and-close/cash-application
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Cash Application Integration (1MV) (1MV_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MV_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Cash Application with Machine Learning** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Cash Application Integration (1MV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232848236)

[2 Prerequisites 3](#_Toc232848237)

[2.1 Model Availability 3](#_Toc232848238)

[2.1.1 Historical Data 3](#_Toc232848239)

[2.1.2 Training Data Extraction 3](#_Toc232848240)

[2.1.3 Machine Learning Training Progress, Benchmark Report, and Model Activation 3](#_Toc232848241)

[2.2 Additional Manual Configuration 4](#_Toc232848242)

[2.3 System Access 4](#_Toc232848243)

[2.4 Roles 4](#_Toc232848244)

[2.5 Business Conditions 4](#_Toc232848245)

[3 Overview Table 5](#_Toc232848246)

[4 Test Procedures 6](#_Toc232848247)

[4.1 Scheduling Accounts Receivable Jobs - Automatic Bank Statement Reprocessing – Receivables Clearing 6](#_Toc232848248)

[4.2 Scheduling Accounts Receivable Jobs – Automatic Lockbox Processing (Optional) 8](#_Toc232848249)

[4.3 Extracting Payment Advice Information 11](#_Toc232848250)

[5 Appendix 13](#_Toc232848251)

[5.1 Machine Learning Model - Prerequisite Check 13](#_Toc232848252)

[5.2 Machine Learning Model - Training 14](#_Toc232848253)

## Purpose

Overview

The SAP Cash Application uses the past data in your system to propose invoice matching prediction results. It helps lower the manual effort in the time-consuming clearing process of open items.

With this scope item, remittance advice can also be created automatically by the system based on the advice file sent from your customers or payees.

To use this solution's functions, you must purchase the extra license on SAP BTP.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Model Availability

To test the scope item, you must activate the respective SAP Cash Application country model in SAP BTP.

The following steps are required to generate SAP Cash Application country model.

#### Historical Data

The SAP Cash Application is a machine-learning-based solution. The algorithm is derived solely from historical cleared bank statement items against the invoices in the system. The minimum historical data required for Cash Application is 10,000 cleared bank statement items.

For technical details of the data requirement, see the [SAP Cash Application Prerequisites](https://help.sap.com/viewer/60e4f6eb9b6a427db1963afb7e9791b5/LATEST/en-US/3adb6b8be55646d68d0939fcfa851303.html) on the SAP Help Portal.

#### Training Data Extraction

Upon confirmation that the historical data met the prerequisite volume and clearing processes, such data need to be sent to Cash Application as training data.

This is can be done by scheduling the Cash Application: Training job in Schedule Account Receivable Jobs, by selecting Incoming Payment, and specifying the Description, Company Code, Posting Date, and Posting Rule parameters according the the scope.

#### Machine Learning Training Progress, Benchmark Report, and Model Activation

Upon completion of the training job in SAP S/4HANA, the machine learning training status can be monitored via the Model Manager UI. Once the overall training progress is completed successfully, you can view the benchmark result. The country model can then be activated.

For more information on the Model Manager UI Onboarding process and activities, see the [Model Manager for SAP Cash Application](https://help.sap.com/viewer/60e4f6eb9b6a427db1963afb7e9791b5/Latest/en-US/73fd86f7258b46bf84ef47f415af18fa.html) documentation on SAP Help Portal.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/7eb279798c03d09ccf07c9f8c297a4fc)

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
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Must be in scope as prerequisite. |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Scheduling Accounts Receivable Jobs - Automatic Bank Statement Reprocessing – Receivables Clearing](#unique_12) [page ] 6 | Accounts Receivable Accountant | Schedule Accounts Receivable Jobs (F2366) |  |
| [Scheduling Accounts Receivable Jobs – Automatic Lockbox Processing (Optional)](#unique_13) [page ] 8 | Cash Management Specialist (local)Note This step is only relevant for the US and Canada. | Schedule Lockbox Jobs (F3821); Reprocess Incoming Checks - From Lockbox (FEBA_LOCKBOX) |  |
| [Extracting Payment Advice Information](#unique_14) [page ] 11 | Accounts Receivable Accountant | Manage Payment Advices - Deprecated (F2550) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

If you activate and use communication scenario SAP_COM_0650 (SAP Cash Application Integration), run the steps in this Test Procedure section. If you activate and use communication scenario SAP_COM_0A20 (SAP Cash Application for ISLM Integration), run the steps in the [Appendix](#unique_16) [page ] 13 section.

For more information on the communication scenarios, see the [Additional Manual Configuration](#unique_7) [page ] 4 topic.

### Scheduling Accounts Receivable Jobs - Automatic Bank Statement Reprocessing – Receivables Clearing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This background job automatically matches invoices to bank statements, thus supporting the accounts receivable accountant in clearing the items.

Prerequisites

Open bank statements exist in the system. If not, see the Bank Integration with File Interface (1EG) scope item to upload bank statement files, or the Basic Cash Operations (BFB) scope item for manual bank statement creation.

Open invoices are sent to the Cash Application using the Cash Application: Open Item Upload (SAP_COM_0650) job template.

|  |
| --- |
| Note For the new cash app architecture, a separate template is not needed for sending open invoices. |

The model for the Bank Statement Company Code's country is available and activated.

To maintain the reprocessing rules, see the Accounts Receivable (J59) test script, section Manage Bank Statement Reprocessing Rules (Optional).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accounts Receivable Jobs (F2366). |  |  |
| 3 | Create a New Job | Choose Create. | The New Jobs view is displayed. |  |
| 4 | Enter Job Data | Make the following entries and choose Schedule:General Information section:Job Template: Cash Application: Automatic Bank Statement Reprocessing (SAP_COM_0650)Scheduling Options section:Start Immediately: SelectedParameter section:Statement Number: <the bank statement number to be processed>Company Code: <your company code>, for example, 1010Account Type for Clearing: D - CustomersAutomatic Clearing: <see note>Note If you select this checkbox, the matched items are cleared automatically. If you don't select the checkbox, the matched items are cleared manually per the following steps.Open Items Proposal: <scheduled jobs to receive a list of machine learning proposals for matching receivables to existing bank statement items>Account Proposal: <scheduled jobs to receive a list of Machine Learning proposals for matching accounts to existing bank statement items>Note A template with the description Cash Application: Automatic Bank Statement Reprocessing specifies the new cash app architecture template. | The background job is scheduled and the page skips back to the Application Jobs view. |  |
| 5 | Check the Logs | Monitor the job status. The status is Finished once the job has been processed.Access the log of proposals for bank statement items sent to the SAP Cash Application.Save the bank statement number and company code to process the subsequent steps.Note If you are using the cash app template mentioned in the note in step 4 above, the log is not available via the application job app. Instead, use the Intelligent Scenario Management (F4470) app for more information. | Make a note of the bank statement numbers and company code: __________ __________ |  |
| 6 | Check the explanation (Optional) | Choose Details and choose the Log tab. | You can see the machine learning logs, such as match field and match range, in Log Details. |  |

### Scheduling Accounts Receivable Jobs – Automatic Lockbox Processing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With automatic lockbox processing, you can collect and process incoming payments.

|  |
| --- |
| Note This step is only relevant for the US and Canada. |

Currently, Automatic Lockbox Reprocessing can only be used for Unprocessed or Posted on acct business scenarios.

|  |
| --- |
| Restriction Processing for the Part. applied business scenario is currently not available. |

Prerequisites

Unprocessed or posted on account Lockbox files exist in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist (for US or CA (as appropriate)). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Lockbox Jobs (F3821). | The Application Jobs view displays. |  |
| 3 | Create a New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Details | Make the following entries and choose Step 2:Job Template: Cash Application: Automatic Lockbox ReprocessingJob Name: Cash Application: Automatic Lockbox Reprocessing |  |  |
| 5 | Enter Details | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Details | Make the following entries and choose Schedule:Lockbox Batch Selection:Deposit Date: Date when the Lockbox file failed to process, for example, <Current date>Lockbox: (Optional) Leave the field blank when you don’t know the number.Company Code: <company code>Batch Number: (Optional) <Lockbox batch number to be reprocessed> or leave the field blank when you don’t know the number.Lockbox Batch Posting:Automatic Posting/Clearing: Leave blank.Caution Do NOT select because selecting allows the system to automatically post and clear the A/R invoices without giving you any opportunity to review the machine learning proposal. | The background job is scheduled and returns to the Application Jobs view. When the job is processed, the status changes to Finished. You may need to refresh the view to see the status update. |  |
| 7 | Check the Logs | Access log of proposals for bank statement items sent to the SAP Cash Application. |  |  |
| 8 | Log off | Log off of the SAP Fiori launchpad | You are logged out of the system. |  |
| 9 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist (for US or CA (as appropriate)). |  |  |
| 10 | Access the SAP Fiori App | Open Reprocess Incoming Checks - From Lockbox (FEBA_LOCKBOX). | The Selection of Checks and Lockboxes dialog box displays. |  |
| 11 | HDR Data | Make the following entries:Lockbox: For example, 1234567Date: <Enter the date in the Lockbox File>and choose Execute. | The Lockbox: process checks view displays. |  |
| 12 | Post Clear Invoice (Option 1) | Note There are three options to post and clear an invoice. Choose one of the options that best serves your posting situation.OPTION 1: Select the item that failed to Post.Under Items > Items to be cleared section, machine learning (ML) proposes the document number that is closest to the document that failed.Choose Log to view the confidence level of the proposal.If you agree with the proposal, select Post and invoice proposed by ML is cleared and the field 1 Document will be updated with the clearing document. If ML proposal appears to be incorrect, then go to option 2 for manual selection. | The Lockbox: process checks view displays.The Document XXXXXXXXXX was posted in company code YYYY notification displays. |  |
| 13 | Post Clear Invoice (Option 2) | Remember There are three options to post and clear an invoice. Choose the option that best serves your requirements.OPTION 2: On the Payt Adv. Change Payment Advice field, double-click the document number.When the document number is correct.Double-clicking the document number opens an overview that displays the item details of the Payment Advice. When there is only one document number available and that is the correct document, select the line and choose Save.When the document number is not correctIf the document number proposed is not correct, select Choose and the Payment Advice: Line Item Data view appears.Change the document number to the invoice to be cleared and choose Save.When a new document number is requiredIf the none of the documents proposed in the Payment Advice Items section are to be cleared, select New Item and enter the document number and choose Save.The Lockbox: Process Checks view displays.Select the document number from the Items to be Cleared section and choose Post.The Post with clearing process open items view displays.Select any invoices not required to be cleared and choose Deactivate Items.Note The amount in the Not Assigned field should equal zero, to post the clearing document.and then choose Post. | The Lockbox: process checks view displays.The Document XXXXXXXXXX was posted in company code YYYY notification displays. |  |
| 14 | Post Clear Invoice (Option 3) | Remember There are three options to post and clear an invoice. Choose the option that best serves your requirements.OPTION 3: Use menu to post items.Go to More > Edit > Posting Mode > In Foreground .Select Post.Post with Clearing: Header Data displays.Select Choose open itemsA Post with Clearing Add G/L account item dialog box appears with OK Code: /07,choose OKA new Post with Clearing Add G/L account item dialog box displays with OK Code: /00, choose OKAnother Post with Clearing Add G/L account item dialog box displays with OK Code: /06, choose OKA final Post with Clearing Add G/L account item dialog box displays with OK Code: /11, choose OK | The Lockbox: process checks view displays.The Document XXXXXXXXXX was posted in company code YYYY notification displays. |  |
| 15 | Display Item Details | Expand LOCKBOXDES LOCKBOXORI and double-click document number with the green status. | The document field displays the document number from the previous step.The red status becomes a green status. |  |

### Extracting Payment Advice Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This function lets you automatically extract payment advice information for further processing.

Prerequisites

Open bank statements exist in the system. If not, see the Advanced Cash Operations (J78) scope item to enter bank statements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Payment Advices - Deprecated (F2550) . |  |  |
| 3 | Upload the Payment Advice File | Choose Import. |  |  |
| 4 | Upload the Payment Advice File | Make the following entries:Company Code: <company code>To upload the payment advice file (for example, advice1.pdf) from your local environment, choose +. Locate and upload the file.Choose Process.Choose OK. | The file that contains payment advice details is uploaded for automatic processing. |  |
| 5 | Check the Processing Result | Choose the Confirmation Pending (xx) tab. | The tab displays the new payment advice of type 12. if you open it, you find the relevant information extracted from the document with machine learning. |  |
| 6 | Confirm and Proceed | Choose Confirm and Next. | The information is stored for further processing. |  |

Succeeding Process

For information on processing payment advices, see the Accounts Receivable (J59) scope item.

## Appendix

Purpose

The steps in this section are used if you activated the communication scenario SAP_COM_0A20 (SAP Cash Application for ISLM Integration). If you use communication scenario SAP_COM_0650 (SAP Cash Application Integration), execute the steps in the Test Procedures section instead.

For more information on the communication scenarios, see the [Additional Manual Configuration](#unique_7) [page ] 4 topic.

### Machine Learning Model - Prerequisite Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the prerequisite checks for the machine learning model training.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Analytics Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Intelligent Scenario Management (F4470). |  |  |
| 3 | Enter Details | Make the following entries and press Enter:Intelligent Scenario: FIN_CASHAPP_INTG_GLM | The list of scenarios is updated. |  |
| 4 | Select Scenario | Select the radio button for the scenario and choose > (Details). |  |  |
| 5 | Prerequisite Checks | Choose the Prerequisite Checks button. | The Prerequisite Check Run for FIN_CASHAPP_INTG_GLM view is displayed. |  |
| 6 | General Information | Enter a description and choose Step 2. |  |  |
| 7 | Checks | Choose Step 3. |  |  |
| 8 | Parameters | Make the following entries and choose Review:No. of cleared Bank Statement Items: 10000 |  |  |
| 9 | Start Run | Review your entries. When ready, choose Start Prerequisite Check Run. | The run is scheduled. Wait until the run is finished. You do not need to refresh the screen. Once the run is complete, the status automatically changes to Successful. |  |
| 10 | Repeat Steps | Repeat these steps for Intelligent Scenario: FIN_CASHAPP_INTG_RAI. |  |  |

### Machine Learning Model - Training

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the machine learning model training.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Analytics Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Intelligent Scenario Management (F4470). |  |  |
| 3 | Enter Details | Make the following entries and press Enter:Intelligent Scenario: FIN_CASHAPP_INTG_GLM | The list of scenarios is updated. |  |
| 4 | Select Scenario | Select the radio button for the scenario and choose > (Details). |  |  |
| 5 | Select Scenario | Select the radio button for the scenario and choose Train. | The Train dialog box is displayed. |  |
| 6 | Enter Details | In the Version field, select the latest version.In the Package Size field, enter 1000. |  |  |
| 7 | Enter Details | In the Training Filters pane, choose + Add Filter. |  |  |
| 8 | Enter Details | Make the following entries:Name: COMPANYCODELow: 1010 |  |  |
| 9 | Enter Details | In the Training Details pane, make the following entries:Training Description: <description> |  |  |
| 10 | Train | Choose Train. | The training is scheduled. Wait until the run is finished. You do not need to refresh the screen. Once the run is complete, the status automatically changes to Completed. |  |
| 11 | Repeat Steps | Repeat these steps for Intelligent Scenario: FIN_CASHAPP_INTG_RAI. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/steps-to-create-bai2-format-file-207]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MV_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 26,385 chars in the whole document
