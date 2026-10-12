---
id: 11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-03
title: "Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 3 of 3"
description: "SAP test script for scope item 6W3 Transportation Execution (AE), S/4HANA Cloud 2608; ends with accrual posting, error repost, follow-on processes."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-planning-and-execution]
aliases: []
keywords: [Transportation Planning and Execution, freight cost accruals, accrual posting errors, freight cost allocation, subcontracting with tm, process integration, freight settlement, transportation execution, service purchase orders, group valuation]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx#lines-5534-5580"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1195
topic: 11-inventory-warehouse-and-transportation/transportation-planning-and-execution
language: EN
part: 3/3
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 3 of 3

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx`, part 3 of 3 (lines 5534–5580 of the extracted text), extracted with `mammoth`. Grouped under **Transportation Planning and Execution** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

See [Business Conditions](#unique_7) [page ] 9.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BMY - Subcontracting | After step Set Ready for Warehousing for the Inbound processing, perform Receive Goods from Subcontracting PO. |
| 6W4 - Freight Settlement | After the last step in this scope item, continue with the scope item 6W4 - Freight Settlement. |

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
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-02]]
- related-to :: [[11-inventory-warehouse-and-transportation/manual-transportation-planning-6w2-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-external-transportation-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx` — lines 5534–5580 of the extracted text · extracted with `mammoth` · 505,382 chars in the whole document
