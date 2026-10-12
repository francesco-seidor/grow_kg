---
id: 12-production-and-manufacturing/test-script-make-to-stock-production-with-variant-configuration-21d-ae
title: "Test Script: Make-to-Stock Production with Variant Configuration (21D_AE) (21D_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 21D_AE: prerequisites and steps to produce, stock, sell and bill forklifter material variants."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/variant-configured-production]
aliases: [21D_S4CLD2608_BPD_EN_AE]
keywords: [Production of Variant-Configured Products, make-to-stock production, variant configuration, material variants, variant matching, sales order processing, test procedures, preliminary steps, initial stock posting, configurable bill of material]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21D_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-796
topic: 12-production-and-manufacturing/variant-configured-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Stock Production with Variant Configuration (21D_AE) (21D_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21D_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Production of Variant-Configured Products** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Stock Production with Variant Configuration (21D_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848664)

[2 Prerequisites 4](#_Toc232848665)

[2.1 System Access 4](#_Toc232848666)

[2.2 Roles 4](#_Toc232848667)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232848668)

[2.4 Business Conditions 7](#_Toc232848669)

[2.5 Preliminary Steps 8](#_Toc232848670)

[2.5.1 Initial Stock Posting for the Material in BoM of FG-FL-MV-V00 8](#_Toc232848671)

[2.5.2 Exclude Characteristics for Variant Matching 9](#_Toc232848672)

[2.5.3 Assign Configurable Material in Material Variant Master Data 9](#_Toc232848673)

[2.5.4 Link Configurable BoM to Material Variant 11](#_Toc232848674)

[2.5.5 Maintain Production Version for Material Variant 11](#_Toc232848675)

[2.5.6 Create Master Data for Fast Data Entry 12](#_Toc232848676)

[2.5.6.1 Create Application Group 12](#_Toc232848677)

[2.5.6.2 Create Characteristic Display 13](#_Toc232848678)

[3 Overview Table 15](#_Toc232848679)

[4 Test Procedures 16](#_Toc232848680)

[4.1 Production Planning 16](#_Toc232848681)

[4.2 Production Execution 17](#_Toc232848682)

[4.3 Sales Order Processing 19](#_Toc232848683)

[4.3.1 Create Sales Order With Material Variant 19](#_Toc232848684)

[4.4 Delivery and Billing Processing 22](#_Toc232848685)

[5 Appendix 24](#_Toc232848686)

[5.1 Succeeding Processes 24](#_Toc232848687)

## Purpose

Overview

This scope item shows the Make-to-Stock Production with Variant Configuration in which Advanced Variant Configuration enables efficient state-of-the-art configuration for configurable products variants that reflect common definitions of a configurable material. The material variant is defined as a Bill of Material (BOM) where the components meet certain criteria. Initially, this material variant is produced and put into stock as later sales of it are anticipated by collection of Planned-Independent Requirements (PIRs). When a customer orders a fork lifter where the characteristics of the components meet those of the material variant, the fork lifter is taken directly from stock as production already happened based on PIRs. The sales price calculation is then based on the characteristics of the material variant. Since the material variant is available on stock, the fork lifter is directly delivered. The process finishes with the billing of the delivered fork lifter.

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
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

Manufacturing / Trading

Production Plant

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG-FL-MV-V00 | Forklifter Material Variant |  |
| Material | CM-FL-V00 | Configurable Forklifter |  |
| Material | SF-FL-COMB | FORKLIFTER BASE MODEL ELECTRICAL | Initial stock posting required |
| Material | SF-FL-CWEIGHT | COUNTERWEIGHT 1000KG | Initial stock posting required |
| Material | SF-FL-FORK-M | FORK (1.800 MM) | Initial stock posting required |
| Material | SF-FL-TIRE-CUSH | CUSHION TIRE ASSEMBLY | Initial stock posting required |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

This is a super BoM list for configurable materials. Not all components necessarily used in production order.

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| CM-FL-V00 | 0 | KMAT | PC | Configurable Forklifter |  |
| SF-FL-COMB | 1 | HALB | PC | FORKLIFTER BASE MODEL COMBUSTI-ON |  |
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

Application Groups

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Application Groups | SD | Sales and Distribution Document |  |

Characteristic Display

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Characteristic Display | PROD_FK | Assigned Characteristics:Lifter ModelPower Source1Wheel TypeCounterweightFork SizeBattery Capacity [Ah] |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 2NI | Create Application Group and Characteristic Display - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run - MDS | You have completed the steps described in the master data script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up-to-date. |

### Preliminary Steps

#### Initial Stock Posting for the Material in BoM of FG-FL-MV-V00

Purpose

In a real business case, the materials are usually purchased from external vendors; in that case, that process is covered by the standard purchasing or subcontracting processes. This process step shows you how to post initial stock directly to the storage locations. Please note that you only need to post initial stock in case there is none available or the current stock is insufficient. Ensure that at least as many components for the material variant, i.e. forklifter, are available as you intend to sell in the later steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entry and press Enter:Material: All components materials listed in Master Data section needed for FG-FL-MV-V00. Except for CM-FL-V00Plant: 3310 |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331BUnrestricted-Use Stock | A dialog box appears. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <enter a number> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

#### Exclude Characteristics for Variant Matching

Purpose

This process step shows you how to exclude characteristics for variant matching.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Characteristic Exclusions (F5984). | The Manage Characteristic Exclusions screen displays. |  |
| 3 | Search for Characteristics | In the header section, enter FG-FL-MV-V00 for Product and choose Go. | The list of characteristics displays. |  |
| 4 | Edit Exclusion for Characteristics | Choose the Edit icon for characteristic AVC_CR_SDCOMVKOND_VXX.In the popup dialog, select the checkbox for Product-independent Variants Matching Exclusion and choose Save.Repeat the same step for characteristic AVC_CR_STPOQTY_VXX. |  |  |

#### Assign Configurable Material in Material Variant Master Data

Purpose

This process step shows you how to assign a configuration material to material variant in material Master data.

This assignment needs to be executed once for each plant only.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen displays. |  |
| 3 | Input Product | Make the following entry in the search box and choose Go: FG-FL-MV-V00 |  |  |
| 4 | Select Product | Choose the searched record.Choose Edit on the top right corner of the screen.Choose Plants tab. And choose the record for plant 3310. | The Product screen displays. |  |
| 5 | Assign Configurable Material | In the Configuration section, make the following entry and choose Configure Variant.Configurable Product: CM-FL-V00 | The Configuration screen displays. |  |
| 6 | Select Characteristic Value | Select values for the following fields from dropdown menu. Double click Apply to go back to Product screen.Lifter Model: StandardPower Source: CombustionWheel Type: Cushion TiresCounterweight(KG): 2000Fork Size: Normal |  |  |
| 7 | Save Entry | Choose Save. | Master data record is saved. |  |
| 8 | Repeat the Steps | Repeat step 3 to 7 for product FG-FL-MV-V01 and FG-FL-MV-V02.Select following value for each product.For FG-FL-MV-V01:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion TiresCounterweight(KG): 1000kgFork Size: NormalFor FG-FL-MV-V02:Lifter Model: HeavyPower Source: CombustionWheel Type: Cushion TiresCounterweight(KG): 5000kgFork Size: Normal |  |  |

#### Link Configurable BoM to Material Variant

Purpose

This process step shows you how to link the BoM of configurable material to material variant.

This assignment need to be executed once for each plant only.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Link to Configurable Material (CS40). | The Create Link to Configurable Material: Initial Screen displays. |  |
| 3 | Input Product | Make the following three entries and choose Enter:Material: FG-FL-MV-V00Plant: 3310BOM Usage: 1Material: FG-FL-MV-V01Plant: 3310BOM Usage: 1Material: FG-FL-MV-V02Plant: 3310BOM Usage: 1 | The Create Link to Configurable Material: New Assignments screen displays. |  |
| 4 | Save Entry | Choose Save. |  |  |

#### Maintain Production Version for Material Variant

Purpose

This process step shows you how to maintain production version for material variant.

This only needs to be executed once for each plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | The Production Version: Mass Processing screen displays. |  |
| 3 | Input Selection Condition | Make the following entry and choose Enter:Plant: 3310Material : FG-FL-MV-V00 |  |  |
| 4 | Select Production Version | Select the first line of product versions. |  |  |
| 5 | Check Production Version | Choose Consistency Check. |  |  |
| 6 | Save Data | Close the detail screen and go back to Production Version: Mass Processing screen.Choose Save. |  |  |
| 7 | Repeat the Steps | Repeat step 3 to 6 for material FG-FL-MV-V01 and FG-FL-MV-V02. |  |  |

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
| 3 | Enter Application Group | On the Change View "Application Group": Overview screen, choose New Entries. And make the following two entries.Transact.: (Select from dropdown list) SD Sales and Distribution DocumentAppl Grp: <Enter the Application group ID you would like to create>, for example, SDTransact. : (Select from dropdown list) PP Production OrderAppl Grp: <Enter the Application group ID you would like to create>, for example, PP | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Save Your Data | Choose Save. |  |  |

##### Create Characteristic Display

Purpose

This process step shows you how to create characteristic display, and assign characteristic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Char. Display for Configuration (CU_CHAR_DISPLAY) | The Change View "Application Group": Overviewscreen displays. |  |
| 3 | Enter Application Group | On the Change View "Application Group" : Overview screen, double-click Charactersitic Display.Choose New Entry. Make the following entry and choose Enter.Char. Display: PROD_FKDescription: Product Fork LifterAppl. Grp: SD | The Change View "Characteristic Display": Overview screen displays. |  |
| 4 | Assign Characteristic | Choose the characteristic display created in step3 and double-click Characteristic Assignment and choose New Entries.Make the following entries.Sequence Characteristic:5 AVC_CR_LIFTERMODEL_VXX10 AVC_CR_POWERSOURCE_VXX20 AVC_CR_WHEELTYPE_VXX30 AVC_CR_COUNTERWEIGHT_VXX40 AVC_CR_FORKSIZE_VXX50 AVC_CR_BCAPACITY_V00Go back to the Change View "Application Group": Overview screen, repeat step 3 and 4 with following values.Char. Display: PP_FKDescription: Product Fork LifterAppl.: Grp: PPSequence Characteristic:5 AVC_CR_LIFTERMODEL_VXX10 AVC_CR_POWERSOURCE_VXX20 AVC_CR_WHEELTYPE_VXX30 AVC_CR_COUNTERWEIGHT_VXX40 AVC_CR_FORKSIZE_VXX50 AVC_CR_BCAPACITY_V00 | The Change View "Characteristic Assignment": Overview screen displays. |  |
| 5 | Save Your Data | Choose Save. |  |  |

## Overview Table

The scope item Make-to-Stock Production with Variant Configuration consists of several process steps provided in the following table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Production Planning](#unique_16) [page ] 16 |  |  |  |
| [Production Execution](#unique_17) [page ] 17 |  |  |  |
| Sales Order Processing |  |  |  |
| [Create Sales Order With Material Variant](#unique_18) [page ] 19 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Delivery and Billing Processing](#unique_19) [page ] 22 |  |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Production Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you make planned independent requirements and perform requirement planning for the finished goods.

|  |
| --- |
| Caution To execute this activity, process the following steps using the master data from this document (see also the following table). |

BJ5 - Make-to-Stock Production – Discrete Manufacturing

| Test Procedure No. | Test Procedures | Note |
| --- | --- | --- |
| 4.1.1 | Create Planned Independent Requirements |  |
| 4.1.2 | Material Requirements Planning at Plant Level |  |
| 4.1.3 | Evaluate Stock / Requirements Situation | Check components in planned order.Choose the planned order and choose Change Planned Order. On the Change Planned Order: Individual customer order screen, choose Componenet Overview. The components in the planned order depend on the characteristic value maintained in the product master in 21D preliminary step.Quantity of Counterweight = Planned Order Quantity* 2Forksize = SF-FL-FORK-M (Normal)Type of Tire = SF-FL-TIRE-CUSH (Cushion Tire)Power source = SF-FL-COMB (Combustion) |

| Master Data | Sample Value |
| --- | --- |
| Material | FG-FL-MV-V00 |
| Plant | 3310 |

Result

You successfully planned the production of the finished good.

### Production Execution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to manufacture the finished good and put it into stock.

|  |
| --- |
| Caution To execute this activity, process the following steps using the master data from this document (see also the following table). |

Make-to-Stock Production – Discrete Manufacturing (BJ5)

| Test Procedure No. | Test Procedures | Note |
| --- | --- | --- |
| 4.2.1 | Conversion into Production Orders for Subassembly and Final Assembly | Check configuration in production order.Choose the generated production order and choose Open. The Production order Display: Header screen displays. There are two options to check configuration.Choose Fast Entry tab. Choose Product Fork Lifter for Char. Display. The characteristics Lifer Model, Power Source, Wheel Type, Counterweight and Battery Capacity display in the columns. Check if characteristic value displays as below.Choose Display Configuration (or choose from menu bar Header > Configuration ), on the Variant Configuration screen, check if characteristic value displays as below.Lifter Model: StandardPower Source: CombustionWheel Type: Cushion TireCounterweight(KG): 2000kgForksize: Normal Fork |
| 4.4.2 | Release Finished GoodsProduction Orders for Final Assembly |  |
| 4.4.4 | Pick Components for Final Assembly |  |
| 4.4.7 | Final Confirmation of Production Operations for Final Assembly | The only operation number for CM-FL-V00 material is 0010. |
| 4.4.8 | Post Goods Receipt for Final Assembly Production Order |  |

| Master Data | Sample Value |
| --- | --- |
| Material | FG-FL-MV-V00 |
| Plant | 3310 |

### Sales Order Processing

#### Create Sales Order With Material Variant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a customer wants to buy a forklift with a configuration which leads to a material variant of the configurable forklift. This material variant was already produced so the selling happens directly from stock. For selling an individual configuration of the forklift to a customer which has to be produced individually for the customer (make-to-order), please refer to the scope item 1YT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com-ment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders (F1873) screen, choose Create Sales Order - VA01. |  |  |
| 4 | Enter the Order Type OR (Standard Order) | On the Create Sales Documents, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview, make the following entries and choose Enter:Sold To Party: 33100001Ship To Party: 33100001Cust. Reference: <Reference number> Enter a customer purchase order number as reference.Req. Deliv.Date: <Current Date + 3 days> |  |  |
| 6 | Enter Material Variant: Directly or by Entering Characteristic Values and Search for Matching Product | You can directly input material number of material variant as below and then continue with step 9.Material Number: FG-FL-MV-V00Quantity:For example, 1 PCAlternatively, you can find material variant via variant matching after entering characteristic value. You can follow step 6, or 7, or 8.In the All Items section, enter the following value and press Enter.Material Number: CM-FL-V00Quantity: For example, 1 PCOn Variant Configuration screen, select value for characteristics below.Power Source: CombustionWheel Type: Cushion TireForksize: Normal ForkChoose Variant Matching, and on the Display Matching Product Variants screen, the following product display as Type of Match: Partial Match.FG-FL-MV-V00FG-FL-MV-V01FG-FL-MV-V022 Characteristic displays in Valuation Difference column, Choose 2 characteristic to check the difference between present value and variant value,AVC_CR_COUNTERWEIGHT_VXXAVC_CR_LIFTERMODEL_VXXClose the dialog screen, and select value for characteristic below.Lifter Model: StandardChoose Variant Matching, and on the Display Matching Product Variants screen, the following product display as Type of Match: Partial Match.FG-FL-MV-V00FG-FL-MV-V011 Characteristic displays in Valuation Difference column. Choose 1 characteristic to check the difference between present value and variant value,AVC_CR_COUNTERWEIGHT_VXXClose the dialog screen, and select value for characteristic below.Counterweight(KG): 2000FG-FL-MV-V00 displays as Fully Matching Product Variant in header. Choose Variant Matching button, and on the Display Matching Product Variants screen, the following product display as Type of Match: Full Match.FG-FL-MV-V00Choose product FG-FL-MV-V00. Choose Replace on the dialog screen. Choose Apply on the Review Availability Check Result screen. | The Variant Configuration screen displays.Material Variant FG-FL-MV-V00 replaces CM-FL-V00 in the Material field of sales order item. |  |
| 7 | Enter Characteristic Value and Choose Material Variant (Optional) | In the All Items section, enter the following value and press Enter.Material Number:CM-FL-V00Quantity: For example, 1 PCOn the Variant Configuration screen, select value for characteristics below. :Power Source: CombustionWheel Type: Cushion TireForksize: Normal ForkLifter Model: StandardCounterweight: 2000Choose Done, on the Display Material Variants screen, select the material s and choose OK.Choose Apply on the Review Availability Check Result screen. |  |  |
| 8 | Fast Entry of Characteristic Value (Optional) | Choose Configuration tab and choose Product Fork Lifter for Char. Display.The characteristics Lifer Model, Power Source, Wheel Type, Fork Size, Counterweight and Battery Capacity[Ah] then display in the columns of All Items section.Make the following entries and press Enter:Material: CM-FL-V00Order Quantity: For example, <1 PC>Choose value for characteristic by using F4 search help. Choose Enter after select each characteristic value.Lifter Model: STDWheel Type: CFork Size: MCounterweight(KG): 2000On the Display Material Variants screen, select the material FG-FL-MV-V00 and choose OK.On the Review Availability Check Result screen, choose Apply. | Material Variant FG-FL-MV-V00 replaces CM-FL-V00 in the Material field of sales order item. |  |
| 9 | Display Print Preview | On the Create Standard Order: Overview screen, choose Header Output Preview.On the Create Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document.Check the configuration details on the displayed PDF document.Variant pricing: CounterweightConfiguration:Power Source: CombustionLifter Model: StandardWheel Type: CushionCounterweight: 2000kgForksize: Normal |  |  |
| 10 | Save Document | Choose Save. Make a note of the sales order number: __________. | The order is saved and the order confirmation is printed out.Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

### Delivery and Billing Processing

Purpose

This process step shows you how to deliver material FG-FL-MV-V00 to the customer.

|  |
| --- |
| Caution To execute this activity process the following steps using the master data from this document (see also the following table). |

Sell from Stock (BD9)

| Test Procedure No. | Test Procedures | Note |
| --- | --- | --- |
| 4.9 | Create Delivery |  |
| 4.11 | Execute Picking |  |
| 4.15 | Post Goods Issue |  |
| 4.18 | Create Billing Document |  |

| Master Data | Sample Value |
| --- | --- |
| Material | FG-FL-MV-V00 |
| Plant | 3310 |

Result

You successfully created the delivery and billing for the finished goods.

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Complete the following activities:Posting a Customer Invoice in AccountingOverdue ReceivablesDisplay Customer BalancesManage Customer Line Items |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
> Flagged while digesting this document, not verified: Material SF-FL-COMB is described as 'FORKLIFTER BASE MODEL ELECTRICAL' in the master data table, but as the combustion base model in the BoM table (where SF-FL-ELECTRIC is the electrical one) and as 'Power source = SF-FL-COMB (Combustion)' in the planned order check.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/set-up-configurable-model-using-variant-configuration-22t-ae-test-scri]]
- related-to :: [[12-production-and-manufacturing/test-script-lot-size-of-one-with-advanced-variant-configuration-55e-ae]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-order-production-with-variant-configuration-1yt-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21D_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 34,707 chars in the whole document
