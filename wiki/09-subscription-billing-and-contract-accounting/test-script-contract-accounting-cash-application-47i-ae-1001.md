---
id: 09-subscription-billing-and-contract-accounting/test-script-contract-accounting-cash-application-47i-ae-1001
title: Test Script - Contract Accounting – Cash Application (47I_AE) (47I_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 test script for scope item 47I: ML-based cash application in FI-CA, transferring and processing clarification cases and posting ML proposals."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-cash-application]
aliases: [47I_S4CLD2608_BPD_EN_AE]
keywords: [Contract Accounting Cash Application, cash application, machine learning clearing, clarification cases, inference jobs, payment lots, confidence rating, contract accounting, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/47I_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1001
topic: 09-subscription-billing-and-contract-accounting/fi-ca-cash-application
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - Contract Accounting – Cash Application (47I_AE) (47I_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/47I_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contract Accounting Cash Application** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Cash Application (47I_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854524)

[2 Prerequisites 3](#_Toc232854525)

[2.1 Additional Manual Configuration 3](#_Toc232854526)

[2.2 System Access 3](#_Toc232854527)

[2.3 Roles 3](#_Toc232854528)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232854529)

[2.5 Business Conditions 5](#_Toc232854530)

[3 Overview Table 6](#_Toc232854531)

[4 Test Procedures 7](#_Toc232854532)

[4.1 Inference Call 7](#_Toc232854533)

[4.1.1 Transfer Clarification Cases 7](#_Toc232854534)

[4.1.2 Process Returned and Reserved Clarification Cases 9](#_Toc232854535)

[4.2 Process Clarification Case with Machine Learning Proposal 15](#_Toc232854536)

## Purpose

Manually clearing of incoming payments to open receivables is one of the most labour-intense processes in today’s accounting departments. The main goal of this solution is to significantly improve the automatic clearing rate by applying machine learning techniques to the bank statement incoming payment/clearing process in order to reduce the manual work and to save cost.

Overview

In this process, when you transfer your bank statement to payment lots, standard rule-based proposals are generated and the automatic posting and clearing is executed. If you've activated this scope item, the new machine learning service is triggered for payment lot items where the clearing isn't successfully completed. This service proposes selection categories and selection values for triggering the FI-CA clearing control. If you choose to trigger the automatic clearing and the confidence level is above the threshold, the FI-CA clearing control is automatically processed with consideration to the machine learning proposals.

In this document, you can:

- Connect to machine learning service and configure machine learning confidence level
- Train your machine learning model
- Run payment lot, send data to machine learning service and fetch the proposal
- Process the clarifications

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/d34b7b968fec5cd8e65e083e658af0ab)

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
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  | Company code |
| Company Code Group | 3310 |  | Company Code Group |

### Business Conditions

Before this scope item can be tested, meet the following business conditions.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Business partner and contract account have been created for posting. |
| 2BI - Contract Accounting – Customer Initiated Payments | Must be run before this test script. Payment lots have been created for training machine leaning model and posting. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Transfer Clarification Cases](#unique_9) [page ] 7 | Administrator - Accounts Payable and Receivable (FI-CA) | Data Exchange with Cash Application - Inference of Clarification Proposals (F4203) | The clarification cases should be send to Machine learning. |
| [Process Returned and Reserved Clarification Cases](#unique_10) [page ] 9 | Administrator - Accounts Payable and Receivable (FI-CA) | Data Exchange with Cash Application (F4203) | The clarification cases should be processed by Machine learning. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Inference Call

#### Transfer Clarification Cases

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This mass activity can be executed each time after processing a bank statement and posting the corresponding payment lot. If the company code is enabled for ML support and the most recently trained ML model does not exceed the maximum age defined in customizing, any clarification cases created will be automatically updated with a new status. These cases will then be sent to the Cash App for review before any manual processing by an accountant.

Prerequisite

Make sure you already have an active machine learning model. Please refer to step Fetching Training Status from Machine Learning in Setting Up Contract Accounting – Cash Application (47I).

Prepare the clarification cases. Please refer to step Payment Lot Processing in Contract Accounting – Customer Initiated Payments (2BI). You can import and process bank statement to post payment lot then get clarification cases. Also, you can create and post payment lot manually to get clarification cases. The clarification cases must have the memo line for Machine Learning analysis. When you try to clarify the payment lot, an error message Clarification Case has been reserved for Machine Learning should be displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Data Exchange with Cash Application - Inference of Clarification Proposals (F4203). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job screen is displayed. |  |
| 4 | Enter Required Parameters | Make the following entry:Job Template: Transfer Clarification CasesChoose Step 2.Start immediately: selectStart: <Today's Date>Choose Step 3.Run ID Prefix: ID0Company code: 3310Lot: <Payment lot ID>Problem Class: Additional InformationNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the Recurring run for Mass activity for your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 7 | Display Job | Navigate to the new application job by choosing the information icon.Note down the Run ID. | The Job Log screen displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log as below:The number of data records to be sent should be > 0.The total number of CSV files should be > 0.At least one File name ‘Clarifications1’ should be created successfully.Mass activity for at least 1 case should be actually carried out. |  |
| 8 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 9 | Access App | Open Process Payment Lot (FP05). | The Process Payment Lot screen displays. |  |
| 10 | Input Parameters | Make the following entry on the Process Payment Lot tab:Payment Lot: <Input Payment Lot ID in step 4>Choose List, mark one item and choose Payments. | At the bottom of the screen, a new section Machine Learning information should be displayed. The ML status should be a proposal was requested. The Prediction Rate should be 0,0000. |  |
| 11 | Clarify Payment | Choose Clarify Payment. | Message Clarification Case has been reserved for Machine Learning should be displayed. |  |

#### Process Returned and Reserved Clarification Cases

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can test the application for Processing the Inference Jobs.

Prerequisite

Check the setting of SAP Cash Application, change the settings if necessary. Please refer to step Self Service Configuration UI for Cash Application for Contract Accounting in Setting Up Contract Accounting – Cash Application (47I).

Procedure

Obtain ML proposal for successfully transferred inference jobs.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Data Exchange with Cash Application (F4203). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job screen is displayed. |  |
| 4 | Enter Required Parameters | Make the following entry:Job Template: Process Returned and Reserved Clarification CasesChoose Step 2.Start immediately: SelectStart: <Today's Date>Choose Step 3.Date ID: <Select Date ID from an existing mass run>Run ID: <Select Identification from an existing mass run>Data Sent Successfully: SelectOn the Options tab:Adjust Confidence Rating: <Causes a ML proposal to be checked before saving if the confidence rating meets the values set in Customizing>Adjustment Type for Uncertain: <When reviewing an uncertain ML proposal, causes possible clearing to be seen as successful, even with posting on account. Only consider this setting if the indicator for adjusting the confidence rating is set>Adjustment Type for Certain Pr: <When reviewing a secure ML proposal, causes possible clearing is seen as successful, even with posting on account. Only consider this setting if the indicator for adjusting the confidence rating is set>Clear Automatically: <Specifies that if the confidence quota of a machine learning proposal has attained the confidence quota set for the clearing, the automatic clearing posting is triggered>Release Clarification Cases: <If errors occur during communication with the Cash Application, the reserved clarification cases can be released for manual processing. Possible causes of error may include errors in the classification case transfer or errors in the proposal request. After another attempt to request the proposal, the clarification cases are released in the event of errors>Simulation Run: UnselectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the Recurring run for Mass activity for your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. | Case 1:Adjust Confidence Rating: UnselectClear Automatically: UnselectCase 2:Adjust Confidence Rating: SelectClear Automatically: UnselectCase 3:Clear Automatically: SelectCase 4:Release Clarification Cases: Select |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 7 | Display Job | Navigate to the new application job by choosing the information icon. | The application log should display that a proposal has been obtained. At least include one successfully processed job.Case 1:Adjust Confidence Rating: UnselectClear Automatically: UnselectThe application log should display that a proposal has been obtained. At least include one successfully processed job. If the application log displays that a proposal could not be obtained (the call to ML id failed), go to Test Case 4 directly.Case 2:Adjust Confidence Rating: SelectClear Automatically: UnselectThe application log should display that a proposal has been obtained. If a wrong proposal with a high confidence exists, a message The confidence rating was lowered from <x> to <y> should be displayed. If a correct proposal with a low confidence exists, a message The confidence rating was raised from <x> to <y> should be displayed. At least one successfully processed job.If the application log displays that a proposal could not be obtained (the call to ML id failed), go to Test Case 4 directly.Case 3:Clear Automatically: SelectThe application log should display that a proposal has been obtained. At least include one successfully processed job. If the application log displays that a proposal could not be obtained (the call to ML id failed), go to Test Case 3 directly.Case 4:Release Clarification Cases: SelectThe application log should display that a proposal could not be obtained, but all clarification cases have been released for manual processing. One successfully processed job. |  |
| 8 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 9 | Access App | Open Process Payment Lot (FP05). | The Process Payment Lot screen displays. |  |
| 10 | Input Parameters | Make the following entry on the Process Payment Lot tab:Payment Lot: Input Payment Lot ID in step 4Choose List, mark one item and click Payments. | Case 1/Case 2:At the bottom of the screen, the section Machine Learning information should be displayed. The ML status should be one of these:No proposal was created (no prediction rate or below the confidence rate for review)No valid proposal was created (prediction rate below confidence rate for proposal)One valid proposal has been created (prediction rate between the confidence rate for proposal and clearing)One valid proposal has been created (prediction rate between the confidence rate for proposal and clearing)Case 3:At the bottom of the screen, the section Machine Learning information should be displayed. The ML status should be one of these:No proposal was created (no prediction rate)No valid proposal was created (prediction rate below confidence rate for proposal)One valid proposal has been created (prediction rate between the confidence rate for proposal and clearing)A secure proposal has been created (prediction rate above confidence rate for clearing)A secure proposal has been created with clearing (prediction rate above confidence rate for clearing)In case the ML status is not the last one, go back to test Case 3 and execute another mass run. |  |
| 11 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 12 | Access App | Open Clarify Incoming Payments (FPCPL). | The Clarify Incoming Payments screen displays. |  |
| 13 | Input Parameters | Make the following entry on the Process Payment Lot tab:Payment Lot: Input Payment Lot ID in step 4Choose Execute. | Case 1/Case 2:The ML status should be displayed accordingly. If a valid or secured proposal exists, it should be displayed.If the prediction rate displayed in Process Payment Lot is above the confidence rate for proposal, the ML proposal should be displayed.If the prediction rate displayed in Process Payment Lot is below the confidence rate for proposal, the ML proposal should not be displayed.Case 3:If a secure proposal has been created, the clarification item should be completed.No clarification item should be displayed |  |

Process clarification cases for not successfully transferred inference jobs.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Data Exchange with Cash Application (F4203) | The Post Document: Initial Screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job screen is displayed. |  |
| 4 | Enter Required Parameters | Make the following entry:Job Template: Process Returned and Reserved Clarification CasesStart immediately: SelectStart: <Today's Date>Date ID: <Select Date ID from an existing mass run>Identification: <Select Identification from an existing mass run>Data Sent with Errors: SelectOn the Option tab:Release Clarification Cases: <If errors occur during communication with the Cash Application, the reserved clarification cases can be released for manual processing. The clarification case (inference job) transfer contained errors: The clarification cases can be released immediately>Delete Jobs: Select <If the transfer of the current clarification case to the Cash Application for Contract Accounting contained errors, you can delete the jobs generated after you have carried out a transfer once again>Simulation Run: UnselectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the Recurring run for Mass activity for your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. | Case 5:Release Clarification Cases: UnselectDelete Jobs: SelectCase 6:Release Clarification Cases: SelectDelete Jobs: Unselect |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 7 | Display Job | Navigate to the new application job by choosing the information icon. | Case 5:The number of successfully processed jobs should be 0. The messages in the application log should indicate that the jobs can be deleted.Case 6:The number of successfully processed jobs should be > 0. The messages in the application log should indicate that the clarification cases have been released for manual processing. |  |

### Process Clarification Case with Machine Learning Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can test the ML enhancements of the application for Payment Assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Clarify Incoming Payments (FPCPL). | The Clarify Incoming Payments screen displays. |  |
| 3 | Input Parameters | Make the following entry on the Process Payment Lot tab:Payment Lot: Input Payment Lot IDChoose Execute. |  |  |
| 4 | Clarify Payment Lot | Select a clarification case and double-click it (or choose clarify). | At the bottom of the clarification screen, the section Machine Learning information should be displayed.The ML status should be one of these:One valid proposal has been created (prediction rate between confidence rate for proposal rate and clearing)A secure proposal has been created (prediction rate above confidence rate for clearing)At the top of the clarification screen (under selection proposal) a new column ML Proposal should indicate which of the proposals has been generated by the Cash Application. |  |
| 5 | Test Step: Post using the ML Proposal | Only select the proposals which are marked as ML proposal and post. |  |  |

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
- see-also :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-integration-with-sales-documents-43y-a]]
- see-also :: [[03-financial-accounting-and-close/steps-to-create-bai2-format-file-207]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/47I_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,047 chars in the whole document
