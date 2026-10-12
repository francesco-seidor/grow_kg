---
id: 08-sales-order-management/basic-available-to-promise-processing-2ln-ae-test-script-832
title: Basic Available-to-Promise Processing (2LN_AE) - Test Script (2LN_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2LN_AE: product availability monitoring, backorder processing (BOP) setup and runs, ATP log deletion."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/availability-check-atp]
aliases: [2LN_S4CLD2608_BPD_EN_AE]
keywords: [Available-to-Promise and Backorder Processing, available-to-promise, product availability check, display product availability, backorder processing, bop segment, bop variant, custom bop sorting, bop run scheduling, bop run monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LN_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-832
topic: 08-sales-order-management/availability-check-atp
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Basic Available-to-Promise Processing (2LN_AE) - Test Script (2LN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Available-to-Promise and Backorder Processing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Basic Available-to-Promise Processing (2LN_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Basic Available-to-Promise Processing (2LN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849556)

[2 Prerequisites 4](#_Toc232849557)

[2.1 System Access 4](#_Toc232849558)

[2.2 Roles 4](#_Toc232849559)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849560)

[2.4 Business Conditions 6](#_Toc232849561)

[3 Overview Table 7](#_Toc232849562)

[4 Test Procedures 8](#_Toc232849563)

[4.1 Monitor Product Availability 8](#_Toc232849564)

[4.2 Display Product Availability 9](#_Toc232849565)

[4.3 Backorder Processing 10](#_Toc232849566)

[4.3.1 Preparation Activities for Running Backorder Processing 10](#_Toc232849567)

[4.3.1.1 Configure BOP Segment 10](#_Toc232849568)

[4.3.1.2 Configure BOP Variant 12](#_Toc232849569)

[4.3.1.3 Configure Custom BOP Sorting 14](#_Toc232849570)

[4.3.2 Backorder Run 15](#_Toc232849571)

[4.3.2.1 Schedule BOP Run 15](#_Toc232849572)

[4.3.2.2 Monitor BOP Run 16](#_Toc232849573)

[5 Appendix 19](#_Toc232849574)

[5.1 Delete Availability Check Data 19](#_Toc232849575)

## Purpose

Overview

A product availability check can be executed for planned orders, production orders, deliveries, sales orders, and stock transport orders, resulting in the order document containing one or more confirmed schedule lines.

If the available quantity of a material is insufficient to fulfill requirements, backorder processing can be performed for sales orders or stock transport orders in alignment with a specific business strategy. Backorder processing is scheduled to run automatically and periodically, resulting in the generation of reprioritized requirements.

Characteristic catalogs contain attributes that can be used as characteristics when you check availability and can be adapted to suit your business needs.

The review availability check result can be used to display if the ordered products can be delivered in time and quantity, and when and how much of the ordered product will presumably be delivered. The result can also list if alternative shipping locations were found, and if so, which can be used.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2LN_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Order Fulfillment Manager | SAP_BR_ORDER_FULFILLMNT_MNGR | Order Fulfillment Management | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Data Privacy Specialist | SAP_BR_DATA_PRIVACY_SPECIALIST | Data Protection and Privacy - Master Data / Data Protection and Privacy | SAP_CA_SPT_DPP_PC / SAP_BR_DATA_PRIVACY_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch |  |
| Sold-to Party | 3310000433100003 | Domestic UAE Customer 4Domestic UAE Customer 3 |  |
| Ship-to Party | 3310000433100003 | Domestic UAE Customer 4Domestic UAE Customer 3 |  |
| Payer | 33100004 | Customer domestic 04 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Business Conditions

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | To run through this scope item, the required materials must be available in stock and sales orders must be available.Sell from Stock (BD9) - Create Sales Order |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Monitor Product Availability](#unique_8) [page ] 8 | Internal Sales Representative | Monitor Product Availability (CO09) |  |
| [Display Product Availability](#unique_9) [page ] 9 | Internal Sales Representative | Display Product Availability (F7884) |  |
| Backorder Processing |  |  |  |
| [Configure BOP Segment](#unique_10) [page ] 10 | Order Fulfillment Manager | Configure BOP Segment (F2158) |  |
| [Configure BOP Variant](#unique_11) [page ] 12 | Order Fulfillment Manager | Configure BOP Variant (F2160) |  |
| [Configure Custom BOP Sorting](#unique_12) [page ] 14 | Order Fulfillment Manager | Configure Custom BOP Sorting (F2983) |  |
| Backorder Run |  |  |  |
| [Schedule BOP Run](#unique_13) [page ] 15 | Order Fulfillment Manager | Schedule BOP Run (F2665) |  |
| [Monitor BOP Run](#unique_14) [page ] 16 | Order Fulfillment Manager | Monitor BOP Run (F2159) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Monitor Product Availability

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the availability of material-plant combinations. This enables you to check if a material is available as required, before executing subsequent processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Product Availability (CO09). | The Availability Overview screen displays. |  |
| 3 | Enter Data | On the Availability Overview screen, make the following entries and choose Continue:Material: <Material Number>Plant: 3310 |  |  |
| 4 | Availability Overview | The Availability Overview screen is divided into three sections:The upper section displays the check parameters.The middle Totals display section displays aggregated material availability at plant level. This enables you to identify a material shortage quickly.The lower ATP situation section displays the daily availability situation for the selected material at plant level, according to the scope of check.For each date and MRP element, the system displays a totals requirement with a receipt quantity (for stocks and receipts) or a requirement quantity, a committed quantity (only for requirements), and a cumulated ATP quantity. The system uses negative indicators to display the requirements. The data is sorted chronologically and starts with the plant section (if no special stocks are displayed). If necessary, the storage location section, batch section, and batch storage location section follow. |  |  |

### Display Product Availability

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to view the available quantities for products in different locations based on the specified availability context and availability date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Product Availability (F7884). | The Display Product Availability screen displays. |  |
| 3 | Enter Data | On the Display Product Availability screen, make the following entries and choose Go:Product: <Product Number>Availability Date: TodayAvailability Context: SalesSpecial Stock Type: No Special Stock |  |  |
| 4 | Availability Overview | You can also do the following check:Availability of a product across multiple plants and MRP areas.Availability of multiple products.Availability of products between the Plant and Storage Location tabs.View the CO2e footprint.View the supply protection status: Active or Inactive. | Note This app provides limited functionality and does not include all features found in the Monitor Product Availability (CO09) app. For more advanced capabilities, consider using that app. |  |
| 5 | View Availability Details | On the Plant or Storage Location tab, choose either a product or a plant. View the details such as MRP elements included in availability calculation.Choose Show Scope of Check to display the availability scope of check. |  |  |

### Backorder Processing

#### Preparation Activities for Running Backorder Processing

##### Configure BOP Segment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a backorder processing segment (aka BOP segment) in which you define criteria for filtering and prioritizing requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure BOP Segment (F2158). | The Configure BOP Segment screen displays. |  |
| 3 | Create a BOP Segment | Choose Create on the table toolbar and enter <your segment name> in the Segment Name field. | The Configure BOP Segment screen displays. |  |
| 4 | Enter Selection Criteria | Enter valid condition in the Selection Conditions section. Choose the + icon to add a new row.For example:Material Number is TG11Plant is 3310 | On the Criterion 1 tab, Document Type Base (Sales Document) is prefilled. You can choose the + icon to add a new criteria for different document type. |  |
| 5 | Define a Prioritizer | In the Prioritizer section, the table is prefilled with the sort attribute Record Creation Date. Choose the + icon to add a new sort attribute.For example:Sold-to PartyLine Item NumberDocument Number |  |  |
| 5a | Define a Custom Sort Order for Requirements (Optional) | Proceed as described in the procedure Configure Custom BOP Sorting. |  |  |
| 6 | Simulate Requirement Selection | Choose Simulate. The requirements that will potentially be selected by a backorder processing run are calculated and displayed on the basis of the segment with its current configuration. |  |  |
| 7 | Reorder Sort Attributes of Prioritizer | Choose Move to Top, Move Up, Move Down and Move to Bottom to reorder the sort attributes:Sold-to PartyDocument NumberLine Item Number | The sort attributes are listed in the intended order. |  |
| 8 | Change Sort Order of Sort Attribute | You can change Sort Order (Ascending or Descending) for sort attribute. For example change Sort Order for Document number to Descending so that new document appears in the top. | The Descending is highlighted in blue. |  |
| 9 | Activate BOP Segment | Choose Create in the lower right corner of the screen. |  |  |

##### Configure BOP Variant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a backorder processing variant (aka BOP variant) with which you define the scope of a backorder processing run.

Prerequisite

A BOP variant uses one or more BOP segments. The procedure for creating a BOP segment, Configure BOP Segment, is a prerequisite for this procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure BOP Variant (F2160). | The Configure BOP Variant screen displays. |  |
| 3 | Create a BOP Variant | Choose the + icon to create a new variant. On the Variant Setting screen, make the following entries and leave other entries as they are:Variant Name: <your variant name>Variant Description: <your variant description>Document Types: Sales DocumentChecking As: Sales Order (Business Scenario: A)Exception Behavior (optional): You can choose to stop processing only those material-plant combinations experiencing an exception or to stop the run completely when an exception occurs.Fallback Variant Name (optional): You can assign a fallback BOP variant to handle the requirements in the Win or Gain confirmation strategies when they cannot be fulfilled.Global Segment Name (optional): You can assign a BOP segment to define the overall set of requirements to be processed.Choose Apply. To change variant settings after close window, choose Edit Header in the top right corner of the screen. | A draft of the BOP variant is created. |  |
| 4 | Add Segment to Variant | Specify <your segment01 name> in the empty Segment Name field below IMPROVE. | The segment and its defined selection criteria are displayed. The segment is automatically assigned to the IMPROVE confirmation strategy. |  |
| 5 | Add Segment to Confirmation Strategy | In case you’ve created multiple segments in previous step, you can add them and move to different strategies.Choose + icon to add new segment. A new empty row is added as the last row in IMPROVE section.Start to type <your segment02 name> in the Segment Name field.When the segment and its defined selection criteria are displayed, you can highlight the segment, choose the rightmost arrow icon to Move to a Different Strategy, and choose confirmation strategy Win from the dropdown list (note that the currently assigned confirmation strategy cannot be chosen).Note The Add to Improve dropdown list at the top of the screen simply adds an empty segment line below the chosen confirmation strategy. You cannot use this button to reassign a segment from one confirmation strategy to another. | Confirmation strategy Win is added and a new tab and the chosen segment and selection criteria are listed. |  |
| 6 | Save BOP Variant | Choose Create. | The variant is saved. |  |
| 7 | Start BOP Run (optional) | You can start a BOP run immediately on the Configure BOP Variant screen. Choose Run from the dropdown next to the Simulate. | The app confirms that a BOP run was scheduled for your variant. |  |
| 8 | Display BOP Run Results (optional) | On the Configure BOP Variant screen, choose Show Last Runs. | On the Monitor BOP Run screen, BOP runs for your BOP variant displays. |  |

##### Configure Custom BOP Sorting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a custom backorder processing sorting with which you define the sort order of the requirements in a backorder processing run. These sorting can be assigned to corresponding sort attribute in the BOP segment you create.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Custom BOP Sorting (F2983). | The Configure Custom BOP Sorting screen displays. |  |
| 3 | Create a Sequence | Choose Create. On the Sequence screen, make the following entries:Sequence Name: <your sequence name>Sequence Description: <your sequence description>Sort Attribute: <your sort attribute>, for example, Sold-to party | A draft of the sequence is created. |  |
| 4 | Add Values to Sequence | Enter a value, for example, 33100001, in the first empty Value field above All others. Enter another value, for example, 33100002, in the last empty Value field below All others. |  |  |
| 5 | Add New Value | Choose Add and a new empty line added at the end of table. Enter a value, for example, 33100013. |  |  |
| 6 | Set Position for Value | You can resort the value by highlighting the line and choose Move up or Move down to change the Position of the line.Alternatively, you can highlight the line, and choose Set Position to directly enter a New Position for this line. |  |  |
| 7 | Save Sequence | Choose Create. | The sequence is saved. |  |

#### Backorder Run

##### Schedule BOP Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to trigger and schedule a backorder processing run (aka BOP run).

Prerequisite

The prerequisite for triggering and scheduling a BOP run is the availability of at least one BOP variant, created in the procedure [Configure BOP Variant](#unique_11) [page ] 12.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Schedule BOP Run (F2665) app. | The Application Jobs screen displays. |  |
| 3 | Create a Job | Choose Create to create a new BOP run.In the Template Selection section, Job Template ATP: Backorder Processing Default is default. Enter a name for your BOP run in the Job Name field.In the Scheduling Options section, select the Start Immediately checkbox. To make it a recurring job, choose Define Recurrence Pattern, and choose one pattern from the dropdown list.In the Parameters Section, enter the following:BOP Variant:Variant Name: <your variant name>Message Log：Force Log: <selected>Granularity: AllChoose Schedule. | A new job is created and run immediately. |  |
| 4 | Open Log (Optional) | A log is available when the job finishes. In the list of all scheduled BOP runs, navigate to the Log. | The log created during the BOP run displays. |  |

##### Monitor BOP Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the results of a BOP run. The prerequisite for this procedure is the execution of at least one BOP run, as processed in the procedure steps [Configure BOP Variant](#unique_11) [page ] 12 or [Schedule BOP Run](#unique_13) [page ] 15.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor BOP Run (F2159). | The BOP Run List displays and BOP varies with which BOP runs have been processed or are running. |  |
| 3 | BOP Run Overview | Navigate to the Run Overview by choosing one of the listed runs.Check the BOP run information, for example, the variant name or user name. It’s possible to navigate to the details of BOP variant by choosing Show Variant in the top right corner of the screen. | The information in the overview page is as intended and a list of material-plant combinations displays. |  |
| 4 | Quick Filter for Confirmation Issues | In the Filter Bar, choose Confirmation Issues. | The list of all material-plant combinations contains only those combinations where a confirmation issue exists. |  |
| 5 | Quick Filter for Processing Issues | In the Filter Bar, choose Processing Issues. | The list of all material-plant combinations contains only those combinations where a processing issue exists. |  |
| 6 | Select a Material-plant Combination and Check Details | Choose one of the displayed material-plant combinations and check the confirmation key figures. | The requirement list screen displays.Detailed information is displayed for each requirement, for example, the confirmation strategy and the name of the BOP segment from which it was selected. The confirmation key figures also display.The Status indicator displays the correct status of each requirement. |  |
| 7 | Check Requirement Details | Choose one of the listed requirements. | A dialog screen displays the Confirmation Details of the selected requirement. The earliest date and available-to-promise quantity display as a reference. |  |
| 8 | Navigate to the BOP Run Overview | Click the name of the BOP variant in the path above the header. | The overview page displays. |  |
| 9 | Select a Confirmation Strategy and Check Details | Choose the CONFIRMATION STRATEGY tab in the header.Choose one of the displayed confirmation strategies and examine the confirmation key figures. | The confirmation strategies used in the BOP variant are listed and the key figures are correct. |  |
| 10 | Navigate to the BOP Run Overview | Click the name of the BOP variant in the path above the header. | The Run Overview screen displays. |  |
| 11 | Select a Recipient and Check Details | Choose the RECIPIENT tab in the header.Choose one of the displayed recipients and examine the confirmation key figures. | The Requirement List screen displays. The requirements for the recipients from the processed sales orders are listed and the key figures are correct. |  |

## Appendix

### Delete Availability Check Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule the deletion of logs created by Available-to-Promise.

Prerequisites

Before you can delete any logs containing ATP results, at least one log has to have been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open ILM Data Destruction (F2662). | The ILM Data Destruction screen displays. |  |
| 3 | Choose Data Destruction Object | Choose the Data Destruction Objects tab. In the Not Schedule section, find and select the checkbox for object ATP_CHECK_LOG_DESTRUCTION. | The Schedule is selectable. |  |
| 4 | Schedule Delete | Choose Schedule on the tool bar. Choose Delete in the Schedule Delete dialog box. | Destruction run is scheduled. |  |

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
- related-to :: [[08-sales-order-management/test-script-advanced-available-to-promise-consumer-products-6n0-ae-117]]
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-advanced-available-to-pro]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 32,348 chars in the whole document
