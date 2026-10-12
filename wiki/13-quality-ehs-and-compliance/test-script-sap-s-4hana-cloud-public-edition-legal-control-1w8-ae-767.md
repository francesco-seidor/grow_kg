---
id: 13-quality-ehs-and-compliance/test-script-sap-s-4hana-cloud-public-edition-legal-control-1w8-ae-767
title: Test Script SAP S/4HANA Cloud Public Edition - Legal Control (1W8_AE) (1W8_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 1W8 Legal Control (UAE, company code 3310): configuration, master data, control classes, licenses, allow/blocklisting rules, inbound and outbound checks."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/trade-classification-and-legal-control]
aliases: [1W8_S4CLD2608_BPD_EN_AE]
keywords: [Trade Classification and Legal Control, legal control, trade compliance, control classes, product classification, trade licenses, allowlisting rules, blocklisting rules, license type rules, legal control configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1W8_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-767
topic: 13-quality-ehs-and-compliance/trade-classification-and-legal-control
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Legal Control (1W8_AE) (1W8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1W8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Trade Classification and Legal Control** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 14-07-26 |
| --- | --- |
|  | Legal Control (1W8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc237128350)

[2 Prerequisites 5](#_Toc237128351)

[2.1 System Access 5](#_Toc237128352)

[2.2 Roles 5](#_Toc237128353)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc237128354)

[2.4 Additional Manual Configuration 8](#_Toc237128355)

[2.5 Preliminary Steps 9](#_Toc237128356)

[2.5.1 Configuration Activities with DEMO Data 9](#_Toc237128357)

[2.5.2 Configuration Activities Without DEMO Data 13](#_Toc237128358)

[2.5.3 Create Testing Business Partner 23](#_Toc237128359)

[2.5.3.1 Create Testing Business Partner for North Korea (KP) 23](#_Toc237128360)

[2.5.3.2 Create Testing Supplier 25](#_Toc237128361)

[2.5.4 Maintain Condition Record 26](#_Toc237128362)

[3 Overview Table 29](#_Toc237128363)

[4 Test Procedures 35](#_Toc237128364)

[4.1 Basic Process of Legal Control 35](#_Toc237128365)

[4.1.1 Manage Control Classes 35](#_Toc237128366)

[4.1.1.1 Manage Control Classes 35](#_Toc237128367)

[4.1.1.2 Manage Control Classes from Data Provider (Optional) 36](#_Toc237128368)

[4.1.1.2.1 Schedule Control Classes Content Request to Data Provider (Background Job) 36](#_Toc237128369)

[4.1.1.2.2 Manage Control Classes Content from Data Provider 37](#_Toc237128370)

[4.1.1.3 Manage Control Groupings (Optional) 38](#_Toc237128371)

[4.1.2 Classify Products - Legal Control 39](#_Toc237128372)

[4.1.2.1 Classify Products - Legal Control 39](#_Toc237128373)

[4.1.2.2 Reclassify Products - Legal Control (Optional) 40](#_Toc237128374)

[4.1.2.3 Display Classified Products 41](#_Toc237128375)

[4.1.3 Inbound Process 43](#_Toc237128376)

[4.1.3.1 Manage Purchase Documents 43](#_Toc237128377)

[4.1.3.1.1 Manage Purchase Orders 43](#_Toc237128378)

[4.1.3.1.2 Manage Stock Transfer Orders (Optional) 44](#_Toc237128379)

[4.1.3.1.3 Manage Purchase Scheduling Agreements (Optional) 45](#_Toc237128380)

[4.1.3.1.4 Manage Purchase Requisitions (Optional) 45](#_Toc237128381)

[4.1.3.2 Manage Licenses - Trade Compliance 45](#_Toc237128382)

[4.1.3.3 Manage Documents - Trade Compliance 46](#_Toc237128383)

[4.1.3.4 Check Purchase Order Status 48](#_Toc237128384)

[4.1.3.5 Manage Inbound Deliveries 48](#_Toc237128385)

[4.1.4 Outbound Process 49](#_Toc237128386)

[4.1.4.1 Manage Sales Documents 49](#_Toc237128387)

[4.1.4.1.1 Manage Sales Orders 50](#_Toc237128388)

[4.1.4.1.2 Manage Sales Orders Without Charge (Optional) 51](#_Toc237128389)

[4.1.4.1.3 Manage Sales Scheduling Agreements (Optional) 51](#_Toc237128390)

[4.1.4.2 Manage Licenses - Trade Compliance 51](#_Toc237128391)

[4.1.4.3 Manage Documents - Trade Compliance 53](#_Toc237128392)

[4.1.4.4 Manage Outbound Deliveries 54](#_Toc237128393)

[4.1.5 Schedule Recheck Documents Background Job for Trade Compliance (Optional) 55](#_Toc237128394)

[4.1.6 Display License Assignments 56](#_Toc237128395)

[4.1.7 Analyze and Resolve Blocked Documents 57](#_Toc237128396)

[4.2 Manage Legal Control Rule for Allowlisting 58](#_Toc237128397)

[4.2.1 Manage Control Classes 58](#_Toc237128398)

[4.2.2 Classify Products - Legal Control 59](#_Toc237128399)

[4.2.3 Maintain Decision Table for Allowlisting 60](#_Toc237128400)

[4.2.4 Inbound Process 61](#_Toc237128401)

[4.2.4.1 Manage Purchase Documents 61](#_Toc237128402)

[4.2.4.1.1 Manage Purchase Orders 62](#_Toc237128403)

[4.2.4.1.2 Manage Stock Transfer Orders (Optional) 63](#_Toc237128404)

[4.2.4.1.3 Manage Purchase Scheduling Agreements (Optional) 63](#_Toc237128405)

[4.2.4.1.4 Manage Purchase Requisitions (Optional) 63](#_Toc237128406)

[4.2.4.2 Manage Documents - Trade Compliance 63](#_Toc237128407)

[4.2.5 Outbound Process 64](#_Toc237128408)

[4.2.5.1 Manage Sales Documents 64](#_Toc237128409)

[4.2.5.1.1 Manage Sales Orders 65](#_Toc237128410)

[4.2.5.1.2 Manage Sales Orders Without Charge (Optional) 66](#_Toc237128411)

[4.2.5.1.3 Manage Sales Scheduling Agreements (Optional) 66](#_Toc237128412)

[4.2.5.2 Manage Documents - Trade Compliance 66](#_Toc237128413)

[4.3 Manage Legal Control Rule for Blocklisting 67](#_Toc237128414)

[4.3.1 Maintain Decision Table for Blocklisting 67](#_Toc237128415)

[4.3.2 Inbound Process 68](#_Toc237128416)

[4.3.2.1 Manage Purchase Documents 68](#_Toc237128417)

[4.3.2.1.1 Manage Purchase Orders 69](#_Toc237128418)

[4.3.2.1.2 Manage Purchase Scheduling Agreements (Optional) 70](#_Toc237128419)

[4.3.2.1.3 Manage Purchase Requisitions (Optional) 70](#_Toc237128420)

[4.3.2.2 Manage Documents - Trade Compliance 71](#_Toc237128421)

[4.3.3 Outbound Process 71](#_Toc237128422)

[4.3.3.1 Manage Sales Documents 71](#_Toc237128423)

[4.3.3.1.1 Manage Sales Orders 72](#_Toc237128424)

[4.3.3.1.2 Manage Sales Orders Without Charge (Optional) 73](#_Toc237128425)

[4.3.3.1.3 Manage Sales Scheduling Agreements (Optional) 73](#_Toc237128426)

[4.3.3.2 Manage Documents - Trade Compliance 73](#_Toc237128427)

[4.4 Manage Legal Control Rule for License Types based on Control Class and Country 74](#_Toc237128428)

[4.4.1 Maintain License Types based on Control Class and Country 74](#_Toc237128429)

[4.4.2 Inbound Process 76](#_Toc237128430)

[4.4.2.1 Manage Purchase Documents 76](#_Toc237128431)

[4.4.2.1.1 Manage Purchase Orders 76](#_Toc237128432)

[4.4.2.1.2 Manage Stock Transfer Orders (Optional) 77](#_Toc237128433)

[4.4.2.1.3 Manage Purchase Scheduling Agreements (Optional) 78](#_Toc237128434)

[4.4.2.1.4 Manage Purchase Requisitions (Optional) 78](#_Toc237128435)

[4.4.2.2 Manage Documents - Trade Compliance 78](#_Toc237128436)

[4.4.3 Outbound Process 79](#_Toc237128437)

[4.4.3.1 Manage Sales Documents 79](#_Toc237128438)

[4.4.3.1.1 Manage Sales Orders 79](#_Toc237128439)

[4.4.3.1.2 Manage Sales Orders Without Charge (Optional) 80](#_Toc237128440)

[4.4.3.1.3 Manage Sales Scheduling Agreements (Optional) 81](#_Toc237128441)

[4.4.3.2 Manage Documents - Trade Compliance 81](#_Toc237128442)

## Purpose

Overview

This scope item supports global trade compliance with checks of relevant documents for adherence to the defined trade regulations.

You can classify materials, define regulations and licenses, and activate export checks for documents and company codes. When relevant sales or purchasing documents are generated, and documents in violation of the trade policies are blocked, these blocked documents are resolved to remain compliant.

|  |
| --- |
| Caution If you are activating the Legal Control (1W8) check in SAP S/4HANA Cloud Public Edition for international trade, it is not possible to activate the Compliance Management with SAP Global Trade Services (24J). Trade Compliance checks are to be done exclusively in either SAP S/4HANA Cloud Public Edition or Global Trade Services system. |

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
| Trade Classification Specialist | SAP_BR_TRD_CLS_SPECIALIST | International Trade Classification | SAP_BR_TRD_CLS_SPECIALIST |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |
| Trade Compliance Specialist | SAP_BR_TRD_CMPLNC_SPECIALIST | International Trade Compliance | SAP_BR_TRD_CMPLNC_SPECIALIST |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Administrator - International Trade | SAP_BR_ADMINISTRATOR_SLL | International Trade Administration | SAP_BR_ADMINISTRATOR_SLL |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Table for Inbound

| Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Order Type | NB |  |  |
| Purchase Organization | 3310 | Purchase Org. 3310 |  |
| Purchase Group | 001 | Group 001 |  |
| Plant | 3310 | Plant 1 AE |  |
| Supplier | Please refer to [Create Testing Business Partner for North Korea (KP)](#unique_6) [page ] 23 to create a supplier XXXX for KP. Please refer to [Create Testing Supplier](#unique_7) [page ] 25 to create a supplier XXXX for US. | Foreign Supplier XXXX | International Purchase |
| Goods Supplier | The same with the Supplier XXXX | Foreign Supplier XXXX | International Purchase |
| Material | TG12, TG0012 and TG0011 | Material Master Data TG12, TG0012 and TG0011 are used. |  |

|  |
| --- |
| Note Business documents supported by legal control for inbound process:Purchase OrdersStock Transfer Orders (optional)Purchase Scheduling Agreements (optional)Purchase Requisitions (optional) |

Table for Outbound

| Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Order Type | OR | Standard Sales Order |  |
| Sales Organization | 3310 | Sales Organization for AE |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Sold-To Party | 33100050 | Foreign Customer (US) | International Sales from United Arab Emirates to US |
| Ship-To Party | 33100050 | Foreign Customer (US) | International Sales from United Arab Emirates to US |
| Sold-To Party | Please refer to [Create Testing Business Partner for North Korea (KP)](#unique_6) [page ] 23 to create a customer XXXX for KP. | Foreign Customer XXXX (KP) | International Sales from United Arab Emirates to KP |
| Ship-To Party | The same with the Sold-To Party XXXX. | Foreign Customer XXXX (KP) | International Sales from United Arab Emirates to KP |
| Plant | 3310 | Plant 1 AE |  |
| Material | TG12, TG0012 and TG0011 | Material Master Data TG12, TG0012 and TG0011 are used. |  |

|  |
| --- |
| Note Business documents supported by legal control for outbound process:Sales OrdersSales Orders Without Charge (optional)Sales Scheduling Agreements (optional) |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/5e838bae9d0b0d2a3ac5a46a28876d7c)

### Preliminary Steps

#### Configuration Activities with DEMO Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the scope item was activated with Demo Data, the system has pre-delivered demo data configuration and you still need to maintain the following configurations by SSCUI and customizing activity before performing testing.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). Navigate to Configure Your Solution. | The Configure Your Solution view displays. |  |
| 3 | Configure Your Solution | In the Configure Your Solution: Realize Phase view, make the following entries:Application Area: FinanceSub Application Area: International Trade Management | Configuration items are shown. |  |
| 4 | Navigate to Configuration Step | Each time you access your configuration step, navigate to the Configure Your Solution: Realize Phase view and search for the step name in the Search field, for example, Activate Sales Documents.In the search result, select the configuration activity and go to the next screen. | Configuration steps are shown. |  |
| 5 | Activate Sales Documents | On the Configure Your Solution - General Settings for International Trade screen, go to the configuration step: Activate Sales Documents and choose Configure.Make the following entries and choose Save:Sales Document Type: For example, ORTrade Compliance: <Flag should be checked> | Sales order type is activated for Trade Compliance. |  |
| 6 | Activate Delivery Documents | On the Configure Your Solution - General Settings for International Trade screen, go to the configuration step: Activate Delivery Documents and choose Configure.Make the following entries and choose Save:Delivery Type: for example, LFTrade Compliance: <Flag should be checked> | Delivery type is activated for Trade Compliance. |  |
| 7 | Activate Checks for Purchasing Documents | Go to the configuration step: Activate Checks for Purchasing Documents and choose Configure.Make the following entries and choose Save:Purchase Document Type: for example, NBTrade Compliance: <Flag should be checked> | Purchase order type is activated for Trade Compliance. |  |
| 8 | Activate Checks for Company Codes | Go to the configuration step: Activate Checks for Company Codes and choose Configure.Make the following entries:Company Code: 3310Activation Level: Company Code LevelLegal Control: <Flag should be checked> | Company Code 3310 is activated for legal control. |  |
| 9 | Switch Off Subsequent Functions | Go to the configuration step: Switch Off Subsequent Functions and choose Configure.Choose New Entries.Make the following entries and choose Save:Trade Regulation Area: 01 Legal ControlStatus: B PendingSubsequent Functions: 03 Outbound Delivery CreationCondition active: <Flag should be checked> | Outbound delivery creation is not allowed since sales order is blocked by legal control.Note Suppressing of outputting corresponding sales documents is also supported.You can also choose C Blocked which means only confirm blocked Sales orders are not allowed to creating follow-on documents. |  |
| 10 | Configure Your Solution - Legal Control | Back to the Configure Your Solution: Realize Phase view, choose the item named Legal Control. | The Configure Your Solution - Legal Control view appears. |  |
| 11 | Control Settings for Legal Regulations for Legal Control | Search for the configuration step: Control Settings for Legal Regulations for Legal Control and choose Configure.Legal Regulation: for example, ITR01Product Maint.: B Only Specifically Selected Products Are Relevant for ChecksNumbering Scheme for Control Class: for example, QAL02Set the following flags as Checked:Check Outbound ProcessCheck Inbound ProcessCheck Third Country/Region ProcessCheck EU ProcessesBRFplus Application: ITR_LEGAL_CONTROL_RULESFunction for Allowlisting: ALLOWLISTINGFunction for Blocklisting: BLOCKLISTINGFunction for License Type: LICENSE_TYPE_DETERMINATIONChoose Save. | Legal regulation controls the products of which control classes are classified into and cover all the sales and purchase processes. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Configuration Activities | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity, for example, Activate Sales Documents.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The related configuration activities screen displays. |  |
| 3 | Activate Sales Documents | Make the following entries and choose Save:Sales Document Type: For example, ORTrade Compliance: <Flag should be checked> | Sales order type is activated for Trade Compliance. |  |
| 4 | Activate Delivery Documents | Go back to the Configuration Activities tab.Search for the following activity: Activate Delivery Documents.Make the following entries and choose Save:Delivery Type: for example, LFTrade Compliance: <Flag should be checked> | Delivery type is activated for Trade Compliance. |  |
| 5 | Activate Checks for Purchasing Documents | Search for the following activity: Activate Checks for Purchasing Documents.Make the following entries and choose Save:Purchase Document Type: for example, NBTrade Compliance: <Flag should be checked> | Purchase order type is activated for Trade Compliance. |  |
| 6 | Activate Checks for Company Codes | Search for the following activity: Activate Checks for Company Codes.Make the following entries:Company Code: 3310Activation Level: Company Code LevelLegal Control: <Flag should be checked> | Company Code 3310 is activated for legal control. |  |
| 7 | Switch Off Subsequent Functions | Search for the following activity: Switch Off Subsequent Functions.Choose New Entries.Make the following entries and choose Save:Trade Regulation Area: 01 Legal ControlStatus: B PendingSubsequent Functions: 03 Outbound Delivery CreationCondition active: <Flag should be checked> | Outbound delivery creation is not allowed since sales order is blocked by legal control.Note Suppressing of outputting corresponding sales documents is also supported.You can also choose C Blocked which means only confirm blocked Sales orders are not allowed to creating follow-on documents. |  |
| 8 | Control Settings for Legal Regulations for Legal Control | Search for the following activity: Control Settings for Legal Regulations for Legal Control.Legal Regulation: for example, ITR01Product Maint.: B Only Specifically Selected Products Are Relevant for ChecksNumbering Scheme for Control Class: for example, QAL02Set the following flags as Checked:Check Outbound ProcessCheck Inbound ProcessCheck Third Country/Region ProcessCheck EU ProcessesBRFplus Application: ITR_LEGAL_CONTROL_RULESFunction for Allowlisting: ALLOWLISTINGFunction for Blocklisting: BLOCKLISTINGFunction for License Type: LICENSE_TYPE_DETERMINATIONChoose Save. | Legal regulation controls the products of which control classes are classified into and cover all the sales and purchase processes. |  |

#### Configuration Activities Without DEMO Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the scope item was activated without Demo Data, the system has no pre-delivered Demo Data configuration and you will need to maintain all the following configurations by Configuration Activities before performing testing.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). Navigate to Configure Your Solution. | The Manage Your Solution view appears. |  |
| 3 | Configure Your Solution | In the Configure Your Solution: Realize Phase view, select Finance for Application AreaProduct-Specific Configuration and International Trade Management for Sub Application Area. | The Configure Your Solution: Realize Phase view is displayed. |  |
| 4 | Navigate to Configuration Step | To search for your configuration step, you could search for the step name in the Search field, for example, Activate Sales Documents.Or you could choose the configuration item and go to the next screen to see the configuration steps. | Configuration steps are shown. |  |
| 5 | Configure Your Solution - General Settings for International Trade | In the Configure Your Solution: Realize Phase view, choose the item named General Settings for International Trade. | The Configure Your Solution - General Settings for International Trade view appears. |  |
| 6 | Activate Sales Documents | Go to the configuration step: Activate Sales Documents and choose Configure.Sales Document Type: for example, ORTrade Compliance: <Flag should be checked>Choose Save. | Sales order type is activated for Trade Compliance. |  |
| 7 | Activate Delivery Documents | Go to the configuration step: Activate Delivery Documents and choose Configure.Delivery Type: for example, LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type is activated for Trade Compliance. |  |
| 8 | Activate Checks for Purchasing Documents | Go to the configuration step: Activate Checks for Purchasing Documents and choose Configure.Purchase Document Type: for example, NBTrade Compliance: <Flag should be checked>Choose Save. | Purchase order type is activated for Trade Compliance. |  |
| 9 | Activate Checks for Company Codes | Go to the configuration step: Activate Checks for Company Codes and choose Configure.Choose New Entries.Company Code: 3310Activation Level: Company Code LevelLegal Control: <Flag should be checked>Choose Save. | Company Code is activated for legal control. |  |
| 10 | Switch Off Subsequent Functions | Go to the configuration step: Switch Off Subsequent Functions and choose Configure.Choose New Entries.Trade Regulation Area: 01 Legal ControlStatus: B PendingSubsequent functions: 03 Outbound Delivery CreationCondition active: <Flag should be checked>Choose Save. | Outbound delivery creation is not allowed since sales order is blocked by legal control.Note Suppressing of outputting corresponding sales documents is also supported.You can also choose C Blocked which means only confirm blocked Sales orders are not allowed to creating follow-on documents |  |
| 11 | Define Trade Compliance Legal Regulations | Go to the configuration step: Define Trade Compliance Legal Regulations and choose Configure.Choose New Entries.Legal Regulation: for example, ITR01Description: Legal Regulation for International TradeTrade Regulation Area: Legal ControlChoose Save. | Legal regulation is defined. |  |
| 12 | Configure Your Solution - Classification | Back to the Configure Your Solution: Realize Phase view, choose the item named <Flag should be checked>Classification. | The Configure Your Solution - Classification view appears. |  |
| 13 | Define Numbering Scheme for Control Classes | Go to the configuration step: Define Numbering Scheme for Control Classes and choose Configure.Choose New Entries.Numbering Scheme: for example, QAL02Numbering Scheme Description: Control Classes for Legal Regulation ITR01Choose Save. | Numbering scheme is defined. |  |
| 14 | Define Numbering Scheme Content for Control Classes | Go to the configuration step: Define Numbering Scheme Content for Control Classes and choose Configure.Choose New Entries.No.Scheme Content: for example, QAL02No. Scheme Content Description: for example, Control Classes Content for Legal Regulation ITR01Content Source: LocalChoose Save. | Numbering scheme content is defined for control class.You can also log onto the SAP Fiori Launchpad using the Administrator - International Trade role, under tab Numbering Scheme Content Configuration , use app Define Numbering Scheme Content for Control Classes to configure the activity. The entries are the same as in this step. |  |
| 15 | Define Numbering Scheme Content for Control Classes (Optional) | Go to the configuration step: Define Numbering Scheme Content for Control Classes and choose Configure.Choose New Entries.No. Scheme Content: QAL02_DPNo. Scheme Content Description: Control classes provided by data providerContent Source: Data ProviderContent Reference: <Please check with data provider>Data Provider: _A BundesanzeigerClassification Number Length: <Please check with data provider>Choose Save. | It’s an optional step if the control classes are provided by Data Provider.The numbering scheme content is activated for control class.The data provider information depends on which data provider customers use. |  |
| 16 | Activate Numbering Scheme Content for Control Classes | Go to the configuration step: Activate Numbering Scheme Content for Control Classes and choose Configure.Enter Numbering Scheme: for example, QAL02, choose Continue (Enter).Choose New Entries.Valid From: 01/01/2017Valid To: 12/31/9999No. Scheme Content: For example, QAL02Choose Save. | Numbering scheme content is activated for control class.You can also log onto the SAP Fiori Launchpad using the Administrator - International Trade role, under tab Numbering Scheme Content Configuration , use app Activate Numbering Scheme Content for Control Classes to configure the activity. The entries are the same as in this step. |  |
| 17 | Configure Your Solution - Legal Control | Back to the Configure Your Solution: Realize Phase view, choose the item named Legal Control. | The Configure Your Solution - Legal Control view appears. |  |
| 18 | Activate Legal Regulations for Legal Control | Go to the configuration step: Activate Legal Regulations for Legal Control and choose Configure.Choose New Entries.Legal Regulation: for example, ITR01Country/Region:AEChoose Save. | Legal regulation is activated for specific country/ region. |  |
| 19 | Control Settings for Legal Regulations for Legal Control | Go to the configuration step: Control Settings for Legal Regulations for Legal Control and choose Configure.Choose New Entries.Legal Regulation: for example, ITR01Product Maint.: B Only Specifically Selected Products Are Relevant for ChecksNumbering Scheme for Control Class: for example, QAL02Please also set the following flags as Checked:Check Outbound ProcessCheck Inbound ProcessCheck Third Country/Region ProcessCheck EU ProcessesBRFplus Application: ITR_LEGAL_CONTROL_RULESFunction for Allowlisting: ALLOWLISTINGFunction for Blocklisting: BLOCKLISTINGFunction for License Types: LICENSE_TYPE_DETERMINATIONChoose Save. | Legal regulation controls the products which control classes are classified and cover all the sales processes. |  |
| 20 | Define License Type | Go to the configuration step: Define License Type and choose Configure.Legal Regulation: for example, ITR01Choose New Entries.License Type: LTY01 License type for legal regulation ITR01 - OutboundLicense Category: 02 General LicensePlease set the following General Attributes as Checked:Valid for Outbound ProcessesCountry/RegionControl ClassChoose Save.Choose New Entries.License Type: LTY02 License type for legal regulation ITR01 - InboundLicense Category: 02 General LicensePlease set the following General Attributes as Checked:Valid for Inbound ProcessesCountry/RegionControl ClassChoose Save. | License type is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Configuration Activities | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity, for example, Activate Sales Documents.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The related configuration activities screen displays. |  |
| 3 | Activate Sales Documents | Sales Document Type: for example, ORTrade Compliance: <Flag should be checked>Choose Save. | Sales order type is activated for Trade Compliance. |  |
| 4 | Activate Delivery Documents | Go to the Business Processes Configuration app.Search for the following activity: Activate Delivery Documents.Delivery Type: for example, LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type is activated for Trade Compliance. |  |
| 5 | Activate Checks for Purchasing Documents | Search for the following activity: Activate Checks for Purchasing Documents.Purchase Document Type: for example, NBTrade Compliance: <Flag should be checked>Choose Save. | Purchase order type is activated for Trade Compliance. |  |
| 6 | Activate Checks for Company Codes | Search for the following activity: Activate Checks for Company Codes.Choose New Entries.Company Code: 3310Activation Level: Company Code LevelLegal Control: <Flag should be checked>Choose Save. | Company Code is activated for legal control. |  |
| 7 | Switch Off Subsequent Functions | Search for the following activity: Switch Off Subsequent Functions.Search for the following activity: Switch Off Subsequent Functions.Choose New Entries.Trade Regulation Area: 01 Legal ControlStatus: B PendingSubsequent functions: 03 Outbound Delivery CreationCondition active: <Flag should be checked>Choose Save. | Outbound delivery creation is not allowed since sales order is blocked by legal control.Note Suppressing of outputting corresponding sales documents is also supported.You can also choose C Blocked which means only confirm blocked Sales orders are not allowed to creating follow-on documents |  |
| 8 | Define Trade Compliance Legal Regulations | Search for the following activity: Define Trade Compliance Legal Regulations.Choose New Entries.Legal Regulation: for example, ITR01Description: Legal Regulation for International TradeTrade Regulation Area: Legal ControlChoose Save. | Legal regulation is defined. |  |
| 9 | Define Numbering Scheme for Control Classes | Search for the following activity: Define Numbering Scheme for Control Classes.Choose New Entries.Numbering Scheme: for example, QAL02Numbering Scheme Description: Control Classes for Legal Regulation ITR01Choose Save. | Numbering scheme is defined. |  |
| 10 | Define Numbering Scheme Content for Control Classes | Search for the following activity: Define Numbering Scheme Content for Control Classes.Choose New Entries.No.Scheme Content: for example, QAL02No. Scheme Content Description: for example, Control Classes Content for Legal Regulation ITR01Content Source: LocalChoose Save. | Numbering scheme content is defined for control class.You can also log onto the SAP Fiori Launchpad using the Administrator - International Trade role, under tab Numbering Scheme Content Configuration , use app Define Numbering Scheme Content for Control Classes to configure the activity. The entries are the same as in this step. |  |
| 11 | Define Numbering Scheme Content for Control Classes (Optional) | Search for the following activity: Define Numbering Scheme Content for Control Classes.Choose New Entries.No. Scheme Content: QAL02_DPNo. Scheme Content Description: Control classes provided by data providerContent Source: Data ProviderContent Reference: <Please check with data provider>Data Provider: _A BundesanzeigerClassification Number Length: <Please check with data provider>Choose Save. | It’s an optional step if the control classes are provided by Data Provider.The numbering scheme content is activated for control class.The data provider information depends on which data provider customers use. |  |
| 12 | Activate Numbering Scheme Content for Control Classes | Search for the following activity: Activate Numbering Scheme Content for Control Classes.Enter Numbering Scheme: for example, QAL02, choose Continue (Enter).Choose New Entries.Valid From: 01/01/2017Valid To: 12/31/9999No. Scheme Content: For example, QAL02Choose Save. | Numbering scheme content is activated for control class.You can also log onto the SAP Fiori Launchpad using the Administrator - International Trade role, under tab Numbering Scheme Content Configuration , use app Activate Numbering Scheme Content for Control Classes to configure the activity. The entries are the same as in this step. |  |
| 13 | Activate Legal Regulations for Legal Control | Search for the following activity: Activate Legal Regulations for Legal Control.Choose New Entries.Legal Regulation: for example, ITR01Country/Region:AEChoose Save. | Legal regulation is activated for specific country/ region. |  |
| 14 | Control Settings for Legal Regulations for Legal Control | Search for the following activity: Control Settings for Legal Regulations for Legal Control.Choose New Entries.Legal Regulation: for example, ITR01Product Maint.: B Only Specifically Selected Products Are Relevant for ChecksNumbering Scheme for Control Class: for example, QAL02Please also set the following flags as Checked:Check Outbound ProcessCheck Inbound ProcessCheck Third Country/Region ProcessCheck EU ProcessesBRFplus Application: ITR_LEGAL_CONTROL_RULESFunction for Allowlisting: ALLOWLISTINGFunction for Blocklisting: BLOCKLISTINGFunction for License Types: LICENSE_TYPE_DETERMINATIONChoose Save. | Legal regulation controls the products which control classes are classified and cover all the sales processes. |  |
| 15 | Define License Type | Search for the following activity: Define License Type.Legal Regulation: for example, ITR01Choose New Entries.License Type: LTY01 License type for legal regulation ITR01 - OutboundLicense Category: 02 General LicensePlease set the following General Attributes as Checked:Valid for Outbound ProcessesCountry/RegionControl ClassChoose Save.Choose New Entries.License Type: LTY02 License type for legal regulation ITR01 - InboundLicense Category: 02 General LicensePlease set the following General Attributes as Checked:Valid for Inbound ProcessesCountry/RegionControl ClassChoose Save. | License type is defined. |  |

#### Create Testing Business Partner

##### Create Testing Business Partner for North Korea (KP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create a business partner for North Korea (KP) for legal control testing. Use the following entries (from step 1 to step 3) and refer to master data script BND document to create a customer master record with the country key KP. Use the following entries (step 4) and refer to master data script BNE document to create a supplier master record with the same ID as the customer. The business partner is only for Decision Table for Blocklisting, including inbound and outbound process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Creating Customer Master Data - General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: External alpha-numeric numberingTitle: 0003 -CompanyName: Test customer for legal controlPostal Code/City: 999093/ PyongyangCtry/Reg.: KP (North Korea)Language: English | The KP customer XXXX with general data is created. |  |
| 2 | Create Customer Master Data - Company Code Data | Make the following entries:Company Code: 3310Reconciliation Account: 12120000 (Trade Receivables Foreign)Terms of Payment: 0001 (Payable immediately Due net) | The KP customer XXXX with company code level data is created. |  |
| 3 | Create Customer Master Data - Sales Area Data | Make the following entries:Sales Org.: 3310Distr. Channel:10Division: 00Currency: AEDDelivery Priority: 02 NormalDelivering Plant: 3310 AE PlantShipping Conditions: 01 StandardIncoterms: <EXW/Location of seller>Payment Terms: 0001 (Payable immediately Due net)AcctAssgGr: <Account assignment group> 02 Foreign RevenuesTax Classification: 0 Tax ExemptPartner Function:SP - Sold-To PartyBP - Bill-To PartyPY - PayerSH - Ship-To Party | KP customer XXXX with sales area level data is created. |  |
| 4 | Create Supplier Master Data - Purchasing Organization Data | Make the following entries:Purchase Org.: 3310Currency: AEDPartner Function:VN - SupplierPI - Invoicing PartyGS - Goods SupplierNote In case PRA functionality is activated in your system, please enter the PRA related attributes ( "Additional Data, PRA General") for business partner's supplier role, for example: Res. Country/Reg.: US, Region: AA, Entity Type: 06, Payment Type: C, Frequency: 1. | KP supplier XXXX with purchasing organization data is created. |  |

##### Create Testing Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you can create a supplier for DE for legal control testing. Use the following entries and refer to master data script BNE Create Supplier Master - MDS to create a supplier master record with the country/region key DE.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Creating Supplier- General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: External alpha-numeric numberingTitle: 0003-CompanyName: Test business partner for legal controlPostal Code/City: 69190/ WalldorfCountry: DERegion: BWLanguage: English | The Supplier XXXX with general data is created. |  |
| 2 | Create Supplier - Company Code Data | Make the following entries:Company Code: 3310Reconciliation Account: 21200000 (Payables Foreign)Terms of Payment: 0001 (Payable immediately Due net) | The Supplier XXXX with company code level data is created. |  |
| 3 | Create Supplier - Purchasing | Make the following entries:Purch. Organization: 3310Currency: AEDPartner Function:VN - SupplierPI - Invoicing PartyGS - Goods SupplierNote In case PRA functionality is activated in your system, please enter the PRA related attributes ( "Additional Data, PRA General") for business partner's supplier role, for example: Res. Country/Reg.: US, Region: AA, Entity Type: 06, Payment Type: C, Frequency: 1. | The Supplier XXXX with purchasing level data is created. |  |

#### Maintain Condition Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To ensure Sales Orders with international business partner be created successfully, corresponding Condition Record needs to be maintained.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Pricing Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the Fiori App | Open the Set Material Prices - Sales (VK12) app. | The Change Condition Records view is displayed. |  |
| 3 | Choose Condition Type | In the Change Condition Records view, maintain below information:Condition Type: PPR0Then choose Enter, and in the Key Combination window, select Material with release status and choose Choose.Condition Type : <input country-specific condition type>, for example, TTX1 for DEThen choose Enter, and in the Key Combination window, select Export Taxes and choose Choose. | If PPR0 is missing when creating sales order, please maintain condition type PPR0.If TTX1 is missing when creating sales order, please maintain condition type TTX1, or other condition type according to your country-specific requirement. |  |
| 4 | Maintain Condition Record: Change Price | In the Change Price(PPR0): Selection view, maintain below information:Sales Organization: 3310Distribution Channel: 10Material: TG0012Then choose Execute. |  |  |
| 5 | Maintain Condition Record: Change Pricing Condition | In the Change Pricing Condition (PPR0): Overview view, maintain a new entry with below information:Material: TG0012Amount: 5Valid From: For example, current dateValid To: 12/31/9999Choose Save to save the change. |  |  |
| 6 | Maintain Condition Record: Change Output Tax | On the next screen, maintain the information below:Departure Ctry/Reg.: AEThen choose Execute. |  |  |
| 7 | Maintain Condition Record: Change Output Tax | In the next view, maintain a new entry with information below:Dest. Country/Region: KPTaxClass1-Cust.: 0Tax Class. Material: 1Valid From: for example, <current date>Valid To: 12/31/9999Tax Code: <Please select appropriate tax code, for example, A0 for DE>Choose Save.Note The above Countries are only used as examples to showcase how to maintain condition records. Please adjust accordingly against your business requirement. | Records are maintained. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Basic Process of Legal Control

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Manage Control Classes |  |  |  |
| [Manage Control Classes](#unique_13) [page ] 35 | Trade Classification Specialist | Manage Control Classes (F2518) | Control Class is created / changed. |
| [Manage Control Classes from Data Provider (Optional)](#unique_14) [page ] 36 |  |  |  |
| [Schedule Control Classes Content Request to Data Provider (Background Job)](#unique_15) [page ] 36 | Administrator - International Trade | Schedule Content Request to Data Provider - Control Classes (F3568) | Jobs is created. |
| [Manage Control Classes Content from Data Provider](#unique_16) [page ] 37 | Administrator - International Trade | Manage Content from Data Provider - Control Classes (F3582) | The control class of Numbering scheme content is active. |
| [Manage Control Groupings (Optional)](#unique_17) [page ] 38 | Trade Classification Specialist | Manage Control Groupings (F2515) | Control Grouping is created / changed. |
| Classify Products - Legal Control |  |  |  |
| [Classify Products - Legal Control](#unique_18) [page ] 39 | Trade Classification Specialist | Classify Products - Legal Control (F2390) | Control Class is assigned to products. |
| [Reclassify Products - Legal Control (Optional)](#unique_19) [page ] 40 | Trade Classification Specialist | Reclassify Products - Legal Control (F2391) | Control Class is changed for products. |
| [Display Classified Products](#unique_20) [page ] 41 | Trade Compliance Specialist | Display Classified Products - International Trade (F3789) | Classification data is displayed. |
| Inbound Process |  |  |  |
| [Manage Purchase Documents](#unique_21) [page ] 43 |  |  |  |
| [Manage Purchase Orders](#unique_22) [page ] 43 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase order is created. |
| [Manage Stock Transfer Orders (Optional)](#unique_23) [page ] 44 | Purchaser | Create Purchase Order - Advanced (ME21N) | Stock Transfer Order is created. |
| [Manage Purchase Scheduling Agreements (Optional)](#unique_24) [page ] 45 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Purchase scheduling agreement is created. |
| [Manage Purchase Requisitions (Optional)](#unique_25) [page ] 45 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisition is created. |
| [Manage Licenses - Trade Compliance](#unique_26) [page ] 45 | Trade Compliance Specialist | Manage Licenses (F2545) | Inbound licenses are created/changed. |
| [Manage Documents - Trade Compliance](#unique_27) [page ] 46 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Legal Control blocks on purchaser orders are resolved. |
| [Check Purchase Order Status](#unique_28) [page ] 48 | Purchaser | Manage Purchase Orders (F0842A) | No error message against legal control. |
| [Manage Inbound Deliveries](#unique_29) [page ] 48 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery is created |
| Outbound Process |  |  |  |
| [Manage Sales Documents](#unique_30) [page ] 49 |  |  |  |
| [Manage Sales Orders](#unique_31) [page ] 50 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created. |
| [Manage Sales Orders Without Charge (Optional)](#unique_32) [page ] 51 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order without charge is created. |
| [Manage Sales Scheduling Agreements (Optional)](#unique_33) [page ] 51 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Sales scheduling agreement is created. |
| [Manage Licenses - Trade Compliance](#unique_34) [page ] 51 | Trade Compliance Specialist | Manage Licenses (F2545) | Outbound licenses are created/changed. |
| [Manage Documents - Trade Compliance](#unique_35) [page ] 53 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Legal Control blocks on sales orders are resolved. |
| [Manage Outbound Deliveries](#unique_36) [page ] 54 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Schedule Recheck Documents Background Job for Trade Compliance (Optional)](#unique_37) [page ] 55 | Trade Compliance Specialist | Schedule Recheck Documents - Trade Compliance (F4285) |  |
| [Display License Assignments](#unique_38) [page ] 56 | Trade Compliance Specialist | Display License Assignments - Trade Compliance (F4047) | You can view the license assignments for documents. |
| [Analyze and Resolve Blocked Documents](#unique_39) [page ] 57 | Trade Compliance Specialist | Analyze and Resolve Blocked Documents - Trade Compliance (F5445) |  |

Table 3: Manage Legal Control Rule for Allowlisting

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Control Classes](#unique_40) [page ] 58 | Trade Classification Specialist | Manage Control Classes (F2518) | Control class is created. |
| [Classify Products - Legal Control](#unique_41) [page ] 59 | Trade Classification Specialist | Classify Products - Legal Control (F2390) | Control class is assigned. |
| [Maintain Decision Table for Allowlisting](#unique_42) [page ] 60 | Trade Compliance Specialist | Manage Legal Control Rules (SLL_WD_LCC_BRF_RULES_MAINTAIN (SLL_WD_LCC_BRF_RULES_MAINTAIN)) | Objects are saved and activated. |
| Inbound Process |  |  |  |
| [Manage Purchase Documents](#unique_43) [page ] 61 |  |  |  |
| [Manage Purchase Orders](#unique_44) [page ] 62 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase order is created. |
| [Manage Stock Transfer Orders (Optional)](#unique_45) [page ] 63 | Purchaser | Create Purchase Order - Advanced (ME21N) | Stock Transfer Order is created. |
| [Manage Purchase Scheduling Agreements (Optional)](#unique_46) [page ] 63 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Purchase scheduling agreement is created. |
| [Manage Purchase Requisitions (Optional)](#unique_47) [page ] 63 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisition is created. |
| [Manage Documents - Trade Compliance](#unique_48) [page ] 63 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Purchase orders have been released by system check. |
| Outbound Process |  |  |  |
| [Manage Sales Documents](#unique_49) [page ] 64 |  |  |  |
| [Manage Sales Orders](#unique_50) [page ] 65 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created. |
| [Manage Sales Orders Without Charge (Optional)](#unique_51) [page ] 66 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order without charge is created. |
| [Manage Sales Scheduling Agreements (Optional)](#unique_52) [page ] 66 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Sales scheduling agreement is created. |
| [Manage Documents - Trade Compliance](#unique_53) [page ] 66 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Sales order have been released by system check. |

Table 4: Manage Legal Control Rule for Blocklisting

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Decision Table for Blocklisting](#unique_54) [page ] 67 | Trade Compliance Specialist | Manage Legal Control Rules (SLL_WD_LCC_BRF_RULES_MAINTAIN (SLL_WD_LCC_BRF_RULES_MAINTAIN)) | Objects are saved and activated. |
| Inbound Process |  |  |  |
| [Manage Purchase Documents](#unique_55) [page ] 68 |  |  |  |
| [Manage Purchase Orders](#unique_56) [page ] 69 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase order is created. |
| [Manage Purchase Scheduling Agreements (Optional)](#unique_57) [page ] 70 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Purchase scheduling agreement is created. |
| [Manage Purchase Requisitions (Optional)](#unique_58) [page ] 70 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisition is created. |
| [Manage Documents - Trade Compliance](#unique_59) [page ] 71 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Purchase orders have been confirmed block by system check. |
| Outbound Process |  |  |  |
| [Manage Sales Documents](#unique_60) [page ] 71 |  |  |  |
| [Manage Sales Orders](#unique_61) [page ] 72 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created. |
| [Manage Sales Orders Without Charge (Optional)](#unique_62) [page ] 73 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order without charge is created. |
| [Manage Sales Scheduling Agreements (Optional)](#unique_63) [page ] 73 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Sales scheduling agreement is created. |
| [Manage Documents - Trade Compliance](#unique_64) [page ] 73 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Sales order have been confirmed block by system check. |

Table 5: Manage Legal Control Rule for License Types based on Control Class and Country

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain License Types based on Control Class and Country](#unique_65) [page ] 74 | Trade Compliance Specialist | Manage Legal Control Rules (SLL_WD_LCC_BRF_RULES_MAINTAIN (SLL_WD_LCC_BRF_RULES_MAINTAIN)) | Objects are saved and activated. |
| Inbound Process |  |  |  |
| [Manage Purchase Documents](#unique_66) [page ] 76 |  |  |  |
| [Manage Purchase Orders](#unique_67) [page ] 76 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase order is created. |
| [Manage Stock Transfer Orders (Optional)](#unique_68) [page ] 77 | Purchaser | Create Purchase Order - Advanced (ME21N) | Stock Transfer Order is created. |
| [Manage Purchase Scheduling Agreements (Optional)](#unique_69) [page ] 78 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Purchase scheduling agreement is created. |
| [Manage Purchase Requisitions (Optional)](#unique_70) [page ] 78 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisition is created. |
| [Manage Documents - Trade Compliance](#unique_71) [page ] 78 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Purchase orders have been released by system check; the licenses have been assigned to respective purchase orders. |
| Outbound Process |  |  |  |
| [Manage Sales Documents](#unique_72) [page ] 79 |  |  |  |
| [Manage Sales Orders](#unique_73) [page ] 79 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created. |
| [Manage Sales Orders Without Charge (Optional)](#unique_74) [page ] 80 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order without charge is created. |
| [Manage Sales Scheduling Agreements (Optional)](#unique_75) [page ] 81 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Sales scheduling agreement is created. |
| [Manage Documents - Trade Compliance](#unique_76) [page ] 81 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Sales order have been released by system check; the licenses have been assigned to respective sales orders. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item. The test procedures are include import process and export process to check documents if them are in violation of the trade policies. Option 1 is the export process to check the trade compliance. Option 2 is the import process to check the trade compliance.

### Basic Process of Legal Control

#### Manage Control Classes

##### Manage Control Classes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can define a control class, which will be assigned to products for legal control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Control Classes (F2518). |  |  |
| 3 | Control Class Worklist | No. Scheme Content: QAL02Choose GO. | Control Class related to QAL02 displays. |  |
| 4 | Create Control Class | Choose  .Enter Control Class: CC01_TESTOfficial Description: <description>Valid From: for example, 07/25/2017Valid To: for example, 12/30/9999Choose Save.Click ADD to create control class 3A002 and 3A004. | Control Class CC01_TEST is created. |  |

##### Manage Control Classes from Data Provider (Optional)

If the Control Classes will be provided by Data Provider, below steps should be maintained.

|  |
| --- |
| Note Additional Manual Configuration:To manage control classes from a Data Provider, you need to complete the additional and mandatory configuration steps that are described in the Set-up Instructions for this scope item. These configuration steps are specific for your implementation. These include mandatory settings that are not delivered by SAP and must be created by you. For more information, see the Set-up Instructions for this scope item in the SAP Signavio Process Navigator. |

|  |
| --- |
| Note Additional Information:To manage control classes from a Data Provider, you need to have a commercial contract with Data Provider. |

###### Schedule Control Classes Content Request to Data Provider (Background Job)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job which can trigger a content request automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator - International Trade. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Content Request to Data Provider - Control Classes (F3568). |  |  |
| 3 | Schedule Control Classes Content Request to Data Provider by Background Job | In the overview view, choose Create.In the New Job view, make the following entries:Job Template: Schedule Content Request to Data Provider – Control ClassesChoose Step 2.Start Immediately: <Select>Choose Step 3.No. Scheme Content: QAL02_DPRequest Initial Version: <Select>Choose Schedule. | Job is scheduled and shown in the list. |  |

###### Manage Control Classes Content from Data Provider

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor the application log.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Trade Classification Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Content from Data Provider - Control Classes (F3582). |  |  |
| 3 | Active the Control Classes | In the overview view, make the following entries and choose Go:No. Scheme Content: QAL02_DPData Provider ID: _AChoose the No. Scheme Content and click Active.The Data Provider ID should be unified with the communication arrangement in the setup Instruction. | The control classes of numbering scheme content is active. |  |
| 4 | View Application Log (Optional) | In the Manage Content from Data Provider - Control Classes view, if the content consistency is marked failed, choose the content consistency and view the application log.Choose the log and check the information description. |  |  |

##### Manage Control Groupings (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can define a control group, which will be assigned to products for legal control when Control Grouping Activated is checked for legal regulation ITR01.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Classification Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Control Groupings (F2515). | The Control Groupings view appears. |  |
| 3 | Control Grouping Worklist | Legal Regulation: ITR01Choose GO. | Control Grouping related to ITR01 will be displayed. |  |
| 4 | Create Control Grouping | Choose Add.Enter Control Groping Name: CG01_TESTDescription: Control grouping test for ITR01Choose Save. | Control Grouping CG01_TEST is created. |  |

#### Classify Products - Legal Control

##### Classify Products - Legal Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can assign the control class, which is maintained in a previous step to the product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Classify Products - Legal Control (F2390). | The Classify Products - Legal Control view displays. |  |
| 3 | Classify Product Worklist | Legal Regulation: ITR01Valid On: for example, 25/07/2017Product : TG12Choose GO.Note You can select your own product in the worklist which has not been classified. | Product: TG12 displays in the worklist. |  |
| 4 | Classify Product | Select Product TG12 and choose Classify.Check Control Relevant flag.Classification Period: for example, 25/07/2017 to 30/12/9999Control Class: CC01_TESTRemark: <your remark>Choose Save.Repeat the process to classify product TG0011 with control class 3A004.Note You can also assign Control Grouping CG01_TEST when Control Grouping Activated is checked for legal regulation ITR01. | Control Class CC01_TEST is assigned to Product TG12. |  |

##### Reclassify Products - Legal Control (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can reassign the control class which is maintained in a previous step to the product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Classification Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reclassify Products - Legal Control (F2391). | The Reclassify Products - Legal Control view appears. |  |
| 3 | Create New Control Class | Please refer to step [Manage Control Classes](#unique_13) [page ] 35 to create new control class CC02_TEST. | Control Class CC02_TEST is created. |  |
| 4 | Reclassify Product Worklist | Legal Regulation: ITR01Valid On: for example, 25/07/2017Product: TG12Choose GO． | Product: TG12 displays in the worklist. |  |
| 5 | Reclassify Product | Select Product TG12 and choose Reclassify.Check Control Relevant flag.Classification Period: 25/07/2017 to 30/12/9999Control Class: CC02_TESTRemark: <your remark>Choose SAVE. | Control Class CC02_TEST is assigned to Product TG12. |  |

##### Display Classified Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, you can display all the international trade classification data including commodity code, control class, customs tariff number, and Intrastat services codes for the products you classified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Classified Products - International Trade (F3789). |  |  |
| 3 | Enter Filters | In the Display Classified Products view, make the following entries and choose Go:Plant: <Enter the plant, for example, 3310> |  |  |
| 4 | Display the List for Classified Products | In the Display Classified Products view, choose the product. |  |  |
| 5 | Display Classification Data for Product | In the Classification Overview view, you can find different tabs for the classification data including Commodity Codes, Customs Tariff Numbers, Legal Control and Intrastat Service Codes.Click the Numbering Scheme you maintained for the product, for example, Legal Regulation for International Trade (ITR01). | The Classification for Legal Control displays. |  |
| 6 | Display the Classification History for Control Class | In the Legal Control view, you can find the classification history of control classes for the product with validation period.In the Change Documents tab, you can see the details of changed data including old and new values, created by, created on, and change types for the fields belonging to classification.You can follow the same steps to display other classification data like customs tariff numbers for the product. | The classification history of control classes for the product with validation period displays. |  |

#### Inbound Process

##### Manage Purchase Documents

In this section, you can manage purchase documents which are supported by legal control.

Manage purchase orders is taken as an example to show how legal control is embedded in the inbound process.

To manage other purchase documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before managing purchase documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating purchase documents, choose foreign suppliers which are created in the preliminary step.

###### Manage Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create a purchase order which triggers the Legal Control inbound license check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order - Advanced (ME21N) view displays. |  |
| 3 | Create Advanced Purchase Order | Make the following entries:Order type: NB Standard POSupplier: Above created US supplier XXXXIn Header section, on the Org. Data tab:Purchasing Org.: 3310Purchasing Group:001Company Code: 3310In Items section,Material: TG12Plant: 3310Quantity: <Enter the quantity>Net Price: <Enter the quantity> |  |  |
| 4 | Save Purchase Order | Choose Save. | International Purchase Order is created. |  |
| 5 | Check Compliance Status for the Purchase Order | Open Display Purchase Order - Advanced (ME23N).Choose the Other Purchase Order button, make the following entries, then choose Other Document:Purchase Order: <XXXX> Purchase order number XXXX was created in previous stepNavigate to the Compliance tab for this item.Check the Legal Control Status: BlockedCheck the item status: item is blocked. | The legal control status is blocked. Item is blocked. |  |

###### Manage Stock Transfer Orders (Optional)

Stock transfer order is a special type of purchase order which transfers materials between two plants. We support legal control checks of stock transfer orders for both the receiving plant’s inbound check and the supplying plant’s outbound check.

To create a stock transfer order, refer to the test step Optional: Create Stock Transport Order in the test script of the scope item Stock Transfer with Delivery (BME). The test script for BME tests the process between two plants in the same country. Thus, before creating the Stock Transfer Order, please go to the configuration step: Control Settings for Legal Regulations for Legal Control, select Check Domestic Processes. Please also maintain the License with partner country DE in step Manage License -Trade Compliance.

###### Manage Purchase Scheduling Agreements (Optional)

To create a purchase scheduling agreement, refer to the Create Scheduling Agreement process step in the test script of the scope item Scheduling Agreements in Procurement (BMR).

Legal control check on purchase scheduling agreements is supported only when creating scheduling agreements with Manage Purchase Scheduling Agreements (F2179), and you need to make sure to add the schedule lines into scheduling agreements before saving the preparation status.

###### Manage Purchase Requisitions (Optional)

To create a purchase requisition, refer to the Create Purchase Requisition process step in the test script of the scope item Purchase Contract (BMD).

When creating purchase requisitions, you need to assign either Fixed Vendor or Desired Supplier in the Source of Supply tab to activate legal control check on purchase requisitions. We also support outbound check for purchase requisition scenario when you assigned Supplying (issuing) plant in case of stock transport order.

##### Manage Licenses - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can maintain inbound license for trade compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Trade Compliance Specialist. | The SAP fiorilaunchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Licenses (F2545). | The Manage License screen is displayed. |  |
| 3 | Licenses Worklist | Make the following entries and choose Go:Legal Regulation: ITR01 | Licenses with type LTY01 and ITR02 are displayed in the worklist. |  |
| 4 | Create License | Choose Create and make the following entries:License Owner: 3310Legal Regulation: ITR01License Type: LTY01Choose OK. |  |  |
| 5 | Maintain General Information | In the overview view, make the following entries:Official License No.: <Import License for 1W8>Valid From: for example, 25/07/2017Valid To: for example, 25/07/2018 | General information is maintained. |  |
| 6 | Maintain Control Classes | Choose Create and make the following entry:Control Class: CC01_TEST | Control class is assigned to license. |  |
| 7 | Maintain Partner Countries | Choose Create and make the following entry:Partner's Country/Region: DE | Partner Country/Region is assigned to license. |  |
| 8 | Save License | Choose Save. | License XXXXXXXX is created. |  |
| 9 | Activate License | Choose Set to Active. | License XXXXXXXX status is License Active (B). |  |

|  |
| --- |
| Note You can also click the Related Apps button to navigate from License Master to app Display License Assignments. Additionally, a daily background job is scheduled to auto set licenses with an expired Valid-To date to status License Expired (C). |

##### Manage Documents - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can recheck and resolve blocked purchase documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance view displays. |  |
| 3 | Document Worklist | Document Number: <XXXX>Choose GO.Note Purchase Order number XXXX was created in the previous procedure. | Purchase document XXXX displays with blocking reason. |  |
| 4 | Release Purchase Document | Select Document Number: <XXXX>Go to the Legal Control Status screen by choosing the purchase order.Input the License number and choose Save. | Purchase Order XXXX is released. |  |

|  |
| --- |
| Note From 2111 release, you can search directly for Trade Compliance documents via the Enterprise search box on the top right of the screen via selecting Trade Compliance Documents in the search criteria.In the result list you can either jump into the app Manage Documents – Trade Compliance, or display the details of the trade compliance document via the document number. |

##### Check Purchase Order Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can check the status of purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders (Version 2) view displays. |  |
| 3 | Search Purchase Order | Mark the following entries and choose GO:Purchase Order: <XXXX>Note Purchase order number XXXX was created in previous step |  |  |
| 4 | Check Purchase Order Messages | No messages regarding legal control blocked could be displayed. |  |  |

##### Manage Inbound Deliveries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an inbound delivery to trigger legal control check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Inbound Delivery (VL31N). | The Create Inbound Delivery view displays. |  |
| 3 | Create Inbound Delivery | Mark the following entries and choose Enter:Supplier: <Enter your foreign supplier>Purchase Order: <Created purchase document number>Delivery Date: <Delivery selection date>Note Purchase order number XXXX was created in previous step. |  |  |
| 4 | Save | Choose Save. | Creation of a delivery is triggered. |  |
| 5 | Check legal Control Status | Please refer to step [Manage Documents - Trade Compliance](#unique_27) [page ] 46 to manage the blocking status for the created delivery. | The legal control is checked for the created delivery. |  |

#### Outbound Process

##### Manage Sales Documents

In this section, you can manage sales documents which are supported by legal control.

Manage sales orders is taken as an example to show how legal control is embedded in the outbound process.

To manage other sales documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before creating sales documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating sales documents, choose foreign customers which are created in the preliminary step.

###### Manage Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create a sales order which triggers the Legal Control outbound license check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Sales Orders - VA01 (VA01). | The Create Standard Order: Overview view appears. |  |
| 3 | Create Sales Order | Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. |  |  |
| 4 | Enter Sales Order Item Data and Save | Sold-To Party: 3310<0050>Ship-To Party:3310<0050>Cust. Reference: Legal control testingMaterial: TG0011Order Quantity: 10Plant: 3310Choose Save. | Standard Order XXXX has been saved.You can also use Display Sales Orders - VA03 (VA03) app to check the international trade status in every item's Status tab. |  |

|  |
| --- |
| Note If the sales order requires approval, follow the Process Sales Order Approval (Optional) steps described in the Sell from Stock (BD9) test script. This scope item also supports a legal control check for sales scheduling agreements. |

###### Manage Sales Orders Without Charge (Optional)

To create a sales order without charge, refer to the Create Sales Order process step in the test script of the scope item Free of Charge Delivery (BDA).

###### Manage Sales Scheduling Agreements (Optional)

To create a sales scheduling agreement, refer to the Create Sales Scheduling Agree-ment process step in the test script of the scope item Sales Scheduling Agreements (3NR).

The legal control check is triggered only when the delivery schedule is maintained in the created sales scheduling agreement.

##### Manage Licenses - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can maintain outbound license for trade compliance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Trade Compliance Specialist. | The SAP fiorilaunchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Licenses (F2545). | The Manage License screen is displayed. |  |
| 3 | Licenses Worklist | Make the following entries and choose Go:Legal Regulation: ITR01 | Licenses with type LTY01 and ITR02 are displayed in the worklist. |  |
| 4 | Create License | Choose Create and make the following entries:License Owner: 3310Legal Regulation: ITR01License Type: LTY01Choose OK. |  |  |
| 5 | Maintain General Information | In the overview view, make the following entries:Official License No.: <Export License for 1W8>Valid From: for example, 25/07/2017Valid To: for example, 25/07/2018 | General information is maintained. |  |
| 6 | Maintain Control Classes | Choose Create and make the following entry:Control Class: CC01_TEST | Control class is assigned to license. |  |
| 7 | Maintain Partner Countries | Choose Create and make the following entry:Partner's Country/Region: DE | Destination Country/Region is assigned to license. |  |
| 8 | Save License | Choose Save. | License XXXXXXXX is created. |  |
| 9 | Activate License | Choose Set to Active. | License XXXXXXXX status is License Active (B). |  |

|  |
| --- |
| Note You can also click the Related Apps button to navigate from License Master to app Display License Assignments. Additionally, a daily background job is scheduled to auto set licenses with an expired Valid-To date to status License Expired (C). |

##### Manage Documents - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can recheck and resolve blocked sales documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance view displays. |  |
| 3 | Sales Document Worklist | Document Number: <XXXX>Choose GO.Note Sales Order number XXXX was created in the previous procedure. | Sales document XXXX displays with blocking reason. |  |
| 4 | Release Sales Document | Select Document Number: <XXXX>Go to the Legal Control Status screen by choosing the sales order.Input the License number and choose Save. | Sales Order XXXX is released. |  |

|  |
| --- |
| Note From 2111 release, you can search directly for Trade Compliance documents via the Enterprise search box on the top right of the screen via selecting Trade Compliance Documents in the search criteria.In the result list you can either jump into the app Manage Documents – Trade Compliance, or display the details of the trade compliance document via the document number. |

##### Manage Outbound Deliveries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create outbound deliveries to trigger legal control outbound licenses check.

|  |
| --- |
| Note Due to the configuration of Switch Off Subsequent Functions in Configuration Step, the related sales order should be released for legal control in the previous step. Otherwise, you are not allowed to create the delivery and would get the error message Schedule Line is blocked by Legal Control (International Trade). |

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries From Sales Orders view displays. |  |
| 3 | Search Sales Order | Mark the following entries and choose GO:Shipping Point: 1010Planned Creation Date: <Delivery selection date>SD Document: <XXXX> | Sales order number XXXX was created in [Manage Sales Orders](#unique_31) [page ] 50. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Legal Control Status | Please refer to previous steps [Manage Documents - Trade Compliance](#unique_35) [page ] 53 to check the legal control status. | Delivery is released by legal control. |  |

#### Schedule Recheck Documents Background Job for Trade Compliance (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job that can schedule job requests automatically for mass recheck of the trade compliance documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Trade Compliance Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Schedule Recheck Documents - Trade Compliance (F4285). | The overview screen appears. |  |
| 3 | Schedule Mass Recheck Documents by Background Job | Choose Create. In the New Job screen, make the following entries:Job Template: Schedule Recheck of Trade Compliance DocumentsChoose Step 2.Start Immediately: <Select the checkbox>Choose Step 3.Document Date: <Select a date range>Document Category: <Sales order, for example>Company Code: 3310Choose Schedule. | The job is scheduled and shown in the list. You can click on i in the Log column to see the log details. |  |

#### Display License Assignments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can view the license assignments for document items, such as from purchase orders, sales orders, and outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display License Assignments - Trade Compliance (F4047). | The Display License Assignments screen appears. |  |
| 3 | Search Licenses | Make the following entries and choose Go:License Owner: <enter the company code>, for example 1010 | The licenses with assigned documents appear. |  |
| 4 | Display Assigned Documents to License | You can select a license item to see the document assignments and details for that license. | The License with Documents Assigned view displays. |  |
| 5 | Export Document Assignments | You can see the general information for this license in the header level. You can also see all the assigned document items in the table. To download the document assignments for this license, choose Export button. | The document assignments are exported to Excel. |  |

#### Analyze and Resolve Blocked Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this process step, you can analyze blocked trade compliance documents, which, for example, may have missing classifications, are blocked by embargo, or are missing licenses. You can make use of analytical features such as the visual filter bar and chart view result list. Default visual filters are the number of blocked documents by legal regulation, number of blocked documents by company code and number of blocked documents by document category. To use your own selection criteria, you can switch to the Compact Filter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log onto the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Analyze and Resolve Blocked Documents - Trade Compliance (F5445). | The Analyze and Resolve Documents screen appears. |  |
| 3 | Analyze and Resolve Blocked Documents - Trade Compliance | On the Adapt Filters Basic screen, make the following entries and choose OK.Display Currency: Enter the currency, for example EURExchange Rate Type: <Enter the exchange rate type, for example M>Use the visual filters to filter blocked documents by Legal Regulation, Company Code and Document Category.Select the arrow on the right of the desired document from the Items list. On the Details of Blocks screen, you can add missing license, confirm Embargo block, or release Embargo block.Note You can also use compact filters instead of visual filters by choosing the icon on the top right of the screen. | Standard screen with report details displays. |  |

### Manage Legal Control Rule for Allowlisting

#### Manage Control Classes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you can define control class, which will be assigned to products for legal control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Control Classes (F2518). | The Control Class view displays. |  |
| 3 | Control Class Worklist | In the filter bar, make the following entries:No. Scheme Content: QAL02Choose Go. | Control Class view related to QAL02 displays. |  |
| 4 | Create Control Class | Choose Add and make the following entries:Control Class Name: CC03_TESTOfficial Description: <description>Valid From: For example, 25/07/2017Valid To: For example, 30/12/9999Choose Save. | Control Class CC03_TEST is created. |  |

#### Classify Products - Legal Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you can assign the control class, which is maintained in previous step to the product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Classification Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Classify Products - Legal Control (F2390). | The Classify Products - Legal Control view displays. |  |
| 3 | Control Class Worklist | Legal Regulation: ITR01Valid On: For example, 25/07/2017Product: TG0012Choose Go. | Product: TG0012 is displayed in the worklist.Note If the material of TG0012 is classified, reprocess Reclassify Products - Legal Control (Optional) section to reclassify TG0012 to Control Class CC03_TEST. |  |
| 4 | Create Control Class | Select Product TG0012 and choose Classify.Check the Control Relevant flag.Classification Period: for example, 25/07/2017 to 30/12/9999Control Class: CC03_TESTRemark: <your remark>Choose Save. | Control Class CC03_TEST is assigned to Product TG0012. |  |

#### Maintain Decision Table for Allowlisting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you can maintain the decision table for allowlisting with legal regulation, control class, partner country/region, and release status. It then manages the sales document to released status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Legal Control Rules (SLL_WD_LCC_BRF_RULES_MAINTAIN (SLL_WD_LCC_BRF_RULES_MAINTAIN)). | The Legal Control Rule Maintenance screen is displayed. |  |
| 3 | Legal Control Rules | In the filter bar, make the following entries:Show Rules for: Export Administration RegulationsRule: Allowlisting | The Table Contents screen is displayed. |  |
| 4 | Maintain Business Rules | Choose Edit.Choose +.Make the following entries:Legal Regulation: Direct value input : is equal to ITR01.Choose OK.Control Class: Direct value input : is equal to CC03_TEST.Choose OK.Partner Country/Region: Direct value input : is equal to US (the USA)Choose OK.Release Status: Direct value input: is equal to X (Yes).Choose OK.Choose Activate. | Objects saved and activated. |  |

#### Inbound Process

##### Manage Purchase Documents

In this section, you can manage purchase documents which are supported by legal control.

Manage purchase orders is taken as an example to show how legal control is embedded in the inbound process.

To manage other purchase documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before managing purchase documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating purchase documents, choose foreign suppliers which are created in the preliminary step.

###### Manage Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create a purchase order which triggers the Legal Control inbound license check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order - Advanced view displays. |  |
| 3 | Create Purchase Order - Advanced | Enter all of the necessary data,Order type: NB Standard POSupplier : Above created US supplier <XXXX>.In the Header section, on the Org. Data tab,Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310In the Items section,Material: TG0012Plant: 3310Quantity: <Enter the quantity>Net Price: <Enter the price> |  |  |
| 4 | Save Purchase Order | Choose Save. |  |  |

###### Manage Stock Transfer Orders (Optional)

Stock transfer order is a special type of purchase order which transfers materials between two plants. We support legal control checks of stock transfer orders for both the receiving plant’s inbound check and the supplying plant’s outbound check.

To create a stock transfer order, refer to the step Optional: Create Stock Transport Order in the test script of the scope item Stock Transfer with Delivery (BME). The test script for BME tests the process between two plants in the same country. Thus, before creating the Stock Transfer Order, please go to the configuration step: Control Settings for Legal Regulations for Legal Control, select Check Domestic Processes. Please also maintain the License for partner country DE in step Manage License -Trade Compliance.

###### Manage Purchase Scheduling Agreements (Optional)

To create a purchase scheduling agreement, refer to the Create Scheduling Agreement process step in the test script of the scope item Scheduling Agreements in Procurement (BMR).

Legal control check on purchase scheduling agreements is supported only when creating scheduling agreements with Manage Purchase Scheduling Agreements (F2179), and you need to make sure to add the schedule lines into scheduling agreements before saving the preparation status.

###### Manage Purchase Requisitions (Optional)

To create a purchase requisition, refer to the Create Purchase Requisition process step in the test script of the scope item Purchase Contract (BMD).

When creating purchase requisitions, you need to assign either Fixed Vendor or Desired Supplier in the Source of Supply tab to activate legal control check on purchase requisitions. We also support outbound check for purchase requisition scenario when you assigned Supplying (issuing) plant in case of stock transport order.

##### Manage Documents - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can check purchase order status if it is released by legal control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance view displays. |  |
| 3 | Document Worklist | On the overview screen, make the following entries:Document Number: <XXXX>Choose GO. | Purchase order document XXXX displays with Blocking Status Released. You can also check the reason for your information.Purchase Order number XXXX was created in the previous step: [Manage Purchase Orders](#unique_44) [page ] 62. |  |

#### Outbound Process

##### Manage Sales Documents

In this section, you can create sales documents which are supported by legal control.

Manage sales orders is taken as an example to show how legal control is embedded in the outbound process.

To manage other sales documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before creating sales documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating sales documents, choose foreign customers which are created in the preliminary step.

###### Manage Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create sales orders to trigger legal control outbound license check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Sales Orders - VA01 (VA01). | The Create Standard Order: Overview view appears. |  |
| 3 | Create Sales Order | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. |  |  |
| 4 | Enter Sales Order Item Data and Save | Sold-To Party: 33100050Ship-To Party:33100050Cust. Reference: Legal control testingMaterial: TG0012Order Quantity: 1Plant: 3310Choose Save.Note If the message Pricing/euro: Attention: Euro Customizing not maintained is displayed, please skip this message and choose Enter. | Standard Order XXXX has been saved. |  |

###### Manage Sales Orders Without Charge (Optional)

To create a sales order without charge, refer to the Create Sales Order process step in the test script of the scope item Free of Charge Delivery (BDA).

###### Manage Sales Scheduling Agreements (Optional)

To create a sales scheduling agreement, refer to the Create Sales Scheduling Agreement process step in the test script of the scope item Sales Scheduling Agreements (3NR).

The legal control check is triggered only when the delivery schedule is maintained in the created sales scheduling agreement.

##### Manage Documents - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can check sales order status if it is released by legal control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance view displays. |  |
| 3 | Document Worklist | On the overview screen, make the following entries:Document Number: <XXXX>Choose GO. | Sales document XXXX displays with Blocking Status Released. You can also check the reason for your information.Sales order number XXXX was created in the previous step [Manage Sales Orders](#unique_50) [page ] 65. |  |

### Manage Legal Control Rule for Blocklisting

#### Maintain Decision Table for Blocklisting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you can maintain the decision table for blocklisting with legal regulation, control class, partner country/region and release status. Then it will manage the sales documents and purchase orders to confirm blocked status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Legal Control Rules (SLL_WD_LCC_BRF_RULES_MAINTAIN (SLL_WD_LCC_BRF_RULES_MAINTAIN)). | The Legal Control Rule Maintenance view displays. |  |
| 3 | Legal Control Rules | In the filter bar, make the following entries:Show Rules for: Export Administration RegulationsRule: Blocklisting | The Table Contents view displays. |  |
| 4 | Maintain Business Rules | Choose Edit.Choose +.Make the following entries:Legal Regulation: Direct value input : is equal to ITR01.Choose OK.Control Class: Direct value input : is equal to CC01_TEST.Choose OK.Partner Country/Region: Direct value input: is equal to KP (North Korea).Choose OK.Blocking Status: Direct value input: is equal to X (Yes).Choose OK.Choose Activate. | Objects are saved and activated. | Note By adding a country's region into the business rule, you can manage regional embargos for specific regions of that country.Follow these steps to add a region to the business rule:In the Edit mode under Maintain Business Rules area, choose Table Settings.Under the Condition Columns of the opened Table Settings window, choose Insert Column and then choose From Context Data Objects.Scroll the Object table to select the Partner Region row, and then choose OK to make the column TCPRN (Partner Region) available in the decision table.In the Table Contents area, additionally maintain the values in the Partner Region column for the row entry. |

#### Inbound Process

##### Manage Purchase Documents

In this section, you can manage purchase documents which are supported by legal control.

Manage purchase orders is taken as an example to show how legal control is embedded in the inbound process.

To manage other purchase documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before managing purchase documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating purchase documents, choose foreign suppliers which are created in the preliminary step.

###### Manage Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create a purchase order which triggers the Legal Control inbound license check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order Advanced view displays. |  |
| 3 | Create Purchase Order - Advanced | Enter all of the necessary data,Order type: NB Standard POSupplier : Above created KP supplier <XXXX>.In the Header section, on the Org. Data tab,Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310In the Items section,Material: TG12Plant: 3310Quantity: <Enter the quantity>Net Price: <Enter the price> |  |  |
| 4 | Save Purchase Order | Choose Save. | International Purchase Order is saved. |  |
| 5 | Check Compliance Status for the Purchase Order | Open Display Purchase Order - Advanced (ME23N).Choose the Other Purchase Order button, make the following entries, then choose Other Document:Purchase Order: <XXXX> Purchase order number XXXX was created in previous stepNavigate to the Compliance tab for this item.Check the Legal Control Status: BlockedCheck the item status: item is blocked. | The legal control status is blocked. Item is blocked. |  |

###### Manage Purchase Scheduling Agreements (Optional)

To create a purchase scheduling agreement, refer to the Create Scheduling Agreement process step in the test script of the scope item Scheduling Agreements in Procurement (BMR).

Legal control check on purchase scheduling agreements is supported only when creating scheduling agreements with Manage Purchase Scheduling Agreements (F2179), and you need to make sure to add the schedule lines into scheduling agreements before saving the preparation status.

###### Manage Purchase Requisitions (Optional)

To create a purchase requisition, refer to the Create Purchase Requisition process step in the test script of the scope item Purchase Contract (BMD).

When creating purchase requisitions, you need to assign either Fixed Vendor or Desired Supplier in the Source of Supply tab to activate legal control check on purchase requisitions. We also support outbound check for purchase requisition scenario when you assigned Supplying (issuing) plant in case of stock transport order.

##### Manage Documents - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can check purchase order status if it is blocked by legal control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance view displays. |  |
| 3 | Document Worklist | On the overview screen, make the following entries:Document Number: <XXXX>Choose GO. | Purchase order document XXXX displays with Blocking Status Blocked. |  |

#### Outbound Process

##### Manage Sales Documents

In this section, you can create sales documents which are supported by legal control.

Manage sales orders is taken as an example to show how legal control is embedded in the outbound process.

To manage other sales documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before creating sales documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating sales documents, choose foreign customers which are created in the preliminary step.

###### Manage Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create sales orders to trigger legal control outbound license check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Sales Orders - VA01 (VA01). | The Create Standard Order: Overview view appears. |  |
| 3 | Create Sales Order | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. |  |  |
| 4 | Enter Sales Order Item Data and Save | Sold-To Party: <the KP customer XXXX created in the previous step>Ship-To Party: <the KP customer XXXX created in the previous step>Cust. Reference: Legal control testingMaterial: TG12Order Quantity: 1Plant: 3310Choose Save. | Standard Order XXXX is saved. |  |

###### Manage Sales Orders Without Charge (Optional)

To create a sales order without charge, refer to the Create Sales Order process step in the test script of the scope item Free of Charge Delivery (BDA).

###### Manage Sales Scheduling Agreements (Optional)

To create a sales scheduling agreement, refer to the Create Sales Scheduling Agreement process step in the test script of the scope item Sales Scheduling Agreements (3NR).

The legal control check is triggered only when the delivery schedule is maintained in the created sales scheduling agreement.

##### Manage Documents - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can check sales order status if it is blocked by legal control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance view displays. |  |
| 3 | Document Worklist | On the overview screen, make the following entries:Document Number: <XXXX>Choose GO.Note Sales order number XXXX is created in the previous step. | Sales document XXXX displays with Blocking Status Blocked. |  |

### Manage Legal Control Rule for License Types based on Control Class and Country

#### Maintain License Types based on Control Class and Country

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can maintain the rules of License Type based on Control Class and Country, and you release sales documents and purchase orders with an assigned license number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Legal Control Rules (SLL_WD_LCC_BRF_RULES_MAINTAIN (SLL_WD_LCC_BRF_RULES_MAINTAIN)). | The Legal Control Rule Maintenance view displays. |  |
| 3 | Legal Control Rules | In the filter bar, make the following entries:Show Rules for: Export Administration RegulationsRule: License Type based on Control Class and CountryNote You can also choose Rule of License Type based on Control Grouping and Country. | The Table Contents view displays. |  |
| 4 | Maintain Business Rules | Choose Edit.Choose +.Make the following entries with two lines:First line:Legal Regulation: Direct value input : is equal to ITR01.Choose OK.Control Class: Direct value input : is equal to CC01_TEST.Choose OK.Partner Country/Region: Direct value input: is equal to US (the USA).Choose OK.Sequence Number: Direct value input: Sequence Number: 1.Choose OK.License Type: Direct value input: License Type: LTY01.Choose OK.Choose Activate.Choose Yes in Confirm Activation.Second line:Legal Regulation: Direct value input : is equal to ITR01.Choose OK.Control Class: Direct value input : is equal to CC01_TEST.Choose OK.Partner Country/Region: Direct value input: is equal to US (the USA).Choose OK.Sequence Number: Direct value input: Sequence Number: 1.Choose OK.License Type: Direct value input: License Type: LTY02.Choose OK.Choose Activate.Choose Yes in Confirm Activation.Note If you choose the Rule of License Type based on Control Grouping and Country, the Control Grouping could be maintained as CG01_TEST in the previous step. | Objects are saved and activated. |  |

#### Inbound Process

##### Manage Purchase Documents

In this section, you can manage purchase documents which are supported by legal control.

Manage purchase orders is taken as an example to show how legal control is embedded in the inbound process.

To manage other purchase documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before managing purchase documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating purchase documents, choose foreign suppliers which are created in the preliminary step.

###### Manage Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create a purchase order which triggers Legal Control inbound licenses check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order - Advanced view displays. |  |
| 3 | Create Advanced Purchase Order | Make all the following entries:Order type: NB Standard POSupplier : Above created US supplier <XXXX>.In the Header section, on the Org. Data tab,Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310In the Items section,Material :TG12Plant: 3310Quantity: <Enter the quantity>Net Price: <Enter the price>. |  |  |
| 4 | Save Purchase Order | Choose Save. | The Purchase order is saved with number XXXXX. |  |

###### Manage Stock Transfer Orders (Optional)

Stock transfer order is a special type of purchase order which transfers materials between two plants. We support legal control checks of stock transfer orders for both the receiving plant’s inbound check and the supplying plant’s outbound check.

To create a stock transfer order, refer to the step Optional: Create Stock Transport Order in the test script of the scope item Stock Transfer with Delivery (BME). The test script for BME tests the process between two plants in the same country. Thus, before creating the Stock Transfer Order, please go to the configuration step: Control Settings for Legal Regulations for Legal Control, select Check Domestic Processes. Please also maintain the License type with partner country DE in step Maintain License Types based on Control Class and Country.

###### Manage Purchase Scheduling Agreements (Optional)

To create a purchase scheduling agreement, refer to the Create Scheduling Agreement process step in the test script of the scope item Scheduling Agreements in Procurement (BMR).

Legal control check on purchase scheduling agreements is supported only when creating scheduling agreements with Manage Purchase Scheduling Agreements (F2179), and you need to make sure to add the schedule lines into scheduling agreements before saving the preparation status.

###### Manage Purchase Requisitions (Optional)

To create a purchase requisition, refer to the Create Purchase Requisition process step in the test script of the scope item Purchase Contract (BMD).

When creating purchase requisitions, you need to assign either Fixed Vendor or Desired Supplier in the Source of Supply tab to activate legal control check on purchase requisitions. We also support outbound check for purchase requisition scenario when you assigned Supplying (issuing) plant in case of stock transport order.

##### Manage Documents - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can check purchase order status if it is released by license number assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance view displays. |  |
| 3 | Document Worklist | On the overview screen, make the following entries:Document Number: <XXXX>Choose GO.Note Purchase order number XXXX is created in previous step. | Purchase order XXXX is displayed with Blocking Status Released. |  |

#### Outbound Process

##### Manage Sales Documents

In this section, you can create sales documents which are supported by legal control.

Manage sales orders is taken as an example to show how legal control is embedded in the outbound process.

To manage other sales documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before creating sales documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating sales documents, choose foreign customers which are created in the preliminary step.

###### Manage Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can create sales orders to trigger legal control outbound license check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Sales Orders - VA01 (VA01). | The Create Standard Order: Overview view appears. |  |
| 3 | Create Sales Order | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. |  |  |
| 4 | Enter Sales Order Item Data and Save | Make the following entries:Sold-To Party: 3310<0050>Ship-To Party:3310<0050>Cust. Reference: Legal control testingMaterial: TG12Order Quantity: 1Plant: 3310Choose Save. | Standard Order XXXX is saved. |  |

###### Manage Sales Orders Without Charge (Optional)

To create a sales order without charge, refer to the Create Sales Order process step in the test script of the scope item Free of Charge Delivery (BDA).

###### Manage Sales Scheduling Agreements (Optional)

To create a sales scheduling agreement, refer to the Create Sales Scheduling Agreement process step in the test script of the scope item Sales Scheduling Agreements (3NR).

The legal control check is triggered only when the delivery schedule is maintained in the created sales scheduling agreement.

##### Manage Documents - Trade Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can check sales order status if it is released by license number assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance view displays. |  |
| 3 | Document Worklist | On the overview screen, make the following entries:Document Number: <XXXX>Choose GO.Note Sales order number XXXX is created in the previous step. | Sales document XXXX displays with Blocking Status Released. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/classification-for-customs-tariff-number-and-commodity-code-2u3-ae-868]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1W8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 131,439 chars in the whole document
