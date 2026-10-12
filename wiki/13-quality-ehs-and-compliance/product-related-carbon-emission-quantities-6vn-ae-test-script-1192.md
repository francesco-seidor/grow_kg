---
id: 13-quality-ehs-and-compliance/product-related-carbon-emission-quantities-6vn-ae-test-script-1192
title: Product-Related Carbon Emission Quantities (6VN_AE) Test Script (6VN_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6VN: determining, displaying and releasing CO2e emission quantities in product costing runs."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/product-footprint-and-carbon-emissions]
aliases: [6VN_S4CLD2608_BPD_EN_AE]
keywords: [Product Footprints and Carbon Emission Quantities, carbon emission quantities, product costing, costing runs, product footprint management, activity cost rates, material cost estimates, standard cost release, ledger-specific costing, sap analytics cloud integration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6VN_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1192
topic: 13-quality-ehs-and-compliance/product-footprint-and-carbon-emissions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Product-Related Carbon Emission Quantities (6VN_AE) Test Script (6VN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6VN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Product Footprints and Carbon Emission Quantities** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Product-Related Carbon Emission Quantities (6VN_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Product-Related Carbon Emission Quantities (6VN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232859157)

[2 Prerequisites 3](#_Toc232859158)

[2.1 System Access 3](#_Toc232859159)

[2.2 Roles 3](#_Toc232859160)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232859161)

[2.4 Business Conditions 4](#_Toc232859162)

[2.5 Preliminary Steps 5](#_Toc232859163)

[2.5.1 Display Activity Price with CO2e Emission Quantities 5](#_Toc232859164)

[2.5.2 Display Raw Material Price with CO2e Emission Quantities 6](#_Toc232859165)

[3 Overview Table 8](#_Toc232859166)

[4 Test Procedures 9](#_Toc232859167)

[4.1 Determine CO2e Emission Quantities for Manufactured Products 9](#_Toc232859168)

[4.2 Display CO2e Emission Quantities for Manufactured Products 11](#_Toc232859169)

[4.3 Release of CO2e Emission Quantities for Manufactured Quantities 12](#_Toc232859170)

## Purpose

Overview

This process enables you to post and analyze the quantity breakdown of greenhouse gas emissions (in carbon equivalents CO2e) for product-related scenarios. Emission quantities are allocated in alignment with the flow of costs throughout the company's value chain. You can gain insights into quantities of certain greenhouse gas emission scopes connected to financial attributes and values.

This scope item runs only in combination with the following mandatory prerequisite scope items that must be activated:

- Integrated Financial Planning (4RC)
- Import Connection Setup with SAP Analytics Cloud (1YB)
- Product Footprint Management (5IM)

This scope covers the business requirement of tracking greenhouse gas emissions in the form of carbon equivalent (CO2e) allocated to products that are sold to customers. As a result, the Product Costing area must be enhanced. The determination of total CO2e quantities for semi-finished and finished products is rolled up from retrieved emission quantities in the same way standard costs are rolled up for for manufactured products with BOMs and routings. The breakdown of greenhouse gas emission quantities in product costing applies to planning. The process must ensure quantity conversion - defining a quantity component for one base unit. This process enables you to post and analyze the quantity breakdown of greenhouse gas emissions (expressed in CO2e) for product-related scenarios. Emission quantities are allocated accordingly, following the flow of costs across a company's value chain. You can gain insight into the quantities of specific greenhouse gas emission scopes linked to financial attributes and values.

Before calculating CO2e emissions for semi-finished and finished products through Product Costing, the following prerequisites must be completed to retrieve the emission quantities associated with consumed materials from other tools such as SAP Sustainability Footprint Management and SAP Analytics Cloud (SAC). Activity rates, with CO2e emission quantities and other greenhouse gas attributes, are computed and transferred as a result of cost center planning in SAC.

- Raw material C02e emission quantities
- Cost center planned activity rate C02e emission quantities

During the calculation of material cost estimates, the CO2e emission quantities of finished and semi-finished goods are also factored into the cost. For details, see [https://me.sap.com/notes/3408777](https://me.sap.com/notes/3408777).

In the long term, the Universal Component Breakdown is the proposed solution to fulfill Transactional Carbon Accounting requirements, utilizing a bottom-up approach. For more information, see [https://help.sap.com/docs/SAP_S4HANA_CLOUD/6b39bd1d0e5e4099a5b65d835c29c696/71a6d231c4fd404ca73b6b8d320aad25.html?version=2402.500](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6b39bd1d0e5e4099a5b65d835c29c696/71a6d231c4fd404ca73b6b8d320aad25.html?version=2402.500).

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
| Administrator - Product Footprint Management | SAP_BR_ADMIN_SUS_PFM | Product Footprint Management | SAP_BR_ADMIN_SUS_PFM |  |
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Cost Center | * | All cost centers |  |
| Activity Types | * | All activity types | All activity types used in the routings / work centers of the materials to be calculated. |
| Material Master | * | Material type FERT, HALB, ROH | Select all materials which belong to this material type. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| 3KW | Create CO Cost RatesNote Ledger-specific material prices should be available (in 1ZT: Managing Material Price Changes and Inventory Values) if ledger-specific calculation is used. |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 4RC - Integrated Financial Planning | Financial Planning in SAP Analytics Cloud (SAC) has the CO2e emission quantities for activity cost rates for plan in measurement unit kilogram. This information is required as a basis for the business processes in SAP S/4HANA Cloud Public Edition to provide the CO2 Emission Quantity Breakdown.Get (Push) CO2 emission quantities from SAC for activity cost rates and take it over into SAP S/4HANA Cloud Public Edition table ACCOSTRATE.Note SAC story UCB_SAP_FI_IFP_IM_OPEX_ActivityCostRatePlanning_1 is used for data download from SAC. |
| 1YB - Import Connection Setup with SAP Analytics Cloud | Financial Planning in SAP Analytics Cloud (SAC) has the CO2e emission quantities for activity cost rates for plan in measurement unit kilogram. This information is required as a basis for the business processes in SAP S/4HANA Cloud Public Edition to provide the CO2 Emission Quantity Breakdown.Get (Push) CO2 emission quantities from SAC for activity cost rates and take it over into SAP S/4HANA Cloud Public Edition table ACCOSTRATE.Note SAC story UCB_SAP_FI_IFP_IM_OPEX_ActivityCostRatePlanning_1 is used for data download from SAC. |
| 5IM - Product Footprint Management | The SAP SFM (Sustainability Footprint Management) has the CO2e emission quantities for raw materials and trading goods in measurement unit kilogram. This information is required as a basis for the business processes in SAP S/4HANA Cloud Public Edition to provide the CO2 Emission Quantity Breakdown.Get (Push) CO2 emission quantities from SFM for raw materials and trading goods (request material number, plant, and supplier) and take it over into SAP S/4HANA Cloud Public Edition tables of Integration Component (for audit reasons or documentation of changes). |

|  |
| --- |
| Note If this scope 6VN - Product-Related Carbon Emission Quantities is activated with demo data, we supply CO2 demo data for cost rate and raw materials related to the finished product FG126. So, for testing purposes in SAP S/4HANA Cloud Public Edition with demo data, integration with 4RC/1YB and 5IM is not explicitly required, given that CO2 data is already updated as demo content. |

|  |
| --- |
| Note For more information, see [https://me.sap.com/notes/3408777](https://me.sap.com/notes/3408777) and [https://help.sap.com/docs/SAP_S4HANA_CLOUD/6b39bd1d0e5e4099a5b65d835c29c696/71a6d231c4fd404ca73b6b8d320aad25.html?version=2402.500](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6b39bd1d0e5e4099a5b65d835c29c696/71a6d231c4fd404ca73b6b8d320aad25.html?version=2402.500). |

### Preliminary Steps

#### Display Activity Price with CO2e Emission Quantities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you enter activity price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Rates - Plan (F3162). | The Manage Cost Rate - Plan screen displays. |  |
| 3 | Enter Variables | Make the following entries :Cost Center: 33101301Activity Type: 1Choose GoSelect the row and choose Component Breakdown. | The Edit Cost Rates screen displays. |  |
| 4 | Make Price Changes | In the dialog box, you can display the CO2 emission quantity that was updated via SAC integration. | Activity prices are posted for the fiscal year. |  |

#### Display Raw Material Price with CO2e Emission Quantities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This process step shows you how to search and view product footprints for a plant and product, or plant, product, and supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Administrator - Product Footprint Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open View Product Footprints (F5783). | The View Product Footprints screen displays. |  |
| 3 | View Product Footprints by Product | On the entry screen, select a product for which a product footprint has been published to SAP S/4HANA Cloud Public Edition for at least one plant. Choose Go. | A list showing one or multiple product footprints for the selected product displays. |  |
| 4 | View Product Footprints by Plants | On the entry screen, select a plant that has products assigned for which a product footprint has been published to SAP S/4HANA Cloud Public Edition.Choose Go. | A list showing one or multiple product footprints for the selected plant displays. |  |
| 5 | View Product Footprints by Filter Criteria | On the entry screen, select different filter criteria and combinations of the following filter criteria:● Product● Product Group● Plant● Supplier● Company Code● Quantity● Reference BasisChoose Go. | A list showing one or multiple product footprints according to the filter criteria displays. |  |

## Overview Table

This scope item consists of several process steps as provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Determine CO2e Emission Quantities for Manufactured Products](#unique_10) [page ] 9 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | The Manage Costing Runs Estimated Costs view displays and costing run is created. |
| [Display CO2e Emission Quantities for Manufactured Products](#unique_11) [page ] 11 | Cost Accountant - Inventory | Display Material Cost Estimates (CK13N) | The report presents itemization breakdown of product costs, and shows the CO2 quantity breakdown analysis. |
| [Release of CO2e Emission Quantities for Manufactured Quantities](#unique_12) [page ] 12 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | The Manage Costing Runs Estimated Costs view displays and costing run is executed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Determine CO2e Emission Quantities for Manufactured Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a costing run with CO2 emission quantity breakdown.

You can have separate standard product costing for each Ledger. The following table shows the combinations available in standard content:

|  |
| --- |
| Note Ledger-specific prices can be maintained in the material master within creation mode or via the Manage Material Valuations (F2680) app. |

| Costing Type | Ledger | Costing Variant | Valuation Variant | Costing Sheet | Impact |
| --- | --- | --- | --- | --- | --- |
| 01 | Blank - means update to all Ledgers | PPC1-Standard Cost Est. (Mat.) | 001 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 01 | Blank - means update to all Ledgers | PYC1-Cost Estimate Standard 0Y1 | 0Y1 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 01 | Blank - means update to all Ledgers | PYC2-Cost Estimate Plan 0Y2 | 0Y2 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 0L | 0L - only update to 0L | P00L-Legal Mat Cst Est Ldgr-0L | 00L | XXXXPC (XXXX represents default company code) | Will update Ledger 0L only |
| 2L | 2L - only update to 2L | P02L-Legal Mat Cst Est Ldgr-2L | 02L | XXXXPC (XXXX represents default company code) | Will update Ledger 2L (should use only when you have Ledger 2L in FI) |
| 3L | 3L - only update to 3L | P03L-Legal Mat Cst Est Ldgr-3L | 03L | XXXXPC (XXXX represents default company code) | Will update Ledger 3L (should use only when you have Ledger 3L in FI) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs - Estimated Costs view displays. |  |
| 3 | Creating Costing Run | Choose the Create button. | The Create New Costing Run view displays. |  |
| 4 | Enter Parameters for Costing Run | Make the following entries and choose Enter.Costing Run: Test1 (XX can be any number)Costing Run Date: <Enter the current date>Description: Costing Run Test1 (XX can be any number)Costing Variant: PYC1Note The ledger is updated based on the costing type mapped to the costing variant. Select per your business needs.Costing Version: 1Controlling Area: A000Company Code: 3310Costing Date From: <Enter the current date>Costing Date To: <Adopt the default value>Qty Structure Date: <Enter the current date>Valuation Date: <Enter the current date> |  |  |
| 5 | Save Costing Run | Choose the Save button. |  |  |
| 6 | Create Cost Estimates | Open the Process section. From the Selection row, choose the Change Parameter button and make the following entries:Material Type : HALB, ROH, FERTNote For testing purposes, enter material number FG126 instead of material type.Plant: 3310Select the Explode Multilevel Structure checkbox.Deselect Background Processing indicator and then choose Save.Choose Back and save the entries as required.Choose Execute, which displays in the Execute column, and the status light for the Selection row turns green. | The selection is executed. |  |
| 7 | Create Cost Estimates - Selection | From the Costing row, choose the Change Parameter button. On the Costing Run: Cost Estimate – Change Parameters view, deselect Background Processing indicator and then choose Save.Choose Back.Choose Execute, which displays in the Execute column and the status light for the Costing row turns green. | Costing Run is executed. |  |
| 8 | Create Cost Estimates - Costing | From the menu, in case the Edit is not visible directly, choose Menu > Edit > Costing Results .If the status light for this row is red, review the Costing levels report. Correct errors in the report. To re-run the costing (if necessary), repeat steps for Selection Struct. Explosion and Costing Rows. | Costing Run is executed. |  |
| 9 | Create Cost Estimates - Analysis | On the Analysis row, choose the Change Parameter button. Select SAP&11 for the parameter setting and then select Choose. On the Costing Run: Analysis - Change Parameters view, deselect Background Processing checkbox and then choose Save.Choose Back.Choose Execute, which displays in the Execute column.Choose Back and confirm the message with yes to leave the list. | Costing Run is executed. |  |

### Display CO2e Emission Quantities for Manufactured Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You can view material cost estimates calculated in previous steps, and the result of cost component split (based on the costing lot size) and costing itemization results by G/L accounts. This app includes CO2 quantity breakdown analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Material Cost Estimates (CK13N). | The Display Material Cost Estimate with Quantity Structure view displays. |  |
| 3 | Execute Report | Make the following entries and press Enter.Material: <enter a material, for example SG21>Note The material must have a valid costing run executed for the costing variant selected or the date of your costing run, for example, the first day of the next year as used in the Create Costing Run step.Plant: 3310Costing Variant: PYC1Costing Version: 1Valid On: <Enter the current date>Choose the UCB Component button. | The screen shows the itemization of CO2e emission quantities. |  |

### Release of CO2e Emission Quantities for Manufactured Quantities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you execute the costing run. Configured materials are not included.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs - Estimated Costs view displays. |  |
| 3 | Select Costing Run | Search for the costing run created in the previous step.Select the costing run and choose Edit. | The Edit Costing Run view displays. |  |
| 4 | Edit Costing Run | Make the desired changes and choose Continue. Save the changes as required. |  |  |
| 5 | Create Cost Estimates - Marking | On the Marking row, choose the Lock button.Note The allowance must be set for the period for which the price update is scheduled.On the Price Update: Organizational Measure view, select the company code 3310 row for the appropriate ledger 0L.In the Permitted Costing Variant dialog box, enter the costing variant of PYC1 and the costing version of 1, and then choose Issue allowance for marking. The status light of the row turns green.Choose Back.Choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute.Note Check the log and resolve error messages. Warning messages may also be potential problems later on in the process, so those need to be resolved as well. | Costing Run is executed.The following is an excerpt of potential messages:The messages Costing error for material SGPI*1 to 10: no BOM and routing and Costing error for material FG_FL*0 to FG_FL*2 : no BOM and routing are ok. These materials are sample master data for additional processes.In case no price could be determined for single-level material, the following message displays No price could be determined for material/batch PPPP plant XX10 (PPPP stands for Material number/XX stands for Country ID). For correction, refer to scope item 1ZT: Managing Material Price Changes and Inventory Values. |  |
| 6 | Create Cost Estimates - Release | On the Release row, choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute. | The current prices will be updated in the material master data.Note The new standard price cannot be updated before the first day of the validity of the costing run. For example, if costing run is valid from 01/01/<planning year>, then releasing the standard price is possible on 01/01/<planning year> at the earliest. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/product-footprint-management-5im-test-script-1104]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6VN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,355 chars in the whole document
