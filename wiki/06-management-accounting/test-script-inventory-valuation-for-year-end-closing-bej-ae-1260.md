---
id: 06-management-accounting/test-script-inventory-valuation-for-year-end-closing-bej-ae-1260
title: "Test Script: Inventory Valuation for Year-End Closing (BEJ_AE) (BEJ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item BEJ_AE: FIFO, lowest-value determination, balance sheet value and adjustment for year-end inventory valuation."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/inventory-valuation-and-actual-costing]
aliases: [BEJ_S4CLD2608_BPD_EN_AE]
keywords: [Inventory Valuation and Actual Costing, inventory valuation, year-end closing, fifo valuation, lowest value determination, range of coverage, movement rate, inventory costing, inventory balance sheet valuation, balance sheet value adjustment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BEJ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1260
topic: 06-management-accounting/inventory-valuation-and-actual-costing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Inventory Valuation for Year-End Closing (BEJ_AE) (BEJ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BEJ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Inventory Valuation and Actual Costing** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Inventory Valuation for Year-End Closing (BEJ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861374)

[2 Prerequisites 4](#_Toc232861375)

[2.1 System Access 4](#_Toc232861376)

[2.2 Roles 4](#_Toc232861377)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232861378)

[2.4 Business Conditions 6](#_Toc232861379)

[2.5 Preliminary Steps 6](#_Toc232861380)

[3 Overview Table 7](#_Toc232861381)

[4 Test Procedures 9](#_Toc232861382)

[4.1 FIFO Valuation 9](#_Toc232861383)

[4.1.1 Flag Materials as Relevant for FIFO 9](#_Toc232861384)

[4.1.2 Create FIFO Valuation Extract 10](#_Toc232861385)

[4.1.3 Execute FIFO Valuation 11](#_Toc232861386)

[4.1.4 Optional: Analyze Results with Inventory Balance Sheet Valuation 12](#_Toc232861387)

[4.2 Determine Lowest Value: Market Prices 13](#_Toc232861388)

[4.3 Optional: Execute Inventory Costing 15](#_Toc232861389)

[4.4 Optional: Analyze Results with Inventory Balance Sheet Valuation 18](#_Toc232861390)

[4.5 Determine Lowest Value: Range of Coverage 18](#_Toc232861391)

[4.6 Determine Lowest Value: Movement Rate 20](#_Toc232861392)

[4.7 Optional: Analyze Results with Inventory Balance Sheet Valuation 22](#_Toc232861393)

[4.8 Determine Inventory Balance Sheet Value 23](#_Toc232861394)

[4.9 Balance Sheet Value Adjustment 24](#_Toc232861395)

[4.9.1 Option 1: Execute Price Change 24](#_Toc232861396)

[4.9.1.1 Execute Price Change 24](#_Toc232861397)

[4.9.1.2 Analyze Results with Inventory Balance Sheet Valuation 26](#_Toc232861398)

[4.9.2 Option 2: Automatic FI Posting via Delta Run 27](#_Toc232861399)

[4.9.2.1 Perform Delta Posting 27](#_Toc232861400)

[4.9.2.2 Analyze Results with Inventory Balance Sheet Valuation 28](#_Toc232861401)

## Purpose

Overview

This scope item provides you with an example of a process description that you can use as a template for your valuation processes. Inventory valuation is performed in accordance with local legislation (such as the German Commercial Code), including settings for overhead structure, valuation variant, and stock valuation with devaluation based on movement rate.

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
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |

For details about the business role content, refer to the section Maintenance of Fiori Artefacts for SAP S/4HANA in the configuration guide Check S/4HANA Technical Settings (BG0).

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material master |  | Materials used for procurement and materials that are produced. For example materials with material type FERT/HALB/ROH/VERP/HAWA | No specific materials necessary, but transaction data must be available |
| Production master Data – BOM, Work center, routing |  | For all FERT and HALB data that is used for costing with quantity structure |  |
| Cost center | 33101201 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS) |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNJ | Create Production Work Center - MDS |
| BNL | Create Routing - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

|  |
| --- |
| Note For Demo purpose make sure there is enough goods receipt and goods issued. If the system is new, and not enough goods are posted, create demo data. For example, by posting material TG12, post other goods receipt of 300 EA and goods issued to cost center 100 EA. |

| Scope Item | Business Condition |
| --- | --- |
| BMD - Purchase Contract and/orJ45 - Procurement of Direct Materials | At least one of these scripts must be executed for this test. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing and/orBJ8 - Make-to-Stock – Process Manufacturing Based on Process Order and/orBJH - Make-to-Stock Production – Repetitive Manufacturing | Make-to-Stock Production – Discrete Manufacturing (for material FG126) and/orMake-to-Stock – Process Manufacturing Based on Process Order (for material FG29) and/orMake-to-Stock Production – Repetitive Manufacturing (for material SG21) |

### Preliminary Steps

First, check if purchase requisitions are available. If no purchase requisitions are available, perform the following steps:

- In case of material planned by reorder point planning: MRP does not create purchase requisitions or if the available quantity is bigger than the reorder point, in this case, reduce the stock of that material.
- In case of material planned by MRP type PD (MRP): MRP does not create purchase requisitions or if the available quantity is larger than the current requirements, in this case, create planned independent requirements.

## Overview Table

The scope item consists of several process steps provided in the table below.

Table 2: FIFO Valuation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Flag Materials as Relevant for FIFO](#unique_9) [page ] 9 | Cost Accountant - Inventory | Flag Materials for FIFO Valuation (MRF4) | Certain material are marked as relevant for alternative (FIFO) valuations. |
| [Create FIFO Valuation Extract](#unique_10) [page ] 10 | Cost Accountant - Inventory | Create FIFO Valuation Extract (MRF3) | Generates a report that displays documents relevant for FIFO evaluations. |
| [Execute FIFO Valuation](#unique_11) [page ] 11 | Cost Accountant - Inventory | Execute FIFO Valuation (MRF1) | Executes FIFO valuation and displays results. |
| [Optional: Analyze Results with Inventory Balance Sheet Valuation](#unique_12) [page ] 12 | Cost Accountant - Inventory | Inventory Balance Sheet Valuations (F3343) | Report shows lowest valuation by range of coverage for various criteria displays. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Determine Lowest Value: Market Prices](#unique_13) [page ] 13 | Cost Accountant - Inventory | Determine Lowest Value - Market Prices (MRN0) | Materials master records is updated with the lowest value of material type ROH and HAWA. |
| [Optional: Analyze Results with Inventory Balance Sheet Valuation](#unique_12) [page ] 12 | Cost Accountant - Inventory | Inventory Balance Sheet Valuations (F3343) | Report shows lowest valuation by range of coverage for various criteria displays. |
| [Determine Lowest Value: Range of Coverage](#unique_14) [page ] 18 | Cost Accountant - Inventory | Determine Lowest Value - Range of Coverage (MRN1N) | The system outputs an evaluation for each material. This evaluation specifies the price that is used. |
| [Determine Lowest Value: Movement Rate](#unique_15) [page ] 20 | Cost Accountant - Inventory | Determine Lowest Value - Movement Rate (MRN2N) | The system outputs an evaluation for each material. This evaluation specifies the price that is used. |
| [Optional: Analyze Results with Inventory Balance Sheet Valuation](#unique_12) [page ] 12 | Cost Accountant - Inventory | Inventory Balance Sheet Valuations (F3343) | Report shows lowest valuation by range of coverage for various criteria displays. |
| [Determine Inventory Balance Sheet Value](#unique_16) [page ] 23 | Cost Accountant - Inventory | Determine Inventory Balance Sheet Value (MRN9N) | The lowest value is determined and inventory balance sheet valuation is updated. |

Table 3: Balance Sheet Value Adjustment

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Option 1: Execute Price Change |  |  |  |
| [Execute Price Change](#unique_17) [page ] 24 | Cost Accountant - Inventory | Adjust Inventory Balance Sheet Accounts - Price Change (MRNP) | The posting is done and prices are updated in MM master record. |
| [Analyze Results with Inventory Balance Sheet Valuation](#unique_18) [page ] 26 | Cost Accountant - Inventory | Inventory Balance Sheet Valuations (F3343) | Valuation alternatives are reviewed. |
| Option 2: Automatic FI Posting via Delta Run |  |  |  |
| [Perform Delta Posting](#unique_19) [page ] 27 | Cost Accountant - Inventory | Adjust Inventory Balance Sheet Accounts - Delta Posting (MRND) | Posting is done. |
| [Analyze Results with Inventory Balance Sheet Valuation](#unique_18) [page ] 26 | Cost Accountant - Inventory | Inventory Balance Sheet Valuations (F3343) | Delta postings based on valuation alternative BSV is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item. The test should take around 40 minutes.

### FIFO Valuation

Context

FIFO valuation is a method that enables you to valuate the stocks of a material as realistically as possible. FIFO (first in, first out) uses the assumption that the first stocks of a material to be received are the first to be consumed. The value of the stock is calculated based on the last stocks received.

#### Flag Materials as Relevant for FIFO

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Executing this transaction code flags the materials selected in the First In, First Out (FIFO) run. Material Codes must be flagged for FIFO to be considered during the FIFO Valuation Run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Flag Materials for FIFO Valuation (MRF4). | The FIFO Valuation: Flag Materials Screen displays. |  |
| 3 | Data Entry | Make the following entries in the Restriction of Selection portion of the view:Material Type: ROH, HAWA and HALB, FERTCompany Code: 3310Plant: 3310Ensure that the Set button is selected in the LIFO/FIFO Indicator portion of the view.In the Update section, select the Material Master box.Select the Output Messages box in the Log portion of the view. |  |  |
| 4 | Run | Choose the Run button. | The materials specified in the selection criteria are marked as relevant for FIFO valuation. |  |

#### Create FIFO Valuation Extract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This procedure allows the system to select the transactions to be considered for First In, First Out (FIFO) Valuation. The selection uses the FIFO method defined, as well as the movement types defined as FIFO-relevant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FIFO Valuation Extract (MRF3). | The FIFO Valuation: Create Document Extra view displays. |  |
| 3 | Data Entry | In the Procedures section of the view, choose CURWSR method for the FIFO Method field.In the Restriction of Selection section of the view, make the following entries:Company Code: 3310Material: TG12In the Time Restrictions section of the view, select From Specified Period and enter the dates for the entire fiscal year for the Posting Date range selection.In the Update section of the screen, select the Receipt Data checkbox.In the Print List section of the screen, select the List Display checkbox. |  |  |
| 4 | Run | Choose the Run button. | A report generates that displays the documents relevant for FIFO valuation. |  |

#### Execute FIFO Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This activity enables the system to perform First In, First Out (FIFO) valuation. In this example, the FIFO inventory value must be lower than the current inventory value, as the system uses the lower of the two to determine whether revaluation is required.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Execute FIFO Valuation (MRF1). | The Execute FIFO Valuation view displays. |  |
| 3 | Enter Data | In the Procedures area of the view, choose method CURWSR for field FIFO Method.In the Restriction of Selection area of the view, make the following entries:Company Code: 3310Plant: 3310Material: TG12In the Comp. Lowest Values area of the view, select the Execute checkbox.In the Results area of the view, select the FIFO Price Table and Update Inventory Balance Sheet Valuations checkboxes.Choose the Update Prices button, choose the Valuation Alternatives tab, select the FIF FIFO Matl Ledger option. In Dynamic Period, use the dropdown to select Current Fiscal Period and choose Continue.Note The period is determined based on the combination of ledger and company code. | The necessary fields are completed as specified. |  |
| 4 | Run | Choose the Run button. | Results of the FIFO valuation display. |  |

#### Optional: Analyze Results with Inventory Balance Sheet Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This activity covers the process of analyzing the material prices. The price comparison report supplies the current stock values and the lowest stock value at various aggregation levels: material stock account, material type, and material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. |  |  |
| 2. | Access the SAP Fiori App | Open Inventory Balance Sheet Valuations (F3343). |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Posting Period: <MM>Year: <YYYY> |  |  |
| 4 | Go | In the Inventory Balance Sheet Valuations section, choose the (>) Detail button on any material to view material specific detail. | A report showing lowest value based on different valuation alternatives displays. Click on the alternative to view the corresponding valuation values. |  |

### Determine Lowest Value: Market Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The lowest value based on market prices should be determined. The system identifies the lowest price (or alternatively, the most recent price) from the various prices recorded for each material. This determination can be done at the material level or based on other criteria, such as the material type. The process steps are based on the material types.

|  |
| --- |
| Note This step applies only to externally procured materials. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Determine Lowest Value - Market Prices (MRN0). | The Determine Lowest Value: Market Prices view displays. |  |
| 3 | Valuation Level | Choose the Valuation Level button. In the Valuation Level dialog box that appears, select either valuation area or compamy code based on your requirements, and choose the Continue button. |  |  |
| 4 | Enter Selection Data | Make the following entries:Company Code: 3310Ledger: <for example, 0L>Key Date: <Enter Current Period End Date>Currency Type: <use the default>Plant: 3310Material Type: Choose the Multiple selection icon to enter the material types ROH, HAWA and choose the Copy button to continue. |  |  |
| 5 | Price Comparison | In the Price Comparison section, choose the Comparison Price button. | The Select a Comparison Price view appears. |  |
| 6 | Select Comparison Price Data | In the Relationship to Market Price section, select Lowest Val. Comparisn.In the Phys. Inventory Prices tab, select Current Material Price and Mat. Price Prev. Month checkboxes.In the Valuation Alternatives tab, select LMP LVMP Mat. Ledger. Make the following entry:From Posting Period: <current posting period and fiscal year> ORIn Dynamic Period, use the dropdown to select Current Fiscal PeriodChoose Continue. |  |  |
| 7 | Enter Data and Run | In the Results section, select Update Inventory Balance Sheet Valuations.In the Print List section, select List Output.Choose the Run button to determine the lowest value. | The system displays a warning saying that you have not entered a material number interval.If you have large volumes of material master data, enter a material number interval.You could search material number using the Material by Material Type option. The system outputs an evaluation for each material. This evaluation specifies the price that is used as the comparison price and shows whether a new price was determined for the valuation. |  |

### Optional: Execute Inventory Costing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create cost estimates for finished and semifinished products. These products use the lowest market cost for the components (such as raw materials, activity rates, and overheads) and stores the estimates for the balance sheet.

For finished goods, a multilevel cost estimate combines the adjusted raw material values and the lowest activity rate to provide an alternate conservative cost of goods manufactured for balance sheet purposes. You can use this estimate to make adjustments to the balance sheet to lower the stated inventory values.

Inventory costing and standard costing use the same basic mechanism. However, inventory costing requires a separate costing variant to determine the valuation values and where to update the values with the valuation alternative based on strategy sequence V.

Our predelivered content comes with the following values for inventory valuation:

Table 4:

| Ledger | Costing Variant | Valuation Variant | Costing Type | Valuation Alternative |
| --- | --- | --- | --- | --- |
| 0L | PYYL | YYL | YL | LMP |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Creating Costing Run | Choose the Create button. | The Create New Costing Run view displays. |  |
| 4 | Enter Parameters for Costing Run | Make the following entries and choose Enter.Costing Run: Test1Costing Run Date: <Enter the current date>Description: Costing Run Test1Costing Variant: PYYLNote This variant is valid for ledger 0L.Costing Version: 1Controlling Area: A000Company Code: 3310Costing Date From: <Enter the first day of next year>Costing Date To: Adopt default valueQty Structure Date: <Enter the first day of next year>Valuation Date: <Enter the first day of next year> |  |  |
| 5 | Save Costing Run | Choose the Save button. |  |  |
| 6 | Select Costing Run | Search for the costing run created in the previous step.Select the costing run and choose Edit. | The Edit Costing Run view displays. |  |
| 7 | Create Cost Estimates - Selection | Open the Process section. From the Selection row, choose the Change Parameter button and make the following entries:Material Type : <any semifinished or finished product, for example FG126>Plant: 3310Select the Explode Multilevel Structure checkbox.Deselect Background Processing indicator and then choose Save.Choose Back and save the entries as required.Choose Execute, which displays in the Execute column, and the status light for the Selection row turns green. | The selection is executed.Note Make sure all the previous steps are executed and prices are available in valuation alternative LMP (configured in costing variant PYYL for Ledger 0L) for all raw materials used in BOM for costed material, otherwise you would get errors for missing prices. |  |
| 8 | Create Cost Estimates - Costing | From the Costing row, choose the Change Parameter button. On the Costing Run: Cost Estimate – Change Parameters view, deselect Background Processing indicator and then choose Save.Choose Back.Choose Execute, which displays in the Execute column and the status light for the Costing row turns green. | Costing Run is executed. |  |
| 9 | Create Cost Estimates - Analysis | On the Analysis row, choose the Change Parameter button. Select SAP&11 for the parameter setting and then select Choose. On the Costing Run: Analysis - Change Parameters view, deselect Background Processing checkbox and then choose Save.Choose Back.Choose Execute, which displays in the Execute column.Choose Back and confirm the message with yes to leave the list. | Costing Run is executed. |  |
| 10 | Create Cost Estimates - Price Update | On the Price Update row, choose the Change Parameter button.In the Update of Valuation Alternative section, select the Valuation Alternative checkbox, and enter valuation alternative INC. Also, make the following entries:Fiscal Year: <current year>Posting Period: <current period>CostCompView: <Search and select 06-Inventory Valuation>Under Processing Options, deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute. | Costing Run is executed. |  |

### Optional: Analyze Results with Inventory Balance Sheet Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This activity covers the process of analyzing the material prices. The price comparison report supplies the current stock values and the lowest stock value at various aggregation levels: material stock account, material type, and material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. |  |  |
| 2. | Access the SAP Fiori App | Open Inventory Balance Sheet Valuations (F3343). |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Posting Period: <MM>Year: <YYYY> |  |  |
| 4 | Go | In the Inventory Balance Sheet Valuations section, choose the (>) Detail button on any material to view material specific detail. | A report showing lowest value based on different valuation alternatives displays. Click on the alternative to view the corresponding valuation values. |  |

### Determine Lowest Value: Range of Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This activity helps you determine the lowest value based on range of coverage. In the determination of lowest value by range of coverage, you can define which deduction percentages should apply by company code/valuation area, material type, and any range of coverage intervals. The determination can be done at material level or based on other selections, for example the material type used. This process step is based on material types.

|  |
| --- |
| Note Devaluation based on range of coverage has demo data in cloud content. You can maintain their own devaluation percentage via the configuration activity Maintain Devaluation Percentage by Range of Coverage. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori App | Open Determine Lowest Value - Range of Coverage (MRN1N). | The Determine Lowest Value: Range of Coverage view displays. |  |
| 3. | Enter Data | In the Selection section, make the following entries:Company Code: 3310Plant: 3310In the Determine Range of Coverage section, make the following entries:Valuation Alternative: ROC (Select from the Search icon)Note You can now do this step by ledger. Valuation alternatives, for example, R0L, R2L, R3L can be created with respective ledger combination via the configuration activity Set Up Valuation Alternatives.Period To: <MM/YYYY>Number of Period back: 1Valuation Level: <Select valuation level per your requirement>Note We support the company code valuation level for lowest value determination based on range of coverage, movement rates, and market prices. |  |  |
| 4. | Enter Data | In the Base Price Lowest of section, make the following entries,Inventory Price: Select the checkboxValuation Alternative: Select a valuation alternative other than ROC |  |  |
| 5. | Enter Data | In the Results section:Update Inventory Balance Sheet Valuations: Select the checkboxList Output: Select the checkbox |  |  |
| 6. | Enter Data | Make the following entries:Material Type: ROH, HAWA, FERT, HALBNote Choose the Multiple Selection icon to enter the material types and choose the Copy button to continue. |  |  |
| 7. | Run | Choose the Run button to determine the lowest value. | The system outputs an evaluation for each material. This evaluation specifies the price that is used. |  |

### Determine Lowest Value: Movement Rate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This activity helps you determine the lowest value based on rate of movement. In the determination of lowest value by movement rate, the system determines a devaluation indicator. The devaluation indicator is based on a proportion between total consumption and/or total receipt and stock. If the proportion is less or equal a threshold, the devaluation indicator will be increased. The deduction percentage will be derived based on the devaluation indicator. The determination can be done at material level or based on other selections, for example, the material type used. This process step is based on material types.

|  |
| --- |
| Note Devaluation based on movement rate has demo data in cloud content. You can maintain their own devaluation percentage via the configuration activity Maintain Devaluation Percentage by Movement Rate. Depending on your configuration environment, the configuration activity can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. |  |  |
| 2 | Access the SAP Fiori App | Open Determine Lowest Value - Movement Rate (MRN2N). | The Determine Lowest Value: Movement Rate view displays. |  |
| 3 | Enter Data | In the Selection section, make the following entries:Company Code: 3310Plant: 3310In the Determine Movement Rate section, make the following entries:Valuation Alternative: LMR (Select from the Search icon)Note You can now do this step by ledger. Valuation alternatives, for example, G0L, G2L, G3L can be created with respective ledger combination via the configuration activity Set Up Valuation Alternatives.Period To: <MM/YYYY>Number of Period back: 1Valuation Level: <Select valuation level per your requirement>Note We support the company code valuation level for lowest value determination based on range of coverage, movement rates, and market prices.Consumption Divided by Stock (%) Less or Equal Than: <numeric value between 0 and 99>Receipt Divided by Stock (%) Less or Equal Than: <numeric value between 0 and 99>Note At least one of the last two fields must have an entry, though both may be used at the same time. |  |  |
| 4 | Enter Data | In the Base Price Lowest of section, make the following entries,Inventory Price: Select the checkboxValuation Alternative: Select a valuation alternative other than LMR |  |  |
| 5 | Enter Data | In the Results section:Update Inventory Balance Sheet Valuations: Select the checkbox |  |  |
| 6 | Enter Data | Make the following entries:Material Type: ROH, HAWA, FERT, HALBNote Choose the Multiple Selection icon to enter the material types and choose the Copy button to continue. |  |  |
| 7 | Run | Choose the Run button to determine the lowest value. | The system outputs an evaluation for each material. This evaluation specifies the price that is used. |  |

### Optional: Analyze Results with Inventory Balance Sheet Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This activity covers the process of analyzing the material prices. The price comparison report supplies the current stock values and the lowest stock value at various aggregation levels: material stock account, material type, and material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. |  |  |
| 2. | Access the SAP Fiori App | Open Inventory Balance Sheet Valuations (F3343). |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Posting Period: <MM>Year: <YYYY> |  |  |
| 4 | Go | In the Inventory Balance Sheet Valuations section, choose the (>) Detail button on any material to view material specific detail. | A report showing lowest value based on different valuation alternatives displays. Click on the alternative to view the corresponding valuation values. |  |

### Determine Inventory Balance Sheet Value

Use

This step updates the valuation alternatives.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Determine Inventory Balance Sheet Value (MRN9N). | The Determine Inventory Balance Sheet Value view displays. |  |
| 3 | Enter Data | Make the following entries:Company Code: 3310Plant: 3310Material Type: ROH, HALB, HAWA, FERT |  |  |
| 4 | Determine Balance Sheet Value | Enter the following:Currency Type: 10Valuation Alternative: BSVNote You can now do this step by Ledger. Valuation alternatives, for example, B0L, B2L, B3L can be created with respective ledger combination via SSCUI Set Up Valuation Alternatives (102600).Period/Year: <enter a period and year> ORIn Dynamic Period, use the dropdown to select Current Fiscal PeriodInventory Value: <select the checkbox>Update Inventory Balance Sheet Valuations: <select the checkbox>Filter Options:Note If you select Only stocks > 0, only materials with stock greater than zero are displayed. If you select Devaluations Only, only materials with a devaluation amount are included in the results. |  |  |
| 5 | Run | Choose the Execute button. If warning messages appear, choose Enter to confirm.Note To display the logs, select Messages. In the Analyze Application Log view, choose the Execute button. | The lowest value is determined and inventory balance sheet valuation is updated. |  |

### Balance Sheet Value Adjustment

#### Option 1: Execute Price Change

##### Execute Price Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

With this activity, you can directly update the price change of inventory based on valuation alternatives.

Prerequisites

- Material valuation
- Stocks
- Evaluation by material stock account only in the case of system integration (account determination) with FI
- Physical inventory

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Adjust Inventory Balance Sheet Accounts - Price Change (MRNP). | The Adjust Balance Sheet Accounts - Price Change view displays. |  |
| 3 | Enter Data | Make the following entries and choose Enter:Company Code: 3310Plant: 3310Material Type: ROHIn the Price Change from Valuation Alternative section, make the following entries:Valuation Alternative: BSVNote You can do this step by ledger. Valuation alternatives, for example, B0L, B2L, B3L can be created with respective ledger combination via the configuration activity Set Up Valuation Alternatives.Period/Year: <enter a period and year>Price carried over: <selected automatically>Header Text: <enter a header text> |  |  |
| 4 | Run | Choose the Run button. If warning messages appear, choose Enter to confirm.Note To display the logs, select Messages. In the Analyze Application Log view, choose the Execute button. | The posting is done and prices are updated in MM master record. |  |

##### Analyze Results with Inventory Balance Sheet Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This activity covers the process of analyzing the material prices. The price comparison report supplies the current stock values and the lowest stock value at various aggregation levels: material stock account, material type, and material.

Prerequisites

• Material valuation

• Stocks

• Physical inventory

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. |  |  |
| 2. | Access the SAP Fiori App | Open Inventory Balance Sheet Valuations (F3343). | The Adapt Filters screen displays. |  |
| 3 | Enter Data | Make the following entries,Company Code: 3310Fiscal Period: <MM>Fiscal Year: <YYYY>Plant: 3310Valuation Alternative: BSV | The report presents the balance sheet values for each account, subdivided into valuation areas and material numbers. |  |
| 4 | Go | When done, choose Go. | A report showing lowest value based on different valuation alternatives displays. Click on the alternative to view the corresponding valuation values. |  |

#### Option 2: Automatic FI Posting via Delta Run

##### Perform Delta Posting

Use

The price comparison report supplies the current stock values and the lowest stock value at various aggregation levels: material stock account, material type, and material. The difference between the stock values can then be posted in FI as a stock value adjustment.

Prerequisites

- Material valuation
- Stocks
- Evaluation by material stock account only in the case of system integration (account determination) with FI
- Physical inventory

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Adjust Inventory Balance Sheet Accounts - Delta Posting (MRND). | The Adjust Balance Sheet Accounts - Delta Posting view displays. |  |
| 3 | Enter Data | Make the following entries:Company Code: 3310Plant: 3310Material Type: ROH |  |  |
| 4 | Delta Posting | Enter the following:Valuation Alternative: BSVNote You can now do this step by Ledger. Valuation alternatives, for example, B0L, B2L, B3L can be created with respective ledger combination via SSCUI Set Up Valuation Alternatives (102600).Period/Year: <enter a period and year> ORIn Dynamic Period, use the dropdown to select Current Fiscal PeriodHeader Text: <enter a header text>Reverse in Subsequent Period: <select the checkbox> | The Assignment: Prices to Valuation Levels view appears. |  |
| 5 | Run | Choose the Run button. If warning messages appear, choose Enter to confirm.Note To display the logs, select Messages. In the Analyze Application Log view, choose the Execute button. | The posting is done. |  |

##### Analyze Results with Inventory Balance Sheet Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This activity covers the process of analyzing the material prices. The price comparison report supplies the current stock values and the lowest stock value at various aggregation levels: material stock account, material type, and material.

Prerequisites

• Material valuation

• Stocks

• Physical inventory

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. |  |  |
| 2. | Access the SAP Fiori App | Open Inventory Balance Sheet Valuations (F3343). | The Adapt Filters screen displays. |  |
| 3 | Enter Data | Make the following entries,Company Code: 3310Fiscal Period: <MM>Fiscal Year: <YYYY>Plant: 3310Valuation Alternative: BSV | The report presents the balance sheet values for each account, subdivided into valuation areas and material numbers. |  |
| 4 | Go | When done, choose Go. | A report showing lowest value based on different valuation alternatives displays. Click on the alternative to view the corresponding valuation values. |  |

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
- related-to :: [[06-management-accounting/managing-material-price-changes-and-inventory-values-1zt-ae-test-scrip]]
- related-to :: [[06-management-accounting/test-script-actual-costing-33q-ae-sap-s-4hana-cloud-public-edition-903]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BEJ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 47,024 chars in the whole document
