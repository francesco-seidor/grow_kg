---
id: 03-financial-accounting-and-close/psm-preparation-guide-254
title: PSM Preparation Guide (BP_CLD_ENTPR_PSM_Preparation_Guide)
description: Preparation steps in a starter system and test-script adjustments needed to test SAP S/4HANA Cloud with Public Sector Management (non-US countries).
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/public-sector-fund-accounting]
aliases: [BP_CLD_ENTPR_PSM_Preparation_Guide]
keywords: [Fund Accounting and Public Sector Setup, public sector management, starter system preparation, cost center derivation, substitution rules, government budget management, test script adjustments, down payment requests, financial statement versions, functional areas]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/BP_CLD_ENTPR_PSM_Preparation_Guide.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-254
topic: 03-financial-accounting-and-close/public-sector-fund-accounting
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# PSM Preparation Guide (BP_CLD_ENTPR_PSM_Preparation_Guide)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/BP_CLD_ENTPR_PSM_Preparation_Guide.docx`, extracted with `mammoth`. Grouped under **Fund Accounting and Public Sector Setup** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
|  |  |
| PSM Preparation GuideSAP S/4HANA Cloud 2402January 2024English | Customer |
| Using Test Scripts from SAP Best Practices for SAP S/4HANA Cloud Public Edition for Public Sector ManagementPreparation Steps in Starter System for Non-US Countries |  |

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

Table of Contents

1 Purpose 4

2 Preparation 5

2.1 Prerequisites 5

3 Configuration 6

3.1 Deactivate Cost of Sales Accounting 6

3.2 Delete YBXX Functional Areas from G/L Accounts 6

3.3 Assign Sponsored Classes to G/L Accounts when Posting to a Relevant Grant Master (Applies to Scope Item 71S) 6

3.4 Create Your Own Financial Statement Version (Applies to Several Financial Scope Items such as J58, 7AU, …) 7

3.5 Adjust Warehouse Cost Center (Applies to Several Procurement and Inventory Scope Items such as BML, BNX, …) 7

3.6 Derive Cost Center for Billing – Applies to Scope Item 2EQ (Sales of Services), BD9 (Sell from Stock) 7

4 Application Adjustments 10

4.1 Load and Maintain Public Sector Budget – Refers to the Scope Item 6YU (Government Budget Management) 10

4.2 Assign PSM Account Assignment to Cost Centers 10

5 Adjusted Testing Procedures of Existing Scope Items 11

5.1 Assign PSM Account Assignments to WBS Elements – Refers for example to the Scope Items 1NT (Project Financial Control), 35F (Capital Investment Project Management),4RF (Project Control Procurement), BNA (Period End Closing – Projects) 11

5.2 Skip Testing of Project Budget and Availability Control Steps – Applies to the Scope Items 1NT (Project Financial Control), 35F (Capital Investment Project Management) 11

5.3 Skip Commitment Management and Cost Center Budgeting – Applies to the Scope Item J54 (Overhead Accounting) 11

5.4 Skip Repost Line Items – Applies to the Scope Item J54 (Overhead Accounting) 12

5.5 Skip Execute Profit Center Distribution – Applies to the Scope Item J54 (Overhead Accounting) 12

5.6 Skip Predictive Analytics – Applies to the Scope Item 2I3 (Predictive Commitments Management) 12

5.7 Create Single Payment (Direct) – Applies to the Scope Item J60 (Accounts Payable) 12

5.8 Create Down Payment Request – Applies to the Scope Items J59 (Accounts Receivable) and J60 (Accounts Payable) 12

5.9 Skip Free Form Payments – Applies to the Scope Item J60 (Accounts Payable) 13

5.10 Message “Line item requires an assigned fund” (for Example Scope Item J58) 13

5.11 Create Invoices Without Sales Order / Create Customer Down Payment Request – Applies to the Scope Item J59 (Accounts Receivable) 13

## Purpose

This document describes the additional configuration and implementation steps that you must carry out in your starter system before you can test the SAP S/4HANA Cloud solution with Public Sector Management using pre-delivered demo data. Please note that some standard scope item test scripts contain entries that might not apply to a Public Sector environment and as a result, those testing steps need to be skipped. These topics need to be communicated to your testers at testing kick-off.

## Preparation

### Prerequisites

To carry out the following activity, a business user with a business role must exist. The business role must contain the business catalog SAP_CORE_BC_COM (Communication Management), for example, the business role SAP_BR_ADMINISTRATOR (Administrator) is required.

Additionally, the business role SAP_BR_BPC_EXPERT must be assigned to the user.

## Configuration

Procedure

1. Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution → Configure Your Solution. You can search for a configuration step. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

### Deactivate Cost of Sales Accounting

Search for the following configuration activities and create the required settings:

| Configuration Activity | Instruction |
| --- | --- |
| Deactivate Cost of Sales Accounting (SSCUI) | Deactivate Cost of Sales Accounting: |

### Delete YBXX Functional Areas from G/L Accounts

