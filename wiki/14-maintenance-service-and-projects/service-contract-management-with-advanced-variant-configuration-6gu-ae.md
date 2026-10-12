---
id: 14-maintenance-service-and-projects/service-contract-management-with-advanced-variant-configuration-6gu-ae
title: "Service Contract Management with Advanced Variant Configuration (6GU_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6GU_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6GU_AE: service contracts and templates with configurable products (AVC), prerequisites and steps."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-contract-management]
aliases: [6GU_S4CLD2608_BPD_EN_AE]
keywords: [Service Contract Management, advanced variant configuration, configurable products, service contract templates, follow-up transactions, service contract printing, date profiles, service and response profiles, service contract pricing, situation handling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GU_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1169
topic: 14-maintenance-service-and-projects/service-contract-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Service Contract Management with Advanced Variant Configuration (6GU_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6GU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Service Contract Management** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Contract Management with Advanced Variant Configuration (6GU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859042)

[2 Prerequisites 4](#_Toc232859043)

[2.1 System Access 4](#_Toc232859044)

[2.2 Roles 4](#_Toc232859045)

[2.3 Master Data, Organizational Data, and Transactional Data 5](#_Toc232859046)

[2.4 Additional Manual Configuration 6](#_Toc232859047)

[2.5 Preliminary Steps 6](#_Toc232859048)

[2.5.1 Create Employee via CSV File Upload 6](#_Toc232859049)

[2.5.2 Create Date Profile 6](#_Toc232859050)

[2.5.3 Create Service and Response Profiles 9](#_Toc232859051)

[2.5.4 Adapt Price for Service Contract Product (optional) 14](#_Toc232859052)

[2.5.5 Settings for Situation Handling (Optional) 17](#_Toc232859053)

[2.5.6 Settings for Credit Check Management (Optional) 18](#_Toc232859054)

[3 Overview Table 19](#_Toc232859055)

[4 Test Procedures 20](#_Toc232859056)

[4.1 Service Contract Template 20](#_Toc232859057)

[4.1.1 Create Service Contract Templates with Configurable Products 20](#_Toc232859058)

[4.1.2 Create Follow Up Transaction for Service Contracts 21](#_Toc232859059)

[4.2 Service Contract Management 23](#_Toc232859060)

[4.2.1 Create Service Contract with Configurable Product 23](#_Toc232859061)

[4.2.2 Check Net Value and Print Service Contract 24](#_Toc232859062)

[4.2.3 Service Contract Billing 25](#_Toc232859063)

[4.2.4 Service Contract Change Processes (Optional) 25](#_Toc232859064)

[5 Appendix 26](#_Toc232859065)

[5.1 Process Integration 26](#_Toc232859066)

[5.1.1 Preceding Processes 26](#_Toc232859067)

[5.1.2 Succeeding Processes 26](#_Toc232859068)

## Purpose

Overview

This scope item covers service contract creation with configurable products using advanced variant configuration (AVC) in SAP S/4HANA Cloud Public Edition.

Customers can create service contracts with configurable products. Configurable products can be added as standard contract items, price adaptation items, and ad-hoc billing items. If you add a configurable product as a service contract item, it's required to configure the product that has been added. To configure the product, the customer navigates to the configuration user interface and selects the characteristics and characteristic values that are defined in the product master data. By default, the status of the configurable product is incomplete. When the product configuration is complete, the configuration status is changed to released. Depending on the product definition, the selection of characteristics and characteristic values of a configurable product can impact the price of a contract item based on the defined variant conditions.

After creating configurable products in service contracts, customers can follow the process of service contract management of the Service Contract Management (3MO) scope item to finalize service contract relevant steps.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

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
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC | Your system administrator provides the user and password information. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Your system administrator provides the user and password information. |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST | Your system administrator provides the user and password information. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Your system administrator provides the user and password information. |

### Master Data, Organizational Data, and Transactional Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1 | Make sure that the customer you use for this process has either assigned the customer pricing procedure 01 (Procedure 01) or no procedure. |
| Employee | - | < Use your own employee ID that is assigned to your user ID.> |  |
| Service product (services) | SRV_CONTR_CONFIG | ServicesService Contract ProductService Contr.Configurable Prod Service Contract Product Renewal |  |
| Sales Organization | 3310 | Dom. Sales Org |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 5BE | Create Configurable Service Product - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f6a654f6130370e2187638eab9df5194)

### Preliminary Steps

#### Create Employee via CSV File Upload

Purpose

Employees are mandatory master data for service contracts. Create one employee per system user.

Procedure

Refer to the following path explaining how to create new or update existing personal details, employment and service cost level data of an employee:

[https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD) -> Product Assistance <English> -> Human Resources -> Import Employees

#### Create Date Profile

The date profile CONT002 is available via automated content and assigned to the transaction type SC1 Service Contract. If you require additional date profiles, date types, duration types and date rules you can create them according to the following procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Configuration Expert - Business Process Configuration. | The Home screen appears. |  |
| 2 | Open Manage Your Solution application | Choose the Manage Your Solution application tile. | The Manage Your Solution screen appears. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The list report page is displayed in the screen Configure Your Solution: Realize Phase.Configuration Items are displayed in the list. |  |
| 4 | Find configuration item | Select Service in the filter ‘Application Area’ and 'in the filter 'Sub Application Area' General Settings and you will see the configuration item Date ManagementChoose the icon > at the end of this line. | The sub screen Configure Your Solution - Date Management appears. |  |
| 5 | Go to the configuration screen | You see a step 1 Define Date Types, Duration Types and Date RulesNote To use this function, you need assign business catalog SAP_CA_BC_IC_LND_S4CRM_BF0_PC to the BR_BPC_EXPERT role.Choose Configure in the column Actions. | The screen Change View " Duration ": Overview appears. |  |
| 6 | Create new Durations and Date Types | If you need additional entries for durations:In the Dialog Structure choose: DurationsChoose New Entries. Enter the dollowing data, for exampleDuration: CONTDURADescription: Contract Validity PeriodChoose Save.In the dialog structure choose Date TypesEnter the following, for example:Date Type: CONTSTARTDate Profile: checkedMilestone.: checkedDescription: Contract Start DateChoose Save.Repeat these steps for all durations and date types you want to enter.Choose Back | New Duartion Types and Date Types are created. |  |
| 7 | Define Date Profile | On screen Configure Your Solution – Date ManagementIn step 2 Define Date Porfile.Choose Configure in the column Actions.Select a date profile you want to copy.Choose Copy AsEnter the following fields, for exampleDate Profile: YCONT002Name: Date Profile for Service ContractsIn the dialog box Specify object to be copiedChoose Copy allIn the dialog box Information: number of dependent entries copied: xxChoose ContinueSelect the newly created date profile.In the Dialog StructureChoose Date RulesOn the Change View “Date Rules”: Overview, delete the ones you do not need in your new date profile and assign new date rules via New Entries.In the Dialog StructureChoose Date Types.On the Change View “Date Types”: Overview, delete the ones you do not need in your new date profile and assign new date types via New Entries.In the Dialog StructureChoose DurationsOn the Change View “Durations”: Overview, delete the ones you do not need in your new date profile and assign new durations via New Entries.Choose Save.Choose Back. | The screen Change View " Date Profile ": Overview appears.New date profile is created. |  |
| 8 | Assign Date Profile to Transaction Type | If you want to assign your new date profile to the transaction type for service contracts:On screen Configure Your Solution – Date ManagementIn step 3 Assign Date Porfile to Transaction TypeChoose Configure in the column Actions.On the Change View “Assign date Profile to transaction types”: Overview Formatmake the following entries:Trans. Type: SC1Description: Service ContractDate Prof.: your new Date ProfileChoose SaveChoose Back. | A new date profile is assigned to a trans-action type. |  |
| 9 | Assing Date Profile to Item Category | If you want to assign your new date profile to the item categories for service contracts.On screen Configure Your Solution – Date ManagementIn step 4 Assign Date Porfile to Item CategoriesChoose Configure in the column Actions.On the Change View “Assign date Profile to Item Categories”: Overviewmake the following entries, for example:Item Cat.: SCN1Description: Service Contract ItemDate Prof.: your new Date ProfileChoose Save.Choose Back. | A new date profile is assigned to an item category. |  |

#### Create Service and Response Profiles

Purpose

Service profiles define the availability of a service provider and response profiles define the planned response time. They are needed for the feature service level agreement.

Service profiles are not available via automated content and must therefore be created manually.

Two response profiles (FIRST and STANDARD) are available via automated content. If you require additional response profiles beyond the existing ones, according to the following procedure.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Configuration Expert - Business Process Configuration. | The Home screen appears. |  |
| 2 | Open Manage Your Solution application | Choose the Manage Your Solution application tile. | The Manage Your Solution screen appears. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The list report page is displayed in the screen Configure Your Solution: Realize Phase.Configuration Items are displayed in the list. |  |
| 4 | Find configuration item SLA Management | Select Service in the filter ‘Application Area’ and you will see the configuration item SLA ManagementChoose the icon > at the end of this line. | The sub screen Configure Your Solution - SLA Management appears. |  |
| 5 | Go to the configuration screen | You see a step 1 Define Service ProfilesChoose Configure in the column Actions. | The screen Define Service Profiles": Change appears. |  |
| 6 | Create new Service Profile | If not yet done, choose New Entries and maintain your new service profile, for exampleServ Prof.: <7x24>Description: <Mon-Fri: 0-24h>Choose Save.Choose Availability Times to maintain details:In the pop-up screen maintain your available time, for example:Rule: D daily periodic Availability TimesAll: 1 DaysFr.: 0:00To: 24:00(Timezone): UTC+1Exceptions: 0 no exceptionsCalendar Used: All Days Are Working DaysChoose Copy.If not yet done, choose New Entries and maintain your new service profile, for exampleServ Prof.: <5x10>Description: <Mon-Fri: 7-17h>Choose Save.Choose Availability Times to maintain details:In the pop-up screen maintain your available time, for example:Rule: W weekly periodic Availability TimesWeek Rule: 1 every week onSelect: Mo, Tu, We, Th, FrEnter for each day from: 07:00 - 17:00(Timezone): UTC+1Exceptions: K not on non-working daysCalendar Used: Factory Calendar (99 Internatioal)Choose Copy.Choose Save. | A new service profile has been created. |  |
| 7 | Create new Response Profile | If response profiles are not provided by content activation or if you need additional response profiles, you can follow these steps.Go to Step 2 in SLA Management screen. Choose Define Response Profiles for Service Transactions, for exampleResponse Prof.: FIRST, First Level Response TimePriority (select checkbox)Choose Save. | The screen Change View " Response Profile ": Overview appears. |  |
| 8 | Maintain Response Indicators | Choose Indicators Response Times in the Dialog Structure on the left. Maintain an entry in the table Indicators for Response Times for Priority choose New Entries.In the table you can enter a value for Priority, for example: 1Choose Save. | The screen Change View "Indicators Response Times": Overview appears. |  |
| 9 | Maintain Response Time | Select that row in the table by setting the checkbox.Choose Response Times in the Dialog Structure on the left.Choose New Entries to make a new entry in the table Response Times.Name of Duration: In the pop-up screen choose, for example, SRV_RF_DURA (Duration until First Reaction).Duration Value: 1Time Unit: HOUR | The screen Change View: " Response Times": Overview appears. |  |
| 10 | Save | Choose Save. | A new response profile has been created. |  |
| 11 | Maintain additional Response Time | Choose New Entries to make a new entry in the table Response Times.Name of Duration: In the pop-up screen choose, for example, SRV_RR_DURA (Duration until Service End).Duration Value: 24Time Unit: HOURChoose Save. | The screen Change View: " Response Times": Overview appears. |  |
| 12 | Create new Response Profile | Repeat the steps before to create a second response profile STANDARD, Standard Level Response Time.Maintain longer response times, for example, with Duration until First Reaction = 24 hour, and Duration until Service End = 72 hourChoose Save. | A second response profile has been created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Find Configuration Item SLA Management | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Service Profiles.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The configuration activity opens in the SAP S/4HANA Cloud Public Edition system. |  |
| 3 | Create new Service Profile | If not yet done, choose New Entries and maintain your new service profile, for exampleServ Prof.: <7x24>Description: <Mon-Fri: 0-24h>Choose Save.Choose Availability Times to maintain details:In the pop-up screen maintain your available time, for example:Rule: D daily periodic Availability TimesAll: 1 DaysFr.: 0:00To: 24:00(Timezone): UTC+1Exceptions: 0 no exceptionsCalendar Used: All Days Are Working DaysChoose Copy.If not yet done, choose New Entries and maintain your new service profile, for exampleServ Prof.: <5x10>Description: <Mon-Fri: 7-17h>Choose Save.Choose Availability Times to maintain details:In the pop-up screen maintain your available time, for example:Rule: W weekly periodic Availability TimesWeek Rule: 1 every week onSelect: Mo, Tu, We, Th, FrEnter for each day from: 07:00 - 17:00(Timezone): UTC+1Exceptions: K not on non-working daysCalendar Used: Factory Calendar (99 Internatioal)Choose Copy.Choose Save. | A new service profile has been created. |  |
| 4 | Create new Response Profile | If response profiles are not provided by content activation or if you need additional response profiles, you can follow these steps.Choose Response Profile in the Dialog Structure on the left.Choose New Entries and maintain your new response profile, for exampleResponse Prof.: FIRST, First Level Response TimePriority (select checkbox)Choose Save. | The screen Change View " Response Profile ": Overview appears. |  |
| 5 | Maintain Response Indicators | Choose Indicators Response Times in the Dialog Structure on the left. Maintain an entry in the table Indicators for Response Times for Priority choose New Entries.In the table you can enter a value for Priority, for example: 1Choose Save. | The screen Change View "Indicators Response Times": Overview appears. |  |
| 6 | Maintain Response Time | Select that row in the table by setting the checkbox.Choose Response Times in the Dialog Structure on the left.Choose New Entries to make a new entry in the table Response Times.Name of Duration: In the pop-up screen choose, for example, SRV_RF_DURA (Duration until First Reaction).Duration Value: 1Time Unit: HOUR | The screen Change View: " Response Times": Overview appears. |  |
| 7 | Save | Choose Save. | A new response profile has been created. |  |
| 8 | Maintain additional Response Time | Choose New Entries to make a new entry in the table Response Times.Name of Duration: In the pop-up screen choose, for example, SRV_RR_DURA (Duration until Service End).Duration Value: 24Time Unit: HOURChoose Save. | The screen Change View: " Response Times": Overview appears. |  |
| 9 | Create new Response Profile | Repeat the steps before to create a second response profile STANDARD, Standard Level Response Time.Maintain longer response times, for example, with Duration until First Reaction = 24 hour, and Duration until Service End = 72 hourChoose Save. | A second response profile has been created. |  |

#### Adapt Price for Service Contract Product (optional)

Purpose

For the sample service contract product SRV_CONTRACT that is delivered as part of the SAP Best Practices content, a standard price is already maintained. If you want to adapt this price, for example, to maintain different prices for future time periods, proceed like described below. This step is not mandatory for the overall process flow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Pricing Specialist. | The Fiori Launchpad with access to the Set Material Prices application is displayed. |
| 2 | Open Set Material Prices application | Choose the Set Material Prices application tile. | The view Change Condition Records is displayed. |
| 3 | Change validity period of a condition record | Add in the field Condition Type the condition type value “PSI1”.Choose Enter.On the popup Key Combination select the radio button Material.Choose Choose.Fill the fields with the following values:- Sales Organization: 3310- Distribution Channel: 10- Material: SRV_CONTRACTValid On: today's dateChoose Execute.On the next screen Change Price f.Srv.Cntr.Itm Condition (PSI1) : Overview add the product ID “SRV_CONTRACT” in the column Material of the table below.Choose Enter.In the column Valid from change the date to, for example, “the first of this year” and in the column Valid to enter, for example ” the end of this year ”.Choose Save.Choose Back. | The condition record is saved with a new validity period. |
| 4 | Create a new condition record | On the view Change Price f.Srv.Cntr.Itm Condition (PSI1) : Selection. Keep the values in the fields Sales Organization, Distribution Channel and Material.Choose: More > Condtion > Create.Change the value in the field Valid On to the “beginning of the next period when you want to sell the product with different price, for example, first of next year”.Choose Execute.On the next view Change Price fSrv.Cntr.Itm Condition (PSI1) : Overview add the product ID SRV_CONTRACT in the column Material ..Choose Enter.In the column Amount add the “new price for SRV_CONTRACT”.In the column Unit add the currency AEDIn the column per add the value 1In the column UoM (Unit of Measure) add the value AUIn the column Valid from enter “beginning of the second period, for example, first of next year”In the column Valid to enter "end of the second period, for example, the end of next year".Choose Save.Choose Back. | The condition record is saved. |
| 5 | Check Validity Periods | Choose the Set Material Prices application tile.Add in the field Condition Type the condition type value “PSI1”.Choose Enter.On the popup Key Combination select the radio button Material.Choose Choose.Fill the fields with the following values:Sales Organization: 3310Distribution Channel: “10”Material: SRV_CONTRACTValid On: today's dateChoose Execute.Choose Validity Periods. | Different validity periods are displayed in section Existing validity periods.. |
| 6 | Create Service Level-Specific Price | Optionally you can maintain new condition records for the Service and Response Profiles for one product. To do so, access the Set Material Prices app and maintain the following entries:- Condition Type:DSP1Choose Enter.On the next screen maintain the following values:Sales Organization: 3310Distribution Channel: 10Valid On:The first of the current month/yearChoose Execute.On the next screen maintain the following values:Material: SRV_CONTRACTService Profile (Svc. Prof.): 5x10Optionally maintain a Response Profile.Amount: 120Unit: AEDChoose Enter.Choose Save. | You have maintained service level-specific prices.If the respective service profile, and optionally response profile, are assinged in a service contract, the contract price will be adapted accordingly. |

#### Settings for Situation Handling (Optional)

Purpose

Situation handling recognizes business situations by evaluating conditions (rules) on business facts. A business situation occurs when a business object changes a status relevant to a user, when critical deadlines are passed, or a KPI passes a threshold.

Procedure

Notifications are only created in the system once the required configurations in the situation template (including notification recipient settings) are set up. This additional configuration steps should be carried out by customers to activate situation handling.

|  |
| --- |
| Note If you want to use situation handling with Service Contract Management scope item, you have to include also scope item Situation Handling (31N). |

To set up situation handling, create your ready-to-use situation type, maintain the message to be displayed, define the conditions when the situation will be triggered, define recipient groups who will receive notifications, and monitor the instances.

For more information, see the Set-Up Instructions for the scope item Situation Handling (31N).

The following standard situation templates are defined and delivered by SAP for Service Contract Management:

- SRVC_EXPIRING_SERVICE_CONTRACT (Service Contract due to expire soon)
- SRVC_CONTR_WITH_EXP_BILL_VALUE (Service Contract with Zero Billing Value)
- SRVC_EXPIRING_SRVC_CONTR_ITEM (Service Contract Item Due to Expire Soon)

For each situation template, a corresponding responsibility rule is defined in which the responsible person to be notified can be assigned.

For more information and situation template details (default settings, conditions, notification recipients), see the [Situation Templates in Service](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/LATEST/en-US/9d6cee508b2e44a39e93474ee68e6ba9.html) documentation.

|  |
| --- |
| Note If you want to test situation handling with Service Contract Management scope item, execute the steps that are described in the Test Script of scope item Situation Handling (31N). |

#### Settings for Credit Check Management (Optional)

Purpose

You use Credit Management to minimize financial risks for your organization. It enables you to display a business partner's credit rating, or to perform a credit check when creating a transaction document. Credit management can be enabled for Service Contracts to maintain and check credit for relevant business partners.

Follow the procedure below to set up credit management for service orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BPC_EXPERT. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution. | Options for configuring the solutions is displayed. |  |
| 3 | Access Configuration | Choose Configure Your Solution. | List page with all the solutions is displayed with Search bar. |  |
| 4 | Filter the Results | Select application area as Service and Sub Application area General Settings to filter the results | List of application under general settings are displayed |  |
| 5 | Access the Solution | Select Credit management from the list to access the solution | Application is opened with all the details |  |
| 6 | Configure the settings | Select Configure in the configuration step for Activate Credit Management in Transactions. | Configuration page is displayed |  |
| 7 | Configure the Transaction | Select the transactions listed to activate the credit management settings for Service Contracts.SC1 - Service ContractChoose Save | Credit management settings are saved for the transactions selected |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction |
| --- | --- | --- |
| Service Contract Management |  |  |
| [Create Service Contract with Configurable Product](#unique_14) [page ] 23 | Customer Service Manager | Manage Service Contracts |
| [Check Net Value and Print Service Contract](#unique_15) [page ] 24 | Customer Service Manager | Manage Service Contracts |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Service Contract Template

#### Create Service Contract Templates with Configurable Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Key purpose of this step is to create a service contracts template which has the required details of service item which is later used to create a service contracts from it.

Prerequisites

Prerequisite steps for configuration and the creation of configurable service products is described in Master Data Script 5BE. The steps in this master data script must be excuted before you can proceed with this chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the roleCustomer Service Manager (SAP_BR_CUSTOMER_SRVC_MGR). | The Fiori Launchpad with access to the Manage Service Contracts Templates application is displayed. |  |
| 2 | Open Manage Service contracts Templates application | Choose the Manage Service contracts Templates application tile. | The list report page is displayed. |  |
| 3 | Open Create Service contracts Template window | Choose Create from the service contracts templates list page. | A simple Create Service contracts template window will be displayed. |  |
| 4 | Maintain Service contracts Template data | Enter the following data to create a service contracts template:Description: <your description>Employee Responsible: for example, John, Consultant_AEMaintain the following Items in the service contracts template:Product ID: for example, SRV_CONTR_CONFIGQuantity: for example, 1Choose Enter. | Details entered are saved and template screen is opened in edit mode. |  |
| 5 | Configure Characteristics | In the column Actions choose Configure Product to navigate to the Service Contract Template New- Variant Configuration view in edit mode.In section Default Group:Select the following variants using the value help:Preventive Maintenance: Half-YearlyService Channel: Telephone supportChoose Done. | All variants for the characteristics are maintained. The field Net Value is automatically calculated according to the prices for the selected variants.Configuration status is Released. |  |
| 6 | Release and Save | Choose Release All Items.Choose Save. | The Service contract template is released. |  |

#### Create Follow Up Transaction for Service Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step we create a follow up service contract from the previously released service contract template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the roleCustomer Service Manager (SAP_BR_CUSTOMER_SRVC_MGR). | The Fiori Launchpad with access to the Manage Service Contract Templates application is displayed. |  |
| 2 | Open Manage Service contracts Templates application | Choose the Manage Service Contract Templates application tile. | The list report page is displayed. |  |
| 3 | Find Service contract Template | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service contract template in the Search field.Choose Go. | Your service contract template is displayed in the report list. |  |
| 4 | Open Service contract Template and Create a Follow Up transaction | Open the selected Service contract Template and choose Create Follow-UpNote The service contract template should be in Released status for creating a follow up. | A simple Create Service contract template window is displayed. |  |
| 5 | Create a Service contract | Enter the following data to create a service contract:Sold-To Party: for example, 17100001Description: <your description>Select the required Items for creating service contractfor example, SRV_CONTR_CONFIGChoose OKSelect the preferred contact person from the Partner Selection Document Header dialog box.Choose Save. | A new service contract has been created.Note down the service contract number.Your service contract is displayed in the report list within Manage Service Contracts. |  |

### Service Contract Management

#### Create Service Contract with Configurable Product

Purpose

The customer service manager creates a service contract item for a service product that is configurable and assigns the corresponding variants for the item with: configure the product. Pricing is determined dependend on the selected variants with characteristics.

Prerequisites

Prerequisite steps for configuration and the creation of configurable service products is described in Master Data Script 5BE. The steps in this master data script must be excuted before you can proceed with this chapter.

Procedure for Service Contract Item with configurable product

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open Manage Service Contracts application | Log on as Customer Service Manager, choose the Manage Service Contracts application tile. |  |  |
| 2 | Create new Service Contract | Choose Create and maintain the following entries in theService Contract Details:Description: Enter a descriptionSold-to-Party: For example, Domestic UAE Customer 1 (ID: 33100001)If sales organizations are displayed in a Select Orangizational Data dialog box, select Sales Organization:3310, Distribution Channel:10.If contact persons are displayed in a Partner Selection Document header dialog box, select one of them.Contract Start: the first of this monthContract End: the first of this month in one year |  |  |
| 3 | Maintain Service Contract Item | In section Items add the product “SRV_CONTR_CONFIG” in the column Product ID. In the column Quantity add the quantity “1” and choose Enter. | A message is displayed:Item 100: configure product SRV_CONTR_CONF |  |
| 4 | Configure Characteristics | In the column Actions choose Configure Product to navigate to the Service Contract New- Variant Configuration view in edit mode.In section Default Group:Select the following variants using the value help:Preventive Maintenance: Half-YearlyService Channel: Telephone supportChoose Done. | All variants for the characteristics are maintained. The field Net Value is automatically calculated according to the prices for the selected variants.Configuration status is Released. |  |
| 5 | Check Price Details | On the Service Contract: New screen, choose Price – DetailsAnd check the End Value for Price Element for variantsHalf-YearlyTelephone support | End values for all price element are calculated and displayed. |  |
| 6 | Release and Save | Navigate back to view Service Contract: xxxxxxxxxx, Description.Choose Release All Items.Choose Save. | The new Service Contract is created.Success massage is displayed. |  |

#### Check Net Value and Print Service Contract

Purpose

The Customer Service Manager checks the net value after maintaining the configuration. The service contract can be printed out or sent as e-mail to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 3 | Search for Service Contracts | Enter search terms in filter bar and choose Go.For example, enter the service contract number created in previous chapter in Transaction ID Contract field. | Service contract is displayed in result list. |  |
| 4 | Select Service Contract | Choose a service contract with Error Status: No Errors. | Service Contract is displayed. |  |
| 5 | Check Price Details | On the Service Contract: xxxxxxxxxx, Description screen, choose Price – DetailsAnd check the End Value for Price Element for variantsHalf-YearlyTelephone support | End values for all price element are calculated and displayed. |  |
| 6 | View Output Items | On the Service Contract: xxxxxxxxxx, Description view, choose the Output Items tab. | View Output Details is displayed. |  |
| 7 | Send Output | In section Output Details, select a line with output channel you want to use.Choose Send Output to print the document or send it via e-mail. | Document is sent to the selected output channel. |  |
| 8 | Display Print Preview | To display the document, in the Display column choose Display Document. Optionally save a local copy of the PDF document. | A PDF document is displayed. |  |

#### Service Contract Billing

For Service Contract Billing processes, please check scope item 3MO Service Contract Management

#### Service Contract Change Processes (Optional)

For Change Processes, please check scope item 3MO Service Contract Management

## Appendix

### Process Integration

#### Preceding Processes

The following processes and conditions can precede this process.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3MO | Service Contracts Management |

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
- related-to :: [[14-maintenance-service-and-projects/test-script-service-contract-management-3mo-ae-sap-s-4hana-cloud-publi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 43,351 chars in the whole document
