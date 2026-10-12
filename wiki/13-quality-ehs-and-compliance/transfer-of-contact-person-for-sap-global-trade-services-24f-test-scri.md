---
id: 13-quality-ehs-and-compliance/transfer-of-contact-person-for-sap-global-trade-services-24f-test-scri
title: Transfer of Contact Person for SAP Global Trade Services (24F) - Test Script (24F_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 24F: transferring customer contact persons to SAP Global Trade Services via SOAP or RFC."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/gts-master-data-transfer]
aliases: [24F_S4CLD2608_BPD_EN_XX]
keywords: [Transfer of Contact Persons and BOMs to SAP GTS, contact person transfer, global trade services, business partner replication, soap services, filter criteria, value mapping, code lists, changed master data transfer, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24F_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-804
topic: 13-quality-ehs-and-compliance/gts-master-data-transfer
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Transfer of Contact Person for SAP Global Trade Services (24F) - Test Script (24F_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24F_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Transfer of Contact Persons and BOMs to SAP GTS** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Transfer of Contact Person for SAP Global Trade Services (24F) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847169)

[2 Prerequisites 3](#_Toc232847170)

[2.1 Additional Manual Configuration 3](#_Toc232847171)

[2.2 System Access 3](#_Toc232847172)

[2.3 Roles 3](#_Toc232847173)

[2.4 Business Conditions 4](#_Toc232847174)

[2.5 Master Data, Organizational Data, and Other Data 4](#_Toc232847175)

[3 Overview Table 6](#_Toc232847176)

[4 Test Procedures 7](#_Toc232847177)

[4.1 Schedule Transfer of Contact Persons 7](#_Toc232847178)

[4.2 Schedule Transfer of Changed Master Data (Optional) 11](#_Toc232847179)

[5 Appendix 13](#_Toc232847180)

[5.1 Additional Configurations for Data Transfer of Business Partner with SOAP Services 13](#_Toc232847181)

[5.1.1 Define Filter Criteria in SAP S/4HANA Cloud Public Edition System 13](#_Toc232847182)

[5.1.2 Maintain Value Mapping in SAP Global Trade Services System 14](#_Toc232847183)

[5.1.3 Assign Code Lists to Elements and Systems in SAP Global Trade Services System 15](#_Toc232847184)

## Purpose

Overview

You can integrate SAP Global Trade Services 11.0 on-premise with SAP S/4HANA Cloud Private Edition or SAP S/4HANA Cloud Public Edition to use existing rules for trade being managed in the cloud.

This scope item enables the communication scenario and the appropriate RFC calls for synchronizing the contact person. Successfully synchronizing the contact person requires that the corresponding business partner already exists in the SAP Global Trade Services system.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/40a2cac694792231c693a7eccfd3fad2)

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA System | Accessible via Fiori Launchpad.Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator - International Trade | SAP_BR_ADMINISTRATOR_SLL | International Trade Administration | SAP_BR_ADMINISTRATOR_SLL |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 1WA - Transfer of Primary Master Data for SAP Global Trade Services | Before you can transfer a contact person, you must first transfer the corresponding customer. |

Additional configurations in SAP Global Trade Services system:

To make the master data transfer successful, you may need to make additional configurations in the SAP Global Trade Services system (for example, the regions in address). These configurations depend on your SAP Global Trade Services system. This is not covered in this document.

If the transfer is not successful, you may check the application logs in SAP Global Trade Services system to get the error details and then fix it.

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your S/4 HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics.Check your SAP system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document

| Data | Sample Value | Detail | Comment |
| --- | --- | --- | --- |
| Contact Person | <name of contact person at customer> |  | Caution If you do not maintain the address for the contact person, the data transfer will fail. Once the missing address is maintained for the contact person, update the corresponding customer master data to reassign the relationship. |

For more information about creating master data, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Script documentation.

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |

## Overview Table

The scope item Transfer of Contact Person for SAP Global Trade Services consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Result |
| --- | --- | --- | --- |
| [Schedule Transfer of Contact Persons](#unique_9) [page ] 7 | Configuration Expert - Business Network Integration | Replicate by Replication Model (DRF_WDA0478) | The contact persons are transferred with SOAP services to the SAP Global Trade Services system. |
| [Schedule Transfer of Contact Persons](#unique_9) [page ] 7 | Administrator - International Trade | Schedule Transfer of Contact Persons - Global Trade Services (F2803) | The selected contact persons are transferred to SAP Global Trade Services system. |
| [Schedule Transfer of Changed Master Data (Optional)](#unique_10) [page ] 11 | Administrator - International Trade | Schedule Transfer of Changed Master Data - Global Trade Services (F6041) | The application jobs of transfer changed master data are scheduled, and the changed master data is transferred by the scheduled application jobs. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Schedule Transfer of Contact Persons

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Transfer the contact person master data to SAP Global Trade Services system.

Prerequisites

|  |
| --- |
| Caution Before you start the test procedures, ensure that the Set-up Instruction Guide of this scope item is executed to ensure working connectivity between the SAP S/4HANA Cloud Public Edition system and the SAP Global Trade Services system. |

Procedure

Depending on your system environments, choose one of the following options to transfer contact person master data:

|  |
| --- |
| Note If your SAP Global Trade Services system operates on the SAP HANA edition, it is recommended to set SOAP services as the default method for transferring business partner data.If the multiple address handling functionality is activated in the SAP S/4HANA Cloud Public Edition system, using SOAP services for business partner transfer is the sole option for transferring contact person data. |

|  |
| --- |
| Caution During testing, ensure that you use different contact persons for each option. |

Option 1: Business Partner Transfer with SOAP Services

|  |
| --- |
| Caution Before you start the data transfer, ensure that the chapter [Additional Configurations for Data Transfer of Business Partner with SOAP Services](#unique_12) [page ] 13 has been completed. |

|  |
| --- |
| Note The business partner data transfer depends on the output mode chosen for the business object type 986 - Business Partner including Relationships. This output mode is set in the step Create Communication Agreement of SAP_COM_0008, which is described in the Set-up Instruction of this scope item.When the output mode is not specified, set to Object - Dependent Default, or set to D - Direct Output, business partners are instantly replicated upon creation or modification. Whereas when the output mode is set to P - Pooled Output, changes to business partners are accumulated and replicated later through scheduled jobs. |

Below are the steps for manually replicating selected business partners for your reference:

1. Execute Manual Replication in SAP S/4HANA Cloud Public Edition System:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP S/4HANA Cloud Public Edition System | Log onto the SAP Fiori launchpad using the role Configuration Expert - Business Network Integration. |  |  |
| 2 | Access App | Choose Define Filter Criteria (F6519) | The Define Filter Criteria screen is displayed. | Note If the filter criteria is defined, you can directly choose the app Replicate by Replication Model. |
| 3 | Define Filter Criteria | Under the filter area, enter the following replication model and choose Go:Replication Model: <Select the replication model, for example, S4BUPAGTS>Click on the selected replication model.Choose Edit, and click on the filter object BP Service Filter (OTC 986) under the Main Filters area.Next, choose Create to add the filter entry below, and then click on Apply.Field Name: Business Partner Number (PARTNER)Filter: equal toValue: <Select the business partner number of the contact person>Choose Save. | The filter criteria is defined, and the business partner is selected for replication.Next, access the app Replicate by Replication Model to start the replication. | The replication model is defined in the step Create Communication Agreement of SAP_COM_0008, which is described in the Set-up Instruction of this scope item. |
| 4 | Access App | Choose Replicate by Replication Model (DRF_WDA0478) | The Replicate by Replication Model screen is displayed. | You can also execute the data replication by accessing the app Replicate by Object Selection from the SAP Fiori launchpad using the role Configuration Expert - Business Network Integration. |
| 5 | Execute Data Replication | Make the following entries and choose Replicate:Replication Model: <Select the replication model, for example, S4BUPAGTS>System ID: <Select the target system of the SAP Global Trade Services>Business Object: Business Partner including RelationshipsReplication Mode: Manual | The replication scope is chosen, and the replication is executed. | The replication model is defined in the step Create Communication Agreement of SAP_COM_0008, which is described in the Set-up Guide of this scope item.Note Once the replication is triggered, you can check the replication logs by accessing the app Monitor Replication (DRF_WDA0475). |

1. Check the Replicated Business Partners in SAP Global Trade Services System:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Trade Compliance Specialist (GTS) in the SAP Global Trade Services system. |  |  |
| 2 | Access App | Choose Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Input Selection Values | Make the following entries in the Find area and choose Start:Find: PersonsBy: External NumberExternal Number: <Enter the business partner number of the contact person from the SAP S/4HANA Cloud Public Edition system> |  | Note In this process, you can use the business partner number instead of the external number. To find the business partner number in the SAP Global Trade Services system, follow these steps:Run transaction code SRT_MONI.Select the row of the web service.Double-click the Message ID.In the BusinessPartner message segment, locate the value of ReceiverInternalID, which represents the business partner number created in the SAP Global Trade Services system. |
| 4 | Check Replicated Data | Check the replicated business partners. |  |  |

Option 2: Business Partner Transfer with RFC

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. |  |  |
| 2 | Access App | Choose Schedule Transfer of Customers - Global Trade Services (F2806). | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Contact Persons Background Job | Choose Create. | The New Job screen displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Schedule Transfer of Contact Persons - Global Trade ServicesJob Name: Schedule Transfer of Contact Persons - Global Trade Services |  |  |
| 5 | Scheduling Options | Choose Define Recurrence Pattern. Make the following entries and choose OK. Then choose Step 3:Start Immediately: <Select>Recurrence Pattern: Single Run |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Title of Transfer Log: <Enter a log description>Contact Person: <Leave blank> | The job is scheduled and shown in the list.If the customers were transferred beforehand, their corresponding contact persons are transferred in this step. |  |

### Schedule Transfer of Changed Master Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the master data is updated, you can schedule application jobs to transfer changed master data.

|  |
| --- |
| Note This step is not relevant for the data transfer with SOAP services. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. |  |  |
| 2 | Access App | Choose Schedule Transfer of Changed Master Data - Global Trade Services (F6041). | The Application Jobs screen displays. |  |
| 3 | Create Schedule Transfer of Changed Master Data Application Jobs | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Schedule Transfer of Changed Master Data to Global Trade ServicesJob Name: Schedule Transfer of Changed Master Data to Global Trade Services | The application logs for the transfer of changed master data are checked. |  |
| 5 | Scheduling Options | Choose Define Recurrence Pattern. Make the following entries and choose OK. Then choose Step 3:Start Immediately: <Select>Recurrence Pattern: Single Run |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Message Type: /SAPSLL/CPMAS_SLL | The job is scheduled and displayed in the list. |  |

## Appendix

### Additional Configurations for Data Transfer of Business Partner with SOAP Services

It is relevant for transferring business partner data, including customers, suppliers, and contact persons, via SOAP services. And it is only applicable to SAP Global Trade Services, edition for SAP HANA.

|  |
| --- |
| Caution Particularly when the multiple address handling is activated with the configuration activity Activate Multiple Address Handling in SD Documents Using SAP BP in the SAP SAP S/4HANA Cloud Public Edition system, the business partner data transfer with SOAP services is the only option for customer and contact person data transfer, and you are not allowed to use the SAP Fiori apps Schedule Transfer of Customers - Global Trade Services (F2806) and Schedule Transfer of Contact Persons - Global Trade Services (F2803) to transfer such customer and contact person data with RFC option. |

|  |
| --- |
| Note Before proceeding with the configurations outlined below, ensure that the integration for business partner replication via SOAP services has been set up in both your SAP S/4HANA Cloud Public Edition and your SAP GTS system. For further information, please refer to the Set-up Instructions for this scope item.Please note that the following configurations may vary according to your system environment, and the steps and input values may differ accordingly in your systems. |

#### Define Filter Criteria in SAP S/4HANA Cloud Public Edition System

Purpose

This step is to define the filter criteria to specify which data is replicated to the SAP Global Trade System.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Configuration Expert - Business Network Integration in SAP S/4HANA Cloud Public Edition system. |  |  |
| 2 | Access App | Choose Define Filter Criteria (F6519). | The Define Filter Criteria screen is displayed. |  |
| 3 | Choose Replication Model | Under the filter area, enter the following replication model and choose Go:Replication Model: <Select the replication model, for example S4BUPAGTS>Click on the selected replication model. |  | The replication model is defined in the step Create Communication Agreement of SAP_COM_0008, which is described in the Set-up Guide of this scope item. |
| 4 | Edit Main Filters | Choose Edit, and click on the filter object BP Service Filter (OTC 986) under the Main Filters area.Then, choose Create to add the filter entries to specify which business partners will be replicated, for example, including the BP roles FLCU01, FLVN01 and BUP001.Choose Apply. |  |  |
| 5 | Edit Segment Filters | Under the Segment Filters area, click on the specific filter objects to restrict data in replicated segments. For example, select the filter object Business Partner Role - 98601 to configure the segment filters. You can restrict segments of the BP role to include only specific roles, such as FLCU01 for customers, BUP001 for contact persons, and FLVN01 for suppliers.Choose Apply. |  |  |
| 6 | Save Filter Criteria | Choose Save. | The filter criteria are defined. |  |

#### Maintain Value Mapping in SAP Global Trade Services System

Purpose

This step is to configure mapping from system-internal code values to code values on external code lists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Transaction Code | In the Command field, enter VMIMG and press Enter. |  |  |
| 3 | Access the IMG Activity | From the IMG, go to the following path: Value Mapping > Maintain Value Mapping. | The Change View “Maintain Value Mapping Fields”: Overview view displays. |  |
| 4 | Choose the Entry for Mapping | Choose the entry of the Data Element object type and the MDG_FND_PARTY_ROLE_CODE global Data Type, and click on the Display mapping relationships button. | The Display View “Assign Code Lists”: Overview view displays. |  |
| 5 | Assign Code Lists | Choose Display > Change . Make the following entries and double-click Define Value Mapping:Mapping ID: <enter mapping ID>List Agency ID: <business system of SAP S/4HANA Cloud Public Edition system>List ID: MDG_FND_PARTY_ROLE_CODE |  |  |
| 6 | Define Value Mapping | Make the following entries and choose Save:Internal Code ValueExternal Code ValueCommentSLLCPCFLCU01CustomerSLLCPSFLVN01SupplierBUP001BUP001Contact Person | The value mapping is maintained.Note You have to define value mapping even if the corresponding business partner role is identical in both the SAP S/4HANA Cloud Public Edition and SAP GTS systems, such as the contact person role BUP001. |  |

#### Assign Code Lists to Elements and Systems in SAP Global Trade Services System

Purpose

This step is to assign the code lists to business systems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Transaction Code | In the Command field, enter VMIMG and press Enter. |  |  |
| 3 | Access the IMG Activity | From the IMG, go to the following path: Value Mapping > Assign Code Lists to Elements and Systems . | The Change View “Assign Code Lists to Elements and Systems”: Overview view displays. |  |
| 4 | Assign Code Lists to Elements and Systems | Choose New Entries. Make the following entries and choose Save:Type: Data ElementGlobal Data Type: MDG_FND_PARTY_ROLE_CODEBusiness System: <business system of SAP S/4HANA Cloud Public Edition system>List ID: MDG_FND_PARTY_ROLE_CODEList Agency ID: <business system of SAP S/4HANA Cloud Public Edition system> | The code list is assigned to SAP S/4HANA Cloud Public Edition system. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/test-script-transfer-of-primary-master-data-for-sap-global-trade-servi]]
- related-to :: [[13-quality-ehs-and-compliance/transfer-of-bill-of-materials-for-sap-global-trade-services-24h-ae-805]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24F_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 27,084 chars in the whole document
