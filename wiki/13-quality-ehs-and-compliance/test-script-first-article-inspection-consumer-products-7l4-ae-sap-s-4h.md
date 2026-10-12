---
id: 13-quality-ehs-and-compliance/test-script-first-article-inspection-consumer-products-7l4-ae-sap-s-4h
title: "Test Script: First Article Inspection – Consumer Products (7L4_AE), SAP S/4HANA Cloud Public Edition (7L4_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 7L4: first article inspection (FAI) and regular goods receipt inspection with PPAP in the quality info record."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/first-article-inspection]
aliases: [7L4_S4CLD2608_BPD_EN_AE]
keywords: [First Article Inspection, production part approval process, quality info record, inspection plans, goods receipt inspection, inspection results recording, usage decision, rejected FAI reinspection, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7L4_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1217
topic: 13-quality-ehs-and-compliance/first-article-inspection
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: First Article Inspection – Consumer Products (7L4_AE), SAP S/4HANA Cloud Public Edition (7L4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7L4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **First Article Inspection** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | First Article Inspection – Consumer Products (7L4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860431)

[2 Prerequisites 4](#_Toc232860432)

[2.1 System Access 4](#_Toc232860433)

[2.2 Roles 4](#_Toc232860434)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860435)

[2.4 Business Conditions 7](#_Toc232860436)

[2.5 Preliminary Steps 7](#_Toc232860437)

[2.5.1 Create Info Record for Material 7](#_Toc232860438)

[2.5.2 Create Quality Info Record in Procurement 8](#_Toc232860439)

[3 Overview Table 10](#_Toc232860440)

[4 Test Procedures 13](#_Toc232860441)

[4.1 First Article Inspection (FAI) – QM-Integration in Production Part Approval Process (PPAP) 14](#_Toc232860442)

[4.1.1 Display Inspection Plans for Inspection Characteristics 14](#_Toc232860443)

[4.1.2 Create Purchase Order 16](#_Toc232860444)

[4.1.3 Change Quality Info Record 18](#_Toc232860445)

[4.1.4 Display Material Stock before Goods Receipt (Optional) 19](#_Toc232860446)

[4.1.5 Post Goods Receipt for Purchase Order 20](#_Toc232860447)

[4.1.6 Display Material Stock Before Quality Inspection (Optional) 21](#_Toc232860448)

[4.1.7 Quality Inspection (FAI) 22](#_Toc232860449)

[4.1.7.1 Display Quality Technician Overview (Optional) 22](#_Toc232860450)

[4.1.7.2 Display Open Inspection Lots (Optional) 23](#_Toc232860451)

[4.1.7.3 Record Inspection Results 24](#_Toc232860452)

[4.1.7.4 Display Quality Engineer Overview (Optional) 27](#_Toc232860453)

[4.1.7.5 Make Usage Decision 28](#_Toc232860454)

[4.1.8 Display Material Stock After Quality Inspection (Optional) 29](#_Toc232860455)

[4.1.9 Review Quality Info Record (Optional) 30](#_Toc232860456)

[4.2 Accepted FAI (Case 1): Regular Quality Inspection for 2nd Purchase Order 31](#_Toc232860457)

[4.2.1 Create Purchase Order 32](#_Toc232860458)

[4.2.2 **Display Material Stock before Goods Receipt (Optional)** 32](#_Toc232860459)

[4.2.3 Post Goods Receipt for Purchase Order 32](#_Toc232860460)

[4.2.4 Display Material Stock Before Quality Inspection (Optional) 32](#_Toc232860461)

[4.2.5 Quality Inspection (Regular Inspection) 33](#_Toc232860462)

[4.2.5.1 Display Quality Technician Overview (Optional) 33](#_Toc232860463)

[4.2.5.2 Display Open Inspection Lots (Optional) 33](#_Toc232860464)

[4.2.5.3 Record Inspection Results 33](#_Toc232860465)

[4.2.5.4 **Display Quality Engineer Overview (Optional)** 35](#_Toc232860466)

[4.2.5.5 Make Usage Decision 35](#_Toc232860467)

[4.2.6 Display Material Stock After Quality Inspection (Optional) 35](#_Toc232860468)

[4.3 Rejected FAI (Case 2): New FAI Inspection for 2nd Purchase Order (Optional) 35](#_Toc232860469)

[4.3.1 Create Purchase Order 35](#_Toc232860470)

[4.3.2 Change Quality Info Record 36](#_Toc232860471)

[4.3.3 Processing of the Purchase Order and Quality Inspection 36](#_Toc232860472)

## Purpose

Overview

This scope item describes a process in the consumer products industry to manage the first article inspection (FAI) and regular inspection of a raw material. As an example material, a foil is used, which becomes a viewing window bag during production. Before the foil is released to production, the material must meet the specifications negotiated with the supplier. To ensure this, a small sample quantity is ordered with the first purchase order and inspected with a special inspection plan. The Production Part Approval Process (PPAP) in the quality info record controls this, where the purchase order item is maintained.

At goods receipt, the inspection lot is created with the special first article inspection plan for first check. This plan contains a general goods receipt inspection by the quality team as well as an additional inspection by a special team responsible for the print layout inspection. After results recording and the usage decision, you can monitor the result of the first article inspection in the quality info record.

If the FAI is accepted, the print layout is shared with the supplier. A new purchase order with normal quantity can be created. The process continues with the goods receipt and the regular goods receipt inspection. If the FAI is rejected, the same process can be repeated with a new purchase order item and a new quality info record maintenance.

This type of first article inspection requires an inspection plan structure with several operations. However, the structure of this inspection plan can be simpler in your company, as you may not need different operations and work centers, though you may need different inspection plans with the corresponding inspection plan usage.

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

Table 1:

| Name (Role Template) | ID (Role Template) | Description (Space Template) | ID (Space Template) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchaser | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | Purchaser |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Technician |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineer |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK | Warehouse Clerk |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER | Quality Planner |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

Material Master Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | RM0509 | Viewing Window Bag | Raw material, batch managed |

Organization Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost center | 33101301 | Manufacturing 1 (AE) |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Work center

| Work Center | Plant | Work Center Category | Work Center Description |
| --- | --- | --- | --- |
| QMLABS | 3310 | 0001 | Quality Check Labs |
| QMCP | 3310 | 0001 | Quality Check Point |

Suppliers:

| Master Data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 | Domestic Supplier 1 |  |
| Supplier | 33300002 | Domestic Supplier 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purchase Organization 3310 |  |

Quality Master Inspection Characteristics:

| Master Data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Master Inspection Characteristic | YQM00013 | Goods Receipt Inspection | QUAL01-OK/NOK |
| Master Inspection Characteristic | YQM00014 | Print Layout | QUAL01-OK/NOK |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNE | Create Supplier Master - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNY | Create Quality Management Attributes for Material/Product Master - MDS |
| BF5 | Create Quality Info Record - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNQ - Create Quality Inspection Plan - MDS | You have completed the step described in the Create Quality Inspection Plan - MDS (BNQ) master data script.Inspection Plan with plan usage 5 (GR) and 51 (GR Model Inspection). |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | You have completed the step described in the Create Quality Management Attributes for Material/Product Master - MDS (BNY) master data script.Inspection Type 01 (GR for Purchase Order) and Procurement Control Key 0001 (Vendor Release). |
| BF5 - Create Quality Info Record - MDS | You have completed the step described in the Create Quality Info Record - MDS (BF5) master data script.See also Preliminary Steps in this document. |
| BHD - Create Purchasing Info Record - MDS | You have completed the step described in the Create Purchasing Info Record - MDS (BHD) master data script. |

### Preliminary Steps

#### Create Info Record for Material

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Info Record Description: <Short text>Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Purchasing Group: 002Material Group: L002Material: RM0509 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX>, for example, 2Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: for example, 10Goods-Receipt-Based Invoice Verification: unmarked | Delivery and Quantity Data is added. |  |
| 6 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Today’s Date>Amount: 15,00Pricing Unit: 1Valid To: 12/31/9999Currency: AEDChoose the Apply icon. | Condition Data is added. |  |
| 7 | Save Your Data | Choose Create. | A purchasing info record is saved.Note down the purchasing info record number. |  |

#### Create Quality Info Record in Procurement

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Quality Info Records (F2256A). | The Manage Quality Info Records screen displays. |  |
| 3 | Open New Quality Info Record | Choose Create. | The Quality Info Record screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Material: RM0509Plant: 3310Supplier: 33300001 |  |  |
| 5 | Enter Release Data | In the Release section, enter the following data:Release Until: 12/31/9999 alt.31/12/9999 |  |  |
| 6 | Save Your Data | Choose Create. | Your data is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| First Article Inspection (FAI) – QM-Integration in Production Part Approval Process (PPAP) |  |  |  |
| [Display Inspection Plans for Inspection Characteristics](#unique_10) [page ] 14 | Quality Technician | Manage Inspection Plans (F3788). | Stock/Requirements situation for the planned materials is analyzed. |
| [Create Purchase Order](#unique_11) [page ] 16 | Purchaser | Manage Purchase Orders (F0842A) | A purchase order is created. |
| [Change Quality Info Record](#unique_12) [page ] 18 | Quality Planner | Manage Quality Info Records (F2256A) | The quality info record is displayed. PPAP is enabled. |
| [Display Material Stock before Goods Receipt (Optional)](#unique_13) [page ] 19 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed |
| [Post Goods Receipt for Purchase Order](#unique_14) [page ] 20 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843). | Goods receipt for PO is posted. |
| [Display Material Stock Before Quality Inspection (Optional)](#unique_15) [page ] 21 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. The goods receipt quantity from previous step is shown in the quality stock. |
| Quality Inspection (FAI) |  |  |  |
| [Display Quality Technician Overview (Optional)](#unique_16) [page ] 22 | Quality Technician | Quality Technician Overview (F2361) | List of open inspection results is displayed. |
| [Display Open Inspection Lots (Optional)](#unique_17) [page ] 23 | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. The Quality Technician can select the next inspection lot he or she wants to record the results for. |
| [Record Inspection Results](#unique_18) [page ] 24 | Quality Technician | Manage Inspection Lots (F2343) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_19) [page ] 27 | Quality Engineer | Quality Engineer Overview (F2360) | The Quality Engineer Overview displays. |
| [Make Usage Decision](#unique_20) [page ] 28 | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted |
| [Display Material Stock After Quality Inspection (Optional)](#unique_21) [page ] 35 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. Depending on the usage decision, the stock quantity is shown in the blocked stock, in unrestricted or in another storage location. |
| [Review Quality Info Record (Optional)](#unique_22) | Quality Planner | Manage Quality Info Records (F2256A) | The quality info record is displayed. FAI results are shown. |
| Accept FAI (Case 1): Regular Quality Inspection for 2nd Purchase Order |  |  |  |
| [Create Purchase Order](#unique_23) [page ] 32 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is created. |
| [Display Material Stock before Goods Receipt (Optional)](#unique_24) [page ] 32 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed |
| [Post Goods Receipt for Purchase Order](#unique_25) [page ] 32 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt for PO is posted. |
| [Display Material Stock Before Quality Inspection (Optional)](#unique_26) [page ] 32 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. The goods receipt quantity from previous step is shown in the quality stock. |
| Quality Inspection (Regular Inspection) |  |  |  |
| [Display Quality Technician Overview (Optional)](#unique_27) [page ] 33 | Quality Technician | Quality Technician Overview (F2361) | List of open inspection results is displayed. |
| [Display Open Inspection Lots (Optional)](#unique_28) [page ] 33 | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. The Quality Technician can select the next inspection lot he or she wants to record the results for. |
| [Record Inspection Results](#unique_29) [page ] 33 | Quality Technician | Manage Inspection Lots (F2343) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_30) [page ] 35 | Quality Engineer | Quality Engineer Overview (F2360) | The Quality Engineer Overview displays. |
| [Make Usage Decision](#unique_31) [page ] 35 | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted |
| [Display Material Stock After Quality Inspection (Optional)](#unique_21) [page ] 35 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. Depending on the usage decision, the stock quantity is shown in the blocked stock, in unrestricted or in another storage location. |
| Reject FAI (Case 2): New FAI Inspection for 2nd Purchase Order |  |  |  |
| [Create Purchase Order](#unique_32) [page ] 35 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is created. |
| [Change Quality Info Record](#unique_33) [page ] 36 | Quality Planner | Manage Quality Info Records (F2256A) | The quality info record is displayed. PPAP is enabled. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The high level overall process flow of first article inspection follows the subsequent logic

purchase order is created where the ordered material is subject to a first article inspection (FAI). A specific QM inspection plan is stored for the relevant purchase order item that contains the characteristics for a first article inspection ([Display Inspection Plans for Inspection Characteristics](#unique_10) [page ] 14 – [Display Material Stock before Goods Receipt (Optional)](#unique_13) [page ] 19)

At goods receipt for the purchase order, an inspection lot is automatically created to be used for first article inspection. The inspection plan defines which characteristics are inspected, which methods and tolerances apply, and how the results are recorded ([Post Goods Receipt for Purchase Order](#unique_14) [page ] 20 – [Display Material Stock Before Quality Inspection (Optional)](#unique_15) [page ] 21).

The quality inspection is performed based on the inspection plan and the results are recorded in SAP. The recorded results are valuated and the first article is released or rejected based on the results(steps 4.1.7– [Review Quality Info Record (Optional)](#unique_22))

Option 1: When the first article is released, a regular purchase order is placed for the material ([Create Purchase Order](#unique_23) [page ] 32 – [Display Material Stock After Quality Inspection (Optional)](#unique_21) [page ] 35).

Option 2: In case of rejection, further steps are required to resolve the material issue ([Create Purchase Order](#unique_32) [page ] 35 – 4.3.3)

Create again a purchase order that requires a new first article inspection

Post good receipt for new purchase order item

Execute Quality inspection

Depending on the inspection results follow logic in Option 1 or 2

The Production Part Approval Process (PPAP) status is managed in the quality info record and reflects the state of first article inspection.

The high level overall process flow of first article inspection follows the subsequent logic:

A. Regular and FAI inspection are inspected with different inspection plans, controlled by different inspection plan usages ([Display Inspection Plans for Inspection Characteristics](#unique_10) [page ] 14).

B. Purchase order is created where the ordered material is subject to a first article inspection (FAI). FAI is controlled via manual user entry of this first purchase order (1st) in the relevant supplier specific quality info record: PPAP (Production Part Approval) section ([Create Purchase Order](#unique_11) [page ] 16 – [Change Quality Info Record](#unique_12) [page ] 18).

C. At goods receipt for the purchase order, an inspection lot is automatically created. Because of the entry in quality info record, the FAI inspection plan with plan usage 51 GR Model Inspection is assigned to the inspection lot. For better understanding, we call it “FAI inspection lot”. The quality inspection is performed based on the inspection plan and the results are recorded in SAP. The recorded results are valuated and the FAI inspection lot is accepted or rejected based on the results ([Display Material Stock before Goods Receipt (Optional)](#unique_13) [page ] 19 – [Display Material Stock After Quality Inspection (Optional)](#unique_21) [page ] 35).

D. After usage decision, the valuation of FAI inspection lot is reflected to relevant purchase order item in quality info record, section PPAP. ([Review Quality Info Record (Optional)](#unique_22)).

Depending on the inspection results follow logic in Option 1 or 2.

Option 1: When the FAI inspection lot is accepted, a regular purchase order with normal quantity is placed for the material ([Create Purchase Order](#unique_23) [page ] 32 – [Display Material Stock After Quality Inspection (Optional)](#unique_21) [page ] 35)

Option 2: In case of FAI inspection lot rejection, the FAI inspection must be repeated ([Create Purchase Order](#unique_32) [page ] 35 – 4.3.3)

Create again a purchase order that requires a new first article inspection: quantity = 1

Change quality info record and maintain 2nd purchase order in PPAP section.

Post goods receipt for new purchase order item

Execute Quality inspection.

Review Quality Info Record.

### First Article Inspection (FAI) – QM-Integration in Production Part Approval Process (PPAP)

#### Display Inspection Plans for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, inspection plans can be displayed to the raw material. The inspection plan defines all inspection characteristics used later in the quality inspection.

There are two inspection plans available:

First inspection plan with inspection plan usage “GR Inspection” (usage 5).

Second inspection plan with inspection plan usage "GR Model Inspection" (usage 51). The inspection plan usage 51 specifies that this plan should be used for First Article Inspection.

Display Inspection Plan (Regular Inspection)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Plans (F3788). | The Manage Inspection Plans screen displays. |  |
| 3 | Enter Selection Fields | Adapt the filter by adding Material as filter criteria.Make the following entries and choose Go.Material: RM0509Plant: 3310 |  |  |
| 4 | Select Inspection Plan | Select the entry with description Regular Inspection - Foil, click on the selected line. | Check plan usage 5 (Goods Receipt). |  |
| 5 | Go to Inspection Characteristics Overview | Select the operation 0010 Goods Receipt Inspection with work center QMLABS and click on the selected line.Note If the field work center is not displayed in the filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center and choose OK. Choose Go.Go to Characteristics. | The Manage Inspection Plans screen displays. |  |
| 6 | Review the Inspection Characteristics | Review the following :Master Inspection Characteristics– YQM00013Inspection Characteristic Description– Goods Receipt Inspection | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedure can be reviewed in the inspection plan with the quality planner role. |  |

Display Inspection Plan (First Article Inspection)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Plans (F3788). | The Manage Inspection Plans screen displays. |  |
| 3 | Enter Selection Fields | Adapt the filter by adding Material as filter criteria.Make the following entries and choose Go.Material: RM0509Plant: 3310 |  |  |
| 4 | Select Inspection Plan | Select the entry with description First Article Inspection (FAI) - Foil, click on the selected line. | Check plan usage 51 (GR Model Inspection). |  |
| 5 | Go to Inspection Characteristics Overview - operation 0010 | Select the operation 0010 Goods Receipt Inspection with work center QMLABS and click on the selected line.Note If the field work center is not displayed in the filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center and choose OK. Choose Go.Go to Characteristics. | The Manage Inspection Plans screen displays. |  |
| 6 | Review the Inspection Characteristics | Review the following :Master Inspection Characteristics– YQM00013Inspection Characteristic Description– Goods Receipt Inspection | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedure can be reviewed in the inspection plan with the quality planner role. |  |
| 7 | Go to Inspection Characteristics Overview - operation 0020 | Select the operation 0020 Print Layout Check (Foil) with work center QMCP and click on the selected line.Note If the field work center is not displayed in the filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center and choose OK. Choose Go.Go to Characteristics. | The Characteristics Overview screen displays. |  |
| 8 | Review the Inspection Characteristics | Review the following :Master Inspection Characteristics– YQM00014Inspection Characteristic Description– Print Layout | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedure can be reviewed in the inspection plan with the quality planner role. |  |

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

For First Article Inspection only a small sample quantity , e.g. 1 is ordered for inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Purchaser. | The Fiori Launchpad displays. |  |
| 2 | Open Manage Purchase Orders | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. | The Purchase Order screen displays. |  |
| 4 | Enter Purchase Order data | Make the following data:General Information:Supplier : 33300001Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002Currency: AEDCreate an item, choose it and then Purchase Order Item screen displays. Make the following entries:Tab - General InformationMaterial: RM0509Plant: 3310Order Quantity: 1Storage Location: 331CTab – Schedule LinesDelivery date: a date in the futureChoose Apply. | Supplier 33300006 supports also the process BMK Return to Supplier; supplier 33300001 only supports to return to supplier without delivery. We are using Purchasing Group 002 here.Back to the Purchase Order screen. |  |
| 5 | Save Purchase Order | Choose the Order to save the purchase order. | A new Purchase Order is created. The system displays the message Purchase Order has been created. |  |

#### Change Quality Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

First article inspections are controlled in the quality info record by maintaining the corresponding purchase order item for first article delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Quality Info Records (F2256A). | The Manage Quality Info Records screen displays. |  |
| 3 | Enter Search Fields | Make the following entries and choose Go.Plant: 3310Material: RM0509Supplier: 33300001 |  |  |
| 4 | Select Quality Info Record | In the results table, open the respective quality info record with a click.In the Production Part Approval section, review PPAP Level and PPAP Status fields. | Quality info record is opened in display mode. |  |
| 5 | Change Quality Info Record | Choose Edit to switch to edit mode.Press Enable button. | Quality info record was changed.Now, the Production Part Approval (PPAP) is enabled.Note You can also define the different PPAP Level (e.g. Warrant Only, Warranty with Product Samples and Limited Supporting Data) and PPAP Status (e.g. in Process). Both, PPAP Level and PPAP Status are not required for First Article Inspection. |  |
| 6 | Prepare Quality Info Record for FAI | After enabling the PPAP in quality info record: Link the purchase order and item from previous step.Choose Add.Enter Purchasing Document and Item. | With this maintenance the system controls that inspection plan with inspection plan usage GR Model Inspection (51) will be assigned to the inspection lot after goods receipt for purchase order. |  |
| 7 | Save Your Data | Choose Save. | Your data is saved. |  |

#### Display Material Stock before Goods Receipt (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the material stock is done.

Prerequisite

The goods receipt from purchase order was posted for the raw material to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material | Make the following entry and press Enter.Material: RM0509 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and storage location 331C specifically. And have a look in the same plant at the unrestricted stock, blocked stock and the storage location 331R for later use. |  |  |

#### Post Goods Receipt for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods ordered by a purchase order arrive in the warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Open Post Goods Receipt for Purchase Order | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search Purchase Order | Enter Purchase Order. | The system displays the data for the goods receipt. If the Storage Location was not specified in the Purchase Order, it needs to be maintained now (for example, 331C). |  |
| 4 | Maintain Manufacturing Date | Choose the Item Tab and make the following entryProduction Date: <Today-1 week> | The manufacturing date is maintained. Optionally, you can maintain a batch number. |  |
| 5 | Post | Select the item. Choose Post. | The system displays the message: x document(s) created: Material Document xxxxxxxxxx/xx.In case you want to print the goods receipt slip, you can follow the description in Procurement of Direct Materials (J45). |  |

#### Display Material Stock Before Quality Inspection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the material stock is done. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from purchase order was posted for the raw material to quality inspection stock.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material | Make the following entry and choose Enter:Material: RM0509 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and storage location 331C. | Quantity received is posted in quality stock. |  |

#### Quality Inspection (FAI)

The raw material undergoes a quality inspection to ensure that it meets the predefined quality requirements.

In this step, the quality technician records the inspection result for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot has been created automatically upon goods receipt for the purchase order.

For first article against purchase order, system creates an inspection lot with inspection type "01" and inspection plan usage "GR Model Inspection".

##### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan. |  |

##### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the goods receipt and purchase order are verified as well as the sample size used for quality inspection reviewed.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Select Inspection Lot | In the inspection lot list, select the inspection lot which you created before. | Inspection lot is displayed. |  |
| 4 | Check Inspection Lot by Selecting the Line | Under Origin, verify the referenced purchase order and material document.Additionally you can look for the inspection type. | The purchase order number and material document number from which the inspection lot originates are displayed.Inspection Type is Goods Receipt. |  |
| 5 | Choose Operation (0010) | In Result, choose operation Goods Receipt Inspection. |  |  |
| 6 | Choose Characteristic (0010) | Click Goods Receipt Inspection in the Characteristics column.Go back to previous screen. | A dialog box appears with the Characteristics Details. |  |
| 7 | Choose Operation (0020) | In Result, choose operation Print Layout Check (Foil). |  |  |
| 8 | Choose Characteristic (0010) | Click Print Layout in the Characteristics column. | A dialog box appears with the characteristics details. |  |

##### Record Inspection Results

Procedure

Record Inspection Results for the Inspection Lot (First Article Inspection) with different work centers.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Record Inspection Results for Operation 0010

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entry and choose Go.Purchase Order: <Purchase Order ID> (from previous step). | If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchase Order from Add Filter drop down and choose OK. Choose Go.Alternatively, you can search for the inspection lot <Inspection Lot ID> (from previous step). |  |
| 4 | Display the Corresponding Operations | Switch from Inspection Lots list tab to the Operations list tab. | Both Inspection lot operations with relevant work center are offered. |  |
| 5 | Enter additional Filter Fields | Expand Header for additional filter, make the following entry and choose Go.Work Center: QMLABS | If Work Center is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center from Add Filter drop down and choose OK.Choose Go.Only Inspection lot operations and master characteristics for filtered work center will be offered for results recording. |  |
| 6 | Choose Record Results | Choose Record Multiple Results. |  |  |
| 7 | Enter Inspection Result | Choose Edit.Depending on the inspection result, select one of the following two options:Positive ResultGoods Receipt Inspection: Code Group - Code: QUAL01 OKNegative ResultGoods Receipt Inspection: Code Group - Code: QUAL01 NOKNote Remark field is mandatory | For qualitative characteristic (Goods Receipt Inspection) the search help is needed to select a value.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. |  |
| 8 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for work center QMLABS has been performed and results recorded. |  |

Record Inspection Results for Operation 0020

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entry and choose Go.Purchase Order: <Purchase Order ID> (from previous step). | If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchase Order from Add Filter drop down and choose OK. Choose Go.Alternatively, you can search for the inspection lot <Inspection Lot ID> (from previous step). |  |
| 4 | Display the Corresponding Operations | Switch from Inspection Lots list tab to the Operations list tab. | Both Inspection lot operations with relevant work center are offered. |  |
| 5 | Enter additional Filter Fields | Expand Header for additional filter, make the following entry and choose Go.Work Center: QMCP | If Work Center is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center from Add Filter drop down and choose OK.Choose Go.Only Inspection lot operations and master characteristics for filtered work center will be offered for results recording. |  |
| 6 | Choose Record Results | Choose Record Multiple Results. |  |  |
| 7 | Enter Inspection Result | Choose EditDepending on the inspection result, select one of the following two options:Positive ResultPrint Layout: Code Group - Code: QUAL01 OKNegative ResultPrint Layout: Code Group - Code: QUAL01 NOKNote Remark field is mandatory | For qualitative characteristic (Print Layout) the search help is needed to select a value.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. |  |
| 8 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for work center QMCP has been performed and results recorded. |  |

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360)app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (Optional) | Choose card Inspection Lots Without Inspection Plan. | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4 | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision Chapter. |  |
| 5 | Select the Corresponding Inspection Lot you have created before (Optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative Entry to Chapter Manage Usage Decision. |  |
| 6 | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status. | Alternative Entry to Chapter Manage Usage Decision. |  |
| 7 | Select Card Inspection Lots Ready for Usage Decision (Optional) | Choose card Inspection Lots Ready for Usage Decision. | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the goods receipt depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entry and choose Go.Inspection Lot: From previous step |  |  |
| 4 | Select Corresponding Inspection Lot | Select the corresponding inspection lot. | The Usage Decision screen displays. |  |
| 5 | Choose Edit and Add Document | Choose Edit. In the Attachments section choose Upload, select the path and add the document. | For example to upload pictures to visualize the defect. |  |
| 6 | Enter UD code | Navigate to Usage Decision section.Depending on the inspection result, select one of the following two options.Positive ResultUD code: A1 (Accepted – unrestricted stock)A2 (Accepted-unrestricted – minor quality)A3 (Accepted-unrestricted-sample consumption)Negative ResultUD code: R1 (Rejected – blocked stock)R210 (Rejected-return supplier w/o delivery)R220 (Rejected-return supplier with delivery) | Note The corresponding Stock Posting is processed automatically in the background for the complete quantity for Usage Decision codes A1, A2, R1, R210 and R220. |  |
| 7 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted in different stock posting proposals. | Note For the First Article Inspection (FAI), the inspection lot contains a small sample quantity which will usually be kept in the QMCP work center. If you want to document sample consumption, you can do this manually while usage decision. |  |
| 8 | Save Usage Decision | Choose Save.Choose Yes if dialog Confirmation Prompt appear. | The usage decision is made with regard to the raw material. The system automatically triggers the material movements associated with the usage decision code or according to modified stock posting.Usage decision code provides Valuation Code (Accepted or Rejected) and transfers it to the quality info record purchase order item line. |  |

#### Display Material Stock After Quality Inspection (Optional)

Based on the usage decision, review the updated stock situation to confirm the lot’s availability or restrictions.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, we now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

Dependent on the usage decision of the previous steps, the quantity of the material is posted.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock – Single Material screen displays. |  |
| 3 | Enter Selection Fields | Make the following entry and press Enter.Material: RM0509 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock and Blocked storage location: 331C/331R. | The stock quantities for material RM0509 are updated based on the quality inspection and respective usage decision of the previous steps.After posting FAI quantity into sample consumption, the stock is reduced for that quantity. |  |

#### Review Quality Info Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

First article inspections are controlled in the quality info record by maintaining the corresponding purchase order item for first article delivery. After usage decision of FAI inspection lot, the valuation code is populated in quality info record to respective purchase order item line.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Quality Info Records (F2256A). | The Manage Quality Info Records screen displays. |  |
| 3 | Enter Search Fields | Make the following entries and choose Go.Plant: 3310Material: RM0509Supplier: 33300001 |  |  |
| 4 | Select Quality Info Record | In the results table, open the respective quality info record with a click.In the Production Part Approval section, review PPAP Level and PPAP Status fields. | Quality info record is opened in display mode. |  |
| 5 | Review Valuation Code | Review Purchasing Document and Item from previous step. | Quality info record was changed.Dependent on the usage decision of the previous steps, Valuation Code changes from Not valuated to Accepted or Rejected. |  |

### Accepted FAI (Case 1): Regular Quality Inspection for 2nd Purchase Order

Procedure

After acceptance of first article inspection, proceed with the creation of a new purchase order (second iteration). Therefore, repeat steps [Create Purchase Order](#unique_11) [page ] 16 and create purchase order. Then proceed with steps [Display Material Stock before Goods Receipt (Optional)](#unique_13) [page ] 19 to [Display Material Stock After Quality Inspection (Optional)](#unique_36) [page ] 29 and perform the goods receipt inspection using the regular inspection plan. This inspection plan is automatically assigned by the system because the corresponding purchase order item is NOT maintained in the quality info record.

Compare inspection type of inspection lot (regular inspection).

Check the quantities that are posted automatically using the usage decision code. To do so, you can follow the description in Quality Management in Procurement (1FM).

|  |
| --- |
| Note Note: If the first article inspection has been rejected in [Make Usage Decision](#unique_20) [page ] 28, skip [Accepted FAI (Case 1): Regular Quality Inspection for 2nd Purchase Order](#unique_37) [page ] 31 and continue with [Rejected FAI (Case 2): New FAI Inspection for 2nd Purchase Order (Optional)](#unique_38) [page ] 35. |

#### Create Purchase Order

Procedure

Execute step [Create Purchase Order](#unique_11) [page ] 16 and create a new purchase order with normal quantity, e.g. 30.

Note down the new purchase order no.: ___________________________

#### Display Material Stock before Goods Receipt (Optional)

Procedure

Execute step [Display Material Stock before Goods Receipt (Optional)](#unique_13) [page ] 19 with the new purchase order.

#### Post Goods Receipt for Purchase Order

Procedure

Execute step [Post Goods Receipt for Purchase Order](#unique_14) [page ] 20 with the new purchase order.

#### Display Material Stock Before Quality Inspection (Optional)

Procedure

Execute step [Display Material Stock Before Quality Inspection (Optional)](#unique_15) [page ] 21 with the new purchase order.

#### Quality Inspection (Regular Inspection)

##### Display Quality Technician Overview (Optional)

Procedure

Execute step [Display Quality Technician Overview (Optional)](#unique_16) [page ] 22 with new purchase order.

##### Display Open Inspection Lots (Optional)

Procedure

Execute step [Display Open Inspection Lots (Optional)](#unique_17) [page ] 23 with the new purchase order.

Review Inspection Type.

|  |
| --- |
| Note The system recognizes, that this is a regular inspection. Therefore, the inspection plan (Regular Inspection) is assigned to the inspection lot. |

##### Record Inspection Results

Procedure

Execute step Record Inspection Results for Purchase Order with the new purchase order.

|  |
| --- |
| Note The system recognizes that this is a regular inspection. Therefore, the inspection plan (Regular Inspection) is assigned to the inspection lot. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Record Inspection Results for Operation 0010

Record Inspection Results for the Inspection Lot (Regular Inspection) with only one work center.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entry and choose Go.Purchase Order: <Purchase Order ID> (from previous step). | If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchase Order from Add Filter drop down and choose OK. Choose Go.Alternatively, you can search for the inspection lot <Inspection Lot ID> (from previous step). |  |
| 4 | Display the Corresponding Operations | Switch from Inspection Lots list to the Operations list. | Both Inspection lot operations with relevant work center are offered. |  |
| 5 | Enter Additional Filter Fields | Expand Header for additional filter, make the following entry and choose Go.Work Center: QMLABS | If Work Center is displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center from Add Filter drop down and choose OK.Choose Go.Only Inspection lot operations and master characteristics for filtered work center will be offered for results recording. |  |
| 6 | Choose Record Results | Choose Record Multiple Results. |  |  |
| 7 | Enter Inspection Result | Choose Edit.Depending on the inspection result, select one of the following two options:Positive ResultGoods Receipt Inspection: Code Group - Code: QUAL01 OKNegative ResultGoods Receipt Inspection: Code Group - Code: QUAL01 NOKNote Remark field is mandatory | For qualitative characteristic (Goods Receipt Inspection) the search help is needed to select a value.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. |  |
| 8 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for work center QMLABS has been performed and results recorded. |  |

##### Display Quality Engineer Overview (Optional)

Procedure

Execute step [Display Quality Engineer Overview (Optional)](#unique_19) [page ] 27 with new purchase order.

##### Make Usage Decision

Procedure

Execute step [Make Usage Decision](#unique_20) [page ] 28 with the new purchase order.

#### Display Material Stock After Quality Inspection (Optional)

Procedure

Execute step [Display Material Stock After Quality Inspection (Optional)](#unique_36) [page ] 29.

### Rejected FAI (Case 2): New FAI Inspection for 2nd Purchase Order (Optional)

Procedure

After the first article inspection has been rejected, further steps are required to overcome the identified issues and you need to order new material.

Therefore, you repeat some of the previous steps to create a new purchase order and re-execute quality steps for FAI. Another first article inspection is automatically triggered with a new entry of the purchase order item in the quality info record.

#### Create Purchase Order

Procedure

Execute step [Create Purchase Order](#unique_11) [page ] 16 and create a new purchase order with a small quantity, e.g. 1

Note down new purchase order no.: ___________________________

#### Change Quality Info Record

Procedure

Execute step [Change Quality Info Record](#unique_12) [page ] 18 with new purchase order created in step [Create Purchase Order](#unique_32) [page ] 35

Create a new line with the new purchase order item in the Quality Info Record.

#### Processing of the Purchase Order and Quality Inspection

Procedure

Repeat the following first article inspection steps with the new purchase order created in steps [Create Purchase Order](#unique_11) [page ] 16 and [Post Goods Receipt for Purchase Order](#unique_14) [page ] 20 :

1. [Quality Inspection (FAI)](#unique_35) [page ] 22
    1. [Record Inspection Results](#unique_18) [page ] 24
    2. [Make Usage Decision](#unique_20) [page ] 28

If the usage decision this time results in an acceptance of the material, proceed with the steps described in [Accepted FAI (Case 1): Regular Quality Inspection for 2nd Purchase Order](#unique_37) [page ] 31 for second purchase order.

If there are issues with the article again, repeat steps [Create Purchase Order](#unique_11) [page ] 16 to [Processing of the Purchase Order and Quality Inspection](#unique_39) [page ] 36 again.

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
- see-also :: [[13-quality-ehs-and-compliance/qualitatsinfosatz-anlegen-sds-bf5-550]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7L4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 64,439 chars in the whole document
