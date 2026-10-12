---
id: 08-sales-order-management/intercompany-sales-order-processing-make-to-order-6gc-ae-1166
title: Intercompany Sales Order Processing – Make-to-Order (6GC_AE) (6GC_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 test script for scope item 6GC_AE: creating an intercompany make-to-order sales order for a configurable forklifter (UAE/DE)."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/intercompany-make-to-order]
aliases: [6GC_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Make-to-Order Sales, intercompany sales orders, make-to-order, sales order creation, variant configuration, initial stock, business roles, test master data, pricing condition records, succeeding processes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GC_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1166
topic: 08-sales-order-management/intercompany-make-to-order
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intercompany Sales Order Processing – Make-to-Order (6GC_AE) (6GC_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GC_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Make-to-Order Sales** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Intercompany Sales Order Processing – Make-to-Order (6GC_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Intercompany Sales Order Processing – Make-to-Order (6GC_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232858894)

[2 Prerequisites 3](#_Toc232858895)

[2.1 System Access 3](#_Toc232858896)

[2.2 Roles 3](#_Toc232858897)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232858898)

[2.4 Additional Manual Configuration 5](#_Toc232858899)

[2.5 Business Conditions 5](#_Toc232858900)

[2.6 Preliminary Steps 5](#_Toc232858901)

[2.6.1 Create Initial Stock 5](#_Toc232858902)

[2.6.2 Create Condition Records (Optional) 6](#_Toc232858903)

[3 Overview Table 8](#_Toc232858904)

[4 Test Procedures 9](#_Toc232858905)

[4.1 Create Sales Orders 9](#_Toc232858906)

[5 Appendix 11](#_Toc232858907)

[5.1 Succeeding Processes 11](#_Toc232858908)

[5.2 Relevant Processes (Optional) 11](#_Toc232858909)

## Purpose

Overview

This scope item enables intercompany sales transactions. As an example, the functionality is leveraged when a company (located in a specific country or region) sells products to a customer in the same country or region. The products are shipped from a separate location belonging to an affiliated company belonging to a different company code than the selling company.

This scope item provides capabilities to record the sale, define the pricing to apply to the transaction, and generate the Accounts Payable posting required.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | CM-FL-V00 | Configurable Forklifter | Material which is used to be provided to the customer |
| End-Customer | 33100002 | Domestic UAE Customer 2 |  |
| Intercompany Customer | 33403310 | Customer in company code 3310 (AE) representing the ordering AE company (company code 3310) |  |
| Intercompany Supplier | 10401010 | Supplier in company code 1010 (DE) representing the delivering DE company (company code 1010) |  |
| Sales Organization | 3310 | Company Code 3310Sales organization in ordering company |  |
| Sales Organization | 1010 | Sales organization in supplying company |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the 1HO Set-Up Instructions: Setting Up Intercompany Sales Order Processing - Domestic (1HO) and 1MX Set-Up Instructions: Setting Up Intercompany Sales Order Processing - International (1MX) for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you.

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Open new posting period in company codes 1010, 1020, 1710, and 1720 respectively. |
| 1MX - Intercompany Sales Order Processing – International | Activate this scope item as prerequisite intercompany processes. |

### Preliminary Steps

#### Create Initial Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entry and choose Enter:Material: CM-FL-V00 (For example)Supply Plant: <Supply Plant in the affiliate/foreign company> | The Stock overview for the material is displayed. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: <Storage Location in the affiliate/foreign supply plant>Unrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: todayPosting Date: todayStock Change: Initial EntryQuantity: enter a number | The system displays Material document XXX created. The stock has been added. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other apps not included on the homepage using the search bar.If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Orders](#unique_11) [page ] 9 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access Sales Order Worklist | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order | Choose Create Sales Orders. | The Sales Order entry screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Enter.Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | Create Sales order: Overview screen displays. |  |
| 5 | Enter Order Details | Make the following entries and choose Enter:Sold-to Party: 33100002Cust. Reference: <PO number>Deliver.Plant: <Delivery Plant in another company code>, for example, 1030Material: <Material Number>, for example CM-FL-V00Order Quantity: <Quantity>, for example, 1Note If you want to create billing plan for this sales order, manually enter the following value as well. If not, choose Enter.ItCa (Item category): CBTD or CBTCOn the Variant Configuration screen, select value for characteristics below and choose Done.Lifter Model: <Heavy, Standard>Power Source: <Combustion, Electrical>. Combustion displays as default value.Wheel Type: <Cushion Tires, Pneumatic Tires>Fork Size: <Small, Normal, Large> (If customer-material info record is maintained as described in preliminary step, Small displays as default value)Counterweight (KG): <1.000, 2.000, 5.000>Battery Capacity(Ah): <50, 80, 140>Variant Condition: AVC_CWEIGHT by defaultNet Value: Varies according to characteristic value chosenChoose Done. |  |  |
| 6 | Enter Tax Departure Country | On the top menu, choose More > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region | In the Billing section, input:Tax Departure Ctry/R: AE |  |  |
| 8 | Go Back | Choose Back. | The Create Standard Order: Overview screen displays. |  |
| 9 | Check Intercompany Pricing Condition Type | Select the line item and choose Conditions, check intercompany pricing condition type exists, for example, PI02 Intercompany. |  |  |
| 10 | Save | Choose Save. | An intercompany sales order is created.Make a note of the sales order document number: ___________ |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Complete the following activities:Posting a Customer Invoice in AccountingOverdue ReceivablesDisplay Customer BalancesManage Customer Line Items |
| Event-Based Production Cost Posting (3F0) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Periodic closing BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer to https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html.If you are still using period-end posting, you may need to refer to non-standard Scope Item Period-End Closing – Plant (BEI). |

### Relevant Processes (Optional)

If the following processes (scope item 1MX,1YT & BJE) are enabled in your system, you can also test these business processes for the configurable material described in this test script.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Create Delivery | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| Perform Picking | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Material is picked. |
| Post Goods Issue | Shipping Specialist | Manage Outbound Deliveries (F0867A) | The Manage Outbound Deliveries screen displays. |
| Create F2 Invoice | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |
| Create Intercompany Invoice | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |

| Test Procedure No. of BJE | Test Procedure | Note |
| --- | --- | --- |
| 4.4.1 | Material Requirements Planning for Sales Order | After MRP run is complete, a purchase requisite is created for BoM component SF-XXX. Execute scope item US_2XU to get stock of this material.The material is picked by production order in step 4.6.3. |
| 4.6.1 | Create Production Order (CO01) | Before convert planned order into production order, you can check components in planned order.Choose the planned order and Open - Planned Order. On the Change Planned Order: Individual customer order screen, choose Componenet Overview. The components and component quantity in the planned order depend on the characteristic value chosen in sales order.Quantity of Counterweight = Planned Order Quantity* Counterweight (SF-FL-CWEIGHT) chosen in sales order/1000Quantity of Counterweight = Planned Order Quantity* Counterweight chosen in sales order/1000Material forksize = The fork size chosen in sales order: SF-FL-FORK-S (Small), SF-FL-FORK-M (Normal) or SF-FL-FORK-L (Large)Type of Tire = The Tire type chosen in sales order: SF-FL-TIRE-PNEU (Pneumatic Tire) or SF-FL-TIRE-CUSH (Cushion Tire)Model type = The power source chosen in sales order: SF-FL-COMB (Combustion) or SF-FL-ELECTRIC (Electrical)After production order is created, check configuration and operation in production order.Choose the generated production order and Open. Production order Display: Header, the screen displays.Choose Display Configuration (or choose from menu bar Header > Configuration ), on the Variant Configuration screen, check if characteristic value displays the same as chosen in sales order. Choose Close after done.Choose Operation. There are two cases.If configuration power source is combustion, there are two operations: 0010 and 0031.If configuration power source is electrical, there are 2 operations 0010 and 0032 in standard sequence. Choose Sequence, and double choose sequence 1, the 0011 operation is also available. |
| 4.6.2 | Release Production Orders (CO05N) | With the Production Supervisor - Discrete Manufacturing role, you can check configuration in the Manage Production Orders (F2336) App.Go to the order in the Manage Production Orders (F2336) App, choose the production order number and choose Open Production Order. On the Production Order screen, go to Items tab, and choose Display in Configuration column.You can check configuration details for the product. For multilevel configuration product, configuration for final product displays. On the top right corner, choose Change Log to display the change history of configuration. |
| 4.6.3 | Pick Components (Picking List) |  |
| 4.6.4 | Confirm Assembly Activities | In case power source is combustion, confirm operation 0010 and 0031.In case power source is electrical, confirm operation 0010, 0011 and 0032. |
| 4.6.5 | Posting Goods Receipt for Production Order |  |

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
- related-to :: [[08-sales-order-management/test-script-advanced-intercompany-sales-make-to-order-and-variant-conf]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GC_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 20,765 chars in the whole document
