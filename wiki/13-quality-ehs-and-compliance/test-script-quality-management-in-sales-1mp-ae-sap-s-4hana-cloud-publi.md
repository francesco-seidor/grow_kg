---
id: 13-quality-ehs-and-compliance/test-script-quality-management-in-sales-1mp-ae-sap-s-4hana-cloud-publi
title: "Test Script: Quality Management in Sales (1MP_AE) - SAP S/4HANA Cloud Public Edition (1MP_S4CLD2608_BPD_EN_AE)"
description: "Test script, SAP S/4HANA Cloud scope item 1MP_AE (UAE): quality inspection in outbound delivery, sales order to usage decision, goods issue or blocked stock."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-inspection-procurement-and-sales]
aliases: [1MP_S4CLD2608_BPD_EN_AE]
keywords: [Quality Inspection in Procurement and Sales, quality inspection in sales, scope item testing, inspection lots, inspection results recording, usage decision, rejected material handling, goods issue posting, blocked stock transfer, outbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MP_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-738
topic: 13-quality-ehs-and-compliance/quality-inspection-procurement-and-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Quality Management in Sales (1MP_AE) - SAP S/4HANA Cloud Public Edition (1MP_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MP_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Quality Inspection in Procurement and Sales** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Quality Management in Sales (1MP_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847336)

[2 Prerequisites 4](#_Toc232847337)

[2.1 System Access 4](#_Toc232847338)

[2.2 Roles 4](#_Toc232847339)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847340)

[2.4 Business Conditions 5](#_Toc232847341)

[2.5 Preliminary Steps 6](#_Toc232847342)

[2.5.1 Create Raw Material Stock 6](#_Toc232847343)

[3 Overview Table 8](#_Toc232847344)

[4 Test Procedures 9](#_Toc232847345)

[4.1 Create Sales Order 9](#_Toc232847346)

[4.2 Display Inspection Plan for Inspection Characteristics (Optional) 10](#_Toc232847347)

[4.3 Create Delivery and Pick Quantity 11](#_Toc232847348)

[4.3.1 Create Delivery 11](#_Toc232847349)

[4.3.2 Execute Picking 12](#_Toc232847350)

[4.4 Quality Inspection 14](#_Toc232847351)

[4.4.1 Display Quality Technician Overview (Optional) 14](#_Toc232847352)

[4.4.2 Display Open Inspection Lots (Optional) 14](#_Toc232847353)

[4.4.3 Record Inspection Results 15](#_Toc232847354)

[4.4.4 Display Quality Engineer Overview (Optional) 18](#_Toc232847355)

[4.4.5 Make Usage Decision 19](#_Toc232847356)

[4.4.5.1 Material Accepted 20](#_Toc232847357)

[4.4.5.1.1 Post Goods Issue for Outbound Delivery 20](#_Toc232847358)

[4.4.5.2 Material Rejected 21](#_Toc232847359)

[4.4.5.2.1 Post Unrestricted Stock to Blocked Stock 21](#_Toc232847360)

[4.4.5.2.2 Update Delivery 22](#_Toc232847361)

[4.4.6 Display Inspection Results History (Optional) 24](#_Toc232847362)

[5 Appendix 26](#_Toc232847363)

[5.1 Process Integration 26](#_Toc232847364)

[5.1.1 Succeeding Processes 26](#_Toc232847365)

## Purpose

Overview

This scope item manages quality inspection activities in outbound delivery processes. Quality inspection activities may be important before goods issue.

When creating an outbound delivery for a material that is the subject of an inspection in the sales and delivery process, an inspection lot is created based on an inspection plan. The quality technician records the inspection results for a sample size. Based on these inspection results, the quality engineer makes a usage decision, for example, accepting or rejecting the material. If accepted, the goods are posted and sent to the customer. If rejected, the whole quantity is posted to blocked stock and the delivery is updated. For the rejected results, a defect is automatically recorded. Any further stock of the same material must be accepted before they are delivered.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Customer | 33100003 | Domestic UAE Customer 3 |  |
| Material | QM001 | Trading Good for Regular Procurement (PD planning) |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA), you can either:Run through the Procurement of Direct Materials(J45) processOr create stock using FLP tile Post Goods Movement (for details see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period - MDS | Complete all steps in the master data script. Posting Period is up-to-date. |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | Complete all steps in the master data script for inspection type 10. |
| BNQ - Create Quality Inspection Plan - MDS |  |

### Preliminary Steps

#### Create Raw Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, the materials must be available in stock. Stock can be available after a goods receipt of a purchasing process. In this case, you do not need this preliminary step. This process step shows you how to create raw material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and Choose Enter:Plant: 3310Material: QM001 | The Stock Overview for the material displays. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331AUnrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: Enter today's datePosting Date: Enter today's dateStock Change: Initial EntryQuantity: Enter a number,for example, <10> | The system displays Material document XXX created. The stock has been added. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_9) [page ] 9 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_10) [page ] 10 | Quality Technician | Display Inspection Plan (QP03) | The inspection plan is checked. |
| [Create Delivery and Pick Quantity](#unique_11) [page ] 11 |  |  |  |
| [Create Delivery](#unique_12) [page ] 11 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Execute Picking](#unique_13) [page ] 12 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Delivery is picked. |
| [Display Quality Technician Overview (Optional)](#unique_14) [page ] 14 | Quality Technician | Quality Technician Overview (F2361) | The Quality Technician Overview screen displays. |
| [Display Open Inspection Lots (Optional)](#unique_15) [page ] 14 | Quality Technician | Manage Inspection Lots (F2343) | Inspection lot is displayed. |
| [Record Inspection Results](#unique_16) [page ] 15 | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded |
| [Display Quality Engineer Overview (Optional)](#unique_17) [page ] 18 | Quality Engineer | Quality Engineer Overview (F2360) | The Quality Engineer Overview screen displays. |
| [Make Usage Decision](#unique_18) [page ] 19 | Quality Engineer | Manage Usage Decisions (F2345) |  |
| Material Accepted:[Post Goods Issue for Outbound Delivery](#unique_19) [page ] 20 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |
| Material Rejected:[Post Unrestricted Stock to Blocked Stock](#unique_20) [page ] 21[Update Delivery](#unique_21) [page ] 22 | Warehouse ClerkShipping Specialist | Transfer Stock - In-Plant (F1061)Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |
| [Display Inspection Results History (Optional)](#unique_22) [page ] 24 | Quality Engineer | Display Results History (F2428) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for material QM001 .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) . | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, select Create Sales Order. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold To party: 33100003Ship To party: 33100003Cust. Reference: <Reference number> Enter a customer purchase order number as referenceRequested Delivery Date: Current date plus 2 working daysNote If a popup appears for example after changing the Delivery Date, choose Enter and accept it.Material Number: QM001Order Quantity: <Quantity> For example, < 10 PC > |  |  |
| 6 | Save Document | Choose Save. Make a note of the sales order number. | The order is saved. |  |

### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to review the inspection plan, which defines all inspection characteristics used later in the quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03) . (Without a subtitle) | The Display Inspection Plan: Initial screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: QM001Plant: 3310 |  |  |
| 4 | Select Entry Instruction | On the Entry Option: Group screen, select the row with Inspection Plan for Sales and then click Choose. |  |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the operation 0010 and choose Inspection Characteristics. | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There are two Master Inspection Characteristics:One is Qualitative – SurfaceOne is Quantitative – Length | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedure can be reviewed in the inspection plan with the quality planner role. |  |

### Create Delivery and Pick Quantity

Purpose

This process step shows you how to create the delivery and execute the picking process, which involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as aShipping Specialist . |  |  |
| 2. | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping point: 3310Planned Creation Date: <input the date range>SD Document: Sales order number created previously |  |  |
| 4. | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5. | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries.Make a note of the delivery number. | Make a note of the delivery number. |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. It shows you how to execute picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries - VL06O screen displays. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute.Shipping Point: 3310Only Picking without WM: X |  |  |
| 5 | Change Outbound Delivery | From Day’s Workload for Picking , select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | Navigate to the Picking tab.For picking related items, make the following entry Picked Qty: quantity equal to delivery Qty |  |  |
| 7 | Choose Enter | Press Enter. |  |  |
| 8 | Check the corresponding Inspection Lot | Double-click the Item line and go to the Processing tab. | Check the inspection lot number. |  |
| 9 | Save | Choose Save. | The delivery has been picked. |  |

### Quality Inspection

#### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to display the open inspection lot list via the overview page for quality technicians.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview screen displays.You can get an overview of the inspection lots with open results recording and navigate directly to the Record Inspection Results App. Additionally, you can check the inspection lots without an inspection plan. |  |

#### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to display the open inspection lot list via the Manage Inspection Lots app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter FIelds | Make the following entry and choose Go:Delivery Document: Obtained from previous step | The open inspection lots are displayed.If Delivery is not displayed in the Filters, choose Adapt Filters. On the pop-up screen Adapt Filters, find, and Sales and Distribution choose More Filters. Select Delivery and choose OK. Choose Go. |  |
| 4 | Select Inspection Lot | In the inspection lot list, click the inspection lot that was created before. | Inspection lot displays. |  |
| 5 | Check Inspection Lot | Under Origin, verify the referenced sales order. | The sales order number from which the inspection lot originates is displayed. |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to record the inspection results.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results (F1685A) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entry and choose Go.Delivery: Obtained from previous step | If Delivery is not displayed in the Filters, choose Adapt Filters. On the pop-up screen Filters, find Sales and Distribution and choose More Filters. Select Delivery and choose OK. Choose Go |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the corresponding inspection lot for the delivery created in a previous step. |  |  |
| 5 | Choose Record Results | Choose Record Multiple Results at the top right. |  |  |
| 6 | Enter Inspection Results | Click Edit. Depending on the inspection result, select one of the following two options:Positive ResultSurface: Code Group – Code SURFACE 0020 (Smooth)Length: Mean Value (cm): 160Negative ResultSurface: Code Group – Code SURFACE 0010 (Rough)Length: Mean Value (cm): 90 | For qualitative characteristic (Surface) the search help is required to select a value. For the quantitative characteristic (Length) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well as a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic.With the App: Record Results – Hierarchical View.A user can exceptionally overrule the automatic evaluation, for example, to document that the tolerance is always at the upper border, then the generic defect ‘tolerance issue’ will be used. |  |
| 7 | Save Inspection Lot | Choose Save. |  |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for several inspection lots at the same time, execute the following process flow

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365). | The Record Inspection Results in Table Formscreen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots displays. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the dialogue box Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose OK. | The Record Inspection Results in Table Formscreen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 | Show Work Center (Optional) | Choose Settings in the upper right corner of the table. In the Define Colunm Properties dialogue box, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above, for example, data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Note Depending on the defined valuation mode (check inspection method details), the valuation is either done automatically by the system or must be done manually by the user.If an inspection result requires an inspection remark (check master inspection characteristic settings), it is not possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message displays. |  |

#### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As an optional entry point for making this usage decision, you can use the app Manage Usage Decisions. This optional process step shows you how to display the open inspection lot regarding the usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview screen displays. |  |
| 3 | Select Inspection Lots Without Usage Decision | Click the card Inspection Lots Without Usage Decision. | A list of inspection lots without usage decisions displays. For this selection of complete inspection lots without deviations, you can use Make Quick Usage Decision to close the inspection lot with an accepted code. |  |
| 4 |  | Continue with chapter Make Usage Decision. | The Manage Usage Decisions screen displays. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the material depending on the inspection result. This process step shows you how to make usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). | The Record Usage Decision: Initial screen displays. |  |
| 3 | Enter Inspection Lot number | On the Record Usage Decision: Initial Screen, make the following entry:Inspection Lot: <your Inspection Lot number from previous step>Choose Continue. | The Record Usage Decision: Characteristic Overview screen appears, and your inspection lot is displayed. |  |
| 4 | Display Defects | Check the details of defects on the Defects tab. | Only available if you have recorded a Negative result. |  |
| 5 | Attach a Document | On the Documents tab, choose Add, select the path and add the document. | For example, to upload pictures to visualize the defect. |  |
| 6 | Enter Usage Decision Code | On the Characteristics tab, in the Usage Decision section, depending on the inspection result, select one of the following entries as the UD code:Positive ResultA - AcceptedNegative ResultR - Rejected |  |  |
| 7 | Save Usage Decision | Choose Save. |  |  |

##### Material Accepted

###### Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the material is accepted, you can post the goods issue for outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and Choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select Today's date from the dialog box. | The goods issue is posted. If a popup appears to enter the actual goods movement date, confirm the actual date. |  |

The process has been completed with this step. You can proceed with the step[Display Inspection Results History (Optional)](#unique_22) [page ] 24 in this scope item.

##### Material Rejected

###### Post Unrestricted Stock to Blocked Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the material is rejected, post the material from unrestricted stock to blocked stock.

Procedure

Follow the steps described:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open Transaction | Log on to the SAP Fiori Launchpad as a Warehouse Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the appropriate fields:Plant: 3310Material: QM001 | Entries are made. |  |
| 4 | Select Transfer from Stock | Select the icon beside the unrestricted stock that you want to transfer from. | The icons change. |  |
| 5 | Select Transfer to Stock | Select the icon beside the blocked stock that you want to transfer to. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity that you want to transfer:Quantity: x PC, for example: 10 PC |  |  |
| 7 | Post | Choose Post. | The system displays a message Material document xxx created.The goods stock status is switched from unrestricted use to blocked. Goods stock is excluded from MRP calculations. |  |

###### Update Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you delete the rejected material from the delivery.

Procedure

Option 1:

If there is enough or partial stock on inventory, a new line item can be created (with reference to the sales order item).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and Choose Execute.Shipping Point: 3310 |  |  |
| 4 | Change Outbound Delivery | Mark the relevant delivery and choose Change Outbound Deliveries. | The Delivery XXXXX Change: Overview screen displays. |  |
| 5 | Delete Delivered Quantity and Picked Quantity | On the Picking tab, delete the Deliv. Qty and Picked Qty.. |  |  |
| 6 | Save the Delivery | Choose Save. | If the Warning Message Delivery quantity must be entered for the itemappears, choose Enter to confirm. |  |
| 7 | Change Outbound Delivery | Mark the relevant delivery again and choose Change Outbound Deliveries. | The Delivery XXXXX Change: Overview screen displays. |  |
| 8 | Reopen the Delivery | Choose Menu > Outbound Delivery > Deliver Sales Order .In the pop-up screen Delivery Sales Order, enter the following entries and then choose Continue.Order: Obtained from previous step | A new line item is created with reference to the sales order item. |  |
| 9 | Save the Delivery Again | Choose Save. | For the new line item another inspection lot is created; the process continues with section Record Inspection Results. After Record Inspection Results is checked OK, the goods issue can be posted later. |  |

Option 2:

If there is not enough inventory on stock, the delivery is saved without this material. A new delivery is created as soon as stock is available (continue with section Create Delivery and Pick Quantity).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and Choose Execute.Shipping Point: 3310 |  |  |
| 4 | Change Outbound Delivery | Mark the relevant delivery and choose Change Outbound Deliveries. | The Delivery XXXXX Change: Overview screen displays. |  |
| 5 | Delete the Material | On the Item Overview tab, select the Item with material QM001 and then choose Delete Item(s). |  |  |
| 6 | Post Goods | Choose Save. | If a dialog box of Delete selected item(s)? appears, choose Yes to confirm. |  |

#### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to display inspection results history.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristics | A list of inspection characteristics displays. |  |
| 4 | Select an Inspection Characteristics | Select an Master Inspection Characteristics, for example, Length. | Several information shows about the selected characteristics for process control.For example,A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability. For example, Variance. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BD9 – Sell from Stock |  |

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
> Flagged while digesting this document, not verified: Internal app inconsistency: the Overview Table lists Manage Outbound Deliveries (F0867A) for Execute Picking and Manage Usage Decisions (F2345) for Make Usage Decision, but the Test Procedures use Manage Outbound Deliveries - VL06O (VL06O_CLOUD) and Record Usage Decision (QA11) respectively.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/quality-management-in-procurement-1fm-ae-test-script-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MP_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 41,008 chars in the whole document
