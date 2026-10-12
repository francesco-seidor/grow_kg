---
id: 13-quality-ehs-and-compliance/test-script-supplier-compliance-in-the-value-chain-5oj-ae-1115
title: "Test Script: Supplier Compliance in the Value Chain (5OJ_AE) (5OJ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5OJ (AE) Supplier Compliance in the Value Chain: purchase order blocking by supplier assessment status."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/supplier-compliance]
aliases: [5OJ_S4CLD2608_BPD_EN_AE]
keywords: [Supplier Compliance in the Value Chain, supplier compliance, purchase order blocking, supplier assessment, product compliance, compliance check configuration, business roles, master data, posting periods, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OJ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1115
topic: 13-quality-ehs-and-compliance/supplier-compliance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Supplier Compliance in the Value Chain (5OJ_AE) (5OJ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OJ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Supplier Compliance in the Value Chain** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Supplier Compliance in the Value Chain (5OJ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232857500)

[2 Prerequisites 3](#_Toc232857501)

[2.1 System Access 3](#_Toc232857502)

[2.2 Roles 3](#_Toc232857503)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232857504)

[2.4 Business Conditions 5](#_Toc232857505)

[2.5 Preliminary Steps 5](#_Toc232857506)

[2.5.1 Open a New Materials Management (MM) Period 5](#_Toc232857507)

[2.5.2 Adapt Behavior of Compliance Checks in Value Chain 6](#_Toc232857508)

[3 Overview Table 8](#_Toc232857509)

[4 Test Procedures 9](#_Toc232857510)

[4.1 Assign Product and Supplier to the Compliance View and Request Supplier Assessment 9](#_Toc232857511)

[4.2 Create Purchase Order 10](#_Toc232857512)

[4.3 Assess Supplier Compliance and Review Supplier Check Status 12](#_Toc232857513)

## Purpose

Overview

This scope item supports a check that is carried out in purchasing documents. For each compliance-relevant product that is added to the purchasing document, the system checks the status of the supplier assessment. If the supplier of all items is compliant, the document can be processed. If the supplier isn't approved for an item, the item and the business transaction are blocked. For a blocked item, a compliance request for the product steward specialist is created to check the assessment of the supplier. If the compliance result of the assessment is positive, the block is released.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Business Role or Template) | ID | Description (Space) | ID | Log On |
| --- | --- | --- | --- | --- |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Master Data Specialist - Product Compliance | SAP_BR_MD_SPECIALIST_PCL | Master Data - Product Compliance | SAP_BR_MD_SPECIALIST_PCL |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_BR_PURCHASER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Compliance Purpose | Raw Material Default Compliance Purpose | The following compliance requirement is assigned:Supplier SDS provided | The compliance purpose is active. |
| Plant | 3310 | Plant 1 AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Material | RMPC06 | Material Number: RMPC06Material Description: Raw PMA 06Material Type: ROH | Compliance relevant in product master is set to Yes. |
| Supplier | 33300001 | Domestic Supplier 1 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNR | Create Product Master of Type “Raw Material” |
| BNE | Create Supplier Master |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting period is up to date. |
| J45 - Procurement of Direct Materials | You have implemented and tested scope item J45. |

### Preliminary Steps

In this section, you find the steps that you need to carry out before you start the procedures in this test script.

#### Open a New Materials Management (MM) Period

Use

The period must be set up at the beginning of each new posting period to ensure values and goods movement are posted to the correct period. Usually, only the current posting period is open for posting. All other posting periods are closed.

Procedure

Check the current posting period and open a new one, if needed, following the process step from the Create New Open MM Posting Period - MDS master data script for company code 1710.

|  |
| --- |
| Note You can find the BNZ master data script under [Your Master Data](https://support.sap.com/content/dam/SAAP/Sol_Pack/BP_CLD_ENTPR/BP_CLD_ENTPR_S4CLD2008_21_Master_Data_EN_XX.htm). |

#### Adapt Behavior of Compliance Checks in Value Chain

Use

Before you can start with the procedures in the test script, you have to carry out the following preliminary steps.

Procedure

In the Adapt Behavior of Compliance Checks in Value Chain activity, the configuration expert can specify how the supplier check behaves if the supplier assessment is still in progress. The configuration expert can specify whether the supplier check blocks a document in this case or not. Carry out the described steps to check the configuration.

Depending on your configuration environment, choose one of the following options:

Configure Your Solution

| Test Step | Test step name | Instruction | Expected Result | Pass / Fail/Comment |
| --- | --- | --- | --- | --- |
| 2 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 3 | Access the App | Open the Manage Your Solution (F1241) app. | The app opens and the Manage You Solution screen is displayed. |  |
| 4 | Go to Configure Your Solution | Choose Configure Your Solution | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 5 | Go to the Configuration Activity | Enter Adapt Behavior of Compliance Checks in Value Chain in the Search field and choose Enter.In the search result, select the configuration item.On the Configure Your Solution – Settings for the Integration screen, go to the configuration step Adapt Behavior of Compliance Checks in Value Chain and choose Configure. | The Adapt Behavior of Compliance Checks in Value Chain: Change screen is displayed. |  |
| 6 | Check Configuration Settings | Check if an entry with the following values is available:Issue: S_CONFIGIP (Supplier Assessment is in Progress)Origin: S_PUR (Purchasing)Result: S_BLK_CRQ (Blocked and request triggered)If the entry is not available, create one with the described settings. |  |  |

SAP Central Business Configuration

| Test Step | Test step name | Instruction | Expected Result | Pass / Fail/Comment |
| --- | --- | --- | --- | --- |
| 2 | Log On | Log on to SAP Central Business Configuration. |  |  |
| 3 | Open Active Flexible Workflow | From the Activities list on the left-hand side, navigate to the Configuration entry and search for the following activity: Adapt Behavior of Compliance Checks in Value Chain.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Adapt Behavior of Checks in Logistics Documents screen is displayed. |  |
| 4 | Check Configuration Settings | Check if an entry with the following values is available:Issue: S_CONFIGIP (Supplier Assessment is in Progress)Origin: S_PUR (Purchasing)Result: S_BLK_CRQ (Blocked and request triggered)If the entry is not available, create one with the described settings. | The Configure Your Solution - Product Compliance Configuration screen is displayed. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Assign Product and Supplier to the Compliance View and Request Supplier Assessment](#unique_11) [page ] 9 | Master Data Specialist - Product Compliance | Manage Basic Compliance Data - Raw Materials (F3024)Supplier Compliance for Raw Material (F3040) | The compliance view for a raw material exists and is assigned to a product master.The supplier is assigned to the product and the supplier compliance is set to Requested. |
| [Create Purchase Order](#unique_12) [page ] 10 | Purchaser | Manage Purchase Orders (F0842A) | The purchase order is created and the Product Compliance check status is Blocked – Decision Pending. |
| [Assess Supplier Compliance and Review Supplier Check Status](#unique_13) [page ] 12 | Product Stewardship Specialist - Product ComplianceMaster Data Specialist - Product CompliancePurchaser | Process Requests from Logistics (F3342)Manage Basic Compliance Data - Raw Materials (F3024)Supplier Compliance for Raw Material (F3040)Manage Purchase Orders (F0842A) | A compliance request is created for the blocked purchase order.The supplier compliance status is Approved.The compliance status for the supplier in the purchase order is OK – Approved. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Assign Product and Supplier to the Compliance View and Request Supplier Assessment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance checks if the compliance view for the raw material exists and assigns a product from the product master. The Master Data Specialist - Product Compliance also assigns a supplier to the compliance view and requests the assessment of the supplier compliance.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Raw Materials (F3024) app and search for Product Marketability RMC30-B. | The app opens and displays the raw material in the Raw Materials table. |  |
| 3 | Open a Raw Material | On the Manage Basic Compliance Data - Raw Materials screen, in the Raw Materials table, choose the row with the internal name Product Marketability RMC30-B. | The Raw Material - Basic Compliance Data screen is displayed. |  |
| 4 | Verify Compliance Purpose Assignments | In the Compliance Purposes section, verify the compliance purpose assignment. | The Raw Material Default Compliance Purpose must be assigned. |  |
| 5 | Check for Assigned Products | In the Related Products in Product Master table, check if material RMPC06 has already been assigned.If it is assigned, skip to step 8.If not, proceed with step 6. |  |  |
| 6 | Edit Raw Material | Choose Edit. | Product Marketability RMC30-B is editable. |  |
| 7 | Assign Related Product | In the Assigned Products section, in the Related Products in Product Master table, enter product RMPC06 in the Product field and choose Save. | Product RMPC06 is assigned to compliance view of the raw material. |  |
| 8 | Create Supplier Assignment | In the Suppliers section, choose Create. | The Assign Supplier dialog is displayed. |  |
| 9 | Add Supplier | In the Assign Supplier dialog, enter the following data, and then choose Save:Supplier: 33300001Responsible Unit: Permitted for all Responsible Units (S_ALL) | The supplier is displayed in the Suppliers table. |  |
| 10 | Verify Supplier Compliance | In the Suppliers table, choose the row of the supplier that you have assigned. | The Supplier Compliance for Raw Material (F3040) app opens and displays the supplier data for the raw material.The Compliance Data status is Missing and the Supplier Status for Raw Material status is In Progress. |  |
| 11 | Request Compliance Data from Supplier | On the Supplier Compliance for Raw Material screen, open the Set Compliance Data Status dropdown and choose Set to Requested. | The Compliance Data status has changed to Requested. The Supplier Status for Raw Material status stays In Progress. |  |

### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purchaser creates a purchase order for a raw material for which the assessment of the supplier compliance is still in progress. The system verifies the supplier compliance status and blocks the purchase order.

Note that the supplier check needs compliance data for the check and, therefore, does not support the use of one-time suppliers.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app and choose Create. | The app opens and displays the Purchase Order screen and the General Information tab. |  |
| 3 | Enter Supplier | In the General Information tab in the Basic Data section, enter the following data and then choose Enter :Supplier: 33300001 | The system fills the data for currency, purchasing group, purchasing organization, and company code. If the system does not fill in this data automatically, enter the following data manually:Currency: AEDPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310 |  |
| 4 | Create Purchase Order Item | Choose the Items tab and in the Items section, choose Create. | The Items table is displayed with a red line marking missing but required data. |  |
| 5 | Enter Purchase Order Item | Enter the following data:Material: RMPC06Order Quantity: 1Net Order Price: 1If the Plant field is not filled by the system, enter 3310. | The purchase order item is added and the red marking line turns into orange. |  |
| 6 | Process Purchase Order | Choose Order.Note the purchase order number: ________________.Note that you can only process the purchase order, when the color of the line of the purchase order item is orange or green. If the line is red, data is missing that you need to enter. | The screen changes to Purchase Order and shows the purchase order data in display mode. |  |
| 7 | View Supplier Check Status for the Document | Choose the Product Compliance tab and view the data of the compliance status in the header of the document. | The Product Compliance Supplier Check Status is Blocked – By Supplier. |  |
| 8 | View Supplier Check Status for the Item | Select the Items tab, navigate to the details of the item and, on the Product Compliance tab, view the data of the compliance status for the item. | The Product Compliance Supplier Check Status is Blocked – Decision Pending. |  |

### Assess Supplier Compliance and Review Supplier Check Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the purchase order is created and blocked, a compliance request is generated. The Product Stewardship Specialist - Product Compliance finds the created compliance request in the Process Requests from Logistics (F3342) app and checks the issue. Since the supplier assessment is missing, the Product Stewardship Specialist - Product Compliance informs the Master Data Specialist - Product Compliance to assess the compliance of the supplier.

The Master Data Specialist - Product Compliance approves the supplier.

The Purchaser checks the status of the purchasing order. The document is no longer blocked.

Procedure

Check Compliance Request

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Requests from Logistics (F3342) app. | The app opens showing lists of requests that are unprocessed, in progress, or closed. |  |
| 3 | Search for Request | In the Search field enter RMPC06 and choose Enter. | In the list on the Unprocessed tab, the request for product RMPC06 is displayed. |  |
| 4 | View Request Status in Compliance Request | Go to the Unprocessed tab and open the request for product RMPC06. | The Compliance Request from Logistics screen opens, displaying The supplier assessment is not complete. information message in the header of the request. |  |

Approve Supplier

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Raw Materials (F3024) app. | The app opens showing a list of raw materials. |  |
| 3 | Open Raw Material | Search for material RMPC06 and choose the row with this raw material to navigate to its details. | The Raw Material - Basic Compliance Data screen is displayed. |  |
| 4 | Open Supplier Compliance Data | In the Suppliers table, choose the row of the supplier that you have assigned. | The Supplier Compliance for Raw Material (F3040) app opens and displays the supplier data for the raw material. |  |
| 5 | Approve Supplier | On the Supplier Compliance for Raw Material screen, open the Set Supplier Status dropdown and choose Approve. | The Supplier Status for Raw Material is set to Approved. |  |

Check Status of Supplier Check in Purchase Order

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. In the Purchase Order field, enter the number of the purchase order that you have created in procedure [Create Purchase Order](#unique_12) [page ] 10 and choose Go. | You purchase order is displayed in the Purchase Order table. |  |
| 3 | Open Purchase Order | Choose the row with your purchase order in the Purchase Order table. | Your purchase order is displayed. |  |
| 4 | View Approved Supplier Compliance Status | On the Product Compliance tab, view the compliance status. | The Product Compliance Supplier Check Status has changed to OK - Approved. |  |

Search for Your Compliance Request

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Requests from Logistics (F3342) app. | The app opens showing lists of requests that are unprocessed, in progress, or closed. |  |
| 3 | Search for Request | In the Search field, enter RMPC06 and choose Enter. | The request for product RMPC06 is no longer displayed in the list on the Unprocessed tab. It is now displayed on the Closed tab. |  |

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
> Flagged while digesting this document, not verified: Posting period step references company code 1710 while sample data and PO use company code 3310 (AE)

## Connections
- part-of :: [[_cluster]]
- see-also :: [[13-quality-ehs-and-compliance/assess-dangerous-goods-for-a-product-3fc-ae-test-script-933]]
- see-also :: [[10-procurement/test-script-vendor-performance-consumer-products-6a6-ae-1154]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OJ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 26,342 chars in the whole document
