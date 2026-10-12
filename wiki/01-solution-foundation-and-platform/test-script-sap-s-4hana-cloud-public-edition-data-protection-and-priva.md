---
id: 01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-data-protection-and-priva
title: "Test Script: SAP S/4HANA Cloud Public Edition - Data Protection and Privacy (5LE_AE) (5LE_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 5LE (AE): ILM-based blocking/deletion, information retrieval, consent administration and read access logging in S/4HANA Cloud Public Edition 2608."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/information-lifecycle-and-data-protection]
aliases: [5LE_S4CLD2608_BPD_EN_AE]
keywords: [Information Lifecycle Management and Data Protection, data protection, blocking and deletion, information lifecycle management, master data blocking, master data unblocking, information retrieval, consent management, archiving and destruction, read access logging]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5LE_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1108
topic: 01-solution-foundation-and-platform/information-lifecycle-and-data-protection
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP S/4HANA Cloud Public Edition - Data Protection and Privacy (5LE_AE) (5LE_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5LE_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Information Lifecycle Management and Data Protection** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Data Protection and Privacy (5LE_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857394)

[2 Prerequisites 4](#_Toc232857395)

[2.1 System Access 4](#_Toc232857396)

[2.2 Roles 4](#_Toc232857397)

[2.3 Additional Manual Configuration 5](#_Toc232857398)

[2.4 Business Conditions 5](#_Toc232857399)

[2.5 Preliminary Steps 6](#_Toc232857400)

[2.5.1 Simplified Blocking and Deletion 6](#_Toc232857401)

[2.5.1.1 Create Customer and Business Partner Master Data 6](#_Toc232857402)

[2.5.1.2 Create Transactional Data (Sales Orders) 7](#_Toc232857403)

[2.5.1.3 Create ILM Rule Group (SD_VBAK) 8](#_Toc232857404)

[2.5.1.4 Maintain Authorization Groups for Blocking 9](#_Toc232857405)

[2.5.1.5 Define ILM Policy for Transactional Data (SD_VBAK) 10](#_Toc232857406)

[2.5.1.6 Assign Application Rule Variants and Groups for the Customer/ Supplier EoP Check 11](#_Toc232857407)

[2.5.1.7 Define ILM Policies for Customer and Business Partner Master Data 13](#_Toc232857408)

[2.5.2 Information Retrieval 14](#_Toc232857409)

[2.5.2.1 Create Purposes for Information Retrieval 14](#_Toc232857410)

[3 Overview Table 16](#_Toc232857411)

[4 Test Procedures 18](#_Toc232857412)

[4.1 Simplified Blocking and Deletion 18](#_Toc232857413)

[4.1.1 Blocking and Deletion of Transactional Data 18](#_Toc232857414)

[4.1.1.1 Block Sales Order 18](#_Toc232857415)

[4.1.1.2 Destroy Archived Sales Order 19](#_Toc232857416)

[4.1.2 Blocking, Unblocking and Deletion of Master Data 21](#_Toc232857417)

[4.1.2.1 Block Customer and Business Partner Master Data 21](#_Toc232857418)

[4.1.2.1.1 Successful Blocking of Customer and Business Partner Master Data 21](#_Toc232857419)

[4.1.2.1.2 Unsuccessful Blocking of Customer and Business Partner Master Data 22](#_Toc232857420)

[4.1.2.2 Unblock Business Partner Master Data 23](#_Toc232857421)

[4.1.2.3 Unblock Customer Master Data 25](#_Toc232857422)

[4.1.2.4 Destroy Customer and Business Partner Master Data 26](#_Toc232857423)

[4.2 Information Retrieval 28](#_Toc232857424)

[4.2.1 Trigger a Search for Personal Data 28](#_Toc232857425)

[4.2.2 View the Search Results 30](#_Toc232857426)

[4.3 Consent Administration 31](#_Toc232857427)

[4.3.1 Import Consent Data from File 31](#_Toc232857428)

[4.3.2 Manage Consents 32](#_Toc232857429)

[4.4 Read Access Logging 33](#_Toc232857430)

## Purpose

Overview

When configuring, applying, or operating an IT landscape, companies have always regarded general, country/region-specific, local, and industry-specific legislation. General data protection regulation is associated with numerous legal requirements and privacy concerns that may affect the configuration and setup of an IT system. For example, this may include commercial, fiscal, accounting, or specific tax requirements.

SAP S/4HANA Cloud Public Edition supports customers in their journey to comply with relevant data protection and privacy requirements. SAP S/4HANA Cloud Public Edition supports data protection by providing security features and specific data-protection-relevant functions, such as simplified blocking and deletion of personal data, information retrieval framework, read access logging, and consent management. SAP doesn't provide legal advice in any form. The used definitions and other terms don't necessarily refer to specific legislation.

|  |
| --- |
| Note SAP does not provide legal advice in any form. The used definitions and other terms do not necessarily refer to specific legislation. |

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
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Data Privacy Specialist | SAP_BR_DATA_PRIVACY_SPECIALIST | Data Protection and Privacy - Master Data / Data Protection and Privacy | SAP_CA_SPT_DPP_PC / SAP_BR_DATA_PRIVACY_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Data Privacy Specialist - Consent Management | SAP_BR_DATA_PRIV_SPEC_CONS | Overview - Consents | SAP_BR_DATA_PRIV_SPEC_CONS |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/30f62cf23b08fcd6660c33c24dba774f)

### Business Conditions

Before you can test this scope item, the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| 1KA - Information Lifecycle Management | Data protection is based on settings made in SAP Information Lifecycle Management (ILM).Refer to the respective set-up instructions guide and the test script before initiating the test activities for 5LE.The blocking and deletion of personal data requires maintaining residence and retention rules for both application and master data. In this context, you must also maintain audit areas, create ILM object groups and and maintain authorization groups to manage the read access to blocked data. The actual blocking and deletion of data is also performed using SAP ILM.In addition, the business-specific output of search results for the information retrieval feature, i.e. what data was collected for which purpose, is based on the purposes you define in ILM.For more information about ILM, see scope item [1KA](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1KA). |

### Preliminary Steps

#### Simplified Blocking and Deletion

To test the blocking and deletion of personal data, you must first create sample data (master data and transactional data) in your system and define the relevant ILM settings for that data. After you've maintained residence and retention periods for the data using SAP Information Lifecycle Management, the actual blocking and deletion of data can be tested as described in section 4.1.

Follow the preliminary steps in the order they appear in the following section.

##### Create Customer and Business Partner Master Data

Purpose

This preliminary step shows you how to create customer master data that is used for testing the blocking and deletion of master data.

Create two customer master data records:

- CUS01 is used to demonstrate the successful blocking procedure. It's assigned to a sales order that will later be blocked and deleted, therefore blocking and deletion of CUS01 is also allowed.
- CUS02 is used to demonstrate the unsuccessful blocking procedure. It's assigned to a sales order that will be kept in status "Open" and thus is still relevant for business activities. Blocking and deletion for the master data record is therefore not allowed.

When creating a customer, the system automatically creates a corresponding business partner. Therefore, in the subsequent steps for blocking and deletion, both customer and business partner master data must be considered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the App | Open the Manage Customer Master Data (F0850A) app. | On the entry screen of the app, you get an overview of all existing customers. |  |
| 3 | Create a Sales Order | Create new customer master data by choosing Create and then Person. | A dialog window appears on which you must maintain the customer-specific data. |  |
| 4 | Maintain Customer Master Data Details | On the dialog window, fill out the mandatory entry fields with the following values:BP Role: FLCU01 - CustomerLast Name: <CUS01>Country/ Region: AE (United Arab Emirates)Language: ArabicSales Organization:3310 (Dom. Sales Org)Currency: AED (UAE Dirham)Choose Ok. | You maintained the basic data for creating a customer. After choosing Ok, you're directed to the Details screen. |  |
| 5 | Confirm Entry | On the Details screen, you can double-check your entries. If everything looks okay, choose Create. No further input is needed. | You created customer<CUS01>.On the Details screen in the title the customer name is displayed e.g. CUS01 and below in the subtitle the business partner ID, e.g. 10XXXXX. |  |
| 6 | Create a Second Customer | Repeat steps 1-5 to create another customer master data record. | You created customer <CUS02>.On the Details screen in the title the customer name is displayed e.g. CUS01 and below in the subtitle the business partner ID, e.g. 10XXXXX. |  |

##### Create Transactional Data (Sales Orders)

Purpose

This preliminary step shows you how to create two sales orders that serve as test data for the follow-on processes described in this script. One of these sales orders is set to status Completed, this status is required for archiving and thus blocking the document in the system. To test the unsuccessful blocking procedure (see section [Unsuccessful Blocking of Customer and Business Partner Master Data](#unique_10) [page ] 22), the other sales order is kept in status Open.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open the Create Sales Orders - VA01 (VA01) app. |  |  |
| 3 | Create Sales Orders | To create a sales order, fill out the mandatory entry fields with the following values:Order Type: CCFU (Consignment Fill-Up)Sales Organization: 3310 (Dom. Sales Org)Choose Continue. |  |  |
| 4 | Maintain Sales Order Details | On the Create Consignment Fill-Up: Overview screen, fill out the following fields that are man-datory to create a sales order:Sold-To: <CUS01> (ID of the customer you created in step [2.5.1.1](#unique_8))Customer Reference: <free text entry>Incoterms: <CIF>Inco. Location 1: <select a location available in your system>In addition, you must add a material to the sales order. For this, choose Create Item in the All Items section and add any material available in your system.Then choose Save. Note down the number of the newly created sales order. | You created a new sales order with customer <CUS01> assigned to it. |  |
| 5 | Access the App | On the Fiori Launchpad, open the Change Sales Orders app. |  |  |
| 6 | Set Sales Order to Completed | On the entry screen of the app, use the Order field to enter the number of the sales order you created. Choose Search.On the upcoming screen, go to the Reason for Rejection tab and select a rejection reason from the dropdown list in column Reason for Rejection.Choose Save. | You rejected the only item assigned to the sales order. Its overall status is moved to Completed. |  |
| 7 | Create a Second Sales Order | Repeat the steps 1–4 to create another sales order.This sales order is kept in status Open, so that it can't be archived and thus is used to demonstrate the unsuccessful blocking procedure. Note down the number of the newly created sales order. | You created a new sales order with customer <CUS02> assigned to it. |  |

##### Create ILM Rule Group (SD_VBAK)

Purpose

This preliminary step shows you how to create ILM rule groups that are an important requirement for creating application rule variants for the customer/ supplier EoP check (see step [Assign Application Rule Variants and Groups for the Customer/ Supplier EoP Check](#unique_12) [page ] 11).

|  |
| --- |
| Note This step is part of the scope item 1KA. In the following section, you find a high-level overview of the required settings to be made in the ILM apps. For a detailed description on how to work with the app, please refer to the test script of scope item 1KA. |

Procedure

Table 1:

| Test Step | Test Step Name | Description | More Information |
| --- | --- | --- | --- |
| 1 | Create ILM Object Group | As a prerequisite for creating rule groups, you must first create an ILM object group. In the Maintain ILM Object Groups configuration activity, create a new object group with policy category retention rules and assign ILM object SD_VBAK to it. | Test script of scope item 1KA, see section Maintain ILM Object Groups. |
| 2 | Create a Rule Group for SD_VBAK | Edit your newly created ILM object group and add a rule group to it. You don't have to maintain any rules at this point. Note down the name of your rule group and choose Save. |  |

##### Maintain Authorization Groups for Blocking

Purpose

This preliminary step shows you how to maintain authorization groups that ensure that personal data in the archive is blocked and an authorization check for the read access to the archive is done. The authorization group created in this step will be used during rule maintenance for ILM object SD_VBAK, as explained in step [Define ILM Policy for Transactional Data (SD_VBAK)](#unique_14) [page ] 10. If you don't assign an authorization group, archived data can be read by anyone with the authorization to read from archive.

|  |
| --- |
| Note This step is part of the scope item 1KA. In the following section, you find a high-level overview of the required settings to be made in the ILM apps. For a detailed description on how to work with the app, please refer to the test script of scope item 1KA. |

Procedure

Table 2:

| Test Step | Test Step Name | Description | More Information |
| --- | --- | --- | --- |
| 1 | Create Authorization Group | In your configuration environment, navigate to the configuration activity Maintain Authorization Groups for ILM Blocking.Create a new authorization group. You must only enter a name and a description. Choose Save. | Set-Up instructions guide of scope item 1KA, see section Maintain Authorization Groups for ILM Blocking. |
| 2 | Assign Authorization Group to Business Catalog External Auditing | Users that should be allowed to read blocked data can be assigned the business catalog Data Privacy - External Auditing (SAP_CA_BC_EXTERNAL_AUDIT_PC). Use restriction type BLOCKED_DATA of this catalog to enter your newly created authorization group.That way, only users with the External Auditing catalog assigned in combination with the specified authorization group are able to read blocked data belonging to ILM object SD_VBAK. | Product assistance for SAP S/4HANA Cloud Public Edition, see [How to Define Authorizations Based on Restrictions.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/c926d691d7144f7dba16f8e12ad81d28.html) |
| 3 | Use Authorization Group in Policy Maintenance | In the following step, assign the newly created authorization group to the ILM policy for SD_VBAK. | [Define ILM Policy for Transactional Data (SD_VBAK)](#unique_14) [page ] 10 |

##### Define ILM Policy for Transactional Data (SD_VBAK)

Purpose

This preliminary step shows you how to maintain the ILM settings that are required for blocking and deleting application data.

Firstly, create residence rules for the ILM object SD_VBAK. These rules determine when data can be archived once it has reached the end of business. For this test scenario, the residence rules for SD_VBAK is set to 0 days.

Next, create retention rules for the ILM object SD_VBAK. These rules specify when the data can be deleted from the archive. For testing purposes, the retention period is set to only 1 day (minimum time period).

For more information on defining residence rules in the context of data protection and privacy, refer to[ILM Settings for Data Protection](https://help.sap.com/docs/SAP_S4HANA_CLOUD/55a7cb346519450cb9e6d21c1ecd6ec1/5604718fdc70485fb62a13f347d92cd3.html).

|  |
| --- |
| Note This step is part of the scope item 1KA. In the following section, you find a high-level overview of the required settings to be made in the ILM apps. For a detailed description on how to work with the app, please refer to the test script of scope item 1KA. |

Procedure

Table 3:

| Test Step | Test Step Name | Description | More Information |
| --- | --- | --- | --- |
| 1 | Create a New Audit Area | To define retention rules for ILM object SD_VBAK, you must create a new audit area.In your configuration environment, open the configuration activity Maintain Audit Area. Create a new audit area <Z_TEST> for policy category RTP and assign an ILM object SD_VBAK to it. | Set-up instructions of scope item 1KA, see section Maintain Audit Areas. |
| 2 | Define Retention Rules for SD_VBAK | In your configuration environment, open the configuration activity Maintain ILM Policies and Rules. Define the following retention periods for your newly created audit area for ILM object SD_VBAK:Rule Group: <name of rule group created in step 2.5.1.3>Min Retention Period: 1Time unit: DayTime reference: Last Changed OnAuthorization Group: <name of authorization group created in 2.5.1.4>Alternatively, you can use the Manage ILM Business Rules app, which helps you in creating residence and retention periods based on the data controllers and purposes that exist in your system | Set-up instructions of scope item 1KA, see sections Maintain ILM Policies and Manage ILM Business Rules. |

##### Assign Application Rule Variants and Groups for the Customer/ Supplier EoP Check

Purpose

This preliminary step shows you how to assign rule variants and groups for the EoP check for customer master data. The use of application rule variants is necessary if the system must consider more than one residence or retention rule for an application-specific ILM object (for example, because you must maintain different rules for a cus-tomers and its corresponding business partner). Application rule variants provide a mapping that allows the system to determine the correct end of residence/ end of retention date for business partner master data.

|  |
| --- |
| Note This process step is optional. In this test scenario, the system only has one retention policy to consider for ILM object SD_VBAK, however, for demonstration purposes you can follow the instructions outlined in the table below to learn more about the use of application rule variants. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | In the Manage Your Solution (F1241) app, choose Configure Your Solution .Note You might need to set the country version first (see the button on the lower right side of the screen). | You've accessed Configure your Solution and set a specific country/region, for example: Germany (DE). |  |
| 3 | Start Configuration Activity | On the Configure Your Solution screen, type in Data Protection in the Search field. From the search results, choose the configuration item Data Protection Settings.On the next screen, all configuration steps of the item are listed. In the row for Assign Rule Variants and Groups for the Customer/Supplier EoP Check, choose Configure to start the activity. |  |  |
| 4 | Create a New Variant | To create a new application rule variant, choose New Entries and enter the following information:ID Type: Customer Master DataApplication Name: ERP_SDApplication Rule Variant: <CCFU>Application Rule Variant Description: <SD_VBAK CCFURule Group: <name of rule group created in step 2.5.1.3>Choose Save. | You've assigned the application rule variant <CCFU> with application ERP_SD for the customer master data EoP check. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Rule Variants and Groups for the Customer/Supplier EoP Check.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | You've accessed Configure your Solution and set a specific country/region, for example: Germany (DE). |  |
| 3 | Create a New Variant | To create a new application rule variant, choose New Entries and enter the following information:ID Type: Customer Master DataApplication Name: ERP_SDApplication Rule Variant: <CCFU>Application Rule Variant Description: <SD_VBAK CCFURule Group: <name of rule group created in step 2.5.1.3>Choose Save. | You've assigned the application rule variant <CCFU> with application ERP_SD for the customer master data EoP check. |  |

##### Define ILM Policies for Customer and Business Partner Master Data

Purpose

For the system to determine if a certain master data record can be blocked or deleted, you must first define residence and retention periods for that data using Information Lifecycle Management. This preliminary step shows you how to maintain policies for master data using the application rule variant you created in the previous step.

|  |
| --- |
| Note This step is part of the scope item 1KA. In the following section, you find a high-level overview of the required settings to be made in the ILM apps. For a detailed description on how to work with the app, please refer to the test script of scope item 1KA. |

Procedure

Table 4:

| Test Step | Test Step Name | Description | More Information |
| --- | --- | --- | --- |
| 1 | Edit Audit Area BUPA_DP | The SAP-delivered audit area BUPA_DP is used to maintain residence rules for master data ILM objects CA_BUPA, FI_ACCPAYB, and FI_ACCRECV. Maintaining ILM policies in this audit area is required for the end of purpose (EoP) check for business partners. For retention rules, it's not mandatory to use this audit area.Assign ILM objects CA_BUPA and FI_ACCRECV to audit area BUPA_DP. | Set-up instructions guide of scope item 1KA, see section Maintain Audit Areas. |
| 2 | Define Residence Rules for FI_ACCRECV | In configuration activity ILM Policies and Rules, create a new ILM policy for ILM object FI_ACCRECV called <ERP_SD> (audit area: BUPA_DP) and add the following residence rule to it:Application Name: ERP_SDApplication Rule Variant: <CCFU>Residence Period: 1Residence Period Unit: DayTime Reference: Start of Retention PeriodYou must create a second ILM policy for FI_ACCRECV called <ERP_CUST> (audit area: BUPA_DP) and add the following residence rule to it:Application Name: ERP_CUSTResidence Period: 1Residence Period Unit: DayTime Reference: Start of Retention Period | Set-up instructions guide of scope item 1KA, see sections Maintain ILM Policies |
| 3 | Define Retention Rules for Customer (FI_ACCRECV) | In configuration activity Maintain ILM Policies and Rules app, create a new ILM policy for ILM object FI_ACCRECV called <ERP_SD> (audit area: BUPA_DP) and add the following retention rule to it:Application Name: ERP_SDApplication Rule Variant: <CCFU>Min. Retention Time: 1Max. Retention Time: 1Retention Time Unit: DayTime Reference: Start of Retention Period |  |
| 4 | Define Residence and retention Rules for Business Partner (CA_BUPA) | Repeat steps 2-4 for the ILM Object CA_BUPA. Instead of ERP_SD and ERP_CUST, use the application name BUP. |  |

#### Information Retrieval

##### Create Purposes for Information Retrieval

Purpose

This preliminary step shows you how to create purposes that are required for the business-specific output of search results, that is which data was collected for which purpose. For this, the information retrieval apps use purposes that were created in a central configuration activity.

|  |
| --- |
| Note This step is part of the scope item 5LE. In the following section, you find a high-level overview of the required settings to be in your configuration environment. For a detailed description, please refer to the set-up instructions guide of scope item 5LE. |

Procedure

Table 5:

| Test Step | Test Step Name | Description | More Information |
| --- | --- | --- | --- |
| 1 | Maintain Purposes | In your configuration environment, navigate to the configuration activity Maintain Purposes.Choose New Entries, enter a name and a description for your purpose. | Set-up instructions guide of scope item 5LE, see section Maintain Purposes. |
| 2 | Assign ILM Object to Purpose | In your configuration environment, navigate to the configuration activity Maintain IRF Purposes (configuration activity 103525). Click button Refresh Purpose. The purpose, which was created in the previous step, will appear in the list.Select the purpose and double-click the folder Assign ILM ObjectsNote Since the starting point for the data retrieval is a business partner number, you must make sure that the ILM object CA_BUPA is assigned to the purpose. |  |

## Overview Table

The Data Protection and Privacy (5LE) scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 6: Simplified Blocking and Deletion

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Blocking of Transactional Data](#unique_18) | Data Privacy Specialist | Manage Archiving Variants (F0627A)Monitor Archiving Jobs (F0510A) |  |
| [Deletion of Transactional Data](#unique_19) | Data Privacy Specialist | ILM Data Destruction (F2662) |  |
| [Blocking of Customer and Business Partner Master Data](#unique_20) | Data Privacy Specialist | Block Master Data - Customer & Supplier (CVP_PRE_EOP)Monitor Archiving Jobs (F0510A) |  |
| [Unblocking of Customer and Business Partner Master Data](#unique_21) | Data Privacy Specialist | Unblock Request - Master Data (BUP_REQ_UNBLK) |  |
| [Deletion of Customer and Business Partner Master Data](#unique_22) | Data Privacy Specialist | ILM Data Destruction (F2662) |  |

Table 7: Information Retrieval

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Trigger a Search for Personal Data](#unique_23) [page ] 28 | Data Privacy Specialist | Start Data Collection (DTINF_START_COLL) |  |
| [View the Search Results](#unique_24) [page ] 30 | Data Privacy Specialist | Process Data Collection Results (DTINF_PROC_COLL) |  |

Table 8: Consent Administration

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Import Consent Data from File](#unique_25) [page ] 31 | Data Privacy Specialist - Consent Management | Import Consents from File (F3306) |  |
| [Manage Consents](#unique_26) [page ] 32 | Data Privacy Specialist - Consent Management | Manage Consents (F3307) |  |

Table 9: Read Access Logging

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Read Access Logging](#unique_27) [page ] 33 | AdministratorData Privacy Specialist | Set Up the Read Access configuration |  |

|  |
| --- |
| Note If you can't find an app that is described in this table on your SAP Fiori launchpad, choose your user icon in the upper left corner of the SAP Fiori launchpad screen and go to the App Finder. Search for the app and assign it to the appropriate catalog. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Simplified Blocking and Deletion

In this section, an overall process for blocking and deletion of both master and transactional data is described with sample data for testing purposes. Before moving on with this section, please make sure that you've completed the preliminary steps described in section [Prerequisites](#unique_2) [page ] 4.

SAP does not assume any warranty or liability for the correct definition of your ILM policies or your adherence to retention periods required by law. For this reason, the settings of the ILM policies as well as the data used in this section are only for testing purpose. This data shall not be used in the production system.

#### Blocking and Deletion of Transactional Data

##### Block Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a job to archive and thus block the sales orders that you previously created. After the scheduled job has run successfully, the sales order in status Completed is archived. The other sales order is considered as being used in open business and therefore is considered during the archiving run.

|  |
| --- |
| Note This step is part of the scope item 1KA. In the following section, you find a high-level overview of the required settings to be made in the ILM apps. For a detailed description on how to work with the app, please refer to the test script of scope item 1KA. |

Procedure

Table 10:

| Test Step | Test Step Name | Description | More Information |
| --- | --- | --- | --- |
| 1 | Create a New Variant | Archiving is performed using the Manage Archiving Variants (F0627A) app.Launch the app and select the archiving object SD_VBAK from the overview list on the entry screen. Create a new variant for archiving object SD_VBAK using the following values:Name: <Z_CCFU>Description: <Archiving CCFU>Variant Type: WriteAction: ArchivingTo create a new variant, enter the selection parameters:Sales Doc. Type: CCFUCreated on: <the date on which you created your sales orders>Choose Save. A success message is displayed. | Test script of scope item 1KA, see section Manage Archiving Variants. |
| 2 | Schedule Archiving | Select All Variants and call up your newly created variant and schedule an archiving run. |  |
| 3 | Check Archiving Status | To check if the sales orders were archived, go to the Monitor Archiving Jobs (F0510A) app and select the archiving object SD_VBAK from the overview list on the entry screen.If the <Z_CCFU> archiving job is completed, go to the Completed tab. Check the Job Details, Job Log, and Application Log.Check if the sales order that you set to Completed is in the archive file. Make a note of the name of the new archive file, for example 001336-001SD-VBAK.Tip By default, the background job for data archiving is scheduled to run every Friday at 22:00 UTC.If the archiving job is completed successfully, the business user with the Internal Sales Representative business role isn't able to see the sales order anymore.Because the authorization group you created and its assignment to both an ILM policy as well as to the business catalog Data Privacy - External Auditing (restriction type BLOCKED_DATA), access to that data is allowed for users with that business catalog only. |  |

##### Destroy Archived Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the retention time of the SD_VBAK ILM object has expired (in this example, 1 day), the archive file can be permanently deleted, meaning destroyed. This process step shows you how to start the job which destroys the archive file.

|  |
| --- |
| Note This step is part of the scope item 1KA. In the following section, you find a high-level overview of the required settings to be made in the ILM apps. For a detailed description on how to work with the app, please refer to the test script of scope item 1KA. |

Procedure

Table 11:

| Test Step | Test Step Name | Description | More Information |
| --- | --- | --- | --- |
| 1 | Trigger a Destruction Run | In the ILM Data Destruction (F2662) app, search for the SD_VBAK ILM object and click on it to open a list of the corresponding archive files.Select the archive file whose ID you noted down in the previous step and choose Schedule. On the appearing dialog box, confirm the deletion.Tip By default, the background job for data destruction is scheduled to run every Saturday at 22:00 UTC. | Test script of scope item 1KA, see section ILM Data Destruction. |
| 2 | Check the Deletion Job | After the scheduled job has run, check the Jobs tab. The Job Log of the deletion is displayed..Note The archived file is not displayed in the Archive Explorer (SARE) app anymore, not even with the External Auditor role assigned to your user. |  |

#### Blocking, Unblocking and Deletion of Master Data

##### Block Customer and Business Partner Master Data

In this step, you're testing the blocking of customer master data. Two test procedures are executed in this example:

- [Successful Blocking of Customer and Business Partner Master Data](#unique_30) [page ] 21: The residence period of the customer ILM object is over and its data is no longer used in any business transaction, that is the corresponding sales order has been archived. For this scenario, use the ID of <CUS01> for which the corresponding sales order was archived and deleted in section [Blocking and Deletion of Transactional Data](#unique_18).
- [Unsuccessful Blocking of Customer and Business Partner Master Data](#unique_10) [page ] 22: The residence period of the customer ILM object is over, but its data is still being used in ongoing business, that is the corresponding sales order in status Open. For this scenario, use the ID of <CUS02>.

###### Successful Blocking of Customer and Business Partner Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform the manual blocking of master data using the Block Master Data - Customer & Supplier (CVP_PRE_EOP) app. As already outlined in chapter [Create Customer and Business Partner Master Data](#unique_8) [page ] 6, a business partner was automatically created together with the new customer master data. According to the business partner approach, blocking and deletion for customer and supplier master data is part of the blocking and deletion of the business partner master data. This means that the business partner considers all residence periods of linked customer or supplier master data.

Please note that it's also possible to schedule a regular job for blocking data in the Scheduling Block Customers app. This process isn't tested in this document. You can find more information on the scheduling apps in the product assistance for SAP S/4HANA Cloud Public Edition: [Scheduling Block Customers](https://help.sap.com/docs/SAP_S4HANA_CLOUD/55a7cb346519450cb9e6d21c1ecd6ec1/26fd06583ac69144e10000000a4450e5.html).

To perform the following test, use the customer master data <CUS01> (and its corresponding business partner) for which the assigned sales order was archived and deleted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Block Master Data - Customer & Supplier (CVP_PRE_EOP) app. |  |  |
| 3 | Enter a Partner | In the Partner field, enter the ID of the business partner that was created with customer <CUS01>. |  |  |
| 4 | Define End of Purpose Chec Execution Mode | From the End of Purpose Check Execution Mode field, select Overall. |  |  |
| 5 | Define Processing Options | From the Processing Options field, select Production Mode. |  |  |
| 6 | Execute | Choose Execute.The system displays a log listing all applications that were checked for the specified business partner master data. The final result of the blocking process is displayed at the bottom. | The residence time for the business partner and the corresponding customers has elapsed and it's no longer used in any business application. You blocked business partner with customer <CUS01>.Note By blocking the business partner master data of customer, the corresponding customer master data is also blocked from further processing. |  |
| 7 | Verify Blocking Results | To check if the business partner (and consequently the related customer) was blocked, log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data.Go to the Maintain Business Partner app and search for the business partner for which you triggered the blocking process, for example, by entering the business partner number. | The system does not display any results for the business partner specified, as the blocked data is no longer visible for regular business users. |  |

###### Unsuccessful Blocking of Customer and Business Partner Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to test the unsuccessful blocking of master data to demonstrate how the blocking logic works. To perform the following test, use the customer master data <CUS02> (and its corresponding business partner) for which the assigned sales order hasn't been archived yet. Therefore, blocking is not possible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Block Master Data - Customer & Supplier (CVP_PRE_EOP) app. |  |  |
| 3 | Enter a Partner | In the Partner field, enter the ID of the business partner that was created with customer <CUS02>. |  |  |
| 4 | Define End of Purpose Check Execution Mode | From the End of Purpose Check Execution Mode field, select Overall. |  |  |
| 5 | Define Processing Options | From the Processing Options field, select Production Mode. |  |  |
| 6 | Execute | Choose Execute.The system displays a log listing all applications that were checked for the specified business partner master data. The final result of the blocking process is displayed at the bottom. | The residence time for the customer ILM object FI_ACCRECV for customer <CUS02> has elapsed, however, its data is still being used in the ERP_SD application. The customer wasn't blocked. Consequently, the corresponding business partner could also not be blocked. |  |

##### Unblock Business Partner Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this and the following process step, the master data for customer <CUS01> is unblocked again. As a prerequisite, you must first unblock the corresponding business partner master data.

In general, unblocking master data can be necessary in case new business starts with a historic business partner, customer or supplier and their master data hasn't yet been deleted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Unblock Request - Master Data (BUP_REQ_UNBLK) app. |  |  |
| 3 | Enter a Business Partner Number | Choose Business Partner Master Data and enter the ID of the business partner that is related to customer <CUS01>. |  |  |
| 4 | Enter a Reason | Click inside the Reason Code field and call up the value help (F4). The reason codes and their corresponding descriptions are displayed in a dialog box.Select a reason from the list and choose Enter.Optionally, enter a description. | You specified a reason for your unblock request. |  |
| 5 | Request Unblocking | From the top of the screen, choose Request Unblocking. | The Unblock Request Log screen is displayed. A message tells you that an unblocking request has been created. |  |
| 6 | Access the Unblock Master Data – Business Partner App | Go back to the SAP Fiori launchpad and open the Unblock Master Data – Business Partner app. |  |  |
| 7 | Approve Unblocking | Enter the business partner ID in the Partner field. Select the Production Mode checkbox and choose Execute.A list of unblocking requests is displayed.Select the line of your previously created unblocking request and choose Approve. | A success message is displayed. It tells you that the business partner has been unblocked. |  |

##### Unblock Customer Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to unblock customer master data. Unblocking master data can be necessary in case new business starts with a historic customer or supplier and their master data hasn't yet been deleted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Unblock Request - Master Data (BUP_REQ_UNBLK) app. |  |  |
| 3 | Enter a Customer Number | Choose Customer Master Data and enter the number of the customer that you want to unblock (<CUS01>). |  |  |
| 4 | Enter a Reason | Click inside the Reason Code field and call up the value help (F4). The reason codes and their corresponding descriptions are displayed in a dialog box.Select a reason from the list and choose Enter.Optionally, enter a description. | You specified a reason for your unblock request. |  |
| 5 | Request Unblocking | From the top of the screen, choose Request Unblocking. | The Unblock Request Log screen is displayed. A message tells you that an unblocking request has been created.Note To request suppliers to be unblocked, follow these steps as well, but choose the Supplier object type. |  |
| 6 | Access the Unblock Master Data – Customer & Supplier App | Go back to the SAP Fiori launchpad and open the Unblock Master Data – Customer & Supplier app. |  |  |
| 7 | Approve Unblocking | Go to the Customer Master Data tab.To go to the specific unblocking request, select the Customer checkbox and enter the customer number. Select the Production Mode checkbox and choose Execute.Note Optionally, to display all unblocking requests, leave the Customer checkbox blank. Make the appropriate settings in the Approval Status section and select the Production Mode checkbox. Choose Execute. Confirm that you want to unblock all partners.A list of unblocking requests is displayed.Select the line of your previously created unblocking request and choose Approve.The Reason for Approval/Rejection dialog box is displayed. Enter a reason and choose Continue.Choose Save. | A success message is displayed. It tells you that the customer has been unblocked.Note To unblock a supplier, follow these steps as well, but choose the Supplier Master Data tab. |  |

##### Destroy Customer and Business Partner Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the residence period for master data is completed and data is blocked, it either remains in the database or is stored in an archive. If the blocked data remains in the database, the data manager can delete the blocked business partner, customer, and supplier master data from the database using the corresponding archiving objects. A necessary prerequisite for deletion is that the retention period defined for the data has elapsed.

In this test scenario, the master data stayed in the database and wasn't archived. This process step shows you how to delete the customer and business partner master data from the database. First, you must destroy the customer, then the business partner.

The destruction of the general customer master data record, which contains dependent data in Sales and Finance, is a three-step process. It involves creating archiving variants and scheduling the destruction in the sequence of Sales data, Finance data, and then the general customer master data.

|  |
| --- |
| Note This step is part of the scope item 1KA. In the following section, you find a high-level overview of the required settings to be made in the ILM apps. For a detailed description on how to work with the app, please refer to the test script of scope item 1KA. |

Procedure

Table 12:

| Test Step | Test Step Name | Description | More Information |
| --- | --- | --- | --- |
| 1 | Create a New Variant for FI_ACCRECV (SD Data) | Destruction from the database is performed using the Manage Archiving Variants (F0627A) app.Launch the app and create a new variant for archiving object FI_ACCRECV using the following values:Name: <Z_CUS01_SD>Description: <Destroying SD Data Related to CUS01>Variant Type: WriteAction: DestructionUse the following selection parameters:Data To be Archived: From the value help, choose SD - SD DataCustomer: ID of <CUS01>Choose Save. A success message is displayed. | Test script of scope item 1KA, see section Manage Archiving Variants. |
| 2 | Create a New Variant for FI_ACCRECV (FIN Data) | Repeat step number 1, using the following selection parameters:Name: <Z_CUS01_FI>Description: <Destroying FI Data Related to CUS01>Variant Type: WriteAction: DestructionUse the following selection parameters:Data To be Archived: From the value help, choose FI - FI DataCustomer: ID of <CUS01>Choose Save. A success message is displayed. |  |
| 3 | Create a New Variant for FI_ACCRECV (General Data) | Repeat step number 1, using the following selection parameters:Name: <Z_CUS01>Description: <Destroying General Data of CUS01>Variant Type: WriteAction: DestructionUse the following selection parameters:Data To be Archived: From the value help, choose MD - General DataCustomer: ID of <CUS01>Choose Save. A success message is displayed. |  |
| 4 | Schedule Archiving | Call up your newly created variants and schedule an archiving run in destruction mode.Again, start with the SD data, then FI data and |  |
| 5 | Check Archiving Status | To check if the customer data was deleted, go to the Monitor Archiving Jobs (F0510A) app and select the archiving object FI_ACCRECV from the overview list on the entry screen.Check if the <Z_CUS01> job shows up on the Completed tab. If so, select it and check the subtabs Job Details, Job Log, and Application Log. The customer master data <CUS01> was deleted from the database. | Test script of scope item 1KA, see section Monitor Archiving Jobs. |
| 6 | Destroy Business Partner Master Data | Repeat the steps to destroy the related business partner using the archiving object CA_BUPA with the following condition fields:Name: <Z_BP_CUS01>Description: <Destroying BP Related to CUS01>Variant Type: WriteAction: DestructionUse the following selection parameters:Business Partner: ID of business partner created with <CUS01>Choose Save. A success message is displayed. |  |

### Information Retrieval

#### Trigger a Search for Personal Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you trigger a cross-application search for all personal data of a specified data subject, on the database as well as in archive files.

|  |
| --- |
| Tip You can further configure the retrieval of personal data according to your needs with the help of profiles. Profiles allow you to store personalized settings that influence the collection, display, and download of personal data. If you want to start your data collection with a specific profile, please refer to the set-up instructions guide of scope item 5LE first to get more information on how to create profiles in your SAP S/4HANA Cloud Public Edition system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Start Data Collection (DTINF_START_COLL)app. |  |  |
| 3 | Enter Details for the Data Collection Run | On the next screen, fill out the following fields:Data Subject ID Type: <choose either Business Partner Number or User Name>Data Subject ID: <enter a business partner number or user name>Language: <select a language from the list>Purpose: <select a purpose from the list>Note The purposes available in this list are based on settings made in the Information Lifecycle Management (ILM) apps. For more information on how to define purposes, see[Business Conditions](#unique_6) [page ] 5.Profile: <optional> |  |  |
| 4 | Start the Data Collection Run | Choose Execute to start a search for personal data. | You have started the data collection for a specific business partner/ user.. |  |

#### View the Search Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you display the search results of the data collection process triggered with the Start Data Collection app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Process Data Collection Results (DTINF_PROC_COLL)app. |  |  |
| 3 | Select Data Collection Request | On the entry screen of the app, you get an overview of all existing data collection requests.Select the request for which you triggered a data collection run in test step [Trigger a Search for Personal Data](#unique_23) [page ] 28 and double-click it. |  |  |
| 4 | Select a Purpose | On the following screen, select a purpose from the Select Purpose dropdown list and choose Go to view all personal data that was collected for this specific purpose. | The results are displayed hierarchically on the left-hand side of the subscreen.Double-click a node to get additional details on the data found for an entry, for example name, address, date of birth, employment, or creditworthiness data.If the system finds attachments containing personal data of the data subject specified, the metadata (e.g. file name, file description) of these attachments is displayed in the tree view. To display the actual attachment, you must download the search results. |  |

### Consent Administration

In this section, you will conduct a test to upload consent data from your device to the SAP S/4HANA Cloud Public Edition system. Once uploaded, you will then use the Manage Consents (F3307) app to search for and display the consent data.

#### Import Consent Data from File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you manually upload consent data from a file that is stored on your device.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist - Consent Management. |  |  |
| 2 | Access the App | Open the Import Consents from File (F3306) app. |  |  |
| 3 | Select Parameters for Import | On the entry screen of the app, fill out the following fields:Source File: Select the file containing the consent data to be imported from your local desktop by clicking BrowseNote The file that you want to import must be available in JSON (Java Script Object Notation) format. For more information on the overall structure of a JSON file and the fields relevant to a consent record, refer to SAP Note [2607792](https://me.sap.com/notes/2607792).Import Log Detail Level: Use the dropdown list to select the level of detail for the import log. You can find more information on the detail level by calling up the field help (F1) in the app.External Reference ID: Enter a reference ID, if required.Import Parameters: Define if you want to skip expired consents/ if you want to run the import in test mode first. |  |  |
| 4 | Import | Choose Import | A message is displayed indicating that the import has started. |  |

#### Manage Consents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you view the consent data that you imported from file as described in step [Import Consent Data from File](#unique_25) [page ] 31.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist - Consent Management. |  |  |
| 2 | Access the App | Open the Manage Consents (F3307) app. |  |  |
| 3 | Search for Consent Record | On the entry screen of the app, use the End of Validity field (mandatory) to specifiy a time period that corresponds to the consent data stored in the file you uploaded in the precious step.Choose Go. |  |  |
| 4 | Display Consent Record Details | To navigate to the details of a consent, click on the Row Item in the consent table, whose details you want to check. | The details of the consent record are displayed. |  |

### Read Access Logging

You can use Read Access Logging (RAL) to monitor and log access to personal data. The information provided may include, for example, which business users accessed business partner personal data, and in which time frame. With the RAL application, you have the ability to enable Read Access Logging, adapt the RAL configurations (mention what to log) and view logs using the Read Access Logging monitor.

The test steps that explain how to configure Read Access Logging by using the predelivered configurations and recordings in SAP S/4HANA Cloud Public Edition are described in the set-up instructions of the Data Protection and Privacy (5LE) scope item. You find this document on the SAP Signavio Process Navigator:[https://me.sap.com/processnavigator/SolP/5LE](https://me.sap.com/processnavigator/SolP/5LE).

The Display Static System Audit App allow the external auditors to get an overview of static system information. Please see the on the SAP Help portal for more details: [Display Static System Audit](https://help.sap.com/viewer/DRAFT/a630d57fc5004c6383e7a81efee7a8bb/2105.500/en-US/236eeb2ae7544d31bf3b672d26dc0452.html).

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
- related-to :: [[01-solution-foundation-and-platform/data-protection-and-privacy-data-controller-and-purpose-6n9-ae-1180]]
- related-to :: [[01-solution-foundation-and-platform/test-script-information-lifecycle-management-1ka-sap-s-4hana-cloud-pub]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5LE_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 63,180 chars in the whole document
