---
id: 03-financial-accounting-and-close/intercompany-billing-for-cross-company-cost-accounting-postings-4an-ae
title: Intercompany Billing for Cross-Company Cost Accounting Postings (4AN_AE) - Test Script (4AN_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4AN: intercompany sales order, billing request and invoice between US (delivering) and DE (ordering)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/intercompany-cost-billing]
aliases: [4AN_S4CLD2608_BPD_EN_AE]
keywords: [Billing of Costs Between Affiliated Companies, intercompany billing, intercompany sales order, intercompany billing request, intercompany invoice, cross-company cost accounting, test scripts, business roles, master data, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AN_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1010
topic: 03-financial-accounting-and-close/intercompany-cost-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intercompany Billing for Cross-Company Cost Accounting Postings (4AN_AE) - Test Script (4AN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Billing of Costs Between Affiliated Companies** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Billing for Cross-Company Cost Accounting Postings (4AN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854430)

[2 Prerequisites 3](#_Toc232854431)

[2.1 System Access 3](#_Toc232854432)

[2.2 Roles 3](#_Toc232854433)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232854434)

[2.4 Additional Manual Configuration 5](#_Toc232854435)

[2.5 Business Conditions 5](#_Toc232854436)

[3 Overview Table 7](#_Toc232854437)

[4 Test Procedures 8](#_Toc232854438)

[4.1 Time and Expenses Intercompany Settlement 8](#_Toc232854439)

[4.1.1 Check Intercompany Sales Order 8](#_Toc232854440)

[4.1.2 Generate Intercompany Billing Request 9](#_Toc232854441)

[4.2 Invoicing 12](#_Toc232854442)

[4.2.1 Create Intercompany Invoice 12](#_Toc232854443)

## Purpose

Overview

Applications (such as Time Recording for EPPM or Services) can create cross-company cost accounting documents. Additionally, cross-company cost accounting documents can be created manually in Controlling with the Manage Direct Activity Allocation app. For these FI documents, you must still create legal invoices, including tax. Based on resource-related intercompany billing functionality, you can create the necessary customer invoices with the affiliated company as customer. After the invoices are created, the system can automatically create mirroring accounts payable documents in the receiving affiliated company.

|  |
| --- |
| Note The intercompany process described here is sample data.The ordering company is DE.The delivering company is US.The scenario described in this test script is based on a scenario where an US company delivers services for a German (“DE”) affiliated company.If you want to apply Inter Company for other countries/regions, adapt country-specific data. This scope item describes the entire process sequence for the intercompany process for professional services. |

|  |
| --- |
| Note Both country solutions for DE and US have to be activated to support the intercompany process. The intercompany process is only applicable for the two countries DE and US, not for any other countries/regions. |

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline Package, you can use the following Baseline Package scenario data:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | P002 | Project-Based Service: Time & Expenses | Material which is used in order to describe different services being provided to the customer |
| Material | E001 | Accommodation |  |
| Material | E002 | Airfare |  |
| Material | E003 | Ground Transportation |  |

|  |
| --- |
| Note Allowed changes to the above listed service-related materials are limited to descriptions and some attributes, since they are provided with DIP-Profile, a technical object necessary for selling of project-based services. |

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Sold-to party | 10401010 | Customer in delivering company, for example 1710 (US) representing the ordering company, for example 1010 (DE) | This is sample data. You can apply other countries/regions' data on your needs. |
| Supplier | 10401710 | Supplier in delivering company, for example 1010 (DE) representing the ordering company, for example 1710 (US) | This is sample data. You can apply other countries/regions' data on your needs. |
| Sales Organization | 3310 | 3310 Sales Org., for example, US | This is sample data. You can apply other countries/regions' data on your needs. |
| Distribution Channel | 10 | 10 Direct Sales | This is sample data. You can apply other countries/regions' data on your needs. |
| Division | 00 | 00 Product Division 00 | This is sample data. You can apply other countries/regions' data on your needs. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 31X | Create Product Master of type "Service Product" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/356bb9c70bdff678af245a394d56c62a)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

|  |
| --- |
| Note Both country/region solutions have been activated, for example, delivering company is US and ordering company is DE. |

| Scope Item | Business Condition |
| --- | --- |
| 4AU - Project Control – Intercompany | Must be run before this test script. See details below. |
| 16T - Intercompany Processes – Project-Based Services | Must be run before this test script. See details below. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Time and Expenses Intercompany Settlement |  |  |  |
| [Check Intercompany Sales Order](#unique_9) [page ] 8 | Internal Sales Representative - Professional Services | List Sales Orders - Intercompany (VA05_AUART) | Intercompany sales order is created in delivering company code 1710 for selling company code 1010. |
| [Generate Intercompany Billing Request](#unique_10) [page ] 9 | Internal Sales Representative - Professional Services | Generate Intercompany Billing Request (F1829) | One of the following documents is created based on whether the entry Activate new Intercompany Billing exists:A debit memo request is created when the entry Activate new Intercompany Billing does not exist..A billing document request is created when the entry Activate new Intercompany Billing exists. |
| Invoicing |  |  |  |
| [Create Intercompany Invoice](#unique_11) [page ] 12 | Billing Clerk | Execute Billing - Business Partner (FKKBIX_S) | An intercompany invoice is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Time and Expenses Intercompany Settlement

#### Check Intercompany Sales Order

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
| 3 | Check if Intercompany Sales Order is Existing | Make necessary filter to check if an intercompany sales order exists in delivering company.For example, delivering company 1710 to customer 10401010, set as sales organization: 1710, Sold-to-party: 10401010Choose Execute at the right bottom to display list of sales order.Note If the intercompany sales order does not exist, proceed with the following steps to create the order. | One (and only one) intercompany sales order exists.Make a note of the sales order document number. |  |
| 4 | Access the App | Open Create Sales Orders - VA01 (VA01) | The Create Intercompany Order: Overview screen displays. |  |
| 5 | Verify the Order Type | The system defaults the Order Type. You can verify it by selecting on the top left arrow, near the SAP logo and the Home icon.Order Type: SO03 - Intercompany OrderChoose Continue. |  |  |
| 6 | Enter Order Detail | In the Header section, make the following entries:Sold-To Party: for example, 10401010Dialogue box of possible Sales Area related to Sold-To Party displays. Select the correct one of your scenarios.In the All Items section near bottom of the page, make the following entries:Material: P002Amount: 1000 | This is sample data. You can apply other countries/regions' data on your needs.Note Order Quantity is disabled and Target Quantity is filled with "1" by system automatically. |  |
| 7 | Save Intercompany Sales Order | Save the sales order document.Note The currency of the delivering company will be used in the sales order. For example, if the delivering company is US, the currency: USD. | An intercompany sales order is created. Make a note of the sales order document number. |  |

#### Generate Intercompany Billing Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate either one of the following intercompany billing requests based on whether the entry Activate new Intercompany Billing exists in the configuration step Activate New Resource Related Intercompany Billing, which happens via scheduling of an application job.

This step is for intercompany billing for time recordings and expenses that are used by intercompany services.

- Billing document request - generated when the entry Activate new Intercompany Billing exists. To run the new intercompany billing solution, see [Generate Billing Document Request](#unique_10).

Procedure

Generate Billing Document Request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check the Configuration Step - Activate New Resource Related Intercompany Billing (106898) | Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution:Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Navigate to Manage Your Solution > Configure Your Solution. Search for the configuration step Activate New Resource Related Intercompany Billing. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.SAP Central Business ConfigurationLog on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. You can search for the configuration step Activate New Resource Related Intercompany Billing to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). | The Activate New Resource Related Intercompany Billing screen displays. |  |
| 2 | Check if the Entry Activate new Intercompany Billing Exists | On the Activate New Resource Related Intercompany Billing screen, check if the entry Activate new Intercompany Billing exists.If the entry doesn't exist, continue with the following steps.If the entry exists, go to step Maintain Billing Profile ICOBLG001. |  |  |
| 3 | Maintain the Confituration Activity - Activate New Resource Related Intercompany Billing (106898) | Choose New Entries, and the entry Activate new Intercompany Billing is displayed and selected. Choose Save.In the pop-up dialog, choose Yes. | The new entry Activate new Intercompany Billing is created. |  |
| 4 | Maintain Billing Profile ICOBLG001 | For detailed information on this step, refer to the section Maintain a Billing Profile in Project Billing – Project-Based Services (4E9). | Billing profile ICOBLG001 is maintained. |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative - Professional Services. | The SAP Fiori launchpad displays. |  |
| 6 | Access the App | Open Generate Intercompany Billing Request (F1829). | The Generate Intercompany Billing Request screen displays. |  |
| 7 | Schedule Job to Create Intercompany Billing Request | Choose Create. | The New Job screen displays. |  |
| 8 | Enter Schedule Job Details | Make the following entries:Job Template: Resource-Related Billing Between Company CodesJob Name: Resource-Related Billing Between Company CodesChoose Step 2, and make the following entries:Start Immediately: XChoose Step 3, and make the following entries:Intercompany Sales Document: <Document number>Current Month: XChoose Schedule. | Note Click the icon of the Log column to the log detail. There you may find the BDR number in one line of the log content.The billing document request is created. |  |
| 9 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 10 | Access the App | Open Manage Billing Document Requests (F2960). | The Manage Billing Document Requests screen displays. |  |
| 11 | Enter Document Number | Enter the document number of the billing document request you have created before and choose Go.Billing Document Request: <Document number>Note The currency of the sending company will be used in the billing document request. For example, if the sending company is US, the currency: USD. | The billing document request displays. |  |

### Invoicing

#### Create Intercompany Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an intercompany invoice for services which have been executed in the delivering company of the intercompany process. A journal entry is created in finance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Billing Due List screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings and ensure the settings for Automatically post billing document and Display billing document after creation are ON. |  |  |
| 4 | Create Intercompany Invoice | Select the document you created previously and choose Create Billing Documents.In the Create Billing Documents dialog box, select Intercompany Invoice (CI02) from the Billing Type value help. | The Intercompany Invoice screen displays. Check if all billing information here is correct. |  |
| 5 | Check Taxes on Invoice | Check that taxes on the intercompany invoice are zero. | Tax amount is zero. |  |
| 6 | Save the Intercompany Invoice | Choose Save at the right bottom to trigger the formal intercompany invoice. | A formal invoice (start with "9") is generated.Note To check the details of the IDoc generated by the intercompany billing document, you can refer to the section Set up for IDoc Communication in Setting Up Intercompany Billing for Cross-Company Cost Accounting Postings (4AN).The currency of the delivering company will be used in the intercompany invoice. For example, if the delivering company is US, the currency: USD. |  |
| 7 | Preview Intercompany Invoice | On the Billing Document screen, choose the Preview button to generate and print a PDF.Note When you generate output (for example, print) of invoices in the context of the current scope item, SAP recommends that you use the output form template SDBIL_IC_PROF_SRV_US for intercompany invoices. To enable the system to automatically determine this form template when needed, you must create a corresponding entry for billing type CI02 in the Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app. | A PDF printout of the billing document is displayed. |  |
| 8 | Post the Invoice | Choose Post Billing Doc to create an Accounting document. | The invoice is transferred to Accounting. The system displays the message Billing documents posted. |  |
| 9 | Open App (Optional) | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. Open Intercompany Cost Allocation Reconciliation - Review Booklet.Specify filter values as needed:Receiver Company CodeSender Company CodeFiscal YearFiscal Periodand choose Go.Check report for Billing Document and Accounting document (AR) posted as well as invoiced Management Accounting Journal Entries. | The Intercompany Cost Allocation Reconciliation screen displays. |  |

Financial Posting

|  |
| --- |
| Note In all the scenarios related to a Sales Flow, whatever Billing Document is created (Customer Invoice, Debit Note, Credit Note, Intercompany Invoice, etc.) the Journal Entry type is determined according to the following rule:If the Destination country/region is Italy, the FI document type is W1 IT Local Cust. SalesIf the Destination country/region is within European Union, the FI document type is W2 IT EU Cust. SalesIf the Destination country/region is outside European Union, the FI document type is W3 IT EXEU Cust. Sales |

Result

Intercompany billing has been created. In the meantime, the FI posing for A/P (ordering company) will be automatically posted via IDoc.

|  |
| --- |
| Note The currency of the ordering company will be used in the A/P. For example, if the ordering company is DE, the currency: EUR. |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Financial Posting note describes FI document types W1/W2/W3 for Italy/EU/non-EU destinations (Italian localisation), which does not fit the DE/US-only scenario described elsewhere in the same document.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/billing-of-costs-between-affiliated-companies-3zb-ae-test-script-989]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 26,057 chars in the whole document
