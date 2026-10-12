---
id: 13-quality-ehs-and-compliance/test-script-preference-management-with-sap-global-trade-services-3jx-a
title: "Test Script: Preference Management with SAP Global Trade Services (3JX_AE) (3JX_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 3JX_AE: SAP GTS Preference Management with S/4HANA Cloud Public Edition, covering LTSD worklists and configurable materials."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/gts-compliance-and-preference]
aliases: [3JX_S4CLD2608_BPD_EN_AE]
keywords: [SAP GTS Compliance and Preference Management Integration, preference management, long-term vendor declarations, global trade services integration, preference determination, configurable materials, document transfer settings, master data transfer, background jobs, gts configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3JX_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-948
topic: 13-quality-ehs-and-compliance/gts-compliance-and-preference
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Preference Management with SAP Global Trade Services (3JX_AE) (3JX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3JX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **SAP GTS Compliance and Preference Management Integration** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Preference Management with SAP Global Trade Services (3JX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232853010)

[2 Prerequisites 5](#_Toc232853011)

[2.1 Additional Manual Configuration 5](#_Toc232853012)

[2.2 System Access 5](#_Toc232853013)

[2.3 Roles 5](#_Toc232853014)

[2.4 Business Conditions 7](#_Toc232853015)

[2.5 Master Data, Organizational Data, and Other Data 7](#_Toc232853016)

[2.6 Preliminary Steps 8](#_Toc232853017)

[2.6.1 Preliminary Steps in S/4HANA Cloud System 8](#_Toc232853018)

[2.6.1.1 Prerequisite Configuration Activities 8](#_Toc232853019)

[2.6.1.2 Create a Supplier for Preference Processing 12](#_Toc232853020)

[2.6.1.3 Create a Customer for Preference Processing 13](#_Toc232853021)

[2.6.1.4 Schedule Transfer of Procurement Indicators 13](#_Toc232853022)

[2.6.1.5 Schedule Transfer of Product Prices 15](#_Toc232853023)

[2.6.1.6 Schedule Transfer of Minimum /Maximum Product Prices 16](#_Toc232853024)

[2.6.1.7 Schedule Transfer of Suppliers Product Name (Optional) 17](#_Toc232853025)

[2.6.1.7.1 Create Purchasing info Record 17](#_Toc232853026)

[2.6.1.7.2 Schedule Transfer of Suppliers Product Name 18](#_Toc232853027)

[2.6.1.8 Schedule Transfer of Customer Product Name (Optional) 19](#_Toc232853028)

[2.6.1.8.1 Create Customer Material Info Record 19](#_Toc232853029)

[2.6.1.8.2 Schedule Transfer of Customer Product Name 20](#_Toc232853030)

[2.6.1.9 Schedule Transfer of Changed Master Data 21](#_Toc232853031)

[2.6.2 Preliminary Steps in Global Trade Services System 23](#_Toc232853032)

[2.6.2.1 Transfer Determination of Preference Agreement to Feeder System 23](#_Toc232853033)

[2.6.2.2 Display Product Master in Global Trade Services System 24](#_Toc232853034)

[3 Overview Table 27](#_Toc232853035)

[4 Test Procedures 29](#_Toc232853036)

[4.1 Display Worklist for Vendor-Based Long-Term Vendor Declaration 29](#_Toc232853037)

[4.1.1 Create Purchase Document to Supplier 30](#_Toc232853038)

[4.1.2 Post Goods Receipt 31](#_Toc232853039)

[4.1.3 Schedule Transfer of Purchasing Documents - Global Trade Services (Optional) 32](#_Toc232853040)

[4.1.4 Schedule Transfer of Material Documents - Global Trade Services (Optional) 33](#_Toc232853041)

[4.1.5 Display the Worklist for Purchasing Documents/Material Document 34](#_Toc232853042)

[4.2 Display Worklist for Long-term Vendor Declaration for Customer's Purpose 36](#_Toc232853043)

[4.2.1 Create Sales Order to Customer 37](#_Toc232853044)

[4.2.2 Create Outbound Delivery 38](#_Toc232853045)

[4.2.3 Create Billing 39](#_Toc232853046)

[4.2.4 Schedule Transfer of Billing Documents - Global Trade Services (Optional) 40](#_Toc232853047)

[4.2.5 Display the Worklist: Long-Term Vendor Declaration for Customer’s Purpose 41](#_Toc232853048)

[4.3 Preference Determination for Configurable Materials (Optional) 43](#_Toc232853049)

[4.3.1 Create Sales Order with Configurable Material 43](#_Toc232853050)

[4.3.2 Explode and Transfer Configurable Materials 45](#_Toc232853051)

[4.3.3 Perform Preference Determination for Documents 46](#_Toc232853052)

[4.3.4 Schedule Reprocessing of Documents 47](#_Toc232853053)

[4.3.5 Display Worklist of Configurable Materials 48](#_Toc232853054)

[4.3.6 Production Process for Sales Order 49](#_Toc232853055)

[4.3.7 Create Outbound Delivery 50](#_Toc232853056)

[4.3.8 Create Billing 51](#_Toc232853057)

[4.3.9 Check the Billing 51](#_Toc232853058)

[5 Appendix 53](#_Toc232853059)

[5.1 Additional Configurations in SAP Global Trade Services System 53](#_Toc232853060)

[5.1.1 Define Legal Units 53](#_Toc232853061)

[5.1.2 Assign Plant to Legal Unit 54](#_Toc232853062)

[5.1.3 Define Cross-Plant BOM Evaluation 54](#_Toc232853063)

[5.1.4 Assign Partner Functions 55](#_Toc232853064)

[5.1.5 Define Administrative Unit for Vendor Declarations 56](#_Toc232853065)

[5.1.6 Define Administrative Unit Attributes 57](#_Toc232853066)

[5.1.7 Define Legal Regulation 57](#_Toc232853067)

[5.2 Additional Configurations in SAP Global Trade Services System with edition for SAP HANA 2020 SP01 or higher 58](#_Toc232853068)

[5.2.1 Define Legal Units 58](#_Toc232853069)

[5.2.2 Assign Plant to Legal Unit 59](#_Toc232853070)

[5.2.3 Define Cross-Plant BOM Evaluation 59](#_Toc232853071)

[5.2.4 Assign Partner Functions 60](#_Toc232853072)

[5.2.5 Define Legal Regulation 61](#_Toc232853073)

[5.2.6 Define Administrative Unit for Vendor Declarations 61](#_Toc232853074)

[5.2.7 Define Administrative Unit Attributes 61](#_Toc232853075)

[5.2.8 Define Settings for the LTSD Process 62](#_Toc232853076)

[5.2.9 Activate Documents of Origin 63](#_Toc232853077)

[5.2.10 Assign Action Profiles 64](#_Toc232853078)

[5.2.11 Assign Text Modules 64](#_Toc232853079)

[5.3 Message Monitoring and Troubleshooting using Application Interface Framework 66](#_Toc232853080)

## Purpose

Overview

This scope item integrates SAP Global Trade Services Preference Management with SAP S/4HANA Private Edition or SAP S/4HANA Cloud Public Edition. Customers can use their existing SAP Global Trade Services installations to manage long-term vendor declarations and the preference determination for static bills of materials.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b3b815dfc7f33a4d7bd1c56e066f9a54)

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
| Administrator - International Trade | SAP_BR_ADMINISTRATOR_SLL | International Trade Administration | SAP_BR_ADMINISTRATOR_SLL | Please ask your system administrator to assign to the testers. |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC | Please ask your system administrator to assign to the testers. |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | Please ask your system administrator to assign to the testers. |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Please ask your system administrator to assign to the testers. |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | Please ask your system administrator to assign to the testers. |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK | Please ask your system administrator to assign to the testers. |

### Business Conditions

The business processes described in this test script are part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to go through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 1WA - Transfer of Primary Master Data for SAP Global Trade Services | The product master data has been transferred into SAP Global Trade Services system.The components of the products has been transferred into SAP Global Trade Services system.The supplier master data, which is relevant for import purchasing document transfer, has been transferred to SAP Global Trade Services system.The customer master data, which is relevant for export sales document transfer, has been transferred to SAP Global Trade Services system. |
| 24H - Transfer of Bill of Materials for SAP Global Trade Services | The bill of materials master data have been transferred to SAP Global Trade Services system. |

Additional Configurations in SAP Global Trade Services System:

To make the master data transfer successful, additional configurations might be needed in SAP Global Trade Services system, for example the regions in address, the mapping of document types and partner functions. These configurations depend on your SAP Global Trade Services system, and are not covered in this document. The following are the minimum configurations needed:

- Company Code Mapping to FTO
- Plant Mapping to Legal Unit
- Partner Function Mapping
- Plant Mapping to Administrative unit

You can check the details by referring to Additional Configurations in SAP Global Trade Services System Page 39.

If the transfer is not successful, you may check the application logs in SAP Global Trade Services system to get the error details and then fix it.

### Master Data, Organizational Data, and Other Data

As the complete test steps in the SAP S/4HANA Cloud Public Edition system are described in the reference scope items, please refer to corresponding scope items which are listed in the chapter Test Procedures to get the related organizational data and master data information.

### Preliminary Steps

#### Preliminary Steps in S/4HANA Cloud System

##### Prerequisite Configuration Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you must switch on the transfer of relevant document types to the SAP Global Trade Services system using the SSCUI (Self-Service Configuration User Interface).

Procedure

|  |
| --- |
| Note When you run this scope item for testing purposes, please do revert the configuration settings below once your testing is completed. Otherwise it will have the impact on other business processes and might block other testing. |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Choose Manage Your Solution (F1241) | The Configure Your Solution screen is displayed. |  |
| 3 | Filter Display | Choose Configure Your Solution.Make the following entries and press Enter:Application Area: FinanceSub Application Area: Integration with SAP Global Trade Services |  |  |
| 4 | General Settings | Choose the arrow button at the right of the row for General Settings for Integration to SAP Global Trade Services. | The right pane opens to show relevant settings. |  |
| 5 | Control Settings for Document Transfer | In the right pane, for the Configure Control Settings for Document Transfer row, choose Configure. |  |  |
| 6 | MM0A Settings | Select the leftmost checkbox for the application level MM0A entry, and in the Dialog Structure pane, double-click Document Types.Note To activate document transfer at the organization level, you need to select one of the organization levels for the Activation Level, such as Document Type/Company Code. After selecting this level, double-click on it in the left Dialog Structure pane, and then enable the document transfer for the organizations within the chosen level.You can select the organization level that best suits your requirements. The following organization levels are supported for the Activation Level:Document Type/Company CodeDocument Type/Sales OrganizationDocument Type/PlantDocument Type/Sales Organization and PlantDocument Type/Purchasing OrganizationDocument Type/Purchasing Organization and Plant |  |  |
| 7 | MM0A Settings | If you need to to add purchasing document types, for example to add the document type FNB, choose New Entries. Select the purchasing document type and select Transfer Documents for Managing LTSDs indicator. | After you set this indicator, the system transfers the purchasing data that is required to request for vendor-based long-term vendor declarations (requesting) to SAP GTS. |  |
| 8 | Application Level | In the Dialog Structure pane, double-click Application Level. |  |  |
| 9 | MM0C Settings | Repeat steps 6 to 8 for the following data:Application Level: MM0CDoc.Type: 101BDoc.Type: 101BNote Choose New Entries to add material movement types if necessary. | After you set this indicator, the system transfers the goods receipt data that is required to request for vendor-based long-term vendor declarations (requesting) to SAP GTS. |  |
| 10 | SD0A Settings | Repeat steps 6 to 8 for the following data:Application Level: SD0ADoc.Type: ORNote Choose New Entries to add sales document types if necessary.Set Preference Indicator in Document: <Select this indicator>Check configurable Materials: <Select this indicator>The Check configurable Materials field must be selected for testing Preference Determination for Configurable Materials. | After you set this indicator, the preference indicator that is determined in GTS is transferred back to the feeder system document.In the feeder system, it can then be stored in the document. |  |
| 11 | SD0C Settings | Repeat steps 6 to 8 for the following data:Application Level: SD0CBilling Type: F2Note Choose New Entries to add billing types if you need to transfer documents of this billing type.Select the document type and select Set Preference Indicator in Document.Set Preference Indicator in Document: <Select this indicator>Generate Worklist of Long-Term Vendor Declarations for Customers' Purposes: <Select this indicator> | After you set this indicator, the billing data required by GTS to manage long-term vendor declarations for customer's purposes is transferred from the feeder system to SAP GTS.And the preference indicator that is determined in GTS is transferred back to the feeder system document. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Configure Control Settings for Document Transfer | Go to the Business Processes Configuration app and search for the following activity: Configure Control Settings for Document Transfer.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Add your reconciliation case and ensure column Active is checked. | The Configure Control Settings for Document Transfer screen displays. |  |
| 3 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 4 | MM0A Settings | Select the leftmost checkbox for the application level MM0A entry, and in the Dialog Structure pane, double-click Document Types.Note To activate document transfer at the organization level, you need to select one of the organization levels for the Activation Level, such as Document Type/Company Code. After selecting this level, double-click on it in the left Dialog Structure pane, and then enable the document transfer for the organizations within the chosen level.You can select the organization level that best suits your requirements. The following organization levels are supported for the Activation Level:Document Type/Company CodeDocument Type/Sales OrganizationDocument Type/PlantDocument Type/Sales Organization and PlantDocument Type/Purchasing OrganizationDocument Type/Purchasing Organization and Plant |  |  |
| 5 | MM0A Settings | If you need to to add purchasing document types, for example to add the document type FNB, choose New Entries. Select the purchasing document type and select Transfer Documents for Managing LTSDs indicator. | After you set this indicator, the system transfers the purchasing data that is required to request for vendor-based long-term vendor declarations (requesting) to SAP GTS. |  |
| 6 | Application Level | In the Dialog Structure pane, double-click Application Level. |  |  |
| 7 | MM0C Settings | Repeat steps 4 to 6 for the following data:Application Level: MM0CDoc.Type: 101BDoc.Type: 101BNote Choose New Entries to add material movement types if necessary. | After you set this indicator, the system transfers the goods receipt data that is required to request for vendor-based long-term vendor declarations (requesting) to SAP GTS. |  |
| 8 | SD0A Settings | Repeat steps 4 to 6 for the following data:Application Level: SD0ADoc.Type: ORNote Choose New Entries to add sales document types if necessary.Set Preference Indicator in Document: <Select this indicator>Check configurable Materials: <Select this indicator>The Check configurable Materials field must be selected for testing Preference Determination for Configurable Materials. | After you set this indicator, the preference indicator that is determined in GTS is transferred back to the feeder system document.In the feeder system, it can then be stored in the document. |  |
| 9 | SD0C Settings | Repeat steps 4 to 6 for the following data:Application Level: SD0CBilling Type: F2Note Choose New Entries to add billing types if you need to transfer documents of this billing type.Select the document type and select Set Preference Indicator in Document.Set Preference Indicator in Document: <Select this indicator>Generate Worklist of Long-Term Vendor Declarations for Customers' Purposes: <Select this indicator> | After you set this indicator, the billing data required by GTS to manage long-term vendor declarations for customer's purposes is transferred from the feeder system to SAP GTS.And the preference indicator that is determined in GTS is transferred back to the feeder system document. |  |

##### Create a Supplier for Preference Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you need to create a supplier.

Procedure

You can create a supplier which is located within a preference agreement country/ region.

Once the supplier is created, please refer to the scope item 1WA - Transfer of Primary Master Data for SAP Global Trade Services to transfer the supplier data into SAP Global Trade Services system.

No detail procedure is given here. Please refer to the master data script BNE - Create Supplier Master - MDS to create the supplier.

##### Create a Customer for Preference Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you need to create a customer to create a sales order.

Procedure

You can create a customer which is located within a preference agreement country/ region.

Please create a customer. Once the new customer is created, please refer to the scope item 1WA -Transfer of Primary Master Data for SAP Global Trade Services to transfer the customer data into SAP Global Trade Services system.

No detail procedure is given here. Please refer to the master data script BND - Create Customer Master - MDS to create a customer.

##### Schedule Transfer of Procurement Indicators

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you need to transfer the materials and materials’ procurement indicators to SAP Global Trade Services system.

|  |
| --- |
| NoteWith the activation of the scope item, the background jobs will be activated as well, which try to trigger the transfer via change points for master data change. That means once you successfully complete the initial transfer, the background jobs will automatically transfer the subsequent data changes.These background jobs are scheduled hourly regardless of whether initial transfer is made or not.You have no possibility to deactivate or change the transfer rhythm. |

Procedure

First, Please refer to the test script 1WA - Transfer of Primary Master Data for SAP Global Trade Services to transfer the product data into SAP Global Trade Services system.

Then please execute following steps to transfer the product procurement indicators to SAP Global Trade Services system.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Schedule Transfer of Procurement Indicators - Global Trade Services (F3747). | The Application Jobs view is displayed. |  |
| 3 | Create Schedule Transfer of Procurement Indicators Background Job | In the Application Jobs screen, choose Create.In the New Job view, make the following entries:Job Template: Schedule Transfer of Procurement Indicators - Global Trade ServicesJob Name: Schedule Transfer of Procurement Indicators - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.Then choose Step 4.Log Title: <Enter the log description>Material: <Enter the material number>Choose Schedule. | The New Job view is displayed. |  |

##### Schedule Transfer of Product Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you need to transfer products’ prices to SAP Global Trade Services system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Schedule Transfer of Product Prices - Global Trade Services (F3746). | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Product Prices Background Job | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Product Prices - Global Trade ServicesJob Name: Schedule Transfer of Product Prices - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.Then choose Step 4.Log Title: <Enter the log description>Material: <Enter the material number>Choose Schedule. | Job is scheduled and shown in the list. |  |

##### Schedule Transfer of Minimum /Maximum Product Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you need to transfer products’ prices to SAP Global Trade Services system.

|  |
| --- |
| Note Execute the Preliminary Steps in Global Trade System [Transfer Determination of Preference Agreement to Feeder System](#unique_14) [page ] 23 and [Display Product Master in Global Trade Services System](#unique_15) [page ] 24. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Schedule Transfer of Min./Max. Product Prices - Global Trade Services (F3745). | The Application Jobs view is displayed. |  |
| 3 | Create Schedule Transfer of Min./Max. Product Prices Background Job | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Min. / Max. Material Prices - Global Trade ServicesJob Name: Schedule Transfer of Min. / Max. Material Prices - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.Then choose Step 4.Log Title: <Enter the log description>Period in Number of Days: <Enter the number>Material: <Enter the material number>Plant: <Select a plant from the F4 Help>Choose Schedule.Note You can only transfer a Min. and a Max. price if a purchase invoice with goods receipt is available. | Job is scheduled and shown in the list. |  |

##### Schedule Transfer of Suppliers Product Name (Optional)

Purpose

Before starting the business process, you can transfer suppliers’ product names into SAP Global Trade Services system if you created the purchasing information record.

###### Create Purchasing info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

No detail procedure is given here. Please refer to the Master Data Script BHD - Create Purchasing Info Record - MDS to create product number used by suppliers.

###### Schedule Transfer of Suppliers Product Name

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
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Schedule Transfer of Supplier Product Names - Global Trade Services (F3744). | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Suppliers Product Name Background Job | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Supplier Product Name - Global Trade ServicesJob Name: Schedule Transfer of Supplier Product Name - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.Then choose Step 4.Label: <Enter the log description>Purchasing Info Record: <Enter the Purchasing Info Record number>Choose Schedule. | Job is scheduled and shown in the list. |  |

##### Schedule Transfer of Customer Product Name (Optional)

Purpose

Before starting the business process, you can transfer customer’s products name to SAP Global Trade Services system if you created product number used by customer.

###### Create Customer Material Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

No detail procedure is given here. Please refer to Create Customer-Material Info Record - MDS(2YX) to create the product name used by customer.

###### Schedule Transfer of Customer Product Name

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
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Schedule Transfer of Customer Product Names - Global Trade Services (F3743). | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Customer Product Name Background Job | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Customer Product Name - Global Trade ServicesJob Name: Schedule Transfer of Customer Product Name - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.Then choose Step 4.Label: <Enter the log description>Sales Organization: <Enter the Sales Organization>Distribution Channel: <Enter the Distribution Channel>Customer: <Enter the customer number>Material: <Enter the material number>Choose Schedule. | Job is scheduled and shown in the list. |  |

##### Schedule Transfer of Changed Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you can schedule application jobs regularly to transfer the changes of master data into SAP Global Trade Services system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP GUI | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. |  |  |
| 2 | Access the App | Choose Schedule Transfer of Changed Master Data - Global Trade Services (F6041). | The Application Jobs screen is displayed. |  |
| 3 | Create Background Job for Change Pointer of Product Name at Partners | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Changed Master Data to Global Trade ServicesJob Name: Schedule Transfer of Changed Master Data to Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: DailyEvery: 1 Day(s)End: NoneOn Non-Working Day: No RestrictionChoose OK.Choose Step 3.Input ParametersMessage Type: /SAPSLL/INFMAT_SLL- Change Pointer for Product Name at Partners.Then choose Schedule. | Job is scheduled and shown in the list. |  |
| 4 | Create Background Job for Change Pointer of Procurement and Sales/Distribution | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Changed Master Data to Global Trade ServicesJob Name: Schedule Transfer of Changed Master Data to Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: DailyEvery: 1 Day(s)End: NoneOn Non-Working Day: No RestrictionChoose OK.Choose Step 3.Input ParametersMessage Type: /SAPSLL/PSDMAT_SLL- Change Pointer for Procurement and Sales/DistributionThen choose Schedule. | Job is scheduled and shown in the list. |  |
| 5 | Create Background Job for Change Pointer of Product Price | Job Template: Schedule Transfer of Changed Master Data to Global Trade ServicesJob Name: Schedule Transfer of Changed Master Data to Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: DailyEvery: 1 Day(s)End: NoneOn Non-Working Day: No RestrictionChoose OK.Choose Step 3.Input ParametersMessage Type: /SAPSLL/PRCMAT_SLL- Change Pointer for Product Price.Then choose Schedule. | Job is scheduled and shown in the list. |  |

#### Preliminary Steps in Global Trade Services System

##### Transfer Determination of Preference Agreement to Feeder System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you should transfer the determination of preference agreements to S/4HANA Cloud system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Run Transaction | Enter the transaction /SAPSLL/PRE_SET_DIST in the command filed. | The Distribute Settings to S/4HANA Systems screen is displayed. |  |
| 3 | Distribute Settings to S/4HANA Systems | Please enter the logical system which you want to synchronize the preference agreements. | The Preference Agreements are transferred to S/4HANA Cloud. |  |

##### Display Product Master in Global Trade Services System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you should display the product master data in GTS system to make sure the mandatory data regarding preference processing have been transferred from S/4HANA Cloud system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Run Transaction | Enter the transaction /sapsll/prod_pref_03 in the command filed.Please also make the following entries:Logical System Group: for example, 0MB85UOProduct Number: for example, TG0011 | The Display Products screen is displayed. |  |
| 3 | Display Partner-Specific Data | Select the tab Partner-Specific Data.You will see multiple BP Partner data with its specific product name.Suppliers Product Name and Customer Product Name are transferred from S/4HANA Cloud system . | The Partner-Specific Data screen is displayed. |  |
| 4 | Display Prices and Values Data | Select the tab Prices and Values.You will see the Multiple Prices which you transferred from S/4HANA Cloud system.Price Types: PROD_PRICE and NET_COST belong to the report for product prices.Price Types: MIN_PRICE and MAX_PRICE belong to the report Min./Max. product prices. | The Prices and Values screen is displayed. |  |
| 5 | Display Procurement Indicator | Select the tab Procurement.You will see the Procurement Indicator and Preference Model based on plant and plant group. | The Procurement screen is displayed. |  |

|  |
| --- |
| Note The following steps are applicable to SAP Global Trade Services, edition for SAP HANA 2020 SP01. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP GUI | Log on to SAP Global Trade Services system using the role Preference Specialist (GTS). |  |  |
| 2 | Access App | Open the app Manage Products.Please also make the following entries:Logical System Group: for example, 0MB85UOProduct Number: for example, TG0011Click Display. | The Display Products screen is displayed. |  |
| 3 | Display Partner-Specific Data | Select the tab Partner-Specific Data.You will see multiple BP Partner data with its specific product name.Suppliers Product Name and Customer Product Name are transferred from S/4HANA Cloud system . | The Partner-Specific Data screen is displayed. |  |
| 4 | Display Prices and Values Data | Select the tab Prices and Values.You will see the Multiple Prices which you transferred from S/4HANA Cloud system.Price Types: PROD_PRICE and NET_COST belong to the report for product prices.Price Types: MIN_PRICE and MAX_PRICE belong to the report Min./Max. product prices. | The Prices and Values screen is displayed. |  |
| 5 | Display Procurement Indicator | Select the tab Procurement.You will see the Procurement Indicator and Preference Model based on plant and plant group. | The Procurement screen is displayed. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Display worklist for Vendor-Based Long-Term Vendor Declaration

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Document to Supplier](#unique_24) [page ] 30 | Purchaser | Create Purchase Order - Advanced (ME21N) | The purchase order is created |
| [Post Goods Receipt](#unique_25) [page ] 31 | Warehouse Clerk | Post Goods Receipts | The material document is created |
| [Schedule Transfer of Purchasing Documents - Global Trade Services (Optional)](#unique_26) [page ] 32 | Administrator - International Trade | Schedule Transfer of Purchasing Documents - Global Trade Services (F3742) | The purchasing document is transferred to GTS |
| [Schedule Transfer of Material Documents - Global Trade Services (Optional)](#unique_27) [page ] 33 | Administrator - International Trade | Schedule Transfer of Material Documents - Global Trade Services | The material document is transferred to GTS |
| [Display the Worklist for Purchasing Documents/Material Document](#unique_28) [page ] 34 |  | /n/SAPSLL/PRE_WLI_001 | The purchasing document and material document are displayed |

Display worklist for Long-Term Vendor Declaration for Customer's Purpose

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order to Customer](#unique_29) [page ] 37 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order is created |
| [Create Outbound Delivery](#unique_30) [page ] 38 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | The outbound delivery is created and goods issue is posted |
| [Create Billing](#unique_31) [page ] 39 | Billing Clerk | Create Billing Documents - VF01 (VF01) | The billing document is created |
| [Schedule Transfer of Billing Documents - Global Trade Services (Optional)](#unique_32) [page ] 40 | Administrator - International Trade | Schedule Transfer of Material Documents - Global Trade Services (F3741) |  |
| [Display the Worklist: Long-Term Vendor Declaration for Customer’s Purpose](#unique_33) [page ] 41 |  | /n/SAPSLL/PRE_WLO_001 | The transferred document is in SAP Global Trade Services system |

Preference Determination for Configurable Materials (Optional):

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order with Configurable Material](#unique_34) [page ] 43 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order is created. |
| [Explode and Transfer Configurable Materials](#unique_35) [page ] 45 | Administrator - International Trade | Explode and Transfer Configurable Materials - Global Trade Services | The Configurable Materials for the sales order is transferred to GTS. |
| [Perform Preference Determination for Documents](#unique_36) [page ] 46 | SAP_BR_PREF_SPCLST_LLS in SAP GTS system | Perform Preference Determination - Documents in GTS system | The sales order is displayed in the result list. |
| [Schedule Reprocessing of Documents](#unique_37) [page ] 47 | Administrator - International Trade | Schedule Reprocessing of Documents - Global Trade Services | The document is reprocessed. |
| [Display Worklist of Configurable Materials](#unique_38) [page ] 48 | Administrator - International Trade | Display Worklist of Configurable Materials - Global Trade Services | The configurable material is displayed with the status Calculated. |
| [Production Process for Sales Order](#unique_39) [page ] 49 |  |  | Post Goods Receipt for Production Order |
| [Create Outbound Delivery](#unique_40) [page ] 50 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | The outbound delivery is created, and goods issue is posted. |
| [Create Billing](#unique_41) [page ] 51 | Billing Clerk | Create Billing Documents - VF01 (VF01) | The billing document is created. |
| [Check the Billing](#unique_42) [page ] 51 | Billing Clerk | Display Billing Documents (VF03) | The preference indicator is displayed on the item level |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note - With the activation of the scope item, the background jobs will be activated as well, which try to trigger the transfer via change points for master data change. That means once you successfully complete the initial transfer, the background jobs will automatically transfer the subsequent data changes.- These background jobs are scheduled hourly regardless of whether initial transfer is made or not.- You have no possibility to deactivate or change the transfer rhythm. |

### Display Worklist for Vendor-Based Long-Term Vendor Declaration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Before you start the test procedures, please make sure the Set-up Instruction Guide of this scope item has been followed through to ensure working connectivity between SAP S/4HANA Cloud Public Edition system and SAP Global Trade Services system.

As the document transfer is automatically triggered along with saving the document in the SAP S/4HANA Cloud Public Edition system, you may follow the complete procedures which are described in the reference scope items to create the documents. The procedures here are simply shown the processes in SAP S/4HANA Cloud Public Edition system. The reference document types and associated scope items are listed below:

| Process | Document Type | Scope Item |
| --- | --- | --- |
| Purchasing | NB (F - Purchase Order, Standard PO) | J45 - Procurement of Direct MaterialsBMD - Purchase Contract |
|  | LP (L - Scheduling Agreement, Scheduling Agreement) | BMR - Scheduling Agreements in Procurement2NX - Scheduling Agreement for Subcontracting Procurement2NY - Scheduling Agreement for Consignment Procurement |
| Material Document | 101B (GR goods receipt)102B (GR for PO reversal) | J45 - Procurement of Direct MaterialsBMD - Purchase Contract |

#### Create Purchase Document to Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a purchase document to the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Choose Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Enter Purchase Document | On the Create Purchase Order view, make the following entries:Order Type: for example, Standard POSupplier : <enter your supplier number>Choose the Expand Header button.In the Header section, make the following entries on the Org. Data tab:Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310Choose the Expand Items section.In the Item Overview section, make the following entries:Material: for example TG0011PO Quantity: <enter the quantity>Net Price: <enter the price>Currency :<enter the currency>Plnt: 3310Stor. Location: 331AGo to the Confirmation tab in the Item Detail section, and choose Rough GR in the Conf. Control field. | The purchase document data is maintained. |  |
| 4 | Save Purchase Document | Choose Save. | The purchase document is saved. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the step, you post goods receipts for the purchasing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the Purchase Order ID and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter.Delivery Note: xxxPrinting: Individual slip |  |  |
| 5 | Select Item | From the Items section, select the goods receipt item to be posted.Note Select an item with a quantity of two or more pieces. | You can see that the Post button is activated. |  |
| 6 | Post | Choose Post. | The system displays the message: material document xxx posted. |  |

#### Schedule Transfer of Purchasing Documents - Global Trade Services (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Due to technical issues, the purchase document was not successfully transferred to the Global Trade Services system. Once the issue is resolved, you can use the app to re-initiate the transfer of the purchasing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Schedule Transfer of Purchasing Documents - Global Trade Services (F3742). | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Purchasing Documents background job | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Purchasing Documents - Global Trade ServicesJob Name: Schedule Transfer of Purchasing Documents - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: SelectRecurrence Pattern: choose Single RunChoose OK.Choose Step 3.Then choose Step 4.SAP Compliance Management: SelectPurchasing document: <Enter the purchasing document number>Choose Schedule. | Job is scheduled and shown in the list. |  |

#### Schedule Transfer of Material Documents - Global Trade Services (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If technical issues prevent the material document from being transferred to the Global Trade Services system, you can resolve these issues and then use the app to re-transfer the material documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Schedule Transfer of Material Documents - Global Trade Services (F3741). | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Material Documents Background Job | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Material Documents - Global Trade ServicesJob Name: Schedule Transfer of Material Documents - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.Then choose Step 4.Material Document: Enter the material document numberChoose Schedule. | Job is scheduled and shown in the list. |  |

#### Display the Worklist for Purchasing Documents/Material Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step displays the worklist for vendor declaration in SAP Global Trade Services system.

Procedure

|  |
| --- |
| Note If your GTS system is SAP Global Trade Service, edition for SAP HANA 2020 SP01, the steps are different. Please check the steps after this section. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Display Worklist: Vendor-Based Long-Term Vendor Declaration | Enter the transaction /n /SAPSLL/PRE_WLI_001 in the command filed. |  |  |
|  |  | On the Display Worklist: Vendor-Based Long-Term Vendor Declaration screen, choose Administrative Unit.Enter the External Partner Number and the vendor you created in the previous step.Then choose Execute.On the next screen, you can find the items for the vendor and the product with two Reference Application.One is Relevant MM Purchase order.Another one is Relevant MM Goods Movement. | The Worklist for the Vendor Based Long-Term Vendor Declaration is displayed. |  |

|  |
| --- |
| Note The following steps are applicable to SAP Global Trade Services, edition for SAP HANA 2020 SP01 or higher. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system using the role Preference Specialist (GTS). | The SAP Easy Access page is displayed. |  |
| 2 | Create an LTSD Request | Enter the Transaction /SAPSLL/LTSDREQ_1 in the command field.On the Creation of LTSD Requests Screen,Enter the Administrative Unit, External Partner Number and Contact Person.Choose Execute. | The LTSD Request is created. |  |
| 3 | Log on to SAP GTS Fiori launchpad | Log onto the Fiori launchpad using the Admin Role /SAPSLL/GTS_ADMINISTRATOR in SAP GTS system. |  |  |
| 4 | Access App | Open the app Manage Requests – Long-Term Supplier’s Declarations. |  |  |
|  |  | On the Manage Requests – Long-Term Supplier’s Declarations screen, enter the Administrative Unit and the Vendor Number in LTSD Issuer.Then choose Go.Choose the LTSD Request.In the General Information tab, find the Prodcut that created in the purchase order.Choose the item.You can find the list of purchasing documents in the tab Purchasing Document Items and material documents for this product in the tab Material Document Items. |  |  |

### Display Worklist for Long-term Vendor Declaration for Customer's Purpose

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Before you start the test procedures, please make sure the Set-up Instruction Guide of this scope item has been followed through to ensure working connectivity between SAP S/4HANA Cloud Public Edition system and SAP Global Trade Services system.

As the document transfer is automatically triggered along with saving the document in the SAP S/4HANA Cloud Public Edition system, you may follow the complete procedures which are described in the reference scope items to create the documents. The procedures here are simply shown the processes in SAP S/4HANA Cloud Public Edition system. The reference document types and associated scope items are listed below:

| Process | Document Type | Scope Item |
| --- | --- | --- |
| Billing | F2 (F2 Invoice) | BD9 - Sell from StockBDH - Sales Order Entry with One-Time CustomerBDN - Sales of Non-Stock Item with Order-Specific ProcurementBDW - Returnables ProcessingBKJ - Sales Order Processing with Customer Down Payment1MX - Intercompany Sales Order Processing – International |
|  | F8 (Pro Forma Invoice for Delivery) | BDA - Free of Charge Delivery |
|  | CBST (Intercompany Billing for STO) | 1P9 - Intercompany Stock Transfer |

#### Create Sales Order to Customer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a sales order to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Manage Sales Orders (F1873). | The Manage Sales Orders screen is displayed. |  |
| 3 | Enter Order Type | On the Manage Sales Orders screen, select Create - Create Sales Orders.On the Create Sales Orders screen, make the following entries and choose Create:Sales Order Type: for example ORSales Organization: 3310Distribution Channel: 10Division: 00 | The order type and sales organization are chosen. |  |
| 4 | Enter Order Details | On the New Sales Order Standard Order screen, make the following entries:Sold-To Party: <enter your customer number>Ship-To Party: <enter your customer number>Customer Reference: <enter the reference number>Choose tab Items.Product: for example, TG11Requested Quantity: <enter the quantity>Choose Add Row. | The order details are maintained. |  |
| 5 | Save Order | Choose Save. | The sales order is saved. |  |

|  |
| --- |
| Note If the sales order requires approval, follow the Complete the Process Sales Order Approval steps described in the Sell from Stock (BD9) test script. |

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
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery with Order Reference screen is displayed. |  |
| 3 | Search Sales Order | On the Create Outbound Delivery with Order Reference screen, make the following entries and choose Continue:Shipping Point: 3310Selection Date: <delivery selection date>Order: <enter the created sales order number> | Choose the sales order to create delivery. |  |
| 4 | Create Outbound Delivery | On the Outbound Delivery Create: Overview screen, navigate to the Picking tab and enter the quantity in the Picked Qty field.Choose Post Goods Issue. | The outbound delivery is created. |  |

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
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the roleBilling Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen is displayed. |  |
| 3 | Create Billing Document | On the Create Billing Document screen, enter the created outbound delivery number and choose Save. | The billing document is created. |  |

#### Schedule Transfer of Billing Documents - Global Trade Services (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Due to technical issues, the billing document may not have been successfully transferred to the Global Trade Services system. Once the issue is resolved, you can use the app to re-initiate the transfer of the billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Schedule Transfer of Billing Documents - Global Trade Services (F3740). | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Billing Documents background job | In the Application Jobs screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Transfer of Billing Documents - Global Trade ServicesJob Name: Schedule Transfer of Billing Documents - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: <Select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.Then choose Step 4.Billing Document : <Enter the Billing document number>Choose Schedule. | Job is scheduled and shown in the list. |  |

#### Display the Worklist: Long-Term Vendor Declaration for Customer’s Purpose

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you display the Worklist: Long-Term Vendor Declaration for Customer’s Purpose within the SAP Global Trade Services system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Display Worklist: Long-Term Vendor Declaration for Customer’s Purpose | Enter the transaction /n/SAPSLL/PRE_WLO_001 in the command filed. |  |  |
|  |  | On the Display Worklist: Long-Term Vendor Declaration for Customer’s Purpose screen, choose Administrative Unit.Enter the External Partner Number, the customer you created in the previous step.Then choose Execute.On the next screen, you can find the billing document you created in S/4HANA Cloud system. | The Worklist for Long-Term Vendor Declaration for Customer’s Purpose is displayed. |  |

|  |
| --- |
| Note The following steps are applicable to SAP Global Trade Services, edition for SAP HANA 2020 SP01 or higher. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system using the role Preference Specialist (GTS). | The SAP Easy Access page is displayed. |  |
| 2 | Create an LTSD Request | Enter the Transaction /SAPSLL/LTSDOUT_1 in the command field.On the LTSD Issue Screen,Enter the Administrative Unit, External Partner Number and Contact Person.Choose Execute. | The LTSDs were created and updated. |  |
| 3 | Log on to SAP GTS Fiori launchpad | Log onto the Fiori launchpad using the Admin Role /SAPSLL/GTS_ADMINISTRATOR in SAP GTS system. |  |  |
| 4 | Access App | Open the app Manage Long-Term Supplier’s Declarations Outbound. |  |  |
|  |  | On the Manage Long-Term Supplier’s Declarations Outbound screen, enter the cutomer number in LTSD Receiver.Then choose Go.Choose the LTSD Request.In the Products tab, find the Prodcut that created in the purchase order.Choose the item.In the Preference Statements tab, you can find the list of Preference Agreement for this product.Choose the Preference Agreement that is relevant with the documents created in previous step.In the tab Invoice Documents, you can find the billing documents. |  |  |

### Preference Determination for Configurable Materials (Optional)

Before you start the procedures, make sure the Set-up Instruction Guide of this scope item has been followed through to ensure working connectivity between SAP S/4HANA Cloud Public Edition system and SAP Global Trade Services system.

When a document is saved in the SAP S/4HANA Cloud Public Edition system, the transfer process is automatically initiated. You can follow the detailed procedures outlined in the reference scope items to create the documents. The procedures provided here illustrate the processes within the SAP S/4HANA Cloud Public Edition system. Below is a list of reference document types and their associated scope items:

Table 1:

| Process | Document Type | Scope Item |
| --- | --- | --- |
| Sales order | OR (Standard Order) | 1YT - Make-to-Order Production with Variant Configuration |
| Billing | F2 (F2 Invoice) |  |

#### Create Sales Order with Configurable Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a sales order with configurable material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Manage Sales Orders (F1873). | The Manage Sales Orders screen is displayed. |  |
| 3 | Enter Order Type | On the Manage Sales Orders screen, select Create - Create Sales Orders-VA01.On the Create Sales Orders screen, make the following entries and choose Create:Sales Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The order type and sales organization are chosen. |  |
| 4 | Enter Order Details | On the New Sales Order Standard Order screen, make the following entries:Sold-To Party: <enter your customer number>Ship-To Party: <enter your customer number>Customer Reference: <enter the reference number>Rep. Deliv. Date: <current date+ 5 days> | Details of the order are maintained. |  |
| 5 | Enter Characteristic Value | In the All Items section, enter the following value and choose Enter.Material Number: CM-FL-V00Quantity: for example, 1 PCOn the Variant Configuration screen, select value for characteristics below and choose Done.Lifter Model: <Heavy>Power Source: <Combustion>. Combustion displays as default value.Wheel Type: <Cushion Tires>Fork Size: <Small>Counterweight (KG): <5.000>Battery Capacity(Ah): Pneumatic<50, 80, 140>Net Value: <the values vary according to the chosen characteristic>On the Review Availability Check Result screen, choose Apply. |  |  |
| 6 | Save Order | Choose Save Document. | The sales order is saved. |  |

#### Explode and Transfer Configurable Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the step, you schedule a new job to explode and transfer Configurable Materials to Global Trade Services System.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Explode and Transfer Configurable Materials - Global Trade Services. | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Billing Documents Background Job | On the Application Jobs screen, choose Create.On the New Job screen, make the following entries:Job Template: Explode and Transfer Configurable Materials - Global Trade ServicesJob Name: Explode and Transfer Configurable Materials - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: <Select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.Maintain following entry:Document: <the sales order you created in the previous step>Choose Schedule. | Job is scheduled and shown in the list. |  |

#### Perform Preference Determination for Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you perform Preference Determination Documents in SAP Global Trade Services system.

|  |
| --- |
| Note The following steps are applicable to SAP Global Trade Services, edition for SAP HANA 2020 SP01 or higher. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the Fiori launchpad using the user SAP_BR_PREF_SPCLST_LLS in SAP GTS system. |  |  |
| 2 | Access the App | Choose Perform Preference Determination - Documents. | The Perform Preference Determination for Configured Bills of Material screen is displayed. |  |
| 3 | Select the Document | On the Perform Preference Determination for Configured Bills of Material screen, make the following entry and choose Execute.Logical System Group: <the name of the S/4HANA system>Document: <the sales order created in the previous step>Bill of Material Explosion: T as the default | The Preference Determination - Logging screen is displayed. |  |
| 4 | Check the Result | On the Preference Determination - Logging Screen, you can find the configurable product.On the left side of the screen, you can find the product CM-FL-V00 and find the sales order in the field Reference Number.Choose the product CM-FL-V00, the components of the configurable material CM-FL-V00 are displayed in the tab Components. | The Preference Determination for configurable material is displayed. |  |

#### Schedule Reprocessing of Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the step, you schedule a new job to reprocessing of documents

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Schedule Reprocessing of Documents - Global Trade Services. | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Reprocessing of Documents Background Job | On the Application Jobs screen, choose Create.On the New Job screen, make the following entries:Job Template: Schedule Reprocessing of Documents - Global Trade ServicesJob Name: Schedule Reprocessing of Documents - Global Trade ServicesChoose Step 2.Choose Define Recurrence Pattern.Start Immediately: <Select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.Choose Schedule. | Job is scheduled and shown in the list. |  |

#### Display Worklist of Configurable Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the step, you display worklist of configurable materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Display Worklist of Configurable Materials -Global Trade Services. | The Preference: Display Worklist of Configurable Materials screen is displayed. |  |
| 3 | Display Worklist of Configurable Materials | On the Preference: Display Worklist of Configurable Materials screen, make the following entries and choose Execute.Document: <the sales order created in the previous step>Worklist Status: <leave it blank> | The configurable material is displayed with the status transferred. |  |

#### Production Process for Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the step, you create stock (sales order stock) for configurable materials.

Procedure

To produce the material and get it into Sales Order stock, execute the following steps described in the test script of the scope item Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE_AE).

Master Data Sample Value:

- Material: CM-FL-V00
- Plant: 3310
- Storage Location: 101A

Table 2:

| Test Procedure in BJE | Comment |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery with Order Reference screen is displayed. |  |
| 3 | Search Sales Order | On the Create Outbound Delivery with Order Reference screen, make the following entries and choose Continue:Shipping Point: 3310Selection Date: <delivery selection date>Order: <enter the sales order number you created> | Choose the sales order to create delivery. |  |
| 4 | Create Outbound Delivery | On the Outbound Delivery Create: Overview screen, navigate to the Picking tab and enter the quantity in the Picked Qty field.Choose Post Goods Issue. | The outbound delivery is created. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen is displayed. |  |
| 3 | Create Billing Document | On the Create Billing Document screen, enter the created outbound delivery number and choose Save. | The billing document is created. |  |

#### Check the Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Display Billing Documents (VF03). | The Create Billing Documents screen is displayed. |  |
| 3 | Check Billing Document | On the Display Billing Document screen, enter the created billing document and choose display.Go to the tab Item Detail and check the field Customs Preference. | The billing document is displayed, and the preference indicator is displayed on the item level. |  |

## Appendix

### Additional Configurations in SAP Global Trade Services System

Before using Preference Management in Global Trade Services System, you need to finish all the configurations for Preference Processing in Global Trade System. You can find Configuration Guide for SAP Global Trade Services in SAP Help Portal.

The following chapters list limited customized activities regarding integration with feeder system. The configurations depend on your SAP Global Trade Services system, and the steps and input values might be different in your system.

#### Define Legal Units

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > General Settings > Organizational Structure > Define Legal Units. | The IMG path is navigated. |  |
| 3 | Maintain Legal Units | Define the legal unit, for example LU_1010 and maintain the general data, for example name and address. | The legal unit is maintained or checked. |  |

#### Assign Plant to Legal Unit

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > General Settings > Organizational Structure > Assignment of Organizational Units from Feeder System to Legal Unit > Assign Plant at Feeder System Group Level. | The IMG path is navigated. |  |
| 3 | Assign Plant to Legal Unit | Choose Manually Assign Plant on the Choose Activity dialog box.On the Change View “Mapping: Plant from Feeder System Group to Legal Unit” screen, choose New Entries and making the following entries if you haven’t maintained it:Logical System group: <choose the logical system group>FS Organization: <your plant in S/4HANA, for example,3310>Legal Unit: <your created legal unit, for example, LU_3310>Choose Save. | The plant is assigned to the legal unit. |  |

#### Define Cross-Plant BOM Evaluation

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > General Settings > Organizational Structure > Define Cross-Plant BOM Evaluation. | The IMG path is navigated. |  |
| 3 | Maintain Plant Group for Feeder System Plants | Define the Plant Group for Feeder System Plants, for example PLG_3310 and maintain the description, for example Plant Group for AED. | The Plant Group for Feeder System Plants is maintained. |  |
| 4 | Assign Plants to Plant Group | In the Change View “ Assignment of Plant” : Overview Screen, select the Plant Group you just created, choose New Entries and make the following entry:Logical system: <choose the logical system>Plant: <your plant in S/4HANA, for example,3310> | The Plants are assigned to the Plant Group. |  |

#### Assign Partner Functions

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > General Settings > Partner Structure > Assignment of Partner Functions from Feeder Systems > Assign Partner Function at Feeder System Group Level. | The IMG path is navigated. |  |
| 3 | Assign Partner Functions | Choose Manually Assign Partner Function on the Choose Activity pop-up window.On the Change View “Mapping: Partner Function in FS Group to SAP GTS” screen, choose New Entries and making the following entries if you haven’t maintained it:Logical System GroupBS Partner FunctionPartner Function<logical system group>AGAG<logical system group>WEWE<logical system group>RERE<logical system group>RGRG<logical system group>LFLF<logical system group>DAPODLV<logical system group>RSLFChoose Save. | The partner function mapping is maintained. |  |

#### Define Administrative Unit for Vendor Declarations

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Tr ade Services > Risk Management> Preference Processing > Organizational Structure > Define Administrative Unit for Vendor Declarations . | The IMG path is navigated. |  |
| 3 | Define Administrative Unit for Vendor Declarations | Define Administrative Unit for Vendor Declarations, for example AU_3310 and maintain the general data, for example name and address.You can also extend the BP role Administrative Unit for Vendor Declarations for Foreign Trade Organization FTO_3310 you just created. | The Administrative Unit for Vendor Declarations is created. |  |

#### Define Administrative Unit Attributes

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > Risk Management> Preference Processing > Organizational Structure > Define Administrative Unit Attributes . | The IMG path is navigated. |  |
| 3 | Define Administrative Unit Attributes | On the Display View “ Administrative Unit ”: Overview screen, select the Administrative Unit you just created, for example: FTO_3310Double click Assign Organizational Unit.On the Change View “Assign Organizational Unit”:Overview screen, choose New Entries and maintain following entries:Cross-Plant Preference ModelPlant Group: for example,PLG_3310Double click Currency and Numbering System.On the Change View “ Currency and Numbering System”:Overview screen, choose New Entries and maintain following entries:Currency : <The Currency used in the company, for example,AEDExchange Rate Type: for example, MSchemes : The Numbering scheme used in the country/ region, for example, EUSTABOM Explosion: T Top-Down (Entire Explosion) | The attributes of the Administrative unit is maintained. |  |

#### Define Legal Regulation

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO, and go to the following IMG path: SAP Global Trade Services > General Settings > Legal Regulations > Define Legal Regulation . | The IMG path is navigated. |  |
| 3 | Define Legal Regulation | On the Change View “Legal Regulation: Overview” screen, make sure the legal regulation with legal code Preference Law is defined for your country/ region, for example, the legal regulation PANEG is defined for Germany. | The defined legal regulation is checked. |  |

### Additional Configurations in SAP Global Trade Services System with edition for SAP HANA 2020 SP01 or higher

The following steps are applicable to SAP Global Trade Services, edition for SAP HANA 2020 SP01.

Before using Preference Management in Global Trade Services System, you need to finish all the configurations for Preference Processing in Global Trade System. You can find Configuration Guide for SAP Global Trade Services with the installed version in SAP Help Portal.

The following chapters list limited customized activities regarding integration with feeder system. The configurations depend on your SAP Global Trade Services system, and the steps and input values might be different in your system.

#### Define Legal Units

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA > General Settings > Organizational Structure > Define Legal Units. | The IMG path is navigated. |  |
| 3 | Maintain Legal Units | Define the legal unit, for example LU_1010 and maintain the general data, for example name and address. | The legal unit is maintained or checked. |  |

#### Assign Plant to Legal Unit

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA> General Settings > Organizational Structures > Assignment of Organizational Units from Feeder System to Legal Unit > Assign Plant at Feeder System Group Level. | The IMG path is navigated. |  |
| 3 | Assign Plant to Legal Unit | Choose Manually Assign Plant on the Choose Activity dialog box.On the Change View “Mapping: Plant from Feeder System Group to Legal Unit” screen, choose New Entries and making the following entries if you haven’t maintained it:Logical System group: <choose the logical system group>FS Organization: <your plant in S/4HANA, for example,1010>Legal Unit: <your created legal unit, for example, LU_1010>Choose Save. | The plant is assigned to the legal unit. |  |

#### Define Cross-Plant BOM Evaluation

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA > General Settings > Organizational Structures > Define Cross-Plant BOM Evaluation. | The IMG path is navigated. |  |
| 3 | Maintain Plant Group for Feeder System Plants | Define the Plant Group for Feeder System Plants, for example PLG_1010 and maintain the description, for example Plant Group for EUR. | The Plant Group for Feeder System Plants is maintained. |  |
| 4 | Assign Plants to Plant Group | In the Change View “Assignment of Plant”: Overview Screen, select the Plant Group you just created, choose New Entries and make the following entry:Logical system: <choose the logical system>Plant: <your plant in S/4HANA, for example,1010> | The Plants are assigned to the Plant Group. |  |

#### Assign Partner Functions

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG Activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA > General Settings > Partner Structures > Assignment of Partner Functions from Feeder Systems > Assign Partner Function at Feeder System Group Level. | The IMG path is navigated. |  |
| 3 | Assign Partner Functions | Choose Manually Assign Partner Function on the Choose Activity pop-up window.On the Change View “Mapping: Partner Function in FS Group to SAP GTS” screen, choose New Entries and making the following entries if you haven’t maintained it:Logical System GroupBS Partner FunctionPartner Function<logical system group>AGAG<logical system group>WEWE<logical system group>RERE<logical system group>RGRG<logical system group>LFLF<logical system group>DAPODLV<logical system group>RSLFChoose Save. | The partner function mapping is maintained. |  |

#### Define Legal Regulation

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA> General Settings > Legal Regulations > Define Legal Regulation. | The IMG path is navigated. |  |
| 3 | Define Legal Regulation | On the Change View “Legal Regulation: Overview” screen, make sure the legal regulation with legal code Preference Law is defined for your country/ region, for example, the legal regulation PANEG is defined for Germany. | The defined legal regulation is checked. |  |

#### Define Administrative Unit for Vendor Declarations

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA > Preference Management > Organizational Structures > Define Administrative Unit for Vendor Declarations. | The IMG path is navigated. |  |
| 3 | Define Administrative Unit for Vendor Declarations | Define Administrative Unit for Vendor Declarations, for example AU_1010 and maintain the general data, for example name and address.You can also extend the BP role Administrative Unit for Vendor Declarations for Foreign Trade Organization FTO_1010 you just created. | The Administrative Unit for Vendor Declarations is created. |  |

#### Define Administrative Unit Attributes

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA > Preference Management > Organizational Structures > Define Administrative Unit Attributes . | The IMG path is navigated. |  |
| 3 | Define Administrative Unit Attributes | On the Display View “Administrative Unit ”: Overview screen, select the Administrative Unit you just created, for example: FTO_3310Double-click Assign Organizational Unit.On the Change View “Assign Organizational Unit”: Overview screen, choose New Entries and maintain following entries:Cross-Plant Preference ModelPlant Group: for example, PLG_3310Double-click Calculation Parameters.On the Change View “Calculation Parameters”: Details screen, choose New Entries and maintain following entries:Currency: <the Currency used in the company, for example, AED>Exchange Rate Type: for example, MSchemes: <the Numbering Scheme used in the country/ region, for example, EUSTA>BOM Explosion: T Top-Down (Entire Explosion)Choose Save. | The attributes of the Administrative unit is maintained. |  |

#### Define Settings for the LTSD Process

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA> Preference Management > Supplier’s Declarations > Define Settings for the LTSD Process | The IMG path is navigated. |  |
| 3 | Define Settings for LTSD Process | On the Change View “Define Settings for LTSD Process” screen, choose New Entries and maintain following entries:Administrative Unit: the administrative unit created in previous step.Goods Retention Period: For example: 30 DaysValuation Method: For example: Worst-Case LTSDs and GRsCommunication Medium:From the dropdown list, select the communication type that you want to use as the default for all partners. For example: E-mailOutput Language: select the output language that you want to use as the default for all output. For example: Business Partner’s LanguageRequest All Suppliers: SelectedIssue to All Customers: SelectedMax. Calendar Years for Issue: For example: 1 YearChoose Save. | The defined legal regulation is checked. |  |

#### Activate Documents of Origin

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA> Preference Management > Supplier’s Declarations > Documents of Origin> Activate Documents of Origin | The IMG path is navigated. |  |
| 3 | Activate Documents of Origin | On the Change View “Activate Long-Term Supplier’s Declarations”: Overview screen, choose New Entries and maintain following entries:Administrative Unit: the administrative unit created in previous step.Doc of Origin Type: Select the document of Origin Type For example: EU-LTSDIncoming active: SelectedOutbound Active: SelectedRequest Active: SelectedChoose Save. | The defined legal regulation is checked. |  |

#### Assign Action Profiles

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA> Preference Management > Supplier’s Declarations > Output Management>Assign Action Profiles | The IMG path is navigated. |  |
| 3 | Assign Action Profiles | On the Change View “Assign Action Profiles for LTSD Request”: Overview screen, choose New Entries and maintain following entries:Administrative Unit: the administrative unit created in previous step.Action Profile: select action profile, for example: LLS_PRE_LTSD_EU_REQUESTChoose Save.Choose Assign Action Profile for Customer-based LTSD on left column.On the Change View “Assign Action Profiles for Customer-based LTSD”: Overview screen, choose New Entries and maintain following entries:Administrative Unit: the administrative unit created in previous step.LTSD Type: select LTSD Type, for example: EU-LTSDAction Profile: select action profile, for example: LLS_PRE_LTSD_EU_REQUESTChoose Save. |  |  |

#### Assign Text Modules

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Access the IMG activity | Run the transaction SPRO and go to the following IMG path: SAP Global Trade Services, edition for SAP HANA> Preference Management > Supplier’s Declarations > Output Management>Assign Text Modules | The IMG path is navigated. |  |
| 3 | Assign Action Profiles | On the Change View “Assign General Text Modules”: Overview screen, choose New Entries and maintain following entries:Administrative Unit: the administrative unit created in previous step.Letter Header: for example: ADRS_HEADERText of Footer: for example: ADRS_FOOTERForm Logo: for example: SAP LOGO + TRADEMARKGraphic Type: for example: Black and White Bitmap ImageChoose Save.Choose Assign Text Modules for Sending E-Mails Dispatch on left column.On the Change View “Assign Text Modules for Sending E-Mails Dispatch”: Overview screen, choose New Entries and maintain following entries:Administrative Unit: the administrative unit created in previous step.Action Definition: for example: LLS_PRE_LTSD_SEND_COLL_EMAILE-mail Subject: for example: /SAPSLL/TX_EU_LTSD_EMAIL_S_REQE-Mail Text: for example: /SAPSLL/TX_EU_LTSD_COVLET_REQMail Format: for example: HTMLChoose Save.Choose Request: Assign Text Modules for Form on left column.On the Change View “Request: Assign Text Modules for Form”: Overview screen, choose New Entries and maintain following entries:Administrative Unit: the administrative unit created in previous step.Supplier's Declaration Form Text: for example: /SAPSLL/TX_EU_LTSD_LEGAL_REGCover Letter: for example: /SAPSLL/TX_EU_LTSD_COVLET_REQChoose Save.Choose C-LTSD: Assign Text Modules for Form on left column.On the Change View “C-LTSD: Assign Text Modules for Form”: Overview screen, choose New Entries and maintain following entries:Administrative Unit: the administrative unit created in previous step.LTSD Type: for example: EU-LTSDSupplier's Declaration Form Text: for example: /SAPSLL/TX_EU_LTSD_LEG_REG_ISSCover Letter: for example: /SAPSLL/TX_EU_LTSD_COVLET_ISSUCover Letter (Reissue): for example: /SAPSLL/TX_EU_LTSD_COVLET_REISChoose Save. |  |  |

### Message Monitoring and Troubleshooting using Application Interface Framework

Purpose

You can use the SAP Application Interface Framework to monitor interfaces as well as execute error handling.

For detailed information on the Application Interface Framework, go to the [SAP Help Portal](http://help.sap.com/) and search for SAP Application Interface Framework product page. In the Operations, open Application Help for SAP Application Interface Framework.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Assign Recipients to Users (F2949). | The Assign Recipients to User screen is displayed. |  |
| 3 | Assign Recipients to User | On the Assign Recipients to User screen, choose Add User to add the current logon user, and the select the user.Choose Assign, and make the following entries in the Assign Recipients dialog box:Namespace: /SLLPIRecipient Name: RFC_GTS_INTEGRAIONMessage Type: Application Error or Technical ErrorOverview: XTechnical User: XChoose Assign. | The recipient is assigned to the user. |  |
| 4 | Access App | Choose Message Dashboard(/AIFX/WDA_MSG_MONITOR). | The Interface Monitor screen is displayed. |  |
| 5 | Monitor Interfaces | On the Interface Monitor screen, check the status of the interface SAP GTS Integration - /SLLPI, and execute error handling if necessary.Please check following two interfaces which monitor the status of documents transferring for Preference Management.Purchasing and Material documents for Preference – PVDWLI_SYN/1Invoice documents for Preference - PVDWLO_SYN/1 | The messages in the interface are checked.For detailed information, go to the Application Help for SAP Application Interface Framework on the [SAP Help Portal](http://help.sap.com/). |  |

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
> Flagged while digesting this document, not verified: Display Worklist of Configurable Materials: the Overview Table expects the configurable material 'displayed with the status Calculated', while the procedure's expected result says 'displayed with the status transferred'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table lists 'Schedule Transfer of Material Documents - Global Trade Services (F3741)' for the billing document transfer step, whereas the procedure uses 'Schedule Transfer of Billing Documents - Global Trade Services (F3740)' and F3741 is the material documents app.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Notes state the master-data change-point background jobs are scheduled hourly and the rhythm cannot be changed, yet 'Schedule Transfer of Changed Master Data' (F6041) has the tester schedule daily (Every 1 Day) jobs for the same change pointers.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-compliance-management-with-sap-global-trade-services-24j-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3JX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 106,577 chars in the whole document
