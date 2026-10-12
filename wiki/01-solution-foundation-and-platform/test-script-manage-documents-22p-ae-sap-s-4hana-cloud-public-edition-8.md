---
id: 01-solution-foundation-and-platform/test-script-manage-documents-22p-ae-sap-s-4hana-cloud-public-edition-8
title: "Test Script: Manage Documents (22P_AE) - SAP S/4HANA Cloud Public Edition (22P_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 22P_AE: managing Document Info Records (search, create, version, classify, release, download) as Design Engineer."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/document-and-attachment-management]
aliases: [22P_S4CLD2608_BPD_EN_AE]
keywords: [Document Info Records and Attachment Services, document management, document info records, document versions, document attachments, document search, object links, classification metadata, document release, document types configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22P_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-801
topic: 01-solution-foundation-and-platform/document-and-attachment-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Manage Documents (22P_AE) - SAP S/4HANA Cloud Public Edition (22P_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22P_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Document Info Records and Attachment Services** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Manage Documents (22P_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232848948)

[2 Prerequisites 3](#_Toc232848949)

[2.1 System Access 3](#_Toc232848950)

[2.2 Roles 3](#_Toc232848951)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232848952)

[2.4 Preliminary Steps 4](#_Toc232848953)

[2.4.1 Create Characteristic 4](#_Toc232848954)

[2.4.2 Create Class 4](#_Toc232848955)

[2.4.3 Configure Document Types (Optional) 5](#_Toc232848956)

[3 Overview Table 7](#_Toc232848957)

[4 Test Procedures 8](#_Toc232848958)

[4.1 Search for Document 8](#_Toc232848959)

[4.2 Create New Document 9](#_Toc232848960)

[4.3 Create a New Version of the Document 10](#_Toc232848961)

[4.4 (Optional) Assign Object Link Metadata 11](#_Toc232848962)

[4.5 (Optional) Maintain Attachments 12](#_Toc232848963)

[4.6 (Optional) Maintain Classification Metadata 13](#_Toc232848964)

[4.7 Release Document 14](#_Toc232848965)

[4.8 Download Attachments 15](#_Toc232848966)

## Purpose

Overview

During the product engineering phase, new products are designed and developed. You design new products or product lines to take advantage of current process technology and to improve quality and reliability. Alternately, you change an existing product due to changing market or customer requirements. The result of this product phase is drawings and specifications that must be maintained through the documents created in the Document Management System. This scope item allows for creation of a Document Info Record (DIR), and the addition and maintenance of metadata and attachments to the DIR.

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
| Design EngineerCreates and manages the lifecycle of a Document Info Record. | SAP_BR_DESIGN_ENGINEER | Document Management | SAP_BR_DESIGN_ENGINEER |  |

### Master Data, Organizational Data, and Other Data

Master Data is not applicable for the test script. In this test script document type AUT has been used as an example. Other test scenarios can make use of this generic scenario with a different document type as needed in that test script. Document status value will be dependent on the document type used.

### Preliminary Steps

#### Create Characteristic

Purpose

In this step, you create the characteristic PRODUCT_TYPE to assign a classification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad appears. |  |
| 2 | Access the app | Open the Manage Characteristics (CT04) app. | The Characteristics screen displays. |  |
| 3 | Create new characteristic | Make the following entry and choose the Create icon:Characteristic: PRODUCT_TYPE | The Create Characteristic screen displays. |  |
| 4 | Enter basic data | On the Basic data tab, make the following entries.Basic data section:Description: Product TypeStatus: Released (default)Format section:Data Type: Character FormatNumber of Chars: 30Value assignment section:Select the Single Value radio button. |  |  |
| 5 | Save the characteristic | Choose Save. | The characteristic is created. |  |

#### Create Class

Purpose

In this process step, you create a class with the class type – 017.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Classes (CL02) app. | The Class screen displays. |  |
| 3 | Create new class | Make entries similar to the following example and choose the Create icon.ExampleClass: PRODUCT_CLASSClass type: 017 | The Create Class screen displays. |  |
| 4 | Enter basic data | On the Basic data tab, make the following entries.Basic data section:Description: Product ClassStatus: Released (Default)Same classification section:Select the Do not check radio button. (Default)Note If you use the same classification, then you can choose the way of checking (warning message, error, none). |  |  |
| 5 | Enter char. | On the Char. tab, in the first row:Make the following entry.Char.: PRODUCT_TYPESelect the Proposal Rel. check box. |  |  |
| 6 | Save the class | Choose Save. | The class is created. |  |

#### Configure Document Types (Optional)

Purpose

In this process step, you can configure document types as per your requirement.

Procedure

1. Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:
    - Configure Your Solution:

Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution

On the Configure Your Solution: Realize Phase screen, filter the list using the following values:

-
    -
        - Application Area: R&D/Engineering
        - Sub Application Area: Project Control and Product Development

Select the line items with item name Product Development Foundation.

Go through the SSC UIs listed in the table below. Select each item and choose Configure.

-
    - SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the activity listed in the table below.

Choose Open Documentation for the found line item to see more details about this configuration activity.

Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

| Configuration Item/SSCUI Title | Description | Configuration Item/SSCUI ID |
| --- | --- | --- |
| Define DMS Document Types | Defines document type which is used in SAP DMS for defining document info records. | 101090 |

## Overview Table

This scope item consists of several process steps, provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Search for Document](#unique_10) [page ] 8 | Design Engineer | Manage Documents (F2733) | Search results display. |
| [Create New Document](#unique_11) [page ] 9 | Design Engineer | Manage Documents (F2733) | A new Document Info Record is created and attachments are added to the document. |
| [Create a New Version of the Document](#unique_12) [page ] 10 | Design Engineer | Manage Documents (F2733) | A new version of the document is created and new attachments are added. |
| [(Optional) Assign Object Link Metadata](#unique_13) [page ] 11 | Design Engineer | Manage Documents (F2733) | SAP object is linked to the document. |
| [(Optional) Maintain Attachments](#unique_14) [page ] 12 | Design Engineer | Manage Documents (F2733) | Attachment files of the document are updated. |
| [(Optional) Maintain Classification Metadata](#unique_15) [page ] 13 | Design Engineer | Manage Documents (F2733) | Classification information of the document is assigned or updated. |
| [Release Document](#unique_16) [page ] 14 | Design Engineer | Manage Documents (F2733) | The Status of the document is set to Released. |
| [Download Attachments](#unique_17) [page ] 15 | Design Engineer | Manage Documents (F2733) | Multiple attachments of different documents are downloaded together. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Search for Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you search for the document that you want to manage.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Documents (F2733) app. | The Manage Documents screen displays. |  |
| 3 | Search document using description | Enter the search criterion in the Document Description field, and choose Go.Example Document Description: Design* | The search results in one of the following:The document is not found. If so, proceed with the steps in [Create New Document](#unique_11) [page ] 9 and skip [Create a New Version of the Document](#unique_12) [page ] 10.The document is found and the document status is Released. If so, skip [Create New Document](#unique_11) [page ] 9 and proceed with the steps in [Create a New Version of the Document](#unique_12) [page ] 10.The document is found but the document status is not Released. If so, skip [Create New Document](#unique_11) [page ] 9 and [Create a New Version of the Document](#unique_12) [page ] 10. |  |

### Create New Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a new document. The files attached to the document are transferred to the Document Service repository using the SAP-managed communication scenario SAP_COM_1008.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Documents (F2733) app. | The Manage Documents screen displays. |  |
| 3 | Create new document | Choose Create to create a new document. | The Document Info record screen displays. |  |
| 4 | Enter general information | Make the following entries:Document Type: AUTDocument Part : 000 | The New Document screen displays. |  |
| 5 | Enter meta data | On the General Information tab, make the following entries:Document Type: AUTDocument Part : 000On the Document Data tab, enter a document description. For example, Document Description: Design Document 001.Press Enter. | The Document Status field is set to WR. |  |
| 6 | Upload attachments to the document | Choose the Originals tab.Choose Upload .On the Choose File to Upload dialog box, select the file that you want to upload.Choose Open. | The file is added as an attachment and is checked in. |  |
| 7 | Save the document | Choose Create. | A new document of the type AUT is created. |  |
| 8 | Set the document status to In Work | Choose Edit.On the Document Data tab, set the Document Status field to In Work.Choose Save. | The document status is set to In Work.Remember Note the Document Number. |  |

### Create a New Version of the Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A change in an existing product due to changing market or customer requirements may lead to the corresponding changes in the drawing and specification documents.

In this process step, you create a new version of an existing document. The new version of the document has the original files copied from the source document, and if required, you can add additional files. The files attached to the document are transferred to the Document Service repository using the SAP-managed communication scenario SAP_COM_1008.

Procedure

|  |
| --- |
| Tip If you carry out this test procedure in continuation to [Search for Document](#unique_10) [page ] 8, you can proceed directly to the Create a new version test step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Documents (F2733) app. | The Manage Documents screen displays. |  |
| 3 | Search the document using description | Enter the document description in the Document Description field, and choose Go.Example Document Description: Design | Search results display. |  |
| 4 | Create a new version | Select the document in the search results and choose Create New Version. | The Document screen displays. |  |
| 5 | (Optional) Upload attachments to the document | Choose the Originals tab.Choose the Upload icon.On the Choose File to Upload dialog box, select the file that you want to upload.Choose Open. | The file is added as an attachment and is checked in. |  |
| 6 | Save the document | Choose Create. | A new version of the document of type AUT is created. The previous versions of the document are listed on the Document Versions tab. |  |
| 7 | Set the document status to In Work | Choose Edit.On the Document Data tab, set the Document Status field to In Work.Choose Save. | The document status is set to In Work.Remember Note the Document Number. |  |

### (Optional) Assign Object Link Metadata

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you assign the document to a business object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Documents (F2733) app. | The Manage Documents screen displays. |  |
| 3 | Search the document | Enter the document description in the Document Description field and choose Go.Example Document Description: Design Document 001 | Search results display the details of the document created in [Create New Document](#unique_11) [page ] 9. |  |
| 4 | Create object links | On the Document screen, choose Edit.On the Object Links tab, choose Create.On the SAP Object dialog box, choose the SAP object DRAW.On the Select dialog box, choose the document that you want to link. | The object link with the document key is displayed in the Object Links section. | You can link the Product Master object (MARA) if the document type is SWV. |
| 5 | Save the document | Choose Save. | The document is saved. |  |

### (Optional) Maintain Attachments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you update attachment files associated with the document. The files attached to the document are transferred using the SAP-managed communication scenario SAP_COM_1008.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Documents (F2733) app. | The Manage Documents screen displays. |  |
| 3 | Search the document | Enter the document description in the Document Description field and choose Go.Example Document Description: Design Document 001 | Search results display the details of the document created in [Create New Document](#unique_11) [page ] 9. |  |
| 4 | Check out an attachment | On the Document screen, choose the Edit button and select the Originals tab.Select a file in the list of attachments.Choose Check-out. | The selected file is downloaded to your system.Note The file is downloaded to the Downloads folder specified in the browser settings. |  |
| 5 | Make changes in the downloaded file | Search for the downloaded file, make changes in the file, and then save the changes. | The file is updated. |  |
| 6 | Check in the updated file | On the Originals tab of the Document screen, choose Check-in > Check-in Original .Browse and select the updated version of the file.Choose Open. | The updated file is uploaded. |  |
| 7 | Save the document | Choose Save. | The document is saved. |  |

### (Optional) Maintain Classification Metadata

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you assign or change the classification information of the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Documents (F2733) app. | The Manage Documents screen displays. |  |
| 3 | Search the document | Enter the document description in the Document Description field and choose Go.Example Document Description: Design Document 001 | Search results display the details of the document created in [Create New Document](#unique_11) [page ] 9. |  |
| 4 | Assign or change classification information | On the Document screen, choose Edit.On the Classification tab, choose Click here to assign a class.On the Select: Class dialog box, select the class with name PRODUCT_CLASS.Make the following entry.PRODUCT TYPE: NOTEBOOKS | The classification details of the document, that is, Class and Product Type are displayed. |  |
| 4 | Save the document | Choose Save. | The document is saved. |  |

### Release Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you finalize the changes and release the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Documents (F2733) app. | The Manage Documents screen displays. |  |
| 3 | Search the document | Enter the document description in the Document Description field and choose Go.Example Document Description: Design Document 001 | Search results display the details of the document created in [Create New Document](#unique_11) [page ] 9. |  |
| 4 | Set the document status to Released | In the search results, choose the document record.On the Document screen, choose the Edit button.On the Document Data tab, ensure the following entry:Document Status: Released | The document status is set to Released. |  |
| 5 | Save the document | Choose Save. | The document is saved. |  |

### Download Attachments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you download original files from multiple documents at one go. Downloaded documents can be shared externally for document updates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Design Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Documents (F2733) app. | The Manage Documents screen displays. |  |
| 3 | Search for documents | Enter the search criteria in the Search field and click the Go button.Example Document Description: Design Document 001 | The search result is displayed. |  |
| 4 | Select multiple documents | In the search result, select multiple documents by selecting the respective check boxes. | Multiple documents are selected. |  |
| 5 | Download all attachments | Choose Download Originals. | All attachments are downloaded to the default download folder of the browser. |  |

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
- related-to :: [[01-solution-foundation-and-platform/sap-content-management-core-by-opentext-integration-7wc-test-script-12]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-archiving-and-document-access-core-by-opentext-integra]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-document-management-service-integration-7xy-1234]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-extended-ecm-by-opentext-integration-7y0-1235]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22P_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 26,132 chars in the whole document
