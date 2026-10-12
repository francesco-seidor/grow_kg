---
id: 10-procurement/test-script-vendor-performance-consumer-products-6a6-ae-1154
title: "Test Script: Vendor Performance – Consumer Products (6A6_AE) (6A6_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 6A6: supplier evaluation via weighting/scoring, questionnaires, templates, appraisals and scorecards."
cluster: 10-procurement
tags: [kb/procurement, topic/supplier-evaluation]
aliases: [6A6_S4CLD2608_BPD_EN_AE]
keywords: [Supplier Evaluation and Vendor Performance, supplier evaluation, weighting and scoring, question library, evaluation questionnaires, evaluation templates, group-based evaluation, supplier scorecards, appraiser responses, purchasing categories]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6A6_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1154
topic: 10-procurement/supplier-evaluation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Vendor Performance – Consumer Products (6A6_AE) (6A6_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6A6_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Supplier Evaluation and Vendor Performance** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Vendor Performance – Consumer Products (6A6_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232858159)

[2 Prerequisites 3](#_Toc232858160)

[2.1 System Access 3](#_Toc232858161)

[2.2 Roles 3](#_Toc232858162)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232858163)

[2.4 Business Conditions 5](#_Toc232858164)

[2.5 Additional Manual Configuration 5](#_Toc232858165)

[2.6 Preliminary Steps 5](#_Toc232858166)

[2.6.1 Create the Question Library 5](#_Toc232858167)

[2.6.2 Setup Analytical Reporting Currencies (Optional) 6](#_Toc232858168)

[2.6.3 Create Purchasing Categories 8](#_Toc232858169)

[3 Overview Table 11](#_Toc232858170)

[4 Test Procedures 12](#_Toc232858171)

[4.1 Create Supplier Evaluation Weighting and Scoring 12](#_Toc232858172)

[4.2 Create Sections and Questions in Question Library 15](#_Toc232858173)

[4.3 Create Evaluation Questionnaire 20](#_Toc232858174)

[4.4 Create Group-Based Evaluation Template 26](#_Toc232858175)

[4.5 Start Group-Based Evaluation 27](#_Toc232858176)

[4.6 Maintain Evaluation Response as Appraiser 28](#_Toc232858177)

[4.7 Display Scorecards 30](#_Toc232858178)

## Purpose

Overview

You can evaluate your company's suppliers to obtain a basis for your business relationship with them and to optimize your supply base. Based on the feedback you gather through questionnaires, you obtain a scorecard for each supplier evaluated. The scorecard helps you to assess a supplier’s strengths and shortcomings and to initiate measures for improvement. Evaluation scorecards also let you easily compare suppliers within a peer group.

Ultimately, a combined real-time view across operational and questionnaire-based scores provides a holistic view of your supplier's performance. The business process provides two different use cases for the category manager: Evaluate supplier performance and analyze KPIs based on the evaluation.

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

The Users TESTER_EMP_USER_1 and TESTER_EMP_USER_2 are only optional, they have the same role as EMPLOYEE_PROCUREMENT. If you do not want to create them, replace their names in chapter 5 by EMPLOYEE_PROCUREMENT.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Employee - Procurement | SAP_BR_EMPLOYEE_PROCUREMENT | Self Services - Procurement | SAP_MM_SPT_EMPLOYEE_SERVICES_PC | EMPLOYEE_PROCUREMENT |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | PURCHASER |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | BPC_EXPERT |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This scope item requires new master data set to be created and the needed master data objects are mentioned below.

Suppliers:

Below mentioned Suppliers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 | Domestic AE Supplier 1 | Raw material supplier. |
| Supplier | 33300002 | Domestic AE Supplier 2 | Packaging material supplier. |
| Supplier | 33300003 | Domestic AE Supplier 3 | Packaging material supplier. |
| Supplier | 33300007 | Domestic AE Subcontractor | Subcontractor. |
| Supplier |  | Domestic Subcontractor 05001 | Subcontractor. |
| Supplier | 33300010 | Domestic AE Supplier 10 | Raw material supplier. |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

| Master Data Script ID | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1FM - Quality Management in Procurement (Optional) | Start with the Quality Management in Procurement process and then you can display supplier evaluation by quality inspection lot. |
| 2F9 - Quality Management for Complaints Against Suppliers (Optional) | Start with the Quality Management for Complaints Against Suppliers process, create the quality notification, then you can display supplier evaluation by quality notification. |
| 19E - Supplier Classification and Segmentation (Optional) | Start with the Supplier Classification and Segmentation, create the Purchasing Categories, then add new weighting and scoring for the purchasing categories in Create Supplier Evaluation Weighting and Scoring. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

### Preliminary Steps

#### Create the Question Library

Purpose

In this procedure, you create the question library which is required for creating questions and sections.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Question Library for Supplier Evaluation (/SRMSMC/CREA_QLB_EVL) | The Create Question Library for Supplier Evaluation screen displays. |  |
| 3 | Create the data | Enter below data:Original language: Ex., ENChoose Execute.Note The library can be created only once! Changing the language later is not possible! | The question library has been created. |  |

#### Setup Analytical Reporting Currencies (Optional)

Purpose

In this procedure, you can setup two analytical reporting currencies that will be used in various analytical KPIs and queries Procurement in SAP S/4HANA Cloud Public Edition. If user selects one of the two configured reporting currencies as display currency in an analytical KPI, the system doesn't convert the reporting currency to display currency at runtime. This enhances the performance of the KPI.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Setup the analytical reporting currencies | Choose Configure Your Solution.Choose Sourcing and Procurement in the Application Area field, Operational Procurement in the sub-area then navigate to the to the item name Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step1 Setup Analytical Reporting Currencies.Choose New Entries.Enter below data:Reporting Curr. Id: for example, Reporting Currency 1Currency: for example, AEDChoose Save.Two reporting currencies can be setup. | Reporting currencies are added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Setup Analytical Reporting Currencies.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Setup the analytical reporting currencies | Choose New Entries.Enter below data:Reporting Curr. Id: for example, Reporting Currency 1Currency: for example, AEDChoose Save.Two reporting currencies can be setup. | Reporting currencies are added. |  |

#### Create Purchasing Categories

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a purchasing category is created and a purchaser responsible for the purchasing category is assigned. Suppliers, team employees, and material groups will be assigned to it. This is required to assign the purchasing categories to the supplier evaluation weighting and scoring and the evaluation questionnaires. This process step needs to be done only once. In case it is already available you can continue with the next step.

|  |
| --- |
| Note In this chapter an example on how to create new purchasing categories is described. If you have already maintained Purchasing Categories you need to enhance it by the country specific suppliers (instead of creating new ones). The same purchase category may contain DE as well as the US suppliers |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Categories (F0337) app in the Classification and Segmentation tile group. | The Manage Purchasing Categories screen displays. |  |
| 3 | Enter Purchasing Category data | Choose Create.In the General section, make the following entries:Name: Raw Material SupplierClick on the lookup for Purchaser Responsible: Enter First Name - Example, Last name - Purchaser and click Go Select the relevant userChoose Enter. | All data is entered, no error or warning messages exist. |  |
| 4 | Assign Suppliers | In the Suppliers section, choose Add Line, and enter following data:ID: 33300001, 33300010Choose Enter. | The assignment of suppliers to the purchasing category is done. |  |
| 5 | Assign Material Groups | In the Material Groups section, choose Add Material Groups and enter following data in the dialogue box:Material Group ID: L002Choose GO button.In the search result list select the entry of L002 and choose OK.Enter Purchasing Category Description in the Languages for Purchasing Category Description Section. | The material group is assigned to the purchasing category. |  |
| 6 | Save Purchasing Category | Choose Save. | A new Purchasing Category is created.A message Data saved successfully displays. |  |
| 7 | Enter Purchasing Category data | Choose Create.In the General section, make the following entries:Name: Packaging SupplierPurchaser Responsible: Enter First Name - Example, Last name - Purchaser and click GoChoose Enter. | All data is entered, no error or warning messages exist. |  |
| 8 | Assign Suppliers | In the Suppliers section, choose Add Line, and enter following data:ID: 33300002, 33300003Choose Enter. | The assignment of suppliers to the purchasing category is done. |  |
| 9 | Assign Material Groups | In the Material Groups section, choose Add Material Groups and enter following data in the dialogue box:Material Group ID: L006Choose GO button.In the search result list select the entry of L006 and choose OK.Enter Purchasing Category Description in the Languages for Purchasing Category Description Section. | The material group is assigned to the purchasing category. |  |
| 10 | Save Purchasing Category | Choose Save. | A new Purchasing Category is created.A message Data saved successfully displays. |  |
| 11 | Enter Purchasing Category data | Choose Create.In the General section, make the following entries:Name: Subcontracting SupplierPurchaser Responsible: Enter First Name - Example, Last name - Purchaser and click GoChoose Enter. | All data is entered, no error or warning messages exist. |  |
| 12 | Assign Suppliers | In the Suppliers section, choose Add Line, and enter following data:ID: 33300007,Choose Enter. | The assignment of suppliers to the purchasing category is done. |  |
| 13 | Assign Material Groups | In the Material Groups section, choose Add Material Groups and enter following data in the dialogue box:Material Group ID: L003,L004Choose GO button.In the search result list select the entry of L003 and choose OK. Then add L004 in the same manner.Enter Purchasing Category Description in the Languages for Purchasing Category Description Section. | The material group is assigned to the purchasing category. |  |
| 14 | Save Purchasing Category | Choose Save. | A new Purchasing Category is created.A message Data saved successfully displays. |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/ App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Supplier Evaluation Weighting and Scoring](#unique_12) [page ] 12 | Purchaser | Supplier Evaluation Weighting and Scoring (F2551) | Scoring and Weighing for purchasing criteria has been created/adjusted. |
| [Create Sections and Questions in Question Library](#unique_13) [page ] 15 | Purchaser | Manage Questions - Evaluation (/SRMSMC/WDA0328) | Several Sections and Questions have been created. |
| [Create Evaluation Questionnaire](#unique_14) [page ] 20 | Purchaser | Manage Evaluation Questionnaires - Evaluation (F2194) | Questionnaires have been created. |
| [Create Group-Based Evaluation Template](#unique_15) [page ] 26 | Purchaser | Manage Evaluation Templates - Evaluation (F2193) | Group based Evaluation Templates have been created. |
| [Start Group-Based Evaluation](#unique_16) [page ] 27 | Purchaser | Manage Evaluation Templates - Evaluation (F2193) | Group based Evaluation Requests are created and submitted. |
| [Maintain Evaluation Response as Appraiser](#unique_17) [page ] 28 | Employee - Procurement | Evaluate Suppliers (F1650) | The group based Evaluation response is submitted and answered by the appraiser. |
| [Display Scorecards](#unique_18) [page ] 30 | Purchaser | Display Scorecards - Evaluation Questionnaires (F2191) | The group based Evaluation response is answered and corresponding scorecards are available. |

## Test Procedures

### Create Supplier Evaluation Weighting and Scoring

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create supplier evaluation weighting and scoring. This step is performed once and can be adjusted later if required.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Evaluation Weighting and Scoring (F2551) app in the Supplier Evaluation tile group. | The Supplier Evaluation Weighting and Scoring screen is displayed. |  |
| 3 | Create new weighting and scoring | Choose Add (+) to add new weighting and scoring for a specific purchasing category.In the GENERAL INFORMATION section, enter the following information:Purchasing Category: Subcontracting SupplierIn the CRITERION section, check relevant check box in the column Active, then enter the weighting value below:Inspection Lot: <For example, 10%>Quantity:<For example, 20%>Time: <For example, 20%>Price: <For example, 20%>Questionnaire: <For example, 20%>Quantity Notification: <For example, 10%>Select the field Quantity, in the new screen Criterion, select Add, then enter below data. If Variance Percentage and Variance Score exist, then edit the Variance Percentage and Variance Score. Delete not necessary variances.Variance Percentage: <For example, -100>Variance Score: <For example, 1>Variance Percentage: <For example, -20>Variance Score: <For example, 10>Variance Percentage: <For example, -15>Variance Score: <For example, 40>Variance Percentage: <For example, -10>Variance Score: <For example, 65>Variance Percentage: <For example, -5>Variance Score: <For example, 80>Variance Percentage: <For example, -2>Variance Score: <For example, 90>Variance Percentage: <For example, -1>Variance Score: <For example, 95>Variance Percentage: <For example, 0>Variance Score: <For example, 100>Variance Percentage: <For example, 2>Variance Score: <For example, 95>Variance Percentage: <For example, 10>Variance Score: <For example, 80>Variance Percentage: <For example, 15>Variance Score: <For example, 60>Variance Percentage: <For example, 20>Variance Score: <For example, 40>Variance Percentage: <For example, 30>Variance Score: <For example, 10>Variance Percentage: <For example, 100>Variance Score: <For example, 1>Choose Apply and save the data.Now repeat the steps for the field Time.Select field Time, in the new screen Criterion, click on edit and select Add, then enter below data. If Variance Time in Days and Variance Score exist, then edit the Variance Time in Days and Variance Score. Delete not necessary variances.Variance Time in Days: <For example, 3>Variance Score: <For example, 90>Choose Apply and save the data. Multiple entries can be entered by this way.Select field Price, in the new screen Criterion, select Add, then enter below data. If Variance Time in Days and Variance Score exist, then edit the Variance Time in Days and Variance Score. Delete not necessary variances.Variance Percentage: <For example, 2>Variance Score: <For example, 95>Choose Apply and save the data. Multiple entries can be entered by this way.Select field Quality Notification, in the new screen Criterion, select Add, then enter below data. If Notification Count and Variance Score exist, then edit the Notification Count and Variance Score.Notification Count: <For example, 5>Variance Score: <For example, 90>Choose Apply and save the data. Multiple entries can be entered by this way.Save the entries. | All data is entered and saved.Warning Message Displayed: To access your record, type in the document name in the Purchasing Category field as the dropdown is limited to particular records. |  |
| 4 | Adjust Weighting Factor | Select a Purchasing Category andSelect Adjust Weighting Factor.Adjust the value of Weighting Factor.Save the data. | The Adjust Weighting Factor screen is displayed.Data is adjusted and saved.No error or warning messages comes up. |  |
| 5 | Maintain Classification | Select Classification to maintain the classification data.In the tab Score, enter below data,A: <For example, from 80 To 100>B: <For example, from 60 To 79>C: <For example, from 0 To 59>Save the entries. | The Classification screen is displayed.All data is entered and saved.No error or warning messages displayed. |  |
| 6 | Adjust Quantity Scoring data | Select the entry Quantity.Choose the field Quantity.Choose Edit.Adjust the value of the Variance Percentage and Variance Score if necessary.Save the data. | The Criterion Screen is displayed.Data is adjusted and saved.No error or warning messages displayed. |  |
| 7 | Adjust Time Scoring data | Select the entry Time.Choose the field Time.Choose Edit.Adjust the value of the Variance Time in days and Variance Score if necessary.Save the data. | The Criterion Screen is displayed.Data is adjusted and saved.No error or warning messages displayed. |  |
| 8 | Adjust Price Scoring data | Select the entry Price.Choose the field Price.Choose Edit.Adjust the value of the Variance Percentage and Variance Score if necessary.Save the data. | The Criterion Screen is displayed.Data is adjusted and saved.No error or warning messages displayed. |  |
| 9 | Adjust Quality Notification Scoring data | Select the entry Quality Notification.Choose the field Quality Notification.Choose Edit.Adjust the value of the Notification Count and Variance Score if necessary.Save the data. | The Criterion Screen is displayed.Data is adjusted and saved.No error or warning messages displayed. |  |

|  |
| --- |
| Note The scoring data for inspection lot and questionnaire are calculated automatically, therefore it is not adjustable. |

### Create Sections and Questions in Question Library

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create sections and questions in the question library. This step is performed once and can be adjusted later if required.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Questions - Evaluation (/SRMSMC/WDA0328) app. | Question Library for Supplier Evaluation is displayed.The question library of evaluation is displayed to maintain sections and questions. |  |
| 3 | Create several Sections | Go to the tab Groups.Select New to create a group.Enter the Name of a Group (at least the mandatory fields).Z05_General corporate questionsSelect New to create a group.Enter the Name of a Group (at least the mandatory fields).Z05_Special corporate questionsSave the entries. | All data is entered.No error or warning messages comes up. |  |
| 4 | Create several Sections | Go to the tab Sections.Select New to create several sections.Enter the Section Details (at least the mandatory fields).Section name: Z05_QM_GGroup: Z05_General corporate questionsSection Title: Z05_General Quality Management sectionExplanation: Questions regarding general quality management topics.Select New to create several sections.Enter the Section Details (at least the mandatory fields).Section name: Z05_QM_SGroup: Z05_Special corporate questionsSection Title: Z05_Special Quality Management sectionExplanation: Questions regarding special quality management topics.Select New to create several sections.Enter the Section Details (at least the mandatory fields).Section name: Z05_PP_GGroup: Z05_General corporate questionsSection Title: Z05_General Production Planning sectionExplanation: Questions regarding general production planning topics.Select New to create several sections.Enter the Section Details (at least the mandatory fields).Section name: Z05_PP_SGroup: Z05_Special corporate questionsSection Title: Z05_Special Production Planning sectionExplanation: Questions regarding special production planning topics.Save the entries. | Several Sections Created.No error or warning messages comes up. |  |
| 5 | Create Questions | Go to the tab Questions.Note If you select the Transfer-Button you can export or import questions via xml-files from/ into the question librarySelect New to create several questions. Create at least one question for each question type.Enter the Question Details. Ensure that some questions allow attachments and/or comments.Select New and Choose Option Free Text from Dropdown.Question name: Z05_Continuous ImprovementGroup: Z05_General corporate questionsQuestion text: Explain your continuous improvement processAttachment from Recipient: MANDATORYSelect New and Choose Option Single Answer from Dropdown.Question name: Z05_Quality SystemGroup: Z05_General corporate questionsQuestion text: Which quality system is established?Attachment from Recipient: OPTIONALComment from Recipient: ENABLEDSelect Tab AnswersAnswer text: ISO9001Score: 100Answer text: ISO9002Score: 75Answer text: VDA 6.3Score: 50Answer text: OthersScore: 25Answer text: NoneScore: 0Select New and Choose Option Single Answer from Dropdown.Question name: Z05_System SupportGroup: Z05_General corporate questionsQuestion text: How does the system support the production?Attachment from Recipient: OPTIONALComment from Recipient: ENABLEDSelect Tab AnswersAnswer text: Full automaticallyScore: 100Answer text: Partial full automaticallyScore: 75Answer text: Semi automaticallyScore: 50Answer text: Partial semi automaticallyScore: 25Answer text: NoneScore: 0Select New and Choose Option Yes/No from Dropdown.Question name: Z05_Quality ManagementGroup: Z05_General corporate questionsQuestion text: Is there a quality management established in the company?Attachment from Recipient: OPTIONALComment from Recipient: ENABLEDRadio button Score: YesSelect Yes/NoQuestion name: Z05_Goods receipt controlGroup: Z05_Special corporate questionsQuestion text: Is there a quality control during the goods receipt?Attachment from Recipient: OPTIONALComment from Recipient: ENABLEDRadio button Score: YesSelect Yes/NoQuestion name: Z05_Production planning controlGroup: Z05_General corporate questionsQuestion text: Is there a quality control established in the production?Attachment from Recipient: OPTIONALComment from Recipient: ENABLEDRadio button Score: YesSelect New and Choose Option Multiple Answers from Dropdown.Question name: Z05_Quality control pointsGroup: Z05_Special corporate questionsQuestion text: In which processes are quality control established?Attachment from Recipient: OPTIONALSelect tab AnswersSelect New two timesAnswer text:Goods receiptProduction beginningGoods issueCustomer returnClaim managementDuring the productionEnd control after the productionSelect New and Choose Option Multiple Answers from Dropdown.Question name: Z05_Batch traceabilityGroup: Z05_General corporate questionsQuestion text: Time for an End-to-End batch traceability.Attachment from Recipient: OPTIONALSelect tab AnswersSelect the last two placeholders for answers and click on DeleteAnswer text:< 1hour1 - 4 hours> 4 hoursSelect New Multiple AnswersQuestion name: Z05_Electronic data transferGroup: : Z05_General corporate questionsQuestion text: Technical ways of data transfer.Attachment from Recipient: OPTIONALSelect tab AnswersAnswer text:EDIXMLFile-Transfere-MailManuallyChoose Save. | All data is entered.No error or warning messages comes up.Questions in question library are created. |  |

### Create Evaluation Questionnaire

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity an evaluation questionnaire is created. This step is performed once and can be adjusted later if required.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Evaluation Questionnaires - Evaluation (F2194) app in the Supplier Evaluation tile group. | The Manage Questionnaire Screen is displayed. |  |
| 3 | Create new questionnaire | Select Create.Maintain new questionnaire by entering at least a questionnaire name, external name, sections and questions.Assign purchasing categories by choosing one of the purchasing categories from the dropdown list, then choose Add. Several purchasing categories can be assigned.Search for your previously created sections and questions.Add questions of all types. Mark some questions as mandatory. For questions of type Yes/No, mark some of them as disqualifying and enter weighting factors.For questions of type Single Answer, maintain the scores and weighting factors.Enter an Overall Target Score and an Overall Minimum Score.Data for first Questionnaire:On tab BASIC DATA:Questionnaire name: Z05_Supplier Questionnaire SubcontractingPurchaser Responsible: PURCHASERAssigned Purchasing Categories: Subcontracting SupplierOn tab LANGUAGES FOR EXTERNAL QUESTIONNAIRE NAMEExternal Questionnaire Name: Z05_Supplier Questionnaire SubcontractingOn tab QUESTIONSOverall target score: 100Overall minimum score: 0Press Add Section:Press Go and then select Section name.Section: Z05_QM_GPress Add Question:Press Go and then select Question name.Questions: Z05_Quality ManagementMandatory: YesDisqualifying: YesPress Add Question:Press Go and then select Question name.Questions: Z05_Quality SystemMandatory: YesDisqualifying: blankSave the entries. | The Evaluation Questionnaire: New screen is displayed in new window.All data is entered.A questionnaire with all types of questions is created.No error or warning messages comes up. |  |
| 4 | Release evaluation questionnaire | Select Release. | The previously created questionnaire is released. |  |
| 5 | Create new questionnaire | Select Create.Maintain new questionnaire by entering at least a questionnaire name, external name, sections and questions.Assign purchasing categories by choosing one of the purchasing categories from the dropdown list, then choose Add. Several purchasing categories can be assigned.Search for your previously created sections and questions.Add questions of all types. Mark some questions as mandatory. For questions of type Yes/No, mark some of them as disqualifying and enter weighting factors.For questions of type Single Answer, maintain the scores and weighting factors.Enter an Overall Target Score and an Overall Minimum Score.Data for Second Questionnaire:On tab BASIC DATA:Questionnaire name: Z05_Supplier Questionnaire Raw Material SubcontractingPurchaser Responsible: PURCHASERAssigned Purchasing Categories: Raw Material SupplierOn tab LANGUAGES FOR EXTERNAL QUESTIONNAIRE NAMEExternal Questionnaire Name: Z05_Supplier Questionnaire Raw MaterialOn tab QUESTIONSOverall target score: 100Overall minimum score: 0Press Add Section:Press Go and then select Section name.Section: Z05_PP_GPress Add Question:Press Go and then select Question name.Questions: Z05_Continuous improvementMandatory: YesDisqualifying: blankPress Add Question:Press Go and then select Question name.Questions: Z05_Electronic data transferMandatory: NoDisqualifying: blankPress Add Section:Press Go and then select Section name.Section: Z05_QM_GPress Add Question:Press Go and then select Question name.Questions: Z05_Production planning controlMandatory: NoDisqualifying: blankPress Add Question:Press Go and then select Question name.Questions: Z05_Batch traceabilityMandatory: YesDisqualifying: blankPress Add Section:Press Go and then select Section name.Section: Z05_PP_SPress Add Question:Press Go and then select Question name.Questions: Z05_Production planning controlMandatory: NoDisqualifying: blankPress Add Question:Press Go and then select Question name.Questions: Z05_Quality control pointsMandatory: YesDisqualifying: blankSave the entries. | Create New Questionnaire screen is opened in a new window.All data is entered.A questionnaire with all types of questions is created.No error or warning messages comes up. |  |
| 6 | Release evaluation questionnaire | Select Release. | The previously created questionnaire is released. |  |
| 7 | Create new questionnaire | Select Create.Maintain new questionnaire by entering at least a questionnaire name, external name, sections and questions.Assign purchasing categories by choosing one of the purchasing category from the dropdown list, then choose Add. Several purchasing categories can be assigned.Search for your previously created sections and questions.Add questions of all types. Mark some questions as mandatory. For questions of type Yes/No, mark some of them as disqualifying and enter weighting factors.For questions of type Single Answer, maintain the scores and weighting factors.Enter an Overall Target Score and an Overall Minimum Score.Data for Third Questionnaire:On tab BASIC DATA:Questionnaire name: Z05_Supplier Questionnaire Packaging MaterialPurchaser Responsible: PURCHASERAssigned Purchasing Categories: Packaging SupplierOn tab LANGUAGES FOR EXTERNAL QUESTIONNAIRE NAMEExternal Questionnaire Name: Z05_Supplier Questionnaire Packaging MaterialOn tab QUESTIONSOverall target score: 100Overall minimum score: 0Press Add Section:Press Go and then select Section name.Section: Z05_QM_GPress Add Question:Press Go and then select Question name.Questions: Z05_Continuous improvementMandatory: NoDisqualifying: blankPress Add Question:Press Go and then select Question name.Questions: Z05_Quality ManagementMandatory: YesDisqualifying: YesPress Add Question:Press Go and then select Question name.Questions: Z05_Quality SystemMandatory: NoDisqualifying: blankPress Add Question:Press Go and then select Question name.Questions: Z05_Batch traceabilityMandatory: YesDisqualifying: blankPress Add Section:Press Go and then select Section name.Section: Z05_PP_SPress Add Question:Press Go and then select Question name.Questions: Z05_Production planning controlMandatory: YesDisqualifying: YesPress Add Question:Press Go and then select Question name.Questions: Z05_Quality control pointsMandatory: NoDisqualifying: blankSave the entries. | Create New Questionnaire screen is opened in a new window.All data is entered.A questionnaire with all types of questions is created.No error or warning messages comes up. |  |
| 8 | Release evaluation questionnaire | Select Release. | The previously created questionnaire is released. |  |

### Create Group-Based Evaluation Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an evaluation template.

To add an appraiser, the employee must be an employee user, please refer to the sections in the Administration Guide for the Implementation of SAP Best Practices for SAP S/4HANA.

|  |
| --- |
| Note The creation of the Group-Based Evaluation Template is described for the procurement of raw materials. You can also create for the procurement of subcontracting or packaging material using the master data mentioned above. As appraisers you may use TESTER_EMP_USER_1 and TESTER_EMP_USER_2 instead of EMPLOYEE_PROCUREMENT. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Evaluation Templates - Evaluation (F2193) app in the Supplier Evaluation tile group. | The Manage Templates app is displayed. |  |
| 3 | Maintain new group-based evaluation template | Choose Create button. Maintain the new group-based evaluation template by entering at least a name, an external name, an appraiser (for example: EMPLOYEE_PROCUREMENT) and a supplier and by assigning your previously created evaluation questionnaire.Ensure that you add an appraiser for which you have a user with a maintained e-mail address.Maintain a Questionnaire Introduction.On the tab Questionnaires, add score information and at least one questionnaire created previously.On tab BASIC DATAEvaluation Template Name: Z05_employee_procurement raw materialDays until response deadline: 0Purchasing Category: Raw Material SupplierPurchaser Responsible: PURCHASEROn tab APPRAISERSPress Add Appraiser and then GoSelect Appraiser: EMPLOYEE_PROCUREMENT and Choose OKEnter an E-Mail addressOn tab SUPPLIER PEER GROUPPress Add SupplierA Pop-up appears. Now you could use the purchase category Raw Material Supplier to select raw material supplier.Press GoSelect 33300001 and choose OkOn tab QUESTIONNAIRESOverall target score: 100Overall minimum score: 0Press Add QuestionnaireA Pop-up appears. Now you could use the purchase category Raw Material Supplier to select questionnaires for raw material supplier.Select Z05_Supplier Questionnaire Raw Material Subcontracting and choose Ok.On tab COMMUNICATION WITH APPRAISERSExternal Template Name: Z05_employee_procurement raw materialSave the entries. | The Group-Based Evaluation Template is created.No error or warning messages comes up. |  |
| 4 | Release group-based evaluation template | Choose the Release button to release the group-based evaluation template. | The previously created group-based evaluation template is released. |  |

### Start Group-Based Evaluation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you start a group-based evaluation.

|  |
| --- |
| Note The Group-Based Evaluation Template has been created for the procurement of raw materials in previous step as an example. If you have created the Template for the procurement of subcontracting or packaging materials instead, use these data. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Evaluation Templates - Evaluation (F2193) app in the Supplier Evaluation tile group. | The Manage Templates app is displayed. |  |
| 3 | Open Template | If no entries are displayed after opening the app, Click Go.Select your previously created and released group-based evaluation template and click on the name that is displayed as a link. | The group-based evaluation template is opened. |  |
| 4 | Start Group-Based Evaluation | Choose Start Group-Based Evaluation. | In a new window, the Group-Based Evaluation Request: New screen is opened. |  |
| 5 | Maintain the group-based evaluation request | Maintain the group-based evaluation request by entering at least an Evaluation Request Name Z05_employee_procurement raw material Response Deadline: Current Day plus 1 week> and a Period to Be Evaluated of one week (please Select Start Date and End Date for one week from today).Purchaser Responsible: PURCHASERChoose Submit Evaluation Request. | A Group-Based Evaluation Request is created and submitted. |  |

A group-based evaluation is started, and the request is sent to the entered appraiser(s).

### Maintain Evaluation Response as Appraiser

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you start a group-based evaluation.

|  |
| --- |
| Note The Group-Based Evaluation Template has been created for the procurement of raw materials in previous step as an example. If you have created the Template for the procurement of subcontracting or packaging materials instead, use these data. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as appraiser who was entered in the evaluation template/request (e.g.: Employee - Procurement.) | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Evaluate Suppliers (F1650) app in the Supplier Evaluation tile group. |  |  |
| 3 | Display Evaluation | Choose GO if there is no entry displayed. | The corresponding evaluation is displayed. |  |
| 4 | Start Supplier Evaluation as Appraiser | Select the corresponding evaluation response with status New which has the same name as your group-based evaluation request.In this case for instance select Z05_employee_procurement raw material. |  |  |
| 5 | Answer questions | Scroll down and see the questionnaire row, hit on the sameAnswer the questions. Depending on the type of questions, you may want to add attachments, select the suitable answer, or write the answer as text.Save your changes. | All data is saved.No error or warning messages comes up. |  |
| 6 | Submit the evaluation response | Choose Submit. | The group-based evaluation response is submitted and answered by the appraiser. |  |

### Display Scorecards

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Scorecards - Evaluation Questionnaires (F2191) app in the Supplier Evaluation tile group. | The Display Scorecards screen is displayed. |  |
| 3 | Open the evaluation response | Choose Go.Find the corresponding group-based evaluation response in the list and check the status. |  |  |
| 4 | Check Scorecards | Drill down into details of sections and questions. | The result of the responses is displayed. |  |

Result

The group-based evaluation reponse is answered and corresponding scorecards are available.

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
- related-to :: [[10-procurement/test-script-supplier-evaluation-and-performance-monitoring-sl4-ae-sap]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6A6_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 49,485 chars in the whole document
