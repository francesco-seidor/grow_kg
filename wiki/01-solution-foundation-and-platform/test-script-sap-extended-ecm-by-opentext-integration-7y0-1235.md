---
id: 01-solution-foundation-and-platform/test-script-sap-extended-ecm-by-opentext-integration-7y0-1235
title: "Test Script: SAP Extended ECM by OpenText Integration (7Y0) (7Y0_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 7Y0 on SAP S/4HANA Cloud Public Edition 2608: uploading and downloading attachments via business objects (Product) and the Manage Documents app."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/document-and-attachment-management]
aliases: [7Y0_S4CLD2608_BPD_EN_XX]
keywords: [Document Info Records and Attachment Services, extended ecm integration, document attachments, manage documents app, product master, content management scope items, business roles, test scripts, 7Y0]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Y0_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1235
topic: 01-solution-foundation-and-platform/document-and-attachment-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP Extended ECM by OpenText Integration (7Y0) (7Y0_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Y0_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Document Info Records and Attachment Services** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Extended ECM by OpenText Integration (7Y0) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232792851)

[2 Prerequisites 3](#_Toc232792852)

[2.1 System Access 3](#_Toc232792853)

[2.2 Roles 3](#_Toc232792854)

[2.3 Additional Manual Configuration 3](#_Toc232792855)

[2.4 Business Conditions 4](#_Toc232792856)

[3 Overview Table 5](#_Toc232792857)

[4 Test Procedures 6](#_Toc232792858)

[4.1 Test Procedures at Business-Object Level 6](#_Toc232792859)

[4.1.1 Upload New Attachment 6](#_Toc232792860)

[4.1.2 Download Attachment 7](#_Toc232792861)

[4.2 Test Procedures for the Manage Documents App 8](#_Toc232792862)

[4.2.1 Upload New Attachment 8](#_Toc232792863)

[4.2.2 Download Attachment 9](#_Toc232792864)

## Purpose

Overview

Business processes in SAP S/4HANA Cloud Public Edition are based on structured as well as unstructured content - such as contracts, specifications, drawings, and emails. This unstructured content is often essential for driving business processes.

To empower SAP users with best-in-class content management capabilities, SAP S/4HANA Cloud Public Edition integrates seamlessly with SAP Extended Enterprise Content Management (ECM) by OpenText.

With SAP Extended ECM by OpenText, you can bridge content silos between SAP and non-SAP business users by bringing content in the context of the business process, even across business applications. Users benefit from built-in capabilities such as viewing services, document generation, integration with Microsoft Office 365, and more – streamlining content creation, editing, and management to accelerate the business processes.

|  |
| --- |
| Note During the onboarding process for SAP S/4HANA Cloud Public Edition, a document repository is automatically provisioned by default to support content management. Customers who require extended document management functionality can choose between these scope items:7Y0 - SAP Extended ECM by OpenText Integration (described here)7WC - SAP Content Management Core by OpenText Integration7W6 - SAP Archiving and Document Access Core by OpenText Integration7XY - SAP Document Management Service Integration |

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
| Administrator | SAP_BR_ADMINISTRATOR | Purchasing / Sourcing and Contracting | SAP_BR_ADMINISTRATOR |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products | SAP_BR_PRODMASTER_SPECIALIST |  |
| Design Engineer | SAP_BR_DESIGN_ENGINEER | Document Management | SAP_BR_DESIGN_ENGINEER |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/085db74db26d08f79dc923364020dab3)

### Business Conditions

Before you can test this scope item, you need the business object data for which you want to manage documents. For this scope item, we use Product as an example for a business object. For other business objects, make sure that you activate the corresponding scope item relevant for your respective business object.

|  |
| --- |
| Note Please note that for any business object other than Product, the test procedures under Business-Object Level need to be performed in the respective app for editing your specific business object. You then also require the respective business role needed for the app instead of the Master Data Specialist - Product Data role. |

| Scope Item | Business Condition |
| --- | --- |
| Create Product Master of type "Trading Good" - MDS | Follow the steps described in the scope item to create the corresponding business data. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Process Steps for Managing Documents at Business-Object Level

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Upload New Attachment | Master Data Specialist - Product Data | Manage Product Master (F1602) | A new attachment is created. |
| Download Attachment | Master Data Specialist - Product Data | Manage Product Master (F1602) | The new attachment is downloaded. |

Process Steps for Managing Documents Using the Manage Documents App

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Upload New Attachment | Design Engineer | Manage Documents (F2733) | A new attachment is created. |
| Download Attachment | Design Engineer | Manage Documents (F2733) | The new attachment is downloaded. |

## Test Procedures

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

In this process step, you upload a new attachment for an existing Product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Master Data Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Product Master (F1602) app. | The Manage Product Master screen is displayed. |  |
| 3 | Search for Product | Set values to some filters to search for Product, for example:Product GroupProduct CategoryThen choose Go. | The search results display the Products that match the filter criteria. |  |
| 4 | Display Product | Select any Product.Click Edit. | The Product is displayed. |  |
| 5 | Upload Attachment for DMS | Choose the Attachments > Document Management System section section.In the Select Document Type to Upload dialog box, choose Office-Documents (YBO).Choose Upload.In the Choose File to Upload dialog box, select the file that you want to upload.Choose Open.Choose Save. | A new attachment is uploaded. |  |
| 6 | Upload Attachment for GOS | Choose the Attachments > Document Management System section section.In the Select Document Type to Upload dialog box, choose Generic Object Services.Choose Upload.In the Choose File to Upload dialog box, select the file that you want to upload.Choose Open.Choose Save. | A new attachment is uploaded. |  |

#### Download Attachment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you download an attachment for an existing Product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Master Data Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Product Master (F1602) app. | The Manage Product Master screen is displayed. |  |
| 3 | Search for Product | Set values to some filters to search for Products, for example:Product GroupProduct CategoryThen choose Go. | The search results display the products that match the filter criteria. |  |
| 4 | Display Product | Select the Product.Click Edit. | The Product is displayed. |  |
| 5 | Download DMS Attachment | Navigate to the Choose the Attachments - Document Management System section.Click on the Attachment. | The document is downloaded to the default download folder of the browser. |  |
| 6 | Download GOS Attachment | Navigate to the Choose the Attachments - Document Management System section.Click on the Attachment. | The document is downloaded to the default download folder of the browser. |  |

### Test Procedures for the Manage Documents App

#### Upload New Attachment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you upload a new attachment for an existing Product with the Manage Documents app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as SAP_BR_DESIGN_ENGINEER. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Documents (F2733) app. | The Manage Documents screen is displayed. |  |
| 3 | Create New Document | Choose Create to create a new document. | The Document screen is displayed. |  |
| 4 | Upload Attachment | Choose the required document type, for example: AUT.Choose the Originals tab.Choose Upload.In the Choose File to Upload dialog box, select the file that you want to upload.Choose Open. | The file is added as an attachment and is checked in. |  |
| 5 | Save the Document | Choose Create. | A new document of the type AUT is created. |  |
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

In this process step, you download an attachment for an existing Product with the Manage Documents app.

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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/sap-content-management-core-by-opentext-integration-7wc-test-script-12]]
- related-to :: [[01-solution-foundation-and-platform/test-script-manage-documents-22p-ae-sap-s-4hana-cloud-public-edition-8]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-archiving-and-document-access-core-by-opentext-integra]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-document-management-service-integration-7xy-1234]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Y0_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 16,222 chars in the whole document
