---
id: 10-procurement/create-purchasing-info-record-mds-bhd-master-data-script-563
title: Create Purchasing Info Record - MDS (BHD) Master Data Script (BHD_S4CLD2608_Master_Data_EN_XX)
description: "Master data script for creating and mass-changing purchasing info records (standard, consignment, subcontracting, pipeline) in S/4HANA Cloud Public Edition."
cluster: 10-procurement
tags: [kb/procurement, topic/purchasing-info-records]
aliases: [BHD_S4CLD2608_Master_Data_EN_XX]
keywords: [Purchasing Info Records, consignment info record, subcontracting info record, pipeline info record, mass changes, mass price changes, number ranges, master data prerequisites, organizational units, tax codes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-563
topic: 10-procurement/purchasing-info-records
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Purchasing Info Record - MDS (BHD) Master Data Script (BHD_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Purchasing Info Records** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Purchasing Info Record - MDS (BHD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904919)

[2 Prerequisites 3](#_Toc233904920)

[2.1 System Access 3](#_Toc233904921)

[2.2 Roles 3](#_Toc233904922)

[2.3 Required Organizational Units 3](#_Toc233904923)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904924)

[2.5 Main Parameters for Data Creation 4](#_Toc233904925)

[2.5.1 Number Ranges 4](#_Toc233904926)

[3 Overview Table 5](#_Toc233904927)

[4 Test Procedures 6](#_Toc233904928)

[4.1 Create Purchasing Info Record 6](#_Toc233904929)

[4.2 Create Purchasing Info Record for Consignment 8](#_Toc233904930)

[4.3 Create Purchasing Info Record for Subcontracting 10](#_Toc233904931)

[4.4 Create Purchasing Info Record for Pipeline 12](#_Toc233904932)

[4.5 Mass Changes to Purchasing Info Record 15](#_Toc233904933)

[4.6 Mass Price Changes to Purchasing Info Record 16](#_Toc233904934)

[5 Appendix 18](#_Toc233904935)

[5.1 Relevant Features 18](#_Toc233904936)

## Purpose

A purchasing info record contains information specific to a material and the supplier providing the material.

It holds information such as the price charged by the supplier, their standard order quantity and tolerances for over delivery and under delivery. It is used in the purchase order transaction.

The information is specific to a particular purchasing unit (known as purchasing organization) and specific site (known as a plant) within your organization.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Required Organizational Units

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Purchasing Data | Purchasing Organization | Purchasing Group, Material Group, GR processing time, and so on. | Purchasing Data can exist for every purchasing organization for which the material is used in the purchasing processes. | Purchasing Organization:__________ |

### Mandatory and Optional Master Data

Purchasing info records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a purchasing info record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Material |  | Mandatory | To input the material, first create material master data. |
| Supplier |  | Mandatory | To input the supplier, first create supplier master data. |

### Main Parameters for Data Creation

In this section, a description is provided for the basic parameters that influence the behavior of a purchasing info record and that are always required to create a purchasing info record.

#### Number Ranges

The following number ranges are defined for purchasing info record:

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| Internal numeric | Internal numeric number range for standard use:5300000000 – 5399999999 | This number range is used when the system automatically assigns a numeric number to a material. |
| External numeric | External numeric number range (high):5400000000 – 5499999999 | This number range is reserved for external numeric number assignment. |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchasing Info Record](#unique_10) [page ] 6 | Purchaser | Manage Purchasing Info Records (F1982) | Purchasing Info Records is created. |
| [Create Purchasing Info Record for Consignment](#unique_11) [page ] 8 | Purchaser | Manage Purchasing Info Records (F1982) | Purchasing Info Record for the consigned is created. |
| [Create Purchasing Info Record for Subcontracting](#unique_12) [page ] 10 | Purchaser | Manage Purchasing Info Records (F1982) | Purchasing Info Record for the subcontracting is created. |
| [Create Purchasing Info Record for Pipeline](#unique_13) [page ] 12 | Purchaser | Manage Purchasing Info Records (F1982) | Purchasing Info Record for the Pipeline is created. |
| [Mass Changes to Purchasing Info Record](#unique_14) [page ] 15 | Purchaser | Mass Changes to Purchasing Info Records (F2667) | Mass Changes to Purchasing Info Record are applied. |
| [Mass Price Changes to Purchasing Info Record](#unique_15) [page ] 16 | Purchaser | Price Changes: Info Records | Mass Price Changes to Purchasing Info Record are applied. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: <Purchasing Organization>Supplier: <Supplier>Material: <Material>Plant: <Plant>Purchasing Group: <Purchasing Group> | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: MM/DD/YYYYAvailable To: MM/DD/YYYY | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: <Incoterm>Incoterm Location 1: <Incoterm location1> | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX Days>Under Delivery Tolerance in %: <XX>Over Delivery Tolerance in %: <XX>Tax Code: <Tax Code>Note When the TDT (Time-Dependent Tax) is activated via Configuration Step 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in Configuration Step.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in Configuration Step 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as default value, but you can change to the valid country ID that is maintained in Configuration Step accordingly.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Order Unit: <Order Unit>Standard Order Quantity: <Standard Order Quantity>Select the following entries if required:Unlimited DeliveryGoods-Receipt-Based Invoice VerificationNo Evaluated Receipt SettlementOrder Acknowledgment RequirementConfirmation Control | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>Pricing Unit: <Pricing Unit>Valid To: <Valid to Date>Currency: <Currency>Choose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (Optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

### Create Purchasing Info Record for Consignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982) | The Manage Purchasing Info Records screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category:< Consignment>Purchasing Organization: <Purchasing Organiza-tion>Supplier: <Supplier>Material: <Material>Plant: <Plant>Purchasing Group: <Purchasing Group> | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: MM/DD/YYYYAvailable To: MM/DD/YYYY | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: <Incoterm>Incoterm Location 1: <Incoterm location1> | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX Days>Under Delivery Tolerance in %: <XX>Over Delivery Tolerance in %: <XX>Tax Code: <Tax Code>Note When the TDT (Time-Dependent Tax) is activated via Configuration Step 101016 (Define Tax Codes for Sales and Purchases) for country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in Configuration Step.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in Configuration Step 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as default value, but you can change to the valid country ID that is maintained in Configuration Step accordingly.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Order Unit: <Order Unit>Standard Order Quantity: <Standard Order Quan-tity> | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>Pricing Unit: <Pricing Unit>Valid To: <Valid to Date>Currency:<Currency>Choose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (Optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

### Create Purchasing Info Record for Subcontracting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category:<Subcontracting>Purchasing Organization: <Purchasing Organization>Supplier: <Supplier>Material: <Material>Plant: <Plant>Purchasing Group: <Purchasing Group> | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: MM/DD/YYYYAvailable To: MM/DD/YYYY | General Information is added. |  |
| 6 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX Days>Under Delivery Tolerance in %: <XX>Over Delivery Tolerance in %: <XX>Tax Code: <Tax Code>Note When the TDT (Time-Dependent Tax) is activated via Configuration Step 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in Configuration Step.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in Configuration Step 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as default value, but you can change to the valid country ID that is maintained in Configuration Step accordingly.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Order Unit: <Order Unit>Standard Order Quantity: <Standard Order Quantity> | Delivery and Quantity Data is added. |  |
| 7 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>Pricing Unit: <Pricing Unit>Valid To: <Valid to Date>Currency: <Currency>Choose Apply. | Condition Data is added. |  |
| 8 | Enter Reference Data (Optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 9 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

### Create Purchasing Info Record for Pipeline

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchasing Info Records (F1982). | The app opens. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Pipeline>Purchasing Organization: <Purchasing organization>Supplier: <Supplier>Material: <Pipeline material>Plant: <Plant>Purchasing Group: <Purchasing group>Material Group: <Material group> | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: MM/DD/YYYYAvailable To: MM/DD/YYYY | General information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: <Incoterm>Incoterm Location 1: <Incoterm location 1> | Purchasing data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <XX days>Under Delivery Tolerance in %: <XX>Over Delivery Tolerance in %: <XX>Tax Code: <Tax code>Note When the TDT (Time-Dependent Tax) is activated via Configuration Step 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in Configuration Step.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in Configuration Step 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as default value, but you can change to the valid country ID that is maintained in configuration step accordingly.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Order Unit: <Order unit>Standard Order Quantity: <Standard order quantity>Select the following entries if required:Unlimited DeliveryGoods-Receipt-Based Invoice VerificationNo Evaluated Receipt SettlementOrder Acknowledgment RequirementConfirmation Control | Delivery and Quantity data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create. Enter the following data:Valid From: <Valid from date>Amount: <Amount>Pricing Unit: <Pricing unit>Valid To: <Valid to date>Currency: <Currency>Choose Apply. | Condition data is added. |  |
| 9 | Enter Reference Data (Optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

### Mass Changes to Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you apply changes to multiple selected Purchasing Info Records in bulk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Mass Changes to Purchasing Info Records (F2667). | The app opens. |  |
| 3 | Search for Purchasing Info Records | To search for purchasing info records, enter the following values to filters:Supplier: <Supplier ID>Purchasing Group: for example, 001Plant: <Plant ID>Choose Go. | The search results display the details of the respective filter criteria.By default, all the purchasing info records are selected for mass change operations. |  |
| 4 | Select Purchasing Info Records | Select the Purchasing Info Records checkbox under the Purchasing Info Records and Purchasing Organization tab.Choose Mass Edit. |  |  |
| 5 | Set New Values | Enter new values in the following entries:In the General Data section:Supplier Mat. No.Supplier Mat. GroupIn the Purchasing Organization Data section:Purchasing GroupMinimum Order QuantityChoose Apply Mass Changes.A dialog box displays to confirm mass changes.On the Apply Mass Changes screen, choose Apply.A dialog box displays with the JOB ID.Choose View Job List. | New values are applied to the selected purchasing info records. |  |
| 6 | Check Application Jobs | Enter search criteria and choose Go.The Application Jobs screen displays with the list of Job IDs for all purchasing info records.Choose Log to verify the success of your selected purchasing info records. |  |  |

### Mass Price Changes to Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the Price Change: Info Records (MEKP) app is used to mass update the prices for info records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Price Change: Info Records (MEKP). | The app opens. |  |
| 3 | Enter Initial Data | Make the following entries and choose Execute:Purchasing Organization: <Purchasing Orgization ID>Supplier: <Supplier ID>Material: <Material ID>Info Records without Material: <Blank>Test Run: <Blank>Go to the Change condition type or gross price section and make the following entries:Condition Type: <Condition Type ID>, for example, PPR0Absulte Amount: <Absulte Amount>, for example, 10Sign: <Sign>, for example, +Gross Price: <Blank>Scale Lines: <X>Go to the Conditions valid section and make the following entries::On: <Current Date>Or From <Blank> To <Blank> | New values are maintained for the purchasing info records. |  |
| 4 | Check Purchasing Info Records Changes | On the Price Change for Info Records of Supplier <XXXX> screen, check the Old and New records and confirm the changes. | The purchasing info records price changes are saved. |  |
| 5 | Exit | Choose Exit. |  |  |

## Appendix

### Relevant Features

Here are listed some important application functionalities related to Purchase Info Record, which are not covered in the above test procedures.

| Function Area | Function | Detailed Information | Comment |
| --- | --- | --- | --- |
| Purchase Info Records | Info Record related apps | WebGUI: Delete Purchasing Info Record (ME15)WebGUI: Display Purchasing Info Record by Supplier (ME1L)WebGUI: Maintain Changes to Purchasing Info Records (ME14)WebGUI: Maintain Purchasing Conditions (MEKA)WebGUI: Maintain Rounding Profile (OWD1) |  |

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
- related-to :: [[10-procurement/criar-registro-info-para-compras-mds-bhd-566]]
- related-to :: [[10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562]]
- related-to :: [[10-procurement/mds-bhd-565]]
- related-to :: [[10-procurement/mds-bhd-567]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 26,732 chars in the whole document
