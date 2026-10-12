---
id: 13-quality-ehs-and-compliance/test-script-assess-marketability-of-a-product-31h-ae-sap-s-4hana-cloud
title: "Test Script: Assess Marketability of a Product (31H_AE) - SAP S/4HANA Cloud Public Edition (31H_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 31H: prerequisites and Fiori app steps to assess product marketability via substance data and supplier disclosures."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/chemical-compliance-and-marketability]
aliases: [31H_S4CLD2608_BPD_EN_AE]
keywords: [Chemical Compliance and Product Marketability, product marketability, market assessment, substance assessment, supplier compliance disclosures, supply chain due diligence, compliance purposes, unpackaged products, analytical composition, material-based composition]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31H_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-892
topic: 13-quality-ehs-and-compliance/chemical-compliance-and-marketability
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Assess Marketability of a Product (31H_AE) - SAP S/4HANA Cloud Public Edition (31H_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31H_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Chemical Compliance and Product Marketability** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Assess Marketability of a Product (31H_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851243)

[2 Prerequisites 4](#_Toc232851244)

[2.1 System Access 4](#_Toc232851245)

[2.2 Roles 4](#_Toc232851246)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232851247)

[2.4 Preliminary Steps 7](#_Toc232851248)

[2.4.1 Create Product Master Records Set as Compliance Relevant 8](#_Toc232851249)

[2.4.2 Create Supplier Master Records 10](#_Toc232851250)

[2.4.3 Create Compliance Purposes 12](#_Toc232851251)

[2.4.4 Create Company Substance 14](#_Toc232851252)

[2.4.5 Create Unpackaged Products, Link to Product Master Records, and Assign Compliance Purpose 15](#_Toc232851253)

[2.4.6 Create Raw Materials with Suppliers 18](#_Toc232851254)

[2.4.7 Approve Suppliers for Raw Materials 20](#_Toc232851255)

[2.4.8 Create Material-Based Composition 21](#_Toc232851256)

[2.4.9 Process Compliance Disclosure for Supplier 23](#_Toc232851257)

[3 Overview Table 26](#_Toc232851258)

[4 Test Procedures 28](#_Toc232851259)

[4.1 Assess Product Marketability Based on Substance Data 28](#_Toc232851260)

[4.1.1 Create Analytical Composition 28](#_Toc232851261)

[4.1.2 Open Marketability Assessment and Initiate Substance Assessment 30](#_Toc232851262)

[4.1.3 Assess Marketability Requirement for Substance as Compliant 31](#_Toc232851263)

[4.1.4 Optional: Verify Product Compliance Events 32](#_Toc232851264)

[4.1.5 Assess Markets for a Product as Allowed 34](#_Toc232851265)

[4.2 Assess Product Marketability Based on Supplier Compliance Disclosures 36](#_Toc232851266)

[4.2.1 Assign Compliance Purpose to Unpackaged Product 36](#_Toc232851267)

[4.2.2 Open Marketability Assessment and Check Compliance Declarations 37](#_Toc232851268)

[4.2.3 Analyze Target State and Current State of Compliance Disclosures for Suppliers 38](#_Toc232851269)

[4.2.4 Process Required Disclosure Template for Supplier 40](#_Toc232851270)

[4.2.5 Optional: Check Marketability Assessments of Raw Materials 42](#_Toc232851271)

[4.2.6 Open Marketability Assessment and Check Compliance Declarations 43](#_Toc232851272)

[5 Appendix 45](#_Toc232851273)

[5.1 Process Integration 45](#_Toc232851274)

[5.1.1 Succeeding Processes 45](#_Toc232851275)

## Purpose

Overview

For a certain country/region and business process, the result of the market assessment for a product describes if a business process for a country/region is allowed, allowed with restrictions, or not allowed.

To start the assessment process, the product stewardship specialist assigns markets (combination of country/region and business process) to the product. Based on these markets, you assign the compliance purposes that cover the relevant countries/regions and business processes (for example, selling an industrial chemical within an EU country/region).

For compliance requirements related to supply chain due diligence acts, the product stewardship specialist identifies which products require compliance declarations from suppliers. The master data specialist for product compliance provides these missing declarations and sets the compliance status of each supplier against each relevant compliance requirement. The product stewardship specialist views the results in marketability assessments of the products.

For a certain country/region and business process, the result of the marketability assessment for a product describes if a business process for a country/region is allowed, allowed with restriction, or not allowed.

To start the assessment process, the product stewardship specialist assigns markets (combinations of country/region and business process) to the product. Based on these markets, the user determines the compliance purposes that cover the relevant countries/regions and business processes, for example, selling an industrial chemical within an EU country.

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Master Data Specialist - Product Compliance | SAP_BR_MD_SPECIALIST_PCL | Master Data - Product Compliance | SAP_BR_MD_SPECIALIST_PCL |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents, for example, products, customers, and suppliers, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note If you create your own packaged and unpackaged products, also carry out the compliance steps for the Safety Data Sheet Management and Dangerous Goods Management solution areas using the test scripts for the scope items listed:Safety Data Sheet Management: 3VR (Manage Safety Data Sheets for Products)Dangerous Goods Management: 3FC (Assess Dangerous Goods for a Product)The demo data described and used in the following is tailored for a smooth execution of the described procedures and suppresses processes of other solution areas in product compliance. |

The following data is valid for all three test scenarios:

Table 1: Substance

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Listed Substance | L00000000009 | CAS Number: 117-81-7Name: 1,2-Benzenedicarboxylic acid bis(2-ethylhexyl) ester | Included in the listed substance index, which is delivered with the software. |

|  |
| --- |
| Note The listed compliance requirement and compliance purpose definitions represent dynamic content based on the legal situation at a given point in time. This data is to be considered exemplary and not a reflection of the currently shipped content. For a complete overview of the currently shipped content, please refer to the application itself. |

Table 2: Compliance Requirement Versions

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Compliance Requirement Version | EU REACH SVHC Status (Jan 2022) (or latest version) | Compliance Requirement: EU REACH SVHC Status | Compliance requirement versions are delivered with the software.Activated via scope item. |
| Compliance Requirement Version | US Dodd-Frank Act | Compliance Requirement: US-Dodd-Frank Act | Compliance requirement versions are delivered with the software.Activated via scope item. |

Table 3: Compliance Purpose

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Compliance Purpose | Product Default Compliance Purpose | The following compliance requirements are assigned:AU-AICS StatusCA-DSL+NDSL StatusCN-IECSC StatusEurope-REACH SVHC StatusJP-ENCS StatusJP-ISHA StatusKR-KECI Notification StatusKR-KECI StatusNZ-NZIOC StatusPH-PICCS StatusTW-TCSCA Chemical RegistrationTW-TCSI StatusUS-TSCA Inventory StatusWorld-SIN List Status | Requirements are relevant for all products.Loaded and activated via scope item. |

Table 4: Product Master Record

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Product | FGPC01 | Product Number: FGPC01Product Type: FERTProduct Description: Product Compliance Finished GoodCompliance Relevant: Yes | Loaded via scope item. |

Table 5: Supplier Master Records

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 | Supplier Name: Domestic Supplier 1 | Loaded via scope item. |
| Supplier | 33300002 | Supplier Name: Domestic Supplier 2 | Loaded via scope item. |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 6: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |

### Preliminary Steps

To run through this scope item, you must first carry out the preliminary steps:

1. [Create Product Master Records Set as Compliance Relevant](#unique_7) [page ] 8
2. [Create Supplier Master Records](#unique_8) [page ] 10
3. [Create Compliance Purposes](#unique_9) [page ] 12
4. [Create Company Substance](#unique_10) [page ] 14
5. [Create Unpackaged Products, Link to Product Master Records, and Assign Compliance Purpose](#unique_11) [page ] 15
6. [Create Raw Materials with Suppliers](#unique_12) [page ] 18
7. [Approve Suppliers for Raw Materials](#unique_13) [page ] 20
8. [Create Material-Based Composition](#unique_14) [page ] 21
9. [Process Compliance Disclosure for Supplier](#unique_15) [page ] 23

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

#### Create Product Master Records Set as Compliance Relevant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you need two product master records for semifinished goods. You create these records in the following steps as a Master Data Specialist - Product Data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Data (SAP_BR_PRODMASTER_SPECIALIST). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Product Master Data (F1602). | The app opens. |  |
| 3 | Search | Enter the product FGPC01 in the Search field. | The products that match the fuzzy search appear in the Products table. |  |
| 4 | Select | Select the entry for FGPC01 (Product Compliance Finished Good) | The row is highlighted in blue. |  |
| 5 | Copy | Choose Copy. | The Select Organizational Data to Copy dialog appears for product Finished PC 01 (FGPC01) with Plants and Distribution Chains preselected. |  |
| 6 | Select Organizational Data to Copy | Deselect Plants, but keep Distribution Chains selected. Then choose OK. | The Create Master Data Record dialog is displayed. |  |
| 7 | Create Record | Add the product number and description:Product Number: SG<XXXXX>31H(replace <XXXXX> with your name)Note The number has to start with SG because of the standard number range.Product Type: Open the value help and choose HALB (Semifinished Product)Product Group: Open the value help and choose L003 (Semi-Finished Goods).Description: Semi <your name> 31HThen choose OK. | The dialog closes, and the Product screen is displayed for your product. |  |
| 8 | Check Compliance Relevance | Choose the Product Compliance tab. In the Compliance Relevant dropdown list, check if Yes is already selected. If not, select Yes. | In the Product Compliance section, the compliance relevance is set to Yes. |  |
| 9 | Add Plant | Choose the Plants tab. In the Plants section, choose Create. | The Plant screen opens. |  |
| 10 | Select Plant | For the Plant field, choose open the value help and choose 3310 (Plant 1 AE). Then choose Apply, and then navigate back. | On the Product screen, the plant 3310 has been added to the Plants table. |  |
| 11 | Select MRP Type | In the Plants table, open the value help for MRP Type for plant 3310. Select the MRP type ND (No planning). | The MRP type ND appears in the Plants table. |  |
| 12 | Add Valuation Area | In the Valuation Areas section, choose Create. | The Valuation Area screen opens. |  |
| 13 | Select Valuation Area and Valuation Class | Open the value help for Valuation Area, and select 3310. Then open the value help for Valuation Class, and select 7900 (Semifinished Goods). Then choose Apply. | On the Product screen, the valuation area 3310 with valuation class 7900 has been added to the Valuation Areas table.Note If an extra empty row appears in the Valuation Areas table, delete it. |  |
| 14 | Choose Create | Choose Create. If any duplicate warnings appear, choose Create again in the Validation Messages dialog. | A message indicates that the master data record has been created. |  |
| 15 | Copy | On the Product screen, choose Copy. | The Select Organizational Data to Copy dialog appears for product Semi <your name> 31H (FGPC01) with Plants and Distribution Chains preselected. |  |
| 16 | Select Organizational Data to Copy | Keep Plants and Distribution Chains selected, and choose OK. | The Create Master Data Record dialog is displayed. |  |
| 17 | Create Record | Add the product number and description:Product Number: SG<XXXXX>31H2(replace <XXXXX> with your name)Note The number has to start with SG because of the standard number range.Product Type: Open the value help and choose HALB (Semifinished Product)Product Group: Open the value help and choose L003 (Semi-Finished Goods).Description: Semi <your name> 31H2Then choose OK. | The dialog closes, and the Product screen is displayed for your product. |  |
| 18 | Choose Create | Choose Create. If any duplicate warnings appear, choose Create again in the Validation Messages dialog. | A message indicates that the master data record has been created.You've now created two master data records for semifinished goods. |  |

#### Create Supplier Master Records

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you need two supplier master records. You create these records in the following steps as a Master Data Specialist - Business Partner Data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Business Partner Data (SAP_BR_BUPA_MASTER_SPECIALIST). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Supplier Master Data (F1053A). | The app opens. |  |
| 3 | Search | Enter the supplier 33300001 in the Search field. | The suppliers that match the fuzzy search appear in the Suppliers table. |  |
| 4 | Select Supplier | Select the entry for 33300001 (Domestic Supplier 1) | The row is highlighted in blue. |  |
| 5 | Copy Supplier | Choose Copy. | The Select Organizational Data to Copy dialog appears for supplier Domestic Supplier 1 (33300001) with Copy with Preselection deselected, and Company Code and Purchasing Organization preselected. |  |
| 6 | Select Organizational Data to Copy | Keep the default selections, and choose OK. | The Supplier screen is displayed. |  |
| 7 | Enter Supplier Name | In the Name 1 field in Basic Data > General Information , enter <your name> Supplier 1. | The supplier name <your name> Supplier 1 is displayed in the Name 1 field. |  |
| 8 | Edit Header | On the Supplier screen, choose Edit Header. | The Edit Header dialog opens. |  |
| 9 | Enter Business Partner Number | In the Business Partner field, enter a number with 10 digits or fewer. The number must be a unique business partner number and use only digits (0 - 9, no letters or special characters).Make note of the business partner number:_________.Then choose OK. | The Edit Header dialog closes. |  |
| 10 | Create Supplier | On the Supplier screen, choose Create. | A success message indicates that the master data record has been created. |  |
| 11 | Navigate Back | Navigate back. | The Manage Supplier Master screen is displayed with 33300001 (Domestic Supplier 1) selected. |  |
| 12 | Select Supplier | Select the entry for 33300002 (Domestic Supplier 2) | The row is highlighted in blue. |  |
| 13 | Copy Supplier | Choose Copy. | The Select Organizational Data to Copy dialog appears for supplier Domestic Supplier 2 (Domestic Supplier 2) with Copy with Preselection deselected, and Company Code and Purchasing Organization preselected. |  |
| 14 | Select Organizational Data to Copy | Keep the default selections, and choose OK. | The Supplier screen is displayed. |  |
| 15 | Enter Supplier Name | In the Name 1 field in Basic Data > General Information , enter <your name> Supplier 2. | The supplier name <your name> Supplier 2 is displayed in the Name 1 field. |  |
| 16 | Edit Header | On the Supplier screen, choose Edit Header. | The Edit Header dialog opens. |  |
| 17 | Enter Business Partner Number | In the Business Partner field, enter a number with 10 digits or fewer. The number must be a unique business partner number and use only digits (0 - 9, no letters or special characters).Make note of the business partner number:_________.Then choose OK. | The Edit Header dialog closes. |  |
| 18 | Create Supplier | On the Supplier screen, choose Create. | A success message indicates that the master data record has been created.You've now created two master data records for suppliers. |  |

#### Create Compliance Purposes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you create the compliance purposes that you assign to the unpackaged product. You create the compliance purposes in the following steps as a Product Stewardship Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Compliance Purposes (F2632). | The app opens. |  |
| 3 | Create Compliance Purpose | Choose Create. | The Compliance Purpose screen is displayed. |  |
| 4 | Create Compliance Purpose Name | Choose Create in the section for compliance purpose names. | A row with empty Language and Name fields appears. |  |
| 5 | Open Value Help for Language | In the Compliance Purpose Names section, open the value help in the first row of the Language column. | The Select: Language dialog opens. |  |
| 6 | Select Language | In the search field of the Select: Language dialog, enter a language key, for example, EN for English, and choose Go. Then choose the row of the language. | The Select: Language dialog closes, and the selected language code appears in the first row of the Language column in the Compliance Purpose Names section. |  |
| 7 | Enter Compliance Purpose Name | In the Compliance Purpose Names section, enter <your name> 31H in the first row of the Name column. | The name <your name> 31H appears in the first row of the Name column in the Compliance Purpose Names section. |  |
| 8 | Create Compliance Purpose with Name | Choose Create at the bottom of the screen. | The compliance purpose is created, and the compliance purpose name is displayed at the top under the Compliance Purpose screen title. |  |
| 9 | Edit Compliance Purpose | On the Compliance Purpose screen, choose Edit. | The app is in edit mode. |  |
| 10 | Add Compliance Requirement | In the Compliance Requirements section, choose Add. | The Assign Compliance Requirements dialog opens. |  |
| 11 | Select Compliance Requirement | Search for and select the compliance requirement EU-REACH SVHC Status, and then press Enter. Select the compliance requirement, and then choose Select. | The Assign Compliance Requirements dialog closes, and the added compliance requirement is displayed in the Compliance Requirements section. |  |
| 12 | Save Compliance Purpose | On the Compliance Purpose screen, choose Save. | A success message indicates that the compliance purpose is saved, and the app switches to display mode. |  |
| 13 | Activate Compliance Purpose | On the Compliance Purpose screen, choose Activate. | A success message indicates that the compliance purpose was activated. |  |
| 14 | Navigate Back | Navigate back. | The Manage Compliance Purposes screen is displayed. |  |
| 15 | Create Compliance Purpose | Choose Create. | The Compliance Purpose screen is displayed. |  |
| 16 | Create Compliance Purpose Name | Choose Create in the section for compliance purpose names. | A row with empty Language and Name fields appears. |  |
| 17 | Open Value Help for Language | In the Compliance Purpose Names section, open the value help in the first row of the Language column. | The Select: Language dialog opens. |  |
| 18 | Select Language | In the search field of the Select: Language dialog, enter a language key, for example, EN for English, and choose Go. Then choose the row of the language. | The Select: Language dialog closes, and the selected language key appears in the first row of the Language column in the Compliance Purpose Names section. |  |
| 19 | Enter Compliance Purpose Name | In the Compliance Purpose Names section, enter <your name> 31H2 in the first row of the Name column. | The name <your name> 31H2 appears in the first row of the Name column in the Compliance Purpose Names section. |  |
| 20 | Add Compliance Requirements | In the Compliance Requirements section, choose Add. | The Assign Compliance Requirements dialog opens. |  |
| 21 | Select Compliance Requirement | Search for and select the compliance requirements US-Dodd-Frank Act.Then choose Select. | The Assign Compliance Requirements dialog closes, and the added compliance requirement is displayed in the Compliance Requirements section. |  |
| 22 | Create Compliance Purpose with Name and Compliance Requirement | On the Compliance Purpose screen, choose Create. | The compliance purpose is created, and the compliance purpose name is displayed at the top under the Compliance Purpose screen title. |  |
| 23 | Activate Compliance Purpose | On the Compliance Purpose screen, choose Activate. | A success message indicates that the compliance purpose was activated. |  |

#### Create Company Substance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To be able to include substances in the analytical composition of your product, you need company substances. You create a company substance in this step as aMaster Data Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance (SAP_BR_MD_SPECIALIST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Substances Compliance (F2578). | The app opens. |  |
| 3 | Create Company Substance | On the Manage Substances Compliance screen, for the Substances table, choose Create. | The New Substance dialog is displayed. |  |
| 4 | Link Existing Listed Substance | Leave the Link Existing Listed Substance radio button selected. Open the value help for Listed Substance. | The Select: Listed Substance dialog opens. |  |
| 5 | Search Based on CAS Number | In the search field, enter the CAS number 117-81-7, and then press Enter. | The Items table is narrowed down to the results that match the fuzzy search. |  |
| 6 | Select Substance | Select the row for the substance with 1,2-Benzenedicarboxylic acid bis(2-ethylhexyl) ester in the Listed Subst. Name column. | The Select: Listed Substance dialog closes. In the New Substance dialog, L00000000009 appears in the Listed Substance field. |  |
| 7 | Save Substance | In the New Substance dialog, choose Save. | A success message indicates that the substance has been created, and the Manage Substances Compliance screen opens. |  |
| 8 | Edit Substance | Choose Edit. | The app is in edit mode. |  |
| 9 | Define Internal Name | In the Internal Name field under Substance Header, enter <your name> DEHP. Then choose Save. | A success message indicates that the substance has been saved. The app is in display mode, and <your name> DEHP is displayed in the Internal Name field. |  |

#### Create Unpackaged Products, Link to Product Master Records, and Assign Compliance Purpose

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you need the compliance views of the relevant unpackaged products. In the following steps, as a Product Stewardship Specialist - Product Compliance, you create the unpackaged products, link them to the relevant product master records, and assign the relevant compliance purpose to the first unpackaged product. You assign the relevant compliance purpose to the second unpackaged product in a later procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The app opens. |  |
| 3 | Create Unpackaged Product | On the Manage Basic Compliance Data screen, for the Unpackaged Products table, choose Create. | The New Product dialog is displayed. |  |
| 4 | Enter Header Data for New Product | Enter the following header data:Internal Name: <your name> 31HProduct Categorization: MixtureSafety Data Sheet Required: <deselected>The rest stays default. | The New Product dialog is displayed with <your name> 31H in the Internal Name field. |  |
| 5 | Save the Unpackaged Product | Choose Save. | The New Product dialog closes, the unpackaged product is created, and the Unpackaged Product - Basic Compliance Data screen is displayed. |  |
| 6 | Assign Related Product in Product Master | In the Assigned Products section, Related Products in Product Master table, choose the value help for the first empty row in the Product column. | The Select: Product dialog opens. |  |
| 7 | Search for Semifinished Good | Enter Semi <your name> 31H in the search field, and then press Enter. | The Items table is narrowed down to the results that match the fuzzy search. |  |
| 8 | Choose Semifinished Good | Choose the row for the product with Semi <your name> 31H in the Product Description column. | The Select: Product dialog closes, and SG<your name>31H appears in the first row of the Related Products in Product Master table. |  |
| 9 | Save the Unpackaged Product | On the Unpackaged Product - Basic Compliance Data screen, choose Save. | The app is in display mode, and the product name at the top of the screen has changed to Semi <your name> 31H. |  |
| 10 | Edit Unpackaged Product | On the Unpackaged Product - Basic Compliance Data screen, choose Edit. | The app is in edit mode. |  |
| 11 | Select Assigned Compliance Purpose | In the Application, Uses, Markets and Purposes section, Assigned Compliance Purposes table, select Product Default Compliance Purpose. | The selected row is highlighted in blue. |  |
| 12 | Remove Default Compliance Purpose | For the Assigned Compliance Purposes table, choose Remove. In the Remove dialog that appears, choose Remove again. | The Product Default Compliance Purpose is removed from the Assigned Compliance Purposes table. |  |
| 13 | Add Compliance Purpose | For the Assigned Compliance Purposes table, choose Add. | The Assign Compliance Purposes dialog opens. |  |
| 14 | Choose Your Compliance Purpose | Search for the compliance purpose <your name> 31H. Select it, and then choose OK. | The compliance purpose <your name> 31H is added to the Assigned Compliance Purposes table. |  |
| 15 | Save Unpackaged Product | On the Unpackaged Product - Basic Compliance Data screen, choose Save. | A success message indicates that the unpackaged product has been saved. |  |
| 16 | Navigate Back | Navigate back. | The Manage Basic Compliance Data - Unpackaged Product screen is displayed. |  |
| 17 | Create Unpackaged Product | On the Manage Basic Compliance Data screen, for the Unpackaged Products table, choose Create. | The New Product dialog is displayed. |  |
| 18 | Enter Header Data for New Product | In the Internal Name field, enter <your name> 31H2. Then deselect Safety Data Sheet Required.The rest stays default. | The New Product dialog is displayed with <your name> 31H2 in the Internal Name field. |  |
| 20 | Save the Unpackaged Product | Choose Save. | The New Product dialog closes, the unpackaged product is created, and the Unpackaged Product - Basic Compliance Data screen is displayed. |  |
| 21 | Assign Related Product in Product Master | In the Assigned Products section, Related Products in Product Master table, choose the value help for the first empty row in the Product column. | The Select: Product dialog opens. |  |
| 22 | Search for Semifinished Good | Enter Semi <your name> 31H2 in the search field, and then press Enter. | The Items table is narrowed down to the results that match the fuzzy search. |  |
| 23 | Choose Semifinished Good | Choose the row for the product with Semi <your name> 31H2 in the Product Description column. | The Select: Product dialog closes, and SG<your name>31H2 appears in the first row of the Related Products in Product Master table. |  |
| 24 | Save Unpackaged Product | On the Unpackaged Product - Basic Compliance Data screen, choose Save. | A success message indicates that the unpackaged product has been saved.You've now created two unpackaged products. |  |

#### Create Raw Materials with Suppliers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you need the compliance views of the relevant raw materials with suppliers assigned. In the following steps, as a Master Data Specialist - Product Compliance, you create the raw materials and assign the suppliers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance (SAP_BR_MD_SPECIALIST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Basic Compliance Data - Raw Materials (F3024). | The app opens. |  |
| 3 | Create Raw Material | On the Manage Basic Compliance Data - Raw Materials screen, choose Create. | The New Raw Material dialog is displayed. |  |
| 4 | Enter Header Data for New Raw Material | Enter the following header data:Internal Name: <your name> RM 31HProduct Categorization: MixtureThe rest stays default. | The New Raw Material dialog is displayed with <your name> RM 31H in the Internal Name field. |  |
| 5 | Save the Raw Material | Choose Save. | The New Raw Material dialog closes, the unpackaged product is created, and the Raw Material - Basic Compliance Data screen is displayed. |  |
| 6 | Remove Default Compliance Purpose | In the Compliance Purposes section, select the Raw Material Default Compliance Purpose. Then choose Remove. In the Remove dialog, choose Remove again. | The Assigned Compliance Purposes table in the Compliance Purposes section is empty. |  |
| 7 | Save Your Changes | On the Raw Material - Basic Compliance Data screen, choose Save. | A message indicates that your changes have been saved.The app is in display mode. |  |
| 8 | Navigate to Suppliers | On the Raw Material - Basic Compliance Data screen, choose the Suppliers tab. | The app scrolls down to the Suppliers section. |  |
| 9 | Assign Supplier | For the Suppliers of Raw Material table, choose Create. | The Assign Supplier dialog opens. |  |
| 10 | Search for Supplier | Open the value help for the Supplier field. In the Select: Supplier dialog, enter the business partner number that you defined for <your name> Supplier 1, and then press Enter. | The Items table is narrowed down to the suppliers that match the fuzzy search. |  |
| 11 | Choose Supplier | In the Items table in the Select: Supplier dialog, choose the row for <your name> Supplier 1 | The Select: Supplier dialog closes. In the Assign Supplier dialog, the business partner number for <your name> Supplier 1 is displayed in the Supplier field. |  |
| 12 | Save Supplier Assignment | In the Assign Supplier dialog, choose Save. | <your name> Supplier 1 appears in the Suppliers of Raw Material table. |  |
| 13 | Navigate Back | Navigate back. | The Manage Basic Compliance Data - Raw Materials screen is displayed. |  |
| 14 | Create Raw Material | On the Manage Basic Compliance Data screen, for the Raw Materials table, choose Create. | The New Raw Material dialog is displayed. |  |
| 15 | Enter Header Data for New Raw Material | In the Internal Name field, enter <your name> RM 31H2.The rest stays default. | The New Raw Material dialog is displayed with <your name> RM 31H2 in the Internal Name field. |  |
| 16 | Save the Raw Material | Choose Save. | The New Product dialog closes, the unpackaged product is created, and the Raw Material - Basic Compliance Data screen is displayed. |  |
| 17 | Remove Default Compliance Purpose | In the Compliance Purposes section, select the Raw Material Default Compliance Purpose. Then choose Remove. In the Remove dialog, choose Remove again. | The Assigned Compliance Purposes table in the Compliance Purposes section is empty. |  |
| 18 | Save Your Changes | On the Raw Material - Basic Compliance Data screen, choose Save. | A message indicates that your changes have been saved.The app is in display mode. |  |
| 19 | Navigate to Suppliers | On the Raw Material - Basic Compliance Data screen, choose the Suppliers tab. | The app scrolls down to the Suppliers section. |  |
| 20 | Assign Supplier | For the Suppliers of Raw Material table, choose Create. | The Assign Supplier dialog opens. |  |
| 21 | Search for Supplier | Open the value help for the Supplier field. In the Select: Supplier dialog, enter the business partner number for <your name> Supplier 2, and then press Enter. | The Items table is narrowed down to the suppliers that match the fuzzy search. |  |
| 22 | Choose Supplier | In the Items table in the Select: Supplier dialog, choose the row for <your name> Supplier 2 | The Select: Supplier dialog closes. In the Assign Supplier dialog, the business partner number for <your name> Supplier 2 is displayed in the Supplier field. |  |
| 23 | Save Supplier Assignment | In the Assign Supplier dialog, choose Save. | <your name> Supplier 2 appears in the Suppliers of Raw Material table.You've now created two raw materials with suppliers. |  |

#### Approve Suppliers for Raw Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance approves the suppliers that provide the raw materials in the before-production material-based composition of the unpackaged product.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Basic Compliance Data - Raw Materials (F3024). | The app opens. |  |
| 3 | Search for Raw Material | Enter <your name> RM 31H in the search field. | The table is filtered for the raw materials that match the fuzzy search. |  |
| 4 | Open Raw Material | In the Raw Materials table, choose the row for <your name> RM 31H. | The Raw Material - Basic Compliance Data screen opens. |  |
| 5 | Navigate to Supplier | On the Raw Material - Basic Compliance Data screen, choose the Suppliers tab. | The app scrolls down to the Suppliers section. |  |
| 6 | Choose Supplier | In the Suppliers section, choose the row for <your name> Supplier 1. | The Supplier Compliance for Raw Material screen opens. |  |
| 7 | Approve Supplier | On the Supplier Compliance for Raw Material screen, choose Set Supplier Status > Approve . | The value in the Supplier Status for Raw Material field changes to Approved. |  |
| 8 | Navigate Back | Navigate back twice. | The Manage Basic Compliance Data screen is displayed. The Raw Materials table is filtered for the raw materials that match the fuzzy search for <your name> RM 31H. |  |
| 9 | Open Raw Material | In the Raw Materials table, choose the row for <your name> RM 31H2. | The Raw Material - Basic Compliance Data screen opens. |  |
| 10 | Navigate to Supplier | On the Raw Material - Basic Compliance Data screen, choose the Suppliers tab. | The app scrolls down to the Suppliers section. |  |
| 11 | Choose Supplier | In the Suppliers section, choose the row for <your name> Supplier 2. | The Supplier Compliance for Raw Material screen opens. |  |
| 12 | Approve Supplier | On the Supplier Compliance for Raw Material screen, choose Set Supplier Status > Approve . | The value in the Supplier Status for Raw Material field changes to Approved.You've now approved both suppliers. |  |

#### Create Material-Based Composition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The before-production material-based composition provides the raw material analysis of the unpackaged product that considers the suppliers. In this case, the unpackaged product consists of two raw materials. You create and release both the before-production and after-production material-based compositions with the business role Product Stewardship Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Manage Basic Compliance Data - Unpackaged Products (F2641) tile. | The Manage Basic Compliance Data - Unpackaged Products screen is displayed. |  |
| 3 | Search Unpackaged Product | Enter the product name Semi <your name> 31H2 in the Search field. | The table is filtered for entries that match the fuzzy search. |  |
| 4 | Navigate to Basic Compliance Data | Choose the row for the unpackaged product Semi <your name> 31H2. | The Unpackaged Product - Basic Compliance Data screen opens in display mode. |  |
| 5 | Navigate to Material-Based Composition | Choose the Compositions tab. In the Compositions section, choose the row with Material-Based Composition in the Composition column and In Progress - Initial Version in the Processing Status column. | The Unpackaged Product - Material-Based Composition screen opens. |  |
| 6 | Switch to Edit Mode | On the Unpackaged Product - Material-Based Composition screen, choose Edit. | The app is in edit mode. |  |
| 7 | Search for Raw Materials by Internal Name | In the Before Production section, enter the internal name <your name> RM 31H in the Compliance View field. Select the correct value from the search results.Repeat this step in the newly added row for your second raw material. | The raw materials appear in the Before Production table. |  |
| 8 | Specify Concentration Before Production | In the Concentration column of the Before Production table, enter 50 for each newly added raw material. Leave the unit of measurement as % (percent). | The concentration before production is filled in for the material-based composition before production. |  |
| 9 | Add Remaining Components | Under the After Production tab, in the Remaining Components table, choose Add. | The Add Remaining Components dialog appears, in which all components from the Before Production composition are displayed. |  |
| 10 | Take Over Components Before Production | In the dialog, select all components in the Before Production table, and then choose Add. | The selected raw materials appear in the Remaining Components table. |  |
| 11 | Enter Concentration After Production and Save | For each remaining component, enter the same concentration as in the concentration before production:Concentration: 50Unit of Measurement: %Then choose Create. | The concentration after production is filled in your material-based composition, and your composition is saved. |  |
| 12 | Check and Release Material-Based Composition | On the Unpackaged Product - Material-Based Composition screen, choose Release. | A success message indicates that the material-based composition has been released. |  |
| 13 | Check Processing Status | Navigate back. | The Unpackaged Product - Basic Compliance Data screen opens. In the Compositions table, for the row with Material-Based Composition in the Composition column, the entry in the Processing Status column is Released. For subsequent compliance checks, this released material-based composition is considered. |  |

#### Process Compliance Disclosure for Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance has received a compliance disclosure from the supplier in the form of a self-assessment, and assigns the relevant compliance requirement version to the supplier. Based on this data, the Master Data Specialist - Product Compliance assesses the compliance of the supplier with the relevant supply chain due diligence act.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Compliance Disclosures - For Suppliers (F7370) app. | The Process Compliance Disclosures - For Suppliers screen is displayed. |  |
| 3 | Create Compliance Disclosure | For the Compliance Disclosures table, choose Create. | The Create dialog opens. |  |
| 4 | Provide Header Data | In the Create dialog, provide the following data:Supplier: Business partner number for <your name> Supplier 1Type: Self-AssessmentDate of Receipt: <today's date>Then choose Create. | The Compliance Disclosure screen opens. |  |
| 5 | Open Value Help for Compliance Requirement Version | In the Compliance Declarations table, Compliance Requirement Version field, open the value help. | The Select: Compliance Requirement Version dialog opens. |  |
| 6 | Select Compliance Requirement Version | Choose the compliance requirement version with US-Dodd-Frank Act in the Compliance Requirement column. | The Select: Compliance Requirement Version dialog closes. On the Compliance Disclosure screen, in the Compliance Declarations table, the newly added compliance requirement version appears in the Compliance Requirement Version column. |  |
| 7 | Assess Supplier as Compliant | In the Compliance Declarations table, Supplier Compliance Status column, select Compliant from the dropdown list in the row for US Dodd-Frank Act. | In the Compliance Declarations table, Compliant appears in the Supplier Compliance Status column for US Dodd-Frank Act. |  |
| 8 | Optional: Add a Remark | Optional: In the Compliance Declarations table, Supplier Compliance Status column, in the row for US Dodd-Frank Act, enter a remark. | In the Compliance Declarations table, Remark column, your remark is displayed for US Dodd-Frank Act. |  |
| 9 | Optional: Upload an Attachment | Optional: In the Attachments section, choose Upload, and select a file from your computer. | The uploaded file appears in the Attachments section, and a success message confirms that the file has been uploaded. |  |
| 10 | Finalize Creation of Compliance Disclosure | Choose Create. | A success message confirms that the object was created. |  |
| 11 | Set Compliance Disclosure to Completed | On the Compliance Disclosure screen, choose Set to Completed. | In the Compliance Declarations table, the value in the Effective column for US Dodd-Frank Act has changed to Yes. |  |

## Overview Table

This scope item consists of several process steps provided in the table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Analytical Composition](#unique_17) [page ] 28 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | The analytical composition is created and released for the product. |
| [Open Marketability Assessment and Initiate Substance Assessment](#unique_18) [page ] 30 | Product Stewardship Specialist - Product Compliance | Assess Marketability Requirements - For Products (F3219) | The substance assessment for the product is initiated so the marketability status of the product can be determined. |
| [Assess Marketability Requirement for Substance as Compliant](#unique_19) [page ] 31 | Master Data Specialist - Product Compliance | Assess Marketability Requirements - For Substances (F3220) | The marketability assessment for the substance is carried out. |
| [Optional: Verify Product Compliance Events](#unique_20) [page ] 32 | Product Stewardship Specialist - Product Compliance | Process Product Compliance Events (F4005) | The events reflecting the changes made in the system are checked. |
| [Assess Markets for a Product as Allowed](#unique_21) [page ] 34 | Product Stewardship Specialist - Product Compliance | Assess Markets - For Products (F2612) | The product can be produced and sold in the selected country/region in which the compliance requirement is valid. |
| [Assign Compliance Purpose to Unpackaged Product](#unique_22) [page ] 36 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | The compliance purpose with a compliance requirement related to supply chain due diligence acts is assigned to the unpackaged product. |
| [Open Marketability Assessment and Check Compliance Declarations](#unique_23) [page ] 37 | Product Stewardship Specialist - Product Compliance | Assess Marketability Requirements - For Products (F3219) | The product stewardship specialist finds out that a compliance declaration is required for one of the suppliers. |
| [Analyze Target State and Current State of Compliance Disclosures for Suppliers](#unique_24) [page ] 38 | Master Data Specialist - Product Compliance | Analyze Compliance Disclosures - For Suppliers (F7460) | The master data specialist for product compliance verifies that a compliance declaration is required for one of the suppliers. |
| [Process Required Disclosure Template for Supplier](#unique_25) [page ] 40 | Master Data Specialist - Product Compliance | Process Compliance Disclosures - For Suppliers (F7370) | After contacting the supplier and receiving the missing data, the master data specialist for product compliance provides the required compliance disclosure. |
| [Optional: Check Marketability Assessments of Raw Materials](#unique_26) [page ] 42 | Master Data Specialist - Product Compliance | Assess Marketability Requirements - For Raw Materials (F3221) | The master data specialist for product compliance verifies that the compliance declarations exist at the raw material level. |
| [Open Marketability Assessment and Check Compliance Declarations](#unique_27) [page ] 43 | Product Stewardship Specialist - Product Compliance | Assess Marketability Requirements - For Products (F3219) | The product stewardship specialist verifies that the unpackaged product is compliant with the relevant supply chain due diligence act. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Assess Product Marketability Based on Substance Data

#### Create Analytical Composition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The analytical composition provides the chemical analysis of the unpackaged product. In this case, the unpackaged product consists of only one substance, m-xylene. You create and release the analytical composition with the business role Product Stewardship Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Manage Basic Compliance Data - Unpackaged Products (F2641) tile. | The Manage Basic Compliance Data - Unpackaged Products screen is displayed. |  |
| 3 | Search Unpackaged Product | Enter the product name Semi <your name> 31H in the Search field. | The table is filtered for entries that match the fuzzy search. |  |
| 4 | Navigate to Basic Compliance Data | Choose the row for the unpackaged product Semi <your name> 31H. | The Unpackaged Product - Basic Compliance Data screen opens in display mode. |  |
| 5 | Navigate to Analytical Composition | Choose the Compositions tab. In the Compositions section, choose the row with Analytical Composition in the Composition column and In Progress - Initial Version in the Processing Status column. | The Unpackaged Product - Analytical Composition screen opens. |  |
| 6 | Switch to Edit Mode | On the Unpackaged Product - Analytical Composition screen, choose Edit. | The app is in edit mode. |  |
| 7 | Create Substance | In the Analytical Components section, for the Substances table, choose Create. | The Assign Substances dialog opens. |  |
| 8 | Search for Substance by Internal Name | Enter the internal name <your name> DEHP in the search field. | The table is filtered to the substance with internal name <your name> DEHP. |  |
| 9 | Select and Confirm Substance | Select the substance with internal name <your name> DEHP, and then choose OK. | The substance appears in the Substances table. |  |
| 10 | Specify Concentration and Save Analytical Composition | In the Concentration column of the Substances table, enter 100 for the newly added substance. Leave the unit of measurement as % (percent). Then choose Save | A success message indicates that your changed have been saved. |  |
| 11 | Check and Release Analytical Composition | On the Unpackaged Product - Analytical Composition screen, choose Release. | A success message indicates that the analytical composition has been released. The app is in display mode. |  |
| 12 | Check Processing Status | Navigate back. | The Unpackaged Product - Basic Compliance Data screen opens. In the Compositions table, for the row with Analytical Composition in the Composition column, the entry in the Processing Status column is Released. For subsequent compliance checks, this released analytical composition with the substance DEHP (CAS number: 117-81-7) is considered. |  |

#### Open Marketability Assessment and Initiate Substance Assessment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product isn't compliant with the compliance requirement, and the substance requires further assessment. You open the marketability assessment for the product and initiate a substance assessment as a Product Stewardship Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Assess Marketability Requirements - For Products (F3219) tile. | The app opens. |  |
| 3 | Search Unpackaged Product | Enter the product name Semi <your name> 31H in the Search field, and then press Enter. | The Unreleased Marketability Assessments table is filtered for entries that match the fuzzy search. |  |
| 4 | Navigate to Marketability Assessment | Choose the row for the marketability assessment with Semi <your name> 31H in the Product Name column, and EU REACH SVHC Status (Jan 2022) (or latest version) in the Compliance Requirement Version column. | The Marketability Assessment screen opens. |  |
| 5 | Navigate to Assessment Details | On the Marketability Assessment screen, choose the Assessment Details tab. | The screen scrolls down to the Assessment Details section. |  |
| 6 | View Substance Assessment Details | For the Substance Assessment section under Assessment Details, choose Show Details. | A table appears with the title Restricted Substance Assessment (Based On: Analytical Composition). The table has one row, with the following data in each column:Assessment Status: Not AssessedSubstance List: EU REACH SVHCSubstance: Bis (2-ethylhexyl)phthalateCAS Number: 117-81-7Role in Composition: Active IngredientUsed Concentration: 100.000%Threshold: <This value varies depending on the active compliance requirement version.>Substance Assessment: Initiate Assessment |  |
| 7 | Initiate Substance Assessment | In the Substance Assessment column of the table, choose Initiate Assessment for the substance. | A success message indicates that the substance assessment has been initiated. In Progress appears in the Assessment Status column, and View Details appears in the Substance Assessment column. |  |
| 8 | View Substance Assessment | In the Substance Assessment column of the table, choose View Details. | The Marketability Assessment - Substance screen opens. The marketability status is Unknown.The next step is for the Master Data Specialist - Product Compliance to assess the substance against the compliance requirement version. |  |

#### Assess Marketability Requirement for Substance as Compliant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The substance requires further assessment to ensure that the product is compliant with the assigned compliance requirement. You carry out the marketability assessment for the substance as a Master Data Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance (SAP_BR_MD_SPECIALIST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Master Data Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Assess Marketability Requirements - For Substances (F3220) tile. | The app opens. |  |
| 3 | Search Based on Substance Name | Enter the substance name DEHP in the Search field, and then press Enter. | The Marketability Assessments table is filtered for entries that match the fuzzy search. |  |
| 4 | Navigate to Marketability Assessment for Substance | Choose the row with EU REACH SVHC Status (Jan 2022) (or latest version) in the Compliance Requirement Version column, and DEHP in the Substance Name column. | The Marketability Assessment - Substance screen opens in display mode. |  |
| 5 | Switch to Edit Mode | Choose Edit. | The app is in edit mode. |  |
| 6 | Optional: Add Exemption | In the Exemptions section, choose Add. | The Select Exemption dialog opens. |  |
| 7 | Optional: Select Exemption | In the Select Exemption dialog, select any exemption, and then choose Select. | The exemption appears in the Exemptions table. |  |
| 8 | Set Marketability Status and Save Assessment | In the Compliance Details section, set the marketability status to Compliant. Then choose Save. | A success message indicates that the compliance assessment has been saved. |  |

#### Optional: Verify Product Compliance Events

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An event is the occurrence of a change of state in an object, which is published throughout the system. An event that occurs within the area of Product Compliance is known as a product compliance event. Some user actions enable such events that must be captured and processed by the system to ensure that all compliance-relevant data for your whole product portfolio stays up to date. Depending on the product compliance event, the system determines which objects are affected and carries out the necessary actions for them. In this case, setting the marketability status of the substance assessment to Compliant and saving it enabled an event to calculate and release the compliance assessment for your product. In this test procedure, you check product compliance events as a Product Stewardship Specialist - Product Compliance, but it is also possible to check product compliance events as a Master Data Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Search for App | Search for Process Product Compliance Events (F4005) in the search bar for Apps. | The Process Product Compliance Events tile is displayed. |  |
| 3 | Access App | Select the Process Product Compliance Events tile. | The app opens. |  |
| 4 | View Completed Events | Choose the Completed tab. | The list of completed product compliance events is displayed. |  |
| 5 | Check for Your Events | Check that the following events are listed, with the latest event first:Event: EU REACH SVHC Status (Jan 2022) (or latest version) ReleasedInitiating Object Name: Semi <your name> 31HInitiated By: SAP System ProcessingEvent: EU REACH SVHC Status (Jan 2022) (or latest version) SavedInitiating Object Name: DEHPInitiated By: Example MdSpecialistPcl or your userEvent: EU REACH SVHC Status (Jan 2022) (or latest version) CreatedInitiating Object Name: DEHPInitiated By: Example ProdstwrdSplstPcl or your userNote If this event doesn't appear in the Completed tab, check the New or In Progress tab, in case the event processing has not yet finished. | Based on the events listed in the table, you can see that the system has automatically released, or will soon release, the marketability assessment of the product Semi <your name> 31H against the compliance requirement version EU REACH SVHC Status (Jan 2022) (or latest version). The calculation leading to the automatic release is based on the substance assessment that you enabled as a Product Stewardship Specialist - Product Compliance and completed as a Master Data Specialist - Product Compliance. |  |

#### Assess Markets for a Product as Allowed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance proactively assesses the product for a relevant market. The result of the market assessment is used as basis for the chemical compliance checks within the logistical processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Assess Markets - For Products (F2612) tile. | The Assess Markets - For Products (F2612) screen is displayed and shows the list of unpackaged products with pending market requests.Note Continue with the next test step even if the list of unpackaged products with pending market requests is empty. An empty list can result from the default values in the filter fields Released Assessments and Assessments in Progress. |  |
| 3 | Search Unpackaged Product | Enter the product name <your name> 31H in the Search field.Delete the default values in the fields for the filters Released Assessments and Assessments in Progress. | The list is filtered and the entry for the unpackaged product <your name> 31H is displayed. |  |
| 4 | Navigate to Market Assessment for a Single Product | Choose the line for the unpackaged product <your name> 31H. | The Product - Assess For Markets screen opens in display mode. |  |
| 5 | Switch to Edit Mode | Choose Edit. | The Product - Assess for Markets screen switches to edit mode. |  |
| 6 | Add Production and Sales Countries/Regions | For the Assess Markets and Production Countries/Regions table, choose Add. | The Assign Countries/Regions dialog opens. |  |
| 7 | Select the countries/regions | Select any EU country/region, for example, Germany. Then choose OK. | The selected country/region is added to the Assess Markets and Production Countries/Regions table. |  |
| 8 | Process Market Request for Production | Choose the row for the newly added country/region. For these countries/regions. | A second screen opens in edit mode with the name of the country/region displayed at the top. |  |
| 9 | Enter Assessment | In the Compliance per Business Process section, choose Allowed from the dropdown list for the required Assessment Status for Production and Assessment Status for Sales fields. Then choose Apply. | The value Allowed is entered in the required Assessment Status for Production and Assessment Status for Sales fields. |  |
| 10 | Save Your Assessment | Choose Save. | A message confirming that your changes have been saved is displayed on the screen. |  |

### Assess Product Marketability Based on Supplier Compliance Disclosures

#### Assign Compliance Purpose to Unpackaged Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The unpackaged product must meet the compliance requirements related to supply chain due diligence acts. The Product Stewardship Specialist - Product Compliance assigns these compliance requirements to the unpackaged product via the relevant compliance purpose.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Manage Basic Compliance Data - Unpackaged Products (F2641) tile. | The Manage Basic Compliance Data - Unpackaged Products screen is displayed. |  |
| 3 | Search Unpackaged Product | Enter the product name Semi <your name> 31H2 in the Search field. | The table is filtered for entries that match the fuzzy search. |  |
| 4 | Navigate to Basic Compliance Data | Choose the row for the unpackaged product Semi <your name> 31H2. | The Unpackaged Product - Basic Compliance Data screen opens in display mode. |  |
| 5 | Switch to Edit Mode | On the Unpackaged Product - Basic Compliance Data screen, choose Edit. | The app is in edit mode. |  |
| 6 | Select Assigned Compliance Purpose | In the Application, Uses, Markets and Purposes section, Assigned Compliance Purposes table, select Product Default Compliance Purpose. | The selected row is highlighted in blue. |  |
| 7 | Remove Default Compliance Purpose | For the Assigned Compliance Purposes table, choose Remove. In the Remove dialog that appears, choose Remove again. | The Product Default Compliance Purpose is removed from the Assigned Compliance Purposes table. |  |
| 8 | Add Compliance Purpose | For the Assigned Compliance Purposes table, choose Add. | The Assign Compliance Purposes dialog opens. |  |
| 9 | Choose Your Compliance Purpose | Search for the compliance purpose <your name> 31H2. Select it, and then choose OK. | The compliance purpose <your name> 31H is added to the Assigned Compliance Purposes table. |  |
| 10 | Save Unpackaged Product | On the Unpackaged Product - Basic Compliance Data screen, choose Save. | A success message indicates that the unpackaged product has been saved. |  |

#### Open Marketability Assessment and Check Compliance Declarations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The system has checked the product structure of your unpackaged product and identified the suppliers of the raw materials in the before-production material-based composition. The system identifies for which suppliers a compliance declaration already exists for the compliance declaration and for which suppliers the compliance declaration is missing. You open the marketability assessment for the product as a Product Stewardship Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Assess Marketability Requirements - For Products (F3219) tile. | The app opens. |  |
| 3 | Search Unpackaged Product | Enter the product name Semi <your name> 31H2 in the Search field, and then press Enter. | The Unreleased Marketability Assessments table is filtered for entries that match the fuzzy search. |  |
| 4 | Navigate to Marketability Assessment | Choose the row for the marketability assessment with Semi <your name> 31H2 in the Product Name column, and US Dodd-Frank Act in the Compliance Requirement Version column. | The Marketability Assessment screen opens. |  |
| 5 | Navigate to Supplier Compliance Declarations | On the Marketability Assessment screen, choose the Supplier Compliance Declarations tab. | The screen scrolls down to the Supplier Compliance Declarations section. The table includes the following suppliers:<Your name> Supplier 1 with the following data:Status: CompletedMarketability Status: Compliant<Your name> Supplier 2 with the following data:Status: RequiredMarketability Status: Unknown |  |

#### Analyze Target State and Current State of Compliance Disclosures for Suppliers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance asks the Master Data Specialist - Product Compliance to verify the status of Domestic UAE Supplier 1 and Domestic Supplier 2 for the compliance requirement version US Dodd-Frank Act based on the existing supplier compliance disclosures. The Master Data Specialist - Product Compliance analyzes the current state and target state of compliance disclosures for these suppliers in the Analyze Compliance Disclosures - For Suppliers app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Master Data Specialist - Product Compliance (SAP_BR_MD_SPECIALIST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose the Analyze Compliance Disclosures - For Suppliers (F7460) tile. | The analytic list page for supplier compliance disclosures is displayed. |  |
| 3 | Switch Filter View | Switch the header filter view by choosing the <!-- image omitted: unnamed -->(Compact Filter) icon. | The header filter view switches to a more compact version without graphs. |  |
| 4 | Filter for Required and Completed Declarations | In the dropdown list for the Status filter, keep Completed selected, and select Required. | Completed and Required appear in the Status field. |  |
| 5 | Remove Compliance Status Filter | In the Compliance Status field, remove the Not Compliant filter. | The Compliance Status field is empty. |  |
| 6 | Open Value Help for Compliance Requirement Filter | Open the value help for Compliance Requirement. | The Compliance Requirement dialog opens. |  |
| 7 | Select Compliance Requirement | In the Items list in the Compliance Requirement dialog, select US-Dodd-Frank Act. Then choose OK.Note If US-Dodd-Frank Act doesn't appear in the list, remove the Status and Compliance Status filters, choose Go, and then check the list again. | The dialog closes, and US-Dodd-Frank Act appears in the Compliance Requirement field. |  |
| 8 | Open Value Help for Supplier Filter | Open the value help for Supplier. | The Supplier dialog opens. |  |
| 9 | Select Suppliers | In the Supplier dialog, remove the Status and Compliance Status filters, and then choose Go. In the Items list, choose the Supplier heading, and sort the list ascending by supplier name. In the sorted list, select <your name> Supplier 1 and <your name> Supplier 2. Then choose OK in the Supplier dialog.Note In the value help, search for the suppliers by their supplier numbers. For supplier numbers under 10 characters, add leading zeroes as necessary. | The dialog closes, and 2 Items is displayed as a hyperlink in the Supplier field. If you choose the link, <your name> Supplier 2 are displayed. |  |
| 10 | Filter the Compliance Declarations Table | On the Analyze Compliance Disclosures - For Suppliers screen, choose Go. | The Compliance Declarations table is filtered for declarations for the following suppliers for the compliance requirement version US Dodd-Frank Act:<your name> Supplier 1 with the following data:Status: CompletedCompliance Status: CompliantType: Self-Assessment<your name> Supplier 1 with the following data:Status: RequiredCompliance Status: UnknownType: Compliance Disclosure Template<your name> Supplier 2 with the following data:Status: RequiredCompliance Status: UnknownType: Compliance Disclosure TemplateBased on this information, the Master Data Specialist - Product Compliance verifies the information provided in the marketability assessment. |  |

#### Process Required Disclosure Template for Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After verifying that a compliance declaration is required for Domestic Supplier 2 for US Dodd-Frank Act, the Master Data Specialist - Product Compliance has contacted the supplier and received a compliance disclosure in the form of a self-assessment. Based on this data, the Master Data Specialist - Product Compliance assesses the compliance of the supplier with the relevant supply chain due diligence act.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Compliance Disclosures - For Suppliers (F7370) app. | The Process Compliance Disclosures - For Suppliers screen is displayed. |  |
| 3 | Create Compliance Disclosure | For the Compliance Disclosures table, choose Create. | The Create dialog opens. |  |
| 4 | Provide Header Data | In the Create dialog, provide the following data:Supplier: Business partner number for <your name> Supplier 2Type: Self-AssessmentDate of Receipt: <today's date>Then choose Create. | The Compliance Disclosure screen opens. |  |
| 5 | Open Value Help for Compliance Requirement Version | In the Compliance Declarations table, Compliance Requirement Version field, open the value help. | The Select: Compliance Requirement Version dialog opens. |  |
| 6 | Select Compliance Requirement Version | Choose the compliance requirement version with US-Dodd-Frank Act in the Compliance Requirement column. | The Select: Compliance Requirement Version dialog closes. On the Compliance Disclosure screen, in the Compliance Declarations table, the newly added compliance requirement version appears in the Compliance Requirement Version column. |  |
| 7 | Assess Supplier as Compliant | In the Compliance Declarations table, Supplier Compliance Status column, select Compliant from the dropdown list in the row for US Dodd-Frank Act. | In the Compliance Declarations table, Compliant appears in the Supplier Compliance Status column for US Dodd-Frank Act. |  |
| 8 | Optional: Add a Remark | Optional: In the Compliance Declarations table, Supplier Compliance Status column, in the row for US Dodd-Frank Act, enter a remark. | In the Compliance Declarations table, Remark column, your remark is displayed for US Dodd-Frank Act. |  |
| 9 | Optional: Upload an Attachment | Optional: In the Attachments section, choose Upload, and select a file from your computer. | The uploaded file appears in the Attachments section, and a success message confirms that the file has been uploaded. |  |
| 10 | Finalize Creation of Compliance Disclosure | Choose Create. | A success message confirms that the object was created. |  |
| 11 | Set Compliance Disclosure to Completed | On the Compliance Disclosure screen, choose Set to Completed. | In the Compliance Declarations table, the value in the Effective column for US Dodd-Frank Act has changed to Yes. |  |

#### Optional: Check Marketability Assessments of Raw Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Now, the Master Data Specialist - Product Compliance has provided the required compliance declaration and set it to Compliant, in addition to the existing compliance declaration. The Master Data Specialist - Product Compliance checks that the marketability status of the raw materials has been set accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance (SAP_BR_MD_SPECIALIST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Master Data Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Assess Marketability Requirements - For Raw Materials (F3221) tile. | The app opens. |  |
| 3 | Search Raw Material | Enter the raw material name <your name> RM 31H in the Search field, and then press Enter. | The Unreleased Marketability Assessments table is filtered for entries that match the fuzzy search. |  |
| 4 | Navigate to Marketability Assessment | Choose the row for the marketability assessment with <your name> RM 31H in the Raw Material Name column, and US Dodd-Frank Act in the Compliance Requirement Version column. | The Marketability Assessment screen opens. |  |
| 5 | Navigate to Supplier Compliance Declarations | On the Marketability Assessment screen, choose the Supplier Compliance Declarations tab. | The screen scrolls down to the Supplier Compliance Declarations section. The table includes the supplier <your name> Supplier 1 with the following data:Status: CompletedMarketability Status: Compliant |  |
| 6 | Navigate Back | Navigate back. | The Assess Marketability Requirements - For Raw Materials screen is displayed, and is filtered for entries that match the fuzzy search for <your name> RM 31H. |  |
| 7 | Navigate to Marketability Assessment | Choose the row for the marketability assessment with <your name> RM 31H2 in the Raw Material Name column, and US Dodd-Frank Act in the Compliance Requirement Version column. | The Marketability Assessment screen opens. |  |
| 8 | Navigate to Supplier Compliance Declarations | On the Marketability Assessment screen, choose the Supplier Compliance Declarations tab. | The screen scrolls down to the Supplier Compliance Declarations section. The table includes the supplier <your name> Supplier 2 with the following data:Status: CompletedMarketability Status: CompliantYou've verified that both relevant raw materials are compliant with the compliance requirement version US Dodd-Frank Act based on the supplier compliance declarations. |  |

#### Open Marketability Assessment and Check Compliance Declarations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance has provided the missing compliance declaration and checked the marketability assessments of both affected raw materials. To verify that the unpackaged product is now compliant with the US Dodd-Frank Act, you open the marketability assessment for the product as a Product Stewardship Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Choose the Assess Marketability Requirements - For Products (F3219) tile. | The app opens. |  |
| 3 | Search Unpackaged Product | Enter the product name Semi <your name> 31H2 in the Search field, and then press Enter. | The Unreleased Marketability Assessments table is filtered for entries that match the fuzzy search. |  |
| 4 | Navigate to Marketability Assessment | Choose the row for the marketability assessment with Semi <your name> 31H2 in the Product Name column, and US Dodd-Frank Act in the Compliance Requirement Version column. | The Marketability Assessment screen opens. The marketability status of the unpackaged product is Compliant. |  |
| 5 | Navigate to Supplier Compliance Declarations | On the Marketability Assessment screen, choose the Supplier Compliance Declarations tab. | The screen scrolls down to the Supplier Compliance Declarations section. The table includes the following suppliers:<Your name> Supplier 1 with the following data:Status: CompletedMarketability Status: Compliant<Your name> Supplier 2 with the following data:Status: CompletedMarketability Status: CompliantYou've verified that the marketability status of both suppliers, as well as the unpackaged product itself, is Compliant. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 31J – Chemical Compliance in the Value Chain | Product SG<your name>31H is assessed as Allowed for the Produce In and Sell In business processes in the relevant country/region. |

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
> Flagged while digesting this document, not verified: The Create Analytical Composition purpose says the unpackaged product consists of only one substance, m-xylene, but the test steps and expected results use DEHP (CAS 117-81-7) as that single substance.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/substance-volume-tracking-4ol-ae-test-script-sap-s-4hana-cloud-public]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-chemical-compliance-approval-for-purchased-material-and-su]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31H_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 90,521 chars in the whole document
