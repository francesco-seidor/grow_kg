---
id: 09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-02
title: Test Script SAP S/4HANA Cloud Public Edition - Contract Accounting – Customer Initiated Payments (2BI_AE) (2BI_S4CLD2608_BPD_EN_AE) — part 2 of 2
description: "Test script for FI-CA customer-initiated payments (S/4HANA Cloud 2608); this part: External Cash Desk setup and APIs, intraday bank statement posting."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-payments]
aliases: []
keywords: [Contract Accounting Incoming and Outgoing Payments, external cash desk, cash desk configuration, external cash point api, payment group closing, intraday bank statements, bank statement transfer, payment lots, payment reversal, open item summary]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BI_S4CLD2608_BPD_EN_AE.docx#lines-2973-3152"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-811
topic: 09-subscription-billing-and-contract-accounting/fi-ca-payments
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Contract Accounting – Customer Initiated Payments (2BI_AE) (2BI_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BI_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 2973–3152 of the extracted text), extracted with `mammoth`. Grouped under **Contract Accounting Incoming and Outgoing Payments** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 8 | Return to Configuration Steps | Click the back button (next to the SAP icon) until the Configuration Steps screen is displayed. | The External Cash Desk configuration is displayed with a list of configuration steps. |  |
| 9 | Create Master Data for the External Cash Desk | Locate Step 3 and choose the Configure button. | The Assign External ID for Branch/Agent ID is displayed. |  |
| 10 | Create the External Cash Desk Structure | Choose New Entries.Enter:an ID for the External Branchthe Branch namean Agent ID - if relevant)select the Branch (created in Step 7) from the drop-down listClick Save.Select the new entry and double-click the Assign External ID for Cash Desks Internal ID node.Choose New Entries.Enter:an ID for the Ext Cash Desk IDa Nameselect the Desk (created in Step 7) from the drop-down-lista company codeHouse Bank ID (if relevant)Bank Account ID (if relevant)Save the changes. |  |  |
| 11 | Return to Configuration Steps | Click the back button (next to the SAP icon) until the Configuration Steps screen is displayed. | The External Cash Desk configuration is displayed with a list of configuration steps. |  |
| 12 | Create Cash Desk Clearing Accounts | Locate Step 5 and choose the Configure button. | A Chart of Accounts dialog box is displayed. |  |
| 13 | Choose Chart of Accounts | Click the drop-down list button and select a chart of accounts. Click Enter to continue. | The Chart of Accounts is accepted and the Maintain Cash Desk/Cash Journal: Cash Desk Clearing Accounts Overview screen is displayed. |  |
| 14 | Enter a Clearing Account | Click Create and enter a Company Code and then select a Cash Desk Clearing Account. | A new entry is stored. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Cash Desk Structure | Go to the Business Processes Configuration app and search for the following activity: Define Cash Desk Structure.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Branches": Overview is displayed |  |
| 3 | Create a Cash Desk Structure | Choose New Entries.Enter:a 3 character ID for the Branchthe Branch nameselect a Branch Category from the drop-down listClick Save.Select the new entry and double-click the Define Cash Desks node.Choose New Entries.Enter a 2 character ID for the desk and a NameSave the changes. | A new branch and desk are stored. |  |
| 4 | Open Define Master Data for External Cash Desk Services | Go to the Business Processes Configuration app and search for the following activity: Define Master Data for External Cash Desk Services.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Assign External ID for Branch/Agent Internal ID": Overview is displayed. |  |
| 5 | Create the External Cash Desk Structure | Choose New Entries.Enter:an ID for the External Branchthe Branch namean Agent ID - if relevant)select the Branch (created in Step 7) from the drop-down listClick Save.Select the new entry and double-click the Assign External ID for Cash Desks Internal ID node.Choose New Entries.Enter:an ID for the Ext Cash Desk IDa Nameselect the Desk (created in Step 7) from the drop-down-lista company codeHouse Bank ID (if relevant)Bank Account ID (if relevant)Save the changes. |  |  |
| 6 | Open Define Cash Desk Clearing Accounts | Go to the Business Processes Configuration app and search for the following activity: Define Cash Desk Clearing Accounts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Chart of Accounts is displayed. |  |
| 7 | Choose Chart of Accounts | Click the drop-down list button and select a chart of accounts. Click Enter to continue. | The Chart of Accounts is accepted and the Maintain Cash Desk/Cash Journal: Cash Desk Clearing Accounts Overview screen is displayed. |  |
| 8 | Enter a Clearing Account | Click Create and enter a Company Code and then select a Cash Desk Clearing Account.Save the changes. | A new entry is stored. |  |

