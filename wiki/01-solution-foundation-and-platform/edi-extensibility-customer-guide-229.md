---
id: 01-solution-foundation-and-platform/edi-extensibility-customer-guide-229
title: EDI Extensibility Customer Guide (S4CLD2608_2T_ EDI Extensibility_User_Guide_EN)
description: "Customer guide for adding custom fields to EDI-based SOAP APIs and IDocs in SAP Cloud ERP, with a Sales Order example, prerequisites and AIF monitoring."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/edi-and-api-extensibility]
aliases: [S4CLD2608_2T_ EDI Extensibility_User_Guide_EN]
keywords: [EDI and API Field Extensibility, edi extensibility, custom fields, soap api, error monitoring, idoc, communication arrangement, business roles, sales order]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Integration/S4CLD2608_2T_ EDI Extensibility_User_Guide_EN.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-229
topic: 01-solution-foundation-and-platform/edi-and-api-extensibility
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# EDI Extensibility Customer Guide (S4CLD2608_2T_ EDI Extensibility_User_Guide_EN)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Integration/S4CLD2608_2T_ EDI Extensibility_User_Guide_EN.docx`, extracted with `mammoth`. Grouped under **EDI and API Field Extensibility** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | EDI Extensibility |
| SAP SE Dietmar-Hopp-Allee 16 69190 Walldorf Germany | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 25.01.2018 | Initial version of document |
| 1 | 02.06.2026 | Update |

Only add a revision when corrections are made to a published document. Do not change the original published date. Set back to revision 0 after a full upgrade of the Customer Guide.

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Content

[1 Purpose 6](#_Toc501443128)

[2 Business Requirements 6](#_Toc501443129)

[3 Technical Details 6](#_Toc501443130)

[3.1 Prerequisites 6](#_Toc501443131)

[3.2 Mapping Prerequisites 7](#_Toc501443132)

[3.3 Error Handling & Monitoring 8](#_Toc501443133)

[4 Test Script 10](#_Toc501443134)

[4.1 Purpose 10](#_Toc501443135)

[4.2 Prerequisites 10](#_Toc501443136)

[4.2.1 System Access 11](#_Toc501443137)

[4.2.2 Roles 11](#_Toc501443138)

[4.2.3 Master Data, Organizational Data and Other Data 11](#_Toc501443139)

[4.3 Overview Table 11](#_Toc501443140)

[4.4 Test Procedure 12](#_Toc501443141)

## Purpose

This document will provide the details on adding the custom fields in EDI based SOAP API.

## Business Requirements

During Integration of SAP Cloud ERP with other SAP and non-SAP systems via EDI, sometimes the business communication might require the additional fields to be present in SOAP API or IDoc apart from the standard delivered fields by SAP. To make such integration feasible and easy, SAP Cloud ERP provides the capability of Extensibility in EDI.

## Technical Details

There are mainly 2 ways in which EDI extensibility is provisioned:

1. Custom Fields at SOAP services
2. Custom Fields at IDocs

### Prerequisites

The following list of prerequisite configurations are to be in place to realize EDI extensibility:

- The API to be extended should be enabled for extension and attached to a Business Context by SAP.
- The User doing EDI Extensibility should be a Key User.
- To enable the extended field in UI, it should be enabled under ‘UI and Reports’ section of ‘Custom Fields and Logic’ Application.

### Error Handling & Monitoring

Monitoring of errors/interfaces can be done using AIF(Application Interface Framework) in SAP Cloud ERP. Use ‘Message Dashboard’ SAP AIF Application for same.

The business role required here is “SAP_BR_CONF_EXPERT_BUS_NET_INT”.

Before Accessing ‘Message Dashboard’ application, the recipients need to be assigned to users via ‘Assign Recipients ’ and those users would then be able to monitor the interfaces and messages they are assigned to. Even the types of messages which a user can see in the ‘Message Dashboard’ can be defined.

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

## Procedure/Steps to follow

### Purpose

This section provides a detailed procedure for testing the EDI extensibility deployment. Steps that are not in scope of the process but are needed for testing are marked accordingly.

### Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

**Note:**

For the example taken here, addition of a custom field in EDI based SOAP API is covered. The API taken in this example is EDI Integration: Create/Change Sales Order (OrderRequest_In) which is available under Business Context – ‘Sales Document’.

#### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

#### Roles

Assign the following business roles to your individual test users.

Note: The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role | Business Role ID as Delivered by SAP | Comment |
| --- | --- | --- |
| Administrator | SAP_BR_ADMINISTRATOR | Extensibility |
| Configuration Expert | SAP_BR_CONF_EXPERT_BUS_NET_INT | Message Monitoring (AIF) |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Display Sales Order (for the example taken here) |

#### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure.

### Overview

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Create a Custom Field |  | Custom Fields and Logic |  |
| Enable Usage for the relevant SOAP APIs or IDocs |  | Custom Fields and Logic | Custom Field will be available in enabled APIs or IDocs |
| Enable Usage in ‘UIs and Reports’ section |  | Custom Fields and Logic | Custom Field will be available in the Custom Fields tab in UI |

### 4.4 Detailed Steps

This section describes procedures to follow for achieving EDI extensibility in SOAP. In the example here, we will create a custom field ‘Partner No.’ and add it to EDI based Sales Order API as well as Sales Order user interface:

**4.4.1** Logon to SAP Cloud ERP and Launch ‘Custom Fields and Logic’ application.

Create a Custom Field based on Business Context – ‘Sales Document’.

<!-- image omitted: unnamed -->

**4.4.2** Enable its usage in SOAP API as well as the required user interface and Publish it.

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

**4.4.3** Create Communication User, Communication System and Communication Arrangement with respect to the Communication Scenario associated with the API (SAP_COM_0223 for our example).

<!-- image omitted: C:\Users\i322726\AppData\Local\Microsoft\Windows\INetCache\Content.Word\5.png -->

**4.4.4** This API with the added custom field can now be tested using any external tool e.g.: SoapUI. For this, download the WSDL from Communication Arrangement and create your respective XML payload in SoapUI project. The service URL generated in the Communication Arrangement would be used to hit the system with your Payload.

<!-- image omitted: unnamed --> SoapUI is just written as an example for the invocation of API to enable you for testing and is not part of SAP Cloud ERP. Other invocation methods/tools can also be utilized based on the individual need.

<!-- image omitted: unnamed -->

**4.4.6** Once the request is successfully sent from the invocation tool, the sales order would be created in SAP Cloud ERP and the data sent in the custom field would be visible in the Sales Order Header of ‘Display Sales Order’ application.

<!-- image omitted: C:\Users\i322726\AppData\Local\Microsoft\Windows\INetCache\Content.Word\9.png -->

**4.4.7** The monitoring and error handling can be done using ‘Message Monitoring’ application enabled by AIF.

<!-- image omitted: unnamed -->

## Connections
- part-of :: [[_cluster]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-erp-integration-setup-document-230]]
- see-also :: [[01-solution-foundation-and-platform/test-script-business-event-handling-1nn-748]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Integration/S4CLD2608_2T_ EDI Extensibility_User_Guide_EN.docx` — full document · extracted with `mammoth` · 9,801 chars in the whole document
