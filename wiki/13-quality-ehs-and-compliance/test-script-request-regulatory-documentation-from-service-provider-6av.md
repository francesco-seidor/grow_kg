---
id: 13-quality-ehs-and-compliance/test-script-request-regulatory-documentation-from-service-provider-6av
title: "Test Script: Request Regulatory Documentation from Service Provider (6AV) - SAP S/4HANA Cloud Public Edition (6AV_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 6AV: simulating cooperation with a regulatory documentation service provider via substance and product service requests."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/safety-data-sheets-and-labels]
aliases: [6AV_S4CLD2608_BPD_EN_XX]
keywords: ["Safety Data Sheet Authoring, Distribution and Labels", regulatory documentation, service provider cooperation, reference service, private substance request, product request, service request status, substance data checks, product data entry, compliance requirement versions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AV_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1157
topic: 13-quality-ehs-and-compliance/safety-data-sheets-and-labels
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Request Regulatory Documentation from Service Provider (6AV) - SAP S/4HANA Cloud Public Edition (6AV_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AV_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Safety Data Sheet Authoring, Distribution and Labels** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Request Regulatory Documentation from Service Provider (6AV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232825982)

[2 Prerequisites 3](#_Toc232825983)

[2.1 System Access 3](#_Toc232825984)

[2.2 Roles 3](#_Toc232825985)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232825986)

[2.4 Additional Manual Configuration 9](#_Toc232825987)

[2.5 Preliminary Steps 9](#_Toc232825988)

[2.5.1 Check Compliance Requirement Versions 9](#_Toc232825989)

[3 Overview Table 12](#_Toc232825990)

[4 Test Procedures 14](#_Toc232825991)

[4.1 Check Data and Request Private Substance 14](#_Toc232825992)

[4.1.1 Check Substance Data 14](#_Toc232825993)

[4.1.2 Create Private Substance Request 15](#_Toc232825994)

[4.2 Check Data and Request Product 17](#_Toc232825995)

[4.2.1 Check and Enter Product Data 17](#_Toc232825996)

[4.2.2 Create Product Request 19](#_Toc232825997)

[4.2.3 Check Data Received from Service Provider (Reference Service) 20](#_Toc232825998)

## Purpose

Overview

This scope item enables you to use compliance data that is provided by an external service provider for regulatory documentation in the Product Compliance solution. The external service provider can, for example, take over the collection of regulatory data, such as GHS classifications and dangerous goods classifications for your compliance-relevant products. In addition, the service provider generates regulatory documentation, such as safety data sheets.

This scope item supports the following processes:

- Simulate the cooperation with a service provider for regulatory documentation
- Cooperate with a service provider for regulatory documentation

Because the cooperation with a service provider for regulatory documentation only works in a productive environment, the test script only tests the simulation of the cooperation. You create service requests for substances and products and send data to a reference service simulating the regulatory documentation of the service provider. You can monitor the status of the service requests and check received data that is transferred from the reference service to the Product Compliance solution.

To productively use the service of a regulatory documentation service provider, a license is required.

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
| Master Data Specialist - Product Compliance | SAP_BR_MD_SPECIALIST_PCL | Master Data - Product Compliance | SAP_BR_MD_SPECIALIST_PCL |  |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Dangerous Goods Specialist - Product Compliance (Product Compliance) | SAP_BR_DG_SPLST_PCL | Dangerous Goods | SAP_BR_DG_SPLST_PCL |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents, for example, products, customers, and suppliers, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Listed Substance | L00000008564 | Name: Cinnarizine | Included in the listed substance index, which is delivered with the software. |
| Listed Substance | L00000006111 | Name: Morpholine | Included in the listed substance index, which is delivered with the software. |
| Compliance Requirement Version | ADN | Compliance Requirement ID: ADN | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | ADR | Compliance Requirement ID: ADR | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | IATA-DGR | Compliance Requirement ID: IATA-DGR | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | IMDG-Code | Compliance Requirement ID: IMDG-Code | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | RID | Compliance Requirement ID: RID | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | UNRTDG | Compliance Requirement ID: UNRTDG | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | CA-SDS | Compliance Requirement ID: CA-SDS | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | DE-SDS | Compliance Requirement ID: DE-SDS | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | FR-SDS | Compliance Requirement ID: FR-SDS | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | MX-SDS | Compliance Requirement ID: MX-SDS | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | US-SDS | Compliance Requirement ID: US-SDS | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | EU-GHS Classification | Compliance Requirement ID: EU-GHS Classification | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | World-GHS Classification | Compliance Requirement ID: World-GHS Classification | Compliance requirement versions are delivered with the software. |
| Compliance Requirement Version | World-UN Hazardous Ingredients | Compliance Requirement ID: World-UN Hazardous Ingredients | Compliance requirement versions are delivered with the software. |
| Compliance Purpose | Transport in Europe | The following compliance requirements are assigned:UNRTDGIMDG-CodeIATA-DGRADRRIDADN | Requirements are relevant for Europe.Loaded and activated with the scope item. |
| Compliance Purpose | Transport in North America | The following compliance requirements are assigned:49 CFRIATA-DGRIMDG-CodeNOMTDG | Requirements are relevant for North America.Loaded and activated with the scope item. |
| Compliance Purpose | Transport in South America | The following compliance requirements are assigned:ANTTIATA-DGRIMDG-CodeNCh382UNRTDG | Requirements are relevant for South America.Loaded and activated with the scope item. |
| Compliance Purpose | Transport in Middle East, Africa, Asia | The following compliance requirements are assigned:ADGIATA-DGRIMDG-CodeNZS 5433SANAS 10228UNRTDG | Requirements are relevant for Middle East, Africa, Asia.Loaded and activated with the scope item. |
| Compliance Purpose | SDS for CA, DE, FR, MX, US | CA-SDSDE-SDSFR-SDSMX-SDSUS-SDS | Requirements are relevant for Safety Data Sheets for Canada, Germany, France, Mexico, and United States.Loaded and activated with the scope item. |
| Compliance Purpose | SDS Authoring CRs | EU-GHS ClassificationWorld-GHS ClassificationWorld-UN Hazardous Ingredients | Requirements are relevant for SDS Authoring.Loaded and activated with the scope item. |

Data Set 1

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Compliance View: Manage Substance Compliance | Morpholine | Linked with listed substance L00000006111 | Loaded with the scope item. |
| Compliance View: Substance – Physical-Chemical Properties | Morpholine | State of Matter: solidColor: whiteOdor: acidicForm: crystalline | Loaded with the scope item. |
| Compliance View: Substance – Safety-Related Properties | Morpholine | Flash Point:Closed Cup: > 200 - <= 210 °C | Loaded with the scope item. |

Data Set 2

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Compliance View: Manage Substance Compliance | Cinnarizine | Linked with listed substance L00000008564 | Loaded with the scope item. |
| Compliance View: Substance – Physical-Chemical Properties | Cinnarizine | State of Matter: solidColor: whiteOdor: acidicForm: crystalline | Loaded with the scope item. |
| Compliance View: Substance – Safety-Related Properties | Cinnarizine | Flash Point:Closed Cup: > 200 - <= 210 °C | Loaded with the scope item. |

Data Set 3

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Compliance View: Unpackaged Product - Basic Data | Unpackaged Product RDSP_R_PRD90 | Internal Name: Unpackaged Product RDSP_R_PRD90Assigned Compliance Purposes:Transport in EuropeTransport in North AmericaTransport in South AmericaTransport in Middle East, Africa, AsiaSDS for CA, DE, FR, MX, USSDS Authoring CRs | Loaded with the scope item. |
| Compliance View: Unpackaged Product - Analytical Composition | Unpackaged Product RDSP_R_PRD90 | Substance: MorpholineRole in Composition: Active IngredientConcentration: 42.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: CinnarizineRole in Composition: Active IngredientConcentration: 58.000000Lower Limit: 0.000000Upper Limit: 0.000000 | Loaded with the scope item. |
| Compliance View: Unpackaged Product – Physical-Chemical Properties | Unpackaged Product RDSP_R_PRD90 | State of Matter: solidColor: whiteOdor: acidicForm: crystalline | Loaded with the scope item. |
| Compliance View: Unpackaged Product – Safety-Related Properties | Unpackaged Product RDSP_R_PRD90 | Flash Point:Closed Cup: > 213 - >= 223 °CMethod for Closed Cup: ASTM D 93Open Cup: > 223 - <= 233 °CMethod for Open Cup: ASTM D 92 | Loaded with the scope item. |

Data Set 4

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Compliance View: Unpackaged Product Basic Data | Unpackaged Product RDSP_R_PRD91 | Internal Name: Unpackaged Product RDSP_R_PRD91Assigned Compliance Purposes:Transport in EuropeTransport in North AmericaTransport in South AmericaTransport in Middle East, Africa, AsiaSDS for CA, DE, FR, MX, USSDS Authoring CRs | Loaded with the scope item. |
| Compliance View: Unpackaged Product - Analytical Composition | Unpackaged Product RDSP_R_PRD91 | Substance: MorpholineRole in Composition: Active IngredientConcentration: 42.000000Lower Limit: 0.000000Upper Limit: 0.000000Substance: CinnarizineRole in Composition: Active IngredientConcentration: 58.000000Lower Limit: 0.000000Upper Limit: 0.000000 | Loaded with the scope item. |
| Compliance View: Unpackaged Product - Physical-Chemical Properties | Unpackaged Product RDSP_R_PRD91 | State of Matter: solidColor: whiteOdor: acidicForm: crystalline | Loaded with the scope item. |
| Compliance View: Unpackaged Product - Safety-Related Properties | Unpackaged Product RDSP_R_PRD91 | Flash Point:Closed Cup: > 213 - >= 223 °CMethod for Closed Cup: ASTM D 93Open Cup: > 223 - <= 233 °CMethod for Open Cup: ASTM D 92 | Loaded with the scope item. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/dfd71e92c384cd90e61bf43b45d20e73)

### Preliminary Steps

In this section, you find the steps that you need to carry out before you start the procedures in this test script.

#### Check Compliance Requirement Versions

Use

Before you can start with the procedures in this test script, you have to check if specific compliance requirement versions are active. If they are not active, you need to activate them.

Procedure

Check Compliance Requirement Versions for Dangerous Goods

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dangerous Goods Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Activate Compliance Requirements - Dangerous Goods (F3439) app. | The app opens and displays the requirements in the New or Updated tab. |  |
| 3 | Check Compliance Requirement Versions | Check that only the latest version of the following compliance requirements is active:ADRRIDADNCFR 49IMDG-CodeIATA-DGRTo check the compliance requirement versions, used the search function to search for a compliance requirement.If the latest version of the compliance requirement is on the Active tab, check if there are older active versions and deactivate all older versions by choosing Deactivate in the Action column.If the latest version of the compliance requirement is on the New or Updated tab, activate it by choosing Activate in the Action column. Then, choose the Active tab, check for older active versions, and deactivate all older versions by choosing Deactivate in the Action column.If the latest version of the compliance requirement is on the Inactive tab, activate it by choosing Activate in the Action column. Then, choose the Active tab, check for older active versions, and deactivate all older versions by choosing Deactivate in the Action column. | Only the latest versions of the compliance requirements are active. |  |

Check Compliance Requirement Versions for Safety Data Sheets

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Activate Compliance Requirements - Safety Data Sheets (F8003) app. | The app opens and displays the requirements in the New or Updated tab. |  |
| 3 | Check Compliance Requirement Versions | Check that only the latest version of the following compliance requirements is active:World GHS ClassificationWorld UN Hazardous IngredientsIf the latest version of the compliance requirement is on the Active tab, check if there are older active versions and deactivate all older versions by choosing Deactivate in the Action column.If the latest version of the compliance requirement is on the New or Updated tab, activate it by choosing Activate in the Action column. Then, choose the Active tab, check for older active versions, and deactivate all older versions by choosing Deactivate in the Action column.If the latest version of the compliance requirement is on the Inactive tab, activate it by choosing Activate in the Action column. Then, choose the Active tab, check for older active versions, and deactivate all older versions by choosing Deactivate in the Action column. | Only the latest versions of the compliance requirements are active. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- | --- | --- |
| [Check Substance Data](#unique_10) [page ] 14 | Master Data - Product Compliance | SAP_BR_MD_SPECIALIST_PCL | Master Data Specialist - Product Compliance | Manage Substances Compliance (F2578)Manage Physical Chemical Properties (F4606)Manage Safety-Related Properties (F5157) | All data needed for creating a substance request is available. |
| [Create Private Substance Request](#unique_11) [page ] 15 | Master Data - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Master Data Specialist - Product Compliance | Process Service Requests - Regulatory Documentation (F4295) | Substance requests for the substances Cinnarizine and Morpholine are created. |
| [Check and Enter Product Data](#unique_12) [page ] 17 | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Stewardship Specialist - Product Compliance | Manage Basic Compliance Data - Unpackaged Products (F2641)Unpackaged Product (F2647)Manage Analytical Compositions (F3210)Manage Physical Chemical Properties (F4606)Manage Safety-Related Properties (F5157)Manage Uses (F5467) | All data needed for creating a product request is available. |
| [Create Product Request](#unique_13) [page ] 19 | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Stewardship Specialist - Product Compliance | Process Service Requests - Regulatory Documentation (F4295) | Product requests for the products Unpackaged Product RDSP_R_PRD90 and Unpackaged Product RDSP_R_PRD9 1 are created. |
| [Check Data Received from Service Provider (Reference Service)](#unique_14) [page ] 20 | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Stewardship Specialist - Product Compliance | Process Service Requests - Regulatory Documentation (F4295)Assess GHS Classification (F5369)Assess Hazardous Ingredients (F5086)Classify Dangerous Good (F4465)Managing Safety Data Sheets (F3972) | Data for the GHS classification and the dangerous goods classification, hazardous ingredients, and safety data sheets are received from the reference service simulating a service provider for regulatory documentation. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check Data and Request Private Substance

#### Check Substance Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before creating a substance request, the Master Data - Product Compliance has to ensure that all needed data is entered in the Product Compliance solution.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a . Master Data - Product Compliance | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Substances Compliance (F2578) app. | The app opens and displays a list of all substances used in the Product Compliance solution. |  |
| 3 | Search for Substance | Enter substance Cinnarizine in the Search field. | In the Substance list, the search result is displayed. |  |
| 4 | Open Substance | Select the row with the substance Cinnarizine. | A details screen opens and displays compliance data for the substance. |  |
| 5 | Open Physical-Chemical Properties | In the Properties section, select the row for the physical-chemical properties.Note the status of the property. If the status is not Released, you have to release the data in the next step. | The Manage Physical Chemical Properties (F4606) app opens and displays the physical-chemical data that is entered for substance |  |
| 6 | Check Physical-Chemical Properties | In the General section, check that there are values for state of matter, color, odor, and form entered. If values for additional physical-chemical properties are entered, they are also sent to the service provider (reference service) when you create a private substance request.If the property data is not released, release it. | Data is entered for the state of matter, color, odor, and form. |  |
| 7 | Navigate Back | Navigate back to the Manage Substances Compliance (F2578) app. | The app opens and displays compliance data for the substance. |  |
| 8 | Open Safety-Related Properties | In the Properties section, choose the row for the safety-related properties.Note the status of the property. If the status is not Released, you have to release the data in the next step. | The Manage Safety-Related Properties (F5157) app opens and displays the safety-related data that is entered for the substance. |  |
| 9 | Check Safety-Related Properties | In the Flammability section, check that data for the flashpoint is entered. If values for additional safety-related properties are entered, they are also sent to the service provider (reference service) when you create a private substance request.If the property data is not released, choose Release so that the data can be used in follow-on processes such as in a service request. | Data is entered for the flashpoint. |  |
| 10 | Navigate Back | Navigate back to the Manage Substances Compliance (F2578) app. | The app opens and displays compliance data for the substance. |  |
| 11 | Check Substance Data for Second Substance | Navigate back to the Substance list and repeat steps 3 - 10 for the substance Morpholine. |  |  |

#### Create Private Substance Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Master Data Specialist - Product Compliance creates a service request to be sent to the service provider for regulatory documentation for a private substance. This data is needed to subsequently process a service request for a product that contains the requested substance in its composition.

When creating a private substance request, all data that the service provider needs to derive and generate the regulatory information for that substance has to be provided in the service request, such as physical-chemical properties and safety-related properties.

To simulate the cooperation with a service provider for regulatory documentation, the Product Compliance solution sends sample data to a reference service.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Service Requests - Regulatory Documentation (F4295) app. | The app opens and displays the open service requests. |  |
| 3 | Create Private Substance Request (Fist Substance) | Choose New Service Request and in the Select the Types of the Service Request popup, select New Private Substance. | The Select Substance for Request Creation dialog opens and shows a list of all company substances. |  |
| 4 | Select Substance | In the Select Substance for Request Creation dialog, search for Cinnarizine and select the search result. | The Confirm Request Creation dialog is displayed. |  |
| 5 | Create Request | In the Confirm Request Creation dialog, choose Create Request. | The system creates a substance request, closes the dialog, and displays the request in the Open tab. |  |
| 6 | Create Private Substance Request (Second Substance) | Repeat steps 3 - 5 for substance Morpholine |  |  |
| 7 | Process Again | Choose Process Again, and then Refresh. | The system reprocesses all service requests, and the displayed list is updated.Note: Wait until the processing status of the service requests are In Progress. This status indicates that the data has been successfully transferred to the service provider (reference service).It may take some time until the request is in status In Progress. You can choose Process Again, and then Refresh to monitor the status.As soon as the status for both substance requests switch from In Process to Completed, you can continue with [Check and Enter Product Data](#unique_12) [page ] 17. |  |

### Check Data and Request Product

#### Check and Enter Product Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before creating a product request, the Product Stewardship Specialist - Product Compliance has to ensure that all needed data is entered in the Product Compliance solution and all substances that are contained in the composition of the product are already requested.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Basic Compliance Data - Unpackaged Products (F2641) app. | The app opens and displays a list of all unpackaged products used in the Product Compliance solution. |  |
| 3 | Search for Product | Enter product Unpackaged Product RDSP_R_PRD90 in the Search field. | The Unpackaged Products list shows the search result. |  |
| 4 | Open Product | Select the row with the Unpackaged Product RDSP_R_PRD90 product. | The Unpackaged Product (F2647) app opens and displays compliance data for the product. |  |
| 5 | Open Analytical Composition | In the Composition section, choose the row for the analytical composition.Note the status of the composition. If the status is not Released, you have to release the data in the next step. | The Manage Analytical Compositions (F3210) app opens and displays the analytical composition of the product. |  |
| 6 | Check Analytical Composition | In the Analytical Components table, check the components.If the analytical composition is not released, release it. | The following substances are entered as components:Substance: MorpholineSubstance: Cinnarizine |  |
| 7 | Navigate Back | Navigate back to the Unpackaged Product (F2647) app. | The app opens and displays compliance data for the product. |  |
| 8 | Open Physical-Chemical Properties | In the Properties section, choose the row for the physical-chemical properties.Note the status of the property. If the status is not Released, you have to release the data in the next step. | The Manage Physical Chemical Properties (F4606) app opens and displays the physical-chemical data that is entered for the product. |  |
| 9 | Check Physical-Chemical Properties | In the General section, check that there are values for state of matter, color, odor, and form entered. If values for additional physical-chemical properties are entered, they are also sent to the service provider (reference service) when you create a product request.If the property data is not released, release it. | Data is entered for the state of matter, color, odor, and form. |  |
| 10 | Navigate Back | Navigate back to the Unpackaged Product (F2647) app. | The app opens and displays compliance data for the product. |  |
| 11 | Open Safety-Related Properties | In the Properties section, choose the row for the safety-related properties.Note the status of the properties. If the status is not Released, you have to release the data in the next step. | The Manage Safety-Related Properties (F5157) app opens and displays the safety-related data that is entered for the product. |  |
| 12 | Check Safety-Related Properties | In the Flammability section, check that data for the flashpoint is entered. If values for additional safety-related properties are entered, they are also sent to the service provider (reference service) when you create a product request.If the property data is not released, choose Release so that the data can be used in follow-on processes such as in a service request. | Data is entered for the flashpoint. |  |
| 13 | Navigate Back | Navigate back to the Unpackaged Product (F2647) app. | The app opens and displays compliance data for the product. |  |
| 14 | Create Uses | For Assigned Uses in the Application, Uses, Markets and Purposes section, choose Create.In the Create Use dialog, select (World). | A use is created and is displayed in the Assigned Uses table. |  |
| 15 | Open Use | In the Assigned Uses table, select the row with the newly created use. | The Manage Uses (F5467) app opens and displays details about the use. |  |
| 16 | Edit Use | Choose Edit.In the Recommended Uses table, choose Add.In the Assign Recommended Uses dialog, select one phrase and choose OK.Save and release your entries. | The selected phrase is assigned to the use and is displayed in the Recommended Uses table. |  |
| 17 | Navigate Back | Navigate back to the Unpackaged Product (F2647) app. | The app opens and displays compliance data for the product. |  |
| 18 | Check and Release Data for Second Product | Navigate back to the Manage Basic Compliance Data - Unpackaged Products (F2641) app and repeat step 3 - 17 for the product Unpackaged Product RDSP_R_PRD91. |  |  |

#### Create Product Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After requesting all substances that are contained in the composition of a product, the Product Stewardship Specialist - Product Compliance creates a service request to be sent to the service provider for regulatory documentation for the product.

When you create a product request, all data that the service provider needs to derive and generate the regulatory information for that product has to be provided in the service request, such as the analytical composition, physical-chemical properties, and safety-related properties.

To simulate the cooperation with a service provider for regulatory documentation, the Product Compliance solution sends sample data to a reference service.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Service Requests - Regulatory Documentation (F4295) app. | The app opens and displays the open service requests. |  |
| 3 | Create Product Request | Choose New Service Request, and in the Select the Types of the Service Request dialog, select New Product. | The Select Product for Request Creation dialog opens and shows a list of all products. |  |
| 4 | Select Product | In the Select Product for Request Creation dialog, search for Unpackaged Product RDSP_R_PRD90 and select the search result. | The Confirm Request Creation dialog is displayed showing information about data to be sent to the service provider (reference service) and the safety data sheets that are requested from the service provider (reference service). |  |
| 5 | Create Request | In the Confirm Request Creation dialog, choose Create Request. | The system creates a new product request, closes the dialog, and displays the request in the Open tab. |  |
| 6 | Create Second Product Request | Repeat steps 3 - 6 for the product Unpackaged Product RDSP_R_PRD91. |  |  |
| 7 | Process Again | Choose Process Again, and then Refresh. | The system reprocesses all service requests, and the displayed list is updated.Note: Wait until the processing status of the service request is Completed. This status indicates that the data has been successfully transferred to the service provider (reference service) and the data from the service provided has been transferred successfully to the Product Compliance solution.It may take some time until the request is in status Completed. You can choose Process Again, and then Refresh to monitor the status. |  |

#### Check Data Received from Service Provider (Reference Service)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the service request is in status Ready, the service provider has finished gathering the requested data. The data provided by the service provider is retrieved and the status of the service request is changed to Completed. Once the service request is completed, the Product Stewardship Specialist - Product Compliance can check the data that is provided by the service provider in the Product Compliance solution.

To simulate the cooperation with a service provider for regulatory documentation, a reference service returns sample data for the requested products Unpackaged Product RDSP_R_PRD90 and Unpackaged Product RDSP_R_PRD91.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Service Requests - Regulatory Documentation (F4295) app. | The app opens and displays the open service requests. |  |
| 3 | Open Product Request | On the Completed tab, choose the line with the Unpackaged Product RDSP_R_PRD91 product.Note that if your request is not on the Completed tab, check the other tabs for your request. Choose Process Again and refresh your screen until your request is completed. | The Product Compliance Service Request screen opens and displays the requested safety data sheets and the sent and received data. |  |
| 4 | Open GHS Classification | In the Data Received section, select a line for GHS classification data. | The Assess GHS Classification (F5369) app opens and displays the received GHS classification data. |  |
| 5 | Check GHS Classification | Check if there is data for the GHS classification. | Data for the GHS classification is available. |  |
| 6 | Navigate Back | Navigate back to the Process Service Requests - Regulatory Documentation (F4295) app. | The app opens and displays the Product Compliance Service Request screen. |  |
| 7 | Open Hazardous Ingredients | In the Data Received section, select a line for hazardous ingredients data. | The Assess Hazardous Ingredients (F5086) app opens and displays the received hazardous ingredients. |  |
| 8 | Check Hazardous Ingredients | Check if there are any hazardous ingredients listed. | Hazardous ingredients are listed. |  |
| 9 | Navigate Back | Navigate back to the Process Service Requests - Regulatory Documentation (F4295) app. | The app opens and displays the Product Compliance Service Request screen. |  |
| 10 | Open Dangerous Goods Basic Classification | In the Data Received section, select a line for dangerous goods data, for example, ADR 2021. | The app for classifying unpackaged products according to the selected dangerous goods regulation, for example, Process Service Requests - Regulatory Documentation (F4295), opens and displays the dangerous goods basic classification. |  |
| 11 | Check Dangerous Goods Basic Classification | In the app for classifying unpackaged products according to dangerous goods regulations, check if there is data for a dangerous goods classification. | Data for the dangerous goods classification is available. |  |
| 12 | Navigate Back | Navigate back to the Process Service Requests - Regulatory Documentation (F4295) app. | The app opens and displays the Product Compliance Service Request screen. |  |
| 13 | Open Safety Data Sheet | In the Data Received section, select any line for a safety data sheet. | The Managing Safety Data Sheets (F3972) app opens and displays the available safety data sheets. |  |
| 14 | Check Safety Data Sheet | Check if there are any safety data sheets available. | Safety data sheets are available. |  |
| 15 | Navigate Back | Navigate back to the Process Service Requests - Regulatory Documentation (F4295) app. | The app opens and displays the Product Compliance Service Request screen. |  |
| 16 | Check Received Data for the Second Product | Navigate back to the Process Service Requests – Regulatory Documentation screen and repeat Step 3 - 15 for the product Unpackaged Product RDSP_R_PRD90.Note the following:In step 5, check that the hazardous definition is Not a hazardous substance or mixture.In step 11, check if the product is classified as No Dangerous Goods. |  |  |

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
> Flagged while digesting this document, not verified: Internal inconsistency in launchpad space IDs: the Roles table gives the space 'Master Data - Product Compliance' the ID SAP_BR_MD_SPECIALIST_PCL, but the Overview Table row for Create Private Substance Request lists the same space name with ID SAP_BR_PRODSTWRD_SPLST_PCL (the Product Stewardship role's ID).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/product-compliance-document-authoring-7do-ae-test-script-sap-s-4hana-c]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-label-management-6mt-ae-sap-s-4hana-cloud-public-edition-1]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-manage-safety-data-sheets-for-products-3vr-ae-sap-s-4hana]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AV_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 42,383 chars in the whole document
