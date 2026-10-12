---
id: 14-maintenance-service-and-projects/test-script-intercompany-processes-project-based-services-16t-ae-704
title: "Test Script: Intercompany Processes – Project-Based Services (16T_AE) (16T_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for intercompany project-based services (scope item 16T), US delivering company billing DE ordering company."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/intercompany-project-services]
aliases: [16T_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Project-Based Services and Project Control, intercompany project billing, intercompany sales order, customer project, travel expense invoice, time recording, business roles, master data, business conditions, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/16T_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-704
topic: 14-maintenance-service-and-projects/intercompany-project-services
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Processes – Project-Based Services (16T_AE) (16T_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/16T_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Project-Based Services and Project Control** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Processes – Project-Based Services (16T_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232846430)

[2 Prerequisites 3](#_Toc232846431)

[2.1 System Access 3](#_Toc232846432)

[2.2 Roles 3](#_Toc232846433)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232846434)

[2.4 Business Conditions 5](#_Toc232846435)

[3 Overview Table 7](#_Toc232846436)

[4 Test Procedures 8](#_Toc232846437)

[4.1 Check Intercompany Sales Order 8](#_Toc232846438)

[4.2 Create Customer/Internal Project 9](#_Toc232846439)

[4.3 Time Recording 10](#_Toc232846440)

[4.4 Create Supplier Invoice for Travel Expenses of Intercompany Resource 10](#_Toc232846441)

[4.5 Run Intercompany Billing Process 10](#_Toc232846442)

## Purpose

Overview

A company has an affiliate company. The affiliate company delivers a service to the ordering company in the course of a customer project. The affiliate company posts expenses and records time on the project. These expenses are transformed into billing document requests. An intercompany invoice with reference to billing document request is created by the delivering company. The intercompany invoice is posted automatically also to the accounts payables of the ordering company.

|  |
| --- |
| Note The intercompany process described here is sample data.The ordering company is DE.The delivering company is US.The scenario described in this test script is based on a scenario where an US company delivers services for a German (“DE”) affiliated company.If you want to apply intercompany process for other countries/regions, adapt country/region-specific data as mentioned in the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) scope item. |

|  |
| --- |
| Note Both country/region solutions for DE and US have to be activated to support the intercompany process. The intercompany process is only applicable for the two countries/regions DE and US, not for any other countries/regions. |

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
| Internal Sales Representative - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV | Internal Sales - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV | Suggested sample user INTERNAL_SALES_REP_PRSV representing the business role Internal Sales Representative - Professional Services. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Suggested sample user BILLING_CLERK representing the business role Billing Clerk. |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Management – Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Suggested sample user PROJECT_MANAGER_PROF representing the business role Project Manager – Professional Services. |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC | Suggested sample user EMPLOYEE representing the business role Employee. |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Suggested sample user AP_ACCOUNTANT representing the business role Accounts Payable Accountant. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline Package, you can use the following Baseline Package scenario data:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | P002 | Project-based Service: Time & Expenses | Material which is used in order to describe different services being provided to the customer |
| Material | E001 | Accommodation |  |
| Material | E002 | Airfare |  |
| Material | E003 | Ground Transportation |  |

|  |
| --- |
| Note Allowed changes to the above listed service-related materials are limited to descriptions and some attributes, since they are provided with DIP-Profile, a technical object necessary for selling of project-based services. |

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 10401010 | Customer in ordering company, for example 1710 (US) representing the receiving company, for example 1010 (DE) | This is sample data. You can apply other countries'/regions' data on your needs. |
| Supplier | 17401710 | Supplier in ordering company, for example 1010 (DE) representing the receiving company, for example 1710 (US) | This is sample data. You can apply other countries'/regions' data on your needs. |
| Sales Organization | 1710 | Sales Org., for example, US | This is sample data. You can apply other countries'/regions' data on your needs. |
| Distribution Channel | 10 | Direct Sales | This is sample data. You can apply other countries'/regions' data on your needs. |
| Division | 00 | Product Division 00 | This is sample data. You can apply other countries'/regions' data on your needs. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 31X | Create Product Master of type "Service Product" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

|  |
| --- |
| Note Both country/region solutions have been activated, for example, delivering company is US and ordering company is DE. |

| Scope Item | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based Services | Must be run in ordering company, for example, DE before this test script. See details below. |
| J12 - Time Recording – Project-Based Services | Must be run before this test script. See details below. |
| J13 - Service and Material Procurement – Project-Based Services | Must be run before this test script. See details below. |
| 4AN - Intercompany Billing for Cross-Company Cost Accounting Postings | To execute the intercompany billing process for projects, the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) scope item must be activated. |

|  |
| --- |
| Note Specific data that has to be used for the Intercompany process in test scripts J11, J12 and J13 is listed in the following chapters of this document. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Check Intercompany Sales Order](#unique_8) [page ] 8 | Internal Sales Representative - Professional Services | List Sales Orders - Intercompany (VA05_AUART) | Intercompany Sales Order is created in delivering company code 1710 for selling company code 1010. |
| [Create Customer/Internal Project](#unique_9) [page ] 9 | Project Manager - Commercial Services | See Customer Project Management – Project-Based Services(J11) scope item | A customer project is created in company code 1010. |
| [Time Recording](#unique_10) [page ] 10 | See Time Recording – Project-Based Services(J12) scope item | See Time Recording – Project-Based Services(J12) scope item | Time is recorded for employees (DE and US employees) staffed on the project. |
| [Create Supplier Invoice for Travel Expenses of Intercompany Resource](#unique_11) [page ] 10 | Accounts Payable Accountant | See Service and Material Procurement – Project-Based Services(J13) scope item | A supplier invoice for travel expenses of the intercompany resource is created in company code 1710. |
| [Run Intercompany Billing Process](#unique_12) [page ] 10 |  | See Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) scope item |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check Intercompany Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

This process step shows you how to check intercompany sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open List Sales Orders - Intercompany (VA05_AUART). | The List of Sales Orders screen displays. |  |
| 3 | Check if Intercompany Sales Order Exists | Make necessary filter to check if an intercompany sales order exists in delivering company.For example, delivering company 1710 to customer 10401010, set as sales organization: 1710, Sold-to-party: 10401010Choose Execute at the right bottom to display list of sales order.Note If the intercompany sales order does not exist, proceed with the steps in scope item Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) and create the order. | One (and only one) intercompany sales order exists.Make a note of the sales order document number. |  |
| 4 | Access the App | Open Create Sales Orders - VA01 (VA01) | The Create Intercompany Order: Overview screen displays. |  |
| 5 | Verify the Order Type | The system defaults the Order Type. You can verify it by selecting on the top left arrow, near the SAP logo and the Home icon.Order Type: SO03 - Intercompany OrderChoose Continue. |  |  |
| 6 | Enter Order Details | In the Header section, make the following entries:Sold-To Party: for example, 10401010Dialogue box of possible Sales Area related to Sold-To Party displays. Select the correct one of your scenario.In the All Items section near bottom of the page, make the following entries:Material: P002Amount: 1000 | This is sample data. You can apply other countries/regions' data on your needs.Note Order Quantity is disabled and Target Quantity is filled with "1" by system automatically. |  |
| 7 | Save Intercompany Sales Order | Save the sales order document.Note The currency of the delivering company will be used in the sales order. For example, if the delivering company is US, the currency: USD. | An intercompany sales order is created. Make a note of the sales order document number. |  |

### Create Customer/Internal Project

In this activity a customer/internal project is created with a work package for time and material in ordering company, for example company code 1010 (DE).

An internal employee and intercompany resource from delivering company, for example company code 1710 are staffed to the project.

Proceed with the following test steps:

For Customer Project:

1. Create Customer Project: create a customer project as described in test script Customer Project Management – Project-Based Services (J11) for the ordering service org. company, for example DE (Sales Area 1010 / 10 / 00). Customer: Inlandskunde DE 1.
2. Maintain work packages and Time-based planning. Create a work package for time and material as described in test script Customer Project Management – Project-Based Services (J11).
3. Maintain work package Staffing with intercompany resource. Maintain staffing of the work package as described in test script Customer Project Management – Project-Based Services(J11). Staff an internal employee (own employee = tester) and an intercompany resource from delivering company, for example company code 1710 (Consultant1_US).
4. Maintain Customer Project Billing. The project billing information is maintained as described in test script Customer Project Management – Project-Based Services (J11). Create a billing item for time and expense.

For Internal Project:

1. Create Internal Project: create an internal project as described in test script Internal Project Management – Project-Based Services (1A8) for the ordering service org. company.
2. Maintain work packages and Time-based planning. Create a work package for time and material as described in Internal Project Management – Project-Based Services(1A8).
3. Maintain work package Staffing with intercompany resource. Maintain staffing of the work package as described in test script Internal Project Management – Project-Based Services (1A8). Staff an internal employee (own employee = tester) and an intercompany resource from delivering company, for example company code 1710 (Consultant1_US).

### Time Recording

For both employees staffed on the project (internal employee and intercompany resource) time has to be recorded.

Please refer to test script Time Recording – Project-Based Services(J12) and proceed with the step “Perform time recording”. For internal employee with the employee user used above. For the intercompany employee, for example, Consultant_1US.

### Create Supplier Invoice for Travel Expenses of Intercompany Resource

A supplier invoice for travel expenses of the intercompany resource is created in delivering company, for example company code 1710.

Please refer to test script Service and Material Procurement – Project-Based Services (J13), step Posting expenses for internal employees w/o PO relation. Use the following data for the supplier invoice:

| Field | Value |
| --- | --- |
| Document Type | ER – Manual Expense Travel |
| Account | Accommodation (61003000) |

Assign the expenses to the work package of the project created before in ordering company, for example, company code 1010. This type is triggering the reposting of the expenses to the target company code, for example, company code 1010.

### Run Intercompany Billing Process

Procedure

To execute this activity, perform the whole intercompany billing process described in the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) test script.

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
- related-to :: [[14-maintenance-service-and-projects/test-script-project-control-intercompany-4au-ae-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/16T_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 20,534 chars in the whole document
