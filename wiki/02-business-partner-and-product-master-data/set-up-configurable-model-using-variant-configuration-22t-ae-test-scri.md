---
id: 02-business-partner-and-product-master-data/set-up-configurable-model-using-variant-configuration-22t-ae-test-scri
title: "Set Up Configurable Model Using Variant Configuration (22T_AE) - Test Script, SAP S/4HANA Cloud Public Edition 2608 (22T_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 22T: model, simulate and replicate a configurable forklift using variant configuration."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data, topic/variant-configured-production]
aliases: [22T_S4CLD2608_BPD_EN_AE]
keywords: [Configurable Materials and Characteristic Display, variant configuration, configurable bom, characteristics and classes, variant tables, configuration profile, constraint net, high-level dependencies, super bom, configuration simulation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22T_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-802
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Set Up Configurable Model Using Variant Configuration (22T_AE) - Test Script, SAP S/4HANA Cloud Public Edition 2608 (22T_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22T_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Set Up Configurable Model Using Variant Configuration (22T_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848679)

[2 Prerequisites 4](#_Toc232848680)

[2.1 System Access 4](#_Toc232848681)

[2.2 Roles 4](#_Toc232848682)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232848683)

[2.4 Preliminary Steps 10](#_Toc232848684)

[2.4.1 Assign Routing for CM-FL-V01 10](#_Toc232848685)

[2.4.2 Assign Dependency to Operation and Sequence in Routing 10](#_Toc232848686)

[3 Overview Table 13](#_Toc232848687)

[4 Test Procedures 15](#_Toc232848688)

[4.1 Create Configurable BOM 15](#_Toc232848689)

[4.1.1 Create Characteristic 15](#_Toc232848690)

[4.1.2 Create Class – Class type 300: Variants 16](#_Toc232848691)

[4.1.3 Assign Class to Product 18](#_Toc232848692)

[4.1.4 Create Variant Table 19](#_Toc232848693)

[4.1.5 Create Variant Table Content 20](#_Toc232848694)

[4.1.6 Create Configuration Profile 22](#_Toc232848695)

[4.1.7 Change Configuration Profile to Assign Characteristic Group 23](#_Toc232848696)

[4.1.8 Create Constraint Net 26](#_Toc232848697)

[4.1.9 Create and Assign High-Level Dependencies 27](#_Toc232848698)

[4.1.9.1 Define Constraint 27](#_Toc232848699)

[4.1.9.2 Define Procedure 29](#_Toc232848700)

[4.1.9.3 Define Precondition on a Characteristic 31](#_Toc232848701)

[4.1.9.4 Define Precondition on a Characteristic Value 32](#_Toc232848702)

[4.1.10 Create Super BOM 34](#_Toc232848703)

[4.1.11 Simulate Single-Level Configurable BOM 37](#_Toc232848704)

[4.1.12 (Optional) Replicate Configuration Model to SAP Business Technology Platform 40](#_Toc232848705)

[4.1.13 (Optional) Simulate Multi-Level Configurable BOM 42](#_Toc232848706)

[4.1.14 Simulate Configurable Routing 43](#_Toc232848707)

[4.1.15 (Optional) Analyze Configurable BOM Simulation 45](#_Toc232848708)

[4.2 Maintain Configurable BOM 48](#_Toc232848709)

[4.2.1 Without Requirement Driven Development 48](#_Toc232848710)

[4.2.1.1 Create High-Level Dependency and Simulate 48](#_Toc232848711)

[4.2.1.2 (Optional) Replicate Modeling Changes to SAP Business Technology Platform 50](#_Toc232848712)

[4.3 (Optional) Create Sales Set 52](#_Toc232848713)

[4.4 (Optional) Additional Manual Configuration for Replicate Configurable Models using Product Data Replication (PDR) 52](#_Toc232848714)

[4.4.1 (Optional) Product Data Replication (PDR) 52](#_Toc232848715)

[4.4.1.1 (Optional) Configure PDR Using SSCUIs 53](#_Toc232848716)

[4.4.1.2 (Optional) Replicate Configurable Models using Product Data Replication (PDR) 55](#_Toc232848717)

## Purpose

Overview

Improve your company's product engineering, sales, and manufacturing performance with SAP software for integrated variant configuration and classification. Enable your business process to handle highly individualized products in sales and manufacturing.

A comprehensive simulation environment supports state-of-the-art configuration, sophisticated analysis of your configurable products, and real-time integration to the configurable BOM Explosion. Get support from integrated requirements management.

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
| Product Configuration ModelerMaintains the variant-configuration-specific master data such as classes, characteristics, variant conditions, dependencies, configuration profiles, and so on.Collaborates with PLM department, production supervisors, and others relevant to manufacturing. | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Master Data Specialist - Product DataMaintains the product master details in collaboration with the other departments such as PLM, production, planning, purchase, sales, and so on. | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Production Engineer - Discrete ManufacturingMaintains the production-specific master data such as BOM, routing, and so on, for discrete manufacturing.Collaborates with the engineering and planning departments, production supervisors, and others relevant to manufacturing. | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in the system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedures.

Table 1: Single-Level Configurable BOM

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Material | CM-FL-V01 | Forklift | Configurable MaterialNoteIf the material CM-FL-V01 already exists, then create the material CM-FL-Vnn, where nn is the running number.Ensure that the AVC_CL_REFCSTC_VXX and AVC_CL_COMMON_VXX classes are assigned to the material. |
| Material | SF-FL-COMB | Forklift Base Combustion Model | Semi-finished Material |
| Material | SF-FL-ELECTRIC | Forklift Base Electrical Model | Semi-finished Material |
| Material | SF-FL-CWEIGHT | Forklift Counterweight Plate | Semi-finished Material |
| Material | SF-FL-TIRE-CUSH | Forklift Cushion Tire | Semi-finished Material |
| Material | SF-FL-TIRE-PNEU | Forklift Pneumatic Tire | Semi-finished Material |
| Material | SF-FL-FORK-S | Forklift Small Fork | Semi-finished Material |
| Material | SF-FL-FORK-M | Forklift Medium Fork | Semi-finished Material |
| Material | SF-FL-FORK-L | Forklift Large Fork | Semi-finished Material |
| Characteristic | AVC_CR_LIFTERMODEL_VXX | Lifter Model |  |
| Characteristic | AVC_CR_POWERSOURCE_VXX | Power Source |  |
| Characteristic | AVC_CR_WHEELTYPE_VXX | Wheel Type |  |
| Characteristic | AVC_CR_COUNTERWEIGHT_VXX | Counter Weight |  |
| Characteristic | AVC_CR_FORKSIZE_VXX | Fork Size |  |
| Characteristic | AVC_CR_STPOQTY_VXX | Component Quantity |  |
| Characteristic | AVC_CR_FORKLENGTH_VXX | Fork Length |  |
| Class | AVC_CL_COMMON_VXX | Forklifter High Level Configuration | Variant Class (type: 300) |
| Class | AVC_CL_REFCSTC_VXX | Reference Cstics | Variant Class (type: 300) |
| Class | AVC_CL_FORK_VXX | Fork for Class Node | Material – Configurable Objects (type: 200) |
| Dependencies | AVC_OD_CALCPRICECWEIGHT_VXX | HL: Procedure Pricing |  |
| Dependencies | AVC_OD_CALCFORKLEN_VXX | LL: Determine Fork Length |  |
| Dependencies | AVC_OD_CALCCWEIGH_VXX | LL: Calc Counterweight Qty |  |
| Dependencies | AVC_OD_CTIREONLY_VXX | LL: Cushion Tire |  |
| Dependencies | AVC_OD_PTIREONLY_VXX | LL: Pneumatic Tire |  |
| Dependencies | AVC_OD_COMBONLY_VXX | LL: Combustion Power Source |  |
| Dependencies | AVC_OD_ELECONLY_VXX | LL: Electrical Power Source |  |

Table 2: Multi-Level Configurable BOM

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Material | CM-MLFL-KM-VXX | Multi-Level Forklifter | Configurable Material |
| Material | SF-FL-COMB | Forklift Base Combustion Model | Semi-finished Material |
| Material | SF-FL-ELECTRIC | Forklift Base Electrical Model | Semi-finished Material |
| Material | SF-FL-CWEIGHT | Forklift Counterweight Plate | Semi-finished Material |
| Material | SF-FL-TIRE-CUSH | Forklift Cushion Tire | Semi-finished Material |
| Material | SF-FL-TIRE-PNEU | Forklift Pneumatic Tire | Semi-finished Material |
| Material | SF-FL-FORK-S | Forklift Small Fork | Semi-finished Material |
| Material | SF-FL-FORK-M | Forklift Medium Fork | Semi-finished Material |
| Material | SF-FL-FORK-L | Forklift Large Fork | Semi-finished Material |
| Material | SF-FL-FORKSEAT-VXX | Seat Type of Fork lifter (HALB) | Semi-finished Material |
| Characteristic | AVC_CR_LIFTERMODEL_VXX | Lifter Model |  |
| Characteristic | AVC_CR_POWERSOURCE_VXX | Power Source |  |
| Characteristic | AVC_CR_WHEELTYPE_VXX | Wheel Type |  |
| Characteristic | AVC_CR_COUNTERWEIGHT_VXX | Counter Weight |  |
| Characteristic | AVC_CR_FORKSIZE_VXX | Fork Size |  |
| Characteristic | AVC_CR_STPOQTY_VXX | Component Quantity |  |
| Characteristic | AVC_CR_FORKLENGTH_VXX | Fork Length |  |
| Characteristic | AVC_CR_BCAPACITY_VXX | Battery Capacity [Ah] |  |
| Characteristic | AVC_CR_SEAT_TYPE_VXX | Seat Type |  |
| Characteristic | AVC_CR_SEAT_COLOR | Seat Color |  |
| Characteristic | AVC_CR_PLPOVGW03_VXX | Standard Value |  |
| Class | AVC_CL_COMMON_VXX | Forklifter High Level Configuration | Variant Class (type: 300) |
| Class | AVC_CL_REFCSTC_VXX | Reference Cstics | Variant Class (type: 300) |
| Class | AVC_CL_ELECADD_VXX | Add Cstics for Electrical Forklifter | Variant Class (type: 300) |
| Class | AVC_CL_FORK_VXX | Fork for Class Node | Material – Configurable Objects (type: 200) |
| Class | AVC_CL_FORKSEAT_VXX | Cstics for Forklifter Seat | Variant Class (type: 300) |
| Variant Table and Content | AVC_VT_BASECMB_VXX | Forklifter Common Model Restriction |  |
| Configuration Profile | AVC_CP_MULTILEVEL_VXX |  |  |
| Configuration Profile | AVC_CP_FORKSEAT_VXX |  |  |
| Dependency Net | AVC_OD_CNSTRNET_VXX |  |  |
| Dependency | AVC_OD_CALCPRICECWEIGHT_VXX | HL: Procedure Pricing |  |
| Dependency | AVC_OD_CALCFORKLEN_VXX | LL: Determine Fork Length |  |
| Dependency | AVC_OD_CALCCWEIGH_VXX | LL: Calc Counterweight Qty |  |
| Dependency | AVC_OD_CTIREONLY_VXX | LL: Cushion Tire |  |
| Dependency | AVC_OD_PTIREONLY_VXX | LL: Pneumatic Tire |  |
| Dependency | AVC_OD_COMBONLY_VXX | LL: Combustion Power Source |  |
| Dependency | AVC_OD_ELECONLY_VXX | LL: Electrical Power Source |  |
| Dependency | AVC_OD_CNSTRNET_VXX | HL: Constraint Net |  |
| Dependency | AVC_OD_RESTRICTMODEL_VXX | HL: Constraint Common Restrict |  |
| Dependency | AVC_OD_DEFPSOURCE_VXX | HL: Procedure Default Value |  |
| Dependency | AVC_OD_VALFORLFORK_VXX | HL: Only Large Fork |  |
| Dependency | AVC_OD_CSTICFORELEC_VXX | HL: Show for Electrical Lifter |  |
| Dependency | AVC_OD_HDSEAT_VXX | HL: Heavy Duty Seat |  |
| Super BOM | CM-MLFL-KM-VXX |  |  |
| BOM Item | SF-FL-COMB |  |  |
| BOM Item | SF-FL-ELECTRIC |  |  |
| BOM Item | SF-FL-TIRE-PNEU |  |  |
| BOM Item | SF-FL-TIRE-CUSH |  |  |
| BOM Item | SF-FL-CWEIGHT |  |  |
| BOM Item | AVC_CL_FORK_VXX |  |  |
| BOM Item | SF-FL-FORKSEAT-VXX |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 3: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS |

### Preliminary Steps

#### Assign Routing for CM-FL-V01

Purpose

In this process step, you assign routing for the configurable material.

This step has to be executed only once for material CM-FL-V01.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). | The Change Routing Initial |  |
| 3 | Enter the data on the initial screen | On the Change Routing Initial screen, make the following entries and choose Continue:Material: CM-MLFL-KM-VXXPlant:3310 | The Change Routing: Header Details screen displays. |  |
| 4 | Enter the data on the header details screen | In the menu bar, choose Routing. The Change Routing: Overview screen will display. Choose Assignment from Routing option drop down.GrC: 1Material: CM-FL-V01Plant:3310Choose Continue. | The Material Assignment screen displays. |  |
| 5 | Save the routing | Choose Save: | The routing is created. |  |

#### Assign Dependency to Operation and Sequence in Routing

Purpose

For configurable routing, you must assign dependencies to operations and sequence so that routing is variable according to configuration of the material.

You must execute this step once only.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the app | Open Change Routing (CA02). | The Change Routing: Initial Screen screen displays. |  |
| 3 | Enter the plant and the material name | Make the following entries, and choose Continue:Material: CM-FL-V01Plant:3310Group: 43310039 |  |  |
| 4 | Create Parallel Sequence 1 | Choose More > Sequences .Choose New entries.On the Choose Sequence Category dialog box, select Parallel Sequence and choose Continue.Make the following entries:Sequence: 1Description: Parallel Seq for ElecBranch Operation: 0010Return Operation: 0010Choose Operation and make the following entries:Operation: 0011Work center: ASSEMBLEControl Key: YBP1Description: Preparation of electrical enginePress Enter.Choose the Back icon. |  |  |
| 5 | Assign dependency to Sequence 1 | Choose More > Extras > Object Dependencies > Assignments .Enter the following dependency:Dep.: AVC_OD_ELECONLY_VXXChoose Back. | The dependency is assigned to the sequence. |  |
| 6 | Assign dependencies to operation | In the Operation Overview table, select the check box for the operation 0010.Choose More > Extras > Object Dependencies > Assignments .Enter the following dependency:Dep.: AVC_OD_CALCCLABOR_VXXChoose Back.Repeat the steps 1 to 4 for the following:Operation 0031 and Dep.: AVC_OD_COMBONLY_VXXOperation 0032 and Dep.: AVC_OD_ELECONLY_VXX | The dependencies are assigned to the operation. |  |
| 7 | Save the routing | Choose Save. | The routing is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Characteristic](#unique_9) [page ] 15 | Product Configuration Modeler | Manage Characteristics (CT04) | Characteristic is created. |
| [Create Class – Class type 300: Variants](#unique_10) [page ] 16 | Product Configuration Modeler | Manage Classes (CL02) | Class is created. |
| [Assign Class to Product](#unique_11) [page ] 18 | Master Data Specialist - Product Data | Manage Product Master Data (F1602) | Class is assigned to the product. |
| [Create Variant Table](#unique_12) [page ] 19 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Variant table is created. |
| [Create Variant Table Content](#unique_13) [page ] 20 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Variant table content is created. |
| [Create Configuration Profile](#unique_14) [page ] 22 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Configuration profile is created. |
| [Change Configuration Profile to Assign Characteristic Group](#unique_15) [page ] 23 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Characteristic group is created and assigned to the configuration profile. |
| [Create Constraint Net](#unique_16) [page ] 26 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Constraint net is created. |
| [Create and Assign High-Level Dependencies](#unique_17) | Product Configuration Modeler | VC Modeling Environment (PMEVC) | High-level dependencies are created and assigned to respective objects. |
| [Create Super BOM](#unique_18) [page ] 34 | Production Engineer - Discrete Manufacturing | Maintain Bill Of Material - Create, change & display BOMs (F1813) | Super BOM is created. |
| [Simulate Single-Level Configurable BOM](#unique_19) [page ] 37 | Production Engineer - Discrete Manufacturing | Simulate Configuration Models (F2570) | Single-level configurable BOM is simulated with the variant data. |
| [(Optional) Replicate Configuration Model to SAP Business Technology Platform](#unique_20) [page ] 40 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Knowledge base is created and replicated to SAP Business Technology Platform. |
| [(Optional) Simulate Multi-Level Configurable BOM](#unique_21) [page ] 42 | Production Engineer - Discrete Manufacturing | Simulate Configuration Models (F2570) | Multi-level configurable BOM is simulated with the variant data. |
| [Simulate Configurable Routing](#unique_22) [page ] 43 | Production Engineer - Discrete Manufacturing | Simulate Configuration Models (F2570) | Routing of configurable BOM is simulated with the variant data. |
| [(Optional) Analyze Configurable BOM Simulation](#unique_23) [page ] 45 | Production Engineer - Discrete Manufacturing | Simulate Configuration Models (F2570) | Trace messages are analyzed for the configurable BOM simulation. |
| [Without Requirement Driven Development](#unique_24) | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Configurable BOM is simulated with the variant data. |
| [(Optional) Replicate Modeling Changes to SAP Business Technology Platform](#unique_25) [page ] 50 | Product Configuration Modeler | VC Modeling Environment (PMEVC) | Knowledge base is updated and replicated to SAP Business Technology Platform (SAP BTP). |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Configurable BOM

#### Create Characteristic

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a characteristic.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Characteristics (CT04) app. | The Characteristics screen displays. |  |
| 3 | Enter the characteristic name | Make the following entry, and choose the Create icon.Characteristic: AVC_CR_BCAPACITY_V01NoteThe value in the Valid from field is auto-populated.If the characteristic AVC_CR_BCAPACITY_V01 already exists, then create the characteristic AVC_CR_BCAPACITY_Vnn, where nn is the running number. | The Create Characteristic screen displays. |  |
| 4 | Enter basic data | On the Basic data tab, make the following entries.Basic data section:Description: Battery CapacityStatus: Released (default)Format section:Data Type: Numeric FormatNumber of Chars: 4Decimal Places: 0Value assignment section:Select the Single-value radio button.Select the Restrictable checkbox. |  |  |
| 5 | Enter the values | On the Values tab, in the Allowed Values section, make the following entries.Char. Value:5080140 |  |  |
| 6 | Save the characteristic | Choose Save. | The characteristic is created. |  |

#### Create Class – Class type 300: Variants

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a class with the class type - 300.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Classes (CL02) app. | The Class screen displays. |  |
| 3 | Enter the class name | Make the following entries, and choose the Create icon.Class: AVC_CL_ELECADD_V01Class Type: 300NoteThe value in the Valid from field is auto-populated.If the class AVC_CL_ELECADD_V01 already exists, then create the class AVC_CL_ELECADD_Vnn, where nn is the running number. | The Create Class screen displays. |  |
| 4 | Enter basic data | On the Basic data tab, make the following entries.Basic data section:Description: Add Cstics for electrical forklifterStatus: Released (Default)Same classification section:Select the Do not check radio button. (Default)Note If you use the same classification, then you can choose the way of checking (warning message, error, none). |  |  |
| 5 | Enter char. | On the Char. tab, make the following entry.Char.: AVC_CR_BCAPACITY_V01 |  |  |
| 6 | Save the class | Choose Save. | The class is created. |  |

#### Assign Class to Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you assign class to a product.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Product Master Data (F1602) app. | The Manage Product Master Data screen displays. |  |
| 3 | Search for the product | Make the following entry, and choose Go.Product: CM-FL-V01 | The product is displayed. |  |
| 4 | Open the product details | Select the product. | The Product screen displays. |  |
| 5 | Open the product for editing | Choose Edit. | The object page is now editable. |  |
| 6 | Assign class | On the Classification tab, choose Assign Class and then choose Using this Class type.On the Select: Class dialog box, in the Name field, enter the class that you created in the step Create Class – Class type 300: Variants.Choose Go.Select the item from the search result list. | The class is assigned.Tip To verify, look for the newly assigned class in the Class drop-down list. |  |
| 7 | Evaluate characteristic | Select the characteristic Battery Capacity value help, select all the values, and choose Select. | The selected values are assigned to the characteristic. |  |
| 8 | Save the product | Choose Save. | The product is updated. |  |

#### Create Variant Table

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a variant table.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material: CM-FL-V01Class Type: 300 (Default)Plant: 3310BOM Application:PP01 | The configuration screen displays. |  |
| 4 | Select the material | On the configuration screen, select CM-FL-V01. | The material is selected. |  |
| 5 | Enter the table name | Expand the Environment node.Right-click Variant Tables and choose Create Variant Table.On the Create Variant Table dialog box, make the following entry.Variant Table: AVC_VT_BASECMB_V01Note If the table AVC_VT_BASECMB_V01 already exists, then create the table AVC_VT_BASECMB_Vnn, where nn is the running number.Choose Continue. | The Create Table screen displays and the Basic Data tab is selected. |  |
| 6 | Enter basic data | On the Basic Data tab, make the following entries.Basic Data section:Description: Common Model RestrictionStatus: In Preparation (Default) |  |  |
| 7 | Enter characteristics | On the Characteristics tab, make the following entries.Characteristic:AVC_CR_LIFTERMODEL_VXXAVC_CR_POWERSOURCE_VXXAVC_CR_WHEELTYPE_VXXAVC_CR_COUNTERWEIGHT_VXX |  |  |
| 8 | Save the table | Choose Save. | The variant table is created. |  |

#### Create Variant Table Content

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create variant table content.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler.Note If you are logged on and are currently on the material configuration screen, then skip to the Assign the variant table step. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material CM-FL-V01Class Type: 300Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Select the material | On the configuration screen, select CM-FL-V01. | The material is selected. |  |
| 5 | Assign the variant table | Expand the Environment node.Right-click Variant Tables and choose Add Single Variant Table.On the Add Variant Table dialog box, make the following entry.Variant Table: AVC_VT_BASECMB_V01Choose Continue. | The AVC_VT_ BASECMB_V01 table gets added under the Variant Tables node. |  |
| 6 | Set the table status to Released | Double-click the added table.The Create Table screen displays and the Basic Data tab is selected.Choose the Change icon.The Open Variant Table dialog box displays.Click Continue.Set the Status field to Released.Choose Save. | The status of the table is set to Released and its contents can be edited. |  |
| 7 | Add content to the variant table | Choose the Change icon.The Open Variant Table dialog box displays.Choose Continue.On the Contents tab, use the Insert Row icon and make the entries to modify the table to as follows:AVC_ CR_ LIFTERMODEL_ VXXAVC_ CR_ POWERSOURCE_ VXXAVC_ CR_ WHEELTYPE_ VXXAVC_ CR_ COUNTERWEIGHT_ VXXSTDCOMBC1,000STDCOMBC2,000STDELECC1,000STDELECC2,000HVYCOMBP5,000HVYCOMBC5,000Note If you are unable to view the columns, then scroll right. | The entered rows are appended to the table. |  |
| 8 | Save the table | Choose Save. | Content is added to the variant table. |  |

#### Create Configuration Profile

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a configuration profile.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the Configuration Model Data | On the initial screen, make the following entries, and choose Enter Model.Material CM-FL-V01Class Type: 300 (Default)Plant: 3310BOM Application:PP01 | The configuration screen displays. |  |
| 4 | Create the Configuration Profile | In the Object section, right-click CM-FL-V01 and select Create Configuration Profile.In the Create Configuration Profile dialog box, make the following entry.Configuration Profile: AVC_CP_STANDARDNote If the configuration profile AVC_CP_STANDARD already exists, create the configuration profile AVC_CP_STANDARD_Vnn, where nn is the running number.Choose Continue. | The Configuration Profile screen displays in the right panel and the Basic Data tab is selected. |  |
| 5 | Save the Configuration Profile | Choose Save. | The configuration profile is created. |  |

#### Change Configuration Profile to Assign Characteristic Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create and assign characteristic group to configuration profile.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material: CM-FL-V01Class Type: 300 (Default)Plant: 3310BOM Application:PP01 | The configuration screen displays. |  |
| 4 | Assign characteristic group to profile | In the Object section, expand the root node and double-click the configuration profile AVC_CP_STANDARD node.The Configuration Profile screen displays in the right pane.Select the Characteristic Group tab.Choose Assign Characteristic Groups.Note If a dialog box displays to confirm whether you want to leave the page with unsaved data, choose Ok. | The Configuration Profile screen displays in a new browser tab. |  |
| 5 | Create characteristic group | Choose Edit.Note The Edit button is available only for the first time you create a characteristic group.Choose Create Group. | The Configuration Characteristic Group page displays. |  |
| 6 | Add general information | In the General Information section, make the following entry.Characteristics Group: AVC_CG_TECHNICAL_V01Note If the characteristic group AVC_CG_TECHNICAL_V01 already exists, then create the class AVC_CG_TECHNICAL_Vnn, where nn is the running number. |  |  |
| 7 | Add description | In the Description section, choose Create, and add the following description:Language: ENDescription: Technical |  |  |
| 8 | Add characteristics | In the Characteristics section, choose Assign Characteristic. | The Select: Assign Characteristic dialog box displays. |  |
| 9 | Select and assign characteristics | In the Characteristic field, enter AVC_CR_FORKSIZE_VXX and choose Go.In the search result, select the check box corresponding to the characteristic AVC_CR_FORKSIZE_VXX.Repeat the steps 1 and 2 for the following characteristics.AVC_CR_WHEELTYPE_VXXAVC_CR_BCAPACITY_V01AVC_CR_COUNTERWEIGHT_VXXChoose OK.The Select: Assign Characteristic dialog box closes and the selected characteristics are listed in the Characteristics section.Enter the corresponding sorting orders for the characteristics as listed in the following table.CharacteristicSorting OrderAVC_CR_FORKSIZE_VXX1AVC_CR_WHEELTYPE_VXX2AVC_CR_BCAPACITY_V013AVC_CR_COUNTERWEIGHT_VXX4Choose Create.After choosing create, go back to reach the configuration profile screen for assigning the newly created characteristic group. | The characteristics are assigned to the group.The Configuration Profile screen displays. |  |
| 10 | Assign group to configuration profile | Choose Assign Group. The Select: Assign Characteristic Groups screen appearsIn the Name field, search for AVC_CG_TECHNICAL, and choose Go.Select the item displayed under the Items section, and choose Ok. On the Configuration Profile screen, the selected characteristic is displayed under the Characteristic Groups section.Maintain the sorting order for the characteristic group as 1.Choose Save. | Characteristics group is assigned to the configuration profile. |  |
| 11 | Close the Assign Groups to Profile page | Choose the close button. |  |  |

#### Create Constraint Net

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a constraint net.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material CM-FL-V01Class Type: 300Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Select the configuration profile | On the configuration screen, expand the CM-FL-V01 node.Select AVC_CP_STANDARD. | The configuration profile is selected. |  |
| 5 | Create the constraint net | Right-click AVC_CP_STANDARD and choose Create Dependency > Global (Reusable) .If the Open Configuration Profile dialog box displays, choose Continue.On the Create Dependency on Configuration Profile dialog box, make the following entries:Dependency: AVC_OD_CNSTRNET_V01Dependency Type: Constraint Net (Default)Choose Continue.Note If the dependency AVC_OD_ CNSTRNET_V01 already exists, then create the dependency AVC_OD_ CNSTRNET_Vnn, where nn is the running number. | The Create Constraint Net screen displays and the Basic Data tab is selected. |  |
| 6 | Enter basic data | On the Basic Data tab, make the following entries:Description: HL: Constraint NetProcessing Mode: Advanced Variant ConfigurationStatus: Released |  |  |
| 7 | Save the constraint net | Choose Save. | The constraint net is created. |  |

#### Create and Assign High-Level Dependencies

##### Define Constraint

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you define a constraint assigned to the configuration profile.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material CM-FL-V01Class Type: 300Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Select the constraint net | On the configuration screen, double-click the CM-FL-V01 > AVC_CP_STANDARD > AVC_OD_CNSTRNET_V01 node. | The Create Constraint Net screen displays and the Basic Data tab is selected. |  |
| 5 | Create the constraint | Choose the Change icon.On the Open Dependency dialog box, choose Continue.On the Constraints tab, make the following entry:Constraint: AVC_OD_RESTRICTMODEL_V01Note If the constraint AVC_OD_ RESTRICTMODEL_ V01 already exists, then create the constraint AVC_OD_ RESTRICTMODEL_ Vnn, where nn is the running number.Double-click the constraint entry to open its details. | The Create Constraint screen displays and the Basic Data tab is selected. |  |
| 6 | Enter basic data | On the Basic Data tab, make the following entry.Description: Constraint Common Restr |  |  |
| 7 | Enter the syntax | On the Editor tab, enter the following syntax:Code SyntaxOBJECTS:(300)AVC_CL_COMMON_VXX WHERE MODEL = AVC_CR_LIFTERMODEL_VXX; SOURCE = AVC_CR_POWERSOURCE_VXX; TIRES = AVC_CR_WHEELTYPE_VXX; WEIGHT = AVC_CR_COUNTERWEIGHT_VXX. RESTRICTIONS: TABLE AVC_VT_BASECMB_V01 ( AVC_CR_LIFTERMODEL_VXX = MODEL, AVC_CR_POWERSOURCE_VXX = SOURCE, AVC_CR_WHEELTYPE_VXX = TIRES, AVC_CR_COUNTERWEIGHT_VXX = WEIGHT). INFERENCES: MODEL, SOURCE, TIRES, WEIGHT.Click the Check icon.Note If you get any syntax errors, use the Input Help icon to troubleshoot. Also, delete any extra space and tab characters, as they can cause syntax errors. | The Syntax Check Error-Free message displays. |  |
| 8 | Release the constraint | On the Basic Data tab, set the Status field to Released. |  |  |
| 9 | Save the constraint | Choose Save. | The constraint is saved. |  |

##### Define Procedure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you define a procedure assigned to the configuration profile.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model:Material: CM-FL-V01Class Type: 300Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Select the configuration profile | Select the CM-FL-V01 > AVC_CP_STANDARD node. | The configuration profile is selected. |  |
| 5 | Create the procedure | Right-click AVC_CP_STANDARD and choose Create Dependency > Global (Reusable) .If the Open Configuration Profile dialog box displays, choose Continue.On the Create Dependency on Configuration Profile dialog box, make the following entries:Dependency: AVC_OD_DEFPSOURCE_V01Dependency Type: ProcedureChoose Continue.Note If the dependency AVC_OD_ DEFPSOURCE_V01 already exists, then create the dependency AVC_OD_DEFPSOURCE_Vnn, where nn is the running number. | The Create Dependency screen displays and the Basic Data tab is selected. |  |
| 6 | Enter basic data | On the Basic Data tab, make the following entries:Description: HL: Procedure Default ValueProcessing Mode: Advanced Variant Configuration |  |  |
| 7 | Enter the syntax | On the Editor tab, enter the following syntax:Code Syntax$SELF.AVC_CR_POWERSOURCE_VXX ?= 'COMB' if not specified $SELF.AVC_CR_POWERSOURCE_VXX.Click the Check icon. | The Syntax Check Error-Free message displays. |  |
| 8 | Release the procedure | On the Basic Data tab, set the Status field to Released. |  |  |
| 9 | Save the procedure. | Choose Save. | The procedure is saved. |  |

##### Define Precondition on a Characteristic

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you define a precondition assigned to a characteristic.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material CM-FL-V01Class Type: 300Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Create the precondition | On the configuration screen, expand the CM-FL-V01 node.Expand the 300 AVC_CL_ELECADD_V01 node.Right-click AVC_CR_BCAPACITY_V01 and choose Create Dependency > Global (Reusable) .If the Open Configuration Profile dialog box displays, choose Continue.On the Create Dependency on Characteristic dialog box, make the following entries:Dependency: AVC_OD_CSTICFORELEC_V01Dependency Type: Precondition (Default)Choose Continue.Note If the dependency AVC_OD_CSTICFORELEC_V01 already exists, then create the dependency AVC_OD_CSTICFORELEC_Vnn, where nn is the running number. | The Create Dependency screen displays and the Basic Data tab is selected. |  |
| 5 | Enter basic data | On the Basic Data tab, make the following entry:Description: HL: Show for Electrical LifterProcessing Mode: Advanced Variant Configuration |  |  |
| 6 | Enter the syntax | On the Editor tab, enter the following syntax:Code SyntaxAVC_CR_POWERSOURCE_VXX = 'ELEC'.Click the Check icon. | The Syntax Check Error-Free message displays. |  |
| 7 | Release the precondition | On the Basic Data tab, set the Status field to Released. |  |  |
| 8 | Save the precondition. | Choose Save. | The precondition is saved. |  |

##### Define Precondition on a Characteristic Value

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you define a precondition assigned to a characteristic value.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material CM-FL-V01Class Type: 300Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Create the precondition | On the configuration screen, expand the CM-FL-V01 node.Expand the 300 AVC_CL_ELECADD_V01 node.Expand the AVC_CR_BCAPACITY_V01 node.Right-click 140 and choose Create Dependency > Global (Reusable) .If the Open Configuration Profile dialog box displays, choose Continue.On the Create Dependency on Characteristic Value dialog box, make the following entries:Dependency: AVC_OD_VALFORLFORK_V01Dependency Type: Precondition (Default)Choose Continue.Note If the dependency AVC_OD_VALFORLFORK_V01 already exists, then create the dependency AVC_OD_VALFORLFORK_Vnn, where nn is the running number. | The Create Dependency on Characteristic Value screen displays and the Basic Data tab is selected. |  |
| 5 | Enter basic data | On the Basic Data tab, make the following entry:Description: HL: Only Large ForkProcessing Mode: Advanced Variant Configuration |  |  |
| 6 | Enter the syntax | On the Editor tab, enter the following syntax:Code SyntaxAVC_CR_FORKSIZE_VXX = 'L'.Click the Check icon. | The Syntax Check Error-Free message displays. |  |
| 7 | Release the precondition | On the Basic Data tab, set the Status field to Released. |  |  |
| 8 | Save the precondition. | Choose Save. | The precondition is saved. |  |

#### Create Super BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a super BOM.

|  |
| --- |
| Note A super BOM is also referred to as a configurable BOM. |

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Maintain Bill Of Material - Create, change & display BOMs (F1813) app. | The Maintain Bill of Material screen displays. |  |
| 3 | Create BOM | Choose Create BOM. | The Create BOM dialog box displays. |  |
| 4 | Enter initial data | Make the following entries:Material: CM-FL-V01Plant: 3310BOM Usage: 1Choose Create.Note The value in the Valid From field is auto-populated. | The Maintain Bill of Material screen displays the details of the BOM. |  |
| 5 | Add the SF-FL-COMB stock item | In the Components section.Enter the following component details:Item: 0010Item Category: Stock item (L)Material: SF-FL-COMBComponent quantity: 1Press the Enter key. | The material component is added. |  |
| 6 | Add the SF-FL-ELECTRIC stock item | Enter the following component details:Item: 0010Item Category: Stock item (L)Material: SF-FL-ELECTRICComponent quantity: 1Press the Enter key. | The material component is added. |  |
| 7 | Add the SF-FL-CWEIGHT stock item | Enter the following component details:Item: 0020Item Category: Stock item (L)Material: SF-FL-CWEIGHTComponent quantity: 1Press the Enter key. | The material component is added. |  |
| 8 | Add the SF-FL-TIRE-CUSH stock item | Enter the following component details:Item: 0030Item Category: Stock item (L)Material: SF-FL-TIRE-CUSHComponent quantity: 4Press the Enter key. | The material component is added. |  |
| 9 | Add the SF-FL-TIRE-PNEU stock item | Enter the following component details:Item: 0030Item Category: Stock item (L)Material: SF-FL-TIRE-PNEUComponent quantity: 4Press the Enter key. | The material component is added. |  |
| 10 | Add the AVC_CL_ FORK_VXX class item | Enter the following component details:Item: 0040Item category: Class item (K)Component quantity: 1Unit of Measurement: PCPress the Enter key.Click the newly created component entry and enter the following details:Class Type: 200Class: AVC_CL_FORK_VXXRes. item category: LChoose Apply. | The class component is added. |  |
| 11 | Save the BOM | Choose Create. | The BOM is saved. |  |
| 12 | Edit the BOM | Choose Edit. | The BOM is available to edit. |  |
| 13 | Assign low-level object dependencies to component items | Refer to the table and proceed as follows to assign the respective object dependencies to the component items one-by-one:In the Components section, select the component item.Choose Object Dependencies.On the Assigned Dependencies page, enter the corresponding object dependency in the Dependency field.Choose Save.Close the Assigned Dependencies page.Item numberComponent itemDependency0010SF-FL-COMBAVC_OD_COMBONLY_VXX0010SF-FL- ELECTRICAVC_OD_ELECONLY_VXX0020SF-FL-CWEIGHTAVC_OD_CALCCWEIGH_VXX0030SF-FL-TIRE-CUSHAVC_OD_CTIREONLY_VXX0030SF-FL-TIRE-PNEUAVC_OD_PTIREONLY_VXX0040AVC_CL_FORK_ VXXAVC_OD_CALCFORKLEN_VXX | Assigned Dependencies screen appears. |  |
| 14 | Save the BOM | Choose Save. | The BOM is saved. |  |

#### Simulate Single-Level Configurable BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you simulate single-level BOM configurations.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Simulate Configuration Models (F2570) app. | The Simulation Configuration Models screen displays. |  |
| 3 | Create simulation | Choose Create New Simulation.In the New Simulation dialog box, make the following entries, and choose OK.Product: CM-FL-V01Plant: 3310BOM Application: PP01Simulation Context: SimulationTip If you want to analyze the trace messages, then set the Activate Trace switch to On.Note For details on analyzing the trace messages, see [(Optional) Analyze Configurable BOM Simulation](#unique_23) [page ] 45. | The configurable characteristics and the corresponding value details display in the right pane. |  |
| 4 | Validate the characteristic group | On the Simulate Configurable Models screen, verify whether the characteristics assigned in [Change Configuration Profile to Assign Characteristic Group](#unique_15) [page ] 23 are available. | The characteristics in the characteristic group are available. |  |
| 5 | Validate the default power source (The AVC_OD_ DEFPSOURCE_ V01 dependency) | Note the value in the Default Group > Power Source field. | The default value in the Default Group > Power Source field is Combustion. |  |
| 6 | Validate the battery capacity dependency for the Combustion power source (The AVC_OD_ CSTICFORELEC_ V01 dependency) | Ensure that the Default Group > Power Source field is set to Combustion and that the other fields are either blank or are set to (None). | The Technical > Battery Capacity field is disabled and is hidden. |  |
| 7 | Validate the battery capacity dependency for the Electrical power source (The AVC_OD_ CSTICFORELEC_ V01 dependency) | In the Default Group > Power Source field, select Electrical. | The Technical > Battery Capacity field is enabled and is visible.The Default Group > Lifter Model field is set to Standard and is disabled.The Technical > Wheel Type field is set to Cushion Tire and is disabled. |  |
| 8 | Validate the variant details for the Standard lifter model (The AVC_OD_ RESTRICTMODEL_ V01 dependency) | Set the fields that you changed in the previous step to (None).Set the Default Group > Lifter Model field to Standard. | The drop-down list in the Default Group > Power Source field displays both Combustion and Electrical.The Technical > Wheel Type field is set to Cushion Tire and is disabled.The drop-down list in the Technical > Counterweight field:Displays 1,000 kg and 2,000 kg.Does not display 5,000 kg. |  |
| 9 | Validate the variant details for the Heavy lifter model (The AVC_OD_ RESTRICTMODEL_ V01 dependency) | Set the fields that you changed in the previous step to (None).Set the Default Group > Lifter Model field to Heavy. | The Default Group > Power Source field is set to Combustion and is disabled.The drop-down list in the Technical > Wheel Type field displays both Cushion Tire and Pneumatic Tire.The Technical > Counterweight field is set to 5,000 kg and is disabled. |  |
| 10 | Validate the dependencies for the Large fork size (The AVC_OD_ VALFORLFORK_ V01 dependency) | Validate the dependency for the electrical power source and the normal fork size:Set the fields that you changed in the previous step to (None).Set the Default Group > Power Source field to Electrical and the Technical > Fork Size field to Normal.Validate the dependency for the electrical power source and the battery capacity 140:Set the fields that you changed in the previous step to (None).Set the Default Group > Power Source field to Electrical and the Technical > Battery Capacity field to 140. | If the Default Group > Power Source field is set to Electrical and the Technical > Fork Size field is set to Normal, then the value help list for the Technical > Battery Capacity field:Displays 50 and 80.Does not display 140.If the Default Group > Power Source field is set to Electrical and the Technical > Battery Capacity field is set to 140, then the Technical > Fork Size field shows values Small, Normal, and Large. However, choosing any value other than Large causes an inconsistency in the simulation. |  |
| 11 | Explode BOM | Set the fields that you changed in the previous step to (None).Set the fields as follows:Default Group > Lifter Model : StandardDefault Group > Power Source : ElectricalTechnical > Counterweight : 2,000 kgTechnical > Fork Size : NormalIn the Exploded BOM pane, choose the Re-explode BOM icon. | The Technical > Wheel Type field is set to Cushion Tire and is disabled.The exploded BOM contains the following items:ProductQtySF-FL-ELECTRIC1SF-FL-CWEIGHT2SF-FL-TIRE-CUSH4SF-FL-FORK-M1NoteThe quantity for SF_FL_ CWEIGHT is 2 PC and is determined based on the counterweight of 2,000 kg.The component SF-FL-FORK-M is determined based on the Normal fork size. |  |
| 12 | Explode BOM | Set the fields that you changed in the previous step to (None).Set the fields as follows:Default Group > Lifter Model : HeavyTechnical > Wheel Type : Pneumatic TireTechnical > Fork Size : LargeIn the Exploded BOM pane, choose the Re-explode BOM icon. | The Default Group > Power Source field is set to Combustion and is disabled.The Technical > Counterweight field is set to 5,000 and is disabled.The exploded BOM contains the following items:ProductQtySF-FL-COMB1SF-FL-CWEIGHT5SF-FL-TIRE-PNEU4SF-FL-FORK-L1NoteThe quantity for SF_FL_ CWEIGHT is 5 PC and is determined based on the counterweight of 5,000 kg.The component SF-FL-FORK-L is determined based on the Large fork size. |  |
| 13 | Save the simulation | Choose Save.On the Save Simulation dialog box, choose Save and Exit. | The simulation is saved. |  |

#### (Optional) Replicate Configuration Model to SAP Business Technology Platform

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create knowledge base for a configuration model.

The knowledge base is then replicated on SAP Business Technology Platform (SAP BTP) by activating the communication arrangement SAP_COM_0537.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material: CM-FL-V01Class Type: 300 (Default)Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Enter knowledge base details | In the left pane, under the Object column, right-click the root node and select Create or Assign KB object.On the Create or Assign KB object dialog box, make the following entries:KB Object: KBO-CM-FL-V01Description: Knowledge base for Fork lifterKB Profile: KBP-CM-FL-V01Description: Profile for Fork lifterClass type: 300Choose Continue. | The knowledge base object screen displays. |  |
| 5 | Save the knowledge base object | Choose Save. | The knowledge base object is saved. |  |
| 6 | Create run-time version of the knowledge base | In the left pane, under the Object column, right-click the knowledge base object KBO-CM-FL-V01 node, and choose Create Runtime Version.On the Create Runtime Version dialog box, make the following entry:Version: .01Choose Continue.On the KB object screen, in the Status field, enter 1.Choose the Generate and Save icon.On the Generate and Save Runtime Version dialog box, choose Yes. | The run-time version is created and a confirmation message is displayed. |  |
| 7 | Verify whether the knowledge base object is replicated in SAP Business Technology Platform | Log on to the Administration Cockpit of SAP Variant Configuration and Pricing with the BusinessExpert role.Note For details, see the Administration Guide for SAP Variant Configuration and Pricing manual on SAP Help portal.In the left pane, choose Replication > Configuration .The Configuration Replication page is displayed.In the search box, enter KBO-CM-FL-V01, and choose the Search icon. | The knowledge base object is displayed in the list view. |  |

#### (Optional) Simulate Multi-Level Configurable BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a multi-level configuration, the hierarchy has a configurable material SF-FL-FORKSEAT-VXX as a child of the configurable material CM-MLFL-KM-VXX. To simulate CM-MLFL-KM-VXX, perform the test steps documented in the [Simulate Single-Level Configurable BOM](#unique_19) [page ] 37 test procedure. However, when validating the dependencies, you must use the dependencies with the VXX extension (and not the V01 extension).

In this process step, you simulate the SF-FL-FORKSEAT-VXX in a multi-level BOM configuration and test the behavior of the dependencies that get influenced by CM-MLFL-KM-VXX.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Simulate Configuration Models (F2570) app. | The Simulation Configuration Models screen displays. |  |
| 3 | Create simulation | Choose Create New Simulation.On the New Simulation dialog box, make the following entries, and choose OK.Product: CM-MLFL-KM-VXXPlant: 3310BOM Application: PP01Simulation Context: Simulation | The configurable characteristics and the corresponding value details display in the right pane. |  |
| 4 | Select configurable items view | In the left pane, choose the Select View icon and choose Configurable Items. | Configurable view of material CM-MLFL-KM-VXX is displayed.Note Simulation of CM-MLFL-KM-VXX would be like the Simulate Configurable BOM (CM-FL-V01). However, the dependency validation should be performed with dependencies which has extension VXX instead of dependencies which has extension V01. |  |
| 5 | Validate the seat type dependency for Standard lifter model (The AVC_OD_ HDSEAT_VXX dependency) | Select the product CM-MLFL-KM-VXX.Set Lifter Model to Standard.Select the product SF_FL_FORKSEAT_VXX. | The drop-down list in the Seat Type field displays only Standard seat and Air suspension seat. |  |
| 6 | Validate the seat type dependency for Heavy lifter model (The AVC_OD_ HDSEAT_VXX dependency) | Select the product CM-MLFL-KM-VXX.Set Lifter Model to Heavy.Select the product SF_FL_FORKSEAT_VXX. | The drop-down list in the Seat Type field displays Standard seat, Heavy duty seat, and Air suspension seat. |  |
| 7 | Save the simulation | Choose Save.On the Save Simulation dialog box, choose Save and Exit. | The simulation is saved. |  |

#### Simulate Configurable Routing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you simulate routing configurations.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Simulate Configuration Models (F2570) app. | The Simulation Configuration Models screen displays. |  |
| 3 | Create simulation | Choose Create New Simulation.On the New Simulation dialog box, make the following entries, and choose OK.Product: CM-FL-V01Plant: 3310BOM Application: PP01Simulation Context: SimulationNote You must execute the preliminary step [Assign Routing for CM-FL-V01](#unique_6) [page ] 10 for this step to work. | The configurable characteristics and the corresponding value details display in the right pane. |  |
| 4 | Select routing view | In the left pane, choose the Click to Select icon corresponding to the product CM-FL-V01.Note If the Select Routing dialog box is displayed, select the entry that corresponds to 43310039. | In the left pane, the routing sequence along with the operations is displayed. |  |
| 5 | Validate the operation 0010 – Assembly w/o engine (The AVC_OD_ CALCCLABOR_ VXX dependency) | In the Counter Weight field, select 5000 KG.Choose the Refresh Routing icon.Select the operation 0010 – Assembly w/o engine. | In the Inspector pane, in the Standard Values section, Labor is set to 250.000 MIN. |  |
| 6 | Validate the operation 0031 – Final assembly with combustion engine (The AVC_OD_ COMBONLY_VXX dependency) | In the Power Source field, select Combustion.Choose the Refresh Routing icon. | In the left pane, under the routing view, only the following operations are displayed.0010 Assembly w/o engine.0031 Final assembly with combustion engine. |  |
| 7 | Validate the operations 0011 – Parallel Seq for Elec and 0032 – Final Assembly with electrical engine (The AVC_OD_ ELECONLY_VXX dependency) | In the Power Source field, select Electrical.Choose the Refresh Routing icon. | In the left pane, under the routing view, only the following operations are displayed.→Parallel Seq for Elec0010 Assembly w/o engine.←Parallel Seq for Elec.0032 Final Assembly with electrical engine.NoteIf you choose the parallel sequence Parallel Seq for Elec, the operation 0011 Preparation of electrical engine is displayed.To view the sequence again, choose ←0010 Assembly w/o engine. |  |
| 8 | Save the simulation | Choose Save.On the Save Simulation dialog box, choose Save and Exit. | The simulation is saved. |  |

#### (Optional) Analyze Configurable BOM Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you analyze trace messages for the configurable BOM simulation.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Simulate Configuration Models (F2570) app. | The Simulation Configuration Models screen displays. |  |
| 3 | Open the simulation | Make the following entries, and choose Go:Type: SimulationProduct: CM-FL-V01Plant: 3310In the search results, select the simulation. | The configurable characteristics of the BOM display on the screen. |  |
| 4 | Filter by high-level trace messages | In the right pane, choose Trace.Tip If the right pane is not present, choose the Toggle Inspector icon.Choose the filter icon.In the Trace Filter dialog box, make the following entry:Trace Level: High-Level ConfigurationChoose Go. | Only high-level trace messages are displayed. |  |
| 5 | Filter by the message type Value Assignment | Choose the filter icon.In the Trace Filter dialog box, make the following entry:Message Type: Value AssignmentChoose Go. | Only value assignment trace messages are displayed. |  |
| 6 | Remove the filters | Choose the filter icon.In the Trace Filter dialog box, choose Reset.Choose Go. | All trace messages are displayed. |  |
| 7 | Filter by a characteristic | In the trace message section, choose a characteristic.Example AVC_CR_POWERSOURCE_VXXFrom the actions, choose to filter by the characteristic.Example Filter Trace by Characteristic AVC_CR_POWERSOURCE_VXX | Trace messages related to the selected characteristic only are displayed. |  |
| 8 | Inspect a characteristic | In the trace message section, choose a characteristic.Example AVC_CR_POWERSOURCE_VXXFrom the actions, choose to inspect the characteristic.Example Inspect Characteristic AVC_CR_POWERSOURCE_VXX | The properties of the selected characteristic are displayed. |  |
| 9 | Remove the filters | In the right pane, choose Trace.On the filter bar, choose the x icon to reset the filters. | All trace messages are displayed. |  |
| 10 | Filter by low-level trace messages | In the right pane, choose Trace.Choose the filter icon.In the Trace Filter dialog box, make the following entry:Trace Level: Low-Level ConfigurationChoose Go. | Only low-level trace messages are displayed. |  |
| 11 | Filter by a BOM item | In the trace message section, choose a BOM item.Example SF-FL-COMBFrom the actions, choose to filter by the BOM item.Example Filter Trace by Characteristic SF-FL-COMB | Trace messages related to the selected BOM item only are displayed. |  |
| 12 | Filter by a dependency | In the trace message section, choose a dependency.Example AVC_OD_COMBONLY_VXXFrom the actions, choose to filter by the dependency.Example Filter Trace by Dependency AVC_OD_COMBONLY_VXX | Trace messages related to the selected dependency only are displayed. |  |
| 13 | Inspect a dependency | In the trace message section, choose a dependency.Example AVC_OD_COMBONLY_VXXFrom the actions, choose to inspect the dependency.Example Inspect Dependency AVC_OD_COMBONLY_VXX | The properties of the selected dependency are displayed. |  |
| 14 | Remove the filters | In the right pane, choose Trace.On the filter bar, choose the x icon to reset the filters. | All trace messages are displayed. |  |

### Maintain Configurable BOM

#### Without Requirement Driven Development

##### Create High-Level Dependency and Simulate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you change a procedure assigned to the configuration profile.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Simulate Configuration Models (F2570) app. | The Simulation Configuration Models screen displays. |  |
| 3 | Create simulation | Choose Create New Simulation.On the New Simulation dialog box, make the following entries, and choose OK.Product: CM-FL-V01Plant: 3310BOM Application: PP01Tip If you want to analyze the trace messages, then set the Activate Trace switch to On.For details on analyzing the trace messages, see [(Optional) Analyze Configurable BOM Simulation](#unique_23) [page ] 45. | The configurable characteristics and the corresponding value details display in the right pane. |  |
| 3 | Open the variant configuration modeling environment | Choose Open VC Modeling Env. | The configuration screen displays in a new window or a new tab depending on your browser settings. |  |
| 4 | Select the configuration profile | On the configuration screen, expand the CM-FL-V01 node.Select AVC_CP_STANDARD. |  |  |
| 5 | Create the procedure | Expand the CM-FL-V01 node.Right-click AVC_CP_STANDARD and choose Create Dependency > Global (Reusable) .If the Open Configuration Profile dialog box displays, choose Continue.On the Create Dependency on Configuration Profile dialog box, make the following entries:Dependency: AVC_OD_DEFWTYPE_V00Dependency Type: ProcedureTip If the dependency AVC_OD_DEFWTYPE_V00already exists, then create the dependency AVC_OD_DEFWTYPE_Vnn, where nn is the running number.Choose Continue. | The Create Dependency screen displays and the Basic Data tab is selected. |  |
| 6 | Enter basic data | On the Basic Data tab, make the following entry:Description: HL: Procedure Default Value2Processing Mode: Advanced Variant Configuration |  |  |
| 7 | Enter the syntax | On the Editor tab, enter the following syntax:Code Syntax$SELF.AVC_CR_WHEELTYPE_VXX ?= 'P'.Choose the Check icon. | The Syntax Check Error-Free message displays. |  |
| 8 | Save the procedure | On the Basic Data tab, set the Status field to Released.Choose Save. | The procedure is saved. |  |
| 9 | Reload the variant model | Return to the screen that was displayed in the Create simulation test step.Choose the Reload Configuration Model icon. | The configurable characteristics and the corresponding value details of the model are reloaded. |  |
| 10 | Validate the default wheel type (The AVC_OD_ DEFWTYPE_V00 dependency) | Note the value in the Wheel Type field. | The default value in the Wheel Type field is Pneumatic Tire. |  |
| 11 | Save the simulation | Choose Save.On the Save Simulation dialog box, choose Save and Exit. | The simulation is saved. |  |

##### (Optional) Replicate Modeling Changes to SAP Business Technology Platform

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the change is an enhancement to the existing configuration model and should become active in a future release, then you must generate a new run-time version of the knowledge base object for a configuration model.

In this process step, you generate a new run-time version of the knowledge base object for a configuration model.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material: CM-FL-V01Class Type: 300 (Default)Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Create the new run-time version of the knowledge base object | In the left pane, under the Object column, right-click the knowledge base object KBO-CM-FL-V01 node, and choose Create Runtime Version.On the Create Runtime Version dialog box, make the following entry:Version: .02Choose Continue.On the KB object screen, in the Status field, enter 1.In the Valid From field, enter <current date> + 1 (the date on the next day).Choose the Generate and Save icon.On the Generate and Save Runtime Version dialog box, choose Yes.Note If the change is not an enhancement and should become active in the current release, then:In the left pane, under the Object column, expand the knowledge base object KBO-CM-FL-V01 node, and double-click the .01 sub-node.On the KB object screen, choose the Change icon.Choose the Generate and Save icon.On the Generate and Save Runtime Version dialog box, choose Yes. | A new version of the knowledge base object is created and a confirmation message is displayed. |  |
| 5 | Verify whether the updated knowledge base object is replicated in SAP Business Technology Platform | Log on to the Administration Cockpit of SAP Variant Configuration and Pricing with the BusinessExpert role.Note For details, see the Administration Guide for SAP Variant Configuration and Pricing manual on SAP Help portal.In the left pane, choose Replication > Configuration .The Configuration Replication page is displayed.In the search box, enter KBO-CM-FL-V01, and choose the Search icon.The knowledge base object is displayed in the list view.Verify the value in the Build column. | If the list view, a new entry for the knowledge base object KBO-CM-FL-V01 is added with the Build value 1. |  |

### (Optional) Create Sales Set

The configuration modeler can also be used to define a configuration model for the Sales set functionality. For that, you must configure a few settings differently. The following list is a compilation of the key points that you must take care of.

- Configuration Profile

On the Basic Data tab:

-
    - In the Process section, select SALES Order (SET).
    - In the BOM Explosion section, in the Application field, select SD01 Sales and Distribution.
- Bill of Material
    - BOM Usage: 5 (Sales and Distribution)
    - For all the items created under the BOM, on the Status/Long Text tab, select the Relevant to sales field.
- Item Category Group
    - In the General Item Category Group field:
        - For Sales Set Header material, enter 0004
        - For non-KMAT material, enter NORM
        - For KMAT material, enter 0002

For more information see the Make-to-Order Production for Sales Kits with Variant Configuration (4OC) test script.

### (Optional) Additional Manual Configuration for Replicate Configurable Models using Product Data Replication (PDR)

If you want to replicate the configurable models using Product Data Replication(PDR), you must complete the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, refer to the following document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/be57e04d7a01ab017b28e5b09a7c5d06)

#### (Optional) Product Data Replication (PDR)

Production Data Replication is a method that allows to fully distribute Product Configuration Models between systems through a systematic identification and packaging of all objects of a product configuration model with versions. PDR provides a complete monitoring and transparency of overall replication process, hence allows the users to have complete control on the same

Business Benefits

Cost Savings

Targeted registering of systems and users for products allows targeted replication of products and the objects belonging to them in the target systems. Each user or system receives only the product information that is really required. This avoids both redundant data maintenance and a piling up of unneeded data in target systems, which reduces the administrative overhead.

Increased Data Quality

Targeted replication for registered systems and users reduces data redundancy and thereby the maintenance effort, by enabling the reuse of parts. Targeted registering also ensures that each user or system can rely on getting the data required. The continuity of business processes across system boundaries is also ensured.

The targeted choice of the replication time and packet set-up with the checking mechanisms involved ensure consistent, correct, and complete data.

The time of data transfer can be determined individually in the target system. This ensures that ongoing business processes (such as planning and production) are not hampered.

Improved Transparency and Monitoring

The logging of replication in source and target systems provides transparency and therefore monitoring functionality. The history of replicated data can be traced.

##### (Optional) Configure PDR Using SSCUIs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can customize packet types and also enable auto approval using the following SSCUI as per your requirement.

|  |
| --- |
| Note The packet types should be same in both the source and destination systems. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to ALE Distribution Units: Packet Types | Choose the link Configure your solution.Make the following entriesApplication Area: R&D/EngineeringSub Application Area: Project Control and Product DevelopmentSelect the line items with item name Define Configurations related to Product Development | The ALE Distribution Units: Packet Types app is displayed. |  |
| 4 | Create a Packet Type | Select the Self Service Configurations (SSCUIs) listed below.Tip We recommend that you refer to the template content provided for packet type “SAP_REPLI” and copy the same to create a new packet type.SSCUI Title: ALE Distribution Units: Packet TypesDescription: Defines different packet types depending on requirement.SSCUI Title: 180035Select each item and choose Configure. | PacketType is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 2 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 3 | Open ALE Distribution Units: Packet Types . | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: ALE Distribution Units: Packet Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as aConfiguration Expert - Business Process Configuration. | The ALE Distribution Units: Packet Types screen is displayed. |  |

##### (Optional) Replicate Configurable Models using Product Data Replication (PDR)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Refer the section [(Optional) Additional Manual Configuration for Replicate Configurable Models using Product Data Replication (PDR)](#unique_31) [page ] 52

Purpose

In this process step, you can replicate objects from a source system to a target system using Product Data Replication (PDR).

You can post the already replicated objects from source system to target system using PDR. It is presumed that the link between source and target system is already established.

Packet type name and managed objects for the package type should be same in the sender and receiver system. The prerequisite is that first the package is sent and then received in the cloud environment .

Refer the SAP Note [1103146](https://me.sap.com/notes/1103146) for the configuration required at the sender side.

For more information, refer to the following document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/be57e04d7a01ab017b28e5b09a7c5d06)

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Product Configuration Modeler. |  |  |
| 2 | Access the App (optional) | Open the UPS Distribution Unit: Post IDocs (UPSMAS) app.Remember Open this app only if the UPSMAS IDOC is not posted in your cloud system and you need to repost the IDoc. | The ALE Distribution Unit: PostDSPMAS Idocs Again screen is displayed. |  |
| 3 | Post the IDocs (Optional) | Select the required UPS Name for immediate post. | The IDOCS (Intermediate Documents)gets posted. |  |
| 4 | Access the App | Open the UPS Distribution Cockpit: Maintain Units (UPS) app. | The UPS Distribution Cockpit selection screen is displayed. |  |
| 5 | View Distribution Packet Name | Enter Distribution Packet name. Choose Execute. | The selected Display UPS Distribution Unit screen is displayed. |  |
| 6 | Change UPS Distribution Packet | Choose Display/Change to enable change mode | The Display/Change UPS Distribution Unit screen is displayed. |  |
| 7 | Set Status | The status of the Unit will be Received. Choose the Status field and depending on the requirement, select Approve Packet or Reject Packet which will accordingly change the status to Approved or Rejected.Note If the auto approval from SSCUI is configured in the section [(Optional) Configure PDR Using SSCUIs](#unique_33) [page ] 53, the status will automatically change to Approved first and then changes to either Posted or Incomplete. In SAP S/4HANA Cloud Public Edition, the auto posting flag is always switched on in the customizing of packet types and cannot be changed. In that case, step 7 and 8 can be skipped by the user. | The Change UPS Distribution Unit screen is displayed and the status of the packet changes to Approved or Rejected. |  |
| 8 | Change Status | If the status does not change to Approve/Rejected , repeat Set Status as required for the required changes to reflect. | Status changes to Approve/Rejected. |  |
| 9 | Check Log | In case of an error for any entry under Object List, select that entry and choose Display Log button below to view Log.Note Upon choosing Display Log, the messages will be displayed only if :The object IDOCs are already posted by the Application Interface Framework(AIF) .The auto approval from SSCUI is enabled; the package is posted by the background job and an outcome(success or error) is available. | Details of the execution is displayed as log. |  |
| 10 | Check IDOCS (optional) | In case of an error for any entry under Object List, select that entry and choose Display iDocs button below to view iDoc status. If you are unable to navigate, refer the SAP Note [3064518](https://me.sap.com/notes/3064518) for AIF and object navigations. | The Message Dashboard screen is displayed. |  |
| 11 | Check Detail View (Optional) | In case of an error for any entry under Object List, select that entry and choose Display Detail View button below to view Detail View Log. If you are unable to navigate to Object Application, refer the SAP Note [3064518](https://me.sap.com/notes/3064518) for AIF and object navigations. | The application related to the object in the object list is opened. |  |
| 12 | Save UPS Distribution Packet | In case of no errors across all the entries , choose Save. | The UPS Distribution Cockpit : Packet is posted. |  |
| 13 | Update UPS Distribution Package | Once the status of the packet changes to Approved or Rejected, choose Update.Status changes to Posted or Updated upon successful posting.Status changes to Errors found or Posting Incomplete upon unsuccessful posting.This might take some time depending on the objects being replicated. | The Display UPS Distribution Unit screen is displayed. |  |
| 14 | Trigger Repost | When the posting is unsuccessful, the status of the packet changes to Errors found or Posting Incomplete.Check the Application Log or IDoc Messages for any errors and correct these errors.Repost the packet in the change mode.Repeat the previous step (step 13- Update UPS Distribution Package) to check the status again. | The UPS Distribution Cockpit : Packet is posted and the Display UPS Distribution Unit screen is displayed. |  |
| 15 | UPS Distribution Package Updated | Once the posting is successful, the status changes to Posted and Updated.The replicated objects in the Object ID column of Object List will now be available in the target system. | The Display UPS Distribution Unit screen is displayed. |  |

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
> Flagged while digesting this document, not verified: Preliminary step 'Assign Routing for CM-FL-V01' enters Material CM-MLFL-KM-VXX on the Change Routing initial screen, while its purpose and later steps concern CM-FL-V01; the material may be mismatched.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]
- related-to :: [[02-business-partner-and-product-master-data/crear-grupo-de-aplicaciones-y-visualizacion-de-caracteristicas-mds-2ni]]
- related-to :: [[02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-configurable-material]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22T_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 91,596 chars in the whole document
