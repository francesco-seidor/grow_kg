---
id: 17-leasing-and-real-estate/test-script-integration-of-sap-s-4hana-and-sap-cloud-for-real-estate-4
title: "Test Script: Integration of SAP S/4HANA and SAP Cloud for Real Estate (4X3) (4X3_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 4X3: assigning a building in SAP Cloud for Real Estate to an existing or new leasing contract via app F6627 (S/4HANA Cloud Public 2608)."
cluster: 17-leasing-and-real-estate
tags: [kb/leasing-and-real-estate, topic/real-estate-contracts-and-leasing]
aliases: [4X3_S4CLD2608_BPD_EN_XX]
keywords: [Real Estate Rental Objects and Lease Accounting, real estate integration, building contract assignment, test scripts, business roles, lease accounting, prerequisites, 4X3]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X3_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1054
topic: 17-leasing-and-real-estate/real-estate-contracts-and-leasing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Integration of SAP S/4HANA and SAP Cloud for Real Estate (4X3) (4X3_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X3_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Real Estate Rental Objects and Lease Accounting** in Leasing and Real Estate. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Integration of SAP S/4HANA and SAP Cloud for Real Estate (4X3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232832640)

[2 Prerequisites 3](#_Toc232832641)

[2.1 System Access 3](#_Toc232832642)

[2.2 Roles 3](#_Toc232832643)

[2.3 Additional Manual Configuration 3](#_Toc232832644)

[2.4 Business Conditions 4](#_Toc232832645)

[3 Overview Table 5](#_Toc232832646)

[4 Test Procedures 6](#_Toc232832647)

[4.1 SAP Cloud for Real Estate 6](#_Toc232832648)

[4.1.1 Assign Building to Existing Contract 6](#_Toc232832649)

[4.1.2 Assign Building to New Contract 7](#_Toc232832650)

## Purpose

Overview

This scope item is only relevant for the integration with SAP Cloud for Real Estate. It enables you to connect master data such as contracts or equipment records to a building, floor, or room in SAP Cloud for Real Estate.

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
| Contract Specialist - Leasing | SAP_BR_RECM_SPECIALIST | Leasing Contract Management / Leasing Contract Management - Sales-Based Rent | SAP_BR_RECM_SPECIALIST / SAP_BR_RECM_SALES_REPORTER |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b2edd0a95b63a8bc2472e99e8603694f)

### Business Conditions

Before this scope item can be tested, the following two business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1T6 - Lease-In Accounting or21P - Lease-In Accounting – Group Ledger IFRS or21Q - Lease-Out Accounting or21R - Service Contract or2SB - Lease-Out for Sublease Accounting or2SA - Lease-Out for Sublease Accounting – Group Ledger IFRS or34N - Lease-In Accounting – Group Ledger US GAAP or34O - Lease-Out for Sublease Accounting – Group Ledger US GAAP or3F4 - Sales-Based Rent | At least, one of the below scope items from Contract and Lease Management is activated.SAP Cloud for Real Estate is activated.Leasing contract must exist. |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Assign Building to Existing Contract](#unique_8) [page ] 6 | Contract Specialist - Leasing | Manage Real Estate Locations (F6627) | The building is assigned to existing contract. |
| [Assign Building to New Contract](#unique_9) [page ] 7 | Contract Specialist - Leasing | Manage Real Estate Locations (F6627) | The building is assigned to new contract. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### SAP Cloud for Real Estate

#### Assign Building to Existing Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you assign the building to an existing contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Cloud for Real Estate | Go to the SAP Cloud for Real Estate FLP. Login as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access Manage Real Estate Locations | Open Manage Real Estate Locations (F6627). | The Manage Real Estate Locations app displays. |  |
| 3 | Navigate to Building | Navigate to your building (for example, POT04). | The building displays. |  |
| 4 | Open Dialog to Assign Contract | In the Contracts section, choose Add Contract. | A dialog box displays. |  |
| 5 | Enter Contract data | Make the following entries:Company Code: <your company code>Contract Type: <Per the Create contract test case>Contract Name: <Name for your Contract> | Data is shown. |  |
| 6 | Save Contract Assignment | Choose Add Contract. | The dialog box closes. The table is updated. |  |

#### Assign Building to New Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you assign the building to a new contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Cloud for Real Estate | Go to the SAP Cloud for Real Estate FLP. Login as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access Manage Real Estate Locations | Open Manage Real Estate Locations (F6627). | The Manage Real Estate Locations app displays. |  |
| 3 | Navigate to Building | Navigate to your building (for example, POT04). | The building displays. |  |
| 4 | Open Dialog to Create Contract | In the Contracts section, choose Create Contract. | A dialog box displays. |  |
| 5 | Enter Contract data | Make the following entries:Company Code: <your company code>Contract Type: Per the Create contract test caseContract Name: Name for your Contract | Data is shown. |  |
| 6 | Save Contract | Choose Create. | The dialog box closes. The table is updated. |  |

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
- related-to :: [[17-leasing-and-real-estate/accounting-interface-for-contract-and-lease-management-7od-ae-test-scr]]
- related-to :: [[17-leasing-and-real-estate/create-rental-object-master-data-script-7ad-521]]
- related-to :: [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-523]]
- related-to :: [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-525]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X3_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 10,311 chars in the whole document
