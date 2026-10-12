---
id: 13-quality-ehs-and-compliance/product-compliance-document-authoring-7do-ae-test-script-sap-s-4hana-c
title: "Product Compliance Document Authoring (7DO_AE) - Test Script, SAP S/4HANA Cloud Public Edition (7DO_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 7DO: step-by-step product compliance data entry through to German safety data sheet generation."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/safety-data-sheets-and-labels]
aliases: [7DO_S4CLD2608_BPD_EN_AE]
keywords: ["Safety Data Sheet Authoring, Distribution and Labels", safety data sheet generation, product compliance, unpackaged products, analytical composition, product properties, dangerous goods, marketability assessments, compliance assessments, substance classification]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DO_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1212
topic: 13-quality-ehs-and-compliance/safety-data-sheets-and-labels
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Product Compliance Document Authoring (7DO_AE) - Test Script, SAP S/4HANA Cloud Public Edition (7DO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Safety Data Sheet Authoring, Distribution and Labels** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Product Compliance Document Authoring (7DO_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Product Compliance Document Authoring (7DO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860135)

[2 Prerequisites 4](#_Toc232860136)

[2.1 System Access 4](#_Toc232860137)

[2.2 Roles 4](#_Toc232860138)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860139)

[2.4 Business Conditions 7](#_Toc232860140)

[2.5 Preliminary Steps 7](#_Toc232860141)

[2.5.1 Specify Legal Area 7](#_Toc232860142)

[2.5.2 Apply Regulations 9](#_Toc232860143)

[2.5.3 Create Business Partner – Company Address 10](#_Toc232860144)

[2.5.4 Create Business Partner – SDS Contact Mail 11](#_Toc232860145)

[2.5.5 Create Product Master Record 11](#_Toc232860146)

[2.5.6 Enter Contact Data for Safety Data Sheets 12](#_Toc232860147)

[2.5.7 Assign Template for Safety Data Sheet Generation 14](#_Toc232860148)

[3 Overview Table 15](#_Toc232860149)

[4 Test Procedures 16](#_Toc232860150)

[4.1 Create Unpackaged Product 16](#_Toc232860151)

[4.2 Create Analytical Composition 18](#_Toc232860152)

[4.3 Create Product Identifiers 19](#_Toc232860153)

[4.4 Create Properties of Unpackaged Product 21](#_Toc232860154)

[4.5 Provide Transport Information 26](#_Toc232860155)

[4.6 Carry Out Marketability Assessments 28](#_Toc232860156)

[4.7 Carry Out Compliance Assessments 29](#_Toc232860157)

[4.8 Classify Substances 32](#_Toc232860158)

[4.9 Identify Hazardous Ingredients 33](#_Toc232860159)

[4.10 Generate and View Safety Data Sheet 36](#_Toc232860160)

## Purpose

Overview

Products might pose risks throughout the value chain that many industries handle by creating structured communication documents (often regulated by law). This scope item covers the main process steps for generating product-compliance-relevant documents, using the structure of a safety data sheet as an example.

To create product compliance documents, you may need to gather a large amount of data that must be systematically structured and assessed. To facilitate this, a work view provides you with easy access to both compliance requirements and apps for entering relevant properties. You can efficiently control document output by adapting the template structure to your needs.

|  |
| --- |
| Note This document covers the process of safety data sheet generation for a specific product only for Germany as initial step, in order to demonstrate the capabilities of the solution in a simpler way. All the phrases mentioned in the document are just an example and can be changed or others to be assigned, according to your preferences or needs. |

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
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Dangerous Goods Specialist - Product Compliance | SAP_BR_DG_SPLST_PCL | Dangerous Goods | SAP_BR_DG_SPLST_PCL |  |
| Master Data Specialist - Product Compliance | SAP_BR_MD_SPECIALIST_PCL | Master Data - Product Compliance | SAP_BR_MD_SPECIALIST_PCL |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Product | FGPC01 | Product Type: Finished Product (FERT)Product Description: Product Compliance Finished GoodCompliance Relevant: Yes | Loaded via scope item. |
| Listed Substance | L00000008268 | CAS Number: 151-21-3Name: SODIUM LAURYL SULFATE | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000002558 | CAS Number: 71-23-8Name: n-Propyl alcohol | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000029504 | CAS Number: 5989-27-5Name: d-Limonene | Included in the listed substance index, which is delivered with the software. |
| Company Substance | SODIUM LAURYL SULFATE | Linked with listed substance L00000008268 | Loaded via scope item. |
| Company Substance | n-Propyl alcohol | Linked with listed substance L00000002558 | Loaded via scope item. |
| Company Substance | d-Limonene | Linked with listed substance L00000029504 | Loaded via scope item. |
| Compliance Purpose | Demo Purpose for DE SDS Generation | The following compliance requirements are assigned:DE-SDSADNIATA-DGRIMDG-CodeADRRIDUNRTDGEU-Poison Centre NotificationWorld-Personal ProtectionDE-TRGS 510 Storage classWorld Handling and StorageWorld-First Aid MeasuresWorld-Firefighting MeasuresWorld-Accidental ReleaseDE-Water Hazard class (WGK)EU-Hazardous IngredientsEU-GHS ClassificationEU-GHS Labeling | Requirements are relevant for Germany.Loaded and activated via scope item. |
| Sales Organization | 3310 | Dom. Sales Org |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1LQ - Output Management | The 1LQ scope item must be implemented and tested before testing 7DO scope item. |

### Preliminary Steps

#### Specify Legal Area

Use

The configuration expert needs to specify all legal areas that you want to use within your safety data sheet processes.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Specify Legal Areas for Product Compliance | On the Configure Your Solution screen, search for the following configuration step: Specify Legal Areas for Product Compliance. Press Enter.In the search result, select the configuration activity and go to the next screen.On the Configure Your Solution – General Configuration screen, go to the configuration step Specify Legal Areas for Product Compliance and choose Configure. | The Specify Legal Areas for Product Compliance: Change screen is displayed. |  |
| 5 | Specify Legal Areas | If an entry for European Union already exists, skip the following step.Otherwise, choose New Entries and make the following entries in the respective fields:Legal Area: ZEULegal Area Name: European Union | The new entry is created. |  |
| 6 | Assign Countries/Regions | Select the created line and choose Country/Region Assignment in the tree on the left-hand side of the screen.Choose New Entries and make the following entries:Ctry/Reg: DEAssign other countries/regions that are part of the European Union, if needed.Choose Save. | Country/region assignment is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to Configuration Activity | From the Activities list on the left-hand side, navigate to the Configuration entry and search for the following activity: Specify Legal Areas for Product Compliance.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The change view of Specify Legal Areas for Product Compliance screen is displayed. |  |
| 3 | Specify Legal Areas | If an entry for European Union already exists, skip the following step.Otherwise, choose New Entries and make the following entries in the respective fields:Legal Area: ZEULegal Area Name: European Union | The new entry is created. |  |
| 4 | Assign Country | Select the created line and choose Country/Region Assignment in the tree on the left-hand side of the screen.Choose New Entries and make the following entries:Ctry/Reg: DEAssign other countries/regions that are part of the European Union, if needed.Choose Save. | Country/region assignment is created. |  |

#### Apply Regulations

Use

The product stewardship specialist for product compliance has to ensure that the relevant compliance requirements for safety data sheet regulations for the respective country/region are specified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance |  |  |
| 2 | Access App | Open Apply Regulations - Safety Data Sheets (F3984). | The Apply Regulations – Safety Data Sheets screen is displayed. |  |
| 3 | Select Country/Region | Choose Germany on the map. | The country/region should be marked in green.The country/region detail screen is displayed.In the Classification section, you can see the DE - SDS compliance requirement.In Safety Data Sheet Languages section, you can see language DE.In the Assigned Compliance Purposes section, you can see the purpose Demo Purpose for DE SDS Generation. |  |

#### Create Business Partner – Company Address

Use

The master data specialist for business partner data has to create a business partner whose address is printed for your company in the safety data sheets.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data |  |  |
| 2 | Access App | Open Manage Business Partner Master Data (F3163). | The Manage Business Partner screen is displayed. |  |
| 3 | Create a Business Partner | On the Manage Business Partner screen, choose Create and from the dropdown list, choose Organization.In the Create Organization dialog box, enter data for the following fields:Note Enter an address for your organization in the respective country/region.Name 1StreetHouse NumberCityPostal CodeCountry/Region : GermanyChoose OK . | The Business Partner screen is displayed with the data you have entered. |  |
| 4 | Save Your Entry | Choose Create.Note down the ID of the business partner:________________ | The new business partner is created.In the header, the entered name is displayed with the business partner ID underneath. |  |

#### Create Business Partner – SDS Contact Mail

Use

The master data specialist for business partner data has to create a business partner that you can use as a point of contact for your company in the safety data sheets.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open Manage Business Partner Master Data (F3163). | The Manage Business Partner screen is displayed. |  |
| 3 | Create a Business Partner | On the Manage Business Partner screen, choose Create and from the dropdown list, choose Person.In the Create Person dialog box, enter data for the following fields:First NameLast NameIn the Standard Address section, enter an address in the respective country:StreetHouse NumberPostal CodeCityCountry/Region : GermanyChoose OK. | The Business Partner screen is displayed with the data you have entered. |  |
| 4 | Enter Email Address | In the Address section, in the Standard Communication subsection, enter your email address and choose Create.Note down the ID of the business partner:________________ | The new business partner is created.In the header, the entered name is displayed with the business partner ID underneath. |  |

#### Create Product Master Record

Use

The master data specialist for product data has to create a unique product master data record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen is displayed. |  |
| 3 | Copy a Product | On the Manage Product Master Data screen, search for the FGPC01 product. Choose Go.In the search result, select the checkbox for the Product Compliance Finished Good (FGPC01) and choose Copy.In the Select Organizational Data to Copy dialog box, keep the selection for plants and distribution chains and choose OK. | The Create Master Data Record dialog box is displayed. |  |
| 4 | Create a Master Record | Enter a description in the Description field and leave all other fields with default values.Choose OK. | The Product screen is displayed. |  |
| 5 | Change Translations | In Descriptions section, change the text in the Product field for the relevant languages. |  |  |
| 6 | Save Your Entries | Choose Create to save your entries.If a warning for a potential duplicate appears, choose Create to proceed.Note down the following data:Product Description: _______________Product Number: ________________ | The product master record is created.In the header, the entered product description is displayed with the product number underneath. |  |

#### Enter Contact Data for Safety Data Sheets

Use

The product stewardship specialist for product compliance enters the in-house contact persons for safety data sheets. There could be more than one person in the company that is responsible for diﬀerent sales organizations or countries/regions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Manage Contact Data (F4521) app. | The Manage Contact Data – Safety Data Sheets screen is displayed. |  |
| 3 | Create a New Contact Person | On the Manage Contact Data – Safety Data Sheets screen, choose Create. | The New Safety Data Sheet Contact column is displayed on the right. |  |
| 4 | Enter Contact Header Data | In the Contact Header, enter the following data:Product: <Product Number> of the product that you have created in the [Create Product Master Record](#unique_11) [page ] 11 preliminary step.Sales Organization: 3310Note The restriction on a specific product is a very rare use case. It is used here for test purposes, so multiple persons can test on the same system with different products without interfering. |  |  |
| 5 | Add a Company Address | In the Addresses section, enter the following data:Address Type: Company AddressBusiness Partner: <Business Partner ID> of the business partner that you have created in the [Create Business Partner – Company Address](#unique_9) [page ] 10 preliminary step. |  |  |
| 6 | Add an SDS Contact Mail | In the Addresses section, enter the following data:Address Type: SDS Contact MailBusiness Partner: <Business Partner ID> of the business partner that you have created in the [Create Business Partner – SDS Contact Mail](#unique_10) [page ] 11 preliminary step. |  |  |
| 7 | Add an Emergency Phone Number | In the Emergency Phone Numbers section, select a language from the dropdown list, for example German.Enter a phone number. | The emergency phone number for the company is entered. |  |
| 8 | Add a Logo | In the Logo section, select a logo.Note If no logo is available, you can upload a logo in the Manage Logos (F2761) app as an Extensibility Specialist. Note that this is only possible on a system with extensibility activated. |  |  |
| 9 | Save Your Entries | Choose Create to save your entries and create the contact data. | The safety data sheet contact is created. |  |

#### Assign Template for Safety Data Sheet Generation

Use

The product stewardship specialist for product compliance assigns a document template that is to be used for the generation of the safety data sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Activate Compliance Requirements - Safety Data Sheets (F8003) app. | The Activate Compliance Requirements screen is displayed. |  |
| 3 | Find Compliance Requirement Version | On the Activate Compliance Requirements screen, choose the Active tab and search for the DE-SDS compliance requirement.In the search results, find the active compliance requirement version and choose Edit from the Configuration column for the respective row. | The Configure Compliance Requirements - SDS screen is displayed. |  |
| 4 | Assign Template | Choose Edit.In the Generation section, in the SDS Template, enter or use the value help to select the SDS_STARTER template.Note If the template is already entered, you can skip this step.Choose Save. | The selected template is assigned to the compliance requirement version. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Unpackaged Product](#unique_15) [page ] 16 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | Unpackaged product is created, related product master is assigned, uses of the product are maintained and compliance purpose for SDS generation assigned. |
| [Create Analytical Composition](#unique_16) [page ] 18 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | The analytical composition of the unpackaged product is created and released. |
| [Create Product Identifiers](#unique_17) [page ] 19 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | Identifiers are created. |
| [Create Properties of Unpackaged Product](#unique_18) [page ] 21 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | The physical-chemical, safety-related, stability and reactivity, toxicological and ecological properties of the unpackaged product are created and released. |
| [Provide Transport Information](#unique_19) [page ] 26 | Dangerous Goods Specialist - Product Compliance. | My Unpackaged Dangerous Goods (F3643) | Dangerous goods transport information is created and released. |
| [Carry Out Marketability Assessments](#unique_20) [page ] 28 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | Marketability assessments are released. |
| [Carry Out Compliance Assessments](#unique_21) [page ] 29 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | All required compliance assessments are carried out and released. |
| [Classify Substances](#unique_22) [page ] 32 | Master Data Specialist - Product Compliance | Manage Substances Compliance (F2578) | Hazardous classification of substances is done. |
| [Identify Hazardous Ingredients](#unique_23) [page ] 33 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | Hazards are identified. |
| [Generate and View Safety Data Sheet](#unique_24) [page ] 36 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | Safety data sheet is generated. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Unpackaged Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product stewardship specialist for product compliance creates an unpackaged product, assigns a related product from the product master and a compliance purpose.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The Manage Basic Compliance Data – Unpackaged Products screen is displayed. |  |
| 3 | Create Header Data for a New Product | On the Manage Basic Compliance Data – Unpackaged Products screen, choose Create.In the New Product dialog box, enter the following data:Internal Name: <product name>Note Note down the internal name you have entered as it is needed in the following procedures: ________________Product Categorization: MixtureLeave all other fields with default values and choose Save. | The header data is created and the Unpackaged Product - Basic Compliance Data screen is displayed. |  |
| 4 | Assign Product Master | On the Unpackaged Product - Basic Compliance Data screen, choose Edit.In the Assigned Products section, in the Related Products in Product Master table, enter the product number, that you have created in the [Create Product Master Record](#unique_11) [page ] 11 preliminary step. | The related product is assigned. |  |
| 5 | Assign Uses | In the Applications, Uses, Markets, and Purposes section, in the Assigned Uses table, choose Create.In the Create Use dialog box, select the European Union entry.Select the newly created row in the Assigned Uses table for more details. | The Unpackaged Product – Uses screen is displayed. |  |
| 6 | Enter Recommended Uses | Choose Edit.In the Recommended Uses table, make the following entries:Cleansing agents, acidic.Laboratory chemicalsManufacture of chemical productsLeave the default value Public for the Use of Data field for all entries. |  |  |
| 7 | Enter Restrictions on Use | In the Restrictions on Use table, make the following entries:Drug precursorFood additiveNot to be used as a biocidal product.Leave the default value Public for the Use of Data field for all entries. |  |  |
| 8 | Release Uses Data | Choose Save.Choose Release.Navigate back to the Unpackaged Product - Basic Compliance Data screen. |  |  |
| 9 | Remove the Default Compliance Purpose | In the Application, Uses, Markets, and Purposes section, in the Assigned Compliance Purposes table, select the checkbox for the Product Default Compliance Purpose and choose Remove. | Default purpose is removed. |  |
| 10 | Add a Compliance Purpose | In the Assigned Compliance Purposes table, choose Add.In the newly opened Assign Compliance Purposes dialog box, search for the following purpose:Demo Purpose for DE SDS GenerationSelect the purpose and choose OK. | The selected purpose is assigned. |  |
| 11 | Save Your Entries | Choose Save. | Data is saved and the Unpackaged Product - Basic Compliance Data screen is shown in display mode.The compliance assessments are calculated asynchronously in the background. |  |

### Create Analytical Composition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product stewardship specialist for product compliance creates and releases the analytical composition of the unpackaged product. The analytical composition provides the chemical analysis of the unpackaged product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The Manage Basic Compliance Data – Unpackaged Products screen is displayed. |  |
| 3 | Open Unpackaged Product | On the Manage Basic Compliance Data – Unpackaged Products screen, search for the unpackaged product that you have created in the [Create Unpackaged Product](#unique_15) [page ] 16 procedure. Press Enter.In the search result, select your unpackaged product and go to the next screen. | The Unpackaged Product – Basic Compliance Data screen is shown in display mode. |  |
| 4 | Go to the Analytical Composition | Go to the Compositions section.Select the row with the following details:Composition: Analytical CompositionLegal Area: (World)On the Unpackaged Product - Analytical Composition screen, choose Edit. | The Unpackaged Product - Analytical Composition screen is displayed in edit mode. |  |
| 5 | Add Substances | In the Analytical Components table, choose Add. In the Assign Substances dialog box, search for and select the following substances:SODIUM LAURYL SULFATE with a CAS number 151-21-3n-Propyl alcohol with a CAS number 71-23-8d-Limonene with a CAS number 5989-27-5 | The selected substances are added to the table with a label New Substance in the Changes Since Last Release column. |  |
| 6 | Specify Concentration | In the Concentration column of the Analytical Components table, enter the following concentration for each substance, respectively:SODIUM LAURYL SULFATE: 20n-Propyl alcohol: 75d-Limonene: 5Leave the other fields with their default values. | The concentration of the substances is specified. |  |
| 7 | Save and Release the Composition | Choose Save, then Release. | The analytical composition is created and released. |  |

### Create Product Identifiers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product stewardship specialist for product compliance can create product identifiers for the unpackaged product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Unpackaged Products (F2641) app. | The Manage Basic Compliance Data – Unpackaged Products screen is displayed. |  |
| 3 | Open Unpackaged Product | On the Manage Basic Compliance Data – Unpackaged Products screen, search for the unpackaged product that you have created in the [Create Unpackaged Product](#unique_15) [page ] 16 procedure. Press Enter.In the search result, select your unpackaged product and go to the next screen. | The Unpackaged Product – Basic Compliance Data screen is shown in display mode. |  |
| 4 | Add an Identifiers Property Group | Go to the Properties section and navigate to the details of the Identifiers property group.If the property group Identifiers is not displayed, choose Create.In the newly opened Create Property Group dialog box, select the property group Identifiers. | The new property group is added to the table. |  |
| 5 | Enter Identifiers for Names | Select the Identifiers row to navigate to the details.Choose Edit.In the Identifiers section, in the Names table, enter the following data:Type: select a type from the dropdown listLegal Area: European Union (ZEU)Language: EN, DENote You need to create separate rows in the table for each language.Name: enter a name for the respective language | The identifiers for names are entered. |  |
| 6 | Enter Identifiers for Numbers | In the Identifiers section, in the Numbers table, make the following entries in the respective columns:Type: select a type from the dropdown listLegal Area: European Union (ZEU)Number: enter an appropriate number for identification | The identifiers for numbers are entered. |  |
| 7 | Save Your Entries | Choose Save, then Release. | The product identifiers are created. |  |

### Create Properties of Unpackaged Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product stewardship specialist for product compliance creates physical-chemical properties, safety-related properties, stability and reactivity, toxicological information, and ecological information for the unpackaged product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The Manage Basic Compliance Data – Unpackaged Products screen is displayed. |  |
| 3 | Open Unpackaged Product | On the Manage Basic Compliance Data – Unpackaged Products screen, search for the unpackaged product that you have created in the [Create Unpackaged Product](#unique_15) [page ] 16 procedure. Press Enter.In the search result, select your unpackaged product and go to the next screen. | The Unpackaged Product – Basic Compliance Data screen is shown in display mode. |  |
| 4 | Enter Physical-Chemical Properties | Go to Properties section and select Physical-Chemical Properties to navigate to the next screen.On the Unpackaged Product - Physical-Chemical Properties screen, choose Edit.In the General section, make the following entries:Physical State at 20° (68°F), 101.3kPa: liquidPhysical State at 40° (104°F), 101.3kPa: liquidForm at 20° (68°F), 101.3 kPa: liquidColor: colorlessOdor: citrusOdor Threshold: Select the No Data Available checkboxMolar mass: Select the No Data Available checkboxIn the Particles, make the following entries:Particle Size: Select the No Data Available checkboxParticle Size Distribution : Select the No Data Available checkboxIn the Density section, make the following entries:Density at 15 °C (59 °F): 0.88 kg/m3Density at 20 °C (68 °F): 0.87 kg/m3Density at 50 °C (122 °F): 0.85 kg/m3Relative Density: Select the No Data Available checkboxBulk Density: Select the No Data Available checkboxRelative Vapor Density: Select the No Data Available checkboxIn the Viscosity section, make the following entries:Flow Time: Select the No Data Available checkboxDynamic Viscosity: Select the No Data Available checkboxKinematic Viscosity: Select the No Data Available checkboxIn the Solutions section, make the following entries:In the Solubility in Water subsection:Assessment: completely miscibleIn the pH subsection:Measured pH Value at 20°C (68°F): <5Concentration: 23Assessment: acidicIn the Phase Transitions section, make the following entries:Melting Point: Select the No Data Available checkboxBoiling Point: 70 °CVapor Pressure at 20 °C (68 °F) .: 35 hPaIn the Evaporation Rate subsection:Evaporation Rate: 0.3Additional Statement: (Diethylether=1.0)Partition Coefficient n-Octanol/Water: Select the No Data Available checkboxNote You can enter any other relevant information in the respective fields.Choose Save, then Release.Navigate back to the Unpackaged Product - Basic Compliance Data screen. | The physical-chemical properties of the product are released. |  |
| 5 | Enter Safety-Related Properties | Go to Properties section and select Safety-Related Properties to navigate to the next screen.On the Unpackaged Product - Safety-Related Properties screen, choose Edit.In the Flammability section, make the following entries:In the Flammability of Liquids subsection:Assessment: Ignitable (see flash point)Flammability of Gases/Solids: Select the No Data Available checkboxIn the Flash Point subsecion:Closed Cup: 22 °CMethod for Closed Cup: Regulation (EC) No. 440/2008, Annex, A.9In the Auto-Ignition Temperature subsection:Temperature: 412 °CFire Point: Select the No Data Available checkboxIn the Lower Explosion/Flammability Limit subsection:Type: Lower explosion limitLower Explosion/Flammability Limit: 4 %(V)Upper Explosion/Flammability Limit: Select the No Data Available checkboxIn the Heat of Combustion subsection:Heat of Combustion: 66Burning Rate: Select the No Data Available checkboxMinimum Ignition Energy: Select the No Data Available checkboxSelf Ignition: Select the No Data Available checkboxSelf Heating: Select the No Data Available checkboxIn the Reaction and Stability section, make the following entries:Thermal Decomposition Temperature: Select the No Data Available checkboxOxidizing: Select the No Data Available checkboxIn the Corrosion of Metals subsection:Corrosion Rate: <1Assessment: (Met. Corr.) Corrosive to metalsPeroxides: Select the No Data Available checkboxSolvent Separation Test: Select the No Data Available checkboxIn the Explosiveness section, make the following entries:In the Explosiveness subsection:Assessment: (EUH018) In use may form flammable/explosive vapor-air mixture.Dust Explosion Class: Select the No Data Available checkboxIn the Other Hazards section, select the No Data Available checkbox.Choose Save, then Release.Navigate back to the Unpackaged Product - Basic Compliance Data screen. | The safety-related properties of the product are released. |  |
| 6 | Enter Information About Stability and Reactivity | Go to Properties section and select Stability and Reactivity to navigate to the next screen.Note If you don't see the Stability and Reactivity property group in the table, choose Create to add it.On the Stability and Reactivity screen, choose Edit.Make the following entries:Reactivity: None reasonably foreseeable.Chemical Stability: Stable under normal conditions.Hazardous Reactions: None reasonably foreseeable.Conditions to Avoid: Stable under recommended storage conditions.Incompatible Materials: No data availableIn the Hazardous Decomposition Products table, choose Set Reason for No Data and select No decomposition if stored and applied as directed.:Reference to Other Sections: Decomposition products in case of fire: see section 5.Choose Save, then Release.Navigate back to the Unpackaged Product - Basic Compliance Data screen. | The information about stability and reactivity is released. |  |
| 7 | Enter Toxicological Information | Go to Properties section and select Toxicological Information to navigate to the next screen.On the Unpackaged Product - Toxicological Information screen, choose Edit.Make the following entries by choosing Create for the respective section:In the Acute Oral Toxicity section, Assessment: The component/mixture is toxic after single ingestion.In the Acute Dermal Toxicity section, Assessment: The component/mixture is minimally toxic after single contact with skin.In the Skin Irritation section, Assessment: Mild skin irritationIn the Eye Irritation section, Eye Irritation Assessment: Assessment: Irritating to eyes.In the Respiratory Sensitization section, Assessment: May cause sensitization by inhalation.In the Skin Sensitization section, Assessment: May cause sensitization by skin contact.Choose Save, then Release.Navigate back to the Unpackaged Product - Basic Compliance Data screen. | The toxicological information for the product is released. |  |
| 8 | Enter Ecological Information | Go to Properties section and select Ecological Information to navigate to the next screen.Note If you don't see the Ecological Information property group in the table, choose Create to add it.On the Unpackaged Product - Ecological Information screen, choose Edit.In the Assessment section, make the following entries:Acute Aquatic Toxicity: (H402) Harmful to aquatic life.Chronic Aquatic Toxicity: (H413) May cause long lasting harmful effects to aquatic life.In the Acute and Prolonged Toxicity to Fish table, chose Create and make the following entries:Species: Pimephales promelas (fathead minnow)Exposure Time: 96 HoursEffect Type: LC50Concentration: >= 0.619 - <= 0.796 mg/lChoose Apply, then Create to add another entry in the same table. Make the following entries:Species: Oncorhynchus mykiss (rainbow trout)Exposure Time: 96 HoursEffect Type: LC50Concentration: 35 mg/lChoose Apply.In the Chronic Toxicity to Fish table, choose Set Reason for No Data and select No data available.In the Acute Toxicity to Aquatic Invertebrates table, chose Create and make the following entries:Species: Daphnia magna (Water flea)Exposure Time: 48 HoursEffect Type: LC50Concentration: 5.102 g/lChoose Apply.In the Chronic Toxicity to Aquatic Invertebrates table, choose Set Reason for No Data and select No data available.In the Toxicity to Aquatic Plants table, chose Create and make the following entries:Species: algaeExposure Time: 72 HoursEffect Type: IC50Concentration: >2 g/lChoose Apply.In the Toxicity to Microorganisms table, choose Set Reason for No Data and select No data available.For each table in the Terrestrial Toxicology section, choose Set Reason for No Data and select No data available.For each table in the Environmental Fate and Pathway section, choose Set Reason for No Data and select No data available.For the Oxygen Demand, Transport Between Environmental Compartments, and Stability in Soil subsections, select the No Data Available checkbox.Choose Save, then Release. | The ecological information for the product is released. |  |

### Provide Transport Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The dangerous goods specialist for product compliance classifies the unpackaged product according to the assigned dangerous goods regulations and set the transport to allowed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dangerous Goods Specialist - Product Compliance. |  |  |
| 2 | Access App | Open My Unpackaged Dangerous Goods (F3643). | The My Unpackaged Dangerous Goods screen is displayed. |  |
| 3 | Open Unpackaged Product | On the My Unpackaged Dangerous Goods screen, search for the unpackaged product that you have created in the [Create Unpackaged Product](#unique_15) [page ] 16 procedure. Press Enter.In the search result, select your unpackaged product and go to the next screen. | The Classify Unpackaged Dangerous Goods screen is displayed. |  |
| 4 | Classify Unpackaged Product | In the Basic Classification section, choose the entry for the ADN regulation to navigate to the next screen.On the Dangerous Good - Classification Details screen, choose Edit.In the Classification section, enter the following data:Classified As: Dangerous GoodsUN Number: Select the UN number with the following details using the value help:UN Number: UN 1993Packing Group: IIAdditional Text: (vapour pressure at 50 °C not more than 110 kPa)Technical Name 1: Use the value help to search among all substance and select n-Propyl alcohol. | The Dangerous Good - Classification Details screen displays additional classification data for the selected UN number. |  |
| 5 | Check Dangerous Goods Basic Description | In the Dangerous Good Basic Description section, check the basic description. | After selecting the UN number, the system has generated the dangerous goods basic description in the languages required by the ADN regulation. |  |
| 6 | Check Transport Permission | In the Transport Permission section, check that the transport permission is set to Allowed by the system. |  |  |
| 7 | Save the Classification | After checking the classification data, choose Save. | The classification data is saved. |  |
| 8 | Navigate Back | Navigate back to the Classify Unpackaged Dangerous Good screen. |  |  |
| 9 | Classify Product According to Other Regulations | Select the checkbox for the ADN regulation and choose Apply Classification to Other Regulations.In the Apply Classification to Other Regulations dialog box, select all regulations and choose Apply Classification. | The system applies the classification you have done for the ADN regulation to all selected regulations and saves the classifications in a draft version. |  |
| 10 | Release Classifications | Select all in-progress regulations and choose Release.In the Release confirmation dialog box, choose Save Drafts and Release. | The released classifications are displayed in the Released section of the Basic Classification table. |  |

### Carry Out Marketability Assessments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product stewardship specialist for product compliance carries out all the applicable marketability assessments of the unpackaged product, according to the respective compliance requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The Manage Basic Compliance Data – Unpackaged Products screen is displayed. |  |
| 3 | Open Unpackaged Product | On the Manage Basic Compliance Data – Unpackaged Products screen, search for the unpackaged product that you have created in the [Create Unpackaged Product](#unique_15) [page ] 16 procedure. Press Enter.In the search result, select your unpackaged product and go to the next screen. | The Unpackaged Product – Basic Compliance Data screen is displayed. |  |
| 4 | Carry Out Marketability Assessment | Choose View Compliance Assessments.In the Marketability Assessments section, choose the entry with latest version of the EU - Poison Centre Notification compliance requirement.On the Manage Poison Centre Notification screen, choose Edit and enter the following data:Registration Status: CompliantUnique Formula Identifier: R3NN-3KVT-2XSG-W43JCountry/Region: Choose Add and select Germany (DE)Note You can enter other EU countries/regions, if needed.Choose Save, then Release. | The marketability assessment is released. |  |

### Carry Out Compliance Assessments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product stewardship specialist for product compliance carries out all the applicable compliance assessments of the unpackaged product, according to the respective compliance requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The Manage Basic Compliance Data – Unpackaged Products screen is displayed. |  |
| 3 | Open Unpackaged Product | On the Manage Basic Compliance Data – Unpackaged Products screen, search for the unpackaged product that you have created in the [Create Unpackaged Product](#unique_15) [page ] 16 procedure. Press Enter.In the search result, select your unpackaged product and go to the next screen. | The Unpackaged Product – Basic Compliance Data screen is displayed. |  |
| 4 | Add First Aid Measures | Choose Work View.On the Display Work View screen, go to Section 4 - First Аid Мeasures and choose the World First Aid Measures entry.On the Manage First Aid Measures screen, choose Edit.Make the following entries by choosing Add in the respective table:General Information: When symptoms persist or in all cases of doubt seek medical advice.Following Inhalation: If inhaled, remove to fresh air.Following Skin Contact: Wash off immediately with soap and plenty of water.Following Eye Contact: Rinse immediately with plenty of water, also under the eyelids.Following Ingestion: Clean mouth with water and drink afterwards plenty of water and If accidentally swallowed obtain immediate medical attention.Protection of First Aid Responders: No special precautions are necessary for first aid responders.Symptoms:central nervous system effectshearing lossNarcotic effectsShortness of breathSpasmVomitingTreatment: Treat symptomatically.Leave the default value Public in the field Use of Data for each entry.Choose Save, then Release.Navigate back to the Display Work View screen. | First aid measures are added. |  |
| 5 | Add Firefighting Measures | On the Display Work View screen, go to Section 5 - Firefighting measures and choose the World Firefighting Measures entry.On the Manage Firefighting Measures screen, choose Edit.Make the following entries by choosing Add in the respective table:Suitable Extinguishing Media: Alcohol-resistant foam, Carbon dioxide (CO2), and Dry powderSpecific Hazards: Do not use a solid water stream as it may scatter and spread fire.Special Protective Equipment: Use personal protective equipment.Choose Save, then Release.Navigate back to the Display Work View screen. | Firefighting measures are added. |  |
| 6 | Add Accidental Release Measures | On the Display Work View screen, go to Section 6 - Accidental release measures and choose the World Accidental Release Measures entry.On the Manage Accidental Release Measures screen, choose Edit.Make the following entries by choosing Add in the respective table:Personal Precautions, Protective Equipment, and Emergency Procedures: Use personal protective equipment.Environmental Precautions: Should not be released into the environment.Methods and Materials for Containment and Cleaning Up: Keep in suitable, closed containers for disposal.Reference to Other Sections: For personal protection see section 8.Leave the default value Public in the field Use of Data for each entry.Choose Save, then Release.Navigate back to the Display Work View screen. | Accidental release measures are added. |  |
| 7 | Add Information About Handling and Storage | On the Display Work View screen, go to Section 7 - Handling and storage and choose the latest version of the DE TRGS 510 Storage Class compliance requirement.On the Manage Storage Class screen, choose Edit.From the Storage Class dropdown list, select (3) Flammable liquids.Choose Save, then Release.Navigate back to the Display Work View screen.Go to Section 7 - Handling and storage and choose the World Handling and Storage entry.On the Manage Handling and Storage screen, choose Edit.Make the following entries by choosing Add in the respective table:Protection Against Fire and Explosion: Vapors may form explosive mixtures with air., Keep away from heat and sources of ignition., and Keep away from sources of ignition - No smoking.Hygiene Measures: Avoid contact with skin, eyes and clothing., Keep away from food, drink and animal feedingstuffs., and Wash hands before eating, drinking, or smoking.Storage Conditions: Keep containers tightly closed in a cool, well-ventilated place. and Store at room temperature in the original container.Select Public from the Use of Data dropdown list for each entry.Choose Save, then Release.Navigate back to the Display Work View screen. | Handling and storage information is added. |  |
| 8 | Add Personal Protection Measures | On the Display Work View screen, go to Section 8 - Exposure controls/personal protection and choose the World Personal Protection Measures entry.On the Manage Personal Protection Measures screen, choose Edit.Make the following entries by choosing Add in the respective table:Eye Protection: Ensure that eyewash stations and safety showers are close to the workstation location. and Safety gogglesHand Protection: Rubber glovesAdditional Hand Protection: Do not wear cotton gloves. and Do not wear leather gloves.Skin and Body Protection: Long sleeved clothing, Safety shoes, and Working clothes must not consist of textiles, which show a dangerous melting behavior in case of fire.Respiratory Protection: In case of mist, spray or aerosol exposure wear suitable personal respiratory protection and protective suit.Respiratory Protection Filter Type: Organic vapor TypeGeneral Protective Measures: Avoid contact with skin.Leave the default value Public in the field Use of Data for each entry.hoose Save, then Release.Navigate back to the Display Work View screen. | The personal protection measures are added. |  |
| 9 | Add Water Hazard Class | On the Display Work View screen, go to Section 15 - Regulatory information and choose the latest version of the DE Water Hazard class (WGK) compliance requirement.On the Unpackaged Product - Water Hazard Class screen, choose Edit.In the Assessments table, choose Create and enter the following data:Class: (WGK 1) slightly hazardous to waterReference: Classification according to AwSV §10(2)Choose Save, then Release. | Water hazard class is added. |  |

### Classify Substances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The master data specialist for product compliance carries out the hazardous classification of the substances that are added to the analytical composition, so the information is visible in the safety data sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Substances Compliance (F2578). | The Manage Substances Compliance screen is displayed. |  |
| 3 | Open Substance | On the Manage Substances Compliance screen, search for the d-Limonene substance. Press Enter.In the search result, choose the substance to go to the next screen. | The Manage Substances Compliance screen is displayed. |  |
| 4 | Enter GHS Classification | On the Manage Substances Compliance screen, choose View Compliance Assessments.In the Safety Data Sheet Assessments section, find and choose the latest version of the EU-GHS Classification compliance requirement.On the Substance - GHS Classification screen, choose Edit.In the Classification table, choose Create and make the following entries:Hazard Class: (Aquatic Acute) Short-term (acute) aquatic hazardHazard Category: (1) Category 1Choose Apply, then Save and Release. | The substance’s classification is created. |  |
| 5 | Classify Other Substances | Repeat steps 3 and 4 with the following data:Substance: n-Propyl alcohol:Hazard Class: (Flam. Liq.) Flammable liquidsHazard Category: (1) Category 1Substance: SODIUM LAURYL SULFATE:Hazard Class: (Eye Irrit.) Eye irritationHazard Category: (2) Category 2 |  |  |

### Identify Hazardous Ingredients

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product stewardship specialist for product compliance identifies hazardous ingredients of the unpackaged product according to the respective compliance requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Unpackaged Products (F2641) app. | The Manage Basic Compliance Data – Unpackaged Products screen is displayed. |  |
| 3 | Open Unpackaged Product | On the Manage Basic Compliance Data – Unpackaged Products screen, search for the unpackaged product that you have created in the [Create Unpackaged Product](#unique_15) [page ] 16 procedure. Press Enter.In the search result, select your unpackaged product and go to the next screen. | The Unpackaged Product – Basic Compliance Data screen is displayed. |  |
| 4 | Identify Hazardous Ingredients | On the Unpackaged Product – Basic Compliance Data screen, choose Work View.On the Display Work View screen, go to Section 3 - Composition/information on ingredients and choose the latest version of the EU Hazardous Ingredients compliance requirement.On the Unpackaged Product - Assess Hazardous Ingredients screen, choose Edit.In the Hazardous Ingredients Based On Analytical Composition table, choose Add. In the newly opened dialog box, select all substances and choose OK.Choose Save, then Release.Navigate back to the Display Work View screen. | The hazardous ingredients of the unpackaged product are specified. |  |
| 5 | Enter GHS Classification | Go to Section 2 - Hazards Identification and choose the latest version of the EU-GHS Classification compliance requirement.On the Unpackaged Product - GHS Classification screen, choose Edit.In the Classification section, choose Create to create entries with the following data:Hazard Class: (Acute Tox.) Acute toxicityHazard Category: (3) Category 3Route of Exposure: InhalationHazard Statements: (H336) May cause drowsiness or dizziness.Choose Apply.Hazard Class: (Acute Tox.) Acute toxicityHazard Category: (4) Category 4Route of Exposure: OralHazard Statements: (H371) May cause damage to organs if swallowed.Choose Apply.Hazard Class: (Aquatic Chronic) Long-term (chronic) aquatic hazardHazard Category: (3) Category 3Hazard Statements: (H412) Harmful to aquatic life with long lasting effectsClassification Procedure: Calculation methodChoose Apply.Hazard Class: (Asp. Tox.) Aspiration hazardHazard Category: (1) Category 1Hazard Statements: (H304) May be fatal if swallowed and enters airways.Choose Apply.Hazard Class: (Eye Dam.) Serious eye damageHazard Category: (1) Category 1Hazard Statements: (H319) Causes serious eye irritation.Choose Apply.Hazard Class: (Flam. Liq.) Flammable liquidsHazard Category: (3) Category 3Hazard Statements: (H224) Extremely flammable liquid and vapor.Choose Apply.Hazard Class: (Skin Sens.) Skin sensitizationHazard Category: (1) Category 1Route of Exposure: DermalHazard Statements: (H317) May cause an allergic skin reaction.Choose Apply.In the Acute Toxicity Estimation (ATE) section, in the Acute Toxicity Estimate (oral) subsection, in the Value field, enter 1,500 mg/kgChoose Save, then Release.Navigate back to the Display Work View screen.Note In case your product contains hazardous ingredients and there is a corresponding GHS assessment for the company substance, this assessment is printed on the safety data sheets, as well. | GHS classification is released. |  |
| 6 | Enter GHS Labeling Data | Go to Section 2 - Hazards Identification and choose the latest version of the EU-GHS Labeling compliance requirement.On the Unpackaged Product - GHS Labeling screen, choose Edit.In the Symbols table, choose Add and select the following symbols:(GHS05) Corrosion(GHS02) Flame(GHS08) Health Hazard(GHS07) Exclamation MarkFrom the Signal Word dropdown list, select Danger.In the Hazard Statements table, choose Add and select the following phrases:(H224) Extremely flammable liquid and vapor.(H304) May be fatal if swallowed and enters airways.(H412) Harmful to aquatic life with long lasting effects.In the Precautionary Statements section, in the Prevention table, choose Add to add the following entries:(P210) Keep away from heat, hot surfaces, sparks, open flames and other ignition sources. No smoking.(P264) Wash skin thoroughly after handling.In the Response table, choose Add to add the following entries:(P305) IF IN EYES:(P351) Rinse cautiously with water for several minutes.(P338) Remove contact lenses, if present and easy to do. Continue rinsing.(P370 + P378) In case of fire: Use foam to extinguish.In the Storage table, choose Add to add the following entries:(P405) Store locked up.In the Disposal table, choose Add to add the following entries:(P501) Dispose of contents/ container to an approved waste disposal plant.Choose Save, then Release. | GHS labeling data is released. |  |

### Generate and View Safety Data Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The product stewardship specialist for product compliance generates a safety data sheet for the unpackaged product with all provided information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The Manage Basic Compliance Data – Unpackaged Products screen is displayed. |  |
| 3 | Open Unpackaged Product | On the Manage Basic Compliance Data – Unpackaged Products screen, search for the unpackaged product that you have created in the [Create Unpackaged Product](#unique_15) [page ] 16 procedure. Press Enter.In the search result, select your unpackaged product and go to the next screen. | The Unpackaged Product – Basic Compliance Data screen is displayed. |  |
| 4 | Go to Safety Data Sheet Assessment | On the Unpackaged Product – Basic Compliance Data, choose Work View.On the Display Work View screen, go to the Safety Data Sheet Assessments section. Find and choose the latest version of the DE-SDS compliance requirement. | The Safety Data Sheet Management screen is displayed. |  |
| 5 | Generate Safety Data Sheet | On the Safety Data Sheet Assessment screen, choose Edit.Choose the row with language German. In the newly opened panel on the right, enter major version number and subversion. Choose Apply.Repeat this step for any additional languages you have added.Choose Generate. | The Safety Data Sheet Status is changed to Available and the table rows are highlighted in green. |  |
| 6 | View Safety Data Sheet | Choose any of the table rows. Check that there is a PDF file available on the right. Choose the file name to view the document.Check that the document contains data for sections 1 to 16.Choose Apply, then Save. | The safety data sheet is generated successfully. |  |
| 7 | Release Safety Data Sheet Version | Choose Release. | The safety data sheet assessment is released. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/test-script-label-management-6mt-ae-sap-s-4hana-cloud-public-edition-1]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-manage-safety-data-sheets-for-products-3vr-ae-sap-s-4hana]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-request-regulatory-documentation-from-service-provider-6av]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 67,958 chars in the whole document
