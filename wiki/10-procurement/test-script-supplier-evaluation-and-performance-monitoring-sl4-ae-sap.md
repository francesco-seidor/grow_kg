---
id: 10-procurement/test-script-supplier-evaluation-and-performance-monitoring-sl4-ae-sap
title: "Test Script: Supplier Evaluation and Performance Monitoring (SL4_AE) - SAP S/4HANA Cloud Public Edition (SL4_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (SL4_AE, 2608): set up and test supplier evaluation by operational KPIs, questionnaires and user-defined criteria."
cluster: 10-procurement
tags: [kb/procurement, topic/supplier-evaluation]
aliases: [SL4_S4CLD2608_BPD_EN_AE]
keywords: [Supplier Evaluation and Vendor Performance, supplier evaluation, test scripts, procurement analytics configuration, operational supplier evaluation, weighting and scoring, questionnaire evaluation, user-defined criteria, parts per million, supplier score history]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/SL4_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1312
topic: 10-procurement/supplier-evaluation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Supplier Evaluation and Performance Monitoring (SL4_AE) - SAP S/4HANA Cloud Public Edition (SL4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/SL4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Supplier Evaluation and Vendor Performance** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 01-07-26 |
| --- | --- |
|  | Supplier Evaluation and Performance Monitoring (SL4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc234569754)

[2 Prerequisites 4](#_Toc234569755)

[2.1 System Access 4](#_Toc234569756)

[2.2 Roles 4](#_Toc234569757)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc234569758)

[2.4 Additional Manual Configuration 5](#_Toc234569759)

[2.5 Business Conditions 5](#_Toc234569760)

[2.6 Preliminary Step 6](#_Toc234569761)

[2.6.1 Create the Question Library 6](#_Toc234569762)

[2.6.2 Schedule Job for Persistency of Supplier Evaluation Scores 7](#_Toc234569763)

[2.6.3 Setup Analytical Reporting Currencies (Optional) 8](#_Toc234569764)

[2.6.4 Schedule Job for Migration of Purchasing Data (Optional) 10](#_Toc234569765)

[2.6.5 Enable Performance Optimization for Purchasing Analytics Apps (Optional) 11](#_Toc234569766)

[2.6.6 Activate User Defined Criteria for Supplier Evaluation 13](#_Toc234569767)

[2.6.7 Maintain Evaluation Criteria for Parts Per Million (Optional) 15](#_Toc234569768)

[2.6.8 Schedule Persistency of Parts Per Million Data 16](#_Toc234569769)

[2.6.9 Set the Configuration for Supplier Evaluation Criteria (Optional) 17](#_Toc234569770)

[2.6.10 Define Document Category Scope for Supplier Evaluation (Optional) 19](#_Toc234569771)

[2.6.11 Enable Factory Calendar Setting (Optional) 21](#_Toc234569772)

[3 Overview Table 24](#_Toc234569773)

[4 Test Procedures 26](#_Toc234569774)

[4.1 Operational Supplier Evaluation 26](#_Toc234569775)

[4.1.1 Create Supplier Evaluation Weighting and Scoring 26](#_Toc234569776)

[4.1.2 Display Supplier Evaluation by Quantity 29](#_Toc234569777)

[4.1.3 Display Supplier Evaluation by Price 30](#_Toc234569778)

[4.1.4 Display Supplier Evaluation by Time 30](#_Toc234569779)

[4.1.5 Display Supplier Evaluation by Quality Notification 31](#_Toc234569780)

[4.1.6 Display Supplier Evaluation by Quality Inspection Lot 32](#_Toc234569781)

[4.1.7 Display Supplier Evaluation by Operational Supplier Evaluation 32](#_Toc234569782)

[4.1.8 Parts Per Million 33](#_Toc234569783)

[4.1.9 Adjust Supplier Evaluation Scores Manually 34](#_Toc234569784)

[4.2 Supplier Evaluation by Questionnaire 34](#_Toc234569785)

[4.2.1 Create Sections and Questions in Question Library 34](#_Toc234569786)

[4.2.2 Create Evaluation Questionnaire 35](#_Toc234569787)

[4.2.3 Create Group-Based Evaluation Template 36](#_Toc234569788)

[4.2.4 Start Group-Based Evaluation 37](#_Toc234569789)

[4.2.5 Maintain Evaluation Response as Appraiser 38](#_Toc234569790)

[4.2.6 Display Scorecards 39](#_Toc234569791)

[4.2.7 Monitor Response 40](#_Toc234569792)

[4.2.8 Display Supplier Evaluation by Questionnaire 41](#_Toc234569793)

[4.3 Supplier Evaluation by User-Defined Criteria 42](#_Toc234569794)

[4.3.1 Manage User-Defined Criteria for Supplier Evaluation 42](#_Toc234569795)

[4.3.2 Display Supplier Evaluation Score by User-Defined Criteria 44](#_Toc234569796)

[4.3.3 Display Overall Supplier Evaluation Score 45](#_Toc234569797)

[4.4 Manage Supplier Evaluation Score 46](#_Toc234569798)

[4.4.1 Display Supplier Evaluation Score History 46](#_Toc234569799)

[4.4.2 Output Supplier Evaluation Score 47](#_Toc234569800)

[5 Appendix 50](#_Toc234569801)

[5.1 Process Integration 50](#_Toc234569802)

[5.1.1 No Succeeding Processes 50](#_Toc234569803)

## Purpose

Overview

You can evaluate your company’s suppliers to obtain a basis for your business relationship with them and to optimize your supply base. Based on the feedback you gather through questionnaires, you obtain a scorecard for each supplier evaluated. The scorecard helps you to assess a supplier’s strengths and shortcomings and to initiate measures for improvement. Evaluation scorecards also enable you to easily compare suppliers within a peer group.

A combined real-time view across operational and questionnaire-based scores provides a holistic view of your supplier’s performance. This scope item provides two different use cases for the category manager:

Evaluate supplier performance and analyze KPIs based on the evaluation.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

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
| Employee - Procurement | SAP_BR_EMPLOYEE_PROCUREMENT | Self Services - Procurement | SAP_MM_SPT_EMPLOYEE_SERVICES_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Supplier | 44300001 |  |  |

For more information on creating needed master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| Master Data Script ID | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/0c6a01312a7f3f336f509fc2c25a4635)

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1FM - Quality Management in Procurement (Optional) | Start with the Quality Management in Procurement process and then you can display supplier evaluation by quality inspection lot. |
| 2F9 - Quality Management for Complaints Against Suppliers (Optional) | Start with the Quality Management for Complaints Against Suppliers process , create the quality notification, then you can display supplier evaluation by quality notification. |
| 19E - Supplier Classification and Segmentation (Optional) | Start with the Supplier Classification and Segmentation, create the Purchasing Categories, then add new weighting and scoring for the purchasing categories in Create Supplier Evaluation Weighting and Scoring. |

### Preliminary Step

#### Create the Question Library

Purpose

In this procedure, you create the question library which is required for creating questions and sections.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Question Library for Supplier Evaluation (/SRMSMC/CREA_QLB_EVL) | The Create Question Library for Supplier Evaluation screen displays. |  |
| 3 | Create the data | Enter below data:Original language: Ex., ENChoose Run.Note The library can be created only once! Changing the language later is not possible! | The question library has been created. |  |

#### Schedule Job for Persistency of Supplier Evaluation Scores

Purpose

In this procedure, you schedule a job to calculate the supplier evalution score for a specific period. You can check supplier evaluation score history later in section Supplier Evaluation Score History. Or you schedule a job to delete the obsolete jobs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Schedule Persistency of Supplier Evaluation Scores (F3814) | The Application Jobs screen displays. |  |
| 3 | Create the job | Choose Create.Enter below data in Template Selection tab,Job Template: Supplier Evaluation Score HistoryJob Name: for example, Supplier Evaluation Score History from Nov till now. Choose Step 2.In Scheduling Options tab,Start Immediately: checkedFor testing, please choose start immediately. You can also choose recurrence pattern, and schedule the job by minutes, hourly, week, month etc.To make sure Start Immediately can be selected, Single Run should be set for Recurrence Pattern firstly.Choose Step 3.In Parameters tab, Scheduling section,Schedule Job(Persist History): checkedSchedule Job(Delete History): uncheckedSchedule Job to Persist Supplier Evaluation Scores Section,Display Currency: for example, AEDStart Date: for example, 11/01/2018End Date: for example, TodayChoose Schedule.Wait until the job status is Finished. | The job has been scheduled. |  |
| 4 | Delete the job | Choose Create.Enter below data in TEMPLATE tab,Job Template: Supplier Evaluation Score HistoryJob Name: for example, Delete Obsolete Supplier Evaluation Score History jobs.In SCHEDULE OPTIONS tab,Start Immediately: checkedFor testing, please choose start immediately. You can also choose recurrence pattern, and schedule the job by minutes, hourly, week, month etc.In Parameters tab,Scheduling section,Schedule Job(Persist History): uncheckedSchedule Job(Delete History): checkedSchedule Job to Delete Supplier Evaluation Score History section,Supplier: for example: 33300001Job Creation Date(From): for example, 02/01/2019(To): for example, TodayJob ID: enter a specific job ID if you want to delete one specific job onlyChoose Schedule.Wait until the job status is Finished. |  |  |

#### Setup Analytical Reporting Currencies (Optional)

Purpose

In this procedure, you can setup two analytical reporting currencies that will be used in various analytical KPIs and queries in Procurement in SAP S/4HANA Cloud Public Edition. If user selects one of the two configured reporting currencies as display currency in an analytical KPI, the system doesn't convert the reporting currency to display currency at runtime. This enhances the performance of the KPI.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Setup the analytical reporting currencies | Choose Configure Your Solution.Choose Sourcing and Procurement in the Application Area field, then navigate to the Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step1 Setup Analytical Reporting Currencies.Choose New Entries.Enter below data:Reporting Curr. Id: for example, Reporting Currency 1Currency: for example, AEDChoose Save.Two reporting currencies can be setup. | Reporting currencies are added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Setup Analytical Reporting Currencies | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Setup Analytical Reporting Currencies.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Setup the analytical reporting currencies | Choose New Entries.Enter below data:Reporting Curr. Id: for example, Reporting Currency 1Currency: for example, AEDChoose Save.Two reporting currencies can be setup. |  |  |

#### Schedule Job for Migration of Purchasing Data (Optional)

Purpose

In this procedure, you migrate purchasing data for analytics. You must enter migration options and some additional parameters to migrate the data. Migration of data leads to performance optimization in purchasing analytics apps.

|  |
| --- |
| Note Reporting currencies in step [Setup Analytical Reporting Currencies (Optional)](#unique_10) [page ] 8 must be set up to schedule migration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Schedule Migration of Purchasing Data for Analytics (F3815) | The Application Jobs screen displays. |  |
| 3 | Create the job | Choose Create.Enter below data in Template Selection tab,Job Template: Schedule Migration of Purchasing Data for AnalyticsJob Name: for example, Schedule Migration of Purchasing Data for Analytics - Initial Run. Choose Step 2.In Scheduling Options tab,Start Immediately: checkedFor testing, please choose Start Immediately. Choose Step 3.In Parameters tab, Performance Optimization for Existing Customers section,Initial Load: checkedReprocess Records: uncheckedDelta Load: uncheckedTo include scheduling agreement, initial run has to be scheduled.If Delta Load is selected, then the following selection condition can be entered:Purchase Order Date (From): for example, 05/01/2019(To): for example, TodaySupplier Names: for example, 33300001Purchase Orders:In Performance Optimization for New Implementation section,Activate Perf. Optimization: UncheckedIn Parallel Processing Parameters section,Number of Tasks: for example, 1Package Size: for example, 1000In Log Level Settings section,Log Level: for example, BasicChoose Schedule.Wait until the job status is Finished. | Job is scheduled and finished. |  |

#### Enable Performance Optimization for Purchasing Analytics Apps (Optional)

Purpose

In this procedure, you can enable performance optimization for purchasing analytics apps. As a new customer, the performance optimization for purchasing analytics apps has to be enabled, otherwise the performance for analytics apps won’t be optimized. This switch will be automatically enabled if you have previously executed the job Schedule Migration of Purchasing Data for Analytics using the option Initial Load.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Setup the analytical reporting currencies | Choose Configure Your Solution.Choose Sourcing and Procurement in the Application Area field, then navigate to the Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step3 Enable Performance Optimization for Purchasing Analytics Apps.Choose the entry Enable Performance Optimization or choose New Entries if there is no entry there.Enter below data:Performance Optimization Switch: Enable Performance OptimizationEnable: CheckedChoose Save.Note Once the Performance Optimization Switch is enabled, it cannot be disabled. | The Performance Optimization Switch is enabled. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Enable Performance Optimization for Purchasing Analytics Apps | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Enable Performance Optimization for Purchasing Analytics Apps.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Setup the analytical reporting currencies | Choose the entry Enable Performance Optimization or choose New Entries if there is no entry there.Enter below data:Performance Optimization Switch: Enable Performance OptimizationEnable: CheckedChoose Save.Note Once the Performance Optimization Switch is enabled, it cannot be disabled. |  |  |

#### Activate User Defined Criteria for Supplier Evaluation

Purpose

In this procedure, you can activate user defined criteria for supplier evaluation. You can also change the description of the criteria. User defined criteria are parameters that you as a user can define based on your specific requirement. This gives you flexibility to have additional parameters which are specific to your business. These criteria will enhance your capabilities to rate your suppliers for a specific business need.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Setup the analytical reporting currencies | Choose Configure Your Solution.Choose Sourcing and Procurement in the Application Area field, then navigate to the Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step 2 Activate User Defined Criteria for Supplier Evaluation.Enter below data:Enabled: check for User-Defined Criteria 1 and User-Defined Criteria 2Criterion Description: for example, Return Delivery of Goods for User-Defined Criteria 1 and Reasonable Discounts for User-Defined Criteria 2Enabled: check for Parts Per MillionNote The description for Parts Per Million can not be changed.Choose Save.Only 6 user-defined criteria are allowed, enable them by needs. | User-defined criteria are enabled and decstiptions are changed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate User Defined Criteria for Supplier Evaluation | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Activate User Defined Criteria for Supplier Evaluation.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Setup the analytical reporting currencies | Enter below data:Enabled: check for User-Defined Criteria 1 and User-Defined Criteria 2Criterion Description: for example, Return Delivery of Goods for User-Defined Criteria 1 and Reasonable Discounts for User-Defined Criteria 2Enabled: check for Parts Per MillionNote The description for Parts Per Million can not be changed.Choose Save.Only 6 user-defined criteria are allowed, enable them by needs. |  |  |

#### Maintain Evaluation Criteria for Parts Per Million (Optional)

Purpose

In this procedure, you can activate the major PPM evaluation criteria. Based on return delivery is activated by default, you can change it if it’s needed.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Setup the analytical reporting currencies | Choose Configure Your Solution.Choose Sourcing and Procurement in the Application Area field, then navigate to the Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step4 Maintain Evaluation Criteria for Parts Per Million.Enter below data:Based on Return Delivery: for example, uncheckedBased on Quality Notification: for example, checkedChoose Save. | The Performance Optimization Switch is enabled. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Evaluation Criteria for Parts Per Million | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Maintain Evaluation Criteria for Parts Per Million.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Setup the analytical reporting currencies | Enter below data:Based on Return Delivery: for example, uncheckedBased on Quality Notification: for example, checkedChoose Save. |  |  |

#### Schedule Persistency of Parts Per Million Data

Purpose

In this procedure, you schedule the job to persist Parts Per Million Data to User-Defined Criteria Parts Per Million.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Schedule Persistency of Parts Per Million Data (F5301) | The Application Jobs screen displays. |  |
| 3 | Create the job | Choose Create.Enter below data in Template Selection,Job Template: Persist Parts Per Million Data to User-Defined CriteriaJob Name: for example, Job for PPMChoose Step 2.In Scheduling Options,Start Immediately: checkedFor testing, please choose Start Immediately.Choose Define Recurrence Pattern.In Scheduling Information,Recurrence Pattern: Single RunChoose OK.Choose Step 3.In Parameters,Supplier: for example,33300001Evaluation Start Date: for example, 01/01/2020Evaluation End Date: todayChoose Schedule.Wait until the job status is Finished. | Job is scheduled and finished. |  |

#### Set the Configuration for Supplier Evaluation Criteria (Optional)

Purpose

In this procedure, you can set the configuration for supplier evaluation criteria. Delivery Completed are parameters that you as a user can set based on your specific requirement. If you choose Set, you can display the purchase order documents which are already delivery completed . If you choose Not Set, you can display the purchase order documents which are not delivery completed. If you choose Both, you can display all purchase order documents.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Setup the analytical reporting currencies | Choose Configure Your Solution.Choose Sourcing and Procurement in the Application Area field, then navigate to the Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step 5 Supplier Evaluation Criteria Configuration.Enter below data:Supplier Evaluation Criteria: Quantity VarianceDelivery Completed: for example, Set for purchase orders that are Delivery Completed could be displayed and Not Set for purchase orders that are not Delivery Completed could be displayed and Both for all purchase orders could be displayed regardless of Delivery Completed Indicator.Note The status of Delivery Completed Indicator is maintained in the Purchase order.Choose Save.Only 3 delivery completed are allowed, default is Both, set them by needs. | Configuration for Supplier evaluation criteria is changed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Supplier Evaluation Criteria Configuration | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Supplier Evaluation Criteria Configuration.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Setup the analytical reporting currencies | Enter below data:Supplier Evaluation Criteria: Quantity VarianceDelivery Completed: for example, Set for purchase orders that are Delivery Completed could be displayed and Not Set for purchase orders that are not Delivery Completed could be displayed and Both for all purchase orders could be displayed regardless of Delivery Completed Indicator.Note The status of Delivery Completed Indicator is maintained in the Purchase order.Choose Save.Only 3 delivery completed are allowed, default is Both, set them by needs. |  |  |

#### Define Document Category Scope for Supplier Evaluation (Optional)

Purpose

In this procedure, you can define document category scope for supplier evaluation. Purchase orders are activated by default, you may change it.

This setting will impact the data in below apps:

- Supplier Evaluation By Quantity - Based on Ordered and Received Quantity (F1661A)
- Supplier Evaluation By Price - Based on PO and Invoice Price (F1663A)
- Supplier Evaluation By Time - Based on Delivery and Goods Receipt Date (F1664A)
- Supplier Evaluation By Quality - Based on Quality Notification (F3295A)
- Parts per Million - By Returns and Quality Notifications (F4885)
- Supplier Evaluation by Quality - Inspection lot (F2309A)
- Operational Supplier Evaluation - Based on Score and Variance (F1662A)
- Adjust Operational Supplier Evaluation Score (F2312)

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Define Document Category Scope for Supplier Evaluation | Choose Configure Your Solution.Choose Sourcing and Procurement in the Application Area field, then navigate to the Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step 6 Define Document Category Scope for Supplier Evaluation.Enter below data:SE DocCnfg: 1 Purchase OrdersActivate: uncheckSE DocCnfg: 2 Scheduling AgreementsActivate: uncheckSE DocCnfg: 3 Purchase Orders and Scheduling AgreementsActivate: checkNote To avoid perfomance issue, before your activate purchase orders and scheduling agreements, you need to complete below steps,Select the Enable option, in the configuration step Enable Performance Optimization for Purchasing Analytics Apps, if not previously done. This configuration step enables performance optimization for purchasing analytics apps. This option cannot be disa-bled once you enable it.Migrate purchasing data (purchase orders and scheduling agreements) using the Schedule Migration of Purchasing Data for Analytics app. Ensure to select the Initial Load option, as this option migrates all the purchasing records.Choose Save. | Configuration for Define Document Category Scope for Supplier evaluation is changed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open the Activity | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Define Document Category Scope for Supplier Evaluation.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Document Category Scope for Supplier Evaluation | Enter below data:SE DocCnfg: 1 Purchase OrdersActivate: uncheckSE DocCnfg: 2 Scheduling AgreementsActivate: uncheckSE DocCnfg: 3 Purchase Orders and Scheduling AgreementsActivate: checkNote To avoid perfomance issue, before your activate purchase orders and scheduling agreements, you need to complete below steps,Select the Enable option, in the configuration step Enable Performance Optimization for Purchasing Analytics apps, if not previously done. This configuration step enables performance optimization for purchasing analytics apps. This option cannot be disa-bled once you enable it.Migrate purchasing data (purchase orders and scheduling agreements) using the Schedule Migration of Purchasing Data for Analytics app. Ensure to select the Initial Load option, as this option migrates all the purchasing records.Choose Save. | Configuration for define document category scope for supplier evaluation is changed. |  |

#### Enable Factory Calendar Setting (Optional)

Purpose

In this procedure, you can Enable Factory Calendar Setting for supplier evaluation. You can only enable it when has been enabled in section 2.6.5.

This setting will impact the data in below app,

- Supplier Evaluation By Time - Based on Delivery and Goods Receipt Date (F1664A)

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Enable Factory Calendar Setting | Choose Configure Your Solution.Choose Sourcing and Procurement in the Application Area field, then navigate to the Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step 7 Enable Factory Calendar Setting.Enter below data:Enable: CheckedNote To avoid data inconsistent issue, please don’t disable it once it’s enabled.Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open the activity | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Enable Factory Calendar Setting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Enable Factory Calendar Setting | Enter below data:Enable: CheckedNote To avoid data inconsistent issue, please don’t disable it once it’s enabled.Choose Save. | Configuration for Enable Factory Calendar Setting is changed. |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/ App Name | Expected Results |
| --- | --- | --- | --- |
| [Operational Supplier Evaluation](#unique_20) [page ] 26 |  |  |  |
| [Create Supplier Evaluation Weighting and Scoring](#unique_21) [page ] 26 | Purchaser | Supplier Evaluation Weighting and Scoring (F2551) | The Supplier Evaluation Weighting and Scoring is created. |
| [Display Supplier Evaluation by Quantity](#unique_22) [page ] 29 | Purchaser | Supplier Evaluation By Quantity - Based on Ordered and Received Quantity (F1661A) | The Supplier Evaluation scores are displayed by Quantity. |
| [Display Supplier Evaluation by Price](#unique_23) [page ] 30 | Purchaser | Supplier Evaluation By Price - Based on PO and Invoice Price (F1663A) | The Supplier Evaluation scores are displayed by Price. |
| [Display Supplier Evaluation by Time](#unique_24) [page ] 30 | Purchaser | Supplier Evaluation By Time - Based on Delivery and Goods Receipt Date (F1664A) | The Supplier Evaluation scores are displayed by Time. |
| [Display Supplier Evaluation by Quality Notification](#unique_25) [page ] 31 | Purchaser | Supplier Evaluation By Quality - Based on Quality Notification (F3295A) | The Supplier Evaluation scores are displayed by Quality Notification. |
| [Display Supplier Evaluation by Quality Inspection Lot](#unique_26) [page ] 32 | Purchaser | Supplier Evaluation by Quality - Inspection lot (F2309A) | The Supplier Evaluation scores are displayed by Quality Inspection Lot. |
| [Display Supplier Evaluation by Operational Supplier Evaluation](#unique_27) [page ] 32 | Purchaser | Operational Supplier Evaluation - Based on Score and Variance (F1662A) | The operational supplier evaluation scores are displayed. |
| [Adjust Supplier Evaluation Scores Manually](#unique_28) [page ] 34 | Purchaser | Adjust Operational Supplier Evaluation Score (F2312) | The evaluation scores are adjusted manually. |
| [Supplier Evaluation by Questionnaire](#unique_29) [page ] 34 |  |  |  |
| [Create Sections and Questions in Question Library](#unique_30) [page ] 34 | Purchaser | Manage Questions (/SRMSMC/WDA_QLB_OVP_MAIN) | Sections and questions in question library is created. |
| [Create Evaluation Questionnaire](#unique_31) [page ] 35 | Purchaser | Manage Evaluation Questionnaires - Evaluation (F2194) | A new questionnaire is created. |
| [Create Group-Based Evaluation Template](#unique_32) [page ] 36 | Purchaser | Manage Evaluation Templates - Evaluation (F2193) | The group-based evaluation template is created. |
| [Start Group-Based Evaluation](#unique_33) [page ] 37 | Purchaser | Manage Evaluation Templates - Evaluation (F2193) | The group-based evaluation is started. |
| [Maintain Evaluation Response as Appraiser](#unique_34) [page ] 38 | Employee - Procurement | Evaluate Suppliers (F1650) | The Evaluation response is created. |
| [Display Scorecards](#unique_35) [page ] 39 | Purchaser | Display Scorecards - Evaluation Questionnaires (F2191) | The group-based evaluation is completed. |
| [Monitor Response](#unique_36) [page ] 40 | Purchaser | Monitor Responses - Evaluation (F1649) | 'The evaluation response is displayed. |
| [Display Supplier Evaluation by Questionnaire](#unique_37) [page ] 41 | Purchaser | Supplier Evaluation By Questionnaire - Based on Supplier Scorecards (F2234A) | The scores are displayed in Supplier Evaluation by Questionnaire app. |
| Supplier Evaluation by User-Defined Criteria |  |  |  |
| [Manage User-Defined Criteria for Supplier Evaluation](#unique_38) [page ] 42 | Purchaser | Manage User-Defined Criteria for Supplier Evaluation (F3812) |  |
| [Display Supplier Evaluation Score by User-Defined Criteria](#unique_39) [page ] 44 | Purchaser | Supplier Eval by User Defined Criteria - Based on Average of Total Weighted Score (F3842A) | . |
| [Display Overall Supplier Evaluation Score](#unique_40) [page ] 45 | Purchaser | Overall Supplier Evaluation - Score (F2019) | . |
| Manage Supplier Evaluation Score |  |  |  |
| [Display Supplier Evaluation Score History](#unique_41) [page ] 46 | Purchaser | Supplier Evaluation Score History (F3811) | The supplier evaluation score history is displayed. |
| [Output Supplier Evaluation Score](#unique_42) [page ] 47 | Purchaser | Supplier Evaluation Score Output (F5061) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Operational Supplier Evaluation

#### Create Supplier Evaluation Weighting and Scoring

Purpose

In this activity, you create supplier evaluation weighting and scoring.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation Weighting and Scoring (F2551) . | The Supplier Evaluation Weighting and Scoring screen is displayed. |  |
| 3 | Create new weighting and scoring | Choose Add (+) to add new weighting and scoring for a specific purchasing category.In the GENERAL INFORMATION section, enter the following information:Purchasing Category: <select a purchasing category from the dropdown list.In the CRITERION section, check all the check box in the column Active, then enter the weighting value below:Inspection Lot: <For example, 10%>Quantity:<For example, 20%>Time: <For example, 20%>Price: <For example, 20%>Questionnaire: <For example, 10%>Quality Notification: <For example, 10%>Enter user-defined criteria if enabled, for example,Return Delivery of Goods: <For example, 4%>Reasonable Discounts: <For example, 5%>Parts Per Million: <for example, 5%>The total weighting value should be 100%.Select the field Quantity, in the new screen Criterion, select Add, then enter below data,Variance Percentage: <For example, 0>Variance Score: <For example, 100>Choose Apply and save the data. Multiple entries can be entered by this way.Select field Time, in the new screen Criterion, select Add, then enter below data,Variance Time in Days: <For example, 3>Variance Score:<For example, 90>Choose Apply and save the data. Multiple entries can be entered by this way.Select field Price, in the new screen Criterion, select Add, then enter below data,Variance Percentage: <For example, 2>Variance Score: <For example, 95>Choose Apply and save the data. Multiple entries can be entered by this way.Select field Quality Notification, in the new screen Criterion, select Add, then enter below data,Notification Count: <For example, 5>Variance Score: <For example, 90>Choose Apply and save the data. Multiple entries can be entered by this way.For user-defined criteria which is enabled, for example, Return Delivery of Goods, Reasonable Discounts andParts Per Million, please repeat above steps, and maintain the variance score.Save the entries. | All data is entered and saved.No error or warning messages come up. | All data is entered and saved.No error or warning messages come up. |
| 4 | Adjust Weighting Factor | Select Adjust Weighting Factor.Adjust the value of Weighting Factor.Save the data. | The Adjust Weighting Factor screen is displayed.Data is adjusted and saved.No error or warning messages come up. |  |
| 5 | Maintain Classification | Select Classification to maintain the classification data.In the tab Score, enter below data,A: <For example, from 80 To 100>B:<For example, from 60 To 79>C:<For example, from 0 To 59>Save the entries. | The Classification screen is displayed.All data is entered and saved.No error or warning messages displayed. |  |
| 6 | Adjust Quantity Scoring data | Select the entry Quantity.Choose the field Quantity.Choose Edit.Adjust the value of the Variance Percentage and Variance Score if necessary.Save the data. | The Criterion Screen is displayed.Data is adjusted and saved.No error or warning messages displayed. |  |
| 7 | Adjust Time Scoring data | Select the entry Time.Choose the field Time.Choose Edit.Adjust the value of the Variance Percentage and Variance Score if necessary.Save the data. | The Criterion Screen is displayed.Data is adjusted and saved.No error or warning messages displayed. |  |
| 8 | Adjust Price Scoring data | Select the entry Price.Choose the field Price.Choose Edit.Adjust the value of the Variance Percentage and Variance Score if necessary.Save the data. | The Criterion Screen is displayed.Data is adjusted and saved.No error or warning messages displayed. |  |
| 9 | Adjust Quality Notification Scoring data | Select the entry Quality Notification.Choose the field Quality Notification.Choose Edit.Adjust the value of the Variance Percentage and Variance Score if necessary.Save the data. | The Criterion Screen is displayed.Data is adjusted and saved.No error or warning messages displayed. |  |

|  |
| --- |
| Note The scoring data for inspection lot and questionnaire are calculated automatically, therefore it is not adjustable. |

#### Display Supplier Evaluation by Quantity

Purpose

In this activity the evaluation scores are displayed in the Supplier Evaluation by Quantity KPI (Key Performance Indicators).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation By Quantity - Based on Ordered and Received Quantity (F1661A) app. | The supplier evaluation by quantity screen is displayed.The variance score and variance % for all suppliers that have corresponding evaluation score are displayed. |  |
| 3 | Check the score by different dimensions | Select a dimension from the dropdown list, for example, by Purchasing Group. | The variance score, variance %, Number of PO Items and Number of POs for all purchasing groups that have corresponding evaluation score are displayed. |  |
| 4 | Check the score by document | Select Document from the dropdown list.Note You can search for both purchase order which are delivery completed or not. Or you can change the configuration for supplier evaluation criteria for specific business need. | The supplier evaluation by document screen is displayed.Note If the Delivery Completed in step Set the Configuration for Supplier Evaluation Criteria is set, only documents that are delivery completed could be displayed, the Delivery Completed in step Set the Configuration for Supplier Evaluation Criteria is not set,only documents that are not delivery completed could be displayed.If the Delivery Completed in step Set the Configuration for Supplier Evaluation Criteria is Both, all documents could be displayed. |  |

Result

The scores are displayed in Supplier Evaluation by Quantity app.

#### Display Supplier Evaluation by Price

Purpose

In this activity the evaluation scores are displayed in the Supplier Evaluation by Price KPI (Key Performance Indicators).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation By Price - Based on PO and Invoice Price (F1663A). | The variance score, variance % , Number of PO Items and Number of POs for all suppliers that have corresponding evaluation score are displayed. |  |
| 4 | Check the score by different dimensions | Select a dimension from the dropdown list, for example, by Purchasing Organization. | The variance score and variance % for all purchasing organizations that have corresponding evaluation score are displayed. |  |

Result

The scores are displayed in Supplier Evaluation by Price app.

#### Display Supplier Evaluation by Time

Purpose

In this activity the evaluation scores are displayed in the Supplier Evaluation by Time KPI (Key Performance Indicators).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation By Time - Based on Delivery and Goods Receipt Date (F1664A). | The Stat. Delivery Score, Stat. Delivery %, Delivery Date % and Delivery Date Score, Number of PO Items and Number of POs for all suppliers that have corresponding evaluation score are displayed. |  |
| 3 | Check the score by different dimensions | Select a dimension from the dropdown list, for example, by Material Group. | The Stat. Delivery Score, Stat. Delivery %, Delivery Date % and Delivery Date Score for all material groups that have corresponding evaluation score are displayed. |  |
| 4 | Check different document date | Select the dimension Document from the dropdown list. | If the Factory Calendar has been enabled in section 2.6.11, you can see more columns, Origl Ststcl Dlv Dte, Original First GR Dt, Original Final GR DT, Original Dlv Dte which is the original date from purchase order or goods receipt. The value of field Stat. Rel.Del. Date, Delivery Date, Frist GR Date, Final GR Date are all with the Factory Calendar applied. |  |

Result

The scores are displayed in Supplier Evaluation by Time app.

#### Display Supplier Evaluation by Quality Notification

Purpose

In this activity the evaluation scores are displayed in the Supplier Evaluation by Quality - Based on Quality Notification KPI (Key Performance Indicators).

|  |
| --- |
| Note App Supplier Evaluation by Quality - Quality Notification (F3295) will be deprecated and removed in 2102 release. The same functionality can be found in a new App Supplier Evaluation by Quality - Based on Quality Notification (F3295A). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation By Quality - Based on Quality Notification (F3295A) . | The Supplier Eval By Quality Notification screen is displayed. |  |
| 3 | Check the score by different dimensions | Select a dimension from the dropdown list, for example, by Plant. | The 5 KPIs Number of Quality Notifications, Quality Notification Score, Number fof PO Items, Rel. Quality Score and Number of POs score are displayed. |  |

Result

The scores are displayed in Supplier Evaluation by Quality Notification app.

#### Display Supplier Evaluation by Quality Inspection Lot

Purpose

In this activity the evaluation scores are displayed in the Supplier Evaluation by Quality - Inspection Lot KPI (Key Performance Indicators).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation by Quality - Inspection lot (F2309A) . | The variance score, Number of PO Items and Number of POs for all suppliers that have corresponding evaluation score are displayed. |  |
| 3 | Check the score by different dimensions | Select a dimension from the dropdown list, for example, Document. | All the documents with variance score are listed. |  |

Result

The scores are displayed in Supplier Evaluation by Quality - Inspection Lot app.

#### Display Supplier Evaluation by Operational Supplier Evaluation

Purpose

In this activity the operational supplier evaluation scores are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Operational Supplier Evaluation - Based on Score and Variance (F1662A) . | The operational score, price variance score, time variance score, quantity var, score, inspection lot score and notification score for all suppliers that have corresponding evaluation score are displayed. |  |
| 3 | Check the score by different dimensions | Select a dimension from the dropdown list, for example, Trend | The operational score, price variance score, time variance score, quantity var, score, inspection lot score and notification score trends, Number of PO Items and Number of POs are displayed. |  |
| 4 | Open up the mini tiles in the KPI header section | Choose Show Mini Tiles on the top right screen. | You can navigate from operational supplier evaluation score KPI to another KPI (for example, supplier evaluation by time). |  |

Result

The scores are displayed in Operational Supplier Evaluation app.

#### Parts Per Million

Purpose

In this activity, the Parts Per Million evaluation scores are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Parts per Million - By Returns and Quality Notifications (F4885) . | The Parts per Million screen is displayed. |  |
| 3 | Check the score by different dimensions | Select a dimension from the dropdown list, for example, Trend | Two KPIs Based On Return Delivery and Based On Quality Notification are displayed. |  |

Result

The scores are displayed in Parts Per Million – By Returns and Quality Notifications app.

#### Adjust Supplier Evaluation Scores Manually

Purpose

In this activity, the evaluation scores are adjusted manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Adjust Operational Supplier Evaluation Score (F2312). | The adjust operational supplier evaluation score screen is displayed. |  |
| 3 | Update score for purchase order/item | Select an entry and choose Edit.Enter the new value.Enter the comments if necessary.Choose OK to save the changes. | The update score for purchase order/item xxx/xxx screen is displayed.The new value is saved and no error message. |  |

Result

The scores are updated in Supplier Evaluation by Adjust Operational Supplier Evaluation Score app.

### Supplier Evaluation by Questionnaire

#### Create Sections and Questions in Question Library

Purpose

In this activity, you create sections and questions in the question library.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Questions (/SRMSMC/WDA_QLB_OVP_MAIN). | The question library of evaluation is displayed to maintain sections and questions. |  |
| 3 | Create several Sections | Go to the tab Sections.Select New to create several sections.Enter the Section Details (at least the mandatory fields).Save the entries. | All data is entered.No error or warning messages come up. |  |
| 4 | Create several Questions | Go to the tab Questions.Select New to create several questions. Create at least one question for each question type.Enter the Question Details. Ensure that some questions allow attachments and/or comments.Choose Save. | All data is entered.No error or warning messages come up. |  |

Result

Sections and questions in question library are created.

#### Create Evaluation Questionnaire

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity an evaluation questionnaire is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Evaluation Questionnaires - Evaluation (F2194) app. | The Manage Questionnaire is displayed. |  |
| 3 | Create new questionnaire | Select Create.Maintain new questionnaire by entering at least a questionnaire name, external name, sections and questions.Assign purchasing categories by choosing one of purchasing category from the dropdown list, then choose Add. Several purchasing categories can be assigned.Search for your previously created sections and questions.Add questions of all types. Mark some questions as mandatory. For questions of type Yes/No, mark some of them as disqualifying and enter weighting factors.For questions of type Single Answer, maintain the scores and weighting factors.Enter an Overall Target Score and an Overall Minimum Score.Save the entries. | Create New Questionnaire screen is opened in a new window.All data is entered.A questionnaire with all types of questions is created.No error or warning messages come up. |  |
| 4 | Release evaluation questionnaire | Select Release. | The previously created questionnaire is released. |  |

Result

A new questionnaire is created and released. .

#### Create Group-Based Evaluation Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an evaluation template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Evaluation Templates - Evaluation (F2193) app. | The Manage Templates app is displayed. |  |
| 3 | Maintain new group-based evaluation template | Choose Create button. Maintain the new group-based evaluation template by entering at least a name, an external name, an appraiser (for example: employee_procurement) and a supplier and by assigning your previously created evaluation questionnaire.Ensure that you add an appraiser for which you have a user with a maintained e-mail address.Maintain a Questionnaire Introduction.On the tab Questionnaires, add score information and at least one questionnaire created previously.Save the entries. | The group-based evaluation templated is created.No error or warning messages come up. |  |
| 4 | Release group-based evaluation template | Choose the Release button to release the group-based evaluation template. | The previously created group-based evaluation template is released. |  |

Result

The group-based evaluation template is created and released.

|  |
| --- |
| Note If you use email template, the language used in the template is based on the correspondence language of the appraiser that receives the email. The correspondence language is part of the business user master data of the corresponding user. |

#### Start Group-Based Evaluation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you start a group-based evaluation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Evaluation Templates - Evaluation (F2193) app.Select your previously created and released group-based evaluation template and click on the name that is displayed as a link. | The Manage Templates app is displayed. The group-based evaluation template is opened. |  |
| 3 | Start Group-Based Evaluation | Choose Start Group-Based Evaluation. | In a new window, the Group-Based Evaluation Request: New screen is opened. |  |
| 4 | Maintain the group-based evaluation request | Maintain the group-based evaluation request by entering at least an Evaluation Request Name and a Period to Be Evaluated.Choose Submit Evaluation Request. | A Group-Based Evaluation Request is created and submitted. |  |

Result

A group-based evaluation is started and the request is sent to the entered appraiser(s).

#### Maintain Evaluation Response as Appraiser

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you start a group-based evaluation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as appraiser which was entered in the evaluation template/request (e.g.: Employee - Procurement ). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Evaluate Suppliers (F1650) app.Select the corresponding evaluation response with status New which has the same name as your group-based evaluation request. | The Evaluate Suppliers app and the corresponding evaluation is displayed. |  |
| 3 | Answer questions | Answer the questions.Save your changes. | All data is saved.No error or warning messages come up. |  |
| 4 | Submit the evaluation response | Choose Submit. | The group-based evaluation response is submitted. |  |

Result

The Evaluation Response is created and answered by the appraiser.

#### Display Scorecards

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity a scorecard is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Scorecards - Evaluation Questionnaires (F2191) app.Find the corresponding group-based evaluation response in the list and check the status. | The Scorecard is displayed. |  |
| 3 | Check Scorecards | Drill down into details of sections and questions. | The result of the responses is displayed. |  |

Result

The groupd-based evaluation reponse is answered and corresponding scorecards are available.

#### Monitor Response

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the answered response is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Select the Monitor Responses - Evaluation (F1649) app.Select the corresponding evaluation response with status Returned which has the same name as your group-based evaluation request. | The Evaluation Response is displayed. |  |
| 3 | Check Response | Drill down into details of sections and questions. | The result of the responses is displayed. |  |

Result

The answered group-based evaluation response is displayed.

#### Display Supplier Evaluation by Questionnaire

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the evaluation scores are displayed in the Supplier Evaluation by Questionnaire KPI (Key Performance Indicators).

App Supplier Evaluation by Questionnaire – (Deprecated) Based on Supplier Scorecards(F2234) will be deprecated and removed in 2111 release. The same functionality can be found in a new App Supplier Evaluation by Questionnaire –Based on Supplier Scorecards(F2234A).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation By Questionnaire - Based on Supplier Scorecards (F2234A). Click Go button.Find the corresponding supplier, for which questionnaires were filled out and check the score. | The questionnaire score for all suppliers that have corresponding evaluation scorecards for the defined time frame (last 365 days) are displayed. |  |
| 3 | Check Document View | Click on the respective supplier and select "Document". | All evaluation scorecards for the supplier in the given timeframe are listed. |  |
| 4 | Check Evaluation Scorecard | Select one line in document view.Go to Jump To and select "display scorecards". | The Display Scorecard app is opened and the values of KPI are bypassed. |  |

Result

The scores are displayed in Supplier Evaluation by Questionnaire app.

### Supplier Evaluation by User-Defined Criteria

#### Manage User-Defined Criteria for Supplier Evaluation

Purpose

In this activity, you create the count for user-defined criteria for supplier evaluation for a specific supplier during a period, you can also deactivate, activate or delete it. Authorization can be set at supplier account group level. If the job in step Schedule Persistency of Parts Per Million Data has been scheduled and run successfully, you can view the Parts Per Millon relevant data. But you can’t create or change parts per million relevant data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage User-Defined Criteria for Supplier Evaluation (F3812). | The Manage User-Defined Criteria screen is displayed. |  |
| 3 | Display Supplier Evaluation Score History | Choose Create.Enter below information on the Manage User-Defined Criteria screen.Supplier: for example: 33300001Valid From: for example: < 01/01/2019>Valid To: for example: <Today>Count: for example: <5. Count can be entered manually or you can use the BAdI MM_PUR_ANA_UDC to update the value of count for a specific user-defined criterion. Value of count can be updated for a combination of suppliers, purchasing categories, and material groups for specific date ranges. Please refer to the online document for more details.>Criterion: for example: <Reasonal Discounts>Comment: <You can enter comment after choosing Save and then Edit button>ChooseCreate. | The supplier evaluation count is saved. |  |
| 4 | Deactivate Supplier Evaluation count | On the Manage User Defined Criteria screen, select one item, choose Deactivate, the status of the item is updated to Inactive (X). | The item is deactivated. |  |
| 5 | Activate Supplier Evaluation count | On the Manage User Defined Criteria screen, select one item, choose Activate, the status of the item is updated to Active (X). | The item is activated. |  |
| 6 | Delete Supplier Evaluation count | On the Manage User Defined Criteria screen, select one item, choose Delete, on the Delete screen, choose Delete, the item is Deleted. | The item is deleted. |  |
| 7 | Display Parts Per Million data | On the Manage User Defined Criteria screen, search area, select the criterion Parts Per Million from the dropdown list,Choose Go.Choose one item, go to details, the comment is Updated From PPM Job.If the job in step Schedule Persistency of Parts Per Million Data has not been scheduled, there may be no data. | The data relevant to Parts Per Million is displayed. |  |

Result

Supplier Evaluation count for user defined criteria is maintained.

#### Display Supplier Evaluation Score by User-Defined Criteria

Purpose

In this activity the supplier evaluation scores by user-defined criteria are displayed.

App Supplier Evaluation Score by User-Defined Criteria – (Deprecated) Based on Average of Total Weighted Score (F3842) will be deprecated and removed in 2111 release. The same functionality can be found in a new App Supplier Evaluation Score by User-Defined Criteria–Based on Average of Total Weighted Score (F3842A).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Eval by User Defined Criteria - Based on Average of Total Weighted Score (F3842A) app. | The Supplier Eval. by User Defined Criteria is displayed. |  |
| 3 | Check Overall Scores by Different Dimensions | Select a dimension from the dropdown list, for example, by Supplier or by Purchasing Category. | The enabled user-defined criteria, like Return Delivery of Goods score, Reasonable score and Avg. Weighted Total Score are displayed. |  |

Result

The scores are displayed in Supplier Evaluation Score by User-Defined Criteria app.

#### Display Overall Supplier Evaluation Score

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the overall supplier evaluation scores are displayed in the Overall Supplier Evaluation app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Overall Supplier Evaluation - Score (F2019) . | The operational score, questionnaire scor, user-defined criteria score which are enabled and overall score for all suppliers that have corresponding evaluation score are displayed. |  |
| 3 | Check Overall Scores by Different Dimensions | Select a dimension from the dropdown list, for example, by Purchasing Category. | The operational score, questionnaire score, user-defined criteria score which are enabled and overall score for all purchasing categories that have corresponding evaluation score are displayed. |  |
| 4 | Navigate to other Fiori APPs | Choose Jump To.Select an APP from the list, for ex-ample, Supplier Evaluation Score Output.You will be navigated to that APP. | The App Supplier Evaluation Score Output will be displayed. |  |

Result

The scores are displayed in Overall Supplier Evaluation - Score app.

### Manage Supplier Evaluation Score

#### Display Supplier Evaluation Score History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the supplier evaluation score history which is calculated by the job in preliminary step Schedule Job for Persistency of Supplier Evaluation Scores. Or you delete the obsolete jobs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation Score History (F3811). | The Supplier Evaluation Score History screen is displayed. |  |
| 3 | Display Supplier Evaluation Score History | Choose Go.On the Operational Score tab, you can see a list including supplier, calendar year, material group, calendar month, operational score, time variance score, price variance score, quantity variance score, inspection lot score, quality notification score.On the Overall Score tab, you can see a list including supplier, calendar month, calendar year, overall score and questionnaire score.On the Aggregated Score tab, you can see a list including supplier, material group, overall score, operational score, time variance score, price variance score, quantity score, inspection lot score, quality notification score and questionnaire score.Select one job run ID, you can see the details on the Job Run Details screen.Run IDStart DateEnd DateExecuted ByExecuted On | The supplier evaluation score history is displayed |  |
| 4 | Delete Supplier Evaluation Score History job | On the Operational Score tab, or the Overall Score tab, choose one or multiple jobs, choose Delete.On the Delete Screen, choose Yes. | Deleted Score from Operational and Overall Score messages come upThe supplier evaluation score history job is deleted. |  |

Result

Supplier Evaluation Score History is displayed and some of them are deleted.

#### Output Supplier Evaluation Score

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you send out the supplier evaluation score via email or print it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Supplier Evaluation Score Output (F5061) | The Supplier Evaluation Score Output screen is displayed. |  |
| 3 | Create Active Scores | Choose Create Active Scores.On the Create Active Scores screen, enter below data,Supplier: For example, 33300001 Multiple suppliers can be selected.Evaluation Start Date: <For example, 01/01/2019>Evaluation End Date: <For example, today>Currency: For example,AEDChoose Create Scores. | The supplier evaluation score output is displayed |  |
| 4 | Send Out or Print Supplier Evalutation Scores for Cur-rent Scores | On the Supplier Evaluation Score Output screen, enter below data"Score Output Type: <For example, Active>Score Creation Date: <For example, today>Choose Go.Choose the item which was created in step 1, please wait and refresh the screen if you can’t fine the item, it may not complete yet.Go to the details of this item.On the Output Message screen, Output Details tab, you see two items, one is for email, the other one is for print.Check the one for email, then choose Send Output, an email is send out to the email address which is maintained in the supplier master data of communication and address-independent communication.Choose Retry if sending out email failed.Choose Set to Completed if you want to complete this task.Choose Duplicate only if the status of this item is completed, but you need to send out an email again. | Current scores are calculated and sent out via email or printed successfully. |  |
| 5 | Delete one entry | On the Supplier Evaluation Score Output screen, choose one entry you want to delete.Choose Delete.The entry is deleted. | An entry is deleted. |  |
| 6 | Send Out or Print Supplier Evalutation Scores for His-torical Scores | On the Supplier Evaluation Score Output screen, enter below data,Score Output Type: <For example, Historical>Choose Go.The supplier evaluation scores which was calculated by the job in preliminary step Schedule Job for Persistency of Supplier Evaluation Scores are listed in the screen.Choose one of the items, and choose Initiate Output.On the Output Message screen, Output Details tab, you see two items, one is for email, the other one is for print.Check the one for email, then choose Send Output, an email is sent out to the email address which is maintained in the Communication section under the Address Tab of supplier master data.Choose Retry if sending out email failed.Choose Set to Completed if you want to complete this task.Choose Duplicate only if the status of this item is completed, but you need to send out an email again. | Historical scores are sent out via email or printed successfully. |  |

Result

Supplier Evaluation Score is printed or sent out via email.

## Appendix

### Process Integration

#### No Succeeding Processes

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
> Flagged while digesting this document, not verified: Create Supplier Evaluation Weighting and Scoring step 3 says total weighting should be 100%, but its example values (Inspection Lot 10, Quantity 20, Time 20, Price 20, Questionnaire 10, Quality Notification 10, Return Delivery 4, Reasonable Discounts 5, PPM 5) add up to 104%.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-vendor-performance-consumer-products-6a6-ae-1154]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/SL4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 83,435 chars in the whole document
