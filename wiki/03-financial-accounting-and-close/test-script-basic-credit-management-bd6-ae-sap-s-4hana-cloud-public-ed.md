---
id: 03-financial-accounting-and-close/test-script-basic-credit-management-bd6-ae-sap-s-4hana-cloud-public-ed
title: "Test Script: Basic Credit Management (BD6_AE) - SAP S/4HANA Cloud Public Edition (BD6_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item BD6_AE Basic Credit Management: credit limits, blocked order release/reject, reporting and credit background jobs (S/4HANA Cloud 2608)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/credit-management]
aliases: [BD6_S4CLD2608_BPD_EN_AE]
keywords: [Credit Management and Credit Agency Integration, basic credit management, credit limit, blocked sales orders, documented credit decision, credit reporting, credit exposure, credit management jobs, credit data deletion, credit data rebuild]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD6_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1249
topic: 03-financial-accounting-and-close/credit-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Basic Credit Management (BD6_AE) - SAP S/4HANA Cloud Public Edition (BD6_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD6_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Credit Management and Credit Agency Integration** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Basic Credit Management (BD6_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860963)

[2 Prerequisites 4](#_Toc232860964)

[2.1 System Access 4](#_Toc232860965)

[2.2 Roles 4](#_Toc232860966)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860967)

[2.4 Business Conditions 6](#_Toc232860968)

[2.5 Additional Manual Configuration 7](#_Toc232860969)

[2.6 Preliminary Steps 7](#_Toc232860970)

[2.6.1 Assign Credit Analyst 7](#_Toc232860971)

[3 Overview Table 9](#_Toc232860972)

[4 Test Procedures 12](#_Toc232860973)

[4.1 Set a Credit Limit 12](#_Toc232860974)

[4.2 Sales Order Processing: Sale from Stock 13](#_Toc232860975)

[4.3 Sales of Non-stock Item with Order-Specific Procurement (optional) 14](#_Toc232860976)

[4.4 Make-to-Order Production – Finished Goods Sales and Final Assembly (Optional) 14](#_Toc232860977)

[4.5 Management of Blocked Orders 15](#_Toc232860978)

[4.5.1 Review and Release or Reject a Sales Order 15](#_Toc232860979)

[4.5.1.1 Review Sales Order 15](#_Toc232860980)

[4.5.1.2 Release Sales Order 17](#_Toc232860981)

[4.5.1.3 Reject Sales Order 18](#_Toc232860982)

[4.6 Reporting 19](#_Toc232860983)

[4.6.1 Display Credit Account Data 19](#_Toc232860984)

[4.6.2 Display Credit Exposure 20](#_Toc232860985)

[4.6.3 Analyze Credit Exposure 21](#_Toc232860986)

[4.6.4 Display Credit Log 22](#_Toc232860987)

[4.6.5 Credit Limit Utilization 23](#_Toc232860988)

[4.7 Schedule Background Jobs for Credit Check on SD Documents 24](#_Toc232860989)

[4.8 Schedule Background Jobs for Business Partner Update 26](#_Toc232860990)

[4.8.1 Assign Credit Management Role to Business Partner 26](#_Toc232860991)

[4.8.2 Update Rule for Scoring and Credit Check 28](#_Toc232860992)

[4.9 Schedule Background Jobs to Send Delta of Payment Behavior Summary 29](#_Toc232860993)

[4.9.1 Send Delta of Payment Behavior Summary 29](#_Toc232860994)

[4.10 Schedule Background Jobs to Delete Credit Management Data 31](#_Toc232860995)

[4.10.1 Delete Credit Exposure 31](#_Toc232860996)

[4.10.2 Delete Payment Behavior Summary 32](#_Toc232860997)

[4.11 Schedule Background Jobs to Rebuild Credit Management Data 33](#_Toc232860998)

[4.11.1 Rebuild Credit Exposure 33](#_Toc232860999)

[4.11.2 Recreate Payment Behavior Summary 35](#_Toc232861000)

[4.11.3 Schedule Background Jobs to Reorganize Credit Segment Assignment in Journal Entries 36](#_Toc232861001)

[5 Appendix 38](#_Toc232861002)

[5.1 Succeeding Processes 38](#_Toc232861003)

## Purpose

Overview

The credit worthiness and payment behavior of your business partners has an immediate effect on the business results of your company. Efficient receivables and credit management reduces the risk of financial losses and helps you to optimize business relationships with your business partners. Basic Credit Management supports your company in the early determination of the risk of losses on receivables from your business partners and supports you in making credit decisions. Basic Credit Management checks the exposure against the current credit limit for the business partner. In addition, you can also perform other checks, such as oldest open item, maximum dunning level, or last payment. If the new order is blocked, the blocked order can be released or rejected by authorized staff.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |  |
| --- | --- | --- |
|  | Type of Data | Details |
| System | System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100005 |  |  |
| Company Code | 3310 |  |  |
| Credit Segment | 1000 |  |  |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | To run through this scope item, the materials must be available in stock.You can create stock using the Manage Stock or Transfer Stock apps. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Execute the Create Sales Order (Optional) step. The Item Category of the sales order must have Credit Active set. |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | Execute the Create Sales Order step. The Item Category of the sales order must have Credit Active set.Note This business condition only applies when SAP S/4HANA Cloud Public Edition is active in your system. |

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| FIN_FSCM_REBUILD_DCD | Rebuild DCD functionality |

### Additional Manual Configuration

Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/940c2529832a930a3d0b385747366a2c)

### Preliminary Steps

#### Assign Credit Analyst

Purpose

In this activity, after the Credit Analyst has been imported, you assign the Credit Analyst to a business partner.

Prerequisite

Ensure that you have created an employee to use in the procedure below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). |  |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: 33100005For the row in the Worklist pane, choose Detail (>). |  |  |
| 4 | Credit Segment | Choose the Credit Segments tab.For the following credit segment, choose Details (>):Credit Segment: 1000 Credit Segment 1000(Maintained) | The Manage Credit Accounts - Credit Segment view displays. |  |
| 5 | Edit | Choose the Edit button. |  |  |
| 6 | Manage Relationship | In the Credit Analysts section, choose Assign Credit Analyst . | The Assign Credit Analyst view displays. |  |
| 7 | Add Relationship | Select the dropdown box.In the Select Credit Analyst) dialog box, enter the Last name and First name created in the prior procedure and choose Go.The dialog box displays the search results. Select the employee from the results and OK. | The credit analyst is assigned. |  |
| 8 | Create | Choose Apply. |  |  |
| 9 | Save | Save your entries. | Changes have been saved. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Set a Credit Limit](#unique_10) [page ] 12 | Credit Controller | Manage Credit Accounts (F4596) | Credit limit set |
| [Sales Order Processing: Sale from Stock](#unique_11) [page ] 13 |  | Procedure described in Sell from Stock (BD9) | Sales Order for the Business Partner is created. |
| [Sales of Non-stock Item with Order-Specific Procurement (optional)](#unique_12) [page ] 14 |  | Procedure described in Sales of Non-Stock Item with Order-Specific Procurement (BDN) | Sales Order for the Business Partner is created. |
| [Make-to-Order Production – Finished Goods Sales and Final Assembly (Optional)](#unique_13) [page ] 14 |  | Procedure described in Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE) | Sales Orders created. |
| Management of blocked orders |  |  |  |
| [Review and Release or Reject a Sales Order](#unique_14) [page ] 15 |  |  |  |
| [Review Sales Order](#unique_15) [page ] 15 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The blocked sales order is reviewed. |
| [Release Sales Order](#unique_16) [page ] 17 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The Sales order is released. |
| [Reject Sales Order](#unique_17) [page ] 18 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The Sales order is rejected. |
| Reporting |  |  |  |
| [Display Credit Account Data](#unique_18) [page ] 19 | Credit Controller | Display Credit Account Data (F4825) | Display generated credit data |
| [Display Credit Exposure](#unique_19) [page ] 20 | Credit Controller | Display Credit Exposure (F4826) | Display credit exposure |
| [Analyze Credit Exposure](#unique_20) [page ] 21 | Credit Controller | Analyze Credit Exposure - By Country (F2541) | Displays credit exposure information |
| [Display Credit Log](#unique_21) [page ] 22 | Credit Controller | Display Credit Management Log (F2162) | Display credit application log |
| [Credit Limit Utilization](#unique_22) [page ] 23 | Credit Controller | Credit Limit Utilization - Business Partner gt 80% Today (F1751) | Credit Limit Utilization data is displayed and filtered. |
| [Schedule Background Jobs for Credit Check on SD Documents](#unique_23) [page ] 24 | Credit Controller | Schedule Credit Management Jobs (F3748) | Credit Checks are scheduled. |
| Schedule Background Jobs for Business Partner Update |  |  |  |
| [Assign Credit Management Role to Business Partner](#unique_24) [page ] 26 | Credit Controller | Schedule Credit Management Jobs (F3748) | Mass assignment of the role to the business partner is scheduled. |
| [Update Rule for Scoring and Credit Check](#unique_25) [page ] 28 | Credit Controller | Schedule Credit Management Jobs (F3748) | You scheduled the update rule. |
| Schedule Background Jobs to Send Delta of Payment Behavior Summary |  |  |  |
| [Send Delta of Payment Behavior Summary](#unique_26) [page ] 29 | Credit Controller | Schedule Credit Management Jobs (F3748) | You scheduled the background job. |
| Schedule Background Jobs to Delete Credit Management Data |  |  |  |
| [Delete Credit Exposure](#unique_27) [page ] 31 | Credit Controller | Delete Credit Management Data (F4802) | You scheduled the deletion job. |
| [Delete Payment Behavior Summary](#unique_28) [page ] 32 | Credit Controller | Delete Credit Management Data (F4802) | You scheduled the deletion job. |
| Schedule Background Jobs to Rebuild Credit Management Data |  |  |  |
| [Rebuild Credit Exposure](#unique_29) [page ] 33 | Credit Controller | Rebuild Credit Management Data (F4234) | You scheduled the background job to rebuild credit exposure. |
| [Recreate Payment Behavior Summary](#unique_30) [page ] 35 | Credit Controller | Rebuild Credit Management Data (F4234) | You scheduled the background job to recreated payment behavior summary. |
| [Schedule Background Jobs to Reorganize Credit Segment Assignment in Journal Entries](#unique_31) [page ] 36 | Credit Controller | Rebuild Credit Management Data (F4234) | You scheduled the reorganization job. |

## Test Procedures

### Set a Credit Limit

Purpose

In this activity, you set a credit limit for the customer. The credit limit currency in all company codes is set to use the group currency, which is defined when the solution is activated.

|  |
| --- |
| Note The credit limit currency in all company codes is set to use the group currency that is defined when the solution is activated. |

|  |
| --- |
| Note If you use the Create Credit Segment configuration step, if you want to set the Credit Segment 1000 in the FLEXIBLE_CHECK field to a value of 3 on the Main Segment and Segment levels, you must also enter a credit limit for Credit Segment 0000. |

Prerequisite

Business partner master record 33100005 is already created with credit management profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). | The Manage Credit Accounts (F4596) view is displayed. |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: 33100005For the row in the Worklist, choose Details (>). |  |  |
| 4 | Maintain Credit Profile | Choose the Scoring tab.Choose Edit.Make the following entries:Calculation Rule: Standard rule without Automatic calculationRisk Class: Medium Default RiskCredit Check Rule: 01 Default - All Checks Active |  |  |
| 5 | Maintain Credit Segment | Choose the Credit Segments tab. Review or enter the following values in the Credit Segment field:Credit Segment: 1000 Credit Segment 1000 (Maintained)Credit Limit: 5.00Go to the Credit Segment line and make the following entry and choose Apply:Limit Valid To: <End of Year>Note If the Valid To field is not visible, you can go into View Settings and select it to display it.Note Repeat this step to set a credit limit on Credit Segment 0000 to avoid the sales order being blocked at headquarter credit check. | The amount and validity date are set for the credit limit. |  |
| 6 | Save | Save your entries. | Changes have been saved. |  |

### Sales Order Processing: Sale from Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This test script describes the entire process sequence for a standard sales process (sale from stock) with a customer.

To test credit management, execute the Create Sales Order procedure from the Sell from Stock (BD9) test script. Executing other procedures in that test script is optional.

Prerequisites

Sales order with customer 33100005 must be created.

Procedure

Complete all activities in the Sell from Stock (BD9) test script regarding the creation of a sales order using the master data from this test script.

### Sales of Non-stock Item with Order-Specific Procurement (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a customer orders a material that is currently not in stock. The material is then procured from an external supplier.

To test credit management, execute the Create Sales Order procedure from the Sales of Non-Stock Item with Order-Specific Procurement (BDN) test script. Completing any additional procedures from that test script is optional.

Prerequisites

Sales order with customer 33100005 must be created. The Item Category of the sales order must have Credit Active set.

Procedure

Complete all activities in the Sales of Non-Stock Item with Order-Specific Procurement (BDN) test script regarding the creation of a sales order using the master data from this test script.

### Make-to-Order Production – Finished Goods Sales and Final Assembly (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes the entire process for a standard sales process Make-to-Order (MTO) with a customer.

To test credit management, execute the Quotation Processing MTO and Create Sales Order with Ref. to Follow-On Quotation procedures from the Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE) test script. Executing any additional procedures from that test script is optional.

Prerequisites

Sales order with customer 33100005 must be created. The Item Category of the sales order must have Credit Active set.

Procedure

Complete all activities in the Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE) test script regarding the creation of a sales order using the master data from this test script.

### Management of Blocked Orders

#### Review and Release or Reject a Sales Order

Context

The sales order failed the credit check. In the following procedures, you review blocked sales orders and resolve any credit issues.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

Credit case has been assign to a Credit Analyst or Person Responsible.

##### Review Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you review blocked sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to a credit check block.

The Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view is displayed. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: <your business partner>Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. | The Document with Credit Block view is displayed. |  |
| 5 | Enable Editing | Choose Edit. | Updates data. |  |
| 6 | Update | Update the DCD fields.Credit Analyst: <Your user with HR Master Record created> | The DCD data is changed. |  |
| 7 | Save | Save your entries. | The changes are saved. |  |
| 8 | Set In Process | Choose Set To In Process | Status changed to In Process. |  |

##### Release Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you release the sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

The Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: <your business partner>Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. |  |  |
| 5 | Release | Choose Release. On the Release dialog box, enter an approval note and choose Release. | The log is displayed and under the Classification and Changes facet, the Last Action is Release. |  |

##### Reject Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you reject the sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

The documented credit decision is assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: 33100005Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select Case | Select the row of the documented credit decision you generated in the previous step.Choose Details (>). | The Document with Credit Block view displays. |  |
| 5 | Reject | Choose Reject. | The Reject dialog box displays. |  |
| 6 | Select Rejection Reason | Make the following entry and choose Reject:Rejection Reason: for example, Rejected by ApproverRejection Note: <any note> | The sales order/service order/service contract is rejected and the DCD Status changes to Closed and the Notes are updated with the note of type Rejection Reason. |  |

### Reporting

#### Display Credit Account Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you generate credit data by business partner.

Prerequisite

A business partner is created and credit management profile is maintained.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Display Credit Account Data (F4825). |  |  |
| 3 | Execute Search | Make the following entries and choose Go:Business Partner: 33100005 |  |  |
| 4 | Display Master Record | For the business partner, choose Details (>). |  |  |
| 5 | Select Credit Segment | Select the credit segment to review the credit data. |  |  |
| 6 | Display Credit Data | The information available includes:Block ReasonExposureCredit LimitUtilization % |  |  |

#### Display Credit Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you generate the credit exposure by business partner.

Prerequisite

A business partner is created and credit management profile is maintained.

Sales orders are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Display Credit Exposure (F4826). |  |  |
| 3 | Execute Search | Make the following entries and choose Go:Business Partner: 33100005 | A list of credit exposure by business partner displays. |  |
| 4 | Display Credit Exposure | For the business partner row, choose Details (>). |  |  |
| 4 | Review Credit Exposure Items | Review the credit exposure items. To see more details, choose Details (>) at the right of the row. |  |  |

#### Analyze Credit Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze credit exposure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Analyze Credit Exposure - By Country (F2541). |  |  |
| 3 | Navigation | Use the dropdown menu to review and analyze credit exposure:By CountryBy Risk ClassBy Business PartnerBy Credit Segment.For example, drill down By Risk Class Partner (Table) and by the top business partners with the highest credit exposure display. | Different views display according to your criteria. |  |

#### Display Credit Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the credit application logs.

Prerequisite

A business partner is created and credit management profile is maintained.

Sales orders are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Display Credit Management Log (F2162). | Application Logs view displays. |  |
| 3 | Search Criteria | Enter the following:Severity: <select all available options>*Date From To: <enter date range> |  |  |
| 4 | Execute Search | Choose Go. | A list of Application Logs are displayed. |  |
| 5 | Select Log | Choose any log to display details. | Log details are displayed with results of credit checks. |  |

#### Credit Limit Utilization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the Key Performance Indicator (KPI) Credit Limit Utilization, that is, the utilization of the credit limit for a business partner.

Prerequisite

Sales orders have been created, credit check has been executed and cases have been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Credit Limit Utilization - Business Partner gt 80% Today (F1751). | The Credit Limit Utilization (S/4HANA) (F1751) view displays. |  |
| 3 | Navigation | To change the view, choose the dropdown list By Business Partner (Top 10 Credit Limit Exceeded) or By Business Partner (Top 10 Credit Exposure) and then use the different icon buttons to filter or change visualized results.For example, you can change the chart type in which the data displays or change from chart to table. | Different views display, based on your actions. |  |

### Schedule Background Jobs for Credit Check on SD Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule background jobs for new credit checks for sales and distribution (SD) documents.

In the following procedure mentioned, the job is executed as a single run. You may choose to schedule the job on a regular basis, typically once a day, in order to facilitate a credit recheck of open sales orders/service orders/service contracts (credit-blocked or non credit-blocked).

For the credit-blocked sales orders/service orders/service contracts, the intention is to verify if the credit situation of the customer has improved since the initial credit check, which led to the credit block. For example, because the customer made a payment since the initial credit check. The sales order/service order/service contract would pass the credit check successfully and no manual interaction is required.

For the non credit-blocked sales orders/service orders/service contracts, the intention is to verify if the credit situation has worsened since the initial credit check, which was passed successfully. For example, because the customer has overdue invoices now outstanding. Typically, you review sales orders/service orders/service contracts that are approaching their delivery date for this purpose.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Credit Management Jobs (F3748). | The Schedule Credit Management Jobs view displays. |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Add General Information | In Template Selection section, make the following entries and choose Step 2:Job Template: Check Credit on SD DocumentsJob Name: Check Credit on SD Documents |  |  |
| 5 | Scheduling Options | In Scheduling Options, make the following entries and choose Step 3.Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Parameter Section | In the Parameter Section, enter:Credit Segment: 1000Credit Account: leave blankRisk Class: leave blankSD document: leave blankOverall document status: use default valueOverall credit status: use default valueNext shipping date: leave blankDate of next credit check: leave blankNote Make sure the Date of next credit check is empty. Clear any values.Sales documents: selectedDeliveries: selected |  |  |
| 8 | Schedule | Choose Schedule.Note If you want to monitor the results, refresh the status on the Application Jobs view. Choose the button in the Results column to view the job results. | The job is scheduled. |  |

### Schedule Background Jobs for Business Partner Update

Purpose

In this activity, you schedule background jobs for business partner update.

#### Assign Credit Management Role to Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you schedule the assignment of the credit management role to the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Credit Management Jobs (F3748). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Create Job | Make the following entries and choose Step 2:Template Selection section:Job Template: Assign Credit Management Role to Business PartnersJob Name: Assign Credit Management Role to Business PartnersMake the following entries and choose Step 3:Scheduling Options section:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK.Make the following entries and choose Schedule:Parameters section:Business Partner: enter the Business Partner needed for the changeNote To make the change on multiple Business Partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Create Credit Profile: DeselectedNote If you need to create a credit profile, ensure that you assigned the default rules in the Define Checking Rules and Create Rule for Scoring and Credit Limit Calculationconfiguration steps.Test Run: DeselectedUpdate Run: SelectedNote If you want to monitor the results, refresh the status on the Application Jobs view. Choose the button in the Results column to view the job results. | The job is scheduled. |  |

#### Update Rule for Scoring and Credit Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you schedule the update rule for scoring and credit check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Credit Management Jobs (F3748). |  |  |
| 3 | Create Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Create Job | Make the following entries and choose Step 2:Template Selection section:Job Template: Update Rules for Scoring and Credit CheckJob Name: Update Rules for Scoring and Credit Check |  |  |
| 5 | Recurrence | Make the following entries and choose Step 3:Scheduling Options section:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Schedule | Make the following entries and choose Schedule:Parameters section:Rule: enter the Rules needed for the changeBusiness Partner: enter the Business Partner needed for the changeNote To make the change on multiple Business Partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Change Rule to: Enter the rule needed to setChange Check Rule to: Enter the check rule needed to setTest Run: DeselectedUpdate Run: Selected | The job is scheduled.Note To monitor the results, refresh the status on the Application Jobs view. Choose the button in the Results column to view the job results. |  |

### Schedule Background Jobs to Send Delta of Payment Behavior Summary

In this activity, you schedule background jobs to send delta of payment behavior summary.

#### Send Delta of Payment Behavior Summary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule background jobs to send delta of payment behavior summary.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Credit Management Jobs (F3748). | The Schedule Credit Management Jobs view displays. |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Add General Information | In Template Selection section, make the following entries and choose Step 2:Job Template: Send Delta of Payment Behavior SummaryJob Name: Send Delta of Payment Behavior Summary |  |  |
| 5 | Scheduling Options | In Scheduling Options, make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Parameter Section | In the Parameterssection, make the following entries:Company Code: <enter the Company Code needed for the change>Customer: <enter the Customer needed for the change>Note To make the change on multiple Customers, choose the Drop Down button and in the Select: Customer (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Test Run: Deselected |  |  |
| 8 | Schedule | Choose Schedule.Note If you want to monitor the results, refresh the status on the Application Jobs view. Choose the button in the Results column to view the job results. | The job is scheduled. |  |

### Schedule Background Jobs to Delete Credit Management Data

#### Delete Credit Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule background jobs to delete credit exposure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Delete Credit Management Data (F4802). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Add General Information | In the Template Selection section, make the following entries and choose Step 2:Job Template: Delete Credit ExposureJob Name: Delete Credit Exposure |  |  |
| 5 | Scheduling Options | In the Scheduling Options section, make the following entries and choose Step 3:Start Immediately: SelectedTo schedule a recurrence pattern, choose the Define Recurrence Pattern button. In the Scheduling Information dialog box, enter Recurrence Pattern: Single Run and choose OK. |  |  |
| 6 | Parameter Section | In the Parameters section, make the following entries and choose Schedule:Business Partner: <enter the Business Partner needed for the deletion>To make the change on multiple Business Partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Credit Segment: <enter the Credit Segment needed for the deletion>Credit Exposure Category: <enter the Credit Exposure Category needed for the deletion>Settings: select the additional Settings according to your requirement | The job is scheduled. |  |

#### Delete Payment Behavior Summary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule background jobs to delete the payment behavior summary.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Delete Credit Management Data (F4802). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Add General Information | In the Template Selection section, make the following entries and choose Step 2:Job Template: Delete Payment Behavior SummaryJob Name: Delete Payment Behavior Summary |  |  |
| 5 | Scheduling Options | In the Scheduling Options section, make the following entries and choose Step 3:Start Immediately: SelectedTo schedule a recurrence pattern, choose the Define Recurrence Pattern button. In the Scheduling Information dialog box, enter Recurrence Pattern: Single Run and choose OK. |  |  |
| 6 | Parameter Section | In the Parameters section, make the following entries and choose Schedule:Business Partner: <enter the Business Partner needed for the deletion>To make the change on multiple Business Partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Credit Segment: <enter the Credit Segment needed for the deletion>Test Run: leave blankDisplay Details: Selected | The job is scheduled. |  |

### Schedule Background Jobs to Rebuild Credit Management Data

In this activity, you schedule background jobs to rebuild credit management data.

|  |
| --- |
| Caution Deletion and rebuilding of credit management data is not part of the regular or daily business. This should be taken into consideration if the respective data are wrong. We strongly recommend that you check SAP Notes before you delete and rebuild credit management data. |

#### Rebuild Credit Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule background jobs to rebuild credit exposure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Rebuild Credit Management Data (F4234). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Add General Information | In the Template Selection section, make the following entries and choose Step 2:Job Template: Rebuild Credit ExposureJob Name: Rebuild Credit Exposure |  |  |
| 5 | Scheduling Options | In Scheduling Options, make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Parameter Section | In the Parameters Section, make the following entries:Credit Segment: <enter the Credit Segment needed for the change>Business Partner: <enter the Business Partner needed for the change>Note To change multiple business partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.) dialog box, enter your parameters and choose OK.Test Run: leave blank |  |  |
| 7 | Schedule | Choose Schedule. | The job is scheduled. |  |

#### Recreate Payment Behavior Summary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule background jobs to recreate payment behavior summary.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Rebuild Credit Management Data (F4234). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Add General Information | In the Template Selection section, Make the following entries and choose Step 2: :Job Template: Recreate Payment Behavior SummaryJob Name: Recreate Payment Behavior Summary |  |  |
| 5 | Scheduling Options | In Scheduling Options, Make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Parameter Section | In the Parameters Section, make the following entries:Company Code: <enter the Company Code needed for the change>Customer: <enter the Customer needed for the change>Note To change multiple customers, choose the Drop Down button and in the Select: Customer (List displays max. 500 hits. If available, use the filter to see all values.) dialog box, enter your parameters and choose OK.Credit Segment: enter the Credit Segment needed for the changeCustomers w/o OIs: selectTest Run: <leave blank> |  |  |
| 8 | Schedule | Choose Schedule. | The job is scheduled. |  |

#### Schedule Background Jobs to Reorganize Credit Segment Assignment in Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule background jobs for reorganization of credit segment Assignments in Journal Entries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Rebuild Credit Management Data (F4234). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Add General Information | In Template Selection, make the following entries and choose Step 2:Job Template: Reorganize Credit Segment Assignment in Journal EntriesJob Name: Reorganize Credit Segment Assignment in Journal Entries |  |  |
| 5 | Scheduling Options | In Scheduling Options, make the following entries and choose Step 3Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Parameter Section | In the Parameter Section, enter:Company Code: <enter the company code to reorganize>Customer: <enter the customer to reorganize>Intended Credit Segment: <enter new credit segment for after reorganization>Output Detail: SelectedTest Run: DeselectedChoose Schedule.If you want to monitor the results, refresh the status on the Application Jobs view. Choose the button in the Results column to view the job results. | The job is scheduled. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following test scripts:

| Process | Business Condition |
| --- | --- |
| Sell from Stock (BD9) (optional) | Entire process sequence for a standard sales process (sale from stock) with a customer.Using the master data from this document, complete the following activities described in the test script:Process Sales Order |
| Sales of Non-Stock Item with Order-Specific Procurement (BDN) (optional) | Customer orders a material that is currently not in stock. The material is procured from an external supplier.Using the master data from this document, complete all of the following activities described in the test script. |
| Sales Order Fulfillment Monitoring and Operations (BKK) (optional) | Collection of periodic activities such as day ending activities or legal requirements, for example Intrastat and Extrastat reporting.Using the master data from this document, complete the following activities described in the test script:Review Blocked Sales Orders section. |

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
- related-to :: [[03-financial-accounting-and-close/advanced-credit-management-1qm-ae-test-script-sap-s-4hana-cloud-public]]
- related-to :: [[03-financial-accounting-and-close/test-script-credit-agency-integration-1ry-759]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD6_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 58,090 chars in the whole document
