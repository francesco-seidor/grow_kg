---
id: 08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-complaint-handling-7bg-12
title: Test Script SAP S/4HANA Cloud Public Edition - Complaint Handling (7BG) (7BG_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 7BG Complaint Handling (2608): create, submit, approve customer complaints, follow-up documents, document flow, pricing, partners, PDF output."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/complaint-handling]
aliases: [7BG_S4CLD2608_BPD_EN_XX]
keywords: [Customer Complaint Handling, complaint handling, customer complaints, complaint approval, complaint with invoice reference, follow-up documents, document flow, pricing authorizations, business partner functions, return order output]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7BG_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1207
topic: 08-sales-order-management/complaint-handling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Complaint Handling (7BG) (7BG_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7BG_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Customer Complaint Handling** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Complaint Handling (7BG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232841835)

[2 Prerequisites 4](#_Toc232841836)

[2.1 System Access 4](#_Toc232841837)

[2.2 Roles 4](#_Toc232841838)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232841839)

[2.4 Additional Manual Configuration (Set-up Instructions Guide) 6](#_Toc232841840)

[3 Overview Table 7](#_Toc232841841)

[4 Test Procedures 8](#_Toc232841842)

[4.1 Manage Customer Complaint 8](#_Toc232841843)

[4.1.1 Create and Submit Customer Complaint Without Reference 8](#_Toc232841844)

[4.1.2 Approve Customer Complaint Without Reference 9](#_Toc232841845)

[4.1.3 Create and Submit Customer Complaint with Reference to an Invoice 10](#_Toc232841846)

[4.1.4 Approve Customer Complaint With Reference 11](#_Toc232841847)

[4.1.5 Create Follow Up Documents 12](#_Toc232841848)

[4.1.6 Display Document Flow 13](#_Toc232841849)

[4.1.7 Display Pricing Information 13](#_Toc232841850)

[4.1.8 Display Business Partner Functions 14](#_Toc232841851)

[4.1.9 Display PDF Output Documents for Return Order 14](#_Toc232841852)

## Purpose

Overview

The SAP Complaint Handling solution helps companies to manage complaints holistically. It provides a transparent view of complaints and follow-up activities to increase customer satisfaction and unlock additional supplier recovery potential.

SAP Complaint Handling is a product on SAP Business Technology Platform for managing complaints. SAP Complaint Handling provides complete view of tracking and resolving complaints that are raised because of defective items.

Until now, all aspects of customer complaints - Quality, Finance, or Logistics are handled separately and not linked to each other. This leads to the following issues:

- Effort to track various aspects of complaints separately
- Inconsistent data
- No dependency among different aspects of complaints

SAP Complaint Handling provides end-to-end process guidance, cross-module process integration via microservice, and flexible process design. The Complaint Handling cockpit enables customers to configure and manage the complaint process in one place. This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

With this application, you can manage complaints related to supplier and customer grievances at one place.

Manage Supplier Complaints

Use this app to:

- Manage complaints related to supplier complaint.
- View statuses across multiple streams and business objects.
- Monitor new Quality Notification created in the backend system and automatically create a complaint to the corresponding quality notification.
- Track changes to the quality notification in the backend system and update the complaint accordingly.

You can also create complaint manually in SAP Complaint Handling cockpit and associate the business objects according to the defects in the complaint. For example, if a defect is critical or recurring, the user can request 8D report. In this scenario, Supplier 8D business object is relevant and required to resolve the complaint. If the defect is not critical, the user can choose to mark 8D as irrelevant. It is mandatory to create quality notification before creating other business objects.

You can capture cost involved in managing defective materials or labor hours to create claims. For more information, see [Manage Supplier Complaints](https://help.sap.com/docs/SAP_CMH/30c2f2d0e84a4242a06dc97386d84f43/c1831dfc84cf4a47a69473a57a5b04a2.html).

Manage Customer Complaints

Use this app to manage customer complaints for ordered items and trigger the required follow-up activities. You can:

- Create a customer complaint with reference or without reference document.
- Create an individual complaint.
- Create a multi-item complaint.
- Search an existing customer complaint.
- View and edit an existing customer complaint.
- Perform header actions, such as Approve, Reject, or Send for Rework.
- Perform follow-up actions, such as create customer return.
- View customer return document in PDF format.

For more information, see [Manage Customer Complaints](https://help.sap.com/docs/SAP_CMH/30c2f2d0e84a4242a06dc97386d84f43/bb50ba809d1e4b1aab0e8ea209d3b7b1.html).

Configure Supplier Complaints

Use this app to configure entities to manage supplier complaints. You can create, view, edit, and deactivate or reactivate configuration entries as required. For more information, see[Configure Supplier Complaints](https://help.sap.com/docs/SAP_CMH/30c2f2d0e84a4242a06dc97386d84f43/e462cf8b9de946b98325a3d20a84b101.html).

Configure Customer Complaints

Use this app to configure entities to manage customer complaints. You can create, view, edit, and deactivate or reactivate configuration entries as required. For more information, see [Configure Customer Complaints](https://help.sap.com/docs/SAP_CMH/30c2f2d0e84a4242a06dc97386d84f43/1826a4d24b83446ab9af4d1883b88384.html).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test should be conducted with the following system:

|  |
| --- |
| Note For system details contact your System Administrator. |

Table 1:

| System | Details |
| --- | --- |
| SAP S/4HANA System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role.The S/4HANA system must be configured in SAP BTP Cockpit as a destination. |
| SAP BTP Cockpit | Your System administrator provides you with URL and login details. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

You can also use the following space templates that determine the SAP Fiori launchpad layout for a business role. With the space template, you create a space with pages containing predefined apps and assign it to the business role. You then assign this business role to your individual users. For more information, refer to [How to Create a Business Role for a Key User](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/8fa28e0107984d42a99b9eea67856cea.html?version=2408.500) in the product assistance for SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note These roles or spaces are examples provided by SAP. You can use them as templates to create your own roles or spaces.For more information about business roles, refer to Assigning business roles to a user in the [Administration Guide to Implementation of SAP S/4HANA with SAP Best Practices](https://help.sap.com/docs/SAP_Best_Practices/4cef93946a0b48ec89533b3c34443b85/17d958a88d244ee293aed687f9bfe37f.html).Not Required for SAP Complaint Handling as only SAP BTP delivered Roles will be used for testing the solution. |

Table 2:

| Name (Role) | ID (Role) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Claims Analyst - Complaints Management (CMH) | SAP_BR_CMH_CLAIM_ANALYST |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Description |
| --- | --- | --- |
| Material | TG_CMH | Trading Good for Reg. Trading (MRP planning) |
| Plant | 1010 | Plant 1 DE |
| Ship-To Party | 1000000 | Domestic DE Customer 3 |
| Sold-to Party | 1000000 | Domestic DE Customer 3 |
| Storage Location | 101A | Std. storage 1 |
| Company Code | 1010 | Company Code 1010 |
| Sales Organization | 1010 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |

|  |
| --- |
| Note To start with complaint’s creation with reference to an invoice, create a sales order, deliver it, and finally create an invoice for this sales order. To do so, make sure to follow the steps mentioned below:Maintain the pricing condition record using transaction VK11, if pricing is not determined for the material in the sales order.Maintain the stock using transcation MIGO, if sales order availability is not confirmed, then go to MIGO, Select Others and enter material, quantity, plant with 501 Movement Type and so on. Post the material document for stock creation.You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .Table 3: Master Data Script ReferenceMDSDescriptionBKPCustomer Returns |

### Additional Manual Configuration (Set-up Instructions Guide)

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/a78a9bdcaa0a6f51b753cefa215b284b)

## Overview Table

This process starts with the creation of a customer complaints.

Table 4:

| Process Step | BTP Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create and submit customer complaint without reference | Complaint Approver | Manage Customer Complaint | Complaint is created |
| Approve customer complaint without reference | Complaint Approver | Manage Customer Complaint | Customer complaint is approved |
| Create and submit customer complaint with reference to an invoice | Complaint Approver | Manage Customer Complaint | Complaint is created |
| Approve customer complaint with reference | Complaint Approver | Manage Customer Complaint | Customer complaint is approved |
| Create follow-up documents | Complaint Approver | Manage Customer Complaint | All follow-up documents are created |
| Display document flow | Complaint Approver | Manage Customer Complaint | Complaint’s document flow with follow ups are displayed as the process flow API is called |
| Display pricing information | Configuration Admin | Configure Customer Complaint | Pricing detail is displayed |
| Display business partner information | Complaint Approver | Manage Customer Complaint | Business Partner function is displayed |
| Display PDF output documents for return order and return delivery | Complaint Print Management Clerk | Print Documents for Customer Complaints | PDF is displayed |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Customer Complaint

#### Create and Submit Customer Complaint Without Reference

Purpose

The purpose of this step is to create the customer complaint without reference and to verify the details.

Procedure

Table 5:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log On to CMH Launchpad.Enter the Tenant IDP.Click on Sign in. | CMH home page is displayed. |  |
| 2 | Navigate to Manage Customer Complaints | Choose the Manage Customer Complaints tile. | Manage Customer Complaints page is displayed. |  |
| 3 | Create Customer Complaint | Choose Create. | The Create Customer Complaint pop up is displayed. |  |
| 4 | Enter Customer Complaint Details | Enter the following details on the pop up screen:Sales Org: Example, 1010Distribution Channel: Example, 10Division: Example, 00Complaint Type, Example, T4_IN_CRRTItem Category , Example, T4_IN_02Choose Create. | The new customer complaint page is opened. |  |
| 5 | Enter Customer Complaint Details | Enter the following details on the new customer complaint screen:Sold-to Party, example,as maintained in master data tableShip-to Party, example, as maintained in master data tableMaterial, Example – TG_CMHComplaint Quantity, Example – 10Adjustment Value, Example – 10Follow up Scenario, Example - 0001Choose Create. | The customer complaint is created. |  |
| 5 | Find and display customer complaint | Choose Manage Customer Complaint > Complaint NumberIn the search area, enter the customer complaint in the filter field.Click Go.Choose the relevant complaint from search result. | The complaint will be displayed in the search result. |  |
| 6 | Check complaint header details | Check the following complaint header details at the top:Complaint NumberLifecycle Status –Open (OPN)Sold-to PartyShip-to PartyGeneral Information > Processing Status – Created (CRTD) | All the details are available in complaint. |  |
| 7 | Submit customer complaint | In the header, click on the Submit button to submit the customer complaint.Details like Pricing, Business Partner tab can be viewed. | Customer complaint is submitted.Net Value is present in Pricing tab.Document Flow is updated.Partner details are visible in Business Partner tab. |  |

#### Approve Customer Complaint Without Reference

Purpose

The purpose of this step is to approve the customer complaint created in the step above and to verify the details.

Procedure

Table 6:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role complaint approver. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Customer Complaints | Choose Complaint Number filter. | Customer Complaint is displayed in the list page. |  |
| 3 | Approve Customer Com-plaint | In customer complaint page, click the Approve button | Customer Complaint is approved and the Lifecycle Status is changed to Released (RELD) and Processing Status is updated to Approved (APP).Net Value is present in Pricing tab.Document Flow is updated.Partner details are visible in Business Partner tab. |  |

#### Create and Submit Customer Complaint with Reference to an Invoice

Purpose

The purpose of this step is to create the customer complaint without reference and to verify the details.

Procedure

Table 7:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com-ment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log On to CMH Launchpad.Enter the Tenant IDP.Click on Sign in. | CMH home page is displayed. |  |
| 2 | Navigate to Manage Customer Complaints | Choose the Manage Customer Complaints tile. | Manage Customer Complaints page is displayed. |  |
| 3 | Create Customer Complaint | Choose Create. | The Create Customer Complaint pop up is displayed. |  |
| 4 | Enter Customer Complaint Details | Enter the following details on the pop up screen:Sales Org: Example, 1010Distribution Channel: Example, 10Division: Example , 01Complaint Type: Example, ICItem Category: Example, DMGReference Document, Example – 90000014Reference Document Item, example - 10Choose Create. | The new customer complaint page is opened. |  |
| 5 | Enter Customer Complaint Details | Enter the following details on the new customer complaint screen:Sold-to Party, Example -as mentioned in master data tableShip-to Party, Example – as mentioned in master data tableMaterial, Example – TG_CMHComplaint Quantity, Example – 10Adjustment Value, Example – 10Follow up scenario, Example - 0001Choose Create. | The customer complaint is created. |  |
| 5 | Find and display customer complaint | Choose Manage Customer Complaint > Complaint NumberIn the search area, enter the customer complaint in the filter field.Click Go.Choose the relevant the complaint from search result. | The complaint is displayed in the search result. |  |
| 6 | Check complaint header details | Check the following complaint header details at the top:Complaint NumberLifecycle Status – Open (OPN)Sold-to PartyShip-to PartyGeneral Information > Processing Status – Created (CRTD) | All the details are available in complaint. |  |
| 7 | Submit customer complaint | In the header, click on the Submit button to submit the customer complaint.Details like Pricing, Business Partner tab can be viewed. | Customer complaint is submitted. |  |

#### Approve Customer Complaint With Reference

Purpose

The purpose of this step is to approve the customer complaint created in above step and to verify the details.

Procedure

Table 8:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role complaint approver. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Customer Complaints | Choose Complaint Number filter.Enter the complaint number created in the step above and click Go. | Customer Complaint is displayed in the list page. |  |
| 3 | Submit Customer Complaint | In customer complaint page, click the Submit button. | Customer Complaint is submitted and the processing status is updated to Submitted (SUBM). |  |

#### Create Follow Up Documents

Purpose

The purpose of this step is to create the follow up documents that get generated in the S/4 HANA system.

Procedure

Table 9:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Subscription Launchpad.Enter the custom IDP.Click on Sign in | Subscription Home page is displayed. |  |
| 2 | Open Customer Complaint | Choose Customer Complaint list page. | The list of available complaint is displayed. |  |
| 3 | Search for Customer Complaint | Enter the following search criteria:Customer Complaint: Complaint Number | The Customer Complaint is displayed. |  |
| 4 | View the Customer Complaint | In the Customer Complaint screen, the following details can be viewed:Lifecycle Status: OpenProcessing Status: Submitted | The basic details on the Customer Complaint are displayed. |  |
| 5 | Check follow up actions | Go to Follow Up Actions to view the details of the follow up list items:Create Customer Return | All follow up actions are displayed. |  |
| 6 | Click to create the follow up actions | Create Customer Return | Follow up action’s status changes from In Process to Created. |  |

#### Display Document Flow

Purpose

The purpose of this step is to verify the document flow.

Procedure

Table 10:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role complaint approver. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Customer Complaints | Choose Complaint Number filter. | Customer Complaint is displayed in the list page. |  |
| 3 | Open Customer Complaint | In customer complaint page, click the Document Flow tab. | All documents are displayed. |  |

#### Display Pricing Information

Purpose

The purpose of this step is to verify the pricing condition.

Procedure

Table 11:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Configuration Admin. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Configure Customer Complaints app | Choose Pricing Authorizations. | Pricing Authorizations are displayed in the list page. |  |
| 3 | Open the destination | In pricing authorization, all pricing procedure items are visible. Select the Complaint Approver checkbox for pricing procedure, as required. | Pricing information based on the condition maintained is displayed. |  |

#### Display Business Partner Functions

Purpose

The purpose of this step is to verify the business partner functions maintained in Partner Function configuration.

Procedure

Table 12:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role complaint approver. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Customer Complaints | Choose Complaint Number filter. | Customer Complaint is displayed in the list page. |  |
| 3 | Open Customer Complaint | In customer complaint page, click the Business Partner tab. | The system displays Partner Function information based on the configuration maintained. |  |

#### Display PDF Output Documents for Return Order

Purpose

This process step displays the output type pdfs for return order and return delivery.

Prerequisite

A follow up document return order has been created.

Procedure

Table 13:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Print Management Clerk. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Print Documents for customer complaint. | The Print Documents for Customer Complaint screen is displayed. |  |
| 3 | Search the Customer return created earlier. | Enter <the document number recorded in Create return order step> in the Complaint Number filter.Choose Go. | The return order is displayed. |  |
| 4 | Display Output PDF | On the Action, click View Document Button. | The output type PDF screen is displayed. |  |
| 5 | Display Print Preview | Select the output line and choose view document. | Print preview for PDF file is displayed. |  |

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
> Flagged while digesting this document, not verified: Approve-with-reference procedure only clicks Submit (status SUBM) rather than Approve, unlike the without-reference approval; Overview Table roles (Complaint Approver, Configuration Admin) differ from the single role listed in Roles (SAP_BR_CMH_CLAIM_ANALYST)

## Connections
- part-of :: [[_cluster]]
- see-also :: [[04-tax-and-statutory-reporting/test-script-invoice-correction-process-with-debit-memo-bdq-ae-1257]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7BG_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 26,583 chars in the whole document
