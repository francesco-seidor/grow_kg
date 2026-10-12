---
id: 13-quality-ehs-and-compliance/test-script-label-management-6mt-ae-sap-s-4hana-cloud-public-edition-1
title: "Test Script: Label Management (6MT_AE) - SAP S/4HANA Cloud Public Edition (6MT_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 6MT Label Management: prerequisites, print queue setup, generic and delivery label test steps."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/safety-data-sheets-and-labels]
aliases: [6MT_S4CLD2608_BPD_EN_AE]
keywords: ["Safety Data Sheet Authoring, Distribution and Labels", label management, label printing, compliance requirements, label configuration, label assignment, logistic labels, print queues, safety data sheet contacts, outbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6MT_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1177
topic: 13-quality-ehs-and-compliance/safety-data-sheets-and-labels
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Label Management (6MT_AE) - SAP S/4HANA Cloud Public Edition (6MT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6MT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Safety Data Sheet Authoring, Distribution and Labels** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Label Management (6MT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859131)

[2 Prerequisites 4](#_Toc232859132)

[2.1 System Access 4](#_Toc232859133)

[2.2 Roles 4](#_Toc232859134)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232859135)

[2.4 Additional Manual Configuration 6](#_Toc232859136)

[2.5 Business Conditions 6](#_Toc232859137)

[3 Preliminary Steps 7](#_Toc232859138)

[3.1 Create Print Queue 7](#_Toc232859139)

[3.2 Set Initial Stock for Material 8](#_Toc232859140)

[3.3 Create Contact Data SDS 9](#_Toc232859141)

[4 Overview Table 11](#_Toc232859142)

[5 Test Procedures 12](#_Toc232859143)

[5.1 Generic Scenario 12](#_Toc232859144)

[5.1.1 Create Compliance Requirement - Labels 12](#_Toc232859145)

[5.1.2 Create Configuration for Labels 13](#_Toc232859146)

[5.1.3 Create Label Assignment 14](#_Toc232859147)

[5.1.4 Validate and Print Labels 15](#_Toc232859148)

[5.2 Delivery Scenario 17](#_Toc232859149)

[5.2.1 Create Configuration for Logistic Label 17](#_Toc232859150)

[5.2.2 Create Logistic Label Assignment 18](#_Toc232859151)

[5.2.3 Create Delivery 19](#_Toc232859152)

[5.2.4 Validate and Print Labels 20](#_Toc232859153)

## Purpose

Overview

This scope item enables you to create and design label templates in external systems and use them in SAP S/4HANA Cloud Public Edition via integration. You can also collect or calculate relevant product data for labels, varying by country/region or language in SAP S/4HANA Cloud Public Edition (for example, Dangerous Goods classifications, GHS classification). Furthermore, you can create print requests for labels in external systems using a third-party output management system.

The labels can then be placed on products, and those products can be shipped to customers.

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

| Name (Business Role or Template) | ID | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administrator | SAP_BR_ADMINISTRATOR |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Table 1: Master Data Script Reference

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FGPCLBL01 | Finished Good Label Mgmt 01 | Loaded and activated with the scope item. |
| Label Template | BPC_TEMPLATE | /BPC/Product Labels/Hazardous/America/North America | Example label template – loaded with the scope item for demo purposes. |
| Label Template | BCP_LOG_TEMPLATE | /BPC/Logistic Labels | Example logistic label template - loaded with the scope item for demo purposes. |
| Ship to Party | 33100003 | Domestic UAE Customer 3 | Business Partner with role Ship To Party |
| Plant | 3310 | Plant 1 AE | Loaded with the scope item. |
| Storage Location | 331A | Std. storage 1 | Loaded with the scope item. |
| Shipping Point | 3310 | Shipping Point 3310 | Loaded with the scope item. |
| Sales Organization | 3310 | Dom. Sales Org | Loaded with the scope item. |
| Distribution Channel | 10 | Direct Sales | Loaded with the scope item. |
| Division | 00 | Product Division 00 | Loaded with the scope item. |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/fa98b96daff9f160b12c29177052b440)

### Business Conditions

Before you can test this scope item, the following business conditions must be met:

| Scope Item ID | Business Condition |
| --- | --- |
| 1LQ - Output Management | The scope item 1LQ must be implemented and tested before testing scope item 6МТ. |
| 1MI - Delivery Processing Without Order Reference | The scope item 1MI must be implemented and tested before testing the delivery scenario for scope item 6МТ. |

## Preliminary Steps

### Create Print Queue

Use

The Administrator maintains print queues to enable the printing of labels.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access App | Open the Maintain Print Queues (F1260) app. | The Maintain Print Queues screen is displayed. |  |
| 3 | Select Print Queue Type | Choose New to create a new print queue.In the newly opened New Print Queue dialog box, choose one of the following:If your output management system (OMS) supports the pulling method to check for the availability of new items to print, choose OMS for Pull Integration Queue from the dropdown list.If your output management system (OMS) supports the notification method to receive information about new items to print, choose OMS for Notification Integration Queue from the dropdown list.Choose Create. | The print queue type is selected. The New Print Queue dialog box is opened with required fields to enter further data for the queue. |  |
| 4 | Enter Details for the Print Queue | In the newly opened dialog box, enter or select the following data:Queue: <Enter Queue Name, for example: PC_LABELING>Description: Queue for LABELINGFormat: XMLDATACommunication User: <Enter the User Name for Inbound Communication that you created as part of the Set-Up Instructions of this scope item.>(only for Notification Integration) Destination: <Filled in automatically after the user is selected.>(only for Notification Integration) Notification Type: Single NotificationRetention: 1Choose Create. | The print queue is created. A success message is displayed. |  |

### Set Initial Stock for Material

Use

Set initial stock for a material so that it is available for executing the delivery scenario of this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Post Goods Movement (MIGO). app. | The Goods Receipt Other screen is displayed. |  |
| 3 | Enter Movement Type | Make the following entries and choose Enter:Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material: FGPCLBL01 |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 100Unit of Entry: BT |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: 3310Storage Location: 331A |  |  |
| 7 | Save Your Entries | Choose Post. |  |  |

### Create Contact Data SDS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance enters the company address and emergency phone number that needs to be printed on the labels.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open the Manage Contact Data - Safety Data Sheets (SDS)(F4521) app. | The Manage Contact Data – Safety Data Sheets screen is displayed. |  |
| 3 | Create New Contact Data | On the Manage Contact Data – Safety Data Sheets screen, choose Create. | The New Safety Data Sheet Contact sub screen is displayed. |  |
| 4 | Enter Header Data | Enter the following header data:Product: FGPCLBL01Additional Information: The restriction on a specific product is only a very rare use case. We're using it here for testing purpose, so that multiple people can test on the same system with different products without influencing each other. |  |  |
| 5 | Add Company Address | In the Addresses section, choose the drop-down in the Address Type field and select Company address. |  |  |
| 6 | Select Company Address | In the Business Partner field, make the following entry:33100003 | The address of the selected business partner is populated. |  |
| 7 | Add Emergency Phone Number | In the Emergency Phone Numbers section, enter EN in the Language field and enter the following phone number against it:999-654-2356 |  |  |
| 8 | Add Logo | In the Logo section, select a logo.Additional Information: If no logo is available, you can upload a logo in the Manage Logos app. Note that this is only possible on a system with extensibility activated and that you need administrator authorizations. | The selected logo is displayed. |  |
| 9 | Save Your Entries | Choose Create to create the contact data and save your entries. | The safety data sheet contact data is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Compliance Requirement - Labels](#unique_12) [page ] 12 | Product Stewardship Specialist - Product Compliance | Manage Compliance Requirements (EHLBL_CR_ENTRY_OIF) | A compliance requirement for labels is created and released. |
| [Create Configuration for Labels](#unique_13) [page ] 13 | Product Stewardship Specialist - Product Compliance | Manage Configurations for Labels (F6689) | A configuration for a label is created. A label template and a compliance requirement are assigned to the configuration. |
| [Create Label Assignment](#unique_14) [page ] 14 | Product Stewardship Specialist - Product Compliance | Manage Label Assignments - Products (F6615) | Labels are assigned to the product. |
| [Create Delivery](#unique_15) [page ] 19 | Shipping Specialist | Create Outbound Delivery - Without Order Reference (VL01NO | An outbound delivery is created. |
| [Validate and Print Labels](#unique_16) [page ] 15 | Product Stewardship Specialist - Product Compliance | Validate and Print Labels (F6656) | Assigned labels are validated and a print request can be created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Generic Scenario

#### Create Compliance Requirement - Labels

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance creates a compliance requirement for labels, fills in the required label details, and releases the compliance requirement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Manage Compliance Requirements (EHLBL_CR_ENTRY_OIF) app. | The Manage Compliance Requirements - Labels screen is displayed. |  |
| 3 | Create Header Data of the Regulation | Choose Create First Version and select Regulation from the dropdown list.In the newly opened Create First Compliance Requirement Version dialog box, enter or select the following data:Compliance Requirement: <Enter a name for your compliance requirement.>Compliance Pattern: Label for Hazardous ProductVersion Name: <Enter a name for the compliance requirement version.>Effective Date: <Keep default selection (today’s date).>Choose Create. | You are navigated to the detailed page of the new compliance requirement of type Regulation.Make a note of your compliance requirement name. You will need it in the next test procedure. |  |
| 4 | Set Validity of the Regulation | In the Compliance Requirement Version section, choose Edit to enter the validity area of the regulation.Choose Add and enter US in the Country/Region Code field.Choose Close. | Validity country/region for the regulation is set.Note If you do not enter any country/region, the compliance requirement is valid for all countries/regions. |  |
| 5 | Enter Regulation Details | On the Regulation Details tab, enter additional information about the regulation, if available. |  |  |
| 6 | Save the Regulation | Choose Save on the bottom right side of the screen. | The regulation is saved. |  |
| 7 | Set Maintenance Status | Choose Set Maintenance Status in the header section and select Released from the dropdown list. In the newly opened confirmation dialog box, choose Yes. | The regulation is released and can be used in follow-on business processes. |  |

#### Create Configuration for Labels

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance creates a label configuration. A label configuration reflects a given label category and the label template that is relevant for it. It also contains information about the compliance requirements applicable to the label.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Manage Configurations for Labels (F6689) app. |  |  |
| 3 | Create a New Configuration | Choose Create and make the following entries in the newly opened Create dialog box:Label Category: Label for Hazardous ProductLabel Template ID: BPC_TEMPLATE - /BPC/Product Labels/Hazardous/America/North AmericaChoose Continue to proceed to the next screen. | The detailed page of the new label configuration is displayed. |  |
| 4 | Specify Configuration Name | In the Configuration Names section make the following entries:Language: ENConfiguration Name: <Enter a name> | Configuration name is specified. Make a note of the name. You will need it in the next test procedure.Note You can enter configuration names in as many languages as you need. |  |
| 5 | Assign a Compliance Requirement to the Configuration | In the Compliance Data section search for the compliance requirement that you created in [Create Compliance Requirement - Labels](#unique_12) [page ] 12 or directly enter its name in the field. | The compliance requirement is assigned to the label configuration. |  |
| 6 | Save | Choose Create on the bottom right side of the screen to save your entries. | The label configuration is saved. |  |

#### Create Label Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance assigns labels to products. Label assignments contain a label category and the corresponding label configurations for it. By creating a label assignment for a product in the system, the Product Stewardship Specialist - Product Compliance performs an initial setup of the label-relevant information for the product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Manage Label Assignments - Products (F6615) app. |  |  |
| 3 | Create New Assignment | Choose Create and select the following entry in the newly opened Create dialog box:Product: FGPCLBL01Choose Continue to proceed to the next screen. | The detailed page of the new label assignment is displayed. |  |
| 4 | Create Label Assignment | In the Label Assignments section, choose or select the following entries:Label Category: Label for Hazardous ProductConfiguration ID: <Select the name of the configuration that you created in [Create Configuration for Labels](#unique_13) [page ] 13> | The label assignment is defined.Note You can create as many label assignments for one product as you need. |  |
| 5 | Save the Label Assignment | Choose Create on the bottom right side of the screen. | The label assignment is created. A success message is displayed. |  |

#### Validate and Print Labels

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance validates the labels assigned to the products, which are separated by business scenario. They also create print requests to the external output management system, which then prints those labels for usage in the respective scenario.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Validate and Print Labels (F6656) app. |  |  |
| 3 | Enter Search Criteria | Make the following entries:Search: FGPCLBL01Scenario: GenericChoose Go to load the results. | The search result is displayed. |  |
| 4 | Check Label Setup | Select the row to navigate to the details of the object.The following data should be visible:Label Category: Label for Hazardous ProductConfiguration Name: <Configuration Name, created in [Create Configuration for Labels](#unique_13) [page ] 13>Country/Region:<Countries for which the assigned label is valid>Button:Create Label Print Request | Label Assignment is validated. |  |
| 5 | Create a Print Request | Choose Create Label Print Request.In the newly opened Create Label Print Request dialog make the following entries:Print queue: <Queue created in [Create Print Queue](#unique_8) [page ] 7>Number of copies: 1Choose Create Label Print Request to send the request to the print queue. | Information message that the label print request was successfully sent. |  |
| 6 | Check Print Request (Optional) | Log on to the SAP Fiori launchpad as an Administrator and navigate to Maintain Print Queues app.Choose Filters and add Queue to the listed fieldsEnter <Queue created in [Create Print Queue](#unique_8) [page ] 7>in the newly added field and choose Go.Select the row to see the available print items.Search for the item, created by your user in the respective date and timeframe. | The print item created by your user is visible in the list. |  |

### Delivery Scenario

#### Create Configuration for Logistic Label

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance creates a label configuration. A label configuration reflects a given label category and the label template that is relevant for it. It also contains information about the compliance requirements applicable to the label, if any.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Manage Configurations for Labels (F6689) app. |  |  |
| 3 | Create a New Configuration | Choose Create and make the following entries in the newly opened Create dialog box:Label Category: Logistic LabelLabel Template ID: BPC_LOG_TEMPLATE - /BPC/Logistic LabelsChoose Continue to proceed to the next screen. | The detailed page of the new label configuration is displayed.. |  |
| 4 | Specify Configuration Name | In the Configuration Names section make the following entries:Language: ENConfiguration Name: <Enter a name> | Configuration name is specified. Make a note of the name. You will need it in the next test procedure.Note You can enter configuration names in as many languages as you need. |  |
| 5 | Save | Choose Create on the bottom right side of the screen to save your entries. | The label configuration is saved. |  |

#### Create Logistic Label Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance assigns labels to products. Label assignments contain a label category and the corresponding label configurations for it. By creating a label assignment for a product in the system, the Product Stewardship Specialist - Product Compliance performs an initial setup of the label-relevant information for the product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Manage Label Assignments - Products (F6615) app. |  |  |
| 3 | Check Assignment | Make the following entry in the Search field and choose Go (or Enter):Product: FGPCLBL01If the search returns a result with this value, select it and then, on the details page choose Edit. Then proceed with the next step.If the search doesn’t return a result, choose Create and select the product in the newly opened Create dialog box:Product: FGPCLBL01Choose Continue to proceed to the next screen. |  |  |
| 4 | Create Label Assignment | In the Label Assignments section, choose or select the following entries:Label Category: Logistic LabelConfiguration ID: <Select the name of the configuration that you created in [Create Configuration for Logistic Label](#unique_18) [page ] 17>Choose the navigation arrow to go to Markets and Production Countries/Regions detail page.Make the following entry in column Sell In:Sell In: <Select the country of the business partner that you entered in [Create Contact Data SDS](#unique_10) [page ] 9>Navigate to the detail page of the created row and make an entry for the languages, needed on your label for the selected country, for example: EN. | The label assignment is defined.Note You can create as many label assignments for one product as you need. |  |
| 5 | Save the Label Assignment | Choose Apply on the bottom right side of the screen, and then Save. | The label assignment is created. A success message is displayed. |  |

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open the Create Outbound Delivery - Without Order Reference (VL01NO) app. |  |  |
| 3 | Enter Key Data for Outbound Delivery Creation | On the Create Outbound Delivery Without Order Reference screen, make the following entries, and choose Enter:Shipping Point: 3310Delivery Type: LOSales Organization: 3310Distribution Channel:10Division:00 |  |  |
| 4 | Enter Delivery Details | On the Delivery without Reference Create: Overview screen, make the following entries and choose Enter:Ship-to Party: 33100003Planned GI:<Planned GI>, for example, <Today's Date>Material Number: FGPCLBL01Deliv. Quantity:<Quantity> , for example, <1 BT>Note If any warning or information pop up comes, please ignore it. |  |  |
| 5 | Save Document | Choose Save. Make a note of the delivery number. |  |  |

#### Validate and Print Labels

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance validates the labels assigned to the products, which are separated by business scenario. They can also create print requests to the external output management system, which then prints those labels for usage in the respective scenario.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. |  |  |
| 2 | Access App | Open the Validate and Print Labels (F6656) app. |  |  |
| 3 | Enter Search Criteria | Make the following entries:Search: <Delivery number from previous step>Scenario: DeliveryChoose Go to load the results. | The search result is displayed. |  |
| 4 | Check Label Setup | Select the row to navigate to the details of the object.In the header, the product, delivery number and quantity should be visible.The following data should be visible in the table:Label Category Description: Logistic LabelConfiguration Name: <Configuration Name, created in [Create Configuration for Logistic Label](#unique_18) [page ] 17>Country/Region:USAButton:Create Label Print Request | Label Assignment is validated. |  |
| 5 | Create a Print Request | Choose Create Label Print Request.In the newly opened Create Label Print Request dialog make the following entries:Print queue: <Queue created in [Create Print Queue](#unique_8) [page ] 7>Number of copies: 1Choose Create Label Print Request to send the request to the print queue. | Information message that the label print request was successfully sent. |  |
| 6 | Check Print Request (Optional) | Log on to the SAP Fiori launchpad as an Administrator and navigate to Maintain Print Queues app.Choose Filters and add Queue to the listed fieldsEnter <Queue created in [Create Print Queue](#unique_8) [page ] 7>in the newly added field and choose Go.Select the row to see the available print items.Search for the item, created by your user in the respective date and timeframe. | The print item created by your user is visible in the list. |  |

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
> Flagged while digesting this document, not verified: Delivery-scenario Validate and Print step expects Country/Region USA, while the ship-to party 33100003 is 'Domestic UAE Customer 3' and the Sell In country is meant to be that business partner's country; the compliance requirement validity in the generic scenario is US.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/product-compliance-document-authoring-7do-ae-test-script-sap-s-4hana-c]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-manage-safety-data-sheets-for-products-3vr-ae-sap-s-4hana]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-request-regulatory-documentation-from-service-provider-6av]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6MT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 35,227 chars in the whole document
