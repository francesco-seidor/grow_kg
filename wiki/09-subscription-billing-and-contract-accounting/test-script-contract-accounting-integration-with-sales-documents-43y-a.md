---
id: 09-subscription-billing-and-contract-accounting/test-script-contract-accounting-integration-with-sales-documents-43y-a
title: "Test Script: Contract Accounting - Integration with Sales Documents (43Y_AE) - SAP S/4HANA Cloud Public Edition (43Y_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 43Y_AE: SD billing posted to FI-CA (lean scenario), with configuration, test steps and reconciliation."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-sd-integration]
aliases: [43Y_S4CLD2608_BPD_EN_AE]
keywords: [Contract Accounting Integration with Sales Documents, contract accounting, sd fi-ca integration, billing documents, billing reconciliation, sales orders, billing cancellation, fi-ca documents, manual configuration, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43Y_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1000
topic: 09-subscription-billing-and-contract-accounting/fi-ca-sd-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Accounting - Integration with Sales Documents (43Y_AE) - SAP S/4HANA Cloud Public Edition (43Y_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43Y_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contract Accounting Integration with Sales Documents** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Integration with Sales Documents (43Y_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854322)

[2 Prerequisites 3](#_Toc232854323)

[2.1 System Access 3](#_Toc232854324)

[2.2 Roles 3](#_Toc232854325)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232854326)

[2.4 Business Conditions 5](#_Toc232854327)

[2.5 Preliminary Steps 5](#_Toc232854328)

[2.5.1 Additional Manual Configuration 5](#_Toc232854329)

[3 Overview Table 8](#_Toc232854330)

[4 Test Procedures 10](#_Toc232854331)

[4.1 Contract Accounting Integrated with SD (Lean Scenario) 10](#_Toc232854332)

[4.1.1 Create Sales Order 10](#_Toc232854333)

[4.1.2 Create Billing Document 11](#_Toc232854334)

[4.1.3 Cancel Billing Document (Optional) 12](#_Toc232854335)

[4.2 Display FI-CA Document 13](#_Toc232854336)

[4.3 Reconcile SD Billing Documents 14](#_Toc232854337)

[5 Appendix 16](#_Toc232854338)

[5.1 Process Integrations 16](#_Toc232854339)

## Purpose

Overview

This process enables you to post open items in Contract Accounting for billing documents from Sales Billing. Once the invoicing order is processed in Sales Billing, the document is posted in Contract Accounting as a follow-on document. You can use then the central functions for payment handling and collection management in Contract Accounting for these open items.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | INTERNAL_SALES_REP |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | BILLING_CLERK |
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA | ADMIN_APR_FICA |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA | APR_ACCOUNTANT_FICA |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | BPC_EXPERT |
| Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | SAP_BR_RECONC_SPEC_APR_FICA | Contract Accounting - Reconciliation | SAP_BR_RECONC_SPEC_APR_FICA | RECONC_SPEC_APR_FICA |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Please use following specific Business Partner master data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Material | CBPTS002 |  |  |
| Sold-to-party | 33100023 |  |  |
| Payer | 33100023 |  |  |
| Plant | 3310 |  |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

Or you can find general information on how to create business partner master data objects in - Contract Accounting – Master Data and Basic Functions (‏2AR‏).

|  |
| --- |
| Note Please assign FICA as the Account Group when you create Business Partner master data. |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Contract partner, contract account, and customer master data have been created. |

### Preliminary Steps

#### Additional Manual Configuration

Before proceeding step: Create Billing Document, if you have specific settings, you can add or change your customized configuration via following configuration steps:

Manage Your Solution:

1. Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned.
    - Configure Derive Main/Sub-Transaction from SD Information (SSCUI: 103206), you can customize your Main/Sub-Transaction for the posting of different billing types.
    - Configure Derive Document Type from SD Billing Doc Data (SSCUI: 103207), you can define the document type for the posting of different billing types.
    - Configure Define Subledger Postings for Order Type and Sales Organization (SSCUI: 103452), you can deactivate SD/FI-CA integration by order type and sales organization based on your business requirement.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. You can search for a configuration activity to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
    - Configure Derive Main/Sub-Transaction from SD Information (SSCUI: 103206), you can customize your Main/Sub-Transaction for the posting of different billing types.
    - Configure Derive Document Type from SD Billing Doc Data (SSCUI: 103207), you can define different document type for the posting of different billing types.
    - Configure Define Subledger Postings for Order Type and Sales Organization (SSCUI: 103452), you can deactivate SD/FI-CA integration by order type and sales organization based on your business requirement.

SAP Central Business Configuration (Only for CBC customers):

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Realize phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define and Parameterize External Transactions. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Add following entries for your company code in the sub-folder Parametrize External Transaction of Dialog Structure:

Table 1:

| Main Transaction | Subtransaction | Company Code | Division | Text for Transaction | Debit/Credit Ind. | Manual Posting | Statistical Key |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0500 | 0011 | 3310 | 00 | SD Invoice Cancellation | H | X |  |
| 0500 | 0012 | 3310 | 00 | SD Credit Memo | H | X |  |
| 0500 | 0014 | 3310 | 00 | SD Down Payment | H | X |  |
| 0500 | 0021 | 3310 | 00 | SD Invoice | S |  |  |
| 0500 | 0022 | 3310 | 00 | SD Debit Memo | S | X |  |
| 0500 | 0024 | 3310 | 00 | SD Down Payment Request | S | X | A |

1. Choose Save.
2. Configure Define Acct Assmt Data Relevant to Main Transactions, add following entries:

Table 2:

| Company Code | Division | Account De | Main Transaction | Subtransaction | G/L Account |
| --- | --- | --- | --- | --- | --- |
| 3310 | 00 |  | 0500 | 0011 | 12100200 |
| 3310 | 00 |  | 0500 | 0012 | 12100200 |
| 3310 | 00 |  | 0500 | 0014 | 21186000 |
| 3310 | 00 |  | 0500 | 0021 | 12100200 |
| 3310 | 00 |  | 0500 | 0022 | 12100200 |
| 3310 | 00 |  | 0500 | 0024 | 21186000 |

1. Choose Save.
2. Configure Define Account Determination Data Relevant to Transactions, add following entries:

Table 3:

| Company Code | Division | Account Determin. ID | Main Transaction | Subtransaction | G/L Account | CO Acct Assignment | Tax Determination |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3310 | 00 |  | 1 | 1 | 1 | Y02 | Y1 |
| 3310 | 00 |  | 2 | 2 | 2 | Y02 | Y1 |
| 3310 | 00 |  | 3 | 3 |  | Y02 | Y1 |
| 3310 | 00 |  | 4 | 4 | 4 | Y02 | Y1 |
| 3310 | 00 |  | 5 | 5 | 5 | Y02 | Y1 |
| 3310 | 00 |  | 6 | 6 |  | Y02 | Y1 |

1. Choose Save.

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Complete Master Data (refer to Scope item 2AR)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create a Business Partner (See Scope item 2AR) | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Business Partner | Business Partner master data is completed for succeeding process. |
| Create a Contract Account (See Scope item 2AR) | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Contract Account | Contract Account master data is completed for succeeding process. |
| Creating Customer Master Data - General Data (See Scope item 2AR) | Invoicing SpecialistMaster Data Specialist - Business Partner Data | Maintain Business Partner(BP) | Customer Master – General Data is created. |
| Creating Customer Master Data - Sales Area Data (See Scope item 2AR) | Invoicing SpecialistMaster Data Specialist - Business Partner Data | Maintain Business Partner(BP) | Customer Master – Sales Area Data is created. |

Order Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Sales Order | Internal Sales Representative | Post Document |  |
| Create Billing Document | Billing Clerk | Display Document |  |
| Cancel Billing Document | Billing Clerk | Change Billing Documents |  |

Check FICA Document

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Display Document | Accounts Payable and Receivable Accountant (FI-CA) | Display Document |  |

Reconcile SD Billing Documents

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Reconcile SD Billing Documents | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Reconcile SD Billing Documents |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Contract Accounting Integrated with SD (Lean Scenario)

Contract Accounting integrated with SD introduces the lean process for SD/FI-CA integration.

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Make sure scope item Contract Accounting – Master Data and Basic Functions 2AR has been processed before you run this test script. Contract Partner, Contract Account and Customer Master Data have been created.

In this activity, you can create sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders (F1873).Choose Create > Create Sales Order - VA01. | The Create Sales Documents screen is displayed. |  |
| 3 | Create Sales Order | On the Create Sales Documents screen, make the following entries:Order Type: ORSales Organization: <your Sales Org.>Distribution Channel: 10Division: 00Choose the Continue button. | The Create Standard Order: Overview screen is displayed. |  |
| 4 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: <your customer ID created in step Master Data, Organizational Data, and Other Data>Ship-to Party: <your customer ID created in step Master Data, Organizational Data, and Other Data>Customer Reference: <Reference>Cust. Ref. Date: <Date>Material Number: CBPTS002 or SM0001Quantity: <Quantity> |  |  |
| 5 | Save Document | Choose Save. Make a note of the sales order number. |  |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk.Note Please make sure the role Billing Clerk (SAP_BR_BILLING_CLERK) has been assigned with business catalog: SAP_FICA_BC_DOC_POST_PC. |  |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen is displayed. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example, current date.In the Docs to Be Processed section, select via search value help with Standard Order #, and choose OK. |  |  |
| 4 | Save Billing Document | On the Create Billing Document screen, choose Save.Make a note of the billing document number. |  |  |
| 5 | Display Billing Document | Open Display Billing Documents. Input the billing document you noted down previously. Click continue. | The billing document is displayed. |  |
| 6 | Display Accounting Document (FICA Document) | Choose Accounting tab.The FI-CA document is displayed.Go back to previous page and click DISPLAY DOCUMENT FLOW.Click the Journal Entry document.Click DISPLAY DOCUMENT. | FICA document is displayed. |  |

#### Cancel Billing Document (Optional)

Context

In this activity, you cancel the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk.Note Please make sure the role Billing Clerk (SAP_BR_BILLING_CLERK) has been assigned with business catalog: SAP_FICA_BC_DOC_POST_PC. |  |  |
| 2 | Access the App | Open Change Billing Documents (VF02). | The Change Billing Documents screen is displayed. |  |
| 3 | Display Billing Document | Make the following entry, and choose Enter:Billing Document: <Invoice or Document number> |  |  |
| 4 | Cancel Billing Document | Choose Menu > Billing Document > Cancel Bill. Doc.Choose Save. | The billing document is cancelled. |  |

### Display FI-CA Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

FI-CA documents can be displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access the SAP Fiori App | Open Display Document (FPE3). | The Display Document: Initial screen is displayed. |  |
| 3 | Select Document to Display | Make the following entry and press ENTER:Document Number: <Journal Entry document in Step Create Billing Document> | The Display Document: Overview screen is displayed. The document details are displayed. |  |

### Reconcile SD Billing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

App Reconcile SD Billing Documents (F4866) is used to reconcile SD billing documents and FI-CA documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access the SAP Fiori App | Open Reconcile SD Billing Documents (F4866). | The Reconcile SD Billing Documents screen is displayed. |  |
| 3 | Enter Selections | Make the following entry:Billing Date: <Last week>Choose Go. | Details of the SD Billing documents status are shown. |  |
| 4 | Check Data | Data created with Document Not Transferred to Contract Accounts is listed on the Not Transferred tab.Document listed on the Inconsistent tab means there are differences between the amounts on the SD billing document and the FI-CA documentDocument listed on the Completed tab means the SD billing document has been transferred to Contract Accounts Receivable and Payable. | Details of the SD Billing documents status are shown on the specific tab. |  |
| 5 | Export and Save | Choose Export to Spreedsheet.Save the document in your file path. Open it and check. | The file is saved to your local. |  |

## Appendix

### Process Integrations

If the following processes are enabled in your system, you can also test these business processes for the FICA/SD integration, Please make sure you use the FICA specific business partner master data accordingly for relevant SD scope item.

| Process | Business Partner | Note |
| --- | --- | --- |
| 1F1 - Debit Memo Processing | 33100021 |  |
| 1EZ - Credit Memo Processing | 33100021 |  |
| 2EQ - Sale of Services (2EQ) | 33100023 | Credit management is out of scope of 43Y in SAP S/4HANA Cloud Public Edition2008. |
| 2ET - Sales Order Processing for Non-Stock Material (2ET) | 3310002333100029 is for customer material record and POD (Proof-of-Delivery) | Credit management is out of scope of 43Y in SAP S/4HANA Cloud Public Edition2008. |
| 31Q - Sales Order Processing for Sales Kits (‏31Q‏) | 33100023 |  |
| BD3 - Sales Processing using Third-Party with Shipping Notification (BD3) | 33100021 |  |
| BD9 - Sell from Stock | 3310002333100028 is for material listing or exclusion33100029 is for customer material record and POD (Proof-of-Delivery) | Credit management is out of scope of 43Y in SAP S/4HANA Cloud Public Edition2008. |
| BDA - Free of Charge Delivery (BDA) | 33100021 |  |
| ‏BDK - Sales Processing Using Third-Party Without Shipping Notification (‏BDK‏) | 33100021 |  |
| ‏BDQ - Invoice Correction Process with Debit Memo (‏BDQ‏) | 33100021 |  |
| BKA - Free Goods Processing (‏BKA‏) | 33100021 |  |
| BKX - Sales Order Processing – SEPA Direct Debit Handling (BKX) | 33100120 | Please make sure scope item Sales Order Processing – SEPA Direct Debit Handling (BKX) has been activated , and you could use Terms of Payment - SEPA for the process. |
| BKJ - Sales Order Processing with Customer Down Payment (BKJ) | 33100024 | Please use Payment Lot function to post a down payment. For more details about the process of Payment Lot, you could refer to scope item - 2BI Contract Accounting – Customer Initiated Payments, step Process Payment Lot and Post Payment Lot.Note A scheduling job is provided to update down payment status of sales order based on down payment clearing situation in FI, and then remove the delivery block and billing block on sales orders. The job can be scheduled via Fiori tile Schedule Update of Down Payment Status - Sales Orders by the Internal Sales Representative. |
| BKL - Invoice Correction Process with Credit Memo (‏BKL‏) | 33100021 |  |

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
- see-also :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-cash-application-47i-ae-1001]]
- see-also :: [[08-sales-order-management/test-script-omnichannel-convergent-billing-1mc-ae-sap-s-4hana-cloud-pu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43Y_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 26,110 chars in the whole document
