---
id: 15-retail-operations/sites-for-retail-3i3-ae-test-script-sap-s-4hana-cloud-public-edition-9
title: "Sites for Retail (3I3_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3I3_S4CLD2608_BPD_EN_AE)"
description: "AE-localized test script for scope item 3I3 Sites for Retail in S/4HANA Cloud Public Edition 2608: creating DC/store sites, business partners, site groups, copy and blocking."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-sites-partners-and-assortments]
aliases: [3I3_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Sites, Business Partners and Assortments", retail site master data, retail site creation, site business partner, business partner roles, merchandise categories, site groups, copy master data, test scripts, supplier master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I3_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-943
topic: 15-retail-operations/retail-sites-partners-and-assortments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sites for Retail (3I3_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3I3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Sites, Business Partners and Assortments** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sites for Retail (3I3_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sites for Retail (3I3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852856)

[2 Prerequisites 4](#_Toc232852857)

[2.1 System Access 4](#_Toc232852858)

[2.2 Roles 4](#_Toc232852859)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852860)

[2.4 Business Conditions 6](#_Toc232852861)

[2.5 Preliminary Steps 7](#_Toc232852862)

[2.5.1 Create Retail Sites 7](#_Toc232852863)

[2.5.1.1 Create Retail Sites – Distribution Center 7](#_Toc232852864)

[2.5.1.2 Create Retail Sites - Store 12](#_Toc232852865)

[2.5.2 Define Groupings and Assign Number Ranges 15](#_Toc232852866)

[3 Overview Table 17](#_Toc232852867)

[4 Test Procedures 19](#_Toc232852868)

[4.1 Create and Assign Business Partner to Site 19](#_Toc232852869)

[4.2 Maintain Site Data for Distribution Center and Store 24](#_Toc232852870)

[4.3 Maintain Merchandise Category and Supplying Site 25](#_Toc232852871)

[4.3.1 Assign Merchandise Category to Site (Optional) 25](#_Toc232852872)

[4.3.2 Assign Supplying Plant to Site (Optional) 28](#_Toc232852873)

[4.4 Manage Site Group 30](#_Toc232852874)

[4.4.1 Create Site Group 30](#_Toc232852875)

[4.4.2 Assign Sites to Site Group 31](#_Toc232852876)

[4.5 Create/Update Business Partner for Distribution Centre/Store 32](#_Toc232852877)

[4.5.1 Create/Update DC/Store Business Partner General Data 32](#_Toc232852878)

[4.5.2 Create/Update DC/Store Business Partner Supplier Master Data - Company Code Data 34](#_Toc232852879)

[4.5.3 Create/Update DC/Store Business Partner Supplier Master Data – Purchasing Organization Data 35](#_Toc232852880)

[4.6 Create/Update Business Partner for Distribution Centre (DC) 37](#_Toc232852881)

[4.6.1 Create/Update DC Business Partner Customer Master Data - Sales Area Data 37](#_Toc232852882)

[4.7 Create/Update Business Partner for Store 40](#_Toc232852883)

[4.7.1 Create/Update Store Business Partner Customer Master Data - Company Code Data 40](#_Toc232852884)

[4.7.2 Create/Update Store Business Partner Customer Master Data - Sales Area Data 41](#_Toc232852885)

[4.8 Assign Existing Business Partner to Site 44](#_Toc232852886)

[4.9 Copy Master Data and Verification 45](#_Toc232852887)

[4.9.1 Copy Master Data 46](#_Toc232852888)

[4.9.2 Check Logs 47](#_Toc232852889)

[4.9.3 Display Factsheet 48](#_Toc232852890)

[4.9.4 Verify Site Assignment to Store Group 49](#_Toc232852891)

[4.10 Maintain Site Blocking Information 50](#_Toc232852892)

## Purpose

Overview

This scope item describes how location master data can be maintained. In Retail, a location is typically referred to as a site and comes in one of two variations: store or distribution center.

A store serves the main purpose of presenting and selling merchandise to consumers. To enable this, additional planning and operational processes are needed, for example goods receipt and physical inventory counting. The task of a distribution center is handling the transfer of merchandise from external suppliers to stores along the supply chain as efficiently as possible. Parameters to be considered include, cost for procurement, transportation, and storing, as well as stock level agreements for stores, among others.

Depending on the detailed needs of a retailer, site-related processes need to be configured. The solution described in this scope item provides an easy way to maintain respective site data. Like other organizational data, sites are maintained using SAP Central Business Configuration.

For ease of maintenance purposes, a defaulting mechanism prefills many parameters, so they don't need to be maintained by the user.

Having consistent and high-quality site master data is crucial for ensuring reliable and smooth operation. SAP supports this by providing a quality assurance environment for testing and by ensuring consistent data replication to the productive environment.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Location Data (Retail) | SAP_BR_MD_SPCLST_SITE_RFM | Site Master Data |  |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration |  |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

- The site master data consist of the following:
- General/additional site data
- Business partner data including
    - Address data
    - Supplier data (site in its capacity as a supplier)

Customer data (site in its capacity as a customer)

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purchase Organization 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Retail Store (Site) | 3340 | Store 3340 AE |  |
| Retail Store (Site) | 3341 | Store 3341 AE |  |
| Retail Store (Site) | 3342 | Store 3342 AE |  |
| Retail Store (Site) | 3343 | Store 3343 AE |  |
| Retail Store (Site) | 3344 | Store 3344 AE |  |
| Retail Distribution Center (DC) | 3350 | DC 3350 AE |  |
| Division | 00 | Product Division 00 |  |
| Distribution Channel | 40 | Store Sales |  |
| Distribution Channel | 50 | Distribution |  |
| Distribution Channel | 10 | Direct Sales |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Storage Location | 995R | St.Loc.Return |  |
| Storage Location | 995W | St.Loc. EWM DC |  |
| Storage Location | 991K | 3rd Party WMS Return DC |  |
| Storage Location | 99IL | Storage Location 3rd Party |  |
| Merchandise Category | R1111001R1111002R1111003R1151003 | Salmon, Trout & TunaCod & White FishSeafoodSalads |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNH – Create Profit Center - MDS | Assignment of profit center is necessary for accounting purpose. Profit center must exist before site creation. |

### Preliminary Steps

#### Create Retail Sites

Follow the subsequent steps to create retail sites for distribution centers and stores.

After you have completed creating sites and setting up organization structure, confirm the milestone Scope and Organizational Structure Phase Is Completed in the project experience in SAP Central Business Configuration.

After completing the activity, you proceed with the following configuration activities in the Business Processes Configuration app to configure your retail sites:

- Maintain Default Purchasing Organization for Retail Site
- Maintain Retail Site Parameters
- Assign Picking Locations
- Assign Shipping Points
- Assign Storage Location for Advanced Returns Management
- Assign Goods Receiving Points for Inbound Deliveries
- Assign Document Type, One-Step Procedure and Under-delivery Tolerance

|  |
| --- |
| Note For detailed information on configuration settings to be performed in SAP S/4HANA Cloud Public Edition, see Configuration Activities chapter in the Set Up Instructions attached to SAP Note [3313681](https://me.sap.com/notes/3313681). |

##### Create Retail Sites – Distribution Center

Use

To execute this scope item, you must have sites available for BP assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Choose Open for activity Set Up Organizational Structure under Scope and Organizational Structure. | The Set Up Organizational Structure activity screen opens. |  |
| 3 | Create Shipping Point | Choose Create.Select Shipping Point.Enter following data:ID: <Shipping Point ID- Standard>Name: <Shipping Point Name>City: <City>Subtype: Without Lead TimesCountry/Region: <pre-populated with the country for which you are creating the shipping point>, for example, US - USAChoose Create.Repeat above steps to create two more shipping points with the subtype Without Lead TimesID: <Shipping Point ID - Consignment>Name: <Shipping Point Name - Consignment>andID: <Shipping Point ID - Return>Name: <Shipping Point Name - Return | A message is displayed indicating organizational unit with site name is created successfully. |  |
| 4 | Create Cloud Warehouse | Prerequisite: Scope item Retail Logistics with Embedded Warehouse Management (69L) activated.Choose Create.Select Warehouse.Enter the following data:ID: <Warehouse ID>Name: <Warehouse Name>Subtype: Cloud WarehouseChoose Create.Select the tab Relations and choose Create Warehouse NumberID: <Warehouse ID>Name: <Warehouse Name>Choose Create. | A message is displayed indicating organizational unit with warehouse number is created successfully |  |
| 5 | Create Third Party Warehouse | Prerequisite: Scope item Retail Logistics with Embedded Warehouse Management (69L) activated.Choose Create.Select Warehouse.Enter the following data:ID: <Warehouse ID>Name: <Warehouse Name>Subtype: Third-Party Warehouse Management System IntegrationChoose Create. | A message is displayed indicating organizational unit with warehouse number is created successfully |  |
| 6 | Create Retail Site | Choose Create Retail Site under Organizational Structure section.Enter following data:ID: <Site ID>Name: <Site Name>City: <City>Subtype : Distribution CenterCountry/Region: <pre-populated with the country for which you are creating the retail site>, for example, US - USAChoose Create. | A message is displayed indicating organizational unit with site name is created successfully. |  |
| 7 | Assign Site to Shipping Point | Select tab Relations and choose Distribution Center to Shipping point w/o preconfigured Lead Times.Assign all 3 shipping points created before by using the button: Create AssignmentID: <Shipping Point ID- Standard>Name: <Shipping Point Name>ID: <Shipping Point ID - Consignment>Name: <Shipping Point Name - Consignment> andID: <Shipping Point ID - Return>Name: <Shipping Point Name – ReturnChoose Save. | A message is displayed indicating distribution center and shipping point without preconfigured lead times created successfully. |  |
| 8 | Assign Site to Purchasing Organization | Choose Distribution Center to Purchasing OrganizationChoose Create Assignment button. A pop-up with available purchasing organizations is displayed.Select purchasing organization.Choose Save. | A message is displayed indicating distribution center and purchasing org assignment created successfully. |  |
| 9 | Assign Site to Sales Organization and Distribution Channel | Choose Distribution Center to Sales Organization and Dist. channelChoose Create Assignment button. A pop-up with a drop down having list of available sales organization is displayed.Select sales organization < Sales Org.>Under section Assign Channels,Select (Store Sales, Ecommerce & Distribution, Standard-wholesale)Choose Save. | A message is displayed indicating relationship created successfully. |  |
| 10 | Create Storage Location | Choose Create Storage Location under Retail Site - Distribution Center section.Enter following data:ID: 995AName: <Storage location DC>City: <City>Subtype: Standard Storage Location for Finished GoodsCountry/Region: <pre-populated with the country for which you are creating the retail site>, for example, US - USAChoose Create.Choose Create Storage Location under Retail Site - Distribution Center section.Enter following data:ID: 995RName: <Storage location Return>City: <City>Subtype: ReturnCountry/Region: <pre-populated with the country for which you are creating the retail site>, for example, US - USAChoose Create.Note Same storage location ID should be assigned to cross-stores and cross country. | A message is displayed indicating organization unit storage location created successfully. |  |
| 11 | Create Storage Location Embedded Warehouse Management | Prerequisite: Scope item Retail Logistics with Embedded Warehouse Management (69L) activated.Choose Create Storage Location under Retail Site - Distribution Center section.Enter following data:ID: 995WName: < Storage Location EWM >City: <City>Subtype: WarehouseCountry/Region: <pre-populated with the country for which you are creating the retail site>, for example, US - USAChoose Create.Select tab Relations and choose Warehouse to Cloud Warehouse.Choose Create Assignment button. A pop-up with available warehouses is displayed.Select Cloud Warehouse created in above section.Choose Save.Note Same storage location ID should be assigned to cross-stores and cross country. | A message is displayed indicating organization unit storage location created successfully. |  |
| 12 | Create Storage Location Third Party Warehouse Management | Prerequisite: Scope item Retail Logistics with Third-Party Warehouse Management (69M) activatedChoose Create Storage Location under Retail Site - Distribution Center sectionEnter following data:ID: 99IL/<use your own storage location>Name: < Storage Location 3rd Party >City: <City>Subtype: 3rd Party WMSCountry/Region: <pre-populated with the country for which you are creating the retail site>, for example, US - USAChoose Create.Select tab Relations and choose 3rd Party WMS to Third Party WarehouseChoose Create Assignment button. A pop-up with available warehouses is displayed.Select Third Party Warehouse created in above section.Choose Save.Choose Create Storage Location under Retail Site - Distribution Center section.Enter following data:ID: 991KName: < Storage Location 3rd Party Return >City: <City>Subtype: 3rd Party WMS ReturnCountry/Region: <pre-populated with the country for which you are creating the retail site>, for example, US - USAChoose Create.Select tab Relations and choose 3rd Party WMS to Third Party Warehouse.Choose Create Assignment button. A pop-up with available warehouses is displayed.Select Third Party Warehouse created in above section.Choose Save.Note Same storage location ID should be assigned to cross-stores and cross country. | A message is displayed indicating organization unit storage location created successfully. |  |
| 13 | Navigate to main screen | Choose Back to Overview button. | Organizational structure set up screen is displayed. |  |
| 14 | Assign Distribution Center to Sales Area | Select Sales Area box that has attribute Sales Area Type as “Distribution Center Business”For example. 3310\|50\|00Select tab Relations and click on Sales Area to Distribution CenterChoose Create Assignment button.A popup window Sales Area to Distribution Center is shown with available Distribution Centers for assignmentSelect radio button for your distribution center and choose Save.Assign Distribution Center: <your Distribution Center ID> | A message is displayed indicating sales area distribution center relationship created successfully |  |
| 15 | Confirm Changes | Choose Confirm button at top right section of page.A pop-up with details of all the assignments done above is displayed.Select check box before Organizational Unit Name.Choose Confirm. | All assignment are saved successfully. |  |

Result

You have created site and further assignment can be done using this.

##### Create Retail Sites - Store

Use

To execute this scope item, you must have sites available for BP assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Choose activities for phase as Scope and Organization and Open Set Up Organizational Structure app |  |  |
| 3 | Create Retail Site | Select Create Retail Site,Enter following data:ID: <Site ID>Name: <Site Name>Subtype : <Store>Country/Region will be pre-populatedEnter Address details:Street: <Street>House Number: <House Number>Postal Code: <Postal Code>City: <City>Select Create. | A message is displayed indicating organizational unit with site name created successfully. |  |
| 4 | Assign Site to Shipping Point | Select tab Relations and click on Store to Shipping point w/o preconfigured Lead Times.Select Create Assignment Button, A pop-up will be displayed with number of shipping points available.Select shipping point. (SP store <>)Select Save.To Assign more shipping point click on Create Assignment button again and select another shipping point. (SP Store Click & Collect)Note Click & collect Shipping point should be assigned to cross-stores and cross country.Standard shipping point should be assigned to cross stores within a country. | A message is displayed indicating store and shipping point without preconfigured lead times created successfully” |  |
| 5 | Assign Site to Purchasing Organization | Click on Store to Purchasing OrganizationSelect Create Assignment Button, A pop-up will be displayed with available purchasing organization.Select purchasing organization <Purchasing Organization>Select Save. | A message is displayed indicating store and purchasing org assignment created successfully. |  |
| 6 | Assign Site to Sales Organization and Distribution Channel | Click on Store to Sales Organization and Dist. channelSelect Create Assignment Button, A pop-up will be displayed with a dropdown having list of available sales organization.Select sales organization < Sales Organization>Under section Assign Channels,Select (Store Sales, Ecommerce & Distribution)Select Save. | A message is displayed indicating relationship created successfully. |  |
| 7 | Create Storage Location | Select Create Storage Location,Enter following data:ID: 994AName: <Standard Storage Location>Subtype: Allow Negative StockEnter Address details:Country/Region will be pre-populatedStreet: <Street>House Number: <House Number>Postal Code: <Postal Code>City: <City>Select Create.Note Same storage location ID should be assigned to cross-stores and cross country. | A message is displayed indicating organization unit Storage location created successfully. |  |
| 8 | Navigate to main screen | Select Back to Overview button | Organizational structure set up screen is displayed |  |
| 9 | Assign Store to Sales Area | Select Sales Area box that has attribute Sales Area Type as “Stores”for example: 3310\|40\|00Select tab Relations and click on Sales Area to StoreSelect Create Assignment buttonA popup window Sales Area to Store is shown with available stores for assignmentChoose radio button for your Store and select button SaveAssign Store: <your Store ID> | A message is displayed indicating sales area store relationship created successfully. |  |
| 10 | Confirm changes | Select Confirm button at top right section of page.A pop-up would appear having details of all assignment done above.Select check box before Organizational Unit NameSelect Confirm. | All assignment are saved successfully. |  |

Result

You have created Site and further assignment can be done using this.

#### Define Groupings and Assign Number Ranges

Use

Business partner groupings determine the number ranges for the business partner IDs. You cannot change the assignment or IDs later.

|  |
| --- |
| Note SAP recommends using external number range grouping and business partner ID must be created same as site ID. The site ID must not exceed more than four characters. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to Configuration Activities | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Groupings and Assign Number Ranges.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Groupings and Assign Number Ranges screen is displayed. |  |
| 3 | Configuration Define Groupings and Assign Number Ranges | Create the following settings:There are three grouping available for Site:S100 (Site Numeric): Number range 01 is assignedS101 (Site Num/ Alpha): Number range 04 is assignedS102 (Site Alpha/Num): Number range AB is assigned | Data is saved. |  |

Result

You have defined your settings for business partner groupings and number ranges.

## Overview Table

This scope item consists of several process step provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create and Assign Business Partner to Site](#unique_12) [page ] 19 | Master Data Specialist - Location Data (Retail) | Maintain Retail Site (F5375) | Business partner is assigned to site. |
| [Maintain Site Data for Distribution Center and Store](#unique_13) [page ] 24 | Master Data Specialist - Location Data (Retail) | Maintain Retail Site (F5375) | Necessary site data can be saved for store or distribution center. |
| Maintain Merchandise Category and Supplying Site |  |  |  |
| [Assign Merchandise Category to Site (Optional)](#unique_14) [page ] 25 | Master Data Specialist - Location Data (Retail) | Maintain Retail Site (F5375) | Merchandise category is assigned to site |
| [Assign Supplying Plant to Site (Optional)](#unique_15) [page ] 28 | Master Data Specialist - Location Data (Retail) | Maintain Retail Site (F5375) | Supplying site is assigned to store. |
| Manage Site Group |  |  |  |
| [Create Site Group](#unique_16) [page ] 30 | Master Data Specialist - Location Data (Retail) | Create Store Group (WB80) | Store group is created. |
| [Assign Sites to Site Group](#unique_17) [page ] 31 | Master Data Specialist - Location Data (Retail) | Maintain Stores in Store Group (WB86) | Site is assigned to store group |
| [Create/Update Business Partner for Distribution Centre/Store](#unique_18) [page ] 32 |  |  |  |
| [Create/Update DC/Store Business Partner General Data](#unique_19) [page ] 32 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Business Partner - General Data is created. |
| [Create/Update DC/Store Business Partner Supplier Master Data - Company Code Data](#unique_20) [page ] 34 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Supplier master – Company code data is created. |
| [Create/Update DC/Store Business Partner Supplier Master Data – Purchasing Organization Data](#unique_21) [page ] 35 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Supplier Master - Purchasing Organization Data is created. |
| Create/Update Business Partner for Distribution Centre (DC) |  |  |  |
| [Create/Update DC Business Partner Customer Master Data - Sales Area Data](#unique_22) [page ] 37 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Customer master - sales area data is created. |
| Create/Update Business Partner for Store |  |  |  |
| [Create/Update Store Business Partner Customer Master Data - Company Code Data](#unique_23) [page ] 40 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Customer Master - Company Code data is created. |
| [Create/Update Store Business Partner Customer Master Data - Sales Area Data](#unique_24) [page ] 41 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Customer master - Sales Area data is created. |
| [Assign Existing Business Partner to Site](#unique_25) [page ] 44 | Master Data Specialist - Business Partner Data | Maintain Retail Site (F5375) | Business partner is assigned to site |
| [Copy Master Data and Verification](#unique_26) [page ] 45 |  |  |  |
| [Copy Master Data](#unique_27) [page ] 46 | Master Data Specialist - Location Data (Retail) | Maintain Retail Site (F5375) | Master data is copied from one plant to another. |
| [Check Logs](#unique_28) [page ] 47 | Master Data Specialist - Location Data (Retail) | Maintain Retail Site (F5375) | Log can be analyzed |
| [Display Factsheet](#unique_29) [page ] 48 | Master Data Specialist - Location Data (Retail) | Site (F0335A) | Stored information is displayed |
| [Verify Site Assignment to Store Group](#unique_30) [page ] 49 | Master Data Specialist - Location Data (Retail) | Display Stores in Store Group (WB89) | Sites belong to group is displayed |
| [Maintain Site Blocking Information](#unique_31) [page ] 50 | Master Data Specialist - Location Data (Retail) | Maintain Retail Site (F5375) | Site is blocked |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create and Assign Business Partner to Site

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step provides instructions for assigning business partner to site.

These are the following options provided:

Procedure: Option 1 - Create and Assign Business Partner using Maintain Retail Site App

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed. |  |
| 3 | Use Filter | Enter below data in the filter:Site: <DC/Store ID>Business Partner Status: Not MaintainedSelect Go. | Site is displayed with business partner not maintained. |  |
| 4 | Select Site | Select the site | Maintain Master Data page opens and in the header below information is displayed:Business Partner Status: Not MaintainedCategory: Distribution Center/Store. |  |
| 6 | Maintain Business Partner | Select Edit and go to Business Partner section.Enter Business partner ID.Note SAP strongly suggests to create business partner ID same as Site ID. Please consider that the site ID is only maximum four characters long. | Business partner is created for site with required role. |  |
| 7 | Maintain Valuation/Inventory Management | Go to section Maintain Valuation/Inventory ManagementEnter existing Profit Center directly or select using F4 help. |  |  |
| 8 | Save | Select Save. | Business partner and profit center assigned successfully to site. |  |
| 9 | Verify Business partner | Select the business partner created in above step.Different options will be displayed, select Business Partner MasterBusiness Partner app will be opened in display mode.Note In this section business partner is created only with minimum required roles, further master data for business partner is not yet filled here. To complete the business partner master data, please refer chapter [Create/Update Business Partner for Distribution Centre/Store](#unique_18) [page ] 32. | Verify business partner is created with all necessary details. |  |

Procedure: Option 2 - Create and Assign Business Partner by Navigating to Maintain Business Partner app from Maintain Retail Site app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed. |  |
| 3 | Use Filter | Enter below data in the filter:Site: <DC/Store ID>Business Partner Status: Not MaintainedSelect Go. | Site is displayed with business partner not maintained. |  |
| 4 | Select Site | Select site | Maintain master data page opens and in the header below information will be displayed.Business Partner Status: Not MaintainedCategory: Distribution Center/Store. |  |
| 5 | Maintain Business Partner | Select Edit and click Create Business PartnerA pop-up with business partner ID is displayedNote Business partner ID is same name as that of site ID, in case if business partner already exists with same ID then pop up is blank and user needs to enter business partner ID.Select OK.Manage Business Partner app is opened, and Create Organization pop up is displayed, enter below information:General Information:TitleName 1Standard Address:StreetHouse NumberCityPostal CodeCountry/RegionLanguageSelect OK.New business partner page is opened, and above values are copied to respective fields.Go to section Roles , enter required supplier and customer roles based on retail site type:There are two ways in which roles can be added:Option 1: Using Create buttonFor distribution center / store, select Create and add below rolesBPSITE: Retail SiteFLVN00: Supplier (Fin.Accounting)FLVN01:SupplierFLCU00: Customer (Fin.Accounting)FLCU01: CustomerOption 2: Using Create with Reference buttonClick Create with Reference, a pop-up will open up. Enter below details:Business Partner: <Reference BP for DC/Store>Role: In role field, click on the option button, a new pop-up will open with all available roles, Select all & click on Select and then select Copy,Select Create, Confirmation message appears “Master data record created”.Select Back button twice to reach Maintain Retail Site screen.Enter Business Partner IDNote While using Customer Role (FLCU01) and Supplier Role (FLVN01), DO NOT enter Site number in the plant field.Note SAP strongly suggests to create Business Partner ID same as Site ID. Please consider that the site ID is only maximum 4 characters long. | Business partner is created for site with required role and these fields are updated in the system. |  |
| 6 | Maintain Valuation/Inventory Management | Go to Maintain Valuation/Inventory Management.Enter existing profit center directly or select using F4 help. |  |  |
| 7 | Save | Select Save | Business Partner and profit center assigned successfully to site. |  |
| 8 | Verify Business partner | Select the business partner created in above step.Different options are displayed, select Business Partner Master.Maintain Business Partner app opens in display mode.Note In this section business partner is created only with minimum required roles; further master data for business partner is not yet filled here. To complete the business partner master data, refer to chapter [Create/Update Business Partner for Distribution Centre/Store](#unique_18) [page ] 32. | Verify business partner is created with all necessary details. |  |

Procedure: Option 3 - Create and Assign Business Partner using Copy Master Data

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed. |  |
| 3 | Copy Site Master Data | Select Copy Master Data, a pop-up is opened with different selection criteria:There are two options available :Individual Entries: Enter following data:Source Site <Site ID of completed Site> e.g. 1050 for DC Germany, 1040 for Store GermanyTarget Site < New Site ID from step 3 above>Value Range: Enter following data:Enter Source Site < Site ID of completed Site > e.g. 1050 for DC Germany, 1040 for Store GermanyRange of Target Site < New Site ID’s from step 3 above > in From and To.You can also select specific data to copy from source to target site:Master DataOpening and Closing TimeMerchandise CategoriesSupplying SitesClassfication DataProfit CenterBusiness Partner DataCustomer Sales Organization DataCustomer Company Code DataSupplier Company Code DataSupplier Purchasing Organization DataSelect OK. | BP will be created and assigned to target Site. |  |

### Maintain Site Data for Distribution Center and Store

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains you how to maintain site data for distribution center and store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed. |  |
| 3 | Use Filter | Enter below data in the filter :Site: <DC/Store ID>Business Partner Status: MaintainedSelect Go. | Site is displayed with business partner maintained. |  |
| 4 | Select Site | Select the site. | Maintain Master Data page opens and in the header below information is displayedBusiness Partner Status: MaintainedCategory: Distribution Center/Store |  |
| 5 | Site Information | Basic details about site is available in Site Information section as follows:SiteCompany CodePurchasing OrganizationSales OrganizationDistribution ChannelDivisionPlant ProfileCalendarPurchasing DataDistribution Profile (Currently not supported)ListingPOS (only relevant for stores) |  |  |
| 7 | Maintain Opening and Closing Dates | Select Edit and go to section Opening and Closing Dates.Enter below information:Opening DateClosing Date |  |  |
| 8 | Maintain Opening and Closing Time | Go to section Opening and Closing Times.There are two ways to maintain:Enter Time Key and time is updated for each weekday accordingly.Keep Time Key field empty and enter opening and closing time manually for each day. |  |  |
| 9 | Save entries | Choose Save. | Site is getting saved with this data, opening and closing dates and opening and closing time. |  |

### Maintain Merchandise Category and Supplying Site

#### Assign Merchandise Category to Site (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign merchandise category to site. It can be done in one of the following two ways:

Procedure: Assign Merchandise Category using Maintain Retail Site application (Option 1).

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed. |  |
| 3 | Use Filter | Enter below data in the filter:Site: <DC/Store ID>Business Partner Status: MaintainedChoose Go. | Site is displayed with business partner status maintained |  |
| 4 | Select Site | Select the Site. | Maintain Master Data page opens and in the header below information is displayed:Business Partner Status: MaintainedCategory: Distribution Center/Store. |  |
| 5 | Assign Merchandise Category | Select Edit and go to section Merchandise CategorySelect Create Page is redirected to enter further values:Merchandise CategoryProcurement ProfilePrice Incl.TaxReplenishment Requirement GroupRevaluation ProfilePrice list/itemSelect Apply, details are saved in draft and details screen of site is displayed.Select Save.Note Maintain data based on your requirement, for further details on each field see details below:Procurement Profile: Exceptions can be maintained at merchandise category level. It is not relevant for the current process scope.Price Incl.Tax: This can be set for POS system (only relevant for stores).Replenishment Requirement Group: It can be relevant for store replenishment process (only relevant for stores).Revaluation Profile: It determines the procedure used for revaluating stock at retail. Exceptions can be maintained at merchandise category level.Price list/item: Can be relevant for retail pricing (P1-P4)(only relevant for stores). | Merchandise category is assigned and saved successfully, |  |
| 6 | Assign Supplying Sites on Merchandise Category Level (Optional) | Supplying site can be assigned on each merchandise category level.Select Create . A new line will be added to enter further values:Supplying SiteValid FromValid ToPrioritySelect Apply , details are saved in draft and details screen of site is displayed.Select Save. | Store gets updated with supplying site information for merchandise categories successfully. |  |

Procedure: Assign Merchandise Category using Assign Merchandise Categories – Sites app (Option 2)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Assign Merchandise Categories - Sites (WB30N) app. | Maintain Merchandise Category / Site Assignment screen is displayed. |  |
| 3 | Use Filter | Enter below data in the initial screen:Selection Mode:Select by Merchandise CategorySelection Criteria:Customer Number for Site : <Customer number created> in chapter [Create and Assign Business Partner to Site](#unique_12) [page ] 19.Select Execute. |  |  |
| 4 | Assign Merchandise Category | Screen is divided in two sections.Left one shows all the available merchandise category and right-side section shows site information.Select the merchandise category from left section and drag and drop to right section of site where you want to assign merchandise category.Select Save. | Merchandise category is assigned, and site is expanded. |  |
| 5 | Mass Maintenance of Merchandise Category (Optional) | You can also maintain many merchandise categories to Site at the same time,Select more than one merchandise category and drag and drop to site (as mentioned above).To maintain additional data like Price Incl. tax, Revaluation Profile, Requirement group, procurement profile and price list, double click on the Site, screen will be enhanced with these fields along with assigned merchandise category in a tabular form.Note Maintain data based on your requirement, for further details on each field see details below:Procurement Profile: Exceptions can be maintained at Merchandise Category level . Not relevant for the current process scope .Price Incl.Tax: This can be set for POS system (only relevant for Stores).Replenishment Requirement Group: It can be relevant for store replenishment process (only relevant for Stores).Revaluation Profile: It determines the procedure used for revaluating stock at retail. Exceptions can be maintained at Merchandise Category level.Price list/item: Can be relevant for retail pricing (P1-P4)(Only relevant for Stores).Select Save. |  |  |

#### Assign Supplying Plant to Site (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign supplying site to store using Maintain Retail Site (F5375) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site screen is displayed. |  |
| 3 | Use Filter | Enter the following data:Site: <Store Id>Business Partner Status: MaintainedSelect Go | Site is displayed with business partner maintained |  |
| 4 | Select Site | Select a store. | Maintain Master Data page opens and in the header below information will be displayedBusiness Partner Status: MaintainedCategory: Store |  |
| 5 | Maintain Supplying Sites | Select Edit and go to section Supplying SitesSelect create, enter following data:Supplying Site (Distribution center)Valid FromValid ToPrioritySelect Save. | Store is updated with supplying site information successfully. |  |

### Manage Site Group

#### Create Site Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create store group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Create Store Group (WB80) app.. | The Create Store Group screen displays and pop-up is displayed to select Class Type. |  |
| 3 | Select Class Type | Select Class Type :‘030’ (Site Grouping)Select OK and select Create. | Create class screen is displayed. |  |
| 4 | Make entries | On the ‘Create Class’ (Screen), make the following entries and choose ENTER.:Class : <Class Name> |  |  |
| 5 | Fill the mandatory fields | On the Tab Basic Data, make the following entries:Description: <Description> |  |  |
| 6 | Save your entries | Select Save. | Store group created successfully |  |

#### Assign Sites to Site Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign sites to a class.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Stores in Store Group (WB86) app. | The Maintain Stores in Group screen displays and pop-up is displayed to select Class Type. |  |
| 3 | Select Class Type | Select Class Type‘030’ (Site Grouping).Press OK and select Maintain Plants in Class | Assign Objects/Classes to Class screen is displayed. |  |
| 4 | Make entries | On the ‘Assign Objects/Classes to Class’ (Screen)’, make the following entries:Class : <Class Name>(Site Group created in above step)Class Type : 030And select only new assignments .Select ‘Plant’ at the pop-up screen and select Continue. |  |  |
| 5 | Fill the fields | On Assignments screen, make the following entries:Customer Number Plant: <Site ID> |  |  |
| 6 | Save your entries | Select Save. | Assignment of site to a site group is successful. |  |

### Create/Update Business Partner for Distribution Centre/Store

By referring to above mentioned steps you can create business partner. However, the business partner master data is not filled with all the necessary information.

Follow the below sections to check the missing information and maintain them for the existing business partner as applicable.

Also, you can create Business Partner from Maintain Business Partner (BP) app and directly assign to a site using following Maintain Retail Site (F5375) app steps.

#### Create/Update DC/Store Business Partner General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for business partner general data.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | The Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Create a BP Organization | Choose Organization. | Create Organization is displayed. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID>Grouping for distribution centers:One of them must be selected based on new sites created<S100 Site Numeric>or <Site Numeric>S101 Site Numeric/Alpha or Site Numeric/AlphaS102 Site Alpha/Numeric or Site Alpha/NumericCreate in BP role: <BPSITE> or <Retail site>A pop-up will appear, click on Create button. |  |  |
| 5 | Enter Address Data | On the Address tab page in the Name section, enter the following data:Title: <Company>Name: <Name> |  |  |
| 6 | Enter Street Address Data | In the Standard Address section, enter the following data.Street/House Number:< Street/House Number>Postal Code: <Postal Code>City: <City>Country: <Country>Region: <Region>Timezone: <timezone> |  |  |
| 7 | Enter Search Term | On the Address tab page in the Search Term section, enter one or more search terms for the Supplier. |  |  |
| 8 | Enter Communication Data | On the Address tab page in the Communication section, enter the following data:Language: <Choose the preferred language of the Business Partner>Telephone: <phone number>E-Mail: <email address> |  |  |
| 9 | Enter Tax Data | On the Identification tab page in Tax Numbers section, enter the following data:Category:AE1Tax Number: AEXXXXXXXXX (Total length should be 11) |  |  |
| 10 | Save Your Data | Save your entries. | Business partner general data is created. Make a note of business partner ID for further use. |  |

#### Create/Update DC/Store Business Partner Supplier Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

You must complete, [Create/Update DC/Store Business Partner General Data](#unique_19) [page ] 32, procedure before proceeding with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | The Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Open BP | Choose Open BP button, enter BP ID created in above step.Choose Enter. | Business partner with general data maintained is displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. |  |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:Supplier (Financial Accounting)The technical key of this business partner role is FLVN00. |  |  |
| 6 | Open Company Code Data | Choose Company Code at the top of the screen. | Change Organization: <BP ID>, new role Supplier (Fin.Accounting) screen is displayed. |  |
| 7 | Enter Company Code | Select Company Codes a pop-up will open, Enter the following data:Company Code ID: 3310And then choose Adopt. |  |  |
| 8 | Enter Vendor Accounting Data | On the Vendor: Account Management tab page in the Account Management section, enter the following data:Reconciliation Account: <21100000> (Payables Domestic)Note There might be other G/L reconciliation accounts for foreign suppliers or affiliates. |  |  |
| 9 | Enter Vendor Payment Data | On the Vendor: Payment Transactions tab page in the Payment Data section, make the following entry:Terms of Payment |  |  |
| 10 | Save Your Data | Save your entries. | Company code details saved successfully. |  |

#### Create/Update DC/Store Business Partner Supplier Master Data – Purchasing Organization Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating supplier master purchasing organization data.

Prerequisite

You must complete the previous section, [Create/Update DC/Store Business Partner General Data](#unique_19) [page ] 32, before you proceed with this section.

Begin the procedure after you have saved data entries, as described in the previous procedure.

|  |
| --- |
| Note While using Supplier Role (FLVN01), DO NOT enter Site number in the plant field under Supplier: General Data tab. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | The Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Open BP | Choose Open BP button, enter business partner ID created in above step.Select ENTER. | Business partner with general data maintained is displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. | The Change mode screen is displayed. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:SupplierNote The technical key of this BP role is FLVN01 |  |  |
| 6 | Open Purchasing Organization Data | Choose Purchasing at the top of the screen. | Change Organization: <BP ID>, new role supplier screen is dispalyed. |  |
| 7 | Enter Purchasing Data | Select Purchasing Organizations,Enter the following data:POrg: 3310And then choose Enter. |  |  |
| 8 | Enter Purchasing Data | On the Purchasing Data tab page in the Conditions section, enter the following data:Order Currency: AEDPayment Terms |  |  |
| 10 | Enter Purchasing Data | On the Purchasing Data tab page in the Additional Purchasing Data section, check the following data:Automatic Purchase Order |  |  |
| 11 | Verify Partner Functions Data | On the Partner Functions tab page in the Partner Functions section, verify entries for LF(VN),BA(OA) and RS(PI) exists. |  |  |
| 12 | Save Your Data | Save your entries. | Message Changes have been saved is displayed. |  |

### Create/Update Business Partner for Distribution Centre (DC)

#### Create/Update DC Business Partner Customer Master Data - Sales Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master sales area data.

Prerequisite

You must complete the previous chapter, [Create/Update DC/Store Business Partner General Data](#unique_19) [page ] 32, before you proceed with this chapter.

Begin the procedure after you have saved the Data entries, as described in the previous chapter.

|  |
| --- |
| Note While using Customer Role (FLCU01), DO NOT enter Site number in the plant field under Customer: General Data tab. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Open BP | Choose Open BP button, enter BP ID created in above step.Choose Enter. | Business partner with general data maintained is displayed. |  |
| 4 | Switch to Change mode | Choose Switch Between Display and Change (F6) button to switch to change mode. |  |  |
| 5 | Change Business Partner Role | In the Change in BP role field, choose the following value:CustomerNote The technical key of this BP role is FLCU01. |  |  |
| 6 | Open Sales Area | Choose Sales and Distribution at the top of the view. | The Sales Area view appears. |  |
| 7 | Enter Sales Area Data | Select Sales Area, a pop-up will open.Enter the following data:Sales Org: 3310Distr. Channel: <10/40/50>Division: 00Choose Transfer.Note These three entries (Sales Organization, Distribution Channel, and Division) form the sales area.Now you are creating Sales Area for one combination of sales organization, distribution channel, and division. To create sales area for other combination refer to Step 14 in this procedure table. |  |  |
| 8 | Enter Sales Orders Data | On the Orders tab page in the Order section, enter the following data:Currency: <relevant currency>In the Pricing/Statistics section, enter the following data:Customer Pricing Procedure :<01> |  |  |
| 9 | Enter Shipping Data | On the Shipping tab page in the Shipping section, enter the following data:Delivery PriorityOrder CombinationShipping Conditions |  |  |
| 10 | Enter Billing Data | On the Billing tab page in the Delivery and Payment Terms section, make the following entries:Incoterms: <FH / Location of seller>Incoterms Loc1: <Location>Terms of Payment |  |  |
| 11 | Enter Tax Data | In the Output Tax section, choose the following value for the existing entry in the table:Tax Classification: <1>For example, value <1> means that this customer is fully taxable. |  |  |
| 12 | Verify Partner Functions Data | On the Partner Functions tab page, Verify the four standard partner functions for this customer. Following values in the PR column should exist:SP - Sold-to PartyBP – Bill-To PartyPY – PayerSH – Ship-to PartyNote The four partner roles mentioned are the minimum set of roles for assigning to a customer master data record, to work in a standard sale and distribution process. |  |  |
| 13 | Save Your Data | Save your entries | Message Changes have been saved is displayed. |  |
| 14 | Create Sales Area Data for other combination | To create sales area data for other combination, follow below steps:Under Sales Area section, Select Switch Area button.Below fields will be available in editable mode, enter new combination of:Sales OrganizationDistribution ChannelDivisionPress EnterTo further complete the other master data, perform step 8 -12.Save your entries.Repeat same steps for third combination of Sales Area. |  |  |
| 15 | Switch Sales Area | To view data of different Sales Area, Select Sales Areas under Sales Area section.A pop-up with list of different Sales Areas will be displayed.Select any one and click on Transfer . | Master data for different Sales Area can be viewed. |  |
| 16 | Open General Data | Choose General Data on the top of the view. |  |  |
| 17 | Save Your Data | Save your entries. | Message Changes have been saved is displayed. |  |

### Create/Update Business Partner for Store

#### Create/Update Store Business Partner Customer Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master company code data.

Prerequisite

You must complete the previous chapter, [Create/Update DC/Store Business Partner General Data](#unique_19) [page ] 32, before you proceed with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/ Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | A new window opens, displaying the Maintain Business Partner (BP) screen. |  |
| 3 | Open BP | Choose Open BP button, enter BP ID created in above step.Choose Enter. | Business partner with general data is displayed. |  |
| 4 | Switch to Change mode | Choose Switch Between Display and Change (F6) button to switch to change mode. |  |  |
| 5 | Change BP role | In the Change in BP role field, choose the following value:Customer (Fin. Accounting)Note The technical key of this BP role is FLCU00. |  |  |
| 6 | Open Company Code Data | Choose Company Code at the top of the screen | Change Organization: <BP ID>, role Customer (Fin.Accounting) screen is displayed. |  |
| 7 | Enter Company Code | Select Company Codes a pop-up will open, Enter the following data:Company Code ID: 3310And then choose Adopt. |  |  |
| 8 | Enter Customer Accounting Data | On the Customer: Account Management tab page in the Account Management section, enter the following data:Reconciliation Account: 12100000 (Receivables Domestic) |  |  |
| 9 | Enter Customer Payment Data | On the Customer: Payment Transactions tab page in the Payment Data section, make the following entry:Terms of Payment |  |  |
| 10 | Save Your Data | Save your entries. | Message Changes have been saved is displayed. |  |

#### Create/Update Store Business Partner Customer Master Data - Sales Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master sales area data.

Prerequisite

You must complete the previous chapter,[Create/Update DC/Store Business Partner General Data](#unique_19) [page ] 32 , before you proceed with this chapter.

Begin the procedure after you have saved the data entries, as described in the previous chapter.

|  |
| --- |
| Note While using Customer Role (FLCU01), DO NOT enter Site number in the plant field under Customer: General Data tab. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | A new window opens, displaying the Maintain Business Partner (BP)screen. |  |
| 3 | Open BP | Choose Open BP button, enter BP ID created in above step.Choose Enter. | Business partner with general data is displayed. |  |
| 4 | Switch to Change mode | Choose Switch Between Display and Change (F6) button to switch to change mode. |  |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:Customer.Note The technical key of this BP role is FLCU01. |  |  |
| 6 | Open Sales Area | Choose Sales and Distribution at the top of the view. | The Sales Area view is displayed. |  |
| 7 | Enter Sales Area Data | Select Sales Area, a pop-up will display.Sales Org: 3310Distr. Channel: <40/50>Division: 00Select Transfer.Note These three entries (Sales Organization, Distribution Channel, and Division) form the sales areaNow you are creating Sales Area for one combination of Sales Organization, Distribution Channel and Division, To create Sales Area for other combination refer Step 15 in this procedure. |  |  |
| 8 | Enter Sales Orders Data | On the Orders tab page in the Order section, enter the following data:Currency |  |  |
| 9 | Enter Sales Orders Data | On the Orders tab page in the Pricing/Statistics section, enter the following data:Customer Pricing Procedure <01> |  |  |
| 10 | Enter Shipping Data | On the Shipping tab page in the Shipping section, enter the following data:Delivery PriorityOrder CombinationShipping Conditions <01> |  |  |
| 11 | Enter Billing Data | On the Billing tab page in the Delivery and Payment Terms section, make the following entries:Incoterms: <FH / Location of seller>Incoterms Loc1: <Location>Terms of Payment |  |  |
| 12 | Enter Tax Data | In the Output Tax section, choose the following value for the existing entry in the table:Tax Classification: <1>For example, value <1> means that this customer is fully taxable. |  |  |
| 13 | Verify Partner Functions Data | On the Partner Functions tab page, verify the four standard partner functions for this customer. Verify the following values in the PR column:SP - Sold-to PartyBP – Bill-To PartyPY – PayerSH – Ship-to PartyNote The four partner roles mentioned are the minimum set of roles for assigning to a customer master data record, to work in a standard sale and distribution process. |  |  |
| 14 | Save Your Data | Save your entries | Message Changes have been saved is displayed. |  |
| 15 | Create Sales Area Data for other combination | To create sales area data for other combination, follow below steps:Under Sales Area section, Select Switch Area button.Below fields will be available in editable mode, enter new combination of:Sales OrganizationDistribution ChannelDivisionChoose EnterTo further complete the other master data, perform step 8 -12.Save your entries. |  |  |
| 16 | Switch Sales Area | To view data of different Sales Area, Select Sales Areas under Sales Area section.A pop-up with list of different Sales Areas will be displayed.Select any one and click on Transfer. |  |  |
| 17 | Open General Data | Choose General Data on the top of the view. |  |  |
| 18 | Save Your Data | Save your entries. | Business Partner with all required values created successfully. |  |

### Assign Existing Business Partner to Site

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for assigning business partner to site using Maintain Retail Site (F5375) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed. |  |
| 3 | Use Filter | Enter below data in the filter:Site: <DC/Store Id>Business Partner Status: Not MaintainedSelect Go. | Site is displayed with business partner is not maintained |  |
| 4 | Select Site | Select the site | Maintain master data page opens and in the header below information is displayedBusiness Partner Status: Not MaintainedCategory: Distribution Center/Store |  |
| 5 | Maintain Business Partner | Select Edit and go to Business Partner section.Enter <BP ID> created in chapter [Create/Update Business Partner for Distribution Centre/Store](#unique_18) [page ] 32 (Store) in business partner field.Select Save.Note Only those existing business partner can be used which is not assigned to any other site. | Business partner is created for site with required role and these field is updated in the system. |  |
| 6 | Verify Business partner | Select business partner created in above step.Different options will be displayed, select Business Partner Master.Maintain Business Partner (BP) app opens in display mode. | Verify business partner is created with all necessary details. |  |

### Copy Master Data and Verification

|  |
| --- |
| Note Copy Master Data feature can only be used when business partner status is Not Maintained for the site. This section will mainly emphasize on how data can be copied using Copy Master Data feature and verify if all data copied successfully. |

#### Copy Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to copy master data from one site to other for a new Site.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed |  |
| 3 | Copy Site Master Data | Select Copy Master Data, a pop-up is opened with different selection criteria:There are two options available :Individual Entries: Enter following dataSource Site <Site ID of completed Site> 3350 for DC, 3340 for StoreTarget Site < New Site ID from preliminary section>Value Range: Enter following dataEnter Source Site < Site ID of completed Site > 3350 for DC, 3340 for Storerange of Target Site < New Site ID’s from step preliminary section > in From and To.You can also select specific data to copy from source to target site:Master DataOpening and Closing TimeMerchandise CategoriesSupplying SitesClassification DataBusiness Partner DataCustomer Sales Organization DataCustomer Company Code DataSupplier Company Code DataSupplier Purchasing Organization DataSelect OK.Note If source site does not have Opening and Closing Times maintained, then the target site also would have these fields blank. You should then maintain the target site individually for Opening and Closing Times (or maintain the Time Key) | A new site is created. |  |

#### Check Logs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to view log details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed. |  |
| 3 | Show Log | After copying the site, logs can be checked for confirmation.Standard filter will be displayed, which areSeverityFromToCategorySubcategoryExternal ReferenceEnter required value and select Go .List is displayed with severity Success, Information, Warning, and ErrorSelect the line and navigate to list of messages for further information. | Logs can be checked for verification. |  |

#### Display Factsheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you see details of site master data

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Site (F0335A) app. | The Site (F0335A)screen is displayed with list of filters |  |
| 3 | Use Filter | Enter <Site ID> in the filter and press GO | Site are displayed in the list. |  |
| 4 | Select Site | Select Site |  |  |
| 5 | Verify details | Below information about site will be displayed:General InformationMerchandise CategorySupplying SitesAssortments | Verify if all information created above is displaying. |  |

#### Verify Site Assignment to Store Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows to verify sites which are copied, also assigned to store group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Display Store in Store Groups (WB87) app. | Class Type screen is displayed. |  |
| 3 | Select Class Type | Select Class Type ‘030’ that is Site Grouping.Select OK and select Display Plants to Classes. | Assign Object to Classes screen is displayed. |  |
| 4 | Fill the fields | On the ‘ Selection ’ (Screen), make entry for CustomerNoPlant: <Site ID> |  |  |
| 5 | Display Assignment | Select Display all assignment. | All assigned classes will be displayed, class assigned in reference site is displayed under this Site. |  |

### Maintain Site Blocking Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to block the site.

For example, if renovation is going on in the store and it needs to closed during a certain time period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Location Data (Retail) |  |  |
| 2 | Access the App | Open Maintain Retail Site (F5375) app. | Maintain Retail Site (F5375) screen is displayed. |  |
| 3 | Use Filter | Enter below data in the filter:Site: <DC/Store ID>Business Partner Status: MaintainedSelect Go | Site is in the list with business partner status is maintained. |  |
| 4 | Select Site | Select a site | Maintain master data page will open and in the header below information will be displayedBusiness Partner Status: MaintainedCategory: Distribution Center/Store. |  |
| 5 | Maintain Site Blocking | Select Edit and go to section Site BlockingEnter below information:FromToBlocking ReasonSelect Save. | Site is Blocked successfully. |  |

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
- related-to :: [[15-retail-operations/test-script-business-partners-for-retail-5fh-ae-sap-s-4hana-cloud-publ]]
- related-to :: [[15-retail-operations/test-script-sap-s-4hana-cloud-public-edition-assortments-3i5-ae-945]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 79,369 chars in the whole document