#### Create Payment

Context

In this activity, you transfer a payment from an external cash point to FI-CA. The payment is then processed in FI-CA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open a web browser and navigate to [https://api.sap.com](https://api.sap.com/). | The SAP API hub home page is displayed. |  |
| 2 | Search for the SAP S/4 HANA Cloud API Tile | Click on the tile to open the SAP S/4 HANA Cloud API package. | The package is opened and a list of tiles representing the API’s is displayed. |  |
| 3 | Find the External Cash Point - Inbound Payment Notification API | Enter External Cash in the search field and execute the search. | The API details for the External Cash Point - Inbound Payment Notification API is displayed. |  |

#### Reverse Payment

Context

In this activity, you transfer a reversal for a previously transmitted payment from an external cash point to FI-CA. The payment reversal is then processed in FI-CA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open a web browser and navigate to [https://api.sap.com](https://api.sap.com/). | The SAP API hub home page is displayed. |  |
| 2 | Search for the SAP S/4 HANA Cloud API Tile | Click on the tile to open the SAP S/4 HANA Cloud API package. | The package is opened and a list of tiles representing the API’s is displayed. |  |
| 3 | Find the External Cash Point - Inbound Reversal Notification API | Enter External Cash in the search field and execute the search. | The API details for the External Cash Point - Inbound Reversal Notification API is displayed. |  |

#### Cash Desk Payment Group Closing

Context

In this activity, you transfer a Closing Amount for previously transmitted payments and with a given Payment Grouping Key, from an external cash point to FI-CA. The payment grouping key is then closed in FI-CA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open a web browser and navigate to [https://api.sap.com](https://api.sap.com/). | The SAP API hub home page is displayed. |  |
| 2 | Search for the SAP S/4 HANA Cloud API Tile | Click on the tile to open the SAP S/4 HANA Cloud API package. | The package is opened and a list of tiles representing the API’s is displayed. |  |
| 3 | Find the External Cash Point - Inbound Closing Notification API | Enter External Cash in the search field and execute the search. | The API details for the External Cash Point - Inbound Closing Notification API is displayed. |  |

#### Cash Desk Payment Group Closing Reverse

Context

In this activity, you transfer a Closing Amount for a previously transmitted Closing Amount for a given Payment Grouping Key, from an external cash point to FI-CA. The payment grouping key is then re-opened in FI-CA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open a web browser and navigate to [https://api.sap.com](https://api.sap.com/). | The SAP API hub home page is displayed. |  |
| 2 | Search for the SAP S/4 HANA Cloud API Tile | Click on the tile to open the SAP S/4 HANA Cloud API package. | The package is opened and a list of tiles representing the API’s is displayed. |  |
| 3 | Find the External Cash Point - Inbound Closing Reverse Notification API | Enter External Cash in the search field and execute the search. | The API details for the External Cash Point - Inbound Closing Reverse Notification API is displayed. |  |

#### Open Item Summary

Context

In this activity, you transfer details of open items belonging to a specified business partner/contract account from FI-CA to an external cash point.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open a web browser and navigate to [https://api.sap.com](https://api.sap.com/). | The SAP API hub home page is displayed. |  |
| 2 | Search for the SAP S/4 HANA Cloud API Tile | Click on the tile to open the SAP S/4 HANA Cloud API package. | The package is opened and a list of tiles representing the API’s is displayed. |  |
| 3 | Find the External Cash Point - Open Item Summary API | Enter External Cash in the search field and execute the search. | The API details for the External Cash Point - Open Item Summary API is displayed. |  |

### Intraday Bank Statement Posting (Optional)

Prerequisite

Before you execute steps, please make sure you've completed the following steps via configuration activity.

1. Maintain bank accounts via SAP Fiori App Define Bank Account Settings - Bank Statements (F5488), set the Posting Category (Intraday) of your bank account as Posting to be Processed, and make sure the bank account is enabled for Intraday Postings.
2. Define Identification of Bank Statement Items in Source System (via configuration activity: 105314)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Define Selections of Subscriber Account Items | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingSearch for Define Selections of Subscriber Account Items and choose Configure. | The Define Selections of Subscriber Account Items: Change screen is displayed. |  |
| 4 | Input Parameters | Choose New Entries and input the following entry for your company code:SrceObj.ID: <for example, LOCAL>Field Value Bank Statement Items: <for example, FICA>Description: <for example, LOCAL/FICA>Save the entry. | Settings are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Define Selections of Subscriber Account Items | Go to the Business Processes Configuration app and search for the following activity: Define Selections of Subscriber Account Items.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Selections of Subscriber Account Items: Change screen is displayed. |  |
| 3 | Input Parameters | Choose New Entries and input the following entry for your company code:SrceObj.ID: <for example, LOCAL>Field Value Bank Statement Items: <for example, FICA>Description: <for example, LOCAL/FICA>Save the entry. | Settings are saved successfully. |  |

Prepare and upload intraday bank statement. For internal testing purpose, you can use report TEST_CR_FICA_BANK_STATEMENTS (SE38) to mock the intraday bank statement. Then, verify that the bank statements have been transferred accurately in SAP Fiori App Manage Bank Statements (F1564).

#### Transfer Run for Bank Statements

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Transfer Run for Bank Statements (FPB7P). | The Transfer Run for Bank Statements screen is displayed. |  |
| 3 | Create | Choose Create. | The New Job screen is displayed. |  |
| 4 | Maintain Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Transfer of Data from Bank Statements to Payment LotsJob Name: FI-CA: Transfer of Data from Bank Statements to Payment Lots |  |  |
| 5 | Maintain Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Maintain Parameters | Make the following entries:Run Identification:Prefix of Run ID: For example, ID0Selection Criteria:Company Code: 3310Short Key: <the Short Key of your bank statement>Further Settings:No Split: <Selected>Create Lot: <Selected> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. For credit card outgoing payment, after executing payment run generated clearing document, please refer to step: Payment Card Settlement in 2BI - Contract Accounting – Customer Initiated Payments. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. Payment documents are created from job log details. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Payment Lot Creation from Intraday Bank Statements

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Transfer Bank Statement (FPB7). | The Data Transfer from Account Statement to Payment/Returns Lot screen is displayed. |  |
| 3 | Enter Required Parameters | Choose search help of Identification, select the Run ID which is same as the run ID of step Transfer Run for Bank Statements. | The corresponding Statement Date and ID are displayed accordingly. |  |
| 4 | Execute | Choose Run. | The Payment Lot is created. |  |
| 5 | Check Result | Choose Job overview. | The Parallel Job - Individual Display screen is displayed. |  |
| 6 | Check Detailed Log | Select the job line. Choose the Show Individual Log button. | The Job Log Entries screen is displayed. The detailed job logs are listed. The Payment Lot key is displayed in log for further step. |  |

#### Display Payment Lot

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Display Payment Lot Items | Enter your payment lot ID:Lot: <Your payment lot ID>Choose List. | Payment lot items is displayed. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-01]]
- related-to :: [[09-subscription-billing-and-contract-accounting/contract-accounting-company-initiated-payments-2dp-ae-test-script-813]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BI_S4CLD2608_BPD_EN_AE.docx` — lines 2973–3152 of the extracted text · extracted with `mammoth` · 268,419 chars in the whole document
