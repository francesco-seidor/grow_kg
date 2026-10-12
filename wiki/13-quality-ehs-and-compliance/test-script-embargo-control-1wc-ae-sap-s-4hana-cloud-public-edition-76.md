---
id: 13-quality-ehs-and-compliance/test-script-embargo-control-1wc-ae-sap-s-4hana-cloud-public-edition-76
title: "Test Script: Embargo Control (1WC_AE) - SAP S/4HANA Cloud Public Edition (1WC_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 1WC Embargo Control (AE, company code 3310): prerequisites, configuration, and outbound/inbound embargo block, release and analysis steps."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/embargo-control]
aliases: [1WC_S4CLD2608_BPD_EN_AE]
keywords: [Embargo Control, trade compliance, countries under embargo, outbound process, inbound process, embargo configuration, blocked documents, business partner test data, condition records, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WC_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-769
topic: 13-quality-ehs-and-compliance/embargo-control
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Embargo Control (1WC_AE) - SAP S/4HANA Cloud Public Edition (1WC_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WC_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Embargo Control** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Embargo Control (1WC_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847720)

[2 Prerequisites 4](#_Toc232847721)

[2.1 System Access 4](#_Toc232847722)

[2.2 Roles 4](#_Toc232847723)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847724)

[2.4 Preliminary Steps 7](#_Toc232847725)

[2.4.1 Configuration Activities with DEMO Data 7](#_Toc232847726)

[2.4.2 Configuration Activities Without DEMO Data 10](#_Toc232847727)

[2.4.3 Create Testing Business Partner for Iran (IR) 15](#_Toc232847728)

[2.4.4 Maintain Condition Record 17](#_Toc232847729)

[3 Overview Table 19](#_Toc232847730)

[4 Test Procedures 21](#_Toc232847731)

[4.1 Manage Countries Under Embargo 21](#_Toc232847732)

[4.2 Outbound Process 22](#_Toc232847733)

[4.2.1 Manage Sales Documents 22](#_Toc232847734)

[4.2.1.1 Manage Sales Quotations (Optional) 22](#_Toc232847735)

[4.2.1.2 Manage Sales Orders 22](#_Toc232847736)

[4.2.1.3 Manage Sales Orders Without Charge (Optional) 24](#_Toc232847737)

[4.2.1.4 Manage Sales Contracts (Optional) 24](#_Toc232847738)

[4.2.1.5 Manage Sales Scheduling Agreements (Optional) 24](#_Toc232847739)

[4.2.2 Manage Documents - Trade Compliance 24](#_Toc232847740)

[4.2.2.1 Option 1: Confirm Block 24](#_Toc232847741)

[4.2.2.2 Option 2: Release Block 25](#_Toc232847742)

[4.2.2.2.1 Release Block 25](#_Toc232847743)

[4.2.2.2.2 Create Outbound Delivery 26](#_Toc232847744)

[4.3 Inbound Process 27](#_Toc232847745)

[4.3.1 Manage Purchase Documents 27](#_Toc232847746)

[4.3.1.1 Manage Purchase Requisitions (Optional) 28](#_Toc232847747)

[4.3.1.2 Manage Purchase Orders 28](#_Toc232847748)

[4.3.1.3 Manage Purchase Contracts (Optional) 29](#_Toc232847749)

[4.3.1.4 Manage Purchase Scheduling Agreements (Optional) 29](#_Toc232847750)

[4.3.2 Manage Documents - Trade Compliance 29](#_Toc232847751)

[4.3.2.1 Option 1: Confirm Block 30](#_Toc232847752)

[4.3.2.2 Option 2: Release Block 30](#_Toc232847753)

[4.3.2.2.1 Release Block 31](#_Toc232847754)

[4.3.2.2.2 Create Inbound Delivery 31](#_Toc232847755)

[4.4 Schedule Recheck Documents Background Job for Trade Compliance (Optional) 32](#_Toc232847756)

[4.5 Analyze and Resolve Blocked Documents 33](#_Toc232847757)

## Purpose

Overview

This scope item supports international trade compliance by identifying embargoed countries or regions for automated checking of business transactions. Transactions blocked for embargo control may be reviewed and released as appropriate.

|  |
| --- |
| Caution If you are activating the Embargo Control (1WC) check in SAP S/4HANA Cloud Public Edition for international trade, it is not possible to activate the Compliance Management with SAP Global Trade Services (24J). Trade Compliance checks are to be done exclusively in either SAP S/4HANA Cloud Public Edition or Global Trade Services system. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |
| Trade Compliance Specialist | SAP_BR_TRD_CMPLNC_SPECIALIST | International Trade Compliance | SAP_BR_TRD_CMPLNC_SPECIALIST |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

If you have installed an SAP Best Practices Baseline package, you can use the following Baseline package scenario data for creating a Standard Sales Order and/or a Standard Purchasing Order. For creating other supported Business Documents which are entitled as 'Optional' in this document, please refer to the respective scenario data of their scope item.

Table 1: Table for Outbound Process

| Data for Creating a Standard Sales Order | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Order Type | OR | Standard Sales Order |  |
| Sales Organization | 3310 | Sales Organization for AE |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Sold-To Party | Please refer to [Create Testing Business Partner for Iran (IR)](#unique_6) [page ] 15 to create a customer XXXX for Iran (IR). | Foreign Customer XXXX (IR) | For Company Code 3310 (AE)International Sales |
| Ship-To Party | <The same with the Sold-To Party XXXX.> | Foreign Customer XXXX (IR) | For Company Code 3310 (AE)International Sales |
| Plant | 3310 | Plant 1 AE |  |
| Material | TG12 | Material Master Data TG12 is used. |  |

|  |
| --- |
| Note Business documents supported by embargo check for outbound process:Sales Quotations (Optional)Sales OrdersSales Orders Without Charge (Optional)Sales Contracts (Optional)Sales Scheduling Agreements (Optional) |

Table 2: Table for Inbound Process

| Data for Creating a Standard Purchasing Order | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Order Type | NB | Standard Purchase Order |  |
| Purchase Organization | 3310 | Purchase Organization for AE |  |
| Purchase Group | 001 | Group 001 |  |
| Vendor | Please refer to [Create Testing Business Partner for Iran (IR)](#unique_6) [page ] 15 to create a vendor XXXX for Iran (IR). | Foreign Vendor XXXX (IR) | For Company Code 3310 (AE)International Purchase |
| Plant | 3310 | Plant 1 AE |  |
| Material | TG0012 | Material Master Data TG0012 is used. |  |

|  |
| --- |
| Note Business documents supported by embargo check for inbound process:Purchase Requisitions (Optional)Purchase OrdersPurchase Contracts (Optional)Purchase Scheduling Agreements (Optional) |

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
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). Navigate to Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure Your Solution - General Settings for International Trade | In the Configure Your Solution: Realize Phase view, select Application Area Finance, Sub Application Area International Trade Management.Choose (>) Details button for the item General Settings for International Trade. | The Configure Your Solution - General Settings for International Trade screen appears. |  |
| 4 | Activate Sales Documents | Sales Document Type: ORTrade Compliance: <Flag should be checked>Choose Save. | Sales order type OR is activated for Trade Compliance. |  |
| 5 | Activate Delivery Documents | Delivery Type: LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type LF is activated for Trade Compliance. |  |
| 6 | Activate Checks for Purchasing Documents | Purchase Document Type: NBTrade Compliance: <Flag should be checked>Choose SAVE. | Purchase order type NB is activated for Trade Compliance. |  |
| 7 | Activate Checks for Company Codes | Company Code: 3310Activation Level: Company Code LevelEmbargo: <Flag should be checked>Choose Save. | Company Code 3310 is activated for embargo control. |  |
| 8 | Switch Off Subsequent Functions in SD Processes | Choose New EntriesTrade Regulation Area: 02 EmbargoStatus: B PendingSubsequent functions: 03 Outbound Delivery CreationCondition Active: <Flag should be checked>Chose SAVE. | Outbound delivery creation is not allowed since sales order is blocked by embargo control.Note We support the suppression of sales document outputs. | You can also choose C Blocked, which means only confirm blocked Sales orders are not allowed to creating follow-on documents. |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Configuration Activities | Go to the Business Processes Configuration app and search for the following activities mentioned in subsequent Test Step Name respectively.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The related configuration activities screen displays. |  |
| 3 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 4 | Activate Sales Documents | Sales Document Type: ORTrade Compliance: <Flag should be checked>Choose Save. | Sales order type OR is activated for Trade Compliance. |  |
| 5 | Activate Delivery Documents | Delivery Type: LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type LF is activated for Trade Compliance. |  |
| 6 | Activate Checks for Purchasing Documents | Purchase Document Type: NBTrade Compliance: <Flag should be checked>Choose SAVE. | Purchase order type NB is activated for Trade Compliance. |  |
| 7 | Activate Checks for Company Codes | Company Code: 3310Activation Level: Company Code LevelEmbargo: <Flag should be checked>Choose Save. | Company Code 3310 is activated for embargo control. |  |
| 8 | Switch Off Subsequent Functions in SD Processes | Choose New EntriesTrade Regulation Area: 02 EmbargoStatus: B PendingSubsequent functions: 03 Outbound Delivery CreationCondition Active: <Flag should be checked>Chose SAVE. | Outbound delivery creation is not allowed since sales order is blocked by embargo control.Note We support the suppression of sales document outputs. | You can also choose C Blocked, which means only confirm blocked Sales orders are not allowed to creating follow-on documents. |

#### Configuration Activities Without DEMO Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the scope item was activated without Demo Data, the system has no pre-delivered Demo Data configuration and you will need to maintain all the following configurations by SSCUIs before performing testing.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). | The Manage Your Solution screen appears. |  |
| 3 | Configure Your Solution - General Settings for International Trade | In the Configure Your Solution: Realize Phase screen, select Application Area Finance, Sub Application Area International Trade Management.Choose (>) Details button for the item General Settings for International Trade. | The Configure Your Solution - General Settings for International Trade screen appears. |  |
| 4 | Activate Sales Documents | Sales Document Type: ORTrade Compliance: <Flag should be checked>Choose Save. | Sales order type OR is activated for Trade Compliance. |  |
| 5 | Activate Delivery Documents | Delivery Type: LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type LF is activated for Trade Compliance. |  |
| 6 | Activate Checks for Purchasing Documents | Purchase Document Type: NBTrade Compliance: <Flag should be checked>Choose Save. | Purchase order type NB is activated for Trade Compliance. |  |
| 7 | Activate Checks for Company Codes | Company Code: 3310Activation Level: Company Code LevelEmbargo: <Flag should be checked>Choose Save. | Company Code 3310 is activated for embargo control. |  |
| 8 | Switch Off Subsequent Functions in SD Processes | Choose New EntriesTrade Regulation Area: 02 EmbargoStatus: B PendingSubsequent functions: 03 Outbound Delivery CreationCondition Active: <Flag should be checked>Choose Save. | Outbound delivery creation is not allowed since sales order is blocked by embargo control.Note We support the suppression of sales document outputs. | You can also choose C Blocked, which means only confirm blocked Sales orders are not allowed to creating follow-on documents. |
| 9 | Define Trade Compliance Legal Regulations | Choose New EntriesLegal Regulation: ITR02Description: Legal Regulation for Embargo ControlTrade Regulation Area: EmbargoChoose Save. | Legal regulation ITR02 is defined. |  |
| 10 | Define Partner Groupings | Choose New Entries.Partner Role Grouping: ZPGEB1Description: Partner Group for "Embargo" Service - ImportAssign Partner Roles LF, WL and RS to defined partner grouping ZPGEB1.Choose SAVE.Back to the change view of the Partner Role Groupings Overview screen.Choose New Entries.Partner Role Grouping: ZPGEB2Description: Partner Group for "Embargo" Service - ExportAssign Partner Roles AG, RE, RG, SP and WE to defined partner grouping ZPGEB2.Choose Save.Note The following values are not allowed for customer systems, so they may not be used as new keys created by customer.Alphanumerical keys beginning with S, Q, R, P, X or YNumerical keys beginning with 0, 5, 6, 7, 8 or 9 | Partner grouping ZPGEB1 & ZPGEB2 is defined.Partner roles (LF, WL, RS) are assigned to partner grouping ZPGEB1.Partner roles (AG, RE, RG, SP, WE) are assigned to partner grouping ZPGEB2. |  |
| 11 | Configure Your Solution - Embargo | Back to the Configure Your Solution: Realize Phase screen, choose (>) Details button for the item Embargo. | The Configure Your Solution - Embargo screen appears. |  |
| 12 | Activate Legal Regulations for Embargo | Choose New EntriesLegal Regulation: ITR02Country/Region: AEChoose Save. | Legal regulation ITR02 is activated for country/region AE. |  |
| 13 | Control Settings for Legal Regulations for Embargo | Select legal regulation ITR02 and maintain as following:Legal Regulation: ITR02Partner Group Import:ZPGEB1Partner Group Export:ZPGEB2Choose SAVE. | Legal regulation ITR02 with the partner grouping code ZPGEB1 will control the embargo check for purchase orders.Legal regulation ITR02 with the partner grouping code ZPGEB2 will control the embargo check for sales processes. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Configuration Activities | Go to the Business Processes Configuration app and search for the following activities mentioned in subsequent Test Step Name respectively.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The related configuration activities screen displays. |  |
| 3 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 4 | Activate Sales Documents | Sales Document Type: ORTrade Compliance: <Flag should be checked>Choose Save. | Sales order type OR is activated for Trade Compliance. |  |
| 5 | Activate Delivery Documents | Delivery Type: LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type LF is activated for Trade Compliance. |  |
| 6 | Activate Checks for Purchasing Documents | Purchase Document Type: NBTrade Compliance: <Flag should be checked>Choose Save. | Purchase order type NB is activated for Trade Compliance. |  |
| 7 | Activate Checks for Company Codes | Company Code: 3310Activation Level: Company Code LevelEmbargo: <Flag should be checked>Choose Save. | Company Code 3310 is activated for embargo control. |  |
| 8 | Switch Off Subsequent Functions in SD Processes | Choose New EntriesTrade Regulation Area: 02 EmbargoStatus: B PendingSubsequent functions: 03 Outbound Delivery CreationCondition Active: <Flag should be checked>Choose Save. | Outbound delivery creation is not allowed since sales order is blocked by embargo control.Note We support the suppression of sales document outputs. | You can also choose C Blocked, which means only confirm blocked Sales orders are not allowed to creating follow-on documents. |
| 9 | Define Trade Compliance Legal Regulations | Choose New EntriesLegal Regulation: ITR02Description: Legal Regulation for Embargo ControlTrade Regulation Area: EmbargoChoose Save. | Legal regulation ITR02 is defined. |  |
| 10 | Define Partner Groupings | Choose New Entries.Partner Role Grouping.: ZPGEB1Description: Partner Group for "Embargo" Service - ImportAssign Partner Roles LF, WL and RS to defined partner grouping ZPGEB1.Choose SAVE.Back to the change view of the Partner Role Groupings Overview screen.Choose New Entries.Partner Role Grouping: ZPGEB2Description: Partner Group for "Embargo" Service - ExportAssign Partner Roles AG, RE, RG, SP and WE to defined partner grouping ZPGEB2.Choose Save.Note The following values are not allowed for customer systems, so they may not be used as new keys created by customer.Alphanumerical keys beginning with S, Q, R, P, X or YNumerical keys beginning with 0, 5, 6, 7, 8 or 9 | Partner roles (LF, WL, RS) are assigned to partner grouping ZPGEB1.Partner roles (AG, RE, RG, SP, WE) are assigned to partner grouping ZPGEB2. |  |
| 11 | Activate Legal Regulations for Embargo | Choose New EntriesLegal Regulation: ITR02Country/Region: AEChoose Save. | Legal regulation ITR02 is activated for country/region AE. |  |
| 12 | Control Settings for Legal Regulations for Embargo | Select legal regulation ITR02 and maintain as following:Legal Regulation: ITR02Partner Group Import:ZPGEB1Partner Group Export:ZPGEB2Choose SAVE. | Legal regulation ITR02 with the partner grouping code ZPGEB1 will control the embargo check for purchase orders.Partner grouping ZPGEB1 & ZPGEB2 is defined.Legal regulation ITR02 with the partner grouping code ZPGEB2 will control the embargo check for sales processes. |  |

#### Create Testing Business Partner for Iran (IR)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner for Iran (IR) for embargo testing. Use the following entries (from step 1 to step 3) and refer to master data script BND document to create a customer master record with the country key IR. Use the following entries (step 4) and refer to master data script BNE document to create a supplier master record with the same ID as the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Creating Customer Master Data - General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: External alpha-numeric numberingTitle: 0003-CompanyName: <Enter the name for the Business Partner>Postal Code/City: 1696700000/ MashhadCtry/Reg.: IR (Iran)Language: English | IR customer XXXX with general data has been created. |  |
| 2 | Create Customer Master Data - Company Code Data | Make the following entries:Company Code: 3310Reconciliation Account: 12120000 (Trade Receivables Foreign)Terms of Payment: 0001 (Payable immediately Due net) | IR customer XXXX with company code level data has been created. |  |
| 3 | Create Customer Master Data - Sales Area Data | Make the following entries:Sales Org.: 3310Distr. Channel:10Division: 00Currency: AEDDelivery Priority: 02 NormalDelivering Plant: 3310 AE PlantShipping Conditions: 01 StandardIncoterms: EXW / Location of sellerPayment Terms: 0001 (Payable immediately Due net)AcctAssgGr: Account assignment group 02 Foreign RevenuesTax Classification: 0 Tax EmptyPartner Function:SP - Sold-to PartyBP - Bill-To PartyPY - PayerSH - Ship-to Party | IR customer XXXX with sales area level data has been created. |  |
| 4 | Create Supplier Master Data - Purchasing Organization Data | Make the following entries:Purchase Org.: 3310Currency: AEDPartner Function:VN - SupplierPI - Invoicing PartyGS - Goods SupplierNote In case PRA functionality is activated in your system, please enter the PRA related attributes ( "Additional Data, PRA General") for business partner's supplier role, for example: Res. Country/Reg.: US, Region: AA, Entity Type: 06, Payment Type: C, Frequency: 1. | IR supplier XXXX with purchasing organization data has been created. |  |

#### Maintain Condition Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To ensure Sales Orders with international business partner (for example, Iran (IR) customer created by step [Create Testing Business Partner for Iran (IR)](#unique_6) [page ] 15) can be created successfully, corresponding Condition Record needs to be maintained.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Pricing Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Navigate | Click into to the app Set Material Prices - Sales (VK12). | The Change Condition Records view displays. |  |
| 3 | Choose Condition Type | In the view Change Condition Records, maintain below information:Condition Type : <input country-specific condition type>, for example, TTX1 for DEThen choose Enter, and in the Key Combination window, select Export Taxesand choose Choose. |  |  |
| 4 | Maintain Condition Record | On the next screen, enter the information below:Departure Ctry/Reg.: AEThen choose Execute.Maintain a new entry with below information:Destination Country/Region: IRTaxClass1-Cust.: 0Tax Class. Material: 1Valid From: for example, <current date>Valid To: 12/31/9999Tax Code: <Please select appropriate tax code, for example, A0 for DE>Choose Save.Note The above countries/regions are only used as examples to showcase how to maintain condition records. Please adjust accordingly according to your business requirement. | Condition Record is maintained. |  |

## Overview Table

The Embargo Control scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Countries Under Embargo](#unique_11) [page ] 21 | Trade Compliance Specialist | Manage Countries Under Embargo (F2791) | Country/region list is created/changed. |
| Outbound Process |  |  |  |
| Manage Sales Documents |  |  |  |
| [Manage Sales Quotations (Optional)](#unique_12) [page ] 22 | Internal Sales Representative | Manage Sales Quotations (F1852) | Sales quotation is created. |
| [Manage Sales Orders](#unique_13) [page ] 22 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Manage Sales Orders Without Charge (Optional)](#unique_14) [page ] 24 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order without charge is created. |
| [Manage Sales Contracts (Optional)](#unique_15) [page ] 24 | Internal Sales Representative | Manage Sales Contracts (F1851) | Sales contract is created. |
| [Manage Sales Scheduling Agreements (Optional)](#unique_16) [page ] 24 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Sales scheduling agreement is created. |
| Outbound Process - [Manage Documents - Trade Compliance](#unique_17) [page ] 24 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Embargo control blocks on sales documents and deliveries are displayed. |
| [Option 1: Confirm Block](#unique_18) [page ] 24 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Sales order is a confirmed block. |
| [Option 2: Release Block](#unique_19) [page ] 25 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Sales order is released. |
| [Create Outbound Delivery](#unique_20) [page ] 26 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| Inbound Process |  |  |  |
| Manage Purchase Documents |  |  |  |
| [Manage Purchase Requisitions (Optional)](#unique_21) [page ] 28 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisition is created. |
| [Manage Purchase Orders](#unique_22) [page ] 28 | Purchaser | Create Purchase Order - Advanced (ME21N) | An on-hold purchase order is created. |
| [Manage Purchase Contracts (Optional)](#unique_23) [page ] 29 | Purchaser | Manage Purchase Contracts (F1600A) | Purchase contract is created. |
| [Manage Purchase Scheduling Agreements (Optional)](#unique_24) [page ] 29 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Purchase scheduling agreement is created. |
| Inbound Process - [Manage Documents - Trade Compliance](#unique_25) [page ] 29 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Embargo control blocks on purchase documents and deliveries are displayed. |
| [Option 1: Confirm Block](#unique_26) [page ] 30 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Purchase order is a confirmed block. |
| [Option 2: Release Block](#unique_27) [page ] 30 | Trade Compliance Specialist | Manage Documents - Trade Compliance (F2826) | Purchase order is released. |
| [Create Inbound Delivery](#unique_28) [page ] 31 | Receiving Specialist | Create Inbound Delivery (VL31N) | Inbound delivery is created. |
| [Schedule Recheck Documents Background Job for Trade Compliance (Optional)](#unique_29) [page ] 32 | Trade Compliance Specialist | Schedule Recheck Documents - Trade Compliance (F4285) | The background job is scheduled. |
| [Analyze and Resolve Blocked Documents](#unique_30) [page ] 33 | Trade Compliance Specialist | Analyze and Resolve Blocked Documents - Trade Compliance (F5445) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Countries Under Embargo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you maintain the list of countries/regions that are under embargo for checking as part of embargo control.

|  |
| --- |
| Note The regional embargos for specific regions of a country can be supported by the legal control rules. For detailed information, refer to the process step Maintain Decision Table for Blocklisting within scope item 1W8 - Legal Control. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Navigate | Access app Manage Countries Under Embargo (F2791). | The Manage Countries/Regions Under Embargo screen appears. |  |
| 3 | Create Country/Region List for Legal Regulation | Enter Legal Regulation: ITR02Choose Add （+）Enter Country/Region: IRValid From: for example, <today's date>Valid To: for example, 12/31/9999Choose Save. | Country Iran (IR) is maintained for legal regulation ITR02. |  |

### Outbound Process

#### Manage Sales Documents

In this section, you can manage sales documents which are supported by embargo. Besides the sales documents, the outbound delivery documents are also supported by embargo.

|  |
| --- |
| Note The outbound delivery without order reference is not shown in this test script, only the outbound delivery with order reference is demonstrated. |

Managing sales order is taken as an example to show how embargo check is embedded in the outbound process. To manage other sales documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before managing sales documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating sales documents, choose foreign customers which are created in the preliminary step.

##### Manage Sales Quotations (Optional)

To create sales quotation, refer to the Create Sales Quotation process step in the test script of the scope item Sales Quotation (BDG).

##### Manage Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a sales order to trigger an embargo check.

|  |
| --- |
| Note The embargo check is also triggered when changing the sales order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders (F1873). | The Manage Sales Orders view displays. |  |
| 3 | Create Sales Order | Choose the Create Sales Order VA01 button, and make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. |  |  |
| 4 | Enter Sales Order Item Data and Save | Sold-To Party: <Above created IR customer XXXX>Ship-To Party: <Above created IR customer XXXX>Cust. Reference: Embargo control testingMaterial: TG12Order Quantity: 10Plant: 3310Choose Save | Standard Order XXXX has been saved. A message shows up with "Item 10 is blocked by Embargo Check (International Trade)".You can also use Display Sales Orders - VA03 (VA03) app to check the international trade status in every item's Status tab. |  |

|  |
| --- |
| Note If the sales order requires approval, follow the Process Sales Order Approval (Optional) steps described in the Sell from Stock (BD9) test script. |

##### Manage Sales Orders Without Charge (Optional)

To create sales order without charge, refer to the Create Sales Order process step in the test script of the scope item Free of Charge Delivery (BDA).

##### Manage Sales Contracts (Optional)

To create sales contract, refer to the Create Sales Contract process step in the test script of the scope item Sales Contract Management (I9I).

##### Manage Sales Scheduling Agreements (Optional)

To create sales scheduling agreement, refer to the Create Sales Scheduling Agreement process step in the test script of the scope item Sales Scheduling Agreements (3NR).

The embargo check is triggered only when the delivery schedule is maintained in the created sales scheduling agreement.

#### Manage Documents - Trade Compliance

Purpose

Confirm or resolve a sales document's blocking by embargo control. For most documents blocked by an embargo control, the block should be retained as part of international trade requirements. However, there are some specific scenarios, such as humanitarian assistance, that make it appropriate to release the blocked document. In these scenarios, you can choose the second option to released blocked sales document.

##### Option 1: Confirm Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note When you choose option 1: confirm block, then the process ends without any follow-on activity. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance screen appears. |  |
| 3 | Sales Document Worklist | Document Number: <XXXX>Choose Go. | Sales document XXXX displays with Blocking Status Blocked | Sales order number XXXX was created in the previous step [Manage Sales Documents](#unique_32) [page ] 22. |
| 4 | Confirm Sales Document | Select Document Number: XXXXGo to the Block screen by choosing the sales document.Input the User Comment (Optional) and choose Confirm Block. | Sales Order XXXX is Confirmed Block. |  |

|  |
| --- |
| Note You can search directly for Trade Compliance documents via the Enterprise search box on the top right of the screen via selecting Trade Compliance Documents in the search criteria.In the result list you can either jump into the app Manage Documents – Trade Compliance, or display the details of the trade compliance document via the document number. |

##### Option 2: Release Block

|  |
| --- |
| Note When you choose option 2: release block, you can create a delivery as the follow-on action. |

###### Release Block

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
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Trade Compliance Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance screen appears. |  |
| 3 | Sales Document Worklist | Document Number: <XXXX>Choose Go. | Sales document XXXX displays with Blocking Status Blocked | Sales order number XXXX was created in the previous step [Manage Sales Documents](#unique_32) [page ] 22. |
| 4 | Release Sales Document | Select Document Number: <XXXX>Go to the Block screen by choosing the sales document.Input the User Comment (Optional) and choose Release Block. | Sales Order XXXX is Released. |  |

###### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create an outbound delivery to trigger an embargo check.

|  |
| --- |
| Note Here the outbound delivery is created by referring to the sales order, you may refer to the test script of the scope item Delivery Processing Without Order Reference (1MI) to create the outbound delivery without order reference to trigger an embargo check.The related sales order should be released for embargo control in step [Release Block](#unique_33) [page ] 25. Otherwise you are not allowed to create delivery and will get the error message Item is blocked by Embargo Check (International Trade). |

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders screen appears. |  |
| 3 | Search Sales Order | Mark the following entries and choose Go:Shipping point: 3310Planned Creation Date: <Delivery selection date>SD Document: <XXXX> |  | Sales order number XXXX was created in previous step [Manage Sales Documents](#unique_32) [page ] 22. |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Embargo Control Status | Please refer to [Manage Documents - Trade Compliance](#unique_17) [page ] 24 to manage the blocking status for the created delivery. | The blocking status is checked for the created delivery. |  |

### Inbound Process

#### Manage Purchase Documents

In this section, you can manage purchase documents which are supported by embargo.

Managing purchase order is taken as an example to show how embargo check is embedded in the inbound process. To manage other purchase documents, go to the corresponding steps to check the reference scope items for detailed procedures.

Before managing purchase documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

When creating purchase documents, choose foreign suppliers which are created in the preliminary step.

##### Manage Purchase Requisitions (Optional)

To create purchase requisition, refer to the Create Purchase Requisition process step in the test script of the scope item Purchase Contract (BMD).

##### Manage Purchase Orders

Purpose

This step creates a purchase order and triggers the embargo control check.

|  |
| --- |
| Note The embargo check is also triggered when changing the pruchase order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App: Purchase Orders | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order - Advanced screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data:Order type: Standard POSupplier: Above created IR supplier XXXXChoose the Header section button, and make the following entries on the Org. Data tab:Purchasing Org.: 3310Purchasing Group:001Company Code: 3310In the Item Overview section,Material :TG0012PO Quantity: <Enter the quantity>Net Price: <Enter the price>Plant: 3310In the Item Detail section,Under Confirmation tab:Conf. Control: Inbound Delivery | The Create Purchase Order - Advanced screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save. When the purchase order number is displayed, write it down for further use. | International Purchase Order from IR supplier to AE.A Purchase Order is created. Purchase Order Number is displayed. | Note Because the trade compliance check is activated for the purchase order type, you can check the trade compliance statuses on the Compliance tab at both the header and item levels.If the trade compliance statuses are either pending or blocked, subsequent processes ‒ such as the creation of inbound deliveries ‒ will be halted. |

##### Manage Purchase Contracts (Optional)

To create purchase contract, refer to the Create Purchase Contract process step in the test script of the scope item Purchase Contract (BMD).

##### Manage Purchase Scheduling Agreements (Optional)

To create purchase scheduling agreement, refer to the Create Scheduling Agreement process step in the test script of the scope item Scheduling Agreements in Procurement (BMR).

The embargo check on purchase scheduling agreements is supported only when creating scheduling agreements with SAP Fiori app Manage Purchase Scheduling Agreements (F2179), so you need to make sure you've added the schedule lines into scheduling agreements before saving in the preparation status.

#### Manage Documents - Trade Compliance

Purpose

Confirm or resolve a purchase document's blocking by embargo control. For most documents blocked by an embargo control, the block should be retained as part of international trade requirements. However, there are some specific scenarios, such as humanitarian assistance, that make it appropriate to release the blocked document. In these scenarios, you can choose the second option to released blocked sales document.

##### Option 1: Confirm Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Recheck and resolve blocked purchase orders. For most documents which are blocked by embargo, system should keep the block for international trade requirements. However, there are some specific scenarios, such as humanitarian assistance, that needs to release the documents. At this situation, you can choose the second option to release blocked purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Trade Compliance Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance screen appears. |  |
| 3 | Purchase Order Worklist | Document Number: <XXXX>Choose Go. | Purchase Order XXXX displays with Blocking Status Blocked. | Purchase order number XXXX was created in the previous step [Manage Purchase Documents](#unique_34) [page ] 27. |
| 4 | Confirm Purchase Order | Select Document Number: <XXXX>Go to the Block screen by choosing the Purchase Order.Input the User Comment (Optional) and choose Confirm Block. | Purchase Order XXXX is Confirmed Block. |  |

##### Option 2: Release Block

|  |
| --- |
| Note When you choose option 2: release block, you can create a delivery as the follow-on action. |

###### Release Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

When you choose option 2: release block, the purchase order status will automatically be changed from on-hold to saved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Trade Compliance Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Documents - Trade Compliance (F2826). | The Manage Documents – Trade Compliance screen appears. |  |
| 3 | Purchase Order Worklist | Document Number: <XXXX>Choose Go. | Purchase order XXXX displays with Blocking Status Blocked. | Purchase order number XXXX was created in the previous step [Manage Purchase Documents](#unique_34) [page ] 27. |
| 4 | Release Purchase Order | Select Document Number: <XXXX>Go to the Block screen by choosing the purchase order.Input the User Comment (Optional) and choose Release Block. | Purchase Order XXXX is Released. | You can go to Manage Documents - Trade Compliance to see that the status of PO is released, and the purchase order status will automatically be changed from on-hold to saved. |

###### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an inbound delivery to trigger an embargo check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Inbound Delivery (VL31N). | The Create Inbound Delivery screen appears. |  |
| 3 | Create Inbound Delivery | Mark the following entries and choose Enter:Supplier: <Enter your foreign supplier>Purchase Order: <Created purchase document number>Delivery Date: <Delivery selection date> |  |  |
| 4 | Save | Choose Save. | Creation of a delivery is triggered. |  |
| 5 | Check Embargo Control Status | Please refer to [Manage Documents - Trade Compliance](#unique_25) [page ] 29 to manage the blocking status for the created delivery. | The blocking status is checked for the created delivery. |  |

### Schedule Recheck Documents Background Job for Trade Compliance (Optional)

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

### Analyze and Resolve Blocked Documents

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
- see-also :: [[13-quality-ehs-and-compliance/test-script-restricted-party-screening-with-sap-watch-list-screening-1]]
- see-also :: [[13-quality-ehs-and-compliance/assess-dangerous-goods-for-a-product-3fc-ae-test-script-933]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WC_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 58,450 chars in the whole document
