---
id: 13-quality-ehs-and-compliance/test-script-compliance-management-with-sap-global-trade-services-24j-a
title: "Test Script: Compliance Management with SAP Global Trade Services (24J_AE) (24J_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 24J: GTS document transfer settings, test steps for transferred documents and reprocessing, GTS mapping appendix."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/gts-compliance-and-preference]
aliases: [24J_S4CLD2608_BPD_EN_AE]
keywords: [SAP GTS Compliance and Preference Management Integration, global trade services integration, document transfer control settings, trade compliance checks, export control statement, transferred document check, document reprocessing, gts configuration mapping, business roles, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24J_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-806
topic: 13-quality-ehs-and-compliance/gts-compliance-and-preference
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Compliance Management with SAP Global Trade Services (24J_AE) (24J_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24J_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **SAP GTS Compliance and Preference Management Integration** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Compliance Management with SAP Global Trade Services (24J_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848823)

[2 Prerequisites 4](#_Toc232848824)

[2.1 Additional Manual Configuration 4](#_Toc232848825)

[2.2 System Access 4](#_Toc232848826)

[2.3 Roles 4](#_Toc232848827)

[2.4 Business Conditions 5](#_Toc232848828)

[2.5 Master Data, Organizational Data, and Other Data 6](#_Toc232848829)

[3 Preliminary Steps 7](#_Toc232848830)

[3.1 Configure Control Settings for Document Transfer 7](#_Toc232848831)

[4 Overview Table 13](#_Toc232848832)

[5 Test Procedures 14](#_Toc232848833)

[5.1 Create Document 14](#_Toc232848834)

[5.2 Check Transferred Documents in SAP Global Trade Services System 17](#_Toc232848835)

[5.3 Schedule Reprocessing of Documents (Optional) 19](#_Toc232848836)

[6 Appendix 21](#_Toc232848837)

[6.1 Additional Configurations in SAP Global Trade Services System 21](#_Toc232848838)

[6.1.1 Define Foreign Trade Organization 21](#_Toc232848839)

[6.1.2 Assign Company Code to Foreign Trade Organization 22](#_Toc232848840)

[6.1.3 Define Legal Units 22](#_Toc232848841)

[6.1.4 Assign Plant to Legal Unit 23](#_Toc232848842)

[6.1.5 Assign Partner Functions 24](#_Toc232848843)

[6.1.6 Assign Document Types 25](#_Toc232848844)

[6.1.7 Assign Item Categories 26](#_Toc232848845)

## Purpose

Overview

You can utilize existing rules in SAP Global Trade Services on-premise by integration with SAP S/4HANA Cloud Private Edition or SAP S/4HANA Cloud Public Edition.

This scope item enables the communication scenario and the appropriate RFC calls for synchronizing the relevant import and export documents. Successfully processing documents requires that the relevant customers and material masters already exist in the SAP Global Trade Services system.

|  |
| --- |
| Caution If you are activating the Compliance Management with SAP Global Trade Services (24J) check, it is not possible to activate either the Legal Control (1W8), Embargo Control (1WC) or Restricted Party Screening with SAP Watch List Screening (1WE) check in SAP S/4HANA Cloud Public Edition for international trade. Trade Compliance checks are to be done exclusively in either SAP S/4HANA Cloud Public Edition or Global Trade Services system. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/3f67d27c82b9842f9ccb675ac0d38319)

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA System | Accessible via FIORI Launchpad.Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Global Trade Services System | Your system administrator provides you the logon information to access the system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Please ask your system administrator to assign to the testers. |
| Administrator - International Trade | SAP_BR_ADMINISTRATOR_SLL | International Trade Administration | SAP_BR_ADMINISTRATOR_SLL | Please ask your system administrator to assign to the testers. |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | Please ask your system administrator to assign to the testers. |
| Trade Compliance Specialist (GTS) | SAP_BR_CMPLNC_SPCLST_LLS | Compliance | SAP_LLS_SP_CMPLNC_SPCLST | This role template is used in SAP Global Trade Services, edition for SAP HANA. |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 1WA - Transfer of Primary Master Data for SAP Global Trade Services | The product master data has been transferred into SAP Global Trade Services system.The customer master data, which is relevant for export sales document transfer, has been transferred into SAP Global Trade Services system.The supplier master data, which is relevant for import purchasing document transfer, has been transferred into SAP Global Trade Services system. |

Additional Configurations in SAP Global Trade Services System:

To make the master data transfer successful, additional configurations might be needed in SAP Global Trade Services system, for example, the regions in address, the mapping of document types and partner functions. These configurations depend on your SAP Global Trade Services system, and are not covered in this document. The following are the minimum configurations needed:

- Company Code Mapping to FTO
- Plant Mapping to Legal Unit
- Partner Function Mapping
- Document Type and Item Category Mapping (Sales Order, Purchasing Document and Delivery)

|  |
| --- |
| Note You can check the details by referring to [Additional Configurations in SAP Global Trade Services System](#unique_7) [page ] 21. |

If the transfer is not successful, you may check the application logs in SAP Global Trade Services system to get the error details and then fix it.

### Master Data, Organizational Data, and Other Data

|  |
| --- |
| Note As the test steps in the SAP S/4HANA Cloud Public Edition system are described in the reference scope items, see the corresponding scope items that are listed in the [Create Document](#unique_9) [page ] 14 section to get the related organizational data and master data information. |

## Preliminary Steps

### Configure Control Settings for Document Transfer

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
| 6 | SD0A Settings | Select the leftmost checkbox for the application level SD0A entry. In the Dialog Structure pane, double-click Document Types. |  |  |
| 7 | SD0A Settings | Note If you need to transfer documents of a sales order type that is not listed, create an appropriate sales order type by choosing New Entries.For the sales order type you want to modify (for example, TA), select the leftmost checkbox, then choose Details.Under Control Settings, select Document Type for the Activation Level.Note To activate document transfer at the organization level, you need to select one of the organization levels for the Activation Level, such as Document Type/Company Code. After selecting this level, double-click on it in the left Dialog Structure pane, and then enable the document transfer for the organizations within the chosen level.You can select the organization level that best suits your requirements. The following organization levels are supported for the Activation Level:Document Type/Company CodeDocument Type/Sales OrganizationDocument Type/PlantDocument Type/Sales Organization and PlantDocument Type/Purchasing OrganizationDocument Type/Purchasing Organization and PlantSelect the Compliance Management checkbox to enable the document transfer for this sales type.To display the results of your transfer to the SAP Global Trade Services system, simply select the GTS Dialog checkbox.Note Once the GTS Dialog (Output Dialog in SAP Global Trade Services) checkbox is enabled, the transfer results are only displayed when the document you posted is blocked by SAP Global Trade Services. If the document is not blocked, the transfer results will not be displayed.Note To access more control settings, make sure the leftmost checkbox for the sales order type is selected, then click on Details.Note To prevent the creation of deliveries for blocked sales orders, double-click on the row of the sales order type and select the Prevent Delivery Creation for blocked Sales Documents checkbox.To prevent the creation of purchase requisitions for blocked sales orders, double-click on the row of the sales order type and select the Prevent Purchase Requisition Creation for blocked Sales Orders checkbox.To prevent output from sales documents for blocked sales orders, double-click on the row of the sales order type and check the Prevent Output for blocked Sales Documents checkbox. | The document transfer control settings have been configured for the selected sales order types. |  |
| 8 | Application Level | In the Dialog Structure pane, double-click Application Level. |  |  |
| 9 | SD0B Settings | Repeat steps 6 to 8 for the following data:Application Level: SD0BDoc.Type: LFNote Choose New Entries to configure the document type if it is not listed.Activation Level: Document TypeCompliance Management: <Selected>GTS Dialog: <Selected>Note To prevent goods issue for blocked outbound deliveries, double-click the row of the outbound delivery type and select the Prevent Goods Issue for blocked Outbound Deliveries checkbox. | The document transfer control settings have been configured for the selected outbound delivery types. |  |
| 10 | MM0A Settings | Repeat steps 6 to 8 for the following data:Application Level: MM0ADoc.Type: FNBNote Choose New Entries to configure the document type if it is not listed.Activation Level: Document TypeCompliance Management: <Selected>GTS Dialog: <Selected>Note To prevent the output for blocked purchase order or scheduling agreement, double-click the row of the purchasing document type and select the Prevent Output for blocked Purchasing Documents checkbox. | The document transfer control settings have been configured for the selected purchasing document types. |  |
| 11 | MM0B Settings | Repeat steps 6 to 8 for the following data:Application Level: MM0BDoc.Type: ELNote Choose New Entries to configure the document type if it is not listed.Activation Level: Document TypeCompliance Management: <Selected>GTS Dialog: <Selected> | The document transfer control settings have been configured for the selected inbound delivery types. |  |
| 12 | Save | Choose Save. | The settings are saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Control Settings for Document Transfer | Go to the Business Processes Configuration app and search for the following activity: Configure Control Settings for Document Transfer.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Control Settings for Document Transfer screen displays. |  |
| 3 | SD0A Settings | Select the leftmost checkbox for the application level SD0A entry. In the Dialog Structure pane, double-click Document Types. |  |  |
| 4 | SD0A Settings | Note If you need to transfer documents of a sales order type that is not listed, create an appropriate sales order type by choosing New Entries.For the sales order type you want to modify (for example, TA), select the leftmost checkbox, then choose Details.Under Control Settings, select Document Type for the Activation Level.Note To activate document transfer at the organization level, you need to select one of the organization levels for the Activation Level, such as Document Type/Company Code. After selecting this level, double-click on it in the left Dialog Structure pane, and then enable the document transfer for the organizations within the chosen level.You can select the organization level that best suits your requirements. The following organization levels are supported for the Activation Level:Document Type/Company CodeDocument Type/Sales OrganizationDocument Type/PlantDocument Type/Sales Organization and PlantDocument Type/Purchasing OrganizationDocument Type/Purchasing Organization and PlantSelect the Compliance Management checkbox to enable the document transfer for this sales type.To display the results of your transfer to the SAP Global Trade Services system, simply select the GTS Dialog checkbox.Note Once the GTS Dialog (Output Dialog in SAP Global Trade Services) checkbox is enabled, the transfer results are only displayed when the document you posted is blocked by SAP Global Trade Services. If the document is not blocked, the transfer results will not be displayed.Note To access more control settings, make sure the leftmost checkbox for the sales order type is selected, then click on Details.Note To prevent the creation of deliveries for blocked sales orders, double-click on the row of the sales order type and select the Prevent Delivery Creation for blocked Sales Documents checkbox.To prevent the creation of purchase requisitions for blocked sales orders, double-click on the row of the sales order type and select the Prevent Purchase Requisition Creation for blocked Sales Orders checkbox.To prevent output from sales documents for blocked sales orders, double-click on the row of the sales order type and check the Prevent Output for blocked Sales Documents checkbox. | The document transfer control settings have been configured for the selected sales order types. |  |
| 5 | Application Level | In the Dialog Structure pane, double-click Application Level. |  |  |
| 6 | SD0B Settings | Repeat steps 3 to 5 for the following data:Application Level: SD0BDoc.Type: LFNote Choose New Entries to configure the document type if it is not listed.Activation Level: Document TypeCompliance Management: <Selected>GTS Dialog: <Selected>Note To prevent goods issue for blocked outbound deliveries, double-click the row of the outbound delivery type and select the Prevent Goods Issue for blocked Outbound Deliveries checkbox. | The document transfer control settings have been configured for the selected outbound delivery types. |  |
| 7 | MM0A Settings | Repeat steps 3 to 5 for the following data:Application Level: MM0ADoc.Type: FNBNote Choose New Entries to configure the document type if it is not listed.Activation Level: Document TypeCompliance Management: <Selected>GTS Dialog: <Selected>Note To prevent the output for blocked purchase order or scheduling agreement, double-click the row of the purchasing document type and select the Prevent Output for blocked Purchasing Documents checkbox. | The document transfer control settings have been configured for the selected purchasing document types. |  |
| 8 | MM0B Settings | Repeat steps 3 to 5 for the following data:Application Level: MM0BDoc.Type: ELNote Choose New Entries to configure the document type if it is not listed.Activation Level: Document TypeCompliance Management: <Selected>GTS Dialog: <Selected> | The document transfer control settings have been configured for the selected inbound delivery types. |  |
| 9 | Save | Choose Save. | The settings are saved. |  |

## Overview Table

The scope item Compliance Management with SAP Global Trade Services consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Document](#unique_9) [page ] 14 | Please refer to the reference scope items which are listed in the next chapter Create Document. | The Apps are given in the reference scope items which are listed in the next chapter Create Document. | The document is automatically transferred to SAP Global Trade Services system along when saving the document in S/4HANA Cloud system. |
| [Check Transferred Documents in SAP Global Trade Services System](#unique_12) [page ] 17 | The business role is applicable to SAP Global Trade Services, edition for SAP HANA:Trade Compliance Specialist (GTS) | /n/SAPSLL/MENU_LEGALThe App is applicable to SAP Global Trade Services, edition for SAP HANA:Display Documents - Compliance Management(F4403) | The transferred document is in SAP Global Trade Services system. |
| [Schedule Reprocessing of Documents (Optional)](#unique_13) [page ] 19 | Administrator - International Trade | Schedule Reprocessing of Documents - Global Trade Services (F3050) | The background job of reprocessing documents is scheduled. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the sales order, purchasing document or delivery document, which triggers the document transfer to the SAP Global Trade Services system.

Prerequisites

|  |
| --- |
| Caution Before you start the test procedures, ensure the Set-up Instruction Guide of this scope item is executed, so as to ensure working connectivity between the SAP S/4HANA Cloud Public Edition system and the SAP Global Trade Services system. |

Procedure

|  |
| --- |
| Note The following Apps are available for initial transfer of documents, and you can log onto the SAP Fiori launchpad to access these Apps by using the role Administrator - International Trade:Schedule Transfer of Sales Documents - Global Trade Services (F4540)Schedule Transfer of Outbound Deliveries - Global Trade Services (F4539)Schedule Transfer of Purchasing Documents - Global Trade Services (F3742)Schedule Transfer of Inbound Deliveries - Global Trade Services (F4541)The App Sales Order Fulfillment - Analyze and Resolve Issues (F0029A) allows you to analyze and resolve issues that impede sales orders from being fulfilled. With this App, you can filter on Trade Compliance Issue in Sales Orders to display sales orders that are transferred into SAP Global Trade Services system and are being blocked due to trade compliance reasons. To access this App, you can log onto the SAP Fiori launchpad by using the role Internal Sales Representative.Once the sales order is released in SAP Global Trade Services system, the updated status can be automatically synchronized to SAP S/4HANA Cloud Public Edition system. When the status update is not successful due to technical reasons, for example the sales order is being blocked in SAP S/4HANA Cloud Public Edition, you can use the following App to schedule the status update job to get the sales order updated in SAP S/4HANA Cloud Public Edition. To access this App, you can log onto the SAP Fiori launchpad by using the role Administrator - International Trade:Schedule Sales Document Status Update - Global Trade Services (F5721)The following App is available for display sales and outbound delivery documents which are blocked in SAP Global Trade Services system. To access this App, you can log onto the SAP Fiori launchpad by using the role Internal Sales Representative, and use App Finder to add this Fiori tile to the homepage:Display Blocked Export Documents (/SAPSLL/BL_DOC_SD_R3) |

|  |
| --- |
| Note Printing of the export control statement is now supported for the delivery note and packing list forms. For necessary modifications to this functionality in the SAP Global Trade Services system, please refer to SAP Note [3639669](https://me.sap.com/notes/3639669). To include the export control statement in the print forms, configure the following settings:Create your own form templates based on the delivery note form template FDP_V2_DELIVERY_NOTE_V1 and the packing list form template FDP_PACKING_LIST. Refer to the guide [How to Create and Use a Custom Form Template](https://help.sap.com/docs/SAP_S4HANA_CLOUD/aff0b3f5f46c42a2b2c0fabfc233bab2/a8deb56a62d44dc087fb6f85e1b99304.html?version=LATEST&locale=en-US) for detailed instructions.Please note that the Maintain Form Templates (F1434) app can be accessed using the business role SAP_BR_EXTENSIBILITY_SPEC, while the Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app requires the business role SAP_BR_ADMINISTRATOR.In the delivery note form template, opened via the Adobe LiveCycle Designer, add the following field:TradeComplianceStatementText under TradeComplianceStatementNode: represents the trade compliance statementIn the packing list form template, opened via the Adobe LiveCycle Designer, add the following fields:Textline under ForeignTradeHeaderTextNode: represents the trade compliance statement at header levelTextline under ForeignTradeItemTextNode: represents the trade compliance statement at item levelActivate the compliance check for the outbound delivery type in the configuration activity [Configure Control Settings for Document Transfer](#unique_10) [page ] 7.Create the text templates for the trade compliance statements in the configuration activity Define Trade Text Templates.The texts are language dependent. The Trade Compliance Item Statement template type supports the following placeholders: <<LEGAL_REGULATION>>, <<CONTROL_CLASS>>, <<LICENSE_NUMBER>>, <<LICENSE_VALID_FROM>>, <<LICENSE_VALID_TO>>. You can include the needed placeholders in your item-level statements.Specify which header-level statement should be included in the print forms in the configuration activity Specify Output of Trade Compliance Statements.To meet your specific legal requirements, you can either choose a pre-delivered compliance statement, such as the Destination Control Statement, or your own defined text template.Specify which item-level statement should be included in the print forms in the configuration activity Specify Output of Trade Compliance Item Statements.Use your own defined text template for the item-level statement. You can also exclude statement output for specific control classes.The legal control check has to be activated in SAP Global Trade Services system, and the product used for export sales must be control relevant within this system.A valid export license must be maintained in the SAP Global Trade Services system, and this license must be identified within the customs document. |

|  |
| --- |
| Note The following configuration activities allow you to prevent the distribution of outbound deliveries to warehouses in case the deliveries are blocked by compliance check in the SAP Global Trade Services system:Configure Control Settings for SAP EWM managed warehousesConfigure Control Settings for 3PL warehouses |

|  |
| --- |
| Note The payment run integration with SAP Global Trade Services is now supported. To enable this functionality, go to the following configuration activity:Activate Check in SAP Global Trade Services for FI PaymentsFor details on payment run and screening with SAP Global Trade Services, refer to the scope item J60 – Accounts Payable. |

|  |
| --- |
| Note No testing step is provided here. As the document transfer is automatically triggered along with saving the document in the SAP S/4HANA Cloud Public Edition system, you may follow the procedures which are described in the reference scope items to create the documents. The reference document types and the associated scope items are listed below: |

| Process | Document Type | Scope Item |
| --- | --- | --- |
| Export - Sales | TA (Standard Order) | BD9 -Sell from StockBD3 -Sales Processing using Third-Party with Shipping NotificationBDH -Sales Order Entry with One-Time CustomerBDK -Sales Processing Using Third-Party Without Shipping NotificationBDN -Sales of Non-Stock Item with Order-Specific ProcurementBDW -Returnables ProcessingBKJ -Sales Order Processing with Customer Down Payment1HO -Intercompany Sales Order Processing – Domestic1MX -Intercompany Sales Order Processing – International |
|  | CBFD (Deliv.Free of Charge) | BDA -Free of Charge Delivery |
|  | SD2 (Replcmnt Deliv. Ord.) | BKP -Customer Returns |
|  | CBMO (MTO Standard Order) | BJE -Make-to-Order Production – Finished Goods Sales and Final Assembly1BM -Make-to-Order Production – Semifinished Goods Planning and Assembly |
|  | CBMQ (MTO Quotation) | BJE -Make-to-Order Production – Finished Goods Sales and Final Assembly1BM -Make-to-Order Production – Semifinished Goods Planning and Assembly |
| Export - Outbound Delivery | LF (Outbound Delivery) | BD9 -Sell from StockBDH -Sales Order Entry with One-Time CustomerBDN -Sales of Non-Stock Item with Order-Specific ProcurementBDW -Returnables ProcessingBKJ -Sales Order Processing with Customer Down Payment1HO -Intercompany Sales Order Processing – Domestic1MX -Intercompany Sales Order Processing – International |
|  | NL (Replenishment Dlv.) | BME -Stock Transfer with Delivery |
|  | LO (Delivery w/o Ref.) | 1MI -Delivery Processing Without Order Reference |
| Import - Purchasing | NB (F - Purchase Order, Standard PO) | J45 -Procurement of Direct MaterialsBMD -Purchase Contract |
|  | UB (F - Purchase Order, Stock Transp. Order) | BMH -Stock Transfer Without Delivery |
|  | UD (F - Purchase Order, StockTranspOrderDel) | BME -Stock Transfer with Delivery |
|  | LP (L - Scheduling Agreement, Scheduling Agreement) | BMR -Scheduling Agreements in Procurement2NX -Scheduling Agreement for Subcontracting Procurement2NY -Scheduling Agreement for Consignment Procurement |
|  | LPA (L - Scheduling Agreement, SA With Release doc.) | BMR -Scheduling Agreements in Procurement |
| Import - Inbound Delivery | EL (Inbound Delivery) | 2TX -Direct Procurement with Inbound DeliveryBD3 -Sales Processing using Third-Party with Shipping Notification |

### Check Transferred Documents in SAP Global Trade Services System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you check the transferred document in SAP Global Trade Services system.

Procedure

|  |
| --- |
| Note If your GTS system is SAP Global Trade Services, edition for SAP HANA, the steps are different, so please check the steps after this section. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP GUI | Log onto the SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Check Transferred Document | In the Command field, enter /n/SAPSLL/MENU_LEGAL and press Enter. | The SAP Global Trade Services view is displayed. |  |
| 3 | Export | Choose Compliance Management > SAP Legal Control - Export . | The Compliance Management: Legal Control - Export view displays. |  |
| 4 | Check Transferred Documents | In the Monitoring area, check the transferred documents with one of the following options:Execute Display Existing Documents to check all transferred documents.Execute Display Blocked Documents to check the blocked documents.Execute Display Technically Incomplete Documents to see if the transferred documents are technically incomplete. |  |  |
| 5 | Check Transferred Documents | Enter some selection values to execute (for example, enter the sales order or outbound delivery document number in the Reference Number field). You can then check the selected documents. | The transferred export documents are checked. |  |
| 6 | Import | Choose Compliance Management > SAP Legal Control - Import . | The Compliance Management: Legal Control - Import view displays. |  |
| 7 | Check Transferred Documents | In the Monitoring area, check the transferred documents with one of the following options:Execute Display Existing Documents to check all transferred documents.Execute Display Blocked Documents to check the blocked documents.Execute Display Technically Incomplete Documents to see if the transferred documents are technically incomplete. |  |  |
| 8 | Check Transferred Documents | Enter some selection values to execute (for example, enter the purchasing order or inbound delivery document number in the Reference Number field). You can then check the selected documents. | The transferred export documents are checked. |  |

|  |
| --- |
| Note The following steps are applicable to SAP Global Trade Services, edition for SAP HANA. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Trade Compliance Specialist (GTS). |  |  |
| 2 | Access App | Choose Display Documents - Compliance Management (F4403). |  |  |
| 3 | Check Transferred Documents | Enter the created document number in the Reference Number field, and choose Go. You can then check the selected documents. | The transferred documents are checked. |  |

### Schedule Reprocessing of Documents (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule background job to reprocess the documents if the document transfer is discontinued due to some technical reasons.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. |  |  |
| 2 | Access App | Choose Schedule Reprocessing of Documents - Global Trade Services (F3050). | The Application Jobs screen displays. |  |
| 3 | Create Schedule Reprocessing of Documents Background Job | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Schedule Reprocessing of Documents - Global Trade ServicesJob Name: Schedule Reprocessing of Documents - Global Trade Services |  |  |
| 5 | Scheduling Options | Choose Define Recurrence Pattern. Make the following entries and choose OK. Then choose Step 3:Start Immediately: <Select>Recurrence Pattern: Single Run |  |  |
| 6 | Schedule | Choose Schedule. | The job is scheduled and shown in the list.Note In actual business, you may create periodic background jobs. |  |

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

#### Assign Document Types

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | IMG Path | In the IMG, go to the following path: SAP Global Trade Services > General Settings > Document Structure > Assignment of Document Types from Feeder Systems > Assign Document Type at Feeder System Group Level . | The Choose Activity dialog box displays. |  |
| 4 | Assign Document Types | Choose Manually Assign Document Type. | The the Change View “Mapping: Feeder System Group Doc. Type to SAP GTS Doc. Ty” view displays. |  |
| 5 | Assign Document Types | Choose New Entries.If necessary, make the following entries and choose Save:Application LevelLogical System GroupDoc. Type Feed. Sys.Document TypeSD0A<logical system group>for example TAEXPORDSD0B<logical system group>for example LFEXPDLVMM0A<logical system group>for example FNBIMPORDMM0B<logical system group>for example ELDTAVI | The document type mapping is maintained. |  |

#### Assign Item Categories

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | IMG Path | In the IMG, go to the following path: SAP Global Trade Services > General Settings > Document Structure > Assignment of Item Categories from Feeder Systems > Assign Item Category at Feeder System Group Level . | The Choose Activity dialog box displays. |  |
| 4 | Assign Item Category | Choose Manually Assign Item Category. | The Change View “Mapping: FS Item Cat. Group to SAP GTS Item Cat. Group” screen displays. |  |
| 5 | Assign Item Categories | Choose New Entries.If necessary, make the following entries and choose Save:Application LevelLogical System GroupItem Category (FS)Item CategorySD0A<logical system group>for example TANEXORD1SD0B<logical system group>for example TANEXDLV1MM0A<logical system group>IMORD1MM0B<logical system group>for example ELNIMORD1 | The item category mapping is maintained. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/test-script-preference-management-with-sap-global-trade-services-3jx-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24J_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 46,212 chars in the whole document
