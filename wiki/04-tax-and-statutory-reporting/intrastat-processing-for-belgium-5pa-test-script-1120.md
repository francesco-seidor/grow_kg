---
id: 04-tax-and-statutory-reporting/intrastat-processing-for-belgium-5pa-test-script-1120
title: Intrastat Processing for Belgium (5PA) - Test Script (5PA_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5PA: Belgian Intrastat declarations, with prerequisites, configuration, roles, apps and test steps."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/belgium-vat-intrastat-and-compliance-formats]
aliases: [5PA_S4CLD2608_BPD_EN_XX]
keywords: ["Belgium VAT, Intrastat and Compliance Formats", intrastat declarations, intrastat configuration, commodity codes, product classification, providers of information, declaration release, customs units of measure, business roles, background job declarations]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5PA_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1120
topic: 04-tax-and-statutory-reporting/belgium-vat-intrastat-and-compliance-formats
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intrastat Processing for Belgium (5PA) - Test Script (5PA_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5PA_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Belgium VAT, Intrastat and Compliance Formats** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Intrastat Processing for Belgium (5PA)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Intrastat Processing for Belgium (5PA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232824775)

[2 Prerequisites 4](#_Toc232824776)

[2.1 System Access 4](#_Toc232824777)

[2.2 Roles 4](#_Toc232824778)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232824779)

[2.4 Business Conditions 6](#_Toc232824780)

[2.5 Preliminary Steps 7](#_Toc232824781)

[2.5.1 Configuration Steps for Intrastat Reporting 7](#_Toc232824782)

[2.5.2 Configuration Activities for Classification 16](#_Toc232824783)

[3 Overview Table 23](#_Toc232824784)

[4 Test Procedures 25](#_Toc232824785)

[4.1 Manage Commodity Codes 25](#_Toc232824786)

[4.2 Classify Products Commodity Codes 26](#_Toc232824787)

[4.3 Reclassify Products Commodity Codes (Optional) 27](#_Toc232824788)

[4.4 Display Classified Products 28](#_Toc232824789)

[4.5 Create Person Responsible for International Trade 29](#_Toc232824790)

[4.6 Manage Providers of Information 31](#_Toc232824791)

[4.7 Create Intrastat Declarations Manually 32](#_Toc232824792)

[4.8 Create Intrastat Declarations Automatically (Background Job) 34](#_Toc232824793)

[4.9 Display Intrastat Declarations 35](#_Toc232824794)

[4.10 Change Intrastat Declaration Item (Optional) 36](#_Toc232824795)

[4.11 Add Intrastat Declaration Item for Existing Declarations (Optional) 38](#_Toc232824796)

[4.12 Release Intrastat Declarations and Create Declaration File 38](#_Toc232824797)

[4.13 Cancel Release Intrastat Declarations (Optional) 40](#_Toc232824798)

## Purpose

Overview

This scope item provides system generated Intrastat declarations covering company codes outside of Belgium with tax registration in Belgium.

Intrastat is a statistical system used to collect information from enterprises regarding trade between European Union (EU) member states.

When the EU was created in 1993 and the initial EU member states became part of the single market, information about their trade with other EU member states could no longer be obtained from customs documents. Intrastat evolved as a replacement to collect information directly from enterprises about dispatches and arrivals of commodities among member states. Today, Intrastat is used for collecting statistics on the trade in goods (services are excluded) between the EU member states.

For more information, we recommend to check the country roadmap for Registration for Indirect Taxation Abroad (RITA). Verify that the company code country and country of tax registration support the RITA solution.

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

Table 1:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Trade Classification Specialist | SAP_BR_TRD_CLS_SPECIALIST | International Trade Classification | SAP_BR_TRD_CLS_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Intrastat Specialist | SAP_BR_INTRASTAT_SPECIALIST | Intrastat | SAP_BR_INTRASTAT_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC | Please ask your system administrator to assign to the testers. |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC | Please ask your system administrator to assign to the testers. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Please ask your system administrator to assign to the testers. |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 |  | See sections Business Conditions. Following the corresponding scope item. For more information about creating master data, see the following Master Data Script documentation. |
| Plant | Plant abroad located in BE |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. You need to at least choose one of following processes, and then complete the process before you are able to start going through this scope item:

Please use the Business partner mentioned in Master Data, Organization Data and Other data to complete the following processes.

| Scope Item | Business Condition |
| --- | --- |
| BD3 - Sales Processing using Third-Party with Shipping Notification | Must be run before this test script. |
| BD9 - Sell from Stock | Must be run before this test script. |
| BDD - Lean Customer Returns | Must be run before this test script. |
| BDH - Sales Order Entry with One-Time Customer | Must be run before this test script. |
| BDK - Sales Processing Using Third-Party Without Shipping Notification | Must be run before this test script. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Must be run before this test script. |
| BDQ - Invoice Correction Process with Debit Memo | Must be run before this test script. |
| BDW - Returnables Processing | Must be run before this test script. |
| BKL - Invoice Correction Process with Credit Memo | Must be run before this test script. |
| BKZ - Sales Order Processing with Invoice List and Collective Billing | Must be run before this test script. |
| BNX - Consumable Purchasing | Must be run before this test script. |
| J45 - Procurement of Direct Materials | Must be run before this test script. |
| BMK - Return to Supplier | Must be run before this test script. |
| BMY - Subcontracting | Must be run before this test script. |
| BKJ - Sales Order Processing with Customer Down Payment | Must be run before this test script. |
| 1MI - Delivery Processing Without Order Reference | Must be run before this test script. |
| 1MP - Quality Management in Sales | Must be run before this test script. |
| 1MX - Intercompany Sales Order Processing – International | Must be run before this test script. |
| 2ET - Sales Order Processing for Non-Stock Material | Must be run before this test script. |

### Preliminary Steps

#### Configuration Steps for Intrastat Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When some prerequisite scope items from SD and MM are activated in customer system, customer may need to maintain the additional configuration by following Configuration Steps before performing testing. You are recommended to configure Configuration Steps before starting to test in SAP S/4HANA Cloud Public Edition system.

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Configure Your Solution | Navigate to Configure Your Solution.Search for apps mentioned in subsequent test steps respectively. Choose the row that appears on the list. On the second screen, you would see the searched app. Choose Configure. |  |  |
| 4 | Define Default Values for Sales | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the Configuration Step are listed in Table 1.Country of Declaration: BEItem Category: CB1I, used in scope item BDW-Returnables ProcessingIntrastat Group: <Leave blank>Business Transaction Type: 11Procedure for Dispatches or Customer Returns: <Leave blank>Procedure for Receipts or Returns to Supplier: <Leave blank>Movement Code: <leave blank>Choose Save. | The default values for Intrastat report are defined for the item categories which are used for the prerequisite of SD or MM scope items. |  |
| 5 | Define Default Values for Purchasing | This configuration depends on the prerequisite scope items which have been activated in customer systems. Check customer scope items first.The reference configurations in the Configuration Step are listed in Table 2.Country of Declaration: BEThe following Purchasing fields combination is used in scope item BMR scheduling Agreements in Procurement.Purchase Document Category : LPurchase Document Type: LPItem Category: 2Business Transaction type: 12Procedure: <Leave blank>Movement Code: <leave blank>Choose Save. | The default values for Intrastat report are defined for the purchasing fields combination which is used for the prerequisite of SD or MM scope items. |  |
| 6 | Define Exclusion of Sales Document Item Categories | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the Configuration Step are listed in following Table 3.Item Category: CBTEChoose Save. | The exclusion of sales document item categories is defined. |  |
| 7 | Define Sales Document Item Categories for Services | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the Configuration Step are listed in Table 4.Item Category: TAD used in scope item 2ET-Sales Order Processing for Non-Stock Material.Choose Save. | The sales document item categories that contain data regarding services are defined. |  |
| 8 | Define Data Selection Control for Sales | Please check the selection logic of sales for the country of declaration to make sure the default selection logic is compliant with the legal regulation of the authority.Changing the Selection Control indicator could result in a different set of documents being reported for the same month and year.Please refer to the following SAP note [2976331](https://me.sap.com/notes/2976331) to understand the influence of the selection logic to the Intrastat report. | The selection logic is compliant with the legal regulation of the authority. |  |
| 9 | Define Data Selection Control for Purchasing | Please check the selection logic of purchasing for the country of declaration to make sure the default selection logic is compliant with the legal regulation of the authority.Changing the Selection Control indicator could result in a different set of documents being reported for the same month and year.Please refer to the following SAP note [2976331](https://me.sap.com/notes/2976331) to understand the influence of the selection logic to the Intrastat report. | The selection logic is compliant with the legal regulation of the authority. |  |
| 10 | Define Default Values for Specific Business Processes in Sales | In this Configuration Step, you can define the default values for the Intra-Community Customer Consignment processes.This configuration depends on the prerequisite customer consignment scope items which have been activated in customer systems.Check customer scope items first.This configuration depends on the prerequisite scope items which have been activated in customer systems. Check customer scope items first.The reference configurations in the Configuration Step are listed in Table 5.Country of Decl.: BEBusiness Process : A1Item Category: CFN, used in scope item 1IU-Customer ConsignmentIntrastat Group: <Leave blank>Business Trans. Type: 12Procedure Dispatches: <Leave blank>Procedure Receipts : <Leave blank>Movement Code : <Leave blank>Choose Save. | The default values for the specific business processes are defined based on the item categories which are used for the prerequisite scope items. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose the Manage Your Solution (F1241) app. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure Your Solution | Navigate to Configure Your Solution.Search for apps mentioned in subsequent test steps respectively. Choose the row that appears on the list. On the second screen, you would see the searched app. Choose Configure. |  |  |
| 4 | Define Default Values for Sales | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the Configuration Activity are listed in Table 1.Country of Declaration: BEItem Category: CB1I, used in scope item BDW-Returnables ProcessingIntrastat Group: <Leave blank>Business Transaction Type: 11Procedure for Dispatches or Customer Returns: <Leave blank>Procedure for Receipts or Returns to Supplier: <Leave blank>Movement Code: <leave blank>Choose Save. | The default values for Intrastat report are defined for the item categories which are used for the prerequisite of SD or MM scope items. |  |
| 5 | Define Default Values for Purchasing | This configuration depends on the prerequisite scope items which have been activated in customer systems. Check customer scope items first.The reference configurations in the Configuration Activity are listed in Table 2.Country of Declaration: BEThe following Purchasing fields combination is used in scope item BMR scheduling Agreements in Procurement.Purchase Document Category : LPurchase Document Type: LPItem Category: 2Business Transaction type: 12Procedure: <Leave blank>Movement Code: <leave blank>Choose Save. | The default values for Intrastat report are defined for the purchasing fields combination which is used for the prerequisite of SD or MM scope items. |  |
| 6 | Define Exclusion of Sales Document Item Categories | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the Configuration Activity are listed in following Table 3.Item Category: CBTEChoose Save. | The exclusion of sales document item categories is defined. |  |
| 7 | Define Sales Document Item Categories for Services | This configuration depends on the prerequisite scope items which have been activated in customer system. Check customer scope items first.The reference configurations in the Configuration Activity are listed in Table 4.Item Category: TAD used in scope item 2ET - Sales Order Processing for Non-Stock Material.Choose Save. | The sales document item categories that contain data regarding services are defined. |  |
| 8 | Define Data Selection Control for Sales | Please check the selection logic of sales for the country of declaration to make sure the default selection logic is compliant with the legal regulation of the authority.Changing the Selection Control indicator could result in a different set of documents being reported for the same month and year.Please refer to the following SAP note [2976331](https://me.sap.com/notes/2976331) to understand the influence of the selection logic to the Intrastat report. | The selection logic is compliant with the legal regulation of the authority. |  |
| 9 | Define Data Selection Control for Purchasing | Please check the selection logic of purchasing for the country of declaration to make sure the default selection logic is compliant with the legal regulation of the authority.Changing the Selection Control indicator could result in a different set of documents being reported for the same month and year.Please refer to the following SAP note [2976331](https://me.sap.com/notes/2976331) to understand the influence of the selection logic to the Intrastat report. | The selection logic is compliant with the legal regulation of the authority. |  |
| 10 | Define Default Values for Specific Business Processes in Sales | In this Configuration Activity, you can define the default values for the Intra-Community Customer Consignment processes.This configuration depends on the prerequisite customer consignment scope items which have been activated in customer systems.Check customer scope items first.This configuration depends on the prerequisite scope items which have been activated in customer systems. Check customer scope items first.The reference configurations in the Configuration Activity are listed in Table 5.Country of Decl.: BEBusiness Process : A1Item Category: CFN, used in scope item 1IU-Customer ConsignmentIntrastat Group: <Leave blank>Business Trans. Type: 12Procedure Dispatches: <Leave blank>Procedure Receipts : <Leave blank>Movement Code : <Leave blank>Choose Save. | The default values for the specific business processes are defined based on the item categories which are used for the prerequisite scope items. |  |

Table 3: Table 1

| Country of Declaration | Item Category | Intrastat Group | Business Transaction Type | Movement Code | Procedure | Prerequisite Scope Item |
| --- | --- | --- | --- | --- | --- | --- |
| BE | TAX |  | 11 |  |  | 2ET-Sales Order Processing for Non-Stock Material |
| BE | CB1I |  | 11 |  |  | BDW-Returnables Processing |
| BE | CBTA |  | 11 |  |  | BJE-Make-to-Order Production – Finished Goods Sales and Final Assembly |
| BE | RENV |  | 21 |  |  | BKP-Customer Returns |
| BE | TAXN |  | 34 |  |  | BDA-Free of Charge Delivery |
| BE | CBTC |  | 11 |  |  | 1YT-Make-to-Order Production with Variant Configuration |
| BE | NLC |  | 11 |  |  | 1P9-Intercompany Stock Transfer |
| BE | CBTQ |  | 11 |  |  | 31Q-Sales Order Processing for Sales Kits |
| BE | LZN |  | 11 |  |  | 3NR-Sales Scheduling Agreements |
| BE | NCC3 |  | 11 |  |  | 5HP-Advanced Intercompany Stock Transfer |
| BE | NLN |  | 31 |  |  | BME-Stock Transfer with Delivery |
| BE | ELCR |  | 21 |  |  | 2TS-Intercompany Stock Transfer Returns |

Table 4: Table 2

| Country of Declaration | Purchasing Document Type | Purchase Document Category | Item Category | Business Transaction Type | Prerequisite Scope Item |
| --- | --- | --- | --- | --- | --- |
| BE | LP | L | 2 | 32 | BMR-Scheduling Agreements in Procurement |
| BE | LPA | L | 0 | 11 | BMR-Scheduling Agreements in Procurement |
| BE | NB2 | F | 5 | 21 | BKP-Customer Returns |
| BE | NB | F | 7 | 11 | 1P9-Intercompany Stock Transfer |
| BE | NBIC | F | 0 | 11 | 5HP-Advanced Intercompany Stock Transfer |
| BE | NBIC | F | 2 | 12 | 5HP-Advanced Intercompany Stock Transfer |
| BE | NBIC | F | 4 | 51 | 5HP-Advanced Intercompany Stock Transfer |
| BE | NBIC | F | 5 | 11 | 5HP-Advanced Intercompany Stock Transfer |
| BE | NBF2 | F | 0 | 21 | 2TS-Intercompany Stock Transfer Returns |

Table 5: Table 3

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

Table 6: Table 4

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

Table 7: Table 5

| Country of Declaration | Business Process | Item Category | Intrastat Group | Business Transaction Type | Procedure Receipts | Procedure Dispatches | Movement Code | Prerequisite Scope Item |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BE | A1 | CB9F |  | 32 |  |  |  | 1IU-Customer Consignment |
| BE | A1 | CFN |  | 32 |  |  |  | 1IU-Customer Consignment |
| BE | A1 | LKN |  | 32 |  |  |  | 4LZ-Sales Scheduling Agreement with Consignment |
| BE | A1 | CB9P |  | 21 |  |  |  | 1IU-Customer Consignment |
| BE | A1 | CPN |  | 21 |  |  |  | 1IU-Customer Consignment |
| BE | A1 | KAN |  | 21 |  |  |  | 4LZ-Sales Scheduling Agreement with Consignment |
| BE | A2 | CB9F |  | 32 |  |  |  | 1IU-Customer Consignment |
| BE | A2 | CFN |  | 32 |  |  |  | 1IU-Customer Consignment |
| BE | A2 | LKN |  | 32 |  |  |  | 4LZ-Sales Scheduling Agreement with Consignment |
| BE | A2 | CB9P |  | 21 |  |  |  | 1IU-Customer Consignment |
| BE | A2 | CPN |  | 21 |  |  |  | 1IU-Customer Consignment |
| BE | A2 | KAN |  | 21 |  |  |  | 4LZ-Sales Scheduling Agreement with Consignment |
| BE | B1 | TAX |  | 12 |  |  |  | 2ET-Sales Order Processing for Non-Stock Material |
| BE | B1 | CB1I |  | 12 |  |  |  | BDW-Returnables Processing |
| BE | B1 | CBTA |  | 12 |  |  |  | BJE-Make-to-Order Production – Finished Goods Sales and Final Assembly |
| BE | B1 | CBTC |  | 12 |  |  |  | 1YT-Make-to-Order Production with Variant Configuration |
| BE | B1 | CBTQ |  | 12 |  |  |  | 31Q-Sales Order Processing for Sales Kits |
| BE | B1 | LZN |  | 12 |  |  |  | 3NR-Sales Scheduling Agreements |

#### Configuration Activities for Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To ensure the Customs Unit of Measure correctly mapping with internal Supplementary Unit of Measure, you may use following Configuration Steps to manage the customs units of measure.

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). Navigate to Configure Your Solution.Search for apps mentioned in subsequent Test Step Name respectively. Choose the row that appears in the list. On the second screen you would see the searched app. Choose Configure. Please proceed ahead with further steps described in the document. | The Manage Your Solution screen is displayed. |  |
| 3 | Define Unit of Measure System | Choose New Entries.Unit of Measure System: UOM_EUDescription: Measure System for EUChoose the line of UOM_EU and click Customs Unit of Measure.Click New Entries:Customs Unit of Measure: For example, KGMUoM Description: kilogramSave the entries.Then choose Mapping for Customs Unit of Measure.Choose New Entries:Customs UoM: For example, KGMMU(Unit of Measure): KGSave the entries.For the Customs Unit of Measure, you can check following table 1 for reference. | The Customs Unit of Measures are maintained.The Customs Unit of Measure are mapped with internal Unit of Measure. |  |
| 4 | Define Numbering Scheme Content for Commodity Codes | Double click the Numbering Scheme Content EU01.Maintain the following entry:Unit of Measure System: Measure System for EU. | The Unit of Measure System is assigned to the Numbering Scheme Content. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Define Unit of Measure System | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Unit of Measure System.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Unit of Measure System screen is displayed. |  |
| 3 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration | The SAP Fiori launchpad is displayed. |  |
| 4 | Define Measure System | Choose New Entries.Unit of Measure System: UOM_EUDescription: Measure System for EUChoose the line of UOM_EU and click Customs Unit of Measure.Click New Entries:Customs Unit of Measure: For example, KGMUoM Description: kilogramSave the entries.Then choose Mapping for Customs Unit of Measure.Choose New Entries:Customs UoM: For example, KGMMU(Unit of Measure): KGSave the entries.For the Customs Unit of Measure, you can check following table 1 for reference. | The Customs Unit of Measures are maintained.The Customs Unit of Measure are mapped with internal Unit of Measure. |  |
| 5 | Open Define Numbering Scheme Content for Commodity Codes | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Numbering Scheme Content for Commodity Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Numbering Scheme Content for Commodity Codes screen is displayed. |  |
| 6 | Log On to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration | The SAP Fiori launchpad is displayed. |  |
| 7 | Define Numbering Scheme Content for Commodity Codes | Double click the Numbering Scheme Content EU01.Maintain the following entry:Unit of Measure System: Measure System for EU. | The Unit of Measure System is assigned to the Numbering Scheme Content. |  |

Table 8: Table 1

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

To start working with the Intrastat application, you need to carry out the setup steps descriped in the previous chapter Prerequisites.

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Commodity Codes](#unique_10) [page ] 25 | Trade Classification Specialist | Manage Commodity Codes (F2516) | Commodity code is created / changed. |
| [Classify Products Commodity Codes](#unique_11) [page ] 26 | Trade Classification Specialist | Classify Products - Commodity Codes (F2151) | Commodity codes are assigned to products. |
| [Reclassify Products Commodity Codes (Optional)](#unique_12) [page ] 27 | Trade Classification Specialist | Reclassify Products - Legal Control (F2391) | Commodity codes are changed for products. |
| [Display Classified Products](#unique_13) [page ] 28 | Trade Classification Specialist | Display Classified Products - International Trade (F3789) | International trade classification data is displayed. |
| [Create Person Responsible for International Trade](#unique_14) [page ] 29 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Person Responsible is saved. |
| [Manage Providers of Information](#unique_15) [page ] 31 | Intrastat Specialist | Manage Providers of Information (/ECRS/POI_EDIT) | Provider of Info. Is created / changed. |
| [Create Intrastat Declarations Manually](#unique_16) [page ] 32 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) |  |
| [Create Intrastat Declarations Automatically (Background Job)](#unique_17) [page ] 34 | Intrastat Specialist | Select Dispatches and Customer Returns - Intrastat Declaration (F2507) or Select Receipts and Returns to Supplier - Intrastat Declaration (F2508) | Job is scheduled and shown in the list. |
| [Display Intrastat Declarations](#unique_18) [page ] 35 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | All the declarations under the POI and Item details display. |
| [Change Intrastat Declaration Item (Optional)](#unique_19) [page ] 36 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | Changes are saved. |
| [Add Intrastat Declaration Item for Existing Declarations (Optional)](#unique_20) [page ] 38 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | New item is added. |
| [Release Intrastat Declarations and Create Declaration File](#unique_21) [page ] 38 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | Declaration File could be saved in the target folder. |
| [Cancel Release Intrastat Declarations (Optional)](#unique_22) [page ] 40 | Intrastat Specialist | Manage Intrastat Declarations (/ECRS/RP_EDIT) | Release of Declaration is canceled |

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
| 3 | Enter No. Scheme Content | In the overview screen: make the following entries and choose Go :No. Scheme Content: EU01 Commodity Codes for European Union: Combined Nomenclature of the European Union (EU01) |  |  |
| 4 | Enter Commodity Codes details | Choose Add.Make the following entries and choose Enter:Commodity Code: for example, 84713000Official Description: <free text>Valid From: for example, 2016.01.01Valid To: for example, 9999.12.31Choose Save. | Commodity code is saved. |  |

### Classify Products Commodity Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you classify the products with the commodity code you created in previous step.

Procedure

Table 9:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the tile Classify Products - Commodity Codes (F2151). | The Classify Products - Commodity Codes displays. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Valid On: for example: 2016.01.01 (This date should be in the valid period of the Commodity code you want to use)Numbering Scheme: Combined Nomenclature of the European Union (EU01)Product (Optional): for example: TG11 | Product entry is displayed.If the product has already been assigned commodity code, it won't display in this tile. To maintain this one, tile Reclassify Products Commodity Codes should be used. |  |
| 4 | Classify Product | In the Products area, select the product entry, choose Classify: make the following entries :Commodity Code: <Commodity Code created inprevious step>Classification From/To: for example, <current date>Remark: <your remark>Choose Save. | Classification is saved. |  |

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
| 2 | Access App | Open tile Reclassify Products - Commodity Codes (F2152). | The Reclassify Products - Commodity Codes screen is displayed. |  |
| 3 | Enter Filters | On the Reclassify Products - Commodity Codes screen, make the following entries and choose Go:Valid On: for example, 2016.01.01 (This date should be in the valid period of the Commodity code you want to use.)Numbering Scheme: Combined Nomenclature of the European Union (EU01)Product (Optional): for example, TG10 | Product entry displays. |  |
| 4 | Reclassify Product | In the Products area, choose the product entry, choose Reclassify.Make the following entries:Commodity Code: another commodity codeClassification From/To: for example, 2016.01.01 / 9999.12.31Remark: <your remark>Choose Save. | Reclassification is saved. |  |

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
| 3 | Enter Filters | In the Display Classified Products view, make the following entries and choose Go:Product: <Enter a Product, for example, TG11> | The entered product displays. |  |
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
| 3 | Create a BP Person | Choose Person. | The Create Person screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Leave blank>Create in BP role: Person Resp. Intl Trade. The BP role is SLLSTL. |  |  |
| 5 | Enter Address Data | On the Address tab in the Name section, enter the following data:Title: Mr. or Ms.First Name: <First Name>Last Name: <Last Name> |  |  |
| 6 | Enter Standard Address | On the Address tab in the Standard Address section, enter the following data:Street/House number: <free text>Postal Code/City: <Enter the postal code of Person Responsible>Country: <Enter the country of Person Responsible>Region: <Enter the region of Person Responsible>Language: ENChoose Save. |  |  |
| 7 | Enter Communication Data | On the Address tab in the Communication section, enter the following data:Telephone: <Telephone number of the person responsible>Cell Phone: <Cell Phone number of the person responsible>Fax: <Fax number of the person responsible>E-Mail Address: <E-mail address of the person responsible> |  |  |
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

| Test Step # | Test Step Name | Instruction | Expected Resul | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Intrastat Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Providers of Information (/ECRS/POI_EDIT). | The overview screen is displayed. |  |
| 3 | Create Provider of Info | In the Overview view, choose Create and make the following entries:Provider of Info: BE_POICtry of Declaration: BECompany Code: <your company code>Choose Continue and make the following entries:In Provider of Information section:Note Name, Street/House Number, Postal Code, City, Phone, Fax are automatically reused from the address data for company code. You do not need to enter these information again.State of Tax Office: <for example, 11 (Berlin)>Tax Number: <for example, 11 (Bucuresti)1234567890>Additional Number: 000Contact Person: <BP role for contact person is SLLSTL (Person Responsible).>Please enter the number for contact person of POI. For example, 1000050In Basic Settings section:Exchange Rate Type: for example, MReceipt Decl. Level: 2Dispatch Decl. Level: 2Declar. File Format: for example, 3Authentification code: <free text>In Plants section, choose Add Plant. In Plant field, add Plant, for example, 2510.If you have configured scope item 1MX, in Delivery Plants in Intercompany Sales section, choose Add Delivering Plant.Choose Save. | Provider of Information is saved. |  |

### Create Intrastat Declarations Manually

Purpose

In this activity, you create Intrastat declarations for the POI with the fields required by authorities.

|  |
| --- |
| Note The required fields for individual country/region authorities may be different than provided for this procedure. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Intrastat Specialist. | The SAP Fiori launchpad displays showing personal tiles. |  |
| 2 | Access the SAP Fiori App | Open Manage Intrastat Declarations (/ECRS/RP_EDIT). | The Manage Intrastat Declarations: Overview of Declarations displays. |  |
| 3 | Create Declaration for Dispatch | Make the following entry:Provider of Info: <POI from previous procedure>Choose Create Declaration and make the following entries:Year: 2016Month: 9Direction: 2 (Dispatch)You can manually create a Declaration for only one: Receipt or Dispatch.Choose Continue.In the Create Intrastat Declaration: Item Overview view, choose Add (+).Make the following entries:Item Type: <leave blank; it means Standard Item>Business Trans. Type: for example, 1 Final Purchase/Sale (exclude 2, 7 and 8)Partner Country: for example HUPartner VAT Reg. No.: for example, HU123456789.Commodity Code: <product commodity code>Supplem. Unit Qty: <invoiced quantity>Net Weight: <net weight>Invoice Value: <net value>Statistical Value: <statistical value>Country of Origin: For example, FRNote The national authority publishes the standard codes for regions. The conversion of regions from the SAP internal code to the standard code used in Intrastat are defined.Region: for example, 3 Brussels regionDocument: <document number>Item: <item number>Choose Save. | A Declaration is created. |  |
| 4 | Create Declaration for Receipt | In the overview view, make the following entry:Provider of Info.: for example, <the POI from previous procedure>Choose Create Declaration and make the following entries:Year: 2016Month: 9Direction: 1(Receipt)You can manually create a Declaration for only one: Receipt or Dispatch.Choose Continue.In Create Intrastat Declaration: Item Overview view, choose Add (+).Make the following entries:Item Type: for example, <leave blank; it means Standard Item>Business Trans. Type: for example, 1 Final Purchase/Sale (exclude 2, 7 and 8)Partner Country: <country>Commodity Code: <product's commodity code>Supplem. Unit Qty: <invoiced quantity>Net Weight: <net weight>Invoice Value: <net value>Region: <country's region> for example, 02 HamburgRegion: for example, 3 Brussels regionCountry of Origin: for example, DEDocument: <declaration document number>Item: <item number>Choose Save. |  |  |

### Create Intrastat Declarations Automatically (Background Job)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job which can generate the Intrastat declaration documents based on the billing documents and purchase orders automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Intrastat Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | There are 2 apps available for intrastat declaration creation. Choose Select Dispatches and Customer Returns - Intrastat Declaration (F2507), or Select Receipts and Returns to Supplier - Intrastat Declaration (F2508). | The Application Jobs screen is displayed. |  |
| 3 | Create Declaration by Background Job | In the Application Jobs screen: choose Create.In the Template Selection screen, make the following entries:Job Template: Choose Select Dispatches and Customer Returns, or choose Select Receipts and Returns to Supplier.Choose Step 2.Start Immediately: <select>Choose Step 3.Provider of Info.: for example, the one you created in section [Manage Providers of Information](#unique_15) [page ] 31.Check step name and choose Step 4.Declaration Month: for example, 2Choose Schedule.Note The Select Receipts and Returns to Supplier - Intrastat Declaration (F2508) app selects goods receipts in purchasing. The declaration month for these goods receipts is the calendar month in which they occur. If no invoice is received in the same month for a goods receipt, the declaration month for this goods receipt is shifted to the following calendar month.Example 1: The goods and the invoice are received in April. Declaration month is April.Example 2: The goods are received in April and the invoice is not received by the end of April. Declaration month is May.Note While running the App Select Dispatches and Customer Returns - Intrastat Declaration (F2507), the framework for Receipt will also be created, but no values will be filled in;While running the App Select Receipts and Returns to Supplier - Intrastat Declaration (F2508), the framework for Dispatch will also be created, but no values will be filled in. | Job is scheduled and shown in the list. |  |

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
| 2 | Access App | Choose Manage Intrastat Declarations (/ECRS/RP_EDIT). | The Manage Intrastat Declarations: Overview of Declarations screen is displayed. |  |
| 3 | Display Declaration | In the Manage Intrastat Declarations: Overview of Declarations screen, input Provider of Info: for example, create in the last step. Choose Enter.In the Declaration Month section:Current Month: <select>Select the entry, and choose Display.Note You can access your personal settings and adjust your preferences by clicking the Extras button on the menu bar or by pressing the F6 keyboard shortcut.Note The default maximum number of items is 1000. Please change the number if you want to check more than 1000 items.Select the Item and choose Details to display.Note If you implement a cloud BAdI in preliminary steps, please check if the data is correctly displayed according to the customs logic. | All the declarations under the POI and Item details are displayed. |  |

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
| 3 | Change Declaration | In the overview, input Provider of Info: <the one created in the previous step>.Choose Enter.Select the entry, Choose Change.Items are displayed.Select the Item, Choose Change.Items are displayed.Select the item to correct.Choose Details.From the Change Intrastat Declaration: Item view, you can correct data, for example:Business Trans. TypePartner CountryCommodity CodeNet WeightInvoice ValueChoose Save. | All the declarations under the POI and Item details are displayed.Changes are saved. |  |

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
| 1 | Log On | Log onto the SAP Fiori launchpad as an Intrastat Specialist. | The SAP Fiori launchpad screen is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Intrastat Declarations (/ECRS/RP_EDIT). | The Manage Intrastat Declarations: Overview of Declarations view displays. |  |
| 3 | Change Declaration | In the overview, input Provider of Info: <for example, the one you created in last step>. Choose Enter.Select the entry, choose Change. Choose Add, then choose Save.Repeat step 3 or 4 of section [Create Intrastat Declarations Manually](#unique_16) [page ] 32. | New item is added. |  |

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
| 2 | Access App | Open Manage Intrastat Declarations (/ECRS/RP_EDIT). | The Manage Intrastat Declarations: Overview of Declarations view appears. |  |
| 3 | Release Declaration | In the Manage Intrastat Declarations: Overview of Declarations screen:Input Provider of Info: <for example, the one you created in the previous step>Choose Enter.Choose Overview of Declarations.Choose the Declaration you would like to release, then choose Release. | Declaration is released. Information of Released by is user ID. | Before releasing the Intrastat declaration, please check whether the Declaration Correct checkbox is selected for the Intrastat declaration.For correcting the Intrastat declaration, you can maintain the missing data for the incorrect declaration items on the item detail screen for single items or by using the Mass Change function on the item overview screen for multiple items. |
| 4 | Create Declaration File | In the Manage Intrastat Declarations screen:Input Provider of Info: <for example, the one you created in the previous step>.Choose Enter.In the Overview of Declarations view:Select the entry that is Released and choose Create Declaration File.Note For downloading the relevant Declaration File, please also refer to the following SAP Knowledge Base Article :2249454 - ITS Up/Down: Using the WEBGUI File Browser | Declaration File in XML format could be saved in the target folder. |  |

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
| 3 | Display all Released Declaration | In the Manage Intrastat Declarations: Overview of Declarations view, make the following entry:Provider of Info:<the one you created in the previous step>.Choose Enter. | All the declarations including those that have been moved to cold area under the POI are displayed. |  |
| 4 | Cancel Release | In the Overview of Declarations view, select the entry that is Released and choose Cancel Release button. | Release of Declaration is canceled. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-belgium-5p9-test-script-111]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-vat-tax-calculation-and-reporting-for-belgium-5is-1105]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5PA_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 64,120 chars in the whole document
