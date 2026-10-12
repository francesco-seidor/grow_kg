---
id: 13-quality-ehs-and-compliance/test-script-restricted-party-screening-with-sap-watch-list-screening-1
title: "Test Script: Restricted Party Screening with SAP Watch List Screening (1WE_AE) (1WE_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1WE (AE): configuring and testing sanctioned party screening of BPs, sales and purchasing documents via SAP Watch List Screening."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/restricted-party-screening]
aliases: [1WE_S4CLD2608_BPD_EN_AE]
keywords: [Restricted Party Screening with SAP Watch List Screening, watch list screening, restricted party screening, trade compliance configuration, screening hit resolution, business partner screening, sales order screening, purchase order screening, postprocessing jobs, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WE_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-770
topic: 13-quality-ehs-and-compliance/restricted-party-screening
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Restricted Party Screening with SAP Watch List Screening (1WE_AE) (1WE_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WE_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Restricted Party Screening with SAP Watch List Screening** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Restricted Party Screening with SAP Watch List Screening (1WE_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847729)

[2 Prerequisites 4](#_Toc232847730)

[2.1 Additional Manual Configuration 4](#_Toc232847731)

[2.2 System Access 4](#_Toc232847732)

[2.3 Roles 4](#_Toc232847733)

[2.4 Master Data, Organizational Data, and Other Data 6](#_Toc232847734)

[2.5 Preliminary Steps 7](#_Toc232847735)

[2.5.1 Maintain Condition Record 7](#_Toc232847736)

[2.5.2 Configuration Activities with DEMO Data 8](#_Toc232847737)

[2.5.3 Configuration Activities Without DEMO Data 12](#_Toc232847738)

[3 Overview Table 18](#_Toc232847739)

[4 Test Procedures 20](#_Toc232847740)

[4.1 Create Business Partner 20](#_Toc232847741)

[4.2 Schedule Business Partners Screening for SAP Watch List Screening Integration 21](#_Toc232847742)

[4.3 Resolve Screening Hit 22](#_Toc232847743)

[4.4 Schedule Postprocessing for SAP Watch List Screening Integration 23](#_Toc232847744)

[4.5 Outbound Process 25](#_Toc232847745)

[4.5.1 Screening for Sales Order 25](#_Toc232847746)

[4.5.1.1 Sales Order Creation using BP With Sanctioned Address 25](#_Toc232847747)

[4.5.1.1.1 Create Sales Order 25](#_Toc232847748)

[4.5.1.1.2 Create Delivery (Optional) 27](#_Toc232847749)

[4.5.1.2 Sales Order Creation with Manual Changed Address 28](#_Toc232847750)

[4.5.1.2.1 Create Sales Order with Sanctioned Destination 28](#_Toc232847751)

[4.5.1.2.2 Create Delivery While Decision Pending (Optional) 30](#_Toc232847752)

[4.5.1.2.3 Resolve Screening Hit 31](#_Toc232847753)

[4.5.1.2.4 Schedule Postprocessing for SAP Watch List Screening Integration 32](#_Toc232847754)

[4.5.1.2.5 Create Delivery 34](#_Toc232847755)

[4.5.2 Screening for Sales Order Without Charge (Optional) 35](#_Toc232847756)

[4.5.3 Screening for Sales Contract (Optional) 35](#_Toc232847757)

[4.5.4 Screening for Sales Scheduling Agreement (Optional) 35](#_Toc232847758)

[4.5.5 Screening for Sales Quotation (Optional) 35](#_Toc232847759)

[4.6 Inbound Process 35](#_Toc232847760)

[4.6.1 Screening for Purchase Order 36](#_Toc232847761)

[4.6.1.1 Purchase Order Creation using BP With Sanctioned Address 36](#_Toc232847762)

[4.6.1.1.1 Create Purchase Order 36](#_Toc232847763)

[4.6.1.1.2 Display Purchase Order 37](#_Toc232847764)

[4.6.2 Screening for Purchase Contract (Optional) 38](#_Toc232847765)

[4.6.3 Screening for Purchase Scheduling Agreement (Optional) 38](#_Toc232847766)

[4.6.4 Screening for Purchase Requisition (Optional) 38](#_Toc232847767)

## Purpose

Overview

SAP Watch List Screening is a standalone public cloud solution delivered on the SAP Business Technology Platform (SAP BTP) to perform sanctioned party list screening of business partners and relevant documents, such as sales orders and deliveries, as part of international trade compliance.

This scope item provides connection between SAP S/4HANA Cloud Public Edition and SAP Watch List Screening and enables screening against the organization's denied party lists. Self-service configuration allows organizations to define applicable regulations.

You must have a license for SAP Watch List Screening.

|  |
| --- |
| Caution If you are activating the Restricted Party Screening with SAP Watch List Screening (1WE) check in SAP S/4HANA Cloud Public Edition for international trade, it is not possible to activate the Compliance Management with SAP Global Trade Services (24J). Trade Compliance checks are to be done exclusively in either SAP S/4HANA Cloud Public Edition or Global Trade Services system. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/3e62ec0fae2ec97af7032e43f9415c19)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition system | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Business Technology Platform (SAP BTP) | Accessible via Fiori Launchpad redirecting. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Please ask your system administrator to assign to the testers. |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners | SAP_BR_BUPA_MASTER_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Administrator - International Trade | SAP_BR_ADMINISTRATOR_SLL | International Trade Administration | SAP_BR_ADMINISTRATOR_SLL | Please ask your system administrator to assign to the testers. |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | Please ask your system administrator to assign to the testers. |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | Please ask your system administrator to assign to the testers. |
| Trade Compliance Specialist | SAP_BR_TRD_CMPLNC_SPECIALIST | International Trade Compliance | SAP_BR_TRD_CMPLNC_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Screening Specialist |  |  |  | Note Please refer to this [link](http://help.sap.com/wls) and refer to the Chapter 6 User Management in the file Administration Guide for SAP Watch List Screening to create test users. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. |  |
| Sold-to Party | 33100050 | Foreign Customer 50 |  |
| Ship-to Party | 33100050 | Foreign Customer 50 |  |
| Supplier | 33300002 | Domestic Supplier 2 |  |
| Shipping Point | 3310 |  |  |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Preliminary Steps

#### Maintain Condition Record

Purpose

To ensure Sales Orders with international ship-to-party can be created successfully, corresponding Condition Record needs to be maintained.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Pricing Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Navigate | Open the app Set Material Prices - Sales (VK12). | The Change Condition Records screen appears. |  |
| 3 | Choose Condition Type | On the screen Change Condition Records, maintain the information below:Condition Type : <input country-specific condition type>, for example, TTX1 for DEChoose Enter, and in the dialog box, select Export Taxes and choose Choose. |  |  |
| 4 | Maintain Condition Record | On the next screen, maintain the information below:Departure Ctry/Reg.: AEThen choose Execute.On the next screen, maintain a new entry with information below:- Dest. Country/Region: RU- TaxCl1Cust.: 1- Tax Cl. Mat: 1- Valid From.: For example, <current date>- Valid To.: 12/31/9999- Tax Code: <Please select appropriate tax code, for example, A0 for DE>Choose Save to save the change.Note The above countries/regions are only used as examples to showcase how to maintain condition records. Please adjust accordingly based on your business requirement. | Condition Record has been maintained |  |

#### Configuration Activities with DEMO Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the scope item was activated with Demo Data. System has pre-delivered Demo Data configuration and you still need to maintain the following configurations by SSCUI before performing testing.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). Navigate to Configure Your Solution.Search for apps mentioned in subsequent Test Steps respectively. Choose the row that appears in the list. On the second screen you would see the searched app. Choose Configure. Please proceed ahead with further steps described in the document. |  | The Manage Your Solution screen appears. |
| 3 | Activate Sales Documents | Sales Document Type: ORTrade Compliance: <Flag should be checked>Choose Save.Note Activate the relevant document types for trade compliance check according to your business requirements. Business documents supported by Watch List Screening for outbound process are listed:Sales OrdersSales Orders Without ChargeSales ContractsSales Scheduling AgreementsSales Quotations | Sales order type OR is activated for Trade Compliance. |  |
| 4 | Activate Checks for Purchasing Documents | Purchasing Document Type: NBTrade Compliance: <Flag should be checked>Choose Save.Note Activate the relevant document types for trade compliance check according to your business requirements. Business documents supported by Watch List Screening for inbound process are listed:Purchase OrdersPurchase ContractsPurchase Scheduling AgreementsPurchase Requisitions | Purchase order type NB is activated for Trade Compliance. |  |
| 5 | Activate Delivery Documents | For outbound processing, double-click Outbound Deliveries in the Dialogue Structure pane.Delivery Type: LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type LF is activated for Trade Compliance. |  |
|  |  | For inbound processing, double-click Inbound Deliveries in the Dialogue Structure pane.Delivery Type: ELTrade Compliance: <Flag should be checked>Choose Save. | Delivery type EL is activated for Trade Compliance. |  |
| 6 | Activate Checks for Company Codes | Company Code: 3310Watch List Screening: <Flag should be checked> | Company Code 3310 is activated for SAP Watch List Screening. |  |
| 7 | Watch List Screening: Control Settings for Legal Regulation | Legal Regulation: ITR03BP Status: <Flag should be checked> | Legal regulation ITR03 is defined as to check the screening status of business partners | Note Before checking this flag, make sure you have scheduled below jobs regularly to make the screening status on business partners and purchasing / sales documents reliable and updated.(the recommended recurrence pattern is to schedule it hourly)(the recommended recurrence pattern is to schedule it daily)Otherwise, deselect this flag and the system will not check the screening status on BP master data and will send the address to SAP Watch List Screening for screening when purchasing and sales documents are created and changed. |
| 8 | Business Partner Roles for SAP Watchlist Screening | Choose New Entries.BP Role: FLCU01BP Role: FLVN01Choose Save. | Business Partner roles FLCU01 and FLVN01 is added. These roles will then be screened by SAP Watch List Screening | Note The BP roles FLCU01 and FLVN01 are only used as examples. Please adjust accordingly based on your business requirement. |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Configuration Activity | Go to the Business Processes Configuration app.Search for apps mentioned in subsequent Test Steps respectively.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The related configuration activities screen displays. |  |
| 3 | Activate Sales Documents | Sales Document Type: ORTrade Compliance: <Flag should be checked>Choose Save.Note Activate the relevant document types for trade compliance check according to your business requirements. Business documents supported by Watch List Screening for outbound process are listed:Sales OrdersSales Orders Without ChargeSales ContractsSales Scheduling AgreementsSales Quotations | Sales order type OR is activated for Trade Compliance. |  |
| 4 | Activate Checks for Purchasing Documents | Purchasing Document Type: NBTrade Compliance: <Flag should be checked>Choose Save.Note Activate the relevant document types for trade compliance check according to your business requirements. Business documents supported by Watch List Screening for inbound process are listed:Purchase OrdersPurchase ContractsPurchase Scheduling AgreementsPurchase Requisitions | Purchase order type NB is activated for Trade Compliance. |  |
| 5 | Activate Delivery Documents | For outbound processing, double-click Outbound Deliveries in the Dialogue Structure pane.Delivery Type: LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type LF is activated for Trade Compliance. |  |
|  |  | For inbound processing, double-click Inbound Deliveries in the Dialogue Structure pane.Delivery Type: ELTrade Compliance: <Flag should be checked>Choose Save. | Delivery type EL is activated for Trade Compliance. |  |
| 6 | Activate Checks for Company Codes | Company Code: 3310Watch List Screening: <Flag should be checked> | Company Code 3310 is activated for SAP Watch List Screening. |  |
| 7 | Watch List Screening: Control Settings for Legal Regulation | Legal Regulation: ITR03BP Status: <Flag should be checked> | Legal regulation ITR03 is defined as to check the screening status of business partners. | Note Before checking this flag, make sure you have scheduled below jobs regularly to make the screening status on business partners and purchasing / sales documents reliable and updated.(the recommended recurrence pattern is to schedule it hourly)(the recommended recurrence pattern is to schedule it daily)Otherwise, deselect this flag and the system will not check the screening status on BP master data and will send the address to SAP Watch List Screening for screening when purchasing and sales documents are created and changed. |
| 8 | Business Partner Roles for SAP Watchlist Screening | Choose New Entries.BP Role: FLCU01BP Role: FLVN01Choose Save. | Business Partner roles FLCU01 and FLVN01 is added. These roles will then be screened by SAP Watch List Screening. | Note The BP roles FLCU01 and FLVN01 are only used as examples. Please adjust accordingly based on your business requirement. |

#### Configuration Activities Without DEMO Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the scope item was activated without Demo Data. System has no pre-delivered Demo Data configuration and you will need to maintain all the following configurations by Configuration Activities before performing testing.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). Navigate to Configure Your Solution.Search for apps mentioned in subsequent Test Steps respectively. Choose the row that appears in the list. On the second screen you would see the searched app. Choose Configure. Please proceed ahead with further steps described in the document. | The Manage Your Solution screen appears. |  |
| 3 | Activate Sales Documents | Sales Document Type: ORTrade Compliance: <Flag should be checked>Choose Save.Note Activate the relevant document types for trade compliance check according to your business requirements. Business documents supported by Watch List Screening for outbound process are listed:Sales OrdersSales Orders Without ChargeSales ContractsSales Scheduling AgreementsSales Quotations | Sales order type OR is activated for Trade Compliance. |  |
| 4 | Activate Checks for Purchasing Documents | Purchasing Document Type: NBTrade Compliance: <Flag should be checked>Choose Save.Note Activate the relevant document types for trade compliance check according to your business requirements. Business documents supported by Watch List Screening for inbound process are listed:Purchase OrdersPurchase ContractsPurchase Scheduling AgreementsPurchase Requisitions | Purchase order type NB is activated for Trade Compliance. |  |
| 5 | Activate Delivery Documents | For outbound processing, double-click Outbound Deliveries in the Dialogue Structure pane.Delivery Type: LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type LF is activated for Trade Compliance. |  |
|  |  | For inbound processing, double-click Inbound Deliveries in the Dialogue Structure pane.Delivery Type: ELTrade Compliance: <Flag should be checked>Choose Save. | Delivery type EL is activated for Trade Compliance. |  |
| 6 | Activate Checks for Company Codes | Company Code: 3310Watch List Screening: <Flag should be checked> | Company Code 3310 is activated for SAP Watch List Screening. |  |
| 7 | Define Trade Compliance Legal Regulations | Choose New Entries.Legal Regulation: ITR03Description: Legal Regulation for SAP Watch List ScreeningTrade Regulation Area: 03 Watch List ScreeningChoose Save. | Legal regulation ITR03 is defined. |  |
| 8 | Activate Legal Regulations for SAP Watch List Screening | Choose New Entries.Legal Regulation: ITR03Country/Region:AEChoose Save. | Legal regulation ITR03 is activated for country/region AE. |  |
| 9 | Watch List Screening: Control Settings for Legal Regulation | Legal Regulation: ITR03BP Status: <Flag should be checked> | Legal regulation ITR03 is defined as to check the screening status of business partners. | Note Before checking this flag, make sure you have scheduled below jobs regularly to make the screening status on business partners and purchasing / sales documents reliable and updated.(the recommended recurrence pattern is to schedule it hourly)(the recommended recurrence pattern is to schedule it daily)Otherwise, deselect this flag and the system will not check the screening status on BP master data and will send the address to SAP Watch List Screening for screening when purchasing and sales documents are created and changed. |
| 10 | Business Partner Roles for SAP Watchlist Screening | Choose New Entries.BP Role: FLCU01BP Role: FLVN01Choose Save. | Business Partner roles FLCU01 and FLVN01 is added. These roles will then be screened by SAP Watch List Screening. | Note The BP roles FLCU01 and FLVN01 are only used as examples. Please adjust accordingly based on your business requirement. |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Configuration Activity | Go to the Business Processes Configuration app.Search for apps mentioned in subsequent Test Steps respectively.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The related configuration activities screen displays. |  |
| 3 | Activate Sales Documents | Sales Document Type: ORTrade Compliance: <Flag should be checked>Choose Save.Note Activate the relevant document types for trade compliance check according to your business requirements. Business documents supported by Watch List Screening for outbound process are listed:Sales OrdersSales Orders Without ChargeSales ContractsSales Scheduling AgreementsSales Quotations | Sales order type OR is activated for Trade Compliance. |  |
| 4 | Activate Checks for Purchasing Documents | Purchasing Document Type: NBTrade Compliance: <Flag should be checked>Choose Save.Note Activate the relevant document types for trade compliance check according to your business requirements. Business documents supported by Watch List Screening for inbound process are listed:Purchase OrdersPurchase ContractsPurchase Scheduling AgreementsPurchase Requisitions | Purchase order type NB is activated for Trade Compliance. |  |
| 5 | Activate Delivery Documents | For outbound processing, double-click Outbound Deliveries in the Dialogue Structure pane.Delivery Type: LFTrade Compliance: <Flag should be checked>Choose Save. | Delivery type LF is activated for Trade Compliance. |  |
|  |  | For inbound processing, double-click Inbound Deliveries in the Dialogue Structure pane.Delivery Type: ELTrade Compliance: <Flag should be checked>Choose Save. | Delivery type EL is activated for Trade Compliance. |  |
| 6 | Activate Checks for Company Codes | Company Code: 3310Watch List Screening: <Flag should be checked> | Company Code 3310 is activated for SAP Watch List Screening. |  |
| 7 | Define Trade Compliance Legal Regulations | Choose New Entries.Legal Regulation: ITR03Description: Legal Regulation for SAP Watch List ScreeningTrade Regulation Area: 03 Watch List ScreeningChoose Save. | Legal regulation ITR03 is defined. |  |
| 8 | Activate Legal Regulations for SAP Watch List Screening | Choose New Entries.Legal Regulation: ITR03Country/Region:AEChoose Save. | Legal regulation ITR03 is activated for country/region AE. |  |
| 9 | Watch List Screening: Control Settings for Legal Regulation | Legal Regulation: ITR03BP Status: <Flag should be checked> | Legal regulation ITR03 is defined as to check the screening status of business partners. | Note Before checking this flag, make sure you have scheduled below jobs regularly to make the screening status on business partners and purchasing / sales documents reliable and updated.(the recommended recurrence pattern is to schedule it hourly)(the recommended recurrence pattern is to schedule it daily)Otherwise, deselect this flag and the system will not check the screening status on BP master data and will send the address to SAP Watch List Screening for screening when purchasing and sales documents are created and changed. |
| 10 | Business Partner Roles for SAP Watchlist Screening | Choose New Entries.BP Role: FLCU01BP Role: FLVN01Choose Save. | Business Partner roles FLCU01 and FLVN01 is added. These roles will then be screened by SAP Watch List Screening. | Note The BP roles FLCU01 and FLVN01 are only used as examples. Please adjust accordingly based on your business requirement. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Business Partner](#unique_11) [page ] 20 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Customer and Supplier Master Data is created. |
| [Schedule Business Partners Screening for SAP Watch List Screening Integration](#unique_12) [page ] 21 | Administrator - International Trade | Schedule Business Partners Screening - Watch List Screening (F8016) | Job is scheduled. |
| [Resolve Screening Hit](#unique_13) [page ] 22 | Screening Specialist | Review Screening Hits | Screening decision is made for suspicious business partner. |
| [Schedule Postprocessing for SAP Watch List Screening Integration](#unique_14) [page ] 23 | Administrator - International Trade | Schedule Postprocessing - Watch List Screening (F3052) | Job is scheduled. |
| Outbound Process |  |  |  |
| Screening for Sales Order |  |  |  |
| Sales Order Creation using BP With Sanctioned Address |  |  |  |
| [Create Sales Order](#unique_15) [page ] 25 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Create Delivery (Optional)](#unique_16) [page ] 27 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery creation fails as sales order is blocked by SAP Watch List Screening. |
| Sales Order Creation with Manual Changed Address |  |  |  |
| [Create Sales Order with Sanctioned Destination](#unique_17) [page ] 28 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Create Delivery While Decision Pending (Optional)](#unique_18) [page ] 30 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery creation fails as sales order is blocked by SAP Watch List Screening. |
| [Resolve Screening Hit](#unique_19) [page ] 31 | Screening Specialist | Review Screening Hits | Screening decision is made for suspicious business partner. |
| [Schedule Postprocessing for SAP Watch List Screening Integration](#unique_20) [page ] 32 | Administrator - International Trade | Schedule Postprocessing - Watch List Screening (F3052) | Job is scheduled. |
| [Create Delivery](#unique_21) [page ] 34 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Screening for Sales Order Without Charge (Optional)](#unique_22) [page ] 35 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) | Sales order without charge is created. |
| [Screening for Sales Contract (Optional)](#unique_23) [page ] 35 | Internal Sales Representative | Manage Sales Contracts (F1851) | Sales contract is created. |
| [Screening for Sales Scheduling Agreement (Optional)](#unique_24) [page ] 35 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Sales scheduling agreement is created. |
| [Screening for Sales Quotation (Optional)](#unique_25) [page ] 35 | Internal Sales Representative | Manage Sales Quotations (F1852) | Sales quotation is created. |
| Inbound Process |  |  |  |
| Screening for Purchase Order |  |  |  |
| Purchase Order Creation using BP With Sanctioned Address |  |  |  |
| [Create Purchase Order](#unique_26) [page ] 36 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase Order is created. |
| [Display Purchase Order](#unique_27) [page ] 37 | Purchaser | Display Purchase Order - Advanced (ME23N) | Puchase Order is on-hold and blocked by SAP Watch List Screening. |
| [Screening for Purchase Contract (Optional)](#unique_28) [page ] 38 | Purchaser | Manage Purchase Contracts (F1600A) | Purchase contract is created. |
| [Screening for Purchase Scheduling Agreement (Optional)](#unique_29) [page ] 38 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Purchase scheduling agreement is created. |
| [Screening for Purchase Requisition (Optional)](#unique_30) [page ] 38 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisition is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before starting the business process, you need to create a sanctioned Business Partner for later use.

Procedure

|  |
| --- |
| Note No detailed procedure is given here. Please refer to the master data script BNE - Create Supplier Master - MDS and BND - Create Customer Master - MDS to create the foreign supplier. The below address adaption is an example; for production use, please adjust accordingly to a sanctioned address:Name: Osama Bin LadenStreet: Str. 12345Postal Code: 123456City: MoscowCountry/Region: RUTime Zone: <Leave Empty> |

### Schedule Business Partners Screening for SAP Watch List Screening Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Business partner will be sent to SAP Watch List Screening for screening automatically when you create or change the business partner, if you have added the business partner roles in SSCUI Business Partner Roles for SAP Watchlist Screening.

Job Schedule Business Partners Screening - Watch List Screening is also supported to screen business partners proactively. In this activity, you can find detailed steps for you to schedule the job to screen business partners with SAP Watch List Screening.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Choose Schedule Business Partners Screening - Watch List Screening (F8016). | The Schedule Business Partners Screening - Watch List Screeningscreen is displayed. |  |
| 3 | Create Application Job Schedule Business Partners Screening for Watch List Screening | On the Application Jobs screen, choose Create.On the New Job screen, make the following entries:Job Template: Schedule Business Partners Screening - Watch List ScreeningJob Name: Schedule Business Partners Screening - Watch List ScreeningChoose Step 2, then make the following entries:Start Immediately: <Select>Note You can choose Define Recurrence Pattern in Step 2 Scheduling Options to make the job as single run or recurrent. For business partner mass screening, please make sure this job is scheduled regularly to make the screening results on BP master data reliable. For example, schedule the job hourly.For example, make the following entries to make the job as recurrent for every 1 hour.Recurrence Pattern: HourlyEvery: 1End: NoneChoose Step 3 and make the following entries:Business Partner: <Optional, Business partner created in step [Create Business Partner](#unique_11) [page ] 20>Choose Schedule. | Job is scheduled and shown in the list. |  |

### Resolve Screening Hit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to use app Review Screening Hits to make a decision for a suspicious business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the Screening Specialist role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Review Screening Hits.Note To make the SAP Watch List Screening Fiori apps available in S/4HANA Fiori Launchpad, please refer to the Custom Tiles for SAP Watch List Screening Fiori app section in set-up instruction for this scope item to create the corresponding custom tile in S/4HANA Fiori Launchpad.Note As of July 2024, you can use new app Review Screening Hits to review screening hits and release or block business objects. For more detailed and latest information, please refer to the section End-User Information [here](https://help.sap.com/viewer/product/SAP_WATCH_LIST_SCREENING/1.0.0.0/en-US). | The Review Screening Hits screen is displayed. |  |
| 3 | Select Screened Name | On the Review Screening Hits screen, find and single click on the Screened Name previously created, for example:Screened Name: Osama Bin Laden |  |  |
| 4 | Resolve Screening Hit | On the Screened Business Object screen, review the screening hits listed and select YES for Hit column for one or more entries.Choose Block.Note Intelligent Screening has been introduced so that previous decisions on Screening Hits would be automatically applied for future Screening Hits with same names.Note As of July 2024, you can use new app Manage Automatic Screening Decisions to review all the automatic screening decisions. You can then change decisions for future hits or deactivate decisions. For more detailed and latest information, please refer to the section End-User Information [here](https://help.sap.com/viewer/product/SAP_WATCH_LIST_SCREENING/1.0.0.0/en-US). | The Screened Name has been confirmed as an actual hit. |  |

### Schedule Postprocessing for SAP Watch List Screening Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure instructs how to schedule the job to pull back the decision made via Screen Hits UI back to S/4HANA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Choose Schedule Postprocessing - Watch List Screening (F3052). | The Schedule Postprocessing - Watch List Screening screen is displayed. |  |
| 3 | Create Schedule Postprocessing Background Job for Watch List Screening | On the Application Jobs screen, choose Create.On the New Job screen, make the following entries:Job Template: Schedule Postprocessing - Watch List ScreeningJob Name: Schedule Postprocessing - Watch List ScreeningChoose Step 2, then make the following entries:Start Immediately: <Select>Note You can choose Define Recurrence Pattern in Step 2 Scheduling Options to make the job as single run or recurrent. For example, Make the following entries to make the job as recurrent for every 15 minutes.Recurrence Pattern: MinutesEvery: 15End: NoneChoose Step 3 and then choose Schedule. | Job is scheduled and shown in the list.There should be no logs stating transfer failed because of a technical error.Note Screening Status is also available in Business Partner master data. If you want to check the screening status for a Business Partner, run transaction: BP and navigate to the Address Overview tab or the Status tab. |  |

### Outbound Process

In this section, you can create sales documents for Watch List Screening. You can find all the document category which is support by SAP Watch List Screening in this [document](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6dd96f68c48e4c139cda7b1bac5599b1/7cbc580df89b4b92b3711e88a654f79c.html?locale=en-US).

Creation of sales order is taken as an example to show how SAP Watch List Screening is embedded in the outbound process. To create other purchasing document, go to the corresponding steps to check the reference scope items for detailed procedures.

Before creating purchasing documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

#### Screening for Sales Order

##### Sales Order Creation using BP With Sanctioned Address

###### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This test procedure serves a guide on how to create a sales order with sanctioned destination.

|  |
| --- |
| Caution Please make sure the Set-up Instruction Guide of this scope item has been followed through to ensure working connectivity between SAP S/4HANA Cloud Public Edition system and SAP Business Technology Platform (SAP BTP). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the Internal Sales Representative role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Sales order worklist | Open Manage Sales Orders (F1873). | The Manage Sales Orders - Services screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create , then Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: <Business Partner ID which is created in chapter [Create Business Partner](#unique_11) [page ] 20>Ship-to Party: <Business Partner ID which is created in chapter [Create Business Partner](#unique_11) [page ] 20>Customer References: PO numberIn the All Items section, fill in the following fields:Material: TG0011Order Quantity: 20 |  | PO number: Enter a customer purchase order number as reference |
| 6 | Save Document | Choose Save. Make a note of the sales order number: __________. | The order is saved with status blocked. Error message displayed.Note To check the current screening status of a sales order, you can choose Display header details, then navigate to the Status tab in the app Display Sales Orders - VA03 (VA03). | Note If the documents are blocked by SAP Watch List Screening, you can also release them in the Manage Documents - Trade Compliance (F2826) app with sufficient reason.To proceed, please follow the instructions outlined below:Search for the corresponding Trade Compliance Document in the SAP Fiori app: Manage Documents - Trade Compliance (F2826) with role: Trade Compliance Specialist.Choose the Details button for the selected document and choose the active Legal Regulation for Watch List Screening.Choose Release Block at the bottom right of the screen.Enter a comment in the window appears and click OK. |

###### Create Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity showcases that the outbound delivery cannot be created since the sales order has been blocked with sanctioned address.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the Shipping Specialist role. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>SD Document: <Sales order number created previously> | Sales order created previously is displayed in the list. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Outbound Delivery creation fails and log is created. Message appears in the log saying order is blocked and is not able to be delivered. |  |

##### Sales Order Creation with Manual Changed Address

###### Create Sales Order with Sanctioned Destination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This test procedure serves a guide on how to create a sales order with sanctioned address.

|  |
| --- |
| Caution Please make sure the Set-up Instruction Guide of this scope item has been followed through to ensure working connectivity between SAP S/4HANA Cloud Public Edition system and SAP Business Technology Platform (SAP BTP). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the Internal Sales Representative role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Sales order worklist | Open Manage Sales Orders (F1873). | The Manage Sales Orders - Services screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create , then Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: 33100050Ship-to Party: 33100050Customer References: PO numberIn the All Items section, fill in the following fields:Material: TG0011Order Quantity: 20 |  | PO number: Enter a customer purchase order number as reference |
| 6 | Adapt Ship-To Party Address | On the Create Standard Order: Overview screen, double-click on the entry of Ship-to Party.Then on the Create Standard Order: Header Data screen, double click on the entry of Ship-to Party.On the Address From Master Data for Ship-To Party (Document header) screen, make the following changes accordingly:Name: Osama Bin Laden1Street: Str. 12345Postal Code: 123456City: MoscowCtry/Reg.: RUTime zone: <Leave empty>Note The above address is a sample address; for production use, please adjust accordingly to a sanctioned address.Note Change the address manually will trigger watch list screening again for the document. |  |  |
| 7 | Save Document | Choose Save. Make a note of the sales order number: __________. | The order is saved.Note To check the current screening status of a sales order, you can choose Display header details, then navigate to the Status tab in the app Display Sales Orders - VA03 (VA03). |  |

###### Create Delivery While Decision Pending (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity showcases that the outbound delivery cannot be created before a decision is made for the corresponding sales order with possible sanctioned address.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log onto the SAP Fiori launchpad using the Shipping Specialist role. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders(F0869A). | The Create Outbound Deliveries - From Sales Orders screen is displayed. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: <Sales order number created previously> | Sales order created previously is displayed in the list. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Outbound Delivery creation fails and log is created. Message appears in the log saying order is blocked and is not able to be delivered. |  |

###### Resolve Screening Hit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to use app Review Screening Hits to make a decision for a suspicious sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the Screening Specialist role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Review Screening Hits.Note To make the SAP Watch List Screening Fiori apps available in S/4HANA Fiori Launchpad, please refer to the Custom Tiles for SAP Watch List Screening Fiori app section in set-up instruction for this scope item to create the corresponding custom tile in S/4HANA Fiori Launchpad.Note As of July 2024, you can use new app Review Screening Hits to review screening hits and release or block business objects. For more detailed and latest information, please refer to the section End-User Information [here](https://help.sap.com/viewer/product/SAP_WATCH_LIST_SCREENING/1.0.0.0/en-US). | The Review Screening Hits screen is displayed. |  |
| 3 | Select Screened Name | On the Review Screening Hits screen, find and single click on the Screened Name previously created, for example:Screened Name: Osama Bin Laden1 |  |  |
| 4 | Resolve Screening Hit | On the Screened Business Object screen, review the screening hits listed and select No for Hit column for one or more entries.Choose Release.Note Intelligent Screening has been introduced so that previous decisions on Screening Hits would be automatically applied for future Screening Hits with same names.Note As of July 2024, you can use new app Manage Automatic Screening Decisions to review all the automatic screening decisions. You can then change decisions for future hits or deactivate decisions. For more detailed and latest information, please refer to the section End-User Information [here](https://help.sap.com/viewer/product/SAP_WATCH_LIST_SCREENING/1.0.0.0/en-US). | The Screened Name has been confirmed as False Positive. |  |

###### Schedule Postprocessing for SAP Watch List Screening Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure instructs how to schedule the job to pull back the decision made via Screen Hits UI back to S/4HANA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Choose Schedule Postprocessing - Watch List Screening (F3052). | The Schedule Postprocessing - Watch List Screening screen is displayed. |  |
| 3 | Create Schedule Postprocessing Background Job for Watch List Screening | On the Application Jobs screen, choose Create.On the New Job screen, make the following entries:Job Template: Schedule Postprocessing - Watch List ScreeningJob Name: Schedule Postprocessing - Watch List ScreeningChoose Step 2, then make the following entries:Start Immediately: <Select>Note You can choose Define Recurrence Pattern in Step 2 Scheduling Options to make the job as single run or recurrent. For example, Make the following entries to make the job as recurrent for every 15 minutes.Recurrence Pattern: MinutesEvery: 15End: NoneChoose Step 3 and then choose Schedule. | Job is scheduled and shown in the list.There should be no logs stating transfer failed because of an technical error. |  |

###### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity showcases that if a suspicious sales order has been decided as not containing real sanctioned party, then corresponding Outbound Delivery is allowed to be created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori launchpad using the Shipping Specialist role. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders(F0869A). | The Create Outbound Deliveries - From Sales Orders(F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: <Sales order number created previously> | Sales order created previously is displayed in the list. |  |
| 4 | Create Delivery | Select your sales order items and choose Save. | Creation of a delivery is triggered. Outbound Delivery creation hasn’t been blocked by SAP Watch List Screening because the hit has been confirmed as False Positive. |  |

#### Screening for Sales Order Without Charge (Optional)

To create sales order without charge, please refer to the Create Sales Order process step in the test script of the scope item BDA: Free of Charge Delivery. If you create sales order without charge using business partner who has sanctioned address, the sales order will be blocked and error message will be displayed.

#### Screening for Sales Contract (Optional)

To create sales contract, refer to the Create Sales Contract process step in the test script of the scope item Sales Contract Management (I9I). If you create sales contract using business partner who has sanctioned address, the sales contract will be blocked and error message will be displayed.

#### Screening for Sales Scheduling Agreement (Optional)

To create sales scheduling agreement, refer to the Create Sales Scheduling Agreement process step in the test script of the scope item Sales Scheduling Agreements (3NR). The watch list screening check is triggered only when the delivery schedule is maintained in the created sales scheduling agreement.

If you create sales scheduling agreement using business partner who has sanctioned address, the sales scheduling agreement will be blocked and error message will be displayed.

#### Screening for Sales Quotation (Optional)

To create sales quotation, refer to the Create Sales Quotation process step in the test script of the scope item Sales Quotation (BDG). If you create sales quotation using business partner who has sanctioned address, the sales quotation will be blocked and error message will be displayed.

### Inbound Process

In this section, you can create purchasing documents for Watch List Screening. You can find all the document category which is support by SAP Watch List Screening in this [document](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6dd96f68c48e4c139cda7b1bac5599b1/7cbc580df89b4b92b3711e88a654f79c.html?locale=en-US).

Creation of purchase order is taken as an example to show how SAP Watch List Screening is embedded in the inbound process. To create other purchasing document, go to the corresponding steps to check the reference scope items for detailed procedures.

Before creating purchasing documents, activate the relevant document types for trade compliance check, which is described in the preliminary step.

#### Screening for Purchase Order

##### Purchase Order Creation using BP With Sanctioned Address

###### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity showcases how to create a purchase order if the address has been sanctioned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Enter Purchase Order dataEnter Purchase Order data | Enter all of the necessary data:Order type: NB Standard POSupplier: <Business Partner ID which is created in chapter Create Business Partner>In the Header section, on the Org. Data tab:Purchasing Org.: 3310Purchasing Group: 001Company Code: 3310In Items section,Material: TG0011PO Quantity: 10Plant: 3310 | The Create Purchase Order screen displays. |  |
| 4 | Purchase Order | Choose Save.Make a note of the purchase order number: __________. | The order is saved. |  |

###### Display Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Display Purchase Order - Advanced (ME23N). | The Display Purchase Order screen is displayed. |  |
| 3 | Display Purchase Order | Choose Other Purchase Order, then enter the purchase order number created previously.Choose Other Document.Choose the tab Compliance in the purchase order header details. | The purchase order created previously is displayed with screening status blocked in the tab Compliance since the hit has been confirmed in SAP Watch List Screening. | Note If the documents are blocked by SAP Watch List Screening, you can also release them in the Manage Documents - Trade Compliance (F2826) app with sufficient reason.To proceed, please follow the instructions outlined below:Search for the corresponding Trade Compliance Document in the SAP Fiori app: Manage Documents - Trade Compliance (F2826) with role: Trade Compliance Specialist.Choose the Details button for the selected document and choose the active Legal Regulation for Watch List Screening.Choose Release Block at the bottom right of the screen.Enter a comment in the window appears and click OK. |

#### Screening for Purchase Contract (Optional)

To create purchase contract, refer to the Create Purchase Contract process step in the test script of the scope item Purchase Contract (BMD). If you create purchase contract using business partner who has sanctioned address, the purchase contract will be blocked and error message will be displayed.

#### Screening for Purchase Scheduling Agreement (Optional)

To create purchase scheduling agreement, refer to the Create Scheduling Agreement process step in the test script of the scope item Scheduling Agreements in Procurement (BMR).

The watch list screening check on purchase scheduling agreements is supported only when creating scheduling agreements with SAP Fiori app Manage Purchase Scheduling Agreements (F2179), add the schedule lines into scheduling agreements before saving in the preparation status.

If you create purchase scheduling agreement using business partner who has sanctioned address, the purchase scheduling agreement will be blocked and error message will be displayed.

#### Screening for Purchase Requisition (Optional)

To create purchase requisition, refer to the Create Purchase Requisition process step in the test script of the scope item Purchase Contract (BMD). If you create purchase requisition using business partner who has sanctioned address, the purchase requisition will be blocked and the blocking information will be shown in Messages.

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
- see-also :: [[13-quality-ehs-and-compliance/test-script-embargo-control-1wc-ae-sap-s-4hana-cloud-public-edition-76]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WE_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 65,600 chars in the whole document
