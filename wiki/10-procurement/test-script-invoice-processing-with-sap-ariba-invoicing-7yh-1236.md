---
id: 10-procurement/test-script-invoice-processing-with-sap-ariba-invoicing-7yh-1236
title: "Test Script: Invoice Processing with SAP Ariba Invoicing (7YH) (7YH_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 7YH: step-by-step tests for supplier invoice upload, posting, approval and import with SAP Ariba Invoicing and S/4HANA Cloud."
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-invoicing]
aliases: [7YH_S4CLD2608_BPD_EN_XX]
keywords: [Invoice Processing with SAP Ariba Invoicing, ariba invoicing, supplier invoices, invoice upload, invoices without purchase order, invoices with purchase order, invoice approval workflow, manual invoice processing, invoice posting, invoice import]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7YH_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1236
topic: 10-procurement/ariba-invoicing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Invoice Processing with SAP Ariba Invoicing (7YH) (7YH_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7YH_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Invoice Processing with SAP Ariba Invoicing** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Invoice Processing with SAP Ariba Invoicing (7YH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232792775)

[2 Prerequisites 4](#_Toc232792776)

[2.1 System Access 4](#_Toc232792777)

[2.2 Roles 4](#_Toc232792778)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232792779)

[2.4 Additional Manual Configuration 6](#_Toc232792780)

[2.5 Business Conditions 6](#_Toc232792781)

[2.6 Preliminary Steps 6](#_Toc232792782)

[2.6.1 Manage Data Restriction 6](#_Toc232792783)

[2.6.2 Manage Workflows for Supplier Invoice Approval 7](#_Toc232792784)

[3 Overview Table 8](#_Toc232792785)

[4 Test Procedures 10](#_Toc232792786)

[4.1 Process Invoices Without Reference to Purchase Orders 10](#_Toc232792787)

[4.1.1 Upload Supplier Invoices 10](#_Toc232792788)

[4.1.2 View Draft Invoices 13](#_Toc232792789)

[4.1.3 Automatic Invoice Posting to the Connected System 13](#_Toc232792790)

[4.1.4 Manual Invoice Processing in the Connected System: Extensive Edit (Optional) 14](#_Toc232792791)

[4.1.5 Manual Invoice Processing in the Connected System: Submit (Optional) 15](#_Toc232792792)

[4.2 Process Invoices With Reference to Purchase Orders 17](#_Toc232792793)

[4.2.1 Create Purchase Order in the Backend System 17](#_Toc232792794)

[4.2.2 Post Goods Receipt in the Backend System 18](#_Toc232792795)

[4.2.3 Import Purchasing Document 19](#_Toc232792796)

[4.2.4 Upload Supplier Invoices 20](#_Toc232792797)

[4.2.5 Post Supplier Invoices 23](#_Toc232792798)

[4.2.6 Approve Supplier Invoice (Optional) 24](#_Toc232792799)

[4.3 Import Supplier Invoices 25](#_Toc232792800)

[4.3.1 Import Supplier Invoices 25](#_Toc232792801)

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | SAP S/4HANA Cloud Public Edition |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK | SAP S/4HANA Cloud Public Edition |

You also need adequate role templates to access SAP Ariba Invoicing applications in SAP BTP Cockpit. The apps used in this test script are Manage Data Restrictions, Upload Supplier Invoices Centrally and Manage Supplier Invoices Centrally. Follow the links below to check if you have all the role templates required, and assign the missing ones if necessary.

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
| Supplier | 0010300001 | Inlandslieferant DE 1 |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/35deb0729a3717a3850451f3f8ad7463)

### Business Conditions

Scope item 7YH - Invoice Processing with SAP Ariba Invoicing currently does not require additional business condition.

### Preliminary Steps

#### Manage Data Restriction

Purpose

This process shows you how to grant permission to users for each company code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Invoicing Fiori Launchpad with a user with the role template BPC_EXPERT. | SAP Ariba Invoicing home page is displayed. |  |
| 2 | Access the App | Open Manage Data Restrictions. | The application is opened. |  |
| 3 | Grant Permission | On the Manage Data Restriction screen, go to All data restriction, choose Edit , and make sure Upload permission is checked.Choose Save.Caution If upload permission is not granted, you will not be able to upload an invoice in chapter [Upload Supplier Invoices](#unique_9) [page ] 10. | Upload permission is granted. |  |

#### Manage Workflows for Supplier Invoice Approval

Purpose

This process shows you how to create variant for workflows of supplier invoice approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba InvoicingFiori Launchpadwith a user with the role template BPC_EXPERT. | SAP Ariba Invoicing home page is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Supplier Invoice Approval. | The application isopened. |  |
| 3 | Grant Permission | On the Manage Workflows for Supplier Invoice Approval screen, choose Create Variant. On the Create Variant screen, enter below data, Choose Create.Name: Demo VariantChoose Add Start Condition on the section Start.Choose Select item, select Company Code from the list. Then choose select value and select Company code 1010as a sample. Choose Apply.Choose Approval. On the screen Approval, tab General, enter below data,Step Name: ApprovalChoose tab Step Configuration, enter below data,Agent Determination Rule: USERGROUPUser Group: Approval_Group1 (This needs be created in IAS)Step to be completed by: One of the recipientsChoose tab Step Condition, choose Open condition editor. On the Edit Step Condition screen, add below condition, choose Apply.Select item: Gross Amount in company code currencyIs equal to: is greater thanType or select item: 100Choose Save.Choose Back.Choose Deploy All. | Approval variant is created. A message Project deployed shows on the screen. |  |

## Overview Table

This scope item consists of process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Process Invoices Without Reference to Purchase Ordners

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Upload Supplier Invoices](#unique_9) [page ] 10 | Accounts Payable Accountant | Upload Supplier Invoices Centrally | A unique central invoice ID is generated and assigned to the respective invoice. |
| [View Draft Invoices](#unique_12) [page ] 13 | Accounts Payable Accountant | Manage Supplier Invoices Centrally | The invoice status is updated progressively. |
| [Automatic Invoice Posting to the Connected System](#unique_13) [page ] 13 | Accounts Payable Accountant | Manage Supplier Invoices Centrally |  |
| [Manual Invoice Processing in the Connected System: Extensive Edit (Optional)](#unique_14) [page ] 14 | Accounts Payable Accountant | Manage Supplier Invoices Centrally |  |
| [Manual Invoice Processing in the Connected System: Submit (Optional)](#unique_15) [page ] 15 | Accounts Payable Accountant | Manage Supplier Invoices Centrally |  |

Process Invoices With Reference to Purchase Ordners

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order in the Backend System](#unique_16) [page ] 17 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Post Goods Receipt in the Backend System](#unique_17) [page ] 18 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Import Purchasing Document](#unique_18) [page ] 19 | Accounts Payable Accountant | Schedule Import of Purchasing Data (F7619) |  |
| [Upload Supplier Invoices](#unique_19) [page ] 20 | Accounts Payable Accountant | Upload Supplier Invoices Centrally |  |
| [Post Supplier Invoices](#unique_20) [page ] 23 | Accounts Payable Accountant | Manage Supplier Invoices Centrally |  |

Import Supplier Invoices

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Import Supplier Invoices](#unique_21) [page ] 25 | Accounts Payable Accountant | Schedule Import of Supplier Invoices (F5349) |  |

## Test Procedures

### Process Invoices Without Reference to Purchase Orders

#### Upload Supplier Invoices

Purpose

This process step shows you how to upload invoice files in SAP Ariba Invoicing. After the Document Information Extraction service extracts information from the files you upload, the Configure Business Rules application will automatically set invoice tax and account information according to the business logic you customized in the decision tables.

After uploading, invoices will be submitted to the connected system. They will be directly saved to the connected system. If the save is not successful, you will need to implement manual adjustments.

Some errors may occur during the invoice upload. These errors must be fixed for the upload to complete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Go to SAP Ariba Invoicing that has an integrated interface with SAP Fiori Launchpad.Log into the system with a user that has the role template Accounts Payable Accountant. | SAP Ariba Invoicing is displayed. |  |
| 2 | Access the App | Open app Upload Supplier Invoices Centrally. | The Upload Supplier Invoices Centrally screen isdisplayed. |  |
| 3 | Maintain Data and Upload Files | On the Upload Supplier Invoices Centrally screen, enter the mandatory header data:Company Code: your company code, for example, 1010 Description: Any valueClick on the Select button and choose the file you want to upload from your computer.In order to test one automatic invoice processing scenario and two manual invoice processing scenarios, choose Invoice_Non_PO_Based_ReadyToSubmit. jpg once, and choose Invoice_Non_PO_Based_WithManualAdjustment. jpg twice. The following pictures are provided for your testing purposes.Figure 1: Invoice_Non_PO_Based_ReadyToSubmit. jpg<!-- image omitted: unnamed -->Figure 2: Invoice_Non_PO_Based_WithManualAdjustment. jpg<!-- image omitted: unnamed --> |  |  |
| 4 | Check Uploaded Invoices | Check uploaded invoices by clicking on the Go button on the left panel and refreshing the page.Note The files you upload must be of pdf, png or jpg format. The size of the file you upload must be no larger than 50 MB. | A unique central invoice ID is generated and assigned to each invoice. Please note down the central invoice ID for future use.The uploaded files will be displayed on the top of the list, as the default sorting order is Upload Date Descending. |  |

#### View Draft Invoices

Purpose

This process step shows you how to check the status of draft invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Invoicingwith a user with the role template Accounts Payable Accountant. | The SAP Ariba Invoicing home page displays. |  |
| 2 | Access the App | Open Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally screen isdisplayed. |  |
| 3 | View Draft Invoices | For field Status, choose Draft from the dropdown list, and choose Go.The newly uploaded draft invoices is displayed at the top of the search result.You can see that a unique central invoice ID is generated and assigned to each draft invoice. Note down the central invoice IDs for future use.Automatic invoice processing including document extraction service and business rules definition is triggered to save non-PO or PO based invoice. | The invoices will be processed in the following order. You can refresh the page by clicking onGo and check the latest status in the Process Step column.Invoice ReceivedDocument Information ExtractionSupplier DeterminationTax DeterminationWithholding Tax DeterminationAccount DeterminationTax Jurisdiction Code DeterminationSubmitting to Connected SystemManual Adjustment required |  |

#### Automatic Invoice Posting to the Connected System

Purpose

This process step shows you how to post invoices to the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Invoicingwith a user with the role template Accounts Payable Accountant. | The SAP Ariba Invoicing home page displays. |  |
| 2 | Access the App | Open app Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally screen isdisplayed. |  |
| 3 | Check Invoice Status | Search the invoice using the central invoice ID that is assigned to your document, for example Invoice_Non_PO_ReadyToSubmit.jpg. You will find that it has been submitted automatically. | The invoice status has changed to Parked and completed. |  |
| 4 | Check Detail Page | Navigate to the invoice details page by clicking the arrow >.The preview panel automatically opens on the right side of the screen, and displays the attachment. | The attachment is displayed. |  |
| 5 | Check Header Value | Under tab General Information, we can view information about invoice number, invoicing party name, process step, status, company code, gross amount, posting date, and invoice date in respective fields.The invoice is no longer editable anymore.Check the document number displayed at the top left corner. | For example, you will find information as the following:Invoice No: 5105604825\2021Invoicing Party: Berlin Baustoffee (10100001)Company Code: 1010 (1010)Gross Amount:119 EURInvoice Status:Parked and completedProcess Step:Manual Adjustment required |  |
| 6 | Open the Invoice | Open the supplier invoice directly in its connected system by clicking the Open Invoice button.The user can post invoice in the backend system by clicking Post.Once the invoice has been posted in the backend system of SAP S/4HANA Cloud Public Edition, click on the Back button to return to SAP Ariba Invoicing.Click the Refresh button. | The invoice status will be updated to Posted, and the status in column Process Step will be changed to Accepted. |  |

#### Manual Invoice Processing in the Connected System: Extensive Edit (Optional)

Purpose

This process step shows you how to use the extensive edit function in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Invoicingwith a user with the role template Accounts Payable Accountant. | SAP Ariba Invoicinghome page is displayed. |  |
| 2 | Access the App | Open the app Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally screen isdisplayed. |  |
| 3 | Open Invoice | Open the draft invoice generated from the file you uploaded in chapter #unique_9, for example Invoice_NonPO_WithManualAdjustment – 2.jpg. | An invoice is opened. |  |
| 4 | Check Error Message | The error message: Some mandatory information is missing. Complete all mandatory fields. displays. | The error message displays. |  |
| 5 | Update mandatory fields in the invoice | Fill the missing information in the mandatory field External Invoice Reference.External Invoice Reference: Any text value | The value for External Invoice Reference will be updated. |  |
| 6 | Choose Extensive Edit | Choose Extensive Edit. The extensive edit action parks the invoice and directly opens it in the connected system. You can continue editing the invoice in the connected system.Choose OK.Check in the connected system if the invoice is directly opened.Check if the invoice is editable. | The invoice status is changed to Parked. Message The invoice is saved. Invoice Number: XXXXX saved is displayed. The invoice is directly opened in the connected system. |  |
| 7 | Save and Compete Invoice Processing | Choose Save as Completed. | Message Documents have been saved as completed. Supplier invoice: XXXX displays is displayed. |  |

#### Manual Invoice Processing in the Connected System: Submit (Optional)

Purpose

This process step shows you how to submit an invoice in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Invoicingwith a user with the role template Accounts Payable Accountant. | SAP Ariba Invoicinghome page displays. |  |
| 2 | Access the App | Open Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally isdisplayed. |  |
| 3 | Open Invoice | Open the draft invoice generated from the file you uploaded in chapter #unique_9, for example, Invoice_NonPO_WithManualAdjustment – 1.jpg. | An invoice is opened. |  |
| 4 | Check the message | Check the error message: Some mandatory information is missing. Complete all mandatory fields. | An error message is displayed. |  |
| 5 | Update mandatory fields in the invoice | Fill in the missing data in the mandatory field External Invoice Reference.External Invoice Reference: Any text value | External invoice reference will be updated. |  |
| 6 | Save the invoice | Choose Save to save the changes you made in the draft invoice. The invoice is saved in SAP Ariba Invoicing database but not yet submitted to the connected system.You can still edit your draft invoice later by choose the Edit button on the invoice detail page. | External invoice reference is saved. |  |
| 7 | Submit Invoice | Choose Submit button.Check the message dialog. | The submission action saves the invoice as complete in the connected system.Message The invoice is saved. Invoice Number: XXXXXX displays. |  |
| 8 | Check Status | Choose OK.The invoice status has changed to Parked and completed.Once the submission is successful, the invoice can no longer be directly edited in SAP Ariba Invoicing anymore. | Message Documents have been saved as completed. Supplier invoice: XXXX displays. |  |
| 9 | Open Invoice in the Backend System | Choose Open Invoice. | The invoice is opened directly in the backend system SAP S/4HANA Cloud Public Edition.All information is transmitted to the backend system.The attachment is also visible in the backend system and is saved. |  |

### Process Invoices With Reference to Purchase Orders

#### Create Purchase Order in the Backend System

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data.On the General Information tab, make the following entries:Purchasing Doc. Type: Standard PO (NB)Supplier: 10300001Company Code: 1010Purchasing Organization: 1010Purchasing Group: 001Currency: EUROn the Delivery and Invoice tab, make the following entries and choose Enter:Payment Terms: 0003Go to Supplier Contact Data tab, the Supplier Address, Telephone, Fax, Contact Person are shown.On the Notes tab, choose > or < to search for Header Text. On the Header text column, enter the free text: xxx for testing.On the Items tab, from the Purchase Order Items screen, choose Create and make the following entries:Material: TG0011Plant: 1010Order Quantity: 5 PCNet Order Price: 10 EURNavigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.On the General Information tab, make the following entry:Storage Location: 101AFrom the Purchase Order Item section, choose Process Flow tab.The following entries display:Goods Receipt: yesInvoice Receipt: <selected>Verify Goods-Receipt-Based Invoice Verification is selected.On the tab Tax, check the following entries:Tax Code: <Default Value>Tax Date: <Default Value>On the Schedule Lines tab, make the following entry:Delivery date: <a date in the future> | The Purchase Order screen is displayed. |  |
| 5 | Verify Purchase Order for Completeness and Save Purchase Order | Choose Order to save the Purchase Order. | A new Purchase Order is created if no error is displayed in the dialog box. |  |

#### Post Goods Receipt in the Backend System

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the Purchase Order ID and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: xxxPrinting: Individual slip |  |  |
| 5 | Select Item | From the Items section, select the goods receipt item to be posted.Choose Storage Location (for example) 101A. | You can see that the Post button is activated. |  |
| 6 | Post | Choose Post. | The system displays the message Material Document xxx posted. |  |

#### Import Purchasing Document

Purpose

This process step shows you how to replicate purchase orders from backend SAP S4/HANA Cloud Public Edition system to SAP Ariba Invoicing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Invoicing with a user with the role template Accounts Payable Accountant. | SAP Ariba Invoicing home page displays. |  |
| 2 | Access the App | Open Schedule Import of Purchasing Data (F7619). |  |  |
| 3 | Create a new job | Choose Create.Enter below information in the New Schedule page.Name: Import PODescription: Import PO - Immediate RunConnected System: select the connected system from dropdown list.Recurrence Pattern: Single RunChoose Save. | A new job is created. |  |
| 4 | Show Log | Wait until the job Run Status is Successs.Choose the entry of the new job.Choose Show Logs.Go to the details. You can see the message The number of purchase orders imported for company code xxxx is xxxx. | Log details are displayed. |  |

#### Upload Supplier Invoices

Purpose

This process step shows you how to upload invoice files with reference purchase orders in SAP Ariba Invoicing. After the Document Information Extraction service extracts information from the files you upload, the Configure Business Rules application will automatically set invoice tax and account information according to the business logic you customized in the decision tables.

After uploading, invoices will be submitted to the connected system. They will be directly saved to the connected system. If the save is not successful, you will need to implement manual adjustments.

Some errors may occur during the invoice upload. These errors must be fixed for the upload to complete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Go to SAP Ariba Invoicing that has an integrated interface with SAP Fiori Launchpad.Log into the system with a user that has the role template Accounts Payable Accountant. | SAP Ariba Invoicing is displayed. |  |
| 2 | Access the App | Open app Upload Supplier Invoices Centrally. | The Upload Supplier Invoices Centrally screen isdisplayed. |  |
| 3 | Maintain Data and Upload Files | On the Upload Supplier Invoices Centrally screen, enter the mandatory header data:Company Code: your company code, for example, 1010Description: Any valueClick on the Select button and choose the file you want to upload from your computer.The following pictures are provided for your testing purposes.Figure 3: Invoices with reference to PO.png<!-- image omitted: unnamed -->Choose Start Upload button. |  |  |
| 4 | Check Uploaded Invoices | Check uploaded invoices by clicking on the Go button on the left panel and refreshing the page.Note Note The files you upload must be of pdf, png or jpg format.The size of the file you upload must be no larger than 50 MB. | A unique central invoice ID is generated and assigned to each invoice. Please note down the central invoice ID for future use.The uploaded files will be displayed on the top of the list, as the default sorting order is Upload Date Descending. |  |

#### Post Supplier Invoices

Purpose

This process step shows you how to post invoices to the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Invoicing with a user with the role template Accounts Payable Accountant. | The SAP Ariba Invoicing home page displays. |  |
| 2 | Access the App | Open app Manage Supplier Invoices Centrally. | The Manage Supplier Invoices Centrally screen is displayed. |  |
| 3 | Check Invoice Status | Search the invoice using the central invoice ID that is assigned to your document. You will find that it has been submitted automatically. | The invoices will be processed in the following order. You can refresh the page by clicking on Go and check the latest status in the Process Step column.Invoice ReceivedDocument Information ExtractionSupplier DeterminationTax DeterminationWithholding Tax DeterminationAccount DeterminationTax Jurisdiction Code DeterminationSubmitting to Connected SystemManual Adjustment requiredThe invoice status has changed to Parked and completed. |  |
| 4 | Check Detail Page | Navigate to the invoice details page by clicking the arrow >.The preview panel automatically opens on the right side of the screen, and displays the attachment. | The attachment is displayed. |  |
| 5 | Check Header Value | Under tab General Information, we can view information about invoice number, invoicing party name, process step, status, company code, gross amount, posting date, and invoice date in respective fields.The invoice is no longer editable anymore.Check the document number displayed at the top left corner. | For example, you will find information as the following:Invoice No: 5105604825\2021Invoicing Party: Berlin Baustoffee (10300001)Company Code: 1010 (1010)Gross Amount:10 EURInvoice Status:Parked and completedProcess Step:Manual Adjustment required |  |
| 6 | Open the Invoice | Open the supplier invoice directly in its connected system by clicking the Open Invoice button.The user can post invoice in the backend system by clicking Post.Once the invoice has been posted in the backend system of SAP S/4HANA Cloud Public Edition, click on the Back button to return to SAP Ariba Invoicing.Click the Refresh button. | The invoice status will be updated to Posted, and the status in column Process Step will be changed to Accepted. |  |

#### Approve Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a supplier invoice is approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant (One of the approver defined in chapter Manage Workflows for Supplier Invoice Approval). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Inbox. | The My Inbox screen is displayed. |  |
| 3 | Filter Supplier Invoice List | Fill the invoice number in search criteria fields. | The Approval of Invoice xxx is displayed. |  |
| 4 | Check Supplier Invoice Detail | In the list of the Supplier Invoices, select an Invoice Document by clicking the entire row, which is blocked for approval. | The invoice document is displayed. |  |
| 5 | Release the Invoice | Choose Approval. Enter a note in the Approve screen.Choose Approve. | The invoice is approved. |  |
| 6 | Back to SAP Fiori Launch Pad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

### Import Supplier Invoices

#### Import Supplier Invoices

Purpose

This process step shows you how to replicate supplier invoices from backend SAP S4/HANA Cloud Public Edition system to SAP Ariba Invoicing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Ariba Invoicing with a user with the role template Accounts Payable Accountant. | SAP Ariba Invoicing home page displays. |  |
| 2 | Access the App | Open Schedule Import of Supplier Invoices (F5349). |  |  |
| 3 | Create a new job | Choose Create.Enter below information in the New Schedule page.Name: Import InvoicesDescription: Import Invoices - Immediate RunConnected System: select the connected system from dropdown list.Recurrence Pattern: Single RunChoose Save. | A new job is created. |  |
| 4 | Show Log | Wait until the job is completed.Choose the entry of the new job.Choose Show Logs.Go to the details. You can see the message The import of invoices has ended. xxxx invoices were imported.. | Log details are displayed. |  |

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
- related-to :: [[10-procurement/test-script-invoice-processing-with-sap-ariba-invoicing-4n6-1038]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7YH_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 38,203 chars in the whole document
