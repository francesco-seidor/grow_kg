---
id: 13-quality-ehs-and-compliance/assess-dangerous-goods-for-a-product-3fc-ae-test-script-933
title: Assess Dangerous Goods for a Product (3FC_AE) - Test Script (3FC_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3FC: classifying products as dangerous goods or not, and applying regulations to countries."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/dangerous-goods]
aliases: [3FC_S4CLD2608_BPD_EN_AE]
keywords: [Dangerous Goods Classification and Checks, dangerous goods classification, unpackaged products, packaged products, transport permission, no dangerous goods, country regulations, compliance purposes, business roles, test data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3FC_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-933
topic: 13-quality-ehs-and-compliance/dangerous-goods
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Assess Dangerous Goods for a Product (3FC_AE) - Test Script (3FC_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3FC_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Dangerous Goods Classification and Checks** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Assess Dangerous Goods for a Product (3FC_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Assess Dangerous Goods for a Product (3FC_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852488)

[2 Prerequisites 5](#_Toc232852489)

[2.1 System Access 5](#_Toc232852490)

[2.2 Roles 5](#_Toc232852491)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232852492)

[2.4 Business Conditions 12](#_Toc232852493)

[3 Overview Table 14](#_Toc232852494)

[4 Test Procedures 16](#_Toc232852495)

[4.1 Classify Product as Dangerous Goods 16](#_Toc232852496)

[4.1.1 Optional: Check Compliance Relevance for Dangerous Good 16](#_Toc232852497)

[4.1.2 Check Assigned Materials, Package Products, and Compliance Purposes for Unpackaged Products 17](#_Toc232852498)

[4.1.3 Classify Unpackaged Products as Dangerous Goods 18](#_Toc232852499)

[4.1.4 Classify Packaged Products as Dangerous Goods 20](#_Toc232852500)

[4.1.4.1 Classify Packaged Products with All Modes of Transport Allowed 20](#_Toc232852501)

[4.1.4.2 Classify Packaged Products with One Mode of Transport Forbidden 22](#_Toc232852502)

[4.2 Classify Product as No Dangerous Goods 24](#_Toc232852503)

[4.2.1 Optional: Check Compliance Relevance for Non-Dangerous Good 24](#_Toc232852504)

[4.2.2 Check Assigned Materials, Packaged Products, and Compliance Purpose for Unpackaged Products 25](#_Toc232852505)

[4.2.3 Classify Unpackaged Products as No Dangerous Good 26](#_Toc232852506)

[4.2.4 Classify Packaged Products as No Dangerous Good 28](#_Toc232852507)

[4.3 Optional: Apply Regulations to Countries/Regions 29](#_Toc232852508)

[5 Appendix 32](#_Toc232852509)

[5.1 Process Integration 32](#_Toc232852510)

[5.1.1 Preceding Processes 32](#_Toc232852511)

[5.1.2 Succeeding Processes 32](#_Toc232852512)

## Purpose

Overview

This scope item supports the classification of products according to dangerous goods regulations.

When a product is intended to be transported, the product steward specialist assigns compliance purposes to the product. These compliance purposes specify the dangerous goods regulations that are relevant for the transport of the product. You, as a dangerous goods specialist, are responsible to assess the product. If the product is a dangerous good, you classify it according to the applicable dangerous goods regulations and determine whether the transport of this product is allowed in a certain country/region by the certain mode of transport. During the classification process, the system generates the dangerous goods description with rules that are specified for each dangerous goods regulation. This description can be printed on documents, such as sales order confirmations and delivery notes.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

Test Data

In the test procedures, the following products with the following dangerous goods data are used:

| Product | Classified As | Transport Permission |
| --- | --- | --- |
| Semi Finished Good DG01 (SGPCDG01) | Dangerous Goods | Transport allowed |
| Finished Good DG 5l (FGPCDG01) | Dangerous Goods | Transport allowed |
| Finished Good DG 40l (FGPCDG02) | Dangerous Goods | Transport allowed with restrictions |
| Semi Finished Good DG02 (SGPCDG02) | No Dangerous Goods | Transport allowed |
| Finished Good no DG (FGPCDG03) | No Dangerous Goods | Transport allowed |

Further Information on the Test Procedure

Assignment of a Compliance Purpose

The process for the dangerous goods assessment of a product starts with the determination of the dangerous goods-relevant compliance purposes for an unpackaged product. The Product Stewardship Specialist - Product Compliance assigns a compliance purpose that covers the relevant dangerous goods regulations.

In the test procedures, the following data is used:

| Product | Compliance Purpose |
| --- | --- |
| Semi Finished Good DG01 (flammable liquid) (SGPCDG01) | Transport in EuropeTransport in North AmericaTransport in South AmericaTransport in Middle East, Africa, Asia |

Classification of an Unpackaged Product

By assigning a dangerous goods-relevant compliance purposes to the unpackaged product, the system creates classification requests for the unpackaged product. These classification requests can be processed in the My Unpackaged Dangerous Goods (F3643) app.

Starting with the My Unpackaged Dangerous Goods (F3643) app, the Dangerous Goods Specialist - Product Compliance uses different apps to assess and release the classification for the unpackaged product for each regulation. The released classifications can then be used as input for the dangerous goods assessment of the packaged product.

In the test procedures, the following data is used:

| Product | Dangerous Goods Regulation | Transport Permission |
| --- | --- | --- |
| Semi Finished Good DG01 (SGPCDG01) | All applicable regulations | Transport allowed |

Classification of a Packaged Product

After releasing the classifications for an unpackaged product, the Dangerous Goods Specialist uses the My Packaged Dangerous Goods (F3711) app as a starting point to assess and release the classifications for the assigned packaged products.

In the test procedures, the following data is used:

| Product | Dangerous Goods Regulation | Transport Permission |
| --- | --- | --- |
| Finished Good DG 5l (FGPCDG01) | All applicable regulations | Transport allowed |
| Finished Good DG 40l (FGPCDG02) | All applicable regulations (except IATA-DGR)IATA-DGR (Aircraft Cargo)IATA-DGR (Aircraft Passenger) | Transport allowedTransport allowedTransport forbidden |

The released dangerous goods classifications for a packaged product are used for dangerous goods checks in documents within the value chain (see scope item 3G8 - Dangerous Goods in the Value Chain).

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
| Dangerous Goods Specialist - Product Compliance | SAP_BR_DG_SPLST_PCL | Dangerous Goods | SAP_BR_DG_SPLST_PCL |  |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents products, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note If you create your own packaged and unpackaged products, carry out the compliance steps for all relevant solution areas using the test scripts for the scope items listed:Product Marketability: 31H (Assess Marketability of a Product)Safety Data Sheet Management: 3VR (Manage Safety Data Sheets for Products)The demo data described and used in the following is tailored for a smooth execution of the described procedures and suppresses processes of other solution areas in product compliance. |

Data valid for both test scenarios:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Listed Substance | L00000005806 | CAS Number: 108-38-3Name: m-xylene | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000005867 | CAS Number: 108-88-3Name: Toluene | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000007071 | CAS Number: 123-86-4Name: n-butyl acetate | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000003109 | CAS Number: 78-83-1Name: Isobutyl alcohol | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000002316 | CAS Number: 64-17-5Name: ethanol | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000002147 | CAS Number: 60-00-4Name: EDTA | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000033687 | CAS Number: 7732-18-5Name: water | Included in the listed substance index, which is delivered with the software. |
| Compliance Requirement Version | ADR | Compliance Requirement ID: ADR | Compliance requirement versions are delivered with the software.Activated via scope item. |
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
| Compliance Purpose | Transport in EU | The following compliance requirements are assigned:UNRTDGIMDG-CodeIATA-DGRADRRIDADN | Requirements are relevant for Europe.Loaded and activated via scope item. |
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

Data Set 1

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Product | SGPCDG01 | Product Number: SGPCDG01Product Type: HALBProduct Description: Semi Finished Good DG01Compliance Relevant: Yes | Loaded via scope item. |
| Product | FGPCDG01 | Product Number: FGPCDG01Product Type: FERTProduct Description: Finished Good DG 5lCompliance Relevant: Yes | Loaded via scope item. |
| Product | FGPCDG02 | Product Number: FGPCDG02Product Type: FERTProduct Description: Finished Good DG 40lCompliance Relevant: Yes | Loaded via scope item. |
| Chemical Compliance Info Object - Unpackaged Product - Basic Data | Unpackaged Product UPDG10 | Internal Name: Unpackaged Product DG01Assigned Unpackaged Product: SGPCDG01Assigned Packaged Products:FGPCDG01FGPCDG02Assigned Application: Industrial Chemicals | Loaded via scope item. |
| Chemical Compliance Info Object - Unpackaged Product - Released Analytical Composition | Unpackaged Product UPDG10 | Substance: m-xyleneCAS Number: 108-38-3Role in Composition: Active IngredientReaction Product: NoConcentration: 48.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: tolueneCAS Number: 108-88-3Role in Composition: Active IngredientReaction Product: NoConcentration: 14.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: n-butyl acetateCAS Number: 123-86-4Role in Composition: Active IngredientReaction Product: NoConcentration: 12.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: Isobutyl alcoholCAS Number: 78-83-1Role in Composition: SolventReaction Product: NoConcentration: 12.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: ethanolCAS Number: 64-17-5Role in Composition: Active IngredientReaction Product: NoConcentration: 10.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: EDTACAS Number: 60-00-4Role in Composition: Active IngredientReaction Product: NoConcentration: 4.000000Lower Limit: 0.000000Upper Limit: 0.000000 | Loaded via scope item. |

Data Set 2

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Product | SGPCDG02 | Product Number: SGPCDG02Product Type: HALBProduct Description: Semi Finished Good DG02Compliance Relevant: Yes | Loaded via scope item. |
| Product | FGPCDG03 | Product Number: FGPCDG03Product Type: FERTProduct Description: Finished Good no DGCompliance Relevant: Yes | Loaded via scope item. |
| Chemical Compliance Info Object - Unpackaged Product - Basic Data | Unpackaged Product UPDG20 | Internal Name: Unpackaged Product DG02Assigned Unpackaged Product: SGPCDG02Assigned Packaged Product: FGPCDG03Assigned Application: Industrial Chemicals | Loaded via scope item. |
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
| 31H - Assess Marketability of a Product | You have implemented and tested scope item 31H. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Optional: Check Compliance Relevance for Dangerous Good](#unique_8) [page ] 16 | Master Data Specialist - Product Data | Manage Product Master Data (F1602) | Unpackaged product SGPCDG01 and the packaged products FGPCDG01 and FGPCDG02 are relevant for compliance checks. |
| [Check Assigned Materials, Package Products, and Compliance Purposes for Unpackaged Products](#unique_9) [page ] 17 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | After setting the compliance purpose, new classification requests are created for each applicable dangerous goods regulation for the unpackaged product SGPCDG01 and the assigned package products FGPCDG01 and FGPCDG02. |
| [Classify Unpackaged Products as Dangerous Goods](#unique_10) [page ] 18 | Dangerous Goods Specialist - Product Compliance | My Unpackaged Dangerous Goods (F3643) | Unpackaged product SGPCDG01 is classified to one selected dangerous goods regulation as Methanol and the transport is allowed for this regulation. Then, the classification is applied to all other regulations. |
| [Classify Packaged Products with All Modes of Transport Allowed](#unique_11) [page ] 20 | Dangerous Goods Specialist - Product Compliance | My Packaged Dangerous Goods (F3711) | Packaged product FGPCDG01 is classified according to all applicable dangerous goods regulations as Methanol and the transport is allowed for all regulations. |
| [Classify Packaged Products with One Mode of Transport Forbidden](#unique_12) [page ] 22 | Dangerous Goods Specialist - Product Compliance | My Packaged Dangerous Goods (F3711) | With the exemption of IATA DGR, packaged product FGPCDG02 is classified according to all applicable dangerous goods regulations as Methanol and the transport is allowed for all regulations.For IATA DGR 2020, transport is forbidden for the Aircraft Passenger mode of transport. |
| [Optional: Check Compliance Relevance for Non-Dangerous Good](#unique_13) [page ] 24 | Master Data Specialist - Product Data | Manage Product Master Data (F1602) | Unpackaged product SGPCDG02 and packaged product FGPCDG03 are relevant for compliance checks. |
| [Check Assigned Materials, Packaged Products, and Compliance Purpose for Unpackaged Products](#unique_14) [page ] 25 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | After setting the compliance purpose, new classification requests are created for each applicable dangerous goods regulation for the unpackaged product SGPCDG02 and the assigned packaged product FGPCDG03. |
| [Classify Unpackaged Products as No Dangerous Good](#unique_15) [page ] 26 | Dangerous Goods Specialist - Product Compliance | My Unpackaged Dangerous Goods (F3643) | Unpackaged product SGPCDG02 is classified to one selected dangerous goods regulation as No Dangerous Goods and the transport is allowed for this regulation. Then, the classification is applied to all other regulations. |
| [Classify Packaged Products as No Dangerous Good](#unique_16) [page ] 28 | Dangerous Goods Specialist - Product Compliance | My Packaged Dangerous Goods (F3711) | Packaged product FGPCDG03 is classified according to all applicable dangerous goods as No Dangerous Goods regulations and the transport is allowed for all regulations. |
| [Optional: Apply Regulations to Countries/Regions](#unique_17) [page ] 29 | Dangerous Goods Specialist - Product Compliance | Apply Regulations - Dangerous Goods (F3916) | For all countries where packaged products should be shipped from or shipped to, transport check rules are set. These rules are used for dangerous goods checks that are carried out in sales and delivery documents. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Classify Product as Dangerous Goods

#### Optional: Check Compliance Relevance for Dangerous Good

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The compliance-relevant indicator in the product master ensures that the Product Stewardship Specialist - Product Compliance can assess the chemical compliance of the product and the Dangerous Goods Specialist - Product Compliance can classify the product according to dangerous goods regulations. The compliance relevant indicator can be set by the Master Data Specialist - Product Data.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | In the Master Data - Products section, open the Manage Product Master Data (F1602) app. | The initial screen of the app is displayed. |  |
| 3 | Search Product | Enter product SGPCDG01 into the Search field and choose Go. | The product is displayed in the Products list. |  |
| 4 | Select Product | Choose the line for product SGPCDG01. | The details view for the product is displayed. |  |
| 5 | Select the Product Compliance View | Select the Product Compliance tab. | The Product Compliance area for the product is displayed. |  |
| 6 | Check Product Compliance Relevance | Check that the Compliance Relevant field is set to Yes. | The product is compliance relevant. |  |
| 7 | Check Product Compliance Relevance for Further Products | Repeat test steps 3-6 for the following products:FGPCDG01FGPCDG02 | The products are compliance relevant. |  |

#### Check Assigned Materials, Package Products, and Compliance Purposes for Unpackaged Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance has assigned materials and related packaged products to an unpackaged product and to assign a compliance purpose that reflects transportation in countries in which the packaged product is to be transported. In this test procedure, you check the entered data.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Product Compliance section, open the Manage Basic Compliance Data - Unpackaged Products (F2641) app. | The Manage Basic Compliance Data - Unpackaged Product screen is displayed and shows the list of unpackaged products. |  |
| 3 | Search Unpackaged Product | Expand the header of the unpackaged products list by choosing <!-- image omitted: unnamed -->(Expand Header).Enter Semi Finished Good DG01 into the Search field and choose Enter. | The product is displayed in the Unpackaged Products list.Note If the product Semi Finished Good DG01 is not displayed in the list, search for Unpackaged Product UPDG10. |  |
| 4 | Navigate to Unpackaged Product - Basic Compliance Data | Choose the line for the product Semi Finished Good DG01. | The Unpackaged Product - Basic Compliance Data screen is displayed. |  |
| 5 | Check Assigned Related Products in Product Master | In the Assigned Products section, in the Related Products in Product Master subsection, check the assigned products. | Product SGPCDG01 (Semi Finished Good DG01) is assigned. |  |
| 6 | Check Assigned Related Packaged Products | In the Assigned Products section, in the Related Compliance Views subsection, check the assigned packaged products. | Packaged products FGPCDG01 (Finished Good DG01) and FGPCDG02 (Finished Good DG02) are assigned.Note If the packaged products are not assigned, assign them by choosing Create in the Related Compliance Views subsection. |  |
| 7 | Check Assigned Compliance Purposes | In the Applications, Markets and Purposes section in the Assigned Compliance Purposes subsection, check the assigned purposes. | The following dangerous goods relevant compliance purposes are assigned:Transport in EuropeTransport in North AmericaTransport in South AmericaTransport in Middle East, Africa, Asia |  |

#### Classify Unpackaged Products as Dangerous Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dangerous Goods Specialist - Product Compliance classifies an unpackaged product according to the versions of the assigned dangerous goods regulations and allows the transport for all the regulation versions.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Dangerous Goods Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Dangerous Goods section, open the My Unpackaged Dangerous Goods (F3643) app. | The My Unpackaged Dangerous Goods screen is displayed and shows a list of unpackaged products on the For My Responsible Unit tab page. |  |
| 3 | Search Unpackaged Dangerous Good | Enter product SGPCDG01 into the Search field. | The product is displayed in the Unpackaged Products list. |  |
| 4 | Select Unpackaged Dangerous Good | Choose the line for the product SGPCDG01. | The Classify Unpackaged Dangerous Good (F3642) app opens and displays the released analytical composition and a list with the versions or the assigned dangerous goods regulations. |  |
| 5 | Select Regulation Version | In the Basic Classification section, choose the line for a version of the ADR regulation. | The Classify Dangerous Good (F4465) app opens and displays the Dangerous Goods - Classification Details screen to edit the classification data for the selected regulation version.Note that the app ID (for example, F4465 for ADR) varies depending on the selected dangerous goods regulation. |  |
| 6 | Classify Unpackaged Product as Dangerous Goods | Choose Edit and, in the Classification section, select the following data.Classified As: Dangerous Goods | The Dangerous Good - Classification Details screen displays a field for the UN number and the dangerous goods basic description. |  |
| 7 | Select an UN Number | Choose the UN Number field and, in the search dialog, enter 1230.Select the entry for the UN number. | The Dangerous Good - Classification Details screen displays additional classification data for the selected UN number. |  |
| 8 | Check Dangerous Goods Basic Description | In the Dangerous Good Basic Description section, check the basic description. | After selection the UN number, the system has generated the dangerous goods basic description in the languages required by the ADR regulation. (For example, UN 1230 METHANOL, 3 (6.1), II, (D/E) |  |
| 9 | Check Transport Permission | In the Transport Permission section, check that the transport permission is set by the system. | Transport of the dangerous good SGPCDG01 is allowed according to the ADR regulation. |  |
| 10 | Save the Classification | After checking the classification data, choose Save. | The classification data is saved. |  |
| 11 | Navigate Back | Navigate back to the Classify Unpackaged Dangerous Good (F3642) app. | The Classify Unpackaged Dangerous Good (F3642) app opens and displays for the version of the ADR regulation that the product is classified as dangerous goods and that the transport is allowed. In addition, the dangerous goods description is displayed. |  |
| 12 | Classify Product According to the Other Regulations | Select a version of the ADR regulation and choose Apply Classification to other Regulations.In the dialog select all regulation versions and choose Apply Classification. | The system applies the classification you did according to ADR to all other selected regulation versions and saves the classifications as a draft version. |  |
| 13 | Release Classifications | Select all regulation versions in progress, but a version of the UNRTDG regulation, and choose Release.In the Release popup, choose Save Drafts and Release. | The released classifications are displayed in the Released section of the Basic Classification table.Note that if you release all regulation versions, the product is no longer displayed in the My Unpackaged Dangerous Goods (F3643) app. |  |
| 14 | Optional: View all Descriptions | Choose View all Descriptions. | The system displays the View all Descriptions screen that shows the dangerous goods basic descriptions for all regulation versions in the languages required by the dangerous goods regulations. |  |

#### Classify Packaged Products as Dangerous Goods

##### Classify Packaged Products with All Modes of Transport Allowed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dangerous Goods Specialist - Product Compliance classifies a packaged product according to the versions of the assigned dangerous goods regulations and allows the transport for all regulation versions.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dangerous Goods Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Dangerous Goods section, open the My Packaged Dangerous Goods (F3711) app. | The My Packaged Dangerous Goods screen is displayed and shows the list of packaged products on the For My Responsible Unit tab page. |  |
| 3 | Search for Packaged Dangerous Goods | Enter product FGPCDG01 into the Search field. | The product is displayed in the Packaged Products list. |  |
| 4 | Select Packaged Dangerous Good | Choose the line for the product FGPCDG01. | The Classify Packaged Dangerous Good (F3710) app opens and displays product-specific details and a list with all assigned regulation versions.Note that the system takes over the labels from the basic classification of the unpackaged product. |  |
| 5 | Enter Packaging Details | In the Packaging Details subsection, choose Edit.In the Edit Packaging Details popup, enter the following data:Description of Dangerous Goods Packaging: 1B1Quantity of Dangerous Goods Packaging: 5 and lChoose Save. | The Packaging Details screen displays the following data:Description of Dangerous Goods Packaging: Aluminium drumsCode of Dangerous Goods Packaging: 1B1Quantity of Dangerous Goods Packaging: 5.000 lNote Whether a period or comma is used as decimal separator depends on your user settings. To check the settings, open the SAP Fiori launchpad settings and go to Languages & Regions > Decimal Format . |  |
| 6 | Specify Enclosure Variant and Transport Permission | In the Dangerous Goods Classification section, select all regulation versions and choose Specify Enclosure Variant.In the Specify Enclosure Variant popup, select the following data:Enclosure Variant: Packaging (P)Transport Permission: AllowedChoose Save. | The system set the Packaging (P) enclosure variant and the transport permission to Allowed for all selected regulation versions for all applicable modes of transport and saves the classifications as a draft version.In addition, the system generates the description for documents for all selected regulation versions based on the rules for dangerous goods descriptions specified in the dangerous goods regulations. |  |
| 7 | Determine Labels | Select all regulation versions and choose Determine Labels.In the Determine Labels dialog, choose OK. | The system uses specific predefined rules to calculate the applicable labels and automatically fills the labeling section of all selected regulation versions with the determined labels. |  |
| 8 | Release Classifications | Select all regulation versions in progress, but a version of the SANS regulation, and choose Release.In the Release popup, choose Release. | The released classifications are displayed in the Released section of the Dangerous Goods Classification table.Note that if you release all regulation versions, the product is no longer displayed in the My Packaged Dangerous Goods (F3711) app. |  |
| 9 | Optional: View all Descriptions | Choose View all Descriptions.In the View all Descriptions screen, select an output scenario. | For the output scenario that you have selected, all dangerous goods descriptions for all regulation versions and the applicable modes of transport are displayed in the languages required by the dangerous goods regulations. |  |

##### Classify Packaged Products with One Mode of Transport Forbidden

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dangerous Goods Specialist - Product Compliance classifies a packaged product according to the to the version of the assigned dangerous goods regulations and forbids the transport for one the regulation versions.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dangerous Goods Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Dangerous Goods section, open the My Packaged Dangerous Goods (F3711) app. | The My Packaged Dangerous Goods screen is displayed and shows the list of packaged products on the For My Responsible Unit tab page. |  |
| 3 | Search for Packaged Dangerous Goods | Enter product FGPCDG02 into the Search field. | The product is displayed in the Packaged Products list. |  |
| 4 | Select Packaged Dangerous Good | Choose the line for the product FGPCDG02. | The Classify Packaged Dangerous Good (F3710) app opens and displays the packaging details and a list with all assigned versions.Note that the system takes over the labels from the basic classification of the unpackaged product. |  |
| 5 | Enter Packaging Details | In the Packaging Details section, choose Edit.In the Edit Packaging Details popup, enter the following data:Description of Dangerous Goods Packaging: 1B1Quantity of Dangerous Goods Packaging: 40 and lChoose Save. | The Packaging Details screen displays the following data:Description of Dangerous Goods Packaging: Aluminium drumsCode of Dangerous Goods Packaging: 1B1Quantity of Dangerous Goods Packaging: 40.000 lNote Whether a period or comma is used as decimal separator depends on your user settings. To check the settings, open the SAP Fiori launchpad settings and go to Languages & Regions > Decimal Format . |  |
| 6 | Specify Enclosure Variant and Transport Permission | In the Dangerous Goods Classification section, select all regulation versions and choose Specify Enclosure Variant.In the Specify Enclosure Variant popup, select the following data:Enclosure Variant: Packaging (P)Transport Permission: AllowedChoose Save. | The system set the Packaging (P) enclosure variant and the transport permission to Allowed for all selected regulation versions for all applicable modes of transport and saves the classifications as a draft version.In addition, the system generates the description for documents for all selected regulation versions based on the rules for dangerous goods descriptions specified in the dangerous goods regulations. |  |
| 7 | Select Regulation Version | Choose the line for a version of the IATA-DGR regulation. | The Classify Dangerous Good According to IATA - Packaged Product (F4833) app opens and displays the Dangerous Goods - Classification Details screen to edit the classification data for the selected regulation version.Note that the app ID (for example, F4833 for IATA-DGR) varies depending on the selected dangerous goods regulation. |  |
| 8 | Change Transport Permission | in the Modes of Transport section, set the transport permission for aircraft passengers to Forbidden and choose Save. | Transport of dangerous good FGPCDG02 is allowed for IATA-DGR for the Aircraft Cargo mode of transport but forbidden for Aircraft Passenger. |  |
| 9 | Navigate Back | Navigate back to the Classify Packaged Dangerous Good (F3710) app. | The Classify Packaged Dangerous Good (F3710) app opens and displays the transport permission as Restricted for the version of the IATA-DGR regulation. |  |
| 10 | Determine Labels | Select all regulation versions and choose Determine Labels.In the Determine Labels dialog, choose OK. | The system uses specific predefined rules to calculate the applicable labels and automatically fills the labeling section of all selected regulation versions with the determined labels. |  |
| 11 | Release Classifications | Select all regulation versions in progress, but a version of the SANS regulation, and choose Release.In the Release popup, choose Release. | The released classifications are displayed in the Released section of the Dangerous Goods Classification table.Note that if you release all regulation versions, the product is no longer displayed in the My Packaged Dangerous Goods (F3711) app. |  |
| 12 | Optional: View all Descriptions | Choose View all Descriptions. In the View all Descriptions screen, select an output scenario. | For the output scenario that you have selected, all dangerous goods descriptions for all regulation versions and the applicable modes of transport are displayed in the languages required by the dangerous goods regulations. |  |

### Classify Product as No Dangerous Goods

#### Optional: Check Compliance Relevance for Non-Dangerous Good

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The compliance-relevant indicator in the product master ensures that the Product Stewardship Specialist - Product Compliance can assess the chemical compliance of the product and the Dangerous Goods Specialist - Product Compliance can classify the product according to dangerous goods regulations. The compliance relevant indicator can be set by the Master Data Specialist - Product Data.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | In the Product Master section, open the Manage Product Master Data (F1602) app. | The initial screen of the app is displayed. |  |
| 3 | Search Product | Enter product SGPCDG02 into the Search field and choose Go. | The product is displayed in the Products list. |  |
| 4 | Select Product | Choose the line for product SGPCDG02. | The details view for the product is displayed. |  |
| 5 | Select the Product Compliance View | Select the Product Compliance tab. | The Product Compliance area for the product is displayed. |  |
| 6 | Check Product Compliance Relevance | Check that the Compliance Relevant field is set to Yes. | The product is compliance relevant. |  |
| 7 | Check Product Compliance Relevance for Further Products | Repeat test steps 3-6 for product FGPCDG03. | The product is compliance relevant. |  |

#### Check Assigned Materials, Packaged Products, and Compliance Purpose for Unpackaged Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance has assigned materials and related packaged products to an unpackaged product and to assign a compliance purpose that reflects transportation in countries in which the packaged product is to be transported. In this test procedure, you check the entered data.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Product Compliance section, open the Manage Basic Compliance Data - Unpackaged Products (F2641) app. | The Manage Basic Compliance Data - Unpackaged Product screen is displayed and shows the list of unpackaged products. |  |
| 3 | Search Unpackaged Product | Expand the header of the unpackaged products list by choosing <!-- image omitted: unnamed -->(Expand Header).Enter Semi Finished Good DG02 into the Search field. | The product is displayed in the Unpackaged Products list.Note If the product Semi Finished Good DG02 is not displayed in the list, search for Unpackaged Product UPDG20. |  |
| 4 | Navigate to Unpackaged Product - Basic Compliance Data | Choose the line for the product Semi Finished Good DG02. | The Unpackaged Product - Basic Compliance Data screen is displayed. |  |
| 5 | Check Assigned Related Products in Product Master | In the Assigned Products section, in the Related Products in Product Master subsection, check the assigned products. | Product SGPCDG02 (Semi Finished Good DG02) is assigned. |  |
| 6 | Check Assigned Related Packaged Products | In the Assigned Products section, in the Related Compliance Views subsection, check the assigned packaged products. | Packaged product FGPCDG03 (Finished Good DG03) is assigned.Note If the packaged product is not assigned, assign it by choosing Create in the Related Compliance Views subsection. |  |
| 7 | Check Assign Compliance Purposes | In the Applications, Markets and Purposes section in the Assigned Compliance Purposes subsection, check the assigned purposes. | The following dangerous goods relevant compliance purposes are assigned:Transport in EuropeTransport in North AmericaTransport in South AmericaTransport in Middle East, Africa, Asia |  |

#### Classify Unpackaged Products as No Dangerous Good

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dangerous Goods Specialist - Product Compliance classifies an unpackaged product according to the versions of the assigned dangerous goods regulations as no dangerous goods and allows the transport for all the regulation versions.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Dangerous Goods Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Dangerous Goods section, open the My Unpackaged Dangerous Goods (F3643) app. | The My Unpackaged Dangerous Goods screen is displayed and shows a list of unpackaged products on the For My Responsible Unit tab page. |  |
| 3 | Search Unpackaged Dangerous Good | Enter product SGPCDG02 into the Search field. | The product is displayed in the Unpackaged Products list. |  |
| 4 | Select Unpackaged Dangerous Good | Choose the line for the product SGPCDG02. | The Classify Unpackaged Dangerous Good (F3642) app opens and displays the released analytical composition and a list with the versions of the assigned dangerous goods regulations. |  |
| 5 | Select Regulation Version | In the Basic Classification section, choose the line for the version of the ADR regulation. | The Classify Dangerous Good (F4465) app opens and displays the Dangerous Goods - Classification Details screen to edit the classification data for the selected regulation version.Note that the app ID (for example, F4465 for ADR) varies depending on the selected dangerous goods regulation. |  |
| 6 | Classify Unpackaged Product as Dangerous Goods | Choose Edit and, in the Classification section, select the following data.Classified As: No Dangerous Goods | The Dangerous Good - Classification Details screen displays the following data:Classified As: No Dangerous Goods |  |
| 7 | Set Transport Permission | In the Transport Permission section, enter the following data:Transport Permission: Allowed | Transport of the dangerous good SGPCDG02 is allowed according to the ADR regulation. |  |
| 8 | Save the Classification | After checking the classification data, choose Save. | The classification data is saved. |  |
| 9 | Navigate Back | Navigate back to the Classify Unpackaged Dangerous Good (F3642) app. | The Classify Unpackaged Dangerous Good (F3642) app opens and displays for the version of the ADR regulation that the product is classifies as no dangerous goods and that the transport is allowed. |  |
| 10 | Classify Product According to the Other Regulations | Select the version of the ADR regulation and choose Apply Classification to other Regulations.In the dialog select all regulation versions and choose Apply Classification. | The system applies the classification you did according to ADR to all other selected regulation versions and saves the classifications as a draft version. |  |
| 11 | Release Classifications | Select all regulation version in progress, but a version of the UNRTDG regulation, and choose Release.In the Release popup, choose Save Drafts and Release. | The released classifications are displayed in the Released section of the Basic Classification table.Note that if you release all regulation versions, the product is no longer displayed in the My Unpackaged Dangerous Goods (F3643) app. |  |

#### Classify Packaged Products as No Dangerous Good

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dangerous Goods Specialist - Product Compliance classifies a packaged product according to the versions of the assigned dangerous goods regulations as no dangerous goods and allows the transport for all the regulation versions.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dangerous Goods Specialist - Product Compliance. |  |  |
| 2 | Access App | In the Dangerous Goods section, open the My Packaged Dangerous Goods (F3711) app. | The My Packaged Dangerous Goods screen is displayed and shows the list of packaged products on the For My Responsible Unit tab page. |  |
| 3 | Search for Packaged Dangerous Goods | Enter product FGPCDG03 into the Search field. | The product is displayed in the Packaged Products list. |  |
| 4 | Select Packaged Dangerous Good | Choose the line for the product FGPCDG03. | The Classify Packaged Dangerous Good (F3710) app opens and displays the packaging details and a list with the versions of the assigned dangerous goods regulations. |  |
| 5 | Specify Enclosure Variant and Transport Permission | Select all regulation versions and choose Specify Enclosure Variant.In the Specify Enclosure Variant popup, select the following data:Enclosure Variant: <Leave Blank>Transport Permission: AllowedChoose Save. | The system set the transport permission to Allowed for all selected regulation versions for all applicable modes of transport and saves the classifications as a draft version. |  |
| 6 | Release Classifications | Select all regulation versions in progress but a version of the SANS regulation and choose Release.In the Release popup, choose Release. | The released classifications are displayed in the Released section of the Dangerous Goods Classification table.Note that if you release all regulation versions, the product is no longer displayed in the My Packaged Dangerous Goods (F3711) app. |  |
| 7 | Optional: View all Descriptions | Choose View all Descriptions. In the View all Descriptions screen, select an output scenario. | For the output scenario that you have selected, all dangerous goods descriptions for all regulation versions and the applicable modes of transport are displayed in the languages required by the dangerous goods regulations. |  |

### Optional: Apply Regulations to Countries/Regions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you transport dangerous goods into another country/region, you must comply with the dangerous goods regulations valid for this country/region. Compliance involves ensuring that the transport of a dangerous good is allowed for the mode of transport you are using and that the dangerous goods documents are available in the required languages.

For all countries/regions where packaged products are intended to be shipped from or shipped to, the Dangerous Goods Specialist - Product Compliance has to set rules for dangerous goods checks that are carried out in business documents within the value chain, such as sales orders or outbound deliveries. If no valid regulations are assigned or if the transport permission is not set to Always Allowed, the system blocks further processing of the business documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Dangerous Goods Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Dangerous Goods Management section, open the Apply Regulations - Dangerous Goods (F3916) app. | The Apply Regulations - Dangerous Goods screen is displayed and shows a world map. |  |
| 3 | Prefill Regulations for Countries | Choose the Prefill Regulations for Countries button and, in the Prefill Applicable Dangerous Goods Regulations and Languages for Countries/Regions popup, choose OK | The system prefills countries with the applicable dangerous goods regulations for the relevant modes of transport. In addition, the system also prefills the required languages tables.After the data is filled into the corresponding database table, the color of the country/region with prefilled data changes from gray to orange or green. |  |
| 4 | Check Transport Check Rules for Countries | Select the following countries/regions:A country/region that is colored green.A country/region that is colored gray. | On the right side of the screen, the Transport Check Rules are displayed for the selected county.For the country/region that is colored green, at least one domestic mode of transport has either a regulation assigned or the check rules set to Always Allowed.For the country/region that is colored gray, all modes of transport have the check rule set to Always Forbidden. |  |
| 5 | Set Transport Check Rules to Always Allowed | To set the transport rules to Always Allowed, proceed as follows:Select a country/region that is colored gray.On the right side of the screen, in the Transport Check Rules section, select a mode of transport.From the Specify Check Rule dropdown menu, select Transport Allowed. | On the right side of the screen, the Transport Check Rules section, the text Always Allowed is displayed for the selected mode of transport. In the map, the color of the country/region is changed accordingly. |  |
| 6 | Set Transport Check Rules to Regulation Dependent | To set the transport rules to Regulation Dependent, proceed as follows:Select a country/region that is colored gray.On the right side of the screen, in the Transport Check Rules section, select a mode of transport.From the Specify Check Rule dropdown menu, select Regulation Dependent.In the Select Regulation screen, select the regulation that you want to assign to the selected mode of transport.In the Regulation screen, select the official languages and save your entries.Select the Display Languages link and choose Edit. Specify additional languages for departure countries/regions and for destination countries/regions and choose Save. | On the right side of the screen, the Transport Check Rules section, the regulation and a link to edit languages are displayed for the selected mode of transport. In the map, the color of the country/region is changed accordingly. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The are no processes and conditions that precede this process.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Scope item 3G8 - Dangerous Goods in the Value Chain | Product Finished Good DG 5l is classified as dangerous goods with transport permission Allowed.Product Finished Good DG 40l is classified as dangerous goods with transport permission Allowed with Restrictions. |

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
- related-to :: [[13-quality-ehs-and-compliance/test-script-dangerous-goods-in-the-value-chain-3g8-ae-sap-s-4hana-clou]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3FC_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 61,133 chars in the whole document
