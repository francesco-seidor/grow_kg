---
id: 05-treasury-and-cash-management/test-script-advanced-bank-statement-automation-4x8-1056
title: "Test Script: Advanced Bank Statement Automation (4X8) (4X8_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4X8: authorizing the cash specialist role and scheduling jobs that create bank statement reprocessing rule templates."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bank-statement-automation]
aliases: [4X8_S4CLD2608_BPD_EN_XX]
keywords: [Advanced Bank Statement Automation, bank statement automation, reprocessing rules, rule templates, bank statement items, cash specialist role, business roles, accounts receivable jobs, test scripts, 4X8]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X8_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1056
topic: 05-treasury-and-cash-management/bank-statement-automation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Advanced Bank Statement Automation (4X8) (4X8_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X8_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Advanced Bank Statement Automation** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Bank Statement Automation (4X8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232832101)

[2 Prerequisites 3](#_Toc232832102)

[2.1 System Access 3](#_Toc232832103)

[2.2 Roles 3](#_Toc232832104)

[2.3 Business Conditions 4](#_Toc232832105)

[2.4 Preliminary Steps 4](#_Toc232832106)

[2.4.1 Modify Cash Specialist Role 4](#_Toc232832107)

[3 Overview Table 6](#_Toc232832108)

[4 Test Procedures 7](#_Toc232832109)

[4.1 Process Bank Statement Items 7](#_Toc232832110)

[4.2 Schedule Accounts Receivable Jobs – Create Templates for Bank Statement Processing Rules 7](#_Toc232832111)

## Purpose

Overview

Advanced Bank Statement Automation creates templates for reprocessing rules by learning from past patterns of the manual actions taken during the reprocessing of the bank statement items. Instead of only being able to create reprocessing rules manually, you can use the templates to create reprocessing rules more easily.

Moreover, with the scope item activated, the reprocessing of bank statement items is triggered automatically following the initial posting. Thus, the system applies the corresponding reprocessing rules to the pending items to complete the postings.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

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
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Must be in scope as prerequisite. |

### Preliminary Steps

#### Modify Cash Specialist Role

Use

In this activity, you modify the cash specialist role to grant authorization for reprocessing rules..

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Roles (F1492). |  |  |
| 3 | Search for Role | Search for SAP_BR_CASH_SPECIALIST and choose Go. |  |  |
| 4 | Details | Select the SAP_BR_CASH_SPECIALIST row and choose Details (>). |  |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Maintain Restrictions | Choose Maintain Restrictions. |  |  |
| 7 | Write, Read, Value Help | In the Write, Read, Value Help field, choose Restricted. |  |  |
| 8 | Current Setting Types | In the Company Code/Current Settings section, choose the Edit button next to the Current Settings Type for Company Codes field. | The Edit Write Restrictions for Current Settings Type for Company Codes dialog box is displayed. |  |
| 9 | Restrictions | Select the following checkboxes and choose OK:01 Authorization to Automate Reprocessing Rules02 Authorization to Share Reprocessing Rules03 Authorization to Use Template for Reprocessing Rules |  |  |
| 10 | Back | Choose Back. |  |  |
| 11 | Save | Choose Save. | Authorizations are saved to the role. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Process Bank Statement Items](#unique_8) [page ] 7 | Refer to the Accounts Receivable (J59) test script, section Manage Bank Statement Reprocessing Rules (Optional). | Refer to the Accounts Receivable (J59) test script, section Manage Bank Statement Reprocessing Rules (Optional). | You reprocessed the bank statement items. |
| [Schedule Accounts Receivable Jobs – Create Templates for Bank Statement Processing Rules](#unique_9) [page ] 7 | Accounts Receivable Accountant | Schedule Accounts Receivable Jobs (F2366) | You created templates for bank statement reprocessing rules. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Process Bank Statement Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

If this scope item is active, the processing run on the uncompleted or open bank statement items is started automatically after the initial posting. The processing is based on the processing rules that you must maintain beforehand.

If this scope item isn't active, see the Accounts Receivable (J59) scope item, section Process Bank Statement Items for instructions on manual bank statement processing.

Procedure

For detailed instructions on how to reprocess bank statement items, see the Accounts Receivable (J59) scope item, section Manage Bank Statement Processing Rules (Optional).

### Schedule Accounts Receivable Jobs – Create Templates for Bank Statement Processing Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This background job creates templates for bank statement processing rules.

Prerequisite

Completed bank statements items must be in the system with at least three identical postings for one company code. If not, refer to the Bank Integration with File Interface (1EG) scope item to upload bank statement files, or to the Basic Cash Operations (BFB) scope item for manual bank statement creation.

Make sure that the bank statement you created consists of at least three bank statement line items. Post these bank statement line items to the same G/L account.

|  |
| --- |
| Note The G/L account shouldn't have been used previously for the respective company code. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule Accounts Receivable Jobs (F2366). | The Application Jobs view displays. |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Create Job | Make the following entries and choose Step 2:Job Template: Bank Statement: Create Templates for Processing RulesJob Name: Bank Statement: Create Templates for Processing Rules |  |  |
| 5 | Create Job | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Create Job | Make the following entries and choose Schedule:Company Code: <company code> | The background job is scheduled and the page skips back to the Application Jobs view. |  |
| 7 | Repeat for KPI | Repeat steps 4 to 6, using the Job Template and Job Name of Bank Statement: Recalculate KPIs for Templates of Bank Statement Processing Rules | The background job is scheduled and the page skips back to the Application Jobs view. |  |
| 8 | Check the logs | Monitor the job status. When the job is processed, the status is Finished.Access the log of the run. | The log states the number of the proposed templates in a success message. |  |
| 9 | Access Fiori app | Return to the SAP Fiori launchpad.Open Manage Processing Rules - For Bank Statements (F3555). |  |  |
| 10 | Check the rule templates | Choose the Rule Templates tab.Check the created rule templates.Check the KPI and note down the values. | The conditions match the existing postings. The actions match the existing actions. |  |
| 11 | Create a rule from the template | Create a rule from the template by choosing Create Rule from Template. |  |  |
| 12 | Access Fiori app | Return to the SAP Fiori launchpad.Open Reprocess Bank Statement Items (F1520). |  |  |
| 13 | Apply the rules | Create a new bank statement item and that matches the rule. Apply the new rule to the item. | The item gets posted accordingly. |  |
| 14 | Access the SAP Fiori app | Return to the SAP Fiori launchpad.Open Manage Processing Rules - For Bank Statements (F3555). |  |  |
| 15 | Recalculate the KPI | Choose Recalculate KPIs on the rule template and check the result. | The past items matching the rule's conditions are in increments of 1. |  |

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
- see-also :: [[03-financial-accounting-and-close/steps-to-create-bai2-format-file-207]]
- see-also :: [[05-treasury-and-cash-management/swift-sample-data-206]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X8_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 13,708 chars in the whole document
