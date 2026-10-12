---
id: 06-management-accounting/create-universal-allocation-master-data-mds-2us-287
title: Create Universal Allocation Master Data - MDS (2US) (2US_S4CLD2608_Master_Data_EN_XX)
description: SAP S/4HANA Cloud Public Edition 2608 master data script (2US) for creating plan/actual overhead assessment and profit center distribution cycles in Manage Allocations (F3338A).
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/universal-allocation]
aliases: [2US_S4CLD2608_Master_Data_EN_XX]
keywords: [Universal Allocation Cycles, universal allocation, overhead assessment cycles, profit center distribution, plan allocations, actual allocations, allocation template upload, business roles, master data prerequisites, allocation clearing account]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-287
topic: 06-management-accounting/universal-allocation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Universal Allocation Master Data - MDS (2US) (2US_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Universal Allocation Cycles** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Universal Allocation Master Data - MDS (2US) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904554)

[2 Prerequisites 3](#_Toc233904555)

[2.1 System Access 3](#_Toc233904556)

[2.2 Roles 3](#_Toc233904557)

[2.3 Required Organizational Units 3](#_Toc233904558)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904559)

[3 Overview Table 5](#_Toc233904560)

[4 Test Procedures 6](#_Toc233904561)

[4.1 Plan Allocations 6](#_Toc233904562)

[4.1.1 Manage Plan Overhead Assessment Cycles 6](#_Toc233904563)

[4.1.2 Edit Plan Overhead Assessment Cycles 8](#_Toc233904564)

[4.2 Actual Allocations 10](#_Toc233904565)

[4.2.1 Manage Actual Overhead Assessment Cycles 10](#_Toc233904566)

[4.2.2 Edit Actual Overhead Assessment Cycles 12](#_Toc233904567)

[4.3 Plan Profit Center Allocation 13](#_Toc233904568)

[4.3.1 Manage Plan Profit Center Distribution Cycles 13](#_Toc233904569)

[4.4 Actual Profit Center Allocation 16](#_Toc233904570)

[4.4.1 Manage Actual Profit Center Distribution Cycles 16](#_Toc233904571)

## Purpose

Universal Allocation covers plan and actual assessment/distributions of cost centers in overhead cost controlling using various sender/receiver combinations of amounts, percentages and portions. This master data supports annual planning by redistributing the cost through predefined allocation and distribution cycles within a specific company code. By allocating the cost elements to cost centers in overhead cost controlling, you can control your costs, and compare plan and actual costs. In addition, plan and actual assessment/distributions of profit centers are also supported.

This script provides some general examples of creating master data with Universal Allocation but it can be adapted for your specific business requirements by using the various sender/receiver combinations of amounts, percentages and portions.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Divisional Accountant | SAP_BR_DIVISION_ACCOUNTANT |  |  |  |

### Required Organizational Units

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents cost centers and cost center groups, depending on the operational focus of your company.

| Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Controlling Area | General Data | Mandatory |  |
| Company Code | Organizational Units | Mandatory |  |

### Mandatory and Optional Master Data

Cost center and cost center group master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in allocation.

| Master Data Object | Mandatory / Optional | Comments |
| --- | --- | --- |
| Cost Center | Mandatory |  |
| Cost Element | Mandatory |  |
| Statistical Key Figure | Optional |  |
| Profit Center | Mandatory |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Plan Allocations

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Plan Overhead Assessment Cycles](#unique_8) [page ] 6 | Cost Accountant - Overhead | Manage Allocations (F3338A) | Costs are allocated to cost center groups, cost centers or ranges. |
| [Edit Plan Overhead Assessment Cycles](#unique_9) [page ] 8 | Cost Accountant - Overhead | Manage Allocations (F3338A) | Plan overhead allocation cycles are edited. |

Actual Allocations

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Actual Overhead Assessment Cycles](#unique_10) [page ] 10 | Cost Accountant - Overhead | Manage Allocations (F3338A) | Costs are allocated to cost center groups, cost centers or ranges. |
| [Edit Actual Overhead Assessment Cycles](#unique_11) [page ] 12 | Cost Accountant - Overhead | Manage Allocations (F3338A) | Actual overhead allocation cycles are edited. |

Plan Profit Center Allocation

| Process Step | Business Role | Transaction/App | Expected RPesults |
| --- | --- | --- | --- |
| [Manage Plan Profit Center Distribution Cycles](#unique_12) [page ] 13 | Divisional Accountant | Manage Allocations (F3338A) | The plan profit center distribution is created. |

Actual Profit Center Allocation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Actual Profit Center Distribution Cycles](#unique_13) [page ] 16 | Divisional Accountant | Manage Allocations (F3338A) | The profit center distribution is created. |

## Test Procedures

### Plan Allocations

#### Manage Plan Overhead Assessment Cycles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this example, plan overhead assessment cycle uses secondary cost elements to allocate cost from one cost center or a group of cost centers to another cost center or group of cost centers by a fixed percentage within the same company code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Create Cycle Header | Choose the Create button and select Create New Cycle. | The Create New Cycle dialog box displays.Note Mass upload of allocation cycles is possible for the creation of new allocations and/or new segments via the Manage Allocations app using the Upload/Download Template button. You can either download a blank template or select an existing allocation cycle to download as template. |  |
| 4 | Enter values | Make the following entries and choose the Create button:Allocation Cycle: <enter a cycle ID beginning with Z>Allocation Context: <Cost Centers>Allocation Type:Overhead AllocationLedger: 0LValid To: 12/31/2030Cycle Description: <enter a cycle description>Company Code: 1010Actual/Plan: PlanPlan Category: PLN | The <new cycle> view displays. |  |
| 5 | Enter Segment Data | In the lower section of the New Allocation Cycle view under the Segments section, choose the Create button and make the following entries in the Create New Segment window and choose the Create button:Segment Name: <enter a segment beginning with Z>Segment Description: <enter a description> | The <new segment> view displays. |  |
| 6 | Enter Rules | Select the new segment and choose the arrow on the right.In the Rules tab, make the following entries:Overhead Allocation Account: 94201000Sender Rule: Posted amountsReceiver Rule: Fixed percentagesShare in %: 100Currency: <enter your local currency> |  |  |
| 7 | Enter Senders' Details | In the Senders tab, make the following entries:Account Number:Change the value in the Value Type column to GroupIn the Group column, use the dropdown to select 10_CE in the following Select: Account Number viewCost Center: 10101101 |  |  |
| 8 | Enter Receivers' Details | In the Receivers tab, choose Add. In the Add Receivers view, select Cost Center and choose Add. Make the following entries:Cost CenterChange the value in the Value Type column to GroupIn the Group column, use the dropdown to select 1010300 in the following Select: Cost Center view |  |  |
| 9 | Receiver Basis | In the Receiver Basis tab, choose the … (Additional Options) button, and select Distribute Equally. | You can see that the amounts are equally distributed. |  |
| 10 | Save | Choose the Save button. | Your data is saved. |  |

#### Edit Plan Overhead Assessment Cycles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This activity demonstrates the ability to work with allocations that have large amounts of data using templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Enter Values | Make the following entries and choose the Go button:Allocation Context: <Cost Centers>Company Code: 1010Ledger: 0LAllocation Cycle: <the cycle you just created> | The Allocation Cycles view displays. |  |
| 4 | Allocation Cycle Details | Select your allocation cycle and choose the arrow on the right to go to the details. Choose the Edit button. | The Manage Allocations view displays. |  |
| 5 | Segments Section | Scroll down to the Segments section and select your segment and choose the > (Details) on the right. |  |  |
| 6 | Receiver Basis | In the Receiver Basis tab, choose Upload/Download Values. | The Upload Receiver Values view displays. |  |
| 7 | Upload Receiver Values | Select Download Template with Values. Download and save the file. |  |  |
| 8 | Update Percentages | In the file, update the percentage column with values as shown below:Cost CenterPercentage001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | The percentages are updated. |  |
| 9 | Receiver Basis | Go back to the Receiver Basis tab and do the following:Choose Upload/Download Values.In Upload Receiver Values view, choose Browse. Select your saved file. The screen indicates if the values can be uploaded or if corrections are required. Choose Confirm.Choose Save to save the allocation cycle. | You can see that the data has been updated per the csv file upload. |  |

### Actual Allocations

#### Manage Actual Overhead Assessment Cycles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this example, overhead assessment cycle uses secondary cost elements to allocate cost from one cost center or a group of cost centers to another cost center or group of cost centers by a fixed percentage within the same company code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Create Cycle Header | Choose the Create button and select Create New Cycle. | The Create New Cycle dialog box displays. |  |
| 4 | Enter values | Make the following entries and choose the Create button:Allocation Cycle: <enter a cycle ID beginning with Z>Allocation Context: <Cost Centers>Company Code:1010Allocation Type:Overhead AllocationLedger: 0LValid To: 12/31/2030Cycle description: <enter a cycle description>Company Code: 1010Actual/Plan: Actual | The Allocation: Create Plan Overhead Allocation Cycle: Header Data view displays. |  |
| 5 | Enter Segment Data | In the lower section of the New Allocation Cycle view under the Segments section, choose the Add button and make the following entries in the Create New Segment window:Segment Name: <enter a segment beginning with Z>Segment Description: <enter a description> | The Create a new cycle view displays. |  |
| 6 | Enter Rules | Select the new segment and choose the arrow on the right.In the Rules tab, make the following entries:Overhead Alloc. Acct: 94201000Sender Rule: Posted amountsReceiver Rule: Fixed percentages |  |  |
| 7 | Enter Senders' Details | In the Senders tab, make the following entries:Account Number:Change the value in the Value Type column to GroupIn the Group column, use the dropdown to search and select 10_CE in the following Select: Account Number viewCost Center: 10101101Note In addition to standard cost centers and G/L accounts, you can now use specific journal entry attributes such as currency, functional area, profit center, and segment to enable more granular allocation selection within the sender rule. To do so, choose the Add button, then select the desired options. |  |  |
| 8 | Enter Receivers' Details | In the Receivers tab, choose the + (Add) button.Select Cost Center and choose the Add button.Make the following entry:Cost CenterChange the value in the Value Type column to GroupIn the Group column, use the dropdown to search and select 1010300 in the following Select: Cost Center view |  |  |
| 9 | Receiver Basis | In the Receiver Basis tab, choose the … (Additional Options) button, and select Distribute Equally. | You can see that the amounts are equally distributed. |  |
| 10 | Save | Choose the Save button. | Your data is saved. |  |

#### Edit Actual Overhead Assessment Cycles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This activity demonstrates the ability to work with allocations that have large amounts of data using templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Enter Values | Make the following entries and choose the Go button:Allocation Context: <Cost Centers>Company Code: 1010Ledger: 0LAllocation Cycle: <the cycle you just created> | The Allocation Cycles view displays. |  |
| 4 | Allocation Cycle Details | Select your allocation cycle and choose the arrow on the right to go to the details. | The Manage Allocations view displays. |  |
| 5 | Segments Section | Scroll down to the Segments section and select your segment and choose the > (Details) on the right. |  |  |
| 6 | Receiver Basis | In the Receiver Basis tab, choose the Upload/Download Values. | The Upload Receiver Values view displays. |  |
| 7 | Upload Receiver Values | Select Download Template with Values. Download and save the file. |  |  |
| 8 | Update Percentages | In the file, update the percentage column with values as shown below:Cost CenterPercentage001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | The percentages are updated. |  |
| 9 | Receiver Basis | Go back to the Receiver Basis tab and do the following:Choose Upload/Download Values.In Upload Receiver Values view, choose Browse. Select your saved file. The screen indicates if the values can be uploaded or if corrections are required. Choose Confirm.Choose Save to save the allocation cycle. | You can see that the data has been updated per the csv file upload. |  |

### Plan Profit Center Allocation

#### Manage Plan Profit Center Distribution Cycles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This example shows the plan distribution of balance sheet account balances to and from various profit centers.

Prerequisite

A G/L account for allocation clearing must be available. Create G/L 29500000 CO Allocation Clearing using G/L 29500100 as reference. For details on how to create G/L, refer to Create G/L Account and Cost Element - MDS (BNG).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Divisional Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Create Cycle Header | Choose the Create button and select Create New Cycle. | The Create New Cycle dialog box displays. |  |
| 4 | Enter Values | Make the following entries and choose the Create button:Allocation Cycle: <enter a cycle ID beginning with Z>Allocation Context: <Profit Centers>Company Code:1010Allocation Type:DistributionLedger: 0LValid To: 12/31/2030Cycle description: <enter a cycle description>Company Code: 1010Actual/Plan: PlanPlan Category: PLN | The Manage Allocations view appears. |  |
| 5 | Enter Segment Data | In the lower section of the Manage Allocations view under the Segments section, choose the Create button and make the following entries in the Create New Segment window:Segment Name: <enter another segment beginning with ZD>Segment Description: <enter a description>Choose OK. |  |  |
| 6 | Enter Rules | In the Rules tab, make the following entries:Currency: <enter your local currency>Sender Rule: Fixed amountsShare in %: 100Receiver Rule: Fixed percentagesChoose the Senders tab. |  |  |
| 7 | Enter Senders' Details | In the Senders tab, make the following entries:Account Number:29500000Profit Center: YB600Choose the Sender Basis tab. |  |  |
| 8 | Sender Basis | Make the following entry:Amount: 100000Choose the Receivers tab. |  |  |
| 9 | Enter Receivers' Details | In the Receivers tab, choose + (Add). In the Add Receivers view, select Profit Center. Choose the Add button and make the following entries:Value Type: IntervalSingle Entry/From: YB700To Value: YB800Choose the Receiver Basis tab. |  |  |
| 10 | Receiver Basis | In the Receiver Basis tab, choose the … (Additional Options) button, and select Distribute Equally. | You can see that the amounts are equally distributed. |  |
| 11 | Save | Choose the Save button. | The plan profit center distribution is created. |  |

### Actual Profit Center Allocation

#### Manage Actual Profit Center Distribution Cycles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This example shows actual distribution of balance sheet account balances to and from various profit centers.

Prerequisite

A G/L account for allocation clearing must be available. Create G/L 29500000 CO Allocation Clearing using G/L 29500100 as reference. For details on how to create G/L, refer to Create G/L Account and Cost Element - MDS (BNG).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Divisional Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Create Cycle Header | Choose the Create button and select Create New Cycle. | The Create New Cycle dialog box displays. |  |
| 4 | Enter Values | Make the following entries and choose the Create button:Allocation Cycle: <enter a cycle ID beginning with Z>Allocation Context: <Profit Centers>Company Code:1010Allocation Type:DistributionLedger: 0LValid To: 12/31/2030Cycle description: <enter a cycle description>Company Code: 1010Actual/Plan: Actual | The Allocation: Create Plan Distribution Cycle: Header Data view appears. |  |
| 5 | Enter Segment Data | In the lower section of the Manage Allocations view under the Segments section, choose the Add button and make the following entries in the Create New Segment window:Segment Name: <enter another segment beginning with ZD>Segment Description: <enter a description> | The Allocation: Create Plan Distribution Cycle: Header Data view appears. |  |
| 6 | Enter Rules | Select the newly created segment and choose the > sign on the right. In the Rules tab, make the following entries:Currency: <enter your local currency>Sender Rule: Fixed amountsShare in %: 100Receiver Rule: Fixed percentagesChoose the Senders tab. |  |  |
| 7 | Enter Senders' Details | In the Senders tab, make the following entries:Account Number:29500000Profit Center: YB600Choose the Sender Basis tab. |  |  |
| 8 | Sender Basis | Make the following entry:Amount: 100000Choose the Receivers tab. |  |  |
| 9 | Enter Receivers' Details | In the Receivers tab, choose + (Add). In the Add Receivers view, select Profit Center. Choose the Add button and make the following entries:Value Type: IntervalSingle Entry/From: YB700To Value: YB800Choose the Receiver Basis tab. |  |  |
| 10 | Receiver Basis | In the Receiver Basis tab, choose the … (Additional Options) button, and select Distribute Equally. | You can see that the amounts are equally distributed. |  |
| 11 | Save | Choose the Save button. | The profit center distribution is created. |  |

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
- related-to :: [[06-management-accounting/mds-2us-289]]
- related-to :: [[06-management-accounting/mds-2us-291]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-dados-mestre-de-alocacao-universal-mds-2u]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-datos-maestros-de-asignacion-universal]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 26,915 chars in the whole document
