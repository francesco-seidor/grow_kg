---
id: 08-sales-order-management/test-script-create-sales-orders-from-unstructured-data-4x9-ae-sap-s-4h
title: "Test Script: Create Sales Orders from Unstructured Data (4X9_AE) - SAP S/4HANA Cloud Public Edition (4X9_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4X9 (AE): creating sales orders by automatic extraction from PDF purchase orders, with optional setup steps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-order-automation]
aliases: [4X9_S4CLD2608_BPD_EN_AE]
keywords: [Sales Order Automation and Creation from Unstructured Data, sales order creation, automatic data extraction, sales order requests, custom logic, situation handling, ship-to party, duplicate check, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X9_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1057
topic: 08-sales-order-management/sales-order-automation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Create Sales Orders from Unstructured Data (4X9_AE) - SAP S/4HANA Cloud Public Edition (4X9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Order Automation and Creation from Unstructured Data** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Create Sales Orders from Unstructured Data (4X9_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Create Sales Orders from Unstructured Data (4X9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855109)

[2 Prerequisites 4](#_Toc232855110)

[2.1 System Access 4](#_Toc232855111)

[2.2 Roles 4](#_Toc232855112)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232855113)

[2.4 Additional Manual Configuration 6](#_Toc232855114)

[2.5 Business Conditions 6](#_Toc232855115)

[3 Preliminary Steps 8](#_Toc232855116)

[3.1 Creating Custom Logic for Data Proposal (Optional) 8](#_Toc232855117)

[3.2 Enable Situation Handling in Sales Order Request Processing (Optional) 9](#_Toc232855118)

[3.3 Set Ship-to Party as Required for Creating Sales Orders (Optional) 10](#_Toc232855119)

[3.4 Enable Duplicate Check for Uploaded Files (Optional) 11](#_Toc232855120)

[4 Overview Table 14](#_Toc232855121)

[5 Test Procedures 15](#_Toc232855122)

[5.1 Create Sales Orders by Automatic Extraction from a PDF File 15](#_Toc232855123)

[6 Appendix 19](#_Toc232855124)

[6.1 Process Integration 19](#_Toc232855125)

[6.1.1 Process Integration 19](#_Toc232855126)

## Purpose

Overview

You can use the Create Sales Orders – Automated Extraction app automatically creates sales orders. It extracts relevant data from unstructured source formats, such as PDF files, and translates it into sales orders.

Check SAP Note 3126670 for a list of supported languages: https://launchpad.support.sap.com/#/notes/3126670

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch | See Business Conditions and Preliminary Steps sections .Use TG11 to test customer material, recorded with customer 33100009. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No serial number, no batch | See Business Conditions and Preliminary Steps sections. |
| Material | TG20 | Trad.Good 12,Reorder Point,Reg.Trad. | Only use if you have activated Serial Number Managment (BLL). |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP) building block.See Business Conditions and Preliminary Steps sections. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP) building block.See Business Conditions and Preliminary Steps sections. |
| Sold-to Party | 331000033310000533100008331000093310000833100009 | Domestic UAE Customer 3Domestic UAE Customer 5 | You can test the scope item using another domestic customer.33100005 is for credit management.33100008 is for material listing or exclusion33100009 is for customer material record and POD (Proof-of-Delivery) |
| Ship-to Party | 33100003331000053310000833100009 | Domestic UAE Customer 3Domestic UAE Customer 5 |  |
| Company Code | 3310 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/11a06bc3894327e86e9524eebef52ba5)

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this test script, the materials must be available in stock. If you use trading goods (HAWA), you can either:Run through the Procurement of Direct Materials(J45) process,Or create stock using Post Goods Movement app (for details see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS(BNZ) master data script. Posting Period is up to date. |
| 31N - Situation Handling | The scope item should be activated if you want to execuate of Manage Situation Type |

## Preliminary Steps

### Creating Custom Logic for Data Proposal (Optional)

Purpose

The system starts data extraction and proposal for a sales order request immediately after a purchase order file is uploaded. You can implement custom proposal rules for sales order request fields in any of the following situations:

- The SAP-predelivered proposal rules cannot satisfy your needs.
- Data proposal results are not satisfactory.

|  |
| --- |
| Note Before creating custom logic, we recommend that you evaluate SAP-predelivered proposal rules and how the rules actually work for specific sales order requests. |

- For SAP-predelivered proposal rules, see [Create Sales Orders - Automatic Extraction](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/2dcf49a616b842b096e0a3cad4dac458.html?state=latest) on SAP Help Portal.
- To check data proposal details about a sales order request, you can display its application log in the app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Custom Logic (F6957). | The Custom Fields and Logic screen displays. |  |
| 3 | Navigate to Custom Logic | In the menu bar at the top, choose Custom Logic. | The Enhancement Implementations section displays. |  |
| 5 | Create Enhancement Implementation | Choose Create.Make the following entries and choose Create:Business Context: Sales: Sales Order RequestDescription: Sales Order Request custom logicImplementation Description: for example, Set sales area for sales requestImplementation ID: Generated by default | The Draft Logic section displays. |  |
| 6 | Add Logic | For example, in your custom logic, 1010/10/00 is proposed for the sales area if a sales order request is created by a particular user. |  |  |
| 7 | Save and Publish | Choose Save Draft.Choose Publish. | Custom logic is published. |  |

### Enable Situation Handling in Sales Order Request Processing (Optional)

Purpose

You can enable automatic notifications to sales personnel about sales order requests that require manual processing, based on the following situation templates:

Procedure

|  |
| --- |
| Note Please make sure scope item 31N - Situation Handling is activated if you want to execute this step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) | The Manage Situation Types screen displays. |  |
| 3 | Choose situation template | Choose one of the following situation templates, and choose Copy:SD_SOR_EXTRACTION_FAILED (Data Not Extracted for Order Creation)SD_SOR_MD_DETERMINE_INCMPLT (Data Incomplete for Order Creation) | The New Situation Types screen displays. |  |
| 4 | Input ID and name | In the tab of Admin Information, make the following settings:Specify an ID and name for the situation type, for example: Z_SOR_Extraction_FailedLeave the default settings for conditions, situation display, and recipients as they are, or adjust the settings as needed.Choose Create.Choose Yes to enable the situation type. | The New situation type is created and enabled. |  |
| 5 | Enable the other situation template | Choose Back, and choose the other situation template and repeat step 4 to enable it. | The situation type is created and enabled |  |

### Set Ship-to Party as Required for Creating Sales Orders (Optional)

Purpose

By default, the ship-to party is not required for creating sales orders. After you set the ship-to party as required, you cannot proceed to create sales orders from sales order requests without the ship-to party.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Open Configuration Item for : Automatic Sales Order Creation Based on Extracted Data | Enter the following filters:Application Area: SalesSub-Application Area: Sales Order Management and ProcessingIn the items table, select the item with item name:Automatic Sales Order Creation Based on Extracted Data (SSCUI ID: 104787) | The Configure Your Solution - Automatic Sales Order Creation Based on Extracted Data screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Adapt Settings by Company Code configuration steps. | The screen of "Adapt Settings by Company Code": Change appears. |  |
| 6 | Create Entries | Choose New Entries and Make the following settings:Company Code: 3310Ship-to Party Mandatory: CheckedChoose Save. | The settings are added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Sales Order Creation Based on Extracted Data | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Adapt Settings by Company Code or SSCUI ID 104787. |  |  |
| 3 | Create Entries | Choose New Entries and Make the following settings:Company Code: 3310Ship-to Party Mandatory: CheckedChoose Save. | The settings are added. |  |

### Enable Duplicate Check for Uploaded Files (Optional)

Purpose

After you enable duplicate check for uploaded files, an error appears if you upload the same file twice.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Open Configuration Item for : Automatic Sales Order Creation Based on Extracted Data | Enter the following filters:Application Area: SalesSub-Application Area: Sales Order Management and ProcessingIn the items table, select the item with item name: Automatic Sales Order Creation Based on Extracted Data (SSCUI ID: 104787) | The Configure Your Solution - Automatic Sales Order Creation Based on Extracted Data screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Adapt Settings by Company Code configuration steps. | The screen of "Adapt Settings by Company Code": Change appears. |  |
| 6 | Create Entries | Choose New Entries and make the following settings:Company Code: 3310Duplicate Check by File: EnabledChoose Save. | The settings are added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Sales Order Creation Based on Extracted Data | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Adapt Settings by Company Code or SSCUI ID 104787. |  |  |
| 3 | Create Entries | Choose New Entries and make the following settings:Company Code: 3310Duplicate Check by File: EnabledChoose Save. | The settings are added. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Orders by Automatic Extraction from a PDF File](#unique_13) [page ] 15 | Internal Sales Representative | Create Sales Orders - Automatic Extraction (F4920) | Sales orders are created. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as: apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

1. Log on to the SAP Fiori launchpad as a respective user, for example, Internal Sales Representative.
2. Access the Enterprise Search Bar by choosing the magnifying glass icon in the upper right corner.
3. The Enterprise Search bar displays two filter fields next to the search icon: all dropdown menu and a search field. Enter your Search Criteria and choose the business object type, for example, select Sales orders from the dropdown menu, and enter a sales order number in the search field and choose Search, the sales order lists.
4. Choose the sales order number link. The system navigates to the fact sheet screen and sales order related information is integrated and summarized in one Fiori page. You can get detailed data by choosing the corresponding links.

There are fact sheets available for the following objects (visible depending on the assigned role):

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Create Sales Orders by Automatic Extraction from a PDF File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order by automatic extraction from a purchase order PDF by machine learning.

|  |
| --- |
| Note If you encounter extraction accuracy issues, please contact SAP (component SD-SLS-IMP-DOX) for assistance and attach your test/sample files. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - Automatic Extraction (F4920) . | The Create Sales Orders- Automatic Extraction screen displays |  |
| 3 | Upload PDF Files for Pur-chase Order | Choose Upload File. On the Pop-up screen, make following inputFor example, Sales Organization: 3310Choose Browse to search for the PDF file of Purchase Order and choose Open.Choose Upload.Note If duplicate check has been enabled (as procedure describs in set-up instruction), an error appears when you upload the same file twice. | A sales order request is created |  |
| 4 | Check Processing Status | Choose Go to get the data refresh till system generate following data:Data Extraction: ExtractedData Completeness: CompleteIf data extraction failed, you can choose Retry Extraction incase data extraction failedNote If sales order request Data is complete please process step 8If sales order request data is incomplete, you need to manually edit the sales order request.Please process the step 5 to step 7If situation handling has been enabled in preliminary step, you will receive automatic notifications on the SAP Fiori launchpad when the data extraction fails or the sales order request is incomplete. | File data has been extracted and sales order request data is complete. |  |
| 5 | Check for Missing or Inaccurate Data | Choose the sales order request in the list.Choose Edit.Check your sales order request for missing or inaccurate data.Note If the ship-to party has been configured as mandatory （as procedure describs in set-up instruction） the ship-to party is highlighted as a required field if the ship-to party is missing. | Error messages about missing fields display. |  |
| 6 | Open Original File | Choose View File.Verify purchasing details alongside the sales order request data. | An embedded file view is open, with extracted values highlighted. |  |
| 7 | Edit Sales Order Request | Provide the missing data or rectify the inaccurate data.Choose Save. | The sales order request is complete. |  |
| 8 | Check Data | Choose the sales order request in the list.Choose Simulation Creation .Check the Order Simulation status.Note If the simulation result contains errors, revise the sales order request based on messages before you create a sales order. | The simulation result is successful. |  |
| 9 | Create Sales Order | Choose Create Sales Order. | Sales order is created. |  |
| 10 | Enhance Data Proposal for Sold-to Party, Ship-to party, and Product (Optional) | Repeat steps 1 to step 9 to create sales orders based on PDF files from the same customer.Note To know more about data proposal with reference to order creation history, see [Create Sales Orders - Automatic Extraction](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/2dcf49a616b842b096e0a3cad4dac458.html?state=latest) on SAP Help Portal. | Sales orders are created.As more sales orders are created for the same customer, the system can better propose the sold-to party, ship-to party, and product with reference to order creation history. |  |
| 11 | Enhance Data Proposal Using Custom Logic (Optional) | Identify fields with unsatisfactory proposal results.Note To check data proposal details about a sales order request, you can display its application log.You can update custom data proposal rules for these fields as preliminary step: Creating Custom Logic for Data Proposal (Optional)For an introduction to the custom logic, see [App Extensibility: Custom Proposal for Sales Order Request Fields (BAdI)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/ba5ac61b180e4ef39baf9654827734e5.html?state=latest) on SAP Help Portal. | After you upload PDF files, the system performs data proposal as indicated in your custom logic. |  |
| 12 | Ask SAP for Help (Optional) | If you are not satisfied with current extraction results or encounter extraction issues, please contact SAP (component SD-SLS-IMP-DOX) for assistance and attach your sample/test files. | Data extraction quality is enhanced and your sales order creation process goes more smoothly. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Process Integration

After completing the activities in this test script, you can continue testing the following business processes:

Table 2:

| Process | Business Condition |
| --- | --- |
| Sell from Stock(BD9) | Process a sales order, delivery, billing and so on.Using the master data from this document, complete all the activities described in the test script of the scope item. |
| Sales Order Fulfillment Monitoring and Operations (Optional) | This scope item describes the collection of periodic activities, such as day ending activities or legal requirements.Using the master data from this document, complete all the activities described in the Test Script of the scope item: Sales Order Fulfillment Monitoring (BKK) (Chapters Review Sales Documents blocked for billing , Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents). |

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
- related-to :: [[08-sales-order-management/sales-order-automation-73p-ae-test-script-1203]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,709 chars in the whole document
