---
id: 13-quality-ehs-and-compliance/test-script-chemical-compliance-approval-for-purchased-material-and-su
title: "Test Script: Chemical Compliance Approval for Purchased Material and Supplier (31G_AE) (31G_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 31G_AE: assess raw material marketability, approve suppliers, process supplier disclosures."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/chemical-compliance-and-marketability]
aliases: [31G_S4CLD2608_BPD_EN_AE]
keywords: [Chemical Compliance and Product Marketability, chemical compliance, supplier approval, marketability assessment, raw material composition, compliance purpose, compliance disclosure, supplier assignment, raw material master data, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31G_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-891
topic: 13-quality-ehs-and-compliance/chemical-compliance-and-marketability
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Chemical Compliance Approval for Purchased Material and Supplier (31G_AE) (31G_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31G_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Chemical Compliance and Product Marketability** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Chemical Compliance Approval for Purchased Material and Supplier (31G_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232851185)

[2 Prerequisites 3](#_Toc232851186)

[2.1 System Access 3](#_Toc232851187)

[2.2 Roles 3](#_Toc232851188)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232851189)

[2.4 Preliminary Steps 5](#_Toc232851190)

[2.4.1 Create Compliance Purpose 5](#_Toc232851191)

[2.4.2 Create Raw Material and Assign Compliance Purpose 7](#_Toc232851192)

[3 Overview Table 9](#_Toc232851193)

[4 Test Procedures 10](#_Toc232851194)

[4.1 Enter Data and Assess Compliance 10](#_Toc232851195)

[4.1.1 Assign Supplier to Raw Material 10](#_Toc232851196)

[4.1.2 Enter Composition of Supplier Raw Material 11](#_Toc232851197)

[4.1.3 Assess Marketability and Approve Supplier for Raw Material 12](#_Toc232851198)

[4.1.4 Confirm Raw Material Composition and Check Marketability Assessments 15](#_Toc232851199)

[4.2 Optional: Process Compliance Disclosure for Supplier 17](#_Toc232851200)

[4.2.1 Optional: Process Compliance Disclosure for Supplier 17](#_Toc232851201)

## Purpose

Overview

This scope item manages the compliance assessment of purchased materials and their suppliers for fulfillment.

Raw or purchased materials must cover the compliance requirements of the associated products that are produced by using the raw materials.

The compliance data is requested from raw material suppliers. This process lets you first approve or block a supplier, and second, assess whether the raw material fulfills the requirements. When this assessment is done, you have approved suppliers and raw materials. Additionally, detailed compliance data is available for audits.

This scope item manages the compliance assessment for fulfillment of purchased materials and their suppliers.

Raw or purchased materials must cover compliance requirements of the associated products that are produced by using the raw materials.

The compliance data is requested from raw material suppliers. First, this lets you approve or block a supplier and second, assess the fulfillment of a raw material against the requirements. When this is done, you have approved suppliers and raw materials. Additionally, detailed compliance data is available for audits.

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
| Master Data Specialist - Product Compliance | SAP_BR_MD_SPECIALIST_PCL | Master Data - Product Compliance | SAP_BR_MD_SPECIALIST_PCL |  |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents products, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note The listed compliance requirement and compliance purpose definitions represent dynamic content based on the legal situation at a given point in time. This data is to be considered exemplary and not a reflection of the currently shipped content. For a complete overview of the currently shipped content, please refer to the application itself.The demo data described and used in the following is tailored for a smooth execution of the described procedures and suppresses processes of other solution areas in product compliance. |

| Data | Sample Value | Details |
| --- | --- | --- |
| Compliance Requirement | EU-REACH SVHC Status |  |
| Compliance Requirement | World-GADSL Status |  |
| Compliance Requirement | World-UN Stockholm Convention |  |
| Compliance Requirement | US-Dodd-Frank Act |  |
| Compliance Purpose | Raw Material Default Compliance Purpose | Compliance requirements are relevant for all raw materials. The compliance purpose is set to Active. |
| Listed Substance | L00000122417 | Listed substance name: Poly[imino(1,6-dioxo-1,6-hexanediyl)imino-1,6-hexanediyl]CAS number: 32131-17-2 |
| Vendor | 33300001 | Domestic Supplier UAE 1 |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNE | Create Supplier Master - MDS |

### Preliminary Steps

To run through this scope item, you must first carry out the preliminary steps:

1. [Create Compliance Purpose](#unique_7) [page ] 5
2. [Create Raw Material and Assign Compliance Purpose](#unique_8) [page ] 7

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

#### Create Compliance Purpose

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, create the compliance purpose that you assign to the raw material. You create the compliance purpose in the following steps as a Product Stewardship Specialist - Product Compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Product Stewardship Specialist - Product Compliance (SAP_BR_PRODSTWRD_SPLST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Compliance Purposes (F2632). | The app opens. |  |
| 3 | Create Compliance Purpose | Choose Create. | The Compliance Purpose screen is displayed. |  |
| 4 | Create Compliance Purpose Name | In the Compliance Purpose Names section, choose Create. | A row with empty Language and Name fields appears. |  |
| 5 | Open Value Help | Open the value help for the Language field. | The Select: Language dialog opens. |  |
| 6 | Choose Language | Search for the desired language by language key or name, for example, language key EN for English. Then choose the row of the language. | The dialog closes, and the language key appears in the Language field. |  |
| 7 | Enter Compliance Purpose Name | Enter <your name> 31G in the Name field. | The name <your name> 31G appears in the Name field. |  |
| 8 | Create Compliance Purpose with Name | Choose Create at the bottom of the screen. | The compliance purpose is created, and the compliance purpose name <your name> 31G is displayed at the top under the Compliance Purpose screen title. |  |
| 9 | Edit Compliance Purpose | Choose Edit. | The app is in edit mode. |  |
| 10 | Add Compliance Requirements | In the Compliance Requirements section, choose Add. | The Assign Compliance Requirements dialog opens. |  |
| 11 | Select Compliance Requirements | Search for and select the following compliance requirements, and then choose Select:EU-REACH SVHC StatusWorld-GADSL StatusWorld-UN Stockholm Convention | The added compliance requirements are displayed in the Compliance Requirements section. |  |
| 12 | Save Compliance Purpose | Choose Save. | The compliance purpose is saved and switches to display mode. |  |
| 13 | Activate Compliance Purpose | Choose Activate. | A success message indicates that the compliance purpose was activated. |  |

#### Create Raw Material and Assign Compliance Purpose

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you need the compliance view of the relevant raw material. In the following steps, as a Master Data Specialist - Product Compliance, you create the unpackaged product, and assign the relevant compliance purpose.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance (SAP_BR_MD_SPECIALIST_PCL). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Basic Compliance Data - Raw Materials (F3024). | The app opens. |  |
| 3 | Create Raw Material | Choose Create. | The New Raw Material dialog is displayed. |  |
| 4 | Enter Header Data for New Raw Material | In the New Raw Material dialog, enter the following value:Internal Name: <your name> 31GThe rest stays default. | The New Raw Material dialog is displayed with the internal name that you’ve defined. |  |
| 5 | Save the Raw Material | Choose Save. | The raw material is created, and the Raw Material - Basic Compliance Data screen opens in edit mode. |  |
| 6 | Select Assigned Compliance Purpose | In the Compliance Purposes section, Assigned Compliance Purposes table, select Raw Material Default Compliance Purpose. | The row is highlighted in blue. |  |
| 7 | Remove Default Compliance Purpose | Choose Remove, and then choose Remove again in the dialog that appears. | The default compliance purpose is removed, and a text indicates that there are no items available in the Assigned Compliance Purposes table. |  |
| 8 | Add Compliance Purpose | For the Assigned Compliance Purposes table, choose Add. | The Assign Compliance Purposes dialog is displayed. |  |
| 9 | Choose Your Compliance Purpose for Product Marketability | Search for the compliance purpose <your name> 31G. Select it, and then choose OK. | The compliance purpose is added to the Assigned Compliance Purposes table. |  |
| 10 | Save Raw Material | Choose Save. | A success message confirms that your changes have been saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Assign Supplier to Raw Material](#unique_10) [page ] 10 | Master Data Specialist - Product Compliance | Manage Basic Compliance Data - Raw Materials (F3024)Raw Material (F3025) | The supplier is assigned to the compliance view of the raw material. |
| [Enter Composition of Supplier Raw Material](#unique_11) [page ] 11 | Master Data Specialist - Product Compliance | Manage Suppliers Compliance - For Raw Materials (F3034)Supplier Compliance for Raw Material (F3040) | The raw material composition data provided by the supplier is entered at the supplier-specific level for the raw material. |
| [Assess Marketability and Approve Supplier for Raw Material](#unique_12) [page ] 12 | Master Data Specialist - Product Compliance | Marketability Assessment (F3346) | The supplier is assessed as compliant with all compliance requirement versions that are assigned to the raw material. The supplier is approved for the raw material. |
| [Confirm Raw Material Composition and Check Marketability Assessments](#unique_13) [page ] 15 | Master Data Specialist - Product Compliance | Manage Basic Compliance Data - Raw Materials (F3024)Raw Material (F3025)Manage Compliance Assessments (F3204) | Supplier-provided compliance data is harmonized on the raw material level and confirmed. The marketability status of the raw material as assessed against the assigned compliance requirement versions is calculated and released automatically, and verified. |
| [Optional: Process Compliance Disclosure for Supplier](#unique_14) [page ] 17 | Master Data Specialist - Product Compliance | Process Compliance Disclosures - For Suppliers (F7370) | A compliance disclosure is created for a supplier, and the supplier is assessed as compliant with the assigned compliance requirement version. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Enter Data and Assess Compliance

#### Assign Supplier to Raw Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance assigns a supplier to the compliance view of the raw material so that the supplier compliance can be assessed. The supplier is asked to provide the required compliance data to verify the fulfillment of requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the roleMaster Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Raw Materials (F3024) and search for the raw material name <your name> 31G. | The raw materials that match the fuzzy search are displayed in the list of search results. |  |
| 3 | Open a Raw Material | On the Manage Basic Compliance Data - Raw Materials screen, choose the row with the raw material name <your name> 31G. | The Raw Material - Basic Compliance Data screen is displayed. |  |
| 4 | Navigate to Suppliers | Choose the Suppliers tab. | The app scrolls down to the Suppliers tab. |  |
| 5 | Add a Supplier | For the Suppliers of Raw Material table in the Suppliers section, choose Create. | The Assign Supplier dialog is displayed. |  |
| 6 | Assign a Supplier | In the Assign Supplier dialog, enter the following data, and then choose Save:Supplier: 33300001Responsible Unit: Permitted for all Responsible Units (S_ALL) (stays default) | Domestic Supplier UAE 1 is displayed in the Suppliers of Raw Material table. The additional columns are filled as follows:External Product Number: <empty>Supplier Status for Raw Material: In ProgressComposition: Missing |  |
| 7 | Verify the Supplier Compliance for a Raw Material | In the Suppliers of Raw Material table, choose the row of the supplier that you assigned. | The Supplier Compliance for Raw Material screen of supplier Domestic Supplier UAE 1 for raw material <your name> 31G is displayed. |  |
| 8 | Request Compliance Data from a Supplier | On the Supplier Compliance for Raw Material screen, choose Set Compliance Data Status > Requested . | The Compliance Data status has changed to Requested. |  |

#### Enter Composition of Supplier Raw Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance receives the compliance data for a raw material from the supplier and enters the provided data. The compliance data of the supplier is harmonized on raw material level.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Suppliers Compliance - For Raw Materials (F3034) and filter for the following data:Search: <your name>31GCompliance Data: Requested | The suppliers that match the fuzzy search are displayed in the list of search results. |  |
| 3 | Process and Accept a Request | Choose the row of the search result with 33300001 in the Supplier column. | The Supplier Compliance for Raw Material screen is displayed. |  |
| 4 | Switch to Edit Mode | On the Supplier Compliance for Raw Material screen, choose Edit. | The app switches to edit mode. |  |
| 5 | Assign a Substance | In the Analytical Composition section, for the Components table, choose Create. | The Assign Substances dialog is displayed. |  |
| 6 | Search a Substance | Enter 32131-17-2 in the Search field. Then select the substance with 32131-17-2 in the CAS Number field, and choose OK.Note If more than one substance exists with the CAS number 32131-17-2, select the one with the lower internal number. | The substance with CAS number 32131-17-2 is added to the composition table. |  |
| 7 | Enter a Concentration | In the Components table, in the row for the substance that you just added, enter 100 in the Concentration Value column, and then choose Save. | A success message indicates that your changes have been saved, and the app switches to display mode.In the Supplier Status for Raw Material field, the status is In Progress. |  |
| 8 | Set Compliance Data to Done | In the header, choose Set Compliance Data Status > Set to Done . | The Compliance Data status changes to Done. |  |

#### Assess Marketability and Approve Supplier for Raw Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance has received and entered the compliance data for a raw material from the supplier and is ready to assess the supplier against the assigned compliance requirement versions for the raw material. When the supplier is assessed as compliant with all compliance requirement versions, the Master Data Specialist - Product Compliance approves the supplier for the raw material.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Suppliers Compliance - For Raw Materials (F3034) and filter for the following data:Search: <your name>31GCompliance Data: Done | The suppliers that match the fuzzy search are displayed in the list of search results. |  |
| 3 | Process and Accept a Request | Choose the row of the search result with 33300001 in the Supplier column. | The Supplier Compliance for Raw Material screen is displayed. |  |
| 4 | Open a Marketability Assessment | In the Compliance Assessments section, Compliance Assessments of Supplier Raw Material table, choose the row for the compliance requirement version EU REACH SVHC Status (<latest version>). | The Marketability Assessment screen opens. |  |
| 5 | Switch to Edit Mode | On the Marketability Assessment screen, choose Edit. | The app switches to edit mode. |  |
| 6 | Upload a Document | In the Attachments section, choose Upload, and then choose a document to attach. | The file name of the document appears in the Attachments section, and a success message indicates that the document was uploaded. |  |
| 7 | Set Marketability Status | In the Compliance Details section, Marketability Status field, set the marketability status to Compliant. | Compliant is displayed in the Marketability Status field. |  |
| 8 | Save Your Changes | Choose Save. | The app switches to display mode, and a success message indicates that the marketability assessment was saved.In the header, Compliant is displayed in the Marketability Status field. |  |
| 9 | Navigate Back | Navigate back. | The Supplier Compliance for Raw Material screen is displayed. The supplier compliance status for EU REACH SVHC Status (<latest version>) is Compliant. |  |
| 10 | Open a Marketability Assessment | In the Compliance Assessments section, Compliance Assessments of Supplier Raw Material table, choose the row for the compliance requirement version World GADSL Status (<latest version>). | The Marketability Assessment screen opens. |  |
| 11 | Switch to Edit Mode | On the Marketability Assessment screen, choose Edit. | The app switches to edit mode. |  |
| 12 | Upload a Document | In the Compliance Details section, in the Remarks field, enter a remark. | Your remark appears in the Remarks field. |  |
| 13 | Set Marketability Status | In the Compliance Details section, Marketability Status field, set the marketability status to Compliant. | Compliant is displayed in the Marketability Status field. |  |
| 14 | Save Your Changes | Choose Save. | The app switches to display mode, and a success message indicates that the marketability assessment was saved.In the header, Compliant is displayed in the Marketability Status field. |  |
| 15 | Navigate Back | Navigate back. | The Supplier Compliance for Raw Material screen is displayed. The supplier compliance status for EU REACH SVHC Status (<latest version>) and World GADSL Status (<latest version>) is Compliant. |  |
| 16 | Open a Marketability Assessment | In the Compliance Assessments section, Compliance Assessments of Supplier Raw Material table, choose the row for the compliance requirement version World UN Stockholm Convention (<latest version>). | The Marketability Assessment screen opens. |  |
| 17 | Switch to Edit Mode | On the Marketability Assessment screen, choose Edit. | The app switches to edit mode. |  |
| 18 | Add Exemption | In the Exemptions section under Compliance Details, choose Add. | The Select Exemption dialog appears. |  |
| 19 | Select Exemption | In the Select Exemption dialog, select Product has a specific exemption or acceptable purpose. Then choose Select. | Product has a specific exemption or acceptable purpose is displayed in the Exemptions section. |  |
| 20 | Set Marketability Status | In the Compliance Details section, Marketability Status field, set the marketability status to Compliant. | Compliant is displayed in the Marketability Status field. |  |
| 21 | Save Your Changes | Choose Save. | The app switches to display mode, and a success message indicates that the marketability assessment was saved.In the header, Compliant is displayed in the Marketability Status field. |  |
| 22 | Navigate Back | Navigate back. | The Supplier Compliance for Raw Material screen is displayed. The supplier compliance status for EU REACH SVHC Status (<latest version>), World GADSL Status (<latest version>), and World UN Stockholm Convention (<latest version>) is Compliant. |  |
| 23 | Assess Other Compliance Requirement Versions | Check if there are any remaining compliance requirement versions with Unknown in the Supplier Compliance Status column.If not, proceed to the next step.If so, proceed as follows for each remaining compliance requirement version with Unknown in the Supplier Compliance Status column:Choose the row of the compliance requirement version.Choose Edit.In the Compliance Details section, Marketability Status field, select Compliant.Choose Save.Navigate back. | The Supplier Compliance for Raw Material screen is displayed. |  |
| 24 | Approve Supplier | In the header of the Supplier Compliance for Raw Material screen, choose Set Supplier Status > Approve . | Approved appears in the Supplier Status for Raw Material field, and a success message indicates that the supplier is approved. |  |

#### Confirm Raw Material Composition and Check Marketability Assessments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The compliance data of the supplier is harmonized on raw material level. The Master Data Specialist - Product Compliance assesses and releases the harmonized compliance data. The system calculates the marketability status of the raw material and releases the marketability assessment for each assigned compliance requirement version.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Raw Materials (F3024) app and search for the raw material name <your name> 31G. | The raw materials that match the fuzzy search are displayed in the list of search results. |  |
| 3 | Verify Raw Material Compliance Data | On the Manage Basic Compliance Data - Raw Materials screen, choose the row for raw material name <your name> 31G. | The Raw Material - Basic Compliance Data screen is displayed. |  |
| 4 | Navigate to Compositions | On the Raw Material - Basic Compliance Data screen, choose the Compositions tab. | The Raw Material - Basic Compliance Data screen is displayed, scrolled down to the analytical composition. |  |
| 5 | View Details of Composition | Choose the row of the analytical composition in status In Progress - Initial Version. | The Raw Material - Analytical Composition screen opens. The substance with CAS number 32131-17-2 with a concentration of 100% is displayed in the table. |  |
| 6 | Edit Analytical Composition | Choose Edit. | The app is in edit mode. |  |
| 7 | Release the Composition | On the Raw Material - Analytical Composition screen, choose Release. | A success message indicates that the analytical composition has been released. |  |
| 8 | Navigate Back | Navigate back. | The Raw Material - Basic Compliance Data screen is displayed. |  |
| 9 | View Compliance Assessments | On the Raw Material - Basic Compliance Data screen, choose View Compliance Assessments. | The Raw Material - Compliance Assessments screen opens. |  |
| 10 | Verify Released Marketability Assessments | On the Marketability Assessments tab of the Raw Material - Compliance Assessments screen, choose Released. | For all assigned compliance requirement versions, Compliant is displayed in the Marketability Status column, and SAP System is displayed in the Processor/Released By column. These values indicate that the system automatically calculated the marketability status as Compliant based on the information available and released the marketability assessments. |  |

### Optional: Process Compliance Disclosure for Supplier

#### Optional: Process Compliance Disclosure for Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance has received a compliance disclosure from the supplier in the form of a self-assessment, and assigns the relevant compliance requirement version to the supplier. Based on this data, the Master Data Specialist - Product Compliance assesses the compliance of the supplier with the relevant due diligence act.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Compliance Disclosures - For Suppliers (F7370) app. | The Process Compliance Disclosures - For Suppliers screen is displayed. |  |
| 3 | Create Compliance Disclosure | For the Compliance Disclosures table, choose Create. | The Create dialog opens. |  |
| 4 | Provide Header Data | In the Create dialog, provide the following data:Supplier: 33300001Type: Self-AssessmentDate of Receipt: <today's date>Then choose Create. | The Compliance Disclosure screen opens. |  |
| 5 | Open Value Help for Compliance Requirement Version | In the Compliance Declarations table, Compliance Requirement Version field, open the value help. | The Select: Compliance Requirement Version dialog opens. |  |
| 6 | Select Compliance Requirement Version | Choose the compliance requirement version with US-Dodd-Frank Act in the Compliance Requirement column. | The Select: Compliance Requirement Version dialog closes. On the Compliance Disclosure screen, in the Compliance Declarations table, the newly added compliance requirement version appears in the Compliance Requirement Version column. |  |
| 7 | Assess Supplier as Compliant | In the Compliance Declarations table, Supplier Compliance Status column, select Compliant from the dropdown list in the row for US Dodd-Frank Act. | In the Compliance Declarations table, Compliant appears in the Supplier Compliance Status column for US Dodd-Frank Act. |  |
| 8 | Add a Remark | In the Compliance Declarations table, Supplier Compliance Status column, in the row for US Dodd-Frank Act, enter a remark. | In the Compliance Declarations table, Remark column, your remark is displayed for US Dodd-Frank Act. |  |
| 9 | Upload an Attachment | In the Attachments section, choose Upload, and select a file from your computer. | The uploaded file appears in the Attachments section, and a success message confirms that the file has been uploaded. |  |
| 10 | Finalize Creation of Compliance Disclosure | Choose Create. | A success message confirms that the object was created. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/substance-volume-tracking-4ol-ae-test-script-sap-s-4hana-cloud-public]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-assess-marketability-of-a-product-31h-ae-sap-s-4hana-cloud]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31G_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 36,280 chars in the whole document
