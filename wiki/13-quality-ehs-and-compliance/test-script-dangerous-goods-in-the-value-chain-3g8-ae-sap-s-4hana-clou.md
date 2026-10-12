---
id: 13-quality-ehs-and-compliance/test-script-dangerous-goods-in-the-value-chain-3g8-ae-sap-s-4hana-clou
title: "Test Script: Dangerous Goods in the Value Chain (3G8_AE) - SAP S/4HANA Cloud Public Edition (3G8_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3G8 (AE): dangerous goods transport checks in sales orders and outbound deliveries, with prerequisites and steps."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/dangerous-goods]
aliases: [3G8_S4CLD2608_BPD_EN_AE]
keywords: [Dangerous Goods Classification and Checks, dangerous goods, transport permissibility check, sales order creation, outbound delivery, picking and goods issue, transport restrictions, dangerous goods status, sales order fulfillment monitor, transport check rules]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3G8_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-935
topic: 13-quality-ehs-and-compliance/dangerous-goods
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Dangerous Goods in the Value Chain (3G8_AE) - SAP S/4HANA Cloud Public Edition (3G8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3G8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Dangerous Goods Classification and Checks** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Dangerous Goods in the Value Chain (3G8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852623)

[2 Prerequisites 4](#_Toc232852624)

[2.1 System Access 4](#_Toc232852625)

[2.2 Roles 4](#_Toc232852626)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852627)

[2.4 Business Conditions 12](#_Toc232852628)

[2.5 Preliminary Steps 13](#_Toc232852629)

[2.5.1 Post Goods Movement 13](#_Toc232852630)

[2.5.2 Check Assigned Dangerous Goods Regulations and Transport Check Rules for Countries/Regions 14](#_Toc232852631)

[3 Overview Table 16](#_Toc232852632)

[4 Test Procedures 17](#_Toc232852633)

[4.1 Create Sales Documents Containing Dangerous Goods with Transport Allowed 17](#_Toc232852634)

[4.1.1 Create Sales Order with a Dangerous Good with Transport Allowed 17](#_Toc232852635)

[4.1.2 Create Outbound Delivery with a Dangerous Good with Transport Allowed 20](#_Toc232852636)

[4.1.3 Carry Out Picking and Post Goods Issue for a Dangerous Good with Transport Allowed 21](#_Toc232852637)

[4.2 Create Sales Documents Containing Dangerous Goods with Transport Allowed with Restrictions 22](#_Toc232852638)

[4.2.1 Create Sales Order with a Dangerous Good with Transport Allowed with Restrictions 22](#_Toc232852639)

[4.2.2 Analyze Sales Order Status for Dangerous Goods 25](#_Toc232852640)

[4.2.3 Analyze Sales Order Fulfillment Monitor 26](#_Toc232852641)

[4.2.4 Create Outbound Delivery with a Dangerous Good with Transport Allowed with Restrictions 28](#_Toc232852642)

[4.2.5 Analyze Outbound Delivery Status for Dangerous Goods 29](#_Toc232852643)

[4.2.6 Carry Out Picking and Post Goods Issue for a Dangerous Good with Transport Allowed with Restrictions 30](#_Toc232852644)

## Purpose

Overview

This scope item supports a dangerous goods transport permissibility check that is carried out in business documents within the value chain and the printing of the dangerous goods description on certain documents as follows:

- In sales documents and outbound delivery documents, a transport permissibility check is carried out for all compliance-relevant products. For each compliance-relevant product that is added to a business document, the system checks if the product is classified as a dangerous good. If so, the system checks if the transport of the product is allowed. If the product is not classified or if transport is not allowed, this check can result in a block. If a dangerous goods assessment is not yet completed, a corresponding request to the product steward specialist or the dangerous goods specialists is created.
- Dangerous goods descriptions are printed on sales order confirmations, delivery notes, and picking lists.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Dangerous Goods Specialist - Product Compliance (Product Compliance) | SAP_BR_DG_SPLST_PCL | Dangerous Goods | SAP_BR_DG_SPLST_PCL |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note If you create your own packaged and unpackaged products, carry out the compliance steps for all relevant solution areas using the test scripts for the scope items listed:Product Marketability: 31H (Assess Marketability of a Product)Safety Data Sheet Management: 3VR (Manage Safety Data Sheets for Products)Dangerous Goods Management: 3FC (Assess Dangerous Goods for a Product)The demo data described and used in the following is tailored for a smooth execution of the described procedures and suppresses processes of other solution areas in product compliance. |

The following data is valid for both test scenarios:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Listed Substance | L00000005806 | CAS Number: 108-38-3Name: m-xylene | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000005867 | CAS Number: 108-88-3Name: Toluene | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000007071 | CAS Number: 123-86-4Name: n-butyl acetate | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000003109 | CAS Number: 78-83-1Name: Isobutyl alcohol | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000002316 | CAS Number: 64-17-5Name: ethanol | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000002147 | CAS Number: 60-00-4Name: EDTA | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000033687 | CAS Number: 7732-18-5Name: water | Included in the listed substance index, which is delivered with the software. |
| Compliance Requirement Version | ADR | Compliance Requirement ID:ADR | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | UNRTDG | Compliance Requirement ID: UNRTDG | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | IMDG-Code | Compliance Requirement ID: IMDG-Code | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | IATA-DGR | Compliance Requirement ID: IATA-DGR | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | RID | Compliance Requirement ID: RID | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | ADN | Compliance Requirement ID: ADN | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | 49 CFR | Compliance Requirement ID: 49 CFR | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | TDG | Compliance Requirement ID: TDG | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | ADG | Compliance Requirement ID: ADG | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | NZS 5433 | Compliance Requirement ID: NZS 5433 | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | ANTT | Compliance Requirement ID: ANTT | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | NOM | Compliance Requirement ID: NOM | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | NCh382 | Compliance Requirement ID: NCh382 | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | SANS 10228 | Compliance Requirement ID: SANS 10228 | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Purpose | Transport in EU | The following compliance requirements are assigned:UNRTDGIMDG-CodeIATA-DGRADRRIDAND | Requirements are relevant for Europe.Loaded and activated via scope item. |
| Compliance Purpose | Transport in North America | The following compliance requirements are assigned:49 CFRIATA-DGRIMDG-CodeNOMTDG | Requirements are relevant for North America.Loaded and activated via scope item. |
| Compliance Purpose | Transport in South America | The following compliance requirements are assigned:ANTTIATA-DGRIMDG-CodeNCh382UNRTDG | Requirements are relevant for South America.Loaded and activated via scope item. |
| Compliance Purpose | Transport in Middle East, Africa, Asia | The following compliance requirements are assigned:ADGIATA-DGRIMDG-CodeNZS 5433SANAS 10228UNRTDG | Requirements are relevant for Middle East, Africa, Asia.Loaded and activated via scope item. |
| Company Substance | m-xylene | Linked with listed substance L00000005806 | Loaded via scope item. |
| Company Substance | Toluene | Linked with listed substance L00000005867 | Loaded via scope item. |
| Company Substance | n-butyl acetate | Linked with listed substance L00000007071 | Loaded via scope item. |
| Company Substance | Isobutyl alcohol | Linked with listed substance L00000003109 | Loaded via scope item. |
| Company Substance | ethanol | Linked with listed substance L00000002316 | Loaded via scope item. |
| Company Substance | EDTA | Linked with listed substance L00000002147 | Loaded via scope item. |
| Company Substance | water | Linked with listed substance L00000033687 | Loaded via scope item. |
| Sold-to Party (Customer) | 33100003 | Domestic UAE Customer 3 | For the sales order with materials FGPCDG01, FGPCDG02, and FGPCDG03. |
| Ship-to Party (Customer) | 33100003 | Domestic UAE Customer 3 | For the sales order with materials FGPCDG01, FGPCDG02, and FGPCDG03. |
| Payer (Customer) | 33100003 | Customer domestic 03 | For the sales order with materials FGPCDG01, FGPCDG02, and FGPCDG03. |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Delivery Plant | 3310 | Plant 1 AE | id |

Data Set 1

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SGPCDG01 | Material Number: SGPCDG01Material Type: HALBMaterial Description: Semi Finished Good DG01 | Loaded via scope item. |
| Material | FGPCDG01 | Material Number: FGPCDG01Material Type: FERTMaterial Description: Finished Good DG 5l | Loaded via scope item. |
| Material | FGPCDG02 | Material Number: FGPCDG02Material Type: FERTMaterial Description: Finished Good DG 40l | Loaded via scope item. |
| Chemical Compliance Info Object - Unpackaged Product - Basic Data | Unpackaged Product UPDG10 | Internal Name: Unpackaged Product DG01Assigned Unpackaged Product: SGPCDG01Assigned Packaged Products:FGPCDG01FGPCDG02Assigned Application: Industrial Chemicals | Loaded via scope item. |
| Chemical Compliance Info Object - Unpackaged Product - Released Analytical Composition | Unpackaged Product UPDG10 | Substance: m-xyleneCAS Number: 108-38-3Role in Composition: Active IngredientReaction Product: NoConcentration: 48.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: tolueneCAS Number: 108-88-3Role in Composition: Active IngredientReaction Product: NoConcentration: 14.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: n-butyl acetateCAS Number: 123-86-4Role in Composition: Active IngredientReaction Product: NoConcentration: 12.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: Isobutyl alcoholCAS Number: 78-83-1Role in Composition: SolventReaction Product: NoConcentration: 12.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: ethanolCAS Number: 64-17-5Role in Composition: Active IngredientReaction Product: NoConcentration: 10.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: EDTACAS Number: 60-00-4Role in Composition: Active IngredientReaction Product: NoConcentration: 4.000000Lower Limit: 0.000000Upper Limit: 0.000000 | Loaded via scope item. |

Data Set 2

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SGPCDG02 | Material Number: SGPCDG02Material Type:HALBMaterial Description: Semi Finished Good DG02 | Loaded via scope item. |
| Material | FGPCDG03 | Material Number: FGPCDG03Material Type:FERTMaterial Description: Finished Good no DG | Loaded via scope item. |
| Chemical Compliance Info Object - Unpackaged Product - Basic Data | Unpackaged Product UPDG20 | Internal Name: Unpackaged Product DG02Assigned Unpackaged Product:SGPCDG02Assigned Packaged Product: FGPCDG03Assigned Application: Industrial ChemicalsNo Assigned Compliance Purposes | Loaded via scope item. |
| Chemical Compliance Info Object - Unpackaged Product - Released Analytical Composition | Unpackaged Product UPDG20 | Substance: waterCAS Number: 7732-18-5Role in Composition: Active IngredientReaction Product: NoConcentration: 82.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: ethanolCAS Number: 64-17-5Role in Composition: Active IngredientReaction Product: NoConcentration: 3.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: EDTACAS Number: 60-00-4Role in Composition: Active IngredientReaction Product: NoConcentration: 15.000000Lower Limit: 0.000000Upper Limit: 0.000000 | Loaded via scope item. |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNT | Create Product Master of Type Finished Good |
| BNS | Create Product Master of Type Semi-Finished Good |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3FC - Assess Dangerous Goods for a Product | You have implemented and tested scope item 3FC. |
| BD9 - Sell from Stock | You have implemented and tested scope item BD9. |

|  |
| --- |
| Note To be able to ship dangerous goods within a country/region, transport check rules must have been set in scope item 3FC for this country/region. In this scope item, the check rule Classification Dependent or Always Allowed must have been set for at least one domestic mode of transport for this country/region. Otherwise, the system blocks the processing of sales and delivery documents even if the transport for this product is allowed according to its dangerous goods classification.How to set transport check rules, see test procedure Optional: Apply Regulations to Countries for scope item 3FC. |

### Preliminary Steps

In this section, you find the steps that you need to carry out before you start the procedures in this test script.

#### Post Goods Movement

Use

To test this scope item, the used materials must be available in stock.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Post Goods Movement (MIGO) app. | The initial screen of the app is displayed. |  |
| 3 | Select Action and Referenced Documents | Make the following entries and choose Enter:Trans./Event: Goods ReceiptReference Document: Other | The Goods Receipt Other screen is displayed. |  |
| 4 | Select Material | In the Good Receipt Other screen on the Material tab, enter material FGPCDG01 in the Material field and press Enter. | The material is entered in the first line of the table in the General section. |  |
| 5 | Enter Quantity | On the Quantity tab, enter the following data and choose Enter:Qty in Unit of Entry: 100Unit of Entry: BT | The quantity is added in the first line of the table in the General section. |  |
| 6 | Input on the Goods Receipt Other Screen: Where Tab | On the Where tab, enter the following data and press Enter:Movement Type:561 - Receipt per initial entry of stock balances into unrestricted usePlant: 3310Storage Location: 331A | The movement type, plant, and storage location are added in the first line of the table in the General section. |  |
| 7 | Save Your Entries | Choose Post. | Material FGPCDG01 is added to stock. |  |
| 8 | Add Other Materials to Stock | Repeat steps 4–7 for material FGPCDG02. | Material FGPCDG02 is added to stock. |  |

#### Check Assigned Dangerous Goods Regulations and Transport Check Rules for Countries/Regions

Use

When you transport dangerous goods into another country/region, you must comply with the dangerous goods regulations valid for this country/region. Compliance involves ensuring that the transport of a dangerous good is allowed for the mode of transport you are using and that the dangerous goods documents are available in the required languages.

For all countries/regions where packaged products are intended to be shipped from or shipped to, the Dangerous Goods Specialist - Product Compliance has to set rules for dangerous goods checks that are carried out in business documents within the value chain, such as sales orders or outbound deliveries. If no valid regulations are assigned or if the transport permission is not set to Always Allowed, the system blocks further processing of the business documents.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Dangerous Goods Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Dangerous Goods Management section, open the Apply Regulations - Dangerous Goods (F3916) app. | The Apply Regulations - Dangerous Goods screen is displayed and shows a world map.Depending on the color of the country/region in which you want to transport your product, proceed with one of the following steps:If the country/region in which you want to transport your product is colored green, dangerous goods regulations and check rules are already assigned. No further actions need to be taken.If all countries/regions are colored gray, it indicates that the regulations were not prefilled. To prefill the assignments for all countries/regions, proceed with step 3.If the country/region in which you want to transport your product is colored gray or orange, it indicates that no or not all dangerous goods regulations are assigned. To assign the applicable regulations and check rules, proceed with step 4. |  |
| 3 | Prefill Regulations for Countries/Regions | Choose the Prefill Regulations for Countries button and, in the Prefill Applicable Dangerous Goods Regulations and Languages for Countries/Regions popup, choose OK | The system prefills countries with the applicable dangerous goods regulations for the relevant modes of transport. In addition, the system also prefills the required languages tables.After the data is filled into the corresponding database table, the color of the country/region with prefilled data changes from gray to orange or green. |  |
| 4 | Assign Dangerous Goods Regulations and Check Rules to Countries/Regions | Select a gray country/region in which you want to transport your product and set the transport rules to Regulation Dependent, as follows:On the right side of the screen, in the Transport Check Rules section, select a mode of transport.From the Specify Check Rule dropdown menu, select Regulation Dependent.In the Select Regulation screen, select the regulation that you want to assign to the selected mode of transport.In the Regulation screen, select the official languages and save your entries.Select the Display Languages link and choose Edit. Specify additional languages for departure countries/regions and for destination countries/regions and choose Save.Note Carry out these steps for all modes of transport. | On the right side of the screen, the Transport Check Rules are displayed for the selected county/region with the check rule set to Always Forbidden.After you have assigned the check rules with the applicable dangerous goods regulations, the country/region is colored green. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order with a Dangerous Good with Transport Allowed](#unique_11) [page ] 17 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order with dangerous good FGPCDG01 is created. |
| [Create Outbound Delivery with a Dangerous Good with Transport Allowed](#unique_12) [page ] 20 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The outbound delivery with dangerous good FGPCDG01 is created. |
| [Carry Out Picking and Post Goods Issue for a Dangerous Good with Transport Allowed](#unique_13) [page ] 21 | Shipping Specialist | Pick Outbound Delivery (F0868) and Display Outbound Delivery (VL03N) | Picking and post goods issue are carried out for dangerous good FGPCDG01.Afterwards, the delivery note for the delivery with dangerous good FGPCDG01 is printed with dangerous goods descriptions. |
| [Create Sales Order with a Dangerous Good with Transport Allowed with Restrictions](#unique_14) [page ] 22 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order with dangerous good FGPCDG02 is created. |
| [Analyze Sales Order Status for Dangerous Goods](#unique_15) [page ] 25 | Internal Sales Representative | Manage Sales Orders (F1873) | The dangerous goods status for the sales order header and for the item is checked. |
| [Analyze Sales Order Fulfillment Monitor](#unique_16) [page ] 26 | Internal Sales Representative | Sales Order Fulfillment - Analyze and Resolve Issues (F0029A) | You navigate to the Compliance Information - For Products (F3226) app to view the transport permission and dangerous goods data for the item with issues. |
| [Create Outbound Delivery with a Dangerous Good with Transport Allowed with Restrictions](#unique_17) [page ] 28 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The outbound delivery with dangerous good FGPCDG02 is created. |
| [Analyze Outbound Delivery Status for Dangerous Goods](#unique_18) [page ] 29 | Shipping Specialist | Change Outbound Delivery (VL02) | The dangerous goods status for the delivery header and for the item is checked. |
| [Carry Out Picking and Post Goods Issue for a Dangerous Good with Transport Allowed with Restrictions](#unique_19) [page ] 30 | Shipping Specialist | Pick Outbound Delivery (F0868) and Display Outbound Delivery (VL03N) | Picking and post goods issue are carried out for dangerous good FGPCDG02.Afterwards, the delivery note for the delivery with dangerous good FGPCDG02 is printed with dangerous goods descriptions. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Documents Containing Dangerous Goods with Transport Allowed

#### Create Sales Order with a Dangerous Good with Transport Allowed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative creates a sales order for a finished good. The system carries out a dangerous goods check to verify if the transport is allowed. The result of the dangerous goods check is positive and the status for the dangerous goods check in the sales order header is set accordingly. The delivery for this sales order can be created.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Sales Orders (F1873) app. | The Manage Sales Orders screen is displayed. |  |
| 3 | Create Sales Order | Choose Create > Create Sales Order - VA01. | The screen where you create a sales order is displayed. |  |
| 4 | Enter Basic Order Data | On the Create Sales Documents screen, enter the following data and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The screen where you enter the standard order attributes is displayed. |  |
| 5 | Enter Detailed Order Data | On the Create Standard Order: Overview screen, enter the following data and press Enter:Sold-To Party: Enter a sold-to party starting with 3310, such as 33100003Ship-To Party: Enter a ship-to party starting with 3310, such as 33100003Cust. Reference: 123456Cust. Ref. Date: <Select today's date>Delivery Plant: 3310Order Reason: Sales CallNote You may need to scroll down within the Sales tab to access this field. | The screen is displayed with updated data. |  |
| 6 | Display Header Details | On the Create Standard Order: Overview screen, go to Menu > Goto > Header > Shipping . | The Shipping tab in the header details is displayed. |  |
| 7 | Select Shipping Type | Set the Shipping Cond. to Pick-up. | The screen is displayed with updated data. |  |
| 8 | Go Back | Navigate back. | The Create Standard Order: Overview screen is displayed. |  |
| 9 | Enter Order Item | In the All Items table, enter the following data for the first sales order item and press Enter:Material: FGPCDG01Quantity: 1Un (Sales Unit): BTDouble-click in the row for the sales order item. On the Country/Region tab, if available, enter 00 as the tax code. If there’s no Country/Region tab, navigate back to Create Standard Order: Overview. | The item is added to the standard order.In the footer, the system shows a message that errors occurred. |  |
| 10 | Save Entries | Choose Save.Note the sales order number: ________________. | The sales order is saved and the order number is shown in the footer.If there are any issues, the Display Logs dialog opens and displays message for the issues. |  |
| 11 | Access App | Open the Manage Sales Orders (F1873) app again. | The Manage Sales Orders screen is displayed. |  |
| 12 | Search Sales Order | In the Sales Order field, enter the number of the newly created sales order (see step 10) and choose Go. | The Manage Sales Orders screen shows the sales order. |  |
| 13 | Select the Sales Order | Navigate to the details of this sales order by choosing the <!-- image omitted: unnamed -->(Details) icon. | The Display Standard Order xxxxx: Overview screen is displayed. |  |
| 14 | Display Order Confirmation | Choose Header Output Preview. | The Display Standard Order xxxxx: Output screen is displayed. |  |
| 15 | Select Order Confirmation | Select the entry with the following data:Status: CompletedOutput Type: ORDER_CONFIRMATIONChannel: PRINTChoose Display Document. | The order confirmation is displayed as a PDF document. |  |
| 16 | Check Descriptions | On the PDF document, check for the dangerous goods descriptions that you have entered for the product while testing scope item Assess Dangerous Goods for a Product (3FC). | The dangerous goods information is displayed in the order confirmation.Here is an example of how the description should look:Example IMDG-Code: UN 1993, Flammable Liquid, n.o.s. (Xylene, Toluene), 3, IIFiberboard Box X 5 L |  |
| 17 | Close Order Confirmation | Choose Continue. | The order confirmation is closed. |  |
| 18 | Go Back | Navigate back. | The Display Standard Order xxxxx: Overview screen is displayed. |  |

#### Create Outbound Delivery with a Dangerous Good with Transport Allowed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Based on the sales order, the Shipping Specialist creates the outbound delivery.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Create Outbound Deliveries - From Sales Orders (F0869A) app. | The Create Outbound Deliveries screen is displayed. |  |
| 3 | Search Sales Order | Enter the following data and press Enter:Shipping Point: 3310Planned Creation Date: <Due Up Until Next Week>Sales Document: <Enter the previously created sales order number> | The screen shows the sales order with one item. |  |
| 4 | Create Delivery | Select the checkbox for your sales order item and choose Create Deliveries. | The delivery is created. |  |
| 5 | Analyze Delivery Logs | Choose Display Log and note the delivery number displayed in the Delivery column under Deliveries: ________________. | The Analyze Delivery Logs screen is displayed. |  |

#### Carry Out Picking and Post Goods Issue for a Dangerous Good with Transport Allowed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative carries out the picking process. It involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. In addition, the Internal Sales Representative also posts the goods issues for the delivery.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Pick Outbound Delivery (F0868) app. | The Delivery screen is displayed. |  |
| 3 | Pick Outbound Delivery | On the Delivery screen, enter the number of the delivery that you have created in step 5 of [Create Outbound Delivery with a Dangerous Good with Transport Allowed](#unique_12) [page ] 20 and choose Enter. | The Pick Outbound Delivery screen is displayed. |  |
| 4 | Enter Picked Quantity | Select the checkbox for item, and in the Picking Quantity field, enter the same quantity that you have entered as delivery quantity. Choose Save. | The Pick Outbound Delivery screen is displayed with updated data.The Picking Status changed to Completely Processed. |  |
| 5 | Post Good Issue | Choose Post GI. | The goods issue is posted for the delivery.The status has changed from Ready to Post GI to GI Posted. |  |
| 6 | Navigate to Launchpad | Choose the Home button. | The SAP Fiori launchpad is displayed. |  |
| 7 | Access App | Open the Display Outbound Delivery (VL03N) app. | The Display Outbound Delivery screen is displayed. |  |
| 8 | Issue Delivery Output | On the Display Outbound Delivery screen, enter your delivery number and choose Continue.From the Delivery xxxxxxxx Display: Overview screen, go to More > Extras > Delivery Output > Output Control. | The Delivery: Output screen is displayed. |  |
| 9 | Print Preview | On the Delivery: Output screen, select the line with the output type DELIVERY_NOTE and choose Display Document. | A preview of the print document is displayed. |  |
| 10 | Check Descriptions | On the PDF document, check the dangerous goods descriptions. | The same dangerous goods information is displayed on the delivery note as on the order confirmation.Here is an example of how the description should look:Example IMDG-Code: UN 1993, Flammable Liquid, n.o.s. (Xylene, Toluene), 3, IIFiberboard Box X 5 L |  |
| 11 | Print Delivery Note | From the preview of the document, choose the Print icon, select your local destination, and then print the document. | The delivery note is printed. |  |

### Create Sales Documents Containing Dangerous Goods with Transport Allowed with Restrictions

#### Create Sales Order with a Dangerous Good with Transport Allowed with Restrictions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative creates a sales order for a finished good. The system carries out a dangerous goods check to verify if the transport is allowed. The dangerous goods check ends with a warning and the status for dangerous goods check in the sales order header is set accordingly. However, the delivery for this sales order can be created.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Sales Orders (F1873) app. | The Manage Sales Orders screen is displayed. |  |
| 3 | Create Sales Order | Choose Create > Create Sales Order - VA01 . | The screen where you create a sales order is displayed. |  |
| 4 | Enter Basic Order Data | On the Create Sales Documents screen, enter the following data and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The screen where you enter the standard order attributes is displayed. |  |
| 5 | Enter Detailed Order Data | On the Create Standard Order: Overview screen, enter the following data and press Enter:Sold-To Party: Enter a sold-to party starting with 3310, such as 33100003Ship-To Party: Enter a ship-to party starting with 3310, such as 33100003Cust. Reference: 123456Cust. Ref. Date: <Select today's date>Delivery Plant: 3310>Order Reason: Sales CallNote You may need to scroll down within the Sales tab to access this field. | The screen is displayed with updated data. |  |
| 6 | Display Header Details | On the Create Standard Order: Overview screen, go to Menu > Goto > Header > Shipping . | The Shipping tab in the header details is displayed. |  |
| 7 | Select Shipping Type | Set the Shipping Cond. to Pick-up. | The screen is displayed with updated data. |  |
| 8 | Go Back | Navigate back. | The Create Standard Order: Overview screen is displayed. |  |
| 9 | Enter Order Item | In the All Items table, enter the following data for the first sales order item and press Enter:Material: FGPCDG02Quantity: 1Un (Sales Unit): BTDouble-click in the row for the sales order item. On the Country/Region tab, if available, enter 00 as the tax code. If there’s no Country/Region tab, navigate back to Create Standard Order: Overview. | The item is added to the standard order.In the footer, the system shows a message that errors occurred. |  |
| 10 | Save Entries | Choose Save.Note the sales order number: ________________.In the Display Logs dialog, check the message for dangerous goods issues and choose Continue. | The sales order is saved and the order number is shown in the footer.The Display Logs screen is displayed with the message that transportation of product FGPCDG02 is allowed with restrictions. |  |
| 11 | Access App | Open the Manage Sales Orders (F1873) app again. | The Manage Sales Orders screen is displayed. |  |
| 12 | Search Sales Order | In the Sales Order field, enter the number of the newly created sales order (see step 12) and choose Go. | The Manage Sales Orders screen shows the sales order. |  |
| 13 | Select the Sales Order | Navigate to the details of this sales order by choosing the <!-- image omitted: unnamed -->(Details icon. | The Display Standard Order xxxxx: Overview screen is displayed. |  |
| 14 | Display Order Confirmation | Choose Header Output Preview. | The Create Standard Order xxxxx: Output screen is displayed. |  |
| 15 | Select Order Confirmation | Select the entry with the following data:Output Type: ORDER_CONFIRMATIONChannel: PRINTChoose Display Document. | The order confirmation is displayed as a PDF document. |  |
| 16 | Check Descriptions | On the PDF document, check that there are the dangerous goods descriptions that you have entered for the product while testing scope item Assess Dangerous Goods for a Product (3FC). | The dangerous goods information is displayed in the order confirmation.Here is an example of how the description should look:Example IMDG-Code: UN 1993, Flammable Liquid, n.o.s. (Xylene, Toluene), 3, IIFiberboard Box X 5 L |  |
| 17 | Close Order Confirmation | Choose Continue. | The order confirmation is closed. |  |
| 18 | Go Back | Navigate back. | The Display Standard Order xxxxx: Overview screen is displayed. |  |

#### Analyze Sales Order Status for Dangerous Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative created a sales order for a finished good. The dangerous goods check ended with a warning and the system set the dangerous goods status on item level and header level accordingly. The Internal Sales Representative checks the status to determine if further action, such as triggering a dangerous goods assessment, is needed.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Sales Orders (F1873) app. | The Manage Sales Orders screen is displayed. |  |
| 3 | Search for Sales Order | Enter the number of the previously created sales order (see step 12 of [Create Sales Order with a Dangerous Good with Transport Allowed with Restrictions](#unique_14) [page ] 22) in the Sales Order field and choose Go.Note that if the header of the sales order list is not expanded, expand the header by choosing <!-- image omitted: unnamed -->(Expand Header). | The list is filtered and only the previously created sales order is displayed. |  |
| 4 | Display Sales Order | Choose the line for your previously created sales order. | The Display Sales Order - VA03 screen opens and displays the sales order. |  |
| 5 | Navigate to Header Status | Go to Menu > Goto > Header > Status . | The Display Standard Order xxxxx: Header Data screen opens and displays the header data. |  |
| 6 | Check Dangerous Goods Status | In the Processing Status section, check the Dangerous Goods Sts field. | The dangerous goods status for the sales order is Warning – Dangerous Goods Transport Restricted. |  |
| 7 | Navigate back to the Overview | Go to Menu > Goto > Overview (F3) . | The Display Standard Order xxxxx: Overview screen opens again and displays the sales order. |  |
| 8 | Navigate to Item Status | Go to Menu > Goto > Item > Status . | The Display Standard Order xxxxx: Item Data screen opens and displays the item data. |  |
| 9 | Check Dangerous Goods Status | In the Processing Status section, check the status in the Dangerous Goods Status field. | The dangerous goods status for the item is Warning – Transport Restricted. |  |

#### Analyze Sales Order Fulfillment Monitor

Purpose

The Internal Sales Representative analyzes sales documents based on the given issues types. Dangerous Goods issues are visualized in the Delivery Block in Sales Orders and Delivery Issue in Sales Orders issue types.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Under Internal Sales, Insights, open Sales Order Fulfillment - Analyze and Resolve Issues (F0029A) app. | The analytic list page for orders with issues is displayed. |  |
| 3 | Search for Dangerous Goods Issues | Switch the header filter view by choosing the <!-- image omitted: unnamed -->(Compact Filter) icon.Choose Adapt Filter. Select the Dangerous Goods Status filter attribute, and then choose OK.For the Dangerous Goods Status filter, select the following values:Warning – Dangerous Goods Transport RestrictedPartially Blocked – Dangerous Goods Transport ForbiddenBlocked – Dangerous Goods Transport ForbiddenConfirm the new filter settings by choosing Go. | The list is filtered for any sales documents with dangerous goods issues. |  |
| 4 | Select Status Values for Display | Choose the <!-- image omitted: unnamed -->(Settings) icon for the table with the sales documents with issues.Select the checkbox for the Dangerous Goods Status column if it is not already selected, and then choose OK. | The table shows the dangerous goods header status for the sales documents. |  |
| 5 | Select the Sales Order | Search for the sales order from the previous test procedure and navigate to its details by choosing the <!-- image omitted: unnamed -->(Details) icon. | The Track Sales Order Details app is displayed. |  |
| 6 | Navigate to the Compliance Information - For Products App | To display the compliance information for a product, proceed as follows:In the Fulfillment Standard Order XXXXX subpage, go to the Items tab.In the Items Processing Details table, select the hyperlink for the material.On the Link popup, choose More Links to display all possible navigation targets.On the Define Link List screen, select Display Compliance Information for Products and choose OK. | The Display Compliance Information for Products link is visible for navigation. |  |
| 7 | Display Compliance Information | Choose the Display Compliance Information for Products link to display the compliance information for the product that is assigned to the material of the item.If an information popup is displayed, confirm it by choosing OK. | The Compliance Information - For Products (F3226) app opens. |  |
| 8 | Display Compliance Information for Dangerous Goods | Go to the Dangerous Goods tab to display the dangerous goods information. | On the Dangerous Goods tab on the Compliance Information - For Products screen, a map with transport permission information for the packaged product that is assigned to the material of the item is displayed. |  |
| 9 | Expand the Legend | In the Legend list panel, choose the <!-- image omitted: unnamed -->(Expand/Collapse) icon to get more information about the coloring of the countries/regions in the map. | The panel expands and displays information on the coloring of the countries/regions in the map. |  |
| 10 | Expand the Dangerous Goods Details | in the Dangerous Goods Details panel, choose the <!-- image omitted: unnamed -->(Expand/Collapse) icon to view classification data. | The panel expand and displays the Classified As information and the UN Number for the packaged product. |  |
| 11 | Check the Transport Permissions for International Modes of Transport. | In the International Transport panel, check the transport permissions for the international modes of transport. | The panel expands and displays the transport permissions for the international modes of transport. |  |
| 12 | Check the Transport Permissions for Domestic Modes of Transport. | Select the country/region where you ship the product from or to, to display the transport permissions for the domestic modes of transports. | The Domestic Transport dialog for the selected country/region is displayed with information about the transport permissions for the domestic modes of transport. If a dangerous goods regulation is assigned to the mode of transport, it is also displayed. |  |

#### Create Outbound Delivery with a Dangerous Good with Transport Allowed with Restrictions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Based on the sales order, the Shipping Specialist creates the outbound delivery.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Create Outbound Deliveries - From Sales Orders (F0869A) app. | The Create Outbound Deliveries screen is displayed. |  |
| 3 | Search Sales Order | Enter the following data and press Enter:Shipping Point: 3310Planned Creation Date: <Select today>Sales Document: <Enter the previously created sales order number> | The screen shows the sales order with one item. |  |
| 4 | Create Delivery | Select the checkbox for your sales order item and choose Create Deliveries. | The delivery is created. |  |
| 5 | Analyze Delivery Logs | Choose Display Log and note the delivery number: ________________. | The Analyze Delivery Logs screen is displayed. |  |

#### Analyze Outbound Delivery Status for Dangerous Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Shipping Specialist created an outbound delivery from a sales order for a finished good. The dangerous goods check ended with a warning and the system set the dangerous goods status on item level and header level accordingly. The Shipping Specialist checks the status to determine if further action, such as triggering a dangerous goods assessment, is needed.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed. |  |
| 3 | Display Delivery | In the Outbound Delivery field, enter the number of the previously created outbound delivery (see step 5 of [Create Outbound Delivery with a Dangerous Good with Transport Allowed with Restrictions](#unique_17) [page ] 28) and choose Continue. | The Delivery xxxxxxxx Change: Overview screen opens and displays the outbound delivery. |  |
| 4 | Navigate to Header Status | Go to Menu > Go to > Header > Processing . | The Delivery xxxxxxxx Change: Header Details screen opens and displays the overall status data. |  |
| 5 | Check Dangerous Goods Status | In the Overall Status section, check the status in the Dangerous Goods field. | The dangerous goods status for the delivery is Warning – Dangerous Goods Transport Restricted. |  |
| 6 | Navigate back to the Overview | Go to Menu > Go to > Overview . | The Delivery xxxxxxxx Change. Overview screen opens again and displays the overview data. |  |
| 7 | Navigate to Item Status | Go to Menu > Go to > Item > Processing . | The Delivery xxxxxxxx Change: Item Details screen opens and displays the item status data. |  |
| 8 | Check Dangerous Goods Status | In the Item Status section, check the status in the Dangerous Goods field. | The dangerous goods status for the item is Warning – Transport Restricted. |  |

#### Carry Out Picking and Post Goods Issue for a Dangerous Good with Transport Allowed with Restrictions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative carries out the picking process. It involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. In addition, the Internal Sales Representative also posts the goods issues for the delivery.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Pick Outbound Delivery (F0868) app. | The Delivery screen is displayed. |  |
| 3 | Pick Outbound Delivery | On the Delivery screen, enter the number of the delivery that you have created in step 5 of [Create Outbound Delivery with a Dangerous Good with Transport Allowed with Restrictions](#unique_17) [page ] 28 and choose Enter. | The Pick Outbound Delivery screen is displayed. |  |
| 4 | Enter Picked Quantity | Select the item and, in the Picking Quantity field, enter the same quantity that you have entered as delivery quantity. Choose Save. | The Pick Outbound Delivery screen is displayed with updated data.The Picking Status changed to Completely Processed. |  |
| 5 | Post Good Issue | choose Post GI. | The goods issue is posted for the delivery.The status has changed from Ready to Post GI to GI Posted. |  |
| 6 | Navigate to Launchpad | Choose the Home button. | The SAP Fiori launchpad is displayed. |  |
| 7 | Access App | Open the Display Outbound Delivery (VL03N) app. | The Display Outbound Delivery screen is displayed. |  |
| 8 | Issue Delivery Output | On the Display Outbound Delivery screen, enter your delivery number and choose Continue.From the Delivery Change: Overview screen, go to More > Extras > Delivery Output > Output Control. | The Delivery: Output screen is displayed. |  |
| 9 | Print Preview | On the Delivery: Output screen, select the line with the output type DELIVERY_NOTE and choose Display Document. | A preview of the print document is displayed.The same dangerous goods information is displayed on the delivery note as on the order confirmation. |  |
| 10 | Print Delivery Note | From the preview of the document, choose the Print icon. | The delivery note is printed. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/assess-dangerous-goods-for-a-product-3fc-ae-test-script-933]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3G8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 57,734 chars in the whole document