Search for the following activity: “Manage GL Account Master Data”,start the app and go to “Mass Change”. Change the functional areas YB* to space.

### Assign Sponsored Classes to G/L Accounts when Posting to a Relevant Grant Master (Applies to Scope Item 71S)

Please note that whenever posting to a relevant grant master, ensure that you assign a sponsored class to the G/L account. This is described in the test script for scope item 71S.

### Create Your Own Financial Statement Version (Applies to Several Financial Scope Items such as J58, 7AU, …)

If the financial statement versions (FSV) delivered for your country only contain reporting for ‘Cost of Sales’ as hierarchy nodes, which use functional area assignment, create your own financial statement version. Copy an existing FSV and remove the reference to the functional areas.

Use the Define Financial Statement Versions in Global Hierarchies implementation activity for this.

### Adjust Warehouse Cost Center (Applies to Several Procurement and Inventory Scope Items such as BML, BNX, …)

Search for the following activity Derive Account Assignment for Material Stock Postings. Make sure the cost center is suitable for the company code you are testing. The first four characters must equate to your company code. Adjust the cost center if necessary.

### Derive Cost Center for Billing – Applies to Scope Item 2EQ (Sales of Services), BD9 (Sell from Stock)

Whenever Public Sector Management is active, all revenues and expenses need to derive a cost center. For revenues, this is done using a substitution rule. To set up such a substitution rule, please perform the following activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert – Business Process Configuration. | The SAP Fiori Launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution/Validation Rules – Group Journal Entries (F4406). | A list of all existing rules appears. |  |
| 3 | Create Rule | Enter Coding Block as the Business Context, Coding Block as the Event and Substitution Rule as the Rule Type. | The New Substitution screen appears. |  |
| 4 | Fill out Screen Fields and Save the Rule | Rule Name: CCTRSDRule Description: Cost Center for SDAs the Precondition:ReferenceDocumentType (Field) Equal (Operator) to VBRK(Value)CostCenter (Field) is empty (Operator)As Substitution:CostCenter (Target Field) XXXX1101 (Source replace XXXX with the company code you are testing, for example 1010) | Rule is saved with the status New. |  |
| 5 | Activate the Rule by Choosing Activate |  | Rule is activated. |  |
| 6 | Create Another Rule | Enter Coding Block as Business Context, Coding Block as Event and Substitution Rule as Rule Type. | The New Substitution screen appears. |  |
| 7 | Fill out Screen Fields and Save the Rule | Rule Name: CCTRGIRule Description: Cost Center for GRAs Precondition:GLAccount (Field) Between (Operator) 0051000000 (Value) and 0054999999 (Value) ReferenceDocumentType (Field) Equal (Operator) to MKPF (Value)CostCenter (Field) is empty (Operator)As Substitution:CostCenter (Target Field) XXXX1101 (Source XXXX with the company code you are testing, for example 1010) | The rule is saved with the status New. |  |
| 8 | Activate the Rule by Choosing Activate |  | The rule is activated. |  |
| 9 | Create Another Rule | Enter Coding Block as Business Context, Coding Block as Event and Substitution Rule as Rule Type. | The New Substitution screen appears. |  |
| 10 | Fill out Screen Fields and Save Rule | Rule Name: CCTRG2Rule Description: Cost Center for GIAs Precondition:GLAccount (Field) Equal (Operator) to 0054083000 (Value)CostCenter (Field) is empty (Operator)As Substitution:CostCenter (Target Field) XXXX1101(Source XXXX with the company code you are testing, for example 1010) | The rule is saved with the status New. |  |
| 11 | Activate the Rule by Choosing Activate |  | The rule is activated. |  |

## Application Adjustments

### Load and Maintain Public Sector Budget – Refers to the Scope Item 6YU (Government Budget Management)

Whenever you post an expense document, budget is being checked and consumed. If the budget is not sufficient, availability control raises an error message. To avoid such messages, you need to upload Public Sector budget. This step is described in scope item 6YU step Upload Budget. If a tester runs out of budget, it is also possible to increase the budget by posting a budget supplement document. This process is also described in the scope item 6YU.

### Assign PSM Account Assignment to Cost Centers

Whenever you post an expense or revenue to a cost center, Public Sector account assignments (fund, grant, functional area) need to be derived from the cost center. To achieve this, you need to assign PSM account assignments to all cost centers. This procedure with example assignments is described in master data script 7CB (Update Cost Center with Public Sector Management Account Assignments). If testers are creating new cost centers, they need to assign the cost center to the PSM account assignments in the cost center master data manually. Please also note that all functional areas starting with YB need to be replaced in the cost centers.

## Adjusted Testing Procedures of Existing Scope Items

### Assign PSM Account Assignments to WBS Elements – Refers for example to the Scope Items 1NT (Project Financial Control), 35F (Capital Investment Project Management),4RF (Project Control Procurement), BNA (Period End Closing – Projects)

