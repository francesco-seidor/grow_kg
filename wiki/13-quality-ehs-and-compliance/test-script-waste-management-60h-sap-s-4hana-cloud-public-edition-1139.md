---
id: 13-quality-ehs-and-compliance/test-script-waste-management-60h-sap-s-4hana-cloud-public-edition-1139
title: "Test Script: Waste Management (60H) - SAP S/4HANA Cloud Public Edition (60H_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 60H Waste Management: EHS waste process from material data to transport documents."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/waste-management]
aliases: [60H_S4CLD2608_BPD_EN_XX]
keywords: [Waste Management, test scripts, waste material data, waste locations, disposers and transporters, waste permits, waste streams, disposal channels, waste transfer requests, waste transportation documents]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/60H_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1139
topic: 13-quality-ehs-and-compliance/waste-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Waste Management (60H) - SAP S/4HANA Cloud Public Edition (60H_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/60H_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Waste Management** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Waste Management (60H) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232825451)

[2 Prerequisites 4](#_Toc232825452)

[2.1 System Access 4](#_Toc232825453)

[2.2 Roles 4](#_Toc232825454)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232825455)

[2.4 Preliminary Steps 6](#_Toc232825456)

[3 Overview Table 7](#_Toc232825457)

[4 Test Procedures 9](#_Toc232825458)

[4.1 Manage Material Data 9](#_Toc232825459)

[4.1.1 Manage Dangerous Goods Information (Waste Management) 12](#_Toc232825460)

[4.2 Manage Waste Locations 13](#_Toc232825461)

[4.3 Create a Disposer 14](#_Toc232825462)

[4.4 Create a Transporter 16](#_Toc232825463)

[4.5 Create Waste Permits 17](#_Toc232825464)

[4.6 Manage Waste Permits 19](#_Toc232825465)

[4.7 Create Waste Streams 20](#_Toc232825466)

[4.8 Create a Disposal Channel 22](#_Toc232825467)

[4.9 Create a Waste Transfer Request 23](#_Toc232825468)

[4.9.1 Create a Waste Transfer Request from the Beginning 23](#_Toc232825469)

[4.9.2 Create a Waste Transfer Request by Copying an Existing Request 25](#_Toc232825470)

[4.10 Manage a Waste Transfer Request 26](#_Toc232825471)

[4.11 Create a Waste Transportation Document from a Waste Transfer Request 28](#_Toc232825472)

[4.12 Generate a Waste Transportation Document Form 31](#_Toc232825473)

[4.13 Compare Waste Analytics 32](#_Toc232825474)

[4.14 Import Waste Delivery Notes 33](#_Toc232825475)

[4.14.1 Create a Material (Import Delivery Notes) 36](#_Toc232825476)

[4.14.2 Create a Disposer (Import Delivery Notes) 37](#_Toc232825477)

[4.14.3 Create a Transporter (Import Delivery Notes) 39](#_Toc232825478)

[4.14.4 Create a Waste Stream (Import Delivery Notes) 40](#_Toc232825479)

[4.14.5 Create a Disposal Channel (Import Delivery Notes) 41](#_Toc232825480)

[4.15 Delete Waste Delivery Notes 43](#_Toc232825481)

## Purpose

Overview

This scope item supports waste generators in managing waste disposal processes across one or more enterprise locations. It includes:

- Managing hazardous and nonhazardous waste from the point of creation within a plant
- Supporting waste compliance officers and environmental managers in coordination of waste shipments locally or globally
- Supporting production operators in requesting waste pickup and movement
- Performing plausibility checks to ensure compliance with issued permits and registered waste
- Creating waste transportation documents
- Performing waste analytics

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note Environment, Health, and Safety delivers example content (such as reports and regulations) that you can adapt according to your requirements. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/60H_S4CLD2602_BPD_EN_XX.docx)). |

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
| Environmental Manager | SAP_BR_EHS_ENV_MGMT | Environment Management | SAP_BR_ EHS_ENV_MGMT |  |
| Production Operator - EHS Info | SAP_BR_PRODN_OPTR_EHS_INFO |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Location | Plant Wiesbaden | Location of type Plant.Parent location for all other sample locations. |  |
| Location | Wiesbaden Laboratory and Production Line | Location of type Production Unit.Sublocation of Plant Wiesbaden. |  |
| Location | Wiesbaden Storage Building | Location of type Storage Location.Sublocation of Plant Wiesbaden. |  |
| Business Partner | AWB Wiesbaden – Hessen GmbH | (Waste) Business Partner with the role Disposer. |  |
| Business Partner | Rhein Main Hazardous Materials Transport | (Waste) Business Partner with the role Transporter. |  |
| Business Partner | Untere Abfallbehörde Wiesbaden Hessen | Business Partner with the role Authority. |  |
| Product | Hydrochloric Acid | Product. |  |
| Product | Hydrochloric Acid 2L | Product. |  |
| Waste Material | Hydrochloric Acid | Waste Material with the logistics role Emissions Relevant, Disposed and Transported. |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 3SR | Create EHS Location |
| 22G | Create Business Partner for Treasury and Risk Management |
| 660 | Create an EHS Product |
| 65Z | Create an EHS Chemical Compliance Information Material |

### Preliminary Steps

Purpose

Before you begin with the test procedures, make sure that you complete the steps below. You can use your own master data or the following sample data to go through the test procedure. Please refer to the corresponding Master Data Scripts to create your own master data set.

Procedure

1. Start the SAP Fiori launchpad.
2. If the Manage Locations (F3404) tile is not available on your SAP Fiori launchpad home screen, add it via the App Finder.

|  |
| --- |
| Note To add a tile to your SAP Fiori launchpad home screen, go to your profile in the upper right corner of the screen. Select the Edit Home Page option from the list. Then, select the blank tile that appears to go to the App Finder. In the Search field on the upper right side of the screen, enter the name of the app that you want to add to your SAP Fiori launchpad, and press Enter. The app appears in your search results. Select the pin to add the app tile to your SAP Fiori launchpad home screen. In the footer, the system shows a message that the tile has been added successfully. To exit edit mode, go back to your SAP Fiori launchpad home screen and select the Exit Edit Mode option from the list under your profile. |

1. Start the Manage Locations (F3404) app.
2. Select the Plant Wiesbaden location and choose the hyperlink.
3. Navigate to the Persons Responsible tab.
4. Add your user as a person responsible with the Environmental Manager role.
5. Save your entries.
6. Repeat steps 4–7 to assign your user as a person responsible with the Environmental Manager role for all other locations (Wiesbaden Laboratory and Production Line and Wiesbaden Storage Building).

|  |
| --- |
| Note For the Wiesbaden Laboratory and Production Line location, also add your user as a person responsible with the Environmental Technician (Production Operator - EHS Info) role. |

|  |
| --- |
| Note Make sure that all locations are set to Active to enable their use in the test procedures. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Material Data](#unique_8) [page ] 9 | Environmental Manager | Manage Material Data (F4864) | Waste characterization information is entered for a waste material. |
| [Manage Waste Locations](#unique_9) [page ] 13 | Environmental Manager | Manage Locations (WDA0334) | Manage locations created by adding classifiers. |
| [Create a Disposer](#unique_10) [page ] 14 | Environmental Manager | My Transporters and Disposers - Waste Management (F5222) | Disposer is created which disposes waste materials. |
| [Create a Transporter](#unique_11) [page ] 16 | Environmental Manager | My Transporters and Disposers - Waste Management (F5222) | Transporter is created to transport waste materials. |
| [Create Waste Permits](#unique_12) [page ] 17 | Environmental Manager | My Permits (F5192) | Permit is created and assigned to an Environmental Manager associated to certain locations, classified as waste generators. |
| [Manage Waste Permits](#unique_13) [page ] 19 | Environmental Manager | My Permits (F5192) | Contents are set up and waste environmental limits are added to the created permit in order to meet and manage compliance requirements over time. |
| [Create Waste Streams](#unique_14) [page ] 20 | Environmental Manager | My Waste Streams - Waste Management (F5410) | Waste stream is created which represents allocation of waste material to a point of generation. |
| [Create a Disposal Channel](#unique_15) [page ] 22 | Environmental Manager | Manage Waste Disposal Channels - Waste Management (F6543) | Disposal channels, which specify the disposer, transporters and the facility, are created for waste streams. |
| [Create a Waste Transfer Request](#unique_16) [page ] 23 | Production Operator - EHS Info | My Waste Transfer Requests - Waste Management (F6083) | Waste transfer request is created by a Production Operator for waste from a point of waste generation to be transferred to a waste storage location. |
| [Manage a Waste Transfer Request](#unique_17) [page ] 26 | Environmental Manager | Manage Waste Transfer Requests - Waste Management (F6084) | The Environmental Manager takes over the waste transfer request. The waste is then posted for a waste storage location. |
| [Create a Waste Transportation Document from a Waste Transfer Request](#unique_18) [page ] 28 | Environmental Manager | Manage Waste Transfer Requests - Waste Management (F6084) | Legally compliant transportation document is created to dispose of waste. |
| [Generate a Waste Transportation Document Form](#unique_19) [page ] 31 | Environmental Manager | My Waste Transportation Documents (F5290) | Generate a transportation document form for a location, classified as a waste generator.This form confirms that the waste can be externally transported and taken to a disposal facility. |
| [Compare Waste Analytics](#unique_20) [page ] 32 | Environmental Manager | Waste Analytics - Waste Management (F6956) | Perform statistical analysis of several waste products disposed by comparing waste transportation documents. |
| [Import Waste Delivery Notes](#unique_21) [page ] 33 | Environmental Manager | Import Waste Documents - Delivery Notes (F7338) | Import waste transportation documents. |
| [Delete Waste Delivery Notes](#unique_22) [page ] 43 | Environmental Manager | Import Waste Documents - Delivery Notes (F7338) | Delete waste delivery notes. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Material Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager defines the waste-related information of a material including a related packaged product, waste codes, and dangerous goods.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the [Manage Material Data](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F4864) app. | The Manage Material Data screen is displayed. |  |
| 3 | Select a Material | On the Manage Material Data screen, select the material name Hydrochloric Acid.Note You can use the search field to look for the material name. | The Material: Hydrochloric Acid screen is displayed. |  |
| 4 | Add Related Packaged Products | Choose Edit.On the screen, the material Hydrochloric Acid already has one predefined Product with the same name, Hydrochloric Acid.In the section Related Packaged Products, choose Add.Use the value help for the mandatory field Product and search for Hydrochloric Acid – 2L with the logistics roles Emissions Relevant, Disposed, and Transported.Select the product and choose Save. | The Product is preassigned to the material and one new Related Packaged Product is added. |  |
| 5 | Select a Waste Type | Navigate to the Waste Data section.In the Waste Type field, select Hazardous from the dropdown list. | The waste type Hazardous is selected. |  |
| 6 | Maintain Waste Codes | In the Waste Data section, Waste Codes subsection, choose Manage Waste Codes. | The Manage Waste Codes screen is displayed. |  |
| 7 | Add Waste Codes | On the Manage Waste Codes screen, choose Edit.In the Waste Codes screen, choose Add.Search for the waste code 06 01 02* corresponding to Hydrochloric Acid from the compliance requirement EN: COMMISSION DECISION: 2014/955/EU.Select the Required On Manifest and Required On Label checkboxes.Note You can use the value help provided in the Waste Code field.Choose Save and navigate back to the Manage Material Data screen. | The waste codes are added and the waste-related information for the material is saved. |  |
| 8 | Add Dangerous Goods Information | Note If the Product Compliance component is not available on your system, follow the steps in [Manage Dangerous Goods Information (Waste Management)](#unique_24) [page ] 12 instead.Navigate to the Dangerous Goods section and choose Edit.In the Assigned Compliance Purposes subsection, choose Add.Use the value help to search for Compliance Purpose Transport in Europe then choose OK to save.Choose Save.Note The Unpackaged Product Assessments and Packaged Product Assessments are performed separately by a Dangerous Good Specialist. The information will be displayed automatically in the screen when the assessment has been completed.Note The steps 8-11 are optional. You only need to edit this information one time. | The compliance purpose Transport in Europe is added. |  |
| 9 | Manage Analytical Composition | Navigate to the section Analytical Composition and choose Manage Composition. | The Manage Analytical Composition screen is displayed. |  |
| 10 | Add Analytical Components | Choose Edit.Select Substance in the Product-Categorization dropdown list.In the Analytical Components section, choose Create and select the substance Ethanol.Fill in the data for the newly introduced substance:Role in Composition: ImpurityConcentration: 0,05Unit of Measure: %Choose Save and navigate back to the selected material in the [Manage Material Data](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) app. | You have added two substances in the analytical components section. |  |
| 11 | Maintain Default Physical-Chemical Properties | Navigate to the Default Properties section and choose the Physical-Chemical Properties entry. | The Manage Physical-Chemical Properties screen is displayed. |  |
| 12 | Add Physical-Chemical Properties | Choose Edit.Fill in data for the Physical-Chemical Properties:General:Physical State at 20° (68°F), 101.3kPa: liquidColor: colorlessNotes (color): Light yellowOdor: acidicMolar Mass: Not ApplicableDensity:Density at 20°C (68°F): 1,18 g/cm3Solutions:Measured pH Value at 20°C (68°F): 1Concentration: 370 g/lAssessment: acidicPhase Transitions:Melting Point: -26°Vapor Pressure at 20°C (68°F): 190 hPaChoose Save, then choose Release.Navigate back to the [Manage Material Data](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) app. | You added the Physical-Chemical Properties data. |  |

#### Manage Dangerous Goods Information (Waste Management)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager performs dangerous goods assessments for the products related to a waste material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Material Data (F4864) app. | The Manage Material Data screen is displayed. |  |
| 3 | Select a Material | On the Manage Material Data screen, select the material name Hydrochloric Acid.Note You can use the search field to look for the material name. | The Material: Hydrochloric Acid screen is displayed. |  |
| 4 | Create Product Assessment | In the Dangerous Goods section, Product Assessments subsection, choose Create. | The Dangerous Goods Information screen is displayed. |  |
| 5 | Classify Product | In the Basic Classification section, enter the following:Classified As: Dangerous GoodsRegulation: Use the value help to select any <Regulation>.In the Permission Information section, enter the following:Transport Permission: AllowedIn the Dangerous Goods Basic Description section, enter a free-text comment in the Description field.Choose Create. | You have created a product assessment. |  |
| 6 | Create Packaged Product Assessment | In the Dangerous Goods section, Packaged Product Assessments subsection, choose Create. | The Dangerous Goods Information screen is displayed. |  |
| 7 | Classify Packaged Product | In the Dangerous Goods Classification section, enter the following:Packaged Product: Hydrochloric Acid – 2LRegulation: Use the value help to select any <Regulation>.Classified As: Dangerous GoodsIn the Permission Information section, enter the following:Mode of Transport: RoadTransport Permission: AllowedIn the Packaging Information section, enter the following:Packaging Type: BagPackaging Size: 2 LIn the Description for Documents section, enter a free-text comment in the Description field.Choose Create. | You have created a packaged product assessment. |  |

### Manage Waste Locations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a new location record in the location structure. The new record is required because there’s new or changed equipment in the location. The data of the new location record is updated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Locations (WDA0334) app. | The Locations screen is displayed. |  |
| 3 | Navigate to the Location | Use the search function to look for your location named Plant Wiesbaden and select it from the list. | The Location: Plant Wiesbaden screen is displayed. |  |
| 4 | Navigate to Location Classifiers | On the Location: Plant Wiesbaden screen, under the Environmental Details tab, choose Add located under the Location Classifiers section. | The location classifiers dialog box named Location: Plant Wiesbaden is shown. |  |
| 5 | Add Location Classifier | In the dialog box, use the value help and enter the following:Name: Waste GeneratorNote The name must be written exactly, or you can make use of the wild card searchSelect it from the list and choose OK to save, then the dialog box will close. | Waste Generator name has been added as a location classifier to the location. |  |
| 6 | Add Waste Registration Number | You are now back on the Location: Plant Wiesbaden screen.Under the Waste Relevant Data section, add the following information:Waste Registration Number: HE47899 | Waste Registration Number has been added to the location. |  |
| 7 | Save Waste Information | Choose Save at the bottom right hand of the screen to save added waste relevant information.Note Repeat steps 3-5 for locations Wiesbaden Laboratory and Production Line and Wiesbaden Storage Building which have location classifier names Point of Waste Generation and Waste Storage respectively and then save.These locations do not need waste registration numbers, so step 6 can be skipped. | Waste information for the location has been saved. |  |

### Create a Disposer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a disposer which defines a business partner of type disposer and links it to a location, classified as a waste generator.

The Environmental Manager then names a disposal facility and assigns a waste material to it for later disposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open [My Transporters and Disposers - Waste Management](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F5222) app. | The My Transporters and Disposers screen is displayed. |  |
| 3 | Create Disposer | On the My Transporters and Disposers screen, choose Create -> Disposers. | The Create Disposer screen is now displayed. |  |
| 4 | Enter Waste Partner Data | On the Create Disposer screen, under the Waste Partner tab, enter the following data:Business Partner: AWB Wiesbaden - Hessen GmbHWaste Generator: Plant WiesbadenNote You can use the value help to find the business partner and waste generator. | Waste partner data is entered. The Validity Area field is automatically filled based on the selection of the waste generator. |  |
| 5 | Enter Facilities Data | Under the Facilities tab, choose Add.On the Assign Facilities screen, select the address Wiesbaden (67785) and choose OK.Back on the Facilities tab, enter the following data:Facility Name: Wiesbaden Treatment Facility 1Waste Registration Number: HE1579579 | Facility data is added. |  |
| 6 | Enter Waste Material Data | Under the Waste Materials tab, choose Add.On the Assign Waste Material screen, select Hydrochloric Acid and choose OK.Back on the Waste Materials tab, enter the following data:Facility Assigned: Wiesbaden Treatment Facility 1R&D Code: R6Note You can use the dropdown list to find the Facility Name and value help to find the R&D Code.The field name of the code will differ depending on country/region. R&D Code is used in European countries and Management Method Code is used in the U.S.A. | Waste material data is added. |  |
| 7 | Save Disposer | On the My Transporters and Disposers screen, at the bottom right corner of the screen, choose Create. | The disposer is created. |  |

### Create a Transporter

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a transporter which defines business partner of type transporter and links it to a location, classified as a waste generator.

The Environmental Manager then assigns a waste material to be transported to a disposal facility.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open [My Transporters and Disposers - Waste Management](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F5222) app. | The My Transporters and Disposers screen is displayed. |  |
| 3 | Create a Transporter | On My Transporters and Disposers screen, choose Create -> Transporter. | The Create Transporter screen is displayed. |  |
| 4 | Enter Waste Partner Data | On the Create Transporter screen, under the Waste Partner tab, enter the following data:Business Partner: Rhein Main Hazardous Materials TransportWaste Generator: Plant WiesbadenNote You can use the value help to find the Business Partner and Waste Generator. | Waste partner data is entered.The Waste Registration Number field is filled based on the selection of business partner.The Validity Area field is filled based on the selection of waste generator. |  |
| 5 | Enter Waste Material Data | Under the Waste Materials tab, choose Add.On the Assign Waste Material screen, select Hydrochloric Acid and choose OK. | Waste material data is added. |  |
| 6 | Save Transporter | On the My Transporters and Disposers screen, at the bottom right corner of the screen, choose Create. | The transporter is created. |  |

### Create Waste Permits

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a new permit with domain waste for a location with the classifier waste generator that they are responsible for, so they can meet the compliance requirements arising from the permit that is authorized by a corresponding local authority.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Permits (F5192) app. | The My Permits screen is displayed. |  |
| 3 | Create a Permit | On the My Permits screen, choose Create. | The New Permit screen is displayed. |  |
| 4 | Edit General Information Data | On the New Permit screen, under General Information, enter the following data:Basic Details:Name: Disposal HCl WiesbadenDomain: WastePermit Type: Standard Waste PermitPermit Number: ENT22544667Description: Permit to discharge hydrochloric acid from Plant Wiesbaden (Waste Code 06 01 02*)Internal Information:Location: Plant WiesbadenIssuing Authority: Untere Abfallbehörde Hessen – WiesbadenNote This is not a mandatory field.If you would like to enter an issuing authority, please maintain the corresponding business partner first.Note You can use the value help to find the corresponding Location and Issuing Authority.The ID is an internal-system, nonmandatory field, related to the compliance requirement ID.Issuing Organization: Untere Abfallbehörde Hessen – WiesbadenValidity Information:Effective Date: <today's date>Expiration Date: <five years from today's date> | General information for the permit is added. |  |
| 5 | Edit Waste Data | On the same screen, in the Waste Data section, enter the following information:Disposal Facility: Wiesbaden Treatment FacilityWaste Code: 06 01 02*Note You can use the value help to find the corresponding Disposal Facility and Waste Code. | The waste data of the permit is updated. |  |
| 6 | Create Permit | At the bottom right-hand corner of the same screen, choose Create. | Permit is created. |  |
| 7 | Navigate Back to the My Permits Screen | Choose the Back icon on the upper left part of the screen. | The My Permits screen is displayed. |  |
| 8 | Select Created Permit | On the My Permits screen, navigate to the Search field and enter the permit name to find the newly created permit.Select it from the results list.Note Alternatively, use one of the other filters to search and find a permit. | The Permit screen is displayed. |  |
| 9 | Edit Permit Lifecycle Value | Navigate to the Compliance Requirement Details tab.In the Permit Lifecycle field, verify that the following values are in the dropdown list: In Preparation, Application Submitted, Active, For Renewal, and Expired.Select Application Submitted. | Permit Lifecycle status is updated. |  |
| 10 | Edit Set "For Renewal" on Date | On the same screen, select the calendar icon in the Set "For Renewal" on field. Choose a date that is one to two months before the Expiration Date.Choose Save.Note The Send Notification checkbox is automatically selected.You can deselect the check box if you do not want to receive an email notification when the permit reaches the Set "For Renewal" on date. | Set "For Renewal" on date is updated and saved. |  |

### Manage Waste Permits

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager, to comply with applicable requirements, sets up data such as waste environmental limit, upper limit, referenced to the identified permit. This permit was recorded in the previous test procedure ([Create Waste Permits](#unique_12) [page ] 17).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open [My Permits](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) app. | The My Permits screen is displayed. |  |
| 3 | Select Permit | On the My Permits screen, navigate to the Search field and enter the permit name Disposal HCl Wiesbaden to find the previously created permit and select it from the results list.Note Alternatively, use one of the other filters to search and find the permit. | The Permit: Disposal HCl Wiesbaden screen is displayed. |  |
| 4 | Navigate to Waste Data | On the Permit: Disposal HCl Wiesbaden screen, select the Waste Data tab. | The Waste Data tab is displayed. |  |
| 5 | Enter an Upper Limit | In the Limit Data section, enter the following information:Unit: tUpper Limit Value: 250Upper Warning Value: 150Choose Save. | The upper limit for Hydrochloric Acid <= 250 t is created. |  |
| 6 | Edit Permit Lifecycle | Navigate back to the Compliance Requirement Details tab.In the Permit Lifecycle field, select Active from the dropdown list. | The Permit Lifecycle is updated and saved. |  |
| 7 | Edit Status | On the same screen, under the Set Status dropdown list on the upper left-hand corner, select Released. | The Status is updated and saved. |  |

### Create Waste Streams

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a waste stream which represents allocation of waste material to a point of waste generation inside a location, classified as a waste generator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open [My Waste Streams - Waste Management](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F5410). | My Waste Streams screen is displayed. |  |
| 3 | Create Waste Stream | On the My Waste Streams screen, choose Create. | The Waste Stream screen is now displayed. |  |
| 4 | Enter Waste Stream Data | On the Waste Stream screen, under the Waste Stream tab, enter the following data:Waste Stream Name: Waste Stream HCl WiesbadenWaste Stream Handling: Outbound - With Storage Location (OBWS)Product: Hydrochloric AcidNote The product is associated with the waste generator Plant Wiesbaden.Waste Storage Location: Wiesbaden Storage BuildingNote You can use the value help to find the Product and the dropdown lists to find the Waste Stream Handling and Waste Storage Location. | Waste stream data is entered.The Waste Codes field is filled based on the selection of the product. Waste codes were assigned to the material in the Manage Material Data app.The Waste Generator and Validity Area fields are automatically filled based on the assignment of material to waste generator in the My Transporters and Disposers - Waste Management app. |  |
| 5 | Enter Point of Waste Generation Data | Under the Point of Waste Generation tab, choose Add.Enter the following data:Location: Wiesbaden Laboratory and Production LineNote You can use the dropdown list to find the location.Unit of Measure: TO | Point of waste generation data is added. |  |
| 6 | Create Waste Stream | On the Waste Stream screen, at the bottom of the screen, choose Create. | The Waste Stream is created.This is the base for the creation of transfer requests. |  |

### Create a Disposal Channel

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager create a disposal channel which links a predefined waste stream to a predefined disposal facility.

The Environmental Manager also selects the waste transportation document type which defines the conditions on how and how much waste will be transported and disposed.

|  |
| --- |
| Note The waste transportation document types available depend on your country/region. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Waste Disposal Channels - Waste Management app. | The My Waste Streams screen is displayed. |  |
| 3 | Create Disposal Channel | On the Manage Waste Disposal Channels screen, choose Create. | The New: Disposal Channel screen is displayed. |  |
| 4 | Enter Disposal Channel Data | On the Basic Information tab, enter the following data:Disposal Channel Name: Disposal Channel HCl WiesbadenDisposal Facility: Wiesbaden Treatment Facility 1Transportation Document Type: E-BEGLEITSCHEIN (S_E-BGS)Note The list of Transportation Document Types depends on the country/region of where the Waste Generator, associated to the Disposal Facility selected, is located. | Basic waste disposal channel data is added. |  |
| 5 | Enter Permit Information | Under the Permits tab, choose Add and enter the following data:Permit Number: ENT22544667Note The Permit Type field is automatically filled with Standard Waste Permit (S). | Permit information is added. |  |
| 6 | Enter Waste Stream Information | Under the Waste Streams tab, choose Add.In the Waste Stream Name field, use the value help to search for and select Waste Stream HCl Wiesbaden. | Waste Stream information is added. |  |
| 7 | Enter Purchase Order Information (Optional) | Under the Purchase Orders tab, choose Add.In the Purchase Order field, use the value help to search for pre-existing purchase orders created by your Purchaser. | Purchase Order information is added. |  |
| 8 | Create Disposal Channel | Choose Create at the bottom right corner of the screen. | The Waste Disposal Channel is created. |  |
| 9 | Activate Disposal Channel | On the same screen, choose Activate on the top right corner. | The Waste Disposal Channel is activated and is the starting point for creating a transportation document to a disposal facility. |  |

### Create a Waste Transfer Request

#### Create a Waste Transfer Request from the Beginning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Production Operator - EHS Info requests waste to be transferred from a point of waste generation to a storage location once the capacity of the container, which houses the waste, is reached.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Waste Transfer Requests - Waste Management (F6083) app. | The My Waste Transfer Requests - Waste Management screen is displayed. |  |
| 3 | Create Waste Transfer Request | On the My Waste Transfer Requests screen, choose Create. | A pop up screen will appear with the name Select Waste Streams. |  |
| 4 | Select Waste Stream Data | On the Select Waste Streams screen, select the Waste Stream with Point of Waste Generation Wiesbaden Laboratory and Production Line, Product Hydrochloric Acid, and Waste Stream Waste Stream HCl Wiesbaden.Choose Next Step. | Waste Stream data is selected successfully. The Point of Waste Generation, Product, and Waste Stream fields are filled in based on the assignment in the My Waste Streams app. |  |
| 5 | Enter Date and Quantity Information | Fill in Date of Request as <tomorrow's date> and Quantity as it <matches the container’s capacity>.Choose Create.Note You can use the dropdown list to find the unit of measure for the Quantity. | The information is entered correctly, and the waste transfer request is created.You will be redirected to the My Waste Transfer Requests screen. |  |
| 6 | Note the Waste Transfer Request Number | On the My Waste Transfer Requests screen, look for the Waste Transfer Request you created.Note You can find the entry by filtering after Date, Product and/or Point of Generation.Write down its Number which has been automatically generated by the system.Note You will need this document Number for the next steps. | The Waste Transfer Request number is created automatically by the system and displayed on the screen.The transfer request created by the Production Operator can be taken over by the Environmental Manager. |  |
| 7 | Create Multiple Waste Transfer Requests | Repeat steps 3 - 6 and create two new Waste Transfer Requests with Date of Request <one month from tomorrow's date> and another with <one month previous from tomorrow's date> and Quantity <0,5 TO> and another with <1,2 TO>, respectively. | Two waste transfer requests are created. |  |
| 8 | Create a Waste Transfer Request by Copying an Existing Request | On the My Waste Transfer Requests screen, select the request you created in the previous steps, then choose Copy.On the Fill In Required Information (Date and Quantity) screen, enter the following:Date of Request: <one week from tomorrow's date>Quantity: <2 TO>Choose Create. | A new waste transfer request is created with the same point of generation, waste product, and unit of measurement as defined in the copied request.Note Waste transfer requests you create by copying are in New status regardless of the statuses of the copied requests.Note The Copy button is only active when one or more transfer requests are selected. |  |

#### Create a Waste Transfer Request by Copying an Existing Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Production Operator - EHS Info requests waste to be transferred from a point of waste generation to a storage location once the capacity of the container, which houses the waste, is reached.

Prerequisites

To perform this test procedure, you need to have at least one existing waste transfer request in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Waste Transfer Requests - Waste Management (F6083) app. | The My Waste Transfer Requests - Waste Management screen is displayed. |  |
| 4 | Create a Waste Transfer Request by Copying an Existing Request | On the My Waste Transfer Requests screen, select one or more waste transfer requests. Choose Copy. On the Fill required information (Date and Quantity) pop-up, fill in Date of Request as <tomorrow's date> and Quantity as it <matches the container’s capacity>. | A pop up screen will appear with the name Select Waste Streams. |  |

### Manage a Waste Transfer Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager monitors a transfer request created by a Production Operator - EHS Info. The waste is then posted for a waste storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Waste Transfer Requests - Waste Management (F6084) app. | The Manage Waste Transfer Requests screen is displayed. |  |
| 3 | Search for the Waste Transfer Request | On the Manage Waste Transfer Requests screen, choose Go to see all the transfer requests that have been created.Search for and select your newly created waste transfer request from the test procedure [Create a Waste Transfer Request](#unique_16) [page ] 23 by using one or more of the following in the search fields:Point of Waste Generation: Wiesbaden Laboratory and Production LineNumber: <document number>Note Use the saved document number you previously wrote down in the test procedure [Create a Waste Transfer Request](#unique_16) [page ] 23.Status: NewNote You can find the entry by filtering after Date of Request, Product and/or Point of Generation. | The selected waste transfer request is displayed. |  |
| 4 | Add a Disposal Channel | Choose Edit located on the top right of the selected waste transfer request screen.Select Disposal Channel HCl Wiesbaden into the Disposal Channel field.Note You can use the value help to search for the disposal channel.Then, choose Save. | A disposal channel was added to the waste transfer request. |  |
| 5 | Post Waste Transfer Request | On the same screen, choose Post.Note You can only post a waste transfer request if the quantity is greater than zero. | The status of the transfer request is changed to Posted which means the containers are already located in the storage location and are ready to be collected and transported to the disposal facility.If you have the necessary authorizations, a goods receipt (GR) is posted in Inventory Management, and the material document is displayed in the Reference Documents section of the Manage Waste Transfer Requests app.If you subsequently cancel the posting of the waste transfer request, the goods receipt is reversed.Note To be able to post material documents, you need to have a business user with the business catalog Materials Management - Warehouse Processing (SAP_MM_BC_IM_PROCESS_PC). This business catalog is assigned to the Inventory Manager (SAP_BR_INVENTORY_MANAGER) business role. |  |
| 6 | Add Disposal Channel and Change Status of Previously Created Waste Transfer Requests | Repeat steps 3 - 5 to add a disposal channel and change status to Posted for the other waste transfer requests previously created in the test procedure [Create a Waste Transfer Request](#unique_16) [page ] 23. | The previously created waste transfer requests have been updated. |  |

### Create a Waste Transportation Document from a Waste Transfer Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a legally compliant transportation document to dispose of a location's, classified as waste generator, waste.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the [Manage Waste Transfer Requests - Waste Management](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F6084) app. | The Manage Waste Transfer Requests screen is displayed. |  |
| 3 | Search for the Waste Transfer Request | On the Manage Waste Transfer Requests screen, search for and select your newly created Waste Transfer Request from the test procedure [Create a Waste Transfer Request](#unique_16) [page ] 23 by using one or more of the following in the search fields:Point of Waste Generation: Wiesbaden Laboratory and Production LineNumber: <document number>Note Use the saved document number you previously wrote down in the test procedure [Create a Waste Transfer Request](#unique_16) [page ] 23.Status: PostedNote You can find the entry by filtering after Date of Request, Product and/or Point of Generation. | The selected Waste Transfer Request is displayed. |  |
| 4 | Create a Waste Transportation Document from a Waste Transfer Request | On the selected Waste Transfer Request, choose Create New Transportation Document on the top right corner of the screen. | The Create Waste Transportation Documents screen of the app My Waste Transportation Documents (F5290) is displayed. |  |
| 5 | Review Basic Information, Permit, and Waste Generator of the Waste Transportation Document | On the Create Waste Transportation Document screen, review all data under the Basic Information, Permit, and Waste Generator tabs.All data is selected automatically from the selected Waste Transfer Request and its associated Disposal Channel.Note Under the tab Basic Information, the Handover Date is by default <today's date>.The Return By date is set automatically to 30 days after the Handover Date and cannot be edited. | Corresponding data from the selected Waste Transfer Request and its associated Disposal Channel is correctly assigned at the Basic Information, Permit and Waste Generator tabs. |  |
| 6 | Add Waste Product Information | On the Create Waste Transportation Document screen, under the Waste Product tab, enter the following information :Number of Packages: <1>Note The default information of the Product, Outgoing Quantity, and Unit comes from the selected Waste Transfer Request and is editable. | The information of the Waste Product is successfully updated. |  |
| 7 | Enter Waste Transporter | On the same screen, under the Waste Partner tab, under Waste Transporter, choose Create.Enter the following data:Name: Rhein Main Hazardous Materials TransportLicense Plate: WI 578Trailer Plate: WI 777Acceptance Date: <today's date>Contact Person: <your name>Signature Date: <today's date>Note The Acceptance Date associated with the transporter is the disposal pick-up date. | A transporter is added successfully. |  |
| 8 | Edit Waste Disposer Information | Under the Waste Partner tab, under Waste Disposer, enter the following data:Acceptance Date: <today's date>Contact Person: <your name>Signature Date: <six days from today's date>Note The Acceptance Date associated with the disposer is the handover date from the transporter to the disposer. | Additional waste partner disposer information is added. |  |
| 9 | Add Additional Information | Under the Additional Information tab, enter the following data:Remarks: Corrosive material. | The additional information is added successfully. |  |
| 10 | Save Waste Transportation Document | On the same screen, choose Create. | The Waste Transportation Document is created and saved. |  |
| 11 | Create Multiple Waste Transportation Documents | Repeat steps 2 - 10 with previously created Waste Transfer Requests with Handover Date <one month from tomorrow's date> and <two months from tomorrow's date> respectively.Make sure to fill all dates in the Waste Partner section based on the respective Handover Date. | Two new Waste Transportation Documents are created. |  |

### Generate a Waste Transportation Document Form

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager manages and generates a legally compliant form of a waste transportation document for a location, classified as a waste generator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the [My Waste Transportation Documents](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F5290) app. | The My Waste Transportation Documents screen is displayed. |  |
| 3 | Search for Previously Created Waste Transportation Document | On the My Waste Transportation Documents screen, search for the waste transportation document created in the test procedure [Create a Waste Transportation Document from a Waste Transfer Request](#unique_18) [page ] 28 by using one or more of the following the search fields:Waste Generator: Plant WiesbadenDisposal Facility: Wiesbaden Treatment Facility 1Document Type: E-BEGLEITSCHEINStatus: NewNote The Status in this app refers to the lifecycle of the transportation document and not of the waste transfer request.Select the entry. | The selected My Waste Transportation Document screen with the automatically generated document number is displayed. |  |
| 4 | Change Status of Waste Transportation Document | On the selected My Waste Transportation Document details screen, select Schedule Transportation located at the top right corner of the screen.Note Refresh your browser to successfully perform next steps. | The Status of the waste transportation document is changed from New to Transportation Scheduled. |  |
| 5 | Display Waste Transportation Document Form | On the same screen, navigate to the section Output Items and confirm that an item has been generated in Status: In Preparation.On the Display column of the section, choose Open File to generate a preview version of the waste transportation document form in PDF-format.Note If you are unable to see the Display column, choose the Show More per Row icon. | An Output Item entry has been successfully generated and a preview version of the waste transportation document is displayed in PDF-format. |  |
| 6 | Change Status of Multiple Waste Transportation Documents | Repeat steps 3 - 4 for the previously created waste transportation documents, but this time change the waste transportation document Status to Submitted and leave the other document in New.Note To change a waste transportation document into Status: Submitted, the document must first be changed to Status: Transportation Scheduled by selecting Schedule Transportation. Then Submit will become available.No PDF-form is generated for documents in Status: New. | The Status of the waste transportation document is updated. |  |

### Compare Waste Analytics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager performs a statistical analysis of several waste products disposed by using several transportation documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the [Waste Analytics](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F6956) app. | The Waste Analytics screen is displayed. |  |
| 3 | Filter Records by Handover Date | On the Waste Analytics screen, use the filter Handover Date to filter Items from <today's date> to <date two months from today>.Choose Go. | The Items of all products with transportation document Handover Date on this date period are displayed. |  |
| 4 | Filter Records by Waste Generator | Then, use the search field Waste Generator to search for and select Plant Wiesbaden.Choose Go. | The Items of all products from the Waste Generator Plant Wiesbaden are displayed. |  |
| 5 | Compare Sorted Records After Filtering Transportation Document Status | On the same screen, select the Settings icon and the column Transport Document Status.The three transportation documents previously created are now shown on the screen and can be compared. | The column Transportation Document Status is displayed and all Items are rearranged. |  |

### Import Waste Delivery Notes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

To perform this test procedure, you need to create a country/region-specific set of master data. Follow the steps in the related procedures.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Location | Plant Texas | Location of type Plant with the classifier Waste Generator.Parent location for all other sample locations. | Follow the instructions in the master data script 3SR - Create EHS Location. |
| Location | Texas Laboratory and Production Line | Location of type Production Unit with the classifier Point of Generation.Sublocation of Plant Texas. | Follow the instructions in the master data script 3SR - Create EHS Location. |
| Location | Texas Storage Building | Location of type Storage Location with the classifier Waste Storage.Sublocation of Plant Texas. | Follow the instructions in the master data script 3SR - Create EHS Location. |
| Product | Office Paper | Product. | Follow the instructions in the master data script 660 - Create an EHS Product. |
| Waste Material | Office Paper | Waste Material with the logistics role Emissions Relevant, Disposed and Transported. | Follow the steps in [Create a Material (Import Delivery Notes)](#unique_27) [page ] 36. |
| Business Partner | Texas Inc. | (Waste) Business Partner with the role Disposer. | Follow the instructions in the master data script 22G - Create Business Partner for Treasury and Risk Management.Follow the steps in this procedure: [Create a Disposer (Import Delivery Notes)](#unique_28) [page ] 37 |
| Business Partner | Houston Materials Transport | (Waste) Business Partner with the role Transporter. | Follow the instructions in the master data script 22G - Create Business Partner for Treasury and Risk Management.Follow the steps in this procedure: [Create a Transporter (Import Delivery Notes)](#unique_29) [page ] 39. |
| Waste Stream |  |  | Follow the steps in [Create a Waste Stream (Import Delivery Notes)](#unique_30) [page ] 40. |
| Waste Disposal Channel |  |  | Follow the steps in [Create a Disposal Channel (Import Delivery Notes)](#unique_31) [page ] 41. |

Procedure

The Environmental Manager imports waste delivery notes into the system.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Import Waste Documents - Delivery Notes (F7338) app. | The Import Waste Documents - Delivery Notes screen is displayed. |  |
| 3 | Download Template | On the Import Waste Documents - Delivery Notes screen, choose Import Delivery Notes.In the Import Delivery Notes dialog, choose the Download template file for import link. Save the file and extract the template to your computer. | You have downloaded the template to your computer. |  |
| 4 | Fill in the Import Template | In the import template, enter the following information:Waste Stream Handling: OBWSPoint of Generation ID: Texas Laboratory and Production LineWaste Material ID: Enter the internal name of the material. You can find it in the Manage Material Data app.Quantity: 10UoM: TODate of Request: <today's date>Transportation Document Number: 1111The number must not exist in the system already.Waste Generator ID: Plant TexasBusiness Partner ID: Enter the business partner ID of the disposer. You can find it in the My Transporters and Disposers app.Waste Transporter ID: Enter the business partner ID of the transporter. You can find it in theMy Transporters and Disposers app.Disposal Facility ID: Enter the name of the disposal facility. You can find it in the My Transporters and Disposers app.Waste Code: D001License Plate: TstPlt1Handover Date: <today's date>Save your changes. | You have entered the data you want to import in the template. |  |
| 5 | Import the Template | On the Import Waste Documents - Delivery Notes screen, choose Import Delivery Notes.In the Import Delivery Notes dialog, choose Browse... and find the template you filled in.Choose Import. | The data from the template is imported into the system. |  |
| 6 | Display Imported Documents | On the Import Waste Documents - Delivery Notes screen, choose Go.From the results list, select the document you imported. | The imported data is displayed. |  |
| 7 | Delete Imported Delivery Notes | Navigate back to the Import Waste Documents - Delivery Notes screen and select the previously created record.Choose Delete. | The record is deleted from the Imported Delivery Notes list. The statuses of the related waste transportation document and waste transfer request that were created during the import are set to Historical. |  |

#### Create a Material (Import Delivery Notes)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager defines the waste-related information of a material.

Procedure

|  |
| --- |
| Note This procedure is a prerequisite for [Import Waste Delivery Notes](#unique_21) [page ] 33. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the [Manage Material Data](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F4864) app. | The Manage Material Data screen is displayed. |  |
| 3 | Select a Material | On the Manage Material Data screen, select the material name Office Paper.Note You can use the search field to look for the material name. | The Material: Office Paper screen is displayed. |  |
| 4 | Select a Waste Type | Navigate to the Waste Data section.In the Waste Type field, select Non-Hazardous from the dropdown list. | The waste type Non-Hazardous is selected. |  |
| 5 | Maintain Waste Codes | In the Waste Data section, Waste Codes subsection, choose Manage Waste Codes. | The Manage Waste Codes screen is displayed. |  |
| 6 | Add Waste Codes | On the Manage Waste Codes screen, choose Edit.In the Waste Codes screen, choose Add.Search for the waste code D001 corresponding to Office Paper from the compliance requirement Title 40: Protection of Environment; PART 261 - IDENTIFICATION AND LISTING OF HAZARDOUS WASTE.Note You can use the value help provided in the Waste Code field.Choose Save and navigate back to the Manage Material Data screen. | The waste codes are added and the waste-related information for the material is saved. |  |

#### Create a Disposer (Import Delivery Notes)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a disposer which defines a business partner of type disposer and links it to a location, classified as a waste generator.

The Environmental Manager then names a disposal facility and assigns a waste material to it for later disposal.

|  |
| --- |
| Note This procedure is a prerequisite for [Import Waste Delivery Notes](#unique_21) [page ] 33. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open [My Transporters and Disposers - Waste Management](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F5222) app. | The My Transporters and Disposers screen is displayed. |  |
| 3 | Create Disposer | On the My Transporters and Disposers screen, choose Create -> Disposers. | The Create Disposer screen is now displayed. |  |
| 4 | Enter Waste Partner Data | On the Create Disposer screen, under the Waste Partner tab, enter the following data:Business Partner: Texas Inc.Waste Generator: Plant TexasNote You can use the value help to find the business partner and waste generator. | Waste partner data is entered. The Validity Area field is automatically filled based on the selection of the waste generator. |  |
| 5 | Enter Facilities Data | Under the Facilities tab, choose Add.On the Assign Facilities screen, use the value help to select an existing address and choose OK.Back on the Facilities tab, enter the following data:Facility Name: Texas Treatment Facility 1 | Facility data is added. |  |
| 6 | Enter Waste Material Data | Under the Waste Materials tab, choose Add.On the Assign Waste Material screen, select Office Paper and choose OK.Back on the Waste Materials tab, enter the following data:Facility Assigned: Texas Treatment Facility 1 | Waste material data is added. |  |
| 7 | Save Disposer | On the My Transporters and Disposers screen, at the bottom right corner of the screen, choose Create. | The disposer is created. |  |

#### Create a Transporter (Import Delivery Notes)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a transporter which defines business partner of type transporter and links it to a location, classified as a waste generator.

The Environmental Manager then assigns a waste material to be transported to a disposal facility.

Procedure

|  |
| --- |
| Note This procedure is a prerequisite for [Import Waste Delivery Notes](#unique_21) [page ] 33. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open [My Transporters and Disposers - Waste Management](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F5222) app. | The My Transporters and Disposers screen is displayed. |  |
| 3 | Create a Transporter | On My Transporters and Disposers screen, choose Create -> Transporter. | The Create Transporter screen is displayed. |  |
| 4 | Enter Waste Partner Data | On the Create Transporter screen, under the Waste Partner tab, enter the following data:Business Partner: Houston Materials TransportWaste Generator: Plant TexasNote You can use the value help to find the Business Partner and Waste Generator. | Waste partner data is entered.The Waste Registration Number field is filled based on the selection of business partner.The Validity Area field is filled based on the selection of waste generator. |  |
| 5 | Enter Waste Material Data | Under the Waste Materials tab, choose Add.On the Assign Waste Material screen, select Office Paper and choose OK. | Waste material data is added. |  |
| 6 | Save Transporter | On the My Transporters and Disposers screen, at the bottom right corner of the screen, choose Create. | The transporter is created. |  |

#### Create a Waste Stream (Import Delivery Notes)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a waste stream which represents allocation of waste material to a point of waste generation inside a location, classified as a waste generator.

Procedure

|  |
| --- |
| Note This procedure is a prerequisite for [Import Waste Delivery Notes](#unique_21) [page ] 33. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open [My Waste Streams - Waste Management](https://sapdev.accounts.ondemand.com/saml2/idp/sso/sapdev.accounts.ondemand.com) (F5410). | My Waste Streams screen is displayed. |  |
| 3 | Create Waste Stream | On the My Waste Streams screen, choose Create. | The Waste Stream screen is now displayed. |  |
| 4 | Enter Waste Stream Data | On the Waste Stream screen, under the Waste Stream tab, enter the following data:Waste Stream Name: Waste Stream Paper TexasWaste Stream Handling: Outbound - With Storage Location (OBWS)Product: Office PaperNote The product is associated with the waste generator Plant Texas.Waste Storage Location: Texas Storage BuildingNote You can use the value help to find the Product and the dropdown lists to find the Waste Stream Handling and Waste Storage Location. | Waste stream data is entered.The Waste Codes field is filled based on the selection of the product. Waste codes were assigned to the material in the Manage Material Data app.The Waste Generator and Validity Area fields are automatically filled based on the assignment of material to waste generator in the My Transporters and Disposers - Waste Management app. |  |
| 5 | Enter Point of Waste Generation Data | Under the Point of Waste Generation tab, choose Add.Enter the following data:Location: Texas Laboratory and Production LineNote You can use the dropdown list to find the location.Unit of Measure: TO | Point of waste generation data is added. |  |
| 6 | Create Waste Stream | On the Waste Stream screen, at the bottom of the screen, choose Create. | The Waste Stream is created. This is the base for the creation of transfer requests. |  |

#### Create a Disposal Channel (Import Delivery Notes)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a disposal channel which links a predefined waste stream to a predefined disposal facility.

The Environmental Manager also selects the waste transportation document type which defines the conditions on how and how much waste will be transported and disposed.

|  |
| --- |
| Note The waste transportation document types available depend on your country/region. |

Procedure

|  |
| --- |
| Note This procedure is a prerequisite for [Import Waste Delivery Notes](#unique_21) [page ] 33. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Waste Disposal Channels – Waste Management app. | The My Waste Streams screen is displayed. |  |
| 3 | Create Disposal Channel | On the Manage Waste Disposal Channels screen, choose Create. | The New: Disposal Channel screen is displayed. |  |
| 4 | Enter Disposal Channel Data | On the Basic Information tab, enter the following data:Disposal Channel Name: Disposal Channel Paper TexasDisposal Facility: Texas Treatment Facility 1Transportation Document Type: WASTE DELIVERY NOTES (S_WDN)Note The list of Transportation Document Types depends on the country/region of where the Waste Generator, associated to the Disposal Facility selected, is located. | Basic waste disposal channel data is added. |  |
| 5 | Enter Waste Stream Information | Under the Waste Streams tab, choose Add.In the Waste Stream Name field, use the value help to search for and select Waste Stream Paper Texas. | Waste Stream information is added. |  |
| 6 | Create Disposal Channel | Choose Create at the bottom right corner of the screen. | The Waste Disposal Channel is created. |  |
| 7 | Activate Disposal Channel | On the same screen, choose Activate on the top right corner. | The Waste Disposal Channel is activated and is the starting point for creating a transportation document to a disposal facility. |  |

### Delete Waste Delivery Notes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager deletes waste delivery notes.

Prerequisites

To perform this test procedure, you need to have one or more waste delivery note records with status Imported in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Import Waste Documents - Delivery Notes (F7338) app. | The Import Waste Documents - Delivery Notes screen is displayed. |  |
| 3 | Select waste delivery note records | On the Import Waste Documents - Delivery Notes screen, select one or more existing waste delivery note records that you wish to delete.Choose Delete. | The waste delivery notes are deleted and disappear from the Imported Delivery Notes overview. Their related waste transportation documents and waste transfer requests that were created during the import of the notes are set to status Historical. |  |

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
- see-also :: [[13-quality-ehs-and-compliance/stammdatenskript-informationsmaterial-fur-chemische-compliance-ehs-anl]]
- see-also :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/60H_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 80,499 chars in the whole document
