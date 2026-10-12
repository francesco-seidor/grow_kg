---
id: 08-sales-order-management/sales-order-automation-73p-ae-test-script-1203
title: Sales Order Automation (73P_AE) Test Script (73P_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 73P: AI recommendations for sales order completion and customer returns, incl. Turnkey model training."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-order-automation]
aliases: [73P_S4CLD2608_BPD_EN_AE]
keywords: [Sales Order Automation and Creation from Unstructured Data, sales order automation, sales order recommendations, returns order recommendations, turnkey model training, intelligent scenario management, prerequisite checks, incomplete sales orders, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/73P_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1203
topic: 08-sales-order-management/sales-order-automation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales Order Automation (73P_AE) Test Script (73P_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/73P_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Order Automation and Creation from Unstructured Data** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sales Order Automation (73P_AE)Purpose PUBLIC 1Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sales Order Automation (73P_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860416)

[2 Prerequisites 4](#_Toc232860417)

[2.1 System Access 4](#_Toc232860418)

[2.2 Roles 4](#_Toc232860419)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232860420)

[2.4 Business Conditions 5](#_Toc232860421)

[2.5 Preliminary Steps 6](#_Toc232860422)

[2.5.1 Train Model via Turnkey 6](#_Toc232860423)

[2.5.1.1 Check Default Turnkey Schedule 6](#_Toc232860424)

[2.5.1.2 Turn Off Turnkey Manually (Optional) 7](#_Toc232860425)

[2.5.1.3 Turn On Turnkey Manually (Optional) 8](#_Toc232860426)

[2.5.2 Execute Prerequisite Checks Manually (Optional) 9](#_Toc232860427)

[2.5.3 Train and Activate Model Manually (Optional) 10](#_Toc232860428)

[3 Overview Table 12](#_Toc232860429)

[4 Test Procedures 13](#_Toc232860430)

[4.1 Create or Edit Sales Order with Recommendations for Standard Orders 13](#_Toc232860431)

[4.1.1 Option 1: Create Sales Order with Recommendations 13](#_Toc232860432)

[4.1.2 Option 2: Edit Sales Orders with Recommendations 15](#_Toc232860433)

[4.1.2.1 Create an Incomplete Sales Order 15](#_Toc232860434)

[4.1.2.2 Update the Incomplete Sales Order 16](#_Toc232860435)

[4.2 Create Returns Order with Recommendations 17](#_Toc232860436)

[4.2.1 Create Returns Order with Recommendations 17](#_Toc232860437)

[5 Appendix 20](#_Toc232860438)

[5.1 Process Integration 20](#_Toc232860439)

[5.1.1 Succeeding Processes 20](#_Toc232860440)

## Purpose

Overview

This machine learning solution provides recommendations for incomplete fields in sales documents.

With SAP Business AI in customer returns management, a returns clerk is supported for efficiently creating customer returns. For the most common input fields, recommendations are proposed by AI based on historical data of past return documents with the same process variants.​

The solution helps to speed up the creation of customer return objects and reduce errors by using historical data.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Analytics Specialist | SAP_BR_ANALYTICS_SPECIALIST | Analytics / Analytics | SAP_CA_SPT_ANALYTICS_PC / SAP_CORE_SPT_ANALYTICS_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |  |
| Sold-to party | 33100003 | Domestic UAE Customer 3 |  |
| Ship-to party | 33100003 | Domestic UAE Customer 3 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information about creating master data, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Script documentation.

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | As a prerequisite for running through this test script, materials must be available in stock. If you use trading goods (HAWA), you can either:Run through the process Procurement of Direct Materials (J45)Create stock using the Post Goods Movement app (for details, see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the steps described in the Create New Open MM Posting Period - MDS (BNZ) master data script. The posting period is up to date. |

### Preliminary Steps

#### Train Model via Turnkey

##### Check Default Turnkey Schedule

Purpose

You check the default schedule for Turnkey.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Analytics Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Intelligent Scenario Management (F4470). | The Intelligent Scenario Management screen displays. |  |
| 3 | Search for Intelligent Scenario | For Sales Order recommendation, search for the intelligent scenario SLS_DOC_AUTO_COMPLTN. The Turnkey is ON by default.For Returns Order Creation recommendation, search for the intelligent scenario SLS_CUSTRET_RECMDN.The Turnkey is ON by default.Note If the Turnkey is OFF, you can manually change it to ON according to the instructions on the next chapter. | The intelligent scenario displays. |  |
| 4 | Check Model Status | Select the intelligent scenario line and navigate to the Models tab.Click on the model and the detailed information of the model appears.In the Trainings tab, all trainings are completed. In the Deployments tab, only 1 deployment is active for all.Choose Back. |  |  |
| 5 | Check Turnkey Schedules and Turnkey Runs | Navigate to Turnkey tab.Turnkey automation information shows on top of page where Turnkey Schedules are listed. Enter one of the schedules, the schedule settings and Turnkey Runs are shown.In the Turnkey Runs section, the runs for schedule are listed.Navigate to the first Turnkey Run, Run details are shown as follows:StatusGeneral InformationOperation OverviewTurnkey Operations (Activation, Training, Prerequisite Checks and check messages)Choose Back. | The check is done and you can process the test procedures. |  |
| 6 | Check Prerequisite Check Run Report | Navigate to Prerequisite Check Runs tab. Prerequisite check status is listed. Enter the first line of the status and you can check the details, including:DAR connectivityData SizeScope Activation | For Data Size check result:For intelligent scenario SLS_DOC_AUTO_COMPLTN:For less than 100 elements, the run is aborted.For less than 1000 elements, there is a warning.For intelligent scenario SLS_CUSTRET_RECMDN:For less than 1000 elements, the run is aborted.For less than 3000 elements, there is a warning. |  |

##### Turn Off Turnkey Manually (Optional)

Purpose

You can turn off the Turnkey manually if you don’t need it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Analytics Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Intelligent Scenario Management (F4470). | The Intelligent Scenario Management screen displays. |  |
| 3 | Search for Intelligent Scenario and Turn Off the Turnkey | For Sales Order recommendation, search for the intelligent scenario SLS_DOC_AUTO_COMPLTN.For Returns Order Creation recommendation, search for the intelligent scenario SLS_CUSTRET_RECMDN.Choose switch off the Turnkey. | The intelligent scenario displays. |  |
| 4 | Check the Turnkey Details | Select the intelligent scenario and click on the line. No Turnkey automation information is shown in the object page. All the turnkey schedules are turned off. | The Turnkey is switched off. |  |

##### Turn On Turnkey Manually (Optional)

Purpose

You can turn on the Turnkey manually if the Turnkey is off.

|  |
| --- |
| Note You only execute this step if the Turnkey is off. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Analytics Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Intelligent Scenario Management (F4470). | The Intelligent Scenario Management screen displays. |  |
| 3 | Search for Intelligent Scenario and Turn On the Turnkey | For Sales Order recommendation, search for the intelligent scenario SLS_DOC_AUTO_COMPLTN.For Returns Order Creation recommendation, search for the intelligent scenario SLS_CUSTRET_RECMDN.Switch on the Turnkey.In the pop-up window Schedule Turnkey, you can change the Recurrence Pattern by choosing the Edit Turneky Schedule.After all inputs are confirmed, choose Create Turnkey Schedule. | The Turnkey is turned on manually. |  |
| 4 | Check the Turnkey Details | Select the intelligent scenario and click on the line.Navigate to Turnkey tab, the manual schedule is listed in the Turnkey Schedules tab and only one is switched on.Switch to the Tunkey Runs section, check if the current run is listed with status Runinng. |  |  |
| 5 | Check the Turnkey Run Details | Click on the line of the Run, and the details of the Turnkey Run display.You can check the information below:StatusGeneral InformationSchedule IDTurnkey Operations and their messages |  |  |

#### Execute Prerequisite Checks Manually (Optional)

|  |
| --- |
| Note The step is only relevant if you want to execute prerequisite checks manually. |

Purpose

You execute prerequisite checks in this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Analytics Specialist | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Intelligent Scenario Management (F4470). | The Intelligent Scenario Management screen displays. |  |
| 3 | Search for intelligent Scenario | For Sales Order recommendation, search for the intelligent scenario SLS_DOC_AUTO_COMPLTN .For Returns Order Creation recommendation, search for the intelligent scenario SLS_CUSTRET_RECMDN. | The intelligent scenario displays. |  |
| 4 | Execute prerequisite checks | Select the intelligent scenario and choose Prerequisite Checks button. | The Prerequisite Check Run for intelligent scenario displays. |  |
| 5 | Check prerequisite check runs result | Choose Step 2, Mandatory check DAR connectivity displays.Choose step 3, and choose Review.Then choose Start Prerequisite Check Run.You can check the prerequisite check runs result, you can click Check Messages for detail log. | The prerequisite check runs results display.If the check fails, please check if the following step has been done:Make sure that there are more than 100 complete sales orders in the system for intelligent scenario SLS_DOC_AUTO_COMPLTN.Make sure that there are more than 1000 released complete returns order items (sales order type is CBAR) in the system for intelligent scenario SLS_CUSTRET_RECMDN.Please create ticket to SAP with component SD-ANA for further support. |  |

#### Train and Activate Model Manually (Optional)

|  |
| --- |
| Note The step is only relevant if you have manually turned off the Turnkey and want to train/activate the model manually. |

Purpose

You can enable train and activate model SLS_DOC_AUTO_COMPLTN manually.

|  |
| --- |
| Note Train the model with a sufficient amount of data. We recommend that your dataset contains at least 1000 data records (that is, sales document items) for sales order training, and at least 3000 data records (items for returns order type CBAR).By default, training data contains sales documents (except for those related to archived customers) whose overall status is completed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Analytics Specialist | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Intelligent Scenario Management (F4470). | The Intelligent Scenario Management screen displays. |  |
| 3 | Search for intelligent Scenario | For Sales Order recommendation, search for the intelligent scenario SLS_DOC_AUTO_COMPLTN.For Returns Order Creation recommendation, search for the intelligent scenario SLS_CUSTRET_RECMDN. | The intelligent scenario displays. |  |
| 4 | Choose the intelligent scenario | Choose the line of the intelligent scenario. | The intelligent scenario screen displays. |  |
| 5 | Train the intelligent scenario | Choose the line of the intelligent scenario and choose Train.In the pop-up screen input following entry:Intellignet Scnario Version:Version: 3.0Package Size:For SLS_DOC_AUTO_COMPLTN: 1000For SLS_CUSTRET_RECMDN: 5000Note You can add train filter in this step. For example,Training Filters: Choose Add FilterSOLDTOPARTY (Sold-to Party) Between 10100001 and 10109999Then choose Train. | A new version is training. Status is TrainingNote The training time depends on the data volume. It might take at least several minutes. When the traning is done, the status will be changed to Completed. If the training has failed, the status will be changed to Failed and you can click the button Retrain to retrain this model. |  |
| 6 | Deploy the Train Model | Choose the line of training ID, and choose Deploy.In the pop-up window, choose Deploy. | A new deployment will be created. The status is Deployment pending.Note The deploying time depends on the data volume. It might take at least severial minutes. When the deploying is done, the status will be changed to Deployed. If the training is failed, you can click button Redeploy to deploy this model. |  |
| 7 | Activate the Model | Choose section Deployments.Choose the deployed model and choose Activate -> For AllIn the pop-up screen, choose Activate for All. | The deployment will be activated for all users.If click Activate for me, only the current user will can use this model. |  |
| 8 | Deactivate or Redeploy the Model (Optional) | You can choose Deactivate or Redeploy a trained model if needed.You can choose Undeploy a deactivated model. | You can disable an activated trained model or generate a new deployment. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/ Transaction | Expected Results |
| --- | --- | --- | --- |
| Create or Edit Sales Order with Recommendations for Standard Orders |  |  |  |
| [Option 1: Create Sales Order with Recommendations](#unique_13) [page ] 13 | Internal Sales Representative | Create Sales Orders (F3893) | Sales orders are created. |
| Option 2: Edit Sales Orders with Recommendations |  |  |  |
| [Create an Incomplete Sales Order](#unique_14) [page ] 15 | Internal Sales Representative | Create Sales Orders (F3893) | Incomplete sales orders is created. |
| [Update the Incomplete Sales Order](#unique_15) [page ] 16 | Internal Sales Representative | Monitor Recommendations for Sales Document Completion (F7515) | Sales orders are updated |
| Create Returns Order with Recommendations |  |  |  |
| [Create Returns Order with Recommendations](#unique_16) [page ] 17 | Internal Sales Representative | Manage Customer Returns - Version 2 (F4832) |  |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as: apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

1. Log on to the SAP Fiori launchpad as a respective user, for example, Internal Sales Representative.
2. Access the Enterprise Search Bar by choosing the magnifying glass icon in the upper right corner.
3. The Enterprise Search bar displays two filter fields next to the search icon: all dropdown menu and a search field. Enter your Search Criteria and choose the business object type, for example, select Sales orders from the dropdown menu, and enter a sales order number in the search field and choose Search, the sales order lists.
4. Choose the sales order number link. The system navigates to the fact sheet screen and sales order related information is integrated and summarized in one Fiori page. You can get detailed data by choosing the corresponding links.

There are fact sheets available for the following objects (visible depending on the assigned role):

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Create or Edit Sales Order with Recommendations for Standard Orders

#### Option 1: Create Sales Order with Recommendations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order with recommended values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Order screen displays |  |
| 3 | Navigate to Create Order Screen | On the Manage Sales Order screen, and choose Create. |  |  |
| 4 | Enter Data | On the Create screen, make the following entries and choose Continue:Sales Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the New: Sales Order screen, make the following entries:General Information:Sold-to Party: 33100003Ship-to Party: 33100003Customer References: <PO number>Items:Product: TG11Requested Quantity: 5Choose EnterBack to tab General Information, remove the entry of Terms of payment. |  |  |
| 6 | Create Sales Order | Choose Infompleteness Info in the menu. Close the pop-up window.Click on the highlighted field, the recommendations will appear, choose the first line of the recommdations and fill in the value. For example:Terms of Payment: 0004Sales Office: 330Sales Group: 330Then choose Create. | Incomplete fields are filled with recommended values, sales orders are created. |  |

#### Option 2: Edit Sales Orders with Recommendations

##### Create an Incomplete Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a incomplete sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Order screen displays. |  |
| 3 | Navigate to Create Order Screen | On the Manage Sales Order screen, and choose Create. |  |  |
| 4 | Enter Data | On the Create screen, make the following entries and choose Continue:Sales Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the New: Sales Order screen, make the following entries:General Information:Sold-to Party: 33100003Ship-to Party: 33100003Customer References: <PO number>Items:Product: TG11Requested Quantity: 3Choose Enter.Back to General Information tab, remove the entry of Terms of payment.Back to Items tab and click on the line item you just created. On the pop-up screen, remove the value of Plant and choose Apply.Choose Create, ignore messages, and choose SaveNote the sales order number and ignore the warning. | The incomplete sales order created. |  |

##### Update the Incomplete Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to edit an incomplete sales order using recommended values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Recommendations for Sales Document Completion (F7515). | The Monitor Recommendations for Sales Document Completion screen displays. |  |
| 3 | Input sales order number | Input the sales order number you created in last step and choose Go.Choose Incomplete to show the incomplete orders.Check With Recommendations to check the recommedation value for incomplete fields. | The sales order appears. |  |
| 4 | Complete Sales Document | Choose the Complete Document Data in the new screen.Choose Edit. Choose Imcpleteness InfoClick on the highlighted field. The recommendations will appear. Choose the first line of the recommdations and fill in the value. For example:Terms of Payment: 0004Sales Office: 330Sales Group: 330Navigate to Items tab, click on the item. On the new screen, click on the highlighted field. The recommendations will appear. Choose the first line of the recommdations and fill in the value. For example:Plant: 3310Choose Apply.Choose Create. | The sales order is updated. |  |

### Create Returns Order with Recommendations

#### Create Returns Order with Recommendations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order with recommended values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Navigate to Create Order Screen | On the Manage Customer Returns – Version 2 screen, and choose Create.Note If you have the reference document, you can choose Create with Reference and in the pop-up window, input the reference document. |  |  |
| 4 | Enter Data | On the Create screen, make the following entries and choose Continue:Sales Order Type: CBARSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details for General Information | On the New Returns Order screen, make the following entries:General Information:Sold-to Party: 33100003Ship-to Party: 33100003Customer References: <PO number>Note While creating a returns order, for the target fields, the top 3 recommended value will show in the drop down list. Furthermore, if a value probability is over 70%, it will be show in the field with blue highlight. You still need to apply to confirm the recommended values.Returns Order Reason for header level has been generated automatically and highlighted in blue based on your business data, or you can choose the dropdown list to see recommendations.Choose the dropdown list for returns order reason and according to the recommendation values, select the one you want.Returns Order Reason: 009 Standard Return |  |  |
| 6 | Enter Order Details for Items | Choose tab Items.Choose Create.Product: TG11Return Quantity: 3One or more field may generate value automatically and highlighted in blue based on your business data, Choose the field, you can see more recommendations.Returns Order Reason: 003 Product damagedFollow-up Activity: 0001 Receive into PlantRefund Control: PNote Some more fields may also have recommendations, you can check the details via [Input Recommendations for Returns Order Creation](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/2f19fc5f5c9d4cd8ae01ac4313019766.html).You can check and input other mandatory fields if needed, for example:Refund Control: P Create Credit Memo RequestIf a pop-up window for Unaccepted Recommendations shows up, choose Accept and Apply.Choose Save and Release for item level.If a pop-up window for Unaccepted Recommendations shows up, choose Accept and Create for header level.Note You can also choose Reject and Apply / Continue Editing for item level to input the proper value as you want.Choose Reject and Create / Continue Editing for header level to input the proper value as you want. | The returns order has been created. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Description |
| --- | --- |
| Sell from Stock(BD9) | Process a sales order, delivery, billing and so on.Using the master data from this document, complete all the activities described in the test script of the scope item. |
| Sales Order Fulfillment Monitoring and Operations (Optional) | This scope item describes the collection of periodic activities, such as day ending activities or legal requirements.● Using the master data from this document, complete all the activities described in the Test Script of the scope item: Sales Order Fulfillment Monitoring and Operations (Chapters Review Sales Documents blocked for billing , Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents). |

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
- related-to :: [[08-sales-order-management/test-script-create-sales-orders-from-unstructured-data-4x9-ae-sap-s-4h]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/73P_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 31,787 chars in the whole document
