---
id: 16-two-tier-erp-and-central-finance/two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance
title: Two-Tier – Consolidation of autonomous subsidiaries via Central Finance (1W4) (S4CLD2608_2T__Consolidation_with_CFINEN)
description: "Customer guide and test script for scope item 1W4: replicating finance documents from an S/4HANA Cloud Public Edition subsidiary to an on-premise Central Finance HQ."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/central-finance-replication]
aliases: [S4CLD2608_2T__Consolidation_with_CFINEN]
keywords: [Central Finance Replication from Subsidiaries, central finance, two-tier erp, financial consolidation, data replication, subsidiary integration, communication arrangements, supplier invoices, payment run, outgoing invoices]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T__Consolidation_with_CFINEN.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-228
topic: 16-two-tier-erp-and-central-finance/central-finance-replication
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier – Consolidation of autonomous subsidiaries via Central Finance (1W4) (S4CLD2608_2T__Consolidation_with_CFINEN)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T__Consolidation_with_CFINEN.docx`, extracted with `mammoth`. Grouped under **Central Finance Replication from Subsidiaries** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026EnglishEnglish |  |
|  | Two-Tier – Consolidation of autonomous subsidiaries via Central Finance (1W4) |
| SAP SE Dietmar-Hopp-Allee 16 69190 Walldorf Germany | Customer Guide |

Copyright

© 2024 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 01.09.2017 | Initial version of document |
| 1 | 21.05.2020 | Updated version |

Only add a revision when corrections are made to a published document. Do not change the original published date. Set back to revision 0 after a full upgrade of the Customer Guide.

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Content

[1 Purpose 6](#_Toc494189437)

[2 Value Proposition 6](#_Toc494189438)

[2.1 Business Requirements 6](#_Toc494189439)

[2.2 Two-Tier Solution 6](#_Toc494189440)

[3 Business Process Details 7](#_Toc494189441)

[3.1 Prerequisites 7](#_Toc494189442)

[3.2 Process Flow with Technical Details 8](#_Toc494189443)

[4 Technical Requirement 8](#_Toc494189444)

[4.1 Integration Requirements by using API 8](#_Toc494189445)

[4.2 Integration Requirements by using EDI/IDOC 8](#_Toc494189446)

[4.3 Reporting Requirements by using Analytical CDS Views 9](#_Toc494189447)

[4.4 Reporting Requirements by using Analytical API 9](#_Toc494189448)

[5 Test Script 10](#_Toc494189449)

[5.1 Purpose 10](#_Toc494189450)

[5.2 Prerequisites 10](#_Toc494189451)

[5.2.1 System Access and Roles 10](#_Toc494189452)

[5.2.2 Master Data, Organizational Data, and Other Data 11](#_Toc494189453)

[5.2.3 Preliminary Steps 12](#_Toc494189454)

[5.3 Overview Table 13](#_Toc494189455)

[5.4 Test Procedures 14](#_Toc494189456)

[5.4.1 Post Supplier Invoice 14](#_Toc494189457)

[5.4.2 Pay (via payment run) 16](#_Toc494189458)

[5.4.3 Create Outgoing Invoice 18](#_Toc494189459)

[5.4.4 Pay via Incoming Payment 19](#_Toc494189460)

[6 Appendix 22](#_Toc494189461)

[6.1 Relevant Scope ID’s / Test Scripts 22](#_Toc494189462)

**Consolidation of autonomous subsidiaries via Central Finance**

## Purpose

This document will provide the detailed process on Two-Tier approach for the consolidation of the autonomous subsidiaries via central Finance with process flow, technical requirements and followed with testing procedure.

## Value Proposition

*For complex system landscapes, SAP S/4HANA/SAP Cloud ERP Private can be deployed in Tier One as a Central Finance System which holds all financial documents of the entire group and will be a starting point for the centralized financial consolidation.*

In a Two-Tier scenario where the headquarter is S/4HANA On-premise/SAP Cloud ERP Private deployed as a Central Finance System. All financial documents from other SAP and non-SAP systems are replicated into the Central Finance system including the financial documents from a SAP Cloud ERP representing a Tier Two Subsidiary.

### Business Requirements

The following are key business requirements

- Headquarter need access to real-time financial data from the subsidiaries to perform the group level Financial Consolidation and profitability reporting
- Monitoring the end to end processes between headquarters and subsidiaries
- Communication/Data integration between Headquarter and Subsidiaries

### Two-Tier Solution

With Two-tier approach S/4HANA Cloud solution will be deployed on subsidiary and integrates with Headquarters which runs on S/4HANA On-premise deployed as a Central Finance System.

The previous documents (legacy data) are extracted and posted in the Central system in a process called as the ‘Initial Load’. The Initial Load process uses RFC connection to transfer data from the source system to the target system.

After successful completion of the Initial Load, the replication is activated which starts the real time replication of all documents in the source to the target through the System Landscape Transformation Tool (SLT).

The following business benefits will be achieved with Two-tier approach.

- Non-Disruptive & Company wide single source of truth.
- Consistent reporting in a single system which runs on SAP S/4HANA OP
- Leverage embedded planning and real time consolidation in Central Finance.
- Process centralization (shared services team).
- Pre-delivered scenario with in-built mapping and error handling capabilities.
- Same scenario for replication from other source systems
- Get detailed visibility of financial information down to transaction level

## Business Process Details

This Scope item simulates a Two-tier scenario for consolidation of autonomous subsidiaries via Central Finance.

The Integration between the S/4HANA Cloud Public Edition subsidiary and the HQ running on-Premise Central Finance is setup and the data (Supplier/Customer Invoice and Payment) is replicated from the subsidiary to the headquarter for the consolidation purpose.

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Connection/Integration between Headquarter and Subsidiary system
- Master data synchronization between Headquarter and Subsidiary
- Replication must be activated which starts the real time replication of all documents from source to the target system
- IDR is mandatory for carrying out initial load to S/4HANA PCE because of Universal Parallel Accounting (UPA) in SAP S4HANA Cloud Public edition.

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

## Technical Requirement

Refer technical setup guide for integration between S/4HANA Cloud Public Edition and S/4HANA On-premise or Private Cloud deployed as a Central Finance

[https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/1W4_Set-Up_EN_XX.pdf](https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/1W4_Set-Up_EN_XX.pdf)

A communication arrangement needs to be activated in SAP S/4HANA for communication with the on-premise Central Finance instance via SLT Server (using RFC calls supported by SAP Cloud Platform Cloud Connector). The communication arrangement is named as follows: ● SAP_COM_0083 - Central Finance Subsidiary Integration

**Master Data Replication**

Refer the Master Data setup guide

### Integration Requirements by using API

-NA-

### Integration Requirements by using EDI/IDOC

-NA-

### Reporting Requirements by using Analytical CDS Views

-NA-

### Reporting Requirements by using Analytical API

-NA-

## Test Script

### Purpose

This script enables the setup of an integration between SAP S/4HANA Cloud Public Edition Subsidiary and Headquarter running SAP S/4HANA Central Finance.

The integration provides a replication of finance transaction data from SAP S/4HANA Cloud to SAP S/4HANA Central Finance. You can activate the data replication on a company code level in the SAP S/4HANA Cloud Public edition system.

SAP BTP Cloud Connector and SAP Landscape Transformation Replication Server are used as integration technology.

This document provides a detailed procedure for testing the scope item after solution deployment, reflecting the predefined scope of the solution. Each process step is covered in its own section, providing the system interactions (that is, test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly (see the Test Step column). Customer-project-specific steps must be added.

### Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Access and Roles

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| S/4 Cloud Public Edition (Sub) | Your system administrator provides you with the URL |
| onPremise S/4 (HQ) | Your system administrator provides you with the URL to access the various apps assigned to your role. |

Use the following standard test users or assign roles to testers, respectively:

| Business Role | Business Role Description | Business Role ID | Log On |
| --- | --- | --- | --- |
| Account Payable Accountant | Responsible Accountant for Account Payable | AP_ACCOUNTANT | Test user: AP_ACCOUNTANTPassword: Welcome1 |
| Account Receivable Accountant | Responsible Accountant for Account Receivable | AR_ACCOUNTANT | Test user: AR_ACCOUNTANTPassword: Welcome1 |

### 5.2.2 Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline package, you can use the following Baseline package scenario data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1710 | Company Code for US |  |
| Invoicing Party | 17300001 | Supplier Number |  |
| Customer Number | 17100001 | Customer Number |  |
| Invoice G/L Account in | 61006000 | G/L Account used for incoming Invoice |  |
| Invoice G/L Account out | 41090000 | G/L Account used for outgoing Invoice |  |
| Cost Center | 17101101 | Cost Center for Invoice |  |
| Profit Center | YB600 | Profit Center for Invoice |  |
| Segment | 1000_C | Segment for Invoice |  |
| Tax Code In | 10 | Tax Code for incoming tax |  |
| Tax Code Out | 00 | Tax Code for outgoing tax |  |
| Tax Jurisdiction Code | 0100100000 | Tax Jurisdiction Code |  |
| Bank Account | 11001080 | Bank Account for outgoing payments |  |
| House Bank | USBK1 / USAC1 | Own Bank |  |

#### Preliminary Steps

The Integration Scenario SAP_COM_0083 is activated.

SLT Connection is setup.

Refer Document :

[https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/1W4_Set-Up_EN_XX.pdf](https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/1W4_Set-Up_EN_XX.pdf)

## 5.3 Overview Table

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Supplier Invoice](#unique_7) | AP_ACCOUNTANT | Tile: Create Supplier Invoice | Supplier invoice is reposted in CFIN system |
| [Pay (via payment run)](#unique_8) | AP_ACCOUNTANT | Tile: Manage Automatic Payments | Payment is reposted in CFIN system with clearing |
| [Create Outgoing Invoice](#unique_9) | AP_ACCOUNTANT | Tile: Create Outgoing Invoices | Outgoing invoice is reposted in CFIN system |
| [Pay via Incoming Payment](#unique_10) | AP_ACCOUNTANT | Tile: Post Incoming Payments | Payment is reposted in CFIN system with clearing |

## 5.4 Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

#### 5.4.1 Post Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step you create a supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on Source | Log on via Fiori Launchpad with business role AP_ACCOUNTANT in the subsidiary source system. | You are logged on to the system. |  |
| 2 | Navigate | Select the tile Create Supplier Invoice | The Supplier Invoice screen appears. |  |
| 3 | Create a Simple Supplier Invoice | Enter the details or choose the following data via Value Help- Invoicing Party: 17300001- Company Code: 1710- Gross Invoice Amount: Enter your test amount- Invoice Date / Posting Date: Enter the current test dateGoto section G/L Line Items, add a line via the + button and fill:- G/L account: 61006000- Amount: Enter your test amountOpen the Details section via the > button and fill:- Tax data: I0/0100100000- Cost Center: 17101101- Profit Center: YB600- Segment: 1000_C | Invoice is posted without errors. |  |
| 4 | Log on Target | Log on to the target Central Finance system. | You are logged on to the system. |  |
| 5 | Display Documents | Start transaction to display documents (FB03) and click the button Document List and fill:- Posting Date: Enter the current test date.Choose Dynamic Selections (Shift+F4) and make field: Company Code in Sender System available in the selection criteria.Select via:-Company Code in Sender System: 1710 | You should find the document posted successfully.The Sender* fields in the document header should contain the correct information from the source system.Sender Log System: QS8CLNT715Sender CoCode: 1710Sender Doc.No: Enter the G/L document number from step 3.Sender Fiscal Yr: Enter the fiscal year related to the date. |  |

#### 5.4.2 Pay (via payment run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

Pay the supplier invoice via payment run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on Source | Log on via Fiori Launchpad with business role AP_ACCOUNTANT in the subsidiary source system. | You are logged on to the system. |  |
| 2 | Navigate | Select the tile Manage Automatic Payments. | The Manage Automatic Payments screen appears. |  |
| 3 | Select Supplier Invoice | Create a new Payment run via the '+' button; and fill:- Run Date: Enter the current test date.- Identification: For example, RUN001Enter the following data to select the supplier invoice created before:- Company Code: 1710- Next Payment Date: Enter the current test date- Payment Method: Choose all | Invoice is selected. |  |
| 4 | Proposal Run | Save the entries and schedule a proposal run with immediately start. | Proposal is displayed. |  |
| 5 | Execute Payment | Execute Payment Run | Payment is posted and invoice is cleared. |  |
| 6 | Log on Target | Log on to the target Central Finance system | You are logged on to the system. |  |
| 7 | Display Documents | Start transaction to display documents (FB03) and click the button Document List an enter the following details:Posting Date: Enter the current test dateChoose Dynamic Selections (Shift+F4) and make field: Company Code in Sender System available in the selection criteriaSelect via:- Company Code in Sender System: 1710 | The payment document is posted and the document header text contains the payment run information.The payment document line item is updated with the clearing document information. |  |

#### 5.4.3 Create Outgoing Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step you create an outgoing invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on Source | Log on via Fiori Launchpad with business role AR_ACCOUNTANT in the subsidiary source system. | You are logged on to the system. |  |
| 2 | Navigate | Select the tile Create Outgoing Invoices. | The Create Outgoing Invoices screen appears. |  |
| 3 | Create a Simple Outgoing Invoice | Enter or choose the following data via Value Help- Customer No: 17100001- Invoice Date / Posting Date :Enter the current test date- Reference information: Enter a number you choose- Amount: Enter the test amount- G/L Account: 41090000- Tax data: 00/ 0100100000- Cost Center: 17101101 | Invoice is posted without errors. |  |
| 4 | Log on Target | Log on to the target Central Finance system | You are logged on to the system. |  |
| 5 | Display Documents | Start transaction to display documents (FB03) and click the button Document List and fill:- Posting Date: Enter the current test date.Choose Dynamic Selections (Shift+F4) and make field: Company Code in Sender System available in the selection criteria.Select via:- Company Code: 1710 | You should find the document posted successfully.The Sender* fields in the document header should contain the correct information from the source system.Sender Log System: QS8CLNT715Sender CoCode: 1710Sender Doc.No: Enter the G/L document number from step 3.Sender Fiscal Yr: Enter the fiscal year related to the date entered. |  |

### 5.4.4 Pay via Incoming Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

Pay the supplier invoice via an incoming payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on source | Log on via Fiori Launchpad with business role AR_ACCOUNTANT in the subsidiary source system. | You are logged on to the system |  |
| 2 | Navigate | Select the tile Post Incoming Payments. | The Post Incoming Payments screen appears. |  |
| 3 | Define Dates and Bank Data for Payment | Enter or choose the following data via Value Help:- Bank G/L account: 11001080- House Bank: USBK1 / USAC1- Amount: Enter the test amount |  |  |
| 4 | Display Open Items | For customer used in test case 3 (use the button Propose Items) | Open Items are displayed. |  |
| 5 | Pay Open Item | Choose the outgoing invoice from test case 3 for clearing and post the incoming payment. | Payment is posted and invoice is cleared. |  |
| 6 | Log on Target | Log on to the target Central Finance system. | You are logged on to the system. |  |
| 7 | Display Documents | Start transaction to display documents (FB03) and click the button Document List and fill:- Posting Date: Enter the current test date.Choose Dynamic Selections (Shift+F4) and make field: Company Code in Sender System available in the selection criteria.Select via:- Company Code: 1710 | The payment document is posted.The payment document line item is updated with the clearing document information. |  |

## Appendix

### Relevant Scope ID’s / Test Scripts

1W4 - Subsidiary Integration of SAP S/4HANA Cloud Public Edition to Central Finance

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview table lists AP_ACCOUNTANT for Create Outgoing Invoice and Post Incoming Payments, while test procedures use AR_ACCOUNTANT

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document header says SAP Cloud ERP June 2026 but revision history ends 2020 and copyright says 2024

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-process-integration-of-sap-s-4hana-finance-with-central-fi]]
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-project-data-replication-to-central-finance-3w1-978]]
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-subsidiary-integration-of-sap-s-4hana-cloud-to-central-fin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T__Consolidation_with_CFINEN.docx` — full document · extracted with `mammoth` · 21,684 chars in the whole document
