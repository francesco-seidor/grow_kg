---
id: 14-maintenance-service-and-projects/test-script-service-contract-management-3mo-ae-sap-s-4hana-cloud-publi
title: "Test Script: Service Contract Management (3MO_AE) - SAP S/4HANA Cloud Public Edition (3MO_S4CLD2608_BPD_EN_AE)"
description: "SAP test script (scope item 3MO, UAE, release 2608): creating, pricing, billing, renewing, changing and cancelling service contracts in S/4HANA Cloud."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-contract-management]
aliases: [3MO_S4CLD2608_BPD_EN_AE]
keywords: [Service Contract Management, service contracts, service contract creation, service contract templates, service contract billing, price agreements, service contract pricing, ad-hoc billing, contract renewal, billing document requests]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3MO_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-961
topic: 14-maintenance-service-and-projects/service-contract-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Service Contract Management (3MO_AE) - SAP S/4HANA Cloud Public Edition (3MO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3MO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Service Contract Management** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Contract Management (3MO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853350)

[2 Prerequisites 4](#_Toc232853351)

[2.1 System Access 4](#_Toc232853352)

[2.2 Roles 4](#_Toc232853353)

[2.3 Master Data, Organizational Data, and Transactional Data 5](#_Toc232853354)

[2.4 Additional Manual Configuration 6](#_Toc232853355)

[2.5 Preliminary Steps 6](#_Toc232853356)

[2.5.1 Create Employee via CSV File Upload 6](#_Toc232853357)

[2.5.2 Create Date Profile 7](#_Toc232853358)

[2.5.3 Create Service and Response Profiles 10](#_Toc232853359)

[2.5.4 Adapt Price for Service Contract Product (optional) 15](#_Toc232853360)

[2.5.5 Settings for Situation Handling (Optional) 17](#_Toc232853361)

[2.5.6 Settings for Credit Check Management (Optional) 18](#_Toc232853362)

[3 Overview Table 20](#_Toc232853363)

[4 Test Procedures 22](#_Toc232853364)

[4.1 Service Contract Templates 22](#_Toc232853365)

[4.1.1 Create Service Contract Templates 22](#_Toc232853366)

[4.1.2 Release Service Contract Templates 23](#_Toc232853367)

[4.1.3 Create Follow Up Transaction for Service Contract 24](#_Toc232853368)

[4.2 Service Contract Management 26](#_Toc232853369)

[4.2.1 Create Service Contract 26](#_Toc232853370)

[4.2.2 Maintain Product List and create Price Agreement for Service Order Product 29](#_Toc232853371)

[4.2.3 Adapt Service Contract Prices 32](#_Toc232853372)

[4.2.4 Create a Service Contract Item for Ad-hoc Billing 34](#_Toc232853373)

[4.2.5 Print Service Contract 36](#_Toc232853374)

[4.3 Service Contract Billing 36](#_Toc232853375)

[4.3.1 Schedule Billing Document Request Creation 36](#_Toc232853376)

[4.3.2 Manage Billing Document Requests 38](#_Toc232853377)

[4.3.3 Create Billing Document (Invoice) 38](#_Toc232853378)

[4.4 Service Contract Change Processes (optional) 40](#_Toc232853379)

[4.4.1 Manually renew a Service Contract Item 40](#_Toc232853380)

[4.4.2 Manually renew a Service Contract 41](#_Toc232853381)

[4.4.2.1 Renew by creating new item 41](#_Toc232853382)

[4.4.2.2 Renew by creating new contract 44](#_Toc232853383)

[4.4.3 Change Sold-to Party 47](#_Toc232853384)

[4.4.4 Cancel Service Contracts 48](#_Toc232853385)

[5 Service Contracts Dashboard 50](#_Toc232853386)

[6 Appendix 51](#_Toc232853387)

[6.1 Process Integration 51](#_Toc232853388)

[6.1.1 Preceding Processes 51](#_Toc232853389)

[6.1.2 Succeeding Processes 51](#_Toc232853390)

## Purpose

Overview

This scope item covers the creation of service contracts in SAP S/4HANA Cloud Public Edition. Service contracts are outline agreements that define services offered for a period and represent long-term service agreements with customers. Service contracts are billed on a periodic billing plan. Via price adaptations for service contracts, different prices within the contract periods are possible.

Customer-specific price agreements can be defined and handled within service contracts. Service contract determination is enabled for service orders that correspond with the service contract in predefined criteria – in this case, contract and price details from determined service contract are considered.

Customers can define service level agreements and maintain service and response profiles in service contracts.

If desired, you can renew an expiring service contract automatically for a predefined period at a predefined date. You can also manually renew service contracts and items. As part of the change process, you can change the sold-to party of a service contract and create a service contract automatically.

Furthermore, you can enable ad-hoc billing, a structured method of service contract billing that allows you to define billing values and billing dates manually.

This scope item includes situation handling for service contracts. Situation handling is functionality in SAP S/4HANA Cloud Public Edition that lets you bring certain circumstances (situations) to the attention of a relevant group of business users.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/3MO_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Your system administrator provides the user and password information. |

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
| Service product (services) | SRV_01SRV_CONTRACTSRV_CONTR_CONFSRV_CTR_RENEWAL | ServicesService Contract ProductService Contr.Configurable Prod Service Contract Product Renewal |  |
| Sales Organization | 3310 | Dom. Sales Org |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| 5BE | Create Configurable Service Product - MDS |
| 63J | Create Material and Equipment BOM for Service - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c398cacd63b768cad3aee50e43fa0ae7)

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
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Configuration Expert. | The Home screen appears. |  |
| 2 | Open Manage Your Solution application | Choose the Manage Your Solution application tile. | The Manage Your Solution screen appears. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The list report page is displayed in the screen Configure Your Solution: Realize Phase.Configuration Items are displayed in the list. |  |
| 4 | Find configuration item SLA Management | Select Service in the filter ‘Application Area’ and you will see the configuration item SLA Management.Choose the icon > at the end of this line. | The sub screen Configure Your Solution - SLA Management appears. |  |
| 5 | Go to the configuration screen | You see a step 1 Define Availability and Response TimesChoose Configure in the column Actions. | The screen Change View " Service Profile ": Overview appears. |  |
| 6 | Create new Service Profile for availability | If not yet done, choose New Entries and maintain your new service profile, for exampleServ Prof.: <7x24>Description: <Mon-Fri: 0-24h>Choose Save.Choose Availability Times to maintain details:In the pop-up screen maintain your available time, for example:Rule: D daily periodic Availability TimesAll: 1 DaysFr.: 0:00To: 24:00(Timezone): UTC+1Exceptions: 0 no exceptionsCalendar Used: All Days Are Working DaysChoose Copy.If not yet done, choose New Entries and maintain your new service profile, for exampleServ Prof.: <5x10>Description: <Mon-Fri: 7-17h>Choose Save.Choose Availability Times to maintain details:In the pop-up screen maintain your available time, for example:Rule: W weekly periodic Availability TimesWeek Rule: 1 every week onSelect: Mo, Tu, We, Th, FrEnter for each day from: 07:00 - 17:00(Timezone): UTC+1Exceptions: K not on non-working daysCalendar Used: Factory Calendar (99 Internatioal)Choose Copy.Choose Save. | A new service profile has been created. |  |
| 7 | Create new Response Profile | If response profiles are not provided by content activation or if you need additional response profiles, you can follow these steps.Choose Response Profile in the Dialog Structure on the left.Choose New Entries and maintain your new response profile, for exampleResponse Prof.: FIRST, First Level Response TimePriority (select checkbox)Choose Save. | The screen Change View " Response Profile ": Overview appears. |  |
| 8 | Maintain Response Indicators | Choose Indicators Response Times in the Dialog Structure on the left. Maintain an entry in the table Indicators for Response Times for Priority choose New Entries.In the table you can enter a value for Priority, for example: 1Choose Save. | The screen Change View "Indicators Response Times": Overview appears. |  |
| 9 | Maintain Response Time | Select that row in the table by setting the checkbox.Choose Response Times in the Dialog Structure on the left.Choose New Entries to make a new entry in the table Response Times.Name of Duration: In the pop-up screen choose, for example, SRV_RF_DURA (Duration until First Reaction).Duration Value: 1Time Unit: HOUR | The screen Change View: " Response Times": Overview appears. |  |
| 10 | Save | Choose Save. | A new response profile has been created. |  |
| 11 | Maintain additional Response Time | Choose New Entries to make a new entry in the table Response Times.Name of Duration: In the pop-up screen choose, for example, SRV_RR_DURA (Duration until Service End).Duration Value: 24Time Unit: HOURChoose Save. | The screen Change View: " Response Times": Overview appears. |  |
| 12 | Create new Response Profile | Repeat the steps before to create a second response profile STANDARD, Standard Level Response Time.Maintain longer response times, for example, with Duration until First Reaction = 24 hour, and Duration until Service End = 72 hourChoose Save. | A second response profile has been created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Find Configuration Item SLA Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Availability and Response Times.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The configuration activity opens in the SAP S/4HANA Cloud Public Edition system. |  |
| 3 | Create new Service Profile for availability | If not yet done, choose New Entries and maintain your new service profile, for exampleServ Prof.: <7x24>Description: <Mon-Fri: 0-24h>Choose Save.Choose Availability Times to maintain details:In the pop-up screen maintain your available time, for example:Rule: D daily periodic Availability TimesAll: 1 DaysFr.: 0:00To: 24:00(Timezone): UTC+1Exceptions: 0 no exceptionsCalendar Used: All Days Are Working DaysChoose Copy.If not yet done, choose New Entries and maintain your new service profile, for exampleServ Prof.: <5x10>Description: <Mon-Fri: 7-17h>Choose Save.Choose Availability Times to maintain details:In the pop-up screen maintain your available time, for example:Rule: W weekly periodic Availability TimesWeek Rule: 1 every week onSelect: Mo, Tu, We, Th, FrEnter for each day from: 07:00 - 17:00(Timezone): UTC+1Exceptions: K not on non-working daysCalendar Used: Factory Calendar (99 Internatioal)Choose Copy.Choose Save. | A new service profile has been created. |  |
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
- SERVICE_CONTRACT_ITEM_RELEASE_DUE (Service Contract Item is not released, and item start date is passed )
- SRVC_CONTRACT_ITEM_BILLG_BLOCKED (Service Contract Item is blocked for billing)

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

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Service Contract Management |  |  |  |
| [Create Service Contract](#unique_14) [page ] 26 | Customer Service Manager | Manage Service Contracts | Service contract is created. |
| [Maintain Product List and create Price Agreement for Service Order Product](#unique_15) [page ] 29 | Customer Service Manager | Manage Service Contracts | Price agreements are created for a service product that is used in a service order. |
| [Adapt Service Contract Prices](#unique_16) [page ] 32 | Customer Service Manager | Manage Service Contracts | The price has been edited in the service contract billing plan. |
| [Create a Service Contract Item for Ad-hoc Billing](#unique_17) [page ] 34 | Customer Service Manager | Manage Service Contracts | Service Contract with ad-hoc billing item is created and can be billed according to progress. |
| [Print Service Contract](#unique_18) [page ] 36 | Customer Service Manager | Manage Service Contracts | Service contract PDF is displayed. |
| Service Contract Billing |  |  |  |
| [Schedule Billing Document Request Creation](#unique_19) [page ] 36 | Customer Service Manager | Schedule Billing Document Request Creation | Billing document request creation is scheduled. |
| [Manage Billing Document Requests](#unique_20) [page ] 38 | Billing Clerk | Manage Billing Document Requests | Billing document request is processed. |
| [Create Billing Document (Invoice)](#unique_21) [page ] 38 | Billing Clerk | Create Billing Documents (F0798) | Invoice is created. |
| Service Contract Change Processes (optional) |  |  |  |
| [Manually renew a Service Contract Item](#unique_22) [page ] 40 | Customer Service Manager | Manage Service Contracts | New item is created in existing service contract. |
| Manually renew a Service Contract | Customer Service Manager | Manage Service Contracts | New items or contracts are created in existing service contract. |
| [Change Sold-to Party](#unique_23) [page ] 47 | Customer Service Manager | Manage Service Contracts | New service contract is created with new Sold-to Party. |
| [Cancel Service Contracts](#unique_24) [page ] 48 | Customer Service Manager | Manage Service Contracts | Service contract is canceled. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Service Contract Templates

#### Create Service Contract Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Key purpose of this step is to create a service contract template which has the required details of service item which is later used to create a service contract from it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the roleCustomer Service Manager (SAP_BR_CUSTOMER_SRVC_MGR). | The Fiori Launchpad with access to the Manage Service Contract Templates application is displayed. |  |
| 2 | Open Manage Service Contract Templates application | Choose the Manage Service Contract Templates application tile. | The list report page is displayed. |  |
| 3 | Open Create Service Contract Template window | Choose Create from the service contract templates list page. | A simple Create Service contract template window will be displayed. |  |
| 4 | Maintain Service Contract Template data | Enter the following data to create a service contract template:Description: <your description>Employee Responsible: for example, John, Consultant_AEMaintain the following Items in the service contract template:Product ID: for example, SRV_CONTRACTQuantity: for example, 1Choose Enter.Choose Save. | Details entered are saved and template screen is opened in edit mode. |  |

#### Release Service Contract Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step we release the service contract template created in previous step and to be able to convert it into a service contract

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the roleCustomer Service Manager (SAP_BR_CUSTOMER_SRVC_MGR). | The Fiori Launchpad with access to the Manage Service Contract Templates application is displayed. |  |
| 2 | Open Manage Service Contract Templates application | Choose the Manage Service Contract Templates application tile. | The list report page is displayed. |  |
| 3 | Find Service Contract Template | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service contract template in the Search field.Choose Go. | Your service contract template is displayed in the report list. |  |
| 4 | Open Service Contract Template and release | Open the selected Service Contract Template and choose Edit.Choose Release All Items.Choose Save | The Service contract template is released. |  |

#### Create Follow Up Transaction for Service Contract

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
| 2 | Open Manage Service Contract Templates application | Choose the Manage Service Contract Templates application tile. | The list report page is displayed. |  |
| 3 | Find Service Contract Template | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service contract template in the Search field.Choose Go. | Your service contract template is displayed in the report list. |  |
| 4 | Open Service Contract Template and Create a Follow Up transaction | Open the selected Service Contract Template and choose Create Follow-UpNote The service contract template should be in Released status for creating a follow up. | A simple Create Service Contract Template window is displayed. |  |
| 5 | Create a Service contract | Enter the following data to create a service contract:Sold-To Party: for example, 33100001Description: <your description>Note Optionally you can add equipment details in the service contract templateEquipment: choose from F4Select the required Items for creating service contractfor example, SRV_CONTRACTChoose OKSelect the preferred contact person from the Partner Selection Document Header dialog box.Choose Save. | A new service contract has been created.Note down the service contract number.Your service contract is displayed in the report list within Manage Service Contract. |  |

### Service Contract Management

#### Create Service Contract

Purpose

The Customer Service Manager creates a new service contract in the system and changes the price of the service contract items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 2 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. |  |  |
| 3 | Create Service Contract | Choose Create and maintain the following entries:- Description: Enter a description- Sold-to-Party: Domestic UAE Customer 1 (ID: 33100001), or one of the sample customers available in your system.If contact persons are displayed in a Partner Selection Document header dialog box, select one of them.- Contract Start: the first of this month- Contract End: the first of this month in one yearIn section Items add the product SRV_CONTRACT in the column Product ID and choose Enter. In the column Quantity add the quantity 1 and choose Enter. | The contract start date and end date are determined automatically and can be modified. |  |
| 4 | Save | Choose Release All Items.Choose Save.Note the created Service Contract ID number. | The new service contract is created. |  |
| 5 | Edit Service Contract Item - Automatically renew an expiring service contract item | In section Items in column Actions to navigate to the Service Contract Item Details view.Choose Edit.In section Automatic Renewal, set the checkbox for Enable. Add into the field Renewal Period the period within you want the service contract to be renewed by the automatic renewals process run (for example 3 weeks).In the field Contract Extension add the service contract extension time period, which will be valid after the renewal, for example: 6 month.Choose Enter.Note Automatic Renewal is possible for item category SCN1- Service Contract Item and SCN2. SC Itm (Pri.Adptn.).Note The Customer Service Manager can use the Monitor Auto Renewal Logs application tile to see the protocols of the autorenewal execution process for a specific timeframe and identify in case of execution errors, which service contracts are affected.Note To know more about how Auto Renewal works for Service Contracts when Credit Check is enabled, please see [Credit Management for Service Contracts](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/LATEST/en-US/2f7ce9927b424492b5e3e25656e8bfca.html). | The service contract item is set for renewal. |  |
| 6 | Assign Service Level Agreements | Optionally you can select in section Service Level Agreements the response and service profiles for this service contract item. To do so, fill the following fields with the values:Response Profile: First Level Response TimeService Profile: Mo-Fr: 7-17hNote The service level agreements can influence the price of the item, if you have maintained service level specific prices. |  |  |
| 7 | Edit Price Elements | Select the tab Billing Plan.In the field Settlement Period select via the value help Quarterly.Select the tab Price Details.For Price Element Price f.SRV.Cntr.Itm change the Price: for example to 90 AED.Choose Enter.Note If the price details tab is not visible you can add it via Personalize on item details view.Choose Add and select the Price Element Monthly Abs. Disc. (Price Element ID: DRV2). Add in the new row for the Price Element Monthly Abs. Disc. the absolute discount you would like to give, for example - 10 AED.Note The Price Element with ID: PMBL is not meant for the used item category.Choose Enter and and then choose Reprice.Choose Back to navigate to the Service Contract: xxxxxxxxxx, Description. | All billing plan lines has changed to the new price. |  |
| 8 | Edit Billing Plan | Choose the Billing Plan tab.In the Settlement Period drop down, choose Quarterly from the value help. | All billing plan lines have changed to the new billing values. |  |
| 9 | Maintain Reference Object (optional) | In section Items, in column Actions, choose Edit.Choose tab Object List.If the service contract item is only relevant for specific objects, for example, a machine or a location, you can optionally assign one or several reference objects to the item. To do so, in the item’s Object List, use the value help for Equipment ID, Functional Location ID, or Product ID to find a relevant object. For example, assign one of the Functional Location IDs starting with XX.Note If you assign a reference object, the service contract will only be determined in a service order if the same reference object is maintained in the service order as well.Choose Back to navigate to view Service Contract: xxxxxxxxxx, Description. |  |  |
| 10 | Change Employee Responsible (Optional) | On Service Contract Item Details view, in the section Parties Involved, choose Edit List, for Partner Function: Employee Responsible change Employee Responsible via the value help in column Name and choose Enter.Choose Save.Note The system determines a profit center for each service contract item.The system first determines the cost center of the employee responsible for the item and then the profit center that is defined for this cost center. You can also manually change the profit center assigned to a service contract item.For more information, please visit the documentation Profit Center Determination on SAP help portal.Choose Back to navigate to view Service Contract: xxxxxxxxxx, Description. |  |  |
| 11 | Add Attachments | Choose tab Attachments and choose Edit. Then choose Upload. |  |  |
| 12 | Drag and drop file to upload | Drag the file you want to upload to the Attachments dialog box.Note Multiple files can be uploaded by drag and drop from Windows Explorer.Optionally you can Add a Link . | New attachments are assigned to the service contract.Status is: Draft |  |
| 13 | Save and release | In section Items, choose Release All Items.Choose Save. | Note If you have enabled credit check management for service contracts and if the service contract is blocked due to the check then kindly refer to Scope item 1QM to resolve it |  |

#### Maintain Product List and create Price Agreement for Service Order Product

Purpose

The customer service manager creates a price agreement for a service contract on header level, that will be taken into account in a service order to which the service con-tract is assigned.

The customer service manager assigns a service product to the service contract and creates a product price agreement for this product. If the product is used in a service order and the service contract is assigned to the related service order item, the contract-specific price for the product will be determined instead of the standard product price.

The service contract determination is part of the 3D2 (Service Order Management and Monitoring) test case.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. |  |  |
| 2 | Create Service Contract | Choose Create and maintain the following entries:- Description: Enter a description- Sold-to-Party: Domestic UAE Customer 1 (ID: 33100001), or one of the sample customers available in your system.If contact persons are displayed in a Partner Selection Document header dialog box, select one of them.- Contract Start: the first of this month- Contract End: the first of this month in one yearIn section Items add the product SRV_01 in the column Product ID and choose Enter. In the column Quantity add the quantity 1 and choose Enter. | The contract start date and end date are determined automatically and can be modified. |  |
| 3 | Add Price Agreement on Header Level | Navigate to Price Agreement and choose Add.On the Choose Condition Type and Key Combination dialog box, maintain the following entries:Condition Type: Dis.f.Srv.Contr. (DSC3)Access: Doc.Cat./ID/ItmNo. Doc/Material (010)Then choose OK. | The Price Agreement screen is displayed. |  |
| 4 | Maintain Price Agreement | On the Service Contract - Price Agreements screen, maintain the following entries:Condition Amount: Maintain a price, for example, 10,00Condition Curreny: % (defaulted)Valid From: Optionally update the system proposalValid to: Optionally update the system proposal, for example, end of the contractThen choose OK. | A price agreement for a service contract has been maintained. |  |
| 5 | Navigate to Items | In section Items, in column Actions, choose Edit. | The Service Contract Item screen is displayed. |  |
| 6 | Add Product in Product List | In the item’s Product List, maintain Product ID: SRV_01. | The SRV_01 product has been added to the product list. |  |
| 7 | Add Product in Product List from Product Proposal (Optional) | In the item's Product List, choose Product Proposal. In the Product Proposal dialog box, choose the Source Type from drop down and Source from the value help.Note Maintain the Products/Equipments in the Object List tab. The values maintained will appear under the value help for Source in Product Proposal dialog box.Note The list of associated Products and Equipments must be modelled as Bill Of Materials (BOM). For more information on how to create Material and Equipment BOM, please refer to [63J - Create Material and Equipment BOM for Service - MDS](https://help.sap.com/viewer/12667b42a12041c9a40d6ce2697671ac/latest/en-US).For more information, please see [Service and Product List](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/LATEST/en-US/b748b7ac92d7484584f0ebf109e0e6c1.html). | The selected Product or Equipment BOM is inserted in Product List. |  |
| 8 | Choose Condition Type for Price Agreement | It is also possible to create price Agreements on item level.Navigate to Price Agreement on item level and choose Add.On the Choose Condition Type and Key Combination dialog box, maintain the following entries:Condition Type: MtrlPr.in Serv.Cntr (PSC0)Access: Doc.Cat./ID/ItmNo. Doc/Material (010)Then choose OK. | The Price Agreement screen is displayed.The price agreements are displayed under the section Price Agreement. |  |
| 9 | Maintain Price Agreement | On the Service Contract Item - Price Agreements screen, maintain the following entries:Product: SRV_01Condition Amount: Maintain a price, for example, 22,00Condition Currency: If relevant for your solution, optionally update the system proposal.Pricing Unit: 1Unit of Measure: HR (for service product SRV_01)Valid From: Optionally update the system proposal.Valid To: Optionally update the system proposal.Then choose OK.Note Optionally you can add further price agreements like described above. For example, you can maintain a percentual discount for a product with condition type MatlDisc. inSrvc.Cntr (DSC1), or a percentual discount for a material price group with condition type GrpDiscMatlPrSrvCntr (DSC2).Choose Back.Choose Release All Items.Choose Save. | A price agreement for a service product has been maintained. You can verify your entries in the Price Agreement view of the Service Contract Item screen. |  |
| 10 | Create Service Order with Reference to Service Contract | To verify that the service contract's price agreement for service product SRV_01 is determined in the service order, create a service order as described in the Service Order Management and Monitoring (3D2) scope item, chapter Service Order -> Service Items->Create Service Order. Important: Make sure to use the same customer in the service order as you use for the service contract, for example: Domestic UAE Customer 1 (ID: 33100001)Navigate to Price Details tab of the service order.Important: The service contract must be released so that it can be determined in the service order.Assign the service product SRV_01 to your service order. | The product price for SRV_01 used in the service order is updated to the price you have maintained in the service contract’s price agreements.Note There is an SSC-UI available to specify the service contract determination per transaction type. |  |

#### Adapt Service Contract Prices

Purpose

Over time, service contract prices might need to be adapted. For example, the initial price is valid until end of the year, and a new price becomes valid in the new year.

As well the Customer Service Manager creates Service contract item with item category SCN4 POC service contract item for price adaption (POC SC Itm(Pr.Adp.)) for Cost based percentage of completion method of revenue recognition for price adaption.

Procedure for Price Adaptation Item

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open Manage Service Contracts application | Log on as Customer Service Manager, choose the Manage Service Contracts application tile. |  |  |
| 2 | Create new Service Contract | Choose Create and maintain the following entries in theService Contract Details:Description: Enter a descriptionSold-to-Party: For example, Domestic UAE Customer 1 (ID: 33100001)If contact persons are displayed in a Partner Selection Document header dialog box, select one of themContract Start: the first of this month (it should be a month from the first half of the year)Contract End: the first of this month in one year |  |  |
| 3 | Maintain Service Contract Item | In section Items add the product “SRV_CONTRACT” in the column Product ID and choose Enter. In the column Quantity add the quantity “1” and choose Enter.Note Choose SCN4 PoC SC Itm(Pri. Adptn.) Item Category for Cost based Percentage of complete method.On the popup Item Category, choose OK. |  |  |
| 4 | Change Settlement Rule | In the column Actions choose Edit to navigate to the “Service Contract Item Details” view in edit mode.Select the tab Billing Plan. In section Settlement Rules in the field Pricing Date select via the value help Settlement Start Date in Billing Request Line. | All billing plan lines changed to the new price for each time period as defined in the condition record for the product. |  |
| 5 | Change Prices | Choose Change Prices - Fast Entry to change the price for the last three months of the contract. To do so fill the fields on the pop up with the following values:SettlementStart: “the third month before the contract end date”SettlementEnd: “the last month of the contract duration”Condition Type: “Man.Price f. BRqLine (PMBL)”Net Value: “value you want to define as price for the last three months of the service contract”Choose Save Changes.Optionally you can go to the first column of the table Actions and choose the link Details to navigate to the Billing Request Line Details. In the next screen select the tab Price Details.Choose Add and select the Price Element “Man.Price f. BRqLine” (Price Element ID: PMBL). Add in the new row for the Price Element “Man.Price f. BRqLine” a new price for the product, for example, 90 AED.Choose Enter.Choose Reprice.Choose Back. | The price has been chanced manually in the billing request line. |  |
| 6 | Check Prices | The column Billing Value in the table below contains now different product price for the two time periods as defined in the condition record in the previous step. | Billing plan lines have changed to the new price for the defined time periods. |  |
| 7 | Release and Save | Navigate back to view Service Contract: xxxxxxxxxx, Description.Choose Release All Items.Choose Save, | The new Service Contract is created.Success massage is displayed. |  |

#### Create a Service Contract Item for Ad-hoc Billing

Purpose

The customer service manager creates a service contract item with item category SCN3 that can be billed according to progress, for instance when certain milestones are reached or services have been fullfiled for the customer.

As well the Customer Service Manager creates Service contract item with item category SCN5 POC service contract item for ad hoc billing (POC SC Itm (Ad Hoc)) for Cost based percentage of completion method of revenue recognition.

Procedure for Ad-Hoc Billing Item

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open Manage Service Contracts application | Log on as Customer Service Manager, choose the Manage Service Contracts application tile. |  |  |
| 2 | Create new Service Contract | Choose Create and maintain the following entries in theService Contract Details:Description: Enter a descriptionSold-to-Party: For example, Domestic UAE Customer 1 (ID: 33100001)If sales organizations are displayed in a Select Orangizational Data dialog box, select Sales Organization:3310, Distribution Channel:10.If contact persons are displayed in a Partner Selection Document header dialog box, select one of them.Contract Start: the first of last monthContract End: the first of last month in one year | The service contract details are mainted |  |
| 3 | Maintain Service Contract Item | In section Items add the product “SRV_CONTRACT” in the column Product ID. In the column Quantity add the quantity “1” and choose Enter.Note Choose SCN5 (PoC SC Itm (ad Hoc)) for Cost-based Percentage of completion (POC) method of revenue recognition for Service contracts.In the column Item Category select SC Itm (Ad-hoc Bill)In the pop up Item Category choose OKChoose Save |  |  |
| 4 | Maintain Billing Request Line | In the column Actions choose Edit to navigate to the “Service Contract Item Details” view in edit mode.Note Auto renewal is not possible for this item category.Select the tab Billing Plan. In section Ad-hoc BillingChoose InsertEnter the following values:Billing Date: e.g.today’s dateBilling Value: e.g. 500Currency: USDChoose Enter. | A billing request line is entered, billing status is Not transferred to billing.In section Billing Plan the field % of Net Value Planned for Billing is updated. |  |
| 5 | (Optional) Change Prices | Optionally you can enter a fix amount for this item.Select the tab Price Details.Choose Add and select the Price Element “Manual Item Amount” (Price Element ID: PMV1). Add in the new row for the Price Element “Manual Item Amount” a new price for the product, for example, 2000 USD.Choose Enter.Choose Reprice. | The price has been chanced manually in the billing request line. The Status of the Price Element Price f.Srv.Cntr.Itm is Price Element Inacitv.In section Billing Plan the field Net Value is up-dated to 2000 USD and the field % of Net Value Planned for Billing is updated accordingly. |  |
| 6 | Bill Remaining Net Value | In section Ad-hoc BillingChoose Bill Remaining Net ValueIf an error message occursItem 100: Duplicate billing dates exist. Delete the duplicate or change a date.Change the following value:Billing Date: e.g.first of next monthThe fieldsBilling Value andCurrency are updated automaticallsChoose Enter. | The field % of Net Value Planned for Billing is up-dated to 100 %. |  |
| 7 | Release and Save | Navigate back to view Service Contract: xxxxxxxxxx, Description.Choose Release All Items.Choose Save, | The new Service Contract is created.Success massage is displayed. |  |

#### Print Service Contract

Purpose

The Customer Service Manager prints out the service contract or sends it as e-mail to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 3 | Search for Service Contracts | Enter search terms in filter bar and choose Go.For example, enter a service contract number in Transaction ID Contract field. | Service contract is displayed in result list. |  |
| 4 | Select Service Contract | Choose a service contract with Error Status: No Errors. | Service Contract is displayed. |  |
| 5 | View Output Items | On the Service Contract: xxxxxxxxxx, Description view, choose the Output Items tab. | View Output Details is displayed. |  |
| 6 | Send Output | In section Output Items, select a line with output channel you want to use.Choose Send Output to print the document or send it via e-mail. | Document is sent to the selected output channel. |  |
| 7 | Display Print Preview | To display the document, in the Display column choose Display Document. Optionally save a local copy of the PDF document. | A PDF document is displayed. |  |

### Service Contract Billing

#### Schedule Billing Document Request Creation

Purpose

The Customer Service Manager creates a job to schedule the billing document request creation. This step is a prerequisite so the billing clerk can check the billing requests and create invoices accordingly. The creation of billing request lines as per billing plan for one service contract is followed by:

Event-based Revenue Recognition, refer to the steps described in the scope item 3M3 (Event-based Revenue Recognition).

Account receivable, refer to the steps described in the J59 (Account Receivables) scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Schedule Billing Document Request Creation application is displayed. |  |
| 2 | Open Schedule Billing Document Request Creation application | Choose the Schedule Billing Document Request Creation application tile. | The list report page is displayed. |  |
| 3 | Create a new Job | On table tool bar, choose Create to create a new job.In step 1 Template Selection select the job template “Schedule BDR Creation” via the value for Job Template.Enter your job name in the field. Choose Step 2.Choose Define Recurrence Pattern in the section Scheduling Options.Start immediately checked.Recurrency pattern: Single RunChoose Step 3.In section Parameters leave the field BDR Creation Horizon (in days) empty to generate all the BDRs.Leave the field Service Contract IDs empty.In this case the job will be scheduled for all Service Contracts.Optionally you can schedule a job for one single service contract. To do so, follow all the previous steps from chapter Schedule Billing Document Request Creation and enter in the field Service Contract IDs the ID of the Service Contract for which you want to schedule the Billing Document Request Creation.Note Either field BDR Creation Horizon (in days) or field Service Contract IDs should be specified. Both fields cannot be left empty.Choose Schedule . | The new job is created.The new job is displayed in the list report page. |  |

#### Manage Billing Document Requests

Purpose

The Billing Clerk has identified one Service Contract and wants to check, if a Billing Document Request is already available for it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Billing Clerk. | The Fiori Launchpad with access to the Manage Billing Document Request application is displayed. |  |
| 2 | Open Manage Billing Document Requests application | Choose the Manage Billing Document Requests application tile. | The list report page is displayed. |  |
| 3 | Search for the Service Contract to be checked | To find the service contract for which the Billing Document Request should be checked, use the available filters Source Document: Service Contract ID and Status: To Be Invoiced.Choose Go. | The Billing Document Requests associated with the searched Service Contract are displayed in the result list. |  |
| 4 | Display Billing Document Request | To display one Billing Document Request, choose the row containing the Billing Document Request ID in the result list.Note the ID of the selected Billing Document Request for which the Invoice needs to be created.To close the Billing Document Request Details view, choose Exit . | The Billing Document Request Details view of the corresponding billing document request ID is displayed. |  |

#### Create Billing Document (Invoice)

Purpose

The Billing Clerk has identified one Billing Document Request for which the Invoice Document needs to be created manually.

|  |
| --- |
| Note To adjust the billing document output to your needs, refer to [Extensibility for Output Forms and Email Templates of Billing Documents](https://help.sap.com/viewer/DRAFT/a376cd9ea00d476b96f18dea1247e6a5/2005.500/en-US/0b6ec00b397349b09ec69ec7e60c2667.html). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Billing Clerk | The Fiori Launchpad with access to the Create Billing Documents application is displayed. |  |
| 2 | Access the App | Open the Create Billing Documents (F0798) app. | The Create Billing Documents screen is displayed. |  |
| 3 | Define Billing Settings | In the Create Billing Documents view, choose Billing Settings.On the Billing Settings dialog window, maintain the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFFChoose OK. | The Billing Settings dialog window is displayed. |  |
| 4 | Search for a Billing Document Request | To find the Billing Document Request noted in previous chapter Manage Billing Document Requests for which the Invoice shall be created, use the available filters SD Document and SD Document Category: “<Billing Document Request>”.Choose Go. | The billing document request is displayed in the result list. |  |
| 5 | Select Item(s) for Billing | To create the Invoice Document, select the check box in front of the row with the Billing Document Request for which the Invoice should be created.Choose Create Billing Documents. | A Create Billing Documents dialog window is displayed. |  |
| 6 | Maintain Billing Data | Choose the following values:Billing Type : F2 Invoice (F2)Billing Date: <current date> | The F2 Invoice screen is displayed. |  |
| 7 | Save Billing Document | Invoice screen, choose Save.The billing document with ID xxxxxxxx is created. Make a note of the billing document number for further reference. | Billing document is created. |  |
| 8 | Open Manage Billing Documents application | Choose the Manage Billing Documents application tile. | The list report page is displayed. |  |
| 9 | Search for an Invoice Document | To find the newly created Billing in the previous step, use the available filter Billing Document. | The searched Billing Document is displayed in the result list. |  |
| 10 | Display Invoice Document | To display the Invoice Document, choose the row on the result list, containing the searched Invoice ID. | The Invoice Details view of the corresponding Invoice ID is displayed. |  |

### Service Contract Change Processes (optional)

#### Manually renew a Service Contract Item

Purpose

You can use this change process to create a follow-up item in the system when a service contract item ends.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 2 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 3 | Create new Service Contract | Choose Create and fill the following Service Contract header fields in section Service Contract Details:- Description:enter a description- Sold-to-Party: "Domestic UAE Customer 1" (ID: 33100001If contact persons are displayed in a Partner Selection Document header dialog box, select one of them- Contract Start:“the first of this month”- Contract End: “the first of this month in one year”Under the section Items add the product “SRV_CONTRACT” in the column Product ID and choose Enter. In the column Quantity add the quantity “1” and choose Enter.In section Items, choose Release All Items. Choose Save. | The new Service Contract is created.Success massage is displayed. |  |
| 4 | Define manually the renewal of the Service Contract Item | In section Items choose the item number in the first column' with: in column Actions, choose Edit to navigate to the Service Contract Item Details view.Choose Change Processes to define the renewal of the service contract item.On the next screen Service Contract Item: 100, Service Contract Product - Change Processes select via the drop-down list the valueContract Renewal - One Item Only and choose Enter.In section Change Process Parameters, check and change the default values if needed:- Date Received: “current day”- Duration: “6 Month”Choose Execute Change Process.Choose Back to navigate Service Contract: xxxxxxxxxx view.Choose Save. | The service contract item has been renewed.Item executed with message: Change process executed for item 100. |  |
| 5 | Check info and release item after the renewal | On service contract detail page, check relevant information.A new item line 200 is added in the item table with following values:- Status: open- Contract Start: Current date of Next Year' with '+ one year- Contract End:Current date + 6 months + one year- Quantity:1Note One Service Contract item can be renewed only one time an only when it is in status Released. The item should not be canceled or set for auto renewal. | The Service contract is updated.A new service contract item is created. |  |

#### Manually renew a Service Contract

##### Renew by creating new item

Purpose

You can use this change process to extend the validity period of all the items that are contained in a released service contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 2 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 3 | Create new Service Contract | Choose Create and fill the following Service Contract header fields in section Service Contract Details:- Description:enter a description- Sold-to-Party: Domestic UAE Customer 1 (ID: 33100001If contact persons are displayed in Partner Selection Document header dialog box, select one of them- Contract Start:the first of this month- Contract End: the first of this month in one yearIn section Organiational Data, fill the following details.- Sales Organization: 1010- Distribution Channel: 10- Division: 00In section Items add the products SRV_CONTRACTIn the column Quantity add the quantity 1 and choose Enter.Add a second item:Product ID: SRV_CONTRACTQuantity: 1Item Category: SC Itm (Pri Adoptn.)In section Items, choose Release All Items.Choose Save, | The new Service Contract is created.Success massage is displayed. |  |
| 4 | Maintain Price Agreement | In section Items, in column Actions, choose Edit to navigate to the Service Contract Item Details view.Navigate to Price Agreement and choose Add.On the Choose Condition Type and Key Combination dialog box, select the relevant Condition Type PSC0 and Access.Choose OK.On the Service Contract Item – Price Agreements screen, maintain the following entries:Product: SRV_CONTRACTCondition Amount: Maintain a price, for example, 25,00Condition Currency: If relevant for your solution, optionally update the system proposal.Pricing Unit: 1Unit of Measure: HR (for service product SRV_01)Valid From: Optionally update the system proposal.Valid To: Optionally update the system proposal.Choose OK.Choose Apply.Choose Save. |  |  |
| 5 | Define manually the renewal of the Service Contract | On Service Contract detail page, select Change Processes.On the next screen, Service Contract: ********(Contract ID), ******(Contract Description) - Change Processes select Contract Renewal - New Items from the dropdown list and choose Enter.Under the Section Change Process Parameters Select check-box Release Automatically and check the default values- Date Received: current day- Duration: 6 MonthChoose Execute Change Process.Choose Back to navigate to the Service Contract: xxxxxxxxxx view, then choose Save. | The service contract has been renewed.Item executed with message: Change process executed.To execute the change process, make sure that your service contract does not contain any errors and that the status is set to Released. The items should not be canceled or set for auto renewal. |  |
| 6 | Check info of released item after the renewal | On Service Contract detail page, check relevant information.New item lines are added in the item table with following values:- Status: ReleasedIn section Items, in column Actions, choose Edit to navigate to the Service Contract Item Details view of the automatically created items:- Contract Start: Date of original service contract item + 1 year- Contract End: New contract start date + 6 months- Quantity:1Note If the check-box of Release Automatically was not checked the Status of new items will be Open. | The Service contract is updated and new items are created for all items in the existing contract. |  |
| 7 | Check Price Agreements in new contract items | On the Service Contract Item – Price Agreements screen, check the entries for the newly created items. | All condition records for the Price Agreements have been copied to the new items.Note When copying, editing or deleting contract items which includes price agreements, the price agreements are copied, edited or deleted as well. |  |

##### Renew by creating new contract

Purpose

You can use this change process to extend the validity period of all the items that are contained in a released service contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 2 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 3 | Create new Service Contract | Choose Create and fill the following Service Contract header fields in section Service Contract Details:- Description:enter a description- Sold-to-Party: Domestic UAE Customer 1 (ID: 33100001If contact persons are displayed in Partner Selection Document header dialog box, select one of them- Contract Start:the first of this month- Contract End: the first of this month in one yearIn section Organiational Data, fill the following details.- Sales Organization: 1010- Distribution Channel: 10- Division: 00In section Items add the products SRV_CONTRACTIn the column Quantity add the quantity 1 and choose Enter.Add a second item:Product ID: SRV_CONTRACTQuantity: 1Item Category: SC Itm (Pri Adoptn.)In section Items, choose Release All Items.Choose Save, | The new Service Contract is created.Success massage is displayed. |  |
| 4 | Maintain Price Agreement | In section Items, in column Actions, choose Edit to navigate to the Service Contract Item Details view.Navigate to Price Agreement and choose Add.On the Choose Condition Type and Key Combination dialog box, select the relevant condition type PSC0 and Access.Choose OK.On the Service Contract Item – Price Agreements screen, maintain the following entries:Product: SRV_CONTRACTCondition Amount: Maintain a price, for example, 25,00Condition Currency: If relevant for your solution, optionally update the system proposal.Pricing Unit: 1Unit of Measure: HR (for service product SRV_01)Valid From: Optionally update the system proposal.Valid To: Optionally update the system proposal.Choose OK.Choose Apply.Choose Save. |  |  |
| 5 | Define manually the renewal of the Service Contract | On Service Contract detail page, select Change Processes.On the next screen, Service Contract: ********(Contract ID), ******(Contract Description) - Change Processes select Contract Renewal - New Contract from the dropdown list and choose Enter.Under the Section Change Process Parameters Select check-box Release Automatically and check the default values- Date Received: current day- Duration: 6 MonthChoose Execute Change Process.Choose Back to navigate to the Service Contract: xxxxxxxxxx view, then choose Save. | New service contract has been created.Succesfully executed with message: Transaction ***** saved.To execute the change process, make sure that your service contract does not contain any errors and that the status is set to Released. The items should not be canceled or set for auto renewal. |  |
| 6 | Check info of released contract after the renewal | On Service Contract detail page, check relevant information.New line item added in Transaction History section with the following values:- Transaction Type: Service Contract- Status: ReleasedIn column Transaction, select the transaction to navigate to next screen to view the items.On the next screen, Service Contract: ********(Contract ID), ******(Contract Description), in the Items section, new items are created with the following value:- Product ID: SRV_CONTRACT- Quantity: 1Note If the Release Automatically checkbox was not selected, then the status of new items will be Open. | The Service contract is updated.New items are created for all items in the existing contract. |  |
| 7 | Check Price Agreements in new contract items | In Items section of the newly created contract, choose the item and navigate to Price Agreement section.Check the entries for the newly created items of new service contract. | All condition records for the Price Agreements have been copied to the new items.Note When copying, editing, or deleting contract items which includes price agreements, the price agreements are copied, edited, or deleted as well. |  |

#### Change Sold-to Party

Purpose

You can use change processes to change sold-to party for an active service contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 2 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 3 | Search for Service Contracts | Select the service contract you have created in chapter [Create Service Contract](#unique_14) [page ] 26. | The contract is displayed. |  |
| 4 | Display Service Contract Details | Choose Change Processes. | The change process selection screen is displayed. |  |
| 5 | Select change process | Choose CSLT - Change Sold-to Party via value help. | The change process parameters appear. |  |
| 6 | Enter data | In field Date received enter the data, when you received the information for the change of the sold-to party, for example todays date.In the field New Partner enter the ID of the new sold-to party, for example 33100003.In the field Effective Date enter the date, when the change shall be effective, for example first of next month.Select checkbox Release Automatically. | Necessary data for the change process is entered. |  |
| 7 | Execute change process | Choose Execute Change Process.Choose Back. | A new contract is created and released with the new sold-to party. The new contract is shown in the Transaction History.This contract will be valid from the effective date until the end-date of the original contract.The end-date of the original contract: item changes to the effective date. |  |
| 8 | Save | Choose Save. |  |  |

#### Cancel Service Contracts

Purpose

The Customer Service Manager has identified a service contract that must be cancelled. In this case, the manager can cancel the contract by adding a cancelling party, date, and reason.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 2 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 3 | Search for the Service Contract to be canceled | To find the service contract to be canceled use the available filters, for example Description. The description of the contract you want to cancel.Choose Go. | The service contract is displayed in the result list. |  |
| 4 | Cancel single Service Contract Items | To cancel single service contract items, choose the row containing the Service Contract ID.In In section Items in column Actions, choose Edit in the row with the item you would like to cancel.In the view Service Contract Item Details, select the tab Cancellation and fill the fields with the following values:Actual Cancellation Date: a date within the service contract validityCancelling Party: CustomerReason: Price increaseChoose Back.Choose Save.Go back to the service contracts list view. | The service contract item has been canceled.Success message is shown. |  |
| 5 | Cancel a Service Contract from the list report page | In the result list select the check box in front of the row with the Service Contract you want to cancel.Choose Cancel .On the dialog Cancel Service Contract maintain the required information:In the field Canceling Party select via the value help Vendor.In the field Cancellation Date enter via the value help the Date when the contract should be canceled.In the field Reason select via the value help Payment Missing.Choose Cancel Service contract. | The selected service contract (and all items associated) is canceled.If any error occurs during canceling, an error message is displayed. |  |

## Service Contracts Dashboard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SAP Analytics Cloud (SAC) provides a comprehensive tool for strategic live-data analysis in solution business. The Purpose is to help the Sales Manager to review the Service Contract that are going to expire or Service contract that has maximum profitability.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Choose app Service Contracts Dashboard | The Service Contracts Dashboard app is displayed. |  |
| 3 | Overview Page | Choose Overview from the dropdown. | The Overview page shows Net Value of Service Contracts and Net Value of Canceled Service Contracts. |  |
| 4 | Service Contract Item Details | Choose Service Contract Item Details from the dropdown. | The Service Contract Item Details page shows Net Value of Service Contract Items and Service Contract Item Details. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can precede this process.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 43B | Service Monitoring and Analytics |
| J59 | Accounts Receivables |
| 3M3 | Event -Based Revenue Recognition - Service Documents |
| 3M4 | Event -Based Revenue Recognition - Service Documents - IFRS |
| 3M5 | Event -Based Revenue Recognition - Service Documents - US GAAP |
| 3D2 | Service Order Management |
| 49X | Service Order Processing with SAP Field Service Management |
| 3XK | In House Repair |
| 4GG | Credit Memo Processing for Service Processes |
| 4V7 | Predictive Accounting for Service Contract Management |

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
> Flagged while digesting this document, not verified: Internal contradiction in Schedule Billing Document Request Creation: steps say leave both BDR Creation Horizon (in days) and Service Contract IDs empty to schedule all contracts, but a note says either field must be specified and both cannot be empty.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample data lists Sales Organization 3310 (with UAE customer 33100001), but the renewal procedures instruct entering Sales Organization 1010 for the same customer.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/service-contract-management-with-advanced-variant-configuration-6gu-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3MO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 88,856 chars in the whole document
