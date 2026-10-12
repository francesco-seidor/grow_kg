---
id: 12-production-and-manufacturing/test-script-make-to-order-production-with-variant-configuration-1yt-ae
title: "Test Script: Make-to-Order Production with Variant Configuration (1YT_AE) - SAP S/4HANA Cloud Public Edition (1YT_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 (AE) test script for scope item 1YT_AE: make-to-order production of configurable fork lifters, from quotation to billing."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/variant-configured-production]
aliases: [1YT_S4CLD2608_BPD_EN_AE]
keywords: [Production of Variant-Configured Products, make-to-order production, variant configuration, test scripts, sales order creation, sales quotation, multilevel configurable material, production order processing, down payment, billing plan]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YT_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-789
topic: 12-production-and-manufacturing/variant-configured-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Order Production with Variant Configuration (1YT_AE) - SAP S/4HANA Cloud Public Edition (1YT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Production of Variant-Configured Products** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Order Production with Variant Configuration (1YT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848516)

[2 Prerequisites 4](#_Toc232848517)

[2.1 System Access 4](#_Toc232848518)

[2.2 Roles 4](#_Toc232848519)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232848520)

[2.4 Business Conditions 8](#_Toc232848521)

[2.5 Preliminary Steps 9](#_Toc232848522)

[2.5.1 Initial Stock Posting for the Material in BOM of CM-FL-V00 9](#_Toc232848523)

[2.5.2 Assign Dependency to Operation and Sequence in Routing 10](#_Toc232848524)

[2.5.3 Create Production Version for CM-FL-V01 (Optional) 11](#_Toc232848525)

[2.5.4 Disable Production Version 13](#_Toc232848526)

[2.5.5 Create Master Data for Fast Data Entry 13](#_Toc232848527)

[2.5.5.1 Create Application Group 13](#_Toc232848528)

[2.5.5.2 Create Characteristic Display 14](#_Toc232848529)

[2.5.6 Create Customer-Material Info Record 15](#_Toc232848530)

[2.5.6.1 Create Class in Class Type 052 for Classification 16](#_Toc232848531)

[2.5.6.2 Create Customer-Material Info Record 16](#_Toc232848532)

[3 Overview Table 18](#_Toc232848533)

[4 Test Procedures 19](#_Toc232848534)

[4.1 Make to Order Production with Single Level Configurable Material 19](#_Toc232848535)

[4.1.1 Create Sales Quotation for Configurable Material (Optional) 19](#_Toc232848536)

[4.1.2 Create Sales Order with Reference to Sales Quotation (Optional) 23](#_Toc232848537)

[4.1.3 Create Sales Order with Configurable Material 25](#_Toc232848538)

[4.1.4 Create Down Payment Request 31](#_Toc232848539)

[4.1.5 Post Down Payment 31](#_Toc232848540)

[4.1.6 Manufacturing Steps Production Order Processing 32](#_Toc232848541)

[4.1.7 Delivery and Billing Processing 34](#_Toc232848542)

[4.2 Make to Order Production with Multilevel Configurable Material 36](#_Toc232848543)

[4.2.1 Create Sales Order with Configurable Material 36](#_Toc232848544)

[4.2.2 Create Down Payment Request 40](#_Toc232848545)

[4.2.3 Post Down Payment 41](#_Toc232848546)

[4.2.4 Manufacturing Steps Production Order Processing 41](#_Toc232848547)

[4.2.5 Delivery and Billing Processing 43](#_Toc232848548)

[5 Appendix 46](#_Toc232848549)

[5.1 Succeeding Processes 46](#_Toc232848550)

[5.2 Relevant Processes 46](#_Toc232848551)

## Purpose

Overview

This scope item shows a Make-to-Order Production scenario using the Advanced Variant Configuration for an efficient state-of-the-art configuration of a material ordered by a customer, covering single-level and multi-level configurable materials. The configurable material is defined as a bill of material. In this process, a sales order (optionally based on a sales quotation) is created with an individual configuration for a fork lifter. This is captured by defining the different component characteristics desired by the customers and considering the constraints and dependencies of the components. The sales price calculation is then based on the individually chosen characteristics of the components. The sales order is considered for production planning when doing the Materials Requirements Planning (MRP). The production execution for the individual fork lifter takes place before delivering it to the customer. The process finishes with the billing to the customer.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

Manufacturing / Trading

Production Plant

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | CM-MLFL-KM-VXX | Multilevel Forklifter | This is a multilevel configurable material. One of its component is also a configurable material. |
| Material | CM-FL-V00 | Configurable Forklifter | Alternatively, you can also use material CM-FL-V01. In this case, firstly check if you have executed all steps described in scope item 22T (Set Up Configurable Model Using Variant Configuration). |
| Material | SF-FL-COMB | FORKLIFTER BASE MODEL COMBUSTION | Initial stock posting required |
| Material | SF-FL-ELECTRIC | FORKLIFTER BASE MODEL ELECTRICAL | Initial stock posting required |
| Material | SF-FL-CWEIGHT | COUNTERWEIGHT 1000KG | Initial stock posting required |
| Material | SF-FL-FORK-S | FORK (1.200 MM) | Initial stock posting required |
| Material | SF-FL-FORK-M | FORK (1.800 MM) | Initial stock posting required |
| Material | SF-FL-FORK-L | FORK (2.400 MM) | Initial stock posting required |
| Material | SF-FL-TIRE-CUSH | CUSHION TIRE ASSEMBLY | Initial stock posting required |
| Material | SF-FL-FORKSEAT-VXX | Seat Type of Fork lifter(HALB) | The material is configurable and external procured. |
| Material | SF-FL-TIRE-PNEU | PNEUMATIC TIRE ASSEMBLY | Initial stock posting required |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| CM-MLFL-KM-VXX | 0 | KMAT | PC | Configurable Forklifter |  |
| SF-FL-COMB | 1 | HALB | PC | FORKLIFTER BASE MODEL COMBUSTION |  |
| SF-FL-ELECTRIC | 1 | HALB | PC | FORKLIFTER BASE MODEL ELECTRICAL |  |
| SF-FL-CWEIGHT | 1 | HALB | KG | COUNTERWEIGHT 1000KG |  |
| SF-FL-FORK-S | 1 | HALB | PC | FORK (1.200 MM) |  |
| SF-FL-FORK-M | 1 | HALB | PC | FORK (1.800 MM) |  |
| SF-FL-FORK-L | 1 | HALB | PC | FORK (2.400 MM) |  |
| SF-FL-TIRE-CUSH | 1 | HALB | PC | CUSHION TIRE ASSEMBLY |  |
| SF-FL-TIRE-PNEU | 1 | HALB | PC | PNEUMATIC TIRE ASSEMBLY |  |
| SF-FL-FORKSEAT-VXX | 1 | HALB | PC | Seat Type of Fork lifter(HALB) |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

This is a super BOM list for configurable materials. Not all components necessarily used in production order.

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| CM-FL-V00 | 0 | KMAT | PC | Configurable Forklifter |  |
| SF-FL-COMB | 1 | HALB | PC | FORKLIFTER BASE MODEL COMBUSTION |  |
| SF-FL-ELECTRIC | 1 | HALB | PC | FORKLIFTER BASE MODEL ELECTRICAL |  |
| SF-FL-CWEIGHT | 1 | HALB | KG | COUNTERWEIGHT 1000KG |  |
| SF-FL-FORK-S | 1 | HALB | PC | FORK (1.200 MM) |  |
| SF-FL-FORK-M | 1 | HALB | PC | FORK (1.800 MM) |  |
| SF-FL-FORK-L | 1 | HALB | PC | FORK (2.400 MM) |  |
| SF-FL-TIRE-CUSH | 1 | HALB | PC | CUSHION TIRE ASSEMBLY |  |
| SF-FL-TIRE-PNEU | 1 | HALB | PC | PNEUMATIC TIRE ASSEMBLY |  |

Sales Center

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Sales Organization | 3310 | Dom. Sales Org | National |
| Distribution Channel | 10 | Direct Sales | Direct Sales |
| Customer | 33100001 | Domestic UAE Customer 1 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 2NI | Create Application Group and Characteristic Display - MDS |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| 22T - Set Up Configurable Model Using Variant Configuration (Optional) | If you are going to execute 1YT with Set Up Configurable Model Using Variant Configuration Sample Master Data, you must have completed the preliminary step in 1YT for CM-FL-V01 material to enable the material for production and sales and distribution process. |

### Preliminary Steps

#### Initial Stock Posting for the Material in BOM of CM-FL-V00

Purpose

In a real business case, the materials are usually purchased from external vendors; in that case, that process is covered by the standard purchasing or subcontracting processes. This process step shows you how to post initial stock directly to the storage locations. Note that you only need to post initial stock in case there is none available or the current stock is insufficient. Ensure that at least as many components for the configurable material, for example, forklifter, are available as you intend to sell in the later step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and press Enter:Material: <All material listed of the BoM for CM-FL-V00 in Master Data Section>. Except for CM-FL-V00Plant:3310 |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331BUnrestricted - Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <Enter a number> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

#### Assign Dependency to Operation and Sequence in Routing

Purpose

This process step shows you of configurable routing, for which dependencies must be assigned to operations and sequence, so routing is variable according to configuration for the material.

This step has to be executed only once.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). | The Change Routing (CA02) screen displays. |  |
| 3 | Enter the Plant and the Material Name | On the Change Routing (CA02) screen, make the following entries and choose Continue:Material: CM-MLFL-KM-VXXPlant:3310 | The Change Routing: Initial Screen displays. |  |
| 4 | Create Parallel Sequence 1 | Choose menu Sequences, and choose New entry. On the dialog screen, choose Parallel Sequence and choose Continue.Enter the following value:Sequence: 1Description: Parallel Seq for ElecBranch Operation: 0010Return Operation: 0010Choose Operations, and enter the following value:Operation: 0011Work center: ASSEMBLEControl Key: YBP1Description: Preparation of electrical engine | If sequence 1 is already created, please skip this step. |  |
| 5 | Assign Dependency to Sequence | Choose menu Sequences, mark Sequence 1 and choose from menu path More > Extras > Object dependencies > Assignments .Enter the following dependency.Dep.: AVC_OD_ELECONLY_VXXChoose Back. | Dependency is assigned to sequence. |  |
| 6 | Assign Dependency to Operation | Choose sequence 0, and choose Operations from menu bar. Mark operation 0010, and choose from menu path More > Extras > Object dependencies > Assignments , enter the following dependency.Dep.: AVC_OD_CALCCLABOR_VXXChoose Back.Repeat for operation 0031 and 0032 with following dependencies.For 0031, assign AVC_OD_COMBONLY_VXXFor 0032, assign AVC_OD_ELECONLY_VXX | Dependency is assigned to operation. |  |
| 7 | Save Routing | Choose Save. | Routing is saved. |  |

#### Create Production Version for CM-FL-V01 (Optional)

Purpose

This process step shows you how to test this scope item with material CM-FL-V01, and you must execute this step. A production version determines which alternative BoM is used with a routing to produce a material. In this process step, you create a production version for a configurable material.

This step has to be executed only once for material CM-FL-V01.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | The Prodution Version: Mass Processing screen displays. |  |
| 3 | Enter the Plant and the Material Name | On the Prodution Version: Mass Processing screen, make the following entries and choose Continue:Plant:3310Material: CM-FL-V01 | The Production versions not found; check your selection criteria message displays. |  |
| 4 | Create a Production Version | Choose the Create Production Version icon. | The Maintain Production Version: Detail Screen dialog box displays. |  |
| 5 | Enter the Production Version Details | In the Production Version section, make the following entries:Material: CM-FL-V01Product Version: 0002Short Text for Production Version: Forklift ConfigurableMinimum Lot Size: 1Maximum Lot Size: 99,999,999Valid from: Enter the current dateValid to: 12/31/9999 |  |  |
| 6 | Enter the Task List Details | In the Task List section, enter the following data:Task List Type: N RoutingGroup: 43310039Group Counter: 1 | The values in the Task List Type, Group, and Group Counter fields are populated. |  |
| 7 | Enter the Bill of Material Details | In the Bill of Material section, in the Alternative BOM field, use the value help and proceed as follows:In the Alternative BOM (1) dialog box, select one item in the list.Choose OK (Copy). | The values in the Alternative BOM and BOM Usage fields are populated. |  |
| 8 | Check the Production Version | In the Maintain Production Version: Detail Screen dialog box, choose Check. | The Consistency Check of Production Versions log displays in the Maintain Production Version: Detail Screen dialog box. |  |
| 9 | Check and Close the Consistency Check Log | Verify the following in the consistency check log of production versions:Task list existsBOM existsNo error messages exist.Choose the Cancel (Escape) icon. | The consistency check log closes. |  |
| 10 | Save the Production Version Details | In the Maintain Production Version: Detail Screen dialog box, choose Save Changes and Close Screen. | The Maintain Production Version: Detail Screen dialog box closes. |  |

#### Disable Production Version

Purpose

This process step shows you how to invalidate the old production version in case multiple production version exists for sample material (CM-FL-V00, CM-FL-V01).

This step has to be executed only once.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | The Prodution Version: Mass Processing screen displays. |  |
| 3 | Enter the Plant and the Material Name | On the Prodution Version: Mass Processing screen, make the following entries and choose Continue:Plant:3310Material: CM-FL-V00, CM-FL-V01 | The Production versions not found; check your selection criteria screen displays. |  |
| 4 | Invalid a Production Version | For the production version 0001, change the Valid to date to yesterday. | Old production version 0001 is invalid. |  |
| 5 | Save the Production Version Details | On the Maintain Production Version: Detail Screen dialog box, choose Save Changes and Close Screen. | The Maintain Production Version: Detail Screen dialog box closes. |  |

#### Create Master Data for Fast Data Entry

To enable fast data entry in sales order, application group and characteristic display need to be created.

##### Create Application Group

Purpose

This process step shows you how to create application group SD and PP.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Char. Display for Configuration (CU_CHAR_DISPLAY). | The Change View "Application Group": Overview screen displays. |  |
| 3 | Enter Application Group | On the Change View "Application Group": Overview screen, choose New Entries. Then make the following entries:Transact. : <SD Sales and Distribution Document>Appl Grp: SDTransact.: <PP Production Order>Appl Grp: PP | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Save Data | Choose Save. |  |  |

##### Create Characteristic Display

Purpose

This process step shows you how to create characteristic display, and assign characteristic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Char. Display for Configuration (CU_CHAR_DISPLAY). | The Change View "Application Group": Overview screen displays. |  |
| 3 | Enter Application Group | On the Change View "Application Group": Overview screen, double-click Charactersitic Display.Choose New Entries. Make the following entries and choose Enter.Char. Display: PROD_FKDescription: Product Fork LifterAppl. Grp: SD | The Change View "Characteristic Display": Overview screen displays. |  |
| 4 | Assign Characteristic | Choose the characteristic display created in step 3 and double-click Characteristic Assignment.Choose New Entries, and make the following entries.Sequence Characteristic:5 AVC_CR_LIFTERMODEL_VXX10 AVC_CR_POWERSOURCE_VXX20 AVC_CR_WHEELTYPE_VXX30 AVC_CR_COUNTERWEIGHT_VXX40 AVC_CR_FORKSIZE_VXX50 AVC_CR_BCAPACITY_V00Go back to Change View "Application Group": Overview screen, repeat step 3 and 4 with following value:Char. Display: PP_FKDescription: Product Fork LifterAppl.: Grp: PPSequence Characteristic:5 AVC_CR_LIFTERMODEL_VXX10 AVC_CR_POWERSOURCE_VXX20 AVC_CR_WHEELTYPE_VXX30 AVC_CR_COUNTERWEIGHT_VXX40 AVC_CR_FORKSIZE_VXX50 AVC_CR_BCAPACITY_V00 | The Change View "Characteristic Assignment": Overview screen displays. |  |
| 5 | Save Data | Choose Save. |  |  |

#### Create Customer-Material Info Record

You can create customer-material info record for a configurable material. In the info record, you can maintain classification for customer-material combination.

##### Create Class in Class Type 052 for Classification

Purpose

This process step shows you how to create class in class type 052.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Classes (CL02). | The Class screen displays. |  |
| 3 | Enter Class Name | Make the following entries, and choose Create.Class:AVC_CL_COM_CLA_V00Class Type: 052Note If the class AVC_CL_COM_CLA_V00 already exists, you can skip this step and create customer-material info record directly. | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Enter Basic Data | On the Basic data tab, make the following entries.Description: for example, <Common Char. For customer>Status: Released (Default)Select Do not check radio. (Default) |  |  |
| 5 | Assign Characteristic | On the Char. tab, enter the characteristics to be maintained in the customer-material info record:AVC_CR_FORKSIZE_VXX |  |  |
| 6 | Save Data | Choose Save. | The class is created. |  |

##### Create Customer-Material Info Record

Purpose

This process step shows you how to create customer-material info reocd and maintain classification for configurable material.

You can also refer to Master Data Script in Create Customer-Material Info Record - MDS (2YX) for more details of creating customer-material info record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Materials (F2499). | The Manage Customer Materials screen displays. |  |
| 3 | Create Customer Material Info Record | Choose Create. On the Customer Material screen, make the following entries:Customer: 33100001Material : CM-FL-V00Sales organization: 3310Distribution Channel: 10Note If message Customer material for material CM-FL-V00 already exists display, you can skip creating customer-material info record and start with test procedures. |  |  |
| 4 | Assign Class | On the Classification tab, choose Assign to assign a class.On the popup Select: Classscreen , search for the class AVC_CL_COM_CLA_V00 created in previous step and choose Go.Choose the searched class. |  |  |
| 5 | Maintain Char-acteristic Values | Choose Small for Fork Size. | In later step, when you create sales order for this customer-material combination, Small will default for characteristic Fork Size on the Variant Configuration screen. |  |
| 6 | Save Data | Choose Create. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Quotation for Configurable Material (Optional)](#unique_18) [page ] 19 | Internal Sales Representative | Manage Sales Quotations (F1852) | The Manage Sales Quotations screen displays. |
| [Create Sales Order with Reference to Sales Quotation (Optional)](#unique_19) [page ] 23 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Create Sales Order with Configurable Material](#unique_20) [page ] 25 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Create Down Payment Request](#unique_21) [page ] 31 |  |  |  |
| [Post Down Payment](#unique_22) [page ] 31 |  |  |  |
| [Manufacturing Steps Production Order Processing](#unique_23) [page ] 32 |  |  |  |
| [Delivery and Billing Processing](#unique_24) [page ] 34 |  |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Make to Order Production with Single Level Configurable Material

#### Create Sales Quotation for Configurable Material (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to enter the sales quotation after a customer has requested it.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) screen displays. |  |
| 3 | Navigate to Create Sales Quotation Screen | On the Manage Sales Quotations (F1852) screen, choose Create Quotation. |  |  |
| 4 | Enter Quotation Details | Make the following entries and choose Continue:Quotation Type: QTSales Organization: 3310Distribution Channel: 10Division: 00 | Quotation creation started |  |
| 5 | Enter Quotation Details | Make the following entries:Sold To party: 33100001Ship To party: 33100001Req. Deliv. Date: <Current date + 5 days>Valid to: <enter a date>, for example, one month after today |  |  |
| 6 | Enter Characteristic Value | There are two ways to configure the characteristic value for the material. Execute step 6, the most common way to configure a material.Optionally it is possible to configure a material using a fast entry of characteristics as described in step 7.In the All Items section, enter the following value and press Enter.Material Number: CM-FL-V00Quantity: for example, 1 PCNote If you want to create billing plan for the follow-on sales order, manually enter the following value as well. If not, press Enter.ItCa (Item category): CBAPOn the Variant Configuration screen, select value for characteristics below and choose Done.Lifter Model: <Heavy, Standard>Power Source: <Combustion, Electrical>. Combustion displays as default value.Wheel Type: <Cushion Tires, Pneumatic Tires>Fork Size: <Small, Normal, Large> (If customer-material info record is maintained as described in preliminary step, Small displays as default value.)Counterweight (KG): <1.000, 2.000, 5.000>Battery Capacity(Ah) : <50, 80, 140>Variant condition: AVC_CWEIGHT by defaultNet Value: Varies according to characteristic value chosenThe combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automaticallyWheel Type: Cushion Tires or Pneumatic TiresFork Size: Small or Medium or LargeVariant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeCombination Two:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Variant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeCombination Three:Lifter Model: StandardPower Source: ElectricalWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Battery Capacity(Ah): 50 or 80 or 140 (140 only available when fork size is L)Variant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeOn the Quotation: Availability Control screen, choose Continue. | Variant Configuration screen displays. | If the characteristic value chosen matches a mate-rial variant, please refer to another scope item 21D to handle it. |
| 7 | Fast Entry of Characteristic Value (Alternative) | To use fast entry functionality, make sure you have created master data for fast data entry by executing preliminary step.Choose Configuration tab and choose Product Fork Lifter for Char. Display. Choose Selection, and the characteristics Lifer Model, Power Source, Wheel Type, Fork Size, Counterweight and Battery Capacity then display in the columns of All Items section.Enter the following entries in All Items section.Material Number: CM-FL-V00Quantity: for example, 1 PCNote If you want to create billing plan for this sales order, manually enter the following value as well. If not, press Enter.ItCa (Item category): CBTDPress Enter. Combustion is defaulted for Power Source.Enter value for Lifer Model, Power Source, Wheel Type, Fork Size, Counterweight, and Battery Capacity.Lifter Model: HVY, STDPower Source: COMB, ELECWheel Type: C, PFork Size: S, M, L (If customer-material info record is maintained as described in preliminary step, S displays as default value.)Counterweight (KG): 1.000, 2.000, 5.000Battery Capacity(Ah): 50, 80, 140Press Enter after entering value for each characteristic and value entered is replaced by value description in each field. Allowed combinations of characteristic values are the same as step 6.Note To change value for characteristics, instead of choosing F4 search help button, manually enter the new value in the field directly. |  |  |
| 8 | Check Pricing | Select Quotation item and select Item Conditions icon above the line item. Pricing of variant components displays.Check the condition value of condition type PVA0.CounterweightThe condition value for Counterweight is calculated by the formula below.Condition value = Sales order quantity * Amount (Unit price) * Char. Value for Counterweight/1000For example, if choose Char. Value 5000KG for Counterweight in Step 6, then Condition value = Sales Quotation quantity * Amount * 5000/1000Small ForkIf choose Char. Value S for Fork Size in step 6, then a minus value for SMALLFORK displays.Large ForkIf choose Char. Value L for Fork Size in step 6, then a value for LARGEFORK displays.Choose Back. |  |  |
| 9 | Display Print Preview | On the Create Quotation: Overview screen, choose Header Output Preview button.On the Display Quotation xxx: Output screen, select the line already created for the print output and choose Display Document.Check the variant pricing and configuration details on the displayed PDF document.Variant pricing: Counterweight, Large Fork(optional), Small Fork(optional)Configuration: Fork Size, Counterweight, Wheel Type, Lifer Model, Power Source, Battery Capacity [Ah] (optional).Choose Back. | Choose your local destination and choose Print. |  |
| 10 | Save Document | Choose Save. Make a note of the quotation number: __________. | The quotation is saved. |  |

#### Create Sales Order with Reference to Sales Quotation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a customer order regarding the quotation after the customer accepted the quotation. Finally, the order confirmation is printed and can be sent to the customer.

If a sales order is created with reference to quotation. The next step Create Sales Order with Configurable Material can be skipped.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays.screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders (F1873) screen, choose Create Sales Order - VA01. |  |  |
| 4 | Enter the Order Type and the Sales Organization | Make the following entries and choose Create with Reference:Order Type: OR | The dialogue window Create with Reference displays. |  |
| 5 | Enter Quotation Number | Make the following entries and choose Copy:Quotation: <Quotation Number> (The Quotation from previous step)On the Review Availability Check Result screen, choose Apply. | The Create MTO Standard Order: Overview displays. |  |
| 6 | Change the Delivery Date and Enter Order Details | Make the following entries and choose Enter:Cust. Reference: <Enter a reference number> |  |  |
| 7 | Choose Billing Plan | In case you manually choose Item cateogry: CBAP in step 6 or 7 of [Create Sales Quotation for Configurable Material (Optional)](#unique_18) [page ] 19, then you need to maintain billing plan for the sales order item.If not, you can skip step 7 to 9.Select the item.Choose More > Goto Item > Billing Plan . |  |  |
| 8 | Enter Details | For the first line item (Down Payment), make the following entries for the advance payment:Billing Date: Billing Date, <Enter today's date>Date Description (DTDS): Y009Billing Value: Downpayment value to be invoiced, for example, <1000>Date Category (DCat): 03Press Enter, and delete the entry billing block Y2 in Block field. |  |  |
| 9 | Enter Details | For the second line item make the following entries for the advance payment:Billing Date: Billing Date, <Enter today's date>Date Description (DTDS): Y008Date Category (DCat): 02Press Enter and go back. |  |  |
| 10 | Check Configuration | Option 1: Select the line item and choose Item details: Configuration. On the Variant Configuration screen, check characteristics value and choose Done.Option 2: Select the line item and choose Configuration tab. Choose Product Fork Lifter for Char. Display. Check characteristics value.Note Changing configuration in sales order may change product cost, and results in different product costs in quotation and corresponding sales order. Therefore, if changing of configuration is required by customer, it is suggested to cancel sales order/quotation and create a new quotation instead. |  |  |
| 11 | Display Print Preview | On the Create Sales Order: Overview screen, choose Header Output Preview button.On the Display Sales Order xxx: Output screen, select the line already created for the print output and choose Display Document.Check the variant pricing and configuration details on the displayed PDF document.Variant pricing: Counterweight, Large Fork(optional), Small Fork(optional)Configuration:Fork Size, Counterweight, Wheel Type, Lifer Model, Power Source, Battery Capacity [Ah](optional). | Choose your local destination and press Print. |  |
| 12 | Save | Choose Save. | Sales order is saved.Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation . |

#### Create Sales Order with Configurable Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how a customer buys a forklifter with an individual configuration which is not available on stock and has therefore to be produced individually.

If sales order is already created in the previous two steps, this step can be skipped.

Alternatively, customer can use planning strategy 26 for selling an open material variant which is not available on stock (make-to-order). In this case, configuration is not mandatory in sales order creation, but the predefined configuration in open material variant is copied into sales order.

For selling a material variant of the forklifter which have been produced upfront to selling to customers (make-to-stock), refer to the scope item 21D.

Characteristics of the forklifter can be configured in an additional screen or directly in the sales order line item. Both ways are described in the test procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders (F1873) screen, select Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Order: Initial Screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and press Enter.Sold To party: 33100001Ship To party: 33100001Cust. Reference: <customer purchase order number as reference>Rep. Deliv. Date: <Current date + 5 days> |  |  |
| 6 | Enter Characteristic Value | There are two optional ways to configure the characteristic value for the material. You can choose to execute either step 6 or 7.In the All Items section, enter the following value and choose Enter.Material Number: CM-FL-V00Quantity: for example, 1 PCNote If you want to create billing plan for this sales order, manually enter the following value as well. If not, press Enter.ItCa (Item category): CBTD.On the Variant Configuration screen, select value for characteristics below and choose Done.Lifter Model: <Heavy, Standard>Power Source: <Combustion, Electrical>. Combustion displays as default value.Wheel Type: <Cushion Tires, Pneumatic Tires>Fork Size: <Small, Normal, Large> (If customer-material info record is maintained as described in preliminary step, Small displays as default value.)Counterweight (KG): <1.000, 2.000, 5.000>Battery Capacity(Ah) : Pneumatic<50, 80, 140>Variant condition: AVC_CWEIGHT by defaultNet Value: Varies according to characteristic value chosenThe combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automaticallyWheel Type: Cushion Tires orFork Size: Small or Medium or LargeVariant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeCombination Two:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Variant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeCombination Three:Lifter Model: StandardPower Source: ElectricalWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Battery Capacity(Ah): 50 or 80 or 140 (140 only available when fork size is L)Variant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeOn the Review Availability Check Result screen, choose Apply. |  | If you choose the following combination, a material variant FG-FL-MV-V00 is hit. Material variant will not be covered in this scope item, and there is another scope item 21D to handle it.Lifter Model: STDPower Source: COMBWheel Type: CFork Size: MCounterweight: 2.000kg |
| 7 | Fast Entry of Characteristic Value (Alternative) | Choose Configuration tab and choose Product Fork Lifter for Char. Display. The characteristics Lifer Model, Power Source, Wheel Type, Fork Size, Counterweight and Battery Capacity then display in the columns of All Items section.Enter the following entries in All Items section.Material Number: CM-FL-V00Quantity: for example, 1 PCNote If you want to create billing plan for this sales order, manually enter the following value as well. If not, press Enter.ItCa (Item category): CBTDChoose Enter. Combustion is defaulted for Power Source.Enter value for Lifer Model, Power Source, Wheel Type, Fork Size, Counterweight, and Battery Capacity.Lifter Model: HVY, STDPower Source: COMB, ELECWheel Type: C, PFork Size: S, M, L(If customer-material info record is maintained as described in preliminary step, S displays as default value.)Counterweight (KG): 1.000, 2.000, 5.000Battery Capacity (Ah): 50, 80, 140Press Enter after entering value for each characteristic and value entered is replaced by value description in each field. Allowed combinations of characteristic values are the same as step 6.Note To change value for characteristics, instead of choosing F4 search help button, manually enter the new value in the field directly. |  |  |
| 8 | Choose Billing Plan | In case you manually choose ItCa (Item cateogry): CBTD in step 6 or 7, then you need to maintain billing plan for the item.If not, you can skip step 8 to 10.Select the item Choose More > Goto > Item > Billing Plan | The Billing Plan screen displays. |  |
| 9 | Enter Details | For the first line item (Down Payment), make the following entries for the advance payment:Billing Date: Billing Date, <Enter today's date>Date Description (DTDS): Y009Billing Value: <Downpayment value to be invoiced>, for example, 1000Date Category (DCat): 03Press Enter, and delete the entry billing block Y2 in Block field. |  |  |
| 10 | Enter Details | For the second line item make the following entries for the advance payment:Billing Date: Billing Date, <Enter today's date +1 month>Date Description (DTDS): Y008Date Category (DCat): 02Press Enter and go back. |  |  |
| 11 | Check Pricing | Double-click sales order item and select Condition tab. Pricing of variant components displays.Check the condition value of condition type PVA0.CounterweightThe condition value for Counterweight is calculated by the formula below.Condition value = Sales order quantity * Amount(Unit price) * Char. Value for Counterweight/1000For example, if choose Char. Value 5000KG for Counterweight in Step 6, then Condition value = Sales Quotation quantity * Amount * 5000/1000Small ForkIf choose Char. Value S for Fork Size in step 6, then a minus value for SMALLFORK displays.Large ForkIf choose Char. Value L for Fork Size in step 6, then a value for LARGEFORK displays.Choose Back. | Item Data screen displays |  |
| 12 | Display Print Preview | On the Create Quotation: Overview screen, choose Header Output Preview button.On the Display Quotation xxx: Output screen, select the line already created for the print output and choose Display Document.Check the variant pricing and configuration details on the displayed PDF document.Variant pricing: Counterweight, Large Fork(optional), Small Fork(optional)Configuration:Fork Size, Counterweight, Wheel Type, Lifer Model, Power Source, Battery Capacity [Ah](optional). | Choose your local destination and press Print. |  |
| 13 | Save Document | Choose Save Document. Make a note of the sales order number: __________. | The order is saved.Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation. |

#### Create Down Payment Request

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
| Note In case you maintained billing plan for sales order in section 4.1.2 or 4.1.3, you create an invoice according to your billing plan. Finally, you print out the down payment request and sent it to your customer. If you didn’t maintain billing plan, then you can skip section 4.1.4 and 4.1.5. |

Procedure

To execute this activity, process the following steps using the master data from this document.

Sales Order Processing with Customer Down Payment（BKJ_AE).

- Create Down Payment Request

#### Post Down Payment

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
| Note If you created a down payment request in section 4.1.4, you post the down payment received from your customer in this step. If not you can skip this step. |

Procedure

To execute this activity, process the following steps using the master data from this document.

Sales Order Processing with Customer Down Payment（BKJ_AE).

- Post Down Payment

| Master Data | Sample Value |
| --- | --- |
| Customer | 33100001 |

#### Manufacturing Steps Production Order Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create stock (Sales order stock) for material finished goods.

Procedure

To produce the material and get it into Sales Order stock, execute the following steps described in the Business Process Documentation Test Script of the scope item Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE_AE).

| Master Data | Sample Value |
| --- | --- |
| Material | CM-FL-V00 |
| Plant | 3310 |
| Storage Location | 331A |
| Area of Responsibility Production Supervisor | Plant 1 AE (3310) MTO VC -Valuated (YB3) |

| Test Procedure No. of BJE | Test Procedure | Note |
| --- | --- | --- |
| 4.4.1 | Material Requirements Planning for Sales Order |  |
| 4.6.1 | Create Production Order (CO01) | Before convert planned order into production order, you can check components in planned order.Choose the planned order and choose Open - Planned Order. On the Change Planned Order: Individual customer order screen, choose Componenet Overview. The components and component quantity in the planned order depend on the characteristic value chosen in sales order.Quantity of Counterweight = Planned Order Quantity* Counterweight (SF-FL-CWEIGHT) chosen in sales order/1000Quantity of Counterweight = Planned Order Quantity* Counterweight chosen in sales order/1000Material forksize = The fork size chosen in sales order: SF-FL-FORK-S (Small), SF-FL-FORK-M (Normal) or SF-FL-FORK-L (Large)Type of Tire = The Tire type chosen in sales order: SF-FL-TIRE-PNEU (Pneumatic Tire) or SF-FL-TIRE-CUSH (Cushion Tire)Model type = The power source chosen in sales order: SF-FL-COMB (Combustion) or SF-FL-ELECTRIC (Electrical)After production order is created, check configuration and operation in the Display Production Order (CO03) App.Choose the generated production order and choose Open. Production order Display: Header, the screen displays.Choose Fast Entry tab. Choose Product Fork Lifter for Char. Display. The characteristics Lifer Model, Power Source, Wheel Type, Counterweight and Battery Capacity then display in the columns. Check characteristic value displays the same as chosen in sales order.Choose Display Configuration (or choose from menu bar Header > Configuration ), on the Variant Configuration screen, check if characteristic value displays the same as chosen in sales order. Choose Close after done.Choose Operations. There are two cases:If configuration power source is combustion, there are two operations 0010 and 0031.If configuration power source is electrical, there are two operations 0010 and 0032 in standard sequence. Choose Sequence, and double choose sequence 1, the 0011 operation is also available. |
| 4.6.2 | Release Production Orders (CO05N) | With the Production Supervisor - Discrete Manufacturing role, you can check configuration in the Manage Production Orders (F2336) App.Go to the order in the Manage Production Orders (F2336) App, choose the production order number and choose Open Production Order. On the Production Order screen, go to Items tab, and choose Display in Configuration column.You can check configuration details for the product. On the top right corner, choose Change Log to display the change history of configuration. |
| 4.6.3 | Pick Components (Picking List) |  |
| 4.6.4 | Confirm Assembly Activities | In case power source is combustion, confirm operation 0010 and 0031.In case power source is electrical, confirm operation 0010, 0011 and 0032. |
| 4.6.5 | Posting Goods Receipt for Production Order |  |

#### Delivery and Billing Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to deliver material CM-FL-V00 to the customer and handle the billing.

|  |
| --- |
| Note The delivery and billing processing is differentiated depend on whether you create billing plan in section 4.1.2 or 4.1.3 or not. |

Caution

Without Billing Plan Case

If billing plan is not maintained for the sales order, execute the following steps using the master data from this document (see also the following table).

Sell from Stock (BD9)

| Master Data | Sample Value |
| --- | --- |
| Material | CM-FL-V00 |
| Plant | 3310 |

| Test Procedure No.of BD9 | Test Procedure | Note |
| --- | --- | --- |
| 4.9 | Create Delivery |  |
| 4.11 | Execute Picking |  |
| 4.16 | Post Goods Issue |  |
| 4.20 | Create Billing Document |  |

With Billing Plan Case

If billing plan is maintained for the sales order, execute the following steps using the master data from this document (see also the following table).

Sales Order Processing with Customer Down Payment（BKJ_AE).

| Master Data | Sample Value |
| --- | --- |
| Material | CM-FL-V00 |
| Plant | 3310 |

| Test Procedure No.of BKJ | Test Procedure | Note |
| --- | --- | --- |
| 4.6 | Create Delivery |  |
| 4.8 | Execute Picking |  |
| 4.10 | Post Goods Issue |  |
| 4.11 | Change Sales Orders (Remove Billing Block) |  |
| 4.12 | Billing |  |

Result

You successfully created the delivery and billing.

### Make to Order Production with Multilevel Configurable Material

#### Create Sales Order with Configurable Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how a customer buys a forklifter with an individual configuration which is not available on stock and has therefore to be produced individually.

The forklifter is a multilevel configurable material. One of its components, the seat of the fork lifter is also configurable. Therefore, customer configures the component in sales order as well.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders (F1873) screen, select Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Order: Initial Screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and press Enter:Sold To party: 33100001Ship To party: 33100001Cust. Reference: Reference number Enter a customer purchase order number as referenceRep. Deliv. Date: <Current date + 5 days>Material Number: CM-MLFL-KM-VXXQuantity: for example, 1 PCNote If you want to create billing plan for this sales order, manually enter the following value as well. If not, press Enter.ItCa (Item category): CBTD |  |  |
| 6 | Enter Characteristic Value for Header Material | On the Variant Configuration screen, choose Default Group. Select value for characteristics below:Lifter Model: <Heavy, Standard>Power Source: <Combustion, Electrical>. Combustion displays as default value.Choose Technical and select value for other characteristics.Wheel Type: <Cushion Tires, Pneumatic Tires>Fork Size: <Small, Normal, Large>Counterweight (KG): <1.000, 2.000, 5.000>Battery Capacity(Ah) : <50, 80, 140>The combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automaticallyWheel Type: Cushion Tires or Pneumatic TiresFork Size: Small or Medium or LargeCombination Two:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Combination Three:Lifter Model: StandardPower Source: ElectricalWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Battery Capacity(Ah): 50 or 80 or 140 (140 only available when fork size is L) |  |  |
| 7 | Enter Characteristic value for Component Material | Choose Toggle Structure Panel icon on the top right corner.Choose product SF-FL-FORKSEAT-VXX in the Configuable item panel.Choose value for the following characteristic and choose Done.Seat Color: Black, White or GreySeat Type: Standard, Heavy Duty, or Air suspensionNote Heavy Duty is only selectable if the fork lifter model is Heavy.On the Review Availability Check Result screen, choose Apply. | Configurable item panel displays. |  |
| 8 | Choose Billing Plan | In case you manually choose ItCa (Item cateogry): CBTD in step 5, then you need to maintain billing plan for the item.If not, you can skip step 8 to 10.Select the item Choose More > Goto > Item > Billing Plan. |  |  |
| 9 | Enter Details | For the first line item (Down Payment), make the following entries for the advance payment:Billing Date: Billing Date, <Enter today's date>Date Description (DTDS): Y009Billing Value: <Downpayment value to be invoiced>, for example, 1000Date Category (DCat): 03Press Enter, and delete the entry billing block Y2 in Block field. |  |  |
| 10 | Enter Details | For the second line item make the following entries for the advance payment:Billing Date: Billing Date, <Enter today's date +1 month>Date Description (DTDS): Y008Date Category (DCat): 02Press Enter and go back. |  |  |
| 11 | Check Pricing | Double-click sales order item and select Condition tab. Pricing of variant components displays.Check the condition value of condition type PVA0.CounterweightThe condition value for Counterweight is calculated by the formula below.Condition value = Sales order quantity * Amount(Unit price) * Char. Value for Counterweight/1000For example, if choose Char. Value 5000KG for Counterweight in Step 6, then Condition value = Sales Quotation quantity * Amount * 5000/1000Small ForkIf choose Char. Value S for Fork Size in step 6, then a minus value for SMALLFORK displays.Large ForkIf choose Char. Value L for Fork Size in step 6, then a value for LARGEFORK displays. | The Item Data screen displays. |  |
| 12 | Display Print Preview | On the Create Sales Order: Overview screen, choose Header Output Preview.On the Create Sales Order xxx: Output screen, select the line already created for the print output and choose Display Document.Check the variant pricing and configuration details on the displayed PDF document.Variant pricing: Counterweight, Large Fork(optional), Small Fork(optional)Configuration: Fork Size, Counterweight, Wheel Type, Lifer Model, Power Source, Battery Capacity [Ah](optional). | Choose your local destination and press Print. |  |
| 13 | Save Document | Choose Save Document. Make a note of the sales order number: __________. | The order is saved.Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation. |

#### Create Down Payment Request

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
| Note In case you maintained billing plan for sales order in section 4.2.1, you create an invoice according to your billing plan. Finally, you print out the down payment request and sent it to your customer. If you didn’t maintain billing plan, then you can skip section 4.2.2 and 4.2.3. |

Procedure

To execute this activity, process the following steps using the master data from this document.

Sales Order Processing with Customer Down Payment（BKJ_AE).

- Create Down Payment Request

#### Post Down Payment

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
| Note If you created a down payment request in section 4.2.2, you post the down payment received from your customer in this step. If not you can skip this step. |

Procedure

To execute this activity, process the following steps using the master data from this document.

Sales Order Processing with Customer Down Payment（BKJ_AE).

- Post Down Payment

| Master Data | Sample Value |
| --- | --- |
| Customer | 33100001 |

#### Manufacturing Steps Production Order Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create stock (Sales order stock) for material finished goods. As one of the components is external procured, to get supply of seat, execute scope item Procurement of Materials with Variant Configuration (2XU_AE) after step 4.6.2 as below.

Procedure

To produce the material and get it into Sales Order stock, execute the following steps described in the Business Process DocumentationTest Script of the scope item Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE_AE)

| Master Data | Sample Value |
| --- | --- |
| Material | CM-MLFL-KM-VXX |
| Plant | 3310 |
| Area of Responsibility Production Supervisor | Plant 1 AE (3310) MTO VC -Valuated (YB3) |

| Test Procedure No. of BJE | Test Procedure | Note |
| --- | --- | --- |
| 4.4.1 | Material Requirements Planning for Sales Order | After MRP run is complete, a purchase requisite is created for BoM component SF-FL-FORKSEAT-VXX. Execute scope item AE_2XU to get stock of this material.The material is picked by production order in step 4.6.3. |
| 4.6.1 | Create Production Order (CO01) | Before convert planned order into production order, you can check components in planned order.Choose the planned order and Open - Planned Order. On the Change Planned Order: Individual customer order screen, choose Componenet Overview. The components and component quantity in the planned order depend on the characteristic value chosen in sales order.Quantity of Counterweight = Planned Order Quantity* Counterweight (SF-FL-CWEIGHT) chosen in sales order/1000Quantity of Counterweight = Planned Order Quantity* Counterweight chosen in sales order/1000Material forksize = The fork size chosen in sales order: SF-FL-FORK-S (Small), SF-FL-FORK-M (Normal) or SF-FL-FORK-L (Large)Type of Tire = The Tire type chosen in sales order: SF-FL-TIRE-PNEU (Pneumatic Tire) or SF-FL-TIRE-CUSH (Cushion Tire)Model type = The power source chosen in sales order: SF-FL-COMB (Combustion) or SF-FL-ELECTRIC (Electrical)After production order is created, check configuration and operation in production order.Choose the generated production order and Open. Production order Display: Header, the screen displays.Choose Display Configuration (or choose from menu bar Header > Configuration ), on the Variant Configuration screen, check if characteristic value displays the same as chosen in sales order. Choose Close after done.Choose Operation. There are two cases.If configuration power source is combustion, there are two operations: 0010 and 0031.If configuration power source is electrical, there are 2 operations 0010 and 0032 in standard sequence. Choose Sequence, and double choose sequence 1, the 0011 operation is also available. |
| 4.6.2 | Release Production Orders (CO05N) | With the Production Supervisor - Discrete Manufacturing role, you can check configuration in the Manage Production Orders (F2336) App.Go to the order in the Manage Production Orders (F2336) App, choose the production order number and choose Open Production Order. On the Production Order screen, go to Items tab, and choose Display in Configuration column.You can check configuration details for the product. For multilevel configuration product, configuration for final product displays. On the top right corner, choose Change Log to display the change history of configuration. |
| 4.6.3 | Pick Components (Picking List) |  |
| 4.6.4 | Confirm Assembly Activities | In case power source is combustion, confirm operation 0010 and 0031.In case power source is electrical, confirm operation 0010, 0011 and 0032. |
| 4.6.5 | Posting Goods Receipt for Production Order |  |

#### Delivery and Billing Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to deliver material CM-MLFL-KM-VXX to the customer and handle the billing.

|  |
| --- |
| Note The delivery and billing processing is differentiated depend on whether you create billing plan in section 4.2.1 or not. |

Caution

Without Billing Plan Case

If billing plan is not maintained for the sales order, execute the following steps using the master data from this document (see also the following table).

Sell from Stock (BD9)

| Master Data | Sample Value |
| --- | --- |
| Material | CM-MLFL-KM-VXX |
| Plant | 3310 |

| Test Procedure No.of BD9 | Test Procedure | Note |
| --- | --- | --- |
| 4.9 | Create Delivery |  |
| 4.11 | Execute Picking |  |
| 4.16 | Post Goods Issue |  |
| 4.20 | Create Billing Document |  |

With Billing Plan Case

If billing plan is maintained for the sales order, execute the following steps using the master data from this document (see also the following table).

Sales Order Processing with Customer Down Payment（BKJ_AE).

| Master Data | Sample Value |
| --- | --- |
| Material | CM-MLFL-KM-VXX |
| Plant | 3310 |

| Test Procedure No.of BKJ | Test Procedure | Note |
| --- | --- | --- |
| 4.6 | Create Delivery |  |
| 4.8 | Execute Picking |  |
| 4.10 | Post Goods Issue |  |
| 4.11 | Change Sales Orders (Remove Billing Block) |  |
| 4.12 | Billing |  |

Result

You successfully created the delivery and billing.

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Complete the following activities:Posting a Customer Invoice in AccountingOverdue ReceivablesDisplay Customer BalancesManage Customer Line Items |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

### Relevant Processes

If the following processes are enabled in your system, you can also test these business processes for the configurable material described in this test script.

| Process |
| --- |
| BD9 - Sell from Stock |
| BDD - Lean Customer Returns |
| BDG - Sales Quotation |
| BDH - Sales Order Entry with One-Time Customer |
| BDQ - Invoice Correction Process with Debit Memo |
| BDW - Returnables Processing |
| BKL - Invoice Correction Process with Credit Memo |
| BKZ - Sales Order Processing with Invoice List and Collective Billing |
| BKX - Sales Order Processing – SEPA Direct Debit Handling |
| BKP - Customer Returns |
| 1F1 - Debit Memo Processing |
| 1EZ - Credit Memo Processing |
| 1B6 - Sales Rebate Processing |
| 1MC - Omnichannel Convergent Billing |
| 1Z1 - Digital Payments – Sales |

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
- related-to :: [[02-business-partner-and-product-master-data/set-up-configurable-model-using-variant-configuration-22t-ae-test-scri]]
- related-to :: [[12-production-and-manufacturing/test-script-lot-size-of-one-with-advanced-variant-configuration-55e-ae]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-production-with-variant-configuration-21d-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 73,884 chars in the whole document
