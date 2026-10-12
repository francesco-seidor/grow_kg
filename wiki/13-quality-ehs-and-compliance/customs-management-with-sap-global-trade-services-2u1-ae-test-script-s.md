---
id: 13-quality-ehs-and-compliance/customs-management-with-sap-global-trade-services-2u1-ae-test-script-s
title: "Customs Management with SAP Global Trade Services (2U1_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2U1_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 2U1: integrating SAP S/4HANA Cloud Public Edition with SAP GTS for export management and import declaration before goods receipt."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/gts-customs-management]
aliases: [2U1_S4CLD2608_BPD_EN_AE]
keywords: [Customs Management with SAP GTS, customs management, document transfer settings, export management, import management, customs offices, gts configuration, business roles, foreign trade organization, message monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U1_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-866
topic: 13-quality-ehs-and-compliance/gts-customs-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Customs Management with SAP Global Trade Services (2U1_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2U1_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U1_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customs Management with SAP GTS** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customs Management with SAP Global Trade Services (2U1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850412)

[2 Prerequisites 4](#_Toc232850413)

[2.1 Additional Manual Configuration 4](#_Toc232850414)

[2.2 System Access 4](#_Toc232850415)

[2.3 Roles 4](#_Toc232850416)

[2.4 Business Conditions 6](#_Toc232850417)

[2.5 Master Data, Organizational Data, and Other Data 7](#_Toc232850418)

[2.6 Preliminary Steps 7](#_Toc232850419)

[2.6.1 Configure Control Settings for Document Transfer 7](#_Toc232850420)

[2.6.2 Create a Foreign Customer for Export Management 14](#_Toc232850421)

[2.6.3 Create a Foreign Supplier for Import Management 15](#_Toc232850422)

[2.6.4 Create a Customs Office for Export Management 15](#_Toc232850423)

[2.6.4.1 Create a Customs Office in SAP S/4HANA 16](#_Toc232850424)

[2.6.4.2 Create a Customs Office in SAP GTS 17](#_Toc232850425)

[2.6.4.3 Assign Customs Offices in SAP S/4HANA 17](#_Toc232850426)

[2.6.5 Define Customs Business Transaction Types 18](#_Toc232850427)

[2.6.6 Schedule Transfer of Duty-Paid Stock 19](#_Toc232850428)

[2.6.7 Schedule Transfer of Product Attributes 20](#_Toc232850429)

[3 Overview Table 21](#_Toc232850430)

[4 Test Procedures 22](#_Toc232850431)

[4.1 Export Management 22](#_Toc232850432)

[4.1.1 Create Sales Order to Foreign Customer 23](#_Toc232850433)

[4.1.2 Create Outbound Delivery 24](#_Toc232850434)

[4.1.3 Create Billing 25](#_Toc232850435)

[4.1.4 Check Transferred Documents in SAP Global Trade Services System 26](#_Toc232850436)

[4.2 Import Management - Customs Declaration Prior to Goods Receipt 28](#_Toc232850437)

[4.2.1 Create Purchase Document to Foreign Supplier 29](#_Toc232850438)

[4.2.2 Create Inbound Delivery 30](#_Toc232850439)

[4.2.3 Check Transferred Documents in SAP Global Trade Services System 31](#_Toc232850440)

[5 Appendix 34](#_Toc232850441)

[5.1 Additional Configurations in SAP Global Trade Services System 34](#_Toc232850442)

[5.1.1 Define Foreign Trade Organization 34](#_Toc232850443)

[5.1.2 Assign Company Code to Foreign Trade Organization 35](#_Toc232850444)

[5.1.3 Define Legal Units 35](#_Toc232850445)

[5.1.4 Assign Legal Unit to Foreign Trade Organization 36](#_Toc232850446)

[5.1.5 Assign Plant to Legal Unit 37](#_Toc232850447)

[5.1.6 Assign Partner Functions 37](#_Toc232850448)

[5.1.7 Define Legal Regulation 39](#_Toc232850449)

[5.1.8 Assign Document Types 39](#_Toc232850450)

[5.1.9 Assign Item Categories 40](#_Toc232850451)

[5.2 Message Monitoring and Troubleshooting using Application Interface Framework 41](#_Toc232850452)

## Purpose

Overview

SAP Global Trade Services Customs Management installations can be integrated with SAP S/4HANA Cloud Private Edition or SAP S/4HANA Cloud Public Edition to handle global trade scenarios for import before goods receipt and export management.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/98ac0508bbfbe878e746f90e7c5347db)

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Please ask your system administrator to assign to the testers. |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC | Please ask your system administrator to assign to the testers. |
| Administrator - International Trade | SAP_BR_ADMINISTRATOR_SLL | International Trade Administration | SAP_BR_ADMINISTRATOR_SLL | Please ask your system administrator to assign to the testers. |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC | Please ask your system administrator to assign to the testers. |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | Please ask your system administrator to assign to the testers. |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Please ask your system administrator to assign to the testers. |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | Please ask your system administrator to assign to the testers. |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Customs Specialist - Export (GTS) | SAP_BR_EXPORT_SPCLST_LLS | Customs Export | SAP_LLS_SP_EXPORT_SPCLST | This role template is used in SAP Global Trade Services, edition for SAP HANA. |
| Customs Specialist - Import (GTS) | SAP_BR_IMPORT_SPCLST_LLS | Customs Import | SAP_LLS_SP_IMPORT_SPCLST | This role template is used in SAP Global Trade Services, edition for SAP HANA. |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 1WA - Transfer of Primary Master Data for SAP Global Trade Services | The product master data has been transferred into SAP Global Trade Services system.The supplier master data, which is relevant for import purchasing document transfer, has been transferred into SAP Global Trade Services system.The customer master data, which is relevant for export sales document transfer, has been transferred into SAP Global Trade Services system. |

Additional Configurations in Global Trade Services

To make the master data transfer successful, additional configurations might be needed in SAP Global Trade Services system, for example the regions in address, the mapping of document types and partner functions. These configurations depend on your SAP Global Trade Services system, and are not covered in this document. The following are the minimum configurations needed:

- Company Code Mapping to FTO
- Plant Mapping to Legal Unit
- Partner Function Mapping
- Document Type and Item Category Mapping (Delivery, Purchasing Document)

|  |
| --- |
| Note You can check the details by referring to [Additional Configurations in SAP Global Trade Services System](#unique_7) [page ] 34. |

If the transfer is not successful, you may check the application logs in SAP Global Trade Services system to get the error details and then fix it.

### Master Data, Organizational Data, and Other Data

As the complete test steps in the SAP S/4HANA Cloud Public Edition system are described in the reference scope items, please refer to corresponding scope items which are listed in the chapter Test Procedures to get the related organizational data and master data information.

### Preliminary Steps

#### Configure Control Settings for Document Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you must switch on the transfer of relevant document types to the SAP Global Trade Services system using the SSCUI (Self Service Configuration User Interface).

Procedure

|  |
| --- |
| Note When you run this scope item for testing purposes, please do revert the configuration settings below once your testing is completed. Otherwise it will have the impact on other business processes and might block other testing. |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Choose Manage Your Solution (F1241), then choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 3 | Filter Display | Make the following entries and press Enter:Application Area: FinanceSub Application Area: Integration with SAP Global Trade Services |  |  |
| 4 | General Settings | Choose the arrow button at the right of the row for General Settings for Integration to SAP Global Trade Services. | The right pane opens to show relevant settings. |  |
| 5 | Control Settings for Document Transfer | In the right pane, for the Configure Control Settings for Document Transfer row, choose Configure. |  |  |
| 6 | SD0A Settings | Note The application level SD0A is relevant only for sales return. If you don't need customs management for your sales return, skip the settings for SD0A.Select the leftmost checkbox for the application level SD0A entry. In the Dialog Structure pane, double-click Document Types. |  |  |
| 7 | SD0A Settings | Note If you need to transfer documents of a sales order type that is not listed, create an appropriate sales order type by choosing New Entries.For the return order type you want to modify (for example, CBAR), select the leftmost checkbox, then choose Details.Under Control Settings, select Document Type for the Activation Level.Note To activate document transfer at the organization level, you need to select one of the organization levels for the Activation Level, such as Document Type/Company Code. After selecting this level, double-click on it in the left Dialog Structure pane, and then enable the document transfer for the organizations within the chosen level.You can select the organization level that best suits your requirements. The following organization levels are supported for the Activation Level:Document Type/Company CodeDocument Type/Sales OrganizationDocument Type/PlantDocument Type/Sales Organization and PlantDocument Type/Purchasing OrganizationDocument Type/Purchasing Organization and PlantCheck the Customs Management checkbox to enable the document transfer for this sales return order type. | The document transfer control settings have been configured for the selected sales order types. |  |
| 8 | Application Level | In the Dialog Structure pane, double-click Application Level. |  |  |
| 9 | SD0B Settings | Note The application level SD0B is relevant only for return deliveries. If you don't need customs management for your return deliveries, skip the settings for SD0B.Repeat steps 6 to 8 for the following data:Application Level: SD0BDoc.Type: LRNote Select New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected>Note If you want to hold the creation of a goods issue for the delivery when export permission has not yet been granted by customs, double-click on the delivery type row and select the Hold Goods Issue if Export Permission Is Missing checkbox. | The document transfer control settings have been configured for the selected outbound delivery types. |  |
| 10 | SD0C Settings | Repeat steps 6 to 8 for the following data:Application Level: SD0CDoc.Type: F8Note Select New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected>Transfer Documents for Customs Invoice: <Selected> (only if your business uses intercompany processes) | The document transfer control settings have been configured for the selected billing types. |  |
| 11 | MM0A Settings | Repeat steps 6 to 8 for the following data:Application Level: MM0ADoc.Type: FNBNote Select New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected> | The document transfer control settings have been configured for the selected purchasing document types. |  |
| 12 | MM0B Settings | Note This step is relevant for customs declaration based on inbound delivery. You can transfer the inbound delivery documents into SAP Global Trade Services system for customs declaration with this step.Repeat steps 6 to 8 for the following data:Application Level: MM0BDoc.Type: ELNote Choose New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected>Placement into Customs Status before Goods Receipt: <Selected>Note If you select the Compliance Management checkbox to activate the compliance check for the inbound delivery type, you don’t need to select the Placement into Customs Status before Goods Receipt checkbox.Note To prevent a goods receipt when customs unloading permission has not been granted, double-click on the delivery type row and select the Hold Goods Receipt if Unloading Permission Is Missing checkbox. | The document transfer control settings have been configured for the selected inbound delivery types. |  |
| 13 | MM0C Settings | Note This step is optional for the use case [Import Management - Customs Declaration Prior to Goods Receipt](#unique_10) [page ] 28.Repeat steps 6 to 8 for the following data:Application Level: MM0CDoc.Type: 101BNote Select New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected> | The document transfer control settings have been configured for the selected material movement types. |  |
| 14 | Save | Choose Save. | The settings are saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Control Settings for Document Transfer | Go to the Business Processes Configuration app and search for the following activity: Configure Control Settings for Document Transfer.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Control Settings for Document Transfer screen displays. |  |
| 3 | SD0A Settings | Note The application level SD0A is relevant only for sales return. If you don't need customs management for your sales return, skip the settings for SD0A.Select the leftmost checkbox for the application level SD0A entry. In the Dialog Structure pane, double-click Document Types. |  |  |
| 4 | SD0A Settings | Note If you need to transfer documents of a sales order type that is not listed, create an appropriate sales order type by choosing New Entries.For the return order type you want to modify (for example, CBAR), select the leftmost checkbox, then choose Details.Under Control Settings, select Document Type for the Activation Level.Note To activate document transfer at the organization level, you need to select one of the organization levels for the Activation Level, such as Document Type/Company Code. After selecting this level, double-click on it in the left Dialog Structure pane, and then enable the document transfer for the organizations within the chosen level.You can select the organization level that best suits your requirements. The following organization levels are supported for the Activation Level:Document Type/Company CodeDocument Type/Sales OrganizationDocument Type/PlantDocument Type/Sales Organization and PlantDocument Type/Purchasing OrganizationDocument Type/Purchasing Organization and PlantCheck the Customs Management checkbox to enable the document transfer for this sales return order type. | The document transfer control settings have been configured for the selected sales order types. |  |
| 5 | Application Level | In the Dialog Structure pane, double-click Application Level. |  |  |
| 6 | SD0B Settings | Note The application level SD0B is relevant only for return deliveries. If you don't need customs management for your return deliveries, skip the settings for SD0B.Repeat steps 3 to 5 for the following data:Application Level: SD0BDoc.Type: LRNote Select New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected>Note If you want to hold the creation of a goods issue for the delivery when export permission has not yet been granted by customs, double-click on the delivery type row and select the Hold Goods Issue if Export Permission Is Missing checkbox. | The document transfer control settings have been configured for the selected outbound delivery types. |  |
| 7 | SD0C Settings | Repeat steps 3 to 5 for the following data:Application Level: SD0CDoc.Type: F8Note Select New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected>Transfer Documents for Customs Invoice: <Selected> (only if your business uses intercompany processes) | The document transfer control settings have been configured for the selected billing types. |  |
| 8 | MM0A Settings | Repeat steps 3 to 5 for the following data:Application Level: MM0ADoc.Type: FNBNote Select New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected> | The document transfer control settings have been configured for the selected purchasing document types. |  |
| 9 | MM0B Settings | Note This step is relevant for customs declaration based on inbound delivery. You can transfer the inbound delivery documents into SAP Global Trade Services system for customs declaration with this step.Repeat steps 3 to 5 for the following data:Application Level: MM0BDoc.Type: ELNote Choose New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected>Placement into Customs Status before Goods Receipt: <Selected>Note If you select the Compliance Management checkbox to activate the compliance check for the inbound delivery type, you don’t need to select the Placement into Customs Status before Goods Receipt checkbox.Note To prevent a goods receipt when customs unloading permission has not been granted, double-click on the delivery type row and select the Hold Goods Receipt if Unloading Permission Is Missing checkbox. | The document transfer control settings have been configured for the selected inbound delivery types. |  |
| 10 | MM0C Settings | Note This step is optional for the use case [Import Management - Customs Declaration Prior to Goods Receipt](#unique_10) [page ] 28.Repeat steps 3 to 5 for the following data:Application Level: MM0CDoc.Type: 101BNote Select New Entries to configure the document type if it is not listed.Activation Level: Document TypeCustoms Management: <Selected> | The document transfer control settings have been configured for the selected material movement types. |  |
| 11 | Save | Choose Save. | The settings are saved. |  |

#### Create a Foreign Customer for Export Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before you start the business process, you must create a foreign customer for export management if one does not exist.

Procedure

|  |
| --- |
| Note The customer must be a foreign customer.Once the new foreign customer is created, see the Transfer of Primary Master Data for SAP Global Trade Services (1WA) scope item to transfer the customer data into the SAP Global Trade Services system.No detailed procedure is given here. For more information on creating the foreign customer, see the Create Customer Master - MDS (BND) master data script. |

#### Create a Foreign Supplier for Import Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before you start the business process, you must create a foreign supplier for import management if one does not exist.

Procedure

|  |
| --- |
| Note The supplier must be a foreign supplier.Once the new foreign supplier is created, see the Transfer of Primary Master Data for SAP Global Trade Services (1WA) scope item to transfer the supplier data into the SAP Global Trade Services system.No detail procedure is given here. For more information on creating the foreign supplier, see the Create Supplier Master - MDS (BNE) master data script. |

#### Create a Customs Office for Export Management

Before you start the business process of export management, you can create customs office data and maintain the customs office assignment. Once this is done, the customs office can be determined when you create documents in SAP S/4HANA, and the determined customs office can be sent to SAP Global Trade Services during the document transfer (doing away with the need to to manually maintain it in SAP Global Trade Services).

##### Create a Customs Office in SAP S/4HANA

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Choose Maintain Business Partner (BP). |  |  |
| 3 | Organization | Choose Organization. | The Create Organization view is displayed. |  |
| 4 | Choose Business Partner Role | Make the following entries:Create in BP role: Customs OfficeChoose Create on the Change to another BP role in the create mode dialog box. | The Change to another BP role in create mode dialog box is displayed. |  |
| 5 | Create Customs Office | Choose Create. |  |  |
| 6 | Maintain Address Data | Enter standard address information for the customs office (such as Name, Country, Region, and so on). |  |  |
| 7 | Identification | Choose the Identification tab. |  |  |
| 8 | Maintain Customs Office Number | In the Identification Numbers area, make the following entries and choose Save:ID Type: SLLCID Customs Office NumberIdentification Number: <enter the customs office number>Note The Identification Number field is limited to eight characters. | Make a note of the business partner number and the customs office number. |  |

##### Create a Customs Office in SAP GTS

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. |  |  |
| 2 | Run Transaction | In the Command field, enter transaction code BP and press Enter. | The Maintain Business Partner screen is displayed. |  |
| 3 | Organization | Choose Organization. |  |  |
| 4 | Choose BP Role | Make the following entries:Create in BP role: Customs Office | The Change to another BP role in create mode dialog box displays. |  |
| 5 | Create Customs Office | Choose Create. |  |  |
| 6 | Maintain Address Data | Enter basic information for the customs office (for example Title, Name, Country, Region, and the detailed address).Note Ensure that this data matches the values you maintained in the SAP S/4HANA system. |  |  |
| 7 | Identification | Choose the Identification tab. |  |  |
| 8 | Maintain Customs Office Number | In the Identification Numbers section, make the following entries and choose Save:External BP Number: <enter the BP number created in SAP S/4HANA>ID Type: SLLCID Customs Office NumberIdentification Number: <enter the customs office number>Note The Identification Number field is limited to eight characters. | Make a note of the business partner number. |  |

##### Assign Customs Offices in SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. |  |  |
| 2 | Access App | Choose Assign Customs Offices to Countries (/SAPSLL/CUS_OFF_CO). | The Change View Assign Customs Offices to Countries: Overview view is displayed.Note The system provides two options to assign the customs offices. One is based on the countries/regions; other is based on the routes. If you need to assign it to routes, please access the Assign Customs Offices to Routes (/SAPSLL/CUS_OFF_RO) app. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Assign Customs Offices | Make the following entries and choose Enter:Dep. Ctry: <departure country/region from which the goods are delivered to the customer>, for example, DEDest. Ctry: <destination country/region where the customer is located and where the goods are delivered to the customer>Partn. Role: <partner role>, for example, Office of ExitCustoms Office BP: <customs office business partner number you created previously> |  |  |
| 5 | Save | Choose Save. |  |  |

#### Define Customs Business Transaction Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is not a mandatory step. It's relevant for export management, which determines the Customs Business Transaction Types during the transfer of sales documents to SAP Global Trade Services.

Procedure

Define the Customs Business Transaction Types, and then assign the types to sales document item categories. Make sure these Customs Business Transaction Types are defined in SAP Global Trade Services system as well.

It depends on your business, hence no details are given here. In SAP S/4HANA Cloud Public Edition system, you have to perform the following configuration activities using SSCUIs (Self-Service Configuration User Interface).

- Define Customs Business Transaction Types
- Define Default Values for Customs Business Transaction Types

Once the Customs Business Transaction Types are defined and assigned, the Customs Business Transaction Types can be determined during the transfer of sales documents, and the determined Customs Business Transaction Types are available on customs declarations in SAP Global Trade Services.

#### Schedule Transfer of Duty-Paid Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is not a mandatory step. It's relevant for the processing of customs procedures that have an economic impact (for example, customs warehousing, inward processing, processing trade, or foreign-trade zone).

Procedure

The App Schedule Transfer of Duty-Paid Stock - Global Trade Services (F5702) allows you to perform the initial transfer of duty-paid stock to SAP Global Trade Services system. You can log onto the SAP Fiori launchpad to access the App by using the role Administrator - International Trade.

Before you use this app to schedule the application job to execute the transfer of duty-paid stock, you need to conduct some configuration settings in both SAP S/4HANA Cloud Public Edition system and SAP Global Trade Services system.

These configuration settings depend on your business. Hence no details are given here. In SAP S/4HANA Cloud Public Edition, you can perform these configuration activities using the SSCUIs (Self-Service Configuration User Interface).

- Customs Procedures with Economic Impact - Define Customs ID
- Customs Procedures with Economic Impact - Assign Customs ID
- Customs Procedures with Economic Impact (OP) - Assign Customs ID

#### Schedule Transfer of Product Attributes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is not a mandatory step, and it's relevant for the special customs procedures only. It provides the option to maintain and transfer the product attributes which are used for special customs procedures.

Procedure

The App Schedule Transfer of Product Attributes - Global Trade Services (F7231) allows you to schedule the application jobs to transfer the product attributes for special customs procedures from SAP S/4HANA system to SAP Global Trade Services system. You can log onto the SAP Fiori launchpad to access the App by using the role Administrator - International Trade.

Before you use this App to schedule the application jobs to transfer the product attributes, some configuration settings are required in both SAP S/4HANA system and SAP Global Trade Services system, for example customs ID creation and assignment. Also the product master data needs to be transferred to SAP Global Trade Services system in advance.

The configuration settings and the transfer procedures depend on your business. Hence no details are given here.

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Export Management](#unique_21) [page ] 22 |  |  |  |
| [Create Sales Order to Foreign Customer](#unique_22) [page ] 23 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order is created |
| [Create Outbound Delivery](#unique_23) [page ] 24 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | The outbound delivery is created and goods issue is posted |
| [Create Billing](#unique_24) [page ] 25 | Billing Clerk | Create Billing Documents - VF01 (VF01) | The billing document is created |
| [Check Transferred Documents in SAP Global Trade Services System](#unique_25) [page ] 26 | The business role is applicable to SAP Global Trade Services, edition for SAP HANA:Customs Specialist - Export (GTS) | /n/SAPSLL/MENU_LEGALThe App is applicable to SAP Global Trade Services, edition for SAP HANA:Docs for Customs Export Declarations(/SAPSLL/CUHD_DOC_EXP) | The transferred document is in SAP Global Trade Services system |
| [Import Management - Customs Declaration Prior to Goods Receipt](#unique_10) [page ] 28 |  |  |  |
| [Create Purchase Document to Foreign Supplier](#unique_26) [page ] 29 | Purchaser | Create Purchase Order - Advanced (ME21N) | The purchase document is created |
| [Create Inbound Delivery](#unique_27) [page ] 30 | Receiving Specialist | Create Inbound Delivery (VL31N) | The inbound delivery is created |
| [Check Transferred Documents in SAP Global Trade Services System](#unique_28) [page ] 31 | The business role is applicable to SAP Global Trade Services, edition for SAP HANA:Customs Specialist - Import (GTS) | /n/SAPSLL/MENU_LEGALThe App is applicable to SAP Global Trade Services, edition for SAP HANA:Create Import Declaration Before Goods Receipt(/SAPSLL/CIBD_01) | The transferred document is in SAP Global Trade Services system |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Export Management

|  |
| --- |
| Caution Before you start the test procedures, ensure that the Set-up Instruction Guide of this scope item is executed to ensure working connectivity between the SAP S/4HANA Cloud Public Edition system and the SAP Global Trade Services system. |

|  |
| --- |
| Caution Run the export management processes with the foreign customer. |

|  |
| --- |
| Note The plant abroad integration for export processing with SAP Global Trade Services is supported when the scope item 5RP is activated in the SAP S/4HANA Cloud Public Edition system. Additionally, to enable this functionality, implement SAP Note [3664693](https://me.sap.com/notes/3664693) in the SAP Global Trade Services system.Once the billing document for the plant abroad scenario is created and transferred to the SAP Global Trade Services system, the foreign trade organization is determined and used for the export declaration, which is based on the abroad plant's country. For this use case, you may access the Display Export Declarations app and check whether the determined foreign trade organization (assigned to the legal unit corresponding to the abroad plant) is available on the Partners tab of the export customs declaration document header. |

|  |
| --- |
| Note As the document transfer is automatically triggered when you save the document in the SAP S/4HANA Cloud Public Edition system, follow the complete procedures that are described in the reference scope items to create the documents, as shown in the table below (with document type and associated scope items): |

| Process | Document Type | Scope Item |
| --- | --- | --- |
| Export – Outbound Delivery | LF (Outbound Delivery) | BD9 - Sell from StockBDH - Sales Order Entry with One-Time CustomerBDN - Sales of Non-Stock Item with Order-Specific ProcurementBDW - Returnables ProcessingBKJ - Sales Order Processing with Customer Down Payment1MX - Intercompany Sales Order Processing – International |
|  | NLCC (Replen.Cross-Company) | 1P9 - Intercompany Stock Transfer |
| Export – Billing | F2 (F2 Invoice) | BD9 - Sell from StockBDH - Sales Order Entry with One-Time CustomerBDN - Sales of Non-Stock Item with Order-Specific ProcurementBDW - Returnables ProcessingBKJ - Sales Order Processing with Customer Down Payment1MX - Intercompany Sales Order Processing – International |
|  | F8 (Pro Forma Invoice for Delivery) | BDA - Free of Charge Delivery |
|  | CBST (Intercompany Billing for STO) | 1P9 - Intercompany Stock Transfer |

#### Create Sales Order to Foreign Customer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a sales order to the foreign customer.

|  |
| --- |
| Note If the sales order is blocked for approval, follow the Complete the Process Sales Order Approval steps described in the Sell from Stock (BD9) test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. |  |  |
| 2 | Access App | Choose Manage Sales Orders (F1873). |  |  |
| 3 | Enter Order Type | Choose Create Sales Orders - VA01. | The Create Sales Documents view displays. |  |
| 4 | Order Details | Make the following entries and press Enter:Order Type: for example ORSales Organization: 3310Distribution Channel: 10Division: 00 | The order type and sales organization are chosen. The Create Standard Order: Overview view displays. |  |
| 5 | Order Details | Make the following entries and choose Save:Sold-To Party: <foreign customer number>Ship-To Party: <foreign customer number>Customer Reference: <reference number>Material: <material number>Order Quantity: <quantity> | The sales order is saved.Note In order to create the subsequent outbound delivery, the confirmed schedule line has to be available in the sales order. You can execute Item Availability check to analyze the situation and make the schedule line confirmed. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Choose Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery with Order Reference screen is displayed. |  |
| 3 | Search Sales Order | Make the following entries and press Enter:Shipping Point: 3310Selection Date: <delivery selection date>Order: <sales order number> | The Outbound Delivery Create: Overview view displays. |  |
| 4 | Picking | Choose the Picking tab. |  |  |
| 5 | Create Outbound Delivery | Make the following entries and choose Post Goods Issue:Picked Qty: <quantity> | The outbound delivery is created. |  |

#### Create Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Choose Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen is displayed. |  |
| 3 | Create Billing Document | Make the following entry and choose Save:Billing Type: F8 Pro Forma Invoice for DeliveryDocument: <outbound delivery number> | The billing document is created.Note To check the messages, see [Message Monitoring and Troubleshooting using Application Interface Framework](#unique_30) [page ] 41. |  |

#### Check Transferred Documents in SAP Global Trade Services System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the transferred document in the SAP Global Trade Services system.

Procedure

|  |
| --- |
| Note If your GTS system is SAP Global Trade Services, edition for SAP HANA, the steps are different, so please check the steps after this section. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter /n/SAPSLL/MENU_LEGAL and press Enter. | The SAP Global Trade Services view displays. |  |
| 3 | Export | In the Customs Management area, choose Export. | The Customs Management: Export view displays. |  |
| 4 | Display Outbound Activities | In the Operative Cockpit area, choose the Execute icon for Display Outbound Activities. | The Display Outbound Activities view displays. |  |
| 5 | Filter Values | Make the following entries and press Enter:Reference Number: <reference number>Logical System: <logical system> |  |  |
| 6 | Check Transferred Document | Check the billing documents for customs processing. To check the customs office, double-click the document and choose the Geography tab. | The customs office and customs office number are shown in the Customs Offices area.The transferred export documents are checked.Note If Business Transaction Type has been defined in the preliminary step [Define Customs Business Transaction Types](#unique_17), it shows up:under the Transportation tab on the header level, when the document items have the same Business Transaction Type.under the General Data tab on the item level, when the document items have different Business Transaction Types. |  |

|  |
| --- |
| Note The following steps are applicable to SAP Global Trade Services, edition for SAP HANA. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Customs Specialist - Export (GTS). |  |  |
| 2 | Access App | Choose Docs for Customs Export Declarations (/SAPSLL/CUHD_DOC_EXP ). | The Display Documents for Customs Export Declarations view displays. |  |
| 3 | Filter Values | Make the following entries and choose Execute:FT Organizational Unit: <foreign trade organization, for example, FTO_3310> |  |  |
| 4 | Check Transferred Documents | Check the billing documents for customs processing. To check the customs office, double-click the document and choose the Geography tab. | The customs office and customs office number are shown in the Customs Offices area.The transferred export documents are checked.Note If Business Transaction Type has been defined in the preliminary step [Define Customs Business Transaction Types](#unique_17), it shows up:under the Transportation tab on the header level, when the document items have the same Business Transaction Type.under the General Data tab on the item level, when the document items have different Business Transaction Types. |  |

### Import Management - Customs Declaration Prior to Goods Receipt

|  |
| --- |
| Caution Before you start the test procedures, ensure that the Set-up Instruction Guide of this scope item is executed to ensure working connectivity between the SAP S/4HANA system and the SAP Global Trade Services system. |

|  |
| --- |
| Caution Run the import management processes with the foreign supplier. |

|  |
| --- |
| Note The following Apps are available for initial transfer of documents, and you can log onto the SAP Fiori launchpad to access these Apps by using the role Administrator - International Trade:Schedule Transfer of Purchasing Documents - Global Trade Services (F3742)Schedule Transfer of Inbound Deliveries - Global Trade Services (F4541) |

|  |
| --- |
| Note As the document transfer is automatically triggered when you save the document in the SAP S/4HANA system, follow the complete procedures that are described in the reference scope items to create the documents, as shown in the table below (with document type and associated scope items): |

| Process | Document Type | Scope Item |
| --- | --- | --- |
| Import – Purchasing | NB (F - Purchase Order, Standard PO) | J45 - Procurement of Direct MaterialsBMD - Purchase Contract |
|  | LP (L - Scheduling Agreement, Scheduling Agreement) | BMR - Scheduling Agreements in Procurement2NX - Scheduling Agreement for Subcontracting Procurement2NY - Scheduling Agreement for Consignment Procurement |
| Import – Inbound Delivery | EL (Inbound Delivery) | 2TX - Direct Procurement with Inbound DeliveryBD3 - Sales Processing using Third-Party with Shipping Notification |
| Import – Material Document | 101B (GR goods receipt)102B (GR for PO reversal) | 2TX - Direct Procurement with Inbound DeliveryBD3 - Sales Processing using Third-Party with Shipping Notification |

#### Create Purchase Document to Foreign Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a purchase document to the foreign supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Choose Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed. |  |
| 3 | Purchase Document | Make the following entries and choose Save:Order Type: for example, NB Standard POSupplier : <enter your foreign supplier number>Header section:Org. Data tab:Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310Item Overview section:Material: <material number>PO Quantity: <enter the quantity>Net Price: <enter the price>Plant: 3310Storage Location: 331AItem Detail section:Confirmation tab:Conf. Control: Inbound Delivery | The purchase document is saved. |  |

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access App | Choose Create Inbound Delivery (VL31N). | The Create Inbound Delivery screen is displayed. |  |
| 3 | Create Inbound Delivery | Make the following entries and press Enter:Supplier : <enter your foreign supplier>Purchase Order: <the created purchase document number>Delivery Date: <the delivery selection date> |  |  |
| 4 | Save | Choose Save. | The inbound delivery is created.Note To check the messages, see [Message Monitoring and Troubleshooting using Application Interface Framework](#unique_30) [page ] 41 |  |

#### Check Transferred Documents in SAP Global Trade Services System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the transferred document in the SAP Global Trade Services system.

Procedure

|  |
| --- |
| Note If your GTS system is SAP Global Trade Services, edition for SAP HANA, the steps are different, so please check the steps after this section. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter /n/SAPSLL/MENU_LEGAL and press Enter. | The SAP Global Trade Services view displays. |  |
| 3 | Import | In the Customs Management area, choose Import. | The Customs Management: Import view displays. |  |
| 4 | Create and Process Custom Declaration | In the Create and Process Customs Declarations area, choose the Execute icon for Create Declaration Prior to Goods Receipt. | The Create Import Declaration Prior to Goods Receipt view displays. |  |
| 5 | Filter Values | On the Purchase Orders tab, make the following entries and choose Execute:Foreign Trade Organization: <foreign trade organization, for example, FTO_3310>Document Number: <reference number>Logical System: <logical system> |  |  |
| 6 | Check Transferred Document | Check the purchasing documents in the before-goods-receipt worklist. | The transferred documents are checked. |  |

|  |
| --- |
| Note The following steps are applicable to SAP Global Trade Services, edition for SAP HANA. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Customs Specialist - Import (GTS). |  |  |
| 2 | Access App | Choose Create Import Declaration Before Goods Receipt (/SAPSLL/CIBD_01 ). | The Create Import Declaration Prior to Goods Receipt view displays. |  |
| 3 | Filter Values | On the Purchase Orders tab, make the following entries and choose Execute:Foreign Trade Organization: <foreign trade organization, for example, FTO_3310>Document Number: <reference number>Logical System: <logical system> |  |  |
| 4 | Check Transferred Documents | Check the purchasing documents in the before-goods-receipt worklist. | The transferred documents are checked. |  |

## Appendix

### Additional Configurations in SAP Global Trade Services System

The following configurations depend on your SAP Global Trade Services system, and the steps and input values might be different in your system.

#### Define Foreign Trade Organization

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | In the IMG, go to the following path: SAP Global Trade Services > General Settings > Organizational Structure > Define Foreign Trade Organization. |  |  |
| 4 | Maintain Foreign Trade Organization | Define the foreign trade organization, for example FTO_3310 and maintain the general data (such as name and address).Caution When entering an address, pay attention to the country/region. For example, if your company is located in Germany and runs export or import businesses with foreign partners, you must maintain the country/region key DE here. | The foreign trade organization is maintained or checked. |  |

#### Assign Company Code to Foreign Trade Organization

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | In the IMG, go to the following path: SAP Global Trade Services > General Settings > Organizational Structure > Assignment of Organizational Units from Feeder System to Foreign Trade Org. > Assign Company Code at Feeder System Group Level. | The Choose Activity dialog box displays. |  |
| 4 | Assign Company Code | Choose Manually Assign Company Code. | The Change View “Mapping: Company Code Group VS to Organizational Unit” view displays. |  |
| 5 | Assign Company Code to Foreign Trade Organization | Choose New Entries.If necessary, make the following entries and choose Save:Logical System group: <choose the logical system group>FS Organization: <your company code in SAP S/4HANA, for example, 3310>FT Organization: <your created foreign trade organization, for example, FTO_3310> | The company code is assigned to the foreign trade organization. |  |

#### Define Legal Units

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | From the IMG, go to the following path: SAP Global Trade Services > General Settings > Organizational Structure > Define Legal Units. |  |  |
| 4 | Maintain Legal Units | Define the legal unit, for example LU_3310 and maintain the general data, for example name and address. | The legal unit is maintained or checked. |  |

#### Assign Legal Unit to Foreign Trade Organization

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | From the IMG, go to the following path: SAP Global Trade Services > General Settings > Organizational Structure > Assign Legal Unit to the Foreign Trade Organization . |  |  |
| 4 | New Entries | Choose New Entries. |  |  |
| 5 | Assign Legal Unit to Foreign Trade Organization | If necessary, make the following entries:Legal Unit: <your created legal unit, for example, LU_3310>Foreign Trade Organization: <your created foreign trade organization, for example, FTO_3310>Choose Save. | The legal unit is assigned to the foreign trade organization. |  |

#### Assign Plant to Legal Unit

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | In the IMG, go to the following path: SAP Global Trade Services > General Settings > Organizational Structure > Assignment of Organizational Units from Feeder System to Legal Unit > Assign Plant at Feeder System Group Level. | The Choose Activity dialog box displays. |  |
| 4 | Assign Plant | Choose Manually Assign Plant. | The Change View “Mapping: Plant from Feeder System Group to Legal Unit” view displays. |  |
| 5 | New Entries | Choose New Entries. |  |  |
| 6 | Assign Plant to Legal Unit | If necessary, make the following entries and choose Save:Logical System group: <choose the logical system group>FS Organization: <your plant in SAP S/4HANA, for example, 3310>Legal Unit: <your created legal unit, for example, LU_3310>Choose Save. | The plant is assigned to the legal unit. |  |

#### Assign Partner Functions

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | From the IMG, go to the following path: SAP Global Trade Services > General Settings > Partner Structure > Assignment of Partner Functions from Feeder Systems > Assign Partner Function at Feeder System Group Level. | The Choose Activity dialog box displays. |  |
| 4 | Assign Partner Functions | Choose Manually Assign Partner Function. | The Change View “Mapping: Partner Function in FS Group to SAP GTS” view displays. |  |
| 5 | Assign Partner Functions | Choose New Entries.If necessary, make the following entries and choose Save:Logical System GroupBS Partner FunctionPartner Function<logical system group>AGAG<logical system group>WEWE<logical system group>RERE<logical system group>RGRG<logical system group>LFLF<logical system group>DAPODLV<logical system group>RSRS<logical system group>WLWL | The partner function mapping is maintained.Note These entries depend on your feeder systems, and they may not be the same in your systems. |  |

#### Define Legal Regulation

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > General Settings > Legal Regulations > Define Legal Regulation . | The IMG path is navigated. |  |
| 3 | Define Legal Regulation | On the Change View “Legal Regulation: Overview” screen, make sure the legal regulation with legal code 01 Customs Processing is defined for your country/region, for example, the legal regulation ATLAS is defined for Germany. | The defined legal regulation is checked. |  |

#### Assign Document Types

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > General Settings > Document Structure > Assignment of Document Types from Feeder Systems > Assign Document Type at Feeder System Group Level . | The IMG path is navigated. |  |
| 3 | Assign Document Types | Choose Manually Assign Document Type on the Choose Activity dialog box.On the Change View “Mapping: Feeder System Group Doc. Type to SAP GTS Doc. Ty” screen, choose New Entries and make the following entries if you haven’t maintained it:Application LevelLogical System GroupDoc. Type Feed. Sys.Document TypeSD0B<logical system group>for example LFEXPDLVMM0A<logical system group>for example FNBIMPORDMM0B<logical system group>for example ELDTAVIChoose Save. | The document type mapping is maintained. |  |

#### Assign Item Categories

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > General Settings > Document Structure > Assignment of Item Categories from Feeder Systems > Assign Item Category at Feeder System Group Level . | The IMG path is navigated. |  |
| 3 | Assign Item Categories | Choose Manually Assign Item Category on the Choose Activity dialog box.On the Change View “Mapping: FS Item Cat. Group to SAP GTS Item Cat. Group” screen, choose New Entries and make the following entries if you haven’t maintained it:Application LevelLogical System GroupItem Category (FS)Item CategorySD0B<logical system group>for example TANEXDLV1MM0A<logical system group>IMORD1MM0B<logical system group>for example ELNIMORD1Choose Save. | The item category mapping is maintained. |  |

### Message Monitoring and Troubleshooting using Application Interface Framework

Purpose

You can use the SAP Application Interface Framework to monitor interfaces as well as execute error handling.

|  |
| --- |
| Note For detailed information on the Application Interface Framework, go to the [SAP Help Portal](http://help.sap.com/) and search for SAP Application Interface Framework product page. In the Operations, open Application Help for SAP Application Interface Framework. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Assign Recipients to Users (F2949). | The Assign Recipients to User screen is displayed. |  |
| 3 | Assign Recipients to User | On the Assign Recipients to User screen, if the current logon user is not added yet, choose Add User to add the current logon user, and the select the user.Choose Assign, and make the following entries in the Assign Recipients dialog box:Namespace: /SLLPIRecipient Name: RFC_GTS_INTEGRAIONMessage Type: Application Error or Technical ErrorOverview: XTechnical User: XChoose Assign. | The recipient is assigned to the user. |  |
| 4 | Access App | Choose Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). | The Interface Monitor screen is displayed. |  |
| 5 | Monitor Interfaces | On the Interface Monitor screen, check the status of the interface SAP GTS Integration - /SLLPI, and execute error handling if necessary. | The messages in the interface are checked.Note For detailed information, go to the Application Help for SAP Application Interface Framework on the [SAP Help Portal](http://help.sap.com/). |  |

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
- see-also :: [[13-quality-ehs-and-compliance/test-script-transfer-of-primary-master-data-for-sap-global-trade-servi]]
- see-also :: [[13-quality-ehs-and-compliance/test-script-embargo-control-1wc-ae-sap-s-4hana-cloud-public-edition-76]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U1_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 67,777 chars in the whole document
