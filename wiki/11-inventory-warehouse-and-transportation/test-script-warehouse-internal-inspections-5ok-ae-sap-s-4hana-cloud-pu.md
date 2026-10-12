---
id: 11-inventory-warehouse-and-transportation/test-script-warehouse-internal-inspections-5ok-ae-sap-s-4hana-cloud-pu
title: "Test Script: Warehouse Internal Inspections (5OK_AE) - SAP S/4HANA Cloud Public Edition (5OK_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5OK_AE: warehouse internal inspections, inspection lots, usage decisions, warehouse tasks, repacking."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-internal-inspections]
aliases: [5OK_S4CLD2608_BPD_EN_AE]
keywords: [Warehouse Internal Inspections, inspection lot creation, usage decision, warehouse tasks, ad-hoc warehouse task, recurring batch inspection, handling unit repacking, mobile rf devices, batch master data, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OK_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1116
topic: 11-inventory-warehouse-and-transportation/ewm-internal-inspections
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warehouse Internal Inspections (5OK_AE) - SAP S/4HANA Cloud Public Edition (5OK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warehouse Internal Inspections** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Internal Inspections (5OK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856957)

[2 Prerequisites 4](#_Toc232856958)

[2.1 System Access 4](#_Toc232856959)

[2.2 Roles 4](#_Toc232856960)

[2.3 Additional Manual Configuration 4](#_Toc232856961)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232856962)

[2.5 Business Conditions 6](#_Toc232856963)

[2.6 Preliminary Steps 7](#_Toc232856964)

[2.6.1 Create Batch 7](#_Toc232856965)

[3 Overview Table 9](#_Toc232856966)

[4 Test Procedures 11](#_Toc232856967)

[4.1 Create Inspection Lot 11](#_Toc232856968)

[4.1.1 Alternative 1 – Create Inspection Lot with the Warehouse Monitor 11](#_Toc232856969)

[4.1.2 Alternative 2 – Create Inspection Lot with the Mobile RF Device 12](#_Toc232856970)

[4.1.3 Alternative 3 – Create Inspection Lot with the Report Change Stock Attributes 14](#_Toc232856971)

[4.1.4 Alternative 4 – Create Inspection Lot for Batches with the Background Job 15](#_Toc232856972)

[4.2 Create Ad-Hoc Warehouse Task 17](#_Toc232856973)

[4.3 Confirm Warehouse Tasks 18](#_Toc232856974)

[4.3.1 Variant 1: With Fiori App 19](#_Toc232856975)

[4.3.2 Variant 2: With Radio Frequency Device 19](#_Toc232856976)

[4.4 Make Usage Decision 21](#_Toc232856977)

[4.5 Repack Handling Units (Optional) 24](#_Toc232856978)

[4.6 Create Ad-Hoc Warehouse Task (Optional) 26](#_Toc232856979)

[4.7 Confirm Warehouse Tasks 28](#_Toc232856980)

[4.7.1 Variant 1: With Fiori App 28](#_Toc232856981)

[4.7.2 Variant 2: With Radio Frequency Devices 29](#_Toc232856982)

[5 Appendix 32](#_Toc232856983)

[5.1 Process Integration 32](#_Toc232856984)

[5.1.1 Preceding Processes 32](#_Toc232856985)

[5.1.2 Succeeding Processes 32](#_Toc232856986)

## Purpose

Overview

During the storage of goods, a warehouse clerk may identify damage that must be checked and investigated. To follow up, the material is posted to quality inspection stock and an inspection lot is created automatically. The quality engineer inspects the material and makes a usage decision that triggers the posting of the material, for example, to unrestricted stock, to blocked stock, or to scrap.

For batch managed material, a recurring inspection can be set up based on, for example, the next inspection date. With background jobs, inspection lots can be created and inspected on a regular basis.

|  |
| --- |
| Note Since SAP S/4HANA 2111 Cloud Essentials edition, the following changes apply to this process:A Quality Area / Quality Work Center is provided in the warehouse for quality inspection, as opposed to the Clarification Area.Automatic putaway Warehouse Task creation is enabled for Usage Decision with an acceptance usage code.Existing customers do NOT get the changes by upgrade and the process works as it was before. For more information, please see chapter 2.3 [Additional Manual Configuration](#unique_2) [page ] 4. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/87807ffd176c4dbca23d97ff1ec0705c.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |

### Additional Manual Configuration

Before you start the testing, make sure that the steps in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on SAP Activate Roadmap Viewer are completed.

If you are working with a radio frequency device, carry out the steps described in Mobile RF Devices in Warehousing (63V).

|  |
| --- |
| Caution Since SAP S/4HANA Cloud Public Edition 2111, the following changes apply to this process:A Quality Area / Quality Work Center is available for processing Inspection Lots.Automatic putaway Warehouse Task creation is enabled for Usage Decision with an acceptance usage code.Customers who implement this Scope Item as of SAP S/4HANA Cloud Public Edition 2111 will be able to run the process with the changes mentioned above. However, customers who implemented this Scope Item prior to SAP S/4HANA Cloud Public Edition 2111 do not get the changes by upgrade and the process works as it was before. If you want to also apply the changes to the process, implement the following steps from the Warehouse Management Setup Guide:Specify Storage Type Search Sequence for PutawayMaintain Follow-Up ActionsCreate Storage Bin for Quality Area |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | QM001 | QM Regular |  |
| Material | QM007 | Warehouse Recurring Inspection, Batch |  |
| Packaging Material | PMPALLET | Pallet |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purchase Organization 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 335W | Storage Location for Cloud WM |  |
| ERP Warehouse | 335 | Warehouse |  |
| EWM Warehouse | 3350 | Warehouse |  |
| Division | 00 | Product Division 00 |  |
| Distribution Channel | 10 | Direct Sales |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| All Scope Items |  |
| 3M0 - Quality Management in Warehousing | This scope item is used as a predecessor.Follow the process steps described in the part Quality Management in Warehousing (from Supplier) of the test script to procure, inspect and put away the product into the warehouse.Note For product QM007, inspection result recording is not required in the process. |

### Preliminary Steps

#### Create Batch

Purpose

Manual adjustment is needed for batch master data. The batch master is created during goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Batch (MSC2N). | The Change Batch screen displays. |  |
| 3 | Select a Batch | On the Change Batch screen, make the following entries.Material : QM007Batch: Batch Number, e.g. 0000000002Plant: 3310If the batch number is not known search via the search help in the batch number field.Choose Continue. | The batch master of batch number for material TG22 displays. |  |
| 4 | Change the Batch Master Record | On the Change Batch screen, make the following entries.Go to Basic Data 1 tab:Date of Manufacture: Current dateNext Inspection: A date in the futureSupplier Batch: Supplier Batch NumberPress Enter.A pop up is opened that the best-before date is recalculated. Confirm that the new best-before date should be adopted in the item.Choose Yes.Go to Basic Data 2 tab:Short Text: TEXT | The batch master record has been changed. |  |
| 5 | Add Batch to Worklist | Choose Add batch to worklist.The system have a pop-up information Batch was copied to the standard folder in the worklist.Choose Continue. | The batch has been assigned to the standard folder in the worklist for later processing. |  |
| 6 | Save Your Entries | Choose Save. | Changing batch 0000000XXX. |  |
| 7 | Display Stock Overview (Original) | Choose Menu > Environment > Current Stock .To display the Stock Overview, you need further authorizations that should be granted by your company, e.g. the Inventory Manager. | The stock overview for the given batch displays. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Alternative 1 – Create Inspection Lot with the Warehouse Monitor](#unique_11) [page ] 11 | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) |  |
| [Alternative 2 – Create Inspection Lot with the Mobile RF Device](#unique_12) [page ] 12 | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) |  |
| [Alternative 3 – Create Inspection Lot with the Report Change Stock Attributes](#unique_13) [page ] 14 | Warehouse Clerk (EWM) | Change Stock Attributes (/SCWM/STOCK_ATT_CHG) |  |
| [Alternative 4 – Create Inspection Lot for Batches with the Background Job](#unique_14) [page ] 15 | Warehouse Clerk (EWM) | Schedule Stock Attribute Changes (F5506) |  |
| [Create Ad-Hoc Warehouse Task](#unique_15) [page ] 17 | Warehouse Clerk (EWM) | Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) | Warehouse tasks are created. |
| [Confirm Warehouse Tasks](#unique_16) [page ] 18 |  |  | Warehouse tasks for putaway are processed. |
| [Variant 1: With Fiori App](#unique_17) [page ] 19 | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) |  |
| [Variant 2: With Radio Frequency Device](#unique_18) [page ] 19 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Make Usage Decision](#unique_19) [page ] 21 | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is made. System creates follow-up warehouse taks. |
| [Repack Handling Units (Optional)](#unique_20) [page ] 24 | Warehouse Operative (EWM) | Pack Outbound Deliveries (F3193) | Handling units are repacked. |
| [Create Ad-Hoc Warehouse Task (Optional)](#unique_21) [page ] 26 | Warehouse Clerk | Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) | Ad-hoc warehouse task is created. |
| [Confirm Warehouse Tasks](#unique_16) [page ] 18 |  |  | The following system messages appear:Warehouse task xxx is to be confirmed Warehouse task xxx was confirmed |
| [Variant 1: With Fiori App](#unique_22) [page ] 28 | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) |  |
| [Variant 2: With Radio Frequency Devices](#unique_23) [page ] 29 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |

## Test Procedures

### Create Inspection Lot

In this chapter, you find the three alternatives to create an inspection lot.

#### Alternative 1 – Create Inspection Lot with the Warehouse Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk (EWM) selects physical stock in the Warehouse Monitor (/SCWM/MON) and creates an inspection lot for it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM) | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Warehouse Monitor (/SCWM/MON). | The Warehouse Monitor (/SCWM/MON) dialog box appears. |  |
| 3 | Enter Warehouse Number | On the Warehouse Management Monitor dialog box, make the following entries:Warehouse Number: <your warehouse number>Choose Execute. | The Warehouse Management Monitor SAP - Warehouse Number xxx screen appears. |  |
| 4 | Navigate to Physical Stock | On the Warehouse Management Monitor SAP - Warehouse Number xxx screen, choose Stock and Bin > Physical Stock. |  |  |
| 5 | Display Available Stock | Choose the node Physical Stock by double-clicking on it. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 6 | Enter Product | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:ExampleProduct: QM001 |  |  |
| 7 | Choose Execute | On the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, choose Execute. | The Physical Stock is displayed. |  |
| 8 | Create Inspection Lot | Select one or several stock items.Choose More Methods > Create Insp. (IOT5). |  |  |
| 9 | Enter Exception Code | On the Exception for Inspection Creation dialog box, make the following entries:Exception Code: CRID – Create InspectionChoose Continue. | A message log shows:Quality inspection XXXXXXXX createdWarehouse task XXXXXXXX createdStock XXXX QM001 has been processed successfullyNote down the Inspection Lot number. The Posting Change Warehouse task has been created and confirmed and the Stock Type has been changed to Q – Quality Inspection. |  |

#### Alternative 2 – Create Inspection Lot with the Mobile RF Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Operative (EWM) selects stock in the Mobile RF Device and creates an inspection lot for it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI). | The Warehouse Monitor(/SCWM/MON) dialog box appears. |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 05 Internal Process > 04 Quality Management > 01 Production Inspection > 02 Prod. Insp. By Bin.. |  |  |
| 5 | Enter Storage Bin | Make the following entries:Storage Bin: <the storage bin where the product to be inspected is stored>Choose Enter. |  |  |
| 6 | Enter Product Information | Make the following entries:Product: QM001 or QM007Batch: batch number (only applicable for batch managed product.E.g. QM007) |  |  |
| 7 | Choose Exception Code | Choose > next to the Back.Choose Except > 1. Create Inspection | An inspection lot has been created. You can check the Q stock and corresponding inspection lot number in the chosen storage bin via the Warehouse Monitor. |  |
| 8 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save. |  |  |

#### Alternative 3 – Create Inspection Lot with the Report Change Stock Attributes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk (EWM) creates inspection lots with a report for the stock items that have certain attributes. For example, when a goods receipt date is earlier than a certain date, or an expiration data is close to the current date. You can check relevant information in the Warehouse Monitor (/SCWM/MON).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Change Stock Attributes (/SCWM/STOCK_ATT_CHG). | The Change Stock Attributes (/SCWM/STOCK_ATT_CHG) screen appears. |  |
| 3 | Enter Parameters | On the Change Stock Attributes screen, make the following entries:Mode: Create Insp. and Post Stock to QM StockWarehouse Number: <your warehouse number>Product: QM001Goods Receipt Date: <Date from> to <Date to>Storage Type: <Storage Type>Storage Bin: <Storage Bin>Note The GR date, Storage Type, and Storage Bin are examples of conditions that are used for filtering stock.Target Stock Type : QException Code: CRIDSimulate: selectChoose Execute.Check the results of the simulated run. If necessary, adjust the conditions.Deselect the Simulate checkbox and execute. | The Posted stock results - Whse xxxx screen appears. |  |
| 4 | Check Results | On the the Posted stock results - Whse xxxx screen, check the results.Note down the inspection lot number shown in the Quantity Insp. field. |  |  |

#### Alternative 4 – Create Inspection Lot for Batches with the Background Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk (EWM) schedules a background job to create inspection lots in periodical intervals for stock, based on the batch attribute ‘Next Inspection Date’. This is used for the recurring inspection of batches in the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Schedule Stock Attribute Changes (F5506). | The Application Jobs screen appears. |  |
| 3 | Create Job | On the Application Jobs screen, choose Create. |  |  |
| 4 | Select Template | On the New Job: Application Job Template for Change Stock Attribute screen, in the 1. TemplateSelection section, make the following entries:Job Template: Application Job Template for Change Stock AttributeJob Name: e.g Job for Change Stock Attribute - Batch InspectionChoose Step 2. |  |  |
| 5 | Enter Schedule Options | In the 2. Scheduling Options section, choose Start Immediately.Note You can define the start time and recurrence pattern of your own preference. For testing purpose, you can enter Start Immediately.Choose Step 3. |  |  |
| 6 | Enter Parameters | In the 3. Parameters section, make the following entries:Mode: Create Insp. and Post Stock to QM StockWarehouse Number: <your warehouse number>Product: QM007Choose Refresh.Note You need to choose Check for certain fields to become the input ready.Consider Next InspDate (Batch): SelectChoose Check.Offset in Days (+/- Today): <Number in Days>. E.g.10Note You need to make sure the next inspection date falls into the period <current date + Offsetting days>.Target Stock Type : QException Code: CRIDSimulate: deselectChoose Schedule. | The Application Jobs screen appears. |  |
| 7 | Check Job Status | On the Application Jobs screen, the application job is created with status In Process. You can choose GO to refresh the list until the status turns to Finished. |  |  |
| 8 | Find the Inspection Lot numbers | Choose Navigate to the job results to find the inspection lot number. | Note down the inspection lot number. |  |

### Create Ad-Hoc Warehouse Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) creates ad hoc warehouse task(s) to move the stock to the quality bin.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Open the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open SAP Fiori Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT). | The Create Product Warehouse Tasks(/SCWM/MONNAV_CR_P_WT) screen displays. |  |
| 3 | Decide your filter criteria | Enter Product: For example, QM001 or QM007 (Batch material).Choose Execute. | The Create Product Warehouse Task screen displays. |  |
| 4 | Choose your Stock | Choose one of the stock lines and selectMore Methods > Create Warehouse Task. | The Create Warehouse Task dialog box (that requests for data) is displayed. |  |
| 5 | Create Warehouse Task | Create the warehouse task and enter the following data:Src Trgt Qty AUoM (Quantity): For example, 12Whse Proc. Type: S999Destination Bin: For Example CL-AREAThe Destination Storage Type is automatically filled in, for example S970.Note Since the SAP S/4HANA 2111 Cloud Essentials edition, you can use QUAL-I01 as the Destination Bin and S820 as the Destination Storage Type. For more information, see chapter [Additional Manual Configuration](#unique_2) [page ] 4.Choose Create WT. | The warehouse task is created, as you can see in the display log. A Warehouse Task List is automatically printed in the background. |  |
| 6 | Complete the step | Note down the warehouse task and warehouse order number.Choose Continue to close the log and then choose Home. Repeat the steps, if necessary. |  |  |

### Confirm Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Putaway List is printed and handed over to the Warehouse Operative (EWM). He or she performs the warehouse tasks and confirms them in the system.

You can also confirm warehouse tasks using the app Warehouse Monitor (/SCWM/MON) (Business Catalog WM – Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Process Warehouse Tasks (F4595) . |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the check box for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed. |  |

#### Variant 2: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with mobile Radio Frequency device.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-970 or SI-820Note It is likely that in the System-Guided Selection certain unfinished warehouse activities may appear instead of the expected task. If this is the case, choose > 01 Putaway by WO and enter the corresponding WO number in the Whse Order field to process the task.Choose Enter. |  |  |
| 6 | Create Picking HU (Optional) | Make the following entries:Pack.Mat: PMPALLETChoose Handling.The picking HU is created.Note Go directly to step 7, if picking HU is not required. |  |  |
| 7 | Choose Next | Scroll the screen to right with > and choose Next. |  |  |
| 8 | Enter or Verify the Source Information fields | Enter or Verify the following fields if they are required:Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)Choose Enter. |  |  |
| 9 | Verify the Destination information fields | Verify the following fields:DstBin (Destination Bin)Choose Enter. |  |  |
| 10 | Repeat Steps | Repeat steps 6 to 9 until no suitable warehouse orders are found. |  |  |
| 11 | Logoff RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save. |  |  |

### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

|  |
| --- |
| Note In this process the inspection result recording is not described. If you would like to do it, follow this setup to enable the inspection result recording based on task lists:Create your own material with corresponding QM setup as described in the BNY Master Data ScriptInspection Type 08 - Stock transfer inspection for material used in Alternative 1 & 2Inspection Type 09 - Recurring Inspection of Batches for material used in Alternative 3Create an Inspection Plans with usage 9 – Material Check as described in the BNQ Master Data Script.After the required settings are available, refer to the process step Record Inspection Results in Scope Item Quality Management in Procurement(1FM). In the test script, go to Test Procedures > Regular Quality Inspection Process > Quality Inspection > Record Inspection Results .You can find the document here [1FM](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2402/SolP/1FM?region=DE).When making a usage decision, you must decide whether or not to accept the stock.Accept the Inspection Lot: Inspected stock is ok, so the received goods are accepted. The stock is posted to unrestricted stock (stock type “F”) and warehouse tasks for putaway are automatically created upon usage decision.Reject the Inspection Lot: Inspected stock is not ok, so the received goods are rejected and the follow-up activity to post the stock to blocked stock is triggered. The system posts the stock from quality stock (“Q”) to blocked stock (“B”). The stock stays in the Clarification Area / Quality Area. Further processing of the blocked stock does not belong to this process. It is continued by other processes, for example Return to Supplier or Scrapping.Scrap to Cost Center: The stock is scrapped and the costs are posted to a Cost Center.Sample Consumption:The samples that are used for inspection are no longer usable due to a destructive inspection method during inspection. They are then posted goods issue as sample consumption.For both, the Scrap to Cost Center and Sample Consumption, you find the following information in the material document:movement types551 – Withdrawal Scrapping From Unrestricted-Use Customer Stock333 – Withdrawal for Sampling from Unrestricted-Use StockCost CenterG/L Account |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). | The Record Usage Decision (QA11) : Initial Screen displays. |  |
| 3 | Enter Inspection Lot Number | On the Record Usage Decision: Initial Screen, make the following entries:Inspection Lot: <your inspection lot number from previous step>Choose Continue. | The Record Usage Decision: Characteristic Overview screen appears, and your inspection lot is displayed. |  |
| 4 | Decide on Usage Decision - Partial Quantity or Collective Usage Decision | Decide for one of the following options:Make a Partial Quantity Decision: Please continue with step 5.Only make a Collective Usage Decision: Please continue with step 11. | Partial Quantity Decision: Make a usage decision only for a certain part of the inspection-relevant quantities. An example process is to accept certain quantities and put them to the final bin, in order to avoid a production stop caused by limited resources.Collective Usage Decision: Make a usage decision for all pieces of the inspection relevant quantities. |  |
| 5 | Make a Partial Quantity Decision | Select the WM Inspection. | The Stock based Q-Inspection without Work Center dialog box appears and the stock items to be inspected is displayed. |  |
| 6 | Display Quality Inspection Details | Select one of the items, and choose Inspection can be created/changed in the Action column. | The Qual. Inspection details are displayed. |  |
| 7 | Add Inspection Document Item | In the Stock based Q-Inspection without Work Center dialog box in the Qual. Inspection section, select the Add inspection document item. | In the Qual. Inspection section, a new row is added. |  |
| 8 | Distribute Available Quantities | Distribute the available quantities according to your inspection result. |  |  |
| 9 | Select Follow-Up Action | Depending on your inspection result, select in the Decision column one of the following usage decision codes for each of the rows:Usage Decisions:A1 - Accepted-unrestricted stockA3 - Accepted-unrestricted-sample-consumptionR1 - Rejected-blocked stockR310 - Rejected-scrap (partial quantity)Note You are also able to enter cost center and reason.The cost center is used for booking the cost of the sample consumption or scrapping. You can set up your own cost centers for this purpose or leave it blank to use default setup provided by the Best Practices content.Reason codes are optional and are used for evaluations, for example reason for scrapping. Reasons codes can be maintained in SSCUI Maintain Reason Codes for Warehouse. | In case you accept the inspection lot, the corresponding follow-up action is the putaway to the final storage bin.In case you reject the inspection lot, the corresponding follow-up action is the putaway to the clarification zone. The stock is booked to blocked stock.In case you want to scrap the inspection lot, the corresponding follow-up action is Scrap to Cost Center. The stock is scrapped and the costs are booked to a cost center.In case the sample is destroyed during the inspection, the corresponding follow-up action is the Sample Consumption. The sample quantity is posted goods issue as it is no longer usable after the inspection.Example:Total quantity: 12 PCsInspection Result: 8 PCs are ok, 4 PCs are not okCreate two lines:Row 1 - Quantity: 8 PCs, Decision: A1,Row 2 - Quantity: 4 PCs, Decision: R1, |  |
| 10 | Select Take Over Partial Lot Inspection | Select OK. | The Record Usage Decision: Characteristic Overview screen appears. |  |
| 11 | Make a Collective Usage Decision | On the Record Usage Decision: Characteristic Overview screen, enter a usage decision code depending on your inspection result:UD Code:A1 - Accepted-unrestricted stock .A2 - Accepted-unrestricted - minor quality .A3 - Accepted-unrestricted-sample consumption .A9 - Accepted-automatic usage decision .R1 - Rejected-blocked stock .R210 - Rejected-return supplier w/o delivery .R220 - Rejected-return supplier with delivery . | You can also skip the Partial Quantity Decision and only make a Collective Usage Decision. |  |
| 12 | Choose Save | Choose Save. | On the Record Usage Decision: Initial Screen the following messages appear:Usage decision for lot <Inspection Lot Number> is savedThe follow-up actions have been triggered. |  |

### Repack Handling Units (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) repacks the handling unit (HU) to another handling unit.

Procedure

|  |
| --- |
| Caution This step is not optional, in case a partial quantity decision was made with different decisions for one pallet. The goal is to distribute the goods on different pallets, based on their stock type.Example: On a pallet of 12 PCs were 8 PCs decided as ok (accepted) and 4 PCs were decided as not ok (rejected). The 8 PCs of unrestricted stock (stock type “F”) are repacked onto HU 1, and the 4 PCs of blocked stock (stock type “B”) are repacked onto HU 2. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Pack Warehouse Stock (F3738). |  |  |
| 3 | Enter Data | Make the following entries:Work Center: PACKStorage Bin: CL-AREAChoose Enter.Choose Start Packing. |  |  |
| 4 | Enter Data | Make the following entries:Handling Unit/Storage Bin: <enter handling unit in the storage bin>Product /Access Code: <enter the product number in the handling unit>Choose Enter. |  |  |
| 5 | Enter Data to Create HU | Select one of the favorite packaging materials or select other packaging material in the Other Packaging Materials field.Enter the target handling unit number or leave it blank to let the system propose automatically.Choose Create. | The destination HU is created and displayed on the right-hand side of the screen. |  |
| 6 | Choose Items | Choose the product and choose Pack.Note If you want to pack all the items, you can choose Pack All. If you want to pack a partial quantity of the product, you can choose Partially Pack. |  |  |
| 7 | Close HU | The selected products are displayed on the right-hand side.If you want to print the HU, choose Print.Choose Close. |  | . |

### Create Ad-Hoc Warehouse Task (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a usage decision is made to accept the stock, it can be moved to the final putaway bin or scrap bin. Therefore, an ad-hoc warehouse task is created by the Warehouse Clerk (EWM).

|  |
| --- |
| Note Since the SAP S/4HANA 2111 Cloud Essentials edition, automatic putaway warehouse task creation upon usage decision with an acceptance usage code is enabled in this process for new customers. Therefore, this step is only required for existing customers. About how to enable the automatic warehouse task creation upon usage decision for existing customers, see chapter [Additional Manual Configuration](#unique_2) [page ] 4.For scrapping reject stock from Clarification Area (WPT S997)/ Quality Area (WPT S999), manual warehouse task creation is still required. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori launchpad | Open the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open SAP Fiori Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT). | The Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) screen displays. |  |
| 3. | Decide your filter criteria | Enter Storage Type: For example, S001Choose Execute. | The Create Product Warehouse Task screen displays. |  |
| 4. | Choose your Stock | Choose one of the stock lines and select More Methods > Create Warehouse Task. | The Create Warehouse Task dialog box (that requests for data) is displayed. |  |
| 5. | Create Warehouse Task for Accepted Stock | Create the warehouse task and enter the following data:Src Trgt Qty AUoM (Quantity): For example, 8 (Pieces decided as ok)Warehouse Process Type: S997Destination Bin and Destination Storage Type are determined by the system.Choose Create WT. | The warehouse task is created, as you can see in the display log. A Warehouse Task List is automatically printed in the background.You must find the open product warehouse task in the monitor node Warehouse Task. Therefore, note down the warehouse task number. |  |
| 6. | Create Warehouse Task for Rejected Stock | Create the warehouse task and enter the following data:Src Trgt Qty AUoM (Quantity): For example, 4 (Pieces decided as not ok)Warehouse Process Type: S997Destination Bin: SCRAP-AREAThe Destination Storage Type is automatically filled in, for example S840.Choose Create WT. | For Partial Usage Decision Scrap to Cost Center and Sample Consumption, both the scrapped stock and consumed stock are deducted from the warehouse immediately after the usage decision is done. No further ad-hoc warehouse tasks for goods movement are required. |  |
| 7. | Complete the Step | Note down the warehouse task number.Choose Continue to close the log and then choose Home or repeat the steps, if necessary. |  |  |

### Confirm Warehouse Tasks

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Putaway List is printed and handed over to the Warehouse Operative (EWM). The user performs the warehouse tasks and confirms them in the system. Note that he or she can also confirm warehouse tasks using the app Warehouse Monitor (/SCWM/MON) (Business Catalog WM – Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Process Warehouse Tasks (F4595). | The Confirm Warehouse Tasks screen appears. |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <Your warehouse task number>.Choose Go. |  |  |
| 4 | Check Warehouse Task Details | If you would like to check the serial numbers assigned, follow step 4-7. Otherwise go directly to step 7.Choose the Warehouse Task to go into the Warehouse Task details. |  |  |
| 5 | Choose Serial Number link | On the Warehouse Task screen, in the Movement Data section, choose No. of Serial Numbers Entered: X / X. |  |  |
| 6 | Check Serial Number | On the Serial Number Assignment screen, check the serial numbers in the List of Serial Numbers.Choose Cancel twice to go back to the Process Warehouse Task screen. |  |  |
| 7 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed. |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with a mobile Radio Frequency device.

For working with mobile RF devices, make sure all the steps as described in the Setup Instruction Guide for scope item 63V have been performed:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ad27f6503263c30b71125c03596bc081)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter.Note Use resource SHA1-1 for putting away to S001.Use SHR1-1 for putting away to storage types other than S001. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001, SI-F01,SI-B01,SI-G01 or SI-970 |  |  |
| 6 | Verify Source Bin and Enter HU | Note This step is only relevant, if you create handling unit for a goods receipt.Verify the Src.Bin (Source Bin)HU: < Enter the HU ID from step Create Handling Unit (Optional)> |  |  |
| 7 | Verify the Source information fields | Verify the following fields, if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)ChooseEnter . |  |  |
| 8 | Verify the Destination Information fields | Verify the following fields, if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)Choose Enter. |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  | All putaway warehouse tasks have been confirmed. |
| 10 | Logoff RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save.Note If you have the two availability groups setup for your warehouse as described in the Business Condition for 2TX, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

Please see chapter [Business Conditions](#unique_7) [page ] 6.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Warehouse Ad Hoc Goods Issue (3BT) | Material can be scrapped.Using the master data from this document, you can initiate the scrapping process by creating a posting change and a warehouse task to move the material to be scrapped from the source bin to the scrapping zone. After the physical goods movement is completed, you post the unplanned goods issue as described in the Warehouse Ad Hoc Goods Issue (3BT) test script. |

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
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 50,612 chars in the whole document
