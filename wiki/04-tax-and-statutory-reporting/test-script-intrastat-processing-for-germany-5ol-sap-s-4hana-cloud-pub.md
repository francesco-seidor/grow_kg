---
id: 04-tax-and-statutory-reporting/test-script-intrastat-processing-for-germany-5ol-sap-s-4hana-cloud-pub
title: "Test Script: Intrastat Processing for Germany (5OL) - SAP S/4HANA Cloud Public Edition (5OL_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 5OL: Intrastat declarations for Germany (RITA) in S/4HANA Cloud Public Edition 2608 - prerequisites, configuration, commodity codes, POI, declarations."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/germany-vat-and-intrastat]
aliases: [5OL_S4CLD2608_BPD_EN_XX]
keywords: [Germany VAT Returns and Intrastat, intrastat declarations, intrastat configuration, commodity codes, product classification, providers of information, intrastat background jobs, declaration release, customs units of measure, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OL_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1117
topic: 04-tax-and-statutory-reporting/germany-vat-and-intrastat
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intrastat Processing for Germany (5OL) - SAP S/4HANA Cloud Public Edition (5OL_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OL_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Germany VAT Returns and Intrastat** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intrastat Processing for Germany (5OL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232824976)

[2 Prerequisites 4](#_Toc232824977)

[2.1 System Access 4](#_Toc232824978)

[2.2 Roles 4](#_Toc232824979)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232824980)

[2.4 Business Conditions 6](#_Toc232824981)

[2.5 Preliminary Steps 6](#_Toc232824982)

[2.5.1 Configuration Activities for Intrastat Reporting 6](#_Toc232824983)

[2.5.2 Configuration Activities for Classification 15](#_Toc232824984)

[3 Overview Table 22](#_Toc232824985)

[4 Test Procedures 24](#_Toc232824986)

[4.1 Manage Commodity Codes 24](#_Toc232824987)

[4.2 Classify Products Commodity Codes 25](#_Toc232824988)

[4.3 Reclassify Products Commodity Codes (Optional) 26](#_Toc232824989)

[4.4 Display Classified Products 27](#_Toc232824990)

[4.5 Create Person Responsible for International Trade 28](#_Toc232824991)

[4.6 Manage Providers of Information 30](#_Toc232824992)

[4.7 Create Intrastat Declarations Manually 32](#_Toc232824993)

[4.8 Create Intrastat Declarations Automatically (Background Job) 34](#_Toc232824994)

[4.9 Display Intrastat Declarations 36](#_Toc232824995)

[4.10 Change Intrastat Declaration Item (Optional) 36](#_Toc232824996)

[4.11 Add Intrastat Declaration Item for Existing Declarations (Optional) 38](#_Toc232824997)

[4.12 Release Intrastat Declarations and Create Declaration File 38](#_Toc232824998)

[4.13 Cancel Release Intrastat Declarations (Optional) 40](#_Toc232824999)

## Purpose

Overview

This scope item provides system-generated Intrastat declarations.

Intrastat is a statistical system used to collect information from enterprises regarding trade between European Union (EU) member states.

When the EU was created in 1993 and the initial EU member states became part of the single market, information about their trade with other EU member states could no longer be obtained from customs documents.

Intrastat evolved as a replacement to collect information directly from enterprises about dispatches and arrivals of commodities among member states. Today, Intrastat is used for collecting statistics on the trade in goods (services are excluded) between the EU member states.

In general, this scope item is activated when the RITA (Registration of Indirect Tax Abroad) solution is activated in your company. For example: you have a company outside of Germany but with tax registration in Germany. You need to report Intrastat declaration in Germany for the trade in goods (dispatches and arrivals) between Germany and the other EU Member States.

Do you have a company registered in Germany?

- No - In this situation, you have not selected Germany in the scoping and the country solution for Germany has not been activated in your system. Please refer to this document to perform the testing.
- Yes - In this situation, you have selected Germany in the scoping and the country solution for Germany has been activated in your system. Please refer to the test script of scope item [BDT](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BDT) (DE) to perform the testing.

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

For more information, refer to How to Create a Business Role for the Administrator in the [product assistance](https://help.sap.com/viewer/a630d57fc5004c6383e7a81efee7a8bb/latest/en-US/8fa28e0107984d42a99b9eea67856cea.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Trade Classification Specialist | SAP_BR_TRD_CLS_SPECIALIST | International Trade Classification | SAP_BR_TRD_CLS_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Intrastat Specialist | SAP_BR_INTRASTAT_SPECIALIST | Intrastat | SAP_BR_INTRASTAT_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC | Please ask your system administrator to assign to the testers. |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC | Please ask your system administrator to assign to the testers. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Please ask your system administrator to assign to the testers. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 |  | See sections Business Conditions. Following the corresponding scope item. For more information about creating master data, see the following Master Data Script documentation. |
| Plant | Plant abroad located in DE |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. You can choose to complete RITA related process before running the testing for this scope item. For example: Sell from stock from a physical plant abroad before you start going through this scope item.

You can use the business partner mentioned in Master Data, Organization Data and Other data to complete the RITA related processes.

You can also manually create Intrastat declaration without creating RITA related documents. It is also allowed in this scope item.

### Preliminary Steps

#### Configuration Activities for Intrastat Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When some prerequisite scope items from SD and MM are activated in customer system, customer may need to maintain the additional configuration by following SSCUIs before performing testing. You are recommended to configure SSCUIs before starting to test in SAP S/4HANA Cloud Public Edition system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. |  |  |
| 2 | Access the SAP Fiori app | Choose the Manage Your Solution (F1241) app. | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Navigate to Configure Your Solution.Search for apps mentioned in subsequent test steps respectively. Choose the row that appears on the list. On the second screen, you would see the searched app. Choose Configure. |  |  |
| 4 | Define Default Values for Sales | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the SSCUI are listed in Table 1.Country of Decl.: DEItem Category: CB1I, used in scope item BDW-Returnables ProcessingIntrastat Group: <Leave blank>Business Trans. Type: 11Procedure Dispatches: <Leave blank>Procedure Receipts: <Leave blank>Movement Code: <Leave blank>Choose Save. | The default values for Intrastat report are defined for the item categories which are used for the prerequisite of SD or MM scope items. |  |
| 5 | Define Default Values for Purchasing | This configuration depends on the prerequisite scope items which have been activated in customer systems. Check customer scope items first.The reference configurations in the SSCUI are listed in Table 2.Country of Decl.: DEThe following Purchasing fields combination is used in scope item BMR scheduling Agreements in Procurement.Purch. Doc. Category : LPurchasing Doc. Type: LPItem Category: 2Trans. Type Receipts: 12Procedure Receipts: <Leave blank>Movement Code: <Leave blank>Trans.Type Returns: 21Procedure Returns: <Leave blank>Choose Save. | The default values for Intrastat report are defined for the purchasing fields combination which is used for the prerequisite of SD or MM scope items. |  |
| 6 | Define Exclusion of Sales Document Item Categories | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the SSCUI are listed in following Table 3.Item Category: CBTEChoose Save. | The exclusion of sales document item categories is defined. |  |
| 7 | Define Sales Document Item Categories for Services | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the SSCUI are listed in Table 4.Item Category: TAD, used in scope item 2ET-Sales Order Processing for Non-Stock Material.Choose Save. | The sales document item categories that contain data regarding services are defined. |  |
| 8 | Define Data Selection Control for Sales | Please check the selection logic of sales for the country of declaration to make sure the default selection logic is compliant with the legal regulation of the authority.Changing the Selection Control indicator could result in a different set of documents being reported for the same month and year.Please refer to the following SAP note [2976331](https://me.sap.com/notes/2976331) to understand the influence of the selection logic to the Intrastat report. | The selection logic is compliant with the legal regulation of the authority. |  |
| 9 | Define Data Selection Control for Purchasing | Please check the selection logic of purchasing for the country of declaration to make sure the default selection logic is compliant with the legal regulation of the authority.Changing the Selection Control indicator could result in a different set of documents being reported for the same month and year.Please refer to the following SAP note [2976331](https://me.sap.com/notes/2976331) to understand the influence of the selection logic to the Intrastat report. | The selection logic is compliant with the legal regulation of the authority. |  |
| 10 | Define Default Values for Specific Business Processes in Sales | In this SSCUI, you can define the default values for the Intra-Community Customer Consignment processes.This configuration depends on the prerequisite customer consignment scope items which have been activated in customer systems.Check customer scope items first.This configuration depends on the prerequisite scope items which have been activated in customer systems. Check customer scope items first.The reference configurations in the SSCUI are listed in Table 5.Country of Decl.: DEBusiness Process : A1Item Category: CFN, used in scope item 1IU-Customer ConsignmentIntrastat Group: <Leave blank>Business Trans. Type: 12Procedure Dispatches: <Leave blank>Procedure Receipts : <Leave blank>Movement Code : <Leave blank>Choose Save. | The default values for the specific business processes are defined based on the item categories which are used for the prerequisite scope items. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Activities | Go to the Business Processes Configuration app and search for apps mentioned in subsequent Test Step Name respectively. Choose the row that appears in the list.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The related activity screen displays. |  |
| 3 | Define Default Values for Sales | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations are listed in Table 1.Country of Decl.: DEItem Category: CB1I, used in scope item BDW-Returnables ProcessingIntrastat Group: <Leave blank>Business Trans. Type: 11Procedure Dispatches: <Leave blank>Procedure Receipts: <Leave blank>Movement Code: <Leave blank>Choose Save. | The default values for Intrastat report are defined for the item categories which are used for the prerequisite of SD or MM scope items. |  |
| 4 | Define Default Values for Purchasing | This configuration depends on the prerequisite scope items which have been activated in customer systems. Check customer scope items first.The reference configurations are listed in Table 2.Country of Decl.: DEThe following Purchasing fields combination is used in scope item BMR scheduling Agreements in Procurement.Purch. Doc. Category : LPurchasing Doc. Type: LPItem Category: 2Trans. Type Receipts: 12Procedure Receipts: <Leave blank>Movement Code: <Leave blank>Trans.Type Returns: 21Procedure Returns: <Leave blank>Choose Save. | The default values for Intrastat report are defined for the purchasing fields combination which is used for the prerequisite of SD or MM scope items. |  |
| 5 | Define Exclusion of Sales Document Item Categories | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations are listed in the following Table 3.Item Category: CBTEChoose Save. | The exclusion of sales document item categories is defined. |  |
| 6 | Define Sales Document Item Categories for Services | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the Configuration Activities are listed in Table 4.Item Category: TAD, used in scope item 2ET-Sales Order Processing for Non-Stock Material.Choose Save. | The sales document item categories that contain data regarding services are defined. |  |
| 7 | Define Data Selection Control for Sales | Please check the selection logic of sales for the country of declaration to make sure the default selection logic is compliant with the legal regulation of the authority.Changing the Selection Control indicator could result in a different set of documents being reported for the same month and year.Please refer to the following SAP note [2976331](https://me.sap.com/notes/2976331) to understand the influence of the selection logic to the Intrastat report. | The selection logic is compliant with the legal regulation of the authority. |  |
| 8 | Define Data Selection Control for Purchasing | Please check the selection logic of purchasing for the country of declaration to make sure the default selection logic is compliant with the legal regulation of the authority.Changing the Selection Control indicator could result in a different set of documents being reported for the same month and year.Please refer to the following SAP note [2976331](https://me.sap.com/notes/2976331) to understand the influence of the selection logic to the Intrastat report. | The selection logic is compliant with the legal regulation of the authority. |  |
| 9 | Define Default Values for Specific Business Processes in Sales | In this configuration activity, you can define the default values for the Intra-Community Customer Consignment processes.This configuration depends on the prerequisite customer consignment scope items which have been activated in customer systems.Check customer scope items first.This configuration depends on the prerequisite scope items which have been activated in customer systems. Check customer scope items first.The reference configurations in the configuration activityI are listed in Table 5.Country of Decl.: DEBusiness Process : A1Item Category: CFN, used in scope item 1IU-Customer ConsignmentIntrastat Group: <Leave blank>Business Trans. Type: 12Procedure Dispatches: <Leave blank>Procedure Receipts : <Leave blank>Movement Code : <Leave blank>Choose Save. | The default values for the specific business processes are defined based on the item categories which are used for the prerequisite scope items. |  |

Table 2: Table 1

| Country of Declaration | Item Category | Intrastat Group | Business Transaction Type | Movement Code | Procedure | Prerequisite Scope Item |
| --- | --- | --- | --- | --- | --- | --- |
| DE | TAX |  | 11 |  |  | 2ET-Sales Order Processing for Non-Stock Material |
| DE | CB1I |  | 11 |  |  | BDW-Returnables Processing |
| DE | CBTA |  | 11 |  |  | BJE-Make-to-Order Production – Finished Goods Sales and Final Assembly |
| DE | RENV |  | 21 |  |  | BKP-Customer Returns |
| DE | TAXN |  | 34 |  |  | BDA-Free of Charge Delivery |
| DE | CBTC |  | 11 |  |  | 1YT-Make-to-Order Production with Variant Configuration |
| DE | NLC |  | 11 |  |  | 1P9-Intercompany Stock Transfer |
| DE | CBTQ |  | 11 |  |  | 31Q-Sales Order Processing for Sales Kits |
| DE | LZN |  | 11 |  |  | 3NR-Sales Scheduling Agreements |
| DE | NCC3 |  | 11 |  |  | 5HP-Advanced Intercompany Stock Transfer |
| DE | NLN |  | 31 |  |  | BME-Stock Transfer with Delivery |
| DE | ELCR |  | 21 |  |  | 2TS-Intercompany Stock Transfer Returns |

Table 3: Table 2

| Country of Declaration | Purchasing Document Type | Purchase Document Category | Item Category | Trans. Type Receipts | Trans.Type Returns | Procedure for Receipt | Procedure for Return | Movement Code | Prerequisite Scope Item |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DE | LP | L | 2 | 32 | 21 |  |  |  | BMR-Scheduling Agreements in Procurement |
| DE | LPA | L | 0 | 11 | 21 |  |  |  | BMR-Scheduling Agreements in Procurement |
| DE | NB2 | F | 5 |  | 21 |  |  |  | BKP-Customer Returns |
| DE | NB | F | 7 | 11 | 21 |  |  |  | 1P9-Intercompany Stock Transfer |
| DE | NBIC | F | 0 | 11 | 21 |  |  |  | 5HP-Advanced Intercompany Stock Transfer |
| DE | NBIC | F | 2 | 32 | 21 |  |  |  | 5HP-Advanced Intercompany Stock Transfer |
| DE | NBIC | F | 4 | 51 |  |  |  |  | 5HP-Advanced Intercompany Stock Transfer |
| DE | NBIC | F | 5 | 11 | 21 |  |  |  | 5HP-Advanced Intercompany Stock Transfer |
| DE | NBF2 | F | 0 |  | 21 |  |  |  | 2TS-Intercompany Stock Transfer Returns |

Table 4: Table 3

| Item Category | Prerequisite Scope Item |
| --- | --- |
| CBTE | 31Q-Sales Order Processing for Sales Kits |
| G2B | 31Q-Sales Order Processing for Sales Kits |
| G2E | 31Q-Sales Order Processing for Sales Kits |
| G2P | 31Q-Sales Order Processing for Sales Kits |
| L2B | 31Q-Sales Order Processing for Sales Kits |
| L2E | 31Q-Sales Order Processing for Sales Kits |
| L2P | 31Q-Sales Order Processing for Sales Kits |
| TAE | 31Q-Sales Order Processing for Sales Kits |
| TAP | 31Q-Sales Order Processing for Sales Kits |
| TAPF | 31Q-Sales Order Processing for Sales Kits |
| CBEE | 31Q-Sales Order Processing for Sales Kits |
| CBTP | 31Q-Sales Order Processing for Sales Kits |
| REB | 31Q-Sales Order Processing for Sales Kits |

Table 5: Table 4

| Item Category | Prerequisite Scope Item |
| --- | --- |
| PS03 | J14-Sales Order Processing – Project-Based Services |
| PS13 | J14-Sales Order Processing – Project-Based Services |
| PS23 | J14-Sales Order Processing – Project-Based Services |
| PS33 | J14-Sales Order Processing – Project-Based Services |
| PS43 | J14-Sales Order Processing – Project-Based Services |
| PSC1 | J14-Sales Order Processing – Project-Based Services |
| TAD | 2ET-Sales Order Processing for Non-Stock Material |
| TADN | 2ET-Sales Order Processing for Non-Stock Material |
| CTAD | 2ET-Sales Order Processing for Non-Stock Material |
| PS53 | J14-Sales Order Processing – Project-Based Services |

Table 6: Table 5

| Country of Declaration | Business Process | Item Category | Intrastat Group | Business Transaction Type | Procedure Receipts | Procedure Dispatches | Movement Code | Prerequisite Scope Item |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DE | A1 | CB9F |  | 32 |  |  |  | 1IU-Customer Consignment |
| DE | A1 | CFN |  | 32 |  |  |  | 1IU-Customer Consignment |
| DE | A1 | LKN |  | 32 |  |  |  | 4LZ-Sales Scheduling Agreement with Consignment |
| DE | A1 | CB9P |  | 21 |  |  |  | 1IU-Customer Consignment |
| DE | A1 | CPN |  | 21 |  |  |  | 1IU-Customer Consignment |
| DE | A1 | KAN |  | 21 |  |  |  | 4LZ-Sales Scheduling Agreement with Consignment |
| DE | A2 | CB9F |  | 32 |  |  |  | 1IU-Customer Consignment |
| DE | A2 | CFN |  | 32 |  |  |  | 1IU-Customer Consignment |
| DE | A2 | LKN |  | 32 |  |  |  | 4LZ-Sales Scheduling Agreement with Consignment |
| DE | A2 | CB9P |  | 21 |  |  |  | 1IU-Customer Consignment |
| DE | A2 | CPN |  | 21 |  |  |  | 1IU-Customer Consignment |
| DE | A2 | KAN |  | 21 |  |  |  | 4LZ-Sales Scheduling Agreement with Consignment |
| DE | B1 | CB1I |  | 12 |  |  |  | BDW-Returnables Processing |
| DE | B1 | CBTA |  | 12 |  |  |  | BJE-Make-to-Order Production – Finished Goods Sales and Final Assembly |
| DE | B1 | CBTC |  | 12 |  |  |  | 1YT-Make-to-Order Production with Variant Configuration |
| DE | B1 | CBTQ |  | 12 |  |  |  | 31Q-Sales Order Processing for Sales Kits |
| DE | B1 | LZN |  | 12 |  |  |  | 3NR-Sales Scheduling Agreements |
| DE | B1 | TAX |  | 12 |  |  |  | 2ET-Sales Order Processing for Non-Stock Material |

#### Configuration Activities for Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To ensure the Customs Unit of Measure correctly mapping with internal Supplementary Unit of Measure, you may use the following Configuration Activities to manage the customs units of measure.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration | The SAP Fiori launchpad is displayed. |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). Navigate to Configure Your Solution.Search for apps mentioned in subsequent Test Step Name respectively. Choose the row that appears in the list. On the second screen you would see the searched app. Choose Configure. Please proceed ahead with further steps described in the document. | The Manage Your Solution screen is displayed. |  |
| 3 | Define Unit of Measure System | Choose New Entries.Unit of Measure System: UOM_EUDescription: Measure System for EUChoose the line of UOM_EU and click Customs Unit of Measure.Click New Entries:Customs Unit of Measure: For example, KGMUoM Description: kilogramSave the entries.Then choose Mapping for Customs Unit of Measure.Choose New Entries:Customs UoM: For example, KGMMU(Unit of Measure): KGSave the entries.For the Customs Unit of Measure, you can check following table 1 for reference. | The Customs Unit of Measures are maintained.The Customs Unit of Measure are mapped with internal Unit of Measure. |  |
| 4 | Define Numbering Scheme Content for Commodity Codes | Double click the Numbering Scheme Content EU01.Maintain the following entry:Unit of Measure System: Measure System for EU. | The Unit of Measure System is assigned to the Numbering Scheme Content. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Define Unit of Measure System | Go to the Business Processes Configuration app and search for configuration activity: Define Unit of Measure System.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Unit of Measure System screen displays. |  |
| 3 | Define Measure System | Choose New Entries.Unit of Measure System: UOM_EUDescription: Measure System for EUChoose the line of UOM_EU and click Customs Unit of Measure.Click New Entries:Customs Unit of Measure: For example, KGMUoM Description: kilogramSave the entries.Then choose Mapping for Customs Unit of Measure.Choose New Entries:Customs UoM: For example, KGMMU(Unit of Measure): KGSave the entries.For the Customs Unit of Measure, you can check following table 1 for reference. | The Customs Unit of Measures are maintained.The Customs Unit of Measure are mapped with internal Unit of Measure. |  |
| 4 | Open Define Numbering Scheme Content for Commodity Codes | Go to the Business Processes Configuration app and search for configuration activity: Define Numbering Scheme Content for Commodity Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Numbering Scheme Content for Commodity Codes screen displays. |  |
| 5 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration | The SAP Fiori launchpad is displayed. |  |
| 6 | Define Numbering Scheme Content for Commodity Codes | Double click the Numbering Scheme Content EU01.Maintain the following entry:Unit of Measure System: Measure System for EU. | The Unit of Measure System is assigned to the Numbering Scheme Content. |  |

Table 7: Table 1

| Customs Unit of Measure | Description |
| --- | --- |
| ASV | %vol |
| ASVX | %vol/hectolitre |
| CCT | Carrying capacity in tonnes |
| CEN | Hundred items |
| CTM | Carats(1 metric carat=2 x 10-4 kg) |
| DAP | Deka ton |
| DTN | 100 kilograms |
| DTNE | Hectokilogram net drained weight |
| DTNF | Hectokilogram net soft wheat |
| DTNG | Hectokilogram net raw weight |
| DTNM | Hectokilogram net dry matter |
| DTNN | Hectokilogram dead weight |
| DTNR | Hectokilogram raw sugar with a yield of 92% |
| DTNS | Hectokilogram white sugar |
| DTNZ | Hectokilogram per 1% by weight of sucrose |
| GFI | Gram of fissile isotopes |
| GRM | Gram |
| GRT | Gross tonnage |
| HLT | Hectolitre |
| KAC | Kg net Ace K |
| KCC | Kilograms of choline chloride |
| KCL | Tonne of potasium chloride |
| KGM kilogram | Kilogram |
| KGMA kilograms total alcohol | Kilograms total alcohol |
| KGMB kilograms gross weight | Kilograms gross weight |
| KGME | Kilogram drained net weight |
| KGMN | Kilogram dead weight |
| KGMP | Kilogram of lactic matter |
| KGMS | Kg of raw sugar |
| KGMT | Kilogram dry lactic matter |
| KLT | 1000 Litre |
| KMA | Kilogram of methylamines |
| KMT | Kilometer |
| KNI | Kilogram of nitrogen |
| KNS | Kilogram of hydrogen peroxide |
| KPH | Kilogram of Potassium hydroxide(Caustic potash) |
| KPO | Kilogram of potassium oxide |
| KPP | Kilogram of diphosphorus pentaoxide |
| KSD | Kilogram of substance 90% dry |
| KSH | Kilogram of sodium hydroxide(caustic soda) |
| KUR | Kilogram of uranium |
| LPA | Litre pure(100%) alcohol |
| LTR | Litre |
| MIL | Thousand items |
| MTK | Square metres |
| MTQ | Cubic metres |
| MTQC | Thousand cubic meters |
| MTR | Metre |
| MWH | Megawatt hours |
| NAR | Number of items |
| NARB | Per bottle |
| NCL | Number of cells |
| NPR | Number of pairs |
| TJO | Terajoule(gross calorific value) |
| TNE | Tonne net |
| TNEG | Tonne net gross weight |
| TNEI | 1000 kg/biodiesel |
| TNEJ | 1000 kg/ fuel content |
| TNEK | Tonne Bioethanol content |
| TNEM | 1000 kg/ net dry weight |
| TNEN | 1000 kg/ net dead weight |
| TNEZ | 1000 kg/ net / % sacchar. |
| WAT | Watt |

## Overview Table

To start working with the Intrastat application, you need to carry out the setup steps described in the previous chapter Prerequisites.

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Commodity Codes](#unique_11) [page ] 24 | Trade Classification Specialist | Manage Commodity Codes (F2516) | Commodity code is created / changed. |
| [Classify Products Commodity Codes](#unique_12) [page ] 25 | Trade Classification Specialist | Classify Products - Commodity Codes (F2151) | Commodity codes are assigned to products. |
| [Reclassify Products Commodity Codes (Optional)](#unique_13) [page ] 26 | Trade Classification Specialist | Reclassify Products - Legal Control (F2391) | Commodity codes are changed for products. |
| [Display Classified Products](#unique_14) [page ] 27 | Trade Classification Specialist | Display Classified Products - International Trade (F3789) | International trade classification data is displayed. |
| [Create Person Responsible for International Trade](#unique_15) [page ] 28 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Person Responsible is saved. |
| [Manage Providers of Information](#unique_16) [page ] 30 | Intrastat Specialist | Manage Providers of Information (/ECRS/POI_EDIT) | Provider of Info. Is created / changed. |
| [Create Intrastat Declarations Manually](#unique_17) [page ] 32 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) |  |
| [Create Intrastat Declarations Automatically (Background Job)](#unique_18) [page ] 34 | Intrastat Specialist | Select Dispatches and Customer Returns - Intrastat Declaration (F2507) or Select Receipts and Returns to Supplier - Intrastat Declaration (F2508) | Job is scheduled and shown in the list. |
| [Display Intrastat Declarations](#unique_19) [page ] 36 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | All the declarations under the POI and Item details display. |
| [Change Intrastat Declaration Item (Optional)](#unique_20) [page ] 36 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | Changes are saved. |
| [Add Intrastat Declaration Item for Existing Declarations (Optional)](#unique_21) [page ] 38 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | New item is added. |
| [Release Intrastat Declarations and Create Declaration File](#unique_22) [page ] 38 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | Declaration File could be saved in the target folder. |
| [Cancel Release Intrastat Declarations (Optional)](#unique_23) [page ] 40 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | Release of Declaration is canceled |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Commodity Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create commodity code under numbering scheme EU01.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Commodity Codes (F2516). | The Manage Commodity Codes view displays. |  |
| 3 | Enter No. Scheme Content | In the overview screen: make the following entries and choose Go:No. Scheme Content: EU01 Commodity Codes for European Union: Combined Nomenclature of the European Union (EU01) |  |  |
| 4 | Enter Commodity Codes details | Choose +(Add).Make the following entries and choose Enter:Commodity Code: for example, 84713000Valid From/To: for example, 2016.10.01 / 2016.12.31Official Description: <free text>Valid From: for example, 2016.01.01Valid To: for example, 9999.12.311st Customs Unit of Measure: KGM2nd Customs Unit of Measure: <leave blank>Choose Save. | Commodity code is saved. |  |

### Classify Products Commodity Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you classify the products with the commodity code you created in the last step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the tile Classify Products - Commodity Codes (F2151). | The Classify Products - Commodity Codes displays. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Numbering Scheme: Combined Nomenclature of the European Union (EU01)Valid On: for example: 2016.01.01 (This date should be in the valid period of the Commodity code you want to use)Product (Optional): for example: TG0011 | Product entry is displayed.If the product has already been assigned commodity code, it won't display in this tile. To maintain this one, tile Reclassify Products Commodity Codes should be used. |  |
| 4 | Classify Product | In the Products Area, select the product entry, choose Classify: make the following entries :Commodity Code: <Commodity Code created in the last step>Classification From/To: for example, <current date>Remark: <your remark>Choose Save. | Classification is saved. |  |

### Reclassify Products Commodity Codes (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can reclassify the products which were classified with commodity codes before with new commodity codes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori Launchpad using the role Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open tile Reclassify Products - Commodity Codes (F2152). | The overview screen is displayed. |  |
| 3 | Enter Filters | In the overview screen: make the following entries and choose Go:Numbering Scheme: Combined Nomenclature of the European Union (EU01)Valid On: for example, 2016.01.01 (This date should be in the valid period of the Commodity code you want to use.)Product (Optional): for example, TG10 | Product entry displays. |  |
| 4 | Reclassify Product | In the overview screen select the product entry, choose Reclassify.Make the following entries:Commodity Code: another commodity codeClassification From/To: for example, 2016.01.01 / 9999.12.31Remark: <your remark>Choose Save. | Reclassification is saved. |  |

### Display Classified Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, you can display all the international trade classification data including commodity code, control class, customs tariff number and Intrastat Services Codes for the products you have classified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Classified Products - International Trade (F3789). | The Display Classified Products view is displayed. |  |
| 3 | Enter Filters | In the Display Classified Products view, make the following entries and choose Go:Product: <Enter a Product, for example, TG0011> | The entered product displays. |  |
| 4 | Display the List for Classified Products | In the Display Classified Products - International Trade view, choose the product. | The Display Classified Products - International Trade view displays. |  |
| 5 | Display Classification Data for Product | In the Display Classified Products - International Trade view, choose the Numbering Scheme you maintained for the product, for example, Combined Nomenclature of the European Union (EU01). | The Classification for Commodity Code is displayed. |  |
| 6 | Display the Classification History for Commodity Code | In the Commodity Codes tab, you can find the classification history of commodity codes for the product with validation period.In the Change Documents tab, you can see the details of changed data including old and new values, created by, created on, and change types for the fields belonging to classification.You can follow the same steps to display other classification data like Intrastat Service Codes for the product. |  |  |

### Create Person Responsible for International Trade

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the contact person with BP role SLLSTL-Person Responsible for International Trade. The contact person will be maintained in the POI (Providers of Information).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log onto the SAP Fiori Launchpad using the role Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Maintain Business Partner tile. |  |  |
| 3 | Create a BP Person | Choose Create and select Person. | The Create Person screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Leave blank>Create in BP role: Person Resp. Intl Trade. The BP role is SLLSTL. |  |  |
| 5 | Enter Address Data | On the Address tab in the Name section, enter the following data:Title: Mr. or Ms.First Name: <First Name>Last Name: <Last Name> |  |  |
| 6 | Enter Standard Address | On the Address tab in the Standard Address section, enter the following data:Street/House number: <free text>Postal Code/City: <Enter the postal code of Person Responsible>Country: <Enter the country of Person Responsible>Region: <Enter the region of Person Responsible>Language: ENChoose OK. |  |  |
| 7 | Enter Communication Data | On the Address tab in the Standard Communication section, enter the following data:Telephone: <Telephone number of the person responsible>Cell Phone: <Cell Phone number of the person responsible>Fax: <Fax number of the person responsible>E-Mail: <E-mail address of the person responsible> |  |  |
| 8 | Save the data | Choose Save. | Person Responsible is saved. |  |

### Manage Providers of Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create POI (Providers of Information) for the company with the information like country of declaration, address, contact person, telephone, fax. You can also determine the plant and for intercompany sales, determine the delivering plants for the POI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Intrastat Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Providers of Information (/ECRS/POI_EDIT). | The overview screen is displayed. |  |
| 3 | Create Provider of Info | In the Overview view, choose Create and make the following entries:Provider of Info: DE_POICtry of Declaration: DECompany Code: <your company code>Choose Continue and make the following entries:In Provider of Information section:Name, Street/House Number, Postal Code, City, Phone, Fax are automatically reused from the address data for company code. You do not need to enter these information again.State of Tax Office:<for example, 11 (Berlin)>Tax Number: <for example, 11 (Bucuresti)1234567890>Additional Number: 000Contact Person: <BP role for contact person is SLLSTL (Person Responsible)>Please enter the number for contact person of POI.In Basic Settings section:Exchange Rate Type: <for example, M>Receipt Decl. Level: 2 Standard DeclarationDispatch Decl. Level: 2 Standard DeclarationDeclar. File Format: the default value is 2 XML FileReceipt Material No.: <enter receipt number>Dispatch Material No.: <enter dispatch number>In Plants section, choose Add Plant. In Plant field, add the plant number. | Provider of Information is saved.Telephone and fax numbers will be used from the contact person, therefore here leave those fields blank. |  |
| 4 | Create Provider of Information for VAT Group Reporting (Optional) | Back to the Manage Providers of Information view, choose Create and make the following entries in the Create Provider of Information dialog box:Provider of Info: DE_POI_GPCountry of Decl.: DEEntity Type: Select Group of Company CodesLeading Company Code: <for example, 1010>Choose Continue and make the following entries:In the Provider of Information section:Note Name, Street/House Number, Postal Code, City, Phone, and Fax details are automatically retrieved from the company's address data. You don't need to enter this information again.VAT Reg. Number: <for example, VAT12345678>State of Tax Office: <for example, 11 (Berlin)>Tax Number: <for example, 11 (Bucuresti)1234567890>Additional Number: 000Contact Person: <BP role for contact person is SLLSTL (Person Responsible)>Please enter the number for contact person of POI. For example, 1000050In the Basic Settings section:Exchange Rate Type: <for example, M>Receipt Decl. Level: 2Dispatch Decl. Level: 2Declar. File Format: the default value is 2 XML FileReceipt Material No.: <enter receipt>Dispatch Material No.: <enter dispatch number>In the Company Codes section:Choose Create Entry. In the Company Code field, add Company Code, for example, 1020.In the Plants section:Choose Create Entry. In the Plant field, add Plants, for example, 1010 and 1020.If you have configured scope item 1MX, in the Delivering Plants in Intercompany Sales section, choose New Entry. In the Plant field, add Plant, for example, 1010, then choose Save. |  |  |

### Create Intrastat Declarations Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create Intrastat declarations for the POI with the fields required by authorities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Intrastat Specialist. | The SAP Fiori launchpad displays showing personal tiles. |  |
| 2 | Access the SAP Fiori App | Open Manage Intrastat Declarations (/ECRS/RP_EDIT). | The Manage Intrastat Declarations: Overview of Declarations displays. |  |
| 3 | Create Declaration for Dispatch | Make the following entry:Provider of Info: <POI from previous procedure>Choose Create Declaration and make the following entries:Year:2021Month: 4Direction: 2 (Dispatch)You can manually create a Declaration for only one: Receipt or Dispatch.Choose Continue.In the Create Intrastat Declaration: Item Overview view, choose Add (+).Make the following entries:Item Type: <leave blank; it means Standard Item>Business Trans. Type: for example, 11 (Final purchase / Sales)Partner Country: for example, BEPartner VAT Reg. No: <VAT number of the customer>Commodity Code: <product commodity code>Supplem. Unit Qty: <invoiced quantity>Net Weight: <net weight>Invoice Value: <net value>Statistical Value: <statistical value>Country of Origin: for example, DERegion: for example, HamburgNote The national authority publishes the standard codes for regions. The conversion of regions from the SAP internal code to the standard code used in Intrastat are defined.Mode of Transport: for example, 3 RoadDocument: <document number>Item: <item number>Choose Save. | A Declaration is created. |  |
| 4 | Create Declaration for Receipt | In the overview view, make the following entry:Provider of Info.: for example, <the POI from previous procedure>Choose Create Declaration and make the following entries:Year:2021Month: 4Direction: 1(Receipt)You can manually create a Declaration for only one: Receipt or Dispatch.Choose Continue.In Create Intrastat Declaration: Item Overview view, choose Add (+).Make the following entries:Item Type: <leave blank; it means Standard Item>Business Trans. Type: for example, 11 (Final purchase / Sales)Partner Country: for example, DECommodity Code: <product's commodity code>Supplem. Unit Qty: <invoiced quantity>Net Weight: <net weight>Invoice Value: <net value>Statistical Value: <statistical value>Country of Origin: for example, DERegion: for example, 02 HamburgMode of Transport: for example, 3 RoadDocument: <declaration document number>Item: <item number>Choose Save. |  |  |

### Create Intrastat Declarations Automatically (Background Job)

Purpose

In this activity, you schedule a background job which can generate the Intrastat declaration documents based on the billing documents and purchase orders automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Intrastat Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | There are 2 apps available for intrastat declaration creation. Choose Select Dispatches and Customer Returns - Intrastat Declaration (F2507), or Select Receipts and Returns to Supplier - Intrastat Declaration (F2508). | The Application Jobs screen is displayed. |  |
| 3 | Create Declaration by Background Job | In the Application Jobs screen: choose Create.In the Template Selection screen, make the following entries:Job Template: Choose Select Dispatches and Customer Returns, or choose Select Receipts and Returns to Supplier.Choose Step 2.Start Immediately: <select>Choose Step 3.Provider of Info.: for example, the one you created in section [Manage Providers of Information](#unique_16) [page ] 30.Check step name and choose Step 4.Declaration Year: for example, 2021Declaration Month: for example, 4Choose Schedule.Note The Select Receipts and Returns to Supplier - Intrastat Declaration (F2508) app selects invoice receipts in purchasing. The declaration month for these invoice receipts is the calendar month in which invoice receipts occur.If no invoice is received in the same month for a goods receipt, the declaration month for this goods receipt is shifted to the following calendar month.Example 1: The goods and the invoice are received in April. Declaration month is April.Example 2: The goods are received in April and the invoice is not received by the end of April. Declaration month is May.Note While running the App Select Dispatches and Customer Returns - Intrastat Declaration (F2507), the framework for Receipt will also be created, but no values will be filled in;While running the App Select Receipts and Returns to Supplier - Intrastat Declaration (F2508), the framework for Dispatch will also be created, but no values will be filled in. | Job is scheduled and shown in the list. |  |

### Display Intrastat Declarations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the Intrastat declarations which were created manually or generated by background job automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Intrastat Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Intrastat Declarations (/ECRS/RP_EDIT). | The overview screen is displayed. |  |
| 3 | Display Declaration | In the overview, input Provider of Info: for example, create in the last step. Choose Enter.Select the entry, and choose Display.The default maximum number of items is 1000. Please change the number if you want to check more than 1000 items.Select the Item and choose Details to display. | All the declarations under the POI and Item details are displayed. |  |

### Change Intrastat Declaration Item (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can change the Intrastat declaration items that were created in the previous steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Intrastat Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Intrastat Declarations (/ECRS/RP_EDIT). | The overview screen is displayed. |  |
| 3 | Change Declaration | In the overview, input Provider of Info: <the one created in the previous step>.Choose Enter.Select the entry, Choose Change.Items are displayed.Select the Item, Choose Change.Items are displayed.Select the item to correct.Choose Details.From the Change Intrastat Declaration: Change Item view, you can correct data, for example:Business Transaction TypePartner CountryCommodity CodeSupplementary Unit QuantityNet WeightInvoice ValueStatistical ValueTerms of deliveryChoose Save. | All the declarations under the POI and Item details are displayed.Changes are saved. |  |

### Add Intrastat Declaration Item for Existing Declarations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can add declaration items for the existing declarations document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Intrastat Specialist. | The SAP Fiori launchpad screen is displayed. |  |
| 2 | Access App | Open tile Manage Intrastat Declarations (/ECRS/RP_EDIT). | The Manage Intrastat Declarations: Overview of Declarations view displays. |  |
| 3 | Change Declaration | In the overview, input Provider of Info: <for example, the one you created in last step>. Choose Enter.Select the entry, choose Change. Choose Add, then choose Save.Repeat step 3 or 4 of section [Create Intrastat Declarations Manually](#unique_17) [page ] 32 | New item is added. |  |

### Release Intrastat Declarations and Create Declaration File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the Intrastat declarations and create the declaration file to authorities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as an Intrastat Specialist. | The SAP Fiori Launchpad view displays. |  |
| 2 | Access App | Open Manage Intrastat Declarations (/ECRS/RP_EDIT). |  |  |
| 3 | Release Declaration | In the Manage Intrastat Declarations screen:Input Provider of Info: <for example, the one you created in the previous step>.Choose Enter.In the Overview of Declarations view:Double-click the checkbox in the Correct column and choose Release. | Declaration is released. Information of Released by is user ID. | Before releasing the declaration document, please check whether the correct field is selected for the declaration document. If the correct symbol is not marked, you can maintain the missing data for the incorrect declaration items via changing Intrastat Declaration: Item. |
| 4 | Create Declaration File | In the Manage Intrastat Declarations screen:Input Provider of Info: <for example, the one you created in the previous step>.Choose Enter.In the Overview of Declarations view:Select the entry that is Released and choose Create Declaration File.In the Enter Job Title view, make the following entries and choose Continue:Job Title of Contact Person: <Title of person>Job Title of Auth. Signatory: <Title of signatory>Note For downloading the relevant Declaration File, please also refer to the following SAP Knowledge Base Article: 2249454 - ITS Up/Down: Using the WEBGUI File Browser | Declaration File in XML format could be saved in the target folder. |  |

### Cancel Release Intrastat Declarations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can cancel releasing the Intrastat declarations that were released before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as an Intrastat Specialist. | The SAP Fiori Launchpad view displays. |  |
| 2 | Access App | Open Manage Intrastat Declarations (/ECRS/RP_EDIT). | The Overview screen displays. |  |
| 3 | Display all Released Declaration | In the Manage Intrastat Declarations: Overview of Declarations view, make the following entry:Provider of Info: <the one you created in the previous step>.Choose Enter. | All the declarations including those that have been moved to cold area under the POI are displayed. |  |
| 4 | Cancel Release | In the Overview of Declarations view, select the entry that is Released and choose the Cancel Release button. | Release of Declaration is canceled. |  |

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
> Flagged while digesting this document, not verified: Purchasing default step lists Trans. Type Receipts 12 for LP/L/2, while the reference table lists 32 for the same combination (LP, L, item category 2).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-compliance-formats-support-preparation-for-germany-5o6-sap]]
- related-to :: [[04-tax-and-statutory-reporting/vat-tax-calculation-and-reporting-for-germany-55u-test-script-1071]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OL_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 63,540 chars in the whole document
