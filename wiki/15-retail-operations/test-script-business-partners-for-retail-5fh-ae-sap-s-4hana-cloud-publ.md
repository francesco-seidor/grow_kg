---
id: 15-retail-operations/test-script-business-partners-for-retail-5fh-ae-sap-s-4hana-cloud-publ
title: "Test Script: Business Partners for Retail (5FH_AE) - SAP S/4HANA Cloud Public Edition (5FH_S4CLD2608_BPD_EN_AE)"
description: "Test script for Business Partners for Retail (5FH_AE): creating, extending and blocking supplier and customer master data in S/4HANA Cloud (UAE sample data)."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-sites-partners-and-assortments]
aliases: [5FH_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Sites, Business Partners and Assortments", business partner master data, supplier master data, customer master data, supplier blocking, wholesale customer, one-time customer, b2c customer, template customer, partner schemas]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FH_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1078
topic: 15-retail-operations/retail-sites-partners-and-assortments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Business Partners for Retail (5FH_AE) - SAP S/4HANA Cloud Public Edition (5FH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Sites, Business Partners and Assortments** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Business Partners for Retail (5FH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856414)

[2 Prerequisites 4](#_Toc232856415)

[2.1 System Access 4](#_Toc232856416)

[2.2 Roles 4](#_Toc232856417)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856418)

[2.4 Preliminary Steps 6](#_Toc232856419)

[2.4.1 Define Partner Schemas in Supplier Master Record 6](#_Toc232856420)

[3 Overview Table 7](#_Toc232856421)

[4 Test Procedures 9](#_Toc232856422)

[4.1 Create Supplier and extend role as Customer 9](#_Toc232856423)

[4.1.1 Create Supplier Master Data - General Data 9](#_Toc232856424)

[4.1.2 Create Supplier Master Data - Company Code Data 10](#_Toc232856425)

[4.1.3 Create Supplier Master Data - Purchasing Organization Data 12](#_Toc232856426)

[4.1.4 Extend Supplier Master Data – Sales area Data 14](#_Toc232856427)

[4.1.5 Extend Supplier Master Data – Return Supplier 16](#_Toc232856428)

[4.1.6 Block Supplier Master Data 18](#_Toc232856429)

[4.2 Create Wholesale Customer 21](#_Toc232856430)

[4.2.1 Create Customer Master Data - General Data 21](#_Toc232856431)

[4.2.2 Create Customer Master Data - Company Code Data 24](#_Toc232856432)

[4.2.3 Create Customer Master Data - Sales Area Data 25](#_Toc232856433)

[4.3 Create One-time Customer 28](#_Toc232856434)

[4.3.1 Create Customer Master Data - General Data 28](#_Toc232856435)

[4.3.2 Create Customer Master Data - Company Code Data 30](#_Toc232856436)

[4.3.3 Create Customer Master Data - Sales Area Data 31](#_Toc232856437)

[4.4 Create B2C Customer 36](#_Toc232856438)

[4.4.1 Create Customer Master Data - General Data 36](#_Toc232856439)

[4.4.2 Create Customer Master Data - Company Code Data 38](#_Toc232856440)

[4.4.3 Create Customer Master Data - Sales Area Data 40](#_Toc232856441)

[4.5 Create Template Customer (Reference Consumer) 43](#_Toc232856442)

[4.5.1 Creating Customer Master Data - General Data 43](#_Toc232856443)

[4.5.2 Creating Customer Master Data - Company Code Data 45](#_Toc232856444)

[4.5.3 Creating Customer Master Data - Sales Area Data 46](#_Toc232856445)

## Purpose

Overview

A supplier or vendor is a business partner who delivers and sells goods and services to a retailer. A supplier master holds information about the supplier such as its name, address, bank details, tax details, and billing preferences. This supplier information is used and stored in transactions such as purchase orders, goods receipts, and supplier invoices. Some supplier information is specific to a company (known as the company code) or purchasing unit (known as the purchasing organization) within a retailer’s organization.

A customer is a business partner to which goods and services are sold and delivered. A customer master holds information about the customer such as its name, address, bank details, tax details, and delivery and billing preferences. This customer information is used and stored in transactions such as sales orders, deliveries, and billing documents. Some customer information is specific to a company (known as the company code) or sales unit (known as the sales area) within a retailer’s organization.

Business partners have several different functions, described as partner functions. For example, typical partner functions for a supplier are ordering address, goods supplier, invoicing party.

A business partner can be a customer and a supplier at the same time if, for example, the customer also supplies goods or if a supplier is also a customer.

For internal suppliers and customers, see the Sites for Retail (3I3) scope item.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Distribution Center (Site) | 3350 | DC 3350 AE |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10405060 | Direct SalesStore SalesDistributionE-Commerce |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 002 | Group 002 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Division | 00 | Product Division 00 |  |
| Shipping Condition | 010203 | StandardPick-upImmediately |  |
| Tax Category | TTX1 | Tax Category |  |

### Preliminary Steps

#### Define Partner Schemas in Supplier Master Record

Use

Partner schemas allow you to group various partner roles. You can specify that certain roles in a schema are mandatory, that is, cannot be changed after entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Partner Schemas in Supplier Master Record.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The View “Partner Schemas Supplier Master" Change: Overview screen is displayed. |  |
| 3 | Define Partner Schemas in Supplier Master Record | Create the following settings:Choose SUPL (Supplier) as Partner determination procedures.Double click on Partner Functions in Procedure option displaying on the left side of the screen in Dialog Structure section and choose Ordering Address (OA) and Invoicing Party (PI) as Partner Mandatory function. |  |  |
| 4 | Save Your Data | Choose Save. | Data is saved. |  |

## Overview Table

This scope item consists of several <choose the appropriate entity: process steps, reports, items> provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Supplier and extend role as customer |  |  |  |
| [Create Supplier Master Data - General Data](#unique_8) [page ] 9 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Supplier master – general data is created. |
| [Create Supplier Master Data - Company Code Data](#unique_9) [page ] 10 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Supplier master – company code data is created. |
| [Create Supplier Master Data - Purchasing Organization Data](#unique_10) [page ] 12 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Supplier master – purchasing data is created. |
| [Extend Supplier Master Data – Sales area Data](#unique_11) [page ] 14 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Supplier master – company code data is extended. |
| [Extend Supplier Master Data – Return Supplier](#unique_12) [page ] 16 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Supplier master – purchasing data is created. |
| [Block Supplier Master Data](#unique_13) [page ] 18 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Supplier master – is blocked at central level or company code level or purchasing organization level. |
| Create Wholesale Customer |  |  |  |
| [Create Customer Master Data - General Data](#unique_14) [page ] 21 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - general data is created. |
| [Create Customer Master Data - Company Code Data](#unique_15) [page ] 24 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - company code data is created. |
| [Create Customer Master Data - Sales Area Data](#unique_16) [page ] 25 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - sales area data is created. |
| Create One-time Customer |  |  |  |
| [Create Customer Master Data - General Data](#unique_17) [page ] 28 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - general data is created. |
| [Create Customer Master Data - Company Code Data](#unique_18) [page ] 30 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - company code data is created. |
| [Create Customer Master Data - Sales Area Data](#unique_19) [page ] 31 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - sales area data is created. |
| Create Template Customer |  |  |  |
| [Create Customer Master Data - General Data](#unique_20) [page ] 36 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - general data is created. |
| [Create Customer Master Data - Company Code Data](#unique_21) [page ] 38 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - company code data is created. |
| [Create Customer Master Data - Sales Area Data](#unique_22) [page ] 40 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - sales area data is created. |
| Create Template Customer (Reference Consumer) |  |  |  |
| [Creating Customer Master Data - General Data](#unique_23) [page ] 43 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - general data is created. |
| [Creating Customer Master Data - Company Code Data](#unique_24) [page ] 45 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - company code data is created. |
| [Creating Customer Master Data - Sales Area Data](#unique_25) [page ] 46 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) | Customer master - sales area data is created. |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Create Supplier and extend role as Customer

#### Create Supplier Master Data - General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating supplier master data.

Use the following procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Create a BP Organization | Choose Create Organization. | Create Organization screen is displayed. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <XXXXXXXX> (Range in between 10000000 – 999999999)Grouping: <External numeric numbering (higher range)>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Retain this setting. | General data provided. |  |
| 5 | Enter Address Data | On the Address tab page in the Name section, enter the following data:Name : for example, <Food Supplier>Search Term ½: for example, <Retail Supplier> | Address provided. |  |
| 6 | Enter Address Data | In the Standard Address section, enter the address.Street/House number : for example, <Street/House number>Postal Code : for example, <Postal Code>City : for example, <City>Country/ Reg. : for example, AERegion: for example, <Region> | Address provided. |  |
| 7 | Enter Time Zone | In the Street Address section, choose the More fields icon. Enter the following data:Time zone: for example, <CET> | Details provided. |  |
| 8 | Enter Communication Data | On the Address tab page in the Communication section, enter the following data:Language: for example, Arabic | Details provided. |  |
| 9 | Save Your Data | Save your entries. | Business P artner < XXXXXXXX > created message is displayed. |  |

#### Create Supplier Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating supplier master data.

Prerequisite

You must complete the previous chapter, [Create Supplier Master Data - General Data](#unique_8) [page ] 9, before you proceed with this section.

Begin the procedure after you have saved the general data entries, as described in the previous chapter.

Use the following procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Display Business Partner | Choose Open BP and Enter < Business partner > created in chapter [Create Supplier Master Data - General Data](#unique_8) [page ] 9. | Display Organization: < Business Partner > screen is displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:<Supplier (Fin. Accounting)>Note The technical key of this BP role is FLVN00. | Details provided. |  |
| 6 | Open Company Code Data | Choose Company Code at the top of the screen. | Change Organization: <Business Partner>, new role Supplier (Fin. Accounting) screen is displayed. |  |
| 7 | Enter Company Code | Enter the Company Code : 3310 and ENTER. | Details provided. |  |
| 8 | Enter Vendor Accounting Data | On the Supplier: Account Management tab page in the Account Management section, enter the following data:Reconciliation Account: <21100000> (Payables Domestic)Sort key : for example, <009>Note There might be other G/L reconciliation accounts for foreign Suppliers or affiliates. | Details provided. |  |
| 9 | Enter Vendor Payment Data | On the Supplier: Payment Transactions tabUnder Payment Data section, make the following entry:Terms of Payment : <0001>Note The terms of payment defined in this step can be overruled by the terms of payment defined on the purchasing level.Under Invoice Verification section, make the following entry:Tolerance Group : <0001> | Details provided. |  |
| 10 | Enter External Vendor Number | Choose General Data at the top of the screen, navigate to Supplier: General Data tab and verify the following entry:Supplier Number: <Business Partner> | Details provided. |  |
| 11 | Save Your Data | Save your entries.Note Warning is displayed “Vendor <name> is from an EU country/region; enter a VAT registration number (VMD_API043)”Display this message for this business partner again? Choose “No” | The entry in the Change in BP role field switches from Supplier (Fin.Accounting) (New) to Supplier (Fin.Accounting) (defined). |  |

#### Create Supplier Master Data - Purchasing Organization Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating supplier master data.

Prerequisite

You must complete the previous chapter, [Create Supplier Master Data - General Data](#unique_8) [page ] 9, before you proceed with this section.

Begin the procedure after you have saved the general data entries, as described in the previous procedure, on the Display Organization: < Business Partner > view.

Use the following procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Display Business Partner | Choose Open BP and Enter <Business partner> created in chapter [Create Supplier Master Data - General Data](#unique_8) [page ] 9. | Display Organization: <Business Partner> screen is displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:<Supplier>Note The technical key of this BP role is FLVN01 | Details provided. |  |
| 6 | Open Purchasing Organization Data | Choose Purchasing at the top of the screen. | The Purchasing Organization screen appears. |  |
| 7 | Enter Purchasing Data | Enter the following data and hit enter:Purch. Organization : 3310 | Details provided. |  |
| 8 | Enter Purchasing Data | On the Purchasing Data tab page in the Conditions section, enter the following data:Order Currency : AEDPayment terms : <0001>Incoterms: <FH>Incoterms Location 1: for example, <Free House> | Details provided. |  |
| 9 | Enter Purchasing Data | On the Purchasing Data tab page in the Control Data section, enter the following data:Shipping Conditions : <01> (Standard)GR-Based Inv oice Verif. : <yes> | Details provided. |  |
| 10 | Enter Purchasing Data | On the Purchasing Data tab page in the Default Values for Material section, enter the following data:Purchasing Group : 002 Group 002Planned Deliv. Time: <5 days> | Details provided. |  |
| 11 | Enter Purchasing Data | On the Purchasing Data tab page in the Additional Purchasing Data section, enter the following data:Schema Group Supplier : <GP> (Schema Vendor Retail)Automatic Purchase Order : <yes>Pricing Date Control : <1> (Purchase Order Date)Confirmation Control: <0004> (Inbound Delivery) | Details provided. |  |
| 12 | Enter Partner Functions Data | On the Partner Functions tab page in the Partner Functions section, verify that the LF entry (VN when logon language is EN) exists along with OA (Ordering A ddress) and PI (Invoicing Party). | Partner functions verified. |  |
| 13 | Save Your Data | Save your entries.Note A warning is displayed “Vendor <name> is from an EU country/region; enter a VAT registration number (VMD_API043)” Display this message for this business partner again? Choose “No” | The entry in the Change in BP role field switches from Supplier (New) to Supplier (defined). |  |

#### Extend Supplier Master Data – Sales area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for extending supplier to act as customer.

Prerequisite

You must complete the previous chapter, [Create Supplier Master Data - General Data](#unique_8) [page ] 9, before you proceed with this section.

Use the following procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Display Business Partner | Choose Open BP and Enter <Business partner> created in chapter [Create Supplier Master Data - General Data](#unique_8) [page ] 9. | Display Organization: <Business Partner> screen is displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:<Customer>Note The technical key of this BP role is FLCU01 | Details provided. |  |
| 6 | Open Sales and Distribution Data | Choose Sales and Distribution at the top of the screen. | The Sales Area screen appears. |  |
| 7 | Enter Sales Area data | Enter the following data and hit enter:Sales Org: 3310Distr. Channel: 10Division: 00 | Details provided. |  |
| 8 | Enter Sales Area data | On the Shipping tab page in the Shipping section, enter the following data:Shipping Conditions: <01 - Standard>Use Switch Area, enter the same data for distribution chain 40 and 50. (sales areas 3310/40/00 and 3310/50/00)Note Shipping conditions for 3310/50/00 maintained as “RE”. | Details provided. |  |
| 9 | Verify Tax Details | Navigate to Billing tab and provide the details in Output Tax section, enter the following data for country: AETax Classification: <1> | Tax classification entered. |  |
| 10 | Save Your Data | Save your entries.Note A warning is displayed “Customer ##1 is from an EU country/region; entera VAT registrationnumber (CMD_API007)Display this message for this business partneragain? Choose “No” | The entry in the Change in BP role field switches from Customer (New) to Customer (defined). |  |

#### Extend Supplier Master Data – Return Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for configuring return supplier.

Prerequisite

You must complete the previous chapter, Extending Supplier with customer role, before you proceed with this chapter.

Begin the procedure after you have saved the general data entries, as described in the previous procedure, on the Display Organization: < Business Partner > view.

Use the following procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Display Business Partner | Choose Open BP and Enter <Business partner> created in chapter [Create Supplier Master Data - General Data](#unique_8) [page ] 9. | Display Organization: <Business Partner> screen is displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:<Supplier>Note The technical key of this BP role is FLVN01 | Details provided. |  |
| 6 | Open Purchasing Organization Data | Choose Purchasing at the top of the screen. | The Purchasing Organization screen is displayed. |  |
| 7 | Enter Purchasing Data | On the Purchasing Data tab page in the Additional Purchasing Data section, check the following checkboxReturns SupplierCustomer Default Data pop-up windows appears. Check Current Customer and choose Okay button to assign the customer to supplier. | Information Customer successfully mapped is displayed. |  |
| 8 | Save Your Data | Choose Continue and Save your entries.Note A warning is displayed “Customer <Business Partner> is currently not referenced and will be updated accordingly (F2293)Display this message for this business partneragain? Choose “No” | Changes have been saved message is displayed. |  |

#### Block Supplier Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Sometimes is it necessary to block supplier master data for logistics processes. It is possible to block procurement for a specific purchase organization or for all purchase organizations. Also, it is possible to block all postings for a specific company code or all company codes. The block setting can be removed at any time.

The following procedure provides instructions for blocking supplier master data.

Prerequisite

You must have created Supplier Master Data with Company Code Data, Purchasing Organization Data in order to block that supplier.

Begin the procedure after you have saved the General Data entries, as described in the previous procedure, on the Display Organization: < Business Partner > view.

Use the following procedure when your user access presents you with the Maintain Business Partner (BP) app.

Blocking at central level:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Open BP | Click on Open BP present at the top of the screen and in the pop-up, screen input the Business Partner number which you would like to block and click enter. | Business Partner details displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:Business Partner (Gen.) | Details provided. |  |
| 6 | Blocking | Click on tab Status and in section LocksSelect Central Block | Central block is set in supplier master data |  |
| 7 | Save your Data | Select Save.Note A warning is displayed “Customer <Business Partner> is from an EU country/region; enter a VAT registration number (CMD_API007) Display this message for this business partner again?” Choose “No” | Changes have been saved message is displayed. |  |

Blocking at Company Code level:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Open BP | Click on Open BP present at the top of the screen and in the pop-up, screen input the Business Partner number which you would like to block and click enter. | Business partner details displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:Supplier (Financial Accounting)Note The technical key of this BP role is FLVN00 |  |  |
| 6 | Open Company Code Data | Choose Company Code at the top of the screen. | The Company Code screen is displayed. |  |
| 7 | Blocking | Click on tab Vendor: Status and in section Posting Block , choose one of the following as required:Select All Company CodesSelect Selected Company CodeIn section deletion block, choose one of the following as required:Select CoCd del. blockSelect Co. Cde deletion flag | Block is set at company code level or for all company codes |  |
| 8 | Save your Data | Choose Save.Note A warning is displayed “ Vendor <Business Partner> is from an EU country/region;enter a VATregistration number (VMD_API043)Display this message for this business partneragain? ” Choose “No” | Changes have been saved message is displayed. |  |

Blocking at Purchasing Organization level:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data |  |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP) app. | Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Open BP | Click on Open BP present at the top of the screen and in the pop-up, screen input the business partner number which you would like to block and click enter. | Business partner details displayed. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) button to switch to change mode. | Change Organization: <Business Partner> screen is displayed. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:SupplierNote The technical key of this BP role is FLVN01 |  |  |
| 6 | Open Purchasing organization Data | Choose Purchasing at the top of the screen. | The Purchasing Organization screen appears. |  |
| 7 | Blocking | Click on tab Status and in section StatusSelect Delete flag for Purch OrgSelect Purchase block POrg level | Purchasing block is set. |  |
| 8 | Save your Data | Select Save . | Changes have been saved message is displayed. |  |

### Create Wholesale Customer

#### Create Customer Master Data - General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | . |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Create New Organization | In the Customer Master screen, choose Create Organization | Create Organization popup is displayed |  |
| 4 | Enter General Data & Standard Address | In the Create Organization popup make the following entries:General DataBusiness Partner: <XXXXXXXX> (Range in between 10000000 – 999999999)Grouping: <External numeric numbering (higher range) (BP03)>BP Role: FLCU01Name 1 : <Wholesale>Name 2 : <Food>Standard Address :Country/ Region: AELanguage: ArabicChoose OK. | The Customer - New Customer screen opens in Edit Mode. |  |
| 5 | Enter Basic Data | In the Customer - BASIC DATA section make the following entries:General InformationSearch Term 1: for example, <WHOLESALE>Customer InformationDelivery Date Rule: < On Requested Date or Later> | Details provided. |  |
| 6 | Choose Roles | In the Customer - New Customer screen, choose ROLES. | You are navigated to the ROLES section. |  |
| 7 | Enter Roles Data | Under ROLES section, make the following entries:Choose Create and add additional roles:Business Partner Role: FLCU00Note A Customer Master must be created with either BP role FLCU00 (FI Customer) and/or FLCU01 (Customer), with sales data, when used in Sales and/or Purchasing scenarios. | Roles are added. |  |
| 8 | Choose Address | In the Customer - New Customer screen, choose ADDRESS. | You are navigated to the ADDRESS section. |  |
| 9 | Enter Address Data | In the ADDRESS - Standard Address screen make the following entries:Street : <Street>House Number : <1>Postal Code: <Postal Code>City: <City>Country/ Region : United Arab EmiratesRegion: <Region>ADDRESS - Standard CommunicationLanguage: ArabicADDRESS - Address DetailsStandard: <YES> (The system is displayed the above entries as the standard address of the business partner) | Details provided. |  |
| 10 | Choose Bank Accounts | In the Customer - New Customer screen section, choose BANK ACCOUNTS. | You are navigated to the BANK ACCOUNTS section. |  |
| 11 | Choose Create | In the Customer Master - BANK ACCOUNTS section, choose Create. | The Bank Account section appears with a line item in Edit Mode. |  |
| 12 | Enter Bank Data | In the line item, click on the ‘>’ icon to the right and In the Bank Account – Bank Information screen make the following entries:Bank Country /Region: AEBank Key: <Enter bank key>Caution Bank keys and Control keys must be defined beforehand. Use the value help for more information on allowed entries in this field.Bank Valid From: <Enter date>Bank Valid To: <Enter date>Account Number: <Enter account number>Choose Apply. | Bank account is added. |  |
| 13 | (Optional)Choose Tax Number | In the Customer screen, under Identification tab choose TAX NUMBERS. | You are navigated to the TAX NUMBERS section. |  |
| 14 | Choose Create | In the Customer - TAX NUMBERS section, choose Create. | The Tax Number section appears in Edit Mode. |  |
| 15 | Enter Tax Number Data | In the New Tax Number - GENERAL DATA screen make the following entries:Tax Category: <enter the category>Tax Number: <enter the number>Entering Tax Numbers depends on the specific country requirements.Note Choose the correct category that applies for the customer's country. For example, for a German business partner you maintain a value for the Category 1, representing the commonly used VAT tax number (Umsatzsteuer-Identifikationsnummer). | Details provided. |  |
| 16 | Save Your Data | Choose Create. | Master data record created message is displayed. |  |

Only populate the fields if required, otherwise choose Delete to remove the (empty) data set.

#### Create Customer Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

Prerequisite

You must complete the previous chapter, [Create Customer Master Data - General Data](#unique_14) [page ] 21, before you proceed with this section.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already logged on to the Master Data - Customer Master section, Customer Master tile. After you have saved your general data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | The Customer screen opens in Edit Mode again (fields are ready for your input). | . |
| 4 | Choose Company Code | In the Customer screen, choose COMPANY CODES. | You are navigated to the COMPANY CODES section. |  |
| 5 | Choose Create | In the Customer - COMPANY CODES screen section, choose Create. | The Company Code screen opens in Edit Mode. |  |
| 6 | Enter Company Code Data | In the Company Code screen make the following entries:GENERAL DATACompany Code: 3310Finance -AccountingReconciliation Account: <12100000 (Receivables Domestic)>Choose Apply. | Details added. |  |
| 7 | Save Your Data | Choose Save. | Master data record saved message is displayed. |  |

#### Create Customer Master Data - Sales Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

Prerequisite

You must complete the previous chapter [Create Customer Master Data - General Data](#unique_14) [page ] 21, before you proceed with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already logged on to the Master Data - Customer Master chapter, Customer Master tile. After you have saved your data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | The Customer Master view opens in Edit Mode (fields are ready for your input). |  |
| 4 | Choose Sales Area | In Customer screen, choose SALES AREAS | The system navigates to the SALES AREAS section. |  |
| 5 | Choose Create | In the Customer– SALES AREAS section, choose Create. | The Sales Are a screen opens in Edit Mode. |  |
| 6 | Enter Sales Area Data | In Sales Area screen, enter the following data:GENERAL DATASales Org.: 3310Distr. Channel: 10Division: 00SALES AREA DETAILSSales Area Details - Sales OrdersCustomer Group: <Customer Group 01 (01)>Sales Office: Sales Office 330Sales Group: Sales Group 330Order Probability in Percentage: <100>Currency: AEDSales Area Details - Billing:Incoterms: <EXW>Incoterms Location 1: <Store>Payment Terms: <0002>Sales Area Details - Shipping:Delivery Priority: <Normal>Shipping Conditions: <01 - Standard>Delivery Plant: 3350Order Combination : <yes>Sales Area Details - Accounting:Account assignment group: <Domestic Revenues>Partial DeliveriesPartial Delivery Per Item : <Partial delivery allowed> | Details provided. |  |
| 7 | Choose Apply | Choose Apply. | Changes are applied. |  |
| 8 | Save Your Data | Choose Save. | Master data record saved message is displayed. |  |
| 9 | Choose Sales Area – Tax Data | In the Sales Area screen, choose TAXES. | The system navigates to the Sales Area TAX section. |  |
| 10 | Enter Sales Area Data – Tax Data | In Sales Area– TAXES section, make the following entries:Country/Region : AETax Category : TTX1Tax Classification: <1> | Tax data is added. |  |
| 11 | Verify Partner Roles | From Sales Areas screen, choose PARTNER FUNCTIONS and verify the below Partner Roles are displayed:SP (Sold-to Party)BP (Bill-to Party)PY (Payer)SH (Ship-to Party) | Partner roles are verified. |  |

### Create One-time Customer

#### Create Customer Master Data - General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Create New Person | In the Manage Customer Master Data (F0850A) screen, choose Create Person | Create Person popup is displayed |  |
| 4 | Enter General Data & Standard Address | In the Create Person popup make the following entries:General DataBusiness Partner: for example, <R_XXXXXXX>Grouping: <External alpha-numeric for CPD BPs (CPDA)>BP Role: FLCU01First Name: <any>Last Name: <any>Standard AddressCountry/ Region: AELanguage: ArabicChoose OK. | The Customer - New Customer screen opens in Edit Mode. |  |
| 5 | Enter Basic Data | In the Customer - New Customer screen, under BASIC DATA section make the following entries:General InformationNatural Person: <Yes>Customer InformationDelivery Date Rule: <On Requested Date or Later> | Details provided. |  |
| 6 | Choose Roles | In the Customer - New Customer screen, choose ROLES. | You are navigated to the ROLES screen section |  |
| 7 | Enter Roles Data | Under ROLES section, make the following entries:Choose Create and add additional roles:Business Partner Role: FLCU00Note A Customer Master must be created with either BP role FLCU00 (FI Customer) and/or FLCU01 (Customer), with sales data, when used in Sales and/or Purchasing scenarios. | Roles are added. |  |
| 8 | Choose Address | In the Customer- New Customer screen, choose ADDRESS. | You are navigated to the ADDRESS screen section. |  |
| 9 | Enter Address Data | In the ADDRESS - Standard Address screen make the following entries:City: <City>Country/ Region (mandatory): United Arab EmiratesADDRESS - Standard CommunicationLanguage: for example, ArabicADDRESS - Address DetailsStandard: <YES> (The system is displayed these entries as the standard address of the business partner) | Details provided. |  |
| 10 | Save Your Data | Choose Create. | Master data record created message is displayed. |  |

#### Create Customer Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

Prerequisite

You must complete the previous chapter, [Create Customer Master Data - General Data](#unique_17) [page ] 28, before you proceed with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already logged on to the Master Data - Customer Master section, Customer Master tile. After you have saved your general data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | The Customer screen opens in Edit Mode again (fields are ready for your input). | . |
| 4 | Choose Company Code | In the Customer screen, choose COMPANY CODES. | You are navigated to the COMPANY CODES section. |  |
| 5 | Choose Create | In the Customer - COMPANY CODES section, choose Create. | The Company Code screen opens in Edit Mode. |  |
| 6 | Enter Company Code Data | In the Customer Company Code screen make the following entries:GENERAL DATACompany Code: for example, 3310Finance -AccountingReconciliation Account: for example, <12100100 (Receivables Domestic - One Time Accounts)>Sort Key: <External doc.number (009)>FINANCE - Payment DataPayment Terms: <0004> |  |  |
| 7 | Return to Main Screen | Choose Apply. | Changes are applied. |  |
| 8 | Save Your Data | Choose Save. | Master data record saved message is displayed. |  |

#### Create Customer Master Data - Sales Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

Prerequisite

You must complete the previous chapter, [Create Customer Master Data - General Data](#unique_17) [page ] 28, before you proceed with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is dispalyed. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already logged on to the Master Data - Customer Master section, Customer Master tile. After you have saved your data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | The Customer view opens in Edit Mode (fields are ready for your input). |  |
| 4 | Choose Sales Area | From Customer screen,choose SALES AREAS | The system navigates to the SALES AREAS section. |  |
| 5 | Choose Create | In the Customer– SALES AREAS section, choose Create. | The Sales Area screen opens in Edit Mode. |  |
| 6 | Enter Sales Area Data | In New Sales Area, enter the following data:GENERAL DATASales Org.: 3310Distr. Channel: 10Division: 00Sales Area Details - Sales OrdersCurrency:AEDSales Area Details - BillingIncoterms: <EXW>Incoterms Location 1: <Store>Payment Terms: <0004>Payment Guarantee Procedure: <0002>Sales Area Details - Shipping:Delivery Priority: <Normal>Shipping Conditions: <01 - Standard>Delivery Plant: 3350POD Relevant : <Yes>Sales Area Details – Partial DeliveriesPartial Delivery Per Item: <Partial delivery allowed> | Details provided. |  |
| 7 | Choose Sales Area – Tax Data | In the Sales Area screen, choose TAXES. | The system navigates to TAXES section. |  |
| 8 | Enter Sales Area Data – Tax Data | In Sales Area– TAXES section, make the following entries:Country/Region : AETax Category : TTX1Tax Classification: <1> | Tax data is added. |  |
| 9 | Verify Partner Roles | From Sales Areas screen, choose PARTNER FUNCTIONS and verify the below Partner Roles are displayed:SP (Sold-to Party)BP (Bill-to Party)PY (Payer)SH (Ship-to Party) | Partner roles are verified. |  |
| 10 | Choose Apply | Choose Apply. | Changes are applied. |  |
| 11 | Choose Create | Choose Create under Sales Areas section. | The Sales Area screen opens in Edit Mode. |  |
| 12 | Enter Sales Area Data | In New Sales Area, enter the following data:GENERAL DATASales Org.: 3310Distr. Channel: 40Division: 00Sales Area Details - Sales OrdersCurrency: AEDSales Area Details - BillingIncoterms: <EXW>Incoterms Location 1: <Store>Payment Terms:<0001>Sales Area Details - Shipping:Delivery Priority: <Normal>Shipping Conditions: <02 - Pick-up>Delivery Plant: 3350Sales Area Details - Accounting:Account Assignment group: <Domestic Revenues>Sales Area Details – Partial DeliveriesPartial Delivery Per Item: <Partial delivery allowed> | Details provided. |  |
| 13 | Choose Sales Area – Tax Data | In the Sales Area screen, choose TAXES. | The system navigates to TAXES section. |  |
| 14 | Enter Sales Area Data – Tax Data | In Sales Area– TAXES section, make the following entries:Country/Region : AETax Category : TTX1Tax Classification: <1> | Tax data is added. |  |
| 15 | Verify Partner Roles | From Sales Areas screen, choose PARTNER FUNCTIONS and verify the below Partner Roles are displayed:SP (Sold-to Party)BP (Bill-to Party)PY (Payer)SH (Ship-to Party) | Partner roles are verified. |  |
| 16 | Return to Main View | Choose Apply. | Changes are applied. |  |
| 17 | Choose Create | Choose Create under Sales Areas section. | The Sales Area screen opens in Edit Mode. |  |
| 18 | Enter Sales Area Data | In New Sales Area, enter the following data:GENERAL DATASales Org.: 3310Distr. Channel: 60Division: 00Sales Area Details - Sales OrdersCurrency: AEDSales Area Details - BillingIncoterms: <EXW>Incoterms Location 1: <Store>Payment Terms: <0004>Sales Area Details - Shipping:Delivery Priority: <Normal>Shipping Conditions: <02 - Pick-up>Delivery Plant: 3350POD Relevant : <Yes>Sales Area Details – Partial DeliveriesPartial Delivery Per Item: <Partial delivery allowed> | Details provided. |  |
| 19 | Choose Sales Area – Tax Data | In the Sales Area screen, choose TAXES. | The system navigates to TAXES section. |  |
| 20 | Enter Sales Area Data – Tax Data | In Sales Area– TAXES section, make the following entries:Country/Region : AETax Category : TTX1Tax Classification: <1> | Tax data is added. |  |
| 21 | Verify Partner Roles | From Sales Areas screen, choose PARTNER FUNCTIONS and verify the below Partner Roles are displayed:SP (Sold-to Party)BP (Bill-to Party)PY (Payer)SH (Ship-to Party) | Partner roles are verified. |  |
| 22 | Return to Main View | Choose Apply. | Changes are applied. |  |
| 23 | Save Your Data | Choose Save. | Master data record saved message is displayed. |  |

### Create B2C Customer

#### Create Customer Master Data - General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Create New Person | In the Manage Customer Master Data (F0850A) screen, choose Create Person | Create Person popup is displayed |  |
| 4 | Enter General Data & Standard Address | In the Create Person popup make the following entries:General DataBusiness Partner: <XXXXXXXX> (Range in between 10000000 – 999999999)Grouping: < External numeric numbering (higher range) (BP03)>BP Role: FLCU01First Name: <any>Last Name: <any>Standard AddressCountry/Region: AELanguage: ArabicChoose OK. | The Customer - New Customer screen opens in Edit Mode. |  |
| 5 | Enter Basic Data | In the Customer - New Customer screen, under BASIC DATA section make the following entries:General InformationNatural Person: <Yes>Customer InformationDelivery Date Rule: <On Requested Date or Later> | Details provided. |  |
| 6 | Choose Roles | In the Customer - New Customer screen, choose ROLES. | You are navigated to the ROLES screen section |  |
| 7 | Enter Roles Data | Under ROLES section, make the following entries:Choose Create and add additional roles:Business Partner Role: FLCU00Note A Customer Master must be created with either BP role FLCU00 (FI Customer) and/or FLCU01 (Customer), with sales data, when used in Sales and/or Purchasing scenarios. | Roles are added. |  |
| 8 | Choose Address | In the Customer- New Customer screen, choose ADDRESS. | You are navigated to the ADDRESS screen section. |  |
| 9 | Enter Address Data | In the ADDRESS - Standard Address screen make the following entries:Street: <Street>House Number: <House Number>Postal Code: <Postal Code>City: <City>Country/ Region (mandatory): United Arab EmiratesRegion: <Region>ADDRESS - Standard CommunicationLanguage: for example, ArabicADDRESS - Address DetailsStandard: <YES> (The system is displayed the above entries as the standard address of the business partner) | Details provided. |  |
| 10 | Choose Bank Accounts | In the Customer- New Customer screen, choose BANK ACCOUNTS. | You are navigated to the BANK ACCOUNTS screen section. |  |
| 11 | Enter Bank Account Data | In the Customer - New Customer screen, under BANK ACCOUNTS section, choose Create and make the following entries:Bank Country/Region: AEBank Key: <Enter bank key>Bank Valid From: <Enter any date>Bank Valid To: <Enter any date>Account Number: <Enter account number>Choose Apply. | Bank account data is added. |  |
| 12 | Save Your Data | Choose Create. | Master data record created message is displayed. |  |

#### Create Customer Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

Prerequisite

You must complete the previous chapter, Creating Customer Master Data - General Data, before you proceed with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already logged on to the Master Data - Customer Master section, Customer Master tile. After you have saved your general data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | The Customer screen opens in Edit Mode again (fields are ready for your input). | . |
| 4 | Choose Company Code | In the Customer screen, choose COMPANY CODES. | You are navigated to the COMPANY CODES section. |  |
| 5 | Choose Create | In the Customer - COMPANY CODES section, choose Create. | The Company Code screen opens in Edit Mode. |  |
| 6 | Enter Company Code Data | In the Customer Company Code screen make the following entries:GENERAL DATACompany Code: for example, 3310Finance -AccountingReconciliation Account: <Receivables Domestic (12100000)> | Details provided. |  |
| 7 | Return to Main Screen | Choose Apply. | Changes are applied. |  |
| 8 | Save Your Data | Choose Save. | Master data record saved message is displayed. |  |

#### Create Customer Master Data - Sales Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

Prerequisite

You must complete the previous chapter, [Create Customer Master Data - General Data](#unique_20) [page ] 36, before you proceed with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already logged on to the Master Data - Customer Master section, Customer Master tile. After you have saved your data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | The Customer view opens in Edit Mode (fields are ready for your input). |  |
| 4 | Choose Sales Area | From Customer screen, choose SALES AREAS | The system navigates to the SALES AREAS section. |  |
| 5 | Choose Create | In the Customer– SALES AREAS section, choose Create. | The Sales Area screen opens in Edit Mode. |  |
| 6 | Enter Sales Area Data | In New Sales Area, enter the following data:GENERAL DATASales Org.: 3310Distr. Channel: 40Division: 00Sales Area Details - Sales OrdersCustomer Group : <Customer Group 02 (02)>Currency: AEDSales Area Details - BillingIncoterms: <EXW>Incoterms Location 1: <Store>Payment Terms:<0001>Sales Area Details - Shipping:Delivery Plant: 3350Shipping Conditions: <01 - Standard>Sales Area Details - Accounting:A ccount Assignment group: <Domestic Revenues>Sales Area Details – P artial DeliveriesPartial Delivery Per Item: <Partial delivery allowed> | Details provided. |  |
| 7 | Choose Sales Area – Tax Data | In the Sales Area screen, choose TAXES. | The system navigates to TAXES section. |  |
| 8 | Enter Sales Area Data – Tax Data | In Sales Area– TAXES section, make the following entries:Country/Region : AETax Category : TTX1Tax Classification: <1> | Tax data is added. |  |
| 9 | Verify Partner Roles | From Sales Areas screen, choose PARTNER FUNCTIONS and verify the below Partner Roles are displayed:SP (Sold-to Party)BP (Bill-to Party)PY (Payer)SH (Ship-to Party) | Partner roles are verified. |  |
| 10 | Return to Main View | Choose Apply. | Changes are applied. |  |
| 11 | Choose Create | Choose Create under Sales Areas section. | The Sales Area screen opens in Edit Mode. |  |
| 12 | Enter Sales Area Data | In New Sales Area, enter the following data:GENERAL DATASales Org.: 3310Distr. Channel: 60Division: 00Sales Area Details - Sales OrdersCustomer Group : <Customer Group 02 (02)>Currency: AEDSales Area Details - BillingIncoterms: <EXW>Incoterms Location 1: <Store>Payment Terms:<0001>Sales Area Details - Shipping:Shipping Conditions: <02 - Pick-up>Order Combination : <Yes>Sales Area Details - A ccounting:A ccount Assignment group: <Domestic Revenues (01)>Sales Area Details – P artial DeliveriesPartial Delivery Per Item: <Partial delivery allowed> | Details provided. |  |
| 13 | Choose Sales Area – Tax Data | In the Sales Area screen, choose TAXES. | The system navigates to TAXES section. |  |
| 14 | Enter Sales Area Data – Tax Data | In Sales Area– TAXES section, make the following entries:Country/Region : AETax Category : TTX1Tax Classification: <1> | Tax data is added. |  |
| 15 | Verify Partner Roles | From Sales Areas screen, choose PARTNER FUNCTIONS and verify the below Partner Roles are displayed:SP (Sold-to Party)BP (Bill-to Party)PY (Payer)SH (Ship-to Party) | Partner roles are verified. |  |
| 16 | Return to Main View | Choose Apply. | Changes are applied. |  |
| 17 | Save Your Data | Choose Save. | Master data record saved message is displayed. |  |

### Create Template Customer (Reference Consumer)

#### Creating Customer Master Data - General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | . |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A) screen is displayed. |  |
| 3 | Create New Organization | In the Customer Master screen, choose Create Organization. | Create Organization popup is displayed. |  |
| 4 | Enter General Data & Standard Address | In the Create Organization popup make the following entries:General Data tabGrouping: <Internal Numbering for standard use) (BP02)>BP Role: FLCU01Name 1: <Retail Template Customer>Standard Address :Country/ Region: AELanguage: ArabicChoose OK. | The Customer - New Customer screen opens in Edit Mode. |  |
| 5 | Choose Roles | In the Customer - New Customer screen, choose ROLES. | You are navigated to the ROLES section. |  |
| 6 | Enter Roles Data | Under ROLES section, make the following entries:Choose Create and add additional roles:Business Partner Role: FLCU00 | Roles are added. |  |
| 7 | Choose Address | In the Customer - New Customer screen, choose ADDRESS. | You are navigated to the ADDRESS section. |  |
| 8 | Enter Address Data | In the ADDRESS - Standard Address screen, make the following entries:Street: <Street>House Number: <house number>Postal Code: <Postal Code>City: <City>Country/ Region: United Arab EmiratesADDRESS - Standard CommunicationLanguage : Arabic | Details provided. |  |
| 9 | Save Your Data | Choose Create. | Master data record created message is displayed. |  |

#### Creating Customer Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

Prerequisite

You must complete the previous chapter, [Creating Customer Master Data - General Data](#unique_23) [page ] 43, before you proceed with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A)screen is displayed. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already logged on to the Master Data - Customer Master section, Customer Master tile. After you have saved your general data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | The Customer screen opens in Edit Mode again (fields are ready for your input). | . |
| 4 | Choose Company Code | In the Customer screen, choose COMPANY CODES. | You are navigated to the COMPANY CODES section. |  |
| 5 | Choose Create | In the Customer - COMPANY CODES screen section, choose Create. | The Company Code screen opens in Edit Mode. |  |
| 6 | Enter Company Code Data | In the Company Code screen, make the following entries:GENERAL DATACompany Code: 3310Finance -AccountingReconciliation Account: <12100000 (Receivables Domestic)>Choose Apply. | Details added. |  |
| 7 | Save Your Data | Choose Save. | Master data record saved message is displayed. |  |

#### Creating Customer Master Data - Sales Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data.

Prerequisite

You must complete the previous chapter, [Creating Customer Master Data - General Data](#unique_23) [page ] 43, before you proceed with this chapter.

Begin the procedure after you have saved the General Data entries, as described in the previous chapter.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A) app. | The Manage Customer Master Data (F0850A)screen is dipalyed. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes you are continuing from the previous step and are already logged on to the Master Data - Customer Master section, Customer Master tile. After you have saved your data from the previous section, the system is in Display Mode. To proceed, you must be in Edit Mode. | The Customer Master view opens in Edit Mode (fields are ready for your input). |  |
| 4 | Choose Sales Area | In Customer screen, choose SALES AREAS. | The system navigates to the SALES AREAS section. |  |
| 5 | Choose Create | In the Customer SALES AREAS section, choose Create. | The Sales Area screen opens in Edit Mode. |  |
| 6 | Enter Sales Area Data | In Sales Area screen, enter the following data:GENERAL DATASales Org.: 3310Distr. Channel: 40Division: 00SALES AREA DETAILSCurrency: AEDSales Area Details - BillingIncoterms: <EXW>Incoterms Location 1: <Store>Payment Terms:<0002>Sales Area Details - Shipping:Shipping Conditions: <03 - Immediately> | Details provided. |  |
| 7 | Choose Sales Area – Tax Data | In the Sales Area screen, choose TAXES. | The system navigates to TAXES section. |  |
| 8 | Enter Sales Area Data – Tax Data | In Sales Area– TAXES section, make the following entries:Country/Region : AETax Category : TTX1Tax Classification: <1> | Tax data is added. |  |
| 9 | Choose Apply | Choose Apply. | Changes are applied. |  |
| 10 | Save Your Data | Choose Save. | Master data record saved message is displayed. |  |

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
- related-to :: [[15-retail-operations/sites-for-retail-3i3-ae-test-script-sap-s-4hana-cloud-public-edition-9]]
- related-to :: [[15-retail-operations/test-script-sap-s-4hana-cloud-public-edition-assortments-3i5-ae-945]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 75,070 chars in the whole document
