---
id: 08-sales-order-management/test-script-omnichannel-convergent-billing-1mc-ae-sap-s-4hana-cloud-pu
title: "Test Script: Omnichannel Convergent Billing (1MC_AE) - SAP S/4HANA Cloud Public Edition (1MC_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 1MC: combining external and internal billable data into one invoice via EBDR."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/external-billing]
aliases: [1MC_S4CLD2608_BPD_EN_AE]
keywords: [External Billing Interface, omnichannel convergent billing, external billing document requests, billing document creation, combined invoices, excel upload, invoice lists, test scripts, professional services billing, sell from stock billing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MC_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-735
topic: 08-sales-order-management/external-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Omnichannel Convergent Billing (1MC_AE) - SAP S/4HANA Cloud Public Edition (1MC_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MC_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **External Billing Interface** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Omnichannel Convergent Billing (1MC_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847276)

[2 Prerequisites 3](#_Toc232847277)

[2.1 System Access 3](#_Toc232847278)

[2.2 Roles 3](#_Toc232847279)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232847280)

[2.4 Business Conditions 5](#_Toc232847281)

[2.5 Preliminary Steps 5](#_Toc232847282)

[2.5.1 Create Condition Records (Optional) 5](#_Toc232847283)

[3 Overview Table 6](#_Toc232847284)

[4 Test Procedures 7](#_Toc232847285)

[4.1 Create a Billing Document with External Data 7](#_Toc232847286)

[4.2 Create a Billing Document Combining External Billing Data and Data from Professional Services 9](#_Toc232847287)

[4.3 Create a Billing Document Combining External Billing Data and Data from Sell from Stock 10](#_Toc232847288)

[4.4 Create a Billing Document Combining External Data, Data from Sell from Stock and Data from Professional Services 12](#_Toc232847289)

[4.5 Create a Billing Document with External Data via Excel Upload (Optional) 15](#_Toc232847290)

[4.6 Create Invoice List (Optional) 17](#_Toc232847291)

## Purpose

Overview

This scope item for sales billing enables billable data sent from multiple channels (internal and external) to be combined into a single customer invoice.

After receiving billable data from external channels, the system carries it forward in the form of external billing document requests.

This scope item enables the creation of billing documents in the SAP S/4HANA Cloud Public Edition system by using billable data received from an external system, received from an external system and internal data from a sell-from-stock process, or received from an external system and internal data from project-based services. Billing documents can also be created by combining billable data received from an external system with data from a sell-from-stock process and a project-based services process, or using external data imported into the system from a spreadsheet file.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1MC_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011T001 | Trading Good 0011,PD,Regular Proc. Junior Consultant | Material which will be used in order to be provided to the customer |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the Make-to-Order Production with Variant Configuration (1YT) scope item. |
| Customer | 33100001 | Domestic UAE Customer 1 |  |
| Customer | 33100012 | Domestic Customer Invoice List |  |
| Payer | 33100014 | PAYER - Central |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Plant | 3310 | Plant 1 AE |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock orJ14 - Sales Order Processing – Project-Based Services orJ11 - Customer Project Management – Project-Based Services | Activation of these scope items must be run before the test script. |

### Preliminary Steps

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Name | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create a Billing Document with External Data](#unique_9) [page ] 7 | Billing Clerk | Test Billing Document Request API (EBDR_API_TEST) | The Billing Document Request displays. |
| [Create a Billing Document Combining External Billing Data and Data from Professional Services](#unique_10) [page ] 9 | Billing Clerk | Test Billing Document Request API (EBDR_API_TEST) | The Billing Document Request displays. |
| [Create a Billing Document Combining External Billing Data and Data from Sell from Stock](#unique_11) [page ] 10 | Billing Clerk | Test Billing Document Request API (EBDR_API_TEST) | The Billing Document Request displays. |
| [Create a Billing Document Combining External Data, Data from Sell from Stock and Data from Professional Services](#unique_12) [page ] 12 | Billing Clerk | Test Billing Document Request API (EBDR_API_TEST) | The Billing Document Request displays. |
| [Create a Billing Document with External Data via Excel Upload (Optional)](#unique_13) [page ] 15 | Billing Clerk | Manage Billing Document Requests (F2960) | The Manage Billing Document Requests displays. |
| [Create Invoice List (Optional)](#unique_14) [page ] 17 | Billing Clerk | Manage Invoice Lists (F2740) | The Invoice List is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Only chapter [Create a Billing Document with External Data](#unique_9) [page ] 7 and [Create a Billing Document Combining External Billing Data and Data from Professional Services](#unique_10) [page ] 9 can be tested by professional services standalone customer. |

|  |
| --- |
| Note For testing purposes a simulation tile is used to simulate the integration with the Hybris revenue cloud. This can be applied only in Q- systems. |

### Create a Billing Document with External Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a billing document of the type CBD1 with external billing data received in the external billing document request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Test Billing Document Request API (EBDR_API_TEST).Note Try to find the test App by searching for Apps on the home screen. Navigate to the App Finder and select the test app. Then you can pin it to a group such as your home group in the Fiori launchpad. | The Billing Document Request screendisplays. |  |
| 3 | Data for Creation EBDR via Business API | Make the following entries as sample:Preceding Document Type: EO01Preceding Doc. Item Category: ED01EBDR Type:BDR1Sales Organization: 3310Distribution Channel:10Division: 00Sold-To Party: 33100001Document Currency:AEDMaterial: TG0011Quantity: 10Sales Unit:Plant: 3310Departure Country:AE |  |  |
| 4 | Create EBDR Document | Choose Execute. | The EBDR is created. |  |
| 5 | Go back to Home Screen | Choose the Back arrow. | The Home screen displays. |  |
| 6 | Access the App | Open Create Billing Documents (F0798)(Billing Due List Items). | The Billing Due List screen displays. |  |
| 7 | Define Billing Setting | Choose Billing Settings in the bottom bar, you can make the following settings as below:Set billing date and enter before billing - OFFCreate separate billing document for each item of billing due list - OFFAutomatically Post Billing Documents - OFFDisplay Billing Document after creation - ONChoose delivery items to be billed and select quantities - OFF |  |  |
| 8 | Select the EBDR to be Invoiced | Select the External Billing Document Request you’ve created before and choose Create Billing Documents. | The draft billing document with ID TMPxxxxx will display. |  |
| 9 | Save Billing Document | On the Manage Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: _____. | The system generates an invoice for EBDR. |  |

### Create a Billing Document Combining External Billing Data and Data from Professional Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to combine billing data from the Professional Services process with external billing data received from Professional Services in an external billing document request into one billing document of type CI01.

Procedure

First you need to run the respective steps in J11: Create a Debit Memo Request. Furthermore you need to create an external billing document request receiving external billing data from the Professional Services process as described below. Then the two types of billing data are combined in one billing document.

Make sure that the header data of all preceding documents you want to combine later are in synch, for example, sold-to-party and sales organization.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Test Billing Document Request API (EBDR_API_TEST).Note Try to find the test App by searching for Apps on the home screen. Navigate to the App Finder and select the test app. Then you can pin it to a group such as your home group in the Fiori launchpad. | The Billing Document Request screen displays. |  |
| 3 | Data for Creation EBDR via Business API | Make the following entries as sample:Preceding Document Type: DMR1Preceding Doc. Item Category: PS03EBDR Type: BDR1Sales Organization: 3310Distribution Channel: 10Division: 00Sold-To Party: 33100001Document Currency: AEDMaterial: T001Quantity: 20Plant: 3310Departure Country: AE |  |  |
| 4 | Create EBDR Document | Choose Execute. | The EBDR is created. |  |
| 5 | Go back to Home Screen | Choose the Back arrow. | The Home screen displays. |  |
| 6 | Access the App | Open Create Billing Documents (F0798)(Billing Due List Items). | The Billing Due List screen displays. |  |
| 7 | Define Billing Setting | Choose Billing Settings in the bottom bar, you can make the following settings as below:Set billing date and enter before billing - ONCreate separate billing document for each item of billing due list - OFFAutomatically Post Billing Documents - OFFDisplay Billing Document after creation - ONChoose delivery items to be billed and select quantities - OFF |  |  |
| 8 | Select the EBDR & Data from Professional Services To Be Invoiced | Select the External Billing Document Request you’ve created before and Billing Document Request for Professional Service created from J11 or Manual Debit Memo Request created from J14 and choose Create. | The Create Billing Documents screen displays. |  |
| 9 | Maintain Billing Type and Date | Choose billing type Invoice (CI01) and maintain billing date, for example, <current date>. | The draft billing document with ID Sxxxxxxxx will display. |  |
| 10 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number. | The system generates an invoice. |  |

### Create a Billing Document Combining External Billing Data and Data from Sell from Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to combine external billing data received in an external billing document request from the Sell from Stock process and billing data from the Sell from Stock process into one billing document of type F2.

Procedure

First you need to run the respective steps to prepare a delivery, for example, in BD9: Create Sales, Create Delivery, Execute Picking, Post Goods Issue. Furthermore, you need to create an external billing document request receiving external billing data from the Sell from Stock process as described below.

Then the two types of billing data are combined in one billing document.

Make sure that the header data of all preceding documents you want to combine later are in synch, for example, sold-to-party and sales organization.

.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Test Billing Document Request API (EBDR_API_TEST).Note Try to find the test App by searching for Apps on the home screen. Navigate to the App Finder and select the test app. Then you can pin it to a group such as your home group in the Fiori launchpad. | The Billing Document Request screen displays. |  |
| 3 | Data for Creation EBDR via Business API | Make the following entries as sample:Preceding Document Type: ORPreceding Doc. Item Category: TANEBDR Type:BDR1Sales Organization: 3310Distribution Channel:10Division: 00Sold-To Party: 33100001Document Currency:AEDMaterial: TG0011Quantity: 10Plant: 3310Departure Country: AE |  |  |
| 4 | Create EBDR Document | Choose Execute. | The EBDR is created. |  |
| 5 | Go back to Home Screen | Choose the Back arrow. | The Home screen displays. |  |
| 6 | Access the App | Open Create Billing Documents (F0798)(Billing Due List Items). | The Billing Due List screen displays. |  |
| 7 | Define Billing Setting | Choose Billing Settings in the bottom bar, you can make the following settings as below:Set billing date and enter before billing - ONCreate separate billing document for each item of billing due list - OFFAutomatically Post Billing Documents - OFFDisplay Billing Document after creation - ONChoose delivery items to be billed and select quantities - OFF |  |  |
| 8 | Select the EBDR & Standard Order to be Invoiced | Select the External Billing Document Request you’ve created before combined with the Standard Order (Delivery) created from BD9 and choose Create. | The Create Billing Documents screen displays. |  |
| 9 | Maintain Billing Type and Date | Choose billing type Invoice (F2) and maintain billing date, for example, <current date>, then choose OK. | The draft billing document with ID Sxxxxxxxx will display. |  |
| 10 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: ______. | The system generates an invoice. |  |

### Create a Billing Document Combining External Data, Data from Sell from Stock and Data from Professional Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to combine external billing data received from any source and billing data from the Sell from Stock process and billing data from Professional Services into one billing document of type CBD2.

Procedure

First you need to run the respective steps, for example

In BD9, prepare a delivery: Create Sales, Create Delivery, Execute Picking, Post Goods Issue.

In 3NR, prepare a delivery: Create Sales Scheduling Agreement, Create Delivery, Execute Picking, Post Goods Issue.

In J11, create a billing document request: Create Billing Document Request

In J14, create a debit memo request: Create Manual Debit Memo Request

In BKJ, create sales order for non-stock material with billing plan: Create Sales Orders with Billing Plan.

In 4GT, create a solution order with a sales item, a service item, a service item of fixed price, a service contract item, a subscription item, a professional service project item. Release the solution order and complete the execution of the related follow up documents(scope items mentioned in 4GT) to prepare the following documents:

- a delivery
- a service confirmation billing document request
- a service order billing document request
- a service contract billing document request
- a subscription billing document request
- a project billing document request

|  |
| --- |
| Note You can refer to SAP note 3413050 for an example on how to create combined invoice of solution order document. |

Then you create an external billing document request to receive external billing data as described below. Then several types of billing data are combined in one billing document.

Make sure that the header data of all preceding documents you want to combine later are in synch, for example, sold-to-party and sales organization.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Test Billing Document Request API (EBDR_API_TEST).Note Try to find the test App by searching for Apps in the home screen. Navigate to the App Finder and select the test app. Then you can pin it to a group such as your home group in the Fiori Launchpad. | The Billing Document Request screen displays. |  |
| 3 | Data for Creation EBDR via Business API | Make the following entries as sample:Preceding Document Type: EO02Preceding Doc. Item Category: ED01EBDR Type: BDR1Sales Organization: 3310Distribution Channel:10Division: 00Sold-To Party: 33100001Document Currency:AEDMaterial: TG0011Quantity: 100Plant: 3310Departure Country: AE |  |  |
| 4 | Create EBDR Document | Choose Execute. | The EBDR is created. |  |
| 5 | Go back to Home Screen | Choose the Back arrow. | The Home screen displays. |  |
| 6 | Access the App | Open Create Billing Documents (F0798)(Billing Due List Items). | The Billing Due List screen displays. |  |
| 7 | Define Billing Setting | Choose Billing Settings in the bottom bar, you can make the following settings as below:Set billing date and enter before billing - ONCreate separate billing document for each item of billing due list - OFFAutomatically Post Billing Documents - OFFDisplay Billing Document after creation - ONChoose delivery items to be billed and select quantities - OFF |  |  |
| 8 | Select the EBDR & Standard Order & Data from Professional Services to be Invoiced | Select the External Billing Document Request you’ve created before combined with the Standard Order (Delivery) created from BD9 and the Billing Document Request for Professional Service created from J11 or Manual Debit Memo Request created from J14. Choose Create. | The Create Billing Documents screen displays. |  |
| 9 | Maintain Billing Type and Date | Choose billing type Invoice (CBD2) and maintain billing date, for example, <current date>, then choose OK. | The draft billing document with ID Sxxxxxxxx will displays. |  |
| 10 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number : ______ | The system generates an invoice. |  |

### Create a Billing Document with External Data via Excel Upload (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

It’s possible to transfer external billing document requests from a source to a target system via excel upload. This process step shows you how to download an empty excel template and then fill in your data in SAP S/4HANA Cloud Public Edition system. After you upload the excel sheet then the external billing document requests are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Document Requests (F2960). | The Manage Billing Document Requests screen displays. |  |
| 3 | Create Billing Document Requests | Choose Create. | The Create Billing Document Requests screen displays. |  |
| 4 | Download Excel Template | Choose Download Excel Template. | The excel template has been downloaded. |  |
| 5 | Fill in Data for EBDRs Creation via Uploaded Excel Template | Manually enter billing data that you want to bill in your SAP S/4HANA Cloud Public Edition based on the downloaded excel template in previous step.Note For test purposes, the following fields in the template are always mandatory. You won't be able to create an EBDR unless they’re all filled correctly.In the downloaded excel template, make the following entries in each sheet as sample:In worksheet IS_EBDR_ADMIN which holds basic administrative information.SENDERLOGICALSYSTEM: REV_SYSTEMIn worksheet IT_EBDR_REQUEST which holds the core EBDR data.BILLINGDATE: 20180101DEPARTURECOUNTRY: AEDISTRIBUTIONCHANNEL: 10DIVISION: 00EXTBILLINGDOCREQUESTTYPE: BDR1MATERIAL: TG0011PLANT: 3310PRECEDINGDOCUMENT: 1708310901PRECEDINGDOCUMENTITEM: 10PRECEDINGDOCUMENTITEMCATEGORY: ED01PRECEDINGDOCUMENTTYPE:: EO01QUANTITY: 10SALESORGANIZATION: 3310SOLDTOPARTY: 33100001TRANSACTIONCURRENCY: AED |  |  |
| 6 | Upload External Billing Document Requests into SAP S/4HANA Cloud Public Edition | Choose Upload from Excel.In the Choose a file to Open dialog box, choose Import from native file system and select the file to upload.In the Choose a file to open dialog box, select the file and confirm with Choose. |  |  |
| 7 | Create EBDR Document | Choose Create. | The EBDR is created. |  |
| 8 | Go back to Home Screen | Choose the Back arrow. | The Home screen displays. |  |
| 9 | Access the App | Open Create Billing Documents (F0798)(Billing Due List Items). | The Billing Due List Items screen displays. |  |
| 10 | Define Billing Setting | Choose Billing Settings at the bottom bar, you can make the following settings as below:Set billing date and enter before billing - OFFCreate separate billing document for each item of billing due list - OFFAutomatically post billing documents - OFFDisplay billing documents after creation - ONChoose delivery items to be billed and select quantities - OFF |  |  |
| 11 | Select the EBDR to be Invoiced | Select the External Billing Document Request you’ve created before and choose Create. | The draft billing document with ID Sxxxxxxxx will displays. |  |
| 12 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number:________ . | The system generates an invoice for EBDR. |  |

### Create Invoice List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

It’s possible to create invoice list to Omnichannel Convergent Billing type CBD1, CBD2 and CBC1 (cancellation type). This process step shows you how to create invoice list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Fiori Launchpad tile | Open the Fiori launchpad as an Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). | The Manage Invoice Lists screen is displayed. |  |
| 3 | Navigate to Edit Worklist for Invoice Lists Screen | Choose Create. | The Edit Worklist for Invoice Lists screen displays. |  |
| 4 | Search Billing Documents | Make the following data in section Customer Data and choose Display Worklist for Invoice Lists:Payer: 33100014 | Billing documents displays in the result. |  |
| 5 | Select item(s) for Invoice List | Select the rows of Billing documents created previously and choose Collective Billing Document. | The system generates an invoice list for billing. |  |
| 6 | Check Invoice List Document | On the Edit Worklist for Invoice Lists screen, choose Log Display. And then choose Documents. Make a note of the invoice list document number in Document column: __________. | Invoice list document number displays. |  |

|  |
| --- |
| Note To create invoice list, “Automatically post billing documents – ON” needs to be set by choosing Billing Settings at the bottom bar when creating billing document in previous steps. Please refer to test script BKZ Sales Order Processing with Invoice List and Collective Billing (BKZ_DE) for more details on creating invoice list. CBC1 cancellation type will have invoice list created when corresponding billing document is cancelled after invoice list created. |

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
> Flagged while digesting this document, not verified: Invoice List note says 'Automatically post billing documents - ON' must be set in the earlier billing steps, but the Billing Settings in all preceding test procedures (4.1-4.5) specify 'Automatically Post Billing Documents - OFF'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/external-billing-1z6-ae-test-script-792]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MC_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 34,545 chars in the whole document
