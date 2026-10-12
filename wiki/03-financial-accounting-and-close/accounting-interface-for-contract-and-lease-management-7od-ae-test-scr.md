---
id: 03-financial-accounting-and-close/accounting-interface-for-contract-and-lease-management-7od-ae-test-scr
title: "[DEPRECATED] Accounting Interface for Contract and Lease Management (7OD_AE) - Test Script (7OD_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7OD (AE): real estate expense types, G/L determination, posting periods, and reviewing finance notifications."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/real-estate-contracts-and-leasing]
aliases: [7OD_S4CLD2608_BPD_EN_AE]
keywords: [Real Estate Rental Objects and Lease Accounting, accounting interface, contract and lease management, real estate expense types, g/l account determination, finance notifications, posting periods, journal entries, business roles, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7OD_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: deprecated
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1223
topic: 03-financial-accounting-and-close/real-estate-contracts-and-leasing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Accounting Interface for Contract and Lease Management (7OD_AE) - Test Script (7OD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7OD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Real Estate Rental Objects and Lease Accounting** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Accounting Interface for Contract and Lease Management (7OD_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Accounting Interface for Contract and Lease Management (7OD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232861053)

[2 Prerequisites 3](#_Toc232861054)

[2.1 System Access 3](#_Toc232861055)

[2.2 Roles 3](#_Toc232861056)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232861057)

[2.4 Additional Manual Configuration 4](#_Toc232861058)

[2.5 Preliminary Steps 5](#_Toc232861059)

[2.5.1 Prerequisites – Define Real Estate Expense Types 5](#_Toc232861060)

[2.5.2 Prerequisites – Define Real Estate G/L Account Determination 7](#_Toc232861061)

[2.5.3 Prerequisites – Manage Posting Periods – Cost Accounting 10](#_Toc232861062)

[3 Overview Table 11](#_Toc232861063)

[4 Test Procedure 12](#_Toc232861064)

[4.1 Manage Finance Notifications 12](#_Toc232861065)

## Purpose

Overview

This scope item facilitates seamless integration between third-party applications and SAP Contract and Lease Management, enabling efficient event-based postings to SAP S/4HANA Cloud Public Edition. This integration is particularly crucial for organizations utilizing external applications for order-based transactions, ensuring that all financial activities are accurately captured and reflected within the SAP S/4HANA ecosystem.

Two major business scenarios end up in a cost collection on the third-party side for allocation in SAP S/4HANA Cloud Public Edition: event-based (such as reservation of a meeting room), and internal space/workplace occupancy.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Cost Center | any available cost center with company code relation, for example, 33101101 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

| MDS | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/7aa9f066f9fbf70b9f0da06ce10288b8)

### Preliminary Steps

#### Prerequisites – Define Real Estate Expense Types

Purpose

In this SSC-UI, you define a real estate expense type. You use this as an attribute of the accounting notification for real estate cost allocation to differentiate between different expense posting activities (for example, for area consumption, reservation costs, meal costs, labor costs, or material).

The real estate expense type is a criterion that you can use to define the G/L account determination related to the journal entry processing of real estate cost allocations.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launch Pad displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Define Real Estate Expense Types | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Accounting Buseinss Transaction Interface.Choose the Define Real Estate Expense Types row.Choose New Entries in the Define Real Estate Expense Type: Change screen.Enter the following value on screen New Entries: Add Entries:Expense Typ: <Your expense type>Expense Type Description: <Your expense type description>Choose Save.Note SAP has pre-delivered below real estate expense types as demo data:Table 1:Expense TypeExpense Type DescriptionSC01Space Usage CostsSC02Reservation CostsSC03Catering CostsSC04Material CostsSC05Labor Costs | The Define Real Estate Expense Type: Change view displays and new entrires are maintained. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Define Real Estate Expense Types | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab and search for the following activity: Define Real Estate Expense Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Real Estate Expense Type: Change view displays. |  |
| 3 | Define Real Estate Expense Types | Choose New Entries on the Define Real Estate Expense Type: Change screen.Enter the following value on screen New Entries: Add Entries:Expense Typ: <Your expense type>Expense Type Description: <Your expense type description>Choose Save.Note SAP has pre-delivered below real estate expense types as demo data:Table 2:Expense TypeExpense Type DescriptionSC01Space Usage CostsSC02Reservation CostsSC03Catering CostsSC04Material CostsSC05Labor Costs | New entrires are maintained. |  |

#### Prerequisites – Define Real Estate G/L Account Determination

Purpose

In this SSCUI, you define which G/L accounts are used for the journal entry processing of real estate cost allocations.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launch Pad displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Define Real Estate Expense Types | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Accounting Business Transaction Interface.Choose the Define Real Estate G/L Account Determination row.Choose New Entries on the Define Account Determination: Change screen.Enter the following value on screen New Entries: Add Entries:ChtAccts: YCOAExpense Typ: <Your expense type>Bus. Trans. Category: REA1 or REA2G/L Account: <Your G/L account>Choose Save.Note SAP has predelivered the following G/L account determination as demo data:Table 3:Chart of accountsRE Expense TypeBusiness Transaction CategoryG/L AccountYCOASC01REA197777500YCOASC01REA297777500YCOASC02REA197777500YCOASC02REA297777500YCOASC03REA197777500YCOASC03REA297777500YCOASC04REA197777500YCOASC04REA297777500YCOASC05REA161010000YCOASC05REA261010000 | The Define Account Determination: Change view displays and new entries are maintained. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Define Real Estate Expense Types | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab and search for the following activity: Define Real Estate G/L Account Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Account Determination: Change view displays. |  |
| 3 | Define Real Estate Expense Types | Choose New Entries on the Define Account Determination: Change screen.Enter the following value on screen New Entries: Add Entries:ChtAccts: YCOAExpense Typ: <Your expense type>Bus. Trans. Category: REA1 or REA2G/L Account: <Your G/L account>Choose Save.Note SAP has predelivered the following G/L account determination as demo data:Table 4:Chart of accountsRE Expense TypeBusiness Transaction CategoryG/L AccountYCOASC01REA197777500YCOASC01REA297777500YCOASC02REA197777500YCOASC02REA297777500YCOASC03REA197777500YCOASC03REA297777500YCOASC04REA197777500YCOASC04REA297777500YCOASC05REA161010000YCOASC05REA261010000 | New entries are maintained. |  |

#### Prerequisites – Manage Posting Periods – Cost Accounting

Purpose

In this activity, you can manage posting periods as part of your business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Posting Periods - Cost Accounting (F4684). | The Manage Posting Periods - Cost Accounting screen displays. |  |
| 3 | Check Posting Periods Status | Enter Company Code and Fiscal Year.Choose Go.Find the posting periods for REA1 and REA2. | Data is validated. |  |
| 4 | Open Posting Periods | Select the needed posting periods.Choose Open. | The needed posting periods are open. |  |

## Overview Table

This scope item consists of several processes provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Finance Notifications](#unique_11) [page ] 12 | General Ledger Accountant | Manage Finance Notifications (F8825) | Finance notifications can be checked. |

## Test Procedure

### Manage Finance Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can review finance notifications as part of your daily tasks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Finance Notifications (F8825). | The Manage Finance Notifications screen displays. |  |
| 3 | Choose Finance Notification | In the Reference Document Type field, choose REACN (RE Allocate Costs) and choose Go.From the list of finance notifications you want to review, choose Navigation. | Data is validated.The selected finance notification displays. |  |
| 4 | Check Reference Document | Choose Reference Document.Check if the notification data (for example, expense type, service period, cost center, amount) is correctly received. | The notification data displays. |  |
| 5 | Check Journal Entry | Choose Journal Entries.Click the journal entry number.Choose Display Journal Entries - New Version.On the Journal Entry screen, choose General Information, Line Items, Related Documents, Notes, and Attachments to check if the created journal entry is correct, especially if the G/L account posted is correct. | The Journal Entry screen displays. |  |

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
- related-to :: [[03-financial-accounting-and-close/create-rental-object-master-data-script-7ad-521]]
- related-to :: [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-7ad-523]]
- related-to :: [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-7ad-525]]
- related-to :: [[03-financial-accounting-and-close/script-de-dados-mestre-criar-objeto-de-locacao-mds-7ad-524]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7OD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 19,587 chars in the whole document
