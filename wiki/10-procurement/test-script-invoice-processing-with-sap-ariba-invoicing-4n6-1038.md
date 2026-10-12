---
id: 10-procurement/test-script-invoice-processing-with-sap-ariba-invoicing-4n6-1038
title: "Test Script: Invoice Processing with SAP Ariba Invoicing (4N6) (4N6_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 4N6: upload, view, auto-post and manually process supplier invoices via SAP Ariba Invoicing."
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-invoicing]
aliases: [4N6_S4CLD2608_BPD_EN_XX]
keywords: [Invoice Processing with SAP Ariba Invoicing, supplier invoice upload, ariba invoicing, draft invoices, automatic invoice posting, manual invoice processing, extensive edit, data restrictions, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4N6_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1038
topic: 10-procurement/ariba-invoicing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Invoice Processing with SAP Ariba Invoicing (4N6) (4N6_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4N6_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Invoice Processing with SAP Ariba Invoicing** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Invoice Processing with SAP Ariba Invoicing (4N6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232835544)

[2 Prerequisites 3](#_Toc232835545)

[2.1 System Access 3](#_Toc232835546)

[2.2 Roles 3](#_Toc232835547)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232835548)

[2.4 Additional Manual Configuration 4](#_Toc232835549)

[2.5 Business Conditions 4](#_Toc232835550)

[2.6 Preliminary Steps 5](#_Toc232835551)

[2.6.1 Manage Data Restriction 5](#_Toc232835552)

[3 Overview Table 6](#_Toc232835553)

[4 Test Procedures 7](#_Toc232835554)

[4.1 Upload Supplier Invoices 7](#_Toc232835555)

[4.2 View Draft Invoices 11](#_Toc232835556)

[4.3 Automatic Invoice Posting to the Connected System 11](#_Toc232835557)

[4.4 Manual Invoice Processing in the Connected System: Submit (Optional) 12](#_Toc232835558)

[4.5 Manual Invoice Processing in the Connected System: Extensive Edit (Optional) 14](#_Toc232835559)

## Purpose

Overview

SAP Ariba Invoicing on SAP Business Technology Platform (SAP BTP) provides a unified solution for receiving and managing supplier invoices with connection to multiple systems, such as SAP S/4HANA Cloud Public Edition systems. This business solution contains applications to help you import supplier invoices with precise parameters and manage them in a unified interface. SAP Ariba Invoicing supports the display of invoice attachments in a split screen, as well as a seamless navigation to SAP Fiori apps for invoices or SAP GUI transactions from connected systems. It also provides various options to authorize specific invoice access to different user groups. The SAP Ariba Invoicing, inbound processing module provides embedded invoice inbound processing services, including OCR. This additional module allows users to upload invoice files, edit draft invoices, and save supplier invoices directly to the connected backend system.

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

Assign the following role templates to your user in SAP S/4HANA Cloud Public Edition:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | System |
| --- | --- | --- | --- | --- |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | SAP S/4HANA Cloud Public Edition |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT | SAP S/4HANA Cloud Public Edition |

You also need adequate role templates to access SAP Ariba Central Invoice Management applications in SAP BTP Cockpit. The apps used in this test script are Manage Data Restrictions, Upload Supplier Invoices Centrally and Manage Supplier Invoices Centrally. Follow the links below to check if you have all the role templates required, and assign the missing ones if necessary.

[Assigning Administrator Roles to Yourself or to the Administrator](https://help.sap.com/docs/CENTRAL_INVOICE_MANAGEMENT/7648a91c50d84e38ace80037f82fefae/837749155c9947b59ed4e8e246cfa288.html).

[Assigning User Roles to Your Users in SAP BTP Cockpit](https://help.sap.com/docs/CENTRAL_INVOICE_MANAGEMENT/7648a91c50d84e38ace80037f82fefae/3ab17c636a6b4bd5a83f158a5de493a0.html)

### Master Data, Organizational Data, and Other Data

The master data and organizational data needed is based on these data set up at SAP S/4HANA Cloud Public Edition system.

Regarding SAP S/4HANA Cloud Public Edition, the organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents products, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1010 | Company Code 1010 |  |
| Supplier | 0010300082 | Bunte Farben |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/087fb328f4d8fbd07d002b951028e42d)

### Business Conditions

Scope item 4N6 - Invoice Processing with SAP Ariba Invoicing currently does not require additional business condition.

### Preliminary Steps

#### Manage Data Restriction

Purpose

This process shows you how to grant permission to users for each company code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Central Invoice Management Fiori Launchpad with a user with the role template BPC_EXPERT. | SAP Ariba Central Invoice Management home page is displayed. |  |
| 2 | Access the App | Open Manage Data Restrictions. | The application is opened. |  |
| 3 | Grant Permission | On the Manage Data Restriction screen, go to All data restriction, choose Edit , and make sure Upload permission is checked.Choose Save.Caution If upload permission is not granted, you will not be able to upload an invoice in chapter [Upload Supplier Invoices](#unique_9) [page ] 7. | Upload permission is granted. |  |

## Overview Table

This scope item consists of process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Upload Supplier Invoices](#unique_9) [page ] 7 | Accounts Payable Accountant | Upload Supplier Invoices Centrally | A unique central invoice ID is generated and assigned to the respective invoice. |
| [View Draft Invoices](#unique_11) [page ] 11 | Accounts Payable Accountant | Manage Supplier Invoices Centrally | The invoice status is updated progressively. |
| [Automatic Invoice Posting to the Connected System](#unique_12) [page ] 11 | Accounts Payable Accountant | Manage Supplier Invoices Centrally |  |
| [Manual Invoice Processing in the Connected System: Submit (Optional)](#unique_13) [page ] 12 | Accounts Payable Accountant | Manage Supplier Invoices Centrally |  |
| [Manual Invoice Processing in the Connected System: Extensive Edit (Optional)](#unique_14) [page ] 14 | Accounts Payable Accountant | Manage Supplier Invoices Centrally |  |

## Test Procedures

### Upload Supplier Invoices

Purpose

This process step shows you how to upload invoice files in SAP Ariba Central Invoice Management. After the Document Information Extraction service extracts information from the files you upload, the Configure Business Rules application will automatically set invoice tax and account information according to the business logic you customized in the decision tables.

After uploading, invoices will be submitted to the connected system. They will be directly saved to the connected system. If the save is not successful, you will need to implement manual adjustments.

Some errors may occur during the invoice upload. These errors must be fixed for the upload to complete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Go to SAP Ariba Central Invoice Management that has an integrated interface with SAP Fiori Launchpad.Log into the system with a user that has the role template Accounts Payable Accountant. | SAP Ariba Central Invoice Management is displayed. |  |
| 2 | Access the App | Open app Upload Supplier Invoices Centrally. | The Upload Supplier Invoices Centrally screen is displayed. |  |
| 3 | Maintain Data and Upload Files | On the Upload Supplier Invoices Centrally screen, enter the mandatory header data:Company Code: your company code, for example, 1010Description: Any valueClick on the Select button and choose the file you want to upload from your computer.In order to test one automatic invoice processing scenario and two manual invoice processing scenarios, choose Invoice_Non_PO_Based_ReadyToSubmit. jpg once, and choose Invoice_Non_PO_Based_WithManualAdjustment. jpg twice. The below pictures are provided for your testing purposes.Invoice_Non_PO_Based_ReadyToSubmit. jpg*<!-- image omitted: unnamed -->*Invoice_Non_PO_Based_WithManualAdjustment. jpg*<!-- image omitted: unnamed -->*Choose Start Upload button. |  |  |
| 4 | Check Uploaded Invoices | Check uploaded invoices by clicking on the Go button on the left panel and refreshing the page.Note The files you upload must be of pdf, png or jpg format.The size of the file you upload must be no larger than 50 MB. | A unique central invoice ID is generated and assigned to each invoice. Please note down the central invoice ID for future use.The uploaded files will be displayed on the top of the list, as the default sorting order is Upload Date Descending. |  |

### View Draft Invoices

Purpose

This process step shows you how to check the status of draft invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Central Invoice Management with a user with the role template Accounts Payable Accountant. | The SAP Ariba Central Invoice Management home page displays. |  |
| 2 | Access the App | Open Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally screen is displayed. |  |
| 3 | View Draft Invoices | For field Status, choose Draft from the dropdown list, and choose Go.The newly uploaded draft invoices is displayed at the top of the search result.You can see that a unique central invoice ID is generated and assigned to each draft invoice. Note down the central invoice IDs for future use.Automatic invoice processing including document extraction service and business rules definition is triggered to save non-PO or PO based invoice. | The invoices will be processed in the following order. You can refresh the page by clicking on Go and check the latest status in the Process Step column.ReceivedDocument Information ExtractionTax DeterminationAccount DeterminationTax Jurisdiction Code DeterminationSubmitting to Connected SystemManual Adjustment Required |  |

### Automatic Invoice Posting to the Connected System

Purpose

This process step shows you how to post invoices to the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Central Invoice Management with a user with the role template Accounts Payable Accountant. | The SAP Ariba Central Invoice Management home page displays. |  |
| 2 | Access the App | Open app Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally screen is displayed. |  |
| 3 | Check Invoice Status | Search the invoice using the central invoice ID that is assigned to your document, for example Invoice_Non_PO_ReadyToSubmit.jpg. You will find that it has been submitted automatically. | The invoice status has changed to Parked and completed. |  |
| 4 | Check Detail Page | Navigate to the invoice details page by clicking the arrow >.The preview panel automatically opens on the right side of the screen, and displays the attachment. | The attachment is displayed. |  |
| 5 | Check Header Value | Under tab General Information, we can view information about invoice number, invoicing party name, process step, status, company code, gross amount, posting date, and invoice date in respective fields.The invoice is no longer editable anymore.Check the document number displayed at the top left corner. | For example, you will find information as the following:Invoice No: 5105604825\2021Invoicing Party: Berlin Baustoffee (10100001)Company Code: 1010 (1010)Gross Amount: 119 EURInvoice Status: Parked and completedProcess Step: Manual Adjustment required |  |
| 6 | Open the Invoice | Open the supplier invoice directly in its connected system by clicking the Open Invoice button.The user can post invoice in the backend system by clicking Post.Once the invoice has been posted in the backend system of SAP S/4HANA Cloud Public Edition, click on the Back button to return to SAP Ariba Central Invoice Management.Click the Refresh button. | The invoice status will be updated to Posted, and the status in column Process Step will be changed to Accepted. |  |

### Manual Invoice Processing in the Connected System: Submit (Optional)

Purpose

This process step shows you how to submit an invoice in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Central Invoice Management with a user with the role template Accounts Payable Accountant. | SAP Ariba Central Invoice Management home page displays. |  |
| 2 | Access the App | Open Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally is displayed. |  |
| 3 | Open Invoice | Open the draft invoice generated from the file you uploaded in chapter [Upload Supplier Invoices](#unique_9) [page ] 7, for example, Invoice_NonPO_WithManualAdjustment – 1.jpg. | An invoice is opened. |  |
| 4 | Check the message | Check the error message: Some mandatory information is missing. Complete all mandatory fields. | An error message is displayed. |  |
| 5 | Update mandatory fields in the invoice | Fill in the missing data in the mandatory field External Invoice Reference.External Invoice Reference: Any text value | External invoice reference will be updated. |  |
| 6 | Save the invoice | Choose Save to save the changes you made in the draft invoice. The invoice is saved in SAP Ariba Central Invoice Management database but not yet submitted to the connected system.You can still edit your draft invoice later by choose the Edit button on the invoice detail page. | External invoice reference is saved. |  |
| 6 | Submit Invoice | Choose Submit button.Check the message dialog. | The submission action saves the invoice as complete in the connected system.Message The invoice is saved. Invoice Number: XXXXXX displays. |  |
| 7 | Check Status | Choose OK.The invoice status has changed to Parked and completed.Once the submission is successful, the invoice can no longer be directly edited in SAP Ariba Central Invoice Management anymore. | Message Documents have been saved as completed. Supplier invoice: XXXX displays. |  |
| 8 | Open Invoice in the Backend System | Choose Open Invoice. | The invoice is opened directly in the backend system SAP S/4HANA Cloud Public Edition.All information is transmitted to the backend system.The attachment is also visible in the backend system and is saved. |  |

### Manual Invoice Processing in the Connected System: Extensive Edit (Optional)

Purpose

This process step shows you how to use the extensive edit function in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Central Invoice Management with a user with the role template Accounts Payable Accountant. | SAP Ariba Central Invoice Management home page is displayed. |  |
| 2 | Access the App | Open the app Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally screen is displayed. |  |
| 3 | Open Invoice | Open the draft invoice generated from the file you uploaded in chapter [Upload Supplier Invoices](#unique_9) [page ] 7, for example Invoice_NonPO_WithManualAdjustment – 2.jpg. | An invoice is opened. |  |
| 4 | Check Error Message | The error message: Some mandatory information is missing. Complete all mandatory fields. displays. | The error message displays. |  |
| 5 | Update mandatory fields in the invoice | Fill the missing information in the mandatory field External Invoice Reference.External Invoice Reference: Any text value | The value for External Invoice Reference will be updated. |  |
| 6 | Choose Extensive Edit | Choose Extensive Edit. The extensive edit action parks the invoice and directly opens it in the connected system. You can continue editing the invoice in the connected system.Choose OK.Check in the connected system if the invoice is directly opened.Check if the invoice is editable. | The invoice status is changed to Parked. Message The invoice is saved. Invoice Number: XXXXX saved is displayed. The invoice is directly opened in the connected system. |  |
| 7 | Save and Compete Invoice Processing | Choose Save as Completed. | Message Documents have been saved as completed. Supplier invoice: XXXX displays is displayed. |  |

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
- related-to :: [[10-procurement/test-script-invoice-processing-with-sap-ariba-invoicing-7yh-1236]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4N6_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 23,275 chars in the whole document
