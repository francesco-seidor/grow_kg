---
id: 15-retail-operations/test-script-replenishment-planning-for-stores-3i7-ae-946
title: "Test Script: Replenishment Planning for Stores (3I7_AE) (3I7_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3I7_AE: store replenishment (forecast run, rapid replenishment run, scheduled jobs)."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/store-replenishment-planning]
aliases: [3I7_S4CLD2608_BPD_EN_AE]
keywords: [Replenishment Planning for Stores, store replenishment, rapid replenishment, demand forecasting, scheduled replenishment jobs, article master data, planned independent requirements, consumption values, dynamic target stock, stock transport requisitions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I7_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-946
topic: 15-retail-operations/store-replenishment-planning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Replenishment Planning for Stores (3I7_AE) (3I7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Replenishment Planning for Stores** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Replenishment Planning for Stores (3I7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852962)

[2 Prerequisites 4](#_Toc232852963)

[2.1 System Access 4](#_Toc232852964)

[2.2 Roles 4](#_Toc232852965)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232852966)

[2.4 Preliminary Steps 5](#_Toc232852967)

[2.4.1 Check the Master Data Settings 5](#_Toc232852968)

[2.4.2 Check the Master Data Settings (Optional) 8](#_Toc232852969)

[2.4.3 Check/Maintain Consumption Values 10](#_Toc232852970)

[2.4.4 Check/Maintain PIRs (Optional) 12](#_Toc232852971)

[3 Overview Table 14](#_Toc232852972)

[4 Test Procedures 15](#_Toc232852973)

[4.1 Rapid Replenishment Planning for selected Article 15](#_Toc232852974)

[4.1.1 Execute Forecast Run 15](#_Toc232852975)

[4.1.2 Execute Rapid Replenishment Run 17](#_Toc232852976)

[4.1.3 Execute Rapid Replenishment Run (Optional) 18](#_Toc232852977)

[4.1.4 Check Results of Rapid Replenishment run 19](#_Toc232852978)

[4.1.5 Check Follow-On Documents 20](#_Toc232852979)

[4.2 Periodic Background Jobs 21](#_Toc232852980)

[4.2.1 Schedule Job for Forecast Calculation 21](#_Toc232852981)

[4.2.2 Schedule Job for Replenishment Planning 23](#_Toc232852982)

[4.2.3 Schedule Job for Replenishment Planning (Optional) 25](#_Toc232852983)

[5 Appendix 28](#_Toc232852984)

[5.1 Process Integration 28](#_Toc232852985)

[5.1.1 Succeeding Processes 28](#_Toc232852986)

## Purpose

Overview

The goal of the replenishment process for stores is to calculate optimal dates and quantities for procuring reorderable articles to best meet consumer demand. This helps avoid costly out-of-stock or overstock situations. The source of supply can be a distribution center or an external supplier.

In an optional preliminary step to the replenishment run, demand can be determined by executing forecasting algorithms on historical consumption data, considering various factors (such as seasonality). Alternatively, you can create planned independent requirements (PIRs) to determine demand. Replenishment is executed to calculate the optimal quantities and dates for procurement, considering among others, forecast demand or PIRs, the current stock situation, and already planned goods receipts. Additionally, a manually (for example based on shelf size and presentation stock) or automatically determined target stock can be considered.

Replenishment triggers the creation of purchase requisitions for the determined quantities and dates.

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

The test is conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Replenishment Specialist - Store (Retail) | SAP_BR_RPLNMT_SPCLST_ST_RFM | Store Replenishment | SAP_BR_RPLNMT_SPCLST_ST_RFM |  |
| Master Data Specialist - Product Data (Retail) | SAP_BR_MD_SPCLST_ITEM_RFM | Retail Product Master Data | SAP_BR_MD_SPCLST_ITEM_RFM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | R_1034 | Frozen Herb selection |  |
| Material | R_1035 | White bread small, organic |  |
| Material Type | Trading Goods | HAWA Trading Goods |  |
| Material Category | Single Material | Single Material |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 40 | Store Sales |  |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Store | 3340 | Store 3340 AE |  |
| Storage Location | 995A | Storage Loc. DC |  |

### Preliminary Steps

This chapter provides an overview of detailed technical steps and other relevant pre-requisites.

You can check the master data settings within the Manage Product Master Data (F1602) app.

Currently the maintain article app is being used for maintaining the consumption related data.

#### Check the Master Data Settings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step explains the required settings for running a replenishment run in a store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (Retail) role. |  |  |
| 2 | Access the App | Open Maintain Article (MM42) app. |  |  |
| 3 | Enter Parameters | Enter below detailsMaterial: R_1034In Areas of Validity Section,Store: 3340Flag Logistics: Store view in Views sectionChoose Continue | Change Material R_1034 (Logistics: Store) screen is displayed. |  |
| 4 | Check the Details | Check the below details:In the MRP Parameters sectionMRP Type: RF(RF-Replenish with dynamic Target Stock.Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value)In the Replenishment parameters sectionTarget Coverage: 5 DaysIn the Forecast Parameters sectionForecast Model: K( K - Constant with smoothing factor adjustment)Period Ind: WIn the MRP Controller/Replenishment Data sectionPl Deliv Time: 3 DaysSupply Source :4Optionally SupplySource can be changed to “ 1 – Standard” to create Normal Purchase Requisitions for External SupplierIn the General control parameters sectionAvail.check : ST(ST – Consider only stock)Optionally MRP Type : RP (Replenishment) can be used along with manual entry of Target Stock (static value) and Re-order Point. Further Requirement Group can be used in this variation. This prevents from having to maintain all the data for every combination of plant and material. Requirement Group can be assigned in the Site Master at the Merchandise Category level. Replenishment parameters can be maintained in the material master at requirement group level. | The details are displayed. |  |
| 5 | Navigate back to Maintain Article App | Choose Back | Change Material (Initial Screen) screen is displayed. |  |
| 6 | Enter Parameters | On the Change Material (Initial Screen) enter the following dataMaterial: R_1035In Areas of Validity Section ,Store: 3340 | Change Material R_1035 (Logistics: Store) screen is displayed. |  |
| 7 | Check the Details | Check the below details:In the MRP Parameters sectionMRP Type: RF(RF – Replenish with dynamic Target Stock.Dynamic Target Stock gets calculated at runtime during the planning run from forecast sales value )In the Replenishment parameters sectionTarget Coverage: 5 DaysIn the Forecast Parameters sectionForecast Model: K(K - Constant with smoothing factor adjustment)Period Ind: WIn the MRP Controller/Replenishment Data sectionPl Deliv Time: 3 DaysSupply Source : 4Optionally SupplySource can be changed to “1 – Standard” to create Normal Purchase Requisitions for External SupplierIn the General control parameters sectionAvail.check : ST(ST – Consider only stock)Optionally MRP Type : RP (Replenishment) can be used along with manual entry of Target Stock (static value) and Re-order Point. Further Requirement Group can be used in this variation. This prevents from having to maintain all the data for every combination of plant and material. Requirement Group can be assigned in the Site Master at the Merchandise Category level. Replenishment parameters can be maintained in the material master at requirement group level. | The details are displayed. |  |
| 8 | Navigate to Home Screen | Choose Back till reaches home screen | Home screen is displayed. |  |

|  |
| --- |
| Note Alternatively, you can choose Manage Product Master Data (F1602) to check mandatory settings needed for executing the replenishment run in a store. |

#### Check the Master Data Settings (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step explains the required settings for running a replenishment run in a store using Planned Independent Requierments.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (Retail) role. |  |  |
| 2 | Access the App | Open Maintain Article (MM42) app. |  |  |
| 3 | Enter Parameters | Enter below details:Material: R_1034In Areas of Validity Section,Store: 3340Flag Logistics: Store view in Views sectionChoose Continue | Change Material R_1034 (Logistics: Store) screen is displayed. |  |
| 4 | Check the Details | Maintain the Details:In MRP Controller/Replenishment Data section, Choose MRP Controller - 001.Choose MRP/Forecast DataIn the Planning Section maintain the below values:Strategy Group: 40Consumption mode: 4Bwd. consumption per.: 3Fwd. consumption per.: 3Choose Goto Main Data | The details are displayed. |  |
| 5 | Save the Values | Choose Save | Matiral R_1034 changed message is displayed. |  |
| 6 | Navigate back to the Maintain Article app | Choose Back. | Change Material (Initial Screen) screen is displayed. |  |
| 7 | Enter Parameters | Enter below details:Material: R_1035In Areas of Validity Section,Store: 3340Flag Logistics: Store view in Views sectionChoose Continue | Change Material R_1035 (Logistics: Store) screen is displayed. |  |
| 8 | Check the Details | Maintain the Details:In MRP Controller/Replenishment Data section, Choose MRP Controller - 001.Choose MRP/Forecast DataIn the Planning Section maintain the below values:Strategy Group: 40Consumption mode: 4Bwd. consumption per.: 3Fwd. consumption per.: 3Choose Goto Main Data | The details are displayed. |  |
| 9 | Save the Values | Choose Save | Matiral R_1035 changed message is displayed. |  |

|  |
| --- |
| Note Alternatively, you can choose Manage Product Master Data (F1602) to check mandatory settings needed for executing the replenishment run in a store. |

#### Check/Maintain Consumption Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Consumption values are needed for the Forecast Calculation. Consumption values are stored automatically in the system as soon as the product is sold at POS.

|  |
| --- |
| Note Typically maintaining Consumption Data of Inventory for a material starts before you want to work with this material the first time. |

Important note for testers: Here is the possibility to maintain consumption values for testing purposes and manually correction.

This chapter explains the process for checking consumption values for material R_1034 and R_1035.

You may need to increase consumption values if the testing for this article has already been carried out based on the consumption values mentioned in this test script. In this case Rapid Replenishment Planning (RRP) must have already generated Purchase Requisition/Stock Transport Requisition. New Purchase Requisition/ Stock Transport Requisition generation won’t happen unless until there is a change in the consumption/forecast situation.

You may also consider creating your own article having replenishment parameters exactly similar to sample articles (R_1034, R_1035).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (Retail). |  |  |
| 2 | Access the App | Open Maintain Article (MM42) app. |  |  |
| 3 | Enter Parameters | On the Change Material (Initial Screen) enter the following data,Material: R_1034In Areas of Validity Section,Store: 3340Flag Logistic: Store view in Views sectionChoose Continue. | Change Material R_1034 (Logistics: Store) screen is displayed. |  |
| 4 | Choose Consumption | Choose Consumption vals to maintain historical consumption values for material. | Change Material R_1034 ( Consumption: Store, Trading Goods ) screen is displayed. |  |
| 5 | Maintain Consumption Values | Maintain below values for first 12 Periods in Corrected value columnCorrected value: 100Choose Goto Main Data. | Change Material R_1034 (Logistics: Store) screen is displayed. |  |
| 6 | Save Consumption values | Choose Save. | Material R_1034 changed message is displayed. |  |
| 7 | Enter Parameters | Enter below detailsMaterial: R_1035In Areas of Validity Section,Store: 3340 | Change Material R_1035 (Logistics: Store) screen is displayed. |  |
| 8 | Choose Consumption | Choose Consumption values to maintain historical consumption values for material. | Change Material R_1035 ( Consumption: Store, Trading Goods ) screen is displayed. |  |
| 9 | Maintain Consumption Values | Maintain below values for first 12 Periods in Corrected value columnCorrected value: 100Choose Goto Main Data. | Change Material R_1035 (Logistics: Store) screen is displayed. |  |
| 10 | Save Consumption values | Choose Save. | Material R_1035 changed message is displayed. |  |

#### Check/Maintain PIRs (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step explains the required settings for running a replenishment run in a store using Planned Independent Requierments.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail) role. |  |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3340)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3340Period Indicator: Weekly(W)Version Active: Select all optionsSearch: R_1034 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Edit PIRs | Select the material item and choose Edit in the upper-right corner of the screen.On the screen, enter quantities per period, for example:PIR: 200 for all periodsMake sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |
| 8 | Navigate back to the Maintain PIRs | Select back on the Edit PIRs screen | The Maintain PIRs screen displays. |  |
| 9 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3340Period Indicator: Weekly(W)Version Active: Select all optionsSearch: R_1035 |  |  |
| 10 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 11 | Edit PIRs | Select the material item and choose Edit in the upper-right corner of the screen.On the screen, enter quantities per period, for example:PIR: 200 for all periodsMake sure the version is active.Version Active: Yes |  |  |
| 12 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Execute Forecast Run](#unique_12) [page ] 15 | Replenishment Specialist - Store (Retail) | Schedule Material Demand Forecast Runs (F2464) | Consumption values are displayed and Forecast values are calculated. |
| [Execute Rapid Replenishment Run](#unique_13) [page ] 17 | Replenishment Specialist - Store (Retail) | Execute Rapid Replenishment (WRP1R) | Stock Transport Requisition created for the replenishment quantity. |
| [Execute Rapid Replenishment Run (Optional)](#unique_14) [page ] 18 | Replenishment Specialist - Store (Retail) | Execute Rapid Replenishment (WRP1R) | Stock Transport Requisition created for the replenishment quantity. |
| [Check Results of Rapid Replenishment run](#unique_15) [page ] 19 | Replenishment Specialist - Store (Retail) | Display Replenishment Parameter (WR60) | Replenishment parameters and quantity are displayed. |
| [Check Follow-On Documents](#unique_16) [page ] 20 | Replenishment Specialist - Store (Retail) | Monitor Replenishment (WRMO) | Stock Transport Requisition is displayed. |
| [Schedule Job for Forecast Calculation](#unique_17) [page ] 21 | Replenishment Specialist - Store (Retail) | Schedule Material Demand Forecast Runs (F2464) | Job is defined and forecast results are displayed. |
| [Schedule Job for Replenishment Planning](#unique_18) [page ] 23 | Replenishment Specialist - Store (Retail) | Schedule Rapid Replenishment Run (F5478) | Job is defined and planning results are displayed. |
| [Schedule Job for Replenishment Planning (Optional)](#unique_19) [page ] 25 | Replenishment Specialist - Store (Retail) | Schedule Rapid Replenishment Run (F5478) | Job is defined and planning results are displayed. |

## Test Procedures

This chapter describes the procedures for each process step that belongs to this scope item.

This Test Procedures includes 2 major variations. First variation is RRP with dynamic target stock calculation executed manually and the second variation is Periodic Background Jobs of RRP with dynamic target stock calculation.

### Rapid Replenishment Planning for selected Article

#### Execute Forecast Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process Forecast Values of the article are calculated. The forecast values can be used later in replenishment to calculate a dynamic target stock (MRP type RF).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail). |  |  |
| 2 | Access the App | Open Schedule Material Demand Forecast Runs (F2464) app. |  |  |
| 3 | Create new job | Choose Create to create a new application job. | New Job: Schedule Material Demand Forecasting screen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Information and Scheduling Options sections (Step 1)Job Template:Schedule Material Demand ForecastingJob Name: Schedule Material Demand Forecasting XXChoose Step 2Choose Define Recurrence Pattern to schedule periodic jobFor testing purpose - Flag Start Immediately | Template Information and Scheduling Options of schedule material demand forecasting are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section, make the following entries:Plant: 3340Branches or Distrib. Centers : AMaterial: R_1034Period Indicator: WForecast execution: F | The parameters of Schedule Material Demand Forecasting are defined. |  |
| 6 | Check | Choose Check | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule Job | Choose Schedule | Job Replenishment Planning Job Template XXhas been scheduled message is displayed.Application Jobs screen is displayed again, and the new job displays in the Jobs table. |  |
| 8 | Navigate to Job Results | Check the newly created job row and select the icon Navigate to the job results in Results column. | Document (ID XXXXXXX) screen is displayed. |  |
| 9 | Check Job Results | Check details of Basic data , Control data , No. of values , Historical data and Forecast results section.Check the forecast values for the next twelve periods display in Forecast results section. | Forecast Values for the next twelve periods display in Forecast results section. |  |

#### Execute Rapid Replenishment Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process purchase requisition is created as follow-on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail). |  |  |
| 2 | Access the App | Open tile Execute Rapid Replenishment (WRP1R) app |  |  |
| 3 | Enter Parameters | Enter below detailsIn the Recipient section,Recipient: 3340Materials: R_1034Choose Execute. | Replenishment: Planning screen is displayed. |  |
| 4 | Generate Follow on documents | Choose Generate Follow-on DocumentsSelect Replen. monitor and choose continue on dialog box Run ReplenishmentExpand the subtree with the created replenishment run ID. | General Hierarchy Display screen is displayed.Follow on document stock transport requisition is created.replenishment run id is created.Make a note of stock transport requisition and replenishment run ID. |  |
| 5 | Refer [Succeeding Processes](#unique_21) [page ] 28to display and convert Purchase Requisitions to Purchase Orders. |  |  |  |

#### Execute Rapid Replenishment Run (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process purchase requisition is created as follow-on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail). |  |  |
| 2 | Access the App | Open tile Execute Rapid Replenishment (WRP1R) app |  |  |
| 3 | Enter Parameters | Enter below detailsIn the Recipient section,Recipient: 3340Materials: R_1034Flag: Use PIRs instead of ForecastChoose Execute. | Replenishment: Planning screen is displayed. |  |
| 4 | Generate Follow on documents | Choose Generate Follow-on DocumentsSelect Replen. monitor and choose continue on dialog box Run ReplenishmentExpand the subtree with the created replenishment run ID. | General Hierarchy Display screen is displayed.Follow on document stock transport requisition is created.replenishment run id is created.Make a note of stock transport requisition and replenishment run ID. |  |
| 5 | Refer [Succeeding Processes](#unique_21) [page ] 28to display and convert Purchase Requisitions to Purchase Orders. |  |  |  |

#### Check Results of Rapid Replenishment run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, Replenishment Quantity and status of the Replenishment run are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail). |  |  |
| 2 | Access the App | Open tile Display Replenishment Parameter (WR60) app |  |  |
| 3 | Enter Parameters | Enter below detailsIn the Customers section,Recipient: 3340In the Materials sectionMaterial: R_1034Choose Execute. |  |  |
| 4 | Check Results | Check the details. | Stock, Open PO qty, Targ. stock, Reorder pt, Sfty S tk, TRC, Min. Target Stk, Max.Target Stk, Replen. ID, Replen. Req., St.. is displayed.As the MRP Type maintained is RF below fields will be displayed with values .Stock, Replen. ID, Replen. Req.,St. |  |

#### Check Follow-On Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step an overview of the replenishment activities and messages is displayed. The system stores the replenishment run under an internal number (replenishment run ID). You can use this number to identify the replenishment run in replenishment monitor and is subsequently analysed. The error log of the replenishment run is analysed to correct data. Any articles which could not be processed have to be processed manually and the reason for error must be corrected. Additionally, the numbers of created documents (PRs) can be found here in case of any required verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail). |  |  |
| 2 | Access the App | Open tile Monitor Replenishment (WRMO) app | . |  |
| 3 | Enter Parameters | Enter below detailsIn the Selection Data section,Replenishment run ID: (XXXX)Choose Execute. | General Hierarchy Display screen is displayed. |  |
| 4 | Check Results | Expand the subtree | Stock transport requisition is displayed.Expand the subtree and check for error message if the replenishment run ID displays under node Incorrect.As the Supply Source maintained is 4 the document generated is Stock Transport Requisition |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail). |  |  |
| 2 | Access the App | Open Schedule Material Demand Forecast Runs (F2464) app. |  |  |
| 3 | Create new job | Choose Create to create a new application job. | New Job: Schedule Material Demand Forecasting screen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Information and Scheduling Options section (Step 1)Job Template:Schedule Material Demand ForecastingJob Name: Schedule Material Demand Forecasting XXChoose Step 2Choose Define Recurrence Pattern to schedule periodic jobFor testing purpose - Flag Start Immediately [Optional] | Template Information and Scheduling Options of schedule material demand forecasting are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section, make the following entries:Plant: 3340Branches or Distrib. Centers : AMaterial: R_1035 [Optional]Period Indicator: WForecast execution: F | The parameters of Schedule Material Demand Forecasting are defined. |  |
| 6 | Check | Choose Check | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule Job | Choose Schedule | Job Replenishment Planning Job Template XXhas been scheduled message is displayed.Application Jobs screen is displayed again, and the new job displays in the Jobs table. |  |
| 8 | Navigate to Job Results | Check the newly created job row and select the icon Navigate to the job results in Results column. | Document (ID XXXXXXX) screen is displayed. |  |
| 9 | Check Job Results | Check details of Basic data , Control data , No. of values , Historical data and Forecast results section.Check the forecast values for the next twelve periods display in Forecast results section. | Forecast Values for the next twelve periods display in Forecast results section. |  |

#### Schedule Job for Replenishment Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process Purchase Requisition is created as follow-on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail). |  |  |
| 2 | Access the App | Open Schedule Rapid Replenishment Run (F5478) app | Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create new job | Choose Create to define a new job. | New Job: Replenishment Planning Job Template screen is displayed. Job Template default as Replenishment Planning Job Template. |  |
| 4 | Enter job details | Enter the application job details in the Template Selection and Scheduling Options sections.Job Template: Rapid Replenishment Planning (RRP)Job Name: Rapid Replenishment Planning (RRP) XXChoose Step 2Flag Start Immediately [optional]Choose Define Recurrence Pattern if required to change the Recurrence Pattern | Template Selection Information and Scheduling options of Replenishment Planning Job Template are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section make the following entries:Recipient: 3340Material: R_1035MRP Type: RFFlag Include Forecast Issues | The parameters of Replenishment Planning Job Template are defined. |  |
| 6 | Check | Choose Check | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule Job | Choose Schedule | Job Replenishment Planning Job Template XXhas been scheduled message is displayed.Application JobsInformation : screen is displayed again, and the new job displays in the Jobs table. |  |
| 8 | Check Job Log | On the Application Jobs screen, after job item status turned to Finish, choose Status symbol in the Log column. | Job Log Screen is displayed. |  |
| 9 | Check Details | Check the Message Type in Log Details section | Information : Replenishment Run XXXX startedInformation: Completed for 1 articles with 1 follow-on documents, 0 error messagesMake a note on Replenishment Run ID.The jobs that couldn’t generate follow-on document successfully will generate following messages in job log screen.Information: Replenishment Run XXXX startedInformation : Completed for 1 articles with 0 follow-on documents, 1 error messagesMake use of Monitor Replenishment (WRMO) app to check success/Error messages. |  |
| 10 | Monitor Replenishment | See chapter [Check Follow-On Documents](#unique_16) [page ] 20 with Replenishment run ID XXXX for Recipient 3340 | Stock Transport Requisition is displayed.Expand the subtree and check the error message if the Replenishment Run ID displays under subnode Incorrect. |  |
| 11 | Replenishment Parameter overview | See chapter [Check Results of Rapid Replenishment run](#unique_15) [page ] 19 with Material R_1035 for Recipient 3340 | Stock, Open PO qty, Targ. stock, Reorder pt, Sfty stk, TRC, Min. Target Stk, Max.Target Stk ,Replen. ID, Replen. requirment from last replen. run, Replenishment status is displayed.As the MRP Type maintained is RF below fields will be displayed with values.Stock, Replen. ID, Replen. requirment from last replen. run, Replenishment status. |  |

#### Schedule Job for Replenishment Planning (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process Purchase Requisition is created as follow-on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori Launchpad as a Replenishment Specialist - Store (Retail). |  |  |
| 2 | Access the App | Open Schedule Rapid Replenishment Run (F5478) app | Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create new job | Choose Create to define a new job. | New Job: Replenishment Planning Job Template screen is displayed. Job Template default as Replenishment Planning Job Template. |  |
| 4 | Enter job details | Enter the application job details in the Template Selection and Scheduling Options sections.Job Template: Replenishment Planning Job TemplateJob Name: Replenishment Planning Job Template XXChoose Step 2Flag Start Immediately [optional]Choose Define Recurrence Pattern if required to change the Recurrence Pattern | Template Selection Information and Scheduling options of Replenishment Planning Job Template are defined. |  |
| 5 | Enter Parameters | Choose Step 3In the Parameter section make the following entries:Recipient: 3340Material: R_1035MRP Type: RFFlag Use PIRs instead of Forecast | The parameters of Replenishment Planning Job Template are defined. |  |
| 6 | Check | Choose Check | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule Job | Choose Schedule | Job Replenishment Planning Job Template XXhas been scheduled message is displayed.Application Jobs screen is displayed again, and the new job displays in the Jobs table. |  |
| 8 | Check Job Log | On the Application Jobs screen, after job item status turned to Finish, choose Status symbol in the Log column. | Job Log Screen is displayed. |  |
| 9 | Check Details | Check the Message Type in Log Details section | Information : Replenishment Run XXXX startedInformation: Completed for 1 articles with 1 follow-on documents, 0 error messagesMake a note on Replenishment Run ID.The jobs that couldn’t generate follow-on document successfully will generate following messages in job log screen.Information: Replenishment Run XXXX startedInformation : Completed for 1 articles with 0 follow-on documents, 1 error messagesMake use of Monitor Replenishment (WRMO) app to check success/Error messages. |  |
| 10 | Monitor Replenishment | See chapter [Check Follow-On Documents](#unique_16) [page ] 20 with Replenishment run ID XXXX for Recipient 3340 | Stock Transport Requisition is displayed.Expand the subtree and check the error message if the Replenishment Run ID displays under subnode Incorrect. |  |
| 11 | Replenishment Parameter overview | See chapter [Check Results of Rapid Replenishment run](#unique_15) [page ] 19 with Material R_1035 for Recipient 3340 | Stock, Open PO qty, Targ. stock, Reorder pt, Sfty stk, TRC, Min. Target Stk, Max.Target Stk ,Replen. ID, Replen. requirment from last replen. run, Replenishment status is displayed.As the MRP Type maintained is RF below fields will be displayed with values.Stock, Replen. ID, Replen. requirment from last replen. run, Replenishment status. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| - | Stock Transport Requisition generated for Distribution Center is converted into a Purchase order in the “Store Ordering from Distribution Center”(Scope Item 5FX) process. |
| - | Purchase Requisition generated for external supplier is converted into a Purchase order in the “Procurement for Retail”(Scope Item 5FM) process. |

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
- see-also :: [[15-retail-operations/replenishment-planning-for-distribution-centers-3i8-ae-test-script-947]]
- see-also :: [[15-retail-operations/test-script-store-ordering-from-distribution-center-5fx-ae-1092]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 43,356 chars in the whole document