Whenever you create a WBS element below a project, you assign a fund, a non-relevant grant “NRG” and a functional area (do not use functional areas called YBXX). You enter those values in the section General Information in the WBS element master. These values are derived from the WBS element if it is used during postings to commitment or actual documents.

### Skip Testing of Project Budget and Availability Control Steps – Applies to the Scope Items 1NT (Project Financial Control), 35F (Capital Investment Project Management)

Whenever Public Sector Management is active, budgeting is not processed in project management, but in the scope item 6YU (Government Budget Management). As such, all the related topics must be skipped completely during the testing of any project-related scope item.

The following topics are to be skipped (all functions below are handled by 6YU):

- Upload, adjust, capture, maintain project budget.
- Project availability control profile in configuration and WBS element master data. The fields in the WBS element master data do not appear.
- Monitor notifications.
- Monitor budget reports.
- Situation types
- Manage teams and responsibilities

Whenever you post to a WBS element, you need to make sure to have budget for the WBS element. This step is described in 6YU (Government Budget Management).

### Skip Commitment Management and Cost Center Budgeting – Applies to the Scope Item J54 (Overhead Accounting)

Whenever Public Sector Management is active, budgeting is not processed in overhead accounting for cost centers, but in scope item 6YU (Government Budget Management). As such, all related topics must be skipped completely during the testing of overhead accounting.

The following topics are to be skipped (all functions below are handled by 6YU):

- Upload, adjust, capture, maintain project budget.
- Project availability control profile in the configuration and WBS element master data. The fields in the WBS element master data do not appear.
- Monitor notifications.
- Monitor budget reports.
- Situation types
- Manage teams and responsibilities

### Skip Repost Line Items – Applies to the Scope Item J54 (Overhead Accounting)

The step Repost Line Items - Cost Accounting does not apply to Public Sector and should be skipped.

### Skip Execute Profit Center Distribution – Applies to the Scope Item J54 (Overhead Accounting)

The step Execute Profit Center Distribution does not apply to Public Sector and should be skipped.

### Skip Predictive Analytics – Applies to the Scope Item 2I3 (Predictive Commitments Management)

Since commitments are updated using Public Sector Management, the complete scope item does not apply to Public Sector.

### Create Single Payment (Direct) – Applies to the Scope Item J60 (Accounts Payable)

InDown Payment Requests, a cost center (for example, XXXX1101 and replace XXXX with the company code you are testing, for example 1010) needs to be entered.

### Create Down Payment Request – Applies to the Scope Items J59 (Accounts Receivable) and J60 (Accounts Payable)

In the app Manage Supplier Down Payment Requests (F1688) and Manage Customer Down Payment Requests (F1689) a cost center (for example, XXXX1101 and replace XXXX with the company code you are testing, for example 1010) needs to be entered.

### Skip Free Form Payments – Applies to the Scope Item J60 (Accounts Payable)

The step Free Form Payments does not apply to Public Sector and should be skipped.

### Message “Line item requires an assigned fund” (for Example Scope Item J58)

There are situations (for example in the scope item J58) when you get a message saying that the line requires an assigned fund (or grant or profit center). If possible, enter the fund (or grant or profit center) in the line item.

### Create Invoices Without Sales Order / Create Customer Down Payment Request – Applies to the Scope Item J59 (Accounts Receivable)

In customer invoices and down payment requests, a cost center (for example, XXXX1101 and replace XXXX with the company code you are testing, for example 1010) needs to be entered.

When entering the cost center during the mass import of customer invoices, the prerequisite Manage Default Account Assignments can be skipped.

|  |
| --- |
|  |
| www.sap.com/contactsap |
| © 2024 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company.SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. Please see [http://global.sap.com/corporate-en/legal/copyright/index.epx#trademark](http://global.sap.com/corporate-en/legal/copyright/index.epx#trademark) for additional trademark information and notices.Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP SE or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP SE or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. In particular, SAP SE or its affiliated companies have no obligation to pursue any course of business outlined in this document or any related presentation, or to develop or release any functionality mentioned therein. This document, or any related presentation, and SAP SE’s or its affiliated companies’ strategy and possible future developments, products, and/or platform directions and functionality are all subject to change and may be changed by SAP SE or its affiliated companies at any time for any reason without notice. The information in this document is not a commitment, promise, or legal obligation to deliver any material, code, or functionality. All forward-looking statements are subject to various risks and uncertainties that could cause actual results to differ materially from expectations. Readers are cautioned not to place undue reliance on these forward-looking statements, which speak only as of their dates, and they should not be relied upon in making purchasing decisions. |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Guide is labelled release 2402 (January 2024) although it sits in the 2608 best-practices bundle; may be outdated versus 2608 content.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Section on skipping J54 Commitment Management and Cost Center Budgeting lists project-budget/WBS items (project budget, availability control profile, WBS master data), apparently copied from the project section.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-fund-accounting-7au-sap-s-4hana-cloud-public-edition-1206]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/BP_CLD_ENTPR_PSM_Preparation_Guide.docx` — full document · extracted with `mammoth` · 18,017 chars in the whole document
