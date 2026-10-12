---
id: 01-solution-foundation-and-platform/test-script-sap-document-management-service-integration-7xy-1234
title: Test Script - SAP Document Management Service Integration (7XY) (7XY_S4CLD2608_BPD_EN_XX)
description: SAP S/4HANA Cloud Public Edition test script (7XY) for uploading and downloading attachments via SAP Document Management service on SAP BTP.
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/document-and-attachment-management]
aliases: [7XY_S4CLD2608_BPD_EN_XX]
keywords: [Document Info Records and Attachment Services, document attachments, document management service, manage documents app, purchase contracts, test scripts, business roles, additional manual configuration, document status, 7XY]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7XY_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1234
topic: 01-solution-foundation-and-platform/document-and-attachment-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - SAP Document Management Service Integration (7XY) (7XY_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7XY_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Document Info Records and Attachment Services** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Document Management Service Integration (7XY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232828709)

[2 Prerequisites 3](#_Toc232828710)

[2.1 System Access 3](#_Toc232828711)

[2.2 Roles 3](#_Toc232828712)

[2.3 Additional Manual Configuration 3](#_Toc232828713)

[2.4 Business Conditions 4](#_Toc232828714)

[3 Overview Table 5](#_Toc232828715)

[4 Test Procedures 6](#_Toc232828716)

[4.1 Test Procedures at Business-Object Level 6](#_Toc232828717)

[4.1.1 Upload New Attachment 6](#_Toc232828718)

[4.1.2 Download Attachment 7](#_Toc232828719)

[4.2 Test Procedures for the Manage Documents App 8](#_Toc232828720)

[4.2.1 Upload New Attachment 8](#_Toc232828721)

[4.2.2 Download Attachment 9](#_Toc232828722)

## Purpose

Overview

The integration of SAP Document Management service on SAP Business Technology Platform (SAP BTP) provides archiving and document access functionality specifically designed for SAP S/4HANA Public Cloud. This enables businesses to manage and access SAP-related data and documents efficiently, meeting compliance and regulatory requirements while optimizing IT resources.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition system | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PCSAP_MM_SPT_SOURCING_PC |  |
| Design Engineer | SAP_BR_DESIGN_ENGINEER | Document Management | SAP_BR_DESIGN_ENGINEER |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b868989cc3b5acfd0542dfe4820e77e2)

### Business Conditions

Before you can test this scope item, you need the business object data for which you want to manage documents. For this scope item, we use Purchase Contract as an example for a business object. For other business objects, make sure that you activate the corresponding scope item relevant for your respective business object.

|  |
| --- |
| Note Please note that for any business object other than Purchase Contract, the test procedures under [Test Procedures at Business-Object Level](#unique_7) [page ] 6 need to be performed in the respective app for editing your specific business object. You then also require the respective business role needed for the app instead of the Purchaser role. |

| Scope Item | Business Condition |
| --- | --- |
| BMD - Purchase Contract | Follow steps described in the scope item to create the corresponding business data. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Process Steps for Managing Documents at Business-Object Level

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Upload New Attachment](#unique_9) [page ] 6 | Purchaser | Manage Purchase Contracts (F1600A) | A new attachment is created. |
| [Download Attachment](#unique_10) [page ] 7 | Purchaser | Manage Purchase Contracts (F1600A) | The new attachment is downloaded. |

Process Steps for Managing Documents Using the Manage Documents App

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Upload New Attachment](#unique_11) [page ] 8 | Design Engineer | Manage Documents (F2733) | A new attachment is created. |
| [Download Attachment](#unique_12) [page ] 9 | Design Engineer | Manage Documents (F2733) | The new attachment is downloaded. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Test Procedures at Business-Object Level

The following test steps are relevant for you if you want to manage your documents at business-object level.

#### Upload New Attachment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you upload a new attachment for an existing Purchase Contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Purchase Contracts (F1600A) app. | The Manage Purchase screen is displayed. |  |
| 3 | Search for Purchase Contracts | Set values to some filters to search for Purchase Contracts, for example:SupplierPurchasing GroupPlantThen choose Go. | The search results display the purchase contracts that match the filter criteria. |  |
| 4 | Select and Edit Purchase Contract | Select any Purchase Contract.Click Edit. | The Purchase Contract is displayed. |  |
| 5 | Upload Attachment | Choose the Attachments section.Choose Upload.In the Choose File to Upload dialog box, select the file that you want to upload.Choose Open.Choose Save. | A new attachment is uploaded. |  |

#### Download Attachment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you download an attachment for an existing Purchase Contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Purchase Contracts (F1600A) app. | The Manage Purchase screen is displayed. |  |
| 3 | Search for Purchase Contract | Search for the Purchase Contract for which you have created the new attachment in step [Upload New Attachment](#unique_9) [page ] 6 by entering its name or the same filter criteria as before:SupplierPurchasing GroupPlantThen choose Go. | The search results display the purchase contracts that match the filter criteria. |  |
| 4 | Select and Edit Purchase Contract | Select the Purchase Contract.Click Edit. | The Purchase Contract is displayed. |  |
| 5 | Create Attachment | Choose the Attachments section.Select the Attachment checkbox.Click the Download Originals button. | The document is downloaded to the default download folder of the browser. |  |

### Test Procedures for the Manage Documents App

The following steps are relevant for you if you want to manage your documents using the Manage Documents app.

#### Upload New Attachment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a new document and upload a new attachment for an existing Purchase Contract with the Manage Documents app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as SAP_BR_DESIGN_ENGINEER. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Documents (F2733) app. | The Manage Documents screen is displayed. |  |
| 3 | Create New Document | Choose Create to create a new document. | The Document screen is displayed. |  |
| 4 | Upload Attachment | Choose the Originals tab.Choose Upload.In the Choose File to UPload dialog box, select the file that you want to upload.Choose Open. | The file is added as an attachment and is checked in. |  |
| 5 | Save the Document | Choose Create. | A new document is created. |  |
| 6 | Set the Document Status to In Work | Choose Edit.On the Document Data tab, set the Document Status field to In Work. | The document status is set to In Work.Note Remember to note down the document number. |  |

#### Download Attachment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you download an attachment for an existing Purchase Contract with the Manage Documents app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as SAP_BR_DESIGN_ENGINEER. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Documents (F2733) app. | The Manage Purchase screen is displayed. |  |
| 3 | Search for Documents | Enter the search criteria in the Search field and choose Go.Document Description: Design Document 001 | The search result is displayed. |  |
| 4 | Select Multiple Documents | In the search result, select multiple documents by selecting the respective check boxes. | Multiple documents are selected. |  |
| 5 | Download All Attachments | Choose Download Originals. | All attachments are downloaded to the default download folder of the browser. |  |

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
> Flagged while digesting this document, not verified: Near-identical to the 7W6 OpenText test script; differs only in the integration and set-up link.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/sap-content-management-core-by-opentext-integration-7wc-test-script-12]]
- related-to :: [[01-solution-foundation-and-platform/test-script-manage-documents-22p-ae-sap-s-4hana-cloud-public-edition-8]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-archiving-and-document-access-core-by-opentext-integra]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-extended-ecm-by-opentext-integration-7y0-1235]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7XY_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 14,864 chars in the whole document
