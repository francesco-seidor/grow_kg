---
id: 13-quality-ehs-and-compliance/substance-volume-tracking-4ol-ae-test-script-sap-s-4hana-cloud-public
title: "Substance Volume Tracking (4OL_AE) - Test Script, SAP S/4HANA Cloud Public Edition (4OL_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 4OL_AE: prerequisites and test steps for substance volume tracking across purchasing, manufacturing and sales."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/chemical-compliance-and-marketability]
aliases: [4OL_S4CLD2608_BPD_EN_AE]
keywords: [Chemical Compliance and Product Marketability, substance volume tracking, import responsibility, compliance requirements, legal entity mappings, included movement types, basic compliance data, monitor substance volumes, purchasing process, process manufacturing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4OL_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1040
topic: 13-quality-ehs-and-compliance/chemical-compliance-and-marketability
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Substance Volume Tracking (4OL_AE) - Test Script, SAP S/4HANA Cloud Public Edition (4OL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4OL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Chemical Compliance and Product Marketability** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Substance Volume Tracking (4OL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855423)

[2 Prerequisites 4](#_Toc232855424)

[2.1 System Access 4](#_Toc232855425)

[2.2 Roles 4](#_Toc232855426)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232855427)

[2.4 Business Conditions 8](#_Toc232855428)

[2.5 Preliminary Steps 9](#_Toc232855429)

[2.5.1 Open a New Materials Management (MM) Period 9](#_Toc232855430)

[2.5.2 Specify Included Movement Types 9](#_Toc232855431)

[2.5.3 Create Legal Entity Mappings 11](#_Toc232855432)

[2.5.4 Create a Purchasing Info Record 13](#_Toc232855433)

[2.5.5 Create Basic Compliance Data for Raw Materials 15](#_Toc232855434)

[2.5.6 Approve Suppliers of Raw Materials 17](#_Toc232855435)

[2.5.7 Create Basic Compliance Data for Unpackaged Product 18](#_Toc232855436)

[2.5.8 Enable Substance Volume Tracking for Compliance Requirements 21](#_Toc232855437)

[2.5.9 Set Initial Stock for Material 21](#_Toc232855438)

[3 Overview Table 23](#_Toc232855439)

[4 Test Procedures 25](#_Toc232855440)

[4.1 Purchasing Process 25](#_Toc232855441)

[4.1.1 Create a Purchase Requisition 25](#_Toc232855442)

[4.1.2 Convert a Purchase Requisition to a Purchase Order 27](#_Toc232855443)

[4.1.3 Post Goods Receipt for a Purchase Order 28](#_Toc232855444)

[4.1.4 Analyze Stock Overview (Optional) 29](#_Toc232855445)

[4.2 Manufacturing Process Based on a Process Order 30](#_Toc232855446)

[4.2.1 Create a Process Order 30](#_Toc232855447)

[4.2.2 Manual Goods Issue (Optional) 32](#_Toc232855448)

[4.2.3 Confirm a Process Order 32](#_Toc232855449)

[4.2.4 Post Goods Receipt for a Process Order 33](#_Toc232855450)

[4.3 Sales Process Based on a Sales Order 35](#_Toc232855451)

[4.3.1 Create a Sales Order 35](#_Toc232855452)

[4.3.2 Add a Market Assessment 36](#_Toc232855453)

[4.3.3 Create a Delivery 37](#_Toc232855454)

[4.3.4 Post Goods Issue for an Outbound Delivery 38](#_Toc232855455)

[4.4 Substance Volume Tracking 40](#_Toc232855456)

[4.4.1 Monitor Substance Volumes 40](#_Toc232855457)

[5 Appendix 44](#_Toc232855458)

[5.1 Conditional Procedures 44](#_Toc232855459)

[5.1.1 Apply Regulations to Countries/Regions 44](#_Toc232855460)

[5.1.2 Classify a Packaged Product as No Dangerous Good 45](#_Toc232855461)

[5.2 Error Handling 47](#_Toc232855462)

[5.2.1 Export Logs of Failed Tasks (Optional) 47](#_Toc232855463)

[5.2.2 Process Again Failed Tasks (Optional) 48](#_Toc232855464)

## Purpose

Overview

With this scope item, you can enable tracking of confirmed substance volumes from purchasing, manufacturing, and sales. Substance volume tracking helps you comply with chemical regulations. These regulations require you to track and monitor the volumes of regulated substances that you import to, produce in, or export to a country or region within a certain period. Substance volume tracking is integrated with the logistics processes for purchasing, manufacturing, and sales and tracks, calculates, aggregates, and monitors the imported, produced, and exported substance volumes that result from the processes, considering the system configuration.

Further Information on the Test Procedure

Business processes for purchasing and sales and delivery may lead to an import of substances into a country or region for which a substance-volume-tracking-relevant regulation exists. In these cases, the system checks certain criteria to determine if the buyer or seller is responsible for the import.

Substance volume tracking is performed only for the legal entity that is responsible for the import. For a purchasing processes initiated by the buyer that is responsible for the import, substance volume tracking is carried out only for the legal entity of the buyer. For sales and delivery processes initiated by the seller that is responsible for the import, substance volume tracking is carried out only for the legal entity of the seller.

In the standard purchasing process, the buyer is defined as the default party responsible for the import. If the system does not find any criteria, such as a specific import responsibility setting at the supplier material level, that overrides this default, standard purchase orders that result in an import are tracked for the legal entity of the receiving company or plant as a buyer, and in accordance with the applicable regulations of the target country or region.

In the standard sales and delivery process, the buyer is defined as the default party responsible for the import. If the system does not find any criteria that overrides this default, standard sales orders and deliveries that result in an import into the country or region of the buyer are not tracked for the legal entity of the selling or delivering company or plant as the seller, nor under the applicable regulations of the target country or region.

The purpose of the Purchasing Process test procedure is to demonstrate that the system does perform a substance volume tracking.

The purpose of the Sales Process Based on a Sales Order test procedure is to demonstrate that the system does not perform a substance volume tracking.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Master Data Specialist - Product Compliance | SAP_BR_MD_SPECIALIST_PCL | Master Data - Product Compliance | SAP_BR_MD_SPECIALIST_PCL |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Dangerous Goods Specialist - Product Compliance | SAP_BR_DG_SPLST_PCL | Dangerous Goods | SAP_BR_DG_SPLST_PCL |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Storage location for sales. |
| Storage Location | 331B | Std. storage 2 | Storage location for production. |
| Storage Location | 331C | Raw mat. stoloc. | Storage location for raw materials. |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001/002 | Group 001/Group 002 | Depending on the material. |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Supplier | 33300050 | Foreign Supplier AE 50 (CA) |  |
| Supplier | 33300051 | Foreign Supplier AE 51 (DE) |  |
| Customer | 33100050 | Foreign Customer 50 (DE) |  |
| Material | RMPC07 | Raw PMA 07 | Type ROH, compliance relevant |
| Material | RMPC08 | Raw PMA 08 | Type ROH, compliance relevant |
| Material | SGPCSVT01 | Semi SVT 01 | Type HALB, compliance relevant |
| Material | FGPCSVT01 | Finished SVT 01 | Type FERT, compliance relevant |

Bill of Materials Structure

This overview shows the bill of materials structure and the usage of each component.

| Material | Level | Material Type | Unit | Characteristic of material |
| --- | --- | --- | --- | --- |
| SGPCSVT01 | 0 | HALB | KG | Semifinished product, no batch |
| RMPC07 | 1 | ROH | KG | Raw material, no batch, externally procured |
| RMPC08 | 1 | ROH | KG | Raw material, no batch, externally procured |

Listed Substances

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Listed Substance | L00000002329 | CAS Number: 64-19-7Name: acetic acid | Included in the listed substance index that is delivered with the software. |
| Listed Substance | L00000007041 | CAS Number: 123-51-3Name: isoamyl alcohol | Included in the listed substance index that is delivered with the software. |
| Listed Substance | L00000007079 | CAS Number: 123-92-2Name: isoamyl acetate | Included in the listed substance index that is delivered with the software. |

Sample Compliance Requirements

The following sample compliance requirements are considered exemplary.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Compliance Requirement Version | AE SVT 2020 June - Best Practice Content – Initial Version | Compliance Requirement: AE SVT 2020 June - BPCCountry: AEThreshold: 500 tListed Substances:acetic acidisoamyl alcoholisoamyl acetate | The following default values are fixed and cannot be changed when creating a new version:Tracking Period: January 1 - December 31Scenarios: Import To, Produce In, Export ToAggregate by: Legal Entity |
| Compliance Requirement Version | DE SVT 2020 June - Best Practice Content – Initial Version | Compliance Requirement: DE SVT 2020 June - BPCCountry: DEThreshold: 500 tListed Substances:acetic acidisoamyl alcoholisoamyl acetate | The following default values are fixed and cannot be changed when creating a new version:Tracking Period: January 1 - December 31Scenarios: Import To, Produce In, Export ToAggregate by: Legal Entity |

Company Substances

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Substance | acetic acid | Linked to listed substance: L00000002329 | Acetic acid |
| Company Substance | isoamyl alcohol | Linked to listed substance: L00000007041 | Isopentanol |
| Company Substance | isoamyl acetate | Linked to listed substance: L00000007079 | iso-Pentylacetat |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| 3X8 | Create Resource - MDS |
| 3X9 | Create Master Recipe - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting period is up to date. |
| J45 - Procurement of Direct Materials | The scope item of this document is extending the Procurement of Direct Materials scope item. Therefore, the scope item Procurement of Direct Materials must be implemented and tested before testing the Purchasing scenario of scope item Substance Volume Tracking. |
| BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order | The scope item of this document is extending the Make-to-Stock – Process Manufacturing Based on Process Order scope item. Therefore, the scope item Make-to-Stock – Process Manufacturing Based on Process Order must be implemented and tested before testing the Manufacturing scenario of scope item Substance Volume Tracking. |
| BD9 - Sell from Stock | The scope item of this document is extending the Sell from Stock scope item. Therefore, the scope item Sell from Stock must be implemented and tested before testing the Sales scenario of scope item Substance Volume Tracking. |

### Preliminary Steps

#### Open a New Materials Management (MM) Period

Use

The period must be set up at the beginning of each new posting period to ensure values and goods movement are posted to the correct period. Usually, only the current posting period is open for posting. All other posting periods are closed.

Procedure

Check the current posting period and open a new one, if needed, following the process step from the Create New Open MM Posting Period - MDS master data script for company code 3310.

|  |
| --- |
| Note You can find the BNZ master data script under [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/create-new-open-mm-posting-period-bnz-e6bb56cc6e51c3b42d4cf76e831ab93f/purpose?version=latest). |

#### Specify Included Movement Types

Use

You can specify the movement types that are considered for substance volume tracking.

Substance volumes are tracked for the material document items with a movement type that is specified in this activity. If no movement types are specified, substance volumes will not be tracked.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, follow the steps as described below for either Configure Your Solution, or SAP Central Business Configuration.

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed, showing Realize phase on the right-hand side of the screen. Make sure the correct country version is selected. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Filter by Selection Criteria | Make the following entries in the respective search fields:Application Area: R&D EngineeringSub Application Area: Product Compliance | All items that match the search criteria are listed. |  |
| 5 | Find the Entry | Choose the Settings for Substance Volume Tracking item. | The Configure Your Solution – Settings for Substance Volume Tracking screen is displayed, showing all available configuration steps on the right side of the screen. |  |
| 6 | Go to Specify Included Movement Types | Go to Specify Included Movement Types step and choose Configure. | The Specify Included Movement Types: Change screen is displayed. |  |
| 7 | Create entries | Choose New Entries and make the following entries:For purchasing processes:Business process: PurchasingMovement type ID: 101For manufacturing processes:Business process: ManufacturingMovement type ID: 101For sales processes:Business process: SalesMovement type ID: 601Note If these records were already maintained, you can skip this step. | The Included Movement Types are specified. |  |
| 8 | Save | Choose Save. | Configuration is saved as specified. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Central Business Configuration. | The SAP CBC implementation workspace is displayed. |  |
| 2 | Open Active Flexible Workflow | From the Activities list on the left-hand side, nagivate to the Configuration entry and search for the following activity:Specify Included Movement TypesChoose Open Documentation to see more details about this configuration activity.Choose the line item in the search result to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Specify Included Movement Types: Change screen is displayed. |  |
| 3 | Create Entries | Choose New Entries and make the following entries:For Purchasing process:Business process: PurchasingMovement type ID: 101For Manufacturing process:Business process: ManufacturingMovement type ID: 101For Sales process:Business process: SalesMovement type ID: 601Note If these records were already maintained, you can skip this step. | The Included Movement Types are specified. |  |
| 4 | Save | Choose Save. | Configuration is saved as specified. |  |

#### Create Legal Entity Mappings

Use

The product stewardship specialist for Product Compliance creates legal entity mappings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access the App | Open Manage Legal Entities - Product Compliance (F5755). | The Manage Legal Entities screen is displayed. |  |
| 3 | Create a Legal Entity for Purchasing Process | Choose Create and make the following entries:Legal Entity ID: AE_IMPORT_3310Description: Legal Entity import to plant 3310 AEChoose Create. | A legal entity record is created. |  |
| 4 | Create a Legal Entity for Manufacturing Process | Choose Create and make the following entries:Legal Entity ID: AE_PRODUCE_3310Description: Legal Entity produce in plant 3310 AEChoose Create. | A legal entity record is created. |  |
| 5 | Create a Legal Entity for Sales Process | Choose Create and make the following entries:Legal Entity ID: DE_EXPORTDescription: Legal Entity export to DEChoose Create. | A legal entity record is created. |  |
| 6 | Navigate to Legal Entities Mapping | Open Manage Legal Entity Mappings - Product Compliance (F5935). | The Manage Legal Entity Mappings screen is displayed. |  |
| 7 | Create a New Mapping for Purchasing Process | Choose Create, select Import To from the dropdown list, and make the following entries:Compliance Requirement: AE SVT 2020 June - BPCReceiving Plant: 3310Legal Entity ID: AE_IMPORT_3310Choose Create. | The legal entity mapping is created. |  |
| 8 | Create a New Mapping for Manufacturing Process | Choose Create, select Produce In from the dropdown list, and make the following entries:Compliance Requirement: AE SVT 2020 June - BPCProducing Plant: 3310Legal Entity ID: AE_PRODUCE_3310Choose Create. | The legal entity mapping is created. |  |
| 9 | Create a New Mapping for Sales Process | Choose Create, select Export To from the dropdown list, and make the following entries:Compliance Requirement: DE SVT 2020 June - BPCDelivering Plant: 3310Legal Entity ID: DE_EXPORTChoose Create. | The legal entity mapping is created. |  |

#### Create a Purchasing Info Record

Use

Create source of procurement for materials from foreign suppliers.

|  |
| --- |
| Note If the purchasing info records for the RMPC07 and RMPC08 materials with the corresponding suppliers (33300050 and 33300051) already exist in the system, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | In the Header tab, make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Plant: 3310Purchasing Group: 001Supplier: 33300050Material: RMPC07Material Group: L002 | Header data is added. |  |
| 5 | Enter General Information | In the General Information tab, make the following entries:Available From: <current day>Available To: 31.12.9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | in the Purchasing Data tab, make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | In the Delivery and Quantity tab, make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10Over Delivery Tolerance in %: 10Order Unit: KGStandard Order Quantity: 10Under Purchasing Control, select the following checkboxes:Goods-Receipt-Based Invoice VerificationNo Evaluated Receipt Settlement | Delivery and Quantity details added. |  |
| 8 | Enter Condition Data | In the Conditions tab, choose Create.Make the following entries:Valid From:<current day>Valid To: 31.12.9999Amount: 1.00Currency: AEDPricing Unit: 1Unit of Measure: KGChoose Apply. | Condition data is added. |  |
| 9 | Save Your Data | Choose Create. | The purchasing info record is created. |  |
| 10 | Create Other Purchasing Info Records | Repeat the steps 3 to 9 for the following combinations of supplier and material:Supplier: 33300051, material: RMPC07Supplier: 33300050, material: RMPC08Supplier: 33300051, material: RMPC08 | The purchasing info records are created. |  |

Result

Purchasing info records for the RMPC07 and RMPC08 materials with the corresponding suppliers (33300050 and 33300051) are created.

#### Create Basic Compliance Data for Raw Materials

Use

Create basic compliance data for the raw materials that are used in purchasing and manufacturing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Basic Compliance Data - Raw Materials (F3024). | The Manage Basic Compliance Data - Raw Materials screen is displayed. |  |
| 3 | Check if Compliance Data for Raw Material Exists | In the Search field, enter Product Marketability RMC70-A and press Enter.Proceed accordingly in the following cases:The following entry exists:Raw Material Name: Raw PMA 07Product in Product Master: RMPC07In this case, compare the existing data with the data provided in the next steps.In all other cases, proceed with step 4 to create the raw material. |  |  |
| 4 | Create a New Raw Material | Choose Create. | The New Raw Material dialog box is displayed. |  |
| 5 | Enter Header Data for the Raw Material | Make the following entries and choose Save:Internal Name: Product Marketability RMC70-ALogistics Roles: PurchasedResponsible Unit: Permitted for all Responsible Units (S_ALL)Product Categorization: Mixture | The raw material is created with the entered header data.The Raw Material - Basic Compliance Data screen is displayed. |  |
| 6 | Add Assigned Products | Choose Edit.In the Assigned Products section, under Related Products in Product Master, enter RMPC07 in the Product in Product Master column. | The product details are populated in the table. |  |
| 7 | Check Compliance Purposes | In the Compliance Purposes section, make sure that the following compliance purpose is assigned:Raw Material Default Compliance Purpose |  |  |
| 8 | Navigate to the Analytical Composition | In the Compositions section, choose the Analytical Composition entry. | The Raw Material - Analytical Composition screen is displayed. |  |
| 9 | Edit the Analytical Composition | Choose Edit. | The Raw Material - Analytical Composition screen is displayed in edit mode. |  |
| 10 | Assign a Substance | In the Analytical Components table, choose Add.In the newly opened dialog box, Assign Substances, search for and select the following substance:Substance Name: Isoamyl alcoholInternal Name: IsopentanolChoose OK. | The selected substances and its details are populated in the Analytical Components table. |  |
| 11 | Enter Substance Concentration | In the Analytical Components table, make the following entries for the newly added substance:Concentration: 100Unit of Measure: % |  |  |
| 12 | Release the Composition | Choose Save, then Release. | The analytical composition is released. |  |
| 13 | Save the Raw Material | Navigate back to the Raw Material - Basic Compliance Data screen and choose Save. | The raw material is saved. |  |
| 14 | Create Another Raw Material | Repeat steps 3 to 13 with the following data to compare or create another raw material:In step 3Search for Product Marketability RMC70-B.Raw Material Name: Raw PMA 08Product in Product Master: RMPC08In step 5Internal Name: Product Marketability RMC70-BIn step 6Product: RMPC08In step 10Substance Name: acetic acid |  |  |

Result

Basic compliance data for raw materials is created.

#### Approve Suppliers of Raw Materials

Use

Create and approve suppliers of raw materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Basic Compliance Data - Raw Materials (F3024). | The Manage Basic Compliance Data - Raw Materials screen is displayed. |  |
| 3 | Open a Raw Material | In the Search field, enter RMPC07.Choose the entry for the RMPC07 material to navigate to the compliance view record. | The Raw Material - Basic Compliance Data screen is displayed. |  |
| 4 | Create a Supplier | In the Suppliers section, choose Create.In the newly opened Assign Supplier dialog box, in the Supplier field, enter 33300050.Choose Save. | The supplier is added in the Suppliers of Raw Material table. |  |
| 5 | Approve a Supplier | Choose the entry with the newly added supplier to navigate to the supplier compliance data.From the Set Supplier Status dropdown list, select Approve. | The Supplier Status for Raw Material is set to Approved. |  |
| 6 | Create Another Supplier | Repeat the steps 4 and 5 to create supplier 33300051. | The Supplier Status for Raw Material is set to Approved for the second supplier. |  |
| 7 | Create Suppliers for Another Raw Material | Repeat the steps 3 to 6 to create suppliers for the RMPC08 material. | The suppliers for the raw material are approved. |  |

Result

The RMPC07 and RMPC08 raw materials have approved suppliers.

#### Create Basic Compliance Data for Unpackaged Product

Use

Create basic compliance data for the unpackaged product that is used in manufacturing and sales.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The Manage Basic Compliance Data - Unpackaged Products screen is displayed. |  |
| 3 | Check if Compliance Data for Unpackaged Product Exists | In the Unpackaged Products tab in the Search field, enter Unpackaged Product UPC70 and press Enter.Proceed accordingly in the following cases:The following entry exists:Product Name: Semi SVT 01Product in Product Master: SGPCSVT01In this case, compare the existing data with the data provided in the next steps.The following entry exists:Product Name: Unpackaged Product UPC70Product in Product Master: emptyIn this case, proceed with step 4 to edit the entry.Note There might be more than one entry with the same product name. In this case, select either one of them. |  |  |
| 4 | Edit the Product | Select the entry from the search results to navigate to the product details.Choose Edit. | The Unpackaged Product - Basic Compliance Data screen is displayed in edit mode. |  |
| 5 | Set to not SDS-Relevant | In the Header section, make sure that the Safety Data Sheet Required checkbox is not selected. |  |  |
| 6 | Add Assigned Products | In the Assigned Products section, in the Related Products in Product Master table, enter SGPCSVT01 in the Product in Product Master column. | The product details are populated in the table.Note Please note that when a product is assigned, the name of the Unpackaged Product - Basic Compliance Data object is changed to the name of the product. |  |
| 7 | Create a Packaged Product | In the Assigned Products section, in the Related Compliance Views table, choose Create.In the newly opened dialog box, Create Packaged Product, make the following entries, and choose Save:Product in Product Master: FGPCSVT01Logistics Roles: Sold, Transported | The packaged product is assigned. |  |
| 8 | Check Compliance Purposes | In the Assigned Compliance Purposes table, make sure that only the following compliance purpose is assigned:Product Default Compliance Purpose |  |  |
| 9 | Navigate to the Material-Based Composition | In the Compositions section, choose the Material-Based Composition entry. | The Unpackaged Product - Material-Based Composition screen is displayed. |  |
| 10 | Edit the Material-Based Composition | Choose Edit. | The Unpackaged Product - Material-Based Composition screen is displayed in edit mode. |  |
| 11 | Assign Raw Materials | In the Before Production table, search for RMPC07 in the Compliance View field. Select the correct value from the search result.Repeat this step in the newly added row, for the second raw material RMPC08. | The selected raw materials and their details are populated in the Before Production table. |  |
| 12 | Specify Concentration Before Production | In the Before Production table, make the following entries in the respective columns for the newly added raw materials:For RMPC07 :Concentration: 60Unit of Measure: %For RMPC08 :Concentration: 40Unit of Measure: % | Concentration before production is filled in your material-based composition. |  |
| 13 | Add Produced Substances | Under the After Production tab, in the Remaining and Produced Substances table, choose Add.In the newly opened dialog box, choose the Produced Substances tab, search for and select the following substance:Substance Name: Isoamyl acetateCAS number: 123-92-2Choose Add. | The selected substance and its details are populated in the Remaining and Produced Substances table. |  |
| 14 | Specify Concentration After Production | In the Remaining and Produced Substances table, make the following entries for the newly added substance:Concentration: 100Unit of Measure: % |  |  |
| 15 | Release the Composition | Choose Save, then Release. | The material-based composition is released and in the Overall Concentration section, the total is 100%. |  |
| 16 | Edit the Analytical Composition | Navigate back to the Unpackaged Product - Basic Compliance Data screen.In the Compositions section, choose the Analytical Composition entry. | The Unpackaged Product - Analytical Composition screen is displayed. |  |
| 17 | Check Assigned Substances | Choose Edit.In the Analytical Components table, make sure that there is only the following entry:Substance: Isoamyl acetateCAS Number: 123-92-2Concentration: 100Unit of Measure: % |  |  |
| 18 | Release the Analytical Composition | Choose Release. | The analytical composition is released. |  |

Result

Basic compliance data for unpackaged product is created.

#### Enable Substance Volume Tracking for Compliance Requirements

Use

Enable the process of substance volume tracking for the relevant compliance requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Enable Substance Volume Tracking - for Compliance Requirements (F6964). | The Enable Substance Volume Tracking for Compliance Requirements initial screen is displayed. |  |
| 3 | Select a Compliance Requirement | Search for the following compliance requirement for business process Purchasing and select the row:AE SVT 2020 June - BPCNote You can enable only compliance requirements that are not already enabled for substance volume tracking. If the SVT Enabled field for the corresponding compliance requirement and business process is already set to Yes, skip this step. | The object page is displayed on the right side of the screen and the Enable button is active. |  |
| 4 | Enable Compliance Requirement | Choose Enable for the selected compliance requirement and business process.In the newly opened confirmation dialog, choose Continue. | The SVT Enabled field is changed to Yes, Initial Tracking Date and Enabled On dates are populated. |  |
| 5 | Enable other Compliance Requirements | Repeat steps 3 and 4 for the following combinations of compliance requirements and business processes:Compliance Requirement: AE SVT 2020 June - BPCBusiness Process: ManufacturingCompliance Requirement: DE SVT 2020 June - BPCBusiness Process: Sales | The required compliance requirements are enabled for Substance Volume Tracking and calculation can start. |  |

#### Set Initial Stock for Material

Use

Set initial stock for the material so that it is available for sale.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen is displayed. |  |
| 3 | Enter Movement Type | Make the following selections in the two dropdown lists on the top:Goods ReceiptOther |  |  |
| 4 | Enter Material | On the Material tab under the Detail Data section, make the following entry and press Enter:Material: FGPCSVT01 | The table in the Header Data section is updated with the short description of the material. |  |
| 5 | Enter Material Quantity | On the Quantity tab, make the following entries and press Enter:Qty in Unit of Entry: 1000Unit of Entry: BT | The table in the Header Data section is updated with the entered quantity for the material. |  |
| 6 | Enter Storage Information | On the Where tab, make the following entries and press Enter:Goods Movement Type: 561Plant: 3310Storage Location: 331A | The table in the Header Data section is updated with the storage information. |  |
| 7 | Save Your Entries | Choose Post. | A success message is displayed with the number of the created material document. |  |

Result

The initial stock is created in the selected storage location and it can be used for further processes.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create a Purchase Requisition](#unique_17) [page ] 25 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisition for stock material is created. |
| [Convert a Purchase Requisition to a Purchase Order](#unique_18) [page ] 27 | Purchaser | Process Purchase Requisitions (V2) (F1048A) | Purchase order for stock material is created. |
| [Post Goods Receipt for a Purchase Order](#unique_19) [page ] 28 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt for purchased material is posted. |
| [Analyze Stock Overview (Optional)](#unique_20) [page ] 29 | Warehouse Clerk | Stock - Single Material (F1076) | Stock material is sufficient in order to proceed with manufacturing. |
| [Create a Process Order](#unique_21) [page ] 30 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) | Process order for semifinished material is created. |
| [Manual Goods Issue (Optional)](#unique_22) [page ] 32 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods movements for input materials are posted. |
| [Confirm a Process Order](#unique_23) [page ] 32 | Production Supervisor - Process Manufacturing | Confirm Process Order (CORK) | Process order is confirmed. |
| [Post Goods Receipt for a Process Order](#unique_24) [page ] 33 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt for produced material is posted. |
| [Create a Sales Order](#unique_25) [page ] 35 | Internal Sales Representative | Manage Sales Orders – Version 2 (F3893) | Sales order is created. |
| [Add a Market Assessment](#unique_26) [page ] 36 | Product Stewardship Specialist - Product Compliance | Process Requests from Logistics (F3342) | In case of a marketability block on the sales order, the chosen market is assessed and selling of the product is allowed. |
| [Create a Delivery](#unique_27) [page ] 37 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Post Goods Issue for an Outbound Delivery](#unique_28) [page ] 38 | Shipping Specialist | Manage Outbound Deliveries (F0867A)Pick Outbound Delivery (F0868) | Goods issue is posted for the outbound delivery and a material document is generated. |
| [Monitor Substance Volumes](#unique_29) [page ] 40 | Master Data Specialist - Product Compliance | Monitor Substance Volumes (F4693) | Substance volumes are correct. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Purchasing Process

#### Create a Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to manually create purchase requisitions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions - Professional screen is displayed. |  |
| 3 | Create New Purchase Requisition | Choose Create. | The Purchase Requisition screen is displayed. |  |
| 4 | Select Document Type | In the General Information section, make the following selection:Document Type: Purchase Requisition (NB) |  |  |
| 5 | Create Item | In the Items section, choose Create, then choose Material. | The Purchase Requisition Item screen is displayed. |  |
| 6 | Enter Details | Under the General Information section, make the following entries:Item Category: StandardPlant: 3310Material: RMPC07Storage Location: 331BUnder the Quantity and Date section, make the following entries:Quantity: 100Delivery Date: default valueRequisition Date: default valueRelease Date: <current date>Under the Contact Information section, make the following entries:Requirement Tracking Number: <free text>Purchasing Organization: 3310Purchasing Group:001Choose Apply. | The purchase requisition item is saved and added to the purchase requisition.The Purchase Requisition screen is displayed again. |  |
| 7 | Save Your Entries | Choose Create.If there is a warning message about the delivery date, ignore it, and choose Create. | The purchase requisition is created.Note Note down the purchase requisition number for the material as it is needed in the Convert Purchase Requisition to Purchase Order procedure. |  |
| 8 | Create Purchase Requisition for Other Material | Repeat steps 2 to 7 for material: RMPC08. |  |  |

#### Convert a Purchase Requisition to a Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to convert the assigned purchase requisitions to purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Purchase Requisitions (V2) (F1048A) app. | The Process Purchase Requisitions screen is displayed. |  |
| 3 | Search for Purchase Requisitions | In the Search field, enter the number of the purchase requisition that you have created in the Create Purchase Requisition procedure for material "RMPC07" and choose Go. | The purchase requisition for material "RMPC07" is shown in the search results.Note The purchase requisition is approved automatically in the background, so it might take some time to appear in the search results. |  |
| 4 | Assign a Supplier to a Purchase Requisition | Locate the record with your purchase requisition and check the Assigned Supplier column.If the column is not visible, choose the Show More Per Row button.If a supplier has been assigned to the purchase requisition, you can skip this step.Otherwise, choose the Assign Source of Supply button to select a supplier for your purchase requisition. Select the info record for one of the following suppliers: 33300050 or 33300051, and choose Assign. | The purchase requisition has an assigned supplier. |  |
| 5 | Prepare the Purchase Order | Select the purchase requisition where the assigned supplier is displayed and choose Create Purchase Order. | The Purchase Order screen is displayed. |  |
| 6 | Create the Purchase Order | In the General Information section, make the following selection:Purchase Document Type: Standard PO (NB).Choose Order. | The purchase order is created.Note Note down the purchase order number for the material as it is needed in the Post Goods Receipt procedure. |  |
| 7 | Go Back to Process Purchase Requisition | Navigate back to the Process Purchase Requisitions screen. | The purchase requisition list is displayed again.The processing status of the purchase requisition is changed to PO created. |  |
| 8 | Create a Purchase Order for Another Material | Repeat steps 3 to 7 for material "RMPC08". |  |  |

#### Post Goods Receipt for a Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This porcess step shows you how to post goods receipts for the created purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen is displayed. |  |
| 3 | Search for the Purchase Order | In the Purchasing Documents field, enter the number of the purchase order that you have created for material "RMPC07" and choose Enter. | The purchase order is displayed. |  |
| 4 | Enter a Delivery Note | In the General Information section, make the following entry:Delivery Note: <enter free text> |  |  |
| 5 | Select an Item | Select the items under the Items section. | The Post option is activated. |  |
| 6 | Post Goods Receipt | Choose Post. | A success message is displayed with the number of the created material document.Note Note down the number of the material document as it is needed in the Monitor Substance Volumes procedure. |  |
| 7 | Post Goods Receipt for Another Purchasing Document | Repeat steps 3 to 6 for the purchase order that you have created for material "RMPC08". |  |  |

#### Analyze Stock Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the stock overview is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Stock - Single Material (F1076). | The Stock - Single Material screen is displayed. |  |
| 3 | Enter Material | In the Material field, enter RMPC07. | The stock overview for the material is shown. |  |
| 4 | Change View | Switch to Chart View. | Stock by Plant / Storage Location chart is displayed.You can view the previously procured quantities of the material. |  |
| 5 | View Stock for Other Material | Repeat steps 3 to 4 for material "RMPC08". |  |  |

### Manufacturing Process Based on a Process Order

The manufacturing process starts with the creation of a process order and continues with manual goods issue for input materials, confirmation of operations, and posting of goods receipt. Purchased raw materials that are already in stock are used in the manufacturing process. In this test script, the manufacturing process is shown for the semifinished material "SGPCSVT01".

#### Create a Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create process orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Process Order (COR1). | The Create Process Order: Initial Screen is displayed. |  |
| 3 | Enter Parameters | Make the following entries:Material Number: SGPCSVT01Production Plant: 3310Process Order Type: YBM2Choose Continue. | The Create Process Order: Header – General Data screen is displayed. |  |
| 4 | Enter General Data | Under General Data tab, in the Quantities section, make the following entry:Total Qty: 100In the Scheduling section, make the following entry:Type: Current datePress Enter. | The following confirmation message is displayed: All checked materials in order are available. |  |
| 5 | Enter Goods Receipt Data | Under Goods Receipt tab, in the Receipt section, make the following entry:Location: 331B | Storage location is set. |  |
| 6 | Check the Backflush Indicator | Choose Material List.Check the Backflushing column.If the checkbox is selected for each material in the list, skip the next test procedure - Manual Goods Issue (Optional). Otherwise, proceed with the test script in the given order. |  |  |
| 7 | Release the Record | Choose Release. | A success message is displayed to inform that the release is carried out. |  |
| 8 | Save | Choose Save.If a Cost Calculation dialog box displays, choose Yes. | A success message is displayed with the number of the created process order.Note Note down the number of the process order as it is needed in the next procedures. |  |

#### Manual Goods Issue (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The initial screen is displayed. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter.Action: Goods IssueReference: OrderOrder number: <the number of the process order that you have created>GI for order: 261 | The screen name is updated. |  |
| 4 | Check Each Item | For each item that is shown under the General tab in the Header Data section, select the checkbox in the OK column. | The items are set to OK. |  |
| 5 | Post Goods Movements | Choose Post. | The goods movements are posted. |  |

#### Confirm a Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to control the order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Confirm Process Order (CORK). | The Enter Process Order Confirmation: Initial Screen screen is displayed. |  |
| 3 | Enter Process Order | In the Process Order field, enter the number of the process order that you have created and choose Enter. | The Process Order Confirmation Enter : Actual Data screen is displayed. |  |
| 4 | Enter Confirmation Option | In the Confirmation Type section, choose Final Confirmation and select the checkbox for Clear Reservation.Press Enter. |  |  |
| 5 | Save Confirmation | Choose Save. | The final confirmation of the last operation is carried out. |  |

#### Post Goods Receipt for a Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the process order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The initial screen is displayed. |  |
| 3 | Enter Process Order | Make the following entries and press Enter.Action: Goods ReceiptReference: OrderOrder Number: <the number of the process order that you have created>Movement Type: 101 | The screen name is updated. |  |
| 5 | Check Items | Select the item that is shown under the General tab in the Header Data section.On the bottom of the Detail Data section, select the Item OK checkbox.If there is more than one item, repeat for all of them. | The items are set to OK. |  |
| 6 | Check the Entry | Choose Check in the lower right corner. | The document is checked as OK. |  |
| 7 | Post Goods Movement | Choose Post. | The goods movements are posted.Note Note down the number of the material document as it is needed in the Monitor Substance Volumes procedure. |  |

### Sales Process Based on a Sales Order

#### Create a Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access App | Open Manage Sales Orders – Version 2(F3893)app. | The Manage Sales Orders – Version 2 screen is displayed. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders - Version 2 screen, choose Create. | A New Object screen is displayed. |  |
| 4 | Enter Initial Data to Create a Sales Order | In the newly opened dialog box, make the following entries and choose Continue:Sales Order Type: Standard Order (OR)Sales Organization: 3310Distribution Channel: Direct Sales (10)Division: Product Division 00 (00) | The Sales Order screen is displayed. |  |
| 5 | Complete the Sales Order Information | In the General Information tab, make the following entries:Sold-to Party: 33100050Customer Reference: <enter free text>In the Items tab, make the following entries and choose Add Row or press Enter:Product: FGPCSVT01Requested Quantity: 10 | There might be a warning message for a missing marketability assessment. |  |
| 6 | Create the Sales Order | Save the order by choosing Create. | The sales order is created.Note Note down the number of the sales order as displayed in the header. |  |

Succeeding Procedures

If there is a block on the sales order under Product Marketability Status, follow the steps in the [Add a Market Assessment](#unique_26) [page ] 36 procedure to remove it.

If there is a block on the sales order under Dangerous Goods Status, follow the steps in the [Apply Regulations to Countries/Regions](#unique_34) [page ] 44 and [Classify a Packaged Product as No Dangerous Good](#unique_35) [page ] 45 to remove it.

If there are no blocks on the sales order or when they are all removed, proceed with the [Create a Delivery](#unique_27) [page ] 37 procedure.

#### Add a Market Assessment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When there is a block on the sales order under Product Marketability Status, this process step shows you how to add a market assessment for a product so that the product can be sold.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Process Requests from Logistics (F3342). | The Process Requests from Logistics screen is displayed. |  |
| 3 | Open the Requests for the Product | Search for the unprocessed requests that involve FGPCSVT01 and select the one with the following parameters:Business Process / Area: Sell in <country/region of the customer in the sales order>Request Responsibility: Product ComplianceOrigin: Sales Order | The Compliance Requests from Logistics screen is displayed. |  |
| 4 | View the Market Assessments | Navigate to the Countries/Regions to Verify section and choose View Market Assessments. | The Market Assessment screen is displayed. |  |
| 5 | Add a Market | Choose Edit.In the Product Market Assessments table, choose Add, and select Germany from the dialog box. | A new record is added for Germany in the Product Market Assessments table. |  |
| 6 | Assess a Market | From the Product Market Assessments table, choose the newly created record.On the right screen, select Allowed from the Assessment Status for Sales dropdown list, and choose Apply. | The Product Market Assessments table shows that Sell In is set to Allowed for Germany. |  |
| 7 | Save the Assessment | Choose Save. | The assessment is saved.The block on the sales order for marketability is removed. |  |

#### Create a Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you haw to create an outbound delivery for your sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen is displayed. |  |
| 3 | Find Your Sales Order | Enter the following search criteria and choose Go:Planned Creation Date: Due Up Until Next WeekSales Document: <number of the sales order that you have created> | The search results are listed in the Sales Orders Due for Delivery table. |  |
| 4 | Create a Delivery | Select the checkbox of the row with your sales order and choose Create Deliveries. | The Display Log button is active, and the following message is shown:Logs Created: 1 |  |
| 5 | Check Delivery Logs | Choose Display Logs to check if the delivery is created without issues. | The Analyze Delivery Logs screen is displayed.If there are no messages, note down the number of the created delivery under the Deliveries section. |  |

#### Post Goods Issue for an Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issue for an outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Manage Outbound Deliveries (F0867A). | The Manage Outbound Deliveries screen is displayed. |  |
| 3 | Find Your Outbound Delivery | Enter the following search criteria and choose Go:Overall Status: AllDelivery Document: <number of the delivery you have created>Note You can add the Delivery Document field by choosing Adapt Filters and selecting the field from the list. | The search results are listed in the Deliveries table. |  |
| 4 | Pick Outbound Delivery | Find the entry in the search results with your outbound delivery and choose Pick.Note If the Pick button is missing, choose Show More per Row to expand the view. | You are navigated to the Pick Outbound Delivery (F0868) app. |  |
| 5 | Enter Picking Quantity | In the Delivery Items table, make the following entry for the "FGPCSVT01" material:Picking Quantity: 10Choose Save. | The outbound delivery is saved, and the status is changed to Ready to Post GI. |  |
| 6 | Post Goods Issue | Choose Post GI. | The goods issue is posted, and a material document number is generated.Note Note down the number of the material document as it is needed in the Monitor Substance Volumes procedure. |  |

### Substance Volume Tracking

#### Monitor Substance Volumes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor the substance volumes that are calculated from the periodic tracking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Monitor Substance Volumes (F4693). | The Monitor Substance Volumes initial screen is displayed. |  |
| 3 | Check Substance Volumes | In the Substance Volumes table, check if there are any entries. | If yes, note or write down the substance volumes for the listed entries, so you can compare the results. For example:SubstanceCompliance RequirementLegal EntitySubstance VolumeIsoamyl alcoholAE SVT 2020 June - BPCAE_IMPORT_3310<volume1>acetic acidAE SVT 2020 June - BPCAE_IMPORT_3310<volume2>Isoamyl acetateAE SVT 2020 June - BPCAE_PRODUCE_3310<volume3> |  |
| 4 | Initiate Calculation | Choose Initiate Calculation.Note The system periodically runs a background process that selects all material documents that are relevant for tracking and initiates calculation for these material documents. To avoid waiting for the next periodic calculation, you can use the Initiate Calculation button. | A confirmation message appears on the screen: Calculation StartedCalculation time varies by system and may take a few minutes. |  |
| 5 | Refresh the Page | Refresh the page in the browser. | The Monitor Substance Volumes initial screen is displayed. |  |
| 6 | Verify Substance Volumes | Check the substances in the Substance Volumes table. | The substance volumes have increased with the corresponding quantities that you have imported or produced until now.In case you have imported 100 kg from both "RMPC07" and "RMPC08" and you have produced 100 kg of "SGPCSVT01" the following entries are shown:SubstanceCompliance RequirementLegal EntitySubstance VolumeIsoamyl alcoholAE SVT 2020 June - BPCAE_IMPORT_3310<volume1 + 100>acetic acidAE SVT 2020 June - BPCAE_IMPORT_3310<volume2 + 100>Isoamyl acetateAE SVT 2020 June - BPCAE_PRODUCE_3310<volume3 + 100>"volume1", "volume2", and "volume3" are the substance volumes from step 3. |  |
| 7 | Verify Substance Volumes from Sales | In the Substance Volumes table, check if there is an entry for the "Isoamyl acetate" substance with compliance requirement DE SVT 2020 June - BPC and legal entity DE_EXPORT. | If there is such an entry, make sure that the substance volume is unchanged after you have exported a certain quantity of the "FGPCSVT01" product.Note When a substance is traded internationally, there are certain responsibilities that need to be fulfilled to import it safely and legally. Among other things, the responsible importer must ensure compliance with all necessary regulations. It is important to determine the responsible importer correctly, so the substance volumes can be tracked accordingly.For purchasing and sales scenarios, the responsible importer in substance volume tracking is by default the BuyerIf there is no such entry, proceed with the next step. |  |
| 8 | Check Percentage of Threshold | Check the Percentage of Threshold column for the following substances:"acetic acid""Isoamyl alcohol""Isoamyl acetate" | The percentage of threshold is shown in green when the substance volume is below the threshold.The percentage of threshold is shown in red when the substance volume is above the threshold. |  |
| 9 | Check Monthly Volumes | Select the entry for the "Isoamyl alcohol" substance with compliance requirement: AE SVT 2020 June - BPC. | A new screen is displayed with the Substance Volumes by Month and Scenario table.There is an entry for the current month and year and Purchasing as a business process.Note If you have selected the entry for the "Isoamyl acetate" substance, the business process in the table is Manufacturing. |  |
| 10 | Check Material Documents | Select the entry for the current month and year. | The screen is split and on the right side the detailed data for the selected month and substance are is displayed.In the Material Documents table you can find the number of the material document that you have created in the Post Goods Receipt procedure.Note If you have selected the entry for the "Isoamyl acetate" substance, you can find the number of the material document that you have created in the Post Goods Receipt for a Process Order procedure. |  |
| 11 | View Log | Select the entry with your material document.Choose View Log. | The Log Details screen is displayed with information about the tracking process of the material document. |  |
| 12 | Check Volumes by Product | Close the monthly volumes for the substance screen and go to the Substance Volumes by Product tab.Choose one of the listed products. | The screen is split and on the right side, you can see how the selected product contributed to the total substance volume and which the originating material documents are. |  |
| 13 | Check Material Documents for Another Substance | Navigate back to the Monitor Substance Volumes initial screen.Repeat steps 11 to 14 for the "acetic acid" substance. |  |  |
| 14 | Check Material Documents for Another Substance | Navigate back to the Monitor Substance Volumes initial screen.Repeat steps 11 to 14 for the "Isoamyl acetate" substance. |  |  |
| 15 | Check Monthly Volumes from Sales | Navigate back to the Monitor Substance Volumes initial screen.If there is an entry for the "Isoamyl acetate" substance with compliance requirement: DE SVT 2020 June - BPC, select it.If there is no such entry, go to step 19. | A new screen is displayed with the Substance Volumes by Month and Scenario table.Check if there is an entry for the current month and year and Sales as a business process. |  |
| 16 | Check Material Documents from Sales | If there is an entry for the current month and year, select it.If there is no such entry, go to step 19. | The screen is split and on the right side the Substance Volumes by Material Documents is displayed.Make sure that the number of the material document that you have created in the Post Goods Issue for Outbound Delivery procedure is not displayed. |  |
| 17 | Check Used Legal Entity Mappings | Open Manage Legal Entity Mappings - Product Compliance (F5935) as a Product Stewardship Specialist - Product Compliance.Select the legal entity mapping with the following parameters:Compliance Requirement: AE SVT 2020 June - BPCBusiness Process Scenario: Import ToReceiving Plant: 3310Legal Entity: AE_IMPORT_3310 | The screen is split and details about the legal entity mapping are displayed on the right.The Used in Substance Volume Tracking field is set to Yes.The Delete option is disabled.Note The same results are expected also for the other legal entity mappings that are used for tracking substance volumes. |  |

## Appendix

### Conditional Procedures

#### Apply Regulations to Countries/Regions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For all countries/regions where packaged products should be shipped from or shipped to, the Dangerous Goods Specialist - Product Compliance has to set rules for dangerous goods checks that are carried out in sales documents and delivery documents. If no valid regulations are assigned or if the transport permission is not set to Always Allowed, the system blocks further processing of sales documents and delivery documents. This process step shows you how to check and apply the relevant regulations for the product, so it can be further classified accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dangerous Goods Specialist - Product Compliance. |  |  |
| 2 | Access the App | Open Apply Regulations - Dangerous Goods(F3916) app. | The Apply Regulations - Dangerous Goods screen is displayed and shows a world map. |  |
| 3 | Prefill Regulations for Countries | Choose the Prefill Regulations for Countries/Regions button and, in the Prefill Applicable Dangerous Goods Regulations and Languages for Countries/Regions popup, choose OK. | The system prefills countries with the applicable dangerous goods regulations for the relevant modes of transport. In addition, the system also prefills the required languages tables.After the data is filled into the corresponding database table, the color of the country/region with prefilled data changes from gray to orange or green. |  |
| 4 | Check Relevant Countries/Regions | Check if the respective countries, used in this scenario, are green. If not, then select the respective country/region.On the right side of the screen, in the Transport Check Rules section, select a mode of transport (for example, Aircraft). Then, from the Specify Check Rules dropdown list select Transport Allowed. | On the map, the color of the country/regions are changed accordingly. |  |

#### Classify a Packaged Product as No Dangerous Good

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to classify a packaged product that you want to sell according to dangerous goods regulations and allow the transportation, so the block on the sales order under Dangerous Goods Status is removed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access the App | Open Process Requests From Logistics(F3342). | The Process Requests from Logistics screen is displayed. |  |
| 3 | Open the Requests for the Product | Search for the requests that involve FGPCSVT01 and select the one with the following parameters:Business Process / Area: Transport In <country/region of the customer in the sales order>Solution Area: Dangerous Goods ManagementOrigin: Sales OrderIf the Reason for Request is Undefined Situation, make sure you have completed the [Apply Regulations to Countries/Regions](https://help.sap.com/docs/s4hana-best-practices/substance-volume-tracking-4ol-us/apply-regulations-to-countries-regions?state=DRAFT&version=2308_DEV) procedure. | The Compliance Requests from Logistics screen for the selected entry is displayed |  |
| 4 | Add a Compliance Purpose | In the Compliance Purposes to Verify section, choose Add.In the newly opened dialog box, search and select the following compliance purpose:Transport in North AmericaChoose OK.Note In some scenarios, it might also be required to add Compliance Purpose for Transport in <country/region of the seller>. Always check for additional open requests from logistics for your sales order. | The selected compliance purpose is assigned to the product. |  |
| 5 | Save the Processed Request | Choose Done, then OK to confirm. | The request is processed. |  |
| 6 | Access App | Log on to the SAP Fiori launchpad as a Dangerous Goods Specialist - Product Compliance and open My Unpackaged Dangerous Goods (F3643). | The My Unpackaged Dangerous Goods screen is displayed. |  |
| 7 | Select an Unpackaged Dangerous Good | In the Search field, enter SGPCSVT01, and then select it from the result list. | The Classify Unpackaged Dangerous Good screen is displayed. The released analytical composition and a list with all assigned dangerous goods regulations for the product are displayed. |  |
| 8 | Select a Regulation | In the Basic Classification section, choose the first regulation in the list. | The Dangerous Good - Classification Details screen for the selected regulation is displayed. |  |
| 9 | Classify the Unpackaged Product | Choose Edit.In the Classification section, select the following data:Classified As: No Dangerous GoodsIn the Transport Permission section, select the following data:Transport Permission: AllowedChoose Save. | The classification with the selected data is saved. |  |
| 10 | Navigate Back | Navigate back to the Classify Unpackaged Dangerous Good screen. | The Classify Unpackaged Dangerous Good screen is displayed. |  |
| 11 | Classify Product According to the Other Regulations | Select the regulation that you've just processed and choose Apply Classification to Other Regulations.In the newly opened dialog box, select all regulation, and choose Apply Classification. | The system applies the classification you've done for the first regulation to all other selected regulations and saves the classifications in draft versions. |  |
| 12 | Release Classifications | Select all regulations that are in progress and choose Release.Choose Save Drafts and Release. | All classifications for the product are released. |  |
| 13 | Navigate to App | Open My Packaged Dangerous Goods (F3711). | The My Packaged Dangerous Goods screen is displayed. |  |
| 14 | Select a Packaged Dangerous Good | In the Packaged Products tab, in the Search field, enter FGPCSVT01, and then select it from the result list. | The Classify Packaged Dangerous Good screen is displayed. The packaging details and a list with all assigned dangerous goods regulations for the product are displayed. |  |
| 15 | Specify Enclosure Variant and Transport Permission | Select all regulations and choose Specify Enclosure Variant.In the Specify Enclosure Variant dialog box, select the following data:Enclosure Variant: <Leave Empty>Transport Permission: AllowedChoose Save. | The system set the transport permission to Allowed for all selected regulations for all applicable modes of transport and saves the classifications in draft versions. |  |
| 16 | Release Classifications | Select all regulations that are in progress and choose Release.Choose Save Drafts and Release. | All classifications for the product are released.The block on the sales order for dangerous goods transportation is removed. |  |

### Error Handling

#### Export Logs of Failed Tasks (Optional)

Purpose

This process step shows you how to follow up on periodic tracking processing when you want to analyze why the tracking was not completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Process Product Compliance Events (F4005) app. | The Process Product Compliance Events screen is displayed. |  |
| 3 | Filter Events | Choose SVT: Periodic Tracking Requested from the Event Type dropdown list. | The filter is applied. |  |
| 4 | Follow up Failed Events | Go to the Failed tab.Find and select the event that was started by the user with Master Data Specialist - Product Compliance role and the date and time when the calculation was initiated. | The Product Compliance Event screen is displayed. |  |
| 5 | Follow up Failed Tasks | Go to the failed tasks and select an entry. | The Task screen is displayed. |  |
| 6 | View Log | Choose View Log in the upper right corner. | The Log Details screen is displayed. |  |
| 7 | Export Log | Choose Export or Export As... according to your preference..Save the generated file on your local device.You can export the log for each failed task. | A file with the log details is generated. |  |

Result

Logs of failed tasks exported for additional analysis.

#### Process Again Failed Tasks (Optional)

Purpose

This process step shows you how to process the failed tasks after analyzing the log details and fixing the root cause.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Process Product Compliance Events (F4005). | The Process Product Compliance Events screen is displayed. |  |
| 3 | Filter Events | Choose SVT: Periodic Tracking Requested from the Event Type dropdown list. | The filter is applied. |  |
| 4 | Follow up a Failed Event | Go to the Failed tab.Find and select the event for which you have analyzed task log details. | The Product Compliance Event screen is displayed. |  |
| 5 | Follow up a Failed Task | Go to the failed tasks and select the task you want to process again. | The Task screen is displayed. |  |
| 6 | Reprocess a Task | Choose Process Again in the upper right corner. | Reprocessing started. The processing status of the event is In Process. |  |
| 7 | Return to Tasks | Return back to the Product Compliance Event screen.Repeat steps 5 to 6 for all failed tasks. |  |  |
| 8 | Check Event for Completion | Go to Completed tab on the Process Product Compliance Events screen. | You can find the event for which you have analyzed task log details. The event is completed. |  |
| 9 | Follow up a Failed Event (optional) | If you cannot find the entry under the Completed tab, check if it still under the New or In Progress tab. It may take some time to complete the processing.If you cannot find it there either, repeat this procedure. |  |  |

Result

Failed tasks are processed again.

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
> Flagged while digesting this document, not verified: The 'Classify a Packaged Product as No Dangerous Good' procedure adds the compliance purpose 'Transport in North America' (and links to the 4OL US / 2308_DEV procedure), although the sample customer 33100050 is in DE and the market assessment is added for Germany; the appendix may have been carried over from the US version of this script.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-assess-marketability-of-a-product-31h-ae-sap-s-4hana-cloud]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-chemical-compliance-approval-for-purchased-material-and-su]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4OL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 84,774 chars in the whole document
