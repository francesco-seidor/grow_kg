---
id: 15-retail-operations/empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition-part-02
title: "Empties for Retail (5FK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FK_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "SAP S/4HANA Cloud Public Edition test script for Empties for Retail (5FK_AE): prerequisites, master data, procurement and store/online sales flows with step-by-step test procedures."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/empties-management-retail]
aliases: []
keywords: [Empties Management for Retail, click and collect, order handover, picking request withdrawal, reservation hand over, sales order document flow, manage sales orders, retail store associate, test script conventions, 5FK]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FK_S4CLD2608_BPD_EN_AE.docx#lines-3125-3173"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1080
topic: 15-retail-operations/empties-management-retail
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Empties for Retail (5FK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FK_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FK_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3125–3173 of the extracted text), extracted with `mammoth`. Grouped under **Empties Management for Retail** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 8 | Scan the Picking Request to Withdraw | Select Handover Status on the top right of the screen.Note Hand Over (in case of paid orders), Reservation Hand Over (in case of unpaid orders) and Cancel Order buttons on the bottom of the screen are enabled once the entire order is withdrawn.Select Scan Picking Request on the top right corner of the Handover Status pop-over and scan the picking request bar-code of the order placed in the mentioned handover shelf space using the camera on the device or manually enter the picking request barcode number in the Enter Bar Code pop-up and choose OK and finally select Done | Handover Status pop-over screen is displayed containing the list of Picking Request, Picking Request Status their corresponding Handover Shelf Space numbers and the Withdraw hyperlink.The picking request is withdrawn from the handover shelf space or bin, the hyperlink text changes to Withdrawn and the user is navigated back to the Exceptions tab view. |  |
| 9 | Hand Over Orders | Select Reservation Hand Over on the Hand Over Orders screenNote Reservation Hand Over should be active only for Not Paid orders with picking request status On Track or Order Due for Cancellation. | A confirmation message Reservation Hand Over is processed is displayed on the screen. Order status changes to Reservation Handed Over and the user is navigated back to the order list screen. |  |

#### Validate Sales Order Document and Subsequent Document Flow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to validate the updates on the sales order also the subsequent documents generated after order sales in store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Retail Store Associate. |  |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) app. | Manage Sales Orders (F1873) screen is displayed. |  |
| 3 | Go to App | On the Manage Sales Orders (F1873) screen, enter <your sales order number> in the Sales Order field. Select Go | Sales order line item is displayed in the search result. |  |
| 4 | Open the order details | Select the sales order line item. | Display Standard Order XXXXX: Overview screen is displayed. |  |
| 5 | Navigate to Document Flow | Select Display Document Flow, to investigate the details of the subsequent document, for example, outbound delivery, goods issue, invoice documents, material and accounting documents, select the document and choose Display Document. | Generated documents are displayed on the Document Flow screen. Further, selected documents are displayed to investigate the details. |  |

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
> Flagged while digesting this document, not verified: Step 9 uses Reservation Hand Over, which the same step says is for Not Paid orders only, inside a section titled Click-and-Collect (Pre-Paid Order); pre-paid orders would use Hand Over instead.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FK_S4CLD2608_BPD_EN_AE.docx` — lines 3125–3173 of the extracted text · extracted with `mammoth` · 254,719 chars in the whole document
