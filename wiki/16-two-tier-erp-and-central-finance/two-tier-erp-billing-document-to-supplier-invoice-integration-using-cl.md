---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-billing-document-to-supplier-invoice-integration-using-cl
title: Two Tier ERP – Billing Document to Supplier Invoice Integration using Cloud Integration (S4CLD2608_Two tier ERP_Bill_Invoice_User_Guide_EN)
description: "Customer guide for two-tier ERP integration converting an HQ billing document (IDoc INVOIC02) into a supplier invoice in S/4HANA Cloud Public Edition via Cloud Integration, with test script."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/subsidiary-replenishment-from-hq]
aliases: [S4CLD2608_Two tier ERP_Bill_Invoice_User_Guide_EN]
keywords: [Subsidiary Procurement from Headquarters, two-tier erp, billing document integration, supplier invoice, cloud integration, integration prerequisites, field mapping, error handling, test script, communication arrangements]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Billto Inv/S4CLD2608_Two tier ERP_Bill_Invoice_User_Guide_EN.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-251
topic: 16-two-tier-erp-and-central-finance/subsidiary-replenishment-from-hq
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two Tier ERP – Billing Document to Supplier Invoice Integration using Cloud Integration (S4CLD2608_Two tier ERP_Bill_Invoice_User_Guide_EN)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Billto Inv/S4CLD2608_Two tier ERP_Bill_Invoice_User_Guide_EN.docx`, extracted with `mammoth`. Grouped under **Subsidiary Procurement from Headquarters** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP S/4HANA Cloud Public EditionJune 2026EnglishEnglish |  |
|  | Two Tier ERP – Billing Document to Supplier Invoice Integration using Cloud Integration |
|  | Customer Guide |

Copyright

© 2025 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 13.12.2017 | Initial version of document |
| 1 | 31.03.2021 | Review of Document |

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

This document will provide the Billing Document to Supplier Invoice integration in a 2 tier ERP scenario. The Billing Document created at the HQ (SAP S/4HANA Cloud Private Edition or SAP ERP) will be converted to a Supplier Invoice at the subsidiary (SAP S/4HANA Cloud Public Edition).

## Business Requirements

In a two-tier model, SAP S/4HANA Cloud Public Edition and SAP S/4HANA Cloud Private Edition systems can support the organization and subsidiaries to run in an independent yet integrated fashion. In “Sell from headquarters to subsidiary” scenario. “Sending Billing document from the HQ which gets converted into a Supplier Invoice at the Subsidiary” is one of the business process steps.

## Technical Details

The main steps in the scenario:

1. Billing document IDoc INVOIC02 is created in SAP S/4HANA Cloud Private Edition or SAP ERP.

2. The IDOCs are sent from SAP S/4HANA Cloud Private Edition or SAP ERP system to SAP Cloud Integration and mapped to Supplier Invoice API (SupplierInvoiceERPCreateRequestConfirmation_In).

3. The Supplier Invoice API is triggered from BTP Integration to create Supplier Invoice in SAP S/4HANA Cloud Public Edition System.

Note: If there is a need of enhanced monitoring we can also capture the response from Supplier Invoice API: SupplierInvoiceERPCreateRequestConfirmation_In in our BTP Integration tenant.

### Prerequisites

The following list of prerequisite configurations are to be in place to realize the integration process.

***Configuration in SAP S/4HANA Cloud Public Edition:***

1. Create a Communication User in SAP S/4HANA Cloud Public Edition system. This user credential will be used in Supplier Invoice Create in SAP Cloud Integration tenant.
2. Maintain a Communication System to specify the host details.
3. Maintain a Communication Arrangement to facilitate the read of API. The Communication Scenario used for Supplier Invoice Create is SAP_COM_0057.

***Configuration in SAP S/4HANA Cloud Private Edition or SAP ERP*:**

The outgoing IDOC (INVOIC02) needs to be processed and converted to a supplier Invoice. We need to maintain the following configurations.

1. Maintain the RFC Connection in SM59 to target URL to BTP Integration.
2. Create Port & Partner Profile in WE21 & WE20. Add the message id for Invoic02 in outbound message types.
3. Generate model view in BD64.

**Creation of SAP Cloud Integration iFlow:**

<!-- image omitted: unnamed -->

Figure 1.0

### Mapping Prerequisites

The Customer specific field mappings are suggested below for the target structure. However, the fields might not be limited to the ones given and the Customer needs to take care of the same during implementation. Some constant or logic has to be set against these fields.

| **Target structure field name** | **Description** | **Mapping Logic/ Constant** |
| --- | --- | --- |
| /SupplierInvoice/CompanyID | Company Code | Constant value (eg: 1010) |
| /SupplierInvoice/ProcessingTypeCode | Processing Type Code -header | Constant Value (eg: RE) |
| /SupplierInvoice/CompletenessAndValidationStatusCode | Completeness and Validation Status Code | Constant Value (eg: D) |
| /Item/ProcessingTypeCode | Processing Type Code - item | Constant Value (eg: B) |
| /Item/TaxCalculation/ProductTaxDetails/TaxJurisdictionCode | Tax Jurisdiction Code | Either a Constant or as per business logic |
| /Item/TaxCalculation/ProductTaxDetails/TaxationCharacteristicsCode | Taxation Characteristics Code | Either a Constant or as per business logic |

For more details on Constant Value options which can be maintained for above target structure field names, kindly refer to the attachment in SAP Note: [2321804](https://launchpad.support.sap.com/#/notes/2321804). A copy of this attachment is also attached below:

<!-- image omitted: unnamed -->

### Error Handling & Monitoring

Message Monitoring in SAP Cloud Integration can be used for Error Handling & Monitoring Error/Sucess Messages.

”Monitor Message Processing / Message Processing Details“ Provides the Log, Payload & S4Response Messages as below.

1. Log (figure 1.1) : Shows the Status of the message
2. Payload (figure 1.2) : Shows the Source Idoc xml Payload
3. S4Response(figure1.3): Shows the S4C Response message with details of “Invoice Document Number “ & “Fiscal year” created in S4HC.

We can use the Source & Response Payload to verify & correlate the supplier invoice Created in S4HC

<!-- image omitted: unnamed -->

Figure 1.1(Log)

<!-- image omitted: unnamed -->

Figure 1.2 (source payload)

<!-- image omitted: unnamed -->

Figure 1.3 (response payload)

## Test Script

### Purpose

This section provides a detailed procedure for testing the scope item after solution deployment. Each process step is covered in its own section, providing the system interactions in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly.

### Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

**Note:**

The process to be tested in this test script is for Subsidiary side regarding a two-tier scenario. Hence integration between Subsidiary system (SAP S/4HANA Cloud Public Edition) and Headquarter system (SAP S/4HANA Cloud Private Edition or SAP ERP) shall be set up in advance. You will be able to process the test steps only after the corresponding buyer system has sent the required messages.

#### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

#### Roles

Assign the following business roles to your individual test users.

Note The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT |  |

#### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure.

Make sure that the proper mappings are maintained between the Purchase Order created in SAP S/4HANA Cloud Public Edition and Sales Order in SAP S/4HANA Cloud Private Edition or SAP ERP.

### Overview Table

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Create a Billing Document in SAP S/4HANA Cloud Private Edition or SAP ERP |  |  | Billing document IDoc is created with all the relevant items and other details |
| Check for Supplier Invoice in SAP S/4HANA Cloud Public Edition | SAP_BR_AP_ACCOUNTANT | Supplier Invoices | Supplier Invoice created with relevant details |

### Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on to SAP S/4HANA Cloud Private Edition or SAP ERP | Create Billing Document. Note the billing doc number. | IDoc Triggered in SAP S/4HANA Cloud Private Edition or SAP ERP |
| 2 | Log on to SAP S/4HANA Cloud Public Edition. | Check Supplier invoice created using “Supplier Invoices List” app. The billing doc number will be in the “Reference Id” field of the Invoice. | Supplier Invoice is displayed. |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Billto Inv/S4CLD2608_Two tier ERP_Bill_Invoice_User_Guide_EN.docx` — full document · extracted with `mammoth` · 11,645 chars in the whole document
