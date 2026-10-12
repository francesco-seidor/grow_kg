---
id: 15-retail-operations/replenishment-planning-for-distribution-centers-3i8-ae-test-script-947
title: Replenishment Planning for Distribution Centers (3I8_AE) - Test Script (3I8_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3I8_AE: DC replenishment via forecast, PIR, MRP runs, background jobs and purchase requisition checks."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/dc-replenishment-planning]
aliases: [3I8_S4CLD2608_BPD_EN_AE]
keywords: [Replenishment Planning for Distribution Centers, replenishment planning, distribution center replenishment, forecast run, planned independent requirements, mrp run, material coverage, purchase requisitions, periodic background jobs, article master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I8_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-947
topic: 15-retail-operations/dc-replenishment-planning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Replenishment Planning for Distribution Centers (3I8_AE) - Test Script (3I8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Replenishment Planning for Distribution Centers** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Replenishment Planning for Distribution Centers (3I8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852987)

[2 Prerequisites 4](#_Toc232852988)

[2.1 System Access 4](#_Toc232852989)

[2.2 Roles 4](#_Toc232852990)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852991)

[2.4 Preliminary Steps 5](#_Toc232852992)

[2.4.1 Check the Master Data Settings 6](#_Toc232852993)

[2.4.2 Maintain Consumption Values 8](#_Toc232852994)

[2.4.3 Define Planning Calendar 9](#_Toc232852995)

[3 Overview Table 11](#_Toc232852996)

[4 Test Procedures 12](#_Toc232852997)

[4.1 Material Requirement Planning for an Article 12](#_Toc232852998)

[4.1.1 Execute Forecast Run 12](#_Toc232852999)

[4.1.2 Create Planned Independent Requirement (PIR) 12](#_Toc232853000)

[4.1.3 Check Material Coverage and Start MRP Run 13](#_Toc232853001)

[4.2 Periodic Background Jobs 14](#_Toc232853002)

[4.2.1 Schedule Job for Forecast Calculation 14](#_Toc232853003)

[4.2.2 Schedule Job for Copying Total forecast Runs 16](#_Toc232853004)

[4.2.3 Schedule Job for MRP 18](#_Toc232853005)

[4.2.4 Monitor Purchase Requisitions 19](#_Toc232853006)

[5 Appendix 21](#_Toc232853007)

[5.1 Process Integration 21](#_Toc232853008)

[5.1.1 Succeeding Processes 21](#_Toc232853009)

## Purpose

Overview

The goal of the replenishment process for distribution centers is to calculate optimal dates and quantities for the procurements of reorderable articles from suppliers to best meet demand.

First, demand is determined by executing forecasting algorithms on historical consumption data, considering various factors (such as seasonality) to feed into consumption-based planning. Alternatively, demand can be expressed by planned independent requirements (PIR).

Next, material requirements planning (MRP) is executed to calculate the optimal quantities and dates for the procurement. The replenishment calculation considers demand, current stock situation, already planned goods receipts, and supplier parameters. MRP can be controlled via different MRP types (for example, time phased planning), for which it's possible to specify certain weekdays for ordering and delivery.

The result of the MRP execution is then handed over to the operational procurement via purchase requisitions.

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

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Replenishment Specialist - Distribution Center (Retail) | SAP_BR_RPLNMT_SPCLST_DC_RFM | DC Replenishment | SAP_BR_RPLNMT_SPCLST_DC_RFM |  |
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Article | R_1032 | Frozen Carrots |  |
| Article | R_1003001 | Chocolate, Whole-Milk, DietVariant : R_1003001 |  |
| Material Type | Trading Goods | HAWA Trading Goods |  |
| Material Category | 0001 | Single MaterialGeneric Material |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 50 | Distribution |  |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC |  |
| MRP Controller | 001 | MRP Controller 001 |  |

### Preliminary Steps

This section provides an overview of detailed technical steps and other relevant prerequisites.

You can check the master data settings within the manage product master data app.

Currently Maintain Article (MM42) app is being used for maintaining the consumption related data.

User can create/view the details of calculation data and planning periods maintained in the planning calendar.

#### Check the Master Data Settings

Purpose

This step details out the mandatory settings needed for executing the replenishment run in a distribution center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (Retail) role. |  |  |
| 2 | Access the App | Open Maintain Article (MM42) app. | Change Material (Initial Screen) screen is displayed. |  |
| 3 | Enter Parameters | On the Change Material (Initial Screen) screen enter the following data:Material: R_1032Purchasing Org: 3310Supplier: 33213002Sales Org.: 3310Distr.Channel: 50Distr.Center: 3350and select Logistics: Distribution Center in the Views section.Choose Continue. | Change Material R_1032 (Logistics: Distribution Center) screen is displayed. |  |
| 4 | Check the Details | Check the below details:In the MRP Parameters sectionMRP Type: R1 - Time-Phased PlanningIn the Forecast Parameters sectionPeriod Ind.: W - WeeklyForecast model: K - Constant with smoothing factor adjustmentIn the MRP Controller/Replenishment Data section:MRP Controller: 001Planning Cycle: P01Delivery Cycle: P01Pl. Deliv.Time: 5 DaysSupply Source: 1In the General control parameters sectionAvail. Check: ST - Consider Only StockOptionally MRP Type: R2 - (Time-Phased Planning w.auto.reord.point). can be used if the system calculates the reorder point automatically. |  |  |
| 5 | Navigate back to Maintain Article App | Choose Back. | Change Material (Initial Screen) screen is displayed. |  |
| 6 | Enter Parameters | On the Change Material (Initial Screen) enter the following dataMaterial: R_1003001Purchasing Org: 3310Supplier: 33213002Sales Org.: 3310Distr.Channel: 50Distr.Center: 3350Flag Logistics: Distribution Center view in Views sectionChoose Continue. | Change Material R_1003001 (Logistics: Distribution Center) screen is displayed. |  |
| 7 | Check the Details | Check the below details:In the MRP Parameters sectionType: R1 - Time-Phased PlanningIn the Forecast Parameters sectionPeriod Ind.: W - WeeklyForecast model: K - Constant with smoothing factor adjustmentIn the MRP Controller/Replenishment Data sectionMRP Controller: 001Planning Cycle: P01Delivery Cycle: P01Pl. Deliv.Time: 5 DaysSupply Source: 1In the General control parameters sectionAvail. Check: ST - Consider Only StockOptionally MRP Type:R2 - (Time-Phased Planning w.auto.reord.point) . can be used if the system calculates the reorder point automatically. | The details are displayed. |  |
| 8 | Navigate to Home screen | Choose back till reaches Home screen. | Home screen is displayed. |  |

|  |
| --- |
| Note Alternatively you can choose “ Manage Product Master Data (F1602)” to check mandatory settings needed for executing the replenishment run in a Distribution Center |

.

#### Maintain Consumption Values

Purpose

Consumption values are needed for the forecast calculation.

Here is the possibility to maintain consumption values for testing purposes and manually correction.

This section explains the process for checking consumption values for material R_1032 and R_1003001.

|  |
| --- |
| Note Typically maintaining Consumption Data of Inventory for a material starts before you want to work with this material the first. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Maintain Article (MM42) app. | Change Material (Initial Screen) screen is displayed. |  |
| 3 | Enter Parameters | On the Change Material (Initial Screen), enter the following data:Material: R_1032Purchasing Org: 3310Supplier: 33213002Sales Org.: 3310Distr.Channel: 50Distr.Center: 3350Flag Logistics: Distribution Center in the Views section.Choose Continue. | Change Material R_1032 (Logistics: Distribution Center) screen is displayed. |  |
| 4 | Choose Consumption | Choose Consumption vals to maintain historical consumption values for material | Change Material R_1032 (Consumption: DC, Trading Goods) screen is displayed. |  |
| 5 | Maintain Consumption Values | Maintain below values for first 12 Periods in Corrected value columnCorrected value: 100Choose Goto Main Data. | Change Material R_1032 (Logistics: Distribution Center) screen is displayed. |  |
| 6 | Save Consumption values | Choose Save. | Material R_1032 changed message is displayed. |  |
| 7 | Enter Material | On the Change Material (Initial Screen), enter the following data,Material: R_1003001Purchasing Org: 3310Supplier: 33213002Sales Org.: 3310Distr.Channel: 50Distr.Center: 3350Flag Logistics: Distribution Center in the Views section.Choose Continue. | Change Material R_1003001 (Logistics: Distribution Center) screen is displayed. |  |
| 8 | Choose Consumption | Choose Consumption vals to maintain historical consumption values for material. | Change Material R_1003001 (Consumption: DC, Trading Goods) screen is displayed. |  |
| 9 | Maintain Consumption Values | Maintain below values for first 12 Periods in Corrected value columnCorrected value: 100Choose Goto Main Data. | Change Material R_1003001 (Logistics: Distribution Center) screen is displayed. |  |
| 10 | Save Consumption values | Choose Save. | Variant R_1003001 changed message is displayed. |  |

#### Define Planning Calendar

Use

The following procedure provides instructions for creating planning calendar.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Planning Calendar.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Planning Calendar: Change screen is displayed. |  |
| 3 | Define Planning Calendar | Create the following settings:Choose New Entries and enter the below details in the New Entries: Added Entries screen:Plant : <Enter Plant>Cal : <Enter Planning Calendar Name>Description : <Enter Description of Planning Calendar>Calculation Rule : <Enter Calculation Rule>Wkg Day In : <Enter Woking Day indicator>Per : <Period>Double click on Calculation Data option displaying on the left side of the screen in Dialog Structure section. |  |  |
| 4 | Choose New Entries in Calculation Data Screen | Enter the data in the Calculation Data section.Double click on Planning Periods option displaying on the left side of the screen in Dialog Structure section. |  |  |
| 5 | Choose New Entries in Planning Periods Screen | Choose Calculate Periods option.Planning Periods will get populated with periods. Choose Save. | Planning Calendar is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| ID (Role Template) | Name (Role Template) | App | Expected Results |
| --- | --- | --- | --- |
| [Execute Forecast Run](#unique_11) [page ] 12 | Replenishment Specialist - Distribution Center (Retail) | Schedule Material Demand Forecast Runs (F2464) | Job is defined and forecast results are displayed. |
| [Create Planned Independent Requirement (PIR)](#unique_12) [page ] 12 | Replenishment Specialist - Distribution Center (Retail) | Schedule Copy Total Forecast Runs (F2579) | Job is defined and planned independent requirement is created. |
| [Check Material Coverage and Start MRP Run](#unique_13) [page ] 13 | Replenishment Specialist - Distribution Center (Retail) | Manage Material Coverage - New Version (F0251A) | MRP run is initiated. |
| [Schedule Job for Forecast Calculation](#unique_14) [page ] 14 | Replenishment Specialist - Distribution Center (Retail) | Schedule Material Demand Forecast Runs (F2464) | Job is defined and forecast results are displayed. |
| [Schedule Job for Copying Total forecast Runs](#unique_15) [page ] 16 | Replenishment Specialist - Distribution Center (Retail) | Schedule Copy Total Forecast Runs (F2579) | Job is defined and purchase Info record is created. |
| [Schedule Job for MRP](#unique_16) [page ] 18 | Replenishment Specialist - Distribution Center (Retail) | Schedule MRP Runs (F1339) | Job is defined and the results are displayed. |
| [Monitor Purchase Requisitions](#unique_17) [page ] 19 | Replenishment Specialist - Distribution Center (Retail) | Monitor Stock / Requirements List - Old Version (MD04) | Purchase requisition is created and displayed. |

## Test Procedures

This section describes the procedures for each process step that belongs to this scope item.

This test procedures includes 2 major parts. The first part is about triggering Material Requirement Planning (MRP) for a selected article and the second part describes periodic background jobs used for mass processing.

### Material Requirement Planning for an Article

#### Execute Forecast Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process forecast values of the article is calculated.

Procedure

Execute chapter [Schedule Job for Forecast Calculation](#unique_14) [page ] 14 with Material: R_1032 to create planned independent requirement.

#### Create Planned Independent Requirement (PIR)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process PIR is created for the material.

Procedure

Execute chapter [Schedule Job for Copying Total forecast Runs](#unique_15) [page ] 16 with Material: R_1032 to create planned independent requirement.

#### Check Material Coverage and Start MRP Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process purchase requisition is created as follow on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Replenishment Specialist - Distribution Center (Retail) |  |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A) app. | The Manage Material Coverage screen is displayed. |  |
| 3 | Enter Parameters | Make the following entries and choose Go.Shortage definition: MRP StandardMaterial: R_1032Plant: 3350 | The Manage Material Coverage screen is displayed with the material details. |  |
| 4 | Run MRP to Create Purchase Requisition | Choose Navigation icon in the Materials section and choose Start MRP Run on the right screen. | The MRP run in progress notification is displayed first, and then MRP run was completed notification is displayed. |  |
| 5 | Verify Purchase Requisition | Verify whether the purchase requisition is created. | The purchase requisition is created. |  |

### Periodic Background Jobs

#### Schedule Job for Forecast Calculation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process forecast values of the article is calculated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Replenishment Specialist - Distribution Center (Retail) |  |  |
| 2 | Access the App | Open Schedule Material Demand Forecast Runs (F2464) app. | Application Jobs screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new job. | New Job: Schedule Material Demand Forecasting screen is displayed. |  |
| 4 | Enter job details | Enter the application job details in Template Selection and Scheduling Options sections(Step1).Job Template: Schedule Material Demand ForecastingJob Name: Schedule Material Demand Forecasting XXChoose Step 2Flag Start Immediately [Optional]Choose Define Recurrence Pattern if required to change the Recurrence Pattern. | Template Selection and Scheduling Options of job are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section, make the following entries:Plant: 3350Material: R_1032Note Article is optional for mass processing.Period Indicator: WForecast execution: F | Details in Parameter section are defined. |  |
| 6 | Check | Choose Check. | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule | Choose Schedule. | Job Schedule Material Demand Forecasting XX has been scheduled message is displayed.The Application Jobs screen displays again, and the new job displays in the Jobs table in Finished Status. |  |
| 8 | Navigate to Job Results | Figure out the newly create job row andChoose Results Icon displaying in Results column of the scheduled job. | Document (ID XXXXXXX) screen is displayed. |  |
| 9 | Check Job Results | In the Document (ID XXXXXXX) screen,Check details of Material no., Basic data, Control data, No. of values, Historical data , forecast results and Number of materials forecasts carried out sections.Check the forecast values for the next 12 periods displayed in Forecast results section. | Details verified and forecast values for next 12 periods is displayed. |  |

#### Schedule Job for Copying Total forecast Runs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process planned independent requirements are created for a material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Replenishment Specialist - Distribution Center (Retail) |  |  |
| 2 | Access the App | Open Schedule Copying Total Forecast Runs (F2579) app. | Application Jobs screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new application job. | New Job: Copy Total Forecast screen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Selection and Scheduling Options sections (Step 1).Job Template: Copy Total ForecastJob Name: Copy Total Forecast XXChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence Pattern. | Template Selection and Scheduling Options of job are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section, make the following entries:In the Forecast Restrictions section, make the following entriesPlant: 3350MRP Controller : 001Material: R_1032Note Article is optional for mass processing.In the Selection Period section, make the following entriesfrom : <dd.mm.yyyy>to : <dd.mm.yyyy>In the Requirement Parameters Section, make the following entriesRequirements Type : KSVVersion : 00Flag Requirement ActiveFlag Write HistoryIn the Mode Section, make the following entries :Uncheck No Database Changes (Simulation)In the Output Results section:Flag Results ListSelect Display Detailed Lists | Details in Parameter section are defined. |  |
| 6 | Check | Choose Check. | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule | Choose Schedule. | Job Copy Total Forecast XX has been scheduled message is displayed.The Application Jobs screen is displayed again, and the new job displays in the Jobs table in Finished Status. |  |
| 8 | Navigate to Job Results | Figure out the newly create job rowChoose Results Icon displaying in Results column of the scheduled job. | Document (ID XXXXXXX) screen is displayed. |  |
| 9 | Check Job Results | In the Document (ID XXXXXXX) screen,Check details of Items Selected Altogether, Items with Successful Transfer , Items Without Transfer, Items with Errors and the table with Article details and Status and so on. | Successful result is displayed. |  |

#### Schedule Job for MRP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process purchase requisition is created as follow on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Replenishment Specialist - Distribution Center (Retail) |  |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339) app. | Application Jobs screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new job. | New Job: Material Requirements Planning (MRP) screen is displayed |  |
| 4 | Enter job details | Enter the application job details in the Template Selection and Scheduling Options sections (Step 1).Job Template: Material Requirements Planning (MRP)Job Name: Material Requirements Planning (MRP)XXChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence Pattern. | Template Selection and Scheduling O ptions of job are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter Section, make the following entries:In the Planning Scope (Define at least one selection criterion.) section:Plant: 3350Material: R_1032Note Article is optional for mass processing.MRP Controller: 001In the Control Parameters section:Flag Regenerative PlanningScheduling: 1Planning Mode: 1Flag Output Material List (job log) | Details in Parameter section are defined. |  |
| 6 | Check | Choose Check. | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule | Choose Schedule. | Job Material Requirements Planning(MRP) XX has been scheduled message is displayed.Application Jobs screen displays again, and the new job displays in the Jobs table in Finished Status. |  |
| 8 | Navigate to Job Results | Figure out the newly create job row andChoose Results Icon displaying in Results column of the scheduled job. | Document (ID XXXXXXX) screen is displayed. |  |
| 9 | Check Job Results | In the Document (ID XXXXXXX) screen, check details of Records Passed and Article details displayed in the second table. | Successfully planned Info is displayed for the article in results. |  |

#### Monitor Purchase Requisitions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process purchase requisition is verified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Replenishment Specialist - Distribution Center (Retail). |  |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04) app. | Monitor Stock / Requirements List - Old Version (MD04): Initial Screen is displayed. |  |
| 3 | Enter Values | Enter the below values in the Individual A ccess sectionMaterial: R_1032Plant: 3350Choose Continue. | Stock/Requirements List as of HH:MM hrs screen is displayed. |  |
| 4 | Access Purchase Requisition | Select PurRqs MRP element displaying in the table | Additional Data for MRP Element pop up window is displayed. |  |
| 5 | Monitor Purchase Requisition | Verify details of Purchase Requisition | Purchase requisition details verified. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 5FM - Procurement for Retail | Purchase requisition is converted into a purchase order in the “Procurement for Retail”(5FM) process. |

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
- see-also :: [[15-retail-operations/test-script-store-ordering-from-distribution-center-5fx-ae-1092]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 31,976 chars in the whole document
