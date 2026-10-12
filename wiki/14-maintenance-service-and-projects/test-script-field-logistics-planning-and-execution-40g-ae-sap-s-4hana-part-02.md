---
id: 14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-02
title: "Test Script: Field Logistics Planning and Execution (40G_AE) - SAP S/4HANA Cloud Public Edition (40G_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (AE): final EWM picking steps and technical completion of a maintenance order, plus SAP legal footer."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/field-logistics]
aliases: []
keywords: [Field Logistics Planning and Execution, warehouse task creation, outbound delivery, maintenance order completion, technical completion, goods issue, maintenance order settlement, test script procedure, typographic conventions, 40G]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40G_S4CLD2608_BPD_EN_AE.docx#lines-2555-2612"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-991
topic: 14-maintenance-service-and-projects/field-logistics
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Field Logistics Planning and Execution (40G_AE) - SAP S/4HANA Cloud Public Edition (40G_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40G_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 2555–2612 of the extracted text), extracted with `mammoth`. Grouped under **Field Logistics Planning and Execution** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Manage Outbound Delivery Orders (F6498) app. | The Manage Outbound Delivery Orders screen is displayed. |  |
| 3 | Set Default Warehouse | In user profile settings, enter FOBP as default warehouse. | Warehouse set as default. |  |
| 4 | Filter the Outbound Delivery | In filter settings, clear other filters.Enter LE Delivery: Outbound Delivery created in the step [Receive Goods at Base](#unique_78) [page ] 118.Choose Go. | Outbound delivery is displayed. |  |
| 5 | Select Item | Select item.Choose Chevron. | Outbound delivery order screen is displayed. |  |
| 6 | Create Warehouse Task | Select outbound delivery order item.Choose Missing Task.Select Item.Choose Create Task Manually. | Warehouse tasks are created. |  |
| 7 | Confirm Warehouse Task | Select outbound delivery item.Select Item.Choose Create Pick Warehouse TaskSelect Create Pick Tasks manually from the dropdown list.Enter source bin and quantity.Choose Create | Warehouse tasks confirmed. |  |
| 8 | Post Goods Issue | Select item and choose Goods Issue. | Goods issue is posted. |  |

### Technically Complete Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance notification is completed, and the maintenance order is technically completed after the required maintenance work has been performed. The technical completion reduces all the purchase requisitions, open reservations, and capacities still outstanding for the maintenance order. The order can continue to receive costs, for example, through invoice receipts for delivered and used materials. But it is blocked for all changes in the processing.

The order settlement transfers the costs incurred that were temporarily collected for the maintenance order, to the recipient, for example, to the cost center for the maintained object. This process step shows you how to technically complete maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Find Maintenance Orders - Completion (F2175). | The Maintenance Order screen is displayed. |  |
| 3 | Search for Order Number | On the Maintenance Order screen, enter the order type YA01.Choose Go.Choose the order line that you created in the previous step. |  |  |
| 4 | Navigate to Change Maintenance Order | Choose Related Apps at the top right corner of the screen and choose Change Maintenance Order. |  |  |
| 5 | Set Complete (Technically) Status | Choose Set System Status > Complete Technically .Note In case of TOH or TPOH status is there, technical completion of maintenance order is not possible.Blocking of technical completion only works if phase control is setup properly. | The Complete (Technically) screen is displayed. |  |
| 6 | Reference Data | Enter the following:Reference Date: <Date>Reference Time: <Time>Complete Assigned Notifications: selectedChoose Ok. | The Complete (Technically) status for the maintenance order is done. |  |

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
- related-to :: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-01]]
- related-to :: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-supplier-items-4ah]]
- related-to :: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-field-logistics-planning]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40G_S4CLD2608_BPD_EN_AE.docx` — lines 2555–2612 of the extracted text · extracted with `mammoth` · 255,822 chars in the whole document
