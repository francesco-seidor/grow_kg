---
id: 01-solution-foundation-and-platform/data-protection-and-privacy-data-controller-and-purpose-6n9-ae-1180
title: Data Protection and Privacy – Data Controller and Purpose (6N9_AE) (6N9_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6N9: assigning data controllers and purposes to business partners and testing access restrictions."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/information-lifecycle-and-data-protection]
aliases: [6N9_S4CLD2608_BPD_EN_AE]
keywords: [Information Lifecycle Management and Data Protection, data controller assignment, purpose determination, purpose assumption, data protection and privacy, business partner master data, authorization checks, configuration activation, business roles, test users]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N9_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1180
topic: 01-solution-foundation-and-platform/information-lifecycle-and-data-protection
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Data Protection and Privacy – Data Controller and Purpose (6N9_AE) (6N9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Information Lifecycle Management and Data Protection** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Data Protection and Privacy – Data Controller and Purpose (6N9_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Data Protection and Privacy – Data Controller and Purpose (6N9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858869)

[2 Prerequisites 4](#_Toc232858870)

[2.1 System Access 4](#_Toc232858871)

[2.2 Roles 4](#_Toc232858872)

[2.3 Additional Manual Configuration 5](#_Toc232858873)

[2.4 Business Conditions 5](#_Toc232858874)

[2.5 Preliminary Steps 5](#_Toc232858875)

[2.5.1 Create Data Controllers and Purposes 5](#_Toc232858876)

[2.5.2 Create Business Partner with Supplier Role 6](#_Toc232858877)

[2.5.3 Create Test Users with Different Authorizations 7](#_Toc232858878)

[3 Overview Table 9](#_Toc232858879)

[4 Test Procedures 11](#_Toc232858880)

[4.1 Data Controller Assignment 11](#_Toc232858881)

[4.1.1 Assign Data Controllers to Business Partners 11](#_Toc232858882)

[4.1.2 Verify Restricted Access to Master Data 12](#_Toc232858883)

[4.1.3 Invalidate Existing Data Controller Assignments 13](#_Toc232858884)

[4.2 Data Controller and Purpose Assignment 14](#_Toc232858885)

[4.2.1 Purpose Determination for Application Data 14](#_Toc232858886)

[4.2.1.1 Create Purchase Order 14](#_Toc232858887)

[4.2.1.2 Check Purpose Assignments for Application Objects 16](#_Toc232858888)

[4.2.1.3 Redetermine Purpose Assignments for Application Objects 17](#_Toc232858889)

[4.2.1.4 Determine Purposes for Existing Application Objects 18](#_Toc232858890)

[4.2.2 Purpose Determination for Master Data 20](#_Toc232858891)

[4.2.2.1 Check Purpose Determination and Assignment for Business Partners 20](#_Toc232858892)

[4.2.3 Purpose Assumption 21](#_Toc232858893)

[4.2.3.1 Manually Assign Data Controller with Purpose Assumption 21](#_Toc232858894)

[4.3 Authorization Checks on Business Partner Data 22](#_Toc232858895)

[4.3.1 Verify Access to Master Data Based on Data Controller and Purpose Assignments 22](#_Toc232858896)

[5 Appendix 24](#_Toc232858897)

[5.1 Process Integration 24](#_Toc232858898)

[5.1.1 Preceding Processes 24](#_Toc232858899)

## Purpose

Overview

With this scope item, SAP S/4HANA Cloud Public Edition simplifies the separation of business partner master data based on legal entities (data controllers) and purposes. This approach supports privacy by design and default.

Many business processes that involve personal data begin with the creation of master data. When you create and manage a business partner, you can add several types of data to that business partner. Examples include contact details, financial information, and employment history. Each type of data creates different levels of privacy risk for individuals. To manage these risks, this scope item provides a switch to a data model that lets you manage personal data according to the legal entities responsible for the data (data controllers) and the purposes for collecting and processing the data. This helps you comply with legal standards.

After you centrally define data controllers and purposes and assign these to business partners, you can restrict access to business partner master data based on these assignments. This ensures that only authorized users access the personal data of business partners. You can activate these authorization checks separately for data controllers and purposes. This gives you flexibility in your implementation. You can start by separating data based on data controllers and then introduce purpose-based authorization checks if required.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Business Partner DataNote For the test steps in this guide, create two business users based on the Master Data Specialist role. For more information, refer to chapter [Create Test Users with Different Authorizations](#unique_5) [page ] 7 | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Data Privacy Specialist | SAP_BR_DATA_PRIVACY_SPECIALIST | Data Protection and Privacy - Master Data / Data Protection and Privacy | SAP_CA_SPT_DPP_PC / SAP_BR_DATA_PRIVACY_SPECIALIST |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/0c6a52ebdb682cdf064e2c0cd1d7e303)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 5LE - Data Protection and Privacy | Maintain Data ControllersFirst, you must create data controllers that fit your company’s organizational structure. The definition of data controllers is a necessary prerequisite for the assignment of data controllers to business partner master data as well as for centrally defining purposes. For more information on how to define data controllers in your SAP S/4HANA Cloud Public Edition system, refer to the set-up instructions guide of scope item [5LE](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/5LE) under Maintain Data Controllers.Maintain PurposesYou must centrally create purposes that specify the reason and the goal for the processing of personal data. These purposes can then be assigned to application objects, as outlined in this test script. For more information on how to define purposes in your SAP S/4HANA Cloud Public Edition system, refer to the set-up instructions guide of scope item [5LE](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/5LE) under Maintain Purposes. |

For more information on data controller and purpose creation specific to the test steps described in this guide, refer to [Create Data Controllers and Purposes](#unique_8) [page ] 5.

### Preliminary Steps

#### Create Data Controllers and Purposes

Purpose

In this preliminary step, you define data controllers and purposes which will be used in the test processes described in this test script. You can make the necessary settings in configuration activities Maintain Data Controllers and Maintain Purposes in your configuration environment for SAP S/4HANA Cloud, public edition. For more information on these activities, refer to the setup instructions guide of scope item 5LE

Make sure to maintain the following data controllers and purposes:

Table 1: Data Controllers

| Name | Company Code |
| --- | --- |
| DC01 | Choose any company code available in your system, ensuring it matches the one used for the purchase order you need to create in step [Create Purchase Order](#unique_9) [page ] 14 |
| DC02 | Choose a company code different from the one used for DC01. |

Table 2: Overview of Data Controller and Purposes Required for Testing

| Purpose | Status | Assigned Data Controller | Data Category |
| --- | --- | --- | --- |
| PURP01 | Purpose Assumption Active | DC01 | - |
| PURP02 | Active | DC01 | PURCHASEORDER |
| PURP03 | Purpose Assumption Active | DC02 | - |

#### Create Business Partner with Supplier Role

Purpose

This preliminary step shows you how to create a business partner that serves as test data for the follow-on processes described in this script.

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163) app. | On the entry screen of the app, you get an overview of all existing business partners. |  |
| 3 | Create a New Business Partner | On the entry screen of the app, choose Create and then Organization. | A dialog window appears where you can quickly create the most basic data for the business partner. |  |
| 4 | Maintain Basic Data | Enter at least a Name and a standard address for the business partner and choose OK:Name 1: BUPA_01Address: <any address> | You've maintained the basic data for creating a business partner. After you choose OK, you're directed to the Details screen. |  |
| 5 | Assign Supplier Role | On the Basic Data tab, go to the Roles section and choose Create.In the Business Partner role column, call up the value help (F4) and choose role FLVN00 (Supplier Fin. Accounting) from the list. |  |  |
| 6 | Save | Choose Create to save your draft master data record. | You've created a new business partner with the supplier role. |  |
| 7 | Maintain Supplier Company Code Data | On the entry screen of the Manage Business Partner Master Data (F3163) app, search for your newly created business partner and edit it.Go to the Roles section and click the FLVN00 role. You see the details of that role on a new screen.On the Company Codes tab, select Create. On the screen that appears, in the Company Code field, use the value help (F4) to select a company code.Note For this test scenario, you must use the same company code as the one you assigned to the data controller DC01 created in step [Create Data Controllers and Purposes](#unique_8) [page ] 5.Before you can save your changes, you must also specify a Reconciliation Account and a Sort Key.Choose Apply to save your changes. | You've maintained the company code for the supplier. |  |
| 8 | Maintain Supplier Purchase Organization Data | On the entry screen of the Manage Business Partner Master Data (F3163) app, search for your newly created business partner and edit it.Go to the Purchasing Organization section and choose Create. On the screen that appears, enter the following data:Purchasing OrganizationPurchasing GroupOrder CurrencyChoose Apply to save your changes. | You've created purchasing organization data for the supplier. |  |

#### Create Test Users with Different Authorizations

Purpose

To validate the restriction behavior, you need to create two business users based on the business role template SAP_BR_BUPA_MASTER_SPECIALIST and assign them different restriction settings.

Procedure

1. Create the business role from the template
    - Use the Maintain Business Roles app in the SAP Fiori Launchpad (Identity and Access Management).
    - Create a custom role based on the template SAP_BR_BUPA_MASTER_SPECIALIST.
2. Maintain different restriction types
    - Within the same app, navigate to the Restrictions section of the role and maintain the restriction type B_BUP_DCPD as follows:

Table 3:

| Business Role | Data Controller | Purpose |
| --- | --- | --- |
| USER_01 | DC01 | PURP02 |
| USER_02 | DC02 | PURP03 |

1. Assign roles to users
    - Use the Maintain Business Users app to assign the respective roles to USER_01 and USER_02.

This setup ensures that both users are based on the same role template but behave differently due to their restriction configuration.

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

The test scenarios may differ depending on which level of data protection and privacy you’d like to achieve in your system.

Level 1 - Data Controller Assignment

Prerequisite: Configuration ID BP_DC_CTRLR active

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Assign Data Controllers to Business Partners | Master Data Specialist - Business Partner Data | Manage Business Partner Master Data (F3163) | A data controller is manually assigned to a set of business partner master data. The assignment is displayed on the Basic Data tab under Data Controllers. |
| Verify Restricted Access to Business Partner Master Data | Master Data Specialist - Business Partner Data | Manage Business Partner Master Data (F3163) | Your access to business partner master data is denied due to missing data controller authorizations. |
| Invalidate Existing Data Controller Assignments | Master Data Specialist - Business Partner Data | Manage Business Partner Master Data (F3163) | You defined a data controller as no longer valid for a particular business partner. |

Level 2 - Data Controller and Purpose Assignment

Prerequisite: Configuration IDs BP_DC_CTRLR and BP_PURPOSE active

Purpose Determination for Application Data

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Purchase Order | SAP_BR_PURCHASER | Manage Purchase Orders (F0842A) | You create a purchase order for which the system automatically determines relevant purposes based on data controller and data category assignments. |
| Check Purpose Assignments for Application Objects | Data Privacy Specialist | Monitor Purpose Assignments (F7314) | You verified that the purpose determined for an application object instance is correct. |
| Redetermine Purpose Assignments for Application Objects | Data Privacy Specialist | Monitor Purpose Assignments (F7314) | You retriggered the purpose determination for a specific application object instance. |
| Determine Purposes for Existing Application Objects | Data Privacy Specialist | Schedule Purpose Determination (F7648) | You scheduled the determination of purposes for application object instances that already existed in your system before the purpose determination feature was activated. |

Purpose Determination for Master Data

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Check Purpose Determination and Assignment for Business Partners | Master Data Specialist - Business Partner Data | Manage Business Partner Master Data (F3163) | You verified that the purpose determined for an application object was automatically assigned to the corresponding business partner. |

Purpose Assumption

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Manually Assign Data Controller with Purpose Assumption | Master Data Specialist - Business Partner Data | Manage Business Partner Master Data (F3163) | You assigned a data controller with purpose assumption to a business partner. |

Level 3 - Header-Level Authorization Checks on Business Partner Master Data Based on Data Controller and Purpose Assignments

Prerequisite: Configuration IDs BP_DC_CTRLR, BP_PURPOSE and BP_DC_PURP_HDR_AUTH_CHECK active

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Verify Access to Business Partner Master Data Based on Data Controller and Purpose Assignments | Master Data Specialist - Business Partner Data | Manage Business Partner Master Data (F3163) | Your access to business partner master data is denied due to missing data controller and purpose authorizations. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Data Controller Assignment

#### Assign Data Controllers to Business Partners

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you manually assign data controller DC01 to business partner BUPA_01.

Prerequisites

Make sure you've fulfilled the following prerequisites before continuing with this test step:

- To enable the overall feature of assigning data controllers to business partners, go to configuration activity Manage Data Controller and Purpose Settings for Business Partner and activate the configuration ID BP_DC_CTRLR . This step is irreversible and can significantly impact your master data. Before you activate this configuration, read the setup instructions guide for scope item 6N9.
- You've created a business partner as outlined in chapter [Create Business Partner with Supplier Role](#unique_10) [page ] 6.
- You've defined a data controller as outlined in chapter [Create Data Controllers and Purposes](#unique_8) [page ] 5.

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163) app. | On the entry screen of the app, you get an overview of all existing business partners. |  |
| 3 | Search for the Business Partner | On the entry screen of the app, search for your newly created business partner BUPA_01. |  |  |
| 4 | Manually Assign a Data Controller | On the Basic Data tab, go to the Data Controllers section and choose Create.In the Data Controller column, call up the value help (F4) and choose data controller DC01 from the list.Note In this list, you only find the data controllers that you previously created in configuration activity Maintain Data Controllers. For more information, see section [Business Conditions](#unique_7) [page ] 5. |  |  |
| 6 | Save | Choose Save in the bottom-right corner to save your changes. | You've assigned data controller DC01 to business partner BUPA_01. With this, only users who are authorized for a certain data controller have the rights to access the business partner data. You can verify access restrictions in the next test step.In column Derivation Indicator, you can verify that the data controller was assigned manually (value No is displayed). |  |

#### Verify Restricted Access to Master Data

Purpose

In this step, you verify that access to business partner BUPA_01 is restricted when logging in with business user USER_02. In contrast, business user USER_01 can successfully access the business partner because the required data controller is maintained for this restriction type.

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as USER_01. |  |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163) app. | On the entry screen of the app, you get an overview of all existing business partners. |  |
| 3 | Search for the Business Partner | On the entry screen of the app, search for the business partner BUPA_01. | The master data record BUPA_01 is displayed in the search results list. |  |
| 4 | Log off | Log off from the SAP fiori launchpad. |  |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as USER_02. |  |  |
| 6 | Search for the Business Partner | On the entry screen of the app, search for business partner BUPA_01. | The master data record BUPA_01 is not displayed in the search results list, as USER_02 has no authorization for this data controller. |  |

#### Invalidate Existing Data Controller Assignments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you invalidate the assignment of a data controller DC01 to a business partner BUPA_01.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163) app. | On the entry screen of the app, you get an overview of all existing business partners. |  |
| 3 | Search for Newly Created Business Partner | On the entry screen of the app, use the entry field Last Name to search for your newly created business partner BUPA_01.Select it from the results lists. | You get to the details screen of the business partner you selected. |  |
| 4 | Invalidate Data Controller Assignment | Go in edit mode and navigate to the Data Controllers section on the Basic Data tab.For the data controller you assigned to business partner BUPA_01 in the previous test step, mark the checkbox in the Invalidate Assignment column. |  |  |
| 5 | Save | Save your changes. | You invalidated the data controller assignment DC01 for business partner BUPA_01. |  |

### Data Controller and Purpose Assignment

#### Purpose Determination for Application Data

##### Create Purchase Order

Purpose

In this step, you create a purchase order for which the system automatically determines a purpose. Because the purpose determination feature only works for new instances of an application object, you need to activate the automatic determination of purposes in your configuration environment before creating the purchase order (see the Prerequisites section below).

Prerequisites

Before you create the purchase order, make sure the following prerequisites have been fulfilled:

- You've defined data controllers and purposes as outlined in chapter [Create Data Controllers and Purposes](#unique_8) [page ] 5.
- You've created a business partner as outlined in chapter [Create Business Partner with Supplier Role](#unique_10) [page ] 6.
- In your configuration environment, you've performed the following steps:
    1. To enable the overall feature of assigning purposes to both transactional and master data, go to configuration activity Manage Data Controller and Purpose Settings for Business Partner and activate the configuration ID BP_PURPOSE . This step is irreversible and can significantly impact your master data. Before you activate this configuration, read the setup instructions guide for scope item 6N9.

|  |
| --- |
| Note There is a specific activation sequence for these configuration IDs. You must first activate configuration ID BP_DC_CTRLR . For more information, see the set-up instructions guide of scope item 6N9 in section Manage Data Controller and Purpose Settings for Data Controller |

-
    1. Activate the purpose determination for application object PURCHASEORDER, go to configuration activity Activate/ Deactivate Purpose Determination for Application Objects. For more information, refer to the set-up instructions guide for scope item 6N9.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Purchaser. |  |  |
| 2 | Access the App | Open the Manage Purchase Orders (F0842A) app. |  |  |
| 3 | Create Purchase Order Basic Data | On the entry screen of the app, choose Create to create a new purchase order and fill out the mandatory fields in the Basic Data section.Note For this scenario, make sure you're using the same company code you used for creating the data controller DC01. |  |  |
| 4 | Add Purchase Order Items | On the Items subscreen, choose Create and fill out the following fields:Purchasing Doc Type: Standard PO (NB)Supplier: BUPA_01Company Code: <use the same company code as for DC01>Item Category: <Standard>Material: <choose any material available in your system>Order Quantity: <choose any quantity>Net Price: <enter any price>Then choose Order. Note down the number of the newly created purchase order. |  |  |
| 5 | Save New Sales Order | Then choose Order. | Since you activated the purpose determination before you created the purchase order, the system now automatically assigned a purpose to your newly created order. To verify if this has worked, refer to [Check Purpose Assignments for Application Objects](#unique_16) [page ] 16 |  |

##### Check Purpose Assignments for Application Objects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you verify the purpose assignments made for the purchase order created in step [Create Purchase Order](#unique_9) [page ] 14 of this test script.

|  |
| --- |
| Note The Monitor Purpose Assignments (F7314) app only displays those application object instances for which a purpose determination could be completed successfully. You can check the status of a purpose determination run using the Display Purpose Determination Logs (F7316) app. In case of any errors, you can retrigger the determination in the Manage Purpose Determinations (F7649) app. Since this isn't a standard process, these steps aren't covered in this test script. For more information, please refer to the product assistance for SAP S/4HANA Cloud Public Edition under [Purpose Determination](https://help.sap.com/docs/SAP_S4HANA_CLOUD/55a7cb346519450cb9e6d21c1ecd6ec1/e726223651f74f20ba30fae264d2c14b.html). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access App | Open the Monitor Purpose Assignments (F7314) app. |  |  |
| 3 | Call Up a List of Application Object Instances | On the entry screen of the app, call up the value help for the Application Objects field and select the application object Purchase Order.Choose Go. | The system displays a list of all existing purchase orders for which purposes have successfully been defined. |  |
| 4 | View Details of Purpose Assignment for Purchase Order | From the list, select the purchase order that you created in step [Create Purchase Order](#unique_9) [page ] 14. | A new subscreen is displayed on which you can see the details of the purpose assignment for the purchase order. The purpose PURP01 and data controller DC01 should be displayed here.Here, you can check whether the assigned purposes are correct. If you’d like to redetermine purposes, follow the steps outlined in [Redetermine Purpose Assignments for Application Objects](#unique_17) [page ] 17. |  |

##### Redetermine Purpose Assignments for Application Objects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, trigger the redetermination of purposes for an application object instance . This might be required, for example, if an additional purpose is relevant for an application object.

Prerequisites

For this step, first go back to configuration activity Maintain Purposes, create a new purpose and add it as secondary purpose to PURP02. For this new purpose, use the same data controller (DC01) and data category (PURCHASEORDER) that you assigned before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access App | Open the Monitor Purpose Assignments (F7314) app. |  |  |
| 3 | Call Up a List of Application Object Instances | On the entry screen of the app, call up the value help for the Application Objects field and select the application object Purchase Order.Choose Go. | The system displays a list of all existing purchase orders for which purposes have successfully been defined. |  |
| 4 | View Details of Purpose Assignment | From the list, select the purchase order that you created in step [Create Purchase Order](#unique_9) [page ] 14. | A new subscreen is displayed on which you can see the details of the purpose assignment, such as the name of the purpose, its description, the assigned data controllers, etc. |  |
| 5 | Trigger Redermination | Mark the checkbox next to the purchase order and choose Redetermine Assignments. | A dialog window appears. Choose Ok to confirm the redetermination process.The purchase order is removed from the list in column Application Object Instance. After the next determination run is completed, the object will be displayed again. |  |
| 6 | Check Redetermined Purpose Assignments | After the next determination run is finished, repeat steps 2-4 to display the purpose details of the purchase order. | The newly created purpose should now be displayed in column Purpose. |  |

##### Determine Purposes for Existing Application Objects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you determine purposes for application object instances that already existed in your system before activating the purpose determination feature.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access App | Open the Schedule Purpose Determination (F7648) app. | On the entry screen of the app, you get an overview of all currently existing purpose determination jobs. |  |
| 3 | Create a New Determination Schedule | On the entry screen of the app, choose Create. | A new wizard for creating a schedule is started. |  |
| 4 | Select Template | By default, the template Purpose Determination Application Job Template is selected.Choose Step 2. |  |  |
| 5 | Define Scheduling Options | On the following screen, choose Start Immediately.Choose Step 3. |  |  |
| 6 | Define Parameters | On this screen, you define the application objects for which you want to trigger the purpose determination. Fill in the fields with the following values:Application Object: <select an application object for which you want to determine purposes>Note In the value help of this field, you can only select application objects for which the purpose determination was activated in configuration activity Activate/Deactivate Purpose Determination.From Date: <start date of application object instance creation nterval>To Date: <end date of application object instance creation interval> |  |  |
| 7 | Schedule the Job | Choose Schedule to create a new job for purpose determination. | Your newly created job now appears on the entry screen of the Schedule Purpose Determination (F7648) app.You can check which purposes were assigned to the application object instances in the Monitor Purpose Assignments (F7314) app. |  |

#### Purpose Determination for Master Data

##### Check Purpose Determination and Assignment for Business Partners

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step, you check if the purpose that was determined for the purchase order you created in step [Create Purchase Order](#unique_9) [page ] 14 has also been assigned to the corresponding business partner BUPA_01.

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163) app. | On the entry screen of the app, you get an overview of all existing business partners. |  |
| 3 | Search for the Newly Created Business Partner | On the entry screen of the app, search for business partner BUPA_01 and select it. |  |  |
| 4 | Check for Purpose Assignments | On the Basic Data tab, go to the Data Controllers section.In the Purpose column, the purpose PURP02 is displayed. | You've verified that the purpose determined for an application object has automatically been assigned to the relevant business partner. |  |

#### Purpose Assumption

##### Manually Assign Data Controller with Purpose Assumption

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step, you manually assign a data controller with purpose assumption to business partner BUPA_01. Purpose assumption is a business partner–specific mechanism used during the initial transition to purpose-based processing of personal data. It temporarily covers data categories that are not yet assigned to explicit purposes, ensuring that business partner data remains accessible and compliant while purpose assignments are introduced step by step.

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163) app. | On the entry screen of the app, you get an overview of all existing business partners. |  |
| 3 | Search for the Business Partner | On the entry screen of the app, search for your newly created business partner BUPA_01. |  |  |
| 4 | Manually Assign a Data Controller | On the Basic Data tab, go to the Data Controllers section and choose Create.In the Data Controller column, call up the value help (F4) and choose data controller DC02 from the list. |  |  |
| 5 | Manually Assign a Purpose | Use the value help (F4) for the Purpose field to select purpose PURP03 for which you activated purpose assumption. |  |  |
| 6 | Save | Choose Save in the bottom-right corner to save your changes. | You've assigned data controller DC02 with purpose PURP03 to business partner BUPA_01.Due to the purpose assumption assigned to the data controller, in a migration scenario where purpose-based processing of data is being introduced, the business partner remains accessible—even if not all of its data categories have been assigned to explicit purposes yet. |  |

### Authorization Checks on Business Partner Data

#### Verify Access to Master Data Based on Data Controller and Purpose Assignments

Purpose

In this step, you verify whether access to business partner BUPA_01 is restricted due to missing authorizations. In addition to checks related to the data controller, the system now also verifies that the correct combination of data controller and purpose is maintained before granting access to the business partner data.

Prerequisites

To enable header-level authorization checks on business partner master data based on data controller and purpose assignments, go to configuration activity Manage Data Controller and Purpose Settings for Data Controller and activate the configuration ID BP_DC_PURP_HDR_AUTH_CHECK . This step is irreversible and can significantly impact your master data. Before you activate this configuration, read the setup instructions guide for scope item 6N9.

|  |
| --- |
| Note There is a specific activation sequence for these configuration IDs. You must first activate configuration IDs BP_DC_CTRLR and BP_PURPOSE. For more information, see the set-up instructions guide of scope item 6N9 in section Manage Data Controller and Purpose Settings for Data Controller |

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as USER_02. |  |  |
| 2 | Access App | Open the Manage Business Partner Master Data (F3163) app. | On the entry screen of the app, you get an overview of all existing business partners. |  |
| 3 | Search for the Business Partner (Verify Purpose Assumption) | On the entry screen of the app, search for your newly created business partner BUPA_01. | The master data record BUPA_01 is displayed in the search results list due to DC02 with purpose assumption assigned in step [Manually Assign Data Controller with Purpose Assumption](#unique_20) [page ] 21. |  |
| 4 | Log off | Log off from the SAP fiori launchpad. |  |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as USER_01. |  |  |
| 6 | Search for the Business Partner (Verify Correct Authorizations) | On the entry screen of the app, search for your business partner BUPA_01. | The master data record BUPA_01 is displayed in the search results list, as USER_01 has the required authorizations for DC01 and PURP_02. |  |
| 7 | Create New Business Partner | To verify restricted access to master data, create a new business partner BUPA_02 that does not have DC02 and PURP03 assigned to it. | The business partner data is not displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 5LE (Data Protection and Privacy | You’ve defined data controllers in your S/4HANA Cloud system using configuration activity Maintain Data Controllers.You've defined purposes in your S/4HANA Cloud system using configuration activity Maintain Purposes. |

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
> Flagged while digesting this document, not verified: Internal inconsistency: the test step 'Check Purpose Assignments for Application Objects' says purpose PURP01 and data controller DC01 should be displayed for the purchase order, but Table 2 gives PURP02 as the purpose with data category PURCHASEORDER (PURP01 has no data category) and the later business partner check expects PURP02.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/test-script-information-lifecycle-management-1ka-sap-s-4hana-cloud-pub]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-data-protection-and-priva]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 43,211 chars in the whole document
