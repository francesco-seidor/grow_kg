---
id: 13-quality-ehs-and-compliance/quality-management-in-procurement-1fm-ae-test-script-sap-s-4hana-cloud
title: "Quality Management in Procurement (1FM_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1FM_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 1FM_AE (Quality Management in Procurement, UAE, 2608): prerequisites and five inspection test procedures with apps, roles and sample data."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-inspection-procurement-and-sales]
aliases: [1FM_S4CLD2608_BPD_EN_AE]
keywords: [Quality Inspection in Procurement and Sales, quality management in procurement, regular quality inspection, dynamic modification, sampling scheme, quality info record, quality certificate, usage decision, inspection results recording, test scripts prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1FM_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-717
topic: 13-quality-ehs-and-compliance/quality-inspection-procurement-and-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Quality Management in Procurement (1FM_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1FM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1FM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Quality Inspection in Procurement and Sales** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Quality Management in Procurement (1FM_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Quality Management in Procurement (1FM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232846917)

[2 Prerequisites 5](#_Toc232846918)

[2.1 System Access 5](#_Toc232846919)

[2.2 Roles 5](#_Toc232846920)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232846921)

[2.4 Business Conditions 7](#_Toc232846922)

[2.5 Preliminary Steps 8](#_Toc232846923)

[2.5.1 Create Info Record for Material QM001 8](#_Toc232846924)

[2.5.2 Create Info Record for Material QM002 & QM003 9](#_Toc232846925)

[2.5.3 Create Info Record for Material QM004 11](#_Toc232846926)

[2.5.4 Create Info Record for Material QM005 12](#_Toc232846927)

[2.5.5 Create Quality Info Record in Procurement 13](#_Toc232846928)

[2.5.6 Integration of Quality Management in the Production Part Approval Process (PPAP) First Article Inspection 14](#_Toc232846929)

[3 Overview Table 15](#_Toc232846930)

[4 Test Procedures 19](#_Toc232846931)

[4.1 Regular Quality Inspection Process 19](#_Toc232846932)

[4.1.1 Create Purchase Order 19](#_Toc232846933)

[4.1.2 Display Inspection Plan for Inspection Characteristics (Optional) 20](#_Toc232846934)

[4.1.3 Display Material Stock before Goods Receipt (Optional) 21](#_Toc232846935)

[4.1.4 Post Goods Receipt for Purchase Order 22](#_Toc232846936)

[4.1.5 Display Material Stock Before Quality Inspection (optional) 23](#_Toc232846937)

[4.1.6 Quality Inspection 24](#_Toc232846938)

[4.1.6.1 Display Quality Technician Overview (Optional) 24](#_Toc232846939)

[4.1.6.2 Display Open Inspection Lots (optional) 25](#_Toc232846940)

[4.1.6.3 Record Inspection Results 26](#_Toc232846941)

[4.1.6.4 Print Inspection Report (optional) 29](#_Toc232846942)

[4.1.6.5 Display Quality Engineer Overview (Optional) 30](#_Toc232846943)

[4.1.6.6 Make Usage Decision 31](#_Toc232846944)

[4.1.7 Display Material Stock after Quality Inspection (optional) 33](#_Toc232846945)

[4.1.8 Display Inspection Results History (Optional) 34](#_Toc232846946)

[4.1.9 Display Manage Defects (Optional) 35](#_Toc232846947)

[4.2 Quality Inspection Process with Dynamic Modification 36](#_Toc232846948)

[4.2.1 Execute Regular Quality Inspection Process 37](#_Toc232846949)

[4.2.2 Display Quality Level (optional) 37](#_Toc232846950)

[4.2.3 Create Second Purchase Order 38](#_Toc232846951)

[4.2.4 Post Goods Receipt for Purchase Order 40](#_Toc232846952)

[4.2.5 Display Material Stock (optional) 41](#_Toc232846953)

[4.2.6 Display Quality Level (optional) 41](#_Toc232846954)

[4.2.7 Analyze Quality Level History (optional) 42](#_Toc232846955)

[4.3 Quality Inspection Process with Sampling Scheme and Dynamic Modification 42](#_Toc232846956)

[4.3.1 Create Purchase Order 45](#_Toc232846957)

[4.3.2 Display Inspection Plan and Derive the Sampling Scheme (optional) 47](#_Toc232846958)

[4.3.3 Post Goods Receipt for Purchase Order – 1st iteration 48](#_Toc232846959)

[4.3.4 Display Quality Level – 1st iteration 49](#_Toc232846960)

[4.3.5 Quality Inspection – 1st iteration 50](#_Toc232846961)

[4.3.6 Display Quality Level 51](#_Toc232846962)

[4.3.7 Post Goods Receipt for Purchase Order – 2nd iteration 51](#_Toc232846963)

[4.3.8 Quality Inspection – 2nd iteration 52](#_Toc232846964)

[4.3.9 Display Quality Level – 2nd iteration 54](#_Toc232846965)

[4.3.10 Post Goods Receipt for Purchase Order – 3rd iteration 54](#_Toc232846966)

[4.3.11 Quality Inspection – 3rd iteration 55](#_Toc232846967)

[4.3.12 Analyze Quality Level History (optional) 57](#_Toc232846968)

[4.4 Quality Inspection Process with Material-Supplier Release 57](#_Toc232846969)

[4.4.1 Check Overview Page for Quality Engineer (optional) 57](#_Toc232846970)

[4.4.2 Review or Change Quality Info Record (optional) 58](#_Toc232846971)

[4.4.3 Create Purchase Order 59](#_Toc232846972)

[4.5 Quality Inspection Process with Quality Certificate in Procurement 60](#_Toc232846973)

[4.5.1 Review Quality Settings in Material Master (Optional) 61](#_Toc232846974)

[4.5.2 Create Purchase Order 61](#_Toc232846975)

[4.5.3 Post Goods Receipt for Purchase Order 62](#_Toc232846976)

[4.5.4 Review Inspection Lot Status Before Receipt of Quality Certificate (Optional) 62](#_Toc232846977)

[4.5.5 Enter Receipt of Quality Certificate 63](#_Toc232846978)

[4.5.5.1 Alternative 1: Enter Receipt of Quality Certificate Manually 63](#_Toc232846979)

[4.5.5.2 Alternative 2: Enter Receipt of Quality Certificate with SAP Document AI 64](#_Toc232846980)

[4.5.6 Review Inspection Lot Status After Receipt of Quality Certificate (Optional) 65](#_Toc232846981)

[4.5.7 Quality Inspection 65](#_Toc232846982)

[5 Appendix 66](#_Toc232846983)

[5.1 Process Integration 66](#_Toc232846984)

[5.1.1 Succeeding Processes 66](#_Toc232846985)

## Purpose

Overview

This scope item manages quality inspection in procurement: At goods receipt, a good is posted to quality inspection stock and an inspection lot is created based on an inspection plan. The quality technician records the inspection results. The quality engineer then makes a usage decision – for example, accepting or rejecting the material, posting the material to unrestricted stock or blocked stock, or triggering return to the supplier, with the option of posting as a consumed sample. For rejected results, a defect is automatically recorded. The supplier is rated on the quality score defined in the usage decision. With a dynamic modification rule, quality inspections can be tightened, reduced, or skipped based on previous inspection results. You can block the creation of purchase orders or limit the purchased quantity due to quality reasons. By leveraging quality certificates in procurement, you can ensure that suppliers provide the documents if required.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Master data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Shop floor w/o lean WM |
| Storage Location | 331R | Storage Location Returns | Return storage location |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 002 | Group 002 |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Supplier | 33300006 | Domestic UAE Supplier 6 | The goods can be returned to supplier with delivery if quality issue. |
| Material Group | L001 | License 001 |  |
| Material | QM001 | QM Regular | Used in Regular Quality Inspection Process |
| Material | QM002 | QM Q-Info-Record | Used in Quality Inspection Process with Material supplier Release |
| Material | QM003 | QM Dynamic Modification | Used in Quality Inspection Process with Dynamic Modification |
| Material | QM004 | QM Sampling Scheme | Used in Quality Inspection Process with Sampling Scheme and Dynamic Modification |
| Material | QM005 | QM Quality Certificate in Procurement | Used in Quality Inspection Process with Quality Certificate in Procurement |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNY | Create Quality Management Attributes for Material/Product Master - MDS |
| BF5 | Create Quality Info Record - MDS |
| BHD | Create Purchasing Info Record - MDS |

|  |
| --- |
| Note Make sure that the following fields are filled out in business partner (BP) data before start testing:CNPJ number (identification tab)State tax Number (identification tab)ICMS Contributor (Control tab)IPI Contributor (Control tab)PIS Contributor (Control tab)COFINS Contributor (Control tab)ICMS-ST Contributor (Control tab)ISS Contributor (Control tab) (mandatory for buying services)In the role Supplier, tab Vendor: Tax Data fill out the fields accordingly.Failure to complete the fields will result in an error in the invoice entry process. |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, it must be possible to purchase materials. Prerequisite for 1FM is that the scope item J45 is active and available in the system. |
| BNQ - Create Quality Inspection Plan - MDS | Complete the steps in Add document to inspection method in the chapter Create/Change Inspection Method in BNQ to display attachments for the Inspection Method in chapter Regular Quality Inspection Process - Display Open Inspection Lots (optional) in 1FM. |
| BNZ - Create New Open MM Posting Period - MDS | Complete all steps in the master data script. Posting Period is up to date. |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | Complete all steps in the master data script for inspection type 01. |
| BF5 - Create Quality Info Record - MDS | Complete all steps in the master data script to run the test procedure Quality Inspection Process with Material-supplier Release. |

### Preliminary Steps

#### Create Info Record for Material QM001

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Info Record Description: <Short text>Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Purchasing Group: 002Material Group: L001Material: QM001 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX>, for example, 2Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: for example, 10Goods-Receipt-Based Invoice Verification: unmarked | Delivery and Quantity Data is added. |  |
| 6 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Today’s Date>Amount: 10Pricing Unit: 1Valid To: 12/31/9999Currency: AEDChoose the Apply icon. | Condition Data is added. |  |
| 7 | Save Your Data | Choose Create. | A purchasing info record is saved.Note down the purchasing info record number. |  |
| 8 | Repeat Entire Steps and Create an Info. Record | Repeat the entire steps and create an info record for the master data:Supplier:33300006Material: QM001 |  |  |

#### Create Info Record for Material QM002 & QM003

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Info Record Description: <Short text>Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300006Purchasing Group: 002Material Group: L001Material: QM002 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX>, for example, 2Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: for example, 10Goods-Receipt-Based Invoice Verification: unmarked | Delivery and Quantity Data is added. |  |
| 6 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Today’s Date>Amount: 10Pricing Unit: 1Valid To: 12/31/9999Currency: AEDChoose the Apply icon. | Condition Data is added |  |
| 7 | Save your data | Choose Create. | A purchasing info record is saved.Note down the purchasing info record number. |  |
| 8 | Repeat entire steps and create a new info record | Repeat the entire steps and create a new info record for the master data below:Supplier: 33300006Material: QM003 |  |  |

#### Create Info Record for Material QM004

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Info Record Description: <Short text>Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Purchasing Group: 002Material Group: L001Material: QM004 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days<XX>, for example, 2Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: for example, 10Goods-Receipt-Based Invoice Verification: unmarked | Delivery and Quantity Data is added. |  |
| 6 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data::Valid From: <Today’s Date>Amount: 10Pricing Unit: 1Valid To: 12/31/9999Currency: AEDChoose the Apply icon. | Condition Data is added |  |
| 7 | Save your data | Choose Create. | A purchasing info record is saved.Note down the purchasing info record number. |  |
| 8 | Repeat entire steps and create a new info record | Repeat the entire steps and create a new info record for the master data below:Supplier:33300006Material: QM004 |  |  |

#### Create Info Record for Material QM005

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Info Record Description: <Short text>Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300006Purchasing Group: 002Material Group: L001Material: QM005 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX>, for example, 2Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: for example, 10Goods-Receipt-Based Invoice Verification: unmarked | Delivery and Quantity Data is added. |  |
| 6 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Today’s Date>Amount: 10Pricing Unit: 1Valid To: 12/31/9999Currency: AEDChoose the Apply icon. | Condition Data is added |  |
| 7 | Save Your Data | Choose Create. | A purchasing info record is saved.Note down the purchasing info record number. |  |

#### Create Quality Info Record in Procurement

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Quality Info Records (F2256A). | The Manage Quality Info Records screen displays. |  |
| 3 | Open New Quality Info Record | Choose Create. | The Quality Info Record screen displays. |  |
| 4 | Enter General Data | Make the following entries:Material: QM002Plant: 3310Supplier: 33300006 |  |  |
| 5 | Enter Release Data | In the Release section, enter the following data:Release Until: 12/31/9999 alt.31/12/9999Release Qty Active: flaggedRelease Quantity: for example, 15 |  |  |
| 6 | Enter Block Data | In the Block section, enter the following data:Block Reason: Quality Limitation (Q-Inf) |  |  |
| 7 | Save Your Data | Choose Create. | Your data is saved. |  |

|  |
| --- |
| Note Integration of Quality Management in the Production Part Approval Process (PPAP) First Article Inspection.First article inspections are controlled in the quality info record by maintaining the corresponding purchase order item for first article delivery. There is a separate inspection plan usage for first article inspection. Here is the brief overview.In the material master, select inspection type "GR for purchase order" (01) and define the procurement control key, such as "Vendor Release" (0001). Next step, define the inspection plan with inspection plan usage "GR Model Inspection" (51). The inspection plan usage specifies which inspection plan should be used for First Article Inspection.Now enable Production Part Approval (PPAP) using the Manage Quality Info Records (F2256A) app. You can also define different PPAP levels, such as warranty only, warranty with product samples and limited supporting data. After enabling the PPAP in quality info record, link the purchase order and item within Manage Quality Info Records (F2256A) app.Finally post goods receipt for first article against purchase order. The system creates an inspection lot with inspection type "01" and inspection plan usage "GR Model Inspection". |

#### Integration of Quality Management in the Production Part Approval Process (PPAP) First Article Inspection

First article inspections are controlled in the quality info record through maintaining the corresponding purchase order item for first article delivery. This requires a separate inspection plan usage for first article inspection. Here is the brief overview of the process.

First from the material master select inspection type "GR for purchase order" (01) and define the procurement control key, for example, "Vendor Release" (0001). Then define the inspection plan with inspection plan usage "GR Model Inspection" (51). This inspection plan usage specifies which inspection plan should be used for first article inspection.

Next you can enable Production Part Approval Process (PPAP) in the App Manage Quality Info Records (F2256A). You can choose to define different PPAP levels for example for warranty only, warranty with product samples and limited supporting data. After enabling the PPAP in quality info record, you can ink the purchase order and item in the same App.

Finally, you can post goods receipt for first article against purchase order. System will generate an inspection lot with inspection type "01" and inspection plan usage "GR Model Inspection".

For more information, please refer to the Master Data Script Create Quality Info Record - MDS (BF5).

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Regular Quality Inspection Process

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_14) [page ] 19 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is created |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_15) [page ] 20 | Quality Technician | Display Inspection Plan (QP03) | The data of inspection plan for the supplier and material is displayed.If it is not available the Inspection Planner needs to create one (see Master Data Scripts section) |
| [Display Material Stock before Goods Receipt (Optional)](#unique_16) [page ] 21 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. |
| [Post Goods Receipt for Purchase Order](#unique_17) [page ] 22 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt for PO is posted. |
| [Display Material Stock Before Quality Inspection (optional)](#unique_18) [page ] 23 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. The goods receipt quantity from previous step is shown in the quality stock. |
| [Display Quality Technician Overview (Optional)](#unique_19) [page ] 24 | Quality Technician | Quality Technician Overview (F2361) | List of open inspection results is displayed. |
| [Display Open Inspection Lots (optional)](#unique_20) [page ] 25 | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. The Quality Engineer can select the next inspection lot he or she wants to record the usage decision for. |
| [Record Inspection Results](#unique_21) [page ] 26 | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded |
| [Display Quality Engineer Overview (Optional)](#unique_22) [page ] 30 | Quality Engineer | Quality Engineer Overview (F2360) |  |
| [Make Usage Decision](#unique_23) [page ] 31 | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted |
| [Display Material Stock after Quality Inspection (optional)](#unique_24) [page ] 33 | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. Depending on the usage decision, the stock quantity is shown in the blocked stock, in unrestricted or in another storage location. |
| [Display Inspection Results History (Optional)](#unique_25) [page ] 34 | Quality Engineer | Results History (F2428) |  |
| [Display Manage Defects (Optional)](#unique_26) [page ] 35 | Quality Engineer | Manage Defects (F2649) |  |

Quality Inspection Process with Dynamic Modification

| Process Step, Report or Item | Business Role | Transaction/APP Name | Expected Results |
| --- | --- | --- | --- |
| [Execute Regular Quality Inspection Process](#unique_27) [page ] 37 |  |  |  |
| [Display Quality Level (optional)](#unique_28) [page ] 37 | Quality Engineer | Manage Quality Levels (F2914) | The dynamic modification level is displayed. |
| [Create Second Purchase Order](#unique_29) [page ] 38 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is created |
| [Post Goods Receipt for Purchase Order](#unique_30) [page ] 40 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt for PO is posted. |
| [Display Material Stock (optional)](#unique_31) [page ] 41 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Display Quality Level (optional)](#unique_32) [page ] 41 | Quality Engineer | Manage Quality Levels (F2914) | The dynamic modification level is displayed. |
| [Analyze Quality Level History (optional)](#unique_33) [page ] 42 | Quality Engineer | Quality Level History - Skip Rate in Last 180 Days (F2915) |  |

Quality Inspection Process with Sampling Scheme and Dynamic Modification

| Process Step, Report or Item | Business Role | Transaction/APP Name | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_34) [page ] 45 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | Purchase Order is created. |
| [Display Inspection Plan and Derive the Sampling Scheme (optional)](#unique_35) [page ] 47 | Quality Planner | Display Inspection Plan (QP03) | The inspection plan is displayed. |
| [Post Goods Receipt for Purchase Order – 1st iteration](#unique_36) [page ] 48 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The first goods receipt is posted. |
| [Display Quality Level – 1st iteration](#unique_37) [page ] 49 | Quality Engineer | Manage Quality Levels (F2914) | Quality level is displayed. |
| [Quality Inspection – 1st iteration](#unique_38) [page ] 50 | Quality Technician | Record Inspection Results (F1685A) |  |
| [Post Goods Receipt for Purchase Order – 2nd iteration](#unique_39) [page ] 51 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The second goods receipt is posted. |
| [Display Quality Level – 2nd iteration](#unique_40) [page ] 54 | Quality Engineer | Manage Quality Levels (F2914) | Quality level is displayed. |
| [Post Goods Receipt for Purchase Order – 3rd iteration](#unique_41) [page ] 54 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The third goods receipt is posted. |
| [Quality Inspection – 2nd iteration](#unique_42) [page ] 52 | Quality Technician | Record Inspection Results (F1685A) |  |
| [Post Goods Receipt for Purchase Order – 3rd iteration](#unique_41) [page ] 54 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The third goods receipt is posted. |
| [Quality Inspection – 3rd iteration](#unique_43) [page ] 55 | Quality Technician | Record Inspection Results (F1685A) |  |

Quality Inspection Process with Material-Supplier Release

| Process Step, Report or Item | Business Role | Transaction/APP Name | Expected Results |
| --- | --- | --- | --- |
| [Check Overview Page for Quality Engineer (optional)](#unique_44) [page ] 57 | Quality Engineer | Quality Engineer Overview (F2360) | The Quality Engineer Overview displays. |
| [Review or Change Quality Info Record (optional)](#unique_45) [page ] 58 | Quality Planner | Manage Quality Info Records (F2256A) | The quality info record is displayed. |
| [Create Purchase Order](#unique_46) [page ] 59 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is not created because of the settings in the quality info record. |

Quality Inspection Process with Quality Certificate in Procurement

| Process Step, Report or Item | Business Role | Transaction/APP Name | Expected Results |
| --- | --- | --- | --- |
| [Review Quality Settings in Material Master (Optional)](#unique_47) [page ] 61 | Master Data Specialist - Product Data | Display Material (MM03) | The Display Material (Initial Screen) is displayed. |
| [Create Purchase Order](#unique_48) [page ] 61 | Purchaser | Manage Purchase Orders (F0842A) | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items. |
| [Post Goods Receipt for Purchase Order](#unique_49) [page ] 62 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt for Purchase Order screen displays. |
| [Review Inspection Lot Status Before Receipt of Quality Certificate (Optional)](#unique_50) [page ] 62 | Quality Technician | Manage Inspection Lots (F2343) | The Manage Inspection Lots screen displays. |
| Enter Receipt of Quality Certificate |  |  |  |
| [Alternative 1: Enter Receipt of Quality Certificate Manually](#unique_51) [page ] 63 | Quality Technician | Manage Certificate Receipts (F3233) | The Manage Certificate Receipts screen displays. |
| [Alternative 2: Enter Receipt of Quality Certificate with SAP Document AI](#unique_52) [page ] 64 | Quality Technician | Upload Quality Certificate Documents - SAP Document AI (F8858) | The Upload Quality Certificate Documents screen displays. |
| [Review Inspection Lot Status After Receipt of Quality Certificate (Optional)](#unique_53) [page ] 65 |  |  |  |
| [Quality Inspection](#unique_54) [page ] 65 |  |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Regular Quality Inspection Process

Purpose

In this regular inspection process, the material QM001 is purchased.

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Purchaser. | The Fiori Launchpad displays. |  |
| 2 | Open Manage Purchase Orders | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. | The Purchase Order screen displays. |  |
| 4 | Enter Purchase Order Data | Make the following data:General Information:Supplier: 33300006Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002Currency: AEDCreate an item, choose it and then the Purchase Order Item screen displays. Make the following entries:Tab - General InformationMaterial: QM001Plant: 3310Order Quantity: 30Tab – Schedule LinesDelivery date: a date in the futureTab – Delivery DetailsStorage Location: 331AChoose Apply. | Supplier 33300006 also supports the process BMK Return to Supplier; supplier 33300001 only supports to return to supplier without delivery. We are using Purchasing Group 002 here.Back to the Purchase Order screen. |  |
| 5 | Save Purchase Order | Choose the Order to save the purchase order. | A new Purchase Order is created. The system displays the message Purchase Order has been created. |  |

#### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the inspection plan is related the trading goods. The inspection plan defines all inspection characteristics used later in the quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Plans (F3788). | The Manage Inspection Plans screen displays. |  |
| 3 | Enter Selection Fields | Adapt the filter by adding Material as filter criteria.Make the following entries and choose Go.Material: QM001Plant: 3310 |  |  |
| 4 | Select Inspection Plan | Select the entry with description Inspection Plan for Procurement, click on the selected line. |  |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the operation 0010 and click on the selected line.Got to Characteristics. | The Characteristics Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There are two Master Inspection Characteristics:One is Qualitative – SurfaceOne is Quantitative – Length | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedure can be reviewed in the inspection plan with the quality planner role. |  |

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

The goods receipt from purchase order was posted for the trading goods to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material | Make the following entry and press Enter.Material: QM001 | Stock for the material is displayed. |  |
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
| 4 | Post | Select the item. Choose Post. | The system displays the message: x document(s) created: Material Document xxxxxxxxxx/xx.In case you want to print the goods receipt slip, you can follow the description in Procurement of Direct Materials (J45). |  |

#### Display Material Stock Before Quality Inspection (optional)

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

The goods receipt from purchase order was posted for the trading goods to quality inspection stock.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock Single Material screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material : QM001 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and storage location 331A. | Quantity received is posted in quality stock. |  |

#### Quality Inspection

The trading goods undergo a quality inspection to ensure that it meets the predefined quality requirements.

In this step, the quality technician records the inspection result for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot has been created automatically upon goods receipt for the purchase order.

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

##### Display Open Inspection Lots (optional)

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
| 4 | Check Inspection Lot by Selecting the Line | Under Origin, verify the referenced purchase order and material document. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 5 | Choose Operation (optional) | In Result, choose operation QM for Procurement GR. | For checking the attachment in the inspection method optionally.If you have attached a document in the inspection method as described in BNQ - Create Quality Inspection Plan - MDS, the Quality Technician can review the attachment referring to step 7 to 9. |  |
| 6 | Choose Characteristic (optional) | Click Surface in the characteristics column. | A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 7 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the surface is displayed. |  |  |
| 8 | Display Text | In General , Long Text is displayed. |  |  |

##### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

|  |
| --- |
| Note For the purpose of recording multiple results for several inspection lots, the app Record Inspection Results in Table Form (F3365) can be used. In this app you can record the inspection results for several master inspection characteristics for different inspection lots in a table on a single screen, for example inspecting one characteristic for several materials. This is described in the optional step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchase Document: From previous step | If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchase Order and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Record Results | Choose Record Multiple Results in the bottom-right corner. |  |  |
| 6 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultSurface: Code Group - Code SURFACE 0020 (Smooth)Length: Mean Value (cm): 160Negative ResultSurface: Code Group - Code SURFACE 0010 (Rough)Length: Mean Value (cm): 90 | For qualitative characteristic (Surface) the search help is needed to select a value. For the quantitative characteristic (Length) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic. |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for procurement goods has been performed and result recorded. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for multiple inspection lots at the same time (mass processing), execute the following process flow.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365). | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the pop-up window Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 | Show Work Center (Optional) | Choose the Settings icon in the upper-right corner of the table. In the Define Column Properties pop-up, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Note Depending on the defined valuation mode (check inspection method details), the valuation is either done automatically by the system or must be done manually by the user.If an inspection result requires an inspection remark (check master inspection characteristic settings), it is not possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

##### Print Inspection Report (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Print inspection report by following the steps below.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go.For example, select the inspection lot for which inspection results have been recorded in the previous step. | A list of inspection lot(s) is displayed. |  |
| 4 | Select an Inspection Lot and enter the Inspection Lot Object Page | Select the inspection lot and enter the Inspection Lot Object Page by clicking the arrow at the end of the entry line. | The Inspection Lot Object Page screen displays. |  |
| 5 | Print the Inspection Report | Click on the Print Inspection Report button in the upper-right corner.On the window that pops up, select the channel Printout.To display a preview, click the button Display Document at the end of the line.Note To generate a print output, a printer has to be set up accordingly. | Print preview of the inspection report is displayed. |  |

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360)app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision. If negative inspection results are recorded, you can check the detect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (Optional) | Choose card Inspection Lots Without Inspection Plan. | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4 | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision Chapter. |  |
| 5 | Select the Corresponding Inspection Lot you have created before (Optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative Entry to Chapter Manage Usage Decision. |  |
| 6 | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative Entry to Chapter Manage Usage Decision. |  |
| 7 | Select Card Inspection Lots Ready for Usage Decision (Optional) | Choose card Inspection Lots Ready for Usage Decision. | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 8 | In Card: Inspection Lots with Defects (Optional) | (In case negative inspection results have been recorded ) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 9 | In card: Top Defective Materials (Optional) | (In case negative inspection results have been recorded ) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 10 | In card: Top Defects (Optional) | (In case negative inspection results have been recorded ) Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Inspection Lot: From previous step |  |  |
| 4 | Select Corresponding Inspection Lot | Select the corresponding inspection lot. | The Inspection Lot screen displays. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available you when have recorded a Negative result. For a surface rejection, there will be a surface defect, for a length rejection, there will be a tolerance defect displayed. |  |
| 6 | Choose Edit and Add Document | Choose Edit. In the Document section choose Upload, select the path and add the document. | For example to upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Depending on the inspection result, select one of the following two options and then confirm with Save.UD code: A1 (Accepted – unrestricted stock)A2 (Accepted-unrestricted – minor quality)A3 (Accepted-unrestricted-sample consumption)Negative ResultUD code: R1 (Rejected – blocked stock)R210(Rejected-return supplier w/o delivery)R220 (Rejected-return supplier with delivery)Choose Yes if dialog Confirmation Prompt appear. | Note The corresponding Stock Posting is processed automatically in the background for the complete quantity for Usage Decision codes A1, A2, R1, R210 and R220. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted in different stock posting proposals. | Note If you want to return a subset with UD code R220, you can split the quantity and post To Unrestricted Use and Return Inventory Posting, respectively. If you want to document sample consumption with UD code A3, you can split the quantity and post To Unrestricted Use and To Sample Consumption, respectively. It is also possible to transfer the (partial or full) quantity to a different material. |  |
| 8 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the trading goods. The system automatically triggers the material movements associated with the usage decision code. |  |

#### Display Material Stock after Quality Inspection (optional)

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

Dependent on the usage decision of the previous steps, the quantity of the material is posted differently.

- Positive Result (A1, A2,): quantity is increased in Unrestricted Use Stock and quantity is reduced in Quality Inspection Stock
- Positive Result for ‘sample consumption’ (A3): partial quantity is increased in Unrestricted Stock, inspected quantity is consumed and therefore not in stock anymore, and full quantity is reduced in Quality Inspection Stock
- Negative Result ‘Blocked Stock’ (R1) : quantity is increased in Blocked Stock and quantity is reduced in Quality Inspection Stock
- Negative Result ‘Return to Supplier w/o Delivery’ (R210): quantity is reduced in Quality Inspection Stock
- Negative Result ‘Return to Supplier with Delivery’ (R220): quantity is increased in return storage location Blocked Stock and quantity is reduced in Quality Inspection Stock

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076) . | The Stock – Single Material screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material: QM001 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked storage location331A/331R (in case of negative usage decision). | The stock quantities for material QM001 are updated based on the quality inspection and respective usage decision of the previous steps. |  |

#### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can compare the current inspection results with the results of past inspections. The evaluation is based on an inspection characteristic in the task list or master inspection characteristic. The selected samples are displayed in a list. A color-coded traffic light indicates which samples have been accepted or rejected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). |  |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic | A list of inspection characteristics displays. |  |
| 4 | Select Inspection Characteristics | Select an Inspection Characteristics, for example, Length. | Some information is shown about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability, such as Variance. |  |

#### Display Manage Defects (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. As an optional entry point for checking the details on the defects recorded other than the app Quality Engineer Overview, you can use the app Manage Defects. This app is only used in SAP S/4HANA Cloud Public Edition for Enterprise Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Defects (F2649). | Condition: negative results, for example, surface defects are recorded.The Manage Defects screen displays.Additional information: The analytical list page is divided into three sections: Compact/Visual filter, graphical, and tabular representation of data (top to bottom). Note that the applied filter in a higher page section influences the content that is displayed in a lower page section. |  |
| 3 | Search and analyze defects | Search defects by entering compact filter criteria (e.g. material, plant, inspection lot origin) or switch to Visual Filter by choosing the corresponding button in the top right corner. Drill down into the data in order to narrow down search results. | The Defects are filtered.Additional information: Visual filter displays top three defects by material, inspection lot origins or defect codes, respectively.It is also possible to drill down into the defects (e.g. by year/week, plant, defect code) and limit the results that are displayed in the results table by leveraging the drill down feature of the graphical representation of the data. By choosing the settings button (wheel symbol), the user can select the drill down level(s) and/or the order that is applied in order to cluster the data. |  |
| 4 | Display Defects details | In section Defects, select the defect and navigate to defect details by choosing the greater-than sign in the right column. | Defect detail data is displayed. |  |

### Quality Inspection Process with Dynamic Modification

Purpose

In this variant of the regular quality inspection process with dynamic modification rules , the material QM003 is purchased and only inspected at each 2nd goods receipt – in case the material is inspected o.k.

Prerequisite

You use an inspection plan with dynamic modification rule.

#### Execute Regular Quality Inspection Process

Purpose

In this step, follow the standard process variant as described in chapter [Regular Quality Inspection Process](#unique_56) [page ] 19 with material QM003 and a positive result for the usage decision.

#### Display Quality Level (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, check the dynamic modification at lot level. It is also possible to check the quality level for inspection characteristics as well, depending on the modification level maintained.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Quality Levels (F2914) | The Manage Quality Level screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go.Plant: 3310Material: QM003 |  |  |
| 4 | Check Quality Level | Select the respective inspection lot level and click the entry. | In the Quality Level tab, the next stage is expected to be 20 - Skip.Note Before entering the first goods receipt for this material the quality level should be 10 - Initial.Note Changes of the Quality level described in step 5 and step 6 will affect the following inspection processes. If you change the value, the process that is described in this chapter might not work as described here. |  |
| 5 | Update Quality Level (optional) | Choose Edit.In the tab Quality Level, update the Field:Next Stage: 20 - skipChoose Save. | A message Inspection stage 0020 corresponds to a skip is displayed.Note Change of the quality level will affect the following inspection processes. |  |
| 6 | Tighten the Quality Level (optional) | In the top right, choose the button Tighten. | A message indicating the respected quality level is tightened is expected.Note Change of the quality level will affect the following inspection processes. |  |

#### Create Second Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori Launchpad as a Purchaser. | The Fiori Launchpad displays. |  |
| 2 | Open Manage Purchase Orders | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. | The New Purchase Order screen displays. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data.General Information:Supplier: 33300006Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002Currency: AEDAdd an item, click on it, and the New Purchase Order Item screen displays. Make the following entries:Tab - General InformationMaterial: QM003Plant: 3310Order Quantity: 30Tab – Schedule LinesDelivery date: a date in the futureTab – Delivery DetailsStorage Location: 331AChoose Apply. | Supplier 33300006 also supports the process BMK – Return to Supplier with delivery; supplier 33300006 only supports to return to supplier without delivery.Back to the Purchase Order screen. |  |
| 5 | Save Purchase Order | Choose the Order button to save the Purchase Order. | A new Purchase Order is created. The system displays the message Purchase Order has been saved. |  |

#### Post Goods Receipt for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted. The usage decision is done automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Open Post Goods Receipt for Purchase Order | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search Purchase Order | Enter Purchase Order. | The system displays the data for the goods receipt. If the Storage Location was not specified in the Purchase Order, it needs to be maintained now (e.g. 331A). |  |
| 4 | Select Item | Select the items for which a goods receipt is to be posted. | The Post button is activated. |  |
| 5 | Post | Choose the Post button. | The material is posted to unrestricted stock.The Post Goods Receipt screen displays. The system displays the message Material document xxx posted.Since the derived inspection lot is a skip lot, the inspection lot has the usage decision UD01 – A9 automatically assigned. |  |

#### Display Material Stock (optional)

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock – Single Material screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material: QM003 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock. | The Unrestricted Stock quantity for QM003 is increased. |  |

#### Display Quality Level (optional)

Purpose

In this step, follow the standard process variant as described in chapter [Display Quality Level (optional)](#unique_28) [page ] 37 in order to display the current quality level and next inspection stage. After the automated usage decision, the next stage is expected to be 30 - Normal.

Navigate to section History and switch to table view, Code A9 is expected in Usage Decision column for skipped inspections.

#### Analyze Quality Level History (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you analyze the history of quality level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Level History - Skip Rate in Last 180 Days (F2915). | The current skip rate is displayed in the title of the app.You can change the data displayed on the x-axis by the button Drill Up or Drill Down and check the Lots / Characteristics Skipped and Lots / Characteristics not Skipped for different parameters.Choose one bar in the column chart and switch to List: Inspection Lots and Characteristics to display the list of inspection lots. From the list, select an inspection lot and choose Open In - Manage Inspection Lots to navigate to this inspection lot. Also, you can switch to Inspection Stages by Insp. Lots/Char and Inspection Severities by Insp. Lots/Char. |  |

### Quality Inspection Process with Sampling Scheme and Dynamic Modification

Purpose

Dynamic Modification controls the inspection scope for a series of inspection lots.

The Dynamic Modification Rule defines the number of inspections and skip stages, and the rules that control such quality level changes, for example after three subsequent passed inspections a change to a less severe quality level for the next quality check is proposed and after one failed inspection a change to a more severe quality level for the next quality check is proposed.

The Sampling Procedure determines the sample size. In the chapter for regular quality inspections there is an example of 10% of the lot size as determination rule for samples size. Here we use a sampling scheme with a stepwise approach to determine the sample size.

Prerequisites

Before you test this process, you must have completed the additional configuration in Create Sampling Scheme (optional) chapter in Create Quality Inspection Plan - MDS (BNQ) to create the sampling scheme QM2. And you have to change the sampling type of sampling procedure YSCHMIN1/ YSCHMIN2 to use sampling scheme and assign sample scheme QM2.

However, you cannot change existing sampling procedures if they are already used in plans, as the assignment of sampling scheme is no longer possible. For existing sampling procedures, you need to create new sampling procedures, for example ZSCHMIN1 and ZSCHMIN2 following the additional steps in the Procedure section below. Then replace the old ones with the new ones in your inspection plan using the App Change Inspection Plan (QP02).

Tightened Quality Level

| Lot Size up to | Sample Size |
| --- | --- |
| 10 | 2 |
| 100 | 10 |
| 1000 | 25 |

Normal Quality Level

| Lot Size up to | Sample Size |
| --- | --- |
| 10 | 1 |
| 100 | 5 |
| 1000 | 10 |

Reduced Quality Level

| Lot Size up to | Sample Size |
| --- | --- |
| 10 | 1 |
| 100 | 2 |
| 1000 | 5 |

In this process, the material QM004 is purchased.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Create Sampling Procedure (QDV1). |  |  |
| 3 | Create sampling procedure ZSCHMIN1 | Enter data for the sample procedure, for example, ZSCHMIN1Provide a description, for example "Sampling scheme, char. Attrib. code", and make the following entries:Sampling type: Use Sampling SchemeValuation mode: Valuation according to char.attrib.codeInspection points: choose Without Inspection PointsChoose Continue, and make the following entries:Sampling Scheme: QM2Special Indicators: Leave the No Stage Change field blankChoose Additional Data, and make the following entry:Inspection Severity: 004Choose Continue and Save, and confirm the question Add the sampling procedure to the allowed relationships? with YES.The Allowed Relationships: Sampling Procedures/Dynamic Mod. Rule screen displays. Make a new entry with:Procedure: ZSCHMIN1DynModRule: QM2Choose Save. | Sampling procedure is created. | If no sampling scheme is available, check the chapter Create Sampling Scheme (optional) of the test script BNQ for further instruction. |
| 4 | Create sampling Procedure ZSCHMIN2 | Enter data for the sample procedure: for example, ZSCHMIN2Provide a description, for example "Sampling scheme, mean value", and make the following entries:Sampling type: Use Sampling SchemeValuation mode: Mean value within tolerance rangeInspection points: choose Without Inspection PointsThen follow the same instructions described in the previous step. | Sampling procedure is created. |  |
| 5 | Change Inspection Plan | Open Change Inspection Plan (QP02). |  |  |
| 6 | Enter Selection Fields | Make the following entries and choose Continue.Material: QM004Plant: 3310 |  |  |
| 7 | Select Entry Instruction | On the Entry Option: Group screen, select the row with Inspection Plan for Procurement and then click Choose. | If there is only one inspection plan for material/plant combination available, this screen is skipped and the user must continue with step 5. |  |
| 8 | Go to Inspection Characteristics Overview Screen | Select the operation 0010 and choose either Inspection Characteristics or More > Inspection Characteristics . | The Change Inspection Plan: Characteristic Overview screen displays. |  |
| 9 | Replace Sampling Procedures | There are two Master Inspection Characteristics:One is Qualitative – SurfaceAnother is Quantitative – LengthReplace the sampling procedure YSCHMIN1 with ZSCHMIN1 and YSCHMIN2 with ZSCHMIN2. |  |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Purchaser . | The Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order Creation | Choose Create. | The New Purchase Order screen displays. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data.General Information:Supplier: 33300006Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002Currency: AEDAdd an item, click on it, and then the New Purchase Order Item screen displays. Make the following entries:Tab - General InformationProduct: QM004Plant: 3310Order Quantity: 500Tab – Schedule LinesDelivery date: a date in the futureTab – Delivery DetailsStorage Location: 331AChoose Apply. | Supplier 33300006 also supports the process BMK – Return to Supplier; supplier 33300001 only supports to return to supplier without delivery.Back to the Purchase Order screen. |  |
| 5 | Save Purchase Order | Choose the Order button to save the Purchase Order. | A new Purchase Order is created. The system displays the message Purchase Order has been saved. |  |

#### Display Inspection Plan and Derive the Sampling Scheme (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the inspection plan is related the trading goods. The inspection plan defines sampling scheme used later in the quality inspection.

Dynamic Modification controls the inspection scope for a series of inspection lots.

If the quality of a supply relationship is consistently high, you may want to waive the goods receipt inspection. The reduction of the inspection scope may lead to a skip lot which results in an immediate posting to unrestricted use stock without intervention. If you do not want to waive the goods receipt inspection completely, you can reduce the scope of the inspection as far as the quality level allows.

The Dynamic Modification Rule defines the number of inspections and skip stages, and the rules control such quality level changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03) (without a sub title). | The Display Inspection Plan: Initial screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: QM004Plant: 3310 |  |  |
| 4 | Select Entry Instruction | In the Entry Option: Group screen, select the row with Inspection Plan for Procurement and then click Choose. | If there is only one inspection plan for material/plant combination available, this screen is skipped and the user must continue with step 5. |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the operation 0010 and choose either Inspection Characteristics or More > Inspection Characteristics . | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There are two Master Inspection Characteristics:One is Qualitative – SurfaceOne is Quantitative – Length | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedure can be reviewed in the inspection plan with the quality planner role. |  |
| 7 | Access the App | Open Display Sampling Scheme (QDP3). |  |  |
| 8 | Enter Selection Fields | Sampling scheme: For example, QM2.Choose Continue twice. | Before this, a sampling scheme needs to be created in advance. For more detailed steps, refer to the chapter 4.7 Create Sampling Scheme (Optional) of the test script Create Quality Inspection Plan - MDS (BNQ). |  |
| 9 | Display Normal inspection severity | Select inspection Severity: for example, 4 Normal inspection.Choose Choose.Review the sampling size related to the lot size , especially lot size 10 and lot size 100 and related sample sizes 1 and 5.Go back to the screen Display Sampling Scheme: Header Data. |  |  |
| 10 | Display Tightened inspection severity | Choose Continue.Select inspection Severity: for example, 6 .Choose Choose.Review the sampling size related to the lot size, especially lot size 10 and lot size 100 and related sample sizes 2 and 10. |  |  |

#### Post Goods Receipt for Purchase Order – 1st iteration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted. For Lot size 10 sample size is 1 as described above when displaying the sample scheme.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Open Post Goods Receipt for Purchase Order | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search Purchase Order | Enter Purchase Order. | The system displays the data for the goods receipt. If the Storage Location was not specified in the Purchase Order, it needs to be maintained now (e.g. 331A). |  |
| 4 | Enter Goods Receipt Quantity | Enter 10 in the Delivered field. | 10 pieces of QM004 are posted. |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. | The Post button is activated. |  |
| 6 | Post | Choose the Post button. | The Post Goods Receipt screen displays. The system displays the message Material document xxx posted. |  |

#### Display Quality Level – 1st iteration

Purpose

In this step, follow the standard process variant as described in chapter [Display Quality Level (optional)](#unique_28) [page ] 37 with material QM004 to check the quality level.

Expected quality level 030 Normal (if starting with the process).

|  |
| --- |
| Note The inspection level depends on the usage decisions of the previous inspection lots. Therefore, if previous quality inspections were executed, the displayed quality level might differ. You can change the quality level of the next inspection in apps Change Quality Level or Manage Quality Levels. |

#### Quality Inspection – 1st iteration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician records the inspection result for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Material Document: From previous step | If Material Document is not displayed in the Filters, please choose Adapt Filters. In the dialog box Adapt Filters, find Procurement and choose More Filters. Select Material Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Choose Record Results | Choose Edit on the upper right. | The app switches to the edit mode. |  |
| 6 | Enter Inspection Result | Depending on the inspection result, enter the positive results:Surface: Code Group - Code SURFACE 0020 (Smooth)Length: Mean Value (CM): 160 |  |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for procurement goods has been performed and result recorded. |  |
| 8 | Log Off as Quality Technician |  |  |  |
| 9 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 10 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 11 | Enter Filter Fields | Make the following entries and choose Go.Material Document: From previous step | If Material Document is not displayed in the Filters, please choose Adapt Filters. In the dialog box Adapt Filters, find Inventory Management and choose More Filters. Select Material Document and choose OK. Choose Go. |  |
| 12 | Select Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Order equals to the purchase order: XXXX (from previous step). | If Material Document is not part of list you can add it by choosing Settings button on the right top, add Purchase Order in Columns. |  |
| 13 | Enter UD code | Depending on the inspection result, confirm with UD code: A1 (Accepted – unrestricted stock) |  |  |
| 14 | Save Usage Decision | Choose Save. |  |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for multiple inspection lots at the same time (mass processing), execute the process flow described in chapter Record Inspection Results of the Regular Quality Inspection Process.

#### Display Quality Level

Purpose

In this step, follow the standard process variant as described in chapter [Display Quality Level (optional)](#unique_28) [page ] 37 with material QM004 to check the quality level.

Expected quality level is 030 - Normal.

#### Post Goods Receipt for Purchase Order – 2nd iteration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search Purchase Order | Enter Purchase Order. | The system displays the data for the goods receipt. If the Storage Location was not specified in the Purchase Order, it needs to be maintained now (e.g. 331A). |  |
| 4 | Enter Goods Receipt Quantity | Choose the Quantity tab in detailed data. Enter 100 in Qty in Unit of Entry. | 100 pieces of QM004 are posted. |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. | The Post button is activated. |  |
| 6 | Post | Choose the Post button. | The Post Goods Receipt screen displays. The system displays the messageMaterial document xxx posted. |  |

#### Quality Inspection – 2nd iteration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician records the inspection result for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Material Document: From previous step | If Material Document is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, find Procurement and choose More Filters. Select Material Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Choose Record Results | Choose Edit on the upper right. | The app switches to the edit mode. |  |
| 6 | Enter Inspection Result | Depending on the inspection result, enter the negative results:Surface: Code Group - Code SURFACE 0010 (Rough)Length: Mean Value (CM): 90 |  |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for procurement goods has been performed and result recorded. |  |
| 8 | Log Off as Quality Technician |  |  |  |
| 9 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 10 | Access the App | Open Manage Usage Decisions. | The Manage Usage Decisions screen displays. |  |
| 11 | Enter Filter Fields | Make the following entries and choose Go.Material Document: From previous step | If Material Document is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, find Inventory Management and choose More Filters. Select Material Document and choose OK. Choose Go. |  |
| 12 | Select Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Order equals to the purchase order: XXXX (from previous step). | The Inspection Lot screen displays.If Purchase Document is not part of list you can add it by choosing Settings button on the right top, add Purchase Order in Columns. |  |
| 13 | Enter UD Code | Depending on the inspection result, confirm with UD code: R1 (Rejected-blocked stock). |  |  |
| 14 | Save Usage Decision | Choose Save. |  |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for multiple inspection lots at the same time (mass processing), execute the process flow described in chapter Record Inspection Results of the Regular Quality Inspection Process.

#### Display Quality Level – 2nd iteration

Purpose

In this step, follow the standard process variant as described in chapter [Display Quality Level (optional)](#unique_28) [page ] 37 with material QM004 to check the quality level.

Expected quality level is 040 - Tightened.

#### Post Goods Receipt for Purchase Order – 3rd iteration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Open Post Goods Receipt for Purchase Order | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search Purchase Order | Enter Purchase Order. | The system displays the data for the goods receipt. If the Storage Location was not specified in the Purchase Order, it needs to be maintained now (for example, 331A). |  |
| 4 | Enter Goods Receipt Quantity | Choose Quantity tab in detailed data.Enter 100 in Qty in Unit of Entry. | 100 pieces of QM004 are posted. |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The Post Goods Receipt screen displays. The system displays the message Material document xxx posted. |  |

#### Quality Inspection – 3rd iteration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician records the inspection results.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go.Material Document: From previous step | If Material Document is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, find Procurement and choose More Filters. Select Material Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Choose Record Results | Choose Edit on the upper right. | The app switches to edit mode. |  |
| 6 | Enter Inspection Result | Depending on the inspection result, enter the positive results:Surface: Code Group - Code SURFACE 0020 (Smooth)Length: Mean Value (CM): 120 |  |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for procurement goods has been performed and result recorded. |  |
| 8 | Log off as Quality Technician |  |  |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for multiple inspection lots at the same time (mass processing), execute the process flow described in chapter Record Inspection Results of the Regular Quality Inspection Process.

#### Analyze Quality Level History (optional)

Please refer to chapter [Analyze Quality Level History (optional)](#unique_33) [page ] 42 to analyze the quality level history.

### Quality Inspection Process with Material-Supplier Release

Purpose

In this variant of the regular quality inspection process using a quality info record, the material QM002 is purchased in a larger quantity than released in the quality info record.

#### Check Overview Page for Quality Engineer (optional)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360) . | The Quality Engineer Overview screen displays. |  |
| 3 | Access the Card | Access the card Q-Info Records with Exceptions. | The card displays quality info records with expired release date or with release date that is about to expire in the near future.If you want to review more details, choose one bar to display the respective entries in Manage Quality Info Records (F2256A) app. |  |

#### Review or Change Quality Info Record (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Quality info record has been set up to influence purchasing functions (for example, limit maximum order quantity or block order due to quality reasons). If a quality inspection is not required for a specific material-supplier combination, you can disable the creation of an inspection lot by setting the indicator No Inspection Lot Created. As this inspection setting is more specific than the setting of the material master, quality inspection is bypassed for this material-supplier combination even if quality inspection has been set up in the material master for the respective material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Quality Info Records (F2256A). | The Manage Quality Info Records screen displays. |  |
| 3 | Enter Search Fields | Make the following entries and choose Go.Plant: 3310Material: QM002Supplier: 33300006 |  |  |
| 4 | Select Quality Info Record | In the results table, open the respective quality info record with a click.In the Release section, review Release Quantity field. | Quality info record is opened in display mode.Release quantity should be 15. | If the release quantity is already ordered, the ordered quantity is displayed. Otherwise the ordered quantity is not displayed in display mode. The quantity to be purchased in the next step needs to be higher than release quantity. |
| 5 | Change quality info record (Optional) | Choose Edit to switch to edit mode.Change release quantity and/or block function and block reason.Choose Save. | Quality info record was changed.Note The following process might not work as described if you change the quality info record. |  |

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, if you create a purchase order with a quantity too high, the purchase order will fail.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori Launchpad as a Purchaser. | The Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. | The New Purchase Order screen displays. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data.General Information:Supplier: 33300006Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002Currency: AEDAdd an item, click on it, and the New Purchase Order Item screen displays. Make the following entries:Tab - General InformationMaterial: QM002Plant: 3310Order Quantity: 30Tab – Schedule LinesDelivery date: a date in the futureTab – Delivery DetailsStorage Location: 331AChoose Apply. | Supplier 33300006 also supports the process BMK – Return to Supplier with delivery; supplier 33300006 only supports to return to supplier without delivery.Back to the Purchase Order screen. |  |
| 5 | Check Purchase Order | Choose the Order button. | An error message appears. Purchase Order is not created because of the settings in the quality info record. |  |

### Quality Inspection Process with Quality Certificate in Procurement

Purpose

In this section, the material QM005 is purchased. The material master of this material is set up so that a quality certificate must be provided by the supplier. The certificate can either be provided together with the shipment or separately. To ensure that the quality certificate is received and the receipt is captured correctly in the system, the user cannot make a usage decision until respective data is entered in the certificate record. However, recording of inspection results is possible without the receipt of the quality certificate.

From SAP S/4HANA Cloud Public Edition 2508, you can automatically process incoming quality certificate documents by using AI-assisted processing with SAP Document AI. For more information, refer to the following documents:

- [Integration of SAP Document AI](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d1e58be39d884a0dbf75a7526a9acbf4/c663da41ff1d4c949b299ea0e70a4aee.html)
- Set-Up Instructions for 7TC - Integration with SAP Document AI ()
- Pricing information in SAP Discovery Center: [https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/](https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/)

#### Review Quality Settings in Material Master (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Material (MM03). | The Display Material (Initial Screen) displays. |  |
| 3 | Enter Material | Enter QM005 in the field Material and choose Continue. | The Select View(s) pop-up is displayed. |  |
| 4 | Open Quality Management View | Select Quality Management view. Choose Org.Levels and enter 3310 for Plant. Choose Continue or press Enter. | The Display Material QM005 (Trading Goods) screen displays. |  |
| 5 | Review Quality Management in Procurement Settings | The following value for QM Control Key and Certificate type, respectively, is assigned:QM Control Key: 0009Certificate Type: QM01 | Note By assigning control key 0009 to the material, a certificate must be submitted with the delivered goods. |  |

#### Create Purchase Order

Procedure

Execute step Create Purchase Order of the Regular Quality Inspection Process with material QM005.

#### Post Goods Receipt for Purchase Order

Procedure

Execute step Post Goods Receipt for Purchase Order of the Regular Quality Inspection Process with the purchase order created in the previous test step.

#### Review Inspection Lot Status Before Receipt of Quality Certificate (Optional)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343) . | The Manage Inspection Lots screen displays. |  |
| 3 | Open Inspection Lot | Search for inspection lot for this purchase order and open inspection lot details. |  |  |
| 4 | Review Inspection Lot Status | Review the status on header level. | Inspection lot should have (at least) the system status CTCM Certif.confirmation missing. |  |

#### Enter Receipt of Quality Certificate

##### Alternative 1: Enter Receipt of Quality Certificate Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can manually update a quality certificate of a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Certificate Receipts (F3233) . | The Manage Certificate Receipts screen displays. |  |
| 3 | Open Certificate Record | Search for certificate record for this purchase order and open certificate record details by choosing the respective line item:Purchasing Document: Purchase Order ID | The certificate object details page is displayed. |  |
| 4 | Set Status | Set status to Received using the action in the upper right corner. | The Certificate Status is Received.Note The Quality Engineer cannot make a usage decision unless the Certificate Status is set to Received. |  |

##### Alternative 2: Enter Receipt of Quality Certificate with SAP Document AI

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload certificates through AI-assisted processing of incoming quality certificates with SAP Document AI. This feature utilizes advanced technology and offers a fully automated process, reducing the need for manual input and minimizing human error.

|  |
| --- |
| Note The pricing-relevant Scope Item Integration with SAP Document AI (7TC) needs to be activated before using this functionality. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Certificate Receipts (F3233) . | The Manage Certificate Receipts screen displays. |  |
| 3 | Upload Quality Certificate Documents | If SAP Document AI is integrated, choose Start Certificate Upload and navigate to the app Upload Quality Certificate Documents - SAP Document AI (F8858) to upload quality certificates. | If the system identifies a matching certificate receipt expecting a certificate, it attaches the certificate document to the receipt.If no matching certificate receipt exists, the system creates a new one.If the system can't clearly identify or update the certificate receipt, you can review the extracted data and manually complete the matching process in the new app Review Certificate Document Matches (F8537). |  |
| 4 | Review Status | If the system identifies a matching certificate receipt expecting a certificate, it attaches the certificate document to the receipt and sets the Certificate Status to Received. | The Certificate Status is Received.The Automation Level is set accordingly. |  |

#### Review Inspection Lot Status After Receipt of Quality Certificate (Optional)

Procedure

Execute step [Review Inspection Lot Status Before Receipt of Quality Certificate (Optional)](#unique_50) [page ] 62 of this chapter.

The inspection lot system status should now contain the entry Certificate receipt confirmed (CROK).

#### Quality Inspection

Procedure

Execute the steps described in chapter of the [Regular Quality Inspection Process](#unique_56) [page ] 19 with positive inspection results and a positive usage decision.

## Appendix

### Process Integration

The process to been tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Business Condition | Comment |
| --- | --- |
| BMK - Return to Supplier | Continue with the Return to Supplier (BMK)with respect to the Return Reason ‘Quality Issue’Make sure that in the purchase order, the item is flagged for returns and Stock Type is Blocked stock on Delivery tab. |
| BMC - Core Inventory Management | Continue stock handling for the blocked stock. |
| J45 - Procurement of Direct Materials | Continue purchase process e.g. to create supplier invoice in case with or without reduction. |
| J45 - Procurement of Direct Materials | Continue with Purchasing Analytics.In the section Purchasing Analytics using Tile Supplier Evaluation by Quality. |
| BF5 - Create Quality Info Record - MDS | Complete all steps in the master data script to run the test procedure Quality Inspection Process with Material-supplier Release |

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
> Flagged while digesting this document, not verified: Supplier return support is stated inconsistently: some PO steps say 33300006 supports return with delivery while 33300001 only without delivery; the Create Second Purchase Order step says 33300006 supports with delivery and 33300006 only without delivery.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Storage location for goods receipt/quality stock is 331A in master data and most steps, but the stock-before-GR step and one GR step reference 331C, which is not listed in master data.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-quality-management-in-sales-1mp-ae-sap-s-4hana-cloud-publi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1FM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 114,381 chars in the whole document
