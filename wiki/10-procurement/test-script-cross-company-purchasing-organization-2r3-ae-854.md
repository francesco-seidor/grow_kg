---
id: 10-procurement/test-script-cross-company-purchasing-organization-2r3-ae-854
title: "Test Script: Cross-Company Purchasing Organization (2R3_AE) (2R3_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (scope item 2R3, UAE) for cross-company purchasing organization setup, then PO, goods receipt and supplier invoice."
cluster: 10-procurement
tags: [kb/procurement, topic/direct-material-procurement]
aliases: [2R3_S4CLD2608_BPD_EN_AE]
keywords: [Direct Material Procurement, cross-company purchasing, purchasing organization setup, organizational structure configuration, purchase order creation, goods receipt posting, supplier invoice creation, business partner extension, material master extension, purchasing info records]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2R3_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-854
topic: 10-procurement/direct-material-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Cross-Company Purchasing Organization (2R3_AE) (2R3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2R3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Direct Material Procurement** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Cross-Company Purchasing Organization (2R3_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Cross-Company Purchasing Organization (2R3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849919)

[2 Prerequisites 4](#_Toc232849920)

[2.1 System Access 4](#_Toc232849921)

[2.2 Roles 4](#_Toc232849922)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849923)

[2.4 Business Conditions 6](#_Toc232849924)

[2.5 Preliminary Steps 7](#_Toc232849925)

[2.5.1 Open New MM Period 7](#_Toc232849926)

[2.5.2 Create a New Cross-Country Purchasing Organization 7](#_Toc232849927)

[2.5.3 Create Purchasing Organization Description 8](#_Toc232849928)

[2.5.4 Unassign Company Code for Cross-Country Purchasing Organization 10](#_Toc232849929)

[2.5.5 Assign Cross-Company Purchasing Organization to Plants 11](#_Toc232849930)

[2.5.6 Assign Cross-Country Purchasing Organization to Cross-Country Plants 13](#_Toc232849931)

[2.5.7 Extend Business Partner 14](#_Toc232849932)

[2.5.8 Extend Material Master Data 16](#_Toc232849933)

[2.5.9 Create an Info Record for Cross-Company Purchasing Organization 18](#_Toc232849934)

[2.5.10 Create a Condition Record for EU Countries Intrastate Processing 20](#_Toc232849935)

[2.5.11 Configure Activate HDM for Attachment Object Type (Optional) 21](#_Toc232849936)

[3 Overview Table 23](#_Toc232849937)

[4 Test Procedures 25](#_Toc232849938)

[4.1 Cross-Company Code Purchasing within a Single Country 25](#_Toc232849939)

[4.1.1 Create Purchase Order 25](#_Toc232849940)

[4.1.1.1 Create Purchase Order for One Company Code 25](#_Toc232849941)

[4.1.1.2 Create Purchase Order for another Company Code (Optional) 27](#_Toc232849942)

[4.1.2 Post Goods Receipt 29](#_Toc232849943)

[4.1.3 Create Supplier Invoice 30](#_Toc232849944)

[4.1.4 Change the Cross-Company Purchasing Organization to be Local (Optional) 32](#_Toc232849945)

[4.1.5 Post Goods Receipt (Optional) 33](#_Toc232849946)

[4.1.6 Create Supplier Invoice (Optional) 34](#_Toc232849947)

[4.1.7 Post Goods Receipt (Optional) 36](#_Toc232849948)

[4.1.8 Set the GR Delivery Completed Indicator(Optional) 37](#_Toc232849949)

[4.2 Cross-Company Code Purchasing across Countries 38](#_Toc232849950)

[4.2.1 Create Purchase Order 38](#_Toc232849951)

[4.2.1.1 Create Purchase Order for One Company Code 38](#_Toc232849952)

[4.2.1.2 Create Purchase Order for another Company Code (Optional) 40](#_Toc232849953)

[4.2.2 Post Goods Receipt 42](#_Toc232849954)

[4.2.3 Create Supplier Invoice 43](#_Toc232849955)

## Purpose

Overview

This scope item enables the user to flexibly set up a cross-company purchasing organization. The organization structure can be changed throughout the entire procurement process and provides the capabilities to set up individual organization structures.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Master Data Specialist - Batch Data | SAP_BR_BATCH_MASTER_SPCLST | Master Data - Batch | SAP_BR_BATCH_MASTER_SPCLST |  |
| Tax Specialist | SAP_BR_TAX_SPECIALIST | Tax Rates | SAP_BR_TAX_SPECIALIST |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Plant | 3320 | Plant 2 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 332A | Std. storage 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3330 | Plant 3 AE |  |
| Storage Location | 333A | Std. storage 1 |  |
| Company Code | 3320 | Company Code 3320 |  |
| Central Purchase Organization | 3340 | intra-country PORg. 3340 |  |
| Purchasing group | 001 | Group 001 |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Supplier | 12300001 | Domestic MX Supplier 1 |  |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. |  |
| no Serial no.; no batch | See sections [Business Conditions](#unique_6) [page ] 6 and Preliminary Steps |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ – Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |

|  |
| --- |
| Note To test the cross-company code purchasing across countries scenario, at least two countries solution has to be installed, for example, for US, install DE and US; for DE, install DE and FR.Country IN and BR is out of scope for the cross-company code purchasing across countries scenario.Before you start the testing, make sure the data in Master Data Organizational Data and Other data has been created. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following steps from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period.

- Closing MM Period and Opening New Posting Period

#### Create a New Cross-Country Purchasing Organization

Purpose

The purpose of this activity is to create a cross-country purchasing organization.

|  |
| --- |
| Note The pricing procedure for the new purchase organization 3340 is same as the original purchasing organization 3310 pricing procedure, if you have any different condition types for different countries, please adjust it manually after the new purchasing organization is created.In a Central Business Configuration (CBC) environment, below second set of organization entity IDs only applies to an Implementation Project. If you are working on an evaluation project (starter or partner demo), to create a second set of organizations, follow the naming rule described in [Using the Set Up Organizational Structure App](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/55c9333eed324cd284f6c4e5dab8462f/d020ff461d504421bcc55d87cbc0ae57.html). |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration . |  |
| 2 | Access the App | Open Manage Your Solution (F1241) tile. | The Manage Your Solution screen displays. |
| 3 | Enter into the OrgStructure-configure | Choose Set Local Version, select United Arab Emirates .On the Configure Your Solution: Realize Phase screen, select Organization in the Application Area field , then navigate to the organization item by choosing the Chevron (>) .In the Configuration Steps section, select the Organizational Structure item, choose Configure. | The Organizational Structure screen displays. |
| 4 | Create a new purchasing organization. | Choose Company Code3310 on the left-hand side pane.On the right-hand side, choose Purchasing Organization, then choose Add.On the Add Purchasing Organization screen, make the following entries:ID: 3340Source: Purch. Org. 3310Choose Ok. | The new cross-company purchasing organization is created. |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |
| 2 | Enter into the OrgStructure-configure | In the Scope and Organizational Structure phase, navigate to the Activities tab and choose Set Up Organization Structure.On the Set Up Organizational Structure, choose Create → Purchasing Organization, and in the dialog box input the following entrys and choose Save.ID: 3340Name: Central PurOrg | The new cross-company purchasing organization is created. |

#### Create Purchasing Organization Description

Purpose

The purpose of this activity is to change the cross-company purchasing organization description.

|  |
| --- |
| Note The pricing procedure for the new purchase organization 3340 is same as the original purchasing organization 3310 pricing procedure, if you have any different condition types for different countries, please adjust it manually. |

Prerequisite

The cross-company purchasing organization has been created in last step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration . |  |
| 2 | Access the App | Open Manage Your Solution (F1241) tile. |  |
| 3 | Enter the new description | Choose Set Local Version, select United Arab Emirates.On the Configure Your Solution: Realize Phase screen, select Organization in the Application Area field , then navigate to the organization item by choosing the Chevron (>) .On the Organizational Structure step ,choose Configure.Choose Company Code3310 on the left-hand side pane.Choose the new purchasing organization 3340 .Choose Configure and then choose Edit. Change the description to inter-country PORg.Choose Save. | The new description is entered. |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |
| 2 | Enter into the OrgStructure-configure | In the Scope and Organizational Structure phase, navigate to the Activities tab and choose Set Up Organization Structure.On the Set Up Organizational Structure, double-click the Purchasing Organization3310 we created in the previous step. In the right-side section Purchasing Organization, you can change the description and choose Save.ID: 3340Name: Central PurOrg 1 | The new description is entered. |

#### Unassign Company Code for Cross-Country Purchasing Organization

Purpose

The purpose of this activity is to unassign the company code for the cross-country purchasing organization.

Prerequisite

The cross-company purchasing organization has been created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using access level as a Configuration Expert - Business Process Configuration |  |
| 2 | Access the App | Open Manage Your Solution (F1241) tile. |  |
| 3 | Unassign Company Code | Choose Set Local Version, select a country of plants.On the Configure Your Solution: Realize Phase screen, select Organization in the Application Area field , then navigate to the organization item by choosing the Chevron (>) .On the Organizational Structure step, choose Configure.Choose the cross-company purchasing organization 3340 on the left-hand side pane.Choose Edit Company Code Assignment on the right-hand pane.Select None on the Edit Company Code Assignment screen, then choose OK. | The assignment is done. |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Assign Purchasing Organization to Company Code | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign purchasing organization to company code.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Maintenance View for Requisitioning Groups for Purchasing" screen is displayed. |  |
| 3 | Save New Entry | On the Assign Purchasing Organization choose the item line you want to unassign, then choose Save. | The assignment is done. |  |

#### Assign Cross-Company Purchasing Organization to Plants

Purpose

The purpose of this activity is to assign cross-company purchasing organization to plants.

Prerequisite

The cross-company purchasing organization has been unassigned from company code in last step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration . |  |
| 2 | Access the App | Open Manage Your Solution (F1241) tile. | The Manage Your Solution (Original) screen displays. |
| 3 | Assign the new purchasing organization to plants | Choose Set Local Version, select the country of purchasing organization.On the Configure Your Solution: Realize Phase screen, select Organization in the Application Area field , then navigate to the organization item by choosing the Chevron (>) .On the Organizational Structure step ,choose Configure.Choose Cross Company Code Purchasing Organizations on the left-hand side pane.Choose the cross-company purchasing organization 3340 on the left-hand side pane.On the right-hand side, choose Add Relationships.On the Add Relationships for inter-country PORg3340 screen, select Plant 1 AE (3310 ) , choose OK.Wait until activation is completed.On the right-hand side, choose Add Relationships.On the Add Relationships for inter-country PORg3340 screen, select New Plant3320 (3320 ), choose OK.Wait until activation is completed.On the right-hand side, choose Add Relationships.On the Add Relationships for inter-country PORg3340 screen, select New Plant3330 (3330 ), choose OK.Wait until activation is completed. | Plants are assigned to the cross-company purchasing organization. |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |
| 2 | Enter into the OrgStructure-configure | In the Scope and Organizational Structure phase, navigate to the Activities tab and choose Set Up Organization Structure.On the Set Up Organizational Structure, choose the Plant. Under the Additional Relations, select the Plant to Purchasing Organization, choose Assign, select the purchasse Org created previously.The system shows the message:Relationship created successfully.Choose Back to Overview, choose Confirm, and in the Confirm Org Units dialog box, select all checkbox, and choose Confirm. | The Purchase Org is assigned to the Plant. |

|  |
| --- |
| Note Any issues during extending organizational structure, create message to the component SV-CLD-FRM-APP.If you assign plant across countries, the plant can be displayed under the relevant purchasing organization. |

#### Assign Cross-Country Purchasing Organization to Cross-Country Plants

Purpose

The purpose of this activity is to assign cross-country purchasing organization to plants.

Prerequisite

The cross-country purchasing organization has been unassigned from company code. Make sure to use the version of country of the selected plants to do the assignment.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. |  |
| 2 | Access the App | Open Manage Your Solution (F1241) . | The Manage Your Solution (Original) screen displays. |
| 3 | Assign the new purchasing organization to plants | Choose Set Local Version, select a country of plants.On the Configure Your Solution: Realize Phase screen, select Organization in the Application Area field , then navigate to the organization item by choosing the Chevron (>) .On the Organizational Structure step, choose Configure.Choose a plant on the left-hand side pane.On the right-hand side, choose Add Relationships->Purchasing Organization.On the Add Relationships for Plant 1 XX screen, select inter-country PORg XXXX under Cross-Company code (Cross-country) tab, choose OK.Wait until activation is completed.Under Purchasing Organization, the inter-country PORg XXXX is added.Choose the purchase organization just assigned, go into the details, all the plants assigned，both of within the same country and across countries are displayed. | Plants are assigned to the cross-company purchasing organization. |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |
| 2 | Enter into the OrgStructure-configure | In the Scope and Organizational Structure phase, navigate to the Activities tab and choose Set Up Organization Structure.On the Set Up Organizational Structure, choose the Plant. Under the Additional Relations, select the Plant to Purchasing Organization, choose Assign, select the purchasse Org created previously.The system shows the message:Relationship created successfully.Choose Back to Overview, choose Confirm, and in the Confirm Org Units dialog box, select all checkbox, and choose Confirm. | The Purchase Org is assigned to the Plant. |

|  |
| --- |
| Note Any issues during extending organizational structure, create message to the component SV-CLD-FRM-APP.If you assign plant across countries, the plant can be displayed under the relevant purchasing organization. |

#### Extend Business Partner

Purpose

The purpose of this activity is to extend business partner to cross-country purchasing organization created in [Create a New Cross-Country Purchasing Organization](#unique_8) [page ] 7 and company code for cross-company code purchasing.

Prerequisite

The cross-country purchasing organization has been created and unassigned from company code.

Procedure

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. |  |
| 2. | Access the App | Open Maintain Business Partner (BP) | The Maintain Business Partner (Original)screen displays. |
| 3 | Extend supplier purchasing data to cross-country purchasing organization | Choose Open BP.In the field Business Partner, make the following entry and choose Enter:Supplier number: 33300001Choose Switch between Display and Change.Make the following entries:Change in BP role: FLVN01 Supplier(Purchasing)(Defined)Choose Purchasing.In the sub-area Purchasing Organization, choose Purchasing Organizations.In the dialog box Supplier (Purchasing ) Change: Purchasing Organizations, choose Create.In the table Purchasing Organizations, add a new entry below:POrg: <Cross-Country Purchasing organization>, for example, 3340Select above new entry and choose Transfer:In the Purchasing Data tab:Order currency: AEDTerms of Payment: 0004If the supplier is for EU countries purchasing, Incoterms can be entered as below:Incoterms: EXWIncoterms Location 1: Incoterms addressShipping Conditions: 01GR-Based Inv. Verif.: XPurchasing Group: 001Planned Deliv. Time: 2Schema Grp Supp: 01In the Partner Functions tab:OA: 33300001VN: 33300001PI: 33300001Choose Save. | Supplier purchasing data of business partner 33300001 is created. |
| 4 | Extend supplier company code data | Make the following entries:Change in BP role: FLVN00 Supplier (FI) (defined)Choose Company Code.In the Sub-area Company Code, choose Company Codes.In the dialog box Supplier (FI) Change: Company Codes, choose Create.In the table Company Codes, add a new entry as below:Company Code: <ordering company code>3320Supplier: XSelect above new entry and choose Adopt.In the Supplier: Account Management tab:Reconciliation acct: 21100000Sort Key: 009In the Supplier: Payment Transactions tab:Terms of Payment: 0004In the Supplier : Correspondence tab:Account with vendor: 1020-LIEF1Choose Save.Note Extend other suppliers 10300001 by following above steps. | Supplier company code data of business partner 33300001 is created. |

#### Extend Material Master Data

Purpose

The purpose of this activity is to extend material master data to plants 3320 and 3330.

Prerequisite

The material master data and plants have been created.

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |
| 2. | Access the App | Open Create Material. | The Change Condition Record (Original) screen displays. |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen) make the follow entries:Material: TG0011Material Typ : Material generalChoose Select View(s):.Select the following entries and choose Continue (Enter):Sales: Sales Org.Data 1Sales: Sales Org.Data 2Sales: General/Plant DataPurchasingMRP 1MRP 2MRP 3MRP 4General Plant Data / Storage 1General Plant Data / Storage 2Accounting 1Accounting 2Maintain following data and choose Continue:In the Organizational levels subarea:Plant: for example, 3320Storage location: for example, 332ASales Organization.: for example, 3310Distribution Channel: for example, 10In the Copy from subarea:Plant: for example, 3310Storage location: for example, 331ASales Organization: for example, 3310Distribution Channel: for example, 10Create Material screen displays.Make the following data or actions and choose Save. Material data for the selected views is created in plant 1020.Sales: Sales Org. 1 tabDelivering Plant: for example, 3320Sales: Sales Org. 2 tabAll fields unchangedSales: General/Plant tabAll fields unchangedPurchasing tabAll fields unchangedMRP 1 tabAll fields unchangedMRP 2 tabAll fields unchangedMRP 3 tabAll fields unchangedMRP 4 tabAll fields unchangedPlant data / Stor. 1 tabAll fields unchangedPlant data / Stor. 2 tabAll fields unchangedAccounting 1 tab :Standard Price: Change if neededPer Unit Price: Change if neededAccounting 2 tab:All fields unchangedNote Extend TG0011 to plant 3330 by following above steps. | The fields can be informed. |

#### Create an Info Record for Cross-Company Purchasing Organization

Purpose

The purpose of this activity is to create Info Record for the Cross-Company Purchasing Organization created in [Create a New Cross-Country Purchasing Organization](#unique_8) [page ] 7 .

Prerequisite

The cross-country purchasing organization has been created and unassigned from company code.

|  |
| --- |
| Caution For CBC based customers, please follow the note [3159557](https://me.sap.com/notes/3159557) to assign pricing procedure to the central purchasing organization created in previous step. |

Procedure

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Purchaser. |  |
| 2. | Access the App | OpenManage Purchasing Info Records (F1982). | The Create Info Record: Initial (Original) screen displays. |
| 3 | Create an info record for cross-country purchasing organization | Make the following entries：Purchasing Info Record Category: StandardSupplier: 33300001Material: TG0011Purchasing Organization: 3340Plant: <blank>Purch.Group: 001Select the Standard checkbox, then choose Enter.Choose Delivery and Quantity, and make the following entries:Delivery Time Days: 2Order Unit: PCStandard Order Quantity: 1000Conversation from Order Unit: 1Conversation to Base Unit: 1Goods-Receipt-Based Invoice Verification: checkChoose Condition, and make the following entries:Valid From: <today>Valid To: 12/31/9999Amount: 14 AEDPrice unit: 1 PCChoose Save.Note Create info record for suppliers 10300001 by following above steps. Do not insert the tax code value for this supplier. | A purchasing info record is saved. |

#### Create a Condition Record for EU Countries Intrastate Processing

Purpose

The purpose of this activity is to create condition record for EU countries for intrastate processing, as intrastate processing is mandatory for EU countries.

Prerequisite

The cross-country purchasing organization has been created and unassigned from company code.

Procedure

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Tax Specialist. |  |
| 2. | Access the App | OpenSet Tax Rates - Purchasing (MEK2). | The Change Condition Record (Original) screen displays. |
| 3 | Create a condition record | On the Change Condition Records screen, make the following entries and choose Enter:Condition Type: GRWROn the Key Combination screen, choose the radio button of Incoterms (Plant-Specific), select Choose.In the Change Statistical Valu(GRWR): Selection screen make the following entries:Purch. Organization: 3340Plant: 3310Choose Execute.In the Change Statistical Valu(GRWR): Overview screen, make the following entries:Incoterms: EXWAmount: 90Choose Save.Note:Note Create condition records for other plants (3320 ) by following above steps. | A condition record is saved. |

#### Configure Activate HDM for Attachment Object Type (Optional)

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution(F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Activate HDM for Attachment Object Type | Search 105346,choose the item from search result,then choose Configure on the right of configuration steps with name of Activate HDM for Attachment Object Type. | The Change View is displayed. |  |
| 5 | Execute Configuration | Select the Check Box in Activate column for item SUPPLIERINVOICE, choose the item SUPPLIERINVOICE, then double-click the Activate Document Frameworks folder in left Dialog Structure.Choose item DMS Document Management System, then double-click the Maintain Default and Restricted Document Types folder in left Dialog Structure. Select the Check Box in Default column for Doc type SI1.Then choose Save.Double-click the Activate HDM for Attachment Object Types folder in left Dialog Structure.Select the Check Box in Activate column for item SUPPLIERINVOICEUPLOAD, choose the item SUPPLIERINVOICEUPLOAD, then double-click the Activate Document Frameworks folder in left Dialog Structure.Choose item DMS Document Management System, then double-click the Maintain Default and Restricted Document Types folder in left Dialog Structure. Select the Check Box in Default column for Doc type SI1.Then choose Save. | The configuration is changed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate HDM for Attachment Object Type | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate HDM for Attachment Object Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View is displayed. |  |
| 3 | Execute Configuration | Select the Check Box in Activate column for item SUPPLIERINVOICE, choose the item SUPPLIERINVOICE, then double-click the Activate Document Frameworks folder in left Dialog Structure.Choose item DMS Document Management System, then double-click the Maintain Default and Restricted Document Types folder in left Dialog Structure. Select the Check Box in Default column for Doc type SI1.Then choose Save.Double-click the Activate HDM for Attachment Object Types folder in left Dialog Structure.Select the Check Box in Activate column for item SUPPLIERINVOICEUPLOAD, choose the item SUPPLIERINVOICEUPLOAD, then double-click the Activate Document Frameworks folder in left Dialog Structure.Choose item DMS Document Management System, then double-click the Maintain Default and Restricted Document Types folder in left Dialog Structure. Select the Check Box in Default column for Doc type SI1.Then choose Save. | The configuration is changed. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Cross-Company Code Purchasing within a Single Country |  |  |  |
| [Create Purchase Order for One Company Code](#unique_19) [page ] 25[Create Purchase Order for another Company Code (Optional)](#unique_20) [page ] 27 | Purchaser | Manage Purchase Orders (F0842A) | The purchase order is created. |
| [Post Goods Receipt](#unique_21) [page ] 29 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| [Create Supplier Invoice](#unique_22) [page ] 30 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The invoice is created. |
| [Change the Cross-Company Purchasing Organization to be Local (Optional)](#unique_23) [page ] 32 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | The central purchaing organization is changed. |
| [Post Goods Receipt (Optional)](#unique_24) [page ] 33 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| [Create Supplier Invoice (Optional)](#unique_25) [page ] 34 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The invoice is created. |
| [Post Goods Receipt (Optional)](#unique_26) [page ] 36 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| [Set the GR Delivery Completed Indicator(Optional)](#unique_27) [page ] 37 | Purchaser | Change Purchase Order - Advanced (ME22N) | The GR Delivery Completed indicator is set. |
| Cross-Company Code Purchasing across Countries |  |  |  |
| [Create Purchase Order for One Company Code](#unique_28) [page ] 38 | Purchaser | Manage Purchase Orders (F0842A) | The purchase order is created. |
| [Create Purchase Order for another Company Code (Optional)](#unique_29) [page ] 40 | Purchaser | Manage Purchase Orders (F0842A) | The purchase order is created. |
| [Post Goods Receipt](#unique_30) [page ] 42 | Warehouse Clerk. | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| [Create Supplier Invoice](#unique_31) [page ] 43 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The invoice is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Cross-Company Code Purchasing within a Single Country

#### Create Purchase Order

##### Create Purchase Order for One Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

|  |
| --- |
| Note Additional Fiscal Data were delivered to send to the External Tax Partner Engine more specific data about the purchasing scenario that the customer is processing. The user can configure the values for AFD fields that will be available on "Purchase order creation" screen. Those are the new fields Business transaction and Usage purpose.Some cases are standard delivered by SAP, but the customer can also add your own data to the table, according procedure described in Create Master Data for Brazil (JD0_BR).If the iNote scenario applies to your business process, it is necessary to use the Create Purchase Order - Advanced app (ME21N) to create the purchase order.In this app, go to Brazil tab, open the button "Additional Fiscal Data" and input these fields:• Business transactionSelect the option that is related to the purchasing process.• Usage purposeSelect the option that is related to the business process.Le |

|  |
| --- |
| Note Before start to test this step, please check if the central purchase organization 3340 is still a cross-country purchasing organization, if it's not, please follow the step [Unassign Company Code for Cross-Country Purchasing Organization](#unique_10) [page ] 10 in preliminary steps. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The Purchase Order screen is shown. |  |
| 4 | Enter the general data | Make the following entries:On the General Information:Supplier: 33300001Company Code: 3310Purchasing Organization:3340Purchasing Group:001Currency: AEDIn the Items section, choose Create, and make the following entries:Material: TG0011Plant: 3310Order Quantity: 10Add another item:Material: TG0011Plant: 3320Order Quantity: 20Net Order Price: x (The price should be retrieved from the central purchasing organization info record.)Navigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.In the Item section, choose Process Flow tabThe next data will be displayed after the article is entered:Goods Receipt: yesInvoice Receipt: xMake sure GR-Based Inv. Verif has been selectedIn the Item section, choose Delivery Details tabStorage Location: 331A or 332AIn the Item section, choose Schedule Lines tab.Delivery date: <a date in the future>Please choose a quantity and total net amount of purchase order less than 500AED (for Purchase Groups = 001)Choose Apply. | The Purchase Order screen is displayed. |  |
| 5 | Check and save Purchase Order | Choose Order to save the Purchase Order.If the system gives you the message, then choose Messages.Check and correct the entries for errors. | A Purchase Order is created . |  |

##### Create Purchase Order for another Company Code (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The Purchase Order screen is shown. |  |
| 4 | Enter Purchase Order data | Make the following entries:On the General Information:Supplier: 33300001Company Code: 3320Purchasing Organization: 3340Purchasing Group:001Currency: AEDIn Items section, choose Add.Material: TG0011Plant: 3330Order Quantity: xNet Order Price: xNavigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.In Item section, choose Process Flow tab.The next data will be displayed after the article is enteredGoods Receipt: yesInvoice Receipt: xGoods-Receipt-Based Invoice Verification: <Selected>In Item section, choose Delivery Details tab:Storage Location: 333AIn the Item section, choose Schedule Lines tab.Delivery date: <a date in the future>Choose a quantity and total net amount of purchase order less than 500 AED (for Purchase Groups = 001Choose Apply. | The Purchase Order screen is displayed. |  |
| 5 | Save Purchase Order | Choose Order to save the Purchase Order.If the system gives you the message, then choose Messages.Check and correct the entries for errors.Choose Order to save the purchase order. | A new Purchase Order is created . |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Post Goods Receipt for Pur chase Order | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt screen is displayed. |  |
| 3 | Enter Purchase Order | Enter one of the Purchase Order number created in [Create Purchase Order for One Company Code](#unique_19) [page ] 25 and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter :Delivery Note: <xxx>Printing: Individual slip |  |  |
| 5 | Post | Select the first items for which a goods receipt to be posted.Delivered: 5Choose Post. | The system is displayed the message1 Material document(s) posted: xxx. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as Accounts Payable Accountant . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Tile | Open Create Supplier Invoice (F0859). | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make thefollowing entries:Transaction: InvoiceCompany Code: 3310 （Enter the company code same as the PO that you want to create supplier invoice for)Gross Invoice Amount : XXXCurrency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: XXX(reference invoice number from invoicing party)Invoice Party:33300001In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310 （Enter the company code same as the PO that you want to create supplier invoice for)Gross Invoice Amount : XXXCurrency: XXX (change the invoice currency)Invoice Date: <Today>Posting Date: <Today>Reference: XXX(reference invoice number from invoicing party)Invoice Party:33300001Select See More at header area, make the following entries.Exchange Rate: XXXNote If you activate HDM for Attachment Object Types SUPPLIERINVOICE and SUPPLI-ERINVOICEUPLOAD via SSCUI 105346 Activate HDM for Attachment Object Type in step[Configure Activate HDM for Attachment Object Type (Optional)](#unique_17) [page ] 21, you can select the Doc. Type to Upload in the tab Attachements, the documents of SI1 and SI2 are protected, the documents of SAT and GOS can be deleted later via app Display Supplier Invoice - Advanced. | The New Supplier Invoices screen is displayed. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References section, add the references.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <PO Number> created in [Create Purchase Order for One Company Code](#unique_19) [page ] 25 | All items of the referenced Purchase Or der are added to the Invoice Items sec tion. |  |
| 5 | Enter Invoice Item data | Select the Invoice Items you want to create invoice for, and make the following entries:Amount: checkQuantity: checkTax Code: check (If there is no tax, specify the tax code <Input Tax Code> ).Tax: check if there is tax code information and enter the tax amount if the tax code value is greater than zero.Calculate the tax by choosing Propose Tax.Check the balance (difference between the calculated amount and the gross Amount you entered in step 3).. | The invoice data is entered. |  |
| 6 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation DetailsDetails area. | The Supplier Invoice is simulated. |  |
| 7 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

#### Change the Cross-Company Purchasing Organization to be Local (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is necessary only when the cross-company purchasing organization becomes a local one. The cross-company purchasing organization is changed to be local.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration . |  |
| 2 | Access the App | Open Manage Your Solution (F1241) tile. | The Manage Your Solution screen displays. |
| 3 | Change the central purchasing organization | Choose Set Local Version, select United Arab Emirates.Choose Configure Your Solution.Enter Organization in the Application Area filter bar.Find the entry with the item name Organization and choose the arrow icon at the item end.Choose Orgnizational Structure and choose Configure.Choose the Cross Company Code … , and choose Purchasing organization3340 on the left-hand side pane.Choose Edit Company Code Assignment on the right-hand pane.Select 3310 on the Edit Company Code Assignment screen, then choose OK. | The cross-company purchasing organization is changed to be local. |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |
| 2 | Open Assign purchasing org to company code | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign purchasing organization to company code.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign purchasing organization -> company code: Overviewscreen displays. |
| 3 | Change the central purchasing organization | On the Change View "Assign Purchaingg Organization → Company Code": Overview, choose the item line, edit the company code and choose Save. | The cross-company purchasing organization is changed to be local. |

#### Post Goods Receipt (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Some of the goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt screen is displayed. |  |
| 3 | Enter general data | Enter the Purchase Order number created in section [Create Purchase Order for One Company Code](#unique_19) [page ] 25 and choose Enter.Make the following entries and Choose Enter :Delivery Note: <xxx>Printing: Individual slipSelect the first item for which a goods receipt is to be posted. Make the following entries:Delivered: 5 PC | The system displays the data for the goods receipt. |  |
| 4 | Post | Choose Post. | The system displays the message1 material document(s) posted: xxx . |  |

#### Create Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad asAccounts Payable Accountant . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make thefollowing entries.Transaction: InvoiceCompany Code: 3310 （Enter the company code same as the PO that you want to create supplier invoice for)Gross Invoice Amount : XXXCurrency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party: 33300001In case of purchase orders created with foreign currency in your system, makethe following entries.Transaction: <Invoice>Company Code: 3310 （Enter the company code same as the PO that you want to create supplier invoice for)Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <XXX>(reference invoice number from invoicing party)Invoice Party: 33300001Select See More at header area, make the following entries:Exchange Rate: <XXX>In the Purchasing Document References section, add the references.Make the following entries:Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <xxx>(The Purchase Order Number created in section [Create Purchase Order for One Company Code](#unique_19) [page ] 25)Select the Invoice Items you want to create invoice for.Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order).In the section Tax, enter the tax amount if there is tax code value.Calculate the tax by choosing Propose Tax.Check the balance (difference be tween the calculated amount and the gross Amount you entered in step 3).Choose Simulate. You can check the simulation results in Simulation Overview and Simulation Details area. | The Supplier Invoice is simulated. |  |
| 4 | Post Invoice | Choose Post. | The invoice is posted. The system mes sage is shown. |  |

#### Post Goods Receipt (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Some of the goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as Warehouse Clerk . | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Post Goods Receipt for Purchase Order | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt screen is displayed. |  |
| 3 | Enter the general data | Enter the Purchase Order number created in [Create Purchase Order for One Company Code](#unique_19) [page ] 25 and choose Enter.on the Goods Receipt screen. Make the following entries and Choose Enter :Delivery Note: <xxx>Printing: Individual slipSelect the second item for which a goods receipt is to be posted. Make the following entries:Delivered: 15 PC |  |  |
| 4 | Post | Choose Post. | The system displays the message: 1 Material document(s)posted xxx. |  |

#### Set the GR Delivery Completed Indicator(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

No more goods ordered can be received, the delivery completed indicator is to be set on the purchase order item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Change Purchase Order Advanced | Open Change Purchase Order - Advanced (ME22N). | The Standard PO XXX Created by XXX screen is displayed. |  |
| 3 | Enter the general data | Without making any selection, chooseOther Purchase Order, and make the following entries:Purchase Order: <xxx> (The PO created in [Create Purchase Order for One Company Code](#unique_19) [page ] 25)Choose Other Document.Choose item 20, go to tab Delivery, check the field Deliv. Compl.Choose Save. | The Document is saved successfully. |  |

### Cross-Company Code Purchasing across Countries

#### Create Purchase Order

##### Create Purchase Order for One Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create . | The Purchase Order screen is displayed. |  |
| 4 | Enter the general data | Make the following entries:On the General Information:Supplier: 12300001Note For European Union (EU) member states, choose a Supplier of a country of EU member state.Company Code: 3310Purchasing Organization:3340Purchasing Group:001Currency: AEDChoose Incoterms tab, and check the following fields:Incoterms: EXWIncoterms Location 1: Plant address (Change if necessary)In the Items section, choose Create, and make the following entries:Material: TG0011Plant: 3310Order Quantity: 10Add another item:Material: TG0011Plant: 3320Order Quantity: 20Net Order Price: x (The price should be retrieved from the central purchasing organization info record.)Navigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.In the Item section, choose Process Flow tab.The next data will be displayed after the article is entered:Goods Receipt: yesInvoice Receipt: xMake sure Goods-Receipt-Based Invoice Verification has been selected.In the Item section, choose Delivery Details tab:Storage Location: 331A or 332AIn the Item section, choose Schedule Lines tab.Delivery date: <a date in the future>Choose a quantity and total net amount of purchase order less than 500 USD (for Purchase Groups = 001)Choose Apply. | The Purchase Order screen is displayed. |  |
| 5 | Check and save Purchase Order | Choose Order to save the Purchase Order.If the system gives you the message, then choose Messages.Check and correct the entries for errors. | A Purchase Order is created . |  |

##### Create Purchase Order for another Company Code (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The Purchase Order screen is shown. |  |
| 4 | Enter Purchase Order data | Make the following entries:On the General Information:Supplier: 12300001Note For European Union (EU) member states, choose a Supplier of a country of EU member state.Company Code: 3320Purchasing Organization: 3340Purchasing Group:001Currency: AEDIn Items section, choose Create.Material: TG0011Plant: 3330Order Quantity: xNet Order Price: xNavigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.In Item section, choose Process Flow tab.The next data will be displayed after the article is entered.Goods Receipt: yesInvoice Receipt: xMake sure GR-Based Inv. Verif has been selected.In Item section, choose Delivery Details tab.Storage Location: 333AIn the Item section, choose Schedule Lines tab.Delivery date: <a date in the future>Choose a quantity and total net amount of purchase order less than 500 USD (for Purchase Groups = 001).Choose Apply. | The Purchase Order screen is displayed. |  |
| 5 | Save Purchase Order | Choose Order to save the Purchase Order.If the system gives you the message, then choose Messages.Check and correct the entries for errors.Choose Order to save the purchase order. | A new Purchase Order is created . |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Post Goods Receipt for Pur chase Order | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt screen is displayed. |  |
| 3 | Enter Purchase Order | Enter one of the Purchase Order number created in [Create Purchase Order for One Company Code](#unique_28) [page ] 38 and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter :Delivery Note: <xxx>Printing: Individual slip |  |  |
| 5 | Post | Select the first items for which a goods receipt to be posted.Deliverd: XXChoose Post. | The system is displayed the message1 Material document(s) posted: xxx. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation.

|  |
| --- |
| Note For EU countries only. Intrastate is mandatory for the trade between European Union (EU) member states. Please follow SI BDT test script and create the intra-state declarations after invoice is created. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as Accounts Payable Accountant . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Tile | Open Create Supplier Invoice (F0859). | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make thefollowing entries:Transaction: InvoiceCompany Code: 3310 （Please enter the company code same as the PO company code that you want to create supplier invoice for)Gross Invoice Amount : XXXCurrency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: XXX (reference invoice number from invoicing party)Invoice Party: 12300001Note For European Union (EU) member states, choose a Invoice Party of a country of EU member state.In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310 （Enter the company code same as the PO that you want to create supplier invoice for)Gross Invoice Amount : XXXCurrency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: XXX(reference invoice number from invoicing party)number from invoicing party)Invoice Party: 12300001Note For European Union (EU) member states, choose a Invoice Party of a country of EU member state.Select See More at header area, make the following entries.Exchange Rate: XXX | The New Supplier Invoices screen is displayed. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References section, add the references.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <PO Number> created in [Create Purchase Order for One Company Code](#unique_28) [page ] 38 | All items of the referenced Purchase Or der are added to the Invoice Items sec tion. |  |
| 5 | Enter Invoice Item data | Select the Invoice Items you want to create invoice for, and make the following entries:Amount: checkQuantity: checkTax Code: check (If there is no tax, specify the tax code <Input Tax Code> ).Tax: check if there is tax code information and enter the tax amount if the tax code value is greater than zero.Calculate the tax by choosing Propose Tax.Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The invoice data is entered. |  |
| 6 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation DetailsDetails area. | The Supplier Invoice is simulated. |  |
| 7 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

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
> Flagged while digesting this document, not verified: Purchase order value limit is 'less than 500 AED' in the within-country scenario but 'less than 500 USD' in the across-countries scenario, although the PO currency is AED in both.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/direct-procurement-with-inbound-delivery-2tx-ae-test-script-sap-s-4han]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-procurement-of-direct-mat]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2R3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 69,774 chars in the whole document
