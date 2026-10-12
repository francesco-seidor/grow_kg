---
id: 13-quality-ehs-and-compliance/test-script-manage-safety-data-sheets-for-products-3vr-ae-sap-s-4hana
title: "Test Script: Manage Safety Data Sheets for Products (3VR_AE) - SAP S/4HANA Cloud Public Edition (3VR_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition 2608 test script for scope item 3VR (AE): prerequisites and steps to upload, contact-set, ship and monitor safety data sheets."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/safety-data-sheets-and-labels]
aliases: [3VR_S4CLD2608_BPD_EN_AE]
keywords: ["Safety Data Sheet Authoring, Distribution and Labels", safety data sheets, safety data sheet upload, safety data sheet shipment, shipment monitoring, sds contact data, unpackaged products, compliance purposes, product compliance, regulation application]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VR_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-975
topic: 13-quality-ehs-and-compliance/safety-data-sheets-and-labels
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Manage Safety Data Sheets for Products (3VR_AE) - SAP S/4HANA Cloud Public Edition (3VR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Safety Data Sheet Authoring, Distribution and Labels** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Manage Safety Data Sheets for Products (3VR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232853753)

[2 Prerequisites 3](#_Toc232853754)

[2.1 System Access 3](#_Toc232853755)

[2.2 Roles 3](#_Toc232853756)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232853757)

[2.4 Business Conditions 4](#_Toc232853758)

[2.5 Preliminary Steps 5](#_Toc232853759)

[2.5.1 Create Business Partner – SDS Contact Mail 5](#_Toc232853760)

[2.5.2 Create Business Partner – Company Address 5](#_Toc232853761)

[2.5.3 Create Compliance Purpose 6](#_Toc232853762)

[2.5.4 Apply Regulation 7](#_Toc232853763)

[2.5.5 Create Product Master Record 8](#_Toc232853764)

[3 Overview Table 10](#_Toc232853765)

[4 Test Procedures 11](#_Toc232853766)

[4.1 Create Unpackaged Product 11](#_Toc232853767)

[4.2 Upload Safety Data Sheets for Products 12](#_Toc232853768)

[4.3 Enter Contact Data for Safety Data Sheet 14](#_Toc232853769)

[4.4 Manual Shipment of Safety Data Sheets 16](#_Toc232853770)

[4.5 Monitor Safety Data Sheet Shipments 17](#_Toc232853771)

[4.6 Optional: Output Parameter Determination 18](#_Toc232853772)

## Purpose

Overview

Placing chemical products on the market requires an efficient system support for handling mandatory documentation as defined by regulators. This scope item covers the main process steps for the maintenance of final safety data sheets as documents for products in the required languages for geographically defined jurisdictions.

With this scope item, safety data sheets can be managed and linked to products using the general product compliance purpose concept. Applicable safety data sheet documents can be assigned to products and released. The compliance status of affected products can be tracked. Safety data sheets can be transmitted by the system to customers.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Available via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers depending on, for example, the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to carry out the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Product | FGPC01 | Product Number: FGPC01Product Type: FERTProduct Description: Product Compliance Finished GoodCompliance Relevant: Yes |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNS | Create Product Master of Type “Semi-Finished Good” |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1LQ - Output Management | The scope item 1LQ must be implemented and tested before testing scope item 3VR. |

### Preliminary Steps

#### Create Business Partner – SDS Contact Mail

To run through this scope item, the Master Data Specialist - Business Partner Data has to create a business partner that you can use as the responsible contact for the safety data sheet.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad with the sections and tiles for the Master Data Specialist - Business Partner Data is displayed. |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163)app. | The app opens and the Manage Business Partner screen is displayed. |  |
| 3 | Create Business Partner | On the Manage Business Partner screen, choose Create and in the dropdown, choose Person.In the Create Person popup, enter data for the following fields and choose OK:First NameLast NameStreetHouse NumberPostal CodeCityCountry/Region | The New Business Partner screen is displayed containing your entered data. |  |
| 4 | Enter Email Address | In the Address section under Standard Communication , enter your email address and choose Create.Note down the ID of the business partner: __________________You will use this business partner as the SDS responsible contact in the following test procedure: [Enter Contact Data for Safety Data Sheet](#unique_8) [page ] 14 | The new business partner is created.The system may warn you about potential duplicate records. You can check if they are redundant or you can create the entry anyway.In the header, the entered name is displayed with the business partner ID underneath. |  |

#### Create Business Partner – Company Address

To run through this scope item, the Master Data Specialist - Business Partner Data has to create a business partner that you can use as your company’s SDS contact.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad with the sections and tiles for the Master Data Specialist - Business Partner Data is displayed. |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163)app. | The app opens and the Manage Business Partner screen is displayed. |  |
| 3 | Create | On the Manage Business Partner screen, choose Create and in the dropdown, choose Organization.In the Create Organization popup, enter data for the following fields:Name 1StreetHouse NumberPostal CodeCityCountry/RegionChoose OK. | The New Business Partner screen is displayed containing your entered data. |  |
| 4 | Save | Choose Create.Note down the ID of the business partner: __________________You will use this business partner as the company address in the following test procedure: [Enter Contact Data for Safety Data Sheet](#unique_8) [page ] 14 | The new business partner is created.The system may warn you about potential duplicate records. You can check if they are redundant or you can create the entry anyway.In the header, the entered name is displayed with the business partner ID underneath. |  |

#### Create Compliance Purpose

To run through this scope item, the Product Stewardship Specialist - Product Compliance has to create a compliance purpose that includes the SDS compliance requirement relevant for your country/region.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Manage Compliance Purposes (F2632) app. | The Manage Compliance Purposes screen is displayed. |  |
| 3 | Create Compliance Purpose | On the Manage Compliance Purposes screen, choose Create. | The Compliance Purposes screen is displayed. |  |
| 4 | Enter Compliance Purpose Name | In the Compliance Purpose Names section, choose Create and enter a name in the currently selected languages.Note down the name you've entered: ___________.You will use this compliance purpose in the following test procedure: [Create Unpackaged Product](#unique_11) [page ] 11 |  |  |
| 5 | Assign Compliance Requirement | In the Compliance Requirements section, choose Add. Search for the following compliance requirement and choose Select:XX-SDS for the appropriate shipping country. (Replace XX with a country code.) | The selected compliance requirement is added to the Compliance Requirements table. |  |
| 6 | Save your Entries | In the footer bar, choose Create. | The compliance purpose is created. |  |
| 7 | Activate Compliance Purpose | In the header section, choose Activate. | The Activation Status in the header is set from New to Active. |  |

#### Apply Regulation

To run through this scope item, the Product Stewardship Specialist - Product Compliance has to assure that a unique product master record exists.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Apply Regulations - Safety Data Sheets (F3984) app. | The Apply Regulations – Safety Data Sheets screen is displayed. |  |
| 3 | Select Country/Region | Choose the country/region that is relevant for your shipping scenario. | The country/region should be marked in green.The country/region detail screen is displayed.In the Classification section, you can see the XX-SDS for the appropriate shipping country compliance requirement, which you've added to your compliance purpose in the preliminary step [Create Compliance Purpose](#unique_10) [page ] 6.In Safety Data Sheet Languages section, you can see the relevant languages.In the Assigned Compliance Purposes section, you can see the purpose that you've created in the preliminary step [Create Compliance Purpose](#unique_10) [page ] 6. |  |

#### Create Product Master Record

To run through this scope item, the Master Data Specialist - Product Data has to create a unique product master data record.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data. | The SAP Fiori launchpad with the sections and tiles for the role Master Data Specialist - Product Data is displayed. |  |
| 2 | Access App | Open the Manage Product Master Data (F1602) app. | The Manage Product Master Data screen is displayed. |  |
| 3 | Search for Product | Enter the product FGPC01 into the Search field and choose Go. | Product Compliance Finished Good (FGPC01) is displayed in the Products list. |  |
| 4 | Copy Product | Select the entry for Product Compliance Finished Good (FGPC01) and choose Copy. | The Select Organizational Data to Copy dialog is displayed. |  |
| 5 | Select Organizational Data to Copy | Keep the selection for plants and distribution chains and choose OK. | The Create Master Record dialog is displayed. |  |
| 6 | Create Master Record | Change the text in the Description field, leave all other fields with default values, and choose OK. | The Product screen is displayed. |  |
| 7 | Changed Translations | In Descriptions section, change the text in the Product field for the language that is relevant for your scenario. |  |  |
| 8 | Save Your Entries | Choose Create to save your entries.If a potential duplicate warning appears, choose Create to confirm.Note down the following data:Product Description: _______________Product Number: __________________You will use this material in the following test procedures:[Create Unpackaged Product](#unique_11) [page ] 11[Enter Contact Data for Safety Data Sheet](#unique_8) [page ] 14[Manual Shipment of Safety Data Sheets](#unique_14) [page ] 16[Monitor Safety Data Sheet Shipments](#unique_15) [page ] 17 | The product master record is created.In the header, the entered product description is displayed with the product number underneath. |  |

## Overview Table

This scope item consists of several process steps provided in the table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Unpackaged Product](#unique_11) [page ] 11 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641) | An unpackaged product is created and related products are assigned. In addition a purpose is assigned to the unpackaged. |
| [Upload Safety Data Sheets for Products](#unique_17) [page ] 12 | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641)Managing Safety Data Sheets (F3972) | Safety data sheets in the required language are uploaded and saved for the product. |
| [Enter Contact Data for Safety Data Sheet](#unique_8) [page ] 14 | Product Stewardship Specialist - Product Compliance | Manage Contact Data - Safety Data Sheets (F4521) | Contact information that is printed in chapter 1 on the safety data sheet is entered. |
| [Manual Shipment of Safety Data Sheets](#unique_14) [page ] 16 | Product Stewardship Specialist - Product Compliance | Compliance Information - For Products (F3226) | Safety data sheets with cover sheet is sent manually to an email address. |
| [Monitor Safety Data Sheet Shipments](#unique_15) [page ] 17 | Product Stewardship Specialist - Product Compliance | Monitor Shipments - Safety Data Sheets (F4309) | The safety data sheets with cover sheet is shipped for the product. |
| [Optional: Output Parameter Determination](#unique_18) [page ] 18 | Administrator | Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) | Rules for the output parameter determination are specified. |

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

The Product Stewardship Specialist - Product Compliance creates an unpackaged product, assigns a related product from the product master, and assigns compliance purposes.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Unpackaged Products (F2641) app. | The Manage Basic Data – Unpackaged Products screen is displayed. |  |
| 3 | Create New Product | On the Manage Basic Data – Unpackaged Products screen, choose Create. | The New Product dialog is displayed. |  |
| 4 | Enter a Name for the Product | On the New Product dialog, enter a name in the Internal Name field.In the Product Categorization field, select Mixture.Leave all other fields with default values and choose Save.Note down the name you've entered: ______________ | The Unpackaged Product - Basic Compliance Data screen is displayed. |  |
| 5 | Edit Product Data | On the Unpackaged Product - Basic Compliance Data screen, choose Edit. | The fields on the screen are editable. |  |
| 6 | Assign Product | In the Assigned Products section for the Related Products in Product Master table, choose the value help for the first empty row in the Product in Product Master column. |  |  |
| 7 | Enter Product Number | Enter the <Product Number> that you've created in the preliminary step [Create Product Master Record](#unique_13) [page ] 8. |  |  |
| 8 | Remove Default Compliance Purpose | In the Application, Uses, Markets and Purposes section in the Assigned Compliance Purposes table, select the line Product Default Compliance Purpose.Choose Remove and confirm. | Default purpose is removed. |  |
| 9 | Add new Compliance Purpose | For the Assigned Compliance Purposes table, choose Add. | The Assign Compliance Purposes dialog is displayed. |  |
| 10 | Select Compliance Purpose | Search for the <Purpose> that you've created in the preliminary step [Create Compliance Purpose](#unique_10) [page ] 6.Select the purpose and choose OK. | The dialog is closed and the purpose is added to the Assigned Compliance Purposes table. |  |
| 11 | Save You Entries | Choose Save. | Data is saved and the Manage Basic Data – Unpackaged Products screen is shown in display mode.The compliance assessments are calculated asynchronously in the background. |  |

### Upload Safety Data Sheets for Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance uploads safety data sheets for a product in the required languages.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Unpackaged Products (F2641) app. | The Manage Basic Compliance Data - Unpackaged Products screen is displayed. |  |
| 3 | Search for Unpackaged Product | Expand the header of the list of unpackaged products by choosing the <!-- image omitted: unnamed -->(Expand Header) icon. In the Search field, enter the <Internal Name> of the product that you've created in the [Create Unpackaged Product](#unique_11) [page ] 11 procedure. | The list is filtered and your created unpackaged product is displayed. |  |
| 4 | Open Unpackaged Product | Choose the line for your unpackaged product to navigate to the Unpackaged Product - Basic Compliance Data screen. | The Unpackaged Product - Basic Compliance Data screen is displayed and shows the data of your unpackaged product. |  |
| 5 | Navigate to the Assessment Overview | On the Unpackaged Product - Basic Compliance Data screen, choose View Compliance Assessments. | The Unpackaged Product - Compliance Assessments screen is displayed and shows the status of the assigned assessments. |  |
| 6 | Display Safety Data Sheet Assessments | Choose the Safety Data Sheet Assessments tab. | All assigned safety data sheet assessments are displayed with their status. |  |
| 7 | Process Safety Data Sheet Assessment for Countries/Regions | In the Safety Data Sheet Assessments table, choose the line for a compliance requirement with a country/region-specific safety data sheet assessment to navigate to the Safety Data Sheet Assessment screen. | The Safety Data Sheet Assessment screen is displayed for the selected assessment. |  |
| 8 | Upload Safety Data Sheet for Each Language | Choose Edit to upload the safety data sheets for each language.In the Safety Data Sheet table, choose a line for a language to open the upload screen for the selected language.In the upload screen, enter in the following values:Major Version: 1Subversion: 1In the Attachment section, choose Upload to attach a safety data sheet for the selected language. Note that you can upload only documents with the following file formats: PDF (recommended), RTF, ZIP, or GZ. Uploaded files are shipped unchanged.Choose Apply. |  |  |
| 9 | Repeat for Other Languages | If further languages are required, repeat step 8 for each language. |  |  |
| 10 | Save the Documents | When safety data sheets for all languages are provided, choose Save. | In the Safety Data Sheet table, the status for the uploaded safety data sheet has changed to Available and the version information is added. |  |
| 11 | Release the Assessment | Choose Release. |  |  |

### Enter Contact Data for Safety Data Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance enters the inhouse contact persons for safety data sheets. This could be only one person for the complete company or multiple persons responsible for different sales organizations or countries/regions.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Manage Contact Data - Safety Data Sheets (F4521) app. | The Manage Contact Data – Safety Data Sheets screen is displayed. |  |
| 3 | Create New Contact Person | On the Manage Contact Data – Safety Data Sheets screen, choose Create. | The New Safety Data Sheet Contact sub screen is displayed. |  |
| 4 | Enter Header Data | Enter the following header data:Product: <Product Number> of the product that you've created in the preliminary step [Create Product Master Record](#unique_13) [page ] 8.Sales Organization: 3310Note The restriction on a specific product is only a very rare use case. Here, it is used for testing purposes so that multiple persons can test on the same system with different products without influencing each other. |  |  |
| 5 | Add Company Address | In the Addresses section, choose the value help for the first empty row in the Address Type column. |  |  |
| 6 | Select Company Address | In the Address Type field, choose Company Address.In the Business Partner field, enter the <Business Partner ID> of the business partner that you've created in the preliminary step [Create Business Partner – Company Address](#unique_9) [page ] 5. | The address of the selected business partner is displayed. |  |
| 7 | Add SDS Contact Mail | In the Addresses section, choose the value help for the second row in the Address Type column. |  |  |
| 8 | Add SDS Contact Mail | In the Address Type section, choose SDS Contact Mail.In the Business Partner field, enter the <Business Partner ID> of the business partner that you've created in the preliminary step [Create Business Partner – SDS Contact Mail](#unique_7) [page ] 5. | The address of the selected business partner is displayed. |  |
| 9 | Add Emergency Phone Number | In the Emergency Phone Numbers section, choose the value help for the first empty row in the Language column. Select a language and enter the phone number for this language. |  |  |
| 10 | Add Logo | In the Logo section, select a logo.Additional Information: If no logo is available, you can upload a logo in the Manage Logos app. Note that this is only possible on a system with extensibility activated and that you need administrator authorizations. | The selected logo is displayed. |  |
| 11 | Save Your Entries | Choose Create to create the contact data and save your entries. | The safety data sheet contact is created. |  |

### Manual Shipment of Safety Data Sheets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance sends the safety data sheet manually to an email address.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Compliance Information - For Products (F3226) app. | The Compliance Information - For Products screen is displayed. |  |
| 3 | Search for Product | In the Search field, enter the <Product Number> that you've created in the preliminary step [Create Product Master Record](#unique_13) [page ] 8 and choose Enter. | The product is shown in the Products list. |  |
| 4 | Select Product | Choose the line of your product. | A world map is displayed.In case a warning informs you about no compliance assessments you can confirm. |  |
| 5 | Select Safety Data Sheets View | Choose the Safety Data Sheets tab. | The world map shows information about the availability of safety data sheets for the countries/regions.The country/region for which you've uploaded the safety data sheet in the [Upload Safety Data Sheets for Products](#unique_17) [page ] 12 procedure is colored in green. |  |
| 6 | Select Country/Region | Choose the country/region for which you've uploaded the base safety data sheet in the [Upload Safety Data Sheets for Products](#unique_17) [page ] 12 procedure. | A popup opens and displays the uploaded safety data sheets. |  |
| 7 | Send Safety Data Sheet | Choose Send and on the Send Document dialog, enter the following data:Sales Organization: 3310Choose Send to EmailEmail Address: <Your Email Address>Choose Send.Note At this point, it's also possible to select a business partner (such as a customer) to send the safety data sheet to.The application also supports automatically sending safety data sheets during the sales process as part of post goods issue in the delivery. | The shipment of the safety data sheet is triggered.You'll receive an email with the attached safety data sheet and cover sheet. This might take some time because usually, the shipment of the safety data sheet is scheduled asynchronously. Follow the next chapter to monitor the safety data sheet shipment and to verify the SDS shipment status. |  |

### Monitor Safety Data Sheet Shipments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance can monitor the status of safety data sheet shipment.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Monitor Shipments - Safety Data Sheets (F4309) app. | The Monitor Shipments – Safety Data Sheets screen is displayed. |  |
| 3 | Search for Shipment | In the Search field, enter the <Product Number> that you've created in the preliminary step [Create Product Master Record](#unique_13) [page ] 8.Filter for shipments in status Completed: SDS Shipped. | The shipment is displayed in the Safety Data Sheet Shipments list. |  |
| 4 | Verify Shipment | Choose the shipment for your <Product Number>. | The Safety Data Sheet Shipment Screen is displayed.The Shipment Status is Completed: SDS Shipped. |  |
| 5 | View Safety Data Sheet | In the Safety Data Sheet section, choose your uploaded document. | The shipped safety data sheet is either displayed or downloaded (depending on the configuration of your browser). |  |
| 6 | View Cover Sheet | In the Output Details section, choose Show More per Row. Then, choose Display Document. | The shipped cover sheet is either displayed or downloaded (depending on the configuration of your browser). |  |

### Optional: Output Parameter Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Administrator can specify rules for the output parameter determination for the safety data sheet shipment.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app. | The Output Parameter Determination screen is displayed |  |
| 3 | Show Rules | Choose Safety Data Sheet for the Show Rules field and check the specified rules. | There are different Determination Steps available that provide the possibility to influence the output parameter determination in regards to safety data sheet shipment. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/product-compliance-document-authoring-7do-ae-test-script-sap-s-4hana-c]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-label-management-6mt-ae-sap-s-4hana-cloud-public-edition-1]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-request-regulatory-documentation-from-service-provider-6av]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 36,472 chars in the whole document
